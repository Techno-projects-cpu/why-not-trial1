#!/usr/bin/env python3
"""
Trial 07 — "Slate & Rail".

Usage:  python3 _tools/build-trial07.py

The seventh direction, and the one the brief called for directly: clean and
professional, WHITE first, with a real light/dark mode as the alternative. It
also answers the criticism that the first six were variations on one skeleton,
so the FORM changes too:

  * a left rail on desktop and a bottom tab bar on phones, instead of a
    top header + centred hero;
  * the catalogue is a table of line items you scan, not a grid of cards;
  * the shortlist is a working panel beside the list (a sheet on phones),
    not a floating cart drawer;
  * photographs where a photograph lands the point faster than a sentence, and
    a drawn map of the 23 towns the 25 doors sit in.

Type is Inter with IBM Plex Mono for figures, and both palettes are measured
against WCAG AA in _tools/contrast07.py.
"""

import io
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
REPO = os.path.dirname(HERE)
OUT = os.path.join(REPO, "trial-07-slate")

import content  # noqa: E402
import icons  # noqa: E402
import i18n  # noqa: E402

BRAND = content.BRAND
CATEGORIES = content.CATEGORIES
STATS = content.STATS
HOW = content.HOW
LEADERSHIP = content.LEADERSHIP
TIMELINE = content.TIMELINE
PROMISES = content.PROMISES

# The story arcs the other trials tell, cut to a line each: this trial is
# deliberately terser — a professional page says the same thing in fewer words.
LOG = [
    ("1994", "An LML showroom opens in Tanuku. Two-wheeler finance was the whole business."),
    ("1996", "Bajaj added. The family starts keeping stock of what people actually ask for."),
    ("2006", "Electronics, and with it the appliance counters that carry the shop today."),
    ("Today", "25 showrooms, 23 towns, 300 people, and a helpline that a person answers."),
]

STRIP = [
    ("25", "Showrooms"),
    ("23", "Towns served"),
    ("1994", "Trading since"),
    ("300", "People on the floor"),
]

# category id -> the symbol the scripts also use, so the page and the catalogue
# never disagree about which icon belongs to which category
ART = {"tv": "i-tv", "fridge": "i-fridge", "ac": "i-ac", "washer": "i-washer",
       "kitchen": "i-mixer", "water": "i-droplet", "lighting": "i-bulb",
       "audio": "i-speaker", "mobile": "i-phone", "cleaning": "i-vacuum"}

# Every place the company trades, with the approximate longitude and latitude
# of the town and where its label should sit so two labels never overlap. The
# map is drawn from this table; nothing about it is fetched at runtime.
# (town, district, lon, lat, dx, dy, anchor)
TOWNS = [
    ("Tanuku",           "West Godavari", 81.68, 16.75,  11,  -3, "start"),
    ("Tadepalligudem",   "West Godavari", 81.50, 16.83, -11, -17, "end"),
    ("Bhimadolu",        "West Godavari", 81.28, 16.81, -11,  -5, "end"),
    ("Nidadavolu",       "West Godavari", 81.68, 16.90, -11,  -4, "end"),
    ("Narasapuram",      "West Godavari", 81.70, 16.44,  -6,  16, "end"),
    ("Palakollu",        "West Godavari", 81.73, 16.52,  11,   2, "start"),
    ("Jangareddygudem",  "West Godavari", 81.28, 17.12,  11,   2, "start"),
    ("Devarapalli",      "West Godavari", 81.32, 16.95, -11,   2, "end"),
    ("Eluru",            "West Godavari", 81.10, 16.71,  11,   2, "start"),
    ("Chintalapudi",     "West Godavari", 81.03, 17.07,  11,   2, "start"),
    ("Nallajarla",       "West Godavari", 81.42, 16.87, -13,  23, "end"),
    ("Attili",           "West Godavari", 81.60, 16.72, -11,  -3, "end"),
    ("Bhimavaram",       "West Godavari", 81.52, 16.54, -11,   2, "end"),
    ("Rajahmundry",      "East Godavari", 81.80, 17.00,  11,  -3, "start"),
    ("Kovvur",           "East Godavari", 81.73, 17.01, -11,  -4, "end"),
    ("Amalapuram",       "East Godavari", 82.00, 16.58,  11,   3, "start"),
    ("Tatipaka",         "East Godavari", 82.02, 16.50,   9,  16, "start"),
    ("Ravulapalem",      "East Godavari", 81.83, 16.75,  11,  13, "start"),
    ("Mandapeta",        "East Godavari", 81.93, 16.86,  11,  -3, "start"),
    ("Yeleswaram",       "East Godavari", 82.11, 17.28,  11,  -3, "start"),
    ("Pithapuram",       "East Godavari", 82.25, 17.11,  11,  -3, "start"),
    ("Kakinada",         "East Godavari", 82.24, 16.96,  11,   3, "start"),
    ("Anakapalle",       "Visakhapatnam", 82.99, 17.69, -11,   3, "end"),
]

CAPTIONS = {
    "hero-floor": "The floor at Tanuku, as this concept build imagines it",
    "shelf-detail": "A display wall: appliances in a line, boxes behind",
    "storefront": "A branch on a main road, shutters up at ten",
    "detail-counter": "The bill, the keys, the handover",
}
AI_TAG = "AI stand-in art"


# ------------------------------------------------------------------ fragments
def ic(name):
    """One icon from the page's own sprite."""
    return '<svg class="icon" aria-hidden="true"><use href="#%s"></use></svg>' % name


def btn(href, label, cls="btn", icon=None):
    return '<a class="%s" href="%s">%s%s</a>' % (cls, href, ic(icon) if icon else "", label)


def shot(base, w, h, caption=None, tag=AI_TAG, eager=False, inset=False):
    """A photograph, with its caption and the honesty tag on the face of it."""
    alt = caption or CAPTIONS.get(base, "")
    fig = icons.picture(base, alt, w, h, eager=eager)
    cap = ('<figcaption><span class="shot__tag">%s</span><span>%s</span></figcaption>'
           % (tag, caption)) if caption else ""
    return '<figure class="shot%s">%s%s</figure>' % (" shot--inset" if inset else "", fig, cap)


def band(base, w, h, caption=None, tag=AI_TAG, split=False, side=""):
    inner = icons.picture(base, caption or CAPTIONS.get(base, ""), w, h)
    cap = ('<figcaption><span class="shot__tag">%s</span><span>%s</span></figcaption>'
           % (tag, caption)) if caption else ""
    if split:
        return ('<figure class="band band--split">%s<div class="band__side">%s</div></figure>'
                % (inner, side))
    return '<figure class="band">%s%s</figure>' % (inner, cap)


def switcher():
    """The three-language control. The localiser sees .langswitch already on the
    page and leaves its own insertion alone, so there is exactly one per header
    and it sits where this design wants it."""
    return ('<div class="langswitch" role="group" aria-label="Language / భాష">\n'
            '          <button type="button" class="langswitch__btn" data-lang="en" aria-pressed="true">EN</button>\n'
            '          <button type="button" class="langswitch__btn" data-lang="te" aria-pressed="false">తె</button>\n'
            '          <button type="button" class="langswitch__btn" data-lang="hi" aria-pressed="false">हि</button>\n'
            '        </div>')


MODE_TOGGLE = ('<button type="button" class="mode-toggle" data-mode-toggle aria-pressed="false">\n'
               '          <svg class="icon" aria-hidden="true"><use href="#i-sun"></use></svg>\n'
               '          <span class="mode-toggle__light">Light</span>\n'
               '          <span class="mode-toggle__dark">Dark</span>\n'
               '          <span class="sr" data-mode-state>mode</span>\n'
               '        </button>')

NAV = [
    ("index.html", "Home", "i-slate", "Overview, categories and how buying works here"),
    ("products.html", "Catalogue", "i-tag", "17 items, with today's price on request"),
    ("stores.html", "Showrooms", "i-pin", "25 branches in 23 towns"),
    ("about.html", "About", "i-people", "Trading since 1994 in the Godavari districts"),
    ("contact.html", "Contact", "i-call", "Helpline, email and the enquiry form"),
]

SPRITE = icons.sprite("slate", extra=[
    ("i-moon", '<path d="M52 34.5A20.5 20.5 0 0 1 29.5 12 20.5 20.5 0 1 0 52 34.5Z"/>'),
    ("i-slate", '<rect x="10" y="12" width="44" height="40" rx="4"/><path d="M10 24h44M24 24v28"/>'),
])


def map_svg():
    """The drawn map of the region: sea, coast, the Godavari and its delta, two
    district lines and one dot per town.

    The projection is the whole trick. Longitude spreads across 340 units a
    degree and latitude 420, which stretches the region to fill the frame and
    leaves the sea where the sea actually is — south-east, along the coast from
    Anakapalle down past Kakinada and the delta. An earlier pass had the coast
    running diagonally through the middle of the page: Kakinada, Pithapuram,
    Yeleswaram and Anakapalle all ended up floating in the Bay of Bengal, which
    is exactly the sort of thing a drawn map has to get right.
    """
    def pt(lon, lat):
        return ((lon - 80.92) * 340 + 16, (17.90 - lat) * 420 + 22)

    coast = [(83.60, 18.35), (83.30, 17.70), (83.02, 17.58), (82.80, 17.44),
             (82.55, 17.28), (82.40, 17.10), (82.28, 16.93), (82.32, 16.74),
             (82.30, 16.54), (82.20, 16.34), (82.02, 16.14), (81.85, 15.94)]
    sea = "M%s L900 700 L900 0 Z" % " L".join("%.0f %.0f" % pt(a, b) for a, b in coast)

    godavari = [(81.06, 17.34), (81.38, 17.22), (81.62, 17.10), (81.80, 17.00),
                (82.00, 16.94), (82.18, 16.86), (82.30, 16.78)]
    delta_a = [(82.05, 16.80), (82.14, 16.62), (82.22, 16.46)]
    delta_b = [(82.22, 16.84), (82.30, 16.66), (82.30, 16.54)]

    lines = [
        # West / East Godavari, then East Godavari / Visakhapatnam
        [(81.52, 17.36), (81.62, 17.16), (81.72, 17.02), (81.88, 16.86), (81.96, 16.68), (81.98, 16.42)],
        [(82.04, 17.80), (82.22, 17.56), (82.34, 17.34), (82.30, 17.10)],
    ]

    def poly(points):
        return "M%s" % " L".join("%.0f %.0f" % pt(a, b) for a, b in points)

    dots = []
    for town, district, lon, lat, dx, dy, anchor in TOWNS:
        x, y = pt(lon, lat)
        cls = {"West Godavari": "map__dot", "East Godavari": "map__dot map__dot--east",
               "Visakhapatnam": "map__dot map__dot--vizag"}[district]
        big = " map__dot--big" if town == "Tanuku" else ""
        ring = ('<circle class="map__halt" cx="%.0f" cy="%.0f" r="10"/>' % (x, y)) if town == "Tanuku" else ""
        strong = " map__name--strong" if town in ("Tanuku", "Rajahmundry", "Eluru", "Kakinada", "Anakapalle") else ""
        dots.append(ring +
                    '<circle class="%s%s" cx="%.0f" cy="%.0f" r="4.4"/>' % (cls, big, x, y) +
                    '<text class="map__name%s" x="%.0f" y="%.0f" text-anchor="%s">%s</text>'
                    % (strong, x + dx, y + dy, anchor, town))

    # the two brand stores share the flagship building: two small squares under
    # the Tanuku dot, named once in the legend rather than twice on the map
    tx, ty = pt(81.68, 16.75)
    brand_marks = ('<rect class="map__dot map__dot--brand" x="%.0f" y="%.0f" width="7" height="7" rx="1.5"/>'
                   '<rect class="map__dot map__dot--brand" x="%.0f" y="%.0f" width="7" height="7" rx="1.5"/>'
                   % (tx - 3, ty + 9, tx + 6, ty + 9))

    return """<svg viewBox="0 0 900 700" role="img" aria-labelledby="map-t map-d" class="map__svg">
        <title id="map-t">Map of the Godavari districts and Visakhapatnam</title>
        <desc id="map-d">A drawn map: 25 doors in 23 towns, from Chintalapudi and Jangareddygudem in the west to Kakinada and Anakapalle on the coast. A sketch, not a survey.</desc>
        <rect class="map__land" x="0" y="0" width="900" height="700"/>
        <path class="map__sea" d="%s"/>
        <path class="map__river" d="%s"/>
        <path class="map__river" d="%s" style="stroke-width:1.4"/>
        <path class="map__river" d="%s" style="stroke-width:1.4"/>
        <path class="map__line map__line--soft" d="%s"/>
        <path class="map__line map__line--soft" d="%s"/>
        <text class="map__name map__name--sea" x="620" y="600">Bay of Bengal</text>
        <text class="map__name map__name--sea" x="176" y="296">Godavari</text>
        <g class="map__compass" aria-hidden="true">
          <path d="M852 74 L860 46 L868 74 L860 66 Z"/>
          <text class="map__name" x="860" y="90" text-anchor="middle">N</text>
        </g>
        %s
        %s
      </svg>""" % (sea, poly(godavari), poly(delta_a), poly(delta_b), poly(lines[0]), poly(lines[1]),
                    brand_marks, "".join("  " + d + "\n        " for d in dots))


# --------------------------------------------------------------------- shell
def head(title, description, page, scripts=()):
    return """<!doctype html>
<html lang="en-IN" data-mode="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<meta name="theme-color" content="#ffffff">
<link rel="stylesheet" href="assets/css/style.css">
<script>
  /* White first. The page opens light whatever the machine's system setting
     says — the mode switch is there for the reader who wants dark, and the
     choice is remembered. Applying it here, before first paint, is what stops
     the flash of the wrong palette a mode switch usually causes. */
  (function () {
    try {
      if (localStorage.getItem("whynot-mode") === "dark") {
        document.documentElement.setAttribute("data-mode", "dark");
      }
    } catch (e) {}
  })();
</script>
<script src="assets/js/i18n.js" defer></script>
<script src="assets/js/main.js" defer></script>
%s</head>
<body>
<a class="skip" href="#main">Skip to content</a>
%s
<aside class="rail" aria-label="Main">
  <a class="rail__brand" href="index.html">
    <span class="brand__mark" aria-hidden="true">W</span>
    <span><span class="brand__name">WHYNOT</span>
      <span class="brand__sub">Electronics · 1994</span></span>
  </a>
  <nav class="rail__nav">%s</nav>
  <div class="rail__pick">
    <span><span class="label">My list</span><br><strong data-list-count hidden>0</strong>
      <span class="note" data-list-label>0 items</span></span>
    <a class="btn btn--sm" href="products.html#list">Open</a>
  </div>
  <div class="rail__foot">
    %s
    %s
    <p class="note">Helpline %s<br>%s</p>
  </div>
</aside>

<div class="shell">
  <header class="bar">
    <a class="bar__brand" href="index.html">
      <span class="brand__mark" aria-hidden="true">W</span>
      <span><span class="brand__name">WHYNOT</span><span class="brand__sub">Electronics</span></span>
    </a>
    %s
    <button class="btn btn--sm" type="button" data-panel-open aria-controls="pick">
      <svg class="icon" aria-hidden="true"><use href="#i-cart"></use></svg>
      <span data-list-count hidden>0</span><span class="sr">items in my list</span>
    </button>
  </header>
  <main class="wrap" id="main">
""" % (title, description,
       "".join('<script src="assets/js/%s" defer></script>\n' % fn for fn in scripts), SPRITE,
       "".join('<a href="%s"%s>%s<span>%s</span></a>'
               % (href, ' aria-current="page"' if href == page else "", ic(icon), label)
               for href, label, icon, _ in NAV),
       switcher(), MODE_TOGGLE, BRAND["pretty"], BRAND["email"], switcher())


def foot(current):
    return """
  </main>
  <footer class="wrap foot">
    <div class="foot__grid">
      <p><strong>WHYNOT Electronics Pvt Ltd</strong><br>%s</p>
      <p>Helpline <a href="tel:+91%s">%s</a><br>
         <a href="mailto:%s">%s</a> · open 10 am to 9 pm</p>
      <p class="note">A redesign concept for whynotindia.in, built as portfolio work.
         Not affiliated with the company and not deployed anywhere. Photographs on
         this page are AI-generated stand-in art and the enquiry form has no server
         behind it.</p>
      <p class="note">© <span data-year>2026</span> concept build.</p>
    </div>
  </footer>
</div>

<nav class="tabs" aria-label="Pages">
%s</nav>
<div class="toast" data-toast role="status" aria-live="polite"></div>
</body>
</html>
""" % ("<br>".join(BRAND["address_lines"]), BRAND["helpline"], BRAND["pretty"], BRAND["email"], BRAND["email"],
       "".join('<a href="%s"%s>%s<span>%s</span></a>'
               % (href, ' aria-current="page"' if href == current else "", ic(icon), label)
               for href, label, icon, _ in NAV))


def page(title, description, page_name, body, scripts=()):
    return head(title, description, page_name, scripts) + body + foot(page_name)


# --------------------------------------------------------------------- pages
def index():
    cats = "".join(
        '<a href="products.html?cat=%s" data-goto-cat="%s">'
        '<span class="pick__art"><svg class="icon" aria-hidden="true"><use href="#%s"></use></svg></span>'
        '<span><strong>%s</strong><br><span class="note">%s</span></span>'
        '<span class="pick__n">see list</span></a>' % (cid, cid, ART[cid], label, blurb)
        for cid, label, blurb in CATEGORIES)

    strip = "".join('<div class="strip__cell"><p class="strip__v">%s</p><p class="strip__k">%s</p></div>'
                    % (v, k) for v, k in STRIP)

    nodes = "".join(
        '<div class="diagram__node">'
        '<span>%s%s</span><strong>%s</strong><p>%s</p></div>'
        % (ic(icon), n, title, desc)
        for n, title, desc, icon in [
            ("Step 1", "Add what you like", "Build a list while you browse. Nothing is charged and no account is needed.", "i-tag"),
            ("Step 2", "Send it to us", "One tap opens WhatsApp with your whole list written out, or dials the helpline.", "i-whatsapp"),
            ("Step 3", "We call with the price", "Today's price, which branch has it, EMI if you want it, and a delivery date.", "i-call"),
            ("Step 4", "Collect at your branch", "Fixed at the counter: delivery, installation and who to call afterwards.", "i-store"),
        ])

    body = """
      <section class="hero">
        <div class="hero__text">
          <p class="label">WHYNOT Electronics · Tanuku</p>
          <h1 class="display display--xl">The shop,<br>not the app.</h1>
          <p class="lede">Twenty-five showrooms across the Godavari districts and
             Visakhapatnam. Pick what you want, send the list, and someone from your
             nearest branch comes back with today's price and stock.</p>
          <div class="hero-actions">
            <a class="btn btn--primary" href="products.html">Browse the catalogue</a>
            <a class="btn" href="stores.html">Find your showroom</a>
          </div>
          <div class="hero__proof">
            <span><svg class="icon" aria-hidden="true"><use href="#i-store"></use></svg>25 showrooms</span>
            <span><svg class="icon" aria-hidden="true"><use href="#i-clock"></use></svg>Open 10 am to 9 pm</span>
            <span><svg class="icon" aria-hidden="true"><use href="#i-call"></use></svg>One helpline, a person answers</span>
          </div>
        </div>
        %s
      </section>

      <div class="strip">%s</div>
      <div class="marquee"><div class="marquee__track"><span>25 showrooms</span><span>23 towns</span>
        <span>20 brands</span><span>open 10 to 9</span><span>delivery and installation</span>
        <span>25 showrooms</span><span>23 towns</span><span>20 brands</span><span>open 10 to 9</span>
        <span>delivery and installation</span></div></div>

      <section class="split" aria-labelledby="cats">
        <div class="panel">
          <div class="panel__head"><h2 class="display display--m" id="cats">What we sell</h2>
            <a class="note" href="products.html">All 17 items</a></div>
          <div class="pick">%s</div>
        </div>
        <div>
          <div class="panel panel--raised">
            <div class="panel__head"><h2 class="display display--m">How buying works here</h2></div>
            <div class="panel__body"><div class="diagram">%s</div></div>
          </div>
          <div class="panel" style="margin-top:20px">
            <div class="panel__head"><h2 class="display display--m">Popular this week</h2>
              <a class="note" href="products.html">See the list</a></div>
            <div data-featured></div>
          </div>
        </div>
      </section>

      <section class="stage" aria-labelledby="where">
        <div class="stage__head"><h2 class="display display--l" id="where">Where the 25 doors are</h2>
          <a class="note" href="stores.html">All 25 showrooms</a></div>
        %s
        <p class="note" style="margin-top:10px">A drawn sketch of the region, not a
           survey: the dots sit in the right town, the distances are not to scale.</p>
      </section>

      <section class="stage" aria-labelledby="promises">
        <div class="stage__head"><h2 class="display display--l" id="promises">What you get in writing</h2></div>
        <div class="two-up">
          <div class="panel"><div class="panel__body">
            %s
          </div></div>
          <div>
            %s
            <div class="panel" style="margin-top:20px"><div class="panel__body">
              <p class="label">Service, honestly</p>
              <p class="lede">Brand warranty runs through each manufacturer's authorised
                 network and we coordinate it for you. Installation and delivery are
                 fixed at the counter — the price you agree is the price on the bill.</p>
              <p class="note">Prices are not invented on this page. Ask for today's and
                 you get the number we can actually sell at.</p>
            </div></div>
          </div>
        </div>
      </section>

      <p class="notice" style="margin-top:26px"><strong>About this build:</strong>
         a design concept for whynotindia.in, made as portfolio work. It is not
         affiliated with WHYNOT Electronics and is not deployed anywhere. The
         photographs are AI-generated stand-in art, and the enquiry form does not
         send anything — there is no server behind it.</p>
""" % (shot("hero-floor", 1376, 768, CAPTIONS["hero-floor"], eager=True),
       strip, cats, nodes,
       map_svg(),
       "".join('<p class="tile"><span class="tile__t">%s</span><span class="tile__d">%s</span></p>'
               % (t, d) for t, d in PROMISES),
       shot("detail-counter", 1126, 776, CAPTIONS["detail-counter"]))
    return page("WHYNOT Electronics — a redesign concept (Trial 07)",
                "A clean, professional redesign concept for WHYNOT Electronics: 25 showrooms, "
                "23 towns, appliances priced by the branch you walk into.", "index.html", body,
                scripts=("products.js",))


def products():
    body = """
      <p class="label">Catalogue · 17 items · 10 categories</p>
      <h1 class="display display--xl">The catalogue, as a list.</h1>
      <p class="lede">Seventeen things people actually ask for, in the categories
         the showrooms stock. Add what you want to <strong>my list</strong>, send it
         in one tap, and a person from your nearest branch replies with today's
         price and stock. No card details, no account, nothing charged.</p>

      %s

      <div class="panel">
        <div class="panel__body">
          <div class="filters">
            <div class="filters__row">
              <label class="field"><span class="sr">Search the catalogue</span>
                <input class="input" id="q" type="search" data-product-search
                       placeholder="Search: TV, fridge, 1.5 ton, mixer" autocomplete="off"
                       data-i18n-ph="Search: TV, fridge, 1.5 ton, mixer"></label>
              <label class="field"><span class="sr">Town</span>
                <select class="select" id="town" data-town-select><option value="all">All towns</option></select></label>
            </div>
            <div class="chips" data-cat-chips></div>
          </div>
          <p class="count" data-result-count aria-live="polite">17 products</p>
        </div>
      </div>

      <div class="work" style="margin-top:20px">
        <section class="panel panel--flush" aria-labelledby="list-heading">
          <div class="panel__head"><h2 class="display display--m" id="list-heading">Line list</h2>
            <span class="note">price on request</span></div>
          <div class="rows__head" aria-hidden="true">
            <span class="label">Item</span><span class="label">Category</span>
            <span class="label">Specification</span><span class="label">Available at</span>
            <span class="label">List</span>
          </div>
          <div class="rows" data-products></div>
        </section>

        <aside class="work__aside panel" id="pick" data-aside>
          <div class="panel__head">
            <h2 class="display display--m">My list</h2>
            <button class="btn btn--sm btn--ghost" type="button" data-panel-close>Close</button>
          </div>
          <div class="panel__body" data-list-panel id="list"></div>
        </aside>
      </div>

      <p class="notice" style="margin-top:24px">This is a concept build with no server
         attached. Sending the list opens WhatsApp or your mail app with the items
         written out — nothing is submitted from this page.</p>
""" % band("shelf-detail", 1376, 768, CAPTIONS["shelf-detail"])
    return page("Catalogue — WHYNOT redesign concept (Trial 07)",
                "17 appliances across 10 categories, with a shortlist that ends in a "
                "WhatsApp, call or email enquiry.", "products.html", body,
                scripts=("products.js",))


def stores():
    chips = "".join('<button class="chip" type="button" data-district="%s" aria-pressed="%s">%s</button>'
                    % (d, "true" if d == "all" else "false", label)
                    for d, label in [("all", "All 25"), ("West Godavari", "West Godavari"),
                                     ("East Godavari", "East Godavari"),
                                     ("Visakhapatnam", "Visakhapatnam")])
    legend = """
          <div class="panel__body">
            <p class="label">How to read it</p>
            <ul class="map__legend" style="margin-top:12px">
              <li><i></i><span>West Godavari</span><b class="map__n">13</b></li>
              <li><i class="k-east"></i><span>East Godavari</span><b class="map__n">9</b></li>
              <li><i class="k-vizag"></i><span>Visakhapatnam</span><b class="map__n">1</b></li>
              <li><i class="k-town"></i><span>Tanuku, the flagship</span></li>
              <li><i class="k-brand"></i><span>Two brand stores in the same building</span></li>
            </ul>
            <p class="note" style="margin-top:14px">Twenty-five doors in twenty-three
               towns. The coast runs north to south: Anakapalle and Visakhapatnam
               district at the top, the Godavari delta at the bottom right, and the
               inland towns to the west.</p>
            <p class="note" style="margin-top:10px">A sketch, not a survey — the dots
               are in the right towns, the distances are drawn to fit the page.</p>
          </div>"""
    body = """
      <p class="label">Showrooms · 25 doors · 23 towns</p>
      <h1 class="display display--xl">Twenty-five doors.</h1>
      <p class="lede">Every branch with its address, a map link and the phone number
         that reaches it. The flagship is in Tanuku; the rest are in the towns the
         company has traded in since 1994.</p>

      <div class="strip" style="margin-top:26px">
        <div class="strip__cell"><p class="strip__v" data-shop-state>Open now</p>
          <p class="strip__k">Today · 10 am to 9 pm</p></div>
        <div class="strip__cell"><p class="strip__v">%s</p><p class="strip__k">Helpline</p></div>
        <div class="strip__cell"><p class="strip__v">15</p><p class="strip__k">Doors in West Godavari</p></div>
        <div class="strip__cell"><p class="strip__v">1</p><p class="strip__k">In Anakapalle</p></div>
      </div>

      <section class="stage" aria-labelledby="map-heading">
        <div class="stage__head"><h2 class="display display--l" id="map-heading">The region, drawn</h2>
          <span class="note">25 doors · 23 towns</span></div>
        <div class="map">
          <div class="map__frame">%s</div>
          <div class="panel">%s</div>
        </div>
      </section>

      %s

      <div class="panel" style="margin-top:26px">
        <div class="panel__body">
          <div class="filters">
            <div class="filters__row">
              <label class="field"><span class="sr">Search the showrooms</span>
                <input class="input" type="search" data-store-search placeholder="Search town, road or pincode"
                       data-i18n-ph="Search town, road or pincode" autocomplete="off"></label>
              <button class="btn" type="button" data-store-clear>Clear</button>
            </div>
            <div class="chips">%s</div>
          </div>
          <p class="count" data-store-count aria-live="polite">25 showrooms</p>
        </div>
      </div>

      <div class="dir" data-store-list style="margin-top:20px"></div>
      <p class="panel" data-store-empty hidden><span class="empty">
        <svg class="icon" aria-hidden="true"><use href="#i-search"></use></svg>
        <span class="display display--xs">Nothing matches that</span>
        <span class="note">Try a town, a road or a pincode — or call the helpline and ask.</span></span></p>

      <p class="notice" style="margin-top:24px" data-shop-note>Open until 9 pm today.</p>
""" % (BRAND["pretty"], map_svg(), legend,
       band("storefront", 1200, 670, CAPTIONS["storefront"]), chips)
    return page("Showrooms — WHYNOT redesign concept (Trial 07)",
                "All 25 WHYNOT showrooms across the Godavari districts and Visakhapatnam, "
                "with addresses, a drawn map and map links.", "stores.html", body,
                scripts=("stores.js",))


def about():
    facts = [("Founded", "27 February 1994, as an LML two-wheeler showroom in Tanuku"),
             ("Today", "%d showrooms, %d towns, %d people" % (BRAND["showrooms"], BRAND["towns"], BRAND["staff"])),
             ("What we sell", "Televisions, refrigeration, cooling, laundry, small appliances, lighting, mobile"),
             ("How we sell", "Ask for today's price. No invented numbers on this page"),
             ("Service", "Through each brand's authorised network, coordinated by the branch you bought at"),
             ("Hours", "%s, every day" % BRAND["hours"]),
             ("Helpline", BRAND["pretty"]),
             ("Email", BRAND["email"])]
    fact_rows = "".join("<div><dt>%s</dt><dd>%s</dd></div>" % (k, v) for k, v in facts)
    log = "".join('<div class="log__row"><span class="log__y">%s</span><p class="log__t">%s</p></div>'
                  % (y, t) for y, t in LOG)
    people = "".join('<p class="tile"><span class="tile__t">%s</span><span class="tile__d">%s</span></p>'
                     % (n, r) for n, r in LEADERSHIP)

    body = """
      <p class="label">About · trading since 1994</p>
      <h1 class="display display--xl">Thirty-two years of asking why not.</h1>
      <p class="lede">The name is a question the family kept asking: why not open
         here, why not stock that, why not service what we sell. It started with
         two-wheelers in Tanuku and became one of the largest appliance retailers
         in the Godavari districts.</p>

      %s

      <section class="two-up" aria-labelledby="facts">
        <div class="panel">
          <div class="panel__head"><h2 class="display display--m" id="facts">The facts</h2></div>
          <div class="panel__body"><dl class="facts">%s</dl></div>
        </div>
        <div>
          <div class="panel">
            <div class="panel__head"><h2 class="display display--m">How it got here</h2></div>
            <div class="panel__body"><div class="log">%s</div></div>
          </div>
          <div class="panel" style="margin-top:20px">
            <div class="panel__head"><h2 class="display display--m">Who runs it</h2></div>
            <div>%s</div>
          </div>
        </div>
      </section>

      <section class="stage" aria-labelledby="honest">
        <div class="stage__head"><h2 class="display display--l" id="honest">What we would not put on a page</h2></div>
        <p class="lede">No invented prices, no awards we have not won, no countdown
           timers. The site this concept replaces said "40 branches across 36
           locations" in one place and "25 branches in 23 cities" in another; a shop
           this size should be able to say one true number. Twenty-five, in 23 towns.</p>
        <p class="note" style="margin-top:10px">Figures on this page come from the
           company's own public website, read in October 2026.</p>
      </section>
""" % (band("detail-counter", 1126, 776, CAPTIONS["detail-counter"]), fact_rows, log, people)
    return page("About — WHYNOT redesign concept (Trial 07)",
                "WHYNOT Electronics: founded in 1994, 25 showrooms, 23 towns, 300 people.",
                "about.html", body)


def contact():
    body = """
      <p class="label">Contact · a person answers</p>
      <h1 class="display display--xl">Talk to a person.</h1>
      <p class="lede">The helpline is answered at the branch, not by a call centre.
         Tell us the model and your town and you get today's price, stock and a
         delivery date — in one call.</p>

      <section class="two-up" style="margin-top:26px" aria-labelledby="form-heading">
        <div class="panel panel--raised">
          <div class="panel__head"><h2 class="display display--m" id="form-heading">Send an enquiry</h2></div>
          <div class="panel__body">
            <form class="stack" data-contact-form novalidate>
              <label class="field"><span>Your name</span>
                <input class="input" name="name" type="text" autocomplete="name" required></label>
              <label class="field"><span>Mobile number</span>
                <input class="input" name="mobile" type="tel" inputmode="numeric" autocomplete="tel" required></label>
              <label class="field"><span>What are you looking for?</span>
                <textarea class="textarea" name="message" required
                  placeholder="Model, size, room — anything that helps us price it"></textarea></label>
              <p class="note">This concept build has no server: nothing is submitted.
                 In a live build this would reach the branch you pick.</p>
              <button class="btn btn--primary btn--block" type="submit">Send enquiry</button>
              <div class="notice" data-form-status hidden></div>
            </form>
          </div>
        </div>
        <div>
          <div class="panel">
            <div class="panel__head"><h2 class="display display--m">What happens next</h2></div>
            <div class="panel__body"><ol class="steps">
              <li><div><strong>We read it</strong><p>A person at the nearest branch, not a queue.</p></div></li>
              <li><div><strong>We price it</strong><p>Today's price, stock, EMI and exchange if you want it.</p></div></li>
              <li><div><strong>You decide</strong><p>Nothing is charged from this site and no account is needed.</p></div></li>
            </ol></div>
          </div>
          <div class="panel" style="margin-top:20px">
            <div class="panel__head"><h2 class="display display--m">Or just call</h2></div>
            <div class="panel__body">
              <dl class="facts">
                <div><dt>Helpline</dt><dd><a href="tel:+91%s">%s</a></dd></div>
                <div><dt>Email</dt><dd><a href="mailto:%s">%s</a></dd></div>
                <div><dt>Hours</dt><dd>10 am to 9 pm, every day</dd></div>
                <div><dt>Flagship</dt><dd>%s</dd></div>
              </dl>
            </div>
          </div>
          <p class="note" style="margin-top:16px">Every branch has its own phone
             number and a map link, on the showroom list.</p>
          <p style="margin-top:12px"><a class="btn" href="stores.html">All 25 showrooms</a></p>
        </div>
      </section>
""" % (BRAND["helpline"], BRAND["pretty"], BRAND["email"], BRAND["email"], BRAND["address_one_line"])
    return page("Contact — WHYNOT redesign concept (Trial 07)",
                "Call the WHYNOT helpline, email the branch, or send an enquiry from the form.",
                "contact.html", body, scripts=("contact.js",))


def not_found():
    body = """
      <p class="label">Error 404</p>
      <h1 class="display display--xl">That page isn't here.</h1>
      <p class="lede">An old link, a moved page, or a typo in the address. Nothing
         is lost — the catalogue and all 25 showrooms are where you left them.</p>
      <div class="hero-actions">
        <a class="btn btn--primary" href="products.html">Open the catalogue</a>
        <a class="btn" href="stores.html">Find a showroom</a>
        <a class="btn" href="contact.html">Call a person</a>
      </div>
      <div class="panel panel--raised" style="margin-top:26px">
        <div class="panel__body">
          <form class="stack" action="products.html" method="get">
            <label class="field"><span>Search the catalogue instead</span>
              <input class="input" type="search" name="q" placeholder="Search: TV, fridge, 1.5 ton"
                     data-i18n-ph="Search: TV, fridge, 1.5 ton"></label>
            <button class="btn btn--primary" type="submit">Open the catalogue</button>
          </form>
          <p class="note" style="margin-top:8px">Search runs on the catalogue page; this
             box takes you there with your words.</p>
        </div>
      </div>
      <section class="stage" aria-labelledby="lost">
        <div class="stage__head"><h2 class="display display--l" id="lost">Or start from the map</h2></div>
        %s
      </section>
""" % map_svg()
    return page("Not found — WHYNOT redesign concept (Trial 07)",
                "That page is not here. The catalogue and the showroom list are.",
                "404.html", body, scripts=("products.js",))


def main():
    os.makedirs(os.path.join(OUT, "assets", "css"), exist_ok=True)
    os.makedirs(os.path.join(OUT, "assets", "js"), exist_ok=True)
    os.makedirs(os.path.join(OUT, "assets", "fonts"), exist_ok=True)

    for name, html in (("index.html", index()), ("products.html", products()), ("stores.html", stores()),
                       ("about.html", about()), ("contact.html", contact()), ("404.html", not_found())):
        with io.open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
            f.write(html)
        print("  wrote %-14s %5.1f KB" % (name, len(html.encode("utf-8")) / 1024.0))

    # the two Latin faces: the design is Inter with IBM Plex Mono for figures
    fonts = [("inter/package/files/inter-latin-400-normal.woff2", "inter-latin-400-normal.woff2"),
             ("inter/package/files/inter-latin-600-normal.woff2", "inter-latin-600-normal.woff2"),
             ("inter/package/files/inter-latin-700-normal.woff2", "inter-latin-700-normal.woff2"),
             ("ibm-plex-mono/package/files/ibm-plex-mono-latin-400-normal.woff2", "ibm-plex-mono-latin-400-normal.woff2"),
             ("ibm-plex-mono/package/files/ibm-plex-mono-latin-500-normal.woff2", "ibm-plex-mono-latin-500-normal.woff2")]
    for src, dest in fonts:
        path = os.path.join("/tmp/fonts4", src)
        if not os.path.exists(path):
            print("  ! font missing (npm pack into /tmp/fonts4): %s" % src)
            continue
        shutil.copyfile(path, os.path.join(OUT, "assets", "fonts", dest))
        print("  %-34s %5.1f KB" % (dest, os.path.getsize(path) / 1024))

    print("\nNext: python3 _tools/port-js07.py and python3 _tools/localise.py trial-07-slate")


if __name__ == "__main__":
    main()
