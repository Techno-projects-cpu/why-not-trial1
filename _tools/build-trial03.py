#!/usr/bin/env python3
"""
Builder for Trial 03 ("Panel & Ink").

Usage:  python3 _tools/build-trial03.py

Writes the six pages of trial-03-anime/ from the templates below, so the header,
footer, phone bar and the icon sprite stay identical across pages. Edit the page
bodies here and re-run — or edit the HTML directly and stop using this script
(in which case delete it, or the next run will overwrite your edits).
"""

import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from panels import sprite  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "trial-03-anime")

HELPLINE = "8886222448"
PRETTY = "88862 22448"

D = lambda i, c="": '<svg class="doodle %s" aria-hidden="true"><use href="#%s"></use></svg>' % (c, i)

HEAD = """<!DOCTYPE html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0e1230">
<link rel="canonical" href="https://www.whynotindia.in/">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<link rel="icon" href="assets/img/logo-mark.svg" type="image/svg+xml">
<link rel="icon" href="assets/img/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preload" href="assets/fonts/anton-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/plus-jakarta-sans-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/style.css">
<script>
  /* Marks the document as scripted, so reveal-on-scroll can never hide content
     from a visitor (or a crawler) without JavaScript. */
  document.documentElement.classList.add("js");
</script>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
{extra}
"""

HEADER = """
<header class="site-header">
  <div class="wrap site-header__inner">
    <a class="brand" href="index.html" aria-label="WHYNOT — home">
      <span class="brand__mark" aria-hidden="true">W</span>
      <span class="brand__text">
        <span class="brand__name">WHYNOT</span>
        <span class="brand__tag">We drive the change</span>
      </span>
    </a>

    <nav class="nav" aria-label="Primary">
      <a href="index.html"{c_home}>Home</a>
      <a href="products.html"{c_products}>Catalogue</a>
      <a href="stores.html"{c_stores}>Showrooms</a>
      <a href="about.html"{c_about}>About</a>
      <a href="contact.html"{c_contact}>Contact</a>
    </nav>

    <div class="header-actions">
      <a class="icon-btn list-btn" href="products.html#my-list" aria-label="My list">
        <!--ART_i-cart-->
        <span class="list-btn__count" data-list-count hidden>0</span>
      </a>
      <a class="btn btn--sm btn--cyan header-cta" href="tel:+91{phone}">Call {pretty}</a>
      <button class="icon-btn burger" type="button" data-drawer-open aria-expanded="false" aria-controls="drawer" aria-label="Open menu">
        <!--ART_i-menu-->
      </button>
    </div>
  </div>
</header>

<div class="drawer" id="drawer" data-drawer data-open="false" aria-hidden="true">
  <div class="drawer__top">
    <span class="brand">
      <span class="brand__mark" aria-hidden="true">W</span>
      <span class="brand__text"><span class="brand__name">WHYNOT</span></span>
    </span>
    <button class="icon-btn" type="button" data-drawer-close aria-label="Close menu"><!--ART_i-close--></button>
  </div>
  <nav class="drawer__nav" aria-label="Mobile">
    <a href="index.html"{c_home}>Home</a>
    <a href="products.html"{c_products}>Catalogue</a>
    <a href="stores.html"{c_stores}>Showrooms</a>
    <a href="about.html"{c_about}>About us</a>
    <a href="contact.html"{c_contact}>Contact</a>
  </nav>
  <div class="drawer__foot">
    <a class="btn btn--magenta btn--block" href="tel:+91{phone}">Call {pretty}</a>
    <p class="label" style="text-align:center;color:var(--ink-3)">Open 10 am – 9 pm · a person answers</p>
  </div>
</div>
"""

FOOTER = """
<footer class="site-footer">
  <div class="wrap">
    <div class="footer__grid">
      <div class="footer__brand">
        <span class="brand">
          <span class="brand__mark" aria-hidden="true">W</span>
          <span class="brand__text">
            <span class="brand__name">WHYNOT</span>
            <span class="brand__tag">We drive the change</span>
          </span>
        </span>
        <p style="font-size:var(--t-sm);color:rgba(255,255,255,.78)">WHYNOT Electronics Pvt Ltd. Electronics and home appliances across the Godavari districts and Visakhapatnam since 1994.</p>
        <p style="font-size:var(--t-sm)"><a href="https://play.google.com/store/apps/details?id=in.absolin.whynotcust" target="_blank" rel="noopener noreferrer">Get the WHYNOT app</a></p>
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
          <li>RS No 24/1, Ground &amp; Cellar,<br>Sri Sowdha Towers, Undrajavaram Road,<br>Tanuku 534211, Andhra Pradesh</li>
          <li><a href="tel:+91{phone}">{pretty}</a></li>
          <li><a href="mailto:whynot.rayudu@gmail.com">whynot.rayudu@gmail.com</a></li>
        </ul>
      </div>
    </div>

    <div class="footer__bottom">
      <p>© <span data-year>2026</span> WHYNOT Electronics Pvt Ltd. Every address, phone number and brand name here belongs to the company and was taken from their public website.</p>
      <p>Concept redesign — <strong>Trial 03 “Panel &amp; Ink”</strong> · not the live site · <a href="../index.html">all trials</a> · key art is AI-generated stand-in art, not commissioned illustration.</p>
    </div>
  </div>
</footer>

<nav class="mobile-bar" aria-label="Quick actions">
  <a href="tel:+91{phone}"><!--ART_i-call-->Call</a>
  <a href="stores.html"><!--ART_i-pin-->Showrooms</a>
  <a href="products.html#my-list"><!--ART_i-cart-->My list <span class="mobile-bar__count" data-list-count hidden>0</span></a>
</nav>

<div class="toast" data-toast role="status" aria-live="polite" data-open="false"></div>
"""

SCRIPTS = """<script src="assets/js/main.js" defer></script>
<script src="assets/js/products.js" defer></script>
{extra}"""


def page(filename, title, desc, body, current="", scripts_extra=""):
    marks = {k: (' aria-current="page"' if k == current else "")
             for k in ("c_home", "c_products", "c_stores", "c_about", "c_contact")}

    def art(html):
        for token, icon in (("i-menu", "i-menu"), ("i-close", "i-close"), ("i-cart", "i-cart"),
                            ("i-call", "i-call"), ("i-pin", "i-pin"), ("i-whatsapp", "i-whatsapp")):
            html = html.replace("<!--ART_%s-->" % token, D(icon))
        return html

    html = HEAD.format(title=title, desc=desc, extra=sprite())
    html += art(HEADER.format(phone=HELPHONE, pretty=PRETTY, **marks))
    html += art(body)
    html += art(FOOTER.format(phone=HELPHONE, pretty=PRETTY))
    html += SCRIPTS.format(extra=scripts_extra)

    with io.open(os.path.join(ROOT, filename), "w", encoding="utf-8") as f:
        f.write(html + "\n</body>\n</html>\n")
    print("  wrote %-14s %6d bytes" % (filename, len(html)))


HELPHONE = "8886222448"

# ----------------------------------------------------------------- page: home
HOME = """
<main id="main">

  <section class="hero">
    <div class="hero__glow" aria-hidden="true"></div>
    <div class="speedlines speedlines--dark" aria-hidden="true">
      <svg viewBox="0 0 100 100" preserveAspectRatio="none"><use href="#d-speed"></use></svg>
    </div>

    <div class="wrap hero__inner">
      <div class="hero__copy">
        <p class="bubble" style="align-self:start">Godavari districts · since 1994</p>
        <h1 class="shout shout--xl">Big brands.<br><span class="ko">Small towns.</span><br><span class="outline outline--light">Why not?</span></h1>
        <p class="hero__lead">Twenty-five WHYNOT showrooms in 23 towns, every major brand, and a phone number that still works five years after you buy. That has been the whole story since 1994.</p>
        <div class="hero__cta">
          <a class="btn btn--gold" href="products.html">{i_cart} See what we sell</a>
          <a class="btn btn--cyan" href="stores.html">{i_pin} Find my showroom</a>
        </div>
        <ul class="hero__points">
          <li>{i_check} 32 years</li>
          <li>{i_people} 300 staff</li>
          <li>{i_sun} Open 10–9 daily</li>
          <li>{i_truck} Delivery &amp; install</li>
        </ul>
      </div>

      <div class="hero__art">
        <div class="hero__frame">
          <picture>
            <source srcset="assets/img/hero-character.avif" type="image/avif">
            <source srcset="assets/img/hero-character.webp" type="image/webp">
            <img src="assets/img/hero-character.jpg" width="760" height="1140" fetchpriority="high" decoding="async"
                 alt="Illustration: a shopper in a WHYNOT showroom pointing at a large television, speed lines and sparkles behind her.">
          </picture>
        </div>
        <span class="hero__badge" aria-hidden="true">
          <svg viewBox="0 0 120 120"><use href="#d-badge"></use></svg>
          <span>25 shops<br>1 number</span>
        </span>
      </div>
    </div>
  </section>

  <section class="stats-strip" aria-label="WHYNOT at a glance">
    <div class="wrap" style="padding-inline:0">
      <div class="stats-strip__inner">
        <div class="stat"><p class="stat__value"><span data-count="2.5">2.5</span>M</p><p class="stat__label">Customers served</p></div>
        <div class="stat"><p class="stat__value"><span data-count="1">1</span>M</p><p class="stat__label">Products sold</p></div>
        <div class="stat"><p class="stat__value"><span data-count="25">25</span></p><p class="stat__label">Showrooms, 23 towns</p></div>
        <div class="stat"><p class="stat__value"><span data-count="32">32</span></p><p class="stat__label">Years since 1994</p></div>
      </div>
    </div>
  </section>

  <section class="section" id="categories">
    <div class="wrap">
      <div class="section-head">
        <p class="bubble">{i_bolt} Shop by category</p>
        <h2 class="shout shout--lg">Ten aisles.<br>One roof.</h2>
        <p>Tap a panel to see what we stock. Prices move with the season, so every card asks you to get today's price — and we answer with the real number, not a range.</p>
      </div>

      <div class="grid-tiles">
        <a class="tile" href="products.html?cat=tv"><span class="tile__art">{i_tv}</span><span class="tile__name">Televisions</span><span class="tile__meta">QLED · 4K · smart</span></a>
        <a class="tile" href="products.html?cat=fridge"><span class="tile__art">{i_fridge}</span><span class="tile__name">Refrigerators</span><span class="tile__meta">Single &amp; double door</span></a>
        <a class="tile" href="products.html?cat=ac"><span class="tile__art">{i_ac}</span><span class="tile__name">Air conditioners</span><span class="tile__meta">Split · inverter</span></a>
        <a class="tile" href="products.html?cat=washer"><span class="tile__art">{i_washer}</span><span class="tile__name">Washing machines</span><span class="tile__meta">Semi &amp; automatic</span></a>
        <a class="tile" href="products.html?cat=kitchen"><span class="tile__art">{i_mixer}</span><span class="tile__name">Kitchen</span><span class="tile__meta">Mixers · grinders</span></a>
        <a class="tile" href="products.html?cat=water"><span class="tile__art">{i_droplet}</span><span class="tile__name">Water &amp; geysers</span><span class="tile__meta">Purifiers · heaters</span></a>
        <a class="tile" href="products.html?cat=lighting"><span class="tile__art">{i_bulb}</span><span class="tile__name">Lighting</span><span class="tile__meta">LED · strips</span></a>
        <a class="tile" href="products.html?cat=audio"><span class="tile__art">{i_speaker}</span><span class="tile__name">Audio</span><span class="tile__meta">Speakers · bars</span></a>
        <a class="tile" href="products.html?cat=mobile"><span class="tile__art">{i_phone}</span><span class="tile__name">Mobiles</span><span class="tile__meta">5G · budget to flagship</span></a>
        <a class="tile" href="products.html?cat=cleaning"><span class="tile__art">{i_vacuum}</span><span class="tile__name">Cleaning</span><span class="tile__meta">Vacuum · mops</span></a>
      </div>
    </div>
  </section>

  <section class="section" id="popular">
    <div class="wrap">
      <div class="section-head">
        <p class="bubble">{i_star} Popular right now</p>
        <span class="line-strip" aria-hidden="true"><svg viewBox="0 0 64 64"><use href="#d-lines"></use></svg></span>
        <h2 class="shout shout--lg">What people<br>actually ask for</h2>
        <p>The four a month of “what's good in this budget?” conversations usually end on. Sample catalogue — today's price comes from your branch.</p>
      </div>

      <div class="products" data-featured></div>

      <p style="margin-top:24px">
        <a class="btn btn--ink" href="products.html">Open the full catalogue {i_arrow_svg}</a>
      </p>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <figure class="band" data-reveal>
        <picture>
          <source srcset="assets/img/storefront-dusk.avif" type="image/avif">
          <source srcset="assets/img/storefront-dusk.webp" type="image/webp">
          <img src="assets/img/storefront-dusk.jpg" width="1200" height="675" loading="lazy" decoding="async"
               alt="Illustration: a small-town electronics showroom at dusk, lit windows, a scooter parked outside, the moon above.">
        </picture>
        <figcaption class="band__caption">
          <p class="shout shout--sm">Every town deserves the good stuff</p>
          <p>Tanuku · Tadepalligudem · Rajahmundry · Bhimavaram · Eluru · Kakinada · Palakollu · Narasapuram · Amalapuram · Mandapeta · Anakapalle · and 12 more.</p>
          <p><a class="label" style="color:var(--cyan)" href="stores.html">All 25 showrooms</a></p>
        </figcaption>
      </figure>
    </div>
  </section>

  <section class="section" id="why-not">
    <div class="wrap">
      <div class="section-head">
        <p class="bubble">{i_sparkle} The name is the question</p>
        <h2 class="shout shout--lg">Why not…</h2>
        <p>Four questions WHYNOT has answered the same way since an LML showroom in Tanuku in 1994.</p>
      </div>

      <div class="qs">
        <div class="q panel" style="border-width:var(--line)">
          <span class="q__no">01</span>
          <p class="q__q">…put it in your town?</p>
          <p>Twenty-five showrooms in 23 towns, because “drive two hours to the city” is not service. Most opened before anyone else thought the town was big enough.</p>
        </div>
        <div class="q panel panel--gold" style="border-width:var(--line)">
          <span class="q__no" style="color:var(--ink)">02</span>
          <p class="q__q">…pick up the phone after the sale?</p>
          <p>Installation, service and follow-up come from the branch you bought at — not from a call centre that has never seen your street.</p>
        </div>
        <div class="q panel panel--cyan" style="border-width:var(--line)">
          <span class="q__no" style="color:var(--ink)">03</span>
          <p class="q__q">…give the honest price first time?</p>
          <p>Ask for today's price and you get the number we can actually sell at. EMI and exchange details upfront, no theatre.</p>
        </div>
        <div class="q panel panel--violet" style="border-width:var(--line)">
          <span class="q__no" style="color:var(--gold)">04</span>
          <p class="q__q">…still be here in ten years?</p>
          <p>Thirty-two years, two generations of the same family, 300 people from the towns they serve. Your neighbour is the shop.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="brands">
    <div class="wrap">
      <div class="section-head">
        <p class="bubble">{i_tag} Brands</p>
        <h2 class="shout shout--lg">Everything<br>you'd expect</h2>
      </div>
      <ul class="brands" data-reveal>
        <li>LG</li><li>Samsung</li><li>Sony</li><li>Whirlpool</li><li>Bosch</li>
        <li>Daikin</li><li>IFB</li><li>Haier</li><li>Lloyd</li><li>Blue Star</li>
        <li>Mitsubishi</li><li>Panasonic</li><li>Hitachi</li><li>Vivo</li><li>Oppo</li>
        <li>Voltas</li><li>Amaron</li><li>V-Guard</li><li>Luminous</li><li>AO Smith</li>
      </ul>
      <p class="muted" style="font-size:var(--t-xs);margin-top:12px">Names only — no third-party logos were lifted for this concept.</p>
    </div>
  </section>

  <section class="section" id="reviews">
    <div class="wrap">
      <div class="section-head">
        <p class="bubble">{i_heart} In their words</p>
        <h2 class="shout shout--lg">People who<br>came back</h2>
        <p>Reviews shown as they were written on the current site. Named, dated reviews with permission would do more work — see the notes in the repo.</p>
      </div>
      <div class="stack" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px">
        <blockquote class="panel panel--gold panel__pad">
          <p class="shout shout--sm">“I've been a customer for five years. Their pricing and convenience work for me — that's just one of the reasons I use them.”</p>
          <p class="label" style="margin-top:10px;color:var(--ink-2)">WHYNOT customer</p>
        </blockquote>
        <blockquote class="panel panel__pad">
          <p class="shout shout--sm">“The best place for electronics and home appliances in both Godavari districts.”</p>
          <p class="label" style="margin-top:10px;color:var(--ink-2)">WHYNOT customer</p>
        </blockquote>
        <blockquote class="panel panel--cyan panel__pad">
          <p class="shout shout--sm">“It is a store with everything I need.”</p>
          <p class="label" style="margin-top:10px;color:var(--ink-2)">WHYNOT customer</p>
        </blockquote>
      </div>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap">
      <div class="cta panel panel--ink" data-reveal>
        <div class="speedlines speedlines--dark" aria-hidden="true">
          <svg viewBox="0 0 100 100" preserveAspectRatio="none"><use href="#d-speed"></use></svg>
        </div>
        <div class="cta__inner">
          <div class="stack">
            <p class="bubble" style="align-self:start">{i_clock} Open 10 am – 9 pm · <span data-shop-state>Open now</span></p>
            <h2 class="shout shout--md">Come and see it in person</h2>
            <p style="color:rgba(255,255,255,.8);max-width:46ch">Pick what you like in the catalogue, send the list, and a person from your nearest branch calls with today's price.</p>
            <p class="cta__phone"><a href="tel:+91{phone}">{pretty}</a></p>
          </div>
          <div class="cta__actions">
            <a class="btn btn--gold" href="products.html">{i_cart} Start a list</a>
            <a class="btn btn--cyan" href="stores.html">{i_pin} Showrooms</a>
          </div>
        </div>
      </div>
    </div>
  </section>

</main>
"""

# ------------------------------------------------------------- page: catalogue
PRODUCTS = """
<main id="main">

  <section class="hero" style="padding-block:clamp(24px,5vw,56px)">
    <div class="hero__glow" aria-hidden="true"></div>
    <div class="speedlines speedlines--dark" aria-hidden="true">
      <svg viewBox="0 0 100 100" preserveAspectRatio="none"><use href="#d-speed"></use></svg>
    </div>
    <div class="wrap" style="position:relative;display:grid;gap:14px">
      <p class="bubble" style="align-self:start">Catalogue · 17 products · 10 categories</p>
      <h1 class="shout shout--lg" style="color:#fff">Pick what you like.<br><span class="ko ko--cyan">We'll price it.</span></h1>
      <p class="hero__lead">Add anything you're curious about to <strong style="color:#fff">my list</strong>, send it in one tap, and someone from your nearest branch replies with today's price and stock. No card details, no checkout maze.</p>
    </div>
  </section>

  <section class="section section--tight" id="catalogue" style="padding-top:clamp(26px,5vw,48px)">
    <div class="wrap">
      <div class="toolbar">
        <div class="search">
          <label class="visually-hidden" for="q">Search the catalogue</label>
          {i_search}
          <input id="q" type="search" placeholder="SEARCH: TV, FRIDGE, 1.5 TON…" autocomplete="off" data-product-search>
        </div>
        <div class="search" style="border:0;box-shadow:none">
          <label class="visually-hidden" for="town">Only show what is stocked in</label>
          <select class="select" id="town" data-town-select>
            <option value="all">All towns</option>
          </select>
        </div>
      </div>

      <div class="chips" role="group" aria-label="Filter by category" data-cat-chips></div>

      <p class="result-count" data-result-count aria-live="polite">Loading…</p>

      <div class="chips" role="group" aria-label="Popular searches" style="margin:2px 0 4px">
        <a class="chip" href="products.html?cat=water">{i_geyser} Geysers</a>
        <a class="chip" href="products.html?cat=kitchen">{i_grinder} Wet grinders</a>
        <a class="chip" href="products.html?cat=kitchen">{i_micro} Microwave ovens</a>
        <a class="chip" href="products.html?cat=tv">{i_tv} 55-inch TVs</a>
      </div>

      <div class="products" data-products style="margin-top:12px">
        <p class="muted">Loading the catalogue…</p>
      </div>
    </div>
  </section>

  <section class="section" id="my-list">
    <div class="wrap has-tab">
      <span class="tab tab--magenta">My list</span>
      <div class="panel panel__pad">
        <div class="section-head" style="margin-bottom:18px">
          <h2 class="shout shout--md"><span data-list-label>0 items</span> in your list</h2>
          <p>It stays on this phone until you send it. WhatsApp, call or email — whichever is easiest. No account, no card, nothing charged.</p>
        </div>
        <div data-list-panel></div>
      </div>
    </div>
  </section>

  <section class="section" id="how">
    <div class="wrap">
      <div class="section-head">
        <p class="bubble">{i_check} How buying works here</p>
        <h2 class="shout shout--lg">Three steps.<br>No maze.</h2>
      </div>
      <div class="stack" style="grid-template-columns:repeat(auto-fit,minmax(220px,1fr));display:grid">
        <div class="panel panel__pad stack" style="gap:8px">
          <span class="q__no">01</span>
          <p class="shout shout--sm">Add what you like</p>
          <p class="muted" style="font-size:var(--t-sm)">Build a list while you browse. Nothing is charged and no account is needed.</p>
        </div>
        <div class="panel panel--cyan panel__pad stack" style="gap:8px">
          <span class="q__no" style="color:var(--ink)">02</span>
          <p class="shout shout--sm">Send it to us</p>
          <p style="font-size:var(--t-sm)">One tap opens WhatsApp with your whole list written out, or dials the helpline.</p>
        </div>
        <div class="panel panel--gold panel__pad stack" style="gap:8px">
          <span class="q__no" style="color:var(--ink)">03</span>
          <p class="shout shout--sm">We call with the price</p>
          <p style="font-size:var(--t-sm)">Today's price, which branch has it, EMI if you want it, and a delivery date.</p>
        </div>
      </div>

      <div class="stack" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:16px;margin-top:26px">
        <div class="panel panel__pad stack" style="gap:8px">
          <p class="label" style="color:var(--magenta)">{i_shield} Warranty &amp; service</p>
          <p class="muted" style="font-size:var(--t-sm)">Brand warranty runs through each manufacturer's authorised service network, and WHYNOT coordinates it for you.</p>
        </div>
        <div class="panel panel__pad stack" style="gap:8px">
          <p class="label" style="color:var(--magenta)">{i_tag} EMI &amp; exchange</p>
          <p class="muted" style="font-size:var(--t-sm)">Card and Bajaj-style EMI is available at the counter on most large appliances. Old product exchange value is quoted before you buy.</p>
        </div>
        <div class="panel panel__pad stack" style="gap:8px">
          <p class="label" style="color:var(--magenta)">{i_truck} Delivery &amp; installation</p>
          <p class="muted" style="font-size:var(--t-sm)">Fixed at the counter: what it costs, when it arrives, who installs it. No surprises on the bill.</p>
        </div>
        <div class="panel panel__pad stack" style="gap:8px">
          <p class="label" style="color:var(--magenta)">{i_people} Ask a human</p>
          <p class="muted" style="font-size:var(--t-sm)">Unsure between two models? Call <a class="label" style="color:var(--brand)" href="tel:+91{phone}">{pretty}</a> and describe the room. We do this all day.</p>
        </div>
      </div>
    </div>
  </section>

</main>
"""

# --------------------------------------------------------------- page: stores
STORES = """
<main id="main">

  <section class="hero" style="padding-block:clamp(24px,5vw,56px)">
    <div class="hero__glow" aria-hidden="true"></div>
    <div class="speedlines speedlines--dark" aria-hidden="true">
      <svg viewBox="0 0 100 100" preserveAspectRatio="none"><use href="#d-speed"></use></svg>
    </div>
    <div class="wrap" style="position:relative;display:grid;gap:14px">
      <p class="bubble" style="align-self:start">Showrooms · 25 locations</p>
      <h1 class="shout shout--lg" style="color:#fff">One is probably<br><span class="ko">20 minutes away.</span></h1>
      <p class="hero__lead">Search by town, district or pincode. Every address opens straight into Google Maps on your phone.</p>
      <div class="hero__cta">
        <a class="btn btn--gold" href="tel:+91{phone}">{i_call} {pretty}</a>
        <button class="btn btn--cyan" type="button" data-copy="{phone}">{i_copy} Copy number</button>
      </div>
    </div>
  </section>

  <section class="section section--tight" style="padding-top:clamp(26px,5vw,48px)">
    <div class="wrap">
      <div class="toolbar">
        <div class="search">
          <label class="visually-hidden" for="store-search">Search showrooms</label>
          {i_search}
          <input id="store-search" type="search" placeholder="TOWN, DISTRICT OR PINCODE…" autocomplete="off" data-store-search>
        </div>
        <div class="chips" role="group" aria-label="Filter by district">
          <button class="chip" type="button" data-district="all" aria-pressed="true">All</button>
          <button class="chip" type="button" data-district="West Godavari" aria-pressed="false">West Godavari</button>
          <button class="chip" type="button" data-district="East Godavari" aria-pressed="false">East Godavari</button>
          <button class="chip" type="button" data-district="Visakhapatnam" aria-pressed="false">Visakhapatnam</button>
        </div>
      </div>

      <p class="result-count" data-store-count aria-live="polite">25 showrooms</p>

      <div class="stores" data-store-list style="margin-top:12px">
        <p class="muted">Loading the showroom list…</p>
      </div>

      <div class="empty" data-store-empty hidden style="margin-top:12px">
        <p class="shout shout--sm">No showroom matches that</p>
        <p class="muted">Try the town name, a pincode or the district — or just call <a class="label" style="color:var(--brand)" href="tel:+91{phone}">{pretty}</a>.</p>
        <button class="btn btn--sm" type="button" data-store-clear>Clear filters</button>
      </div>

      <noscript>
        <div class="status" style="margin-top:20px">
          <strong>This list is drawn by JavaScript.</strong>
          <span>In production it would render on the server instead. Meanwhile the full list is on
          <a href="https://www.whynotindia.in/stores" target="_blank" rel="noopener noreferrer">whynotindia.in/stores</a>, or call {pretty}.</span>
        </div>
      </noscript>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <p class="bubble">{i_clock} Good to know</p>
        <h2 class="shout shout--lg">Before you<br>drive over</h2>
      </div>
      <div class="stack" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px">
        <div class="panel panel--gold panel__pad stack" style="gap:8px">
          <p class="shout shout--sm">Hours</p>
          <p style="font-size:var(--t-sm)">Open <strong>10 am – 9 pm</strong>. Festival weeks can shift that by an hour, so a call saves a trip. Right now: <strong data-shop-state>Open now</strong>.</p>
        </div>
        <div class="panel panel--cyan panel__pad stack" style="gap:8px">
          <p class="shout shout--sm">Stock is local</p>
          <p style="font-size:var(--t-sm)">Each branch carries its own stock. Tell us the model and your town and we'll confirm which showroom has it on the floor.</p>
        </div>
        <div class="panel panel--mint panel__pad stack" style="gap:8px">
          <p class="shout shout--sm">Brand stores in Tanuku</p>
          <p style="font-size:var(--t-sm)">The flagship building also houses an <strong>LG Best Shop</strong> and a <strong>Samsung Smart Plaza</strong>.</p>
        </div>
        <div class="panel panel--magenta panel__pad stack" style="gap:8px">
          <p class="shout shout--sm">Already bought from us?</p>
          <p style="font-size:var(--t-sm)">Installation, service or a fault — call <a style="color:#fff;text-decoration:underline" href="tel:+91{phone}">{pretty}</a> or walk into your branch. You don't need this website for that.</p>
        </div>
      </div>
    </div>
  </section>

</main>
"""

# ---------------------------------------------------------------- page: about
ABOUT = """
<main id="main">

  <section class="hero" style="padding-block:clamp(24px,5vw,56px)">
    <div class="hero__glow" aria-hidden="true"></div>
    <div class="speedlines speedlines--dark" aria-hidden="true">
      <svg viewBox="0 0 100 100" preserveAspectRatio="none"><use href="#d-speed"></use></svg>
    </div>
    <div class="wrap" style="position:relative;display:grid;gap:14px">
      <p class="bubble" style="align-self:start">{i_store} About us</p>
      <h1 class="shout shout--lg" style="color:#fff">One shop.<br><span class="ko ko--cyan">One question.</span></h1>
      <p class="hero__lead">On 27 February 1994 Mr. Jujjavarapu Venkata Rayudu opened an LML showroom in Tanuku and called it <strong style="color:#fff">Whynot</strong>. Thirty-two years later it is 25 showrooms and 300 people — still run by the same family.</p>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap">
      <div class="section-head">
        <p class="bubble">{i_clock} The story</p>
        <h2 class="shout shout--lg">Six panels,<br>32 years</h2>
      </div>

      <div class="stack" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px">
        <article class="panel panel__pad stack" style="gap:6px">
          <span class="q__no">1994</span>
          <h3 class="shout shout--sm">An LML showroom in Tanuku</h3>
          <p class="muted" style="font-size:var(--t-sm)">A commerce graduate and junior lawyer from Kanuru village starts his first venture, at a time when good products rarely reached semi-urban Andhra Pradesh.</p>
        </article>
        <article class="panel panel--cyan panel__pad stack" style="gap:6px">
          <span class="q__no" style="color:var(--ink)">1996</span>
          <h3 class="shout shout--sm">A Bajaj dealership</h3>
          <p style="font-size:var(--t-sm)">Two-wheelers at scale — and the reputation for after-sales service the electronics business still runs on.</p>
        </article>
        <article class="panel panel--gold panel__pad stack" style="gap:6px">
          <span class="q__no" style="color:var(--ink)">2006</span>
          <h3 class="shout shout--sm">Automobiles to electronics</h3>
          <p style="font-size:var(--t-sm)">The shift to consumer electronics and home appliances, expanding across the East and West Godavari districts into Visakhapatnam district.</p>
        </article>
        <article class="panel panel--violet panel__pad stack" style="gap:6px">
          <span class="q__no" style="color:var(--gold)">2025</span>
          <h3 class="shout shout--sm">WHYNOT Electronics Pvt Ltd</h3>
          <p style="font-size:var(--t-sm)">From 27 February 2025 the company incorporates formally — structured governance, stronger systems, deeper brand partnerships, a digital-first plan.</p>
        </article>
        <article class="panel panel--mint panel__pad stack" style="gap:6px">
          <span class="q__no" style="color:var(--ink)">Today</span>
          <h3 class="shout shout--sm">25 showrooms, 300 people</h3>
          <p style="font-size:var(--t-sm)">A shop in nearly every town of the two Godavari districts, more than 2.5 million customers served, the family still at the desk.</p>
        </article>
        <article class="panel panel--sun panel__pad stack" style="gap:6px">
          <span class="q__no" style="color:var(--ink)">Next</span>
          <h3 class="shout shout--sm">Same shop, online too</h3>
          <p style="font-size:var(--t-sm)">The stated ambition: 50+ branches and an omnichannel experience — same prices, same people, same service, wherever the customer starts.</p>
        </article>
      </div>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap">
      <figure class="band" data-reveal>
        <picture>
          <source srcset="assets/img/storefront-dusk.avif" type="image/avif">
          <source srcset="assets/img/storefront-dusk.webp" type="image/webp">
          <img src="assets/img/storefront-dusk.jpg" width="1200" height="675" loading="lazy" decoding="async"
               alt="Illustration of a small-town electronics showroom at dusk with its windows lit and a scooter parked outside.">
        </picture>
        <figcaption class="band__caption">
          <p class="shout shout--sm">“Nothing is impossible”</p>
          <p>Mr. Rayudu's instinct was to go where bigger retailers did not: the tier-3 and tier-4 towns. That decision built the network — and the barrier around it.</p>
        </figcaption>
      </figure>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <p class="bubble">{i_people} Leadership today</p>
        <h2 class="shout shout--lg">The family<br>at the desk</h2>
      </div>
      <ul class="stack" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px">
        <li class="panel panel__pad"><p class="label" style="color:var(--magenta)">Managing Director</p><p class="shout shout--sm" style="margin-top:4px">Mr. Jujjavarapu Venkata Rayudu</p></li>
        <li class="panel panel__pad"><p class="label" style="color:var(--magenta)">Director</p><p class="shout shout--sm" style="margin-top:4px">Mrs. Jujjavarapu Sridevi</p></li>
        <li class="panel panel__pad"><p class="label" style="color:var(--magenta)">Director</p><p class="shout shout--sm" style="margin-top:4px">Mrs. Jujjavarapu Mounika</p></li>
        <li class="panel panel__pad"><p class="label" style="color:var(--magenta)">Director</p><p class="shout shout--sm" style="margin-top:4px">Mr. Muttavarapu Siddharth Venkatram</p></li>
      </ul>
    </div>
  </section>

  <section class="section" id="brands">
    <div class="wrap">
      <div class="section-head">
        <p class="bubble">{i_tag} Partners</p>
        <h2 class="shout shout--lg">Trusted<br>to sell</h2>
      </div>
      <ul class="brands">
        <li>LG</li><li>Samsung</li><li>Sony</li><li>Whirlpool</li><li>Bosch</li>
        <li>Daikin</li><li>IFB</li><li>Haier</li><li>Lloyd</li><li>Blue Star</li>
        <li>Mitsubishi</li><li>Panasonic</li><li>Hitachi</li><li>Vivo</li><li>Oppo</li>
        <li>Voltas</li><li>Amaron</li><li>V-Guard</li><li>Luminous</li><li>AO Smith</li>
        <li>Livpure</li><li>Preethi</li><li>Butterfly</li><li>Crompton</li><li>TTK Prestige</li>
      </ul>
    </div>
  </section>

</main>
"""

# -------------------------------------------------------------- page: contact
CONTACT = """
<main id="main">

  <section class="hero" style="padding-block:clamp(24px,5vw,56px)">
    <div class="hero__glow" aria-hidden="true"></div>
    <div class="speedlines speedlines--dark" aria-hidden="true">
      <svg viewBox="0 0 100 100" preserveAspectRatio="none"><use href="#d-speed"></use></svg>
    </div>
    <div class="wrap" style="position:relative;display:grid;gap:14px">
      <p class="bubble" style="align-self:start">{i_call} Contact</p>
      <h1 class="shout shout--lg" style="color:#fff">Tell us what you need.<br><span class="ko">A person calls back.</span></h1>
      <p class="hero__lead">No ticket numbers, no “within 48 hours”. Leave your number and someone from your nearest showroom rings you between 10 am and 9 pm.</p>
      <p class="label" style="color:var(--gold)"><span data-shop-state>Open now</span> — <span data-shop-note>Open until 9 pm today.</span></p>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap" style="display:grid;gap:clamp(24px,4vw,48px)">
      <div style="display:grid;gap:clamp(24px,4vw,40px);grid-template-columns:minmax(0,1fr)">
        <form class="form panel panel__pad" data-contact-form novalidate>
          <span class="tab tab--cyan">Enquiry form</span>
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

          <div class="hero__cta">
            <button class="btn btn--magenta" type="submit">Send it</button>
            <a class="btn btn--cyan" href="https://wa.me/91{phone}?text={wa_text}" target="_blank" rel="noopener noreferrer">{i_whatsapp} WhatsApp instead</a>
          </div>
          <p class="muted" style="font-size:var(--t-xs)">This concept build has no server behind it — it checks your details, then tells you honestly that nothing was sent.</p>
        </form>

        <div style="display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(240px,1fr))">
          <div class="panel panel--gold panel__pad stack" style="gap:8px">
            <p class="shout shout--sm">{i_call} {pretty}</p>
            <p style="font-size:var(--t-sm)">Central helpline, 10 am – 9 pm. Installation, service, stock checks, anything.</p>
            <p style="display:flex;gap:8px;flex-wrap:wrap">
              <a class="btn btn--sm btn--ink" href="tel:+91{phone}">Call now</a>
              <button class="btn btn--sm btn--ghost" type="button" data-copy="{phone}">{i_copy} Copy</button>
            </p>
          </div>

          <div class="panel panel--cyan panel__pad stack" style="gap:8px">
            <p class="shout shout--sm">{i_wrench} Faulty product?</p>
            <p style="font-size:var(--t-sm)">Keep the bill number handy and call the helpline. We coordinate the brand's authorised service centre for you — you don't chase two companies.</p>
          </div>

          <div class="panel panel--mint panel__pad stack" style="gap:8px">
            <p class="shout shout--sm">{i_box} Dealers &amp; bulk orders</p>
            <p style="font-size:var(--t-sm)">Buying for a hostel, a function hall or a reseller business? Email <a style="text-decoration:underline" href="mailto:whynot.rayudu@gmail.com">whynot.rayudu@gmail.com</a> with quantities and we'll quote separately.</p>
          </div>

          <div class="panel panel__pad stack" style="gap:8px">
            <p class="shout shout--sm">{i_store} Registered office</p>
            <p class="muted" style="font-size:var(--t-sm)">RS No 24/1, Ground &amp; Cellar, Sri Sowdha Towers, Undrajavaram Road, Tanuku, Andhra Pradesh 534211</p>
            <p><a class="btn btn--sm btn--ghost" href="stores.html">{i_pin} All 25 showrooms</a></p>
          </div>
        </div>
      </div>
    </div>
  </section>

</main>
"""

# ----------------------------------------------------------------- page: 404
NOTFOUND = """
<main id="main">
  <section class="hero" style="padding-block:clamp(40px,10vw,120px)">
    <div class="hero__glow" aria-hidden="true"></div>
    <div class="speedlines speedlines--dark" aria-hidden="true">
      <svg viewBox="0 0 100 100" preserveAspectRatio="none"><use href="#d-speed"></use></svg>
    </div>
    <div class="wrap" style="position:relative;max-width:720px;display:grid;gap:16px">
      <svg class="doodle" style="width:120px;height:120px;color:var(--magenta);opacity:.9" viewBox="0 0 64 64" aria-hidden="true"><use href="#d-burst"></use></svg>
      <p class="bubble" style="align-self:start">{i_search} Error 404</p>
      <h1 class="shout shout--lg" style="color:#fff">This panel is<br><span class="ko">missing.</span></h1>
      <p class="hero__lead">Old link, moved page, or a typo in the address. Nothing is lost — the showrooms are all where you left them.</p>
      <div class="hero__cta">
        <a class="btn btn--gold" href="index.html">{i_store} Back home</a>
        <a class="btn btn--cyan" href="products.html">{i_cart} Catalogue</a>
        <a class="btn" href="stores.html">{i_pin} Showrooms</a>
      </div>
      <p class="label" style="color:rgba(255,255,255,.7)">Looking for one model? Call {pretty} and describe it — we'll say which branch has it.</p>
    </div>
  </section>
</main>
"""

if __name__ == "__main__":
    common = dict(
        i_sparkle=D("i-sparkle"), i_bolt=D("i-bolt"), i_star=D("i-star"), i_heart=D("i-heart"),
        i_cart=D("i-cart"), i_pin=D("i-pin"), i_call=D("i-call"), i_check=D("i-check"),
        i_people=D("i-people"), i_truck=D("i-truck"), i_wrench=D("i-wrench"), i_clock=D("i-clock"),
        i_search=D("i-search"), i_copy=D("i-copy"), i_store=D("i-store"), i_tag=D("i-tag"),
        i_shield=D("i-shield"), i_box=D("i-box"), i_droplet=D("i-droplet"), i_bulb=D("i-bulb"),
        i_speaker=D("i-speaker"), i_tv=D("i-tv"), i_fridge=D("i-fridge"), i_ac=D("i-ac"),
        i_washer=D("i-washer"), i_mixer=D("i-mixer"), i_phone=D("i-phone"), i_vacuum=D("i-vacuum"),
        i_whatsapp=D("i-whatsapp"), i_arrow_svg=D("d-arrow"),
        i_geyser=D("i-geyser"), i_grinder=D("i-grinder"), i_micro=D("i-micro"),
        i_sun=D("i-sun"), i_heart2=D("i-heart"),
        phone=HELPHONE, pretty=PRETTY,
        wa_text="Hi%20WHYNOT%2C%20I%20have%20a%20question%20about",
    )

    print("Building trial 03:")
    page("index.html",
         "WHYNOT — electronics & home appliances in the Godavari districts",
         "25 showrooms in 23 towns, every major brand, and a shop you can walk into. WHYNOT has been selling electronics and home appliances across the Godavari districts since 1994.",
         HOME.format(**common), current="c_home")

    page("products.html",
         "Catalogue — WHYNOT electronics & home appliances",
         "Browse televisions, refrigerators, air conditioners, washing machines and more. Add what you like to your list and get today's price from your nearest WHYNOT showroom.",
         PRODUCTS.format(**common), current="c_products")

    page("stores.html",
         "Showrooms — 25 WHYNOT locations across the Godavari districts",
         "Search all 25 WHYNOT showrooms by town, district or pincode. Every address opens straight into Google Maps.",
         STORES.format(**common), current="c_stores")

    page("about.html",
         "About WHYNOT — 32 years of electronics retail in Andhra Pradesh",
         "From an LML showroom in Tanuku in 1994 to 25 showrooms across the Godavari districts and Visakhapatnam: the story, the founder and the people.",
         ABOUT.format(**common), current="c_about")

    page("contact.html",
         "Contact WHYNOT — helpline, enquiries and service",
         "Call 88862 22448, send a WhatsApp, or leave your number and someone from your nearest WHYNOT showroom calls you back.",
         CONTACT.format(**common), current="c_contact",
         scripts_extra='<script src="assets/js/contact.js" defer></script>')

    page("404.html",
         "Page not found — WHYNOT",
         "That page is not here. Jump back to the catalogue or the showroom list.",
         NOTFOUND.format(**common))
    print("Done. Six pages written to trial-03-anime/")
