# WHYNOT redesign — localisation.
#
# The rule this file follows, and the reason it is not a translation table:
# English copy that gets translated word-for-word into Telugu reads like a
# government circular. So the Telugu and Hindi lines here were WRITTEN in those
# languages — shorter than the English, idiomatic, and saying the thing a shop
# in Tanuku would actually say. Where the English has a marketing sentence, the
# Telugu often has four words.
#
#   EN  "One is probably 20 minutes away."
#   TE  "మీ ఊరిలోనే ఒకటి ఉంటుంది."      (there's one in your own town)
#   HI  "आपके शहर में ही एक है।"
#
# Three languages: English, Telugu (the language of the Godavari districts this
# business actually serves) and Hindi.
#
# LOCALISABLE is keyed by a normalised English string, so a single pass over each
# page can find the elements that need a hook, whichever trial they are in.

LANGS = ("en", "te", "hi")

LANG_LABEL = {"en": "English", "te": "తెలుగు", "hi": "हिन्दी"}
LANG_SHORT = {"en": "EN", "te": "తె", "hi": "हि"}

# html=True means the value may contain markup (<br>, <span>) and must be set as
# innerHTML. Everything else is plain text and is set as textContent.
LOCALISABLE = {
    # ---------------------------------------------------------------- nav
    "Home": dict(en="Home", te="మొదటి పేజీ", hi="होम"),
    "Catalogue": dict(en="Catalogue", te="వస్తువులు", hi="सामान"),
    "Showrooms": dict(en="Showrooms", te="మా షాపులు", hi="हमारी दुकानें"),
    "About": dict(en="About", te="మా గురించి", hi="हमारे बारे में"),
    "About us": dict(en="About us", te="మా గురించి", hi="हमारे बारे में"),
    "Contact": dict(en="Contact", te="సంప్రదించండి", hi="संपर्क"),
    "My list": dict(en="My list", te="నా జాబితా", hi="मेरी सूची"),
    "Shop": dict(en="Shop", te="వస్తువులు", hi="सामान"),
    "Company": dict(en="Company", te="కంపెనీ", hi="कंपनी"),
    "Come over": dict(en="Come over", te="కొట్టుకి రండి", hi="दुकान पर आइए"),
    "Call": dict(en="Call", te="కాల్", hi="कॉल"),

    # --------------------------------------------------------------- home
    "Godavari districts · since 1994": dict(
        en="Godavari districts · since 1994",
        te="గోదావరి జిల్లాలు · 1994 నుంచి",
        hi="गोदावरी ज़िले · 1994 से"),
    "Big brands.<br>Small towns.<br>Why not?": dict(
        en="Big brands.<br>Small towns.<br>Why not?",
        te="పెద్ద బ్రాండ్లు.<br>మన ఊరిలోనే.<br>ఎందుకు కాదు?",
        hi="बड़े ब्रांड.<br>अपने ही शहर में.<br>क्यों नहीं?", html=True),
    'Big brands. <span class="mark mark--marker">Small towns.</span> Why not?': dict(
        en='Big brands. <span class="mark mark--marker">Small towns.</span> Why not?',
        te='పెద్ద బ్రాండ్లు. <span class="mark mark--marker">మన ఊరిలోనే.</span> ఎందుకు కాదు?',
        hi='बड़े ब्रांड. <span class="mark mark--marker">अपने ही शहर में.</span> क्यों नहीं?', html=True),
    "Twenty-five WHYNOT showrooms in 23 towns, every major brand, and a phone number that still works five years after you buy. That has been the whole story since 1994.": dict(
        en="Twenty-five WHYNOT showrooms in 23 towns, every major brand, and a phone number that still works five years after you buy. That has been the whole story since 1994.",
        te="23 ఊళ్లలో 25 షోరూమ్లు. అన్ని పెద్ద బ్రాండ్లు. కొన్ని ఐదేళ్ల తర్వాత కూడా ఫోన్ ఎత్తుతాం — 1994 నుంచి ఇదే మా పద్ధతి.",
        hi="23 शहरों में 25 शोरूम. हर बड़ा ब्रांड. खरीदने के पांच साल बाद भी फोन उठता है — 1994 से यही हमारा तरीका है।"),
    "Twenty-five WHYNOT showrooms in 23 towns, every major brand, and a phone number that still works five years after you buy.": dict(
        en="Twenty-five WHYNOT showrooms in 23 towns, every major brand, and a phone number that still works five years after you buy.",
        te="23 ఊళ్లలో 25 షోరూమ్లు. అన్ని పెద్ద బ్రాండ్లు. కొన్ని ఐదేళ్ల తర్వాత కూడా ఫోన్ ఎత్తుతాం.",
        hi="23 शहरों में 25 शोरूम. हर बड़ा ब्रांड. पांच साल बाद भी फोन उठता है।"),
    "See what we sell": dict(en="See what we sell", te="ఏమేమి ఉన్నాయో చూడండి", hi="क्या-क्या है, देखें"),
    "Find my showroom": dict(en="Find my showroom", te="నా షాపు ఎక్కడ?", hi="मेरी दुकान कहाँ?"),
    "Open the full catalogue": dict(en="Open the full catalogue", te="పూర్తి జాబితా చూడండి", hi="पूरी सूची देखें"),
    "Open 10 am to 9 pm": dict(en="Open 10 am to 9 pm", te="ఉదయం 10 – రాత్రి 9", hi="सुबह 10 – रात 9"),
    "Open 10 am – 9 pm": dict(en="Open 10 am – 9 pm", te="ఉదయం 10 – రాత్రి 9", hi="सुबह 10 – रात 9"),
    "One helpline for 25 showrooms — 88862 22448": dict(
        en="One helpline for 25 showrooms — 88862 22448",
        te="25 షోప్‌లకు ఒకే నంబర్ — 88862 22448",
        hi="25 दुकानों के लिए एक ही नंबर — 88862 22448"),
    "A person answers, 10 am to 9 pm": dict(
        en="A person answers, 10 am to 9 pm",
        te="ఫోన్ ఎప్పుడూ మనిషే ఎత్తుతారు · 10 – 9",
        hi="फोन हमेशा आदमी उठाता है · 10 से 9"),
    "32 years": dict(en="32 years", te="32 ఏళ్లు", hi="32 साल"),
    "300 staff": dict(en="300 staff", te="300 మంది", hi="300 लोग"),
    "Delivery & install": dict(en="Delivery & install", te="డెలివరీ + ఫిట్టింగ్", hi="डिलीवरी + फिटिंग"),
    "Delivery &amp; install": dict(en="Delivery &amp; install", te="డెలివరీ + ఫిట్టింగ్", hi="डिलीवरी + फिटिंग"),
    "Open 10–9 daily": dict(en="Open 10–9 daily", te="రోజూ 10 – 9", hi="रोज़ 10 से 9"),

    # ---------------------------------------------------------------- stats
    "Customers served": dict(en="Customers served", te="కస్టమర్లు", hi="ग्राहक"),
    "Products sold": dict(en="Products sold", te="అమ్మిన వస్తువులు", hi="बिके सामान"),
    "Showrooms, 23 towns": dict(en="Showrooms, 23 towns", te="23 ఊళ్లలో షోరూమ్లు", hi="23 शहरों में शोरूम"),
    "Years since 1994": dict(en="Years since 1994", te="1994 నుంచి ఏళ్లు", hi="1994 से साल"),

    # ------------------------------------------------------------ sections
    "Shop by category": dict(en="Shop by category", te="ఏం కావాలి?", hi="क्या चाहिए?"),
    "Ten aisles.<br>One roof.": dict(
        en="Ten aisles.<br>One roof.",
        te="పది విభాగాలు.<br>ఒకే చోట.",
        hi="दस रैक.<br>एक ही दुकान.", html=True),
    "Prices move with the season, so every card asks for today's price — and we answer with the real number, not a range.": dict(
        en="Prices move with the season, so every card asks for today's price — and we answer with the real number, not a range.",
        te="ధరలు సీజన్‌బట్టి మారుతుంటాయి. అందుకే ప్రతి వస్తువుకు “ఈరోజు ధర అడగండి” అని ఉంటుంది — మేం నిజమైన నంబర్ చెప్తాం, రేంజ్ కాదు.",
        hi="दाम मौसम के हिसाब से बदलते हैं. इसलिए हर सामान पर “आज का दाम पूछें” लिखा है — हम असली रेट बताते हैं, रेंज नहीं।"),
    "Popular right now": dict(en="Popular right now", te="ఇప్పుడు డిమాండ్", hi="अभी ट्रेंड में"),
    "What people<br>actually ask for": dict(
        en="What people<br>actually ask for",
        te="జనం అడిగేవి<br>ఇవే",
        hi="लोग यही<br>मांगते हैं", html=True),
    "The four a month of “what's good in this budget?” conversations usually end on. Sample catalogue — today's price comes from your branch.": dict(
        en="The four a month of “what's good in this budget?” conversations usually end on. Sample catalogue — today's price comes from your branch.",
        te="“ఈ బడ్జెట్‌లో మంచిది ఏది?” అని అడిగినప్పుడు చాలామంది తీసుకునేవి ఇవే. ఇది శాంపిల్ జాబితా — ఈరోజు ధర మీ బ్రాంచ్ చెప్తుంది.",
        hi="“इस बजट में अच्छा क्या है?” — लोग यही लेते हैं. यह नमूना सूची है; आज का दाम आपकी ब्रांच बताएगी।"),
    "The name is the question": dict(en="The name is the question", te="పేరే ప్రశ్న", hi="नाम ही सवाल है"),
    "Why not…": dict(en="Why not…", te="ఎందుకు కాదు…", hi="क्यों नहीं…"),
    "Four questions WHYNOT has answered the same way since an LML showroom in Tanuku in 1994.": dict(
        en="Four questions WHYNOT has answered the same way since an LML showroom in Tanuku in 1994.",
        te="1994లో తనుకులో మొదటి షోరూమ్ నుంచి ఈ నాలుగు ప్రశ్నలకు మా జవాబు మారలేదు.",
        hi="1994 में तनुकु की पहली दुकान से इन चार सवालों का हमारा जवाब नहीं बदला।"),
    "Brands": dict(en="Brands", te="బ్రాండ్లు", hi="ब्रांड"),
    "Everything<br>you'd expect": dict(en="Everything<br>you'd expect", te="మీకు కావాల్సినవి<br>అన్నీ", hi="जो चाहिए<br>वो सब", html=True),
    "Names only — no third-party logos were lifted for this concept.": dict(
        en="Names only — no third-party logos were lifted for this concept.",
        te="పేర్లు మాత్రమే — ఈ డిజైన్ కోసం ఎవరి లోగోనూ వాడలేదు.",
        hi="सिर्फ नाम — इस डिज़ाइन में किसी का लोगो इस्तेमाल नहीं किया।"),
    "In their words": dict(en="In their words", te="వాళ్ల మాటల్లో", hi="उनके शब्दों में"),
    "People who<br>came back": dict(en="People who<br>came back", te="మళ్లీ వచ్చిన<br>వాళ్లు", hi="जो लौटकर<br>आए", html=True),
    "Reviews shown as they were written on the current site. Named, dated reviews with permission would do more work — see the notes in the repo.": dict(
        en="Reviews shown as they were written on the current site. Named, dated reviews with permission would do more work — see the notes in the repo.",
        te="ఇవి ప్రస్తుత సైట్‌లో రాసినట్టుగానే ఉన్నాయి. పేరు, తేదీతో అనుమతి తీసుకుని పెట్టితే ఇంకా బాగా పనిచేస్తాయి.",
        hi="ये समीक्षाएँ मौजूदा साइट जैसी ही हैं. नाम और तारीख के साथ इजाज़त लेकर लगाएँ तो ज़्यादा असर करेंगी।"),
    "Come and see it in person": dict(en="Come and see it in person", te="ఒక్కసారి వచ్చి చూడండి", hi="एक बार आकर देखिए"),
    "Pick what you like in the catalogue, send the list, and a person from your nearest branch calls with today's price.": dict(
        en="Pick what you like in the catalogue, send the list, and a person from your nearest branch calls with today's price.",
        te="నచ్చినవి జాబితాలో పెట్టి పంపండి. మీ దగ్గరి బ్రాంచ్ నుంచి ఒకరు ఫోన్ చేసి ఈరోజు ధర చెప్తారు.",
        hi="पसंद का सामान सूची में डालकर भेजिए. पास की ब्रांच से कोई फोन करके आज का दाम बताएगा।"),
    "Start a list": dict(en="Start a list", te="జాబితా మొదలుపెట్టు", hi="सूची बनाइए"),
    "Every town deserves the good stuff": dict(
        en="Every town deserves the good stuff",
        te="మంచి సరుకు మన ఊరికీ రావాలి",
        hi="अच्छा सामान अपने शहर में भी मिले"),

    # ----------------------------------------------------- catalogue page
    "Catalogue · 17 products · 10 categories": dict(
        en="Catalogue · 17 products · 10 categories",
        te="వస్తువులు · 17 ఐటమ్స్ · 10 విభాగాలు",
        hi="सामान · 17 आइटम · 10 श्रेणियाँ"),
    "Pick what you like.<br>We'll price it.": dict(
        en="Pick what you like.<br>We'll price it.",
        te="నచ్చినవి ఎంచుకోండి.<br>ధర మేం చెప్తాం.",
        hi="पसंद कीजिए.<br>दाम हम बताएंगे.", html=True),
    "Add anything you're curious about to <strong>my list</strong>, send it in one tap, and someone from your nearest branch replies with today's price and stock. No card details, no checkout maze.": dict(
        en="Add anything you're curious about to <strong>my list</strong>, send it in one tap, and someone from your nearest branch replies with today's price and stock. No card details, no checkout maze.",
        te="నచ్చినవి <strong>నా జాబితా</strong>లో పెట్టండి. ఒక్క ట్యాప్‌లో పంపండి. మీ బ్రాంచ్ నుంచి ధర, స్టాక్ చెప్తారు. కార్డ్ డిటెయిల్స్ అవసరం లేదు.",
        hi="पसंद का सामान <strong>मेरी सूची</strong> में डालिए. एक टैप में भेजिए. आपकी ब्रांच दाम और स्टॉक बताएगी. कार्ड डिटेल की ज़रूरत नहीं।", html=True),
    "Search: TV, fridge, 1.5 ton…": dict(en="Search: TV, fridge, 1.5 ton…", te="వెతకండి: TV, ఫ్రిజ్, 1.5 టన్…", hi="खोजें: TV, फ्रिज, 1.5 टन…"),
    "All towns": dict(en="All towns", te="అన్ని ఊళ్లు", hi="सभी शहर"),
    "How buying works here": dict(en="How buying works here", te="ఇక్కడ కొనడం ఎలా?", hi="यहाँ खरीदना कैसे?"),
    "Three steps.<br>No maze.": dict(en="Three steps.<br>No maze.", te="మూడు స్టెప్పులు.<br>అంతే.", hi="तीन कदम.<br>बस इतना.", html=True),

    # -------------------------------------------------------- stores page
    "Showrooms · 25 locations": dict(en="Showrooms · 25 locations", te="మా షాపులు · 25 చోట్లు", hi="हमारी दुकानें · 25 जगह"),
    "One is probably<br>20 minutes away.": dict(
        en="One is probably<br>20 minutes away.",
        te="మీ ఊరిలోనే<br>ఒకటి ఉంటుంది.",
        hi="आपके शहर में<br>ही एक है.", html=True),
    "Search by town, district or pincode. Every address opens straight into Google Maps on your phone.": dict(
        en="Search by town, district or pincode. Every address opens straight into Google Maps on your phone.",
        te="ఊరు, జిల్లా లేదా పిన్ కోడ్‌తో వెతకండి. ప్రతి చిరునామా నేరుగా మ్యాప్‌లో తెరుచుకుంటుంది.",
        hi="शहर, ज़िला या पिनकोड से खोजिए. हर पता सीधे मैप में खुलता है।"),
    "Copy number": dict(en="Copy number", te="నంబర్ కాపీ", hi="नंबर कॉपी"),
    "Town, district or pincode…": dict(en="Town, district or pincode…", te="ఊరు, జిల్లా, పిన్ కోడ్…", hi="शहर, ज़िला, पिनकोड…"),
    "All": dict(en="All", te="అన్నీ", hi="सब"),
    "all": dict(en="All", te="అన్నీ", hi="सब"),
    "Good to know": dict(en="Good to know", te="తెలుసుకోవాల్సినవి", hi="जान लीजिए"),
    "Before you<br>drive over": dict(en="Before you<br>drive over", te="బయలుదేరే<br>ముందు", hi="निकलने से<br>पहले", html=True),
    "Hours": dict(en="Hours", te="టైమింగ్", hi="समय"),
    "Stock is local": dict(en="Stock is local", te="స్టాక్ ఇక్కడే", hi="स्टॉक यहीं है"),
    "Brand stores in Tanuku": dict(en="Brand stores in Tanuku", te="తనుకులో బ్రాండ్ స్టోర్లు", hi="तनुकु में ब्रांड स्टोर"),
    "Already bought from us?": dict(en="Already bought from us?", te="ఇదివరకే కొన్నారా?", hi="पहले खरीदा है?"),

    # ------------------------------------------------------- about page
    "One shop.<br>One question.": dict(en="One shop.<br>One question.", te="ఒక కొట్టు.<br>ఒక ప్రశ్న.", hi="एक दुकान.<br>एक सवाल.", html=True),
    "The story": dict(en="The story", te="మా కథ", hi="हमारी कहानी"),
    "Six panels,<br>32 years": dict(en="Six panels,<br>32 years", te="ఆరు మజిలీలు,<br>32 ఏళ్లు", hi="छह पड़ाव,<br>32 साल", html=True),
    "Leadership today": dict(en="Leadership today", te="ఇప్పటి బాధ్యతలు", hi="आज की ज़िम्मेदारी"),
    "The family<br>at the desk": dict(en="The family<br>at the desk", te="కౌంటర్‌లో<br>ఇంటి వాళ్లే", hi="काउंटर पर<br>परिवार ही", html=True),
    "Partners": dict(en="Partners", te="భాగస్వాములు", hi="साझेदार"),
    "Trusted<br>to sell": dict(en="Trusted<br>to sell", te="నమ్మకమైన<br>బ్రాండ్లు", hi="भरोसे के<br>ब्रांड", html=True),

    # ----------------------------------------------------- contact page
    "Tell us what you need.<br>A person calls back.": dict(
        en="Tell us what you need.<br>A person calls back.",
        te="ఏం కావాలో చెప్పండి.<br>మేమే ఫోన్ చేస్తాం.",
        hi="बताइए क्या चाहिए.<br>हम फोन करेंगे.", html=True),
    "No ticket numbers, no “within 48 hours”. Leave your number and someone from your nearest showroom rings you between 10 am and 9 pm.": dict(
        en="No ticket numbers, no “within 48 hours”. Leave your number and someone from your nearest showroom rings you between 10 am and 9 pm.",
        te="టికెట్ నంబర్లు లేవు, “48 గంటల్లో” లేదు. నంబర్ ఇవ్వండి — మీ దగ్గరి షాప్ నుంచి 10 – 9 మధ్య ఫోన్ వస్తుంది.",
        hi="कोई टिकट नंबर नहीं, “48 घंटे में” नहीं. नंबर दीजिए — पास की दुकान से 10 से 9 के बीच फोन आएगा।"),
    "Your name": dict(en="Your name", te="మీ పేరు", hi="आपका नाम"),
    "Mobile number": dict(en="Mobile number", te="మొబైల్ నంబర్", hi="मोबाइल नंबर"),
    "Your town": dict(en="Your town", te="మీ ఊరు", hi="आपका शहर"),
    "What are you looking for?": dict(en="What are you looking for?", te="ఏం కావాలి?", hi="क्या चाहिए?"),
    "Send it": dict(en="Send it", te="పంపండి", hi="भेजें"),
    "WhatsApp instead": dict(en="WhatsApp instead", te="WhatsApp లో పంపు", hi="WhatsApp पर भेजें"),
    "Send on WhatsApp": dict(en="Send on WhatsApp", te="WhatsApp లో పంపు", hi="WhatsApp पर भेजें"),

    # ------------------------------------------------------------- 404
    "This page is<br>missing.": dict(en="This page is<br>missing.", te="ఈ పేజీ<br>దొరకలేదు.", hi="यह पन्ना<br>नहीं मिला.", html=True),
    "Old link, moved page, or a typo in the address. Nothing is lost — the showrooms are all where you left them.": dict(
        en="Old link, moved page, or a typo in the address. Nothing is lost — the showrooms are all where you left them.",
        te="పాత లింక్, తరిగిన పేజీ, లేదా అడ్రస్‌లో తప్పు. ఏం పోలేదు — షాపులన్నీ ఉన్నచోటే ఉన్నాయి.",
        hi="पुराना लिंक, हटा पन्ना, या पते में गलती. कुछ नहीं खोया — दुकानें अपनी जगह हैं।"),
    "Back home": dict(en="Back home", te="మొదటి పేజీకి", hi="होम पर"),
    "Error 404": dict(en="Error 404", te="ఎర్రర్ 404", hi="एरर 404"),
}

# Strings the JavaScript builds at runtime. These live in products.js / stores.js /
# contact.js and are swapped to T("key") calls by the localiser.
JS_STRINGS = {
    "Add to list": ("add", dict(en="Add to list", te="జాబితాలో చేర్చు", hi="सूची में डालें")),
    "+ Add to my list": ("add", dict(en="+ Add to my list", te="+ జాబితాలో చేర్చు", hi="+ सूची में डालें")),
    "In my list": ("added", dict(en="In my list", te="జాబితాలో ఉంది", hi="सूची में है")),
    "Removed from your list": ("removed", dict(en="Removed from your list", te="జాబితా నుంచి తీసేశాం", hi="सूची से हटा दिया")),
    " item": ("item", dict(en=" item", te=" వస్తువు", hi=" सामान")),
    " items": ("items", dict(en=" items", te=" వస్తువులు", hi=" सामान")),
    "Added to your list": ("addedToast", dict(en="Added to your list", te="జాబితాలో చేర్చాం", hi="सूची में डाल दिया")),
    "In your list": ("added", dict(en="In your list", te="జాబితాలో ఉంది", hi="सूची में है")),
    "Ask today\u2019s price": ("askPrice", dict(en="Ask today\u2019s price", te="ఈరోజు ధర అడగండి", hi="आज का दाम पूछें")),
    "Ask for today\u2019s price": ("askPrice", dict(en="Ask for today\u2019s price", te="ఈరోజు ధర అడగండి", hi="आज का दाम पूछें")),
    "Ask for today's price": ("askPrice", dict(en="Ask for today's price", te="ఈరోజు ధర అడగండి", hi="आज का दाम पूछें")),
    "Send on WhatsApp": ("wa", dict(en="Send on WhatsApp", te="WhatsApp లో పంపు", hi="WhatsApp पर भेजें")),
    "Email the list": ("emailList", dict(en="Email the list", te="మెయిల్ చేయండి", hi="ईमेल करें")),
    "Browse the catalogue": ("browse", dict(en="Browse the catalogue", te="వస్తువులు చూడండి", hi="सामान देखें")),
    "Nothing matches that": ("noMatch", dict(en="Nothing matches that", te="అలాంటిది ఏమీ లేదు", hi="ऐसा कुछ नहीं मिला")),
    "Clear filters": ("clearF", dict(en="Clear filters", te="ఫిల్టర్లు తీసేయి", hi="फ़िल्टर हटाएँ")),
    "Your list is empty": ("emptyList", dict(en="Your list is empty", te="జాబితా ఖాళీగా ఉంది", hi="सूची खाली है")),
    "Ask about this": ("askAbout", dict(en="Ask about this", te="దీని గురించి అడగండి", hi="इसके बारे में पूछें")),
    "Remove": ("remove", dict(en="Remove", te="తీసేయి", hi="हटाएँ")),
    "Directions": ("directions", dict(en="Directions", te="మ్యాప్‌లో చూడండి", hi="मैप में देखें")),
    "Copy address": ("copyAddr", dict(en="Copy address", te="చిరునామా కాపీ", hi="पता कॉपी")),
    "Browse the catalogue": ("browse", dict(en="Browse the catalogue", te="వస్తువులు చూడండి", hi="सामान देखें")),
    "Clear filters.": ("clearF2", dict(en="Clear filters.", te="ఫిల్టర్లు తీసేయి.", hi="फ़िल्टर हटाएँ।")),
    "Hit \u201cadd to list\u201d on anything you want priced. It stays on this device until you send it.": (
        "emptyHelp",
        dict(en="Hit \u201cadd to list\u201d on anything you want priced. It stays on this device until you send it.",
             te="ధర కావాల్సినవాటికి “జాబితాలో చేర్చు” నొక్కండి. పంపే వరకు ఇదే ఫోన్‌లో ఉంటుంది.",
             hi="जिसका दाम चाहिए उस पर “सूची में डालें” दबाइए. भेजने तक यहीं रहता है।")),
    "No card details, no account, nothing charged. A person from your nearest branch replies with today\u2019s price and what is in stock.": (
        "listNote",
        dict(en="No card details, no account, nothing charged. A person from your nearest branch replies with today\u2019s price and what is in stock.",
             te="కార్డ్ డిటెయిల్స్ లేవు, అకౌంట్ లేదు, డబ్బు వసూలు లేదు. మీ బ్రాంచ్ నుంచి ఒకరు ధర, స్టాక్ చెప్తారు.",
             hi="कार्ड डिटेल नहीं, अकाउंट नहीं, कोई पैसा नहीं. आपकी ब्रांच से कोई दाम और स्टॉक बताएगा।")),
    "we will price it and call you": ("weWillPrice", dict(en="we will price it and call you", te="ధర చెప్పి ఫోన్ చేస్తాం", hi="दाम बताकर फोन करेंगे")),
    "In stock at": ("inStockAt", dict(en="In stock at", te="స్టాక్ ఉన్నది:", hi="स्टॉक है:")),
    "item": ("item", dict(en="item", te="ఐటమ్", hi="आइटम")),
    "items": ("items", dict(en="items", te="ఐటమ్స్", hi="आइटम")),
    "products · 10 categories · ask for today's price": ("countAll", dict(
        en="products · 10 categories · ask for today's price",
        te="వస్తువులు · 10 విభాగాలు · ఈరోజు ధర అడగండి",
        hi="सामान · 10 श्रेणियाँ · आज का दाम पूछें")),
    "Showing": ("showing", dict(en="Showing", te="చూపిస్తున్నాం:", hi="दिखा रहे हैं:")),
    "of": ("of", dict(en="of", te="మొత్తం", hi="कुल")),
    "Please enter your name.": ("errName", dict(en="Please enter your name.", te="మీ పేరు రాయండి.", hi="अपना नाम लिखिए।")),
    "Enter a 10-digit mobile number.": ("errMobile", dict(en="Enter a 10-digit mobile number.", te="10 అంకెల మొబైల్ నంబర్ రాయండి.", hi="10 अंकों का मोबाइल नंबर लिखिए।")),
    "Tell us what you are looking for.": ("errMessage", dict(en="Tell us what you are looking for.", te="ఏం కావాలో రాయండి.", hi="क्या चाहिए, लिखिए।")),
    "Thank you, ": ("thanks", dict(en="Thank you, ", te="ధన్యవాదాలు, ", hi="धन्यवाद, ")),
    " — your enquiry was not actually sent.": ("notSent", dict(en=" — your enquiry was not actually sent.", te=" — మీ వివరాలు నిజంగా పంపబడలేదు.", hi=" — आपकी जानकारी असल में नहीं भेजी गई।")),
    "This is a concept build with no server behind it yet, so nothing has actually been sent. ": (
        "conceptNote",
        dict(en="This is a concept build with no server behind it yet, so nothing has actually been sent. ",
             te="ఇది ఒక డిజైన్ డెమో — వెనుక సర్వర్ లేదు, కాబట్టి నిజంగా ఏమీ పంపబడలేదు. ",
             hi="यह एक डिज़ाइन डेमो है — पीछे सर्वर नहीं है, इसलिए असल में कुछ नहीं भेजा गया। ")),
    "We will call you on ": ("willCall", dict(en="We will call you on ", te="మేం ఫోన్ చేస్తాం: ", hi="हम फोन करेंगे: ")),
    "In a working build this would reach the branch, and they would call you back.": (
        "workingNote",
        dict(en="In a working build this would reach the branch, and they would call you back.",
             te="అసలు సైట్‌లో ఇది నేరుగా బ్రాంచ్‌కి వెళ్తుంది, వాళ్లే ఫోన్ చేస్తారు.",
             hi="असली साइट में यह सीधे ब्रांच पहुँचता, वही फोन करती।")),
    "Tell us a model name and your town — we will check the branch stock.": (
        "contactHint",
        dict(en="Tell us a model name and your town — we will check the branch stock.",
             te="మోడల్ పేరు, మీ ఊరు రాయండి — స్టాక్ చూసి చెప్తాం.",
             hi="मॉडल का नाम और अपना शहर लिखिए — स्टॉक देखकर बताएंगे।")),
}


# ---------------------------------------------------------------------------
# The scripts build their markup at runtime, and the three earliest trials write
# some of those strings differently. So the localiser patches by PATTERN, not by
# exact literal: each rule below matches every spelling of the same sentence in
# any trial and replaces it with one T("key") lookup.
# ---------------------------------------------------------------------------
JS_LITERALS = {
    "In my list": "added",
    "&#10003; In my list": "added",
    "In your list": "added",
    "+ Add to my list": "add",
    "Add to list": "add",
    "Removed from your list": "removed",
    "Added to your list": "addedToast",
    "Browse the catalogue": "browse",
    "Nothing matches that": "noMatch",
    "Clear filters": "clearF",
    "Clear filters.": "clearF2",
    "Ask about this": "askAbout",
    "Copy address": "copyAddr",
    "Copy number": "copyNum",
    "Your list is empty": "emptyList",
    "Directions": "directions",
    "Send on WhatsApp": "wa",
    "Email the list": "emailList",
    " item": "item",
    " items": "items",
    "Showing": "showing",
    "of": "of",
    "Ask today\u2019s price": "askPrice",
    "Ask for today\u2019s price": "askPrice",
    "Ask for today's price": "askPrice",
}

# The two literals that carry something dynamic beside them. Each entry is
# (whole literal value, text before the phrase, key, English, text after), and
# the runtime writes it out as:
#     'before' + T("key", "English") + 'after'
# using whichever quote the source used. Nothing here is a substring match.
JS_EXPRESSIONS = [
    ('aria-label="Remove ', 'aria-label="', "remove", "Remove", " "),
    ('">Remove</button>', '">', "remove", "Remove", "</button>"),
]

# Handled in the browser instead, because they sit beside dynamic content:
#   "In stock at <towns>",   "Showing 5 of 17 products"
RUNTIME_PATTERNS = [
    dict(re=r"^([0-9]+) products · sample catalogue, real prices on request$",
         en="$1 products · sample catalogue, real prices on request",
         te="$1 వస్తువులు · ఇది నమూనా జాబితా, ధరలు అడగండి",
         hi="$1 सामान · यह नमूना सूची है, दाम पूछिए"),
    dict(re=r"^([0-9]+) products across ([0-9]+) categories$",
         en="$1 products across $2 categories",
         te="$1 వస్తువులు · $2 విభాగాలు",
         hi="$1 सामान · $2 श्रेणियाँ"),
    dict(re=r"^([0-9]+) products · ([0-9]+) categories · ask for today(?:'|’|&rsquo;)s price$",
         en="$1 products · $2 categories · ask for today's price",
         te="$1 వస్తువులు · $2 విభాగాలు · ఈరోజు ధర అడగండి",
         hi="$1 सामान · $2 श्रेणियाँ · आज का दाम पूछें"),
    dict(re=r"^([0-9]+) products · 10 categories · ask for today(?:'|’|&rsquo;)s price$",
         en="$1 products · 10 categories · ask for today's price",
         te="$1 వస్తువులు · 10 విభాగాలు · ఈరోజు ధర అడగండి",
         hi="$1 सामान · 10 श्रेणियाँ · आज का दाम पूछें"),
    dict(re=r"^([0-9]+) (?:items?|item) — we will price it and call you$",
         en="$1 items — we will price it and call you",
         te="$1 — ధర చెప్పి ఫోన్ చేస్తాం",
         hi="$1 — दाम बताकर फोन करेंगे"),
    dict(re=r"^Ask (?:for )?today(?:'|’|&rsquo;)s price$",
         en="Ask today's price", te="ఈరోజు ధర అడగండి", hi="आज का दाम पूछें"),
    dict(re=r"^Remove", en="Remove", te="తీసేయి", hi="हटाएँ"),
    dict(re=r"^Showing ([0-9]+) of ([0-9]+) products$",
         en="Showing $1 of $2 products",
         te="చూపిస్తున్నాం: $1 / $2",
         hi="दिखा रहे हैं: $1 / $2"),
    dict(re=r"^(In stock at) ", en="In stock at $1", te="స్టాక్ ఉన్నది: ", hi="स्टॉक है: "),
]

LEFTOVER_WATCH = [
    "Ask about this", "Clear filters", "Copy address", "Directions", "Browse the catalogue",
    "Nothing matches that", "Email the list", "In stock at", "Your list is empty",
]

# ---------------------------------------------------------------------------
# Trial 07's own copy. Kept in its own file because this design's English is
# terser, so its Telugu and Hindi are written differently again — merged in here
# so every tool that reads the phrase table picks them up.
from i18n07 import PHRASES as _T7_PHRASES, JS as _T7_JS, PATTERNS as _T7_PATTERNS

LOCALISABLE.update(_T7_PHRASES)
for _en, (_key, _vals) in _T7_JS.items():
    JS_STRINGS[_en] = (_key, _vals)
RUNTIME_PATTERNS = list(RUNTIME_PATTERNS) + list(_T7_PATTERNS)
