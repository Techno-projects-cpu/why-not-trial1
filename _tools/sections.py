# WHYNOT redesign — the page bodies shared by Trials 04, 05 and 06.
#
# One set of neutral class names, interpreted three ways by three stylesheets.
# That is the whole trick of this module: the new trials say identical things in
# identical structure, and the design lives entirely in the CSS — which is the
# honest way to compare three visual directions without changing the content.
#
# BaseSkin holds the parts every design needs (header, drawer, footer, phone bar,
# buttons, panels). Each trial subclasses it and overrides what its design does
# differently: the hero, the dressing, the ornaments.

from content import (BRAND, BRANDS, CATEGORIES, GOOD_TO_KNOW, HOW, LEADERSHIP, PROMISES,
                     REVIEWS, STATS, TIMELINE, TOWNS, WHY_NOT)
from icons import picture

HELPER = BRAND["helpline"]
PRETTY = BRAND["pretty"]


def stage(inner, cls=""):
    return '<section class="stage%s">\n<div class="wrap">\n%s\n</div>\n</section>\n' % (
        (" " + cls) if cls else "", inner)


def head(skin, kicker, title, sub="", cls=""):
    return '<div class="head%s">%s%s%s</div>' % (
        (" " + cls) if cls else "",
        skin.kicker(kicker),
        skin.title(title),
        ('<p class="lede">%s</p>' % sub) if sub else "")


class BaseSkin:
    """Everything the three new trials have in common. Override what differs."""

    label = "Trial 04"
    theme = "#0b0b0b"
    fonts = ()
    brand = BRAND

    # ---------------------------------------------------------------- pieces
    def icon(self, name, cls=""):
        return '<svg class="doodle%s" aria-hidden="true"><use href="#%s"></use></svg>' % (
            (" " + cls) if cls else "", name)

    def mark(self):
        return '<span class="brand__mark" aria-hidden="true">W</span>'

    def header(self, current=""):
        nav = ""
        for href, label in (("index.html", "Home"), ("products.html", "Catalogue"),
                            ("stores.html", "Showrooms"), ("about.html", "About"),
                            ("contact.html", "Contact")):
            mark = ' aria-current="page"' if href == current else ""
            nav += '<a href="%s"%s>%s</a>' % (href, mark, label)
        return """
<header class="site-header">
  <div class="wrap site-header__inner">
    <a class="brand" href="index.html" aria-label="WHYNOT — home">
      %s
      <span class="brand__text">
        <span class="brand__name">WHYNOT</span>
        <span class="brand__tag">%s</span>
      </span>
    </a>
    <nav class="nav" aria-label="Primary">%s</nav>
    <div class="header-actions">
      <a class="icon-btn list-btn" href="products.html#my-list" aria-label="My list">
        %s<span class="list-btn__count" data-list-count hidden>0</span>
      </a>
      <a class="btn btn--sm btn--brand header-cta" href="tel:+91%s">Call %s</a>
      <button class="icon-btn burger" type="button" data-drawer-open aria-expanded="false"
              aria-controls="drawer" aria-label="Open menu">%s</button>
    </div>
  </div>
</header>
""" % (self.mark(), BRAND["tagline"], nav, self.icon("i-cart"), HELPER, PRETTY, self.icon("i-menu"))

    def footer(self):
        return """
<footer class="site-footer">
  <div class="wrap">
    <div class="footer__grid">
      <div class="footer__col footer__col--brand">
        <span class="brand">%s
          <span class="brand__text">
            <span class="brand__name">WHYNOT</span>
            <span class="brand__tag">%s</span>
          </span>
        </span>
        <p>WHYNOT Electronics Pvt Ltd. Electronics and home appliances across the Godavari districts and Visakhapatnam since 1994.</p>
        <p><a href="%s" target="_blank" rel="noopener noreferrer">Get the WHYNOT app</a></p>
      </div>
      <div class="footer__col">
        <h2>Shop</h2>
        <ul>
          <li><a href="products.html?cat=tv">Televisions</a></li>
          <li><a href="products.html?cat=fridge">Refrigerators</a></li>
          <li><a href="products.html?cat=ac">Air conditioners</a></li>
          <li><a href="products.html?cat=washer">Washing machines</a></li>
          <li><a href="products.html?cat=kitchen">Kitchen</a></li>
          <li><a href="products.html">Everything else</a></li>
        </ul>
      </div>
      <div class="footer__col">
        <h2>Company</h2>
        <ul>
          <li><a href="about.html">About WHYNOT</a></li>
          <li><a href="stores.html">All 25 showrooms</a></li>
          <li><a href="contact.html">Contact &amp; service</a></li>
          <li><a href="products.html#my-list">My list</a></li>
        </ul>
      </div>
      <div class="footer__col">
        <h2>Come over</h2>
        <ul>
          <li>%s</li>
          <li><a href="tel:+91%s">%s</a></li>
          <li><a href="mailto:%s">%s</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__bottom">
      <p>© <span data-year>2026</span> WHYNOT Electronics Pvt Ltd. Every address, phone number and brand name here belongs to the company and was taken from their public website.</p>
      <p>Concept redesign — <strong>%s</strong> · not the live site · <a href="../index.html">all trials</a> · imagery is AI-generated stand-in art, not commissioned work.</p>
    </div>
  </div>
</footer>
""" % (self.mark(), BRAND["tagline"], BRAND["app_url"], ", ".join(BRAND["address_lines"]),
       HELPER, PRETTY, BRAND["email"], BRAND["email"], self.label)

    def mobile_bar(self):
        return """
<nav class="mobile-bar" aria-label="Quick actions">
  <a href="tel:+91%s">%sCall</a>
  <a href="stores.html">%sShowrooms</a>
  <a href="products.html#my-list">%sMy list<span class="mobile-bar__count" data-list-count hidden>0</span></a>
</nav>
""" % (HELPER, self.icon("i-call"), self.icon("i-pin"), self.icon("i-cart"))

    # ------------------------------------------------------------- dressing
    def kicker(self, text):
        return '<p class="kicker">%s</p>' % text

    def title(self, text, cls=""):
        return '<h2 class="display%s">%s</h2>' % ((" " + cls) if cls else "", text)

    def sub(self, text):
        return '<p class="lede">%s</p>' % text

    def panel(self, inner, tone="", cls=""):
        return '<div class="panel%s%s">%s</div>' % (
            (" " + tone) if tone else "", (" " + cls) if cls else "", inner)

    def btn(self, label, href="", variant="brand", icon="", attrs="", cls=""):
        tag = "a" if href else "button"
        href_attr = ' href="%s"' % href if href else ' type="button"'
        return '<%s%s class="btn btn--%s%s"%s>%s%s</%s>' % (
            tag, href_attr, variant, (" " + cls) if cls else "", attrs,
            (self.icon(icon) + " ") if icon else "", label, tag)

    def sticker(self, text, tone=""):
        return '<span class="sticker%s">%s</span>' % ((" " + tone) if tone else "", text)

    # Optional hooks. Each design overrides the ones that carry its personality;
    # everything else falls back to plain markup that the stylesheet dresses.
    decorate_stats = False

    def extra_chips(self):
        """Optional row of popular-search chips above the catalogue."""
        return ""

    def before_list(self):
        """Optional banner above the shortlist panel."""
        return ""

    def store_head(self):
        """Optional line above the showroom search."""
        return ""

    def band_picture(self):
        return picture("storefront", "A WHYNOT-style showroom at dusk.", 1200, 675, eager=False)

    def band_picture_two(self):
        return picture("storefront", "A WHYNOT-style showroom at dusk.", 1200, 675)

    def page_hero(self, kicker, title, lead, ctas=None, art=None):
        return stage("%s<h1 class=\"display display--xl\">%s</h1>%s" % (
            self.kicker(kicker), title, self.sub(lead)), "stage--pagehero")

    def swash(self):
        """A decorative divider. Each design supplies its own."""
        return ""

    def after_hero(self):
        return ""

    def hero(self, **kw):
        raise NotImplementedError


# ---------------------------------------------------------------- page pieces

def stats(skin):
    cells = "".join(
        '<div class="stat">'
        '<span class="stat__v"><span data-count="%s">%s</span></span>'
        '<span class="stat__l">%s</span></div>' % (v.rstrip("M"), v, l)
        for v, l in STATS)
    return stage('<div class="stats">%s</div>' % cells, "stage--stats")


def categories(skin):
    tiles = "".join(
        '<a class="tile" href="products.html?cat=%s">'
        '<span class="tile__art tile__art--%d">%s</span>'
        '<span class="tile__name">%s</span><span class="tile__meta">%s</span></a>' % (
            cid, i % 4 + 1, skin.icon("i-" + {"tv": "tv", "fridge": "fridge", "ac": "ac", "washer": "washer",
                                              "kitchen": "mixer", "water": "droplet", "lighting": "bulb",
                                              "audio": "speaker", "mobile": "phone", "cleaning": "vacuum"}[cid]),
            name, meta)
        for i, (cid, name, meta) in enumerate(CATEGORIES))
    return stage(head(skin, "Shop by category", "Ten aisles.<br>One roof.",
                      "Prices move with the season, so every card asks for today's price — and we answer with the real number, not a range.")
                 + '<div class="tiles">%s</div>' % tiles, "stage--cats")


def featured(skin):
    return stage(head(skin, "Popular right now", "What people<br>actually ask for",
                      "The four a month of “what's good in this budget?” conversations usually end on. "
                      "Sample catalogue — today's price comes from your branch.")
                 + '<div class="products products--featured" data-featured></div>'
                 + '<p class="stage__more">%s</p>' % skin.btn("Open the full catalogue", "products.html", "ink"),
                 "stage--featured")


def band(skin, pic, title, text, link_href="stores.html", link_text="All 25 showrooms"):
    cap = ('<div class="band__cap"><p class="band__title">%s</p><p>%s</p>'
           '<p><a class="band__link" href="%s">%s</a></p></div>' % (title, text, link_href, link_text))
    return stage('<figure class="band" data-reveal>%s%s</figure>' % (pic, cap), "stage--band")


def why_not(skin):
    items = "".join(
        skin.panel('<span class="q__no">%s</span><p class="q__q">%s</p><p class="q__a">%s</p>' % (no, q, a),
                   tone="panel--tone%d" % (i % 4 + 1), cls="q") for i, (no, q, a) in enumerate(WHY_NOT))
    return stage(head(skin, "The name is the question", "Why not…",
                      "Four questions WHYNOT has answered the same way since an LML showroom in Tanuku in 1994.")
                 + '<div class="qs">%s</div>' % items, "stage--why")


def reviews(skin):
    cards = "".join(
        skin.panel('<p class="quote">“%s”</p><p class="quote__by">%s</p>' % (q, by),
                   tone="panel--tone%d" % (i % 3 + 1), cls="review")
        for i, (q, by) in enumerate(REVIEWS))
    return stage(head(skin, "In their words", "People who<br>came back",
                      "Reviews shown as they were written on the current site. Named, dated reviews with permission "
                      "would do more work — see the notes in the repo.")
                 + '<div class="reviews">%s</div>' % cards, "stage--reviews")


def brands(skin):
    return stage(head(skin, "Brands", "Everything<br>you'd expect")
                 + '<ul class="brands">%s</ul>' % "".join("<li>%s</li>" % b for b in BRANDS)
                 + '<p class="note">Names only — no third-party logos were lifted for this concept.</p>', "stage--brands")


def cta(skin):
    inner = """
    <div class="cta__copy">
      <p class="kicker">%s Open %s · <span data-shop-state>Open now</span></p>
      <h2 class="display display--md">Come and see it in person</h2>
      <p>Pick what you like in the catalogue, send the list, and a person from your nearest branch calls with today's price.</p>
      <p class="cta__phone"><a href="tel:+91%s">%s</a></p>
    </div>
    <div class="actions">
      %s
      %s
    </div>""" % (skin.icon("i-clock"), BRAND["hours"], HELPER, PRETTY,
                 skin.btn("Start a list", "products.html", "brand", icon="i-cart"),
                 skin.btn("Showrooms", "stores.html", "cyan", icon="i-pin"))
    return stage(skin.panel(inner, tone="panel--cta", cls="cta"), "stage--cta")


def toolbar(skin):
    return """
<div class="toolbar">
  <div class="search">
    <label class="visually-hidden" for="q">Search the catalogue</label>
    %s
    <input id="q" type="search" placeholder="Search: TV, fridge, 1.5 ton…" autocomplete="off" data-product-search>
  </div>
  <label class="visually-hidden" for="town">Only show what is stocked in</label>
  <select class="select" id="town" data-town-select><option value="all">All towns</option></select>
</div>""" % skin.icon("i-search")


def catalogue(skin):
    return stage("""%s
%s
<div class="chips" role="group" aria-label="Filter by category" data-cat-chips></div>
<p class="count" data-result-count aria-live="polite">Loading…</p>
<div class="products" data-products><p class="muted">Loading the catalogue…</p></div>""" % (
        toolbar(skin), skin.extra_chips()), "stage--catalogue", )


def my_list(skin):
    return stage("""%s
%s
<div data-list-panel></div>""" % (
        head(skin, "My list", '<span data-list-label>0 items</span> in your list',
             "It stays on this phone until you send it. WhatsApp, call or email — whichever is easiest. "
             "No account, no card, nothing charged."),
        skin.before_list()), "stage--list")


def how(skin):
    steps = "".join(
        skin.panel('<span class="q__no">%s</span><p class="how__t">%s</p><p class="muted">%s</p>' % (no, t, d),
                   tone="panel--tone%d" % (i % 3 + 1), cls="how__step")
        for i, (no, t, d) in enumerate(HOW))
    return stage(head(skin, "How buying works here", "Three steps.<br>No maze.") + '<div class="steps">%s</div>' % steps)


def promises(skin):
    cards = "".join(
        skin.panel('<p class="promise__t">%s %s</p><p class="muted">%s</p>' % (
            skin.icon(["i-shield", "i-tag", "i-truck", "i-people"][i % 4]), t, d), cls="promise")
        for i, (t, d) in enumerate(PROMISES))
    return stage('<div class="promises">%s</div>' % cards, "stage--promises")


def stores_body(skin):
    chips = "".join(
        '<button class="chip" type="button" data-district="%s" aria-pressed="%s">%s</button>' % (d, "true" if d == "all" else "false", label)
        for d, label in (("all", "All"), ("West Godavari", "West Godavari"),
                         ("East Godavari", "East Godavari"), ("Visakhapatnam", "Visakhapatnam")))
    return stage("""%s
<div class="toolbar toolbar--stores">
  <div class="search">
    <label class="visually-hidden" for="store-search">Search showrooms</label>
    %s
    <input id="store-search" type="search" placeholder="Town, district or pincode…" autocomplete="off" data-store-search>
  </div>
  <div class="chips" role="group" aria-label="Filter by district">%s</div>
</div>
<p class="count" data-store-count aria-live="polite">25 showrooms</p>
<div class="stores" data-store-list><p class="muted">Loading the showroom list…</p></div>
<div class="empty" data-store-empty hidden>
  <p class="display display--xs">No showroom matches that</p>
  <p class="muted">Try the town name, a pincode or the district — or just call %s.</p>
  <button class="btn btn--sm" type="button" data-store-clear>Clear filters</button>
</div>
<noscript><div class="status"><strong>This list is drawn by JavaScript.</strong>
<span>In production it would render on the server instead. Meanwhile the full list is on
<a href="https://www.whynotindia.in/stores" target="_blank" rel="noopener noreferrer">whynotindia.in/stores</a>, or call %s.</span></div></noscript>""" % (
        skin.store_head(), skin.icon("i-search"), chips, PRETTY, PRETTY), "stage--stores")


def good_to_know(skin):
    cards = "".join(
        skin.panel('<p class="promise__t">%s</p><p class="muted">%s</p>' % (t, d),
                   tone="panel--tone%d" % (i % 4 + 1), cls="know")
        for i, (t, d) in enumerate(GOOD_TO_KNOW))
    return stage(head(skin, "Good to know", "Before you<br>drive over") + '<div class="knows">%s</div>' % cards)


def timeline(skin):
    cards = "".join(
        skin.panel('<span class="q__no">%s</span><p class="tl__t">%s</p><p class="muted">%s</p>' % (y, t, d),
                   tone="panel--tone%d" % (i % 6 + 1), cls="tl")
        for i, (y, t, d) in enumerate(TIMELINE))
    return stage(head(skin, "The story", "Six panels,<br>32 years") + '<div class="tls">%s</div>' % cards)


def leadership(skin):
    cards = "".join(
        skin.panel('<p class="lead__role">%s</p><p class="lead__name">%s</p>' % (r, n), cls="lead")
        for r, n in LEADERSHIP)
    return stage(head(skin, "Leadership today", "The family<br>at the desk") + '<div class="leads">%s</div>' % cards)


def contact_form(skin):
    return """
<form class="form" data-contact-form novalidate>
  %s
  <div class="form__row">
    <div class="field">
      <label for="name">Your name</label>
      <input class="input" id="name" name="name" type="text" autocomplete="name" required aria-describedby="name-error">
      <p class="error" id="name-error" role="alert"></p>
    </div>
    <div class="field">
      <label for="mobile">Mobile number</label>
      <input class="input" id="mobile" name="mobile" type="tel" inputmode="numeric" autocomplete="tel" placeholder="10 digits" required aria-describedby="mobile-error">
      <p class="error" id="mobile-error" role="alert"></p>
    </div>
  </div>
  <div class="field">
    <label for="town">Your town</label>
    <input class="input" id="town" name="town" type="text" autocomplete="address-level2" placeholder="e.g. Bhimavaram">
  </div>
  <div class="field">
    <label for="message">What are you looking for?</label>
    <textarea class="textarea" id="message" name="message" required aria-describedby="message-error"
      placeholder="A 55-inch 4K TV for the hall, budget around Rs 60,000. Is it available in Bhimavaram?"></textarea>
    <p class="error" id="message-error" role="alert"></p>
  </div>
  <div class="status" data-form-status aria-live="polite"></div>
  <div class="actions">
    <button class="btn btn--brand" type="submit">Send it</button>
    <a class="btn btn--cyan" href="https://wa.me/91%s?text=Hi%%20WHYNOT%%2C%%20I%%20have%%20a%%20question" target="_blank" rel="noopener noreferrer">%s WhatsApp instead</a>
  </div>
  <p class="note">This concept build has no server behind it — it checks your details, then tells you honestly that nothing was sent.</p>
</form>""" % (skin.icon("i-call"), HELPER, skin.icon("i-whatsapp"))


def contact_cards(skin):
    d = BRAND
    cards = skin.panel('<p class="promise__t">%s %s</p><p>Central helpline, %s. Installation, service, stock checks, anything.</p>'
                       '<div class="actions">%s %s</div>' % (
                           skin.icon("i-call"), PRETTY, d["hours"],
                           skin.btn("Call now", "tel:+91" + HELPER, "ink"),
                           skin.btn("Copy number", "", "ghost", icon="i-copy", attrs=' data-copy="%s"' % HELPER)),
                       tone="panel--tone1", cls="know")
    cards += skin.panel('<p class="promise__t">%s Faulty product?</p><p>Keep the bill number handy and call the helpline. '
                        'We coordinate the brand\'s authorised service centre for you — you don\'t chase two companies.</p>'
                        % skin.icon("i-wrench"), tone="panel--tone2", cls="know")
    cards += skin.panel('<p class="promise__t">%s Dealers &amp; bulk orders</p><p>Buying for a hostel, a function hall or a '
                        'reseller business? Email <a href="mailto:%s">%s</a> with quantities and we\'ll quote separately.</p>'
                        % (skin.icon("i-box"), d["email"], d["email"]), tone="panel--tone3", cls="know")
    cards += skin.panel('<p class="promise__t">%s Registered office</p><p class="muted">%s</p>'
                        '<p>%s</p>' % (skin.icon("i-store"), d["address_one_line"],
                                       skin.btn("All 25 showrooms", "stores.html", "ghost", icon="i-pin")),
                        tone="panel--tone4", cls="know")
    return '<div class="knows knows--contact">%s</div>' % cards


# ------------------------------------------------------------------ pages

def home(skin):
    return (skin.hero() + skin.after_hero() + stats(skin) + skin.swash() + categories(skin)
            + featured(skin) + band(skin, skin.band_picture(),
                                    "Every town deserves the good stuff", TOWNS)
            + skin.swash() + why_not(skin) + reviews(skin) + brands(skin) + cta(skin))


def catalogue_page(skin):
    return (skin.page_hero("Catalogue · 17 products · 10 categories",
                           "Pick what you like.<br>We'll price it.",
                           "Add anything you're curious about to <strong>my list</strong>, send it in one tap, "
                           "and someone from your nearest branch replies with today's price and stock. "
                           "No card details, no checkout maze.")
            + catalogue(skin) + my_list(skin) + how(skin) + promises(skin))


def stores_page(skin):
    return (skin.page_hero("Showrooms · 25 locations",
                           "One is probably<br>20 minutes away.",
                           "Search by town, district or pincode. Every address opens straight into Google Maps on your phone.",
                           ctas=[("Call " + PRETTY, "tel:+91" + HELPER, "brand", "i-call"),
                                 ("Copy number", "", "cyan", "i-copy")])
            + stores_body(skin) + good_to_know(skin))


def about_page(skin):
    return (skin.page_hero("About us",
                           "One shop.<br>One question.",
                           "On 27 February 1994 Mr. Jujjavarapu Venkata Rayudu opened an LML showroom in Tanuku and called it "
                           "<strong>Whynot</strong>. Thirty-two years later it is 25 showrooms and 300 people — still run by the same family.",
                           art="portrait")
            + timeline(skin)
            + band(skin, skin.band_picture_two(),
                   "“Nothing is impossible”",
                   "Mr. Rayudu's instinct was to go where bigger retailers did not: the tier-3 and tier-4 towns. "
                   "That decision built the network — and the barrier around it.")
            + leadership(skin) + brands(skin))


def contact_page(skin):
    return (skin.page_hero("Contact",
                           "Tell us what you need.<br>A person calls back.",
                           "No ticket numbers, no “within 48 hours”. Leave your number and someone from your nearest "
                           "showroom rings you between 10 am and 9 pm.")
            + stage(contact_form(skin) + contact_cards(skin), "stage--contact"))


def notfound(skin):
    return (skin.page_hero("Error 404", "This page is<br>missing.",
                           "Old link, moved page, or a typo in the address. Nothing is lost — the showrooms are all where you left them.",
                           ctas=[("Back home", "index.html", "brand", "i-store"),
                                 ("Catalogue", "products.html", "cyan", "i-cart"),
                                 ("Showrooms", "stores.html", "ghost", "i-pin")])
            + "")
