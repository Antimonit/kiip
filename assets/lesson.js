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

  document.title = lesson.number + ". " + lesson.title + " — KIIP 5";

  var head = document.querySelector(".lesson-head");
  head.appendChild(el("div", "eyebrow", "Chapter " + lesson.number + " · " + lesson.unit));
  head.appendChild(el("h2", null, lesson.title));
  head.appendChild(el("p", "en", lesson.titleEnglish));

  /* --- annotation buttons ---------------------------------------- */

  var buttons = [];

  function annoButton(seg) {
    var key = seg.annotation || seg.word;
    var b = el("button", "anno", seg.word);
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
    // with no meaning of its own, the note written beside the word stands in
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

    if (a.handwritten && a.meaning) {
      card.appendChild(el("p", "handwritten", a.handwritten));
    }

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
                   "sub-title sub-level-" + b.level, b.text);
        if (b.titleTranslation) h.appendChild(el("span", "en-title", b.titleTranslation));
        host.appendChild(h);
        if (b.translation) host.appendChild(translationBlock(b.translation));
        return;
      }

      /* A paragraph and its translation are one unit: the English follows
         the Korean it renders, rather than the whole section's English
         sitting in a block of its own. */
      case "paragraph": {
        var p = fillSpans(el("p", "ko-para" + (b.role ? " is-" + b.role : "")), b.spans);
        if (b.translation) {
          var pair = el("div", "para-pair");
          pair.appendChild(p);
          var wrap = el("div", "en-wrap");
          wrap.appendChild(el("p", "en-para", b.translation));
          pair.appendChild(wrap);
          host.appendChild(pair);
        } else {
          host.appendChild(p);
        }
        return;
      }

      case "bullet": {
        var li = fillSpans(el("li", "ko-bullet"), b.spans);
        var prev = host.lastElementChild;
        if (!prev || prev.tagName !== "UL") {
          prev = el("ul", "ko-list");
          host.appendChild(prev);
        }
        prev.appendChild(li);
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

      case "table": {
        var wrapEl = el("div", "table-wrap");
        var t = el("table");
        if (b.header) {
          var thead = el("thead");
          var tr = el("tr");
          b.header.forEach(function (c) {
            var th = el("th", null, typeof c === "string" ? c : c.text);
            if (c.span) th.colSpan = c.span;
            tr.appendChild(th);
          });
          thead.appendChild(tr);
          t.appendChild(thead);
        }
        var tb = el("tbody");
        b.rows.forEach(function (row) {
          var tr2 = el("tr");
          row.forEach(function (c) { tr2.appendChild(el("td", null, c)); });
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

      case "labels": {
        var lb = el("div", "labels");
        b.items.forEach(function (x) { lb.appendChild(fillSpans(el("span"), x)); });
        host.appendChild(lb);
        return;
      }

      case "figure":
        host.appendChild(el("p", "figure", b.text));
        return;

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
    var unchecked = lesson.notes.filter(function (n) { return !n.checked; }).length;
    var sec = el("section", "sect sect-notes");
    var header = el("header", "sect-head");
    header.appendChild(el("h3", "sect-title", "Transcription notes"));
    if (unchecked) {
      header.appendChild(el("p", "sect-topic",
        unchecked + (unchecked === 1 ? " still needs" : " still need") +
        " checking against the page"));
    }
    sec.appendChild(header);
    var ul = el("ul", "notes");
    lesson.notes.forEach(function (n) {
      var li = el("li", n.checked ? "is-checked" : "is-unchecked");
      if (n.was) {
        li.appendChild(el("span", "ko", n.was + " → " + n.now));
        li.appendChild(document.createTextNode(" — "));
      }
      li.appendChild(document.createTextNode(n.why));
      if (n.count > 1) {
        li.appendChild(el("span", "count", " (×" + n.count + ")"));
      }
      if (n.checked) li.appendChild(el("span", "checked", "checked"));
      ul.appendChild(li);
    });
    sec.appendChild(ul);
    docEl.appendChild(sec);
  }

  /* --- English: two granularities, for comparison ------------------
     PROTOTYPE. One of these is to be deleted once chosen.
       "article"    one control per article, revealing its whole run
       "paragraph"  one control per paragraph                        */

  var EN_MODE = "kiip-en-mode";
  var enMode = localStorage.getItem(EN_MODE) || "article";

  /* Runs of consecutive pairs — each run is the prose of one article. */
  function englishRuns() {
    var runs = [];
    docEl.querySelectorAll(".para-pair").forEach(function (pair) {
      var last = runs[runs.length - 1];
      if (last && last[last.length - 1].nextElementSibling === pair) last.push(pair);
      else runs.push([pair]);
    });
    return runs;
  }

  function fold(targets) {
    var b = el("button", "en-fold", "English");
    b.type = "button";
    b.setAttribute("aria-expanded", "false");
    targets.forEach(function (w) { w.classList.remove("is-open"); });
    b.addEventListener("click", function () {
      var show = !targets[0].classList.contains("is-open");
      targets.forEach(function (w) { w.classList.toggle("is-open", show); });
      b.setAttribute("aria-expanded", String(show));
    });
    return b;
  }

  var controls = document.querySelector("[data-en-controls]");
  var runs = englishRuns();

  if (controls && runs.length) {
    var modeBox = el("div", "mode-toggle");
    var modeButtons = [
      { mode: "article", label: "Per article" },
      { mode: "paragraph", label: "Per paragraph" }
    ].map(function (spec) {
      var b = el("button", null, spec.label);
      b.type = "button";
      b.dataset.mode = spec.mode;
      b.addEventListener("click", function () { applyEnMode(spec.mode); });
      modeBox.appendChild(b);
      return b;
    });

    controls.appendChild(el("span", "en-label", "English"));
    controls.appendChild(modeBox);

    var applyEnMode = function (mode) {
      enMode = mode;
      localStorage.setItem(EN_MODE, mode);
      docEl.querySelectorAll(".en-fold").forEach(function (b) { b.remove(); });

      runs.forEach(function (run) {
        if (mode === "article") {
          var all = run.map(function (p) { return p.querySelector(".en-wrap"); });
          run[0].parentNode.insertBefore(fold(all), run[0]);
        } else {
          run.forEach(function (pair) {
            var wrap = pair.querySelector(".en-wrap");
            pair.insertBefore(fold([wrap]), wrap);
          });
        }
      });

      modeButtons.forEach(function (b) {
        b.setAttribute("aria-pressed", String(b.dataset.mode === mode));
      });
    };

    applyEnMode(enMode);
  }

  /* --- interaction ------------------------------------------------ */

  /* One card is open at a time; it drops in after the block the word sits in. */

  var CARD_HOSTS = ".ko-para, .ko-list, .gloss-row, .sub-title, .sect-title," +
                   " .aside-topic, .verse, .labels, .margin-note";
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
