function fallbackT(key, english) { return english === undefined ? key : english; }
/* WHYNOT — Trial 07 · Slate & Rail · showroom directory.
   The same 25 addresses as every other trial, grouped by district — a
   directory you read down, in a design with no cards in it.
   --------------------------------------------------------------------------- */
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
  var emptyEl = document.querySelector("[data-store-empty]");
  var clearEl = document.querySelector("[data-store-clear]");
  var chips = Array.prototype.slice.call(document.querySelectorAll("[data-district]"));
  var state = { q: "", district: "all" };

  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function icon(id) {
    return '<svg class="icon" aria-hidden="true"><use href="#' + id + '"></use></svg>';
  }
  function mapsUrl(s) {
    return "https://www.google.com/maps/search/?api=1&query=" + encodeURIComponent(
      "WHYNOT " + s.town + ", " + s.address + ", " + s.district + " district, Andhra Pradesh " + s.pincode);
  }

  function card(s) {
    var full = s.town + " \u00b7 " + s.address + ", " + s.district + " district, Andhra Pradesh " + s.pincode;
    return '' +
      '<article class="store" data-district="' + esc(s.district) + '" data-search="' +
        esc((s.town + " " + s.address + " " + s.district + " " + s.pincode).toLowerCase()) + '">' +
        '<div class="store__top">' +
          '<span class="store__name">' + esc(s.town) + "</span>" +
          (s.label ? '<span class="badge">' + esc(s.label) + "</span>" : "") +
          '<span class="note mono">' + esc(s.pincode) + "</span>" +
        "</div>" +
        '<p class="store__addr">' + esc(full) + "</p>" +
        '<div class="store__acts">' +
          '<a class="btn btn--sm" href="' + mapsUrl(s) + '" target="_blank" rel="noopener noreferrer">' +
            icon("i-pin") + " " + T("directions", "Directions") + "</a>" +
          '<button class="btn btn--sm btn--ghost" type="button" data-copy="' + esc(full) + '">' +
            icon("i-copy") + " " + T("copyAddr", "Copy address") + "</button>" +
        "</div>" +
      "</article>";
  }

  /* Grouped by district: a heading per revenue district, then its branches. */
  function render() {
    var districts = [];
    STORES.forEach(function (s) {
      if (districts.indexOf(s.district) === -1) districts.push(s.district);
    });
    districts.sort();
    list.innerHTML = districts.map(function (d) {
      var branches = STORES.filter(function (s) { return s.district === d; });
      return '<section class="dir__group" data-group="' + esc(d) + '">' +
        "<h3>" + esc(d) + " \u00b7 " + branches.length + " " + T("showrooms", "showrooms") + "</h3>" +
        '<div class="dir__items">' + branches.map(card).join("") + "</div>" +
      "</section>";
    }).join("");
  }

  function matches(el) {
    if (state.district !== "all" && el.getAttribute("data-district") !== state.district) return false;
    if (!state.q) return true;
    return el.getAttribute("data-search").indexOf(state.q) !== -1;
  }

  function apply() {
    var nodes = Array.prototype.slice.call(list.children);
    var shown = 0;
    nodes.forEach(function (el) {
      var ok = matches(el);
      el.hidden = !ok;
      if (ok) shown++;
    });
    /* hide a district heading whose branches are all filtered out */
    Array.prototype.slice.call(document.querySelectorAll("[data-group]")).forEach(function (group) {
      var any = Array.prototype.slice.call(group.querySelectorAll(".store")).some(function (el) { return !el.hidden; });
      group.hidden = !any;
      if ("data-count" in group) group.setAttribute("data-count", String(any));
    });
    if (countEl) {
      countEl.textContent = state.q || state.district !== "all"
        ? T("showing", "Showing") + " " + shown + " " + T("of", "of") + " " + STORES.length
        : STORES.length + " " + T("showrooms", "showrooms") + " \u00b7 " + T("twentyThreeTowns", "23 towns") +
          " \u00b7 " + T("oneHelpline", "1 helpline");
    }
    if (emptyEl) emptyEl.hidden = shown !== 0;
  }

  render();

  searchEl && searchEl.addEventListener("input", function () {
    state.q = searchEl.value.trim().toLowerCase();
    apply();
  });

  chips.forEach(function (chip) {
    chip.addEventListener("click", function () {
      state.district = chip.getAttribute("data-district");
      chips.forEach(function (c) { c.setAttribute("aria-pressed", c === chip ? "true" : "false"); });
      apply();
    });
  });

  clearEl && clearEl.addEventListener("click", function () {
    state = { q: "", district: "all" };
    if (searchEl) searchEl.value = "";
    chips.forEach(function (c) { c.setAttribute("aria-pressed", c.getAttribute("data-district") === "all" ? "true" : "false"); });
    apply();
    if (searchEl) searchEl.focus();
  });

  apply();

  /* redraw the generated markup when the language changes */
  window.WHYNOT_RERENDER = function () { apply(); };

})();
