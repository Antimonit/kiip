# -*- coding: utf-8 -*-
"""Write a Doc-sourced chapter's text into its own module.

Until now a chapter transcribed in a Google Doc was built from the HTML
export, which had to be sitting in ~/Downloads for the build to see it. This
reads the Doc one last time and writes what it found into the chapter module
itself, as `blocks` and `annotations`, so the chapter stands on its own like
the ones transcribed from the photos.

What it writes is the text *before* correction, exactly as the Doc has it, so
`fixes` and `approved` go on working: a correction can still be reviewed
against the page, and rejecting one still restores the book's own reading.

    python3 tools/convert.py --src ~/Downloads 05-housing [...]

Every block it writes is read back with the same helpers the module uses and
compared against what the Doc gave, so a chapter it cannot round-trip is
refused rather than half-written.
"""

import argparse
import os
import re
import sys
import textwrap

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import build                                                # noqa: E402
import chapters                                             # noqa: E402
from chapters import CHAPTERS, _spans                       # noqa: E402


WIDTH = 79


# --- Python source for a string ---------------------------------------

def literal(text):
    """One string as source: `"..."` per line, `"\\n\\n"` between paragraphs."""
    parts = []
    for i, para in enumerate(text.split("\n\n")):
        if i:
            parts.append('"\\n\\n"')
        parts.extend('"%s"' % chunk for chunk in wrap(para))
    return parts


def wrap(text):
    """A paragraph as the pieces of an implicitly concatenated literal."""
    text = text.replace("\\", "\\\\").replace('"', '\\"')
    if "\n" in text:
        text = text.replace("\n", "\\n")
    words, line, out = text.split(" "), "", []
    for w in words:
        piece = (line + " " + w) if line else w
        if len(piece) > 58 and line:
            out.append(line + " ")
            line = w
        else:
            line = piece
    out.append(line)
    return out or [""]


BREAK = "\x00"          # a token that asks for a line of its own


def call(name, args, indent):
    """`NAME(arg, arg)` flowed to the page width, continued under the name."""
    tokens = []
    for i, arg in enumerate(args):
        tokens.extend(arg if isinstance(arg, list) else [arg])
        if i < len(args) - 1:
            tokens.append(", ")
    return flow("%s%s(" % (" " * indent, name), tokens, "),")


def flow(head, tokens, closing):
    cont = " " * len(head)
    lines, cur = [], head
    for token in tokens:
        if token == BREAK:
            lines.append(cur.rstrip())
            cur = cont
            continue
        if token.startswith(","):
            cur += token          # a separator stays with what it follows
            continue
        if cur.strip() and len(cur) + len(token) > WIDTH:
            lines.append(cur.rstrip())
            cur = cont
        elif cur.endswith('"') and token.startswith('"'):
            cur += " "
        cur += token
    lines.append(cur.rstrip() + closing)
    return lines


# --- blocks -----------------------------------------------------------

MARKED = re.compile(r"[{}]")


def marked(span_list):
    """A span list as the `{word|headword}` text the helpers parse."""
    out = []
    for span in span_list:
        if isinstance(span, str):
            if MARKED.search(span):
                raise SystemExit("a brace in the text: %r" % span)
            out.append(span)
            continue
        word, key = span["word"], span["annotation"]
        extra = set(span) - {"word", "annotation"}
        if extra:
            raise SystemExit("unexpected span field(s) %s" % sorted(extra))
        out.append("{%s}" % word if key == word
                   else "{%s|%s}" % (word, key))
    return "".join(out)


def cell(c):
    if isinstance(c, str):
        return literal(c)
    if isinstance(c, (int, float)):
        return [repr(c)]
    extra = set(c) - {"text", "span", "spanDown"}
    if extra:
        raise SystemExit("unexpected cell field(s) %s" % sorted(extra))
    args = literal(c["text"])
    if c.get("span"):
        args = args + [", columns=%d" % c["span"]]
    if c.get("spanDown"):
        args = args + [", down=%d" % c["spanDown"]]
    return ["CELL("] + args + [")"]


def rows(table_rows):
    """A table's rows as one bracketed argument, a row to a line."""
    out = ["["]
    for i, row in enumerate(table_rows):
        if i:
            out.append(BREAK)
        out.append("[")
        for j, c in enumerate(row):
            out.extend(cell(c))
            if j < len(row) - 1:
                out.append(", ")
        out.append("]" + ("," if i < len(table_rows) - 1 else ""))
    out.append("]")
    return out


def spanned(items):
    """A list of span lists — labels, margin notes, verse lines."""
    out = []
    for i, item in enumerate(items):
        out.extend(literal(marked(item)))
        if i < len(items) - 1:
            out.append(", ")
    return out


def block_source(b, indent=8):
    """One block as the helper call that builds it."""
    kind, seen = b["type"], set(b)

    def only(*allowed):
        extra = seen - {"type"} - set(allowed)
        if extra:
            raise SystemExit("%s block has unhandled field(s) %s"
                             % (kind, sorted(extra)))

    if kind == "section":
        only("kind", "text")
        return call("SECTION", [literal(b["kind"]), literal(b["text"])], indent)

    if kind == "heading":
        only("level", "text", "translation")
        args = [str(b["level"]), literal(b["text"])]
        if b.get("translation"):
            args.append(["translation="] + literal(b["translation"]))
        return call("HEADING", args, indent)

    if kind == "paragraph":
        only("spans", "role", "translation")
        text = marked(b["spans"])
        if b.get("role") not in (None, "prompt"):
            raise SystemExit("paragraph role %r" % b["role"])
        if (b.get("role") == "prompt") != text.startswith("★"):
            raise SystemExit("prompt role does not follow the star: %r" % text)
        args = [literal(text)]
        if b.get("translation"):
            args.append(["translation="] + literal(b["translation"]))
        return call("PARAGRAPH", args, indent)

    if kind == "bullet":
        only("spans", "ordered", "level")
        args = [literal(marked(b["spans"]))]
        if b.get("ordered"):
            args.append("ordered=True")
        if b.get("level", 1) != 1:
            args.append("level=%d" % b["level"])
        return call("BULLET", args, indent)

    if kind == "glossary":
        only("entries")
        args = []
        for e in b["entries"]:
            extra = set(e) - {"term", "definition", "annotation", "handwritten"}
            if extra:
                raise SystemExit("glossary entry field(s) %s" % sorted(extra))
            piece = ["("] + literal(e["term"]) + [", "] \
                + literal(marked(e["definition"]))
            if e.get("annotation") or e.get("handwritten"):
                piece += [", "] + (literal(e["annotation"])
                                   if e.get("annotation") else ["None"])
            if e.get("handwritten"):
                piece += [", "] + literal(e["handwritten"])
            args.append(([BREAK] if args else []) + piece + [")"])
        return call("GLOSSARY", args, indent)

    if kind == "table":
        only("header", "rows")
        args = []
        if "header" in b:
            args.append(["["] + [x for c in b["header"]
                                 for x in cell(c) + [", "]][:-1] + ["]"])
        args.append(rows(b["rows"]))
        return call("TABLE", args, indent)

    if kind == "labels":
        only("items", "groups")
        if "groups" in b:
            args = []
            for g in b["groups"]:
                args.append(["GROUP("] + literal(marked(g["name"]))
                            + [", "] + spanned(g["items"]) + [")"])
            return call("LABELS", args, indent)
        return call("LABELS", [spanned(b["items"])], indent)

    if kind == "margin":
        only("items")
        return call("MARGIN", [spanned(b["items"])], indent)

    if kind == "verse":
        only("lines")
        return call("VERSE", [spanned(b["lines"])], indent)

    if kind == "figure":
        only("text")
        return call("FIGURE", [literal(b["text"])], indent)

    if kind == "source":
        only("text")
        return call("SOURCE", [literal(b["text"])], indent)

    if kind == "chart":
        only("caption", "unit", "rows")
        return call("CHART", [literal(b["caption"]), literal(b["unit"]),
                              rows(b["rows"])], indent)

    raise SystemExit("no helper writes a %s block" % kind)


HELPERS = {"section": "SECTION", "heading": "HEADING",
           "paragraph": "PARAGRAPH", "bullet": "BULLET",
           "glossary": "GLOSSARY", "table": "TABLE",
           "labels": "LABELS", "margin": "MARGIN", "verse": "VERSE",
           "figure": "FIGURE", "source": "SOURCE", "chart": "CHART"}


# --- annotations ------------------------------------------------------

def annotation_source(key, a, indent=8):
    """One annotation entry as the `"key": dict(...)` it is written as."""
    pad = " " * indent
    lines = ["%s%s: dict(" % (pad, "".join(literal(key)))]
    inner = pad + " " * 4
    if a.get("headword") and a["headword"] != key:
        lines += fold(inner, "headword=", literal(a["headword"]), ",")
    if a.get("hanja"):
        lines += fold(inner, "hanja=", literal(a["hanja"]), ",")
    if a.get("meaning"):
        lines += fold(inner, "meaning=", literal(a["meaning"]), ",")
    if a.get("characters"):
        pieces = []
        for c in a["characters"]:
            reading = (literal(c["reading"]) if c.get("reading")
                       else ["None"])
            pieces.append(["("] + literal(c["char"]) + [", "] + reading
                          + [", "] + literal(c["gloss"] or "") + [")"])
        lines += fold(inner, "characters=[",
                      [x for p in pieces for x in p + [", "]][:-1] + ["]"], ",")
    if a.get("notes"):
        pieces = []
        for n in a["notes"]:
            pieces.append(literal(n))
        lines += fold(inner, "notes=[",
                      [x for p in pieces for x in p + [", "]][:-1] + ["]"], ",")
    if a.get("surfaces"):
        pieces = [literal(s) for s in a["surfaces"]]
        lines += fold(inner, "surfaces=[",
                      [x for p in pieces for x in p + [", "]][:-1] + ["]"], ",")
    lines.append("%s)," % inner[:-4])
    return lines


def fold(pad, opening, pieces, closing):
    """`opening` then `pieces`, wrapped, `closing` on the end."""
    lines, cur = [], pad + opening
    cont = pad + " " * 4
    for piece in pieces:
        if cur.strip() != opening.strip() and len(cur) + len(piece) > WIDTH:
            lines.append(cur.rstrip())
            cur = cont
        cur += piece
    lines.append(cur.rstrip() + closing)
    return lines


# --- rewriting the module ---------------------------------------------

def matched(text, j):
    """The position just past the bracket opened at `j`."""
    depth = 0
    while True:
        ch = text[j]
        if ch in "([{":
            depth += 1
        elif ch in ")]}":
            depth -= 1
            if depth == 0:
                return j + 1
        elif ch == '"':
            j = text.index('"', j + 1)
        j += 1


def drop_key(text, key):
    """Remove a top-level `key=<value>,` from the CHAPTER dict."""
    m = re.search(r"^    %s=" % key, text, re.M)
    if not m:
        return text, False
    j = m.end()
    while text[j] == " ":
        j += 1
    if text[j] == '"':
        j = text.index('"', j + 1) + 1
    elif re.match(r"[A-Za-z_]+\(", text[j:]):
        j = text.index("(", j)
        j = matched(text, j)
    elif text[j] in "([{":
        j = matched(text, j)
    else:
        j = text.index("\n", j)
    while j < len(text) and text[j] in ", ":
        j += 1
    if text[j:j + 1] == "\n":
        return text[:m.start()] + text[j + 1:], True
    return text[:m.start()] + "    " + text[j:], True


ORDER = ("SECTION", "HEADING", "PARAGRAPH", "BULLET", "SOURCE", "FIGURE",
         "LABELS", "GROUP", "MARGIN", "VERSE", "TABLE", "CELL", "CHART",
         "GLOSSARY")


def imports(text, used):
    """Rewrite the module's `from . import` line to what the text now needs.

    The module may already import helpers for blocks of its own in `append`,
    so those are kept alongside the ones the converted text asks for.
    """
    old = re.search(r"^from \. import ([^\n]*(?:\n    [^\n]*)*)$", text, re.M)
    if old:
        used = set(used) | set(re.findall(r"[A-Z]+", old.group(1)))
    names = [n for n in ORDER if n in used]
    line = "from . import " + ", ".join(names)
    if len(line) > WIDTH:
        pieces = [n + (", " if i < len(names) - 1 else "")
                  for i, n in enumerate(names)]
        line = "\n".join(flow("from . import (", pieces, ")"))
    if old:
        return text[:old.start()] + line + text[old.end():]
    return text


DOC_LINE = re.compile(
    r"Source: (\d+\.html) \(Google Docs HTML export\)([.,])")


def restate_source(text):
    """Say where the chapter's text came from, now that it lives here."""
    m = DOC_LINE.search(text)
    if not m:
        return text
    end = min(x for x in (text.find('\n\n', m.start()),
                          text.find('\n"""', m.start())) if x > 0)
    para = " ".join(text[:end].split("\n\n")[-1].split())
    start = end - len(text[:end].split("\n\n")[-1])
    para = DOC_LINE.sub(
        lambda x: "Transcribed in your Google Doc (%s), whose text is carried "
                  "in `blocks` below as the Doc had it%s" % (x.group(1),
                                                             x.group(2)),
        para)
    return text[:start] + "\n".join(textwrap.wrap(para, 78)) + text[end:]


def convert(cfg, srcdir):
    blocks, annotations, orphans, _fixes, _hits = build.from_doc(cfg, srcdir)
    build.normalize_spans(blocks)

    used, lines = set(), []
    for b in blocks:
        used.add(HELPERS[b["type"]])
        if b["type"] == "labels" and "groups" in b:
            used.add("GROUP")
        if b["type"] == "table":
            for c in list(b.get("header", [])) + [x for r in b["rows"] for x in r]:
                if isinstance(c, dict):
                    used.add("CELL")
        lines.extend(block_source(b))

    # read it back the way the module will, and refuse anything that differs
    scope = {n: getattr(chapters, n) for n in dir(chapters) if n.isupper()}
    read = eval("[\n%s\n]" % "\n".join(lines), dict(scope))       # noqa: S307
    build.normalize_spans(read)
    if read != blocks:
        for a, b in zip(read, blocks):
            if a != b:
                raise SystemExit("round-trip differs:\n  %r\n  %r" % (b, a))
        raise SystemExit("round-trip differs in length: %d vs %d"
                         % (len(read), len(blocks)))

    body = ["    blocks=["] + lines + ["    ],"]
    if annotations:
        body.append("    annotations={")
        for key, a in annotations.items():
            body.extend(annotation_source(key, a))
        body.append("    },")
    if orphans:
        body.extend(fold("    ", "chapterGlossary=[",
                         [", ".join('"%s"' % o for o in orphans)] + ["]"], ","))

    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "chapters", cfg["module"])
    text = restate_source(open(path, encoding="utf-8").read())
    for key in ("src", "roles", "insert", "chart", "kinship"):
        text, _ = drop_key(text, key)
    text = text.replace('CHAPTER = dict(\n    number=', 'CHAPTER = dict(\n    number=')
    anchor = re.search(r"^    unit=.*titleEn=.*$", text, re.M)
    if not anchor:
        raise SystemExit("%s: cannot find the title line" % cfg["module"])
    text = (text[:anchor.end()] + "\n\n" + "\n".join(body)
            + text[anchor.end():])
    text = imports(text, used)
    open(path, "w", encoding="utf-8").write(text)
    return len(blocks), len(annotations)


SHAPES = [
    {"type": "section", "kind": "warmup", "text": "생각해 봅시다"},
    {"type": "heading", "level": 3, "text": "국회",
     "translation": "The Assembly\n\nBody text."},
    {"type": "paragraph", "translation": "Making law.",
     "spans": ["법을 ", {"word": "만드는", "annotation": "만들다"}, " 일"]},
    {"type": "paragraph", "spans": ["★ 이야기해 봅시다."], "role": "prompt"},
    {"type": "bullet", "spans": ["첫째"], "ordered": True},
    {"type": "bullet", "spans": ["안쪽"], "level": 2},
    {"type": "glossary", "entries": [{"term": "세", "definition": ["내는 돈"],
                                      "annotation": "세",
                                      "handwritten": "rent"}]},
    {"type": "table", "header": [{"text": "영역", "span": 2}, "제목"],
     "rows": [[{"text": "기본", "spanDown": 2}, "정치", "20. 한국의 민주 정치"]]},
    {"type": "table", "rows": [["가", "나"]]},
    {"type": "labels",
     "groups": [{"name": [{"word": "단독 주택", "annotation": "단독 주택"}],
                 "items": [["양옥"], ["한옥"]]}]},
    {"type": "labels", "items": [["엿"], ["찹쌀떡"]]},
    {"type": "margin", "items": [["스세권"]]},
    {"type": "verse", "lines": [["대한민국은 민주공화국이다."]]},
    {"type": "figure", "text": "국회의사당"},
    {"type": "source", "text": "[출처] 한겨레"},
    {"type": "chart", "caption": "도시화율", "unit": "%",
     "rows": [["1960년", 39.1]]},
]


def selftest():
    """Write one block of every shape and read it back.

    Nothing has a `src` any more, so the conversion itself no longer runs
    over anything. This keeps the writer honest for the next Doc that
    arrives, and catches a helper renamed out from under it.
    """
    lines = []
    for b in SHAPES:
        lines.extend(block_source(b))
    scope = {n: getattr(chapters, n) for n in dir(chapters) if n.isupper()}
    read = eval("[\n%s\n]" % "\n".join(lines), dict(scope))       # noqa: S307
    for want, got in zip(SHAPES, read):
        if want != got:
            raise SystemExit("round-trip differs:\n  %r\n  %r" % (want, got))
    if len(read) != len(SHAPES):
        raise SystemExit("round-trip lost a block")
    print("%d block shapes written and read back" % len(SHAPES))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slugs", nargs="*")
    ap.add_argument("--src", default=os.path.expanduser("~/Downloads"))
    ap.add_argument("--selftest", action="store_true",
                    help="write one block of every shape and read it back")
    args = ap.parse_args()

    if args.selftest:
        return selftest()

    for cfg in CHAPTERS:
        if args.slugs and cfg["slug"] not in args.slugs:
            continue
        if not cfg.get("src"):
            continue
        if not os.path.exists(os.path.join(args.src, cfg["src"])):
            print("%-34s SOURCE MISSING (%s)" % (cfg["slug"], cfg["src"]))
            continue
        blocks, annotations = convert(cfg, args.src)
        print("%-34s %3d blocks %3d annotations written into the module"
              % (cfg["slug"], blocks, annotations))


if __name__ == "__main__":
    main()
