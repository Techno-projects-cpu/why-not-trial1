#!/usr/bin/env python3
"""
Contrast audit for the glassmorphism trial.

Usage:  python3 _tools/contrast.py

Glass is the one direction in this repo where readability can quietly fail: white
text sits on a translucent sheet, which sits on a lit backdrop. So rather than
trusting the look, this reads the actual alpha values out of
trial-05-glass/assets/css/style.css, composites the real layer stack, and computes
WCAG 2.1 contrast ratios against the WORST-CASE backdrop — a nearly white bloom
in the light study — not the average one. If a value it expects is missing, it
says so instead of guessing.

Layer stack, bottom to top:
  1. the backdrop pixel        (255,255,255) worst case / the real dark areas
  2. .bg__wash                 the dark wash, alpha read from the CSS
  3. the surface               .panel / .tile / .card / .stat tint floor
  4. the text                  white at the alpha the CSS declares

AA needs 4.5:1 for body text and 3:1 for large text.
"""

import io
import os
import re
import sys

CSS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                   "trial-05-glass", "assets", "css", "style.css")

TINT = (10, 12, 30)
BLACK = (0, 0, 0)


def read_css():
    s = io.open(CSS, encoding="utf-8").read()
    got = {}

    def alpha(pattern, name, group=1):
        m = re.search(pattern, s)
        if not m:
            sys.exit("contrast.py: could not find %s in style.css — the audit is out of date" % name)
        got[name] = float("0." + m.group(group))   # ".58" -> 0.58, not 58
        return got[name]

    alpha(r"--text-soft:\s*rgba\(255,\s*255,\s*255,\s*\.(\d+)\)", "text_soft")
    alpha(r"--text-faint:\s*rgba\(255,\s*255,\s*255,\s*\.(\d+)\)", "text_faint")
    alpha(r"\.panel\s*\{[^}]*background-color:\s*rgba\(var\(--tint\),\s*\.(\d+)\)", "panel")
    alpha(r"\.tile\s*\{[^}]*rgba\(var\(--tint\),\s*\.(\d+)\)", "tile")
    alpha(r"\.card\s*\{[^}]*rgba\(var\(--tint\),\s*\.(\d+)\)", "card")
    alpha(r"\.stat\s*\{[^}]*rgba\(var\(--tint\),\s*\.(\d+)\)", "stat")
    alpha(r"\.store\s*\{[^}]*rgba\(var\(--tint\),\s*\.(\d+)\)", "store")
    alpha(r"\.band\s*\{[^}]*rgba\(var\(--tint\),\s*\.(\d+)\)", "band")
    alpha(r"\.chip\s*\{[^}]*rgba\(var\(--tint\),\s*\.(\d+)\)", "chip")
    alpha(r"\.kicker\s*\{[^}]*rgba\(var\(--tint\),\s*\.(\d+)\)", "kicker")
    alpha(r"\.head\s*\{[^}]*rgba\(var\(--tint\),\s*\.(\d+)\)", "head_plate")
    alphas = re.search(r"\.bg__wash\s*\{[^}]*?\.(\d+)\)\s*0%.*?\.(\d+)\)\s*55%.*?\.(\d+)\)\s*100%",
                       s, re.S)
    if not alphas:
        sys.exit("contrast.py: could not read the .bg__wash gradient — the audit is out of date")
    got["wash_top"], got["wash_mid"], got["wash_bottom"] = (float("0." + x) for x in alphas.groups())
    return got


def over(fg, a, bg):
    return tuple(a * f + (1 - a) * b for f, b in zip(fg, bg))


def lum(c):
    def f(v):
        v /= 255.0
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (f(x) for x in c)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(a, b):
    la, lb = lum(a), lum(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def main():
    c = read_css()
    print("Trial 05 “Glass & Glow” — measured contrast")
    print("  (alphas read from the stylesheet, not from this file)\n")

    results = []

    def case(name, text_alpha, surface_alpha, wash_alpha, backdrop, size="body"):
        beneath = over(TINT, wash_alpha, backdrop)
        sheet = over(TINT, surface_alpha, beneath) if surface_alpha else beneath
        text = over((255, 255, 255), text_alpha, sheet)
        r = ratio(text, sheet)
        need = 4.5 if size == "body" else 3.0
        ok = r >= need
        results.append((name, r, need, ok))
        print("  %-52s %5.2f:1  (needs %.1f)  %s" % (name, r, need, "PASS" if ok else "FAIL"))
        return ok

    for label, backdrop in (("worst case — a white bloom behind the glass", (255, 255, 255)),
                            ("typical — the dark part of the light study", (28, 24, 62))):
        print("  %s" % label)
        case("heading (full white) on a .panel", 1.0, c["panel"], c["wash_top"], backdrop, "large")
        case("body text on a .panel", c["text_soft"], c["panel"], c["wash_top"], backdrop)
        case("small label on a .panel", c["text_faint"], c["panel"], c["wash_top"], backdrop)
        case("body text on a .stat tile", c["text_soft"], c["stat"], c["wash_mid"], backdrop)
        case("body text on a .tile", c["text_soft"], c["tile"], c["wash_mid"], backdrop)
        case("body text on a .card", c["text_soft"], c["card"], c["wash_mid"], backdrop)
        case("showroom address in a .store", c["text_soft"], c["store"], c["wash_mid"], backdrop)
        case("band caption in a .band", c["text_soft"], c["band"], c["wash_mid"], backdrop)
        case("filter chip label", 1.0, c["chip"], c["wash_top"], backdrop)
        case("kicker chip label", 1.0, c["kicker"], c["wash_top"], backdrop)
        case("section heading on the .head plate", 1.0, c["head_plate"], c["wash_top"], backdrop, "large")
        case("section lede on the .head plate", c["text_soft"], c["head_plate"], c["wash_top"], backdrop)
        print()

    bad = [r for r in results if not r[3]]
    print("  %d of %d combinations below target." % (len(bad), len(results)))
    if bad:
        print("  Failing: %s" % ", ".join(n for n, _, _, _ in bad))
        print("  Raise the surface tint floor, the text alpha, or the top of the wash until this list is empty.")
        return 1
    print("  Every combination passes, including the worst case.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
