function fallbackT(key, english) { return english === undefined ? key : english; }
/* WHYNOT — Trial 07 · Slate & Rail · runtime.
   Mode switch, the mobile tab bar, reveals, counters and the copy button.
   There is no drawer: navigation is a rail on desktop and a tab bar on phones.
   --------------------------------------------------------------------------- */
(function () {
  "use strict";

  var T = window.WHYNOT_T || fallbackT;

  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ---------------------------------------------------------- the mode
     Light and dark are both designed palettes, not an inverted one. The mode is
     applied before paint by the inline script in <head>; this keeps the button
     in step and remembers the choice. */
  var modeBtn = $("[data-mode-toggle]");
  var modeState = $("[data-mode-state]");

  function setMode(mode, remember) {
    document.documentElement.setAttribute("data-mode", mode);
    if (modeBtn) {
      modeBtn.setAttribute("aria-pressed", mode === "dark" ? "true" : "false");
      modeBtn.setAttribute("aria-label", mode === "dark" ? "Switch to light mode" : "Switch to dark mode");
    }
    if (modeState) modeState.textContent = mode === "dark" ? "Dark mode on" : "Light mode on";
    var meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute("content", mode === "dark" ? "#0b0d12" : "#ffffff");
    if (remember) { try { localStorage.setItem("whynot-mode", mode); } catch (e) {} }
  }

  if (modeBtn) {
    setMode(document.documentElement.getAttribute("data-mode") === "dark" ? "dark" : "light", false);
    modeBtn.addEventListener("click", function () {
      setMode(document.documentElement.getAttribute("data-mode") === "dark" ? "light" : "dark", true);
    });
  }

  /* if the reader has not chosen, follow the system as it changes */
  if (window.matchMedia) {
    var mq = window.matchMedia("(prefers-color-scheme: dark)");
    var follow = function (e) {
      var saved = null;
      try { saved = localStorage.getItem("whynot-mode"); } catch (err) {}
      if (!saved) setMode(e.matches ? "dark" : "light", false);
    };
    if (mq.addEventListener) mq.addEventListener("change", follow);
    else if (mq.addListener) mq.addListener(follow);
  }

  /* the shortlist sheet on phones: Escape closes it, tapping the backdrop too */
  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    var aside = document.querySelector("[data-aside]");
    if (aside && aside.getAttribute("data-open") === "true") aside.setAttribute("data-open", "false");
  });

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
      var done = function () { flash(T("copied", "Copied") + "  " + text); };
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
    el.textContent = openNow ? T("openNow", "Open now") : T("closedNow", "Closed now");
  });
  $$("[data-shop-note]").forEach(function (el) {
    el.textContent = openNow
      ? T("openNote", "Open until 9 pm today \u2014 walk in and ask for a demo.")
      : T("closedNote", "We open at 10 am. Leave your number and we'll ring you back.");
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
