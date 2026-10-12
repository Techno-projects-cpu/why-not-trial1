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

  var STRINGS = {
  "te": {
    "Home": "మొదటి పేజీ",
    "Catalogue": "వస్తువులు",
    "Showrooms": "మా షాపులు",
    "About": "మా గురించి",
    "About us": "మా గురించి",
    "Contact": "సంప్రదించండి",
    "My list": "నా జాబితా",
    "Shop": "వస్తువులు",
    "Company": "కంపెనీ",
    "Come over": "కొట్టుకి రండి",
    "Call": "కాల్",
    "Godavari districts · since 1994": "గోదావరి జిల్లాలు · 1994 నుంచి",
    "Big brands.<br>Small towns.<br>Why not?": "పెద్ద బ్రాండ్లు.<br>మన ఊరిలోనే.<br>ఎందుకు కాదు?",
    "Big brands. <span class=\"mark mark--marker\">Small towns.</span> Why not?": "పెద్ద బ్రాండ్లు. <span class=\"mark mark--marker\">మన ఊరిలోనే.</span> ఎందుకు కాదు?",
    "Twenty-five WHYNOT showrooms in 23 towns, every major brand, and a phone number that still works five years after you buy. That has been the whole story since 1994.": "23 ఊళ్లలో 25 షోరూమ్లు. అన్ని పెద్ద బ్రాండ్లు. కొన్ని ఐదేళ్ల తర్వాత కూడా ఫోన్ ఎత్తుతాం — 1994 నుంచి ఇదే మా పద్ధతి.",
    "Twenty-five WHYNOT showrooms in 23 towns, every major brand, and a phone number that still works five years after you buy.": "23 ఊళ్లలో 25 షోరూమ్లు. అన్ని పెద్ద బ్రాండ్లు. కొన్ని ఐదేళ్ల తర్వాత కూడా ఫోన్ ఎత్తుతాం.",
    "See what we sell": "ఏమేమి ఉన్నాయో చూడండి",
    "Find my showroom": "నా షాపు ఎక్కడ?",
    "Open the full catalogue": "పూర్తి జాబితా చూడండి",
    "Open 10 am to 9 pm": "ఉదయం 10 – రాత్రి 9",
    "Open 10 am – 9 pm": "ఉదయం 10 – రాత్రి 9",
    "One helpline for 25 showrooms — 88862 22448": "25 షోప్‌లకు ఒకే నంబర్ — 88862 22448",
    "A person answers, 10 am to 9 pm": "ఫోన్ ఎప్పుడూ మనిషే ఎత్తుతారు · 10 – 9",
    "32 years": "32 ఏళ్లు",
    "300 staff": "300 మంది",
    "Delivery & install": "డెలివరీ + ఫిట్టింగ్",
    "Delivery &amp; install": "డెలివరీ + ఫిట్టింగ్",
    "Open 10–9 daily": "రోజూ 10 – 9",
    "Customers served": "కస్టమర్లు",
    "Products sold": "అమ్మిన వస్తువులు",
    "Showrooms, 23 towns": "23 ఊళ్లలో షోరూమ్లు",
    "Years since 1994": "1994 నుంచి ఏళ్లు",
    "Shop by category": "ఏం కావాలి?",
    "Ten aisles.<br>One roof.": "పది విభాగాలు.<br>ఒకే చోట.",
    "Prices move with the season, so every card asks for today's price — and we answer with the real number, not a range.": "ధరలు సీజన్‌బట్టి మారుతుంటాయి. అందుకే ప్రతి వస్తువుకు “ఈరోజు ధర అడగండి” అని ఉంటుంది — మేం నిజమైన నంబర్ చెప్తాం, రేంజ్ కాదు.",
    "Popular right now": "ఇప్పుడు డిమాండ్",
    "What people<br>actually ask for": "జనం అడిగేవి<br>ఇవే",
    "The four a month of “what's good in this budget?” conversations usually end on. Sample catalogue — today's price comes from your branch.": "“ఈ బడ్జెట్‌లో మంచిది ఏది?” అని అడిగినప్పుడు చాలామంది తీసుకునేవి ఇవే. ఇది శాంపిల్ జాబితా — ఈరోజు ధర మీ బ్రాంచ్ చెప్తుంది.",
    "The name is the question": "పేరే ప్రశ్న",
    "Why not…": "ఎందుకు కాదు…",
    "Four questions WHYNOT has answered the same way since an LML showroom in Tanuku in 1994.": "1994లో తనుకులో మొదటి షోరూమ్ నుంచి ఈ నాలుగు ప్రశ్నలకు మా జవాబు మారలేదు.",
    "Brands": "బ్రాండ్లు",
    "Everything<br>you'd expect": "మీకు కావాల్సినవి<br>అన్నీ",
    "Names only — no third-party logos were lifted for this concept.": "పేర్లు మాత్రమే — ఈ డిజైన్ కోసం ఎవరి లోగోనూ వాడలేదు.",
    "In their words": "వాళ్ల మాటల్లో",
    "People who<br>came back": "మళ్లీ వచ్చిన<br>వాళ్లు",
    "Reviews shown as they were written on the current site. Named, dated reviews with permission would do more work — see the notes in the repo.": "ఇవి ప్రస్తుత సైట్‌లో రాసినట్టుగానే ఉన్నాయి. పేరు, తేదీతో అనుమతి తీసుకుని పెట్టితే ఇంకా బాగా పనిచేస్తాయి.",
    "Come and see it in person": "ఒక్కసారి వచ్చి చూడండి",
    "Pick what you like in the catalogue, send the list, and a person from your nearest branch calls with today's price.": "నచ్చినవి జాబితాలో పెట్టి పంపండి. మీ దగ్గరి బ్రాంచ్ నుంచి ఒకరు ఫోన్ చేసి ఈరోజు ధర చెప్తారు.",
    "Start a list": "జాబితా మొదలుపెట్టు",
    "Every town deserves the good stuff": "మంచి సరుకు మన ఊరికీ రావాలి",
    "Catalogue · 17 products · 10 categories": "వస్తువులు · 17 ఐటమ్స్ · 10 విభాగాలు",
    "Pick what you like.<br>We'll price it.": "నచ్చినవి ఎంచుకోండి.<br>ధర మేం చెప్తాం.",
    "Add anything you're curious about to <strong>my list</strong>, send it in one tap, and someone from your nearest branch replies with today's price and stock. No card details, no checkout maze.": "నచ్చినవి <strong>నా జాబితా</strong>లో పెట్టండి. ఒక్క ట్యాప్‌లో పంపండి. మీ బ్రాంచ్ నుంచి ధర, స్టాక్ చెప్తారు. కార్డ్ డిటెయిల్స్ అవసరం లేదు.",
    "Search: TV, fridge, 1.5 ton…": "వెతకండి: TV, ఫ్రిజ్, 1.5 టన్…",
    "All towns": "అన్ని ఊళ్లు",
    "How buying works here": "ఇక్కడ కొనడం ఎలా?",
    "Three steps.<br>No maze.": "మూడు స్టెప్పులు.<br>అంతే.",
    "Showrooms · 25 locations": "మా షాపులు · 25 చోట్లు",
    "One is probably<br>20 minutes away.": "మీ ఊరిలోనే<br>ఒకటి ఉంటుంది.",
    "Search by town, district or pincode. Every address opens straight into Google Maps on your phone.": "ఊరు, జిల్లా లేదా పిన్ కోడ్‌తో వెతకండి. ప్రతి చిరునామా నేరుగా మ్యాప్‌లో తెరుచుకుంటుంది.",
    "Copy number": "నంబర్ కాపీ",
    "Town, district or pincode…": "ఊరు, జిల్లా, పిన్ కోడ్…",
    "All": "అన్నీ",
    "all": "అన్నీ",
    "Good to know": "తెలుసుకోవాల్సినవి",
    "Before you<br>drive over": "బయలుదేరే<br>ముందు",
    "Hours": "టైమింగ్",
    "Stock is local": "స్టాక్ ఇక్కడే",
    "Brand stores in Tanuku": "తనుకులో బ్రాండ్ స్టోర్లు",
    "Already bought from us?": "ఇదివరకే కొన్నారా?",
    "One shop.<br>One question.": "ఒక కొట్టు.<br>ఒక ప్రశ్న.",
    "The story": "మా కథ",
    "Six panels,<br>32 years": "ఆరు మజిలీలు,<br>32 ఏళ్లు",
    "Leadership today": "ఇప్పటి బాధ్యతలు",
    "The family<br>at the desk": "కౌంటర్‌లో<br>ఇంటి వాళ్లే",
    "Partners": "భాగస్వాములు",
    "Trusted<br>to sell": "నమ్మకమైన<br>బ్రాండ్లు",
    "Tell us what you need.<br>A person calls back.": "ఏం కావాలో చెప్పండి.<br>మేమే ఫోన్ చేస్తాం.",
    "No ticket numbers, no “within 48 hours”. Leave your number and someone from your nearest showroom rings you between 10 am and 9 pm.": "టికెట్ నంబర్లు లేవు, “48 గంటల్లో” లేదు. నంబర్ ఇవ్వండి — మీ దగ్గరి షాప్ నుంచి 10 – 9 మధ్య ఫోన్ వస్తుంది.",
    "Your name": "మీ పేరు",
    "Mobile number": "మొబైల్ నంబర్",
    "Your town": "మీ ఊరు",
    "What are you looking for?": "ఏం కావాలి?",
    "Send it": "పంపండి",
    "WhatsApp instead": "WhatsApp లో పంపు",
    "Send on WhatsApp": "WhatsApp లో పంపు",
    "This page is<br>missing.": "ఈ పేజీ<br>దొరకలేదు.",
    "Old link, moved page, or a typo in the address. Nothing is lost — the showrooms are all where you left them.": "పాత లింక్, తరిగిన పేజీ, లేదా అడ్రస్‌లో తప్పు. ఏం పోలేదు — షాపులన్నీ ఉన్నచోటే ఉన్నాయి.",
    "Back home": "మొదటి పేజీకి",
    "Error 404": "ఎర్రర్ 404",
    "add": "+ జాబితాలో చేర్చు",
    "added": "జాబితాలో ఉంది",
    "removed": "జాబితా నుంచి తీసేశాం",
    "item": "ఐటమ్",
    "items": "ఐటమ్స్",
    "addedToast": "జాబితాలో చేర్చాం",
    "askPrice": "ఈరోజు ధర అడగండి",
    "wa": "WhatsApp లో పంపు",
    "emailList": "మెయిల్ చేయండి",
    "browse": "వస్తువులు చూడండి",
    "noMatch": "అలాంటిది ఏమీ లేదు",
    "clearF": "ఫిల్టర్లు తీసేయి",
    "emptyList": "జాబితా ఖాళీగా ఉంది",
    "askAbout": "దీని గురించి అడగండి",
    "remove": "తీసేయి",
    "directions": "మ్యాప్‌లో చూడండి",
    "copyAddr": "చిరునామా కాపీ",
    "clearF2": "ఫిల్టర్లు తీసేయి.",
    "emptyHelp": "ధర కావాల్సినవాటికి “జాబితాలో చేర్చు” నొక్కండి. పంపే వరకు ఇదే ఫోన్‌లో ఉంటుంది.",
    "listNote": "కార్డ్ డిటెయిల్స్ లేవు, అకౌంట్ లేదు, డబ్బు వసూలు లేదు. మీ బ్రాంచ్ నుంచి ఒకరు ధర, స్టాక్ చెప్తారు.",
    "weWillPrice": "ధర చెప్పి ఫోన్ చేస్తాం",
    "inStockAt": "స్టాక్ ఉన్నది:",
    "countAll": "వస్తువులు · 10 విభాగాలు · ఈరోజు ధర అడగండి",
    "showing": "చూపిస్తున్నాం:",
    "of": "మొత్తం",
    "errName": "మీ పేరు రాయండి.",
    "errMobile": "10 అంకెల మొబైల్ నంబర్ రాయండి.",
    "errMessage": "ఏం కావాలో రాయండి.",
    "thanks": "ధన్యవాదాలు, ",
    "notSent": " — మీ వివరాలు నిజంగా పంపబడలేదు.",
    "conceptNote": "ఇది ఒక డిజైన్ డెమో — వెనుక సర్వర్ లేదు, కాబట్టి నిజంగా ఏమీ పంపబడలేదు. ",
    "willCall": "మేం ఫోన్ చేస్తాం: ",
    "workingNote": "అసలు సైట్‌లో ఇది నేరుగా బ్రాంచ్‌కి వెళ్తుంది, వాళ్లే ఫోన్ చేస్తారు.",
    "contactHint": "మోడల్ పేరు, మీ ఊరు రాయండి — స్టాక్ చూసి చెప్తాం."
  },
  "hi": {
    "Home": "होम",
    "Catalogue": "सामान",
    "Showrooms": "हमारी दुकानें",
    "About": "हमारे बारे में",
    "About us": "हमारे बारे में",
    "Contact": "संपर्क",
    "My list": "मेरी सूची",
    "Shop": "सामान",
    "Company": "कंपनी",
    "Come over": "दुकान पर आइए",
    "Call": "कॉल",
    "Godavari districts · since 1994": "गोदावरी ज़िले · 1994 से",
    "Big brands.<br>Small towns.<br>Why not?": "बड़े ब्रांड.<br>अपने ही शहर में.<br>क्यों नहीं?",
    "Big brands. <span class=\"mark mark--marker\">Small towns.</span> Why not?": "बड़े ब्रांड. <span class=\"mark mark--marker\">अपने ही शहर में.</span> क्यों नहीं?",
    "Twenty-five WHYNOT showrooms in 23 towns, every major brand, and a phone number that still works five years after you buy. That has been the whole story since 1994.": "23 शहरों में 25 शोरूम. हर बड़ा ब्रांड. खरीदने के पांच साल बाद भी फोन उठता है — 1994 से यही हमारा तरीका है।",
    "Twenty-five WHYNOT showrooms in 23 towns, every major brand, and a phone number that still works five years after you buy.": "23 शहरों में 25 शोरूम. हर बड़ा ब्रांड. पांच साल बाद भी फोन उठता है।",
    "See what we sell": "क्या-क्या है, देखें",
    "Find my showroom": "मेरी दुकान कहाँ?",
    "Open the full catalogue": "पूरी सूची देखें",
    "Open 10 am to 9 pm": "सुबह 10 – रात 9",
    "Open 10 am – 9 pm": "सुबह 10 – रात 9",
    "One helpline for 25 showrooms — 88862 22448": "25 दुकानों के लिए एक ही नंबर — 88862 22448",
    "A person answers, 10 am to 9 pm": "फोन हमेशा आदमी उठाता है · 10 से 9",
    "32 years": "32 साल",
    "300 staff": "300 लोग",
    "Delivery & install": "डिलीवरी + फिटिंग",
    "Delivery &amp; install": "डिलीवरी + फिटिंग",
    "Open 10–9 daily": "रोज़ 10 से 9",
    "Customers served": "ग्राहक",
    "Products sold": "बिके सामान",
    "Showrooms, 23 towns": "23 शहरों में शोरूम",
    "Years since 1994": "1994 से साल",
    "Shop by category": "क्या चाहिए?",
    "Ten aisles.<br>One roof.": "दस रैक.<br>एक ही दुकान.",
    "Prices move with the season, so every card asks for today's price — and we answer with the real number, not a range.": "दाम मौसम के हिसाब से बदलते हैं. इसलिए हर सामान पर “आज का दाम पूछें” लिखा है — हम असली रेट बताते हैं, रेंज नहीं।",
    "Popular right now": "अभी ट्रेंड में",
    "What people<br>actually ask for": "लोग यही<br>मांगते हैं",
    "The four a month of “what's good in this budget?” conversations usually end on. Sample catalogue — today's price comes from your branch.": "“इस बजट में अच्छा क्या है?” — लोग यही लेते हैं. यह नमूना सूची है; आज का दाम आपकी ब्रांच बताएगी।",
    "The name is the question": "नाम ही सवाल है",
    "Why not…": "क्यों नहीं…",
    "Four questions WHYNOT has answered the same way since an LML showroom in Tanuku in 1994.": "1994 में तनुकु की पहली दुकान से इन चार सवालों का हमारा जवाब नहीं बदला।",
    "Brands": "ब्रांड",
    "Everything<br>you'd expect": "जो चाहिए<br>वो सब",
    "Names only — no third-party logos were lifted for this concept.": "सिर्फ नाम — इस डिज़ाइन में किसी का लोगो इस्तेमाल नहीं किया।",
    "In their words": "उनके शब्दों में",
    "People who<br>came back": "जो लौटकर<br>आए",
    "Reviews shown as they were written on the current site. Named, dated reviews with permission would do more work — see the notes in the repo.": "ये समीक्षाएँ मौजूदा साइट जैसी ही हैं. नाम और तारीख के साथ इजाज़त लेकर लगाएँ तो ज़्यादा असर करेंगी।",
    "Come and see it in person": "एक बार आकर देखिए",
    "Pick what you like in the catalogue, send the list, and a person from your nearest branch calls with today's price.": "पसंद का सामान सूची में डालकर भेजिए. पास की ब्रांच से कोई फोन करके आज का दाम बताएगा।",
    "Start a list": "सूची बनाइए",
    "Every town deserves the good stuff": "अच्छा सामान अपने शहर में भी मिले",
    "Catalogue · 17 products · 10 categories": "सामान · 17 आइटम · 10 श्रेणियाँ",
    "Pick what you like.<br>We'll price it.": "पसंद कीजिए.<br>दाम हम बताएंगे.",
    "Add anything you're curious about to <strong>my list</strong>, send it in one tap, and someone from your nearest branch replies with today's price and stock. No card details, no checkout maze.": "पसंद का सामान <strong>मेरी सूची</strong> में डालिए. एक टैप में भेजिए. आपकी ब्रांच दाम और स्टॉक बताएगी. कार्ड डिटेल की ज़रूरत नहीं।",
    "Search: TV, fridge, 1.5 ton…": "खोजें: TV, फ्रिज, 1.5 टन…",
    "All towns": "सभी शहर",
    "How buying works here": "यहाँ खरीदना कैसे?",
    "Three steps.<br>No maze.": "तीन कदम.<br>बस इतना.",
    "Showrooms · 25 locations": "हमारी दुकानें · 25 जगह",
    "One is probably<br>20 minutes away.": "आपके शहर में<br>ही एक है.",
    "Search by town, district or pincode. Every address opens straight into Google Maps on your phone.": "शहर, ज़िला या पिनकोड से खोजिए. हर पता सीधे मैप में खुलता है।",
    "Copy number": "नंबर कॉपी",
    "Town, district or pincode…": "शहर, ज़िला, पिनकोड…",
    "All": "सब",
    "all": "सब",
    "Good to know": "जान लीजिए",
    "Before you<br>drive over": "निकलने से<br>पहले",
    "Hours": "समय",
    "Stock is local": "स्टॉक यहीं है",
    "Brand stores in Tanuku": "तनुकु में ब्रांड स्टोर",
    "Already bought from us?": "पहले खरीदा है?",
    "One shop.<br>One question.": "एक दुकान.<br>एक सवाल.",
    "The story": "हमारी कहानी",
    "Six panels,<br>32 years": "छह पड़ाव,<br>32 साल",
    "Leadership today": "आज की ज़िम्मेदारी",
    "The family<br>at the desk": "काउंटर पर<br>परिवार ही",
    "Partners": "साझेदार",
    "Trusted<br>to sell": "भरोसे के<br>ब्रांड",
    "Tell us what you need.<br>A person calls back.": "बताइए क्या चाहिए.<br>हम फोन करेंगे.",
    "No ticket numbers, no “within 48 hours”. Leave your number and someone from your nearest showroom rings you between 10 am and 9 pm.": "कोई टिकट नंबर नहीं, “48 घंटे में” नहीं. नंबर दीजिए — पास की दुकान से 10 से 9 के बीच फोन आएगा।",
    "Your name": "आपका नाम",
    "Mobile number": "मोबाइल नंबर",
    "Your town": "आपका शहर",
    "What are you looking for?": "क्या चाहिए?",
    "Send it": "भेजें",
    "WhatsApp instead": "WhatsApp पर भेजें",
    "Send on WhatsApp": "WhatsApp पर भेजें",
    "This page is<br>missing.": "यह पन्ना<br>नहीं मिला.",
    "Old link, moved page, or a typo in the address. Nothing is lost — the showrooms are all where you left them.": "पुराना लिंक, हटा पन्ना, या पते में गलती. कुछ नहीं खोया — दुकानें अपनी जगह हैं।",
    "Back home": "होम पर",
    "Error 404": "एरर 404",
    "add": "+ सूची में डालें",
    "added": "सूची में है",
    "removed": "सूची से हटा दिया",
    "item": "आइटम",
    "items": "आइटम",
    "addedToast": "सूची में डाल दिया",
    "askPrice": "आज का दाम पूछें",
    "wa": "WhatsApp पर भेजें",
    "emailList": "ईमेल करें",
    "browse": "सामान देखें",
    "noMatch": "ऐसा कुछ नहीं मिला",
    "clearF": "फ़िल्टर हटाएँ",
    "emptyList": "सूची खाली है",
    "askAbout": "इसके बारे में पूछें",
    "remove": "हटाएँ",
    "directions": "मैप में देखें",
    "copyAddr": "पता कॉपी",
    "clearF2": "फ़िल्टर हटाएँ।",
    "emptyHelp": "जिसका दाम चाहिए उस पर “सूची में डालें” दबाइए. भेजने तक यहीं रहता है।",
    "listNote": "कार्ड डिटेल नहीं, अकाउंट नहीं, कोई पैसा नहीं. आपकी ब्रांच से कोई दाम और स्टॉक बताएगा।",
    "weWillPrice": "दाम बताकर फोन करेंगे",
    "inStockAt": "स्टॉक है:",
    "countAll": "सामान · 10 श्रेणियाँ · आज का दाम पूछें",
    "showing": "दिखा रहे हैं:",
    "of": "कुल",
    "errName": "अपना नाम लिखिए।",
    "errMobile": "10 अंकों का मोबाइल नंबर लिखिए।",
    "errMessage": "क्या चाहिए, लिखिए।",
    "thanks": "धन्यवाद, ",
    "notSent": " — आपकी जानकारी असल में नहीं भेजी गई।",
    "conceptNote": "यह एक डिज़ाइन डेमो है — पीछे सर्वर नहीं है, इसलिए असल में कुछ नहीं भेजा गया। ",
    "willCall": "हम फोन करेंगे: ",
    "workingNote": "असली साइट में यह सीधे ब्रांच पहुँचता, वही फोन करती।",
    "contactHint": "मॉडल का नाम और अपना शहर लिखिए — स्टॉक देखकर बताएंगे।"
  }
};
  var PATTERNS = [
  {
    "re": "^([0-9]+) products · sample catalogue, real prices on request$",
    "te": "$1 వస్తువులు · ఇది నమూనా జాబితా, ధరలు అడగండి",
    "hi": "$1 सामान · यह नमूना सूची है, दाम पूछिए"
  },
  {
    "re": "^([0-9]+) products across ([0-9]+) categories$",
    "te": "$1 వస్తువులు · $2 విభాగాలు",
    "hi": "$1 सामान · $2 श्रेणियाँ"
  },
  {
    "re": "^([0-9]+) products · ([0-9]+) categories · ask for today(?:'|’|&rsquo;)s price$",
    "te": "$1 వస్తువులు · $2 విభాగాలు · ఈరోజు ధర అడగండి",
    "hi": "$1 सामान · $2 श्रेणियाँ · आज का दाम पूछें"
  },
  {
    "re": "^([0-9]+) products · 10 categories · ask for today(?:'|’|&rsquo;)s price$",
    "te": "$1 వస్తువులు · 10 విభాగాలు · ఈరోజు ధర అడగండి",
    "hi": "$1 सामान · 10 श्रेणियाँ · आज का दाम पूछें"
  },
  {
    "re": "^([0-9]+) (?:items?|item) — we will price it and call you$",
    "te": "$1 — ధర చెప్పి ఫోన్ చేస్తాం",
    "hi": "$1 — दाम बताकर फोन करेंगे"
  },
  {
    "re": "^Ask (?:for )?today(?:'|’|&rsquo;)s price$",
    "te": "ఈరోజు ధర అడగండి",
    "hi": "आज का दाम पूछें"
  },
  {
    "re": "^Remove",
    "te": "తీసేయి",
    "hi": "हटाएँ"
  },
  {
    "re": "^Showing ([0-9]+) of ([0-9]+) products$",
    "te": "చూపిస్తున్నాం: $1 / $2",
    "hi": "दिखा रहे हैं: $1 / $2"
  },
  {
    "re": "^(In stock at) ",
    "te": "స్టాక్ ఉన్నది: ",
    "hi": "स्टॉक है: "
  }
];
  var ALIAS = {
  "Add to list": "add",
  "+ Add to my list": "add",
  "In my list": "added",
  "Removed from your list": "removed",
  "item": "item",
  "items": "items",
  "Added to your list": "addedToast",
  "In your list": "added",
  "Ask today’s price": "askPrice",
  "Ask for today’s price": "askPrice",
  "Ask for today's price": "askPrice",
  "Send on WhatsApp": "wa",
  "Email the list": "emailList",
  "Browse the catalogue": "browse",
  "Nothing matches that": "noMatch",
  "Clear filters": "clearF",
  "Your list is empty": "emptyList",
  "Ask about this": "askAbout",
  "Remove": "remove",
  "Directions": "directions",
  "Copy address": "copyAddr",
  "Clear filters.": "clearF2",
  "Hit “add to list” on anything you want priced. It stays on this device until you send it.": "emptyHelp",
  "No card details, no account, nothing charged. A person from your nearest branch replies with today’s price and what is in stock.": "listNote",
  "we will price it and call you": "weWillPrice",
  "In stock at": "inStockAt",
  "products · 10 categories · ask for today's price": "countAll",
  "Showing": "showing",
  "of": "of",
  "Please enter your name.": "errName",
  "Enter a 10-digit mobile number.": "errMobile",
  "Tell us what you are looking for.": "errMessage",
  "Thank you,": "thanks",
  "— your enquiry was not actually sent.": "notSent",
  "This is a concept build with no server behind it yet, so nothing has actually been sent.": "conceptNote",
  "We will call you on": "willCall",
  "In a working build this would reach the branch, and they would call you back.": "workingNote",
  "Tell us a model name and your town — we will check the branch stock.": "contactHint",
  "Home": "Home",
  "Catalogue": "Catalogue",
  "Showrooms": "Showrooms",
  "About": "About",
  "About us": "About us",
  "Contact": "Contact",
  "My list": "My list",
  "Shop": "Shop",
  "Company": "Company",
  "Come over": "Come over",
  "Call": "Call",
  "Godavari districts · since 1994": "Godavari districts · since 1994",
  "Big brands. Small towns. Why not?": "Big brands.<br>Small towns.<br>Why not?",
  "Twenty-five WHYNOT showrooms in 23 towns, every major brand, and a phone number that still works five years after you buy. That has been the whole story since 1994.": "Twenty-five WHYNOT showrooms in 23 towns, every major brand, and a phone number that still works five years after you buy. That has been the whole story since 1994.",
  "Twenty-five WHYNOT showrooms in 23 towns, every major brand, and a phone number that still works five years after you buy.": "Twenty-five WHYNOT showrooms in 23 towns, every major brand, and a phone number that still works five years after you buy.",
  "See what we sell": "See what we sell",
  "Find my showroom": "Find my showroom",
  "Open the full catalogue": "Open the full catalogue",
  "Open 10 am to 9 pm": "Open 10 am to 9 pm",
  "Open 10 am – 9 pm": "Open 10 am – 9 pm",
  "One helpline for 25 showrooms — 88862 22448": "One helpline for 25 showrooms — 88862 22448",
  "A person answers, 10 am to 9 pm": "A person answers, 10 am to 9 pm",
  "32 years": "32 years",
  "300 staff": "300 staff",
  "Delivery & install": "Delivery & install",
  "Open 10–9 daily": "Open 10–9 daily",
  "Customers served": "Customers served",
  "Products sold": "Products sold",
  "Showrooms, 23 towns": "Showrooms, 23 towns",
  "Years since 1994": "Years since 1994",
  "Shop by category": "Shop by category",
  "Ten aisles. One roof.": "Ten aisles.<br>One roof.",
  "Prices move with the season, so every card asks for today's price — and we answer with the real number, not a range.": "Prices move with the season, so every card asks for today's price — and we answer with the real number, not a range.",
  "Popular right now": "Popular right now",
  "What people actually ask for": "What people<br>actually ask for",
  "The four a month of “what's good in this budget?” conversations usually end on. Sample catalogue — today's price comes from your branch.": "The four a month of “what's good in this budget?” conversations usually end on. Sample catalogue — today's price comes from your branch.",
  "The name is the question": "The name is the question",
  "Why not…": "Why not…",
  "Four questions WHYNOT has answered the same way since an LML showroom in Tanuku in 1994.": "Four questions WHYNOT has answered the same way since an LML showroom in Tanuku in 1994.",
  "Brands": "Brands",
  "Everything you'd expect": "Everything<br>you'd expect",
  "Names only — no third-party logos were lifted for this concept.": "Names only — no third-party logos were lifted for this concept.",
  "In their words": "In their words",
  "People who came back": "People who<br>came back",
  "Reviews shown as they were written on the current site. Named, dated reviews with permission would do more work — see the notes in the repo.": "Reviews shown as they were written on the current site. Named, dated reviews with permission would do more work — see the notes in the repo.",
  "Come and see it in person": "Come and see it in person",
  "Pick what you like in the catalogue, send the list, and a person from your nearest branch calls with today's price.": "Pick what you like in the catalogue, send the list, and a person from your nearest branch calls with today's price.",
  "Start a list": "Start a list",
  "Every town deserves the good stuff": "Every town deserves the good stuff",
  "Catalogue · 17 products · 10 categories": "Catalogue · 17 products · 10 categories",
  "Pick what you like. We'll price it.": "Pick what you like.<br>We'll price it.",
  "Add anything you're curious about to my list, send it in one tap, and someone from your nearest branch replies with today's price and stock. No card details, no checkout maze.": "Add anything you're curious about to <strong>my list</strong>, send it in one tap, and someone from your nearest branch replies with today's price and stock. No card details, no checkout maze.",
  "Search: TV, fridge, 1.5 ton…": "Search: TV, fridge, 1.5 ton…",
  "All towns": "All towns",
  "How buying works here": "How buying works here",
  "Three steps. No maze.": "Three steps.<br>No maze.",
  "Showrooms · 25 locations": "Showrooms · 25 locations",
  "One is probably 20 minutes away.": "One is probably<br>20 minutes away.",
  "Search by town, district or pincode. Every address opens straight into Google Maps on your phone.": "Search by town, district or pincode. Every address opens straight into Google Maps on your phone.",
  "Copy number": "Copy number",
  "Town, district or pincode…": "Town, district or pincode…",
  "All": "All",
  "all": "all",
  "Good to know": "Good to know",
  "Before you drive over": "Before you<br>drive over",
  "Hours": "Hours",
  "Stock is local": "Stock is local",
  "Brand stores in Tanuku": "Brand stores in Tanuku",
  "Already bought from us?": "Already bought from us?",
  "One shop. One question.": "One shop.<br>One question.",
  "The story": "The story",
  "Six panels, 32 years": "Six panels,<br>32 years",
  "Leadership today": "Leadership today",
  "The family at the desk": "The family<br>at the desk",
  "Partners": "Partners",
  "Trusted to sell": "Trusted<br>to sell",
  "Tell us what you need. A person calls back.": "Tell us what you need.<br>A person calls back.",
  "No ticket numbers, no “within 48 hours”. Leave your number and someone from your nearest showroom rings you between 10 am and 9 pm.": "No ticket numbers, no “within 48 hours”. Leave your number and someone from your nearest showroom rings you between 10 am and 9 pm.",
  "Your name": "Your name",
  "Mobile number": "Mobile number",
  "Your town": "Your town",
  "What are you looking for?": "What are you looking for?",
  "Send it": "Send it",
  "WhatsApp instead": "WhatsApp instead",
  "This page is missing.": "This page is<br>missing.",
  "Old link, moved page, or a typo in the address. Nothing is lost — the showrooms are all where you left them.": "Old link, moved page, or a typo in the address. Nothing is lost — the showrooms are all where you left them.",
  "Back home": "Back home",
  "Error 404": "Error 404"
};
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
