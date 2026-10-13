#!/usr/bin/env python3
"""
Localiser — puts the three languages on every trial.

Usage:  python3 _tools/localise.py [trial-dir ...]     (default: all seven)

What it does, once per trial:

  1. writes assets/js/i18n.js — the runtime. It captures the English text that is
     already in the page, swaps in Telugu or Hindi when asked, remembers the
     choice, and tells the catalogue scripts to redraw their generated markup.
  2. hooks the HTML — every element whose text matches a phrase in
     _tools/i18n.py gets data-i18n (text) or data-i18n-html (phrases containing
     <br> or <span>), so a phrase is only ever written in one place.
  3. hooks the JavaScript — the strings products.js, stores.js and contact.js
     build at runtime ("Add to list", "Directions", the form's validation
     messages) become T("key") lookups, and each script registers a redraw hook
     so switching language updates the catalogue, not just the static markup.
  4. adds the switcher to the header.
  5. installs the type: Noto Sans Telugu and Noto Sans Devanagari, SUBSET to the
     glyphs this site actually uses (about a fifth of the file), and appends a
     block to the trial's stylesheet that re-points its font variables for those
     two languages — plus the looser letter-spacing Indic scripts need.

Everything it writes is idempotent: running it twice changes nothing.
"""

import io
import os
import re
from html import escape, unescape
from html.parser import HTMLParser
import shutil
import sys

from fontTools import subset
from fontTools.ttLib import TTFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import i18n  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT_SRC = {
    "te": {
        "400": "/tmp/fonts4/noto-sans-telugu/package/files/noto-sans-telugu-telugu-400-normal.woff2",
        "700": "/tmp/fonts4/noto-sans-telugu/package/files/noto-sans-telugu-telugu-700-normal.woff2",
        "family": "Noto Sans Telugu",
    },
    "hi": {
        "400": "/tmp/fonts4/noto-sans-devanagari/package/files/noto-sans-devanagari-devanagari-400-normal.woff2",
        "700": "/tmp/fonts4/noto-sans-devanagari/package/files/noto-sans-devanagari-devanagari-700-normal.woff2",
        "family": "Noto Sans Devanagari",
    },
}

SWITCHER = '''<div class="langswitch" role="group" aria-label="Language / భాష">
        <button type="button" class="langswitch__btn" data-lang="en" aria-pressed="true">EN</button>
        <button type="button" class="langswitch__btn" data-lang="te" aria-pressed="false">తె</button>
        <button type="button" class="langswitch__btn" data-lang="hi" aria-pressed="false">हि</button>
      </div>'''


# --------------------------------------------------------------------- runtime
def runtime_js(used, keys):
    """The i18n runtime, with only the strings this trial actually has. English
    comes from the page itself (it is captured at boot), so it is never carried
    twice — and a trial does not pay for the other six trials' copy."""
    import json
    used = sorted(used)   # a set: sort it, or PYTHONHASHSEED rewrites the file every run
    te, hi = {}, {}
    for phrase in used:
        entry = i18n.LOCALISABLE.get(phrase)
        if entry:
            te[phrase] = entry["te"]
            hi[phrase] = entry["hi"]

    alias = {}
    for en, (key, vals) in i18n.JS_STRINGS.items():
        if key not in keys and en not in keys:
            continue
        te[key] = vals["te"]
        hi[key] = vals["hi"]
        # a phrase the scripts generate is stored under its short key, so the DOM
        # pass needs the English it will see on screen mapped to that key
        alias[normalise(en)] = key
    for en, key in i18n.JS_LITERALS.items():
        if key in keys:
            alias.setdefault(normalise(en), key)
    for phrase in used:
        alias.setdefault(normalise(phrase), phrase)

    return """/* WHYNOT — the language switch.
   ---------------------------------------------------------------------------
   Three languages: English, Telugu and Hindi. The Telugu and Hindi copy in here
   was written in those languages rather than translated from the English — it is
   shorter, it uses the words a shop in Tanuku would use, and where the English
   needs a paragraph the Telugu often needs four words.

   How it works: the page is authored in English. On first load this file
   photographs that English (text and markup) per element, then any switch simply
   swaps text in and out. Nothing is re-fetched and the page works with
   JavaScript switched off — because with JS off it never switches.
   --------------------------------------------------------------------------- */
window.WHYNOT_I18N = (function () {
  "use strict";

  var STRINGS = %s;
  var PATTERNS = %s;
  var ALIAS = %s;
  var KEY = "whynot-lang";
  var LANGS = ["en", "te", "hi"];
  var originals = null;   /* the English, captured once */

  function elements() {
    return document.querySelectorAll("[data-i18n], [data-i18n-html]");
  }

  function capture() {
    originals = [];
    var list = elements();
    for (var i = 0; i < list.length; i++) {
      var el = list[i];
      originals.push(el.hasAttribute("data-i18n-html") ? el.innerHTML : el.textContent);
    }
    var fields = document.querySelectorAll("[data-i18n-ph]");
    originals.fields = [];
    for (var j = 0; j < fields.length; j++) originals.fields.push(fields[j].placeholder);
  }

  function text(lang, key) {
    if (lang === "en") return null;
    var table = STRINGS[lang] || {};
    return table[key] || null;
  }

  function apply(lang) {
    if (LANGS.indexOf(lang) === -1) lang = "en";
    if (!originals) capture();
    document.documentElement.lang = lang === "en" ? "en-IN" : lang;

    var list = elements();
    for (var i = 0; i < list.length; i++) {
      var el = list[i];
      var key = el.getAttribute("data-i18n-html") || el.getAttribute("data-i18n");
      var value = text(lang, key);
      if (value === null) value = originals[i];
      if (el.hasAttribute("data-i18n-html")) el.innerHTML = value;
      else el.textContent = value;
    }

    var fields = document.querySelectorAll("[data-i18n-ph]");
    for (var j = 0; j < fields.length; j++) {
      var pk = fields[j].getAttribute("data-i18n-ph");
      fields[j].placeholder = text(lang, pk) || originals.fields[j];
    }

    var buttons = document.querySelectorAll("[data-lang]");
    for (var b = 0; b < buttons.length; b++) {
      buttons[b].setAttribute("aria-pressed", buttons[b].getAttribute("data-lang") === lang ? "true" : "false");
    }

    try { localStorage.setItem(KEY, lang); } catch (e) { /* private mode */ }

    /* let the catalogue, the shortlist and the form redraw their own text */
    translateTree(document, lang);
    if (typeof window.WHYNOT_RERENDER === "function") window.WHYNOT_RERENDER();
    translateTree(document, lang);
    watch(lang);
    document.dispatchEvent(new CustomEvent("whynot:lang", { detail: { lang: lang } }));
  }

  function T(key, fallback) {
    var lang = document.documentElement.lang;
    var value = text(lang, key);
    return value === null || value === undefined ? (fallback === undefined ? key : fallback) : value;
  }

  document.addEventListener("click", function (e) {
    var btn = e.target.closest ? e.target.closest("[data-lang]") : null;
    if (btn) apply(btn.getAttribute("data-lang"));
  });

  function boot() {
    var saved = null;
    try { saved = localStorage.getItem(KEY); } catch (e) { /* ignore */ }
    capture();                       /* always capture English first */
    if (saved && saved !== "en") apply(saved);
  }

  /* A second pass over the DOM, for markup the catalogue builds at runtime. The
     scripts emit English; this translates whatever leaf text matches a phrase we
     know, which is cheaper and far less brittle than threading every string
     through a lookup. */
  var REVERSE = (function () {
    var map = {};
    var all = Object.keys(STRINGS.te || {});
    for (var i = 0; i < all.length; i++) map[normalise(all[i])] = all[i];
    return map;
  })();

  function normalise(s) {
    return String(s).replace(/\s+/g, " ").trim();
  }

  function translateText(node, lang) {
    var parent = node.parentNode;
    if (!parent) return;
    var tag = parent.nodeName.toLowerCase();
    if (tag === "script" || tag === "style" || tag === "svg" || (parent.closest && parent.closest("svg"))) return;
    var raw = node.nodeValue;
    if (!raw || !raw.trim()) return;
    var text0 = normalise(raw);

    /* phrases carrying dynamic content: "In stock at Tanuku", "Showing 5 of 17" */
    for (var p = 0; p < PATTERNS.length; p++) {
      var m = text0.match(new RegExp(PATTERNS[p].re));
      if (!m) continue;
      var out = PATTERNS[p][lang] || PATTERNS[p].en;
      for (var g = m.length - 1; g >= 1; g--) out = out.split("$" + g).join(m[g]);
      node.nodeValue = out;
      return;
    }

    /* exact phrases — in the page's own wording, or a phrase the scripts make */
    var key = REVERSE[text0] || ALIAS[text0];
    if (!key) return;
    var value = text(lang, key);
    if (value !== null) node.nodeValue = value;
  }

  function translateTree(root, lang) {
    if (lang === "en") return;
    /* Walk TEXT NODES, not elements: a button written as
         <a class="btn"> <svg class="doodle">…</svg> Directions </a>
       has a child element, so an element-level pass would skip it — which is
       exactly what it did the first time this was written. */
    var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null);
    var nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    for (var i = 0; i < nodes.length; i++) translateText(nodes[i], lang);
  }

  /* The catalogue, the shortlist and the showroom list redraw themselves long
     after a language was chosen — searching, filtering, adding an item. A watch
     on the DOM translates whatever they produce, so a phrase generated at any
     time is still in the reader's language. Only childList is watched: the pass
     itself writes text values, which cannot loop back into it. */
  var observer = null;

  function watch(lang) {
    if (observer) { observer.disconnect(); observer = null; }
    if (lang === "en" || !window.MutationObserver) return;
    observer = new MutationObserver(function (records) {
      for (var i = 0; i < records.length; i++) {
        var added = records[i].addedNodes;
        for (var j = 0; j < added.length; j++) {
          var node = added[j];
          if (node.nodeType === 1) translateTree(node, lang);
          else if (node.nodeType === 3 && node.parentNode && !(node.parentNode.closest && node.parentNode.closest("svg"))) {
            translateText(node, lang);
          }
        }
      }
    });
    observer.observe(document.body, { childList: true, subtree: true });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();

  return { apply: apply, t: T, STRINGS: STRINGS, KEY: KEY, translateTree: translateTree };
})();

/* The scripts build markup later than this file runs, so give them a handle. */
window.WHYNOT_T = function (key, fallback) { return window.WHYNOT_I18N.t(key, fallback); };
""" % (json.dumps({"te": te, "hi": hi}, ensure_ascii=False, separators=(",", ":")),
       json.dumps([{ "re": p["re"], "te": p["te"], "hi": p["hi"] } for p in i18n.RUNTIME_PATTERNS],
                  ensure_ascii=False, separators=(",", ":")),
       json.dumps(alias, ensure_ascii=False, separators=(",", ":")))


# ------------------------------------------------------------------------ fonts
def subset_fonts(target, trials):
    """Subset the two Indic faces to the glyphs actually used, per trial."""
    chars = {lang: set() for lang in ("te", "hi")}
    for key, entry in i18n.LOCALISABLE.items():
        for lang in ("te", "hi"):
            chars[lang] |= set(entry[lang])
    for en, (key, vals) in i18n.JS_STRINGS.items():
        for lang in ("te", "hi"):
            chars[lang] |= set(vals[lang])
    chars["te"] |= set("తె")
    chars["hi"] |= set("हि")
    # digits, latin and punctuation that share a line with the localised copy
    for lang in chars:
        chars[lang] |= set("0123456789/:.,;()[]-–—+&%!?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ")
    return chars


def install_fonts(root, chars, report):
    out = os.path.join(root, "assets", "fonts")
    for lang, spec in FONT_SRC.items():
        for weight, src in (("400", spec["400"]), ("700", spec["700"])):
            if not os.path.exists(src):
                report("  ! font source missing: %s" % src)
                continue
            name = "noto-%s-%s.woff2" % ("telugu" if lang == "te" else "devanagari", weight)
            dest = os.path.join(out, name)
            text = "".join(sorted(chars[lang]))
            subset.main([src, "--output-file=%s" % dest, "--text=%s" % text,
                         "--layout-features=*", "--flavor=woff2", "--no-hinting",
                         "--desubroutinize", "--drop-tables+=DSIG"])
            report("  %-24s %5.1f KB (from %5.1f KB) covers %d characters" % (
                name, os.path.getsize(dest) / 1024, os.path.getsize(src) / 1024, len(chars[lang])))


def css_block(root, trials_css):
    """Appended to each trial's stylesheet: the language faces, the variable
    overrides that actually switch the type, and the switcher's own styling."""
    fonts = [("Noto Sans Telugu", "telugu"), ("Noto Sans Devanagari", "devanagari")]
    face = ""
    for family, slug in fonts:
        for weight in ("400", "700"):
            face += ('@font-face { font-family: "%s"; font-style: normal; font-weight: %s; font-display: swap;\n'
                     '  src: url("../fonts/noto-%s-%s.woff2") format("woff2"); }\n' % (family, weight, slug, weight))

    vars_ = re.findall(r"(--font-[a-z0-9-]+)\s*:", trials_css)
    vars_ = sorted(set(vars_))
    if not vars_:
        return None, []

    def overrides(family):
        out = []
        body_var = [v for v in vars_ if "body" in v] or list(vars_)
        for v in vars_:
            out.append("%s: \"%s\", %s;" % (v, family, v))
        return body_var, out

    block = "\n\n/* ==========================================================================\n"
    block += "   Languages — Telugu and Hindi\n"
    block += "   The Latin faces in this design have no Indic glyphs, so the font\n"
    block += "   variables are re-pointed for those two languages. Indic scripts also\n"
    block += "   need looser tracking and real word spacing: the tight letter-spacing that\n"
    block += "   makes a Latin headline look designed makes Telugu look broken.\n"
    block += "   ========================================================================== */\n"
    block += face

    for lang, family in (("te", "Noto Sans Telugu"), ("hi", "Noto Sans Devanagari")):
        body_var, over = overrides(family)
        block += '\nhtml[lang="%s"] {\n  %s\n}\n' % (lang, "\n  ".join(over))
        block += ('html[lang="%s"] .display, html[lang="%s"] .shout, html[lang="%s"] h1, html[lang="%s"] h2,\n'
                  'html[lang="%s"] h3, html[lang="%s"] .btn, html[lang="%s"] .brand__name, html[lang="%s"] .stat__v {\n'
                  '  font-weight: 700; letter-spacing: 0;\n}\n'
                  % ((lang,) * 8))
        block += ('html[lang="%s"] .kicker, html[lang="%s"] .label, html[lang="%s"] .card__cat,\n'
                  'html[lang="%s"] .stat__l, html[lang="%s"] .count, html[lang="%s"] .note {\n'
                  '  letter-spacing: .02em;\n}\n' % ((lang,) * 6))

    block += """
/* the language switcher, styled from the trial's own tokens so it belongs */
.langswitch { display: inline-flex; align-items: center; gap: 2px; padding: 3px;
  border: 1px solid currentColor; border-radius: 999px; opacity: .92; }
.langswitch__btn { min-width: 34px; min-height: 30px; padding: 0 6px; border: 0; border-radius: 999px;
  background: transparent; color: inherit; font: inherit; font-size: .6875rem; font-weight: 700;
  letter-spacing: 0; cursor: pointer; }
.langswitch__btn:hover { background: rgba(128, 128, 128, .22); }
.langswitch__btn[aria-pressed="true"] { background: currentColor; }
.langswitch__btn[aria-pressed="true"] { color: transparent; text-shadow: 0 0 0 var(--paper, #fff); }
@media (max-width: 560px) { .langswitch { padding: 2px; } .langswitch__btn { min-width: 30px; min-height: 26px; font-size: .625rem; } }
"""
    return block, vars_


# -------------------------------------------------------------------------- html
def normalise(s):
    s = s.replace("<br>", " ").replace("<br/>", " ").replace("<br />", " ")
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("&amp;", "&").replace("&nbsp;", " ").replace("&rsquo;", "’").replace("&mdash;", "—")
    return re.sub(r"\s+", " ", s).strip()


class Walker:
    """Finds elements and their offsets in the raw HTML, so an attribute can be
    inserted without re-serialising the document (no reformatting, no surprises)."""

    def __init__(self, html):
        self.html = html
        self.line_starts = [0]
        for line in html.splitlines(True):
            self.line_starts.append(self.line_starts[-1] + len(line))
        self.elements = []          # (start, end, tagname, inner_start, inner_end, depth_children)
        self._stack = []

    def offset(self, pos):
        line, col = pos
        return self.line_starts[line - 1] + col

    def parse(self):
        html = self.html
        tag_re = re.compile(r"<(/?)([a-zA-Z][a-zA-Z0-9]*)([^>]*)>")
        void = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta",
                "source", "track", "wbr", "use", "path", "rect", "circle", "g"}
        for m in tag_re.finditer(html):
            closing, name, attrs = m.group(1), m.group(2).lower(), m.group(3)
            if name in void or attrs.rstrip().endswith("/"):
                continue
            if not closing:
                self._stack.append((name, m.start(), m.end()))
            else:
                for i in range(len(self._stack) - 1, -1, -1):
                    if self._stack[i][0] == name:
                        tname, start, inner_start = self._stack.pop(i)
                        self.elements.append((start, m.end(), tname, inner_start, m.start()))
                        break
        return self


def verify_placement(html, name=""):
    """Every hook must sit on the element whose text is that phrase.

    The structural check above proves nothing moved; this proves each hook landed
    on the right element. These pages carry a lot of near-identical markup, and an
    offset that is a character or two out still produces valid HTML — it just
    hooks the wrong node. Comparing the English back to the key is what catches it.
    """
    problems = []
    class P(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.convert_charrefs = True
            self.stack = []
            self.text = []
        def handle_starttag(self, tag, attrs):
            if tag in ("br", "img", "hr", "input", "meta", "link"):
                # a <br> is a line break in the phrase too, so it reads as one here
                if tag == "br":
                    for frame in self.stack:
                        frame[2] += "\n"
                return
            a = dict(attrs)
            key = a.get("data-i18n-html") or a.get("data-i18n") or a.get("data-i18n-ph")
            self.stack.append([tag, key, "", a.get("placeholder") or ""])
        def handle_data(self, data):
            for frame in self.stack:
                frame[2] += data
        def handle_endtag(self, tag):
            for i in range(len(self.stack) - 1, -1, -1):
                if self.stack[i][0] == tag:
                    frame = self.stack.pop(i)
                    key = frame[1]
                    if not key:
                        break
                    if key not in i18n.LOCALISABLE:
                        problems.append("unknown key %r on <%s>" % (key, tag))
                        break
                    want = i18n.LOCALISABLE[key]["en"]
                    got = frame[3] or frame[2]
                    # a <br> in the phrase is a line break in the element, and an
                    # entity in one is the character in the other: compare the
                    # same sentence written each way rather than only verbatim
                    want_forms = set()
                    for form in (want, unescape(want)):
                        want_forms.add(normalise(form))
                        want_forms.add(normalise(re.sub(r"<br\s*/?>", "\n", form)))
                        want_forms.add(normalise(re.sub(r"<[^>]+>", "", form)))
                    if normalise(got) not in want_forms:
                        problems.append("<%s> key %r says %r, element says %r"
                                        % (tag, key, want[:40], got.strip()[:40]))
                    break
    P().feed(html)
    if problems:
        raise SystemExit("hook placement failed in %s:\n    %s" % (name or "?", "\n    ".join(problems[:6])))
    return True


def verify_hooks(before, after, name=""):
    """Every hook is an added attribute, and nothing else. If inserting them has
    moved, truncated or swallowed anything, the tag sequence or the text changes
    and this fails loudly rather than shipping quietly broken markup."""
    def scan(html):
        tags, text = [], []
        class P(HTMLParser):
            def handle_starttag(self, tag, attrs):
                tags.append((tag, tuple(sorted(a for a, _ in attrs))))
            def handle_startendtag(self, tag, attrs):
                tags.append((tag, tuple(sorted(a for a, _ in attrs))))
            def handle_endtag(self, tag):
                tags.append(("/" + tag, ()))
            def handle_data(self, data):
                if data.strip():
                    text.append(re.sub(r"\s+", " ", data).strip())
        P(convert_charrefs=True).feed(html)
        return tags, text

    b_tags, b_text = scan(before)
    a_tags, a_text = scan(after)
    if len(b_tags) != len(a_tags):
        raise SystemExit("hook check failed in %s: %d tags before, %d after" % (name, len(b_tags), len(a_tags)))
    for (bt, ba), (at, aa) in zip(b_tags, a_tags):
        if bt != at:
            raise SystemExit("hook check failed in %s: <%s> became <%s>" % (name, bt, at))
        if not set(ba).issubset(set(aa)):
            raise SystemExit("hook check failed in %s: <%s> lost %s" % (name, bt, sorted(set(ba) - set(aa))))
        extra = [x for x in aa if x not in ba]
        if [x for x in extra if not x.startswith("data-i18n")]:
            raise SystemExit("hook check failed in %s: <%s> gained %s" % (name, bt, extra))
    if b_text != a_text:
        raise SystemExit("hook check failed in %s: page text changed" % name)
    return len(a_tags)


def patch_attributes(html, name=""):
    """Add the i18n hooks. Matching is on normalised text, so it survives the
    different markup each trial uses (<br>, <span class="mark">, entity choices).

    Every insertion is computed against THIS string and applied in one pass at
    the end, back to front. An earlier version ran the placeholder substitution
    first, which shifted every later offset by the length of what it inserted —
    hooks landed inside other attributes and the markup came out mangled."""
    before = html
    by_text = {}
    for key, entry in i18n.LOCALISABLE.items():
        by_text.setdefault(normalise(entry["en"]), (key, entry.get("html", False)))
        # the same phrase as the page would write it: &amp; for &, &#10003; for a tick
        by_text.setdefault(normalise(escape(entry["en"], quote=False).replace("&#x27;", "'")),
                           (key, entry.get("html", False)))

    walker = Walker(html).parse()
    inserts = []          # (offset, string)
    hooked = 0
    for start, end, tagname, inner_start, inner_end in walker.elements:
        if tagname in ("script", "style", "svg", "symbol", "head", "html", "title"):
            continue
        inner = html[inner_start:inner_end]
        if len(inner) > 900 or "data-i18n" in html[start:inner_start]:
            continue
        found = by_text.get(normalise(inner)) or by_text.get(normalise(unescape(inner)))
        if not found:
            continue
        key, needs_html = found
        has_children = bool(re.search(r"<[a-zA-Z]", inner))
        if has_children and not needs_html:
            continue
        # a phrase that reads across a line break is written with <br> in the
        # translations, so it must be swapped in as markup even when the page
        # happens to use a plain newline instead of a <br>
        carries_markup = needs_html or any("<" in v for v in i18n.LOCALISABLE[key].values() if isinstance(v, str))
        attr = "data-i18n-html" if (has_children or carries_markup) else "data-i18n"
        # only the double quote needs escaping: the value is a phrase that may
        # contain one (a quoted figure in a sentence), while <br> and & are both
        # wanted verbatim — <br> to become markup again, & to match the key
        inserts.append((start + 1 + len(tagname), ' %s="%s"' % (attr, key.replace('"', "&quot;"))))
        hooked += 1

    # placeholders on form fields, pinned to the end of the field's own tag
    for m in re.finditer(r'placeholder="([^"]+)"[^>]*>', html):
        value = normalise(m.group(1))
        entry = next((k for k, e in i18n.LOCALISABLE.items() if normalise(e["en"]) == value), None)
        if not entry or "data-i18n-ph" in m.group(0):
            continue
        inserts.append((m.end() - 1, ' data-i18n-ph="%s"' % entry.replace('"', "&quot;")))
        hooked += 1

    for offset, text in sorted(inserts, reverse=True):
        html = html[:offset] + text + html[offset:]

    # the hooks are the only change so far: assert that before adding the switcher
    if name:
        verify_hooks(before, html, name)
        verify_placement(html, name)

    # the switcher, once per page
    if "langswitch" not in html:
        if '<div class="header-actions">' in html:
            html = html.replace('<div class="header-actions">', '<div class="header-actions">\n      ' + SWITCHER, 1)
            hooked += 1
        elif "</header>" in html:
            html = html.replace("</header>", "  " + SWITCHER + "\n</header>", 1)
            hooked += 1
        else:
            return html, hooked, False

    return html, hooked, True


def js_literals(text):
    """Yield (start, end, quote, raw) for every string literal in a script.

    Comments and regex literals are skipped. Both matter: a regex character class
    like /[&<>"']/ carries quote characters, and an earlier version of this
    scanner read the quote inside one as the start of a string, throwing every
    literal after it out of step (which is how phrases stopped being found at
    all). Template literals are treated as literals, escapes are respected."""
    KEYWORDS = ("return", "typeof", "case", "in", "of", "new", "delete", "void",
                "do", "else", "yield", "await", "instanceof", "throw")
    i, n = 0, len(text)
    prev = ""            # last significant character, for the regex test
    prev_word = ""       # last significant word, for the same test
    while i < n:
        ch = text[i]

        if ch.isspace():
            i += 1
            continue

        if ch == "/" and i + 1 < n and text[i + 1] == "/":
            j = text.find("\n", i)
            i = n if j == -1 else j + 1
            continue
        if ch == "/" and i + 1 < n and text[i + 1] == "*":
            j = text.find("*/", i + 2)
            i = n if j == -1 else j + 2
            continue

        # a regex, not a division: only where an expression may start
        if ch == "/" and (prev == "" or prev in "(,=:[!&|?{};+-*%~^<>" or prev_word in KEYWORDS):
            j, in_class = i + 1, False
            while j < n:
                c = text[j]
                if c == "\\":
                    j += 2; continue
                if c == "[":
                    in_class = True
                elif c == "]":
                    in_class = False
                elif c == "/" and not in_class:
                    break
                elif c == "\n":
                    break
                j += 1
            if j < n and text[j] == "/":
                j += 1
                while j < n and text[j].isalpha():
                    j += 1
                i = j
                prev = "/"
                prev_word = ""
                continue

        if ch in "\"'`":
            j, buf = i + 1, []
            while j < n:
                c = text[j]
                if c == "\\":
                    buf.append(text[j:j + 2]); j += 2; continue
                if c == ch:
                    break
                buf.append(c); j += 1
            if j < n:
                yield (i, j + 1, ch, "".join(buf))
                i = j + 1
                prev = ch
                prev_word = ""
                continue

        if ch.isalnum() or ch in "_$":
            k = i
            while k < n and (text[k].isalnum() or text[k] in "_$"):
                k += 1
            prev_word = text[i:k]
            prev = text[k - 1]
            i = k
            continue

        prev = ch
        prev_word = ""
        i += 1


def patch_js(text, report=None, name=""):
    """Point the text the scripts build at the language table.

    Strings are matched as WHOLE LITERALS, not as substrings of the source. An
    earlier version searched the raw text and happily matched a phrase that sat
    inside a longer literal, which produced nested T() calls and, at its worst,
    mangles like T("remove") appearing inside someone else's quotes. A scanner
    that knows where each literal starts and ends cannot make that mistake."""
    if "window.WHYNOT_T" not in text:
        # If the runtime never loads, the English wins: these calls carry their
        # own English as the second argument, so the page still reads correctly.
        stub = ('function fallbackT(key, english) { return english === undefined ? key : english; }\n')
        anchor = '  "use strict";\n'
        if "fallbackT" not in text:
            text = stub + text
        if anchor in text:
            text = text.replace(anchor, anchor + '\n  var T = window.WHYNOT_T || fallbackT;\n', 1)
        else:
            text = 'var T = window.WHYNOT_T || fallbackT;\n' + text

    edits = []
    for start, end, quote, raw in js_literals(text):
        value = raw.replace("\\'", "'").replace('\\"', '"')

        # a literal with something dynamic beside it: break out of the quotes
        swapped = False
        for lit, pre, key, english, post in i18n.JS_EXPRESSIONS:
            if value != lit:
                continue
            edits.append((start, end, "%s%s%s + T(\"%s\", \"%s\") + %s%s%s"
                          % (quote, pre, quote, key, english, quote, post, quote)))
            swapped = True
            break
        if swapped:
            continue

        key = i18n.JS_LITERALS.get(value)
        if not key:
            continue
        # already patched? Patching twice used to wrap the wrapper, so a re-run
        # grew T("k", T("k", T("k", ...))) — one phrase, seven deep, in the file a
        # customer would read. A literal that is already this call's fallback, or
        # its key, is left exactly as it is.
        before_txt, after_txt = text[max(0, start - 40):start], text[end:end + 40]
        if re.search(r'T\(\s*"%s"\s*,\s*$' % re.escape(key), before_txt):
            continue
        if re.match(r'\s*,\s*"%s"\s*\)' % re.escape(key), after_txt):
            continue
        edits.append((start, end, 'T("%s", %s%s%s)' % (key, quote, raw, quote)))

    for start, end, replacement in sorted(edits, reverse=True):
        text = text[:start] + replacement + text[end:]

    if report:
        left = [w for w in i18n.LEFTOVER_WATCH if w in text]
        note = ("   (%d phrases keep English in the source and are translated on screen "
                "by the DOM pass)" % len(left)) if left else ""
        report("  %-12s localised%s" % (name, note))
    return text


def ensure_rerender(text, call):
    """Put the redraw hook *inside* the IIFE — these files are all wrapped in one,
    and a hook registered after it cannot see renderGrid() or apply()."""
    if "WHYNOT_RERENDER" in text:
        return text
    marker = "\n})();"
    hook = ("\n\n  /* redraw the generated markup when the language changes */\n"
            "  " + call + "\n")
    if marker in text:
        at = text.rindex(marker)
        return text[:at] + hook + text[at:]
    return text.rstrip() + "\n" + call + "\n"


# -------------------------------------------------------------------------- main
def localise(root, report=print):
    name = os.path.basename(os.path.abspath(root))
    report("\n%s" % name)

    chars = subset_fonts(root, name)
    install_fonts(root, chars, report)

    # pages
    total = 0
    for fn in sorted(os.listdir(root)):
        if not fn.endswith(".html"):
            continue
        path = os.path.join(root, fn)
        html = io.open(path, encoding="utf-8").read()
        html, hooked, ok = patch_attributes(html, os.path.join(root, fn))
        if not ok:
            report("  ! %s: no header found for the switcher" % fn)
        if "assets/js/i18n.js" not in html:
            html = html.replace('<script src="assets/js/main.js" defer></script>',
                                '<script src="assets/js/i18n.js" defer></script>\n<script src="assets/js/main.js" defer></script>')
        io.open(path, "w", encoding="utf-8").write(html)
        total += hooked
        report("  %-14s %3d phrases hooked + switcher" % (fn, hooked))

    # scripts
    js_dir = os.path.join(root, "assets", "js")
    os.makedirs(js_dir, exist_ok=True)
    for fn, call in (("main.js", None),
                     ("products.js", "window.WHYNOT_RERENDER = function () { renderGrid(); renderFeatured(); renderPanel(); };"),
                     ("stores.js", "window.WHYNOT_RERENDER = function () { apply(); };"),
                     ("contact.js", "window.WHYNOT_RERENDER = function () { var s = document.querySelector('[data-form-status]'); if (s && s.textContent) { s.textContent = s.textContent; } };")):
        path = os.path.join(js_dir, fn)
        if not os.path.exists(path):
            continue
        text = io.open(path, encoding="utf-8").read()
        text = patch_js(text, report, fn)
        if call:
            text = ensure_rerender(text, call)
        # the pass has to be idempotent: a re-run must change nothing. It used to
        # wrap its own wrapper, so running it twice left T("k", T("k", "English"))
        # in the source — seven deep in the worst file, which is not what a
        # customer should read when they open the script.
        again = patch_js(text)
        if again != text:
            raise SystemExit("localiser is not idempotent: %s changed on a second pass" % fn)
        io.open(path, "w", encoding="utf-8").write(text)

    # stylesheet
    css_path = os.path.join(root, "assets", "css", "style.css")
    css = io.open(css_path, encoding="utf-8").read()
    if "Languages — Telugu and Hindi" not in css:
        block, vars_ = css_block(root, css)
        if block:
            io.open(css_path, "w", encoding="utf-8").write(css.rstrip() + block)
            report("  css: re-pointed %s for te/hi, added the switcher styles" % ", ".join(vars_))
        else:
            report("  ! css: found no --font-* variables to re-point")
    else:
        report("  css: language block already present")

    # what this trial actually contains: the phrases hooked on its pages, plus
    # the ones its scripts build (those are in the table under their short keys)
    used = set()
    for fn in sorted(os.listdir(root)):
        if not fn.endswith(".html"):
            continue
        html = io.open(os.path.join(root, fn), encoding="utf-8").read()
        for m in re.finditer(r'data-i18n(?:-html|-ph)?="([^"]*)"', html):
            used.add(unescape(m.group(1)))

    # the keys the scripts look up by name (from their T() calls), so a trial
    # ships its own copy and nothing else
    keys = set()
    code = ""
    for fn in os.listdir(js_dir):
        if not fn.endswith(".js") or fn == "i18n.js":
            continue
        code += io.open(os.path.join(js_dir, fn), encoding="utf-8").read()
    keys.update(m.group(1) for m in re.finditer(r'T\("([A-Za-z0-9_]+)"', code))

    # a phrase some scripts still build by hand (the patcher replaces what it can
    # match, the rest is translated on screen) needs its entry too — otherwise the
    # DOM pass has the English in front of it and nothing to put in its place
    for english, key in i18n.JS_LITERALS.items():
        if english in code:
            keys.add(key)
    for english, (key, _vals) in i18n.JS_STRINGS.items():
        if english in code:
            keys.add(key)
    keys.discard("")

    runtime = runtime_js(used, keys)
    with io.open(os.path.join(js_dir, "i18n.js"), "w", encoding="utf-8") as f:
        f.write(runtime)
    # bytes, not characters: Telugu and Hindi are three bytes each in UTF-8, so a
    # character count under-reports the file by a third and the docs quoted it
    report("  wrote i18n.js — %d languages, %d page phrases + %d script keys of %d, %.1f KB" % (
        len(i18n.LANGS), len(used), len(keys), len(i18n.LOCALISABLE) + len(i18n.JS_STRINGS),
        len(runtime.encode("utf-8")) / 1024.0))

    report("  %d phrases hooked in this trial" % total)


if __name__ == "__main__":
    args = sys.argv[1:] or ["trial-01-minimal", "trial-02-illustrated", "trial-03-anime",
                            "trial-04-brutalist", "trial-05-glass", "trial-06-painting",
                            "trial-07-slate"]
    for d in args:
        localise(os.path.join(REPO, d))
    print("\nDone.")
