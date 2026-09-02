/* Render every page in jsdom, click every annotation, report anything broken.
 *
 *   npm install jsdom && node tools/smoke.js
 *
 * jsdom is not a project dependency — the site itself has none. Install it
 * wherever is convenient and point NODE_PATH at it if it is not local.
 *
 * Passes with no chapters present, which is the state of the branch that
 * carries only the site and the tooling.
 */

const { JSDOM } = require("jsdom");
const fs = require("fs");
const path = require("path");

const ROOT = path.dirname(__dirname);
const LESSONS = path.join(ROOT, "lessons");
let failed = false;

function report(name, problems, stats) {
  console.log(name);
  if (stats) console.log("   " + stats);
  if (problems.length) {
    failed = true;
    problems.forEach(function (p) { console.log("   FAIL " + p); });
  }
}

function read(...parts) {
  return fs.readFileSync(path.join(ROOT, ...parts), "utf8");
}

/* --- boundary lints -------------------------------------------------- */

/* The section system only works if the two layers stay separate: a section
 * kind may set custom properties, but must not size a block type directly. */
function lintSectionLayering() {
  const css = read("assets", "style.css").replace(/\/\*[\s\S]*?\*\//g, "");
  const BLOCKS = ["ko-para", "ko-list", "ko-bullet", "glossbox", "gloss-row",
                  "table-wrap", "chart", "bar-row", "verse", "labels", "figure",
                  "source", "margin-note", "anno-card", "notes", "trans",
                  "sub-title", "sect-topic", "blank", "en-para", "para-pair",
                  "en-title", "en-fold", "en-wrap", "figure-slot"];
  const problems = [];

  for (const m of css.matchAll(/([^{}]+)\{([^{}]*)\}/g)) {
    const selector = m[1].trim();
    if (!/\.sect-(?!title|topic|head)[a-z]+/.test(selector)) continue;
    const block = BLOCKS.find(function (b) {
      return new RegExp("\\." + b + "\\b").test(selector);
    });
    if (!block) continue;
    if (/(^|;)\s*(font-size|line-height|margin|padding)\s*:/.test(m[2])) {
      problems.push("`" + selector + "` sizes ." + block +
                    " directly — set a token on the section instead");
    }
  }
  report("style.css section layering", problems,
    "checked against " + BLOCKS.length + " block types");
}

/* Generated chapter data must stay presentation-free: no markup, and no HTML
 * tag names standing in for block types. Design changes belong in CSS. */
function lintDataPurity(file) {
  const raw = fs.readFileSync(path.join(LESSONS, file), "utf8");
  const problems = [];
  if (/<[a-z/][^>]*>/.test(raw)) {
    problems.push("markup in " + file + " — text and notes should be plain data");
  }
  const tagLike = raw.match(/"type":\s*"(h[1-6]|div|span|b|i|em|strong)"/g);
  if (tagLike) {
    problems.push("HTML tag names as block types in " + file + ": " +
                  [...new Set(tagLike)].join(", "));
  }
  const cryptic = ['"t":', '"s":', '"trans":', '"transTitle":', '"def":',
                   '"a":', '"w":', '"hanjaList":'].filter(function (k) {
    return raw.indexOf(k) !== -1;
  });
  if (cryptic.length) {
    problems.push("abbreviated keys in " + file + ": " + cryptic.join(" "));
  }
  return problems;
}

/* --- page rendering -------------------------------------------------- */

function page(file, url) {
  const dom = new JSDOM(read(file),
    { runScripts: "outside-only", url: "https://example.invalid/" + url });
  dom.window.eval(read("assets", "kiip.js"));
  return dom;
}

function checkChapter(file) {
  const slug = file.replace(/\.js$/, "");
  const dom = page("lesson.html", "lesson.html?ch=" + slug);
  const w = dom.window;
  const problems = lintDataPurity(file);

  try {
    w.eval(fs.readFileSync(path.join(LESSONS, file), "utf8"));
    w.eval(read("assets", "lesson.js"));
  } catch (e) {
    problems.push("script error: " + e.message);
  }

  const d = w.document;
  const buttons = d.querySelectorAll("button.anno");

  buttons.forEach(function (b) {
    b.click();
    const card = d.querySelector(".anno-card");
    if (!card) problems.push("no card for " + b.dataset.key);
    else if (card.textContent.trim() === b.dataset.key) {
      problems.push("empty card for " + b.dataset.key);
    }
    b.click();
  });

  // an answer written into a review gap must start covered, reveal when
  // asked for, and still be present in the text so it can be copied
  d.querySelectorAll("button.blank").forEach(function (b) {
    if (!b.textContent.trim()) problems.push("a covered gap has no answer in it");
    if (b.classList.contains("is-shown")) {
      problems.push("gap “" + b.textContent + "” starts revealed");
    }
    b.click();
    if (!b.classList.contains("is-shown")) {
      problems.push("gap “" + b.textContent + "” did not reveal");
    }
    if (b.getAttribute("aria-pressed") !== "true") {
      problems.push("gap “" + b.textContent + "” did not report being revealed");
    }
    b.click();
    if (b.classList.contains("is-shown")) {
      problems.push("gap “" + b.textContent + "” did not cover again");
    }
  });
  d.querySelectorAll("span.blank.is-empty").forEach(function (s) {
    if (s.textContent) problems.push("an unanswered gap carries text");
  });

  // each translated paragraph must be paired with its own Korean paragraph,
  // in that order, rather than pooled into one block for the section
  d.querySelectorAll(".para-pair").forEach(function (pair) {
    const kids = [...pair.children].map(function (c) { return c.className; })
      .filter(function (c) { return c !== "en-fold"; });
    if (kids.length !== 2 || !/ko-para/.test(kids[0]) || !/^en-wrap/.test(kids[1])) {
      problems.push("a paragraph pair is not [korean, english]: " + kids.join(","));
    }
    if (!pair.querySelector(".en-para").textContent.trim()) {
      problems.push("a paragraph pair has an empty translation");
    }
  });
  d.querySelectorAll(".en-para").forEach(function (en) {
    if (!en.parentNode.classList.contains("en-wrap")) {
      problems.push("a translation is not inside a collapsible wrapper");
    }
    if (/^["\u201c]|["\u201d]$/.test(en.textContent.trim())) {
      problems.push("a translation kept its surrounding quotes");
    }
  });

  // translations start collapsed, and a control reveals exactly its own run
  const folds = [...d.querySelectorAll(".en-fold")];
  const open = [...d.querySelectorAll(".en-wrap.is-open")];
  if (open.length) problems.push(open.length + " translations start open");
  if (d.querySelectorAll(".en-para").length && !folds.length) {
    problems.push("translations present but nothing reveals them");
  }
  if (folds.length) {
    folds[0].click();
    if (!d.querySelectorAll(".en-wrap.is-open").length) {
      problems.push("a translation control revealed nothing");
    }
    if (folds[0].getAttribute("aria-expanded") !== "true") {
      problems.push("a translation control did not report being open");
    }
    folds[0].click();
    if (d.querySelectorAll(".en-wrap.is-open").length) {
      problems.push("a translation control did not close again");
    }
  }

  // a word's explanation belongs between the Korean and its translation
  const marked = d.querySelector(".para-pair button.anno");
  if (marked) {
    marked.click();
    const pair = marked.closest(".para-pair");
    const order = [...pair.children].map(function (c) {
      return c.className.split(" ")[0];
    });
    const card = order.indexOf("anno-card");
    if (card === -1) {
      problems.push("a card opened outside the paragraph pair");
    } else if (card < order.indexOf("ko-para") || card > order.indexOf("en-wrap")) {
      problems.push("card is not between the Korean and its translation: " +
                    order.join(" > "));
    }
    marked.click();
  }

  // the page's own list marker must not be printed inside the item as well
  d.querySelectorAll(".ko-bullet").forEach(function (li) {
    const t = li.textContent.trim();
    if (/^[•·]/.test(t)) problems.push("a list item still starts with a bullet: " + t.slice(0, 30));
    if (/^\d+\.\s/.test(t)) {
      problems.push("a list item still starts with its number: " + t.slice(0, 30));
    }
  });
  d.querySelectorAll("ul.ko-list > li").forEach(function (li) {
    if (/^\d/.test(li.textContent.trim())) return;
  });

  // a caption has something to caption
  d.querySelectorAll("figure.figure").forEach(function (f) {
    if (!f.querySelector(".figure-slot")) problems.push("a caption has no figure above it");
    if (!f.querySelector("figcaption").textContent.trim()) {
      problems.push("an empty caption");
    }
  });

  // no handwritten English is printed beside a term; it belongs in the entry
  d.querySelectorAll(".gloss-en").forEach(function () {
    problems.push("a handwritten gloss is still printed inline");
  });

  // a real parenthetical must not be mistaken for a gap
  if (d.body.textContent.indexOf("(2020년 기준)") === -1 &&
      /2020년 기준/.test(d.body.textContent)) {
    problems.push("(2020년 기준) was treated as a fill-in gap");
  }

  // a header cell that spans must actually span
  d.querySelectorAll(".table-wrap th").forEach(function (th) {
    const cols = th.closest("table").querySelector("tbody tr");
    if (!cols) return;
    const total = [...th.parentNode.children].reduce(function (n, c) {
      return n + (c.colSpan || 1);
    }, 0);
    if (total !== cols.children.length) {
      problems.push("header spans " + total + " columns but the body has " +
                    cols.children.length);
    }
  });

  // leftovers that should never reach the reader (the corrections list is
  // exempt: it quotes the placeholders it replaced)
  const notes = d.querySelector(".sect-notes");
  if (notes) notes.remove();
  const stray = d.body.textContent.match(/undefined|\[object |NaN/);
  if (stray) problems.push("stray " + stray[0]);

  report(slug, problems,
    "sections=" + d.querySelectorAll("section.sect").length +
    " paragraphs=" + d.querySelectorAll(".ko-para").length +
    " glosses=" + d.querySelectorAll(".gloss-row").length +
    " tables=" + d.querySelectorAll(".table-wrap table").length +
    " annotations=" + buttons.length +
    " paired=" + d.querySelectorAll(".para-pair").length +
    " folds=" + d.querySelectorAll(".en-fold").length +
    " whole=" + d.querySelectorAll("details.trans").length +
    " gaps=" + d.querySelectorAll(".blank").length +
    "/" + d.querySelectorAll("button.blank").length + " answered");
}

/* A bad address must say so rather than rendering a blank page. */
function checkAddressHandling() {
  const problems = [];

  // a chapter that does not exist: jsdom will not fetch the injected script,
  // so fail its load by hand to exercise the error path
  let dom = page("lesson.html", "lesson.html?ch=99-nope");
  dom.window.eval(read("assets", "lesson.js"));
  let d = dom.window.document;
  const tag = d.querySelector('script[src="lessons/99-nope.js"]');
  if (!tag) {
    problems.push("no chapter script was requested for a plausible slug");
  } else {
    tag.dispatchEvent(new dom.window.Event("error"));
    if (!d.querySelector(".lesson-head").textContent.includes("not found")) {
      problems.push("a chapter that fails to load renders nothing");
    }
  }

  // a malformed name must be refused outright, not turned into a script src
  dom = page("lesson.html", "lesson.html?ch=" + encodeURIComponent("../secrets"));
  dom.window.eval(read("assets", "lesson.js"));
  d = dom.window.document;
  if (d.querySelector("script[src*='secrets']")) {
    problems.push("a malformed chapter name reached a script src");
  }
  if (!d.querySelector(".lesson-head").textContent.includes("not found")) {
    problems.push("a malformed chapter name renders nothing");
  }

  // no name at all
  dom = page("lesson.html", "lesson.html");
  dom.window.eval(read("assets", "lesson.js"));
  if (!dom.window.document.querySelector(".lesson-head").textContent.includes("not found")) {
    problems.push("an address with no chapter renders nothing");
  }

  report("address handling", problems, "missing, malformed and absent slugs");
}

function checkIndex(chapters) {
  const dom = page("index.html", "index.html");
  const w = dom.window;
  if (fs.existsSync(path.join(LESSONS, "manifest.js"))) {
    w.eval(fs.readFileSync(path.join(LESSONS, "manifest.js"), "utf8"));
  }
  w.eval(read("assets", "index.js"));
  const d = w.document;

  const problems = [];
  const rows = d.querySelectorAll(".lesson-list li");
  if (rows.length !== chapters.length) {
    problems.push("index lists " + rows.length + " of " + chapters.length + " chapters");
  }
  rows.forEach(function (li) {
    const href = li.querySelector("a").getAttribute("href");
    if (!/^lesson\.html\?ch=/.test(href)) problems.push("bad chapter link: " + href);
  });

  // filtering must show exactly the chapters carrying that tag, and clearing
  // it must restore the list — a count that merely changes is not enough,
  // since with one chapter it cannot
  const manifest = w.KIIP.all();
  const tags = d.querySelectorAll(".filters .tag");
  if (tags.length) {
    const label = tags[0].textContent;
    tags[0].click();
    const expected = manifest.filter(function (c) {
      return (c.tags || []).indexOf(label) !== -1;
    }).length;
    const shown = [...d.querySelectorAll(".lesson-list li")];
    if (shown.length !== expected) {
      problems.push("filtering by " + label + " shows " + shown.length +
                    " chapters, expected " + expected);
    }
    shown.forEach(function (li) {
      const rowTags = [...li.querySelectorAll(".tags span")].map(function (s) {
        return s.textContent;
      });
      if (rowTags.indexOf(label) === -1) {
        problems.push("a chapter without " + label + " survived filtering");
      }
    });
    tags[0].click();
    if (d.querySelectorAll(".lesson-list li").length !== manifest.length) {
      problems.push("clearing the filter did not restore the full list");
    }
  } else if (chapters.length) {
    problems.push("chapters present but no topic filters were built");
  }

  if (!chapters.length && d.querySelector("[data-empty]").hidden) {
    problems.push("no chapters, but the empty state is hidden");
  }

  report("index.html", problems,
    "chapters=" + chapters.length + " tags=" + tags.length);
}

/* --- run ------------------------------------------------------------- */

lintSectionLayering();

const chapters = fs.existsSync(LESSONS)
  ? fs.readdirSync(LESSONS).filter(function (f) {
      return f.endsWith(".js") && f !== "manifest.js";
    }).sort()
  : [];

chapters.forEach(checkChapter);
checkAddressHandling();
checkIndex(chapters);

process.exit(failed ? 1 : 0);
