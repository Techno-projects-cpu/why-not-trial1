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
| **Trial 04 · "Slab & Stencil"** — neo-brutalism | [`trial-04-brutalist/`](trial-04-brutalist/) |
| **Trial 05 · "Glass & Glow"** — glassmorphism | [`trial-05-glass/`](trial-05-glass/) |
| **Trial 06 · "Brush & Bloom"** — pastel, painterly | [`trial-06-painting/`](trial-06-painting/) |

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

### Trials 04–06

These three share a builder (`_tools/sections.py`) and therefore share structure, copy and behaviour exactly. They differ only in design — which is the point: it makes them directly comparable, and it means a content change happens once. Trial 07 was added afterwards and deliberately breaks that pattern: sharing a skeleton across three directions is a fair criticism of 04–06, so the seventh changes the form as well as the palette.

| | **04 · Slab & Stencil** | **05 · Glass & Glow** | **06 · Brush & Bloom** |
|---|---|---|---|
| Direction | Neo-brutalism | Glassmorphism | Pastel, painterly, plein-air |
| Type | Archivo Black + Space Grotesk + Space Mono | Sora + Manrope | Fraunces + Karla |
| Surfaces | 5px black rules, hard offset shadows, zero radius | Frosted translucent sheets, 22px backdrop blur | Thin washes on cream paper, 22–30px radii, soft warm shadows |
| Colour | Electric blue, acid yellow, lime, hot pink | Violet/cyan/magenta gradient mesh on near-black | Blush, sage, sky, butter, terracotta |
| Imagery | None — block-art hero, block bands | One light study, used as a fixed backdrop | Three pastel landscape paintings |
| Icon cut | Heavy, square-capped | Hairline, rounded | Soft, with a translucent underlay |
| Signature move | The marquee strip, and a poster of stacked blocks | The measured contrast pass | Brush-stroke ribbon dividers, feathered canvas edges |
| First view | ≈159 KB | ≈168 KB | ≈321 KB (the hero painting is 148 KB of it) |
| Whole directory | 278 KB | 397 KB | 1.6 MB (three paintings × three formats) |

### Trial 07 · Slate & Rail

| | **07 · Slate & Rail** |
|---|---|
| Direction | Clean and professional: a working document, not a poster |
| Form | **Left rail on desktop, bottom tab bar on phones, table catalogue, side-panel shortlist** — a hero built from one photograph and a map of all 25 branches, no cards, no marquee |
| Type | Inter + IBM Plex Mono (figures, labels, counts) |
| Colour | Two designed palettes: slate on white, and a true dark mode (not an inversion) |
| Mode | **Light by default — white is the point** — with a switch to dark, remembered in `localStorage` and applied before first paint so there is no flash; the reader's OS setting is deliberately ignored |
| Imagery | One AI stand-in photograph of a showroom floor (AVIF + WebP + JPEG, labelled on the page) plus a hand-drawn SVG map of the 25 branches |
| Languages | English, Telugu, Hindi — 301 phrases hooked, 308 in the runtime table |
| Measured | `_tools/contrast07.py`: 30 combinations, both modes, 0 below target |
| First view | ≈336 KB uncompressed — **≈42 KB gzipped** of text (34 KB HTML, 26 KB CSS, 107 KB JS of which 66 KB is the three-language runtime, 76 KB latin type) plus a 94 KB AVIF hero |
| Whole directory | 789 KB in 23 files — one photograph in three formats, the rest CSS and SVG |

**Why the form had to change:** the first six trials are all a header, a hero and a grid of cards. That is a good default and a bad habit — a shop with 25 branches is an information problem, so Trial 07 renders the catalogue as a list you scan (item, category, specification, branches, button) and keeps the shortlist beside it as a panel. Nothing about the content changed; the skeleton did.

**Why the icon sets are shared geometry with three different pens:** 60+ hand-written SVG paths per trial is a lot of output for something that reads as a 24px silhouette. Trials 04–06 take the canonical geometry and restyle it — stroke weight, cap, join, and a translucent halo underlay for the painted cut. The *ornaments* (marquee marks, glass prisms, brush strokes) are drawn individually, because that is where the personality actually lives. All three keep the same symbol ids, so one set of JavaScript drives all of them.

---

## What both trials actually fix

1. **One true set of facts.** The current site claims 23, 25 and 40 branches on three different pages. Both trials say 25 showrooms in 23 towns — and say it once.
2. **"Find your nearest showroom" is a job the site can do.** All 25 addresses live in one JavaScript array. Search by town, district or pincode, district filter chips, result counts, an empty state that offers the helpline — and real `google.com/maps/search/?api=1&query=…` deep links that open the Maps app on a phone. (Every one of the 25 map links on the live site is broken.)
3. **A phone number one tap away, on every page,** with an honest "Open now / Closed now" state. The live contact page has no phone number at all.
4. **Products worth browsing.** Both trials ship a catalogue: 10 categories, 17 sample products, live search with a proper keyword index ("fridge" finds refrigerators, "geyser" finds the geyser), a town filter, and a shortlist that travels to the counter complete with every item written out.
5. **A page that loads in a village.** No framework, no CDN, no analytics, no tag manager, no popup, no embedded map. Readable before the fonts land, and every action works with the keyboard.
6. **Accessibility as a baseline.** Skip links, one `h1` per page, real landmarks, visible focus rings, 44 px tap targets, labelled controls, errors tied to fields with `aria-describedby` and `role="alert"`, `prefers-reduced-motion` honoured.
7. **About the money honestly.** No prices are invented for a real company's real products: cards say "Ask today's price", which is also how most Indian electronics retail actually works. Wiring a live price feed or a real cart with payment is a phase-two decision, and the shortlist already maps onto a cart item for item.

### Trial 06 specifics

- **Paintings in frames, feathered into the paper.** Each canvas is a painting inside a soft mat, with an inset cream vignette (`box-shadow: inset`) so the image edge dissolves into the page instead of stopping at a hard line. One is tilted half a degree so it reads as pinned up.
- **Canvas grain with no texture file.** A `feTurbulence` filter inlined as an SVG data URI, multiplied over the page at low opacity. Same trick gives the glass trial its grain.
- **Brush-stroke dividers**: two overlapping tapered strokes per divider, rotating through three pastel inks.
- **Caveat, stated on the page:** the three paintings are AI-generated stand-ins. Pastel landscape is the craft where a commissioned illustrator raises the ceiling most, so this is the direction where that cost belongs on the quote as its own line. Every design element around them — frames, washes, grain, dividers — is plain CSS and SVG.

### Trial 05 specifics

- **Depth from light, not borders.** A fixed backdrop (light study → colour mesh → blurred orbs → grain → dark wash) with `backdrop-filter: blur(22px) saturate(165%)` on every surface.
- **A measured contrast pass, not a vibe.** `python3 _tools/contrast.py` reads the actual alpha values out of the stylesheet, composites the real layer stack and prints WCAG ratios against the worst-case backdrop. It failed on the first run — 3 of 10 combinations — and the fixes are in the CSS: higher text alphas, a dark tint floor under every text-bearing surface, and the systemic one, that *any* translucent white chip puts white text on a near-white surface and so must carry the tint instead of just frost. **24/24 pass**, worst case included.
- **`@supports` fallback**: where `backdrop-filter` is unavailable the frost is swapped for a solid tinted sheet, so the design degrades to something readable rather than to mush.

### Trial 04 specifics

- **No photography by design.** The hero is a poster of stacked blocks; the town band is a wall of coloured slabs; the catalogue's product art is flat colour blocks with heavy icons. It is the smallest trial in the repo at 278 KB, and the loudest.
- **One marquee**, scrolling a single strip of true facts (25 showrooms, 23 towns, since 1994), disabled under `prefers-reduced-motion`.
- **Zero border radius**, everywhere, enforced in the reset — the one place a stray rounded corner would break the whole language.

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
trial-04-brutalist/                          trial-05-glass/                     trial-06-painting/
├── six pages each, built from _tools/sections.py — identical content, three designs
trial-07-slate/
├── six pages, built by _tools/build-trial07.py — rail + tab bar, table catalogue
└── assets/                style.css (light + dark tokens) · 4 scripts · i18n.js · 9 font faces
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
│
│   ── and the shared builder the last three trials use ──
├── content.py              all the words for trials 04–06, in one place
├── sections.py             the page bodies + BaseSkin (header, drawer, footer, phone bar, panels)
├── shell.py                the document shell
├── icons.py                canonical icon geometry, three cuts; <picture> helper for AVIF/WebP/JPEG
├── build-trial04.py        Skin04 — neo-brutalism
├── build-trial05.py        Skin05 — glassmorphism
├── build-trial06.py        Skin06 — pastel painting
├── port-js.py              ports the JavaScript to a new trial, renaming classes and reporting leftovers
├── contrast.py             the glassmorphism WCAG audit (parses the stylesheet, composites the layers)
│
│   ── and the three languages on all seven ──
├── i18n.py                 every phrase in English, Telugu and Hindi, plus the runtime strings
├── i18n07.py               Trial 07's own copy, in the same three languages
├── localise.py             hooks the HTML, patches the scripts, subsets the Indic faces, writes i18n.js
│                           (and refuses to write if a hook landed on the wrong element)
│
│   ── and the seventh direction ──
├── build-trial07.py        six pages: rail, tab bar, facts strip, table catalogue
├── port-js07.py            the catalogue logic, re-rendered as rows, a directory and a panel
├── contrast07.py           both Trial 07 palettes: 30 combinations against WCAG AA
└── test-trials.mjs         185 tests across all seven trials (jsdom), including the languages
```

### Editing the parts you'll want to edit

| Change | File |
|---|---|
| **Trial 02's pages** (all of them) | `_tools/build-trial02.py` — edit the page bodies there and run `python3 _tools/build-trial02.py`. Header, footer, phone bar and doodle sprite stay in sync automatically. |
| **Trial 02's icons** | `_tools/doodles.py` — then rebuild. |
| **Trial 03's pages** | `_tools/build-trial03.py` — same deal, then `python3 _tools/build-trial03.py`. |
| **Trial 03's icons and panel ornaments** | `_tools/panels.py` — crisp, geometric, with `preserveAspectRatio="none"` on the two stretchy backgrounds. |
| **Any copy in trials 04–06** | `_tools/content.py` — one file, then rebuild all three: `python3 _tools/build-trial04.py` (and 05, 06). |
| **A page's structure in trials 04–06** | `_tools/sections.py` if it is shared, the trial's own `build-trial06.py`-style skin if it is not. |
| **Trial 04–07 icons** | `_tools/icons.py` — one geometry, four cuts (`brutal`, `glass`, `paint`, `slate`). |
| **Any Telugu or Hindi copy** | `_tools/i18n.py` (all trials) and `_tools/i18n07.py` (Trial 07), then `python3 _tools/localise.py` |
| **Trial 07's pages** | `_tools/build-trial07.py` (pages) and `port-js07.py` (scripts), then `python3 _tools/localise.py trial-07-slate` |
| **Trial 07's colours, both modes** | `trial-07-slate/assets/css/style.css` — the `:root` and `html[data-mode="dark"]` token blocks, then `python3 _tools/contrast07.py` |
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

Two things exist because they were bugs first. `localise.py` verifies every hook twice: that the
insertion changed attributes and nothing else (same tag sequence, same text), and that each hook sits
on the element whose text is that phrase — an offset a character or two out still produces valid HTML,
it just hooks the wrong node. And the script patch has to be idempotent: running it twice once wrapped
its own wrapper, leaving `T("k", T("k", "English"))` in the file a customer would read, so a second
pass now has to change nothing or the build stops.

185 checks that run the real scripts against the real pages in a real DOM: 17 products render in all three skins, filters and search narrow correctly, the shortlist updates every badge and the WhatsApp and email links carry the list, all 25 map links in all three trials resolve to `google.com/maps/search`, district filters combine with search, the form rejects a bad mobile number and its success state stays honest about there being no server, Trial 03 ships AVIF with WebP behind it and declares its image dimensions, each trial uses only its own localStorage key, and the product data is byte-identical across all three. Trials 04–06 get a shared-contract block with two checks that catch design-port bugs specifically: **every class the rendered page uses must exist in that trial's stylesheet**, and every icon reference must resolve. Both found real bugs the moment they were written (a missing `[data-cat-chips]` container left the catalogue with no category filter at all, and several unstyled classes).

The language block runs on all seven trials: it switches to Telugu, checks that the nav, the button the catalogue *builds*, the result count and the shortlist panel are all in the reader's script (including text generated after a switch, which is what the DOM pass and its observer are for), switches back, and checks the choice was remembered. Trial 07 gets a mode block as well: the switch flips `data-mode`, updates `aria-pressed`, persists the choice, and both palettes are checked to define the same colour tokens — a missing token is how one mode ends up half-styled.

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

Trial 05 · Glass & Glow

| Asset | Raw | Gzipped |
|---|---|---|
| HTML, largest page | 30 KB | 7.3 KB |
| CSS, entire site | 35 KB | 7.6 KB |
| JS, all four files | 37 KB | 12 KB |
| Fonts, 3 faces | 42 KB | — |
| The light study, AVIF (WebP 24 KB, JPEG 85 KB behind it) | 23 KB | — |
| **First view** | **≈168 KB** | **≈75 KB** |

Trial 06 · Brush & Bloom

| Asset | Raw | Gzipped |
|---|---|---|
| HTML, largest page | 41 KB | 7.9 KB |
| CSS, entire site | 34 KB | 7.5 KB |
| JS, all four files | 37 KB | 12 KB |
| Fonts, 4 faces | 61 KB | — |
| Hero painting, AVIF (WebP 153 KB, JPEG 268 KB behind it) | 148 KB | — |
| **First view** | **≈321 KB** | **≈130 KB** |

Trial 07 · Slate & Rail

| Asset | Raw | Gzipped |
|---|---|---|
| HTML, largest page (sprite included) | 33.7 KB | 8.0 KB |
| CSS, both palettes, entire site | 25.7 KB | 6.0 KB |
| JS, five files (i18n.js is 66 KB of it) | 106.7 KB | 27.9 KB |
| Latin type, 4 faces | 75.9 KB | — |
| Indic type, 4 faces | 97.5 KB | downloaded only if the reader picks Telugu or Hindi |
| Hero photograph (AVIF / WebP / JPEG) | 94.1 / 83.9 / 160.6 KB | already compressed |
| **First view, English** | **≈336 KB** | **≈42 KB text, +94 KB AVIF** |

The runtime carries only this trial's copy: 166 hooked phrases plus the 35 keys its scripts look up, out of 308 in the table. Every trial ships its own slice — Trial 01's runtime is 18.3 KB on disk, Trial 07's 65.7 KB, which is the price of this design having the most copy in three languages.

Seven trials, no analytics, no tag manager, no cookie banner (nothing to consent to), no third-party requests of any kind, and no embedded Google Maps iframe — the map only opens when the visitor chooses to ask for directions.

---

## Notes and honesty

- **The redesigns change the presentation, not the facts.** Every address, pincode, phone number, brand name and date comes from the company's own public pages, read on 12 October 2026.
- **No prices were invented.** The catalogue is clearly labelled as a sample; the product types are real categories the company sells, but models, stock and prices would come from their system. Anything else would be putting fake prices on a real shop.
- **District wording is deliberately unchanged.** Several listed towns sit in districts created by Andhra Pradesh's 2022 reorganisation and the live site still says "East/West Godavari" everywhere. Rather than silently rewriting the company's own addresses, both trials keep their wording — see audit item 5.2.
- **Neither trial has a backend.** The contact forms validate properly, then say on screen that nothing was sent. Wiring them to a CRM, WhatsApp Business API or an email relay is an afternoon's work.
- **Reviews are reproduced as written** on the current site, unattributed, with a note on the page that named and dated reviews would be better. Inventing testimonials was not an option.
- **The paintings in Trial 06 and the key art in Trial 03 are AI-generated** stand-ins, and those are the two directions where bought-in artwork would change the most: pastel landscape and anime are both craft styles. Trial 01's photography is a third. Each of those is a line item worth quoting separately rather than hiding inside a build price.
- **The glassmorphism trial's contrast numbers are measured, not asserted** (`_tools/contrast.py`), because that is the one visual direction in the set where taste and readability pull against each other. Trial 07 is measured twice over for the same reason (`_tools/contrast07.py`, both modes, 30 combinations).
- **The Telugu and Hindi were written in those languages, not translated.** A literal translation of a terse English sentence reads like a telegram in Telugu, so the two blocks differ in shape — shorter, and using the words a shop in Tanuku would use. Where a phrase carries a number or a town name, the runtime patches it live ("In stock at Tanuku" becomes "స్టాక్ ఉన్నది: Tanuku").

- **Photography in Trial 01 and the key art in Trial 03 are AI-generated** stand-ins. Trial 01's would be replaced by photographs of the real showrooms; Trial 03's by commissioned illustration, which is a genuine cost worth quoting separately — anime art is a craft style and the difference between generated stand-in art and a real illustrator's work is visible. Trial 02 uses no photography or raster art at all.
- **No third-party logos or trademarks** are reproduced. Brand names appear as text only.
- **Two glyphs are deliberately avoided.** The latin subsets of these fonts contain neither `₹` (U+20B9) nor `↗` (U+2197), so prices are written "Rs" and external arrows are inline SVG. Falling back to a system font for one character is exactly the kind of detail that makes an otherwise composed page look assembled.
- **Not affiliated** with WHYNOT Electronics Pvt Ltd. This is a portfolio/redesign exercise built entirely from public information.

## Trials

- **01 — Paper & Ink** ✅ built (6 pages, catalogue)
- **02 — Crayon & Paper** ✅ built (6 pages, catalogue)
- **03 — Panel & Ink** ✅ anime / manga panels (6 pages, catalogue)
- **04 — Slab & Stencil** ✅ neo-brutalism (6 pages, catalogue)
- **05 — Glass & Glow** ✅ glassmorphism (6 pages, catalogue, measured contrast pass)
- **06 — Brush & Bloom** ✅ pastel, painterly (6 pages, catalogue, three paintings)
- **07 — Slate & Rail** ✅ clean, professional, light/dark modes, table catalogue, structurally different (6 pages, catalogue)
- **All seven** ✅ English, Telugu and Hindi, with the Telugu and Hindi written natively
- **Next, if anyone wants more** ⏳ commerce-first with a real cart and payment gateway (every trial's shortlist already maps onto a cart item for item), or a map-first build where the district map is the homepage and each of the 23 towns gets its own page for local search
