#!/usr/bin/env python3
"""
Builder for Trial 04 ("Slab & Stencil" — neo-brutalism).

Usage:  python3 _tools/build-trial04.py

The pages are assembled from _tools/sections.py (shared page bodies), dressed by
the Skin04 class below, and written through _tools/shell.py. Only the pieces that
make this design this design live here: the hero poster, the marquee, the
dressing of panels and buttons, and the icon cut.

Editing the output HTML directly is fine too — but then stop running this script,
or the next run overwrites you.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import icons            # noqa: E402
import sections         # noqa: E402
import shell            # noqa: E402
from content import BRAND  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "trial-04-brutalist")

# Chunky ornaments in the same square-capped hand as the icons.
ORNAMENTS = [
    ("d-asterisk", '''
      <g fill="currentColor" stroke="currentColor" stroke-width="3">
        <path d="M32 4l6 20 18-13-13 18 20 6-20 6 13 18-18-13-6 20-6-20-18 13 13-18-20-6 20-6-13-18 18 13z"/>
      </g>'''),
    ("d-blocks", '''
      <g fill="currentColor" stroke="none">
        <rect x="2" y="20" width="12" height="24"/><rect x="18" y="10" width="12" height="44"/>
        <rect x="34" y="26" width="12" height="18"/><rect x="50" y="4" width="12" height="56"/>
      </g>'''),
    ("d-arrow-block", '''
      <g fill="currentColor" stroke="none">
        <path d="M4 26h30V14h12v12h14v12H46v12H34V38H4z"/>
      </g>'''),
]

MARQUEE = "25 showrooms ✳ 23 towns ✳ 20 brands ✳ open 10 to 9 ✳ since 1994 ✳ delivery &amp; installation "


class Skin04(sections.BaseSkin):
    label = "Trial 04 “Slab &amp; Stencil”"
    theme = "#1a1aff"
    fonts = ["archivo-black-latin-400-normal.woff2", "space-grotesk-latin-400-normal.woff2"]

    def sprite(self):
        return icons.sprite("brutal", extra=ORNAMENTS)

    # ------------------------------------------------------------------ hero
    def hero(self):
        poster = """
        <div class="hero__art">
          <div class="poster">
            <span class="poster__big">W</span>
            <span class="poster__row poster__row--alt">We drive the change</span>
            <span class="poster__row poster__row--grid"><span>TV</span><span>Fridge</span></span>
            <span class="poster__row poster__row--grid"><span>AC</span><span>Washer</span></span>
            <span class="poster__row">20 brands · one counter</span>
            <span class="poster__stamp">25 shops · 1 number</span>
          </div>
          <span class="hero__badge">Open 10 am to 9 pm</span>
        </div>"""

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
    %s
  </div>
</section>
""" % (self.kicker("Godavari districts · since 1994"),
       self.btn("See what we sell", "products.html", "ink", "i-cart"),
       self.btn("Find my showroom", "products.html", "cyan", "i-pin"),
       self.icon("i-check"), self.icon("i-people"), self.icon("i-truck"), poster)

    def after_hero(self):
        return """
<div class="marquee" aria-hidden="true">
  <div class="marquee__track"><span>%s</span><span>%s</span></div>
</div>
""" % (MARQUEE, MARQUEE)

    # -------------------------------------------------------------- dressing
    def title(self, text, cls=""):
        return '<h2 class="display%s">%s</h2>' % ((" " + cls) if cls else "", text)

    def extra_chips(self):
        return """<div class="chips" role="group" aria-label="Popular searches" style="margin:-6px 0 16px">
  <a class="chip" href="products.html?cat=water">%s Geysers</a>
  <a class="chip" href="products.html?cat=kitchen">%s Wet grinders</a>
  <a class="chip" href="products.html?cat=kitchen">%s Microwaves</a>
  <a class="chip" href="products.html?cat=tv">%s 55-inch TVs</a>
</div>""" % (self.icon("i-geyser"), self.icon("i-grinder"), self.icon("i-micro"), self.icon("i-tv"))

    def before_list(self):
        return ""

    def store_head(self):
        return ""

    # ---------------------------------------------------------------- bands
    def _slabs(self, labels, aria):
        cells = "".join('<span class="band-slab band-slab--%d">%s</span>' % (i % 4 + 1, l)
                        for i, l in enumerate(labels))
        return '<div class="band-slabs" role="img" aria-label="%s">%s</div>' % (aria, cells)

    def band_picture(self):
        return self._slabs(["Tanuku", "Tadepalligudem", "Rajahmundry", "Bhimavaram",
                            "Eluru", "Kakinada", "Palakollu", "Amalapuram"],
                           "Twenty-five WHYNOT showrooms across 23 towns")

    def band_picture_two(self):
        return self._slabs(["1994", "1996", "2006", "2025", "25 shops", "300 people",
                            "2.5M served", "We drive the change"],
                           "Thirty-two years of WHYNOT, in eight blocks")

    def page_hero(self, kicker, title, lead, ctas=None):
        buttons = ""
        for label, href, variant, icon in (ctas or []):
            buttons += self.btn(label, href, variant, icon)
        return """
<section class="stage stage--pagehero">
  <div class="wrap">
    <p class="kicker">%s</p>
    <h1 class="display display--xl">%s</h1>
    <p class="lede">%s</p>
    <div class="hero__cta">%s</div>
  </div>
</section>
""" % (kicker, title, lead, buttons)


def main():
    skin = Skin04()
    print("Building trial 04 (Slab & Stencil):")
    shell.build(ROOT, skin, "index.html", sections.home(skin), current="index.html")
    shell.build(ROOT, skin, "products.html", sections.catalogue_page(skin), current="products.html")
    shell.build(ROOT, skin, "stores.html", sections.stores_page(skin), current="stores.html")
    shell.build(ROOT, skin, "about.html", sections.about_page(skin), current="about.html")
    shell.build(ROOT, skin, "contact.html", sections.contact_page(skin), current="contact.html",
                extra_scripts=["assets/js/contact.js"])
    shell.build(ROOT, skin, "404.html", sections.notfound(skin))
    print("Done — six pages in trial-04-brutalist/")


if __name__ == "__main__":
    main()
