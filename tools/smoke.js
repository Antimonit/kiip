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

const { JSDOM, VirtualConsole } = require("jsdom");
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

/* the toggle changes layout after its fade and then animates the height, so
   the checks have to wait it out; comfortably longer than the 150ms fade plus
   the 260ms resize in assets/style.css */
const SETTLE = 550;
const settle = () => new Promise(function (r) { setTimeout(r, SETTLE); });

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
                  "en-title", "split-toggle", "figure-slot", "row",
                  "label-group", "label-group-name", "label-group-items",
                  "ko-sublist", "columns", "column", "column-title"];
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

/* The two branches are kept apart by hand, and by hand they drift: the site
 * lands in a chapter's commit, or a rebuild of `content` flattens thirty
 * chapters into one. Both have happened. These read the history and say so.
 *
 * A commit belongs to one side or the other. `master` carries the site, the
 * tooling and the design; `content` carries the chapters and what is
 * generated from them. Nothing carries both. */
const MODULE = /^tools\/chapters\/ch\d.*\.py$/;

function lintHistory() {
  let log;
  try {
    log = require("child_process").execFileSync(
      "git", ["log", "--format=%x00%h %s", "--name-status"],
      { cwd: ROOT, encoding: "utf8", stdio: ["ignore", "pipe", "ignore"] });
  } catch (e) {
    return report("git history", [], "no repository to read");   // a copy, not a clone
  }

  const problems = [];
  const commits = log.split("\0").filter(function (c) { return c.trim(); });
  commits.forEach(function (commit) {
    const lines = commit.trim().split("\n");
    const [hash, ...subject] = lines[0].split(" ");
    const changed = lines.slice(1).filter(Boolean).map(function (l) {
      const [status, ...rest] = l.split("\t");
      return { status: status[0], path: rest[rest.length - 1] };
    });
    const say = hash + " " + subject.join(" ").slice(0, 44);

    /* One chapter to a commit. More than one means a rebuild has folded a
     * run of them together and lost who added what. */
    const added = changed.filter(function (c) {
      return c.status === "A" && MODULE.test(c.path);
    });
    if (added.length > 1) {
      problems.push(say + " — adds " + added.length + " chapters at once (" +
                    added.slice(0, 3).map(function (c) {
                      return c.path.replace("tools/chapters/", "");
                    }).join(", ") + "…)");
    }
  });

  report("git history", problems, commits.length + " commits, one chapter each");
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

  /* Every entry is filed under the word it explains, and every mark points
     at an entry that exists. The keys come from the Doc's comment anchors,
     so without this they drift back to a typo or an inflected form. */
  const data = JSON.parse(raw.slice(raw.indexOf("{"), raw.lastIndexOf(")")));
  const notes = data.annotations || {};
  Object.keys(notes).forEach(function (key) {
    const head = (notes[key].headword || key).trim();
    if (head !== key) {
      problems.push("entry filed under " + key + " but explains " + head +
                    " in " + file);
    }
  });
  const dangling = new Set();
  (function walk(node) {
    if (Array.isArray(node)) return node.forEach(walk);
    if (node && typeof node === "object") {
      if (node.word && node.annotation && !notes[node.annotation]) {
        dangling.add(node.annotation);
      }
      return Object.keys(node).forEach(function (k) { walk(node[k]); });
    }
  })(data.blocks || []);
  if (dangling.size) {
    problems.push("marks with no entry behind them in " + file + ": " +
                  [...dangling].join(", "));
  }
  return problems;
}

/* --- page rendering -------------------------------------------------- */

/* pretendToBeVisual gives the page requestAnimationFrame, and the virtual
   console turns anything the page throws into a failure — without it a
   script error inside an event listener passes silently. */
function page(file, url) {
  const failures = [];
  const console_ = new VirtualConsole();
  console_.on("jsdomError", function (e) { failures.push("threw: " + e.message); });
  console_.on("error", function () {
    failures.push("logged an error: " + [...arguments].join(" "));
  });

  const dom = new JSDOM(read(file), {
    runScripts: "outside-only",
    pretendToBeVisual: true,
    virtualConsole: console_,
    url: "https://example.invalid/" + url,
  });
  dom.failures = failures;
  dom.window.eval(read("assets", "kiip.js"));
  return dom;
}

async function checkChapter(file) {
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

  // a translated paragraph is rows of [korean, english], and the English is
  // not rendered until the article is put side by side
  d.querySelectorAll(".para-pair").forEach(function (pair) {
    const rows = [...pair.children];
    if (!rows.length) problems.push("a translated paragraph has no rows");
    rows.forEach(function (row) {
      const kids = [...row.children].map(function (c) { return c.className; });
      if (kids.length !== 2 || kids[0] !== "ko" || kids[1] !== "en") {
        problems.push("a row is not [korean, english]: " + kids.join(","));
      }
      if (!row.querySelector(".en").textContent.trim()) {
        problems.push("a row has an empty translation");
      }
      if (!row.querySelector(".ko").textContent.trim()) {
        problems.push("a row has no Korean");
      }
    });
    if (pair.classList.contains("is-split")) {
      problems.push("a paragraph starts side by side");
    }
    if (pair.style.height) {
      problems.push("a paragraph was left with a measured height on it");
    }
  });

  // reassembling the rows must give back the paragraph, so the sentence cuts
  // cannot have dropped or duplicated anything
  d.querySelectorAll(".para-pair").forEach(function (pair) {
    const joined = [...pair.querySelectorAll(".ko")]
      .map(function (k) { return k.textContent.trim(); }).join(" ");
    const slug2 = file.replace(/\.js$/, "");
    if (!joined) problems.push("rows reassemble to nothing in " + slug2);
  });

  // one control per article, and it switches that article only
  const toggles = [...d.querySelectorAll(".split-toggle")];
  if (d.querySelectorAll(".para-pair").length && !toggles.length) {
    problems.push("translated paragraphs but nothing to reveal them");
  }
  if (toggles.length) {
    toggles[0].click();
    await settle();
    const on = d.querySelectorAll(".para-pair.is-split").length;
    if (!on) problems.push("the control did not put anything side by side");
    if (on === d.querySelectorAll(".para-pair").length && toggles.length > 1) {
      problems.push("one control switched every article, not just its own");
    }
    if (toggles[0].getAttribute("aria-pressed") !== "true") {
      problems.push("the control did not report being on");
    }
    toggles[0].click();
    await settle();
    if (d.querySelectorAll(".para-pair.is-split").length) {
      problems.push("the control did not switch back");
    }
    if (toggles[0].getAttribute("aria-pressed") !== "false") {
      problems.push("the control did not report being off");
    }
  }

  // a word's explanation opens right after the paragraph it was tapped in,
  // in either layout — side by side there is no "between" to sit in
  const marked = d.querySelector(".para-pair button.anno");
  if (marked) {
    marked.click();
    const pair = marked.closest(".para-pair");
    const after = pair.nextElementSibling;
    if (!after || !after.classList.contains("anno-card")) {
      problems.push("a card did not open after the paragraph it belongs to");
    }
    marked.click();
    const closing = pair.nextElementSibling;
    if (closing && closing.classList.contains("anno-card") &&
        !closing.classList.contains("is-collapsed")) {
      problems.push("a card did not begin to close again");
    }
    await settle();               // it folds away before it is removed
    if (pair.nextElementSibling &&
        pair.nextElementSibling.classList.contains("anno-card")) {
      problems.push("a card did not close again");
    }
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

  /* A real parenthetical must not be mistaken for a gap. A gap's answer is a
     word the reader is meant to supply, never a citation — so a date or a
     기준/출처 inside one means the blank detector ate a parenthesis. */
  d.querySelectorAll(".blank").forEach(function (b) {
    if (/\d{4}년|기준|출처|단위/.test(b.textContent)) {
      problems.push("a parenthetical was treated as a fill-in gap: " +
                    b.textContent.trim());
    }
  });

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

  problems.push(...dom.failures);

  report(slug, problems,
    "sections=" + d.querySelectorAll("section.sect").length +
    " paragraphs=" + d.querySelectorAll(".ko-para").length +
    " glosses=" + d.querySelectorAll(".gloss-row").length +
    " tables=" + d.querySelectorAll(".table-wrap table").length +
    " annotations=" + buttons.length +
    " paragraphs+en=" + d.querySelectorAll(".para-pair").length +
    " rows=" + d.querySelectorAll(".para-pair .row").length +
    " articles=" + d.querySelectorAll(".split-toggle").length +
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

function checkIndex(chapters, parts) {
  const dom = page("index.html", "index.html");
  const w = dom.window;
  ["manifest.js", "contents.js"].forEach(function (f) {
    if (fs.existsSync(path.join(LESSONS, f))) {
      w.eval(fs.readFileSync(path.join(LESSONS, f), "utf8"));
    }
  });
  w.eval(read("assets", "index.js"));
  const d = w.document;

  const problems = [];
  const book = w.KIIP.book();
  const inBook = book.parts.reduce(function (n, p) {
    return n + p.chapters.length;
  }, 0);

  /* every chapter the book has is listed, and only the built ones link */
  const rows = [...d.querySelectorAll(".entry")];
  if (rows.length !== (inBook || chapters.length)) {
    problems.push("index lists " + rows.length + " of " +
                  (inBook || chapters.length) + " chapters");
  }
  const links = rows.filter(function (r) { return r.tagName === "A"; });
  if (links.length !== chapters.length) {
    problems.push(links.length + " chapters link, but " + chapters.length +
                  " are built");
  }
  links.forEach(function (a) {
    const href = a.getAttribute("href");
    if (!/^lesson\.html\?ch=/.test(href)) problems.push("bad chapter link: " + href);
  });
  rows.filter(function (r) { return r.tagName !== "A"; }).forEach(function (r) {
    if (!r.classList.contains("is-pending")) {
      problems.push("a chapter neither links nor is marked pending");
    }
  });
  if (inBook && d.querySelectorAll(".part").length !== book.parts.length) {
    problems.push("the contents are not grouped into the book's parts");
  }

  /* the parts are the only grouping, and each names itself in the data so
     the stylesheet can give it the book's colour */
  d.querySelectorAll(".part").forEach(function (sec) {
    if (!sec.dataset.part) problems.push("a part does not say which part it is");
    if (!sec.querySelector(".part-chip .part-name")) {
      problems.push("a part has no name");
    }
  });

  /* a part whose closing spread is built links to it */
  const partLinks = [...d.querySelectorAll(".part-link")];
  if (partLinks.length !== parts.length) {
    problems.push(partLinks.length + " parts link to their closing pages, but "
                  + parts.length + " are built");
  }
  partLinks.forEach(function (a) {
    if (!/^lesson\.html\?ch=part-\d+$/.test(a.getAttribute("href"))) {
      problems.push("bad part link: " + a.getAttribute("href"));
    }
  });

  if (!chapters.length && d.querySelector("[data-empty]").hidden) {
    problems.push("no chapters, but the empty state is hidden");
  }

  problems.push(...dom.failures);

  report("index.html", problems,
    "built=" + chapters.length + " listed=" + rows.length +
    " parts=" + d.querySelectorAll(".part").length +
    " closing=" + partLinks.length);
}

/* --- run ------------------------------------------------------------- */

(async function () {
  lintSectionLayering();
  lintHistory();

  const pages = fs.existsSync(LESSONS)
    ? fs.readdirSync(LESSONS).filter(function (f) {
        return f.endsWith(".js") && f !== "manifest.js" &&
               f !== "contents.js";
      }).sort()
    : [];
  /* a part page is built and rendered as a chapter, but it is not one of the
     book's fifty, so the index does not list it as a row */
  const parts = pages.filter(function (f) { return f.startsWith("part-"); });
  const chapters = pages.filter(function (f) { return !parts.includes(f); });

  for (const file of pages) await checkChapter(file);
  checkAddressHandling();
  checkIndex(chapters, parts);

  process.exit(failed ? 1 : 0);
})();
