#!/usr/bin/env python3
"""
Which visible words on Trial 07's pages have no entry in the language table?

Usage:  python3 _tools/missing07.py

Hooking is driven by the table in _tools/i18n.py plus _tools/i18n07.py, so a
sentence that is not in there stays English in all three languages — easy to do
by accident while editing a page, and invisible unless you switch language and
read every screen. This lists them, at the same granularity the hooker works:
the leaf elements, plus any element whose whole text is one table phrase (a
sentence with a <strong> or a <br> in the middle is one phrase, not three).

Deliberately not listed: proper nouns and place names (a transliterated address
helps nobody show a driver where to go), numbers and email addresses, the
single-letter brand mark, and anything inside <script>, <style>, <title>,
<desc> or an .sr label.
"""

import glob
import io
import os
import re
import sys
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
REPO = os.path.dirname(HERE)

import i18n  # noqa: E402

# names that stay in Latin script on purpose
KEEP = set("""WHYNOT Electronics Tanuku Tadepalligudem Rajahmundry Bhimadolu Nidadavolu
Narasapuram Palakollu Jangareddygudem Devarapalli Amalapuram Tatipaka Ravulapalem Mandapeta Eluru
Yeleswaram Pithapuram Chintalapudi Nallajarla Attili Bhimavaram Anakapalle Kakinada Kovvur
Godavari West East Visakhapatnam Bengal Bay India EN te hi LLM LML Bajaj LG Samsung
Smart Plaza LED QLED HDMI EMI TV CCTV AM PM Rs Mr Mrs Pvt Ltd No Concept
Jujjavarapu Venkata Rayudu Sridevi Mounika Muttavarapu Siddharth Venkatram Sri Sowdha Towers
Undrajavaram Road Andhra Pradesh Ground Cellar""".split())

VOID = {"br", "img", "hr", "input", "meta", "link", "source", "use"}
SKIP_TAGS = {"script", "style", "title", "desc"}


def normalise(text):
    return re.sub(r"\s+", " ", text).strip()


def ignorable(word):
    return (word in KEEP or word.upper() in KEEP or not word[0].isalpha()
            or "@" in word or word.replace("+", "").isdigit())


def looks_like_a_name(text):
    words = re.findall(r"[A-Za-z0-9\u00c0-\u024f'\u2019./-]+", text)
    return bool(words) and all(ignorable(w) for w in words)


def variants(phrase):
    """The same phrase as the page may write it: <br> is a newline, tags go."""
    plain = re.sub(r"<br\s*/?>", "\n", phrase)
    plain = re.sub(r"<[^>]+>", "", plain)
    out = {normalise(phrase), normalise(plain), normalise(plain.replace("\n", " "))}
    return {v for v in out if v}


def build_tree(html):
    """A plain element tree: (tag, cls, text, children, parent)."""
    nodes = [(None, "", "", [], None)]

    class P(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.stack = [0]

        def handle_starttag(self, tag, attrs):
            if tag in VOID:
                if tag == "br":
                    nodes[self.stack[-1]][2] and None
                    nodes[self.stack[-1]] = (nodes[self.stack[-1]][0], nodes[self.stack[-1]][1],
                                             nodes[self.stack[-1]][2] + "\n", nodes[self.stack[-1]][3],
                                             nodes[self.stack[-1]][4])
                return
            cls = dict(attrs).get("class", "")
            nodes.append((tag, cls, "", [], self.stack[-1]))
            nodes[self.stack[-1]][3].append(len(nodes) - 1)
            self.stack.append(len(nodes) - 1)

        def handle_endtag(self, tag):
            if len(self.stack) > 1:
                self.stack.pop()

        def handle_data(self, data):
            i = self.stack[-1]
            nodes[i] = (nodes[i][0], nodes[i][1], nodes[i][2] + data, nodes[i][3], nodes[i][4])

    P().feed(html)
    return nodes


def skipped(node, nodes):
    """True if this node or any ancestor is script/style/title/desc/an .sr label."""
    while node is not None:
        tag, cls = nodes[node][0], nodes[node][1]
        if tag in SKIP_TAGS or "sr" in cls.split() or "brand__mark" in cls.split():
            return True
        node = nodes[node][4]
    return False


def words(text):
    """The words of a phrase, order ignored — a parent's text arrives with its
    children appended where they were not written, so order is not evidence."""
    return sorted(re.findall(r"[A-Za-z0-9\u00c0-\u024f'\u2019.-]+", text))


def full_texts(nodes):
    """Each element's text including everything its children say."""
    full = [None] * len(nodes)
    for i in range(len(nodes) - 1, -1, -1):
        text = nodes[i][2]
        for child in nodes[i][3]:
            if full[child]:
                text += " " + full[child]
        full[i] = normalise(text)
    return full


def is_data(text):
    """Contact data, not copy: an email, a phone line, an address, a person."""
    if "@" in text or re.search(r"\b\d{6}\b", text) or re.search(r"\b\d{5}\b", text):
        return True
    return bool(re.match(r"^(Mr|Mrs|Ms|Dr)\.?\s", text))


def main():
    table = set()
    for key, entry in i18n.LOCALISABLE.items():
        for text in (key, entry.get("en", "")):
            if text:
                table |= variants(text)

    word_sets = set(frozenset(words(t)) for t in table if len(t) > 24)

    def covered(text):
        return normalise(text) in table or looks_like_a_name(text)

    def is_a_phrase_reordered(text):
        return len(text) > 24 and frozenset(words(text)) in word_sets

    pages = sorted(glob.glob(os.path.join(REPO, "trial-07-slate", "*.html")))
    missing = {}
    for page in pages:
        nodes = build_tree(io.open(page, encoding="utf-8").read())
        full = full_texts(nodes)
        gaps = []
        for i, (tag, cls, text, children, parent) in enumerate(nodes):
            if not tag or children:
                continue                      # leaves only; parents are phrases
            if len(text.strip()) < 2 or not re.search(r"[A-Za-z]", text) or skipped(i, nodes):
                continue
            if covered(text) or is_data(text):
                continue
            # a leaf inside a sentence that is itself one phrase is fine
            run, inside = parent, False
            while run is not None:
                # only a *sentence-sized* ancestor can stand in for this phrase:
                # the page, the body and every wrapper above them hold the whole
                # document, and a document always contains a phone number
                if len(full[run]) < 160 and (covered(full[run]) or is_data(full[run])):
                    inside = True
                    break
                if covered(full[run]) or is_a_phrase_reordered(full[run]):
                    inside = True
                    break
                run = nodes[run][4]
            if inside:
                continue
            gaps.append(normalise(text))
        if gaps:
            missing[os.path.basename(page)] = sorted(set(gaps))

    print("pages checked: %d" % len(pages))
    if not missing:
        print("every visible phrase on Trial 07 has a translation")
        return 1
    print("phrases with no translation: %d" % sum(len(v) for v in missing.values()))
    for page, gaps in missing.items():
        print("\n  %s" % page)
        for gap in gaps:
            print("    %s" % gap[:160])
    return 0


if __name__ == "__main__":
    sys.exit(main())
