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
| **Trial 03 · "Panel & Ink"** — anime / manga panels | [`trial-03-anime/`](trial-03-anime/) |

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

| | **01 · Paper & Ink** | **02 · Crayon & Paper** | **03 · Panel & Ink** |
|---|---|---|---|
| Direction | Editorial minimalism, warm paper, hairline rules | Hand-drawn, vibrant, sticker-and-marker | Anime / manga panels: ruled frames, screentones, speed lines |
| Type | Instrument Serif + Inter | Shantell Sans + Nunito + Caveat | Anton + Zen Kaku Gothic New + Plus Jakarta |
| Colour | Ink on paper, one brand blue `#0000FF` | Marker yellow, coral, teal, violet, sky | Indigo ink, magenta, cyan, gold — cel-shaded key art |
| Icons | None — typography does the work | 37 hand-drawn wobble-line doodles | 40 crisp geometric line icons |
| Borders | Hairlines | Wobbling pen lines (uneven corner radii) | Ruled panels, 3–4 px ink, hard offset shadows |
| Dark mode | Yes (follows the OS, remembers your choice) | No — the paper is the point | No — the hero is the dark panel |
| Mobile | Mobile-first, sticky header | Mobile-first + sticky phone action bar | Mobile-first + sticky phone action bar |
| Images | 3 photographs (WebP + JPEG) | None — all SVG | 2 cel-shaded illustrations (AVIF + WebP + JPEG) |
| First view | ≈165 KB uncompressed | ≈160 KB uncompressed | ≈250 KB uncompressed, of which 72 KB is the hero art |

The third direction is the interesting one to compare against the first two: same grid discipline as Trial 01, same energy budget as Trial 02, and the art budget blown on exactly two images instead of three photographs.

---

## What both trials actually fix

1. **One true set of facts.** The current site claims 23, 25 and 40 branches on three different pages. Both trials say 25 showrooms in 23 towns — and say it once.
2. **"Find your nearest showroom" is a job the site can do.** All 25 addresses live in one JavaScript array. Search by town, district or pincode, district filter chips, result counts, an empty state that offers the helpline — and real `google.com/maps/search/?api=1&query=…` deep links that open the Maps app on a phone. (Every one of the 25 map links on the live site is broken.)
3. **A phone number one tap away, on every page,** with an honest "Open now / Closed now" state. The live contact page has no phone number at all.
4. **Products worth browsing.** Both trials ship a catalogue: 10 categories, 17 sample products, live search with a proper keyword index ("fridge" finds refrigerators, "geyser" finds the geyser), a town filter, and a shortlist that travels to the counter complete with every item written out.
5. **A page that loads in a village.** No framework, no CDN, no analytics, no tag manager, no popup, no embedded map. Readable before the fonts land, and every action works with the keyboard.
6. **Accessibility as a baseline.** Skip links, one `h1` per page, real landmarks, visible focus rings, 44 px tap targets, labelled controls, errors tied to fields with `aria-describedby` and `role="alert"`, `prefers-reduced-motion` honoured.
7. **About the money honestly.** No prices are invented for a real company's real products: cards say "Ask today's price", which is also how most Indian electronics retail actually works. Wiring a live price feed or a real cart with payment is a phase-two decision, and the shortlist already maps onto a cart item for item.

### Trial 03 specifics

- **The rule that keeps it from becoming a sticker album:** the page is a grid of ruled panels. Energy — speed lines, halftone, bursts — is spent in exactly four places: the hero, section titles, price tags and the CTA. Everything else stays flat white, so the catalogue is still readable on a 360 px phone.
- **Halftone everywhere, drawn in CSS.** Screentone dots are a `radial-gradient` repeated at 7–9 px; there is no texture image in the repo.
- **AVIF, WebP and JPEG** for both illustrations, built with Pillow. The hero drops from 161 KB (JPEG) to 72 KB (AVIF) — on a site whose whole argument is "loads on a village 4G connection", that is the difference that matters.
- **Kickers are speech bubbles**, section titles are outlined or knocked out of a solid block, and the impact badge is a 16-point manga star.
- **Two AI-generated key visuals.** Anime is a style where the craft shows, so this is the one trial where a commissioned illustrator would clearly beat what is in the repo — worth saying out loud to a client, and it is on the page itself too.

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
trial-03-anime/
├── index.html              dark hero panel + key art, stats strip, categories, popular, art band, reviews, CTA
├── products.html           catalogue, filters, my list, how buying works
├── stores.html             all 25 showrooms
├── about.html              six-panel timeline, founder, leadership, partners
├── contact.html            enquiry form, WhatsApp, dealer enquiries
├── 404.html
└── assets/                 style.css (~34 KB) · 4 scripts · icon sprite · 4 font faces · 2 illustrations × 3 formats
_tools/
├── doodles.py              Trial 02's 37 hand-drawn icons + the hero illustration
├── panels.py               Trial 03's 40 crisp icons, speed lines, bursts and the impact badge
├── build-trial02.py        regenerates Trial 02's six pages
├── build-trial03.py        regenerates Trial 03's six pages
└── test-trials.mjs         66 behavioural tests across all three trials (jsdom)
```

### Editing the parts you'll want to edit

| Change | File |
|---|---|
| **Trial 02's pages** (all of them) | `_tools/build-trial02.py` — edit the page bodies there and run `python3 _tools/build-trial02.py`. Header, footer, phone bar and doodle sprite stay in sync automatically. |
| **Trial 02's icons** | `_tools/doodles.py` — then rebuild. |
| **Trial 03's pages** | `_tools/build-trial03.py` — same deal, then `python3 _tools/build-trial03.py`. |
| **Trial 03's icons and panel ornaments** | `_tools/panels.py` — crisp, geometric, with `preserveAspectRatio="none"` on the two stretchy backgrounds. |
| Add or remove a showroom | `assets/js/stores.js` in either trial — one object in the `STORES` array |
| Add or edit a product | `assets/js/products.js` in any trial — one object in `PRODUCTS` (keep the three files' data blocks identical; the test suite asserts that they are) |
| Phone number, email, address, opening hours | `assets/js/main.js` (`OPEN_HOUR` / `CLOSE_HOUR`) plus the literal number in each page's header and footer |
| Colours, type scale, spacing | `assets/css/style.css` — the `:root` token block |
| Trial 02's hand-drawn borders | The `--wobble-a/b/c` tokens: uneven corner radii are what make a box look drawn rather than generated |

---

## Tests

```bash
cd _tools && npm install jsdom && node test-trials.mjs
```

66 checks that run the real scripts against the real pages in a real DOM: 17 products render in all three skins, filters and search narrow correctly, the shortlist updates every badge and the WhatsApp and email links carry the list, all 25 map links in all three trials resolve to `google.com/maps/search`, district filters combine with search, the form rejects a bad mobile number and its success state stays honest about there being no server, Trial 03 ships AVIF with WebP behind it and declares its image dimensions, each trial uses only its own localStorage key, and the product data is byte-identical across all three.

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

**Trial 03 · Panel & Ink**

| Asset | Raw | Gzipped |
|---|---|---|
| HTML, largest page (includes the 40-icon sprite) | 33 KB | 7.9 KB |
| CSS, entire site | 34 KB | 7.3 KB |
| JS, all four files | 37 KB | 12 KB |
| Fonts, 4 faces across 3 families | 49 KB | — |
| Hero illustration, AVIF (WebP 91 KB, JPEG 161 KB behind it) | 72 KB | — |
| **First view** | **≈250 KB** | **≈105 KB** |

All three trials: no analytics, no tag manager, no cookie banner (nothing to consent to), no third-party requests of any kind, and no embedded Google Maps iframe — the map only opens when the visitor chooses to ask for directions.

---

## Notes and honesty

- **The redesigns change the presentation, not the facts.** Every address, pincode, phone number, brand name and date comes from the company's own public pages, read on 12 October 2026.
- **No prices were invented.** The catalogue is clearly labelled as a sample; the product types are real categories the company sells, but models, stock and prices would come from their system. Anything else would be putting fake prices on a real shop.
- **District wording is deliberately unchanged.** Several listed towns sit in districts created by Andhra Pradesh's 2022 reorganisation and the live site still says "East/West Godavari" everywhere. Rather than silently rewriting the company's own addresses, both trials keep their wording — see audit item 5.2.
- **Neither trial has a backend.** The contact forms validate properly, then say on screen that nothing was sent. Wiring them to a CRM, WhatsApp Business API or an email relay is an afternoon's work.
- **Reviews are reproduced as written** on the current site, unattributed, with a note on the page that named and dated reviews would be better. Inventing testimonials was not an option.
- **Photography in Trial 01 and the key art in Trial 03 are AI-generated** stand-ins. Trial 01's would be replaced by photographs of the real showrooms; Trial 03's by commissioned illustration, which is a genuine cost worth quoting separately — anime art is a craft style and the difference between generated stand-in art and a real illustrator's work is visible. Trial 02 uses no photography or raster art at all.
- **No third-party logos or trademarks** are reproduced. Brand names appear as text only.
- **Two glyphs are deliberately avoided.** The latin subsets of these fonts contain neither `₹` (U+20B9) nor `↗` (U+2197), so prices are written "Rs" and external arrows are inline SVG. Falling back to a system font for one character is exactly the kind of detail that makes an otherwise composed page look assembled.
- **Not affiliated** with WHYNOT Electronics Pvt Ltd. This is a portfolio/redesign exercise built entirely from public information.

## Trials

- **01 — Paper & Ink** ✅ built (6 pages, catalogue)
- **02 — Crayon & Paper** ✅ built (6 pages, catalogue)
- **03 — Panel & Ink** ✅ built (6 pages, catalogue)
- **04 — glassmorphism** ⏳ queued
- **05 — reserved** ⏳ commerce-first or map-first / hyper-local
