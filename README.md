# why-not-trial1

Redesign trials for **[whynotindia.in](https://www.whynotindia.in/)** — WHYNOT Electronics Pvt Ltd, an electronics and home-appliance retail chain with 25 showrooms across the Godavari districts and Visakhapatnam, trading since 1994.

This repository is a **lab**: each trial is a complete, self-contained redesign of the same content in a different visual direction. Nothing here is deployed. Nothing here is affiliated with the company.

---

## Start here

| What | Where |
|---|---|
| **Trial index** (pick which direction you like) | [`index.html`](index.html) |
| **The audit** — what's wrong with the current site and why it costs money | [`docs/AUDIT.md`](docs/AUDIT.md) |
| **Trial 01 · "Paper & Ink"** | [`trial-01-minimal/`](trial-01-minimal/) |

### Running it

No build step, no dependencies, no package manager. Open `index.html` — or serve the folder if you want the absolute paths and WebP sources to behave exactly as they would online:

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

---

## Trial 01 · Paper & Ink

Editorial minimalism. Warm paper, real typography, hairline rules instead of cards. The design stays quiet so the facts, the addresses and the phone number can do the selling.

**Pages:** home · about · showrooms · contact · 404

### What it fixes, concretely

1. **"Find the nearest showroom" is now a job the site can do.** All 25 addresses live in one JavaScript array (`assets/js/stores.js`), with instant search by town, district or pincode, district filter chips, a result count and an empty state. Every "Directions" button opens a real `google.com/maps/search/?api=1&query=…` link — the old site's links went to `about:invalid#zClosurez` or `google.com/maps/undefined` on all 25 entries.
2. **One phone number, one place, on every page.** Header, mobile drawer, CTAs, footer, contact page — all read from the same value. The contact page also tells you whether the showroom is open *right now* and what happens after you send an enquiry.
3. **A form that does not waste your time.** Name, mobile and message are validated as you go, errors are attached to the fields with `aria-describedby` and announced with `role="alert"`, Indian mobile numbers are accepted with or without `+91`, and the success state says exactly who will call and when.
4. **Numbers that agree with each other.** 25 showrooms, 23 towns, since 27 February 1994, 32 years, 300 staff — used consistently, with "2.5 million customers served" framed as served rather than as "happy clients".
5. **Real accessibility baseline.** Skip link, single `h1`, landmarks, visible focus rings, labelled controls, keyboard-operable everything, `prefers-reduced-motion` respected, 44 px minimum tap targets.
6. **Performance treated as a feature.** Five self-hosted font faces (~113 KB, latin subset, `font-display: swap`), three images served as WebP with JPEG fallbacks (25 KB / 51 KB / 65 KB), no framework, no CDN, no analytics, no third-party embeds. Full site CSS is 32 KB uncompressed (7 KB gzipped) and the JS is 21 KB in total, loaded per page.
7. **Even the small things:** dark mode that follows the OS and remembers a choice, per-page titles and descriptions, `Store` structured data, favicons, print styles, and a 404 that offers three ways out.

### Structure

```
index.html              trial index (ink page, links to each trial)
docs/AUDIT.md           the audit of the current site
trial-01-minimal/
├── index.html          home — hero, stats, categories, "why not", brands, service, reviews
├── about.html          history timeline, founder, leadership, partners
├── stores.html         all 25 showrooms, search + district filter
├── contact.html        enquiry form, helpline, hours, service desk
├── 404.html
└── assets/
    ├── css/style.css   design tokens, layout, components (~30 KB)
    ├── js/main.js      theme, drawer, reveal, counters, copy, live open/closed state
    ├── js/stores.js    the 25 showrooms + search/filter rendering
    ├── js/contact.js   form validation and submission state
    ├── img/            3 photographs (WebP + JPEG), logo mark, favicons
    └── fonts/          5 WOFF2 faces, latin subset (Inter 400/500/600, Instrument Serif 400 regular + italic)
```

### Editing the parts you'll want to edit

| Change | File |
|---|---|
| Phone number, email, address, opening hours | `assets/js/main.js` (`OPEN_HOUR` / `CLOSE_HOUR`), plus the literal number in each page's header/footer |
| Add or remove a showroom | `assets/js/stores.js` — one object in the `STORES` array |
| Colours, type scale, spacing | `assets/css/style.css` — the `:root` token block |
| Category names and links | `trial-01-minimal/index.html`, the `#categories` list |

---

## Notes and honesty

- **The redesigns change the presentation, not the facts.** Every address, pincode, phone number, brand name and date comes from the company's own public pages, read on 12 October 2026.
- **District wording is deliberately unchanged.** Several listed towns sit in districts created by Andhra Pradesh's 2022 reorganisation, and the live site still says "East/West Godavari" everywhere. Rather than silently rewriting the company's own addresses, the trials keep their wording — see the audit, item 5.2.
- **Neither trial has a backend.** The contact form validates and shows what would happen, then says so on screen. Wiring it to a CRM, WhatsApp Business API or an email relay is an afternoon's work.
- **Two glyphs are deliberately avoided.** The latin subsets of Inter and Instrument Serif contain neither `₹` (U+20B9) nor `↗` (U+2197), so prices are written "Rs" and external arrows are inline SVG. Falling back to a system font for one character is exactly the kind of detail that makes an otherwise composed page look assembled.
- **Photography is AI-generated** as a stand-in for real showroom photography. Brand logos are not reproduced; brand names appear as text only.
- **Not affiliated** with WHYNOT Electronics Pvt Ltd. This is a portfolio/redesign exercise built from public information.

## Trials

- **01 — Paper & Ink** ✅ built
- **02 — direction to be decided** ⏳
- **03 — reserved** ⏳
