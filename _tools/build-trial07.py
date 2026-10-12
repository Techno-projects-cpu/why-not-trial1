#!/usr/bin/env python3
"""
Trial 07 — "Slate & Rail".

Usage:  python3 _tools/build-trial07.py

The seventh direction, and the one the brief called for directly: clean and
professional, with a real light/dark mode. It also answers the criticism that
the first six were variations on one skeleton — so the FORM changes too:

  * a left rail on desktop and a bottom tab bar on phones, instead of the
    top header + hero every other trial uses;
  * the catalogue is a table of line items you scan, not a grid of cards;
  * the shortlist is a working panel beside the list (a sheet on phones),
    not a floating cart drawer;
  * no hero image and no marquee: a facts strip and a category index instead.

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
    ("index.html", "Home", "Overview, categories and how buying works here"),
    ("products.html", "Catalogue", "17 items, with today's price on request"),
    ("stores.html", "Showrooms", "25 branches in 23 towns"),
    ("about.html", "About", "Trading since 1994 in the Godavari districts"),
    ("contact.html", "Contact", "Helpline, email and the enquiry form"),
]

SPRITE = icons.sprite("slate", extra=[
    ("i-moon", '<path d="M52 34.5A20.5 20.5 0 0 1 29.5 12 20.5 20.5 0 1 0 52 34.5Z"/>'),
    ("i-slate", '<rect x="10" y="12" width="44" height="40" rx="4"/><path d="M10 24h44M24 24v28"/>'),
])


def head(title, description, page, scripts=()):
    return """<!doctype html>
<html lang="en-IN" data-mode="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0b0d12" media="(prefers-color-scheme: dark)">
<link rel="stylesheet" href="assets/css/style.css">
<script>
  /* Set the mode before first paint: the reader's system setting wins, unless
     they have chosen one before. Doing it here avoids a flash of the wrong
     palette, which is the usual bug with a light/dark switch. */
  (function () {
    try {
      var saved = localStorage.getItem("whynot-mode");
      var dark = saved ? saved === "dark"
        : window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
      document.documentElement.setAttribute("data-mode", dark ? "dark" : "light");
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
       "".join('<a href="%s"%s>%s</a>' % (href, ' aria-current="page"' if href == page else "", label)
               for href, label, _ in NAV),
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
         Not affiliated with the company and not deployed anywhere. Artwork is
         AI-generated stand-in art, and the enquiry form has no server behind it.</p>
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
       "".join('<a href="%s"%s>%s</a>' % (href, ' aria-current="page"' if href == current else "", label)
               for href, label, _ in NAV))


def page(title, description, page_name, body, scripts=()):
    return head(title, description, page_name, scripts) + body + foot(page_name)


# ------------------------------------------------------------------- pages
def index():
    cats = "".join(
        '<a href="products.html?cat=%s" data-goto-cat="%s">'
        '<span class="pick__art"><svg class="icon" aria-hidden="true"><use href="#%s"></use></svg></span>'
        '<span><strong>%s</strong><br><span class="note">%s</span></span>'
        '<span class="pick__n">see list</span></a>' % (cid, cid, ART[cid], label, blurb)
        for cid, label, blurb in CATEGORIES)

    strip = "".join('<div class="strip__cell"><p class="strip__v">%s</p><p class="strip__k">%s</p></div>'
                    % (v, k) for v, k in STRIP)

    steps = "".join('<li><div><strong>%s</strong><p>%s</p></div></li>' % (t, d) for _, t, d in HOW)

    body = """
      <p class="label">WHYNOT Electronics · Tanuku</p>
      <h1 class="display display--xl">The shop, not the app.</h1>
      <p class="lede">Twenty-five showrooms across the Godavari districts and
         Visakhapatnam. Pick what you want, send the list, and someone from your
         nearest branch comes back with today's price and stock.</p>
      <div class="hero-actions">
        <a class="btn btn--primary" href="products.html">Browse the catalogue</a>
        <a class="btn" href="stores.html">Find your showroom</a>
      </div>

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
          <div class="panel">
            <div class="panel__head"><h2 class="display display--m">How buying works here</h2></div>
            <div class="panel__body"><ol class="steps">%s</ol></div>
          </div>
          <div class="panel" style="margin-top:18px">
            <div class="panel__head"><h2 class="display display--m">Popular this week</h2>
              <a class="note" href="products.html">See the list</a></div>
            <div data-featured></div>
          </div>
        </div>
      </section>

      <section class="stage" aria-labelledby="promises">
        <div class="stage__head"><h2 class="display display--l" id="promises">What you get in writing</h2></div>
        <div class="two-up">
          <div class="panel"><div class="panel__body">
            %s
          </div></div>
          <div class="panel"><div class="panel__body">
            <p class="label">Service, honestly</p>
            <p class="lede">Brand warranty runs through each manufacturer's authorised
               network and we coordinate it for you. Installation and delivery are
               fixed at the counter — the price you agree is the price on the bill.</p>
            <p class="note">Prices are not invented on this page. Ask for today's and
               you get the number we can actually sell at.</p>
          </div></div>
        </div>
      </section>

      <p class="notice" style="margin-top:22px"><strong>About this build:</strong>
         a design concept for whynotindia.in, made as portfolio work. It is not
         affiliated with WHYNOT Electronics and is not deployed anywhere. The
         artwork is AI-generated stand-in art, and the enquiry form does not send
         anything — there is no server behind it.</p>
""" % (strip, cats, steps, "".join(
        '<p class="tile"><span class="tile__t">%s</span><span class="tile__d">%s</span></p>'
        % (t, d) for t, d in PROMISES))
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

      <div class="panel" style="margin-top:18px">
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

      <div class="work" style="margin-top:18px">
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

      <p class="notice" style="margin-top:22px">This is a concept build with no server
         attached. Sending the list opens WhatsApp or your mail app with the items
         written out — nothing is submitted from this page.</p>
"""
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
    body = """
      <p class="label">Showrooms · 25 doors · 23 towns</p>
      <h1 class="display display--xl">Twenty-five doors.</h1>
      <p class="lede">Every branch with its address, a map link and the phone number
         that reaches it. The flagship is in Tanuku; the rest are in the towns the
         company has traded in since 1994.</p>

      <div class="strip" style="margin-top:20px">
        <div class="strip__cell"><p class="strip__v" data-shop-state>Open now</p>
          <p class="strip__k">Today · 10 am to 9 pm</p></div>
        <div class="strip__cell"><p class="strip__v">%s</p><p class="strip__k">Helpline</p></div>
        <div class="strip__cell"><p class="strip__v">West Godavari</p><p class="strip__k">15 showrooms</p></div>
        <div class="strip__cell"><p class="strip__v">Visakhapatnam</p><p class="strip__k">Anakapalle</p></div>
      </div>

      <div class="panel" style="margin-top:18px">
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

      <div class="dir" data-store-list style="margin-top:18px"></div>
      <p class="panel" data-store-empty hidden><span class="empty">
        <svg class="icon" aria-hidden="true"><use href="#i-search"></use></svg>
        <span class="display display--xs">Nothing matches that</span>
        <span class="note">Try a town, a road or a pincode — or call the helpline and ask.</span></span></p>

      <p class="notice" style="margin-top:22px" data-shop-note>Open until 9 pm today.</p>
"""
    return page("Showrooms — WHYNOT redesign concept (Trial 07)",
                "All 25 WHYNOT showrooms across the Godavari districts and Visakhapatnam, "
                "with addresses and map links.", "stores.html", body % (BRAND["pretty"], chips),
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
          <div class="panel" style="margin-top:18px">
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
""" % (fact_rows, log, people)
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

      <section class="two-up" aria-labelledby="form-heading">
        <div class="panel">
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
          <div class="panel" style="margin-top:18px">
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
      <div class="panel" style="margin-top:22px">
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
"""
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
        print("  wrote %-14s %5.1f KB" % (name, len(html) / 1024))

    # the two Latin faces: the design is Inter with IBM Plex Mono for figures
    fonts = [("inter/package/files/inter-latin-400-normal.woff2", "inter-latin-400-normal.woff2"),
             ("inter/package/files/inter-latin-600-normal.woff2", "inter-latin-600-normal.woff2"),
             ("ibm-plex-mono/package/files/ibm-plex-mono-latin-400-normal.woff2", "ibm-plex-mono-latin-400-normal.woff2"),
             ("ibm-plex-mono/package/files/ibm-plex-mono-latin-500-normal.woff2", "ibm-plex-mono-latin-500-normal.woff2")]
    for src, dest in fonts:
        path = os.path.join("/tmp/fonts4", src)
        if not os.path.exists(path):
            print("  ! font missing (npm pack into /tmp/fonts4): %s" % src)
            continue
        shutil.copyfile(path, os.path.join(OUT, "assets", "fonts", dest))
        print("  %-34s %5.1f KB" % (dest, os.path.getsize(path) / 1024))

    print("\nNext: python3 _tools/localise.py trial-07-slate")


if __name__ == "__main__":
    main()
