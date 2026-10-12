# why-not-trial1

Redesign trials for **[whynotindia.in](https://www.whynotindia.in/)** — WHYNOT Electronics Pvt Ltd, an electronics and home-appliance retail chain with 25 showrooms across the Godavari districts and Visakhapatnam, trading since 1994.

This repository is a **lab**: each trial is a complete, self-contained rebuild of the same content in a different visual direction, implementing the same fix-list. Nothing here is deployed. Nothing here is affiliated with the company.

---

## Start here

| What | Where |
|---|---|
| **The lab** — both trials in live desktop + phone preview boxes | [`index.html`](index.html) |
| **The audit** — what's wrong with the current site, and why it costs money | [`docs/AUDIT.md`](docs/AUDIT.md) |
| **Trial 01 · "Paper & Ink"** — minimal, editorial | [`trial-01-minimal/`](trial-01-minimal/) |
| **Trial 02 · "Crayon & Paper"** — hand-drawn, vibrant | [`trial-02-illustrated/`](trial-02-illustrated/) |

### Running it

No build step, no dependencies, no package manager:

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

Serve it rather than opening the files directly — the preview iframes, the Google Maps links and the WebP sources all behave as they would online.

---

## The two directions

Both trials cover the same six pages, the same 25 verified showroom addresses, the same sample catalogue of 17 products, and the same fix-list from the audit. Only the language changes — which is the point of building two.

| | **Trial 01 · Paper & Ink** | **Trial 02 · Crayon & Paper** |
|---|---|---|
| Direction | Editorial minimalism, warm paper, hairline rules | Hand-drawn, vibrant, sticker-and-marker |
| Type | Instrument Serif + Inter | Shantell Sans + Nunito + Caveat |
| Colour | Ink on paper, one brand blue `#0000FF` | Marker yellow, coral, teal, violet, sky |
| Icons | None — typography does the work | 37 hand-written SVG doodle paths |
| Dark mode | Yes (follows the OS, remembers your choice) | No — the paper is the point |
| Mobile | Mobile-first, sticky header | Mobile-first, plus a sticky phone action bar (Call · Showrooms · My list) |
| Buying | Enquiry + shortlist sent by WhatsApp, email or phone | Same, with WhatsApp as the primary route |
| First view | ≈165 KB uncompressed (≈60 KB over the wire) | ≈160 KB uncompressed (≈50 KB over the wire) |

---

## What both trials actually fix

1. **One true set of facts.** The current site claims 23, 25 and 40 branches on three different pages. Both trials say 25 showrooms in 23 towns — and say it once.
2. **"Find your nearest showroom" is a job the site can do.** All 25 addresses live in one JavaScript array. Search by town, district or pincode, district filter chips, result counts, an empty state that offers the helpline — and real `google.com/maps/search/?api=1&query=…` deep links that open the Maps app on a phone. (Every one of the 25 map links on the live site is broken.)
3. **A phone number one tap away, on every page,** with an honest "Open now / Closed now" state. The live contact page has no phone number at all.
4. **Products worth browsing.** Both trials ship a catalogue: 10 categories, 17 sample products, live search with a proper keyword index ("fridge" finds refrigerators, "geyser" finds the geyser), a town filter, and a shortlist that travels to the counter complete with every item written out.
5. **A page that loads in a village.** No framework, no CDN, no analytics, no tag manager, no popup, no embedded map. Readable before the fonts land, and every action works with the keyboard.
6. **Accessibility as a baseline.** Skip links, one `h1` per page, real landmarks, visible focus rings, 44 px tap targets, labelled controls, errors tied to fields with `aria-describedby` and `role="alert"`, `prefers-reduced-motion` honoured.
7. **About the money honestly.** No prices are invented for a real company's real products: cards say "Ask today's price", which is also how most Indian electronics retail actually works. Wiring a live price feed or a real cart with payment is a phase-two decision, and the shortlist already maps onto a cart item for item.

### Trial 02 specifics

- **Every icon is a path someone wrote by hand** — no icon font, no sprite CDN, no stock glyphs. They live in [`_tools/doodles.py`](_tools/doodles.py) and are inlined as an SVG sprite in each page, so the whole set costs zero extra requests.
- **The hero illustration** (a wobbly shop front with a TV, a fridge, an AC and a waving person) is drawn in the same file.
- **No photographs at all.** The only raster files in the trial are two favicons; everything else is SVG, CSS gradients and type.
- **A sticky phone action bar** — Call · Showrooms · My list — because on a phone that is the whole journey.

---

## Structure

```
index.html                  the lab: both trials in live desktop + phone preview boxes
docs/AUDIT.md               audit of the current site, severity-ranked, with the fix-list
_tools/
├── doodles.py              Trial 02's 37 hand-drawn icons + the hero illustration
├── build-trial02.py        regenerates Trial 02's six pages from the templates
└── test-trials.mjs         45 behavioural tests for both trials (jsdom)
trial-01-minimal/
├── index.html              hero, stats, categories, popular, "why not", brands, service, reviews
├── products.html           catalogue, filters, my list, how buying works
├── stores.html             all 25 showrooms, search + district filter
├── about.html              history timeline, founder, leadership, partners
├── contact.html            enquiry form, helpline, hours, service desk
├── 404.html
└── assets/                 style.css (~32 KB) · 4 scripts · 3 photographs · 5 font faces
trial-02-illustrated/
├── index.html              illustrated hero, category tiles, popular, "why not", brands, reviews
├── products.html           catalogue, filters, my list, how buying works
├── stores.html             all 25 showrooms
├── about.html              sticky-note timeline, founder, leadership, partners
├── contact.html            enquiry form, WhatsApp, dealer enquiries
├── 404.html
└── assets/                 style.css (~30 KB) · 4 scripts · doodle sprite · 5 font faces
```

### Editing the parts you'll want to edit

| Change | File |
|---|---|
| **Trial 02's pages** (all of them) | `_tools/build-trial02.py` — edit the page bodies there and run `python3 _tools/build-trial02.py`. Header, footer, phone bar and doodle sprite stay in sync automatically. |
| **Trial 02's icons** | `_tools/doodles.py` — then rebuild. |
| Add or remove a showroom | `assets/js/stores.js` in either trial — one object in the `STORES` array |
| Add or edit a product | `assets/js/products.js` in either trial — one object in `PRODUCTS` (keep the two files' data blocks identical; the test suite checks that they are) |
| Phone number, email, address, opening hours | `assets/js/main.js` (`OPEN_HOUR` / `CLOSE_HOUR`) plus the literal number in each page's header and footer |
| Colours, type scale, spacing | `assets/css/style.css` — the `:root` token block |
| Trial 02's hand-drawn borders | The `--wobble-a/b/c` tokens: uneven corner radii are what make a box look drawn rather than generated |

---

## Tests

```bash
cd _tools && npm install jsdom && node test-trials.mjs
```

45 checks that run the real scripts against the real pages in a real DOM: 17 products render in both skins, filters and search narrow correctly, the shortlist updates every badge and both WhatsApp and email links carry the list, all 25 map links resolve to `google.com/maps/search`, district filters combine with search, the form rejects a bad mobile number and its success state stays honest about there being no server, and the two trials keep separate localStorage keys so Trial 01's list can't leak into Trial 02's.

---

## Performance budgets (measured, not estimated)

**Trial 01 · Paper & Ink**

| Asset | Raw | Gzipped |
|---|---|---|
| HTML, largest page | 33 KB | 6.6 KB |
| CSS, entire site | 32 KB | 7.3 KB |
| JS, all four files | 28 KB | 9 KB |
| Fonts, 5 faces (latin subset) | 113 KB | — |
| Images: 3 photographs (WebP), 3 icons | 141 KB | — |
| **First view** | **≈165 KB** | **≈60 KB** |

**Trial 02 · Crayon & Paper**

| Asset | Raw | Gzipped |
|---|---|---|
| HTML, largest page (includes the 37-icon sprite) | 36 KB | 8.8 KB |
| CSS, entire site | 31 KB | 6.9 KB |
| JS, all four files | 37 KB | 12 KB |
| Fonts, 5 faces across 3 families | 174 KB | — |
| Images: 2 favicons, everything else is SVG | 4 KB | — |
| **First view** | **≈160 KB** | **≈50 KB** |

Both trials: no analytics, no tag manager, no cookie banner (nothing to consent to), no third-party requests of any kind, and no embedded Google Maps iframe — the map only opens when the visitor chooses to ask for directions.

---

## Notes and honesty

- **The redesigns change the presentation, not the facts.** Every address, pincode, phone number, brand name and date comes from the company's own public pages, read on 12 October 2026.
- **No prices were invented.** The catalogue is clearly labelled as a sample; the product types are real categories the company sells, but models, stock and prices would come from their system. Anything else would be putting fake prices on a real shop.
- **District wording is deliberately unchanged.** Several listed towns sit in districts created by Andhra Pradesh's 2022 reorganisation and the live site still says "East/West Godavari" everywhere. Rather than silently rewriting the company's own addresses, both trials keep their wording — see audit item 5.2.
- **Neither trial has a backend.** The contact forms validate properly, then say on screen that nothing was sent. Wiring them to a CRM, WhatsApp Business API or an email relay is an afternoon's work.
- **Reviews are reproduced as written** on the current site, unattributed, with a note on the page that named and dated reviews would be better. Inventing testimonials was not an option.
- **Photography in Trial 01 is AI-generated** stand-in imagery for photography that would be shot in the real showrooms. Trial 02 uses no photography at all.
- **No third-party logos or trademarks** are reproduced. Brand names appear as text only.
- **Two glyphs are deliberately avoided.** The latin subsets of these fonts contain neither `₹` (U+20B9) nor `↗` (U+2197), so prices are written "Rs" and external arrows are inline SVG. Falling back to a system font for one character is exactly the kind of detail that makes an otherwise composed page look assembled.
- **Not affiliated** with WHYNOT Electronics Pvt Ltd. This is a portfolio/redesign exercise built entirely from public information.

## Trials

- **01 — Paper & Ink** ✅ built (6 pages, catalogue)
- **02 — Crayon & Paper** ✅ built (6 pages, catalogue)
- **03 / 04 — reserved** ⏳ commerce-first, map-first / hyper-local, or dark & cinematic
