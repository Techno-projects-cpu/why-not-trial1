#!/usr/bin/env python3
"""
Builder for Trial 05 ("Glass & Glow" — glassmorphism).

Usage:  python3 _tools/build-trial05.py

Structure, copy and behaviour are identical to Trial 04 (see _tools/sections.py).
This file supplies only what makes the design itself: the lit backdrop, the hero
sheet floating over the light study, the hairline icon cut, and the pill bands.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import icons            # noqa: E402
import sections         # noqa: E402
import shell            # noqa: E402
from content import BRAND  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "trial-05-glass")

ORNAMENTS = [
    ("d-orb", '''
      <g fill="none" stroke="currentColor" stroke-width="1.6">
        <circle cx="32" cy="32" r="26" opacity=".45"/><circle cx="32" cy="32" r="17" opacity=".65"/><circle cx="32" cy="32" r="8"/>
      </g>'''),
    ("d-prism", '''
      <g fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round">
        <path d="M32 6l22 40H10z"/><path d="M32 6v40M10 46l22-13 22 13"/>
      </g>'''),
]


class Skin05(sections.BaseSkin):
    label = "Trial 05 “Glass &amp; Glow”"
    theme = "#05060f"
    fonts = ["sora-latin-600-normal.woff2", "manrope-latin-400-normal.woff2"]

    def sprite(self):
        return icons.sprite("glass", extra=ORNAMENTS)

    # ------------------------------------------------------------ the backdrop
    def background(self, eager=True):
        """One fixed layer behind everything: the light study, a colour mesh, orbs,
        a grain and a dark wash. The wash is what keeps white type readable."""
        load = ' fetchpriority="high"' if eager else ' loading="lazy"'
        return """
<div class="bg" aria-hidden="true">
  <picture>
    <source srcset="assets/img/glass-light.avif" type="image/avif">
    <source srcset="assets/img/glass-light.webp" type="image/webp">
    <img class="bg__img" src="assets/img/glass-light.jpg" width="1600" height="900"%s decoding="async" alt="">
  </picture>
  <div class="bg__mesh"></div>
  <div class="bg__orb bg__orb--1"></div>
  <div class="bg__orb bg__orb--2"></div>
  <div class="bg__orb bg__orb--3"></div>
  <div class="bg__grain"></div>
  <div class="bg__wash"></div>
</div>
""" % load

    # ------------------------------------------------------------------ hero
    def hero(self):
        return """
<section class="hero">
  <div class="wrap hero__inner">
    <div class="panel hero__copy">
      %s
      <h1 class="display display--xl">Big brands.<br>Small towns.<br>Why not?</h1>
      <p class="hero__lead">Twenty-five WHYNOT showrooms in 23 towns, every major brand, and a phone number that still works five years after you buy.</p>
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
      <img src="assets/img/glass-light.avif" width="1600" height="900" fetchpriority="high" decoding="async"
           alt="Light passing through frosted glass in indigo, teal and amber.">
      <p class="hero__badge">A person answers, 10 am to 9 pm
        <span>One helpline for 25 showrooms — %s</span></p>
    </div>
  </div>
</section>
""" % (self.kicker("Godavari districts · since 1994"),
       self.btn("See what we sell", "products.html", "brand", "i-cart"),
       self.btn("Find my showroom", "products.html", "ghost", "i-pin"),
       self.icon("i-check"), self.icon("i-people"), self.icon("i-truck"), BRAND["pretty"])

    def swash(self):
        return '<div class="swash" aria-hidden="true"><span></span></div>\n'

    # -------------------------------------------------------------- dressing
    def extra_chips(self):
        return """<div class="chips" role="group" aria-label="Popular searches" style="margin:-8px 0 16px">
  <a class="chip" href="products.html?cat=water">%s Geysers</a>
  <a class="chip" href="products.html?cat=kitchen">%s Wet grinders</a>
  <a class="chip" href="products.html?cat=kitchen">%s Microwaves</a>
  <a class="chip" href="products.html?cat=tv">%s 55-inch TVs</a>
</div>""" % (self.icon("i-geyser"), self.icon("i-grinder"), self.icon("i-micro"), self.icon("i-tv"))

    def store_head(self):
        return ""

    # ---------------------------------------------------------------- bands
    def _pills(self, labels):
        return '<ul class="band-pills">%s</ul>' % "".join("<li>%s</li>" % l for l in labels)

    def band_picture(self):
        return self._pills(["Tanuku", "Tadepalligudem", "Rajahmundry", "Bhimavaram", "Eluru",
                            "Kakinada", "Palakollu", "Narasapuram", "Amalapuram", "Mandapeta",
                            "Anakapalle", "+ 12 more"])

    def band_picture_two(self):
        return self._pills(["1994", "1996", "2006", "2025", "25 showrooms", "300 people",
                            "2.5M served", "We drive the change"])

    def page_hero(self, kicker, title, lead, ctas=None, art=None):
        buttons = "".join(self.btn(label, href, variant, icon) for label, href, variant, icon in (ctas or []))
        return """
<section class="stage stage--pagehero">
  <div class="wrap">
    <div class="panel">
      %s
      <h1 class="display display--lg" style="margin-top:16px">%s</h1>
      <p class="lede">%s</p>
      <div class="hero__cta">%s</div>
    </div>
  </div>
</section>
""" % (self.kicker(kicker), title, lead, buttons)


def main():
    skin = Skin05()
    bg = skin.background()
    print("Building trial 05 (Glass & Glow):")
    shell.build(ROOT, skin, "index.html", sections.home(skin), current="index.html", background=bg)
    shell.build(ROOT, skin, "products.html", sections.catalogue_page(skin), current="products.html", background=bg)
    shell.build(ROOT, skin, "stores.html", sections.stores_page(skin), current="stores.html", background=bg)
    shell.build(ROOT, skin, "about.html", sections.about_page(skin), current="about.html", background=bg)
    shell.build(ROOT, skin, "contact.html", sections.contact_page(skin), current="contact.html",
                extra_scripts=["assets/js/contact.js"], background=bg)
    shell.build(ROOT, skin, "404.html", sections.notfound(skin), background=bg)
    print("Done — six pages in trial-05-glass/")


if __name__ == "__main__":
    main()
