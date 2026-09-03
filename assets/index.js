/* Landing page: the book's own contents, part by part.

   Every chapter the book has is listed, whether or not it has been built —
   an unbuilt one shows what it covers and where it is in the book, so the
   contents read as the contents and not as a list of what happens to exist.
   The two questions under each title are the book's own 본문 headings.

   The parts are the only grouping. Each carries its number as data, and the
   stylesheet gives it the colour the book prints it in. */

(function () {
  var built = (window.KIIP ? KIIP.all() : []) || [];
  var book = (window.KIIP ? KIIP.book() : null) || { parts: [] };

  var listEl = document.querySelector("[data-list]");
  var emptyEl = document.querySelector("[data-empty]");
  var progressEl = document.querySelector("[data-progress]");

  var byNumber = {};
  built.forEach(function (l) { byNumber[l.number] = l; });

  /* Without contents to go on, fall back to whatever is built, as one part.
     That is the state of a checkout that carries only the site. */
  var parts = book.parts.length ? book.parts : [{
    chapters: built.map(function (l) {
      return { number: l.number, title: l.title, articles: [] };
    })
  }];

  var total = parts.reduce(function (n, p) { return n + p.chapters.length; }, 0);

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }

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
    row.appendChild(body);

    if (c.page) row.appendChild(el("span", "page", "p. " + c.page));
    return row;
  }

  var sections = 0;
  parts.forEach(function (part) {
    if (!part.chapters.length) return;
    sections += 1;

    var sec = el("section", "part");
    if (part.number) sec.dataset.part = String(part.number);

    if (part.title) {
      var head = el("header", "part-head");
      var chip = el("span", "part-chip");
      chip.appendChild(el("span", "part-num", "제" + part.number + "편"));
      chip.appendChild(el("h2", "part-name", part.title));
      head.appendChild(chip);
      if (part.titleEn) head.appendChild(el("span", "part-en", part.titleEn));
      sec.appendChild(head);
    }

    var rows = el("div", "entries");
    part.chapters.forEach(function (c) { rows.appendChild(chapterRow(c)); });
    sec.appendChild(rows);
    listEl.appendChild(sec);
  });

  if (progressEl) {
    progressEl.textContent =
      built.length + " of " + total + " chapters written up";
  }

  emptyEl.textContent = "No chapters yet. Run the build to generate them.";
  emptyEl.hidden = sections > 0;
})();
