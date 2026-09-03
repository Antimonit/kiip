# -*- coding: utf-8 -*-
"""Chapter registry and the helpers chapter modules are written with.

One module per chapter, named `chNN_slug.py`, each defining a single
`CHAPTER` dict. A chapter with a Google Doc names it in `src` and is built
from that; a chapter without one leaves `src` out and is transcribed from the
page photos straight into `append`. They are discovered automatically and ordered by chapter
number, so adding a chapter means adding a file and nothing else.

Everything in a chapter module is content: its title and tags, its
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


def SECT(kind, text):
    """A section of the given kind — see SPECIAL in tools/build.py."""
    return {"type": "section", "kind": kind, "text": text}


def H(level, text):
    return {"type": "heading", "level": level, "text": text}


def P(text):
    return {"type": "paragraph", "spans": _spans(text)}


def B(text, ordered=False):
    item = {"type": "bullet", "spans": _spans(text)}
    if ordered:
        item["ordered"] = True
    return item


def SRC(text):
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


def FIG(caption):
    """A photo on the page, which is not reproduced."""
    return {"type": "figure", "text": caption}


def TABLE(header, rows):
    return {"type": "table", "header": list(header),
            "rows": [list(r) for r in rows]}


def SPAN(text, columns):
    """A header cell printed across more than one column."""
    return {"text": text, "span": columns}


def CHART(caption, unit, rows):
    """A figure on the page whose values are read off it."""
    return {"type": "chart", "caption": caption, "unit": unit,
            "rows": [list(r) for r in rows]}


def GLOSS(*entries):
    """The glossary printed in the margin beside an article.

    Each entry is (term, definition) or (term, definition, headword) where
    the third names the entry the term should open.
    """
    out = []
    for entry in entries:
        out.append({
            "term": entry[0],
            "definition": _spans(entry[1]),
            "annotation": entry[2] if len(entry) > 2 else None,
        })
    return {"type": "glossary", "entries": out}


# --- registry ---------------------------------------------------------

def load():
    found = []
    for info in pkgutil.iter_modules(__path__):
        if not info.name.startswith("ch"):
            continue
        module = importlib.import_module("%s.%s" % (__name__, info.name))
        chapter = dict(module.CHAPTER)
        chapter["module"] = info.name + ".py"
        found.append(chapter)
    return sorted(found, key=lambda c: c["number"])


CHAPTERS = load()
