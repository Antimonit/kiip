/* Landing page: lessons in textbook order, filterable by topic tag. */

(function () {
  var lessons = (window.KIIP ? KIIP.all() : []) || [];
  var listEl = document.querySelector("[data-list]");
  var emptyEl = document.querySelector("[data-empty]");
  var filtersEl = document.querySelector("[data-filters]");
  var active = null;

  var tags = [];
  lessons.forEach(function (l) {
    (l.tags || []).forEach(function (t) {
      if (tags.indexOf(t) === -1) tags.push(t);
    });
  });

  tags.forEach(function (t) {
    var b = document.createElement("button");
    b.className = "tag";
    b.type = "button";
    b.textContent = t;
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

  function render() {
    listEl.replaceChildren();
    var shown = lessons.filter(function (l) {
      return !active || (l.tags || []).indexOf(active) !== -1;
    });

    shown.forEach(function (l) {
      var li = document.createElement("li");
      var a = document.createElement("a");
      a.href = "lesson.html?ch=" + encodeURIComponent(l.slug);

      var num = document.createElement("span");
      num.className = "num";
      num.textContent = String(l.number).padStart(2, "0");

      var body = document.createElement("span");
      var ko = document.createElement("span");
      ko.className = "ko";
      ko.textContent = l.title;
      var en = document.createElement("span");
      en.className = "en";
      en.textContent = l.titleEn;
      body.appendChild(ko);
      body.appendChild(document.createElement("br"));
      body.appendChild(en);

      a.appendChild(num);
      a.appendChild(body);

      if (l.tags && l.tags.length) {
        var tagWrap = document.createElement("span");
        tagWrap.className = "tags";
        l.tags.forEach(function (t) {
          var s = document.createElement("span");
          s.textContent = t;
          tagWrap.appendChild(s);
        });
        a.appendChild(tagWrap);
      }

      li.appendChild(a);
      listEl.appendChild(li);
    });

    emptyEl.textContent = lessons.length === 0
      ? "No chapters yet. Run the build to generate them."
      : "No chapters match that topic.";
    emptyEl.hidden = shown.length > 0;
  }

  render();
})();
