#!/usr/bin/env python3
"""
Contrast audit for Trial 07 — both modes.

Usage:  python3 _tools/contrast07.py

Trial 07 is the only direction with two designed palettes, so it needs two
measurements. The tokens are read out of the stylesheet (never retyped here), the
ratios are computed against the real WCAG formula, and every pair the design
actually puts on screen is listed with the target it has to meet:

  * 4.5:1 for body text and for small labels (WCAG AA, normal text);
  * 3.0:1 for large text (24px, or 19px bold) and for non-text marks like the
    focus ring, borders that carry meaning and the pressed chip;
  * nothing passes just because it looks fine on a good monitor.
"""

import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
CSS = os.path.join(REPO, "trial-07-slate", "assets", "css", "style.css")


def tokens():
    css = io.open(CSS, encoding="utf-8").read()
    light_src = css[css.index(":root {"):css.index("html[data-mode=\"dark\"]")]
    dark_src = css[css.index("html[data-mode=\"dark\"]"):css.index("* , *::before")]

    def read(src):
        out = {}
        for name, value in re.findall(r"(--[a-z0-9-]+)\s*:\s*([^;]+);", src):
            out[name] = value.strip()
        return out

    return read(light_src), read(dark_src)


def rgb(value):
    value = value.strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{6})", value)
    if m:
        h = m.group(1)
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    raise ValueError("cannot read colour %r" % value)


def lum(c):
    def f(v):
        v /= 255.0
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = c
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def ratio(fg, bg):
    a, b = lum(fg), lum(bg)
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)


# (foreground, background, minimum, what it is on screen)
PAIRS = [
    ("--ink", "--bg", 4.5, "body text on the page"),
    ("--ink", "--surface", 4.5, "body text on a panel"),
    ("--ink-2", "--surface", 4.5, "secondary text, lede on a panel"),
    ("--ink-3", "--surface", 4.5, "labels, notes and counts (small text)"),
    ("--ink-3", "--bg", 4.5, "notes on the page background"),
    ("--on-brand", "--brand", 4.5, "the primary button"),
    ("--brand", "--surface", 4.5, "links and current nav item"),
    ("--brand", "--bg", 4.5, "links on the page background"),
    ("--brand", "--brand-soft", 4.5, "badge and the current rail item"),
    ("--good", "--good-soft", 4.5, "the 'in my list' button"),
    ("--surface", "--ink", 4.5, "the pressed chip and the toast"),
    ("--warn", "--surface", 3.0, "warning marks (non-text)"),
    ("--brand", "--bg", 3.0, "focus ring against the page"),
    ("--brand", "--surface", 3.0, "focus ring against a panel"),
    ("--line-strong", "--surface", 1.2, "field borders (decoration only)"),
]


def main():
    light, dark = tokens()
    failures = 0
    for mode, toks in (("light", light), ("dark", dark)):
        print("\n  %s mode" % mode)
        for fg_name, bg_name, minimum, what in PAIRS:
            if fg_name not in toks or bg_name not in toks:
                print("  ! %s or %s missing from the tokens" % (fg_name, bg_name))
                failures += 1
                continue
            got = ratio(rgb(toks[fg_name]), rgb(toks[bg_name]))
            ok = got >= minimum
            failures += 0 if ok else 1
            print("  %-9s on %-14s %5.2f:1  (needs %.1f)  %-4s  %s"
                  % (fg_name, bg_name, got, minimum, "PASS" if ok else "FAIL", what))

    print("\n  %d of %d combinations below target." % (failures, len(PAIRS) * 2))
    if failures:
        print("  Colours need another pass in trial-07-slate/assets/css/style.css.")
        return 1
    print("  Both palettes pass, so the mode switch never drops text below AA.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
