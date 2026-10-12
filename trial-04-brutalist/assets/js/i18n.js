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

  var STRINGS = {"te":{"Six panels,<br>32 years":"ఆరు మజిలీలు,<br>32 ఏళ్లు","Come over":"కొట్టుకి రండి","Shop":"వస్తువులు","Mobile number":"మొబైల్ నంబర్","Before you<br>drive over":"బయలుదేరే<br>ముందు","Speakers · bars":"స్పీకర్లు · బార్లు","Air conditioners":"ఏసీలు","The family<br>at the desk":"కౌంటర్‌లో<br>ఇంటి వాళ్లే","Open now":"ఇప్పుడు తెరిచి ఉంది","Open 10 am to 9 pm":"ఉదయం 10 – రాత్రి 9","Search the catalogue":"జాబితాలో వెతకండి","Audio":"ఆడియో","Brands":"బ్రాండ్లు","The four a month of “what's good in this budget?” conversations usually end on. Sample catalogue — today's price comes from your branch.":"“ఈ బడ్జెట్‌లో మంచిది ఏది?” అని అడిగినప్పుడు చాలామంది తీసుకునేవి ఇవే. ఇది శాంపిల్ జాబితా — ఈరోజు ధర మీ బ్రాంచ్ చెప్తుంది.","Old link, moved page, or a typo in the address. Nothing is lost — the showrooms are all where you left them.":"పాత లింక్, తరిగిన పేజీ, లేదా అడ్రస్‌లో తప్పు. ఏం పోలేదు — షాపులన్నీ ఉన్నచోటే ఉన్నాయి.","Your town":"మీ ఊరు","Card and Bajaj-style EMI is available at the counter on most large appliances. Old product exchange value is quoted before you buy.":"పెద్ద వస్తువులపై కార్డు, బజాజ్ EMI కౌంటర్‌లోనే. పాత వస్తువు మార్పిడి విలువ కొనే ముందే చెప్తాం.","Visakhapatnam":"విశాఖపట్నం","About":"మా గురించి","What people<br>actually ask for":"జనం అడిగేవి<br>ఇవే","Today's price, which branch has it, EMI if you want it, and a delivery date.":"ఈరోజు ధర, ఏ షాపులో ఉంది, కావాలంటే EMI, డెలివరీ తేదీ.","Twenty-five WHYNOT showrooms in 23 towns, every major brand, and a phone number that still works five years after you buy. That has been the whole story since 1994.":"23 ఊళ్లలో 25 షోరూమ్లు. అన్ని పెద్ద బ్రాండ్లు. కొన్ని ఐదేళ్ల తర్వాత కూడా ఫోన్ ఎత్తుతాం — 1994 నుంచి ఇదే మా పద్ధతి.","0 items":"0 వస్తువులు","Shop by category":"ఏం కావాలి?","About us":"మా గురించి","People who<br>came back":"మళ్లీ వచ్చిన<br>వాళ్లు","Showrooms · 25 locations":"మా షాపులు · 25 చోట్లు","All towns":"అన్ని ఊళ్లు","Four questions WHYNOT has answered the same way since an LML showroom in Tanuku in 1994.":"1994లో తనుకులో మొదటి షోరూమ్ నుంచి ఈ నాలుగు ప్రశ్నలకు మా జవాబు మారలేదు.","Hours":"టైమింగ్","Showrooms":"మా షాపులు","Brand warranty runs through each manufacturer's authorised service network, and WHYNOT coordinates it for you.":"వారంటీ కంపెనీ అధికారిక సర్వీస్ నెట్‌వర్క్ ద్వారానే నడుస్తుంది. సమన్వయం WHYNOT చేస్తుంది.","Popular right now":"ఇప్పుడు డిమాండ్","Unsure between two models? Call the helpline and describe the room. We do this all day.":"రెండు మోడళ్ల మధ్య సందిగ్ధమా? హెల్ప్‌లైన్‌కు కాల్ చేసి గది వివరాలు చెప్పండి. ఇదే మా పని.","Managing Director":"మేనేజింగ్ డైరెక్టర్","Washing machines":"వాషింగ్ మెషీన్లు","In their words":"వాళ్ల మాటల్లో","Purifiers · heaters":"ప్యూరిఫైయర్లు · హీటర్లు","Your name":"మీ పేరు","One shop.<br>One question.":"ఒక కొట్టు.<br>ఒక ప్రశ్న.","Add anything you're curious about to <strong>my list</strong>, send it in one tap, and someone from your nearest branch replies with today's price and stock. No card details, no checkout maze.":"నచ్చినవి <strong>నా జాబితా</strong>లో పెట్టండి. ఒక్క ట్యాప్‌లో పంపండి. మీ బ్రాంచ్ నుంచి ధర, స్టాక్ చెప్తారు. కార్డ్ డిటెయిల్స్ అవసరం లేదు.","Mobiles":"మొబైల్స్","How buying works here":"ఇక్కడ కొనడం ఎలా","Ten aisles.<br>One roof.":"పది విభాగాలు.<br>ఒకే చోట.","Pick what you like in the catalogue, send the list, and a person from your nearest branch calls with today's price.":"నచ్చినవి జాబితాలో పెట్టి పంపండి. మీ దగ్గరి బ్రాంచ్ నుంచి ఒకరు ఫోన్ చేసి ఈరోజు ధర చెప్తారు.","Fixed at the counter: what it costs, when it arrives, who installs it. No surprises on the bill.":"కౌంటర్‌లోనే ఖరారు: ఎంత, ఎప్పుడు వస్తుంది, ఎవరు అమర్చుతారు. బిల్లులో ఆశ్చర్యాలు ఉండవు.","Refrigerators":"ఫ్రిజ్‌లు","Lighting":"లైటింగ్","No ticket numbers, no “within 48 hours”. Leave your number and someone from your nearest showroom rings you between 10 am and 9 pm.":"టికెట్ నంబర్లు లేవు, “48 గంటల్లో” లేదు. నంబర్ ఇవ్వండి — మీ దగ్గరి షాప్ నుంచి 10 – 9 మధ్య ఫోన్ వస్తుంది.","Televisions":"టెలివిజన్లు","What are you looking for?":"మీకు ఏం కావాలి?","Years since 1994":"1994 నుంచి ఏళ్లు","Add what you like":"నచ్చినవి జోడించండి","Showrooms, 23 towns":"23 ఊళ్లలో షోరూమ్లు","5G · budget to flagship":"5G · బడ్జెట్ నుంచి టాప్ వరకు","We call with the price":"ధర చెప్పి ఫోన్ చేస్తాం","This page is<br>missing.":"ఈ పేజీ<br>దొరకలేదు.","Town, district or pincode…":"ఊరు, జిల్లా, పిన్ కోడ్…","East Godavari":"తూర్పు గోదావరి","Catalogue":"వస్తువులు","Why not…":"ఎందుకు కాదు…","Reviews shown as they were written on the current site. Named, dated reviews with permission would do more work — see the notes in the repo.":"ఇవి ప్రస్తుత సైట్‌లో రాసినట్టుగానే ఉన్నాయి. పేరు, తేదీతో అనుమతి తీసుకుని పెట్టితే ఇంకా బాగా పనిచేస్తాయి.","My list":"నా జాబితా","Company":"కంపెనీ","Everything<br>you'd expect":"మీకు కావాల్సినవి<br>అన్నీ","Tell us what you need.<br>A person calls back.":"ఏం కావాలో చెప్పండి.<br>మేమే ఫోన్ చేస్తాం.","Split · inverter":"స్ప్లిట్ · ఇన్వర్టర్","QLED · 4K · smart":"QLED · 4K · స్మార్ట్","Customers served":"కస్టమర్లు","Prices move with the season, so every card asks for today's price — and we answer with the real number, not a range.":"ధరలు సీజన్‌బట్టి మారుతుంటాయి. అందుకే ప్రతి వస్తువుకు “ఈరోజు ధర అడగండి” అని ఉంటుంది — మేం నిజమైన నంబర్ చెప్తాం, రేంజ్ కాదు.","Kitchen":"వంటగది","The story":"మా కథ","Brand stores in Tanuku":"తనుకులో బ్రాండ్ స్టోర్లు","Error 404":"ఎర్రర్ 404","Search: TV, fridge, 1.5 ton…":"వెతకండి: TV, ఫ్రిజ్, 1.5 టన్…","Stock is local":"స్టాక్ ఇక్కడే","West Godavari":"పశ్చిమ గోదావరి","Products sold":"అమ్మిన వస్తువులు","One is probably<br>20 minutes away.":"మీ ఊరిలోనే<br>ఒకటి ఉంటుంది.","Every town deserves the good stuff":"మంచి సరుకు మన ఊరికీ రావాలి","Home":"మొదటి పేజీ","Leadership today":"ఇప్పటి బాధ్యతలు","Vacuum · mops":"వాక్యూమ్ · మాప్‌లు","Godavari districts · since 1994":"గోదావరి జిల్లాలు · 1994 నుంచి","Skip to content":"కంటెంట్‌కు వెళ్లు","Big brands.<br>Small towns.<br>Why not?":"పెద్ద బ్రాండ్లు.<br>మన ఊరిలోనే.<br>ఎందుకు కాదు?","The name is the question":"పేరే ప్రశ్న","Semi & automatic":"సెమీ, ఆటోమేటిక్","Good to know":"తెలుసుకోవాల్సినవి","Build a list while you browse. Nothing is charged and no account is needed.":"చూస్తూనే జాబితా చేసుకోండి. డబ్బు ఏమీ కట్టాల్సిన అవసరం లేదు, అకౌంట్ లేదు.","Pick what you like.<br>We'll price it.":"నచ్చినవి ఎంచుకోండి.<br>ధర మేం చెప్తాం.","Single & double door":"సింగిల్, డబుల్ డోర్","Cleaning":"క్లీనింగ్","Mixers · grinders":"మిక్సీలు · గ్రైండర్లు","Today":"ఇప్పుడు","Search by town, district or pincode. Every address opens straight into Google Maps on your phone.":"ఊరు, జిల్లా లేదా పిన్ కోడ్‌తో వెతకండి. ప్రతి చిరునామా నేరుగా మ్యాప్‌లో తెరుచుకుంటుంది.","Already bought from us?":"ఇదివరకే కొన్నారా?","LED · strips":"LED · స్ట్రిప్‌లు","Names only — no third-party logos were lifted for this concept.":"పేర్లు మాత్రమే — ఈ డిజైన్ కోసం ఎవరి లోగోనూ వాడలేదు.","Water & geysers":"నీళ్లు, గీజర్లు","Contact":"సంప్రదించండి","Three steps.<br>No maze.":"మూడు స్టెప్పులు.<br>అంతే.","All":"అన్నీ","Come and see it in person":"ఒక్కసారి వచ్చి చూడండి","Director":"డైరెక్టర్","Open the full catalogue":"పూర్తి జాబితా చూడండి","One tap opens WhatsApp with your whole list written out, or dials the helpline.":"ఒక్క నొక్కు — జాబితా మొత్తం WhatsApp లో సిద్ధంగా ఉంటుంది, లేదా హెల్ప్‌లైన్‌కు కాల్ అవుతుంది.","Catalogue · 17 products · 10 categories":"వస్తువులు · 17 ఐటమ్స్ · 10 విభాగాలు","Send it to us":"మాకు పంపండి","Send it":"పంపండి","add":"+ జాబితాలో చేర్చు","added":"జాబితాలో ఉంది","removed":"జాబితా నుంచి తీసేశాం","item":"ఐటమ్","items":"ఐటమ్స్","addedToast":"జాబితాలో చేర్చాం","askPrice":"ఈరోజు ధర అడగండి","wa":"WhatsApp లో పంపు","emailList":"మెయిల్ చేయండి","browse":"వస్తువులు చూడండి","noMatch":"అలాంటిది ఏమీ లేదు","clearF":"ఫిల్టర్లు తీసేయి","emptyList":"జాబితా ఖాళీగా ఉంది","askAbout":"దీని గురించి అడగండి","remove":"తీసేయి","directions":"మ్యాప్‌లో చూడండి","copyAddr":"చిరునామా కాపీ","weWillPrice":"ధర చెప్పి ఫోన్ చేస్తాం","inStockAt":"స్టాక్ ఉన్నది:","showing":"చూపిస్తున్నాం:","of":"మొత్తం","all":"అన్నీ","callShort":"కాల్","categories":"విభాగాలు","products":"వస్తువులు","showrooms":"షాపులు","twentyThreeTowns":"23 ఊళ్లు","oneHelpline":"ఒకే హెల్ప్‌లైన్","copied":"కాపీ అయింది","openNow":"ఇప్పుడు తెరిచి ఉంది","closedNow":"ఇప్పుడు మూసి ఉంది","openNote":"ఈరోజు రాత్రి 9 వరకు తెరిచి ఉంది — వచ్చి చూడండి.","closedNote":"ఉదయం 10కి తెరుస్తాం. నంబర్ ఇవ్వండి, మేం కాల్ చేస్తాం."},"hi":{"Six panels,<br>32 years":"छह पड़ाव,<br>32 साल","Come over":"दुकान पर आइए","Shop":"सामान","Mobile number":"मोबाइल नंबर","Before you<br>drive over":"निकलने से<br>पहले","Speakers · bars":"स्पीकर · बार","Air conditioners":"एयर कंडीशनर","The family<br>at the desk":"काउंटर पर<br>परिवार ही","Open now":"अभी खुला है","Open 10 am to 9 pm":"सुबह 10 – रात 9","Search the catalogue":"सूची में खोजें","Audio":"ऑडियो","Brands":"ब्रांड","The four a month of “what's good in this budget?” conversations usually end on. Sample catalogue — today's price comes from your branch.":"“इस बजट में अच्छा क्या है?” — लोग यही लेते हैं. यह नमूना सूची है; आज का दाम आपकी ब्रांच बताएगी।","Old link, moved page, or a typo in the address. Nothing is lost — the showrooms are all where you left them.":"पुराना लिंक, हटा पन्ना, या पते में गलती. कुछ नहीं खोया — दुकानें अपनी जगह हैं।","Your town":"आपका शहर","Card and Bajaj-style EMI is available at the counter on most large appliances. Old product exchange value is quoted before you buy.":"बड़े सामान पर कार्ड और बजाज EMI काउंटर पर ही. पुराने सामान का एक्सचेंज मूल्य खरीदने से पहले बता देते हैं.","Visakhapatnam":"विशाखापट्टनम","About":"हमारे बारे में","What people<br>actually ask for":"लोग यही<br>मांगते हैं","Today's price, which branch has it, EMI if you want it, and a delivery date.":"आज का दाम, किस दुकान में है, चाहें तो EMI, और डिलीवरी की तारीख़.","Twenty-five WHYNOT showrooms in 23 towns, every major brand, and a phone number that still works five years after you buy. That has been the whole story since 1994.":"23 शहरों में 25 शोरूम. हर बड़ा ब्रांड. खरीदने के पांच साल बाद भी फोन उठता है — 1994 से यही हमारा तरीका है।","0 items":"0 सामान","Shop by category":"क्या चाहिए?","About us":"हमारे बारे में","People who<br>came back":"जो लौटकर<br>आए","Showrooms · 25 locations":"हमारी दुकानें · 25 जगह","All towns":"सभी शहर","Four questions WHYNOT has answered the same way since an LML showroom in Tanuku in 1994.":"1994 में तनुकु की पहली दुकान से इन चार सवालों का हमारा जवाब नहीं बदला।","Hours":"समय","Showrooms":"हमारी दुकानें","Brand warranty runs through each manufacturer's authorised service network, and WHYNOT coordinates it for you.":"वारंटी हर कंपनी के अधिकृत सर्विस नेटवर्क से चलती है. समन्वय WHYNOT करता है.","Popular right now":"अभी ट्रेंड में","Unsure between two models? Call the helpline and describe the room. We do this all day.":"दो मॉडल में उलझन? हेल्पलाइन पर फ़ोन करके कमरे के बारे में बताइए. यही हमारा रोज़ का काम है.","Managing Director":"मैनेजिंग डायरेक्टर","Washing machines":"वॉशिंग मशीन","In their words":"उनके शब्दों में","Purifiers · heaters":"प्यूरिफ़ायर · हीटर","Your name":"आपका नाम","One shop.<br>One question.":"एक दुकान.<br>एक सवाल.","Add anything you're curious about to <strong>my list</strong>, send it in one tap, and someone from your nearest branch replies with today's price and stock. No card details, no checkout maze.":"पसंद का सामान <strong>मेरी सूची</strong> में डालिए. एक टैप में भेजिए. आपकी ब्रांच दाम और स्टॉक बताएगी. कार्ड डिटेल की ज़रूरत नहीं।","Mobiles":"मोबाइल","How buying works here":"यहाँ खरीदना कैसे होता है","Ten aisles.<br>One roof.":"दस रैक.<br>एक ही दुकान.","Pick what you like in the catalogue, send the list, and a person from your nearest branch calls with today's price.":"पसंद का सामान सूची में डालकर भेजिए. पास की ब्रांच से कोई फोन करके आज का दाम बताएगा।","Fixed at the counter: what it costs, when it arrives, who installs it. No surprises on the bill.":"काउंटर पर तय: कितना खर्च, कब आएगा, कौन लगाएगा. बिल में कोई झटका नहीं.","Refrigerators":"फ्रिज","Lighting":"लाइटिंग","No ticket numbers, no “within 48 hours”. Leave your number and someone from your nearest showroom rings you between 10 am and 9 pm.":"कोई टिकट नंबर नहीं, “48 घंटे में” नहीं. नंबर दीजिए — पास की दुकान से 10 से 9 के बीच फोन आएगा।","Televisions":"टेलीविज़न","What are you looking for?":"आपको क्या चाहिए?","Years since 1994":"1994 से साल","Add what you like":"पसंद का जोड़ें","Showrooms, 23 towns":"23 शहरों में शोरूम","5G · budget to flagship":"5G · बजट से टॉप तक","We call with the price":"दाम बताकर फ़ोन करेंगे","This page is<br>missing.":"यह पन्ना<br>नहीं मिला.","Town, district or pincode…":"शहर, ज़िला, पिनकोड…","East Godavari":"पूर्वी गोदावरी","Catalogue":"सामान","Why not…":"क्यों नहीं…","Reviews shown as they were written on the current site. Named, dated reviews with permission would do more work — see the notes in the repo.":"ये समीक्षाएँ मौजूदा साइट जैसी ही हैं. नाम और तारीख के साथ इजाज़त लेकर लगाएँ तो ज़्यादा असर करेंगी।","My list":"मेरी सूची","Company":"कंपनी","Everything<br>you'd expect":"जो चाहिए<br>वो सब","Tell us what you need.<br>A person calls back.":"बताइए क्या चाहिए.<br>हम फोन करेंगे.","Split · inverter":"स्प्लिट · इनवर्टर","QLED · 4K · smart":"QLED · 4K · स्मार्ट","Customers served":"ग्राहक","Prices move with the season, so every card asks for today's price — and we answer with the real number, not a range.":"दाम मौसम के हिसाब से बदलते हैं. इसलिए हर सामान पर “आज का दाम पूछें” लिखा है — हम असली रेट बताते हैं, रेंज नहीं।","Kitchen":"रसोई","The story":"हमारी कहानी","Brand stores in Tanuku":"तनुकु में ब्रांड स्टोर","Error 404":"एरर 404","Search: TV, fridge, 1.5 ton…":"खोजें: TV, फ्रिज, 1.5 टन…","Stock is local":"स्टॉक यहीं है","West Godavari":"पश्चिम गोदावरी","Products sold":"बिके सामान","One is probably<br>20 minutes away.":"आपके शहर में<br>ही एक है.","Every town deserves the good stuff":"अच्छा सामान अपने शहर में भी मिले","Home":"होम","Leadership today":"आज की ज़िम्मेदारी","Vacuum · mops":"वैक्यूम · मॉप","Godavari districts · since 1994":"गोदावरी ज़िले · 1994 से","Skip to content":"सीधे सामग्री पर जाएँ","Big brands.<br>Small towns.<br>Why not?":"बड़े ब्रांड.<br>अपने ही शहर में.<br>क्यों नहीं?","The name is the question":"नाम ही सवाल है","Semi & automatic":"सेमी और ऑटोमैटिक","Good to know":"जान लीजिए","Build a list while you browse. Nothing is charged and no account is needed.":"देखते-देखते सूची बनाइए. कोई भुगतान नहीं, कोई खाता नहीं.","Pick what you like.<br>We'll price it.":"पसंद कीजिए.<br>दाम हम बताएंगे.","Single & double door":"सिंगल और डबल दरवाज़ा","Cleaning":"सफ़ाई","Mixers · grinders":"मिक्सर · ग्राइंडर","Today":"आज","Search by town, district or pincode. Every address opens straight into Google Maps on your phone.":"शहर, ज़िला या पिनकोड से खोजिए. हर पता सीधे मैप में खुलता है।","Already bought from us?":"पहले खरीदा है?","LED · strips":"LED · स्ट्रिप","Names only — no third-party logos were lifted for this concept.":"सिर्फ नाम — इस डिज़ाइन में किसी का लोगो इस्तेमाल नहीं किया।","Water & geysers":"पानी और गीज़र","Contact":"संपर्क","Three steps.<br>No maze.":"तीन कदम.<br>बस इतना.","All":"सब","Come and see it in person":"एक बार आकर देखिए","Director":"डायरेक्टर","Open the full catalogue":"पूरी सूची देखें","One tap opens WhatsApp with your whole list written out, or dials the helpline.":"एक टैप से पूरी सूची WhatsApp पर तैयार, या हेल्पलाइन पर कॉल.","Catalogue · 17 products · 10 categories":"सामान · 17 आइटम · 10 श्रेणियाँ","Send it to us":"हमें भेजिए","Send it":"भेजें","add":"+ सूची में डालें","added":"सूची में है","removed":"सूची से हटा दिया","item":"आइटम","items":"आइटम","addedToast":"सूची में डाल दिया","askPrice":"आज का दाम पूछें","wa":"WhatsApp पर भेजें","emailList":"ईमेल करें","browse":"सामान देखें","noMatch":"ऐसा कुछ नहीं मिला","clearF":"फ़िल्टर हटाएँ","emptyList":"सूची खाली है","askAbout":"इसके बारे में पूछें","remove":"हटाएँ","directions":"मैप में देखें","copyAddr":"पता कॉपी","weWillPrice":"दाम बताकर फ़ोन करेंगे","inStockAt":"स्टॉक है:","showing":"दिखा रहे हैं:","of":"कुल","all":"सभी","callShort":"कॉल","categories":"श्रेणियाँ","products":"सामान","showrooms":"दुकानें","twentyThreeTowns":"23 शहर","oneHelpline":"एक हेल्पलाइन","copied":"कॉपी हो गया","openNow":"अभी खुला है","closedNow":"अभी बंद है","openNote":"आज रात 9 तक खुला है — आकर देख लीजिए.","closedNote":"सुबह 10 बजे खोलेंगे. नंबर छोड़ जाइए, हम फ़ोन करेंगे."}};
  var PATTERNS = [{"re":"^([0-9]+) products · sample catalogue, real prices on request$","te":"$1 వస్తువులు · ఇది నమూనా జాబితా, ధరలు అడగండి","hi":"$1 सामान · यह नमूना सूची है, दाम पूछिए"},{"re":"^([0-9]+) products across ([0-9]+) categories$","te":"$1 వస్తువులు · $2 విభాగాలు","hi":"$1 सामान · $2 श्रेणियाँ"},{"re":"^([0-9]+) products · ([0-9]+) categories · ask for today(?:'|’|&rsquo;)s price$","te":"$1 వస్తువులు · $2 విభాగాలు · ఈరోజు ధర అడగండి","hi":"$1 सामान · $2 श्रेणियाँ · आज का दाम पूछें"},{"re":"^([0-9]+) products · 10 categories · ask for today(?:'|’|&rsquo;)s price$","te":"$1 వస్తువులు · 10 విభాగాలు · ఈరోజు ధర అడగండి","hi":"$1 सामान · 10 श्रेणियाँ · आज का दाम पूछें"},{"re":"^([0-9]+) (?:items?|item) — we will price it and call you$","te":"$1 — ధర చెప్పి ఫోన్ చేస్తాం","hi":"$1 — दाम बताकर फोन करेंगे"},{"re":"^Ask (?:for )?today(?:'|’|&rsquo;)s price$","te":"ఈరోజు ధర అడగండి","hi":"आज का दाम पूछें"},{"re":"^Remove","te":"తీసేయి","hi":"हटाएँ"},{"re":"^Showing ([0-9]+) of ([0-9]+) products$","te":"చూపిస్తున్నాం: $1 / $2","hi":"दिखा रहे हैं: $1 / $2"},{"re":"^(In stock at) ","te":"స్టాక్ ఉన్నది: ","hi":"स्टॉक है: "},{"re":"^([0-9]+) products$","te":"$1 వస్తువులు","hi":"$1 सामान"},{"re":"^([0-9]+) items?$","te":"$1 వస్తువులు","hi":"$1 सामान"},{"re":"^([0-9]+) showrooms$","te":"$1 షాపులు","hi":"$1 दुकानें"},{"re":"^([0-9]+) towns$","te":"$1 ఊళ్లు","hi":"$1 शहर"},{"re":"^(Showing) ([0-9]+) of ([0-9]+)$","te":"చూపిస్తున్నాం: $2 / $3","hi":"दिखा रहे हैं: $2 / $3"}];
  var ALIAS = {"Add to list":"add","+ Add to my list":"add","In my list":"added","Removed from your list":"removed","item":"item","items":"items","Added to your list":"addedToast","In your list":"added","Ask today’s price":"askPrice","Ask for today’s price":"askPrice","Ask for today's price":"askPrice","Send on WhatsApp":"wa","Email the list":"emailList","Browse the catalogue":"browse","Nothing matches that":"noMatch","Clear filters":"clearF","Your list is empty":"emptyList","Ask about this":"askAbout","Remove":"remove","Directions":"directions","Copy address":"copyAddr","we will price it and call you":"weWillPrice","In stock at":"inStockAt","Showing":"showing","of":"of","All":"all","Call":"callShort","categories":"categories","products":"products","showrooms":"showrooms","23 towns":"twentyThreeTowns","1 helpline":"oneHelpline","ask for today's price":"askPrice","Copied":"copied","Open now":"openNow","Closed now":"closedNow","Open until 9 pm today — walk in and ask for a demo.":"openNote","We open at 10 am. Leave your number and we'll ring you back.":"closedNote","&#10003; In my list":"added","Six panels, 32 years":"Six panels,<br>32 years","Come over":"Come over","Shop":"Shop","Mobile number":"Mobile number","Before you drive over":"Before you<br>drive over","Speakers · bars":"Speakers · bars","Air conditioners":"Air conditioners","The family at the desk":"The family<br>at the desk","Open 10 am to 9 pm":"Open 10 am to 9 pm","Search the catalogue":"Search the catalogue","Audio":"Audio","Brands":"Brands","The four a month of “what's good in this budget?” conversations usually end on. Sample catalogue — today's price comes from your branch.":"The four a month of “what's good in this budget?” conversations usually end on. Sample catalogue — today's price comes from your branch.","Old link, moved page, or a typo in the address. Nothing is lost — the showrooms are all where you left them.":"Old link, moved page, or a typo in the address. Nothing is lost — the showrooms are all where you left them.","Your town":"Your town","Card and Bajaj-style EMI is available at the counter on most large appliances. Old product exchange value is quoted before you buy.":"Card and Bajaj-style EMI is available at the counter on most large appliances. Old product exchange value is quoted before you buy.","Visakhapatnam":"Visakhapatnam","About":"About","What people actually ask for":"What people<br>actually ask for","Today's price, which branch has it, EMI if you want it, and a delivery date.":"Today's price, which branch has it, EMI if you want it, and a delivery date.","Twenty-five WHYNOT showrooms in 23 towns, every major brand, and a phone number that still works five years after you buy. That has been the whole story since 1994.":"Twenty-five WHYNOT showrooms in 23 towns, every major brand, and a phone number that still works five years after you buy. That has been the whole story since 1994.","0 items":"0 items","Shop by category":"Shop by category","About us":"About us","People who came back":"People who<br>came back","Showrooms · 25 locations":"Showrooms · 25 locations","All towns":"All towns","Four questions WHYNOT has answered the same way since an LML showroom in Tanuku in 1994.":"Four questions WHYNOT has answered the same way since an LML showroom in Tanuku in 1994.","Hours":"Hours","Showrooms":"Showrooms","Brand warranty runs through each manufacturer's authorised service network, and WHYNOT coordinates it for you.":"Brand warranty runs through each manufacturer's authorised service network, and WHYNOT coordinates it for you.","Popular right now":"Popular right now","Unsure between two models? Call the helpline and describe the room. We do this all day.":"Unsure between two models? Call the helpline and describe the room. We do this all day.","Managing Director":"Managing Director","Washing machines":"Washing machines","In their words":"In their words","Purifiers · heaters":"Purifiers · heaters","Your name":"Your name","One shop. One question.":"One shop.<br>One question.","Add anything you're curious about to my list, send it in one tap, and someone from your nearest branch replies with today's price and stock. No card details, no checkout maze.":"Add anything you're curious about to <strong>my list</strong>, send it in one tap, and someone from your nearest branch replies with today's price and stock. No card details, no checkout maze.","Mobiles":"Mobiles","How buying works here":"How buying works here","Ten aisles. One roof.":"Ten aisles.<br>One roof.","Pick what you like in the catalogue, send the list, and a person from your nearest branch calls with today's price.":"Pick what you like in the catalogue, send the list, and a person from your nearest branch calls with today's price.","Fixed at the counter: what it costs, when it arrives, who installs it. No surprises on the bill.":"Fixed at the counter: what it costs, when it arrives, who installs it. No surprises on the bill.","Refrigerators":"Refrigerators","Lighting":"Lighting","No ticket numbers, no “within 48 hours”. Leave your number and someone from your nearest showroom rings you between 10 am and 9 pm.":"No ticket numbers, no “within 48 hours”. Leave your number and someone from your nearest showroom rings you between 10 am and 9 pm.","Televisions":"Televisions","What are you looking for?":"What are you looking for?","Years since 1994":"Years since 1994","Add what you like":"Add what you like","Showrooms, 23 towns":"Showrooms, 23 towns","5G · budget to flagship":"5G · budget to flagship","We call with the price":"We call with the price","This page is missing.":"This page is<br>missing.","Town, district or pincode…":"Town, district or pincode…","East Godavari":"East Godavari","Catalogue":"Catalogue","Why not…":"Why not…","Reviews shown as they were written on the current site. Named, dated reviews with permission would do more work — see the notes in the repo.":"Reviews shown as they were written on the current site. Named, dated reviews with permission would do more work — see the notes in the repo.","My list":"My list","Company":"Company","Everything you'd expect":"Everything<br>you'd expect","Tell us what you need. A person calls back.":"Tell us what you need.<br>A person calls back.","Split · inverter":"Split · inverter","QLED · 4K · smart":"QLED · 4K · smart","Customers served":"Customers served","Prices move with the season, so every card asks for today's price — and we answer with the real number, not a range.":"Prices move with the season, so every card asks for today's price — and we answer with the real number, not a range.","Kitchen":"Kitchen","The story":"The story","Brand stores in Tanuku":"Brand stores in Tanuku","Error 404":"Error 404","Search: TV, fridge, 1.5 ton…":"Search: TV, fridge, 1.5 ton…","Stock is local":"Stock is local","West Godavari":"West Godavari","Products sold":"Products sold","One is probably 20 minutes away.":"One is probably<br>20 minutes away.","Every town deserves the good stuff":"Every town deserves the good stuff","Home":"Home","Leadership today":"Leadership today","Vacuum · mops":"Vacuum · mops","Godavari districts · since 1994":"Godavari districts · since 1994","Skip to content":"Skip to content","Big brands. Small towns. Why not?":"Big brands.<br>Small towns.<br>Why not?","The name is the question":"The name is the question","Semi & automatic":"Semi & automatic","Good to know":"Good to know","Build a list while you browse. Nothing is charged and no account is needed.":"Build a list while you browse. Nothing is charged and no account is needed.","Pick what you like. We'll price it.":"Pick what you like.<br>We'll price it.","Single & double door":"Single & double door","Cleaning":"Cleaning","Mixers · grinders":"Mixers · grinders","Today":"Today","Search by town, district or pincode. Every address opens straight into Google Maps on your phone.":"Search by town, district or pincode. Every address opens straight into Google Maps on your phone.","Already bought from us?":"Already bought from us?","LED · strips":"LED · strips","Names only — no third-party logos were lifted for this concept.":"Names only — no third-party logos were lifted for this concept.","Water & geysers":"Water & geysers","Contact":"Contact","Three steps. No maze.":"Three steps.<br>No maze.","Come and see it in person":"Come and see it in person","Director":"Director","Open the full catalogue":"Open the full catalogue","One tap opens WhatsApp with your whole list written out, or dials the helpline.":"One tap opens WhatsApp with your whole list written out, or dials the helpline.","Catalogue · 17 products · 10 categories":"Catalogue · 17 products · 10 categories","Send it to us":"Send it to us","Send it":"Send it"};
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
