/* WHYNOT — the language switch.
   ---------------------------------------------------------------------------
   Three languages: English, Telugu and Hindi. The Telugu and Hindi copy in here
   was written in those languages rather than translated from the English — it is
   shorter, it uses the words a shop in Tanuku would use, and where the English
   needs a paragraph the Telugu often needs four words.

   How it works: the page is authored in English. On first load this file
   photographs that English (text and markup) per element, then any switch simply
   swaps text in and out. Nothing is re-fetched and the page works with
   JavaScript switched off — because with JS off it never switches.
   --------------------------------------------------------------------------- */
window.WHYNOT_I18N = (function () {
  "use strict";

  var STRINGS = {"te":{"Good to know":"తెలుసుకోవాల్సినవి","Shop":"వస్తువులు","Send enquiry":"పంపండి","Mobile number":"మొబైల్ నంబర్","We call with the price":"ధర చెప్పి ఫోన్ చేస్తాం","Washing machines":"వాషింగ్ మెషీన్లు","East Godavari":"తూర్పు గోదావరి","Air conditioners":"ఏసీలు","Catalogue":"వస్తువులు","Or just call":"లేదా ఫోన్ చేయండి","Partners":"భాగస్వాములు","Cleaning":"క్లీనింగ్","Open now":"ఇప్పుడు తెరిచి ఉంది","Search the catalogue":"జాబితాలో వెతకండి","Today":"ఇప్పుడు","In their words":"వాళ్ల మాటల్లో","Find a showroom":"షాపు వెతుకు","Company":"కంపెనీ","Your name":"మీ పేరు","Visakhapatnam":"విశాఖపట్నం","Already bought from us?":"ఇదివరకే కొన్నారా?","Contact":"సంప్రదించండి","Kitchen":"వంటగది","0 items":"0 వస్తువులు","Mobiles":"మొబైల్స్","Error 404":"ఎర్రర్ 404","Shop by category":"ఏం కావాలి?","About us":"మా గురించి","All":"అన్నీ","Service":"సర్వీస్","Send an enquiry":"విచారణ పంపండి","How buying works here":"ఇక్కడ కొనడం ఎలా","All towns":"అన్ని ఊళ్లు","West Godavari":"పశ్చిమ గోదావరి","Stock is local":"స్టాక్ ఇక్కడే","Refrigerators":"ఫ్రిజ్‌లు","Home":"మొదటి పేజీ","Televisions":"టెలివిజన్లు","Showrooms":"మా షాపులు","What are you looking for?":"మీకు ఏం కావాలి?","Add what you like":"నచ్చినవి జోడించండి","Popular right now":"ఇప్పుడు డిమాండ్","Skip to content":"కంటెంట్‌కు వెళ్లు","The name is the question":"పేరే ప్రశ్న","Send it to us":"మాకు పంపండి","add":"+ జాబితాలో చేర్చు","added":"జాబితాలో ఉంది","removed":"జాబితా నుంచి తీసేశాం","item":"ఐటమ్","items":"ఐటమ్స్","addedToast":"జాబితాలో చేర్చాం","wa":"WhatsApp లో పంపు","emailList":"మెయిల్ చేయండి","noMatch":"అలాంటిది ఏమీ లేదు","clearF":"ఫిల్టర్లు తీసేయి","emptyList":"జాబితా ఖాళీగా ఉంది","remove":"తీసేయి","directions":"మ్యాప్‌లో చూడండి","copyAddr":"చిరునామా కాపీ","emptyHelp":"ధర కావాల్సినవి జోడించండి. పంపే వరకు ఇదే ఫోన్‌లో ఉంటుంది.","showing":"చూపిస్తున్నాం:","of":"మొత్తం","all":"అన్నీ","callShort":"కాల్","products":"వస్తువులు","showrooms":"షాపులు","copied":"కాపీ అయింది","openNow":"ఇప్పుడు తెరిచి ఉంది","closedNow":"ఇప్పుడు మూసి ఉంది"},"hi":{"Good to know":"जान लीजिए","Shop":"सामान","Send enquiry":"भेजें","Mobile number":"मोबाइल नंबर","We call with the price":"दाम बताकर फ़ोन करेंगे","Washing machines":"वॉशिंग मशीन","East Godavari":"पूर्वी गोदावरी","Air conditioners":"एयर कंडीशनर","Catalogue":"सामान","Or just call":"या सीधे फ़ोन करें","Partners":"साझेदार","Cleaning":"सफ़ाई","Open now":"अभी खुला है","Search the catalogue":"सूची में खोजें","Today":"आज","In their words":"उनके शब्दों में","Find a showroom":"दुकान खोजें","Company":"कंपनी","Your name":"आपका नाम","Visakhapatnam":"विशाखापट्टनम","Already bought from us?":"पहले खरीदा है?","Contact":"संपर्क","Kitchen":"रसोई","0 items":"0 सामान","Mobiles":"मोबाइल","Error 404":"एरर 404","Shop by category":"क्या चाहिए?","About us":"हमारे बारे में","All":"सब","Service":"सर्विस","Send an enquiry":"पूछताछ भेजें","How buying works here":"यहाँ खरीदना कैसे होता है","All towns":"सभी शहर","West Godavari":"पश्चिम गोदावरी","Stock is local":"स्टॉक यहीं है","Refrigerators":"फ्रिज","Home":"होम","Televisions":"टेलीविज़न","Showrooms":"हमारी दुकानें","What are you looking for?":"आपको क्या चाहिए?","Add what you like":"पसंद का जोड़ें","Popular right now":"अभी ट्रेंड में","Skip to content":"सीधे सामग्री पर जाएँ","The name is the question":"नाम ही सवाल है","Send it to us":"हमें भेजिए","add":"+ सूची में डालें","added":"सूची में है","removed":"सूची से हटा दिया","item":"आइटम","items":"आइटम","addedToast":"सूची में डाल दिया","wa":"WhatsApp पर भेजें","emailList":"ईमेल करें","noMatch":"ऐसा कुछ नहीं मिला","clearF":"फ़िल्टर हटाएँ","emptyList":"सूची खाली है","remove":"हटाएँ","directions":"मैप में देखें","copyAddr":"पता कॉपी","emptyHelp":"जिसका दाम चाहिए वह जोड़ें. भेजने तक यहीं इस फ़ोन में रहता है.","showing":"दिखा रहे हैं:","of":"कुल","all":"सभी","callShort":"कॉल","products":"सामान","showrooms":"दुकानें","copied":"कॉपी हो गया","openNow":"अभी खुला है","closedNow":"अभी बंद है"}};
  var PATTERNS = [{"re":"^([0-9]+) products · sample catalogue, real prices on request$","te":"$1 వస్తువులు · ఇది నమూనా జాబితా, ధరలు అడగండి","hi":"$1 सामान · यह नमूना सूची है, दाम पूछिए"},{"re":"^([0-9]+) products across ([0-9]+) categories$","te":"$1 వస్తువులు · $2 విభాగాలు","hi":"$1 सामान · $2 श्रेणियाँ"},{"re":"^([0-9]+) products · ([0-9]+) categories · ask for today(?:'|’|&rsquo;)s price$","te":"$1 వస్తువులు · $2 విభాగాలు · ఈరోజు ధర అడగండి","hi":"$1 सामान · $2 श्रेणियाँ · आज का दाम पूछें"},{"re":"^([0-9]+) products · 10 categories · ask for today(?:'|’|&rsquo;)s price$","te":"$1 వస్తువులు · 10 విభాగాలు · ఈరోజు ధర అడగండి","hi":"$1 सामान · 10 श्रेणियाँ · आज का दाम पूछें"},{"re":"^([0-9]+) (?:items?|item) — we will price it and call you$","te":"$1 — ధర చెప్పి ఫోన్ చేస్తాం","hi":"$1 — दाम बताकर फोन करेंगे"},{"re":"^Ask (?:for )?today(?:'|’|&rsquo;)s price$","te":"ఈరోజు ధర అడగండి","hi":"आज का दाम पूछें"},{"re":"^Remove","te":"తీసేయి","hi":"हटाएँ"},{"re":"^Showing ([0-9]+) of ([0-9]+) products$","te":"చూపిస్తున్నాం: $1 / $2","hi":"दिखा रहे हैं: $1 / $2"},{"re":"^(In stock at) ","te":"స్టాక్ ఉన్నది: ","hi":"स्टॉक है: "},{"re":"^([0-9]+) products$","te":"$1 వస్తువులు","hi":"$1 सामान"},{"re":"^([0-9]+) items?$","te":"$1 వస్తువులు","hi":"$1 सामान"},{"re":"^([0-9]+) showrooms$","te":"$1 షాపులు","hi":"$1 दुकानें"},{"re":"^([0-9]+) towns$","te":"$1 ఊళ్లు","hi":"$1 शहर"},{"re":"^(Showing) ([0-9]+) of ([0-9]+)$","te":"చూపిస్తున్నాం: $2 / $3","hi":"दिखा रहे हैं: $2 / $3"}];
  var ALIAS = {"Add to list":"add","+ Add to my list":"add","In my list":"added","Removed from your list":"removed","item":"item","items":"items","Added to your list":"addedToast","In your list":"added","Send on WhatsApp":"wa","Email the list":"emailList","Nothing matches that":"noMatch","Clear filters":"clearF","Your list is empty":"emptyList","Remove":"remove","Directions":"directions","Copy address":"copyAddr","Hit “add to list” on anything you want priced. It stays on this device until you send it.":"emptyHelp","Showing":"showing","of":"of","All":"all","Call":"callShort","products":"products","showrooms":"showrooms","Add anything you want priced. It stays on this device until you send it.":"emptyHelp","Copied":"copied","Open now":"openNow","Closed now":"closedNow","&#10003; In my list":"added","Good to know":"Good to know","Shop":"Shop","Send enquiry":"Send enquiry","Mobile number":"Mobile number","We call with the price":"We call with the price","Washing machines":"Washing machines","East Godavari":"East Godavari","Air conditioners":"Air conditioners","Catalogue":"Catalogue","Or just call":"Or just call","Partners":"Partners","Cleaning":"Cleaning","Search the catalogue":"Search the catalogue","Today":"Today","In their words":"In their words","Find a showroom":"Find a showroom","Company":"Company","Your name":"Your name","Visakhapatnam":"Visakhapatnam","Already bought from us?":"Already bought from us?","Contact":"Contact","Kitchen":"Kitchen","0 items":"0 items","Mobiles":"Mobiles","Error 404":"Error 404","Shop by category":"Shop by category","About us":"About us","Service":"Service","Send an enquiry":"Send an enquiry","How buying works here":"How buying works here","All towns":"All towns","West Godavari":"West Godavari","Stock is local":"Stock is local","Refrigerators":"Refrigerators","Home":"Home","Televisions":"Televisions","Showrooms":"Showrooms","What are you looking for?":"What are you looking for?","Add what you like":"Add what you like","Popular right now":"Popular right now","Skip to content":"Skip to content","The name is the question":"The name is the question","Send it to us":"Send it to us"};
  var KEY = "whynot-lang";
  var LANGS = ["en", "te", "hi"];
  var originals = null;   /* the English, captured once */

  function elements() {
    return document.querySelectorAll("[data-i18n], [data-i18n-html]");
  }

  function capture() {
    originals = [];
    var list = elements();
    for (var i = 0; i < list.length; i++) {
      var el = list[i];
      originals.push(el.hasAttribute("data-i18n-html") ? el.innerHTML : el.textContent);
    }
    var fields = document.querySelectorAll("[data-i18n-ph]");
    originals.fields = [];
    for (var j = 0; j < fields.length; j++) originals.fields.push(fields[j].placeholder);
  }

  function text(lang, key) {
    if (lang === "en") return null;
    var table = STRINGS[lang] || {};
    return table[key] || null;
  }

  function apply(lang) {
    if (LANGS.indexOf(lang) === -1) lang = "en";
    if (!originals) capture();
    document.documentElement.lang = lang === "en" ? "en-IN" : lang;

    var list = elements();
    for (var i = 0; i < list.length; i++) {
      var el = list[i];
      var key = el.getAttribute("data-i18n-html") || el.getAttribute("data-i18n");
      var value = text(lang, key);
      if (value === null) value = originals[i];
      if (el.hasAttribute("data-i18n-html")) el.innerHTML = value;
      else el.textContent = value;
    }

    var fields = document.querySelectorAll("[data-i18n-ph]");
    for (var j = 0; j < fields.length; j++) {
      var pk = fields[j].getAttribute("data-i18n-ph");
      fields[j].placeholder = text(lang, pk) || originals.fields[j];
    }

    var buttons = document.querySelectorAll("[data-lang]");
    for (var b = 0; b < buttons.length; b++) {
      buttons[b].setAttribute("aria-pressed", buttons[b].getAttribute("data-lang") === lang ? "true" : "false");
    }

    try { localStorage.setItem(KEY, lang); } catch (e) { /* private mode */ }

    /* let the catalogue, the shortlist and the form redraw their own text */
    translateTree(document, lang);
    if (typeof window.WHYNOT_RERENDER === "function") window.WHYNOT_RERENDER();
    translateTree(document, lang);
    watch(lang);
    document.dispatchEvent(new CustomEvent("whynot:lang", { detail: { lang: lang } }));
  }

  function T(key, fallback) {
    var lang = document.documentElement.lang;
    var value = text(lang, key);
    return value === null || value === undefined ? (fallback === undefined ? key : fallback) : value;
  }

  document.addEventListener("click", function (e) {
    var btn = e.target.closest ? e.target.closest("[data-lang]") : null;
    if (btn) apply(btn.getAttribute("data-lang"));
  });

  function boot() {
    var saved = null;
    try { saved = localStorage.getItem(KEY); } catch (e) { /* ignore */ }
    capture();                       /* always capture English first */
    if (saved && saved !== "en") apply(saved);
  }

  /* A second pass over the DOM, for markup the catalogue builds at runtime. The
     scripts emit English; this translates whatever leaf text matches a phrase we
     know, which is cheaper and far less brittle than threading every string
     through a lookup. */
  var REVERSE = (function () {
    var map = {};
    var all = Object.keys(STRINGS.te || {});
    for (var i = 0; i < all.length; i++) map[normalise(all[i])] = all[i];
    return map;
  })();

  function normalise(s) {
    return String(s).replace(/\s+/g, " ").trim();
  }

  function translateText(node, lang) {
    var parent = node.parentNode;
    if (!parent) return;
    var tag = parent.nodeName.toLowerCase();
    if (tag === "script" || tag === "style" || tag === "svg" || (parent.closest && parent.closest("svg"))) return;
    var raw = node.nodeValue;
    if (!raw || !raw.trim()) return;
    var text0 = normalise(raw);

    /* phrases carrying dynamic content: "In stock at Tanuku", "Showing 5 of 17" */
    for (var p = 0; p < PATTERNS.length; p++) {
      var m = text0.match(new RegExp(PATTERNS[p].re));
      if (!m) continue;
      var out = PATTERNS[p][lang] || PATTERNS[p].en;
      for (var g = m.length - 1; g >= 1; g--) out = out.split("$" + g).join(m[g]);
      node.nodeValue = out;
      return;
    }

    /* exact phrases — in the page's own wording, or a phrase the scripts make */
    var key = REVERSE[text0] || ALIAS[text0];
    if (!key) return;
    var value = text(lang, key);
    if (value !== null) node.nodeValue = value;
  }

  function translateTree(root, lang) {
    if (lang === "en") return;
    /* Walk TEXT NODES, not elements: a button written as
         <a class="btn"> <svg class="doodle">…</svg> Directions </a>
       has a child element, so an element-level pass would skip it — which is
       exactly what it did the first time this was written. */
    var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null);
    var nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    for (var i = 0; i < nodes.length; i++) translateText(nodes[i], lang);
  }

  /* The catalogue, the shortlist and the showroom list redraw themselves long
     after a language was chosen — searching, filtering, adding an item. A watch
     on the DOM translates whatever they produce, so a phrase generated at any
     time is still in the reader's language. Only childList is watched: the pass
     itself writes text values, which cannot loop back into it. */
  var observer = null;

  function watch(lang) {
    if (observer) { observer.disconnect(); observer = null; }
    if (lang === "en" || !window.MutationObserver) return;
    observer = new MutationObserver(function (records) {
      for (var i = 0; i < records.length; i++) {
        var added = records[i].addedNodes;
        for (var j = 0; j < added.length; j++) {
          var node = added[j];
          if (node.nodeType === 1) translateTree(node, lang);
          else if (node.nodeType === 3 && node.parentNode && !(node.parentNode.closest && node.parentNode.closest("svg"))) {
            translateText(node, lang);
          }
        }
      }
    });
    observer.observe(document.body, { childList: true, subtree: true });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();

  return { apply: apply, t: T, STRINGS: STRINGS, KEY: KEY, translateTree: translateTree };
})();

/* The scripts build markup later than this file runs, so give them a handle. */
window.WHYNOT_T = function (key, fallback) { return window.WHYNOT_I18N.t(key, fallback); };
