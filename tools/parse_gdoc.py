"""Parse a Google Docs HTML export into blocks + comments.

The export loses most semantics but keeps two things we need:
  * heading levels and paragraph/table boundaries
  * comment anchors — the commented run survives as its own <span>
    immediately before the <sup>[x]</sup> marker
"""

import json
import re
import sys
from html.parser import HTMLParser

BLOCK_TAGS = {"h1", "h2", "h3", "h4", "h5", "h6", "p", "li"}


class GDoc(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.blocks = []          # document body
        self.comments = {}        # label -> [paragraph, ...]
        self.cur = None           # current block being built
        self.runs = None          # runs of the current block
        self.in_body = False
        self.in_comment = None    # label of comment currently being read
        self.comment_depth = 0
        self.table = None
        self.row = None
        self.cell = None
        self.sup_label = None

    # -- helpers ---------------------------------------------------

    def push_run(self):
        self.runs.append({"text": "", "anno": []})

    def add_text(self, data):
        if self.runs is None:
            return
        if not self.runs:
            self.push_run()
        self.runs[-1]["text"] += data

    def open_block(self, tag):
        self.close_block()
        self.cur = tag
        self.runs = []

    def close_block(self):
        if self.cur is None:
            return
        runs = [r for r in self.runs if r["text"].strip() or r["anno"]]
        if runs:
            block = {"tag": self.cur, "runs": runs}
            if self.cell is not None:
                self.cell.append(block)
            else:
                self.blocks.append(block)
        self.cur = None
        self.runs = None

    # -- parser callbacks ------------------------------------------

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)

        if tag == "body":
            self.in_body = True
            return
        if not self.in_body:
            return

        # a comment body: <div class="c12"><p>...</p></div>
        if tag == "div" and self.in_comment is not None:
            self.comment_depth += 1

        if tag == "a" and a.get("id", "").startswith("cmnt") and not a.get("id", "").startswith("cmnt_ref"):
            # start of a comment definition
            self.close_block()
            self.in_comment = a["id"][4:]
            self.comments.setdefault(self.in_comment, [])
            self.runs = None
            return

        if tag == "a" and a.get("href", "").startswith("#cmnt") and not a.get("href", "").startswith("#cmnt_ref"):
            # in-text reference marker
            self.sup_label = a["href"][5:]
            return

        if tag == "table":
            self.close_block()
            self.table = {"tag": "table", "rows": []}
            return
        if tag == "tr" and self.table is not None:
            self.row = []
            return
        if tag in ("td", "th") and self.row is not None:
            self.cell = []
            return

        if tag == "span":
            if self.runs is not None:
                self.push_run()
            elif self.in_comment is not None:
                self.runs = []
                self.cur = "cmt"
            return

        if tag == "br":
            self.add_text("\n")
            return

        if tag in BLOCK_TAGS:
            if self.in_comment is not None:
                self.cur = "cmt"
                self.runs = []
            else:
                self.open_block(tag)

    def handle_endtag(self, tag):
        if tag == "body":
            self.close_block()
            self.in_body = False
            return
        if not self.in_body:
            return

        if self.in_comment is not None and tag in ("p", "div"):
            if self.runs:
                text = "".join(r["text"] for r in self.runs).strip()
                if text:
                    self.comments[self.in_comment].append(text)
            self.runs = None
            self.cur = None
            if tag == "div":
                if self.comment_depth:
                    self.comment_depth -= 1
                else:
                    self.in_comment = None
            return

        if tag in ("td", "th") and self.cell is not None:
            self.close_block()
            self.row.append(self.cell)
            self.cell = None
            return
        if tag == "tr" and self.row is not None:
            self.table["rows"].append(self.row)
            self.row = None
            return
        if tag == "table" and self.table is not None:
            self.blocks.append(self.table)
            self.table = None
            return

        if tag in BLOCK_TAGS:
            self.close_block()

    def handle_data(self, data):
        if not self.in_body:
            return
        if self.sup_label is not None:
            # data is the "[a]" label text; attach the ref to the previous run
            label = data.strip().strip("[]")
            if self.runs:
                target = None
                for r in reversed(self.runs):
                    if r["text"].strip():
                        target = r
                        break
                if target is not None:
                    target["anno"].append((self.sup_label, label))
            self.sup_label = None
            return
        self.add_text(data.replace("\xa0", " "))


def parse(path):
    src = open(path, encoding="utf-8").read()
    src = re.sub(r"<style.*?</style>", "", src, flags=re.S)
    p = GDoc()
    p.feed(src)

    # map numeric comment ids to their letter labels via the in-text refs
    labels = {}
    def walk(blocks):
        for b in blocks:
            if b["tag"] == "table":
                for row in b["rows"]:
                    for cell in row:
                        walk(cell)
                continue
            for r in b["runs"]:
                for cid, label in r["anno"]:
                    labels[cid] = label
    walk(p.blocks)

    comments = {labels.get(cid, cid): paras for cid, paras in p.comments.items()}
    return {"blocks": p.blocks, "comments": comments}


if __name__ == "__main__":
    for path in sys.argv[1:]:
        out = parse(path)
        dest = sys.argv[-1]
        print(json.dumps(out, ensure_ascii=False))
