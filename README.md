# KIIP Level 5 — study notes

Static reading notes for the KIIP (사회통합프로그램) Level 5 textbook. Each chapter
page carries the Korean text, the textbook's own margin glossary, English
translations where they exist, and inline annotations that break down key words
and their hanja. Clicking an annotated word opens its breakdown directly beneath
the block it sits in; clicking it again, or pressing Escape, closes it.

Live at <https://antimonit.github.io/kiip/>.

## Branches

The site and the content are kept apart:

- **`master`** — the site, the tooling and the design. Everything here is
  chapter-agnostic. It builds and passes its own checks with no chapters
  present at all.
- **`content`** — the chapters, branched off `master`. One editorial module per
  chapter under `tools/chapters/`, plus the data files generated from them.

`content` is rebased onto `master` when the site changes. Because no chapter is
named anywhere in `master`, and no styling decision is recorded in the generated
data, the two rarely touch the same lines.

## Running it

No build step and no dependencies. Open `index.html` directly, or serve the
folder:

```
python3 -m http.server
```

Chapters are addressed as `lesson.html?ch=<slug>` — one page for every chapter
rather than a copy of the same shell per chapter.

## Deployment

GitHub Pages serves the repository root of the deployed branch, so a push
publishes. `.nojekyll` keeps Pages from running Jekyll over the files.

## Where the content comes from

Chapters are transcribed from the textbook photos into Google Docs, with
vocabulary notes left as Docs comments. `tools/build.py` turns an HTML export of
such a doc into the chapter's data file, so a chapter is regenerated from its
source rather than edited by hand.

```
python3 tools/build.py ~/Downloads      # directory holding 1.html … 4.html
```

That writes `lessons/<slug>.js` for each chapter and `lessons/manifest.js`.

### The pipeline

`tools/parse_gdoc.py` reads the export. Two things survive it that the pipeline
depends on: heading and paragraph structure, and comment anchors — the commented
run is left as its own `<span>` immediately before the `[a]` superscript, which
is how each comment is tied back to the word it annotates.

`tools/build.py` then:

- groups blocks into sections (생각해 봅시다, 학습목표, 관련 단원 확인하기, the
  numbered parts, 알아두면 좋아요, 주요 내용정리, 이야기 나누기);
- recognises the margin glossary — a term line followed by its definition;
- parses each comment into a headword, a hanja breakdown and usage notes,
  keyed by the word it is anchored to, merging multiple comments on one word;
- treats a long English comment left on a *heading* as a section translation
  rather than a word note, cutting it to the shape of the Korean paragraphs —
  and, where it divides differently but agrees sentence for sentence, cutting
  it again by sentence;
- falls back to the English written into the chapter under `english` when the
  Doc's translation does not answer the section paragraph for paragraph;
- attaches an annotation written under `extraAnnotations` to the first place
  its word is said — or to the margin-glossary term of the same name, where a
  page carries no comments at all — so an entry does not need a Docs comment
  to be reachable, and reports any entry nothing points at;
- marks a margin-glossary word where the article goes on to say it, so the
  textbook's own vocabulary is clickable in the prose and not only in the
  margin. Running prose is searched first, then headings, then photo labels
  and margin notes, so a word is marked where it is read;
- applies the chapter's corrections and lists every one of them on the page.

A block that the Doc sets as ordinary text can be given its real part by
`roles`, keyed by a `(first, last)` range of source block indices:
`join` folds a paragraph the Doc broke in two back into the one before it,
`heading` and `heading4` promote a line, `labels`, `margin`, `figure`,
`source`, `verse`, `chart`, `table2`, `sublist` and `kinship` name what a
group of lines really is, and `drop` removes a line the page does not have.
`sublist` reads a group as a two-level list, the Doc's plain lines becoming
the outer items and its list items the inner ones — which is how a page that
draws a bracket is set here.

### Adding a chapter

1. Export the Doc as HTML, and put the page photos in `source/<slug>/`.
2. Add `tools/chapters/chNN_slug.py` defining one `CHAPTER` dict. `src`,
   `number`, `slug`, `unit`, `title`, `titleEn`, `tags` are enough to start;
   modules are discovered automatically and ordered by chapter number.
3. Run the build, read the page, and add `fixes`, `headwords` and `roles`
   entries until it reads correctly. Every fix is reported on the page, and the
   build warns about fixes that never matched anything.

Where a Doc does not cover the whole chapter, `insert` and `append` add blocks
transcribed straight from the photos — `insert` by source block index, `append`
at the end — and `extraAnnotations` supplies entries for words those blocks
introduce. Both use the `P` / `B` / `H` / `SECT` / `LABELS` helpers, in whose
text `{word}` marks an annotation and `{surface|headword}` files one under a
different headword. `LABELS` takes `GROUP(name, *labels)` in place of plain
labels where the page sorts its pictures into named kinds, and the grouping
survives into the data rather than being flattened into a row of chips.

### Corrections

Nothing is silently rewritten. Each entry in a chapter's `fixes` list is an
`(old, new, why)` triple — optionally with a fourth element giving the pair to
display — and each one that fires is listed under "Transcription notes" at the
foot of that chapter's page.

Fixes are content, and they are meant to be temporary: each is there to be
checked against the page photos and then retired by correcting the
transcription upstream. **A chapter with an empty `fixes` list is a finished
chapter.** Two mechanics are worth knowing while they are still there:

- The export splits runs mid-phrase, so corrections are applied *after* the
  spans are assembled. A section heading is the exception: a section is
  recognised by its heading, so a slip there is corrected before the name is
  looked up.
- A fix written as `"=word"` must match a whole string exactly, which is how a
  single annotated word gets corrected without touching the same characters
  elsewhere.

## Data and presentation

`lessons/<slug>.js` is data. It says what each block *is* — a paragraph, a
glossary, a section of kind `aside` — and never how it looks. There is no markup
in it, no HTML tag names as block types, and no styling hints. So a design
change is a CSS change, and re-skinning the site does not mean regenerating 50
chapters.

Each file is one `KIIP.chapter({...})` call wrapping a pure JSON payload. The
call rather than a global assignment means nothing mutable is exposed, and the
script tag rather than `fetch()` means the site still works over `file://`.

Three consequences worth knowing:

- Headings carry a `level`, and `assets/lesson.js` chooses the element.
- Corrections are `{was, now, why, count}` objects, and the page formats them.
- Where the textbook prints a label and then the section's subject beside it
  (알아두면 좋아요, 이야기 나누기), the builder folds that heading into the
  section as its `topic`. The renderer emits the same header shape for every
  section; CSS decides whether the two sit on one line.

### The section system

`assets/style.css` has two layers, and the boundary is enforced by a check:

1. A **section kind** declares how dense and prominent its contents are, as
   custom properties — `--scale`, `--aux-scale`, `--lead`, `--flow`, and the
   chrome and heading tokens. It never mentions a block type.
2. A **block component** sizes itself from those properties and never mentions
   a section.

Custom properties inherit, so one declaration on a section retunes everything
inside it. Adding a section kind is one rule listing what differs from the
defaults on `.sect`, however many block types it contains.

## Checking it

`tools/smoke.js` renders every page in jsdom, clicks every annotation, and fails
if any of them has no card or an empty card, if a page leaves `undefined` in the
output, or if a bad address renders a blank page instead of an explanation. It
also lints the two boundaries above — markup or tag names in the generated data,
and section kinds sizing block types directly. It passes with no chapters
present, which is the state of `master`. It needs jsdom, which the site does
not:

```
npm install jsdom && node tools/smoke.js
```

## Layout

```
index.html              chapter list, filterable by topic tag
lesson.html             one page for every chapter: lesson.html?ch=<slug>
assets/style.css        all appearance
assets/kiip.js          content registry and loader
assets/index.js         renders the chapter list
assets/lesson.js        renders a chapter
tools/parse_gdoc.py     Google Docs HTML export -> blocks + comments
tools/build.py          the generator
tools/smoke.js          render check and boundary lints
tools/chapters/
  __init__.py           registry, and the helpers chapter modules use
  chNN_slug.py          one editorial module per chapter        (content)
lessons/
  manifest.js           generated chapter list                  (content)
  <slug>.js             generated chapter data                  (content)
source/<slug>/          original page photos (gitignored)
```
