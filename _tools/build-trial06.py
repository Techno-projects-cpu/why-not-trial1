#!/usr/bin/env python3
"""
Builder for Trial 06 ("Brush & Bloom" — pastel, painterly).

Usage:  python3 _tools/build-trial06.py

Same structure and copy as trials 04 and 05 (see _tools/sections.py); what lives
here is the painting: the framed canvases, the feathered edges, the brush-stroke
dividers, and the soft pastel icon cut. This is the imagery-heavy direction of
the three, so it is also the largest download — the numbers are in the README.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import icons            # noqa: E402
import sections         # noqa: E402
import shell            # noqa: E402
from content import BRAND  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "trial-06-painting")

# Soft ornaments: a painter's blobs and a couple of swashes for the dividers.
ORNAMENTS = [
    ("d-bloom", '''
      <g fill="currentColor" stroke="none" opacity=".55">
        <circle cx="34" cy="34" r="17"/><circle cx="48" cy="24" r="10"/><circle cx="20" cy="44" r="8"/>
      </g>'''),
    ("d-flower", '''
      <g fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round">
        <circle cx="32" cy="32" r="6"/>
        <path d="M32 26c0-8 4-12 0-16M38 32c8 0 12 4 16 0M32 38c0 8-4 12 0 16M26 32c-8 0-12-4-16 0"/>
      </g>'''),
]

# three hand-written brush strokes for the section dividers
SWASHES = [
    ("swash--terra", "M6 14c26-16 52 12 84-4 16-8 34 2 48-2", "M14 20c22-8 44 6 68-2"),
    ("swash--moss", "M4 18c30-18 58 10 96-6", "M18 12c24 8 48-6 74 2"),
    ("swash--dusty", "M8 12c24 12 50-12 80 2 12 4 22 0 30-4", "M20 20c28-6 54 8 82-2"),
]


class Skin06(sections.BaseSkin):
    label = "Trial 06 “Brush &amp; Bloom”"
    theme = "#fbf7f0"
    fonts = ["fraunces-latin-400-normal.woff2", "karla-latin-400-normal.woff2"]

    def sprite(self):
        return icons.sprite("paint", extra=ORNAMENTS)

    def __init__(self):
        self._swash = 0

    # ------------------------------------------------------------- paintings
    def canvas(self, base, w, h, alt, eager=False, rotated=False, quote=None, by=None):
        frame = ' canvas--rotated-r' if rotated == "r" else (' canvas--rotated' if rotated else "")
        cap = ""
        if quote:
            cap = '<p class="canvas__quote">%s<span>%s</span></p>' % (quote, by or "")
        return """
<figure class="canvas%s">
  <div class="canvas__imgwrap">
    %s
  </div>
  %s
</figure>
""" % (frame, icons.picture(base, alt, w, h, eager=eager), cap)

    def band_picture(self):
        return icons.picture("fields-canal",
                             "Painting: paddy fields and an irrigation canal lined with coconut palms, "
                             "a village temple tower on the horizon and egrets in the field.", w=1400, h=640)

    def band_picture_two(self):
        return icons.picture("hero-landscape",
                             "Painting: a wide river at dawn with palms in the mist and herons in flight.",
                             w=1600, h=900)

    # ------------------------------------------------------------------ hero
    def hero(self):
        return """
<section class="hero">
  <div class="wrap hero__inner">
    <div class="hero__copy">
      %s
      <h1 class="display display--xl">Big brands.<br>Small towns.<br>Why not?</h1>
      <p class="hero__lead">Twenty-five WHYNOT showrooms in 23 towns, every major brand, and a phone number that still works five years after you buy. That has been the whole story since 1994.</p>
      <div class="hero__cta">
        %s
        %s
      </div>
      <ul class="hero__points">
        <li>%s 32 years</li>
        <li>%s 300 staff</li>
        <li>%s Delivery &amp; install</li>
      </ul>
    </div>
    <div class="hero__art">
      %s
    </div>
  </div>
</section>
""" % (self.kicker("Godavari districts · since 1994"),
       self.btn("See what we sell", "products.html", "ink", "i-cart"),
       self.btn("Find my showroom", "products.html", "ghost", "i-pin"),
       self.icon("i-check"), self.icon("i-people"), self.icon("i-truck"),
       self.canvas("hero-landscape", 1600, 900,
                   "Painting: a wide flat river at dawn, coconut palms fading into soft mist on both banks, "
                   "a blush and gold sky, herons in flight.",
                   eager=True, quote="We drive the change",
                   by="Tanuku, Andhra Pradesh · since 1994"))

    # -------------------------------------------------------------- dressing
    def swash(self):
        tone, a, b = SWASHES[self._swash % len(SWASHES)]
        self._swash += 1
        return ('<div class="swash %s" aria-hidden="true"><svg viewBox="0 0 200 24" fill="none" '
                'preserveAspectRatio="none">'
                '<path d="%s" stroke="currentColor" stroke-width="9" stroke-linecap="round"/>'
                '<path d="%s" stroke="currentColor" stroke-width="5" stroke-linecap="round" opacity=".55"/>'
                "</svg></div>\n" % (tone, a, b))

    def extra_chips(self):
        return """<div class="chips" role="group" aria-label="Popular searches" style="margin:-8px 0 16px">
  <a class="chip" href="products.html?cat=water">%s Geysers</a>
  <a class="chip" href="products.html?cat=kitchen">%s Wet grinders</a>
  <a class="chip" href="products.html?cat=kitchen">%s Microwaves</a>
  <a class="chip" href="products.html?cat=tv">%s 55-inch TVs</a>
</div>""" % (self.icon("i-geyser"), self.icon("i-grinder"), self.icon("i-micro"), self.icon("i-tv"))

    # --------------------------------------------------------------- heroes
    def page_hero(self, kicker, title, lead, ctas=None, art=None):
        buttons = "".join(self.btn(label, href, variant, icon) for label, href, variant, icon in (ctas or []))
        art_html = ""
        if art == "portrait":
            art_html = '<div class="pagehero__art">%s</div>' % self.canvas(
                "hills-sunset", 900, 1300,
                "Painting: green hills at sunset with coconut palms beside a winding path, mist in the "
                "valleys and a peach and lavender sky.", rotated="r")
        return """
<section class="stage stage--pagehero%s">
  <div class="wrap">
    <div class="pagehero__copy">
      %s
      <h1 class="display display--lg" style="margin-top:16px">%s</h1>
      <p class="lede">%s</p>
      <div class="hero__cta">%s</div>
    </div>
    %s
  </div>
</section>
""" % (" stage--pagehero--art" if art else "", self.kicker(kicker), title, lead, buttons, art_html)


def main():
    skin = Skin06()
    print("Building trial 06 (Brush & Bloom):")
    shell.build(ROOT, skin, "index.html", sections.home(skin), current="index.html")
    shell.build(ROOT, skin, "products.html", sections.catalogue_page(skin), current="products.html")
    shell.build(ROOT, skin, "stores.html", sections.stores_page(skin), current="stores.html")
    shell.build(ROOT, skin, "about.html", sections.about_page(skin), current="about.html")
    shell.build(ROOT, skin, "contact.html", sections.contact_page(skin), current="contact.html",
                extra_scripts=["assets/js/contact.js"])
    shell.build(ROOT, skin, "404.html", sections.notfound(skin))
    print("Done — six pages in trial-06-painting/")


if __name__ == "__main__":
    main()
