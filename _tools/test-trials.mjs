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

const productData = ["trial-01-minimal", "trial-02-illustrated", "trial-03-anime"].map((t) => {
  const src = fs.readFileSync(`${ROOT}/${t}/assets/js/products.js`, "utf8");
  const start = src.indexOf("var PRODUCTS = [");
  return src.slice(start, src.indexOf("];", start) + 2);
});
check(new Set(productData).size === 1, "the product data is byte-identical across all three trials");

console.log("\n" + "=".repeat(52));
console.log(`  ${pass} passed, ${fail} failed`);
console.log("=".repeat(52) + "\n");
process.exit(fail ? 1 : 0);
