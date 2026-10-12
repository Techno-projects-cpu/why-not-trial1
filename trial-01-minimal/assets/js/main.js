/* WHYNOT — Trial 01 runtime.
   No dependencies. Nothing here is required for the page to be readable:
   every feature below is a progressive enhancement. */
(function () {
  "use strict";

  var $ = function (sel, ctx) { return (ctx || document).querySelector(sel); };
  var $$ = function (sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); };

  /* ---------------------------------------------------------------- theme
     The initial value is applied by a tiny inline script in <head> so the
     first paint is already the right colour. This part only handles toggles. */
  var root = document.documentElement;
  var STORE_KEY = "whynot-theme";

  function currentTheme() {
    var set = root.getAttribute("data-theme");
    if (set) return set;
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  $$("[data-theme-toggle]").forEach(function (btn) {
    btn.setAttribute("aria-pressed", currentTheme() === "dark" ? "true" : "false");

    btn.addEventListener("click", function () {
      var next = currentTheme() === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      btn.setAttribute("aria-pressed", next === "dark" ? "true" : "false");
      try { localStorage.setItem(STORE_KEY, next); } catch (e) { /* private mode */ }
    });
  });

  /* ------------------------------------------------------- mobile drawer */
  var drawer = $("[data-drawer]");
  var burger = $("[data-drawer-open]");

  function setDrawer(open) {
    if (!drawer || !burger) return;
    drawer.setAttribute("data-open", open ? "true" : "false");
    drawer.setAttribute("aria-hidden", open ? "false" : "true");
    burger.setAttribute("aria-expanded", open ? "true" : "false");
    document.body.style.overflow = open ? "hidden" : "";
    if (open) {
      var first = drawer.querySelector("a, button");
      if (first) first.focus();
    } else {
      burger.focus();
    }
  }

  if (drawer && burger) {
    burger.addEventListener("click", function () {
      setDrawer(drawer.getAttribute("data-open") !== "true");
    });

    $$("[data-drawer-close]").forEach(function (el) {
      el.addEventListener("click", function () { setDrawer(false); });
    });

    $$("a", drawer).forEach(function (a) {
      a.addEventListener("click", function () { setDrawer(false); });
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && drawer.getAttribute("data-open") === "true") setDrawer(false);
    });

    window.addEventListener("resize", function () {
      if (window.innerWidth >= 1000 && drawer.getAttribute("data-open") === "true") setDrawer(false);
    });
  }

  /* ----------------------------------------------------- reveal on scroll
     One observer for the whole page; elements keep opacity 0 in CSS so there
     is no flash, and reduced-motion users get the final state immediately. */
  var revealables = $$("[data-reveal]");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  if (!("IntersectionObserver" in window) || reduce) {
    revealables.forEach(function (el) { el.classList.add("is-in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-in");
        io.unobserve(entry.target);
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.06 });

    revealables.forEach(function (el, i) {
      el.style.transitionDelay = Math.min(i % 4, 3) * 60 + "ms";
      io.observe(el);
    });
  }

  /* ------------------------------------------------------------- counters
     Stats count up once, and only if motion is welcome. */
  var counters = $$("[data-count]");
  if (counters.length && !reduce && "IntersectionObserver" in window) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        cio.unobserve(el);

        var raw = el.getAttribute("data-count");
        var target = parseFloat(raw);
        if (isNaN(target)) { el.textContent = raw; return; }

        var decimals = (raw.split(".")[1] || "").length;
        var start = null;
        var dur = 900;

        function frame(ts) {
          if (start === null) start = ts;
          var p = Math.min((ts - start) / dur, 1);
          var eased = 1 - Math.pow(1 - p, 3);
          el.textContent = (target * eased).toFixed(decimals);
          if (p < 1) requestAnimationFrame(frame);
          else el.textContent = raw;
        }
        requestAnimationFrame(frame);
      });
    }, { threshold: 0.4 });

    counters.forEach(function (el) { cio.observe(el); });
  }

  /* -------------------------------------------------------- copy to clip */
  var toast = $("[data-toast]");
  var toastTimer;

  function flash(message) {
    if (!toast) return;
    toast.textContent = message;
    toast.setAttribute("data-open", "true");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { toast.setAttribute("data-open", "false"); }, 2600);
  }

  $$("[data-copy]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var text = btn.getAttribute("data-copy");
      var done = function () { flash("Copied  " + text); };

      if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(text).then(done, function () { flash("Could not copy — " + text); });
      } else {
        var ta = document.createElement("textarea");
        ta.value = text;
        ta.setAttribute("readonly", "");
        ta.style.position = "absolute";
        ta.style.left = "-9999px";
        document.body.appendChild(ta);
        ta.select();
        try { document.execCommand("copy"); done(); } catch (e) { flash(text); }
        document.body.removeChild(ta);
      }
    });
  });

  /* ------------------------------------------------------------ shop open
     Everything in the contact page reads from one open/closed state, so the
     site stops telling people to visit at 10 pm. Hours are editable here. */
  var OPEN_HOUR = 10;   // 10:00
  var CLOSE_HOUR = 21;  // 21:00  (9 pm)
  var day = new Date();
  var openNow = day.getHours() >= OPEN_HOUR && day.getHours() < CLOSE_HOUR;

  $$("[data-shop-state]").forEach(function (el) {
    el.textContent = openNow ? "Open now" : "Closed now";
    el.setAttribute("data-state", openNow ? "open" : "closed");
  });
  $$("[data-shop-note]").forEach(function (el) {
    el.textContent = openNow
      ? "Open until 9:00 pm today. Walk in and ask for a demo."
      : "Opens at 10:00 am. Leave your number and we'll call you back.";
  });

  /* -------------------------------------------------------------- footer */
  $$("[data-year]").forEach(function (el) { el.textContent = String(new Date().getFullYear()); });
})();
