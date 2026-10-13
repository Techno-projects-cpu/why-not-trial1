#!/usr/bin/env python3
"""
Trial 07's JavaScript.

Usage:  python3 _tools/port-js07.py

The catalogue logic — the shortlist in localStorage, the filters, the enquiry
text, the form validation — is the same behaviour every trial has, and it is
already written and covered by the test suite. So instead of hand-copying three
hundred lines, this takes Trial 04's scripts (the last trial built on the shared
markup contract) and re-renders their markup for Trial 07's form:

  * the catalogue becomes table rows (div.row) rather than cards;
  * the shortlist panel becomes a working side panel;
  * the showrooms become a directory grouped by district;
  * the store key, the tile markup and the icon class change with the design.

Everything it cannot map it prints, so nothing disappears quietly.
"""

import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
SRC = os.path.join(REPO, "trial-04-brutalist", "assets", "js")
OUT = os.path.join(REPO, "trial-07-slate", "assets", "js")

FILES = ("main.js", "products.js", "stores.js", "contact.js")


def read(name):
    return io.open(os.path.join(SRC, name), encoding="utf-8").read()


def write(name, text):
    io.open(os.path.join(OUT, name), "w", encoding="utf-8").write(text)
    print("  wrote %-12s %5.1f KB" % (name, len(text) / 1024))


def sub_either(text, olds, new, label):
    """Trial 04's source may be plain or already localised, so try both."""
    if new in text:
        return text
    for old in olds:
        if old in text:
            return text.replace(old, new, 1)
    print("  ! could not map: %s" % label)
    return text


def sub_once(text, old, new, label):
    if old not in text:
        print("  ! could not map: %s" % label)
        return text
    return text.replace(old, new, 1)


def header(text, title, note):
    """Replace the file's header comment with Trial 07's own."""
    end = text.index("*/") + 2
    return "/* WHYNOT — Trial 07 · Slate & Rail · %s.\n   %s\n   --------------------------------------------------------------------------- */" % (title, note) + text[end:]


def main():
    # ------------------------------------------------------------- products.js
    p = read("products.js")
    p = header(p, "catalogue + \"my list\"",
               "The same catalogue as every other trial — same data, same behaviour, "
               "same shortlist — laid out as table rows you scan down, because that is\n   the opposite of the card grid the other six directions use.")
    p = sub_once(p, 'var STORE_KEY = "whynot-list-t4";', 'var STORE_KEY = "whynot-list-t7";', "store key")

    # icons: this design's class is .icon, not a doodle
    p = sub_once(p,
                 """  function doodle(art, cls) {
    return '<svg class="doodle ' + (cls || "") + '" aria-hidden="true"><use href="#' + art + '"></use></svg>';
  }""",
                 """  function icon(art) {
    return '<svg class="icon" aria-hidden="true"><use href="#' + art + '"></use></svg>';
  }""",
                 "icon helper")
    p = p.replace("doodle(", "icon(")
    p = p.replace('icon("i-cart", "icon--xl")', 'icon("i-cart")')
    p = p.replace('icon("i-search", "icon--xl")', 'icon("i-search")')

    # the row renderer
    start = p.index("  function cardHtml(p) {")
    end = p.index("  function paintAddButtons() {")
    p = p[:start] + '''  /* One line item. Everything the card in the other trials shows — category,
     specification, which branches have it, the price conversation — as a row in
     a table, so seventeen of them can be read at a glance. */
  function rowHtml(p) {
    var c = cat(p.cat);
    var added = inList(p.id);
    return '' +
      '<div class="row" data-product="' + p.id + '">' +
        '<div>' +
          '<div class="row__name">' + esc(p.title) +
            (p.badge ? ' <span class="badge">' + esc(p.badge) + "</span>" : "") + "</div>" +
          '<div class="row__where">' + esc(p.specs.join(" \\u00b7 ")) + "</div>" +
        "</div>" +
        '<div class="row__cat">' + icon(c.art) + esc(c.label) + "</div>" +
        '<div class="row__specs">' + esc(p.specs.join(" \\u00b7 ")) + "</div>" +
        '<div class="row__where">' + esc(p.towns.join(", ")) + "</div>" +
        '<div class="row__act">' +
          '<button class="btn btn--sm ' + (added ? "btn--done" : "btn--primary") + '" type="button" ' +
            'data-add="' + p.id + '" aria-pressed="' + (added ? "true" : "false") + '">' +
            (added ? T("added", "In my list") : T("add", "Add to list")) + "</button>" +
          '<a class="btn btn--sm btn--ghost" href="contact.html?about=' + encodeURIComponent(p.title) + '">' +
            T("askAbout", "Ask about this") + "</a>" +
        "</div>" +
      "</div>";
  }

''' + p[end:]

    # the grid renderer becomes a table body
    start = p.index("  function renderGrid() {")
    end = p.index("  function buildChips() {")
    p = p[:start] + '''  function renderGrid() {
    var grid = document.querySelector("[data-products]");
    if (!grid) return;

    var shown = PRODUCTS.filter(matches);
    grid.innerHTML = shown.length
      ? shown.map(rowHtml).join("")
      : '<div class="empty">' + icon("i-search") +
        '<p class="display display--xs">' + T("noMatch", "Nothing matches that") + "</p>" +
        '<p class="note">' + T("noMatchHelp", "Try a shorter word, or clear the filters.") + "</p>" +
        '<button class="btn btn--sm" type="button" data-clear>' + T("clearF", "Clear filters") + "</button></div>";

    var count = document.querySelector("[data-result-count]");
    if (count) {
      count.textContent = state.q || state.cat !== "all" || state.town !== "all"
        ? T("showing", "Showing") + " " + shown.length + " " + T("of", "of") + " " + PRODUCTS.length + " " +
          T("products", "products")
        : PRODUCTS.length + " " + T("products", "products") + " \\u00b7 " + CATS.length + " " +
          T("categories", "categories") + " \\u00b7 " + T("askPrice", "ask for today's price");
    }
    paintAddButtons();
  }

''' + p[end:]

    # the shortlist panel, in this design's markup
    start = p.index("  function renderPanel() {")
    end = p.index("  /* A four-card strip for the home page")
    p = p[:start] + '''  function renderPanel() {
    var panel = document.querySelector("[data-list-panel]");
    if (!panel) return;
    var ids = readList();

    if (!ids.length) {
      panel.innerHTML =
        '<div class="empty">' + icon("i-cart") +
          '<p class="display display--xs">' + T("emptyList", "Your list is empty") + "</p>" +
          '<p class="note">' + T("emptyHelp", "Add anything you want priced. It stays on this device until you send it.") + "</p>" +
          '<a class="btn btn--sm" href="#catalogue">' + T("browse", "Browse the catalogue") + "</a>" +
        "</div>";
      return;
    }

    panel.innerHTML =
      '<div class="list-panel">' +
        ids.map(function (id) {
          var p = product(id), c = cat(p.cat);
          return '<div class="list-item">' +
            '<span class="list-item__art">' + icon(c.art) + "</span>" +
            '<div><p class="list-item__title">' + esc(p.title) + "</p>" +
            '<p class="list-item__meta">' + esc(c.label) + " \\u00b7 " + esc(p.towns.join(", ")) + "</p></div>" +
            '<button class="btn btn--sm btn--ghost" type="button" data-remove="' + p.id + '" ' +
              'aria-label="' + T("remove", "Remove") + " " + esc(p.title) + '">' +
              T("remove", "Remove") + "</button>" +
          "</div>";
        }).join("") +
        '<p class="list-total">' + ids.length +
          (ids.length === 1 ? T("item", " item") : T("items", " items")) +
          " \\u2014 " + T("weWillPrice", "we will price it and call you") + "</p>" +
        '<div class="actions">' +
          '<a class="btn btn--primary" href="https://wa.me/91' + HELPLINE + "?text=" + encodeURIComponent(sendText()) + '" target="_blank" rel="noopener noreferrer">' +
            icon("i-whatsapp") + " " + T("wa", "Send on WhatsApp") + "</a>" +
          '<a class="btn" href="tel:+91' + HELPLINE + '">' + icon("i-call") + " " + T("callShort", "Call") + " " + HELPLINE + "</a>" +
          '<a class="btn btn--ghost" href="mailto:' + EMAIL + "?subject=" + encodeURIComponent("Price enquiry from the website") +
            "&body=" + encodeURIComponent(sendText()) + '">' + T("emailList", "Email the list") + "</a>" +
        "</div>" +
        '<p class="note">' + T("conceptNote2", "No card details, no account, nothing charged. A person from your nearest branch replies with today\\u2019s price.") + "</p>" +
      "</div>";
  }

''' + p[end:]

    # the home page strip becomes a list of tiles
    start = p.index("  function renderFeatured() {")
    end = p.index("  /* --------------------------------------------------------------- filters */")
    p = p[:start] + '''  /* Four popular items for the home page, built from the same catalogue so the
     two can never disagree. */
  function renderFeatured() {
    var host = document.querySelector("[data-featured]");
    if (!host) return;
    var picks = ["tv-55", "ac-15", "fr-265", "wm-7"].map(product).filter(Boolean);
    host.innerHTML = picks.map(function (p) {
      var c = cat(p.cat);
      return '<p class="tile"><span class="tile__t">' + esc(p.title) + "</span>" +
        '<span class="tile__d">' + esc(c.label) + " \\u00b7 " + esc(p.specs.join(" \\u00b7 ")) + "</span></p>";
    }).join("");
  }

''' + p[end:]

    # the add button uses this design's own states
    p = sub_once(p,
                 'buttons[i].className = "btn btn--sm " + (added ? "btn--brand" : "btn--brand");',
                 'buttons[i].className = "btn btn--sm " + (added ? "btn--done" : "btn--primary");',
                 "add button states")

    # chips: this design's "all" chip carries no icon
    p = sub_once(p, 'icon("i-sparkle") + "All</button>"', 'T("all", "All") + "</button>"', "all chip")

    # list labels: keep the count wording, this design has no mobile action bar.
    # The source is Trial 04's file, which may already be localised (it has been
    # through localise.py) or still plain, so both spellings of the line are tried.
    p = sub_either(p,
                   ['labels[j].textContent = n === 1 ? "1 item" : n + T("items", " items");',
                    'labels[j].textContent = n === 1 ? "1 item" : n + " items";'],
                   'labels[j].textContent = String(n) + (n === 1 ? T("item", " item") : T("items", " items"));',
                   "list labels")

    # ?q= from the 404 page's search box pre-fills the catalogue search
    p = sub_once(p, """  /* Deep link: products.html?cat=fridge, or a category tapped on the home page. */""",
                 """  /* Deep link: products.html?q=mixer (from the 404 page's box) or ?cat=fridge. */""",
                 "deep-link comment")
    p = sub_once(p, """  var params = new URLSearchParams(location.search);
  var wanted = params.get("cat");""",
                 """  var params = new URLSearchParams(location.search);
  var typed = params.get("q");
  if (typed && search) {
    search.value = typed;
    state.q = typed.trim().toLowerCase();
    renderGrid();
  }
  var wanted = params.get("cat");""",
                 "?q= support")

    # the sheet on phones is opened from the bar
    p = p.replace('''  /* ----------------------------------------------------------------- init */''',
                  '''  /* the shortlist panel: a sheet on phones, a sticky column on desktop */
  var aside = document.querySelector("[data-aside]");
  function setAside(open) {
    if (!aside) return;
    aside.setAttribute("data-open", open ? "true" : "false");
  }
  document.addEventListener("click", function (e) {
    if (e.target.closest("[data-panel-open]")) { setAside(true); return; }
    if (e.target.closest("[data-panel-close]")) { setAside(false); return; }
    if (e.target.closest("[data-add]")) { setAside(true); }
  });

  /* ----------------------------------------------------------------- init */''')

    write("products.js", p)

    # --------------------------------------------------------------- stores.js
    s = read("stores.js")
    s = header(s, "showroom directory",
               "The same 25 addresses as every other trial, grouped by district — a\n   directory you read down, in a design with no cards in it.")
    p = re.sub(r'var STORE_KEY = "[^"]*";', 'var STORE_KEY = "whynot-list-t7";', s) if 'STORE_KEY' in s else s
    s = p
    s = sub_once(s, """  function doodle(id, cls) {
    return '<svg class="doodle ' + (cls || "") + '" aria-hidden="true"><use href="#' + id + '"></use></svg>';
  }""",
                 """  function icon(id) {
    return '<svg class="icon" aria-hidden="true"><use href="#' + id + '"></use></svg>';
  }""", "icon helper")
    s = s.replace("doodle(", "icon(")

    start = s.index("  function card(s) {")
    end = s.index("  function matches(el) {")
    s = s[:start] + '''  function card(s) {
    var full = s.town + " \\u00b7 " + s.address + ", " + s.district + " district, Andhra Pradesh " + s.pincode;
    return '' +
      '<article class="store" data-district="' + esc(s.district) + '" data-search="' +
        esc((s.town + " " + s.address + " " + s.district + " " + s.pincode).toLowerCase()) + '">' +
        '<div class="store__top">' +
          '<span class="store__name">' + esc(s.town) + "</span>" +
          (s.label ? '<span class="badge">' + esc(s.label) + "</span>" : "") +
          '<span class="note mono">' + esc(s.pincode) + "</span>" +
        "</div>" +
        '<p class="store__addr">' + esc(full) + "</p>" +
        '<div class="store__acts">' +
          '<a class="btn btn--sm" href="' + mapsUrl(s) + '" target="_blank" rel="noopener noreferrer">' +
            icon("i-pin") + " " + T("directions", "Directions") + "</a>" +
          '<button class="btn btn--sm btn--ghost" type="button" data-copy="' + esc(full) + '">' +
            icon("i-copy") + " " + T("copyAddr", "Copy address") + "</button>" +
        "</div>" +
      "</article>";
  }

  /* Grouped by district: a heading per revenue district, then its branches. */
  function render() {
    var districts = [];
    STORES.forEach(function (s) {
      if (districts.indexOf(s.district) === -1) districts.push(s.district);
    });
    districts.sort();
    list.innerHTML = districts.map(function (d) {
      var branches = STORES.filter(function (s) { return s.district === d; });
      return '<section class="dir__group" data-group="' + esc(d) + '">' +
        "<h3>" + esc(d) + " \\u00b7 " + branches.length + " " + T("showrooms", "showrooms") + "</h3>" +
        '<div class="dir__items">' + branches.map(card).join("") + "</div>" +
      "</section>";
    }).join("");
  }

''' + s[end:]

    s = sub_once(s, "  list.innerHTML = STORES.map(card).join(\"\");", "  render();", "initial render")
    s = sub_once(s, '''    if (countEl) {
      countEl.textContent = state.q || state.district !== "all"
        ? "Showing " + shown + " of " + STORES.length
        : STORES.length + " showrooms \\u00b7 23 towns \\u00b7 1 helpline";
    }''',
                 '''    if (countEl) {
      countEl.textContent = state.q || state.district !== "all"
        ? T("showing", "Showing") + " " + shown + " " + T("of", "of") + " " + STORES.length
        : STORES.length + " " + T("showrooms", "showrooms") + " \\u00b7 " + T("twentyThreeTowns", "23 towns") +
          " \\u00b7 " + T("oneHelpline", "1 helpline");
    }''', "store count")
    # the long form above may already have matched; this only fires on the short one
    s = sub_once(s, '''    nodes.forEach(function (el) {
      var ok = matches(el);
      el.hidden = !ok;
      if (ok) shown++;
    });''',
                 '''    nodes.forEach(function (el) {
      var ok = matches(el);
      el.hidden = !ok;
      if (ok) shown++;
    });
    /* hide a district heading whose branches are all filtered out */
    Array.prototype.slice.call(document.querySelectorAll("[data-group]")).forEach(function (group) {
      var any = Array.prototype.slice.call(group.querySelectorAll(".store")).some(function (el) { return !el.hidden; });
      group.hidden = !any;
      if ("data-count" in group) group.setAttribute("data-count", String(any));
    });''', "group hiding")
    write("stores.js", s)

    # -------------------------------------------------------------- contact.js
    c = read("contact.js")
    c = header(c, "the enquiry form",
               "Same validation and same honesty as the other trials: the form says\n   plainly that there is no server behind it.")
    c = c.replace('class="field-row"', 'class="filters__row"')
    write("contact.js", c)

    # --------------------------------------------------------------- main.js
    m = read("main.js")
    m = header(m, "runtime",
               "Mode switch, the mobile tab bar, reveals, counters and the copy button.\n   There is no drawer: navigation is a rail on desktop and a tab bar on phones.")
    # the drawer block goes: this design navigates from a rail and a tab bar
    start = m.index("  /* ------------------------------------------------------- mobile drawer */")
    end = m.index("  /* --------------------------------------------------- reveal on scroll */")
    m = m[:start] + '''  /* ---------------------------------------------------------- the mode
     Light and dark are both designed palettes, not an inverted one. The mode is
     applied before paint by the inline script in <head>; this keeps the button
     in step and remembers the choice. */
  var modeBtn = $("[data-mode-toggle]");
  var modeState = $("[data-mode-state]");

  function setMode(mode, remember) {
    document.documentElement.setAttribute("data-mode", mode);
    if (modeBtn) {
      modeBtn.setAttribute("aria-pressed", mode === "dark" ? "true" : "false");
      modeBtn.setAttribute("aria-label", mode === "dark" ? "Switch to light mode" : "Switch to dark mode");
    }
    if (modeState) modeState.textContent = mode === "dark" ? "Dark mode on" : "Light mode on";
    var meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute("content", mode === "dark" ? "#0b0d12" : "#ffffff");
    if (remember) { try { localStorage.setItem("whynot-mode", mode); } catch (e) {} }
  }

  if (modeBtn) {
    setMode(document.documentElement.getAttribute("data-mode") === "dark" ? "dark" : "light", false);
    modeBtn.addEventListener("click", function () {
      setMode(document.documentElement.getAttribute("data-mode") === "dark" ? "light" : "dark", true);
    });
  }

  /* if the reader has not chosen, follow the system as it changes */
  if (window.matchMedia) {
    var mq = window.matchMedia("(prefers-color-scheme: dark)");
    var follow = function (e) {
      var saved = null;
      try { saved = localStorage.getItem("whynot-mode"); } catch (err) {}
      if (!saved) setMode(e.matches ? "dark" : "light", false);
    };
    if (mq.addEventListener) mq.addEventListener("change", follow);
    else if (mq.addListener) mq.addListener(follow);
  }

  /* the shortlist sheet on phones: Escape closes it, tapping the backdrop too */
  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    var aside = document.querySelector("[data-aside]");
    if (aside && aside.getAttribute("data-open") === "true") aside.setAttribute("data-open", "false");
  });

''' + m[end:]

    # the copy toast wording is this design's voice
    m = sub_once(m, 'var done = function () { flash("Copied  " + text); };',
                 'var done = function () { flash(T("copied", "Copied") + "  " + text); };', "copy toast")
    m = sub_once(m, 'el.textContent = openNow ? "Open now" : "Closed now";',
                 'el.textContent = openNow ? T("openNow", "Open now") : T("closedNow", "Closed now");', "shop state")
    m = sub_once(m, '''    el.textContent = openNow
      ? "Open until 9 pm today — walk in and ask for a demo."
      : "We open at 10 am. Leave your number and we'll ring you back.";''',
                 '''    el.textContent = openNow
      ? T("openNote", "Open until 9 pm today \\u2014 walk in and ask for a demo.")
      : T("closedNote", "We open at 10 am. Leave your number and we'll ring you back.");''', "shop note")
    write("main.js", m)

    print("\nNext: node --check each file, then python3 _tools/localise.py trial-07-slate")


if __name__ == "__main__":
    main()
