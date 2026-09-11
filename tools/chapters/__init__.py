# -*- coding: utf-8 -*-
"""Chapter registry and the helpers chapter modules are written with.

One module per chapter, named `chNN_slug.py`, each defining a single
`CHAPTER` dict. A chapter carries its text itself: `blocks` for text that came
from a Google Doc, written into the module when the Doc pipeline was retired,
and `append` for text transcribed straight from the page photos. Modules are
discovered automatically
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


def _plain(text):
    """The text with the annotation braces taken out."""
    return "".join(p["word"] if isinstance(p, dict) else p
                   for p in _spans(text))


def HEADING(level, text, translation=None):
    """A heading. `translation` is the English written beside it.

    A heading may mark a word like any other line — the 생각해 봅시다
    questions do. `text` stays the plain reading of it, which is what the
    build matches headings on, and the marks ride alongside in `spans`.
    """
    block = {"type": "heading", "level": level, "text": _plain(text)}
    if "{" in text:
        block["spans"] = _spans(text)
    if translation:
        block["translation"] = translation
    return block


def PARAGRAPH(text, translation=None):
    """A paragraph. A ★ opens the question a section closes with — the build
    marks that one, after the corrections, since a Doc sometimes typed the
    star as an asterisk."""
    block = {"type": "paragraph", "spans": _spans(text)}
    if translation:
        block["translation"] = translation
    return block


def BULLET(text, ordered=False, level=1, translation=None):
    """A list item. level=2 nests it under the item before it."""
    item = {"type": "bullet", "spans": _spans(text)}
    if translation:
        item["translation"] = translation
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


def COLUMNS(*columns):
    """Prose the book sets side by side, each column under its own title."""
    return {"type": "columns", "columns": list(columns)}


def COLUMN(title, *paragraphs):
    """One column of COLUMNS: a title and the prose beneath it."""
    return {"title": _spans(title),
            "paragraphs": [_spans(t) for t in paragraphs]}


def MARGIN(*texts):
    """Something written in the margin of the page by hand."""
    return {"type": "margin", "items": [_spans(t) for t in texts]}


def VERSE(*lines, **kw):
    """A quoted text set line by line — an anthem, an article of the law.

    `translation` gives the English one paragraph per line, separated by a
    blank line, so a case study reads beside its Korean like prose does.
    """
    block = {"type": "verse", "lines": [_spans(t) for t in lines]}
    english = kw.pop("translation", None)
    assert not kw, "VERSE: unexpected %s" % ", ".join(sorted(kw))
    if english:
        paras = [p.strip() for p in english.split("\n\n") if p.strip()]
        assert len(paras) == len(block["lines"]), (
            "VERSE: %d English paragraphs against %d lines"
            % (len(paras), len(block["lines"])))
        block["translations"] = paras
    return block


def FIGURE(caption):
    """A photo on the page, which is not reproduced."""
    return {"type": "figure", "text": caption}


def _cell(c):
    """One cell: plain text, or spans where it marks a word.

    A cell reads like any other line of the book, so {word} works in it too.
    A cell with nothing marked stays a plain string, which is what most of
    them are.
    """
    if isinstance(c, dict):
        text = c.get("text", "")
        if "{" in text:
            c = dict(c, spans=_spans(text))
            c.pop("text")
        return c
    return {"spans": _spans(c)} if "{" in c else c


def TABLE(header, rows=None):
    """A table. Called with one argument when the book prints no header row."""
    if rows is None:
        return {"type": "table", "rows": [[_cell(c) for c in r]
                                          for r in header]}
    return {"type": "table", "header": [_cell(c) for c in header],
            "rows": [[_cell(c) for c in r] for r in rows]}


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


def CROSSWORD(cols, rows, *entries):
    """The grid of a 가로 세로 퀴즈.

    Only the geometry: each entry is (label, "across"|"down", x, y), with x
    counting columns and y rows from 1 at the top left, over every cell
    including the blocked ones. The words themselves come from the clues in
    the same section — the build reads them out of the answers and checks
    that every crossing agrees.
    """
    return {"type": "crossword", "cols": cols, "rows": rows,
            "entries": [{"label": e[0], "dir": e[1], "x": e[2], "y": e[3]}
                        for e in entries]}


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
