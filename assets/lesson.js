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
  head.appendChild(el("p", "en", lesson.titleEn));

  /* --- annotation buttons ---------------------------------------- */

  var buttons = [];

  function annoButton(seg) {
    var key = seg.a || seg.w;
    var b = el("button", "anno", seg.w);
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
    if (a.meaning) hw.appendChild(document.createTextNode(" — " + a.meaning));
    card.appendChild(hw);

    (a.hanjaList || []).forEach(function (h) {
      var line = el("p", "hanja");
      line.appendChild(el("b", null, h.read ? h.read + "(" + h.char + ")" : h.char));
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
    if (b.topic) header.appendChild(el("p", "sect-topic", b.topic));
    sec.appendChild(header);
    docEl.appendChild(sec);
    host = sec;
    if (b.trans) host.appendChild(translationBlock(b.trans));
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
    switch (b.t) {
      case "section":
        openSection(b);
        return;

      case "heading": {
        host.appendChild(el(b.level <= 2 ? "h4" : "h5",
                            "sub-title sub-level-" + b.level, b.text));
        if (b.trans) host.appendChild(translationBlock(b.trans));
        return;
      }

      case "p": {
        var cls = "ko-para" + (b.role ? " is-" + b.role : "");
        host.appendChild(fillSpans(el("p", cls), b.s));
        if (b.trans) host.appendChild(translationBlock(b.trans));
        return;
      }

      case "bullet": {
        var li = fillSpans(el("li", "ko-bullet"), b.s);
        var prev = host.lastElementChild;
        if (!prev || prev.tagName !== "UL") {
          prev = el("ul", "ko-list");
          host.appendChild(prev);
        }
        prev.appendChild(li);
        return;
      }

      case "gloss": {
        var box = el("div", "glossbox");
        b.items.forEach(function (it) {
          var row = el("div", "gloss-row");
          var term = el("div", "gloss-term");
          if (it.a) {
            term.appendChild(annoButton({ w: it.term, a: it.a }));
          } else {
            term.appendChild(document.createTextNode(it.term));
          }
          if (it.en) term.appendChild(el("span", "gloss-en", " " + it.en));
          row.appendChild(term);
          row.appendChild(fillSpans(el("div", "gloss-def"), it.def));
          box.appendChild(row);
        });
        host.appendChild(box);
        return;
      }

      case "table": {
        var wrapEl = el("div", "table-wrap");
        var t = el("table");
        if (b.head) {
          var thead = el("thead");
          var tr = el("tr");
          b.head.forEach(function (c) {
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

  if (lesson.chapterGloss && lesson.chapterGloss.length) {
    var first = docEl.querySelector("section");
    var box2 = el("div", "glossbox");
    lesson.chapterGloss.forEach(function (key) {
      var a = lesson.annotations[key] || {};
      var row = el("div", "gloss-row");
      var term = el("div", "gloss-term");
      term.appendChild(annoButton({ w: key, a: key }));
      row.appendChild(term);
      row.appendChild(el("div", "gloss-def", a.meaning || ""));
      box2.appendChild(row);
    });
    if (first) docEl.insertBefore(box2, first);
  }

  /* --- transcription notes ---------------------------------------- */

  if (lesson.notes && lesson.notes.length) {
    var sec = el("section", "sect sect-notes");
    sec.appendChild(el("h3", "sect-title", "Transcription notes"));
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
