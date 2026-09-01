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
from parse_gdoc import parse
from chapters import CHAPTERS

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

def split_meaning(text):
    """Split 'head - meaning' / 'head = meaning' into its two halves."""
    m = re.match(r"^(.{1,40}?)\s+%s\s+(.+)$" % DASH, text, re.S)
    if not m:
        m = re.match(r"^(.{1,40}?)\s*=\s*(.+)$", text, re.S)
    return (m.group(1).strip(), m.group(2).strip()) if m else (None, text.strip())


def hanja_run(text):
    """'A(power) B(dignity) = authority' -> ([(A,power),(B,dignity)], 'authority')."""
    m = re.match(r"^((?:[%s]\s*\([^)]*\)\s*)+)=\s*(.+)$" % HANJA, text, re.S)
    if not m:
        return None, None
    pairs = re.findall(r"([%s])\s*\(([^)]*)\)" % HANJA, m.group(1))
    return [{"char": c, "gloss": g.strip()} for c, g in pairs], m.group(2).strip()


def hanja_only(text):
    """'A(explain) B(example) C(book)' with no gloss after it."""
    if not re.match(r"^(?:[%s]\s*\([^)]*\)\s*)+$" % HANJA, text):
        return None
    return [{"char": c, "gloss": g.strip()} for c, g in
            re.findall(r"([%s])\s*\(([^)]*)\)" % HANJA, text)]


def as_hanja_line(text):
    """Recognise a standalone hanja-breakdown line."""
    m = re.match(r"^([가-힣])\s*\(([%s])\)\s*%s\s*(.+)$" % (HANJA, DASH), text, re.S)
    if m:
        return {"read": m.group(1), "char": m.group(2), "gloss": m.group(3).strip()}
    m = re.match(r"^([%s]{1,4})\s*%s\s*(.+)$" % (HANJA, DASH), text, re.S)
    if m:
        return {"char": m.group(1), "gloss": m.group(2).strip()}
    m = re.match(r"^([%s]{1,4})\s*=\s*(.+)$" % HANJA, text, re.S)
    if m:
        return {"char": m.group(1), "gloss": m.group(2).strip()}
    return None


def parse_comment(paras):
    """Turn one Docs comment into {headword, hanja, meaning, hanjaList, notes}."""
    out = {"headword": None, "hanja": None, "meaning": None, "hanjaList": [], "notes": []}
    rest = list(paras)

    first = rest.pop(0) if rest else ""
    head, meaning = split_meaning(first)

    if head and re.search(r"[가-힣]", head):
        m = re.match(r"^(.*?)\s+((?:[%s]\s*\([^)]*\)\s*)+)$" % HANJA, head)
        if m:
            out["hanjaList"] += [{"char": c, "gloss": g.strip()} for c, g in
                                 re.findall(r"([%s])\s*\(([^)]*)\)" % HANJA, m.group(2))]
            head = m.group(1).strip()
        m = re.match(r"^(.*?)\s*[\(（]([%s]+[가-힣]*)[\)）]\s*$" % HANJA, head)
        if m:
            out["headword"], out["hanja"] = m.group(1).strip(), m.group(2)
        else:
            out["headword"] = head
        pairs, tail = hanja_run(meaning)
        if pairs:
            out["hanjaList"] += pairs
            meaning = tail
        out["meaning"] = meaning
    else:
        pairs, tail = hanja_run(first)
        only = hanja_only(first)
        if pairs:
            out["hanjaList"] += pairs
            out["meaning"] = tail
        elif only:
            out["hanjaList"] += only
        elif head:
            line = as_hanja_line(first)
            if line:
                out["hanjaList"].append(line)
            else:
                out["meaning"] = first.strip()
        else:
            out["meaning"] = first.strip()

    for p in rest:
        line = as_hanja_line(p)
        if line and len(p) < 160:
            out["hanjaList"].append(line)
        else:
            out["notes"].append(p)
    return out


def display_headword(surface, parsed):
    """Prefer the dictionary form from the comment, when it really is one."""
    if not parsed or parsed == surface:
        return surface
    if len(parsed) > 12 or re.search(r"[(=]", parsed):
        return surface
    if not re.search(r"[가-힣]", parsed):
        return surface
    if parsed[0] != surface[0]:
        return surface
    return parsed


def merge(into, new):
    for k in ("headword", "hanja", "meaning"):
        if not into.get(k) and new.get(k):
            into[k] = new[k]
        elif into.get(k) and new.get(k) and k == "meaning" and new[k] != into[k]:
            label = new.get("headword")
            new["notes"].insert(0, ("%s — %s" % (label, new[k])) if label else new[k])
    into["hanjaList"] += [h for h in new["hanjaList"] if h not in into["hanjaList"]]
    into["notes"] += new["notes"]
    return into


def is_translation(paras, tag):
    """A whole-section translation: a long English comment left on a heading.

    Long English comments on an ordinary word are usage notes, not
    translations, so the anchor's block tag decides.
    """
    if tag not in ("h1", "h2", "h3", "h4"):
        return False
    text = " ".join(paras)
    if len(text) < 240:
        return False
    korean = len(re.findall(r"[가-힣]", text))
    return korean / max(len(text), 1) < 0.12


# --------------------------------------------------------------------------
# blocks
# --------------------------------------------------------------------------

def block_text(block):
    if "runs" not in block:
        return ""
    return "".join(r["text"] for r in block["runs"])


SKIP_KEYS = {"a", "t", "kind", "slug"}


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
            if k in ("s", "def", "items", "lines") and isinstance(v, list):
                node[k] = tidy(v) if k in ("s", "def") else [normalize_spans(x) for x in v]
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
        w = seg["w"]
        lead, w, trail = w[:len(w) - len(w.lstrip())], w.strip(), w[len(w.rstrip()):]
        if lead:
            out.append(lead)
        out.append(dict(seg, w=w))
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


def spans(block, anno_key):
    out = []
    for r in block["runs"]:
        text = r["text"]
        key = anno_key(r) if r["anno"] else None
        if key is None:
            if out and isinstance(out[-1], str):
                out[-1] += text
            else:
                out.append(text)
        else:
            out.append({"w": text, "a": key})
    return [s for s in out if s != ""]


def first_key(block, anno_key):
    for r in block.get("runs", []):
        if r["anno"]:
            k = anno_key(r)
            if k:
                return k
    return None


def gloss_term(text):
    """'A married' -> ('A', 'married')."""
    t = text.lstrip("• ").strip()
    m = re.match(r"^([^A-Za-z(]+?)\s*([A-Za-z(].*)$", t)
    if m and re.search(r"[가-힣]", m.group(1)):
        return m.group(1).strip(), m.group(2).strip()
    return t, None


# In 주요 내용정리 a parenthesised group is a gap for the student to fill.
# A real parenthetical such as (2020년 기준) has no padding inside the
# brackets, which is what separates the two.
BLANK = re.compile(r"\(\s*\)|\(\s+[^()]*?\s+\)")


def split_blanks(text):
    out, pos = [], 0
    for m in BLANK.finditer(text):
        if m.start() > pos:
            out.append(text[pos:m.start()])
        out.append({"blank": m.group(0)[1:-1].strip()})
        pos = m.end()
    if pos < len(text):
        out.append(text[pos:])
    return out


# A translation comment opens by naming the section, then quotes the body.
# The body is matched paragraph for paragraph against the prose it translates;
# anything that is not running prose ends the run.
PROSE_STOP = {"section", "heading", "gloss", "table", "chart", "verse",
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


def align_translations(blocks, unaligned):
    """Attach each English paragraph to the Korean paragraph it translates.

    Falls back to leaving the whole translation on the heading when the two
    do not divide the same way, rather than pairing them up wrongly.
    """
    for i, b in enumerate(blocks):
        # only a heading or a section carries a whole-section translation;
        # a paragraph's own trans is what this pass produces
        if b["t"] not in ("section", "heading") or not b.get("trans"):
            continue
        paras = [p.strip() for p in b["trans"].split("\n\n") if p.strip()]
        if not paras:
            continue

        quoted = next((k for k, p in enumerate(paras)
                       if p[0] in "\"\u201c"), None)
        if quoted is not None:
            title = " ".join(paras[:quoted]) or None
            body = paras[quoted:]
        elif len(paras) > 1 and len(paras[0]) < 90:
            title, body = paras[0], paras[1:]
        else:
            title, body = None, paras
        body = [strip_quotes(p) for p in body]

        targets = []
        for nxt in blocks[i + 1:]:
            if nxt["t"] == "p" and not nxt.get("role"):
                targets.append(nxt)
            elif nxt["t"] in PROSE_STOP or nxt["t"] == "p":
                break

        if title:
            title = clean_trans_title(title, b.get("text") or "", b.get("topic") or "")
            if title:
                b["transTitle"] = title

        if targets and len(body) == len(targets):
            for target, english in zip(targets, body):
                target["trans"] = english
            del b["trans"]
        else:
            b["trans"] = "\n\n".join(body)
            unaligned.append((b.get("text") or b.get("topic") or "?",
                              len(body), len(targets)))
    return blocks


def mark_blanks(blocks):
    """Turn the gaps in the review section into blank spans.

    An answer already written into the Doc is carried through as the blank's
    content, for the page to keep covered until the reader asks for it.
    """
    in_review = False
    for b in blocks:
        if b["t"] == "section":
            in_review = b["kind"] == "review"
        if not in_review or b["t"] not in ("p", "bullet"):
            continue
        out = []
        for seg in b["s"]:
            if isinstance(seg, str):
                out.extend(split_blanks(seg))
            else:
                out.append(seg)
        b["s"] = out
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
        if waiting is not None and b["t"] == "heading":
            waiting["topic"] = b["text"]
            if b.get("trans"):
                waiting["trans"] = b["trans"]
            waiting = None
            continue
        if b["t"] == "section":
            waiting = b if b["kind"] in PROMOTE_TOPIC else None
        elif b["t"] not in ("labels", "margin", "figure", "source"):
            waiting = None
        out.append(b)
    return out


def build(cfg, srcdir):
    doc = parse(os.path.join(srcdir, cfg["src"]))

    # ---- annotations -------------------------------------------------
    anchors, anchor_tag = {}, {}
    def collect(blocks):
        for b in blocks:
            if b["tag"] == "table":
                for row in b["rows"]:
                    for cell in row:
                        collect(cell)
                continue
            for r in b["runs"]:
                for _cid, label in r["anno"]:
                    anchors[label] = r["text"].strip()
                    anchor_tag[label] = b["tag"]
    collect(doc["blocks"])

    heads = cfg.get("headwords", {})
    annotations, key_of_label, translations, surfaces = {}, {}, {}, {}

    for label, paras in doc["comments"].items():
        surface = anchors.get(label, "")
        if is_translation(paras, anchor_tag.get(label)):
            translations[label] = "\n\n".join(paras)
            key_of_label[label] = None
            continue
        parsed = parse_comment(paras)
        key = heads.get(surface) or surface or label
        key_of_label[label] = key
        annotations[key] = merge(annotations.get(key, parse_comment([])), parsed)
        surfaces.setdefault(key, [])
        if surface and surface not in surfaces[key]:
            surfaces[key].append(surface)

    for key, a in annotations.items():
        parsed = heads.get(key) or a.get("headword")
        shown = display_headword(key, parsed)
        if parsed and shown != parsed and a.get("meaning"):
            a["meaning"] = "%s — %s" % (parsed, a["meaning"])
        a["headword"] = shown
        a["notes"] = [n for n in a["notes"] if n.strip()]
        a["surfaces"] = [s for s in surfaces.get(key, []) if s != key]

    def anno_key(run):
        for _cid, label in run["anno"]:
            k = key_of_label.get(label)
            if k:
                return k
        return None

    def run_translation(block):
        for r in block["runs"]:
            for _cid, label in r["anno"]:
                if label in translations:
                    return translations[label]
        return None

    # ---- block roles -------------------------------------------------
    roles = {}
    for (a, b), role in cfg.get("roles", {}).items():
        for i in range(a, b + 1):
            roles[i] = (role, a, b)

    title_labels = {lb for r in doc["blocks"][0]["runs"] for _c, lb in r["anno"]}
    orphans = sorted({key_of_label[l] for l in title_labels if key_of_label.get(l)})

    inserts = cfg.get("insert", {})
    blocks, i, n = [], 1, len(doc["blocks"])
    section_kind = "intro"

    def emit(b):
        blocks.append(b)

    while i < n:
        for extra in inserts.get(i, []):
            emit(copy.deepcopy(extra))
        block = doc["blocks"][i]
        role = roles.get(i)

        if role:
            name, start, end = role
            if i != start:
                i += 1
                continue
            group = doc["blocks"][start:end + 1]
            group = [g for g in group if g["tag"] != "table"]
            texts = [block_text(g).strip() for g in group]
            rich = [spans(g, anno_key) for g in group]
            if name == "heading":
                emit({"t": "heading", "level": 3, "text": texts[0]})
            elif name == "labels":
                emit({"t": "labels", "items": rich})
            elif name == "margin":
                emit({"t": "margin", "items": rich})
            elif name == "figure":
                emit({"t": "figure",
                      "text": " ".join(t.lstrip("^• ").strip() for t in texts)})
            elif name == "source":
                emit({"t": "source", "text": " ".join(texts)})
            elif name == "verse":
                emit({"t": "verse", "lines": rich})
            elif name == "table2":
                rows = [re.split(r"\s{2,}|\t", t, maxsplit=1) for t in texts]
                emit({"t": "table", "rows": [[c.strip() for c in r] for r in rows]})
            elif name == "chart":
                c = cfg["chart"]
                emit({"t": "chart", "caption": c["caption"], "unit": c["unit"],
                      "rows": [list(r) for r in c["rows"]]})
            elif name == "kinship":
                for t in cfg["kinship"]:
                    emit({"t": "heading", "level": 3, "text": t["title"]})
                    emit({"t": "table", "rows": [list(r) for r in t["rows"]],
                          "head": ["가족", "호칭"]})
            i = end + 1
            continue

        tag, text = block["tag"], block_text(block).strip()

        if tag in ("h1", "h2", "h3", "h4"):
            kind = SPECIAL.get(text)
            if kind:
                section_kind = kind
                emit({"t": "section", "kind": kind, "text": text})
            elif tag == "h1":
                section_kind = "part"
                emit({"t": "section", "kind": "part", "text": text})
            else:
                b = {"t": "heading", "level": int(tag[1]), "text": text}
                tr = run_translation(block)
                if tr:
                    b["trans"] = tr
                emit(b)
            i += 1
            continue

        if tag == "table":
            cells = block["rows"]
            if len(cells) == 1 and len(cells[0]) == 1:
                inner = cells[0][0]
                items, j = [], 0
                while j < len(inner):
                    term, en = gloss_term(block_text(inner[j]).strip())
                    definition = spans(inner[j + 1], anno_key) if j + 1 < len(inner) else []
                    key = first_key(inner[j], anno_key)
                    items.append({"term": term, "en": en, "def": definition, "a": key})
                    j += 2
                emit({"t": "gloss", "items": items})
            else:
                rows = [[" ".join(block_text(bl).strip() for bl in cell) for cell in row]
                        for row in cells]
                # 관련 단원 prints 영역 across the two columns it heads, so a
                # header row short of the body's width spans its first cell
                width = max(len(r) for r in rows)
                head = list(rows[0])
                if head and len(head) < width:
                    head[0] = {"text": head[0], "span": width - len(head) + 1}
                emit({"t": "table", "head": head, "rows": rows[1:]})
            i += 1
            continue

        bulleted = text.startswith("•")
        if section_kind in ("part", "intro") and (tag == "li" or bulleted) and i + 1 < n:
            nxt = doc["blocks"][i + 1]
            nxt_text = block_text(nxt).strip()
            if nxt["tag"] == "p" and not nxt_text.startswith("•"):
                items = []
                while i < n:
                    b = doc["blocks"][i]
                    t = block_text(b).strip()
                    if i in roles or not (b["tag"] == "li" or t.startswith("•")):
                        break
                    if i + 1 >= n:
                        break
                    d = doc["blocks"][i + 1]
                    if d["tag"] != "p" or block_text(d).strip().startswith("•"):
                        break
                    term, en = gloss_term(t)
                    key = first_key(b, anno_key)
                    items.append({"term": term, "en": en,
                                  "def": spans(d, anno_key), "a": key})
                    i += 2
                emit({"t": "gloss", "items": items})
                continue

        if tag == "li" or bulleted:
            emit({"t": "bullet", "s": spans(block, anno_key)})
            i += 1
            continue

        if section_kind == "goals" and re.match(r"^\d+\.\s", text):
            emit({"t": "bullet", "s": spans(block, anno_key)})
            i += 1
            continue

        b = {"t": "p", "s": spans(block, anno_key)}
        if text.startswith("★"):
            b["role"] = "prompt"
        tr = run_translation(block)
        if tr:
            b["trans"] = tr
        emit(b)
        i += 1

    for extra in inserts.get(n, []):
        emit(copy.deepcopy(extra))

    # ---- corrections --------------------------------------------------
    hits = {}
    # the trailing entry collapses double spaces left behind by the fixes above
    fixes = list(cfg["fixes"]) + [("  ", " ", None)]
    shown = {f[0]: f[3] for f in fixes if len(f) > 3}
    blocks = apply_fixes(blocks, fixes, hits)
    # appended blocks are transcribed by hand, so they skip the corrections
    unaligned = []
    blocks = mark_blanks(align_translations(promote_topics(
        normalize_spans(blocks + copy.deepcopy(cfg.get("append", [])))),
        unaligned))
    annotations = apply_fixes(annotations, fixes, hits)

    for key, extra in cfg.get("extraAnnotations", {}).items():
        annotations[key] = {
            "headword": extra.get("headword", key),
            "hanja": extra.get("hanja"),
            "meaning": extra.get("meaning"),
            "hanjaList": [{"char": c, "read": r, "gloss": g}
                          for c, r, g in extra.get("hanjaList", [])],
            "notes": list(extra.get("notes", [])),
            "surfaces": list(extra.get("surfaces", [])),
        }
    for a in annotations.values():
        a["headword"] = a["headword"].strip()

    # Notes are data, not markup: the page decides how to present them.
    notes = []
    for (old, new, why), count in hits.items():
        if why is None:
            continue
        was, now = shown.get(old, (old.lstrip("="), new))
        notes.append({"was": was, "now": now, "why": why, "count": count})
    notes += [{"why": n} if isinstance(n, str) else dict(n)
              for n in cfg.get("extraNotes", [])]
    unused = [f for f in fixes
              if (f[0], f[1], f[2]) not in hits and f[0] != f[1] and f[2]]

    lesson = {
        "number": cfg["number"], "unit": cfg["unit"], "title": cfg["title"],
        "titleEn": cfg["titleEn"], "tags": cfg["tags"],
        "chapterGloss": orphans,
        "blocks": blocks, "annotations": annotations, "notes": notes,
    }
    return lesson, unused, unaligned


BANNER = ("/* Generated by tools/build.py — do not edit.\n"
          "   Content lives in tools/chapters/%s; rebuild after changing it. */\n\n")


def write_payload(path, call, payload, source):
    """Write one content file: a registration call wrapping pure data."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(BANNER % source)
        f.write("KIIP.%s(" % call)
        json.dump(payload, f, ensure_ascii=False, indent=1)
        f.write(");\n")


def main():
    srcdir = os.path.expanduser(sys.argv[1] if len(sys.argv) > 1 else "~/Downloads")
    out = os.path.join(ROOT, "lessons")
    os.makedirs(out, exist_ok=True)

    manifest = []
    for cfg in CHAPTERS:
        lesson, unused, unaligned = build(cfg, srcdir)
        lesson["slug"] = cfg["slug"]
        write_payload(os.path.join(out, cfg["slug"] + ".js"), "chapter", lesson,
                      cfg["module"])
        manifest.append({k: cfg[k] for k in ("number", "slug", "title", "titleEn", "tags")})
        print("%-34s %3d blocks %3d annotations %2d notes %s" % (
            cfg["slug"], len(lesson["blocks"]), len(lesson["annotations"]),
            len(lesson["notes"]),
            "UNUSED FIXES: %s" % [u[0] for u in unused] if unused else ""))
        for where, got, want in unaligned:
            print("    translation left whole on %r: %d English paragraphs "
                  "against %d Korean" % (where[:40], got, want))

    write_payload(os.path.join(out, "manifest.js"), "manifest", manifest,
                  "chNN_*.py")
    if not CHAPTERS:
        print("no chapters found in tools/chapters/ — nothing to build")


if __name__ == "__main__":
    main()
