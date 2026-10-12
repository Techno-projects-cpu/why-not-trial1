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

  var STRINGS = {"te":{"Search: TV, fridge, 1.5 ton…":"వెతకండి: TV, ఫ్రిజ్, 1.5 టన్…","Air conditioners":"ఏసీలు","Big brands.<br>Small towns.<br>Why not?":"పెద్ద బ్రాండ్లు.<br>మన ఊరిలోనే.<br>ఎందుకు కాదు?","Years since 1994":"1994 నుంచి ఏళ్లు","Add anything you're curious about to <strong>my list</strong>, send it in one tap, and someone from your nearest branch replies with today's price and stock. No card details, no checkout maze.":"నచ్చినవి <strong>నా జాబితా</strong>లో పెట్టండి. ఒక్క ట్యాప్‌లో పంపండి. మీ బ్రాంచ్ నుంచి ధర, స్టాక్ చెప్తారు. కార్డ్ డిటెయిల్స్ అవసరం లేదు.","Showrooms":"మా షాపులు","Visakhapatnam":"విశాఖపట్నం","Cleaning":"క్లీనింగ్","Open now":"ఇప్పుడు తెరిచి ఉంది","0 items":"0 వస్తువులు","All":"అన్నీ","Come over":"కొట్టుకి రండి","Catalogue":"వస్తువులు","Showrooms, 23 towns":"23 ఊళ్లలో షోరూమ్లు","All towns":"అన్ని ఊళ్లు","Build a list while you browse. Nothing is charged and no account is needed.":"చూస్తూనే జాబితా చేసుకోండి. డబ్బు ఏమీ కట్టాల్సిన అవసరం లేదు, అకౌంట్ లేదు.","Send it":"పంపండి","Products sold":"అమ్మిన వస్తువులు","Your town":"మీ ఊరు","Skip to content":"కంటెంట్‌కు వెళ్లు","Names only — no third-party logos were lifted for this concept.":"పేర్లు మాత్రమే — ఈ డిజైన్ కోసం ఎవరి లోగోనూ వాడలేదు.","Pick what you like.<br>We'll price it.":"నచ్చినవి ఎంచుకోండి.<br>ధర మేం చెప్తాం.","Lighting":"లైటింగ్","Everything<br>you'd expect":"మీకు కావాల్సినవి<br>అన్నీ","Town, district or pincode…":"ఊరు, జిల్లా, పిన్ కోడ్…","East Godavari":"తూర్పు గోదావరి","West Godavari":"పశ్చిమ గోదావరి","What are you looking for?":"మీకు ఏం కావాలి?","About us":"మా గురించి","Old link, moved page, or a typo in the address. Nothing is lost — the showrooms are all where you left them.":"పాత లింక్, తరిగిన పేజీ, లేదా అడ్రస్‌లో తప్పు. ఏం పోలేదు — షాపులన్నీ ఉన్నచోటే ఉన్నాయి.","Audio":"ఆడియో","Water & geysers":"నీళ్లు, గీజర్లు","Refrigerators":"ఫ్రిజ్‌లు","What people<br>actually ask for":"జనం అడిగేవి<br>ఇవే","Televisions":"టెలివిజన్లు","Search the catalogue":"జాబితాలో వెతకండి","Stock is local":"స్టాక్ ఇక్కడే","Mobiles":"మొబైల్స్","Single & double door":"సింగిల్, డబుల్ డోర్","Your name":"మీ పేరు","Customers served":"కస్టమర్లు","Shop":"వస్తువులు","Before you<br>drive over":"బయలుదేరే<br>ముందు","Brand stores in Tanuku":"తనుకులో బ్రాండ్ స్టోర్లు","Come and see it in person":"ఒక్కసారి వచ్చి చూడండి","Kitchen":"వంటగది","Washing machines":"వాషింగ్ మెషీన్లు","Open until 9 pm today.":"ఈరోజు రాత్రి 9 వరకు తెరిచి ఉంది.","Brand warranty runs through each manufacturer's authorised service network, and WHYNOT coordinates it for you.":"వారంటీ కంపెనీ అధికారిక సర్వీస్ నెట్‌వర్క్ ద్వారానే నడుస్తుంది. సమన్వయం WHYNOT చేస్తుంది.","Hours":"టైమింగ్","Contact":"సంప్రదించండి","Mobile number":"మొబైల్ నంబర్","Why not…":"ఎందుకు కాదు…","No ticket numbers, no “within 48 hours”. Leave your number and someone from your nearest showroom rings you between 10 am and 9 pm.":"టికెట్ నంబర్లు లేవు, “48 గంటల్లో” లేదు. నంబర్ ఇవ్వండి — మీ దగ్గరి షాప్ నుంచి 10 – 9 మధ్య ఫోన్ వస్తుంది.","Four questions WHYNOT has answered the same way since an LML showroom in Tanuku in 1994.":"1994లో తనుకులో మొదటి షోరూమ్ నుంచి ఈ నాలుగు ప్రశ్నలకు మా జవాబు మారలేదు.","Company":"కంపెనీ","My list":"నా జాబితా","Home":"మొదటి పేజీ","Today":"ఇప్పుడు","About":"మా గురించి","Already bought from us?":"ఇదివరకే కొన్నారా?","add":"+ జాబితాలో చేర్చు","added":"జాబితాలో ఉంది","removed":"జాబితా నుంచి తీసేశాం","item":"ఐటమ్","items":"ఐటమ్స్","addedToast":"జాబితాలో చేర్చాం","wa":"WhatsApp లో పంపు","browse":"వస్తువులు చూడండి","noMatch":"అలాంటిది ఏమీ లేదు","clearF":"ఫిల్టర్లు తీసేయి","emptyList":"జాబితా ఖాళీగా ఉంది","askAbout":"దీని గురించి అడగండి","remove":"తీసేయి","directions":"మ్యాప్‌లో చూడండి","copyAddr":"చిరునామా కాపీ","showing":"చూపిస్తున్నాం:","of":"మొత్తం","all":"అన్నీ","callShort":"కాల్","categories":"విభాగాలు","products":"వస్తువులు","showrooms":"షాపులు","twentyThreeTowns":"23 ఊళ్లు","copied":"కాపీ అయింది","openNow":"ఇప్పుడు తెరిచి ఉంది","closedNow":"ఇప్పుడు మూసి ఉంది","openNote":"ఈరోజు రాత్రి 9 వరకు తెరిచి ఉంది — వచ్చి చూడండి.","closedNote":"ఉదయం 10కి తెరుస్తాం. నంబర్ ఇవ్వండి, మేం కాల్ చేస్తాం."},"hi":{"Search: TV, fridge, 1.5 ton…":"खोजें: TV, फ्रिज, 1.5 टन…","Air conditioners":"एयर कंडीशनर","Big brands.<br>Small towns.<br>Why not?":"बड़े ब्रांड.<br>अपने ही शहर में.<br>क्यों नहीं?","Years since 1994":"1994 से साल","Add anything you're curious about to <strong>my list</strong>, send it in one tap, and someone from your nearest branch replies with today's price and stock. No card details, no checkout maze.":"पसंद का सामान <strong>मेरी सूची</strong> में डालिए. एक टैप में भेजिए. आपकी ब्रांच दाम और स्टॉक बताएगी. कार्ड डिटेल की ज़रूरत नहीं।","Showrooms":"हमारी दुकानें","Visakhapatnam":"विशाखापट्टनम","Cleaning":"सफ़ाई","Open now":"अभी खुला है","0 items":"0 सामान","All":"सब","Come over":"दुकान पर आइए","Catalogue":"सामान","Showrooms, 23 towns":"23 शहरों में शोरूम","All towns":"सभी शहर","Build a list while you browse. Nothing is charged and no account is needed.":"देखते-देखते सूची बनाइए. कोई भुगतान नहीं, कोई खाता नहीं.","Send it":"भेजें","Products sold":"बिके सामान","Your town":"आपका शहर","Skip to content":"सीधे सामग्री पर जाएँ","Names only — no third-party logos were lifted for this concept.":"सिर्फ नाम — इस डिज़ाइन में किसी का लोगो इस्तेमाल नहीं किया।","Pick what you like.<br>We'll price it.":"पसंद कीजिए.<br>दाम हम बताएंगे.","Lighting":"लाइटिंग","Everything<br>you'd expect":"जो चाहिए<br>वो सब","Town, district or pincode…":"शहर, ज़िला, पिनकोड…","East Godavari":"पूर्वी गोदावरी","West Godavari":"पश्चिम गोदावरी","What are you looking for?":"आपको क्या चाहिए?","About us":"हमारे बारे में","Old link, moved page, or a typo in the address. Nothing is lost — the showrooms are all where you left them.":"पुराना लिंक, हटा पन्ना, या पते में गलती. कुछ नहीं खोया — दुकानें अपनी जगह हैं।","Audio":"ऑडियो","Water & geysers":"पानी और गीज़र","Refrigerators":"फ्रिज","What people<br>actually ask for":"लोग यही<br>मांगते हैं","Televisions":"टेलीविज़न","Search the catalogue":"सूची में खोजें","Stock is local":"स्टॉक यहीं है","Mobiles":"मोबाइल","Single & double door":"सिंगल और डबल दरवाज़ा","Your name":"आपका नाम","Customers served":"ग्राहक","Shop":"सामान","Before you<br>drive over":"निकलने से<br>पहले","Brand stores in Tanuku":"तनुकु में ब्रांड स्टोर","Come and see it in person":"एक बार आकर देखिए","Kitchen":"रसोई","Washing machines":"वॉशिंग मशीन","Open until 9 pm today.":"आज रात 9 बजे तक खुला है.","Brand warranty runs through each manufacturer's authorised service network, and WHYNOT coordinates it for you.":"वारंटी हर कंपनी के अधिकृत सर्विस नेटवर्क से चलती है. समन्वय WHYNOT करता है.","Hours":"समय","Contact":"संपर्क","Mobile number":"मोबाइल नंबर","Why not…":"क्यों नहीं…","No ticket numbers, no “within 48 hours”. Leave your number and someone from your nearest showroom rings you between 10 am and 9 pm.":"कोई टिकट नंबर नहीं, “48 घंटे में” नहीं. नंबर दीजिए — पास की दुकान से 10 से 9 के बीच फोन आएगा।","Four questions WHYNOT has answered the same way since an LML showroom in Tanuku in 1994.":"1994 में तनुकु की पहली दुकान से इन चार सवालों का हमारा जवाब नहीं बदला।","Company":"कंपनी","My list":"मेरी सूची","Home":"होम","Today":"आज","About":"हमारे बारे में","Already bought from us?":"पहले खरीदा है?","add":"+ सूची में डालें","added":"सूची में है","removed":"सूची से हटा दिया","item":"आइटम","items":"आइटम","addedToast":"सूची में डाल दिया","wa":"WhatsApp पर भेजें","browse":"सामान देखें","noMatch":"ऐसा कुछ नहीं मिला","clearF":"फ़िल्टर हटाएँ","emptyList":"सूची खाली है","askAbout":"इसके बारे में पूछें","remove":"हटाएँ","directions":"मैप में देखें","copyAddr":"पता कॉपी","showing":"दिखा रहे हैं:","of":"कुल","all":"सभी","callShort":"कॉल","categories":"श्रेणियाँ","products":"सामान","showrooms":"दुकानें","twentyThreeTowns":"23 शहर","copied":"कॉपी हो गया","openNow":"अभी खुला है","closedNow":"अभी बंद है","openNote":"आज रात 9 तक खुला है — आकर देख लीजिए.","closedNote":"सुबह 10 बजे खोलेंगे. नंबर छोड़ जाइए, हम फ़ोन करेंगे."}};
  var PATTERNS = [{"re":"^([0-9]+) products · sample catalogue, real prices on request$","te":"$1 వస్తువులు · ఇది నమూనా జాబితా, ధరలు అడగండి","hi":"$1 सामान · यह नमूना सूची है, दाम पूछिए"},{"re":"^([0-9]+) products across ([0-9]+) categories$","te":"$1 వస్తువులు · $2 విభాగాలు","hi":"$1 सामान · $2 श्रेणियाँ"},{"re":"^([0-9]+) products · ([0-9]+) categories · ask for today(?:'|’|&rsquo;)s price$","te":"$1 వస్తువులు · $2 విభాగాలు · ఈరోజు ధర అడగండి","hi":"$1 सामान · $2 श्रेणियाँ · आज का दाम पूछें"},{"re":"^([0-9]+) products · 10 categories · ask for today(?:'|’|&rsquo;)s price$","te":"$1 వస్తువులు · 10 విభాగాలు · ఈరోజు ధర అడగండి","hi":"$1 सामान · 10 श्रेणियाँ · आज का दाम पूछें"},{"re":"^([0-9]+) (?:items?|item) — we will price it and call you$","te":"$1 — ధర చెప్పి ఫోన్ చేస్తాం","hi":"$1 — दाम बताकर फोन करेंगे"},{"re":"^Ask (?:for )?today(?:'|’|&rsquo;)s price$","te":"ఈరోజు ధర అడగండి","hi":"आज का दाम पूछें"},{"re":"^Remove","te":"తీసేయి","hi":"हटाएँ"},{"re":"^Showing ([0-9]+) of ([0-9]+) products$","te":"చూపిస్తున్నాం: $1 / $2","hi":"दिखा रहे हैं: $1 / $2"},{"re":"^(In stock at) ","te":"స్టాక్ ఉన్నది: ","hi":"स्टॉक है: "},{"re":"^([0-9]+) products$","te":"$1 వస్తువులు","hi":"$1 सामान"},{"re":"^([0-9]+) items?$","te":"$1 వస్తువులు","hi":"$1 सामान"},{"re":"^([0-9]+) showrooms$","te":"$1 షాపులు","hi":"$1 दुकानें"},{"re":"^([0-9]+) towns$","te":"$1 ఊళ్లు","hi":"$1 शहर"},{"re":"^(Showing) ([0-9]+) of ([0-9]+)$","te":"చూపిస్తున్నాం: $2 / $3","hi":"दिखा रहे हैं: $2 / $3"}];
  var ALIAS = {"Add to list":"add","+ Add to my list":"add","In my list":"added","Removed from your list":"removed","item":"item","items":"items","Added to your list":"addedToast","In your list":"added","Send on WhatsApp":"wa","Browse the catalogue":"browse","Nothing matches that":"noMatch","Clear filters":"clearF","Your list is empty":"emptyList","Ask about this":"askAbout","Remove":"remove","Directions":"directions","Copy address":"copyAddr","Showing":"showing","of":"of","All":"all","Call":"callShort","categories":"categories","products":"products","showrooms":"showrooms","23 towns":"twentyThreeTowns","Copied":"copied","Open now":"openNow","Closed now":"closedNow","Open until 9 pm today — walk in and ask for a demo.":"openNote","We open at 10 am. Leave your number and we'll ring you back.":"closedNote","&#10003; In my list":"added","Search: TV, fridge, 1.5 ton…":"Search: TV, fridge, 1.5 ton…","Air conditioners":"Air conditioners","Big brands. Small towns. Why not?":"Big brands.<br>Small towns.<br>Why not?","Years since 1994":"Years since 1994","Add anything you're curious about to my list, send it in one tap, and someone from your nearest branch replies with today's price and stock. No card details, no checkout maze.":"Add anything you're curious about to <strong>my list</strong>, send it in one tap, and someone from your nearest branch replies with today's price and stock. No card details, no checkout maze.","Showrooms":"Showrooms","Visakhapatnam":"Visakhapatnam","Cleaning":"Cleaning","0 items":"0 items","Come over":"Come over","Catalogue":"Catalogue","Showrooms, 23 towns":"Showrooms, 23 towns","All towns":"All towns","Build a list while you browse. Nothing is charged and no account is needed.":"Build a list while you browse. Nothing is charged and no account is needed.","Send it":"Send it","Products sold":"Products sold","Your town":"Your town","Skip to content":"Skip to content","Names only — no third-party logos were lifted for this concept.":"Names only — no third-party logos were lifted for this concept.","Pick what you like. We'll price it.":"Pick what you like.<br>We'll price it.","Lighting":"Lighting","Everything you'd expect":"Everything<br>you'd expect","Town, district or pincode…":"Town, district or pincode…","East Godavari":"East Godavari","West Godavari":"West Godavari","What are you looking for?":"What are you looking for?","About us":"About us","Old link, moved page, or a typo in the address. Nothing is lost — the showrooms are all where you left them.":"Old link, moved page, or a typo in the address. Nothing is lost — the showrooms are all where you left them.","Audio":"Audio","Water & geysers":"Water & geysers","Refrigerators":"Refrigerators","What people actually ask for":"What people<br>actually ask for","Televisions":"Televisions","Search the catalogue":"Search the catalogue","Stock is local":"Stock is local","Mobiles":"Mobiles","Single & double door":"Single & double door","Your name":"Your name","Customers served":"Customers served","Shop":"Shop","Before you drive over":"Before you<br>drive over","Brand stores in Tanuku":"Brand stores in Tanuku","Come and see it in person":"Come and see it in person","Kitchen":"Kitchen","Washing machines":"Washing machines","Open until 9 pm today.":"Open until 9 pm today.","Brand warranty runs through each manufacturer's authorised service network, and WHYNOT coordinates it for you.":"Brand warranty runs through each manufacturer's authorised service network, and WHYNOT coordinates it for you.","Hours":"Hours","Contact":"Contact","Mobile number":"Mobile number","Why not…":"Why not…","No ticket numbers, no “within 48 hours”. Leave your number and someone from your nearest showroom rings you between 10 am and 9 pm.":"No ticket numbers, no “within 48 hours”. Leave your number and someone from your nearest showroom rings you between 10 am and 9 pm.","Four questions WHYNOT has answered the same way since an LML showroom in Tanuku in 1994.":"Four questions WHYNOT has answered the same way since an LML showroom in Tanuku in 1994.","Company":"Company","My list":"My list","Home":"Home","Today":"Today","About":"About","Already bought from us?":"Already bought from us?"};
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
