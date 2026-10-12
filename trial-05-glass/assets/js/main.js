function fallbackT(key, english) { return english === undefined ? key : english; }
/* WHYNOT — Trial 05 · Glass & Glow runtime. Small, dependency-free, all progressive. */
(function () {
  "use strict";

  var T = window.WHYNOT_T || fallbackT;

  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ------------------------------------------------------- mobile drawer */
  var drawer = $("[data-drawer]");
  var burger = $("[data-drawer-open]");

  function setDrawer(open) {
    if (!drawer || !burger) return;
    drawer.setAttribute("data-open", open ? "true" : "false");
    drawer.setAttribute("aria-hidden", open ? "false" : "true");
    burger.setAttribute("aria-expanded", open ? "true" : "false");
    document.body.style.overflow = open ? "hidden" : "";
    if (open) { var f = drawer.querySelector("a, button"); if (f) f.focus(); }
    else { burger.focus(); }
  }

  if (drawer && burger) {
    burger.addEventListener("click", function () { setDrawer(drawer.getAttribute("data-open") !== "true"); });
    $$("[data-drawer-close]").forEach(function (el) { el.addEventListener("click", function () { setDrawer(false); }); });
    $$("a", drawer).forEach(function (a) { a.addEventListener("click", function () { setDrawer(false); }); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && drawer.getAttribute("data-open") === "true") setDrawer(false);
    });
    window.addEventListener("resize", function () {
      if (window.innerWidth >= 1000 && drawer.getAttribute("data-open") === "true") setDrawer(false);
    });
  }

  /* --------------------------------------------------- reveal on scroll */
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
    }, { rootMargin: "0px 0px -6% 0px", threshold: 0.05 });
    revealables.forEach(function (el, i) {
      el.style.transitionDelay = Math.min(i % 5, 4) * 55 + "ms";
      io.observe(el);
    });
  }

  /* --------------------------------------------------------- copy to clip */
  var toast = $("[data-toast]");
  var toastTimer;
  function flash(msg) {
    if (!toast) return;
    toast.textContent = msg;
    toast.setAttribute("data-open", "true");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { toast.setAttribute("data-open", "false"); }, 2200);
  }

  $$("[data-copy]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var text = btn.getAttribute("data-copy");
      var done = function () { flash("Copied  " + text); };
      if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(text).then(done, function () { flash(text); });
      } else {
        var ta = document.createElement("textarea");
        ta.value = text; ta.setAttribute("readonly", ""); ta.style.position = "absolute"; ta.style.left = "-9999px";
        document.body.appendChild(ta); ta.select();
        try { document.execCommand("copy"); done(); } catch (e) { flash(text); }
        document.body.removeChild(ta);
      }
    });
  });

  /* ------------------------------------------------- open / closed state */
  var OPEN_HOUR = 10, CLOSE_HOUR = 21;
  var hour = new Date().getHours();
  var openNow = hour >= OPEN_HOUR && hour < CLOSE_HOUR;

  $$("[data-shop-state]").forEach(function (el) {
    el.textContent = openNow ? "Open now" : "Closed now";
  });
  $$("[data-shop-note]").forEach(function (el) {
    el.textContent = openNow
      ? "Open until 9 pm today — walk in and ask for a demo."
      : "We open at 10 am. Leave your number and we'll ring you back.";
  });

  /* ------------------------------------------------------------ counters */
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
        function frame(ts) {
          if (start === null) start = ts;
          var p = Math.min((ts - start) / 850, 1);
          var eased = 1 - Math.pow(1 - p, 3);
          el.textContent = (target * eased).toFixed(decimals);
          if (p < 1) requestAnimationFrame(frame); else el.textContent = raw;
        }
        requestAnimationFrame(frame);
      });
    }, { threshold: 0.4 });
    counters.forEach(function (el) { cio.observe(el); });
  }

  /* ---------------------------------------------------------------- year */
  $$("[data-year]").forEach(function (el) { el.textContent = String(new Date().getFullYear()); });
})();
