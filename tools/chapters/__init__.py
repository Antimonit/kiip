# -*- coding: utf-8 -*-
"""Chapter registry and the helpers chapter modules are written with.

One module per chapter, named `chNN_slug.py`, each defining a single
`CHAPTER` dict. A chapter carries its text itself: `blocks` for text that came
from a Google Doc, written into the module by tools/convert.py, and `append`
for text transcribed straight from the page photos. A chapter that still names
a Doc in `src` is read from the HTML export instead, which is where chapters
1-4 stand until they are converted too. Modules are discovered automatically
and ordered by chapter number, so adding a chapter means adding a file and
nothing else.

`blocks` arrives before correction, exactly as the Doc had it, so `fixes` and
`approved` reach it and a correction can still be reviewed against the page
and then retired. `append` is transcribed from the page, so it skips the
corrections. `annotations` holds the entries the Doc's comments carried, in
the same shape as `extraAnnotations`, and is likewise still under correction.

Everything in a chapter module is content: its title, its
transcription corrections, the dictionary forms of words that appear
inflected, and any blocks transcribed from the page photos. Nothing here
describes appearance — blocks say what a thing is, and assets/style.css
decides how it looks.

`english` holds translations written by hand, keyed by the heading of the
article they translate: {"title": "...", "paragraphs": [...]} with one
paragraph per Korean paragraph. Chapters transcribed from the Doc may already
carry translations as comments on their headings; this is for the rest.

`fixes` are deliberately per-chapter and deliberately visible: each one is
listed on the page it applies to, and each is meant to be reviewed against
the photos and then retired by correcting the transcription upstream. A
chapter with an empty `fixes` list is a finished chapter.
"""

import importlib
import pkgutil
import re


# --- helpers for writing chapter content ------------------------------
#
# In the text of these helpers, {word} marks an annotation and
# {surface|headword} marks one whose entry is filed under a different
# headword.

def _spans(text):
    out = []
    for part in re.split(r"(\{[^}]*\})", text):
        if not part:
            continue
        if part.startswith("{"):
            surface, _, key = part[1:-1].partition("|")
            out.append({"word": surface, "annotation": key or surface})
        else:
            out.append(part)
    return out


def SECTION(kind, text):
    """A section of the given kind — see SPECIAL in tools/build.py."""
    return {"type": "section", "kind": kind, "text": text}


def HEADING(level, text, translation=None):
    """A heading. `translation` is the English written beside it."""
    block = {"type": "heading", "level": level, "text": text}
    if translation:
        block["translation"] = translation
    return block


def PARAGRAPH(text, translation=None):
    """A paragraph. A ★ opens the question a section closes with."""
    block = {"type": "paragraph", "spans": _spans(text)}
    if text.startswith("\u2605"):
        block["role"] = "prompt"
    if translation:
        block["translation"] = translation
    return block


def BULLET(text, ordered=False, level=1):
    """A list item. level=2 nests it under the item before it."""
    item = {"type": "bullet", "spans": _spans(text)}
    if ordered:
        item["ordered"] = True
    if level != 1:
        item["level"] = level
    return item


def SOURCE(text):
    """A source or citation line."""
    return {"type": "source", "text": text}


def LABELS(*texts):
    """Short labels printed on a photo or diagram.

    Pass GROUP(...) instead of plain text where the page sorts the pictures
    into named kinds, and the labels keep that grouping.
    """
    if texts and isinstance(texts[0], dict):
        return {"type": "labels", "groups": list(texts)}
    return {"type": "labels", "items": [_spans(t) for t in texts]}


def GROUP(name, *texts):
    """Labels that the page gathers under one heading."""
    return {"name": _spans(name), "items": [_spans(t) for t in texts]}


def MARGIN(*texts):
    """Something written in the margin of the page by hand."""
    return {"type": "margin", "items": [_spans(t) for t in texts]}


def VERSE(*lines):
    """A quoted text set line by line — an anthem, an article of the law."""
    return {"type": "verse", "lines": [_spans(t) for t in lines]}


def FIGURE(caption):
    """A photo on the page, which is not reproduced."""
    return {"type": "figure", "text": caption}


def TABLE(header, rows=None):
    """A table. Called with one argument when the book prints no header row."""
    if rows is None:
        return {"type": "table", "rows": [list(r) for r in header]}
    return {"type": "table", "header": list(header),
            "rows": [list(r) for r in rows]}


def CELL(text, columns=None, down=None):
    """A cell printed across more than one column, or down more than one row.

    The book merges cells both ways: 영역 sits across two columns of a unit
    table, and 기본 sits down both of its rows.
    """
    cell = {"text": text}
    if columns:
        cell["span"] = columns
    if down:
        cell["spanDown"] = down
    return cell


def CHART(caption, unit, rows):
    """A figure on the page whose values are read off it."""
    return {"type": "chart", "caption": caption, "unit": unit,
            "rows": [list(r) for r in rows]}


def GLOSSARY(*entries):
    """The glossary printed in the margin beside an article.

    Each entry is (term, definition) or (term, definition, headword) where
    the third names the entry the term should open. A fourth element is the
    English written beside the term on the page by hand.
    """
    out = []
    for entry in entries:
        item = {
            "term": entry[0],
            "definition": _spans(entry[1]),
            "annotation": entry[2] if len(entry) > 2 else None,
        }
        if len(entry) > 3 and entry[3]:
            item["handwritten"] = entry[3]
        out.append(item)
    return {"type": "glossary", "entries": out}


# --- registry ---------------------------------------------------------

def _load(prefix, attr):
    found = []
    for info in pkgutil.iter_modules(__path__):
        if not info.name.startswith(prefix):
            continue
        module = importlib.import_module("%s.%s" % (__name__, info.name))
        entry = dict(getattr(module, attr))
        entry["module"] = info.name + ".py"
        found.append(entry)
    return sorted(found, key=lambda c: c["number"])


def load():
    """The chapters, `chNN_slug.py`, ordered by chapter number."""
    return _load("ch", "CHAPTER")


def load_parts():
    """The spreads that close each 편, `ptNN_slug.py`, ordered by part.

    A part page is built exactly as a chapter is — same blocks, same
    annotations, same corrections — and differs only in carrying `part=True`,
    which is what the page reads to say 제N편 rather than Chapter N.
    """
    return _load("pt", "PART")


def contents():
    """The book's own contents, when the content branch supplies them.

    Returns (parts, back). Empty on a checkout that carries only the site and
    the tooling, so the build works there too.
    """
    try:
        module = importlib.import_module("%s.contents" % __name__)
    except ModuleNotFoundError:
        return [], []
    return module.PARTS, module.BACK


CHAPTERS = load()
PARTS = load_parts()
