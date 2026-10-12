# WHYNOT redesign — the page shell shared by Trials 04, 05 and 06.
#
# Trials 01–03 each generated their own header, footer and phone bar. Those three
# files grew the same skeleton three times; from Trial 04 the skeleton lives here
# and each design supplies a "skin" — a small object with the five pieces that
# actually differ (sprite, header, footer, phone bar, background layers).
#
# The contract every skin keeps, because the JavaScript depends on it:
#   [data-drawer], [data-drawer-open], [data-drawer-close], [data-toast],
#   [data-year], [data-count], [data-shop-state], [data-list-count],
#   [data-reveal], and the icon symbol ids listed in icons.py.

import io
import os

HEAD = """<!DOCTYPE html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="{theme}">
<link rel="canonical" href="https://www.whynotindia.in/">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<link rel="icon" href="assets/img/logo-mark.svg" type="image/svg+xml">
<link rel="icon" href="assets/img/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
{preload}<link rel="stylesheet" href="assets/css/style.css">
<script>
  /* Marks the document as scripted, so reveal-on-scroll can never hide content
     from a visitor (or a crawler) that arrives without JavaScript. */
  document.documentElement.classList.add("js");
</script>
</head>
<body{body_class}>
<a class="skip-link" href="#main">Skip to content</a>
{background}{sprite}
"""

DRAWER = """
<div class="drawer" id="drawer" data-drawer data-open="false" aria-hidden="true">
  <div class="drawer__top">
    <span class="brand">
      {mark}
      <span class="brand__text"><span class="brand__name">WHYNOT</span></span>
    </span>
    <button class="icon-btn" type="button" data-drawer-close aria-label="Close menu">{icon_close}</button>
  </div>
  <nav class="drawer__nav" aria-label="Mobile">
    {links}
  </nav>
  <div class="drawer__foot">
    <a class="btn btn--brand btn--block" href="tel:+91{phone}">Call {pretty}</a>
    <p class="label drawer__note">Open 10 am – 9 pm · a person answers</p>
  </div>
</div>
"""

FOOTER = """
<footer class="site-footer">
  <div class="wrap">
    <div class="footer__grid">
      <div class="footer__col footer__col--brand">
        <span class="brand">
          {mark}
          <span class="brand__text">
            <span class="brand__name">WHYNOT</span>
            <span class="brand__tag">{tagline}</span>
          </span>
        </span>
        <p>WHYNOT Electronics Pvt Ltd. Electronics and home appliances across the Godavari districts and Visakhapatnam since 1994.</p>
        <p><a href="{app_url}" target="_blank" rel="noopener noreferrer">Get the WHYNOT app</a></p>
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
          <li>{address}</li>
          <li><a href="tel:+91{phone}">{pretty}</a></li>
          <li><a href="mailto:{email}">{email}</a></li>
        </ul>
      </div>
    </div>

    <div class="footer__bottom">
      <p>© <span data-year>2026</span> WHYNOT Electronics Pvt Ltd. Every address, phone number and brand name here belongs to the company and was taken from their public website.</p>
      <p>Concept redesign — <strong>{label}</strong> · not the live site · <a href="../index.html">all trials</a> · imagery is AI-generated stand-in art, not commissioned work.</p>
    </div>
  </div>
</footer>
"""

TOAST = """
<div class="toast" data-toast role="status" aria-live="polite" data-open="false"></div>
"""


def font_preloads(fonts):
    return "".join('<link rel="preload" href="assets/fonts/%s" as="font" type="font/woff2" crossorigin>\n' % f for f in fonts)


def build(root, skin, filename, body, current="", extra_scripts=(), title=None, desc=None,
          body_class="", background=""):
    """Write one page of a trial. `skin` supplies the five design-specific pieces."""
    from content import PAGES  # local import: keeps this module importable on its own

    t, d = PAGES[filename]
    t = title or t
    d = desc or d

    links = ""
    for href, label in (("index.html", "Home"), ("products.html", "Catalogue"),
                        ("stores.html", "Showrooms"), ("about.html", "About"), ("contact.html", "Contact")):
        mark = ' aria-current="page"' if href == current else ""
        links += '    <a href="%s"%s>%s</a>\n' % (href, mark, label)

    html = HEAD.format(title=t, desc=d, theme=skin.theme, preload=font_preloads(skin.fonts),
                       body_class=(' class="%s"' % body_class) if body_class else "",
                       background=background, sprite=skin.sprite())
    html += skin.header(current)
    html += DRAWER.format(mark=skin.mark(), icon_close=skin.icon("i-close"), links=links,
                          phone=skin.brand["helpline"], pretty=skin.brand["pretty"])
    html += '\n<main id="main">\n' + body + "\n</main>\n"
    html += skin.footer()
    html += skin.mobile_bar()
    html += TOAST
    html += '<script src="assets/js/main.js" defer></script>\n'
    html += '<script src="assets/js/products.js" defer></script>\n'
    for src in extra_scripts:
        html += '<script src="%s" defer></script>\n' % src
    html += "</body>\n</html>\n"

    path = os.path.join(root, filename)
    with io.open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("  %-14s %6d bytes" % (filename, len(html)))
    return html
