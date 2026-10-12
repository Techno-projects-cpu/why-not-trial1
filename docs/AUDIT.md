# WHYNOT — website audit & redesign brief

**Site reviewed:** [whynotindia.in](https://www.whynotindia.in/)
**Reviewed on:** 12 October 2026
**Reviewed by:** redesign trial project (independent concept work)
**Method:** the public site was read page by page — home, `/about`, `/stores`, `/contact`, two category pages (`/c/16/QLED`, `/c/5/REFRIGERATOR`, `/c/12/Mobiles`), one brand page (`/b/4/SAMSUNG`), `/robots.txt`, `/sitemap.xml` and a guessed `/branches`. Findings below are things **visible in the rendered pages**; nothing was tested behind a login, in their admin panel, or against their server.

---

## 1. The short version

The business is genuinely impressive — 25 showrooms in 23 towns, 300 employees, every major brand, 32 years of trading. The website actively undersells all of it. Five problems matter more than the rest:

| # | Problem | Why it costs money |
|---|---|---|
| 1 | **The site says it is three different sizes of company.** Home page: "23 Cities · 25 Branches". About page: "40 branches across 36 locations". Stores page: 25 entries, three of which are the same building (the flagship, LG Best Shop and Samsung Smart Plaza). | A customer comparing you to a big-box store reads three numbers and concludes nobody is minding the shop. Inconsistency is the fastest way to look untrustworthy. |
| 2 | **"Open in Maps" is broken on every single showroom.** 23 of the 25 links go to `about:invalid#zClosurez`, the other 2 to `google.com/maps/undefined` — not one of them works. The branch list at `/branches` 404s as well. | The one action a local retail site exists to perform — "get me there" — does not work. Every customer who taps it lands on nothing. |
| 3 | **The contact page has no phone number, no address, no hours and no shop state.** It is a form, and the helpline `8886222448` is buried in a paragraph on a different page. Nothing tells a visitor whether the shop is open right now. | People who are ready to buy are asked to fill a form and hope. Most of them close the tab and call whichever showroom they can find on Google Maps instead. |
| 4 | **The product pages are empty.** `/c/5/REFRIGERATOR` returns a logo, a "Shopping Cart" link and one large PNG. `/b/4/SAMSUNG` returns a logo and a cart link — nothing else. | There is a shopping cart in the navigation and nothing to put in it. That is worse than not having one: it tells the visitor the site is unfinished. |
| 5 | **The homepage still sells last Ugadi.** A popup loads six festival banner images named `ugadi1.jpg … ugadi4.jpg`, plus a "One Launch event live streaming" link to YouTube with asterisks around it (`****One Launch event live streaming****`). | A dated popup on arrival is the first thing a first-time visitor experiences. It is now October, and the offer is from a different season. |

---

## 2. Everything found, by category

Severity: **S1** = fix this week, **S2** = fix this quarter, **S3** = hygiene.

### Trust & credibility
- **S1 — Contradictory company facts.** Three different branch counts (23 / 25 / 40) and three different locations (23 stated, 36 claimed, 23 listed). Pick one set of numbers and put them in one file that every page reads.
- **S1 — Stats nobody can check.** "2.5 Million Happy Clients", "1 Million Products Sold", "23 Cities", "25 Branches" sit next to each other in four different type sizes with no source, no date and no definition. "Happy clients" is not a metric a customer believes. "32 years", "300 employees", "25 showrooms", "since 27 February 1994" are believable because they are specific.
- **S1 — Unattributed testimonials under a misspelled heading.** The section is titled *"Testmonials"*. Three quotes, no names, no town, no date, no platform, no photo. Reviews with a first name, a town and a date ("Ravi K., Bhimavaram — Google, March 2026") do far more work than a quote signed "customer".
- **S2 — Three showrooms share one address.** Tanuku, "LG Best Shop" and "Samsung Smart Plaza" all list *RS No 24/1, Ground and Cellar, Sri Sowdha Towers, Undrajavaram Road, Tanuku*. Legitimately they are brand shops inside one building — but the page presents them as three unexplained showrooms, which muddles the count and tells a visitor nothing about which one to walk into.
- **S2 — Copy quality.** "catering to the needs of entire Godavari and some parts of Visakhapatnam Districts.Since its inception" (no space after the full stop), "makingus deliver the right product", "VACCUM CLEANER", "Mitusubishi", "whirpool" — some of these are in the visible nav, not just the code. Every typo is a small withdrawal from a trust account that a 32-year-old business has been paying into.
- **S2 — No pricemark for hygiene.** No price, no EMI/`₹`, no offer section that isn't a popup image, no stock indication, no "in stock at Bhimavaram". For durable goods in tier-3 markets, EMI and exchange value are the questions people actually ask.
- **S3 — Corporate evolution is buried.** The 27 Feb 2025 incorporation into *WHYNOT Electronics Pvt Ltd*, the leadership team, and the brand-partner list are all sitting in a wall of untitled paragraphs on `/about`. This is good material that reads like a legal notice.

### Navigation & user journey
- **S1 — `/branches` 404s.** The error page is pleasant, which makes it worse: the visitor is told "sorry, we couldn't find the page you where looking for" — with a typo *in the error message* — and there is no branch directory anywhere in the main navigation until you find `/stores`.
- **S1 — No "find my nearest showroom" path.** The single most useful feature for a chain in 23 towns is missing: search by town, district or pincode. Today, the visitor scrolls a long page of 25 cards with blank map tiles and broken map links.
- **S2 — A "Shopping Cart" that cannot be used.** Present in the header of every page. There is no product to add and no checkout behind it. Either build it or remove it.
- **S2 — Empty category pages are dead ends.** `/c/12/Mobiles` gives a visitor a heading and a cart link. No products, no "call this branch for stock", no alternative.
- **S2 — No search anywhere on the site.**

### Performance & technical quality
- **S1 — Image strategy is "upload the original".** The homepage references dozens of banner images from one folder — every URL a legacy format (`.jpg`, `.jpeg`, even a `.PNG`), every one of them part of the initial page rather than one image that changes, and no sized variants anywhere in those URLs (nothing like `-800w` or `@2x` that would let a phone take a smaller file). No image CDN is involved. The two symptoms a visitor feels are the lag on first load and the layout shifting while the banners arrive.
- **S2 — No `robots.txt` and no `sitemap.xml`.** Both URLs fall through to the HTML error page. Search engines get no sitemap, no crawl guidance.
- **S2 — Rendering depends on JavaScript.** Category and brand pages return almost no content in the HTML; if the scripts fail, the page is blank. Good for crawlers? No. Good on a slow 4G phone in a village? Also no.
- **S2 — No structured data.** No `LocalBusiness` / `Store` schema, so Google has to guess your address, phone, hours, and cannot show a rich result for any of the 25 branches.
- **S3 — 404 page is a dead end for SEO** (soft handling, no suggestions beyond "Go to Homepage").

### Accessibility & inclusive design
- **S2 — Contrast and type size.** Long-form body copy sits in grey at small sizes against light backgrounds; where blue `#0000FF` is used on white for links and labels, contrast is technically passable in places and uncomfortable in others. The brand blue should be reserved for large text and graphics, or paired with white.
- **S2 — Interactive elements with no accessible name.** Icon-only controls (cart, popups) and the map tiles have no text alternative; the map iframe tiles are pure images with no label.
- **S2 — No visible focus styling to speak of, no skip link, no landmarks.** Keyboard users get lost in a page that is one long scroll.
- **S3 — Popup on load.** Modals that open themselves are hostile to screen readers and to anyone on a slow connection; they also hurt Core Web Vitals.

### SEO & findability
- **S2 — Local SEO is basically switched off.** One title tag (`Electronics Showrooms Andhra Pradesh - Why Not Electronics`) repeated across every page, no branch-specific pages, no hours, no pincode-level targeting. "electronics showroom in Bhimavaram" is a search a WHYNOT branch should own outright and currently cannot win.
- **S2 — No per-page titles/descriptions.** Every page shares the homepage title, so Google sees one page repeated.
- **S3 — Category URLs are duplicated as image-only pages** (`/c/5/REFRIGERATOR`) with no crawlable content behind them.

---

## 3. What a redesign actually has to fix

Not a paint job. In priority order:

1. **One true set of facts.** Branch count, founding year, employee count, customer count — defined once, used everywhere, agreed with the client before a line of code is written.
2. **The nearest-showroom job.** Search + district filter + real Google Maps links + a phone number that matches the branch.
3. **A phone number that is one tap away, on every page.** Including a plain statement of opening hours.
4. **Honest, specific proof** instead of round numbers: years in business, towns, brands, real reviews with attribution.
5. **A page that loads on a 4G phone in a village**, because that is where most of the customers are. Budget: under 250 KB of critical assets, no render-blocking third parties, no autoplaying carousel of 50 originals.
6. **Retire what cannot be maintained.** A popup carousel that still advertises Ugadi, and a cart with no products, cost more in credibility than they return in sales — unless someone is going to own them every week.

---

## 4. What this trial (Trial 01 · "Paper & Ink") demonstrates

A deliberately minimal counter-argument to the current site. Same facts, same brand blue `#0000FF`, nothing decorative:

- **Whole site in one screen of CSS + two small scripts.** No framework, no build step, no jQuery, no CDN.
- **Typography done properly.** Two self-hosted families, five faces total: Instrument Serif (regular + italic) for the big statements, Inter (400/500/600) for interface text. Total font payload ≈ 113 KB, latin subset only, `font-display: swap`, so text paints immediately.
- **Images budgeted like money.** Three photographs, each served as WebP with a JPEG fallback, sized to the layout: 25 KB + 51 KB + 65 KB. The old hero alone ships tens of originals.
- **A showroom directory that is actually a directory.** 25 addresses in one data array, instant client-side search by town/district/pincode, district chips, correct `google.com/maps/search/?api=1&query=` deep links (they open the Maps app on a phone and the browser on a desktop — no API key, no broken `about:invalid` links).
- **Accessibility as a baseline, not a feature.** Skip link, one `h1` per page, real landmarks, visible focus rings, labelled search, `role="alert"` errors tied to inputs with `aria-describedby`, keyboard-operable everything, `prefers-reduced-motion` honoured.
- **Dark mode that respects the OS** and remembers an explicit choice — using the same two colours.
- **One place for every fact.** Change the phone number once; it changes in the header, drawer, CTA, footer, contact page and schema.
- **SEO basics done once:** unique title + description + canonical per page, OG tags, `Store` structured data, favicons, theme colour.

### Performance budget (this trial)

| Asset | Weight |
|---|---|
| HTML (largest page) | 33 KB uncompressed, 6.6 KB gzipped |
| CSS, entire site | 32 KB uncompressed, 7.3 KB gzipped |
| Fonts, five faces | ~113 KB (WOFF2, latin subset, three preloaded) |
| Images, all three, WebP | 139 KB (25 / 52 / 66 — only the first loads before the fold) |
| JavaScript | 21 KB across the site (16 KB on the heaviest page), no dependencies |
| **First view** | **≈165 KB uncompressed, ≈60 KB over the wire — and text is readable before the fonts land** |

No analytics, no tag manager, no cookie banner, no embedded Google Maps iframe (the map only loads when the visitor *chooses* to open directions), no web fonts from a third-party CDN, and therefore no consent-banner debt.

---

## 5. What I would ask the client for

To turn a trial into their site:

1. **One verified fact sheet** — branch count, locations, opening hours per branch (they differ), staff count, founding date, and the real review sources.
2. **Confirm the district naming.** Several listed pincodes/towns are in districts created by Andhra Pradesh's 2022 reorganisation; the current site still says "East/West Godavari" throughout, and I have kept the client's own wording rather than silently rewording their addresses.
3. **Named, dated reviews** with permission to publish — or a link to their Google Business profiles.
4. **Real photography** of the actual showrooms, staff and service work. The current site's banner stack is stock-style festival art; a real photograph of a real showroom in Rajahmundry outperforms it.
5. **Analytics access** (even 30 days of it) — the redesign should be judged on enquiries and calls, not on looks.
6. **Brand rules** if any exist: the logo lockup, the exact blue, the "We drive the change" tagline, permitted usages.
7. **A decision on commerce:** is this site a shop, or a catalogue-plus-phone-call? Both are fine. Currently it is a shop with no products, which is the one option that helps nobody.

---

## 6. Verdict

The old site is not sabotaged, it is **unfinished and unmaintained**, and those two things show up in ways customers notice immediately: a cart with nothing in it, a popup from last festival, a map link that opens nothing, a contact page with no phone number, and a company that says it has 23, 25 and 40 branches depending on which paragraph you read.

None of that needs a bigger team to fix. It needs fewer promises, one source of truth, and a site that loads before the customer changes their mind.

---

### Honestly, what this audit is not

- No Lighthouse / PageSpeed run was possible from this environment, so the performance section is based on what is in the markup (image counts, formats and URLs, third-party embeds, script dependencies) rather than field measurements. A tag like `srcset` or `loading` would not have survived the plain-text reading of those pages, so it is not claimed here either way. A real engagement starts by running those on the live site.
- Server behaviour (response codes, caching headers, compression, redirects) could not be verified — `/robots.txt` and `/sitemap.xml` were observed not to return those files, but the HTTP status behind them was not tested.
- No conversion data exists, so every "why it costs money" claim is reasoning from retail fundamentals, not measured revenue. The client's Analytics would settle it in an afternoon.
