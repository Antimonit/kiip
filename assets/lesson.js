/* ------------------------------------------------------------------
   Renders a lesson from the LESSON object in lessons/<slug>/lesson.js.
   No build step: plain script tags, works over file:// as well as http.
   ------------------------------------------------------------------ */

(function () {
  var el = KIIP.el;

  KIIP.theme.mount();

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

  var cardId = "anno-card";        // there is one card, so one id will do

  function annoButton(seg) {
    var key = seg.annotation || seg.word;
    var b = el("button", "anno" + (glossed[key] ? " is-glossed" : ""), seg.word);
    b.type = "button";
    b.dataset.key = key;
    b.setAttribute("aria-expanded", "false");
    b.setAttribute("aria-controls", cardId);
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
    var card = el("div", "anno-card" + (glossed[key] ? " is-glossed" : ""));
    /* a region of its own, named for the word, so a screen reader announces
       what has just appeared and can be told to jump to it */
    card.id = cardId;
    card.setAttribute("role", "region");
    card.setAttribute("aria-label", ((a && a.headword) || key) + " — explanation");
    card.tabIndex = -1;
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

  /* The Korean and its English, sentence by sentence where they divide the
     same way and as one row where they do not. */
  function paired(b) {
    var pair = el("div", "para-pair" + (b.role ? " is-" + b.role : ""));
    var units = b.sentences || [{ spans: b.spans, translation: b.translation }];
    units.forEach(function (unit) {
      var row = el("div", "row");
      var ko = fillSpans(el("span", "ko"), unit.spans);
      ko.appendChild(document.createTextNode(" "));
      row.appendChild(ko);
      row.appendChild(el("span", "en", unit.translation));
      pair.appendChild(row);
    });
    return pair;
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
         row into two columns. One structure, two layouts. A list item is
         translated the same way, which is why this is a function. */
      case "paragraph": {
        if (!b.translation) {
          host.appendChild(fillSpans(
            el("p", "ko-para" + (b.role ? " is-" + b.role : "")), b.spans));
          return;
        }
        host.appendChild(paired(b));
        return;
      }

      case "bullet": {
        var wanted = b.ordered ? "OL" : "UL";
        var list = host.lastElementChild;
        if (!list || list.tagName !== wanted) {
          list = el(b.ordered ? "ol" : "ul", "ko-list");
          host.appendChild(list);
        }
        var item = el("li", "ko-bullet");
        if (b.translation) item.appendChild(paired(b));
        else fillSpans(item, b.spans);
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
        /* A cell is plain text, or spans where the book marks a word in
           it — the 법률 제정 / 집행 / 적용 column of chapter 20's table. */
        function cell(tag, c) {
          var n = el(tag, null,
                     typeof c === "string" ? c : (c.spans ? null : c.text));
          if (typeof c !== "string" && c.spans) fillSpans(n, c.spans);
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

      /* Bars run from a zero line, which is at the left edge until a value
         falls below it — 그리스 at -0.3% in chapter 25 — and then moves in far
         enough for the negative ones to run backwards from it. */
      case "chart": {
        var fig = el("figure", "chart");
        var values = b.rows.map(function (r) { return r[1]; });
        var top = Math.max.apply(null, values.concat(0));
        var base = Math.min.apply(null, values.concat(0));
        var span = top - base;
        var zero = span ? (-base / span) * 100 : 0;

        b.rows.forEach(function (r) {
          var row = el("div", "bar-row");
          row.appendChild(el("span", "bar-label", r[0]));
          var track = el("span", "bar-track");
          var fill = el("span", "bar-fill" + (r[1] < 0 ? " is-below" : ""));
          var size = span ? Math.abs(r[1]) / span * 100 : 0;
          fill.style.width = size + "%";
          fill.style.left = (r[1] < 0 ? zero - size : zero) + "%";
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
        b.lines.forEach(function (l, k) {
          var en = b.translations && b.translations[k];
          if (!en) {
            v.appendChild(fillSpans(el("p"), l));
            return;
          }
          v.appendChild(paired({
            spans: l,
            translation: en,
            sentences: b.sentences && b.sentences[k]
          }));
        });
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
     An article is everything under one heading: its prose, the lists and
     the quoted boxes in it, and the question it closes with. They are
     turned over together, because they are one piece of reading — 이야기
     나누기 in chapter 28 is an article, a case study, a list of five rules
     and a question, and it took nine buttons before this. A heading starts
     the next article; a section that has none is one article. */

  function runs() {
    var found = [];
    docEl.querySelectorAll(".sect").forEach(function (sec) {
      var group = null;
      Array.prototype.forEach.call(sec.children, function (block) {
        if (/^H[1-6]$/.test(block.tagName)) {
          group = null;                       // the next article starts here
          return;
        }
        var pairs = block.classList.contains("para-pair")
          ? [block]
          : Array.prototype.slice.call(block.querySelectorAll(".para-pair"));
        if (!pairs.length) return;
        if (!group) {
          group = { at: block, pairs: [] };
          found.push(group);
        }
        group.pairs = group.pairs.concat(pairs);
      });
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

  runs().forEach(function (group) {
    var b = el("button", "split-toggle", "Side by side");
    b.type = "button";
    b.setAttribute("aria-pressed", "false");
    b.addEventListener("click", function () {
      close(true);      // it sits in a row whose height is about to be read
      setSplit(group.pairs, b, b.getAttribute("aria-pressed") !== "true");
    });
    group.at.parentNode.insertBefore(b, group.at);
  });

  /* --- interaction ------------------------------------------------ */

  /* One card is open at a time; it drops in after the block the word sits in. */

  var CARD_HOSTS = ".para-pair, .ko-para, .ko-list, .gloss-row, .sub-title," +
                   " .sect-title, .aside-topic, .verse, .labels, .margin-note";
  var openBtn = null;
  var card = null;              // the open one, if any
  var CARD_MS = 220;            // must match the transition in style.css

  /* A card is not there and then it is, which on a long page reads as the
     text having jumped. So it grows out of the line it belongs to and folds
     back into it. Two things make that harder than it sounds.

     Height is driven from here and only from here: an inline height outranks
     a class, so a class that sets height 0 would be ignored and the card
     would refuse to fold. The class carries the rest of the closed state.

     And a closed card still parts the margins around it. Margins of adjacent
     blocks collapse to the larger of the two, but not across a box that has
     content in it — so a card folded to nothing still holds a paragraph and
     the heading below it apart, and removing it lets them snap together.
     slack() measures what that snap would be and the closed state carries it
     as a negative margin, so a folded card and no card at all take up the
     same room. */
  function measure(el) {
    return el.getBoundingClientRect().height;
  }

  function slack(el) {
    var above = el.previousElementSibling, below = el.nextElementSibling;
    var a = above ? parseFloat(getComputedStyle(above).marginBottom) : 0;
    var b = below ? parseFloat(getComputedStyle(below).marginTop) : 0;
    return Math.min(a || 0, b || 0);
  }

  /* Set a starting state without animating into it. Going from `auto` to a
     number is the one step that must not be animated: an engine that can
     interpolate it starts a transition of its own, and the real one then
     interrupts it half way — which looked like the card jumping to half its
     height and growing from there. */
  function frozen(el, set) {
    el.style.transition = "none";
    set();
    void el.offsetHeight;
    el.style.transition = "";
  }

  /* Animate to a height from wherever the element is now, then finish on the
     transition rather than on the clock: a timer that fires a frame early
     cuts the last of the movement off, which is seen as a jump. The clock
     stays as a fallback for a transition that never runs. */
  function toHeight(el, h, then) {
    window.clearTimeout(el.timer);
    if (el.ending) el.removeEventListener("transitionend", el.ending);
    var done = function (e) {
      if (e && e.propertyName !== "height") return;
      el.removeEventListener("transitionend", done);
      window.clearTimeout(el.timer);
      el.ending = null;
      if (then) then();
      else el.style.height = "";        // auto, so it can rewrap
    };
    el.ending = done;
    el.addEventListener("transitionend", done);
    el.timer = window.setTimeout(done, CARD_MS + 80);
    el.style.height = h + "px";
  }

  function shut(el) {
    el.classList.add("is-collapsed");
    el.style.marginTop = -slack(el) + "px";
  }

  function open(host, key) {
    var fresh = buildCard(key);
    var stale = host.nextElementSibling;  // one still folding away here
    if (stale && stale.classList.contains("anno-card")) stale.remove();

    card = fresh;
    host.after(card);
    if (still()) return;
    var full = measure(card);
    frozen(card, function () {
      shut(card);
      card.style.height = "0px";
    });
    card.classList.remove("is-collapsed");
    card.style.marginTop = "";
    toHeight(card, full);
  }

  /* Another word in the same place only changes what the card says, so the
     card stays where it is and resizes. Another word somewhere else is
     somewhere else: that card folds away where it stands and a new one grows
     where the word is. */
  function fill(host, key) {
    if (!card || card.previousElementSibling !== host) {
      if (card) {                       // fold it where it stands; the button
        var going = card;               // state belongs to the new card now
        card = null;
        foldAway(going);
      }
      return open(host, key);
    }
    var fresh = buildCard(key);
    var from = measure(card);
    card.classList.toggle("is-glossed", fresh.classList.contains("is-glossed"));
    while (card.firstChild) card.removeChild(card.firstChild);
    while (fresh.firstChild) card.appendChild(fresh.firstChild);
    if (still()) return;
    var to;
    frozen(card, function () {
      card.style.height = "auto";
      to = measure(card);
      card.style.height = from + "px";
    });
    toHeight(card, to);
  }

  function foldAway(el, atOnce) {
    el.removeAttribute("id");         // it is no longer the one being pointed at
    if (atOnce || still()) {
      window.clearTimeout(el.timer);
      return el.remove();
    }
    frozen(el, function () {
      el.style.height = measure(el) + "px";
    });
    shut(el);
    toHeight(el, 0, function () { el.remove(); });
  }

  function close(atOnce) {
    if (card) {
      var going = card;
      card = null;
      foldAway(going, atOnce);
    }
    drop();
  }

  function drop() {
    buttons.forEach(function (b) { b.setAttribute("aria-expanded", "false"); });
    openBtn = null;
  }

  function select(btn) {
    if (btn === openBtn) return close();
    drop();
    openBtn = btn;
    btn.setAttribute("aria-expanded", "true");
    /* Side by side, a paragraph is a column of sentence rows and can run
       longer than a phone screen, so the card sits under the row the word is
       in rather than under the whole paragraph. */
    fill(btn.closest(".para-pair.is-split .row") ||
         btn.closest(CARD_HOSTS) || btn, btn.dataset.key);
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
