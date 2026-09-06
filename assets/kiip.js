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
  var THEME = "kiip-theme";
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

    /* The reader's light/dark choice, remembered in this browser. With
       nothing chosen the page follows the system, which is what the palette
       does on its own; choosing stamps data-theme on <html> and the
       light-dark() colours follow. Storage can throw — a private window, or
       a browser set to block site data — so every touch of it is guarded and
       the page simply falls back to the system setting. */
    theme: {
      chosen: function () {
        try { return localStorage.getItem(THEME); } catch (e) { return null; }
      },

      /* What is actually on screen, whether chosen or inherited. */
      showing: function () {
        var set = this.chosen();
        if (set) return set;
        return window.matchMedia
          && window.matchMedia("(prefers-color-scheme: dark)").matches
            ? "dark" : "light";
      },

      apply: function (name) {
        if (name) document.documentElement.setAttribute("data-theme", name);
        else document.documentElement.removeAttribute("data-theme");
        try {
          if (name) localStorage.setItem(THEME, name);
          else localStorage.removeItem(THEME);
        } catch (e) { /* nothing to remember it in; this page still turns */ }
      },

      /* The button both pages carry, at the end of the masthead. It names
         the theme it would switch to, so the label is the action. */
      button: function () {
        var self = this;
        var b = document.createElement("button");
        b.className = "theme";
        b.type = "button";

        function label() {
          var next = self.showing() === "dark" ? "light" : "dark";
          b.textContent = next === "dark" ? "☾ Dark" : "☀ Light";
          b.setAttribute("aria-label", "Switch to the " + next + " theme");
        }

        b.addEventListener("click", function () {
          self.apply(self.showing() === "dark" ? "light" : "dark");
          label();
        });

        /* the system changing under an unchosen page relabels the button */
        if (window.matchMedia) {
          var mq = window.matchMedia("(prefers-color-scheme: dark)");
          var watch = function () { if (!self.chosen()) label(); };
          if (mq.addEventListener) mq.addEventListener("change", watch);
          else if (mq.addListener) mq.addListener(watch);
        }

        label();
        return b;
      },

      /* Both pages call this once, and the masthead is the same on both. */
      mount: function () {
        var head = document.querySelector(".masthead");
        if (head) head.appendChild(this.button());
      }
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
