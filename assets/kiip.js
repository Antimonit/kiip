/* ------------------------------------------------------------------
   Content registry.

   Chapter files call KIIP.chapter({...}), the manifest calls
   KIIP.manifest([...]) and the book's own contents call KIIP.contents({...}),
   so the content files hold a pure data payload and nothing mutable is
   exposed for them to clobber.

   Chapters are loaded by appending a script tag rather than fetching,
   because fetch() is blocked on file:// and the site is meant to work
   by opening index.html directly.
   ------------------------------------------------------------------ */

window.KIIP = (function () {
  var chapters = {};
  var list = [];
  var book = { parts: [], back: [] };
  var pending = {};

  return {
    /* --- shared by the pages ------------------------------------ */

    /* Both pages build their markup the same way, from the same three
       arguments; there is no reason for two copies of it. */
    el: function (tag, cls, text) {
      var n = document.createElement(tag);
      if (cls) n.className = cls;
      if (text != null) n.textContent = text;
      return n;
    },

    /* --- called by the content files ---------------------------- */

    chapter: function (data) {
      chapters[data.slug] = data;
      var waiting = pending[data.slug] || [];
      delete pending[data.slug];
      waiting.forEach(function (cb) { cb(data); });
    },

    manifest: function (entries) {
      list = entries || [];
    },

    contents: function (data) {
      book = data || { parts: [], back: [] };
    },

    /* --- called by the pages ------------------------------------ */

    all: function () {
      return list;
    },

    /* The book's own contents: every chapter it has, built or not. */
    book: function () {
      return book;
    },

    /* Hand `slug`'s data to `done`, loading it first if needed.
       `done` receives null if the chapter cannot be loaded. */
    need: function (slug, base, done) {
      if (chapters[slug]) return done(chapters[slug]);

      if (pending[slug]) {
        pending[slug].push(done);
        return;
      }
      pending[slug] = [done];

      var s = document.createElement("script");
      s.src = base + slug + ".js";
      s.onerror = function () {
        var waiting = pending[slug] || [];
        delete pending[slug];
        waiting.forEach(function (cb) { cb(null); });
      };
      document.head.appendChild(s);
    },

    /* The chapter a URL asks for: ?ch=<slug>, or #<slug> as a fallback
       for contexts where the query string is dropped. */
    requested: function () {
      var m = /[?&]ch=([^&#]+)/.exec(window.location.search);
      if (m) return decodeURIComponent(m[1]);
      var hash = window.location.hash.replace(/^#\/?/, "");
      return hash ? decodeURIComponent(hash) : null;
    }
  };
})();
