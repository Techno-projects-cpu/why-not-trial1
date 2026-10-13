function fallbackT(key, english) { return english === undefined ? key : english; }
/* WHYNOT — store directory.
   ---------------------------------------------------------------------------
   ONE SOURCE OF TRUTH. The old site had these 25 addresses copy-pasted into
   markup (and the same two Tanuku addresses duplicated three times). Here they
   live in one array; the page, the search and the map links all read from it.
   Adding a showroom = adding one object. Nothing else to update.
   ---------------------------------------------------------------------------
   Data taken from whynotindia.in/stores on 2026-10-12, wording kept as-is.
   district labels follow the wording used on the current site (see docs/AUDIT.md
   — Andhra Pradesh's 2022 district reorganisation should be applied with the
   client's confirmation).                                               */
(function () {
  "use strict";

  var T = window.WHYNOT_T || fallbackT;

  var STORES = [
    {
      town: "Tanuku", label: "Flagship",
      address: "RS No 24/1, Ground and Cellar, Sri Sowdha Towers, Undrajavaram Road, Tanuku",
      district: "West Godavari", pincode: "534211"
    },
    {
      town: "Tadepalligudem",
      address: "2/1/69, 29th Ward, K N Road, Tadepalligudem",
      district: "West Godavari", pincode: "534101"
    },
    {
      town: "Rajahmundry",
      address: "36-4-17, Near Sai Krishna Theatre Road, Rajahmundry",
      district: "East Godavari", pincode: "533101"
    },
    {
      town: "Bhimadolu",
      address: "5-58, Near Bus Stand, Nallajarla Road, Bhimadolu",
      district: "West Godavari", pincode: "534425"
    },
    {
      town: "Nidadavolu",
      address: "2-2-13, Opp State Bank of India, Nidadavolu",
      district: "West Godavari", pincode: "534301"
    },
    {
      town: "Narasapuram",
      address: "5-4-16, Steemer Road, Narasapuram",
      district: "West Godavari", pincode: "534175"
    },
    {
      town: "Palakollu",
      address: "16-5-6, Shavukarpeta, Palakollu",
      district: "West Godavari", pincode: "534200"
    },
    {
      town: "Jangareddygudem",
      address: "10754, Dhruva Diksha Commercial Complex, Aswarao Peta Road, Jangareddygudem",
      district: "West Godavari", pincode: "534447"
    },
    {
      town: "Devarapalli",
      address: "2-32, Eluru Road, Devarapalli",
      district: "West Godavari", pincode: "534313"
    },
    {
      town: "Amalapuram",
      address: "7-3-52, Yerramalli Vari Street, Amalapuram",
      district: "East Godavari", pincode: "534313"
    },
    {
      town: "Tatipaka",
      address: "7-167, Shop No 1 and 2, Main Road, Razole Mandal, Tatipaka",
      district: "East Godavari", pincode: "533249"
    },
    {
      town: "Ravulapalem",
      address: "8-917/6, Adilakshmi Nagar, Ravulapalem",
      district: "East Godavari", pincode: "533238"
    },
    {
      town: "Mandapeta",
      address: "4-1-34, Revenue Ward 2, Dwarapudi Road, Mandapeta",
      district: "East Godavari", pincode: "533308"
    },
    {
      town: "Eluru",
      address: "22C-1-58, Sai Hemalatha Plaza, GNT Road, Near Karra Vanthena Power Pet, Eluru",
      district: "West Godavari", pincode: "534002"
    },
    {
      town: "Yeleswaram",
      address: "2-2-225, Libgamparthy Road, Beside RTC Bus Stand, Yeleswaram",
      district: "East Godavari", pincode: "533429"
    },
    {
      town: "Pithapuram",
      address: "6-1-8, Opp Municipal Office, Main Road, Pithapuram",
      district: "East Godavari", pincode: "533200"
    },
    {
      town: "Chintalapudi",
      address: "12-128, Near Andhra Bank, Beside IOC Petrol Bunk, Main Road, Chintalapudi",
      district: "West Godavari", pincode: "534460"
    },
    {
      town: "Nallajarla",
      address: "6-45, Eluru Road, Nallajarla",
      district: "West Godavari", pincode: "534112"
    },
    {
      town: "Attili",
      address: "16-40/1, Badeti Complex, Opposite TTD Kalyana Mandapam, Tanuku Road, Attili",
      district: "West Godavari", pincode: "534134"
    },
    {
      town: "Bhimavaram",
      address: "27-1-1B and 24-1-2, Ground Floor, Kodandarama Complex, Juvvalapalem Road, Bhimavaram",
      district: "West Godavari", pincode: "534202"
    },
    {
      town: "Anakapalle",
      address: "Lasya Plaza, Plot No 10, D No 10-16-30, Main Road, Anakapalle",
      district: "Visakhapatnam", pincode: "531002"
    },
    {
      town: "Kakinada",
      address: "The Kakinada Merchants Associations, D No 10/12-1-22, Opp Pindala Cheruvu, Ward No 10, Javahar Street, Kakinada",
      district: "East Godavari", pincode: "533004"
    },
    {
      town: "Kovvur",
      address: "Yuvaraj YSTD Centre, Kovvur",
      district: "East Godavari", pincode: "534350"
    },
    {
      town: "LG Best Shop", label: "Brand store",
      address: "RS No 24/1, Ground and Cellar, Sri Sowdha Towers, Undrajavaram Road, Tanuku",
      district: "West Godavari", pincode: "534211"
    },
    {
      town: "Samsung Smart Plaza", label: "Brand store",
      address: "RS No 24/1, Ground and Cellar, Sri Sowdha Towers, Undrajavaram Road, Tanuku",
      district: "West Godavari", pincode: "534211"
    }
  ];

  var list = document.querySelector("[data-store-list]");
  if (!list) return;

  var countEl = document.querySelector("[data-store-count]");
  var searchEl = document.querySelector("[data-store-search]");
  var chips = Array.prototype.slice.call(document.querySelectorAll("[data-district]"));
  var emptyEl = document.querySelector("[data-store-empty]");
  var clearEl = document.querySelector("[data-store-clear]");

  var state = { q: "", district: "all" };

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  function mapsUrl(store) {
    var q = encodeURIComponent("WHYNOT " + store.town + ", " + store.address +
      ", " + store.district + " district, Andhra Pradesh " + store.pincode);
    return "https://www.google.com/maps/search/?api=1&query=" + q;
  }

  function card(store) {
    var full = store.address + ", " + store.district + " district, Andhra Pradesh " + store.pincode;
    var badge = store.label
      ? '<span class="store__badge">' + escapeHtml(store.label) + "</span>"
      : "";

    return '' +
      '<article class="store" data-town="' + escapeHtml(store.town.toLowerCase()) + '"' +
      ' data-district="' + escapeHtml(store.district) + '"' +
      ' data-search="' + escapeHtml((store.town + " " + store.address + " " + store.district + " " + store.pincode).toLowerCase()) + '">' +
        '<div class="store__head">' +
          '<h3 class="store__name">' + escapeHtml(store.town) + "</h3>" +
          '<span class="store__town">' + escapeHtml(store.district) + " · " + escapeHtml(store.pincode) + "</span>" +
          badge +
        "</div>" +
        '<p class="store__addr">' + escapeHtml(full) + "</p>" +
        '<div class="store__actions">' +
          '<a class="btn btn--ghost btn--sm" href="' + mapsUrl(store) + '" target="_blank" rel="noopener noreferrer">' +
            T("directions", "Directions") +
            '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M7 17 17 7M17 7H8M17 7v9"/></svg>' +
          "</a>" +
          '<button class="btn btn--sm" type="button" data-copy="' + escapeHtml(full) + '">Copy address</button>' +
        "</div>" +
      "</article>";
  }

  function matches(el) {
    var d = el.getAttribute("data-district");
    if (state.district !== "all" && d !== state.district) return false;
    if (!state.q) return true;
    return el.getAttribute("data-search").indexOf(state.q) !== -1;
  }

  function render() {
    list.innerHTML = STORES.map(card).join("");
    apply();
  }

  function apply() {
    var nodes = Array.prototype.slice.call(list.children);
    var shown = 0;

    nodes.forEach(function (el) {
      var ok = matches(el);
      el.hidden = !ok;
      if (ok) shown++;
    });

    if (countEl) {
      countEl.textContent = state.q || state.district !== "all"
        ? "Showing " + shown + " of " + STORES.length + " showrooms"
        : STORES.length + " showrooms · updated 12 Oct 2026";
    }
    if (emptyEl) emptyEl.hidden = shown !== 0;
  }

  searchEl &&
    searchEl.addEventListener("input", function () {
      state.q = searchEl.value.trim().toLowerCase();
      apply();
    });

  chips.forEach(function (chip) {
    chip.addEventListener("click", function () {
      state.district = chip.getAttribute("data-district");
      chips.forEach(function (c) {
        c.setAttribute("aria-pressed", c === chip ? "true" : "false");
      });
      apply();
    });
  });

  clearEl &&
    clearEl.addEventListener("click", function () {
      state.q = "";
      state.district = "all";
      if (searchEl) searchEl.value = "";
      chips.forEach(function (c) {
        c.setAttribute("aria-pressed", c.getAttribute("data-district") === "all" ? "true" : "false");
      });
      apply();
      if (searchEl) searchEl.focus();
    });

  render();

  /* redraw the generated markup when the language changes */
  window.WHYNOT_RERENDER = function () { apply(); };

})();
