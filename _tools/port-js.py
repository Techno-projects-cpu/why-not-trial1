#!/usr/bin/env python3
"""
Port the JavaScript from Trial 03 to another trial.

Usage:  python3 _tools/port-js.py 04 05 06
        (or: python3 _tools/port-js.py all)

Trial 03's four scripts already talk to the markup contract that
_tools/sections.py renders — [data-products], [data-list-panel], [data-store-list]
and so on — so a new trial needs the same behaviour with its own storage key and
its own design's class names. This script does exactly that and nothing else, so
the catalogue logic stays in one place instead of being copied by hand and
drifting. Anything it cannot map is printed rather than silently dropped.
"""

import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
SRC = os.path.join(REPO, "trial-03-anime", "assets", "js")
FILES = ("main.js", "products.js", "stores.js", "contact.js")

# target key -> (directory, label used in the file header, storage key)
TRIALS = {
    "04": ("trial-04-brutalist", "Trial 04 · Slab & Stencil", "whynot-list-t4"),
    "05": ("trial-05-glass", "Trial 05 · Glass & Glow", "whynot-list-t5"),
    "06": ("trial-06-painting", "Trial 06 · Brush & Bloom", "whynot-list-t6"),
}

# class names that changed between trial 03's markup and the shared contract in
# sections.py. Left-hand side is what trial 03 emits, right-hand what 04–06 use.
RENAMES = [
    ('class="hero__cta"', 'class="actions"'),
    ('class="shout shout--sm"', 'class="display display--xs"'),
    ('class="h3"', 'class="display display--xs"'),
    ("btn--marker", "btn--brand"),
    ('class="link"', 'class="band__link"'),
]


def port(key):
    target, label, store_key = TRIALS[key]
    dest = os.path.join(REPO, target, "assets", "js")
    os.makedirs(dest, exist_ok=True)
    print("%s → %s" % (target, dest))
    for name in FILES:
        s = io.open(os.path.join(SRC, name), encoding="utf-8").read()
        before = s
        for old, new in RENAMES:
            s = s.replace(old, new)
        s = s.replace("Trial 03 · catalogue +", label + " · catalogue +")
        s = s.replace("Trial 03 · showroom directory", label + " · showroom directory")
        s = s.replace("Trial 03 · the enquiry form", label + " · the enquiry form")
        s = s.replace("/* WHYNOT — Trial 03 runtime.", "/* WHYNOT — %s runtime." % label)
        s = s.replace('var STORE_KEY = "whynot-list-t3";', 'var STORE_KEY = "%s";' % store_key)

        # report anything that still smells of trial 03, rather than hiding it
        leftovers = [t for t in ("trial-03", "Trial 03", "whynot-list-t3", "shout", "hero__cta")
                     if t in s]
        io.open(os.path.join(dest, name), "w", encoding="utf-8").write(s)
        print("   %-12s %6d bytes  %s" % (name, len(s),
                                          ("leftovers: " + ", ".join(leftovers)) if leftovers else "clean"))


if __name__ == "__main__":
    args = sys.argv[1:] or ["all"]
    keys = list(TRIALS) if "all" in args else args
    for k in keys:
        if k not in TRIALS:
            sys.exit("unknown trial %r — expected one of %s" % (k, ", ".join(TRIALS)))
        port(k)
