/* Landing page: the book's own contents, part by part, filterable by topic.

   Every chapter the book has is listed, whether or not it has been built —
   an unbuilt one shows what it covers and where it is in the book, so the
   contents read as the contents and not as a list of what happens to exist.
   The two questions under each title are the book's own 본문 headings. */

(function () {
  var built = (window.KIIP ? KIIP.all() : []) || [];
  var book = (window.KIIP ? KIIP.book() : null) || { parts: [] };

  var listEl = document.querySelector("[data-list]");
  var emptyEl = document.querySelector("[data-empty]");
  var filtersEl = document.querySelector("[data-filters]");
  var progressEl = document.querySelector("[data-progress]");
  var active = null;

  var byNumber = {};
  built.forEach(function (l) { byNumber[l.number] = l; });

  /* Without contents to go on, fall back to whatever is built, as one part.
     That is the state of a checkout that carries only the site. */
  var parts = book.parts.length ? book.parts : [{
    chapters: built.map(function (l) {
      return { number: l.number, title: l.title, articles: [], built: true };
    })
  }];

  var total = parts.reduce(function (n, p) { return n + p.chapters.length; }, 0);

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }

  /* --- topic filter ----------------------------------------------- */

  var tags = [];
  built.forEach(function (l) {
    (l.tags || []).forEach(function (t) {
      if (tags.indexOf(t) === -1) tags.push(t);
    });
  });

  tags.forEach(function (t) {
    var b = el("button", "tag", t);
    b.type = "button";
    b.setAttribute("aria-pressed", "false");
    b.addEventListener("click", function () {
      active = active === t ? null : t;
      filtersEl.querySelectorAll(".tag").forEach(function (x) {
        x.setAttribute("aria-pressed", String(x.textContent === active));
      });
      render();
    });
    filtersEl.appendChild(b);
  });

  /* --- rows -------------------------------------------------------- */

  function chapterRow(c) {
    var lesson = byNumber[c.number];
    var row = el(lesson ? "a" : "div", "entry" + (lesson ? "" : " is-pending"));
    if (lesson) row.href = "lesson.html?ch=" + encodeURIComponent(lesson.slug);

    row.appendChild(el("span", "num", String(c.number).padStart(2, "0")));

    var body = el("span", "body");
    var head = el("span", "head");
    head.appendChild(el("span", "ko", c.title));
    if (lesson && lesson.titleEn) head.appendChild(el("span", "en", lesson.titleEn));
    body.appendChild(head);

    (c.articles || []).forEach(function (q) {
      body.appendChild(el("span", "question", q));
    });

    if (lesson && lesson.tags && lesson.tags.length) {
      var tagWrap = el("span", "tags");
      lesson.tags.forEach(function (t) { tagWrap.appendChild(el("span", null, t)); });
      body.appendChild(tagWrap);
    }
    row.appendChild(body);

    if (c.page) row.appendChild(el("span", "page", "p. " + c.page));
    return row;
  }

  function render() {
    listEl.replaceChildren();
    var shown = 0;

    parts.forEach(function (part) {
      var keep = part.chapters.filter(function (c) {
        if (!active) return true;
        var lesson = byNumber[c.number];
        return lesson && (lesson.tags || []).indexOf(active) !== -1;
      });
      if (!keep.length) return;
      shown += keep.length;

      var sec = el("section", "part");
      if (part.title) {
        var head = el("header", "part-head");
        head.appendChild(el("span", "part-num", "제" + part.number + "편"));
        head.appendChild(el("h2", "part-name", part.title));
        if (part.titleEn) head.appendChild(el("span", "part-en", part.titleEn));
        sec.appendChild(head);
      }
      var rows = el("div", "entries");
      keep.forEach(function (c) { rows.appendChild(chapterRow(c)); });
      sec.appendChild(rows);
      listEl.appendChild(sec);
    });

    if (progressEl) {
      progressEl.textContent = active
        ? shown + (shown === 1 ? " chapter" : " chapters") + " on ‘" + active + "’"
        : built.length + " of " + total + " chapters written up";
    }

    emptyEl.textContent = total === 0
      ? "No chapters yet. Run the build to generate them."
      : "No chapters match that topic.";
    emptyEl.hidden = shown > 0;
  }

  render();
})();
