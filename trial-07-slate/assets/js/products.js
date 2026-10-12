function fallbackT(key, english) { return english === undefined ? key : english; }
/* WHYNOT — Trial 07 · Slate & Rail · catalogue + "my list".
   The same catalogue as every other trial — same data, same behaviour, same shortlist — laid out as table rows you scan down, because that is
   the opposite of the card grid the other six directions use.
   --------------------------------------------------------------------------- */
(function () {
  "use strict";

  var T = window.WHYNOT_T || fallbackT;

  var STORE_KEY = "whynot-list-t7";
  var HELPLINE = "8886222448";
  var EMAIL = "whynot.rayudu@gmail.com";

  /* Categories mirror the 14 the company already sells by. */
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

  var ART = {};
  var LABEL = {};

  /* ------------------------------------------------------------ utilities */
  function cat(id) { for (var i = 0; i < CATS.length; i++) if (CATS[i].id === id) return CATS[i]; return CATS[0]; }
  function product(id) { for (var i = 0; i < PRODUCTS.length; i++) if (PRODUCTS[i].id === id) return PRODUCTS[i]; return null; }
  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function icon(art) {
    return '<svg class="icon" aria-hidden="true"><use href="#' + art + '"></use></svg>';
  }

  /* --------------------------------------------------------- the shortlist
     Kept in localStorage so the count in the header, the badge on the phone
     action bar and the list panel all agree across pages. For a real shop this
     is where a cart (with prices and a payment step) would live — the data
     model is already the same shape. */
  function readList() {
    try {
      var raw = localStorage.getItem(STORE_KEY);
      var arr = raw ? JSON.parse(raw) : [];
      return Array.isArray(arr) ? arr.filter(function (id) { return !!product(id); }) : [];
    } catch (e) { return []; }
  }
  function writeList(ids) {
    try { localStorage.setItem(STORE_KEY, JSON.stringify(ids)); } catch (e) { /* private mode */ }
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
    return i === -1;
  }

  function paintCounts() {
    var n = readList().length;
    var nodes = document.querySelectorAll("[data-list-count]");
    for (var i = 0; i < nodes.length; i++) {
      nodes[i].textContent = String(n);
      nodes[i].hidden = n === 0;
    }
    var labels = document.querySelectorAll("[data-list-label]");
    for (var j = 0; j < labels.length; j++) labels[j].textContent = String(n) + (n === 1 ? T("item", " item") : T("items", " items"));
  }

  /* ------------------------------------------------------------- rendering */
  /* One line item. Everything the card in the other trials shows — category,
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
          '<div class="row__where">' + esc(p.specs.join(" \u00b7 ")) + "</div>" +
        "</div>" +
        '<div class="row__cat">' + icon(c.art) + esc(c.label) + "</div>" +
        '<div class="row__specs">' + esc(p.specs.join(" \u00b7 ")) + "</div>" +
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

  function paintAddButtons() {
    var buttons = document.querySelectorAll("[data-add]");
    for (var i = 0; i < buttons.length; i++) {
      var id = buttons[i].getAttribute("data-add");
      var added = inList(id);
      buttons[i].className = "btn btn--sm " + (added ? "btn--done" : "btn--primary");
      buttons[i].innerHTML = added ? T("added", "&#10003; In my list") : T("add", "+ Add to my list");
    }
  }

  function sendText() {
    var ids = readList();
    if (!ids.length) return "I would like to know today's price for:";
    var lines = ids.map(function (id, i) {
      var p = product(id);
      return (i + 1) + ". " + p.title + " (" + p.specs.join(", ") + ")";
    });
    return "Hi WHYNOT, please share today's price and availability for:\n\n" + lines.join("\n") +
      "\n\nMy town: \nMy mobile: ";
  }

  function renderPanel() {
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
            '<p class="list-item__meta">' + esc(c.label) + " \u00b7 " + esc(p.towns.join(", ")) + "</p></div>" +
            '<button class="btn btn--sm btn--ghost" type="button" data-remove="' + p.id + '" ' +
              'aria-label="' + T("remove", "Remove") + " " + esc(p.title) + '">' +
              T("remove", "Remove") + "</button>" +
          "</div>";
        }).join("") +
        '<p class="list-total">' + ids.length +
          (ids.length === 1 ? T("item", " item") : T("items", " items")) +
          " \u2014 " + T("weWillPrice", "we will price it and call you") + "</p>" +
        '<div class="actions">' +
          '<a class="btn btn--primary" href="https://wa.me/91' + HELPLINE + "?text=" + encodeURIComponent(sendText()) + '" target="_blank" rel="noopener noreferrer">' +
            icon("i-whatsapp") + " " + T("wa", "Send on WhatsApp") + "</a>" +
          '<a class="btn" href="tel:+91' + HELPLINE + '">' + icon("i-call") + " " + T("callShort", "Call") + " " + HELPLINE + "</a>" +
          '<a class="btn btn--ghost" href="mailto:' + EMAIL + "?subject=" + encodeURIComponent("Price enquiry from the website") +
            "&body=" + encodeURIComponent(sendText()) + '">' + T("emailList", "Email the list") + "</a>" +
        "</div>" +
        '<p class="note">' + T("conceptNote2", "No card details, no account, nothing charged. A person from your nearest branch replies with today\u2019s price.") + "</p>" +
      "</div>";
  }

  /* A four-card strip for the home page, built from the same catalogue so the
     two can never disagree. */
  /* Four popular items for the home page, built from the same catalogue so the
     two can never disagree. */
  function renderFeatured() {
    var host = document.querySelector("[data-featured]");
    if (!host) return;
    var picks = ["tv-55", "ac-15", "fr-265", "wm-7"].map(product).filter(Boolean);
    host.innerHTML = picks.map(function (p) {
      var c = cat(p.cat);
      return '<p class="tile"><span class="tile__t">' + esc(p.title) + "</span>" +
        '<span class="tile__d">' + esc(c.label) + " \u00b7 " + esc(p.specs.join(" \u00b7 ")) + "</span></p>";
    }).join("");
  }

  /* --------------------------------------------------------------- filters */
  var state = { cat: "all", q: "", town: "all" };

  function matches(p) {
    if (state.cat !== "all" && p.cat !== state.cat) return false;
    if (state.town !== "all") {
      var towns = p.towns;
      if (towns.indexOf("All showrooms") === -1 && towns.indexOf(state.town) === -1) return false;
    }
    if (!state.q) return true;
    var hay = (p.title + " " + p.specs.join(" ") + " " + p.cat + " " + p.tags.join(" ") + " " + p.towns.join(" ")).toLowerCase();
    return hay.indexOf(state.q) !== -1;
  }

  function renderGrid() {
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
        : PRODUCTS.length + " " + T("products", "products") + " \u00b7 " + CATS.length + " " +
          T("categories", "categories") + " \u00b7 " + T("askPrice", "ask for today's price");
    }
    paintAddButtons();
  }

  function buildChips() {
    var host = document.querySelector("[data-cat-chips]");
    if (!host) return;
    var used = CATS.filter(function (c) {
      return PRODUCTS.some(function (p) { return p.cat === c.id; });
    });
    host.innerHTML =
      '<button class="chip" type="button" data-cat="all" aria-pressed="true">' + T("all", "All") + "</button>" +
      used.map(function (c) {
        return '<button class="chip" type="button" data-cat="' + c.id + '" aria-pressed="false">' + icon(c.art) + esc(c.label) + "</button>";
      }).join("");
  }

  function buildTowns() {
    var sel = document.querySelector("[data-town-select]");
    if (!sel) return;
    var towns = [];
    PRODUCTS.forEach(function (p) {
      p.towns.forEach(function (t) {
        if (t !== "All showrooms" && towns.indexOf(t) === -1) towns.push(t);
      });
    });
    towns.sort();
    sel.innerHTML = '<option value="all">All towns</option>' +
      towns.map(function (t) { return '<option value="' + esc(t) + '">' + esc(t) + "</option>"; }).join("");
  }

  /* --------------------------------------------------------------- events */
  document.addEventListener("click", function (e) {
    var add = e.target.closest("[data-add]");
    if (add) { toggleItem(add.getAttribute("data-add")); return; }

    var remove = e.target.closest("[data-remove]");
    if (remove) { toggleItem(remove.getAttribute("data-remove")); return; }

    var chip = e.target.closest("[data-cat]");
    if (chip) {
      state.cat = chip.getAttribute("data-cat");
      var all = document.querySelectorAll("[data-cat]");
      for (var i = 0; i < all.length; i++) {
        all[i].setAttribute("aria-pressed", all[i] === chip ? "true" : "false");
      }
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
      return;
    }
  });

  var search = document.querySelector("[data-product-search]");
  if (search) {
    search.addEventListener("input", function () {
      state.q = search.value.trim().toLowerCase();
      renderGrid();
    });
  }

  var townSel = document.querySelector("[data-town-select]");
  if (townSel) {
    townSel.addEventListener("change", function () {
      state.town = townSel.value;
      renderGrid();
    });
  }

  /* A card can also be opened from the home page strip. */
  document.addEventListener("click", function (e) {
    var jump = e.target.closest("[data-goto-cat]");
    if (jump) {
      var target = jump.getAttribute("data-goto-cat");
      try { localStorage.setItem("whynot-cat", target); } catch (err) {}
    }
  });

  /* ---------------------------------------------------------------- toast */
  var toast = document.querySelector("[data-toast]");
  var toastTimer;
  function flash(message) {
    if (!toast) return;
    toast.textContent = message;
    toast.setAttribute("data-open", "true");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { toast.setAttribute("data-open", "false"); }, 2200);
  }

  /* the shortlist panel: a sheet on phones, a sticky column on desktop */
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

  /* ----------------------------------------------------------------- init */
  buildChips();
  buildTowns();
  renderFeatured();
  renderGrid();
  renderPanel();
  paintCounts();

  /* Deep link: products.html?q=mixer (from the 404 page's box) or ?cat=fridge. */
  var params = new URLSearchParams(location.search);
  var typed = params.get("q");
  if (typed && search) {
    search.value = typed;
    state.q = typed.trim().toLowerCase();
    renderGrid();
  }
  var wanted = params.get("cat");
  if (!wanted) { try { wanted = localStorage.getItem("whynot-cat"); localStorage.removeItem("whynot-cat"); } catch (e) {} }
  if (wanted) {
    state.cat = wanted;
    var chipEls = document.querySelectorAll("[data-cat]");
    for (var n = 0; n < chipEls.length; n++) {
      chipEls[n].setAttribute("aria-pressed", chipEls[n].getAttribute("data-cat") === wanted ? "true" : "false");
    }
    renderGrid();
  }

  /* redraw the generated markup when the language changes */
  window.WHYNOT_RERENDER = function () { renderGrid(); renderFeatured(); renderPanel(); };

})();
