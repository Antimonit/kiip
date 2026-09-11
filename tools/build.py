# -*- coding: utf-8 -*-
"""Build lessons/<slug>/lesson.js from the Google Docs HTML exports.

    python3 tools/build.py ~/Downloads

Everything the page shows is derived here: the passage text and its inline
annotation anchors come from the export, the annotation bodies come from the
Docs comments, and the transcription corrections come from tools/chapters.py.
"""

import copy
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chapters
from chapters import CHAPTERS, PARTS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HANJA = r"一-鿿"
DASH = r"[—–\-]"
# kinds where the page prints a label and then the section's subject beside it,
# rather than a heading followed by a separate one
PROMOTE_TOPIC = {"aside", "discuss"}

SPECIAL = {
    "생각해 봅시다": "warmup",
    "학습목표": "goals",
    "관련 단원 확인하기": "related",
    "알아두면 좋아요": "aside",
    "주요 내용정리": "review",
    "이야기 나누기": "discuss",
}


# --------------------------------------------------------------------------
# annotations
# --------------------------------------------------------------------------

LEAD = re.compile(r"^[\^>•]\s*")


def strip_lead(spans):
    """Drop the marker a Doc line uses to flag a margin note or a caption."""
    if spans and isinstance(spans[0], str):
        stripped = LEAD.sub("", spans[0])
        if stripped != spans[0]:
            spans = [stripped] + list(spans[1:])
    return spans


def block_text(block):
    if "runs" not in block:
        return ""
    return "".join(r["text"] for r in block["runs"])


SKIP_KEYS = {"annotation", "type", "kind", "slug"}


def apply_fixes(tree, fixes, hits):
    """Rewrite every rendered string in the built lesson.

    Runs after the spans are assembled, because the Docs export splits runs
    mid-phrase and a correction often straddles the split. A fix written as
    "=text" must match a whole string exactly; anything else is a substring.
    """
    def fix(s):
        for old, new, why in ((f[0], f[1], f[2]) for f in fixes):
            if old == new:
                continue
            if old.startswith("="):
                if s == old[1:]:
                    s = new
                    hits[(old, new, why)] = hits.get((old, new, why), 0) + 1
            elif old in s:
                hits[(old, new, why)] = hits.get((old, new, why), 0) + s.count(old)
                s = s.replace(old, new)
        return s

    def walk(node):
        if isinstance(node, str):
            return fix(node)
        if isinstance(node, list):
            return [walk(x) for x in node]
        if isinstance(node, dict):
            return {k: (v if k in SKIP_KEYS else walk(v)) for k, v in node.items()}
        return node

    return walk(tree)


def normalize_spans(node):
    """Move whitespace out of annotated words and off the ends of a span list."""
    if isinstance(node, dict):
        for k, v in node.items():
            if k in ("spans", "definition", "items", "lines") and isinstance(v, list):
                node[k] = tidy(v) if k in ("spans", "definition") else [normalize_spans(x) for x in v]
            else:
                normalize_spans(v)
    elif isinstance(node, list):
        for x in node:
            normalize_spans(x)
    return node


def tidy(segs):
    if not segs or not all(isinstance(x, (str, dict)) for x in segs):
        return [normalize_spans(x) if isinstance(x, dict) else x for x in segs]
    out = []
    for seg in segs:
        if isinstance(seg, str):
            out.append(seg)
            continue
        w = seg["word"]
        lead, w, trail = w[:len(w) - len(w.lstrip())], w.strip(), w[len(w.rstrip()):]
        if lead:
            out.append(lead)
        out.append(dict(seg, word=w))
        if trail:
            out.append(trail)
    merged = []
    for seg in out:
        if isinstance(seg, str) and merged and isinstance(merged[-1], str):
            merged[-1] += seg
        else:
            merged.append(seg)
    if merged and isinstance(merged[0], str):
        merged[0] = merged[0].lstrip()
    if merged and isinstance(merged[-1], str):
        merged[-1] = merged[-1].rstrip()
    return [x for x in merged if x != ""]


# The page prints its own list markers into the text. They are the list's
# markers, not its content, so they come off and the list carries them.
BULLET_MARK = re.compile(r"^\s*[•·]\s*")
NUMBER_MARK = re.compile(r"^\s*\d+\.\s+")


# In 주요 내용정리 a parenthesised group is a gap for the student to fill.
# A real parenthetical such as (2020년 기준) has no padding inside the
# brackets, which is what separates the two.
BLANK = re.compile(r"\(\s*\)|\(\s+[^()]*?\s+\)")


def split_blanks(text, clear=()):
    out, pos = [], 0
    for m in BLANK.finditer(text):
        if m.start() > pos:
            out.append(text[pos:m.start()])
        answer = m.group(0)[1:-1].strip()
        out.append({"blank": "" if answer in clear else answer})
        pos = m.end()
    if pos < len(text):
        out.append(text[pos:])
    return out


# A translation comment opens by naming the section, then quotes the body.
# The body is matched paragraph for paragraph against the prose it translates;
# anything that is not running prose ends the run.
PROSE_STOP = {"section", "heading", "glossary", "table", "chart", "verse",
              "labels", "figure", "source", "margin", "bullet"}


def strip_quotes(text):
    return text.strip().strip("\u201c\u201d\"").strip()


def clean_trans_title(title, *korean):
    """'한국인들이 선호하는 일터 (Workplaces Koreans prefer)' -> the English only."""
    t = title.strip()
    for ko in korean:
        if ko and t.startswith(ko):
            t = t[len(ko):].strip()
            break
    m = re.match(r"^\((.*)\)$", t)
    if m:
        t = m.group(1).strip()
    return t or None


def regroup_translation(body, targets):
    """Redivide a translation that paragraphs differently from the Korean.

    A translation written alongside the Doc often breaks its paragraphs where
    the Korean does not — an opening sentence set on its own, or two Korean
    paragraphs answered by one English one. When the two agree on sentences
    even though they disagree on paragraphs, the English is cut again to the
    Korean's shape. When they do not agree, nothing is guessed.
    """
    wanted = [len(split_korean(t["spans"])) for t in targets]
    english = [s for para in body for s in split_english(para)]
    if sum(wanted) != len(english):
        return None
    out, at = [], 0
    for n in wanted:
        out.append(" ".join(english[at:at + n]))
        at += n
    return out


def align_translations(blocks, unaligned, authored=None):
    """Attach each English paragraph to the Korean paragraph it translates.

    A translation either came from a comment left on the heading in the Doc,
    or was written into the chapter module under `english`. Falls back to
    leaving the whole translation on the heading when the two do not divide
    the same way, rather than pairing them up wrongly.
    """
    authored = authored or {}
    for i, b in enumerate(blocks):
        # only a heading or a section carries a whole-section translation;
        # a paragraph's own translation is what this pass produces
        if b["type"] not in ("section", "heading"):
            continue

        # An article's prose may be preceded by its margin glossary, a figure
        # or a chart, so those are stepped over; once the prose has started,
        # anything that is not more prose ends it.
        targets = []
        for nxt in blocks[i + 1:]:
            if nxt["type"] == "paragraph" and not nxt.get("role"):
                targets.append(nxt)
            elif nxt["type"] in ("section", "heading") or nxt["type"] == "paragraph":
                break
            elif targets:
                break

        if b.get("translation"):
            paras = [p.strip() for p in b["translation"].split("\n\n") if p.strip()]
            if not paras:
                continue
            quoted = next((k for k, p in enumerate(paras)
                           if p[0] in "\"\u201c"), None)
            # the first paragraph is the heading's own line, either because a
            # quote opens the body under it, or because there is one more
            # paragraph here than there is prose to put it against, or
            # because it is short enough to be a title and not a paragraph
            if quoted is not None:
                title = " ".join(paras[:quoted]) or None
                body = paras[quoted:]
            elif len(paras) > 1 and (len(paras) == len(targets) + 1
                                     or len(paras[0]) < 90):
                title, body = paras[0], paras[1:]
            else:
                title, body = None, paras
            body = [strip_quotes(p) for p in body]
        elif b.get("text") in authored:
            entry = authored[b["text"]]
            title = entry.get("title")
            body = list(entry["paragraphs"])
        else:
            continue

        # a heading whose section has no prose to translate — a page of
        # labels, a table, a list — carries the English of its own line
        if not targets and title is None and len(body) == 1:
            title, body = body[0], []

        if title:
            title = clean_trans_title(title, b.get("text") or "", b.get("topic") or "")
            if title:
                b["titleTranslation"] = title

        if targets and len(body) != len(targets):
            regrouped = regroup_translation(body, targets)
            if regrouped:
                body = regrouped
            elif b.get("text") in authored:
                # the Doc's translation does not answer this section paragraph
                # for paragraph — usually because it stops part-way through —
                # so the one written into the chapter stands in for it
                entry = authored[b["text"]]
                if len(entry["paragraphs"]) == len(targets):
                    title = entry.get("title") or title
                    body = list(entry["paragraphs"])

        if len(body) == len(targets):
            for target, english in zip(targets, body):
                target["translation"] = english
            b.pop("translation", None)
        else:
            b["translation"] = "\n\n".join(body)
            unaligned.append((b.get("text") or b.get("topic") or "?",
                              len(body), len(targets)))
    return blocks


# Sentence-final punctuation, then whitespace, then something that is not a
# closing bracket or quote. That last condition is what keeps “…먹자.”라는 and
# (2018년 5월 기준). in one piece.
SENTENCE_END = re.compile(r"([.?!][”’\"']?)(\s+)(?=[^\s)\]”’])")


# What an English sentence may begin with. A lower-case word means the stop
# before it belonged to an abbreviation — "to 4 p.m., and", "(daycare vs.
# kindergarten)" — and an em dash means the clause carries on. Hangul counts,
# because a translation often opens on the Korean term it is explaining.
SENTENCE_START = re.compile(r"[A-Z0-9\"'\u201c\u2018\uac00-\ud7a3]")


# A stop that belongs to an abbreviation rather than to the end of a
# sentence. 'Cell No. 7' is one title, not two sentences.
ABBREV = re.compile(r"\b(No|Nos|Mr|Mrs|Ms|Dr|St|vs|Fig)\.$")


def split_english(text):
    parts, last = [], 0
    for m in SENTENCE_END.finditer(text):
        if not SENTENCE_START.match(text, m.end()):
            continue
        if ABBREV.search(text[:m.end(1)]):
            continue
        parts.append(text[last:m.start() + 1].strip())
        last = m.end()
    if last < len(text):
        parts.append(text[last:].strip())
    return [p for p in parts if p]


def split_korean(span_list):
    """Cut a span list into sentences.

    The split runs over the concatenated text and the offsets are mapped back
    into the array, because a boundary can fall on the seam between spans —
    수준이다. ends one span and the next sentence starts inside the annotated
    공공 기관, so looking within one span at a time misses it. An annotated
    span is never cut.
    """
    plain, ranges = "", []
    for seg in span_list:
        text = seg if isinstance(seg, str) else seg["word"]
        ranges.append((seg, len(plain), len(plain) + len(text)))
        plain += text

    cuts = [m.end() for m in SENTENCE_END.finditer(plain)]
    sentences, ci = [[]], 0

    for seg, start, end in ranges:
        while ci < len(cuts) and cuts[ci] <= start:
            if cuts[ci] == start:
                sentences.append([])
            ci += 1
        if not isinstance(seg, str):
            sentences[-1].append(seg)
            continue
        local = 0
        while ci < len(cuts) and cuts[ci] < end:
            at = cuts[ci] - start
            sentences[-1].append(seg[local:at])
            sentences.append([])
            local = at
            ci += 1
        sentences[-1].append(seg[local:])

    out = []
    for sentence in sentences:
        if sentence and isinstance(sentence[0], str):
            sentence[0] = sentence[0].lstrip()
        kept = [x for x in sentence if not (isinstance(x, str) and not x)]
        if any(not isinstance(x, str) or x.strip() for x in kept):
            out.append(kept)
    return out


def pair_sentences(blocks, unpaired):
    """Pair each Korean sentence with the English sentence that renders it.

    Only when the two divide the same way. Where they do not — a translation
    that merges two sentences into one, say — the paragraph keeps its whole
    translation and is rendered as a single row.
    """
    for b in blocks:
        # a verse is paired line by line, each line standing on its own
        if b["type"] == "verse" and b.get("translations"):
            for k, line in enumerate(b["lines"]):
                korean = split_korean(line)
                english = split_english(b["translations"][k])
                if len(korean) == len(english):
                    b.setdefault("sentences", []).append(
                        [{"spans": ko, "translation": en}
                         for ko, en in zip(korean, english)])
                else:
                    b.setdefault("sentences", []).append(None)
                    unpaired.append((len(korean), len(english)))
            continue
        if b["type"] not in ("paragraph", "bullet") or not b.get("translation"):
            continue
        korean = split_korean(b["spans"])
        english = split_english(b["translation"])
        if len(korean) == len(english):
            b["sentences"] = [{"spans": k, "translation": e}
                              for k, e in zip(korean, english)]
        else:
            unpaired.append((len(korean), len(english)))
    return blocks


def mark_first(blocks, key, saids, inside):
    """Mark the first place the chapter says a word, article prose first.

    A word is often said in 생각해 봅시다 or 학습목표 a page before the
    article that teaches it, and marking it there leaves the word plain
    where the reader actually meets it. So the numbered articles are
    searched first and the rest of the page only if the word is never said
    in one. `saids` are the forms to look for, in order of preference.
    """
    for scope in (inside, None):
        for said in saids:
            for spans in every_span_list(blocks, scope):
                out, done = [], False
                for span in spans:
                    at = -1 if done or not isinstance(span, str) \
                        else word_start(span, said)
                    if at < 0:
                        out.append(span)
                        continue
                    if span[:at]:
                        out.append(span[:at])
                    out.append({"word": said, "annotation": key})
                    if span[at + len(said):]:
                        out.append(span[at + len(said):])
                    done = True
                if done:
                    spans[:] = out
                    return True
    return False


def attach_extras(blocks, extras, heads=None, orphaned=None):
    """Point an annotation written in the chapter module at its word.

    A Doc leaves a comment on the words it explains, and those anchor
    themselves. An entry written into the chapter has no anchor, so the word
    is found in the prose instead — the first time it is said, and only where
    it is not already annotated there. Failing that it claims the margin
    glossary term of the same name, which is bare on a page the Doc left
    uncommented. An entry whose word is never said stays unattached, and the
    build reports it.
    """
    wanted = [k for k in extras if k]
    if not wanted:
        return blocks
    # a word may be written in the prose in an inflected form and filed under
    # its dictionary form, so the surfaces that headwords maps to this entry
    # are worth looking for too
    heads = heads or {}
    surfaces = {}
    for surface, head in heads.items():
        if head in extras:
            surfaces.setdefault(head, []).append(surface)

    # a mark already on the page satisfies the search — unless it sits in
    # the opening boxes, which name a word before the article teaches it
    preface = before_articles(blocks)
    taken = set()
    for spans in every_span_list(blocks, only={
            k: not v for k, v in preface.items()}):
        for span in spans:
            if isinstance(span, dict) and span.get("annotation") in extras:
                taken.add(span["annotation"])

    # longest first, so 단독 주택 wins over 주택 where the two overlap
    inside = in_article(blocks)
    for key in sorted(set(wanted) - taken, key=len, reverse=True):
        if mark_first(blocks, key, [key] + surfaces.get(key, []), inside):
            taken.add(key)

    # a margin glossary term with nothing anchored to it — a Doc with no
    # comments on that page leaves every term bare — takes the entry written
    # for the same word
    for b in blocks:
        for entry in b.get("entries", ()):
            term = entry.get("term", "")
            if not entry.get("annotation") and term in extras:
                entry["annotation"] = term
                taken.add(term)

    if orphaned is not None:
        # for the report, an entry counts as reached if anything at all points
        # at it — a glossary term the Doc anchored, a table cell, a caption
        def reached(node):
            if isinstance(node, dict):
                if node.get("annotation") in extras:
                    taken.add(node["annotation"])
                for v in node.values():
                    reached(v)
            elif isinstance(node, list):
                for v in node:
                    reached(v)
        reached(blocks)
        orphaned.extend(sorted(set(wanted) - taken))
    return blocks


def attach_glossary(blocks, heads=None):
    """Point a margin-glossary term at the place the article says it.

    The textbook glosses a word in the margin and then uses it in the prose a
    line or two later. The gloss carries the annotation, but the word in the
    prose is left plain unless the Doc happened to comment on it there too.
    This marks the first place the article says it, so the word is clickable
    where it is read.
    """
    heads = heads or {}
    terms = {}
    for b in blocks:
        for entry in b.get("entries", ()):
            key = entry.get("annotation")
            if key:
                terms[key] = entry.get("term", key)
    if not terms:
        return blocks
    for spans in every_span_list(blocks):
        for span in spans:
            if isinstance(span, dict):
                terms.pop(span.get("annotation"), None)

    surfaces = {}
    for surface, head in heads.items():
        if head in terms:
            surfaces.setdefault(head, []).append(surface)

    inside = in_article(blocks)
    for key in sorted(terms, key=len, reverse=True):
        mark_first(blocks, key, [terms[key], key] + surfaces.get(key, []),
                   inside)
    return blocks


# the boxes the chapter opens with, before its numbered articles
PREFACE = {"warmup", "goals", "related"}


def in_article(blocks):
    """Which blocks stand inside a numbered article, section by section.

    Everything from a `part` heading until the next section belongs to the
    article; 생각해 봅시다, 학습목표, 알아두면 좋아요 and the closing pages
    do not.
    """
    inside, at = {}, False
    for b in blocks:
        if b["type"] == "section":
            at = b.get("kind") == "part"
        inside[id(b)] = at
    return inside


def before_articles(blocks):
    """Which blocks stand in the boxes the chapter opens with.

    A word marked there — 생각해 봅시다 names it in a question, 학습목표 in
    an aim — is not yet marked where it is taught, so it does not satisfy
    the search for it.
    """
    seen, at = {}, False
    for b in blocks:
        if b["type"] == "section":
            at = b.get("kind") in PREFACE
        seen[id(b)] = at
    return seen


def every_span_list(blocks, only=None):
    """Each run of spans a reader can click a word in.

    Running prose comes first, so that a word looked for across the whole
    chapter is marked where it is read rather than on a photo label. `only`
    is a set of block ids to stay within — the article's own prose, when a
    word is wanted there before anywhere else.
    """
    def wanted(b):
        return only is None or only.get(id(b))

    for b in blocks:
        if not wanted(b):
            continue
        if b["type"] in ("paragraph", "bullet"):
            yield b["spans"]
        if b["type"] == "columns":
            for column in b["columns"]:
                yield column["title"]
                for para in column["paragraphs"]:
                    yield para
    for b in blocks:
        if wanted(b) and b["type"] == "heading" and "spans" in b:
            yield b["spans"]
    for b in blocks:
        if not wanted(b):
            continue
        if b["type"] in ("margin", "labels", "verse"):
            for item in b.get("items") or b.get("lines") or ():
                yield item
            for group in b.get("groups") or ():
                yield group["name"]
                for item in group["items"]:
                    yield item


HANGUL = re.compile(r"[\uac00-\ud7a3]")


def word_start(text, key):
    """Where the key is said as a word, not buried inside a longer one.

    A particle may follow it — 세를, 태교라고 — so only what comes before is
    tested: another Hangul syllable there means this is the middle of a word,
    the 음 of 다음 or the 유아 of 영유아, and not the word being explained.
    """
    at = text.find(key)
    while at >= 0:
        if at == 0 or not HANGUL.match(text[at - 1]):
            return at
        at = text.find(key, at + 1)
    return -1


def mark_blanks(blocks, clear=()):
    """Turn the gaps in a section of questions into blank spans.

    An answer already written into the Doc is carried through as the blank's
    content, for the page to keep covered until the reader asks for it. An
    answer named in the chapter's clearGaps is dropped instead, leaving the
    gap open again.
    """
    in_gaps = False
    for b in blocks:
        if b["type"] == "section":
            in_gaps = b["kind"] in ("review", "quiz", "exam")
        if not in_gaps or b["type"] not in ("paragraph", "bullet"):
            continue
        out = []
        for seg in b["spans"]:
            if isinstance(seg, str):
                out.extend(split_blanks(seg, clear))
            else:
                out.append(seg)
        b["spans"] = out
    return blocks


LABEL_ENGLISH = re.compile(r"^(.+?)\s*\(([A-Za-z][^()]*)\)\s*$")


def absorb_handwriting(blocks, annotations):
    """Move a handwritten English gloss off the page and into its entry.

    The glosses written beside a margin term, or in brackets after a diagram
    label, are notes to self rather than part of the textbook, so they belong
    behind the word instead of printed next to it. A word with no entry yet
    gets one, so the gloss stays reachable.
    """
    def stow(key, headword, english):
        entry = annotations.get(key)
        if entry is None:
            entry = annotations[key] = {
                "headword": headword, "hanja": None, "meaning": None,
                "characters": [], "notes": [], "surfaces": [],
            }
        if english and not entry.get("handwritten"):
            entry["handwritten"] = english
        return key

    for b in blocks:
        if b["type"] == "glossary":
            for entry in b["entries"]:
                english = entry.pop("handwritten", None)
                if not english:
                    continue
                entry["annotation"] = stow(entry.get("annotation") or entry["term"],
                                           entry["term"], english)

        elif b["type"] == "labels":
            runs = [b["items"]] if "items" in b else \
                [g["items"] for g in b["groups"]] + \
                [[g["name"]] for g in b["groups"]]
            for items in runs:
                for k, item in enumerate(items):
                    if len(item) != 1 or not isinstance(item[0], str):
                        continue
                    m = LABEL_ENGLISH.match(item[0])
                    if not m:
                        continue
                    term, english = m.group(1).strip(), m.group(2).strip()
                    items[k] = [{"word": term,
                                 "annotation": stow(term, term, english)}]
    return blocks


def promote_topics(blocks):
    """Fold a section's first heading into the section itself as its topic.

    For the kinds in PROMOTE_TOPIC the page prints a label and then the
    subject beside it, rather than a heading below it. Doing this here keeps
    the renderer from having to know which kinds those are.
    """
    out = []
    waiting = None
    for b in blocks:
        if waiting is not None and b["type"] == "heading":
            waiting["topic"] = b["text"]
            if b.get("translation"):
                waiting["translation"] = b["translation"]
            waiting = None
            continue
        if b["type"] == "section":
            waiting = b if b["kind"] in PROMOTE_TOPIC else None
        elif b["type"] not in ("labels", "margin", "figure", "source"):
            waiting = None
        out.append(b)
    return out


ENTRY_FIELDS = {"headword", "hanja", "meaning", "characters", "notes",
                "surfaces"}


def written_entries(written, module):
    """The annotation entries a chapter module writes out, in payload shape."""
    out = {}
    for key, extra in written.items():
        unknown = set(extra) - ENTRY_FIELDS
        if unknown:
            raise SystemExit(
                "%s: entry %r uses unknown field(s) %s — expected %s"
                % (module, key, ", ".join(sorted(unknown)),
                   ", ".join(sorted(ENTRY_FIELDS))))
        out[key] = {
            "headword": extra.get("headword", key),
            "hanja": extra.get("hanja"),
            "meaning": extra.get("meaning"),
            "characters": [
                {"char": c, "reading": r, "gloss": g} if r else
                {"char": c, "gloss": g}
                for c, r, g in extra.get("characters", [])],
            "notes": list(extra.get("notes", [])),
            "surfaces": list(extra.get("surfaces", [])),
        }
    return out


def marked_keys(blocks):
    """Every entry key a mark on the page points at."""
    found = set()

    def walk(node):
        if isinstance(node, dict):
            if "word" in node and node.get("annotation"):
                found.add(node["annotation"])
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(blocks)
    return found


def refile(annotations, blocks):
    """File every entry under the word it explains.

    An entry is keyed by the word the Doc anchored the comment to, which is
    not always the word the reader ends up seeing: a typo the corrections
    have since put right (출성, now 충성), or an inflected form whose entry
    is written under the dictionary word (차지하며, filed as 차지하다). The
    key is an implementation detail of the Doc, so once the corrections have
    run each entry is refiled under its own headword and every mark that
    pointed at the old key is pointed at the new one.
    """
    moved, claimed = {}, set(annotations)
    for key, entry in annotations.items():
        head = (entry.get("headword") or key).strip()
        if head == key or head in claimed:
            continue
        moved[key] = head
        claimed.add(head)
    if not moved:
        return annotations

    def walk(node):
        if isinstance(node, dict):
            if node.get("annotation") in moved:
                node["annotation"] = moved[node["annotation"]]
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(blocks)
    return {moved.get(k, k): v for k, v in annotations.items()}


def fill_crossword(blocks, module):
    """Put the clues' answers into the grid, and check that they fit.

    The geometry comes from CROSSWORD in the chapter module; the words come
    from the clues in the same section, each of which ends in its answer as a
    gap — ( 온돌 ). A crossing cell is written by two words, so the two must
    agree; where they do not, or a word runs off the grid, the build stops
    rather than draw a wrong puzzle.
    """
    for i, b in enumerate(blocks):
        if b["type"] != "crossword":
            continue

        # the clues that follow it, up to the end of the section
        answers = {}
        for nxt in blocks[i + 1:]:
            if nxt["type"] == "section":
                break
            if nxt["type"] != "bullet":
                continue
            # the gaps have already been turned into blanks, so the answer
            # is the blank's content rather than anything in the text
            head = next((x for x in nxt["spans"] if isinstance(x, str)), "")
            label = head.split(" ", 1)[0]
            gap = next((x["blank"] for x in nxt["spans"]
                        if isinstance(x, dict) and x.get("blank")), None)
            if gap:
                answers[label] = gap.strip().replace(" ", "")

        cells = {}
        for entry in b["entries"]:
            word = answers.get(entry["label"])
            if not word:
                raise SystemExit("%s: the crossword names %s, which has no "
                                 "clue with an answer" % (module, entry["label"]))
            entry["answer"] = word
            entry["cells"] = []
            for k, letter in enumerate(word):
                x = entry["x"] + (k if entry["dir"] == "across" else 0)
                y = entry["y"] + (k if entry["dir"] == "down" else 0)
                if not (1 <= x <= b["cols"] and 1 <= y <= b["rows"]):
                    raise SystemExit(
                        "%s: %s (%s) runs off the %dx%d grid at (%d, %d)"
                        % (module, entry["label"], word, b["cols"], b["rows"],
                           x, y))
                if cells.get((x, y), letter) != letter:
                    raise SystemExit(
                        "%s: %s puts %s at (%d, %d) where another word has %s"
                        % (module, entry["label"], letter, x, y,
                           cells[(x, y)]))
                cells[(x, y)] = letter
                entry["cells"].append([x, y])

        starts = {}
        for entry in b["entries"]:
            starts.setdefault((entry["x"], entry["y"]), []).append(entry["label"])
        b["grid"] = [[None if (x, y) not in cells else
                      {"answer": cells[(x, y)],
                       "labels": starts.get((x, y), [])}
                      for x in range(1, b["cols"] + 1)]
                     for y in range(1, b["rows"] + 1)]
    return blocks


def build(cfg):
    """One chapter's payload, from the text its module carries.

    A chapter's text arrives here before correction — as `blocks`, or, for a
    chapter transcribed straight from the photographs, as `append` alone —
    so `fixes` still reaches it and a correction can be reviewed and retired.
    """
    heads = cfg.get("headwords", {})

    if cfg.get("src"):
        raise SystemExit(
            "%s names src=%r, but the Google Doc reader was removed once "
            "every chapter carried its own text. Recover tools/convert.py "
            "and tools/parse_gdoc.py from an earlier revision to convert it."
            % (cfg["module"], cfg["src"]))

    blocks = copy.deepcopy(cfg.get("blocks", []))
    # the entries the Doc's comments carried, still under correction:
    # `fixes` reaches them exactly as it reached the Doc
    annotations = written_entries(cfg.get("annotations", {}), cfg["module"])
    orphans = list(cfg.get("chapterGlossary", ()))
    # the trailing entry collapses double spaces left behind by the fixes
    fixes = list(cfg.get("fixes", ())) + [("  ", " ", None)]
    hits = {}

    # ---- corrections --------------------------------------------------
    shown = {f[0]: f[3] for f in fixes if len(f) > 3}
    blocks = apply_fixes(blocks, fixes, hits)
    annotations = apply_fixes(annotations, fixes, hits)

    # entries written by hand in the chapter module, before the handwriting
    # on the page is folded in, so an entry can be given a proper breakdown
    # and still keep the note that was scribbled beside the word
    annotations.update(
        written_entries(cfg.get("extraAnnotations", {}), cfg["module"]))

    # appended blocks are transcribed by hand, so they skip the corrections
    unaligned, unpaired, orphaned, empty = [], [], [], []
    blocks = normalize_spans(blocks + copy.deepcopy(cfg.get("append", [])))
    blocks = absorb_handwriting(blocks, annotations)
    # the ★ that opens a section's closing question. Decided here rather than
    # in the helper because a Doc sometimes typed it as an asterisk and it is
    # a fix that puts the star back.
    for b in blocks:
        if b["type"] == "paragraph" and b["spans"] \
                and isinstance(b["spans"][0], str) \
                and b["spans"][0].startswith("\u2605"):
            b["role"] = "prompt"
    # a heading is prose too, so it takes part in the search for a word; it
    # keeps its plain text either way, which is what the English is keyed on.
    # A heading that marks its own words arrives with spans already and is
    # left alone — overwriting them threw the marks away.
    for b in blocks:
        if b["type"] == "heading" and "spans" not in b:
            b["spans"] = [b["text"]]
    blocks = attach_extras(blocks, cfg.get("extraAnnotations", {}), heads,
                           orphaned)
    blocks = attach_glossary(blocks, heads)
    for b in blocks:
        if b["type"] == "heading" and not any(
                isinstance(x, dict) for x in b["spans"]):
            del b["spans"]
    blocks = promote_topics(blocks)
    blocks = align_translations(blocks, unaligned, cfg.get("english"))
    blocks = pair_sentences(blocks, unpaired)
    blocks = mark_blanks(blocks, set(cfg.get("clearGaps", ())))
    blocks = fill_crossword(blocks, cfg["module"])

    for a in annotations.values():
        a["headword"] = a["headword"].strip()
    annotations = refile(annotations, blocks)

    # Notes are data, not markup: the page decides how to present them.
    #
    # A correction listed in `approved` has been read against the page photos
    # and accepted, so it still applies but is no longer reported: what the
    # section shows is what is left to review. A correction that was rejected
    # is simply deleted from `fixes`, which restores the original text.
    approved = set(cfg.get("approved", ()))
    notes = []
    for (old, new, why), count in hits.items():
        if why is None or old in approved:
            continue
        was, now = shown.get(old, (old.lstrip("="), new))
        notes.append({"was": was, "now": now, "why": why, "count": count})
    notes += [{"why": n} if isinstance(n, str) else dict(n)
              for n in cfg.get("extraNotes", [])]
    unused = [f for f in fixes
              if (f[0], f[1], f[2]) not in hits and f[0] != f[1] and f[2]]

    # the mirror of the orphan report: a mark whose entry was never written
    # opens a card with nothing in it but the word
    for key in sorted(marked_keys(blocks) - set(annotations)):
        empty.append(key)

    lesson = {
        "number": cfg["number"], "unit": cfg["unit"], "title": cfg["title"],
        "titleEnglish": cfg["titleEn"],
        "chapterGlossary": orphans,
        "blocks": blocks, "annotations": annotations, "notes": notes,
    }
    return lesson, unused, unaligned, unpaired, orphaned, empty


BANNER = ("/* Generated by tools/build.py — do not edit.\n"
          "   Content lives in tools/chapters/%s; rebuild after changing it. */\n\n")


def write_payload(path, call, payload, source):
    """Write one content file: a registration call wrapping pure data."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(BANNER % source)
        f.write("KIIP.%s(" % call)
        json.dump(payload, f, ensure_ascii=False, indent=1)
        f.write(");\n")


def emit_payload(cfg, out):
    """Build one chapter or part page, write it, and say how it went."""
    lesson, unused, unaligned, unpaired, orphaned, empty = build(cfg)
    lesson["slug"] = cfg["slug"]
    if cfg.get("part"):
        lesson["part"] = True
    write_payload(os.path.join(out, cfg["slug"] + ".js"), "chapter", lesson,
                  cfg["module"])
    print("%-34s %3d blocks %3d annotations %2d notes %s" % (
        cfg["slug"], len(lesson["blocks"]), len(lesson["annotations"]),
        len(lesson["notes"]),
        "UNUSED FIXES: %s" % [u[0] for u in unused] if unused else ""))
    for got, want in unpaired:
        print("    paragraph rendered whole: %d Korean sentences against "
              "%d English" % (got, want))
    for where, got, want in unaligned:
        print("    translation left whole on %r: %d English paragraphs "
              "against %d Korean" % (where[:40], got, want))
    if orphaned:
        print("    annotations nothing points at: %s" % orphaned)
    if empty:
        print("    marks with no entry behind them: %s" % empty)


def main():
    out = os.path.join(ROOT, "lessons")
    os.makedirs(out, exist_ok=True)

    manifest = []
    for cfg in CHAPTERS:
        manifest.append({k: cfg[k]
                         for k in ("number", "slug", "title", "titleEn")})

        emit_payload(cfg, out)

    # the spread that closes each 편, built and addressed as a chapter is
    for cfg in PARTS:
        emit_payload(cfg, out)

    parts, back = chapters.contents()
    if parts:
        done = {c["number"] for c in CHAPTERS}
        closing = {p["number"]: p["slug"] for p in PARTS}
        for part in parts:
            for c in part["chapters"]:
                c["built"] = c["number"] in done
            if part["number"] in closing:
                part["closing"] = closing[part["number"]]
        print("%-34s %3d chapters in %d parts, %d built" % (
            "contents", sum(len(p["chapters"]) for p in parts), len(parts),
            len(done)))
    write_payload(os.path.join(out, "contents.js"), "contents",
                  {"parts": parts, "back": back}, "contents.py")

    write_payload(os.path.join(out, "manifest.js"), "manifest", manifest,
                  "chNN_*.py")
    if not CHAPTERS:
        print("no chapters found in tools/chapters/ — nothing to build")


if __name__ == "__main__":
    main()
