#!/usr/bin/env python3
"""
Builder for Trial 02 ("Crayon & Paper").

Usage:  python3 _tools/build-trial02.py

Writes the six pages of trial-02-illustrated/ from the templates below, so the
header, the footer, the phone action bar and the doodle sprite stay identical
across pages. Edit the page bodies here and re-run — or edit the HTML directly
and stop using this script (in which case delete it, or the next run will
overwrite your edits).
"""

import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from doodles import sprite  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "trial-02-illustrated")

HELPLINE_PRETTY = "88862 22448"
HELPLINE = "8886222448"

D = lambda i, c="": '<svg class="doodle %s" aria-hidden="true"><use href="#%s"></use></svg>' % (c, i)

HEAD = """<!DOCTYPE html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#fffcf3">
<link rel="canonical" href="https://www.whynotindia.in/">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<link rel="icon" href="assets/img/logo-mark.svg" type="image/svg+xml">
<link rel="icon" href="assets/img/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preload" href="assets/fonts/shantell-sans-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/nunito-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
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
      <a class="btn btn--sm btn--brand header-cta" href="tel:+91{phone}">Call {pretty}</a>
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
    <a class="btn btn--brand btn--block" href="tel:+91{phone}">Call {pretty}</a>
    <p class="hand">Open 10 am – 9 pm. A person answers.</p>
  </div>
</div>
"""

FOOTER = """
<footer class="site-footer">
  <div class="wrap">
    <div class="footer__grid">
      <div class="footer__col">
        <span class="brand">
          <span class="brand__mark" aria-hidden="true">W</span>
          <span class="brand__text">
            <span class="brand__name">WHYNOT</span>
            <span class="brand__tag">We drive the change</span>
          </span>
        </span>
        <p class="prose" style="font-size:var(--t-sm)">WHYNOT Electronics Pvt Ltd. Electronics and home appliances across the Godavari districts and Visakhapatnam since 1994.</p>
        <p style="font-size:var(--t-sm)"><a class="link" href="https://play.google.com/store/apps/details?id=in.absolin.whynotcust" target="_blank" rel="noopener noreferrer">Get the WHYNOT app</a></p>
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
      <p>Concept redesign — <strong>Trial 02 “Crayon &amp; Paper”</strong> · not the live site · <a href="../index.html">all trials</a></p>
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
        html = html.replace("<!--ART_i-menu-->", D("i-menu")).replace("<!--ART_i-close-->", D("i-close"))
        html = html.replace("<!--ART_i-cart-->", D("i-cart")).replace("<!--ART_i-call-->", D("i-call"))
        html = html.replace("<!--ART_i-pin-->", D("i-pin")).replace("<!--ART_i-whatsapp-->", D("i-whatsapp"))
        return html

    html = HEAD.format(title=title, desc=desc, extra=sprite())
    html += art(HEADER.format(phone=HELPLINE, pretty=HELPLINE_PRETTY, **marks))
    html += art(body)
    html += art(FOOTER.format(phone=HELPLINE, pretty=HELPLINE_PRETTY))
    html += SCRIPTS.format(extra=scripts_extra)

    with io.open(os.path.join(ROOT, filename), "w", encoding="utf-8") as f:
        f.write(html + "\n</body>\n</html>\n")
    print("  wrote %-14s %6d bytes" % (filename, len(html)))


# ----------------------------------------------------------------- page: home
HOME = """
<main id="main">

  <section class="hero">
    <div class="wrap hero__inner">
      <div class="hero__copy">
        <p class="kicker kicker--coral">{i_sparkle} Godavari districts · since 1994</p>
        <h1 class="h-hero">Big brands.<br><span class="mark mark--marker">Small towns.</span><br>Why not?</h1>
        <p class="lead">Twenty-five WHYNOT showrooms in 23 towns, every major brand, and a phone number that still works five years after you buy. That has been the whole idea since 1994.</p>
        <div class="hero__cta">
          <a class="btn btn--brand" href="products.html">{i_cart} See what we sell</a>
          <a class="btn btn--marker" href="stores.html">{i_pin} Find my showroom</a>
        </div>
        <div class="hero__points">
          <span class="sticker sticker--lime">{i_check} 32 years</span>
          <span class="sticker sticker--sky">{i_people} 300 people</span>
          <span class="sticker sticker--marker">{i_truck} Delivery &amp; install</span>
        </div>
      </div>

      <div class="hero__art">
        <span class="doodle-float doodle-float--1">{i_bolt_big}</span>
        <span class="doodle-float doodle-float--2">{i_star_big}</span>
        <svg class="doodle doodle--scene" viewBox="0 0 320 190" aria-label="A hand-drawn picture of a WHYNOT showroom with a television, a fridge and a washing machine in the window.">
          <use href="#i-scene"></use>
        </svg>
        <p class="hand" style="text-align:center">Walk in. Poke the buttons. Ask the awkward questions.</p>
      </div>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap stats">
      <div class="stat"><p class="stat__value"><span data-count="2.5">2.5</span>M</p><p class="stat__label">Customers served</p></div>
      <div class="stat"><p class="stat__value"><span data-count="1">1</span>M</p><p class="stat__label">Products sold</p></div>
      <div class="stat"><p class="stat__value"><span data-count="25">25</span></p><p class="stat__label">Showrooms, 23 towns</p></div>
      <div class="stat"><p class="stat__value"><span data-count="32">32</span></p><p class="stat__label">Years since 1994</p></div>
    </div>
  </section>

  <section class="section" id="categories">
    <div class="wrap">
      <div class="section-head">
        <p class="kicker kicker--blue">{i_sun} Shop by category</p>
        <h2 class="h2">Ten aisles, one roof</h2>
        <p>Tap a tile to see the sort of things we stock. Prices move with the season, so every card says “ask today's price” — and we answer with the real number.</p>
      </div>

      <div class="tiles">
        <a class="tile tile--sky" href="products.html?cat=tv">{i_tv}<span class="tile__name">Televisions</span><span class="tile__meta">QLED, 4K, smart</span></a>
        <a class="tile tile--lime" href="products.html?cat=fridge">{i_fridge}<span class="tile__name">Refrigerators</span><span class="tile__meta">Single &amp; double door</span></a>
        <a class="tile tile--sky" href="products.html?cat=ac">{i_ac}<span class="tile__name">Air conditioners</span><span class="tile__meta">Split, inverter</span></a>
        <a class="tile tile--teal" href="products.html?cat=washer">{i_washer}<span class="tile__name">Washing machines</span><span class="tile__meta">Semi &amp; fully automatic</span></a>
        <a class="tile tile--mango" href="products.html?cat=kitchen">{i_mixer}<span class="tile__name">Kitchen</span><span class="tile__meta">Mixers, grinders, ovens</span></a>
        <a class="tile tile--sky" href="products.html?cat=water">{i_droplet}<span class="tile__name">Water &amp; geysers</span><span class="tile__meta">Purifiers, heaters</span></a>
        <a class="tile tile--marker" href="products.html?cat=lighting">{i_bulb}<span class="tile__name">Lighting</span><span class="tile__meta">LED bulbs, strips</span></a>
        <a class="tile tile--violet" href="products.html?cat=audio">{i_speaker}<span class="tile__name">Audio</span><span class="tile__meta">Speakers, soundbars</span></a>
        <a class="tile tile--pink" href="products.html?cat=mobile">{i_phone}<span class="tile__name">Mobiles</span><span class="tile__meta">5G, budget to flagship</span></a>
        <a class="tile tile--lime" href="products.html?cat=cleaning">{i_vacuum}<span class="tile__name">Cleaning</span><span class="tile__meta">Vacuum, steam mops</span></a>
      </div>
    </div>
  </section>

  <section class="section" id="popular">
    <div class="wrap">
      <div class="section-head">
        <p class="kicker kicker--coral">{i_heart} Popular right now</p>
        <h2 class="h2">What people actually ask for</h2>
        <p>The four a month of “what's good in this budget?” conversations usually end on.</p>
      </div>

      <div class="products" data-featured></div>

      <p style="margin-top:22px">
        <a class="btn btn--brand" href="products.html">Open the full catalogue {i_arrow}</a>
      </p>
      <p class="hand" style="margin-top:12px">Sample catalogue for the design — real stock and today's prices come from your branch.</p>
    </div>
  </section>

  <section class="section" id="why-not">
    <div class="wrap">
      <div class="section-head">
        <p class="kicker kicker--blue">{i_sparkle} The name is the question</p>
        <h2 class="h2">Why not…</h2>
        <p>Four questions WHYNOT has answered the same way since an LML showroom in Tanuku in 1994.</p>
      </div>

      <div class="qs">
        <div class="q">
          <span class="q__no">why not…</span>
          <p class="q__q">…put it in your town?</p>
          <p>Twenty-five showrooms in 23 towns, because “drive two hours to the city” is not service. Most of them opened before anyone else thought the town was big enough.</p>
        </div>
        <div class="q">
          <span class="q__no">why not…</span>
          <p class="q__q">…pick up the phone after the sale?</p>
          <p>Installation, service and follow-up come from the branch you bought at, not from a call centre that has never seen your street.</p>
        </div>
        <div class="q">
          <span class="q__no">why not…</span>
          <p class="q__q">…give the honest price first time?</p>
          <p>Ask us today's price and you get the number we can actually sell at. EMI and exchange details upfront, no theatre.</p>
        </div>
        <div class="q">
          <span class="q__no">why not…</span>
          <p class="q__q">…still be here in ten years?</p>
          <p>Thirty-two years, two generations of the same family, 300 people from the towns they serve. Your neighbour is the shop.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap grid grid--2">
      <div class="note note--sky">
        <p class="kicker kicker--blue">{i_wrench} Service</p>
        <p class="note__title">The part nobody photographs</p>
        <p class="prose" style="font-size:var(--t-sm)">Electronics are judged in year three, when the AC stops cooling in May. That is the year WHYNOT is built for: 300 people, genuine parts through each brand's own service network, and one number for all of it.</p>
        <p style="margin-top:12px"><a class="btn btn--sm" href="tel:+91{phone}">{i_call} Call {pretty}</a></p>
      </div>
      <div class="note note--lime">
        <p class="kicker kicker--coral">{i_truck} Delivery</p>
        <p class="note__title">Fridge upstairs? We'll take it upstairs</p>
        <p class="prose" style="font-size:var(--t-sm)">Delivery, installation and the demo are arranged at the counter, and the bill includes what it includes — we tell you the total before you pay, not after.</p>
        <p style="margin-top:12px"><a class="btn btn--sm btn--brand" href="stores.html">{i_pin} Nearest showroom</a></p>
      </div>
    </div>
  </section>

  <section class="section section--tight" id="brands">
    <div class="wrap">
      <div class="section-head">
        <p class="kicker kicker--blue">{i_star} Brands</p>
        <h2 class="h2">Everything you'd expect</h2>
      </div>
      <ul class="brands">
        <li>LG</li><li>Samsung</li><li>Sony</li><li>Whirlpool</li><li>Bosch</li>
        <li>Daikin</li><li>IFB</li><li>Haier</li><li>Lloyd</li><li>Blue Star</li>
        <li>Mitsubishi</li><li>Panasonic</li><li>Hitachi</li><li>Vivo</li><li>Oppo</li>
        <li>Voltas</li><li>Amaron</li><li>V-Guard</li><li>Luminous</li><li>AO Smith</li>
      </ul>
    </div>
  </section>

  <section class="section" id="showrooms">
    <div class="wrap">
      <div class="section-head">
        <p class="kicker kicker--coral">{i_pin} Showrooms</p>
        <h2 class="h2">25 shops, 23 towns, 1 number</h2>
        <p>Tanuku · Tadepalligudem · Rajahmundry · Bhimavaram · Eluru · Kakinada · Palakollu · Narasapuram · Amalapuram · Mandapeta · Anakapalle · and more.</p>
      </div>
      <div class="hero__cta">
        <a class="btn btn--brand" href="stores.html">{i_pin} Search all 25</a>
        <a class="btn btn--marker" href="tel:+91{phone}">{i_call} {pretty}</a>
      </div>
    </div>
  </section>

  <section class="section" id="reviews">
    <div class="wrap">
      <div class="section-head">
        <p class="kicker kicker--blue">{i_heart} In their words</p>
        <h2 class="h2">People who kept coming back</h2>
      </div>
      <div class="grid grid--3">
        <div class="note note--marker">
          <p class="hand" style="font-size:1.75rem">“I've been a customer for five years. Their pricing and convenience work for me — that's just one of the reasons I use them.”</p>
          <p class="card__meta" style="margin-top:8px">WHYNOT customer</p>
        </div>
        <div class="note note--pink">
          <p class="hand" style="font-size:1.75rem">“The best place for electronics and home appliances in both Godavari districts.”</p>
          <p class="card__meta" style="margin-top:8px">WHYNOT customer</p>
        </div>
        <div class="note note--sky">
          <p class="hand" style="font-size:1.75rem">“It is a store with everything I need.”</p>
          <p class="card__meta" style="margin-top:8px">WHYNOT customer</p>
        </div>
      </div>
      <p class="hand" style="margin-top:14px">Reviews shown as they were written. Named, dated reviews with permission would be even better — see the notes in the repo.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap note note--lime" style="text-align:center">
      <p class="kicker kicker--coral">{i_clock} Open 10 am – 9 pm · <span data-shop-state>Open now</span></p>
      <h2 class="h2" style="margin:8px 0 10px">Come and see it in person</h2>
      <p class="lead" style="margin-inline:auto">Pick the things you like in the catalogue, send the list, and a person from your nearest branch calls you with today's price.</p>
      <p style="margin-top:16px">
        <a class="btn btn--brand" href="products.html">{i_cart} Start a list</a>
        <a class="btn btn--marker" href="contact.html">{i_call} Ask a question</a>
      </p>
    </div>
  </section>

</main>
"""

# ------------------------------------------------------------- page: catalogue
PRODUCTS = """
<main id="main">

  <section class="section section--tight">
    <div class="wrap">
      <p class="kicker kicker--coral">{i_cart} Catalogue</p>
      <h1 class="h1" style="margin:8px 0 12px">Pick what you like. We'll price it.</h1>
      <p class="lead">Add anything you're curious about to <strong>my list</strong>, send it in one tap, and someone from your nearest branch replies with today's price and stock. No card details, no checkout maze.</p>
      <p style="margin-top:14px"><span class="sticker sticker--sky">{i_sparkle} Sample catalogue — real stock comes from your branch</span></p>
    </div>
  </section>

  <section class="section section--tight" id="catalogue">
    <div class="wrap">
      <div class="toolbar">
        <div class="toolbar__row">
          <div class="search">
            <label class="visually-hidden" for="q">Search the catalogue</label>
            {i_search}
            <input id="q" type="search" placeholder="Search: TV, fridge, 1.5 ton…" autocomplete="off" data-product-search>
          </div>
        </div>
        <div>
          <label class="visually-hidden" for="town">Show what is stocked in a town</label>
          <select class="select" id="town" data-town-select>
            <option value="all">All towns</option>
          </select>
        </div>
      </div>

      <div class="chips" role="group" aria-label="Filter by category" data-cat-chips></div>

      <p class="result-count" data-result-count aria-live="polite">Loading…</p>

      <div class="chips" role="group" aria-label="Popular searches" style="margin-bottom:6px">
        <a class="chip" href="products.html?cat=water">{i_geyser} Geysers</a>
        <a class="chip" href="products.html?cat=kitchen">{i_grinder} Wet grinders</a>
        <a class="chip" href="products.html?cat=kitchen">{i_micro} Microwave ovens</a>
        <a class="chip" href="products.html?cat=tv">{i_tv} 55-inch TVs</a>
      </div>

      <div class="products" data-products>
        <p class="muted">Loading the catalogue…</p>
      </div>
    </div>
  </section>

  <section class="section" id="my-list">
    <div class="wrap">
      <div class="section-head">
        <p class="kicker kicker--blue">{i_cart} My list</p>
        <h2 class="h2">Your list, <span data-list-label>0 items</span></h2>
        <p>It stays on this phone until you send it. Send it on WhatsApp, call, or email — whichever is easiest for you.</p>
      </div>
      <div data-list-panel></div>
    </div>
  </section>

  <section class="section" id="how">
    <div class="wrap">
      <div class="section-head">
        <p class="kicker kicker--coral">{i_check} How buying works here</p>
        <h2 class="h2">Three steps, no checkout maze</h2>
      </div>
      <div class="grid grid--3">
        <div class="note note--marker">
          <p class="note__title">1. Add what you like</p>
          <p class="prose" style="font-size:var(--t-sm)">Build a list while you browse. Nothing is charged and no account is needed.</p>
        </div>
        <div class="note note--sky">
          <p class="note__title">2. Send it to us</p>
          <p class="prose" style="font-size:var(--t-sm)">One tap opens WhatsApp or dials the helpline with your list written out.</p>
        </div>
        <div class="note note--lime">
          <p class="note__title">3. We call back with the price</p>
          <p class="prose" style="font-size:var(--t-sm)">Today's price, what's in stock at which branch, EMI if you want it, and a delivery date.</p>
        </div>
      </div>

      <div class="grid grid--2" style="margin-top:26px">
        <div class="note">
          <p class="note__title">{i_shield} Warranty &amp; service</p>
          <p class="prose" style="font-size:var(--t-sm)">Brand warranty runs through each manufacturer's authorised service network, and WHYNOT coordinates it for you.</p>
        </div>
        <div class="note">
          <p class="note__title">{i_tag} EMI &amp; exchange</p>
          <p class="prose" style="font-size:var(--t-sm)">Card and Bajaj-style EMI options are available at the counter on most large appliances. Old product exchange value is quoted before you buy.</p>
        </div>
        <div class="note">
          <p class="note__title">{i_truck} Delivery &amp; installation</p>
          <p class="prose" style="font-size:var(--t-sm)">Fixed at the counter: what it costs, when it arrives, and who installs it. No surprises on the bill.</p>
        </div>
        <div class="note">
          <p class="note__title">{i_people} Ask a human</p>
          <p class="prose" style="font-size:var(--t-sm)">Not sure between two models? Call <a class="link" href="tel:+91{phone}">{pretty}</a> and describe the room. We do this all day.</p>
        </div>
      </div>
    </div>
  </section>

</main>
"""

# --------------------------------------------------------------- page: stores
STORES = """
<main id="main">

  <section class="section section--tight">
    <div class="wrap">
      <p class="kicker kicker--coral">{i_pin} Showrooms</p>
      <h1 class="h1" style="margin:8px 0 12px">25 showrooms. One is probably 20 minutes away.</h1>
      <p class="lead">Search by town, district or pincode. Every address below opens straight into Google Maps on your phone.</p>
      <p style="margin-top:14px">
        <a class="btn btn--brand" href="tel:+91{phone}">{i_call} {pretty}</a>
        <button class="btn btn--plain" type="button" data-copy="{phone}">{i_copy} Copy number</button>
      </p>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap">
      <div class="toolbar">
        <div class="toolbar__row">
          <div class="search">
            <label class="visually-hidden" for="store-search">Search showrooms</label>
            {i_search}
            <input id="store-search" type="search" placeholder="Town, district or pincode…" autocomplete="off" data-store-search>
          </div>
        </div>
        <div class="chips" role="group" aria-label="Filter by district">
          <button class="chip" type="button" data-district="all" aria-pressed="true">All</button>
          <button class="chip" type="button" data-district="West Godavari" aria-pressed="false">West Godavari</button>
          <button class="chip" type="button" data-district="East Godavari" aria-pressed="false">East Godavari</button>
          <button class="chip" type="button" data-district="Visakhapatnam" aria-pressed="false">Visakhapatnam</button>
        </div>
      </div>

      <p class="result-count" data-store-count aria-live="polite">25 showrooms</p>

      <div class="stores" data-store-list style="margin-top:14px">
        <p class="muted">Loading the showroom list…</p>
      </div>

      <div class="empty" data-store-empty hidden>
        <p class="h3">No showroom matches that</p>
        <p class="muted">Try the town name, a pincode, or the district — or just call <a class="link" href="tel:+91{phone}">{pretty}</a>.</p>
        <button class="btn btn--sm" type="button" data-store-clear>Clear filters</button>
      </div>

      <noscript>
        <div class="status" style="margin-top:20px">
          <strong>This list is drawn by JavaScript.</strong>
          <span>In a production build it renders on the server instead. Meanwhile the full list is on
          <a class="link" href="https://www.whynotindia.in/stores" target="_blank" rel="noopener noreferrer">whynotindia.in/stores</a>, or call <a class="link" href="tel:+91{phone}">{pretty}</a>.</span>
        </div>
      </noscript>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <p class="kicker kicker--blue">{i_clock} Good to know</p>
        <h2 class="h2">Before you drive over</h2>
      </div>
      <div class="grid grid--2">
        <div class="note note--marker">
          <p class="note__title">Hours</p>
          <p class="prose" style="font-size:var(--t-sm)">Showrooms are open <strong>10 am – 9 pm</strong>. Festival weeks can shift that by an hour, so a quick call saves a trip. Right now: <strong data-shop-state>Open now</strong>.</p>
        </div>
        <div class="note note--sky">
          <p class="note__title">Stock is local</p>
          <p class="prose" style="font-size:var(--t-sm)">Each branch carries its own stock. Tell us the model and your town and we'll confirm which showroom has it on the floor.</p>
        </div>
        <div class="note note--lime">
          <p class="note__title">Brand stores in Tanuku</p>
          <p class="prose" style="font-size:var(--t-sm)">The flagship building in Tanuku also houses an <strong>LG Best Shop</strong> and a <strong>Samsung Smart Plaza</strong>.</p>
        </div>
        <div class="note note--pink">
          <p class="note__title">Already bought from us?</p>
          <p class="prose" style="font-size:var(--t-sm)">Installation, service or a fault — call <a class="link" href="tel:+91{phone}">{pretty}</a> or walk into your branch. You don't need this website for that.</p>
        </div>
      </div>
    </div>
  </section>

</main>
"""

# ---------------------------------------------------------------- page: about
ABOUT = """
<main id="main">

  <section class="section section--tight">
    <div class="wrap">
      <p class="kicker kicker--coral">{i_store} About us</p>
      <h1 class="h1" style="margin:8px 0 12px">Started with one shop and a question.</h1>
      <p class="lead">On 27 February 1994 Mr. Jujjavarapu Venkata Rayudu opened an LML showroom in Tanuku and called it <strong>Whynot</strong>. Thirty-two years later it is 25 showrooms and 300 people — still run by the same family.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <p class="kicker kicker--blue">{i_clock} The story</p>
        <h2 class="h2">Sticky notes from the last 32 years</h2>
      </div>

      <div class="grid grid--2">
        <div class="note note--marker" style="transform:rotate(-1deg)">
          <span class="tape">1994</span>
          <p class="note__title" style="margin-top:10px">An LML showroom in Tanuku</p>
          <p class="prose" style="font-size:var(--t-sm)">A commerce graduate and junior lawyer from Kanuru village starts his first venture, at a time when good products rarely reached semi-urban Andhra Pradesh.</p>
        </div>
        <div class="note note--sky" style="transform:rotate(1deg)">
          <span class="tape">1996</span>
          <p class="note__title" style="margin-top:10px">A Bajaj dealership</p>
          <p class="prose" style="font-size:var(--t-sm)">Two-wheelers at scale — and the reputation for after-sales service the electronics business still runs on.</p>
        </div>
        <div class="note note--lime" style="transform:rotate(-.6deg)">
          <span class="tape">2006</span>
          <p class="note__title" style="margin-top:10px">Automobiles to electronics</p>
          <p class="prose" style="font-size:var(--t-sm)">The shift to consumer electronics and home appliances, and expansion across the East and West Godavari districts into Visakhapatnam district.</p>
        </div>
        <div class="note note--pink" style="transform:rotate(.8deg)">
          <span class="tape">2025</span>
          <p class="note__title" style="margin-top:10px">WHYNOT Electronics Pvt Ltd</p>
          <p class="prose" style="font-size:var(--t-sm)">From 27 February 2025 the company incorporates formally — structured governance, stronger systems, deeper brand partnerships, a digital-first plan.</p>
        </div>
        <div class="note note--marker" style="transform:rotate(.7deg)">
          <span class="tape">Today</span>
          <p class="note__title" style="margin-top:10px">25 showrooms, 300 people</p>
          <p class="prose" style="font-size:var(--t-sm)">A shop in nearly every town of the two Godavari districts, more than 2.5 million customers served, and the family still at the desk.</p>
        </div>
        <div class="note note--sky" style="transform:rotate(-.9deg)">
          <span class="tape">Next</span>
          <p class="note__title" style="margin-top:10px">Same shop, online too</p>
          <p class="prose" style="font-size:var(--t-sm)">The stated ambition is 50+ branches and an omnichannel experience — same prices, same people, same service, wherever the customer starts.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap grid grid--2">
      <div class="note note--lime">
        <p class="kicker kicker--coral">{i_people} The founder</p>
        <p class="note__title">“Nothing is impossible.”</p>
        <p class="prose" style="font-size:var(--t-sm)">Mr. Jujjavarapu Venkata Rayudu grew up in an agricultural family in Kanuru, West Godavari. He studied commerce, then law, and started out as a junior lawyer before business pulled him in.</p>
        <p class="prose" style="font-size:var(--t-sm)">His instinct was to go where bigger retailers did not: the tier-3 and tier-4 towns. That decision built the network — and the barrier around it.</p>
      </div>
      <div class="note note--sky">
        <p class="kicker kicker--blue">{i_check} Leadership today</p>
        <ul class="prose" style="font-size:var(--t-sm);display:grid;gap:8px">
          <li><strong>Mr. Jujjavarapu Venkata Rayudu</strong> — Managing Director</li>
          <li><strong>Mrs. Jujjavarapu Sridevi</strong> — Director</li>
          <li><strong>Mrs. Jujjavarapu Mounika</strong> — Director</li>
          <li><strong>Mr. Muttavarapu Siddharth Venkatram</strong> — Director</li>
        </ul>
        <p class="hand" style="margin-top:12px">Customer is the king. Their satisfaction is the priority — the company's own words, 32 years on.</p>
      </div>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap">
      <div class="section-head">
        <p class="kicker kicker--blue">{i_star} Partners</p>
        <h2 class="h2">Brands we are trusted to sell</h2>
      </div>
      <ul class="brands">
        <li>LG</li><li>Samsung</li><li>Sony</li><li>Whirlpool</li><li>Bosch</li>
        <li>Daikin</li><li>IFB</li><li>Haier</li><li>Lloyd</li><li>Blue Star</li>
        <li>Mitsubishi</li><li>Panasonic</li><li>Hitachi</li><li>Vivo</li><li>Oppo</li>
        <li>Voltas</li><li>Amaron</li><li>V-Guard</li><li>Luminous</li><li>AO Smith</li>
        <li>Livpure</li><li>Preethi</li><li>Butterfly</li><li>Crompton</li><li>TTK Prestige</li>
      </ul>
      <p class="hand" style="margin-top:14px">Names only — no third-party logos were lifted for this concept.</p>
    </div>
  </section>

</main>
"""

# -------------------------------------------------------------- page: contact
CONTACT = """
<main id="main">

  <section class="section section--tight">
    <div class="wrap">
      <p class="kicker kicker--coral">{i_call} Contact</p>
      <h1 class="h1" style="margin:8px 0 12px">Tell us what you need. A person calls you back.</h1>
      <p class="lead">No ticket numbers, no “within 48 hours”. Leave your number and someone from your nearest showroom rings you between 10 am and 9 pm.</p>
      <p style="margin-top:14px"><strong data-shop-state>Open now</strong> — <span class="muted" data-shop-note>Open until 9 pm today.</span></p>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap grid grid--2">
      <form class="form" data-contact-form novalidate>
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
          <button class="btn btn--brand" type="submit">Send it</button>
          <a class="btn btn--teal" href="https://wa.me/91{phone}?text={wa_text}" target="_blank" rel="noopener noreferrer">{i_whatsapp} WhatsApp instead</a>
        </div>
        <p class="hand">This concept build has no server behind it — it checks your details, then tells you honestly that nothing was sent.</p>
      </form>

      <aside class="stack">
        <div class="note note--marker">
          <p class="note__title">{i_call} {pretty}</p>
          <p class="prose" style="font-size:var(--t-sm)">Central helpline, 10 am – 9 pm. Installation, service, stock checks, anything.</p>
          <p style="margin-top:10px">
            <a class="btn btn--sm btn--brand" href="tel:+91{phone}">Call now</a>
            <button class="btn btn--sm btn--plain" type="button" data-copy="{phone}">{i_copy} Copy</button>
          </p>
        </div>
        <div class="note note--sky">
          <p class="note__title">{i_wrench} Faulty product?</p>
          <p class="prose" style="font-size:var(--t-sm)">Keep the bill number handy and call the helpline. We coordinate the brand's authorised service centre for you — you don't have to chase two companies.</p>
        </div>
        <div class="note note--pink">
          <p class="note__title">{i_box} Dealers &amp; bulk orders</p>
          <p class="prose" style="font-size:var(--t-sm)">Buying for a hostel, a function hall or a reseller business? Email <a class="link" href="mailto:whynot.rayudu@gmail.com">whynot.rayudu@gmail.com</a> with quantities and we'll quote separately.</p>
        </div>
        <div class="note note--lime">
          <p class="note__title">{i_store} Registered office</p>
          <p class="prose" style="font-size:var(--t-sm)">RS No 24/1, Ground &amp; Cellar, Sri Sowdha Towers, Undrajavaram Road, Tanuku, Andhra Pradesh 534211</p>
          <p style="margin-top:10px"><a class="btn btn--sm" href="stores.html">{i_pin} All 25 showrooms</a></p>
        </div>
      </aside>
    </div>
  </section>

</main>
"""

# ----------------------------------------------------------------- page: 404
NOTFOUND = """
<main id="main">
  <section class="section section--tight" style="padding-block:clamp(48px,12vw,120px)">
    <div class="wrap" style="max-width:640px">
      <p class="kicker kicker--coral">{i_search} 404</p>
      <h1 class="h1" style="margin:10px 0 12px">This page wandered off.</h1>
      <p class="lead">Old link, moved page, or a typo in the address. Nothing is lost — the showrooms are all where you left them.</p>
      <p style="margin-top:18px">
        <a class="btn btn--brand" href="index.html">{i_store} Back home</a>
        <a class="btn btn--marker" href="products.html">{i_cart} Catalogue</a>
        <a class="btn btn--plain" href="stores.html">{i_pin} Showrooms</a>
      </p>
      <p class="hand" style="margin-top:20px">Looking for one model in particular? Call {pretty} and describe it — we'll tell you which branch has it.</p>
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
        i_shield=D("i-shield"), i_droplet=D("i-droplet"), i_bulb=D("i-bulb"), i_speaker=D("i-speaker"),
        i_tv=D("i-tv"), i_fridge=D("i-fridge"), i_ac=D("i-ac"), i_washer=D("i-washer"),
        i_mixer=D("i-mixer"), i_phone=D("i-phone"), i_vacuum=D("i-vacuum"), i_sun=D("i-sun"),
        i_box=D("i-box"), i_geyser=D("i-geyser"), i_grinder=D("i-grinder"), i_micro=D("i-micro"),
        i_arrow=D("i-arrow"), i_whatsapp=D("i-whatsapp"),
        i_bolt_big=D("i-bolt"), i_star_big=D("i-star"),
        phone=HELPLINE, pretty=HELPLINE_PRETTY,
        wa_text="Hi%20WHYNOT%2C%20I%20have%20a%20question%20about",
    )

    print("Building trial 02:")
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
    print("Done. Six pages written to trial-02-illustrated/")
