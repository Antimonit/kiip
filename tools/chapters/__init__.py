# -*- coding: utf-8 -*-
"""Chapter registry and the helpers chapter modules are written with.

One module per chapter, named `chNN_slug.py`, each defining a single
`CHAPTER` dict. They are discovered automatically and ordered by chapter
number, so adding a chapter means adding a file and nothing else.

Everything in a chapter module is content: its title and tags, its
transcription corrections, the dictionary forms of words that appear
inflected, and any blocks transcribed from the page photos. Nothing here
describes appearance — blocks say what a thing is, and assets/style.css
decides how it looks.

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
            out.append({"w": surface, "a": key or surface})
        else:
            out.append(part)
    return out


def SECT(kind, text):
    """A section of the given kind — see SPECIAL in tools/build.py."""
    return {"t": "section", "kind": kind, "text": text}


def H(level, text):
    return {"t": "heading", "level": level, "text": text}


def P(text):
    return {"t": "p", "s": _spans(text)}


def B(text):
    return {"t": "bullet", "s": _spans(text)}


def SRC(text):
    """A source or citation line."""
    return {"t": "source", "text": text}


def LABELS(*texts):
    """Short labels printed on a photo or diagram."""
    return {"t": "labels", "items": [_spans(t) for t in texts]}


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
