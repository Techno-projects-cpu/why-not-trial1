function fallbackT(key, english) { return english === undefined ? key : english; }
/* WHYNOT — Trial 01 · catalogue + "My list".
   ---------------------------------------------------------------------------
   A calmer take on the shop: no illustration, no prices invented for a real
   company, and a shortlist that travels to the counter by WhatsApp, phone or
   email. The PRODUCTS and CATS arrays are byte-identical to Trial 02's, so the
   two designs describe exactly the same shop — only the presentation differs.
   --------------------------------------------------------------------------- */
(function () {
  "use strict";

  var T = window.WHYNOT_T || fallbackT;

  var STORE_KEY = "whynot-list-t1";
  var HELPLINE = "8886222448";
  var EMAIL = "whynot.rayudu@gmail.com";

  var CATS = [
    { id: "tv",       label: "Televisions",       art: "i-tv",      tone: "sky" },
    { id: "ac",       label: "Air conditioners",  art: "i-ac",      tone: "sky" },
    { id: "fridge",   label: "Refrigerators",     art: "i-fridge",  tone: "lime" },
    { id: "washer",   label: "Washing machines",  art: "i-washer",  tone: "teal" },
    { id: "kitchen",  label: "Kitchen appliances",art: "i-mixer",   tone: "mango" },
    { id: "water",    label: "Water & geysers",   art: "i-droplet", tone: "sky" },
    { id: "lighting", label: "Lighting",          art: "i-bulb",    tone: "marker" },
    { id: "audio",    label: "Audio",             art: "i-speaker", tone: "violet" },
    { id: "mobile",   label: "Mobiles",           art: "i-phone",   tone: "pink" },
    { id: "cleaning", label: "Cleaning",          art: "i-vacuum",  tone: "lime" }
  ];

  var PRODUCTS = [
    { id: "tv-55", tags: ["tv", "television", "qled", "smart tv", "4k"],  cat: "tv",      title: "55-inch 4K QLED television",           specs: ["4K QLED", "120 Hz", "3 × HDMI"],        badge: "Best seller",   towns: ["Tanuku", "Bhimavaram", "Rajahmundry"] },
    { id: "tv-43", tags: ["tv", "television", "smart tv", "4k"],  cat: "tv",      title: "43-inch 4K smart television",          specs: ["4K", "Smart OS", "Dolby Audio"],        badge: "",              towns: ["Eluru", "Kakinada", "Bhimavaram"] },
    { id: "ac-15", tags: ["ac", "air conditioner", "split ac", "inverter ac", "1.5 ton"],  cat: "ac",      title: "1.5-ton 5-star inverter split AC",     specs: ["5-star", "Inverter", "Copper coil"],    badge: "Peak-season pick", towns: ["Rajahmundry", "Eluru", "Tanuku"] },
    { id: "ac-10", tags: ["ac", "air conditioner", "split ac", "1 ton"],  cat: "ac",      title: "1-ton 3-star split AC",                specs: ["3-star", "Self-clean", "Copper"],       badge: "",              towns: ["Amalapuram", "Narasapuram"] },
    { id: "fr-265", tags: ["fridge", "refrigerator", "double door", "frost free"], cat: "fridge",  title: "265 L double-door refrigerator",       specs: ["Frost-free", "Inverter", "3-star"],     badge: "Best seller",   towns: ["Tanuku", "Bhimavaram", "Eluru"] },
    { id: "fr-190", tags: ["fridge", "refrigerator", "single door", "direct cool"], cat: "fridge",  title: "190 L single-door refrigerator",       specs: ["Direct cool", "5-star", "Toughened glass"], badge: "",           towns: ["Tadepalligudem", "Palakollu", "Kovvur"] },
    { id: "wm-7", tags: ["washing machine", "washer", "front load", "fully automatic"],   cat: "washer",  title: "7 kg front-load washing machine",      specs: ["7 kg", "1200 rpm", "Inverter"],         badge: "",              towns: ["Bhimavaram", "Rajahmundry", "Eluru"] },
    { id: "wm-65", tags: ["washing machine", "washer", "semi automatic", "twin tub"],  cat: "washer",  title: "6.5 kg semi-automatic washing machine",specs: ["6.5 kg", "Twin tub", "Rust-proof"],     badge: "Easy on budget", towns: ["All showrooms"] },
    { id: "kt-mix", tags: ["mixer", "mixie", "mixer grinder", "kitchen"], cat: "kitchen", title: "750 W mixer grinder, 3 jars",          specs: ["750 W", "3 jars", "Overload safety"],   badge: "",              towns: ["All showrooms"] },
    { id: "kt-micro", tags: ["microwave", "oven", "microwave oven", "kitchen"], cat: "kitchen", title: "25 L convection microwave oven",     specs: ["25 L", "Convection", "Auto-cook menus"], badge: "",            towns: ["Tanuku", "Kakinada", "Rajahmundry"] },
    { id: "kt-grind", tags: ["wet grinder", "grinder", "kitchen"], cat: "kitchen", title: "2 L table-top wet grinder",          specs: ["2 L", "Stone rollers", "Coconut scraper"], badge: "",           towns: ["Palakollu", "Pithapuram"] },
    { id: "wt-ro", tags: ["water purifier", "ro", "purifier", "drinking water"],  cat: "water",   title: "10 L RO + UV water purifier",          specs: ["RO + UV", "10 L", "6-stage"],           badge: "",              towns: ["Bhimavaram", "Eluru", "Tanuku"] },
    { id: "wt-gey", tags: ["geyser", "water heater", "hot water", "storage geyser"], cat: "water",   title: "15 L storage water heater",            specs: ["15 L", "5-star", "Glass-lined tank"],   badge: "",              towns: ["All showrooms"] },
    { id: "lt-led", tags: ["led", "bulb", "light", "lighting", "lamp"], cat: "lighting",title: "9 W LED bulb, pack of 4",              specs: ["9 W", "Cool white", "2-year warranty"], badge: "Add-on",        towns: ["All showrooms"] },
    { id: "au-spk", tags: ["speaker", "bluetooth speaker", "audio", "party speaker"], cat: "audio",   title: "80 W Bluetooth party speaker",         specs: ["80 W", "Bluetooth 5.3", "Karaoke mic"], badge: "",              towns: ["Kakinada", "Rajahmundry"] },
    { id: "mb-5g", tags: ["mobile", "phone", "smartphone", "5g", "cellphone"],  cat: "mobile",  title: "5G smartphone, 8 GB / 128 GB",         specs: ["5G", "8 GB / 128 GB", "5000 mAh"],      badge: "New arrival",   towns: ["Tanuku", "Bhimavaram", "Kakinada"] },
    { id: "cl-vac", tags: ["vacuum", "vacuum cleaner", "cleaning", "hepa"], cat: "cleaning",title: "1200 W vacuum cleaner",                specs: ["1200 W", "HEPA filter", "2 L dust bag"],badge: "",              towns: ["Rajahmundry", "Eluru"] }
  ];

  /* ------------------------------------------------------------ utilities */
  function cat(id) {
    for (var i = 0; i < CATS.length; i++) if (CATS[i].id === id) return CATS[i];
    return CATS[0];
  }
  function product(id) {
    for (var i = 0; i < PRODUCTS.length; i++) if (PRODUCTS[i].id === id) return PRODUCTS[i];
    return null;
  }
  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  /* --------------------------------------------------------- the shortlist */
  function readList() {
    try {
      var arr = JSON.parse(localStorage.getItem(STORE_KEY) || "[]");
      return Array.isArray(arr) ? arr.filter(product) : [];
    } catch (e) { return []; }
  }
  function writeList(ids) {
    try { localStorage.setItem(STORE_KEY, JSON.stringify(ids)); } catch (e) {}
    paintCounts();
    renderPanel();
    paintAddButtons();
  }
  function inList(id) { return readList().indexOf(id) !== -1; }
  function toggleItem(id) {
    var ids = readList();
    var i = ids.indexOf(id);
    if (i === -1) { ids.push(id); flash(T("addedToast", "Added to your list")); }
    else { ids.splice(i, 1); flash(T("removed", "Removed from your list")); }
    writeList(ids);
  }
  function paintCounts() {
    var n = readList().length;
    var nodes = document.querySelectorAll("[data-list-count]");
    for (var i = 0; i < nodes.length; i++) {
      nodes[i].textContent = String(n);
      nodes[i].hidden = n === 0;
    }
    var labels = document.querySelectorAll("[data-list-label]");
    for (var j = 0; j < labels.length; j++) labels[j].textContent = n === 1 ? "1 item" : n + T("items", " items");
  }

  /* ------------------------------------------------------------- rendering */
  function cardHtml(p) {
    var c = cat(p.cat);
    var added = inList(p.id);
    return '' +
      '<article class="pcard">' +
        '<p class="pcard__cat">' + esc(c.label) + "</p>" +
        '<h3 class="pcard__title">' + esc(p.title) + "</h3>" +
        '<p class="pcard__specs">' + esc(p.specs.join(" · ")) + "</p>" +
        '<p class="pcard__meta">' + esc(p.towns.join(", ")) + "</p>" +
        '<p class="pcard__price">Ask for today&rsquo;s price</p>' +
        '<div class="pcard__actions">' +
          '<button class="btn btn--sm ' + (added ? "btn--ghost" : "btn--brand") + '" type="button" data-add="' + p.id + '">' +
            (added ? T("added", "In your list") : T("add", "Add to list")) + "</button>" +
          '<a class="btn btn--sm btn--ghost" href="contact.html?about=' + encodeURIComponent(p.title) + '">Enquire</a>' +
        "</div>" +
        (p.badge ? '<p class="pcard__badge">' + esc(p.badge) + "</p>" : "") +
      "</article>";
  }

  function paintAddButtons() {
    var buttons = document.querySelectorAll("[data-add]");
    for (var i = 0; i < buttons.length; i++) {
      var added = inList(buttons[i].getAttribute("data-add"));
      buttons[i].className = "btn btn--sm " + (added ? "btn--ghost" : "btn--brand");
      buttons[i].textContent = added ? T("added", "In your list") : T("add", "Add to list");
    }
  }

  function listText() {
    var ids = readList();
    var lines = ids.map(function (id, i) {
      var p = product(id);
      return (i + 1) + ". " + p.title + " (" + p.specs.join(", ") + ")";
    });
    return "Hello WHYNOT, please share today's price and availability for:\n\n" + lines.join("\n") +
      "\n\nMy town: \nMy mobile: ";
  }

  function renderPanel() {
    var panel = document.querySelector("[data-list-panel]");
    if (!panel) return;
    var ids = readList();

    if (!ids.length) {
      panel.innerHTML =
        '<div class="empty">' +
          '<p class="h3">Your list is empty</p>' +
          '<p class="muted">Add anything you want priced. It stays on this device until you send it.</p>' +
          '<a class="btn btn--ghost btn--sm" href="#catalogue">Back to the catalogue</a>' +
        "</div>";
      return;
    }

    panel.innerHTML =
      '<ul class="list-panel">' +
        ids.map(function (id) {
          var p = product(id);
          return '<li class="list-row">' +
            '<div>' +
              '<p class="list-row__title">' + esc(p.title) + "</p>" +
              '<p class="list-row__meta">' + esc(cat(p.cat).label) + " · " + esc(p.specs.join(" · ")) + "</p>" +
            "</div>" +
            '<button class="btn btn--sm btn--ghost" type="button" data-remove="' + p.id + '">' + T("remove", "Remove") + '</button>' +
          "</li>";
        }).join("") +
      "</ul>" +
      '<div class="list-actions">' +
        '<a class="btn btn--brand" href="https://wa.me/91' + HELPLINE + "?text=" + encodeURIComponent(listText()) + '" target="_blank" rel="noopener noreferrer">Send on WhatsApp</a>' +
        '<a class="btn btn--ghost" href="mailto:' + EMAIL + "?subject=" + encodeURIComponent("Price enquiry from the website") +
          "&body=" + encodeURIComponent(listText()) + '">Email the list</a>' +
        '<a class="btn btn--ghost" href="tel:+91' + HELPLINE + '">Call ' + HELPLINE + "</a>" +
      "</div>" +
      '<p class="form__note">No account, no card details, no checkout maze. A person from your nearest branch replies with today&rsquo;s price and what is in stock.</p>';
  }

  /* --------------------------------------------------------------- filters */
  var state = { cat: "all", q: "", town: "all" };

  function matches(p) {
    if (state.cat !== "all" && p.cat !== state.cat) return false;
    if (state.town !== "all" && p.towns.indexOf("All showrooms") === -1 && p.towns.indexOf(state.town) === -1) return false;
    if (!state.q) return true;
    var hay = (p.title + " " + p.specs.join(" ") + " " + p.cat + " " + p.tags.join(" ") + " " + p.towns.join(" ")).toLowerCase();
    return hay.indexOf(state.q) !== -1;
  }

  function renderGrid() {
    var grid = document.querySelector("[data-products]");
    if (!grid) return;
    var shown = PRODUCTS.filter(matches);
    grid.innerHTML = shown.length
      ? shown.map(cardHtml).join("")
      : '<div class="empty"><p class="h3">Nothing matches that</p>' +
        '<p class="muted">Try a shorter word or clear the filters.</p>' +
        '<button class="btn btn--ghost btn--sm" type="button" data-clear>Clear filters</button></div>';

    var count = document.querySelector("[data-result-count]");
    if (count) {
      count.textContent = state.q || state.cat !== "all" || state.town !== "all"
        ? "Showing " + shown.length + " of " + PRODUCTS.length + " products"
        : PRODUCTS.length + " products · sample catalogue, real prices on request";
    }
    paintAddButtons();
  }

  function renderFeatured() {
    var host = document.querySelector("[data-featured]");
    if (!host) return;
    host.innerHTML = ["tv-55", "ac-15", "fr-265", "wm-7"].map(product).filter(Boolean).map(cardHtml).join("");
  }

  function buildChips() {
    var host = document.querySelector("[data-cat-chips]");
    if (!host) return;
    var used = CATS.filter(function (c) {
      return PRODUCTS.some(function (p) { return p.cat === c.id; });
    });
    host.innerHTML =
      '<button class="chip" type="button" data-cat="all" aria-pressed="true">All</button>' +
      used.map(function (c) {
        return '<button class="chip" type="button" data-cat="' + c.id + '" aria-pressed="false">' + esc(c.label) + "</button>";
      }).join("");
  }

  function buildTowns() {
    var sel = document.querySelector("[data-town-select]");
    if (!sel) return;
    var towns = [];
    PRODUCTS.forEach(function (p) {
      p.towns.forEach(function (t) { if (t !== "All showrooms" && towns.indexOf(t) === -1) towns.push(t); });
    });
    towns.sort();
    sel.innerHTML = '<option value="all">All towns</option>' +
      towns.map(function (t) { return '<option value="' + esc(t) + '">' + esc(t) + "</option>"; }).join("");
  }

  /* ---------------------------------------------------------------- events */
  document.addEventListener("click", function (e) {
    var add = e.target.closest("[data-add]");
    if (add) { toggleItem(add.getAttribute("data-add")); return; }

    var remove = e.target.closest("[data-remove]");
    if (remove) { toggleItem(remove.getAttribute("data-remove")); return; }

    var chip = e.target.closest("[data-cat]");
    if (chip) {
      state.cat = chip.getAttribute("data-cat");
      var all = document.querySelectorAll("[data-cat]");
      for (var i = 0; i < all.length; i++) all[i].setAttribute("aria-pressed", all[i] === chip ? "true" : "false");
      renderGrid();
      return;
    }

    var clear = e.target.closest("[data-clear]");
    if (clear) {
      state = { cat: "all", q: "", town: "all" };
      var input = document.querySelector("[data-product-search]");
      if (input) input.value = "";
      var sel = document.querySelector("[data-town-select]");
      if (sel) sel.value = "all";
      var chips = document.querySelectorAll("[data-cat]");
      for (var k = 0; k < chips.length; k++) {
        chips[k].setAttribute("aria-pressed", chips[k].getAttribute("data-cat") === "all" ? "true" : "false");
      }
      renderGrid();
    }
  });

  var search = document.querySelector("[data-product-search]");
  if (search) search.addEventListener("input", function () { state.q = search.value.trim().toLowerCase(); renderGrid(); });

  var townSel = document.querySelector("[data-town-select]");
  if (townSel) townSel.addEventListener("change", function () { state.town = townSel.value; renderGrid(); });

  /* ---------------------------------------------------------------- toast */
  var toast = document.querySelector("[data-toast]");
  var toastTimer;
  function flash(msg) {
    if (!toast) return;
    toast.textContent = msg;
    toast.setAttribute("data-open", "true");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { toast.setAttribute("data-open", "false"); }, 2200);
  }

  /* ------------------------------------------------------------------ init */
  buildChips();
  buildTowns();
  renderFeatured();
  renderGrid();
  renderPanel();
  paintCounts();

  var params = new URLSearchParams(location.search);
  var wanted = params.get("cat");
  if (wanted) {
    state.cat = wanted;
    var els = document.querySelectorAll("[data-cat]");
    for (var n = 0; n < els.length; n++) els[n].setAttribute("aria-pressed", els[n].getAttribute("data-cat") === wanted ? "true" : "false");
    renderGrid();
  }

  /* redraw the generated markup when the language changes */
  window.WHYNOT_RERENDER = function () { renderGrid(); renderFeatured(); renderPanel(); };

})();
