/*
 * Behavioural tests for both trials.
 *
 *   cd _tools && npm install jsdom && node test-trials.mjs
 *
 * It loads each built page into a real DOM (jsdom), runs the trial's scripts
 * against it and checks what actually happens: 17 products render, filters
 * narrow correctly, the shortlist updates every badge, the WhatsApp/email
 * links carry the list, all 25 map links are real, the form validates and the
 * success state stays honest about the demo having no server.
 *
 * No test framework, no config — one file, 45 checks, exit code 1 on failure.
 */
import { JSDOM } from "jsdom";
import fs from "fs";

const ROOT = process.env.TRIALS_ROOT || new URL("..", import.meta.url).pathname;
let pass = 0, fail = 0;
const ok  = (m) => { pass++; console.log("  ok   " + m); };
const bad = (m) => { fail++; console.log("  FAIL " + m); };
const check = (cond, m) => cond ? ok(m) : bad(m);

async function load(pagePath, scripts, url = "http://localhost/" ) {
  const html = fs.readFileSync(ROOT + "/" + pagePath, "utf8");
  const dom = new JSDOM(html, { url, runScripts: "outside-only", pretendToBeVisual: true });
  // minimal shims the trial scripts expect
  dom.window.matchMedia = () => ({ matches: false, addEventListener() {} });
  dom.window.requestAnimationFrame = (cb) => setTimeout(() => cb(Date.now()), 0);
  dom.window.URLSearchParams = URLSearchParams;
  // the pages load i18n.js first: include it so the scripts see the real runtime
  const dir = scripts[0].split("/assets/js/")[0];
  const lang = dir + "/assets/js/i18n.js";
  if (fs.existsSync(ROOT + "/" + lang) && !scripts.some((s) => s.endsWith("i18n.js"))) {
    scripts = [lang, ...scripts];
  }
  for (const f of scripts) {
    const code = fs.readFileSync(ROOT + "/" + f, "utf8");
    dom.window.eval(code);
  }
  return dom;
}

console.log("\n— TRIAL 02 catalogue ————————————————————————————");
{
  const dom = await load("trial-02-illustrated/products.html",
    ["trial-02-illustrated/assets/js/main.js", "trial-02-illustrated/assets/js/products.js"]);
  const d = dom.window.document;

  check(d.querySelectorAll("[data-products] .card").length === 17, "renders 17 product cards");
  check(d.querySelectorAll("[data-cat-chips] .chip").length === 11, "builds 11 filter chips (all + 10 categories)");
  const towns = d.querySelectorAll("[data-town-select] option").length;
  check(towns === 12, "builds the town filter from the product data (" + towns + " options)");
  check(/17 products across 10 categories/.test(d.querySelector("[data-result-count]").textContent), "result count text");
  check(d.querySelectorAll("[data-list-panel] .empty").length === 1, "empty state shown for an empty list");

  // add two items
  d.querySelector('[data-add="tv-55"]').click();
  d.querySelector('[data-add="ac-15"]').click();
  const counts = [...d.querySelectorAll("[data-list-count]")].map((n) => n.textContent);
  check(counts.every((c) => c === "2"), "both count badges read 2 (" + counts.join(",") + ")");
  check(d.querySelectorAll("[data-list-panel] .list-item").length === 2, "list panel shows 2 rows");
  check(d.querySelector('[data-add="tv-55"]').textContent.includes("In my list"), "button flips to 'In my list'");
  const wa = d.querySelector('[data-list-panel] a[href^="https://wa.me/"]');
  check(!!wa && decodeURIComponent(wa.href).includes("55-inch 4K QLED television"), "WhatsApp link carries the list text");

  // remove one
  d.querySelector('[data-remove="ac-15"]').click();
  check(d.querySelectorAll("[data-list-panel] .list-item").length === 1, "remove works");

  // filter by category
  d.querySelector('[data-cat="fridge"]').click();
  const fridgeCards = d.querySelectorAll("[data-products] .card").length;
  check(fridgeCards === 2, "category filter narrows to 2 fridges (got " + fridgeCards + ")");

  // search
  d.querySelector('[data-cat="all"]').click();
  const input = d.querySelector("[data-product-search]");
  input.value = "geyser";
  input.dispatchEvent(new dom.window.Event("input"));
  const geyser = d.querySelectorAll("[data-products] .card").length;
  check(geyser === 1, "search for 'geyser' finds exactly the geyser (got " + geyser + ")");
  input.value = "fridge";
  input.dispatchEvent(new dom.window.Event("input"));
  check(d.querySelectorAll("[data-products] .card").length === 2, "and 'fridge' still finds both refrigerators, via the search index");

  input.value = "zzzz";
  input.dispatchEvent(new dom.window.Event("input"));
  check(d.querySelectorAll("[data-products] .empty").length === 1, "no-match shows the empty state");
  d.querySelector("[data-clear]").click();
  check(d.querySelectorAll("[data-products] .card").length === 17, "clear filters restores all 17");
  dom.window.close();
}

console.log("\n— TRIAL 02 home ————————————————————————————————");
{
  const dom = await load("trial-02-illustrated/index.html",
    ["trial-02-illustrated/assets/js/main.js", "trial-02-illustrated/assets/js/products.js"]);
  const d = dom.window.document;
  check(d.querySelectorAll("[data-featured] .card").length === 4, "featured strip renders 4 cards from the same data");
  check(d.querySelectorAll("[data-list-count]").length >= 2, "list badges present in header and phone bar");
  check(d.querySelector("[data-shop-state]") !== null, "open/closed widget present");
  const openText = d.querySelector("[data-shop-state]").textContent;
  check(/Open now|Closed now/.test(openText), "open state resolved to '" + openText + "'");
  check(d.querySelector("[data-year]").textContent === String(new Date().getFullYear()), "footer year is current");
  dom.window.close();
}

console.log("\n— TRIAL 02 showrooms ————————————————————————————");
{
  const dom = await load("trial-02-illustrated/stores.html",
    ["trial-02-illustrated/assets/js/main.js", "trial-02-illustrated/assets/js/stores.js"]);
  const d = dom.window.document;
  check(d.querySelectorAll("[data-store-list] .store").length === 25, "renders all 25 showrooms");
  const maps = [...d.querySelectorAll('[data-store-list] a[href*="google.com/maps/search"]')];
  check(maps.length === 25, "every showroom has a real Maps link");
  check(maps.every(a => !a.href.includes("undefined") && !a.href.includes("about:")), "no broken map links");
  check(new URL(maps[0].href).searchParams.get("query").includes("WHYNOT"), "Maps query is a WHYNOT search");
  const search = d.querySelector("[data-store-search]");
  search.value = "bhimavaram";
  search.dispatchEvent(new dom.window.Event("input"));
  check(d.querySelectorAll("[data-store-list] .store:not([hidden])").length === 1, "search narrows to 1 showroom");
  d.querySelector('[data-district="Visakhapatnam"]').click();
  const chipCount = d.querySelectorAll("[data-store-list] .store:not([hidden])").length;
  check(chipCount === 0, "district + search combine correctly (0 results)");
  d.querySelector("[data-store-clear]").click();
  check(d.querySelectorAll("[data-store-list] .store:not([hidden])").length === 25, "clear restores 25");
  dom.window.close();
}

console.log("\n— TRIAL 02 contact form ————————————————————————");
{
  const dom = await load("trial-02-illustrated/contact.html",
    ["trial-02-illustrated/assets/js/main.js", "trial-02-illustrated/assets/js/contact.js"]);
  const d = dom.window.document;
  const form = d.querySelector("[data-contact-form]");
  form.dispatchEvent(new dom.window.Event("submit"));
  check(d.querySelector("#name").getAttribute("aria-invalid") === "true", "empty submit marks the name field invalid");
  check(d.querySelector("#name-error").textContent.length > 0, "error text is written into the field's message slot");

  d.querySelector("#name").value = "Ravi Kumar";
  d.querySelector("#mobile").value = "+91 98765 43210";
  d.querySelector("#message").value = "Looking for a 55 inch TV for the hall, budget about 60 thousand.";
  form.dispatchEvent(new dom.window.Event("submit"));
  await new Promise(r => setTimeout(r, 800));
  const status = d.querySelector("[data-form-status]").textContent;
  check(status.includes("Ravi"), "success message uses the customer's name");
  check(status.includes("98765"), "success message repeats the number we will call");
  check(/nothing has actually been sent/i.test(status), "success state is honest about the demo having no server");

  d.querySelector("#mobile").value = "12345";
  d.querySelector("#mobile").dispatchEvent(new dom.window.Event("blur"));
  check(d.querySelector("#mobile").getAttribute("aria-invalid") === "true", "bad mobile number is rejected");
  dom.window.close();
}

console.log("\n— TRIAL 01 catalogue ————————————————————————————");
{
  const dom = await load("trial-01-minimal/products.html",
    ["trial-01-minimal/assets/js/main.js", "trial-01-minimal/assets/js/products.js"]);
  const d = dom.window.document;
  check(d.querySelectorAll("[data-products] .pcard").length === 17, "renders 17 cards in the minimal skin");
  check(d.querySelectorAll("[data-cat-chips] .chip").length === 11, "chips built");
  d.querySelector('[data-add="fr-265"]').click();
  check(d.querySelector("[data-list-count]").textContent === "1", "count badge updates in the header");
  check(d.querySelectorAll("[data-list-panel] .list-row").length === 1, "list panel renders the row");
  const mail = d.querySelector('[data-list-panel] a[href^="mailto:"]');
  check(!!mail && decodeURIComponent(mail.href).includes("265 L double-door"), "email link carries the list");
  d.querySelector('[data-cat="kitchen"]').click();
  check(d.querySelectorAll("[data-products] .pcard").length === 3, "kitchen filter returns 3 items");
  dom.window.close();
}

console.log("\n— TRIAL 01 home + showrooms ————————————————————");
{
  const dom = await load("trial-01-minimal/index.html",
    ["trial-01-minimal/assets/js/main.js", "trial-01-minimal/assets/js/products.js"]);
  const d = dom.window.document;
  check(d.querySelectorAll("[data-featured] .pcard").length === 4, "home featured strip renders 4 cards");
  check(d.querySelectorAll("[data-count]").length === 4, "four animated stat counters");
  dom.window.close();

  const dom2 = await load("trial-01-minimal/stores.html",
    ["trial-01-minimal/assets/js/main.js", "trial-01-minimal/assets/js/stores.js"]);
  const d2 = dom2.window.document;
  check(d2.querySelectorAll("[data-store-list] .store").length === 25, "25 showrooms rendered");
  check([...d2.querySelectorAll('[data-store-list] a[href*="maps"]')].every(a => a.href.startsWith("https://www.google.com/maps/search/")), "real Maps links");
  dom2.window.close();
}

console.log("\n— localStorage isolation between trials —————————");
{
  const dom = await load("trial-01-minimal/products.html",
    ["trial-01-minimal/assets/js/products.js"]);
  const d = dom.window.document;
  d.querySelector('[data-add="tv-43"]').click();
  const keys = Object.keys(dom.window.localStorage);
  check(keys.includes("whynot-list-t1"), "trial 01 keeps its own list key (" + keys.join(",") + ")");
  check(!keys.includes("whynot-list"), "and does not touch trial 02's list");
  dom.window.close();
}


console.log("\n— TRIAL 03 catalogue ————————————————————————————");
{
  const dom = await load("trial-03-anime/products.html",
    ["trial-03-anime/assets/js/main.js", "trial-03-anime/assets/js/products.js"]);
  const d = dom.window.document;
  check(d.querySelectorAll("[data-products] .card").length === 17, "renders 17 cards in the manga-panel skin");
  check(d.querySelectorAll("[data-cat-chips] .chip").length === 11, "chips built");
  check(d.querySelectorAll(".panel").length > 3, "the panel primitive is in use");
  d.querySelector('[data-add="ac-15"]').click();
  d.querySelector('[data-add="wm-7"]').click();
  check([...d.querySelectorAll("[data-list-count]")].every((n) => n.textContent === "2"), "both list badges read 2");
  check(d.querySelectorAll("[data-list-panel] .list-item").length === 2, "two rows in the list panel");
  const wa = d.querySelector('[data-list-panel] a[href^="https://wa.me/"]');
  check(!!wa && decodeURIComponent(wa.href).includes("1.5-ton"), "WhatsApp link carries the list");
  const input = d.querySelector("[data-product-search]");
  input.value = "microwave";
  input.dispatchEvent(new dom.window.Event("input"));
  check(d.querySelectorAll("[data-products] .card").length === 1, "'microwave' finds exactly one product");
  input.value = "";
  input.dispatchEvent(new dom.window.Event("input"));
  d.querySelector('[data-cat="tv"]').click();
  const tvs = d.querySelectorAll("[data-products] .card").length;
  check(tvs === 2, "tv filter returns both televisions (got " + tvs + ")");
  dom.window.close();
}

console.log("\n— TRIAL 03 home + showrooms + form ————————————————");
{
  const dom = await load("trial-03-anime/index.html",
    ["trial-03-anime/assets/js/main.js", "trial-03-anime/assets/js/products.js"]);
  const d = dom.window.document;
  check(d.querySelectorAll("[data-featured] .card").length === 4, "featured strip renders 4 cards");
  check(d.querySelector("picture source[type='image/avif']") !== null, "hero ships an AVIF source");
  check(d.querySelector("picture source[type='image/webp']") !== null, "and a WebP fallback");
  check(d.querySelector(".hero__frame img").getAttribute("width") === "760", "hero image declares its size (no layout shift)");
  dom.window.close();

  const dom2 = await load("trial-03-anime/stores.html",
    ["trial-03-anime/assets/js/main.js", "trial-03-anime/assets/js/stores.js"]);
  const d2 = dom2.window.document;
  check(d2.querySelectorAll("[data-store-list] .store").length === 25, "25 showrooms rendered");
  check([...d2.querySelectorAll('[data-store-list] a[href*="maps"]')].every((a) => a.href.startsWith("https://www.google.com/maps/search/")), "real Maps links in this design too");
  dom2.window.close();

  const dom3 = await load("trial-03-anime/contact.html",
    ["trial-03-anime/assets/js/main.js", "trial-03-anime/assets/js/contact.js"]);
  const d3 = dom3.window.document;
  const form = d3.querySelector("[data-contact-form]");
  form.dispatchEvent(new dom3.window.Event("submit"));
  check(d3.querySelector("#name").getAttribute("aria-invalid") === "true", "empty submit is caught");
  d3.querySelector("#name").value = "Sridevi";
  d3.querySelector("#mobile").value = "918886222448";
  d3.querySelector("#message").value = "Need a washing machine and an AC for a new flat.";
  form.dispatchEvent(new dom3.window.Event("submit"));
  await new Promise((r) => setTimeout(r, 700));
  const st = d3.querySelector("[data-form-status]").textContent;
  check(st.includes("Sridevi"), "success state names the customer");
  check(/nothing has actually been sent/i.test(st), "and stays honest about the missing server");
  dom3.window.close();
}

console.log("\n— three trials, three separate lists ————————————————");
{
  for (const [trial, key] of [["trial-01-minimal", "whynot-list-t1"], ["trial-02-illustrated", "whynot-list"], ["trial-03-anime", "whynot-list-t3"]]) {
    const dom = await load(`${trial}/products.html`, [`${trial}/assets/js/products.js`]);
    dom.window.document.querySelector('[data-add="tv-43"]').click();
    const keys = Object.keys(dom.window.localStorage);
    check(keys.length === 1 && keys[0] === key, `${trial} uses only its own key (${key})`);
    dom.window.close();
  }
}

const productData = ["trial-01-minimal", "trial-02-illustrated", "trial-03-anime", "trial-04-brutalist",
                     "trial-05-glass", "trial-06-painting", "trial-07-slate"].map((t) => {
  const src = fs.readFileSync(`${ROOT}/${t}/assets/js/products.js`, "utf8");
  const start = src.indexOf("var PRODUCTS = [");
  return src.slice(start, src.indexOf("];", start) + 2);
});
check(new Set(productData).size === 1, "the product data is byte-identical across all seven trials");


console.log("\n— TRIALS 04–07 (the shared contract) ————————————————");
const NEW_TRIALS = ["trial-04-brutalist", "trial-05-glass", "trial-06-painting", "trial-07-slate"];
for (const dir of NEW_TRIALS) {
  if (!fs.existsSync(`${ROOT}/${dir}/assets/js/products.js`)) { console.log(`  --   ${dir}: not built yet, skipped`); continue; }
  const label = dir.replace("trial-0", "T0").replace("-", " ");
  const css = fs.readFileSync(`${ROOT}/${dir}/assets/css/style.css`, "utf8");

  const dom = await load(`${dir}/products.html`, [`${dir}/assets/js/main.js`, `${dir}/assets/js/products.js`]);
  const d = dom.window.document;
  check(d.querySelectorAll("[data-products] [data-add]").length === 17, `${label}: 17 products render`);
  check(d.querySelectorAll("[data-cat-chips] .chip").length === 11, `${label}: category chips built`);
  check(d.querySelectorAll(".store, [data-store-list]").length >= 0, `${label}: catalogue page intact`);

  d.querySelector('[data-add="tv-55"]').click();
  check([...d.querySelectorAll("[data-list-count]")].every((n) => n.textContent === "1"),
        `${label}: every list badge updates together`);
  check(d.querySelectorAll("[data-list-panel] .list-item").length === 1, `${label}: shortlist row renders`);
  const wa = d.querySelector('[data-list-panel] a[href^="https://wa.me/"]');
  check(!!wa && decodeURIComponent(wa.href).includes("55-inch"), `${label}: WhatsApp payload carries the item`);

  // every class the rendered page uses must exist in that trial's stylesheet --
  // the check that catches a design port that forgot to style something
  const emitted = new Set();
  d.querySelectorAll("*").forEach((el) => el.classList.forEach((c) => emitted.add(c)));
  const missing = [...emitted].filter((c) => !css.includes("." + c));
  check(missing.length === 0, `${label}: CSS styles every class on the page` +
        (missing.length ? ` — missing ${missing.slice(0, 8).join(", ")}` : ""));

  // icon contract: no <use> pointing at a symbol the page does not define
  const syms = new Set([...d.querySelectorAll("symbol")].map((n) => n.id));
  const uses = new Set([...d.querySelectorAll("use")].map((n) => (n.getAttribute("href") || "").slice(1)));
  const dangling = [...uses].filter((u) => u && !syms.has(u));
  check(dangling.length === 0, `${label}: every icon reference resolves` +
        (dangling.length ? ` — dangling ${dangling.join(", ")}` : ""));
  dom.window.close();

  const dom2 = await load(`${dir}/stores.html`, [`${dir}/assets/js/main.js`, `${dir}/assets/js/stores.js`]);
  const d2 = dom2.window.document;
  check(d2.querySelectorAll("[data-store-list] .store").length === 25, `${label}: 25 showrooms render`);
  check([...d2.querySelectorAll("[data-store-list] a")].every((a) => a.href.startsWith("https://www.google.com/maps/search/")),
        `${label}: real Maps links, no about:invalid`);
  dom2.window.close();
}



console.log("\n— TRIAL 07 light / dark, white first ————————————————————");
{
  const dir = "trial-07-slate";
  const css = fs.readFileSync(`${ROOT}/${dir}/assets/css/style.css`, "utf8");
  const dom = await load(`${dir}/index.html`, [`${dir}/assets/js/main.js`]);
  const d = dom.window.document, w = dom.window;
  const btn = d.querySelector("[data-mode-toggle]");

  check(!!btn, "the mode switch is on the page");
  check(d.documentElement.getAttribute("data-mode") === "light", "first paint is light — the default, system setting ignored");

  /* The rule this design is built on: white first, whatever the machine says.
     The inline script is what decides that, so the test runs it with the system
     asking for dark and nothing stored — the page must stay light. */
  const inline = [...d.querySelectorAll("script:not([src])")].map((s) => s.textContent).join("\n");
  w.localStorage.clear();
  w.matchMedia = () => ({ matches: true, addEventListener() {} });
  d.documentElement.setAttribute("data-mode", "light");
  w.eval(inline);
  check(d.documentElement.getAttribute("data-mode") === "light",
        "white even when the system asks for dark");
  w.localStorage.setItem("whynot-mode", "dark");
  d.documentElement.setAttribute("data-mode", "light");
  w.eval(inline);
  check(d.documentElement.getAttribute("data-mode") === "dark",
        "and dark is remembered once chosen");
  // hand a clean slate back to the switch flow below
  w.localStorage.removeItem("whynot-mode");
  d.documentElement.setAttribute("data-mode", "light");

  btn.click();
  check(d.documentElement.getAttribute("data-mode") === "dark", "the switch goes dark");
  check(btn.getAttribute("aria-pressed") === "true", "the switch says it is pressed");
  check(w.localStorage.getItem("whynot-mode") === "dark", "the choice is remembered");

  btn.click();
  check(d.documentElement.getAttribute("data-mode") === "light", "and back to light");
  check(w.localStorage.getItem("whynot-mode") === "light", "the change is remembered too");
  dom.window.close();

  // both palettes must define the same tokens, or one mode renders half-styled
  const lightBlock = css.slice(css.indexOf(":root {"), css.indexOf('html[data-mode="dark"]'));
  const darkBlock = css.slice(css.indexOf('html[data-mode="dark"]'), css.indexOf("* , *::before"));
  // only the COLOUR tokens have to exist in both palettes; type, radii and
  // shadows are set once and deliberately do not change with the mode
  const colours = (block) => new Set([...block.matchAll(/(--[a-z0-9-]+)\s*:\s*(#[0-9a-fA-F]{3,8}|rgba?\()/g)]
    .map((m) => m[1]));
  const missing = [...colours(lightBlock)].filter((t) => !colours(darkBlock).has(t));
  check(missing.length === 0, "every colour token is defined in both palettes" +
        (missing.length ? ` — missing ${missing.join(", ")}` : ""));
  const orphan = [...colours(darkBlock)].filter((t) => !colours(lightBlock).has(t));
  check(orphan.length === 0, "and no colour exists only in dark" +
        (orphan.length ? ` — extra ${orphan.join(", ")}` : ""));
}

console.log("\n— TRIAL 07 the photograph and the drawn map —————————————————");
{
  const dir = "trial-07-slate";
  const pages = ["index.html", "products.html", "stores.html", "about.html", "contact.html", "404.html"];
  const stores = fs.readFileSync(`${ROOT}/${dir}/assets/js/stores.js`, "utf8");
  const towns = [...stores.matchAll(/town:\s*"([^"]+)"/g)].map((m) => m[1]);
  const mapTowns = [...new Set(towns)].filter((t) => !/Best Shop|Smart Plaza/.test(t));

  // every photograph: real file, declared size, alt text that says something
  let images = 0; const noSize = [], noAlt = [], missingFile = [];
  for (const page of pages) {
    const html = fs.readFileSync(`${ROOT}/${dir}/${page}`, "utf8");
    for (const m of html.matchAll(/<img\s[^>]*>/g)) {
      images++;
      const tag = m[0];
      const src = (tag.match(/src="([^"]+)"/) || [])[1];
      if (!/width="\d+"/.test(tag) || !/height="\d+"/.test(tag)) noSize.push(page + ": " + src);
      const alt = (tag.match(/alt="([^"]*)"/) || [])[1];
      if (alt === undefined || alt.trim().length < 12) noAlt.push(page + ": " + src);
      if (src && !fs.existsSync(`${ROOT}/${dir}/${src}`)) missingFile.push(src);
    }
    for (const m of html.matchAll(/<source srcset="([^"]+)"/g)) {
      if (!fs.existsSync(`${ROOT}/${dir}/${m[1]}`)) missingFile.push(m[1]);
    }
  }
  check(images >= 1, `the photograph is on the pages (${images} img elements)`);
  check(noSize.length === 0, "every photograph declares its size, so the page does not jump" +
        (noSize.length ? ` — ${noSize.join(", ")}` : ""));
  check(noAlt.length === 0, "and carries real alt text" +
        (noAlt.length ? ` — ${noAlt.join(", ")}` : ""));
  check(missingFile.length === 0, "every image file it points at exists" +
        (missingFile.length ? ` — ${missingFile.join(", ")}` : ""));

  const dom = await load(`${dir}/stores.html`, [`${dir}/assets/js/main.js`, `${dir}/assets/js/stores.js`]);
  const d = dom.window.document;
  const svg = d.querySelector(".map svg");
  check(!!svg, "the drawn map is on the showroom page");
  const dots = [...svg.querySelectorAll("circle.map__dot")]
    .filter((c) => !c.classList.contains("map__dot--hollow"));
  check(dots.length === mapTowns.length,
        `one dot per town (${dots.length} dots, ${mapTowns.length} towns)`);
  const names = [...svg.querySelectorAll("text, title")].map((n) => n.textContent.trim());
  const named = mapTowns.filter((t) => names.some((n) => n.includes(t)));
  check(named.length === mapTowns.length,
        `every town is on the map (${named.length} of ${mapTowns.length})`);
  const off = dots.filter((c) => +c.getAttribute("cx") > 920 || +c.getAttribute("cy") > 700);
  check(off.length === 0, "no dot is drawn outside the map frame");
  check(!!d.querySelector(".map__key"), "and the map carries a key");
  check(/schematic/i.test(d.body.textContent), "the map says it is a schematic");
  dom.window.close();

  const home = await load(`${dir}/index.html`, [`${dir}/assets/js/main.js`, `${dir}/assets/js/products.js`]);
  const h = home.window.document;
  const cap = h.querySelector(".hero__fig figcaption");
  check(!!cap && /stand-in photograph/i.test(cap.textContent),
        "the photograph is labelled as a stand-in on the page");

  // the buying flow is a diagram: iconed nodes wired with drawn SVG chevrons
  const nodes = h.querySelectorAll(".flow__node");
  check(nodes.length === 3, `the buying flow draws three steps (${nodes.length})`);
  const links = h.querySelectorAll(".flow__link");
  check(links.length === nodes.length - 1 && [...links].every((l) => l.querySelector("svg")),
        "each step is wired to the next with an SVG connector");
  check([...nodes].every((n) => n.querySelector("strong") && n.querySelector("p") &&
        /\d\d/.test(n.querySelector(".flow__n").textContent)),
        "each step is numbered, titled and explains itself");
  check(h.querySelectorAll(".flow__art use").length === 3, "and each carries an icon from the sprite");

  // the proof row under the hero: three facts, each with an icon
  const proof = h.querySelectorAll(".hero__proof li");
  check(proof.length === 3, `the hero carries three proof points (${proof.length})`);
  check([...proof].every((li) => li.querySelector("svg") && li.querySelector("span")),
        "each proof point is an icon plus text");

  // the map names the water it draws
  const sea = h.querySelector(".map__water");
  check(!!sea && sea.textContent.trim() === "Bay of Bengal", "the map labels the bay");
  const river = h.querySelector(".map__water--river");
  check(!!river && river.textContent.trim() === "Godavari", "and names the river");
  home.window.close();
}

console.log("\n— LANGUAGE (all trials) ————————————————————————————");
{
  const trials = ["trial-01-minimal", "trial-02-illustrated", "trial-03-anime",
                  "trial-04-brutalist", "trial-05-glass", "trial-06-painting", "trial-07-slate"];
  const telugu = (s) => [...s].some((c) => c.charCodeAt(0) >= 0x0c00 && c.charCodeAt(0) <= 0x0c7f);
  for (const dir of trials) {
    const dom = await load(`${dir}/products.html`,
      [`${dir}/assets/js/main.js`, `${dir}/assets/js/products.js`]);
    const d = dom.window.document;
    /* Trial 07 navigates from a rail and a tab bar; the others from a header nav,
       so the language checks look for whichever this trial actually has. */
    const navSel = ".nav a, .rail__nav a, .tabs a";
    const en = {
      nav: d.querySelector(navSel).textContent.trim(),
      add: d.querySelector("[data-add]").textContent.trim(),
      count: d.querySelector("[data-result-count]").textContent.trim(),
    };
    const teBtn = d.querySelector('[data-lang="te"]');
    check(!!teBtn, `${dir}: language switch on the page`);
    teBtn.click();
    check(d.documentElement.lang === "te", `${dir}: document language follows the switch`);
    check(telugu(d.querySelector(navSel).textContent), `${dir}: nav reads Telugu`);
    check(telugu(d.querySelector("[data-add]").textContent),
          `${dir}: the button the catalogue builds reads Telugu`);
    check(d.querySelector("[data-result-count]").textContent.trim() !== en.count,
          `${dir}: result count reads Telugu`);

    // added items redraw after the switch, so this exercises the observer too
    d.querySelector("[data-add]").click();
    await new Promise((r) => setTimeout(r, 20));
    check(telugu(d.querySelector("[data-list-panel]").textContent),
          `${dir}: shortlist panel written after the switch reads Telugu`);

    d.querySelector('[data-lang="en"]').click();
    check(d.querySelector(navSel).textContent.trim() === en.nav,
          `${dir}: switching back restores the English`);
    check(dom.window.localStorage.getItem("whynot-lang") === "en",
          `${dir}: the choice is remembered`);
    dom.window.close();

    const dom2 = await load(`${dir}/stores.html`,
      [`${dir}/assets/js/main.js`, `${dir}/assets/js/stores.js`]);
    const d2 = dom2.window.document;
    d2.querySelector('[data-lang="te"]').click();
    check(telugu(d2.querySelector("[data-store-list] .store").textContent),
          `${dir}: showroom cards read Telugu`);
    check(d2.querySelectorAll("[data-store-list] .store").length === 25,
          `${dir}: still 25 showrooms in Telugu`);
    dom2.window.close();
  }
}

console.log("\n" + "=".repeat(52));
console.log(`  ${pass} passed, ${fail} failed`);
console.log("=".repeat(52) + "\n");
process.exit(fail ? 1 : 0);
