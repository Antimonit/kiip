/* ------------------------------------------------------------------
   Renders a lesson from the LESSON object in lessons/<slug>/lesson.js.
   No build step: plain script tags, works over file:// as well as http.
   ------------------------------------------------------------------ */

(function () {
  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }

  function render(lesson) {

  /* --- head ------------------------------------------------------ */

  /* a part page is addressed and rendered as a chapter; only what it calls
     itself differs */
  var name = lesson.part ? "제" + lesson.number + "편 " + lesson.unit
                         : lesson.number + ". " + lesson.title;
  document.title = name + " — KIIP 5";

  var head = document.querySelector(".lesson-head");
  head.appendChild(el("div", "eyebrow", lesson.part
    ? "제" + lesson.number + "편 · " + lesson.unit
    : "Chapter " + lesson.number + " · " + lesson.unit));
  head.appendChild(el("h2", null, lesson.title));
  head.appendChild(el("p", "en", lesson.titleEnglish));

  /* --- annotation buttons ---------------------------------------- */

  var buttons = [];

  /* The words the textbook itself glosses in the margin beside an article,
     as against the ones marked in the text for other reasons. Both are
     annotations and behave alike; the stylesheet tells them apart. */
  var glossed = {};
  (lesson.blocks || []).forEach(function (b) {
    (b.entries || []).forEach(function (e) {
      if (e.annotation) glossed[e.annotation] = true;
    });
  });

  function annoButton(seg) {
    var key = seg.annotation || seg.word;
    var b = el("button", "anno" + (glossed[key] ? " is-glossed" : ""), seg.word);
    b.type = "button";
    b.dataset.key = key;
    b.setAttribute("aria-expanded", "false");
    buttons.push(b);
    return b;
  }

  /* A gap in the review section. An answer is kept covered until asked
     for — still present in the text, so copying it works. */
  function blankSlot(answer) {
    if (!answer) return el("span", "blank is-empty");

    var b = el("button", "blank", answer);
    b.type = "button";
    b.setAttribute("aria-pressed", "false");
    b.title = "Show the answer";
    b.addEventListener("click", function () {
      var shown = b.classList.toggle("is-shown");
      b.setAttribute("aria-pressed", String(shown));
      b.title = shown ? "Hide the answer" : "Show the answer";
    });
    return b;
  }

  function fillSpans(node, segs) {
    (segs || []).forEach(function (seg) {
      if (typeof seg === "string") {
        node.appendChild(document.createTextNode(seg));
      } else if (seg.blank !== undefined) {
        node.appendChild(blankSlot(seg.blank));
      } else {
        node.appendChild(annoButton(seg));
      }
    });
    return node;
  }

  /* --- annotation card ------------------------------------------- */

  function buildCard(key) {
    var a = (lesson.annotations || {})[key];
    var card = el("div", "anno-card");
    if (!a) {
      card.appendChild(el("p", null, key));
      return card;
    }

    var hw = el("p");
    hw.appendChild(el("span", "headword", a.headword + (a.hanja ? "(" + a.hanja + ")" : "")));
    // the note written beside the word stands in only where the word has no
    // definition of its own; otherwise it just repeats it
    var gloss = a.meaning || a.handwritten;
    if (gloss) hw.appendChild(document.createTextNode(" — " + gloss));
    card.appendChild(hw);

    (a.characters || []).forEach(function (h) {
      var line = el("p", "hanja");
      line.appendChild(el("b", null, h.reading ? h.reading + "(" + h.char + ")" : h.char));
      line.appendChild(document.createTextNode(" (" + h.gloss + ")"));
      card.appendChild(line);
    });

    (a.notes || []).forEach(function (t) {
      card.appendChild(el("p", "usage", t));
    });

    if (a.surfaces && a.surfaces.length) {
      card.appendChild(el("p", "surfaces", "in the text: " + a.surfaces.join(", ")));
    }
    return card;
  }

  /* --- blocks ----------------------------------------------------- */

  var docEl = document.querySelector("[data-doc]");
  var host = docEl;

  /* Every section gets the same header shape — a title and, when the data
     supplies one, the section's topic. Whether those sit on one line, and
     whether the title reads as a chip or a heading, is left to CSS. */
  function openSection(b) {
    var sec = el("section", "sect sect-" + b.kind);
    var header = el("header", "sect-head");
    header.appendChild(el("h3", "sect-title", b.text));
    if (b.topic) {
      var topic = el("p", "sect-topic", b.topic);
      if (b.titleTranslation) topic.appendChild(el("span", "en-title", b.titleTranslation));
      header.appendChild(topic);
    }
    sec.appendChild(header);
    docEl.appendChild(sec);
    host = sec;
    if (b.translation) host.appendChild(translationBlock(b.translation));
  }

  function translationBlock(text) {
    var d = el("details", "trans");
    d.appendChild(el("summary", null, "English"));
    text.split("\n\n").forEach(function (p) {
      d.appendChild(el("p", null, p.replace(/^"|"$/g, "")));
    });
    return d;
  }

  (lesson.blocks || []).forEach(function (b) {
    switch (b.type) {
      case "section":
        openSection(b);
        return;

      case "heading": {
        var h = el(b.level <= 2 ? "h4" : "h5",
                   "sub-title sub-level-" + b.level, b.spans ? "" : b.text);
        if (b.spans) fillSpans(h, b.spans);
        if (b.titleTranslation) h.appendChild(el("span", "en-title", b.titleTranslation));
        host.appendChild(h);
        if (b.translation) host.appendChild(translationBlock(b.translation));
        return;
      }

      /* A translated paragraph is built as rows of sentence pairs. In its
         default state the rows are inline, so the Korean reads as one
         paragraph and the English is out of the way; side by side turns each
         row into two columns. One structure, two layouts. */
      case "paragraph": {
        if (!b.translation) {
          host.appendChild(fillSpans(
            el("p", "ko-para" + (b.role ? " is-" + b.role : "")), b.spans));
          return;
        }
        var pair = el("div", "para-pair");
        var units = b.sentences ||
          [{ spans: b.spans, translation: b.translation }];
        units.forEach(function (unit) {
          var row = el("div", "row");
          var ko = fillSpans(el("span", "ko"), unit.spans);
          ko.appendChild(document.createTextNode(" "));
          row.appendChild(ko);
          row.appendChild(el("span", "en", unit.translation));
          pair.appendChild(row);
        });
        host.appendChild(pair);
        return;
      }

      case "bullet": {
        var wanted = b.ordered ? "OL" : "UL";
        var list = host.lastElementChild;
        if (!list || list.tagName !== wanted) {
          list = el(b.ordered ? "ol" : "ul", "ko-list");
          host.appendChild(list);
        }
        var item = fillSpans(el("li", "ko-bullet"), b.spans);
        /* a nested item hangs off the item above it, which is how the page
           draws a bracketed sub-list */
        var over = b.level > 1 ? list.lastElementChild : null;
        if (over) {
          var sub = over.lastElementChild;
          if (!sub || sub.tagName !== "UL") {
            sub = el("ul", "ko-list ko-sublist");
            over.appendChild(sub);
          }
          sub.appendChild(item);
          return;
        }
        list.appendChild(item);
        return;
      }

      case "glossary": {
        var box = el("div", "glossbox");
        b.entries.forEach(function (it) {
          var row = el("div", "gloss-row");
          var term = el("div", "gloss-term");
          if (it.annotation) {
            term.appendChild(annoButton({ word: it.term, annotation: it.annotation }));
          } else {
            term.appendChild(document.createTextNode(it.term));
          }
          row.appendChild(term);
          row.appendChild(fillSpans(el("div", "gloss-def"), it.definition));
          box.appendChild(row);
        });
        host.appendChild(box);
        return;
      }

      /* A cell is plain text, or text that the book merges across columns
         or down rows. */
      case "table": {
        function cell(tag, c) {
          var n = el(tag, null, typeof c === "string" ? c : c.text);
          if (c.span) n.colSpan = c.span;
          if (c.spanDown) n.rowSpan = c.spanDown;
          return n;
        }
        var wrapEl = el("div", "table-wrap");
        var t = el("table");
        if (b.header) {
          var thead = el("thead");
          var tr = el("tr");
          b.header.forEach(function (c) { tr.appendChild(cell("th", c)); });
          thead.appendChild(tr);
          t.appendChild(thead);
        }
        var tb = el("tbody");
        b.rows.forEach(function (row) {
          var tr2 = el("tr");
          row.forEach(function (c) { tr2.appendChild(cell("td", c)); });
          tb.appendChild(tr2);
        });
        t.appendChild(tb);
        wrapEl.appendChild(t);
        host.appendChild(wrapEl);
        return;
      }

      case "chart": {
        var fig = el("figure", "chart");
        var max = Math.max.apply(null, b.rows.map(function (r) { return r[1]; }));
        b.rows.forEach(function (r) {
          var row = el("div", "bar-row");
          row.appendChild(el("span", "bar-label", r[0]));
          var track = el("span", "bar-track");
          var fill = el("span", "bar-fill");
          fill.style.width = (r[1] / max * 100) + "%";
          track.appendChild(fill);
          row.appendChild(track);
          row.appendChild(el("span", "bar-value", r[1] + b.unit));
          fig.appendChild(row);
        });
        fig.appendChild(el("figcaption", null, b.caption));
        host.appendChild(fig);
        return;
      }

      case "verse": {
        var v = el("div", "verse");
        b.lines.forEach(function (l) { v.appendChild(fillSpans(el("p"), l)); });
        host.appendChild(v);
        return;
      }

      /* Photo labels. Where the page sorts the pictures into named kinds,
         the data says so and each kind keeps its own heading. */
      case "labels": {
        var lb = el("div", "labels" + (b.groups ? " is-grouped" : ""));
        function chips(into, items) {
          items.forEach(function (x) { into.appendChild(fillSpans(el("span"), x)); });
          return into;
        }
        if (b.groups) {
          b.groups.forEach(function (g) {
            var box = el("div", "label-group");
            box.appendChild(fillSpans(el("p", "label-group-name"), g.name));
            box.appendChild(chips(el("div", "label-group-items"), g.items));
            lb.appendChild(box);
          });
        } else {
          chips(lb, b.items);
        }
        host.appendChild(lb);
        return;
      }

      /* The page has a photo here. It is not reproduced, but the caption
         needs something to caption or it reads as a stray sentence. */
      case "figure": {
        var fig = el("figure", "figure");
        fig.appendChild(el("div", "figure-slot"));
        fig.appendChild(el("figcaption", null, b.text));
        host.appendChild(fig);
        return;
      }

      /* Prose the book sets side by side — two columns of an aside, three
         of a news page. Each column keeps its own title. */
      case "columns": {
        var cols = el("div", "columns");
        b.columns.forEach(function (c) {
          var col = el("div", "column");
          col.appendChild(fillSpans(el("h5", "column-title"), c.title));
          (c.paragraphs || []).forEach(function (p) {
            col.appendChild(fillSpans(el("p", "ko-para"), p));
          });
          cols.appendChild(col);
        });
        host.appendChild(cols);
        return;
      }

      case "source":
        host.appendChild(el("p", "source", b.text));
        return;

      case "margin": {
        var mg = el("div", "margin-note");
        mg.appendChild(el("span", "margin-label", "여백 메모"));
        b.items.forEach(function (x) { mg.appendChild(fillSpans(el("span"), x)); });
        host.appendChild(mg);
        return;
      }
    }
  });

  /* --- chapter-level glosses (annotations anchored on the title) -- */

  if (lesson.chapterGlossary && lesson.chapterGlossary.length) {
    var first = docEl.querySelector("section");
    var box2 = el("div", "glossbox");
    lesson.chapterGlossary.forEach(function (key) {
      var a = lesson.annotations[key] || {};
      var row = el("div", "gloss-row");
      var term = el("div", "gloss-term");
      term.appendChild(annoButton({ word: key, annotation: key }));
      row.appendChild(term);
      row.appendChild(el("div", "gloss-def", a.meaning || ""));
      box2.appendChild(row);
    });
    if (first) docEl.insertBefore(box2, first);
  }

  /* --- transcription notes ---------------------------------------- */

  if (lesson.notes && lesson.notes.length) {
    var sec = el("section", "sect sect-notes");
    var header = el("header", "sect-head");
    header.appendChild(el("h3", "sect-title", "Transcription notes"));
    header.appendChild(el("p", "sect-topic",
      lesson.notes.length === 1 ? "1 still to check against the page"
                                : lesson.notes.length + " still to check against the page"));
    sec.appendChild(header);
    var ul = el("ul", "notes");
    lesson.notes.forEach(function (n) {
      var li = el("li");
      if (n.was) {
        li.appendChild(el("span", "ko", n.was + " → " + n.now));
        li.appendChild(document.createTextNode(" — "));
      }
      li.appendChild(document.createTextNode(n.why));
      if (n.count > 1) {
        li.appendChild(el("span", "count", " (×" + n.count + ")"));
      }
      ul.appendChild(li);
    });
    sec.appendChild(ul);
    docEl.appendChild(sec);
  }

  /* --- English: side by side, one control per article ---------------
     An article is a run of consecutive translated paragraphs, which is
     exactly the prose one translation covers. */

  function runs() {
    var found = [];
    docEl.querySelectorAll(".para-pair").forEach(function (pair) {
      var last = found[found.length - 1];
      if (last && last[last.length - 1].nextElementSibling === pair) last.push(pair);
      else found.push([pair]);
    });
    return found;
  }

  var FADE_MS = 150;     // must match the opacity transition in style.css
  var RESIZE_MS = 260;   // must match the height transition in style.css

  function still() {
    return window.matchMedia &&
      window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  }

  /* Fade through, and animate the height the change costs.
  
     Nothing about turning a paragraph into a column of sentences can be
     interpolated, so the paragraph fades out, changes layout while it cannot
     be seen, and fades back. But the change also makes the paragraph taller
     or shorter, and left alone that moves everything below it in one frame.
     So the height is measured before and after and animated between the two,
     which is the only part of this that the eye can actually follow. */
  function setSplit(run, button, on) {
    button.setAttribute("aria-pressed", String(on));

    var swap = function () {
      run.forEach(function (pair) {
        pair.classList.toggle("is-split", on);
        pair.classList.remove("is-fading");
      });
    };

    if (still()) return swap();

    var before = run.map(function (pair) {
      return pair.getBoundingClientRect().height;
    });

    run.forEach(function (pair, i) {
      pair.style.height = before[i] + "px";
      pair.classList.add("is-fading");
    });

    window.setTimeout(function () {
      run.forEach(function (pair, i) {
        pair.classList.toggle("is-split", on);

        pair.style.height = "auto";
        var after = pair.getBoundingClientRect().height;

        pair.style.height = before[i] + "px";
        void pair.offsetHeight;          // commit the starting height
        pair.classList.add("is-resizing");
        pair.style.height = after + "px";
        pair.classList.remove("is-fading");

        window.setTimeout(function () {
          pair.classList.remove("is-resizing");
          pair.style.height = "";
        }, RESIZE_MS);
      });
    }, FADE_MS);
  }

  runs().forEach(function (run) {
    var b = el("button", "split-toggle", "Side by side");
    b.type = "button";
    b.setAttribute("aria-pressed", "false");
    b.addEventListener("click", function () {
      setSplit(run, b, b.getAttribute("aria-pressed") !== "true");
    });
    run[0].parentNode.insertBefore(b, run[0]);
  });

  /* --- interaction ------------------------------------------------ */

  /* One card is open at a time; it drops in after the block the word sits in. */

  var CARD_HOSTS = ".para-pair, .ko-para, .ko-list, .gloss-row, .sub-title," +
                   " .sect-title, .aside-topic, .verse, .labels, .margin-note";
  var openBtn = null;

  function close() {
    var c = docEl.querySelector(".anno-card");
    if (c) c.remove();
    buttons.forEach(function (b) { b.setAttribute("aria-expanded", "false"); });
    openBtn = null;
  }

  function select(btn) {
    var reopening = btn === openBtn;
    close();
    if (reopening) return;
    openBtn = btn;
    btn.setAttribute("aria-expanded", "true");
    // between the Korean and its translation: the word first, then the
    // whole paragraph's English below it
    (btn.closest(CARD_HOSTS) || btn).after(buildCard(btn.dataset.key));
  }

  buttons.forEach(function (b) {
    b.addEventListener("click", function () { select(b); });
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && openBtn) {
      var b = openBtn;
      close();
      b.focus();
    }
  });

  }   /* end render */

  /* --- entry point ------------------------------------------------ */

  function fail(message) {
    var head = document.querySelector(".lesson-head");
    head.appendChild(el("h2", null, "Chapter not found"));
    head.appendChild(el("p", "en", message));
  }

  var slug = KIIP.requested();
  if (!slug) {
    fail("No chapter was named in the address. Pick one from the chapter list.");
  } else if (!/^[a-z0-9-]+$/.test(slug)) {
    fail("“" + slug + "” is not a chapter name.");
  } else {
    KIIP.need(slug, "lessons/", function (lesson) {
      if (lesson) render(lesson);
      else fail("No chapter is filed under “" + slug + "”.");
    });
  }
})();
