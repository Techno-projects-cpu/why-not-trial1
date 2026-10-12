# Trial 07's copy, in the same three languages.
#
# The Telugu and Hindi here are written in those languages rather than translated
# from the English, and they are shorter on purpose: this design's voice is terse
# English, and a literal translation of a terse English sentence reads like a
# telegram in Telugu. Where the English needs a clause, the Telugu often needs
# three words — so the two text blocks genuinely differ in shape.
#
# Proper nouns (the family names, the streets, WHYNOT itself) stay as they are:
# transliterating an address only makes it harder to show to a driver.

PHRASES = {
    # ---------------------------------------------------------------- shell
    "Skip to content": dict(en="Skip to content", te="కంటెంట్‌కు వెళ్లు", hi="सीधे सामग्री पर जाएँ"),
    "Electronics · 1994": dict(en="Electronics · 1994", te="ఎలక్ట్రానిక్స్ · 1994", hi="इलेक्ट्रॉनिक्स · 1994"),
    "Electronics": dict(en="Electronics", te="ఎలక్ట్రానిక్స్", hi="इलेक्ट्रॉनिक्स"),
    "Open": dict(en="Open", te="చూడు", hi="खोलें"),
    "Light": dict(en="Light", te="వెలుగు", hi="लाइट"),
    "Dark": dict(en="Dark", te="చీకటి", hi="डार्क"),
    "0 items": dict(en="0 items", te="0 వస్తువులు", hi="0 सामान"),
    "Towns served": dict(en="Towns served", te="ఊళ్లు", hi="शहर"),
    "Trading since": dict(en="Trading since", te="మొదలు", hi="शुरुआत"),
    "People on the floor": dict(en="People on the floor", te="మా జనం", hi="हमारे लोग"),
    "A redesign concept for whynotindia.in, built as portfolio work. Not affiliated with the company and not deployed anywhere. Artwork is AI-generated stand-in art, and the enquiry form has no server behind it.":
        dict(en="A redesign concept for whynotindia.in, built as portfolio work. Not affiliated with the company and not deployed anywhere. Artwork is AI-generated stand-in art, and the enquiry form has no server behind it.",
             te="ఇది whynotindia.in కోసం చేసిన డిజైన్ నమూనా. కంపెనీకి సంబంధం లేదు, ఎక్కడా లైవ్‌లో లేదు. బొమ్మలు AI తో చేసినవి. ఫారం ఎక్కడికీ పంపదు.",
             hi="यह whynotindia.in के लिए बनाया गया डिज़ाइन नमूना है. कंपनी से कोई संबंध नहीं, कहीं लाइव नहीं. तस्वीरें AI से बनी हैं. फ़ॉर्म कहीं नहीं भेजता."),

    # ---------------------------------------------------------------- 404
    "That page isn't here.": dict(en="That page isn't here.", te="ఆ పేజీ ఇక్కడ లేదు.", hi="वह पन्ना यहाँ नहीं है."),
    "An old link, a moved page, or a typo in the address. Nothing is lost — the catalogue and all 25 showrooms are where you left them.":
        dict(en="An old link, a moved page, or a typo in the address. Nothing is lost — the catalogue and all 25 showrooms are where you left them.",
             te="పాత లింక్, తరిగిన పేజీ, లేదా అడ్రస్‌లో తప్పు. ఏం పోలేదు — జాబితా, 25 షాపులూ ఉన్నచోటే ఉన్నాయి.",
             hi="पुराना लिंक, हटा पन्ना, या पते में गलती. कुछ नहीं खोया — सूची और सभी 25 दुकानें अपनी जगह हैं."),
    "Open the catalogue": dict(en="Open the catalogue", te="జాబితా చూడు", hi="सूची खोलें"),
    "Find a showroom": dict(en="Find a showroom", te="షాపు వెతుకు", hi="दुकान खोजें"),
    "Call a person": dict(en="Call a person", te="ఫోన్ చేయండి", hi="फ़ोन करें"),
    "Search the catalogue instead": dict(en="Search the catalogue instead", te="బదులుగా జాబితాలో వెతుకు", hi="इसके बजाय सूची में खोजें"),
    "Search runs on the catalogue page; this box takes you there with your words.":
        dict(en="Search runs on the catalogue page; this box takes you there with your words.",
             te="వెతకడం జాబితా పేజీలో జరుగుతుంది. ఇక్కడ టైప్ చేస్తే అక్కడికి తీసుకెళ్తాం.",
             hi="खोज सूची वाले पन्ने पर चलती है. यहाँ लिखें, हम आपको वहीं ले जाएँगे."),

    # ---------------------------------------------------------------- about
    "About · trading since 1994": dict(en="About · trading since 1994", te="మా గురించి · 1994 నుంచి", hi="हमारे बारे में · 1994 से"),
    "Thirty-two years of asking why not.":
        dict(en="Thirty-two years of asking why not.", te="ముప్ఫై రెండేళ్లు “ఎందుకు కాదు” అని అడుగుతూ.", hi="बत्तीस साल से “क्यों नहीं” पूछते हुए."),
    "The name is a question the family kept asking: why not open here, why not stock that, why not service what we sell. It started with two-wheelers in Tanuku and became one of the largest appliance retailers in the Godavari districts.":
        dict(en="The name is a question the family kept asking: why not open here, why not stock that, why not service what we sell. It started with two-wheelers in Tanuku and became one of the largest appliance retailers in the Godavari districts.",
             te="పేరే ఒక ప్రశ్న. ఇక్కడ ఎందుకు కాదు, అది ఎందుకు అమ్మకూడదు, అమ్మినది ఎందుకు సర్వీస్ చేయకూడదు. తనుకులో రెండు చక్రాలతో మొదలై, గోదావరి జిల్లాల్లో పెద్ద ఎలక్ట్రానిక్స్ షాపుల్లో ఒకటైంది.",
             hi="नाम ही सवाल है. यहाँ क्यों नहीं, वह क्यों न रखें, बेचा सामान क्यों न सुधारें. तनुकू में दोपहिया से शुरू हुआ कारोबार गोदावरी ज़िलों की बड़ी इलेक्ट्रॉनिक्स दुकानों में गिना जाता है."),
    "The facts": dict(en="The facts", te="వాస్తవాలు", hi="तथ्य"),
    "Founded": dict(en="Founded", te="ప్రారంభం", hi="स्थापना"),
    "27 February 1994, as an LML two-wheeler showroom in Tanuku":
        dict(en="27 February 1994, as an LML two-wheeler showroom in Tanuku",
             te="27 ఫిబ్రవరి 1994, తనుకులో LML షోరూమ్‌గా",
             hi="27 फ़रवरी 1994, तनुकू में LML शोरूम के रूप में"),
    "Today": dict(en="Today", te="ఇప్పుడు", hi="आज"),
    "25 showrooms, 23 towns, 300 people": dict(en="25 showrooms, 23 towns, 300 people", te="25 షాపులు, 23 ఊళ్లు, 300 మంది", hi="25 दुकानें, 23 शहर, 300 लोग"),
    "What we sell": dict(en="What we sell", te="ఏం అమ్ముతాం", hi="क्या बेचते हैं"),
    "Televisions, refrigeration, cooling, laundry, small appliances, lighting, mobile":
        dict(en="Televisions, refrigeration, cooling, laundry, small appliances, lighting, mobile",
             te="టీవీలు, ఫ్రిజ్‌లు, ఏసీలు, వాషింగ్ మెషీన్లు, చిన్న వస్తువులు, లైటింగ్, మొబైల్స్",
             hi="टीवी, फ्रिज, एसी, वॉशिंग मशीन, छोटे सामान, लाइटिंग, मोबाइल"),
    "How we sell": dict(en="How we sell", te="ఎలా అమ్ముతాం", hi="कैसे बेचते हैं"),
    "Ask for today's price. No invented numbers on this page":
        dict(en="Ask for today's price. No invented numbers on this page",
             te="ఈరోజు ధర అడగండి. ఈ పేజీలో ఊహించిన ధరలు లేవు.",
             hi="आज का दाम पूछिए. इस पन्ने पर कोई बनावटी दाम नहीं."),
    "Service": dict(en="Service", te="సర్వీస్", hi="सर्विस"),
    "Through each brand's authorised network, coordinated by the branch you bought at":
        dict(en="Through each brand's authorised network, coordinated by the branch you bought at",
             te="మీరు కొన్న షాపు ద్వారానే, కంపెనీ అధికారిక సర్వీస్ నెట్‌వర్క్‌లో",
             hi="आपने जिस दुकान से खरीदा, उसी के ज़रिए कंपनी के अधिकृत नेटवर्क से"),
    "10 am – 9 pm, every day": dict(en="10 am – 9 pm, every day", te="ఉదయం 10 – రాత్రి 9, రోజూ", hi="सुबह 10 – रात 9, रोज़"),
    "10 am to 9 pm, every day": dict(en="10 am to 9 pm, every day", te="ఉదయం 10 నుంచి రాత్రి 9 వరకు, రోజూ", hi="सुबह 10 से रात 9 तक, रोज़"),
    "Helpline": dict(en="Helpline", te="హెల్ప్‌లైన్", hi="हेल्पलाइन"),
    "Email": dict(en="Email", te="ఈమెయిల్", hi="ईमेल"),
    "How it got here": dict(en="How it got here", te="ఎలా ఇక్కడికి వచ్చింది", hi="यहाँ तक कैसे पहुँचे"),
    "An LML showroom opens in Tanuku. Two-wheeler finance was the whole business.":
        dict(en="An LML showroom opens in Tanuku. Two-wheeler finance was the whole business.",
             te="తనుకులో LML షోరూమ్ మొదలైంది. అప్పుడు రెండు చక్రాల ఫైనాన్సే గిట్టుబాటు.",
             hi="तनुकू में LML शोरूम खुला. तब दोपहिया फ़ाइनेंस ही पूरा धंधा था."),
    "Bajaj added. The family starts keeping stock of what people actually ask for.":
        dict(en="Bajaj added. The family starts keeping stock of what people actually ask for.",
             te="బజాజ్ చేరింది. జనం అడిగేది స్టాక్‌లో పెట్టడం మొదలైంది.",
             hi="बजाज जुड़ी. लोग जो माँगते थे, वही स्टॉक में रखना शुरू हुआ."),
    "Electronics, and with it the appliance counters that carry the shop today.":
        dict(en="Electronics, and with it the appliance counters that carry the shop today.",
             te="ఎలక్ట్రానిక్స్ మొదలైంది. ఈ రోజు షాపును నడిపేది అదే.",
             hi="इलेक्ट्रॉनिक्स शुरू हुआ. आज दुकान उसी से चलती है."),
    "25 showrooms, 23 towns, 300 people, and a helpline that a person answers.":
        dict(en="25 showrooms, 23 towns, 300 people, and a helpline that a person answers.",
             te="25 షాపులు, 23 ఊళ్లు, 300 మంది. హెల్ప్‌లైన్‌లో మనిషే మాట్లాడతారు.",
             hi="25 दुकानें, 23 शहर, 300 लोग. हेल्पलाइन पर इंसान ही बोलता है."),
    "Who runs it": dict(en="Who runs it", te="ఎవరు నడుపుతున్నారు", hi="कौन चलाते हैं"),
    "Managing Director": dict(en="Managing Director", te="మేనేజింగ్ డైరెక్టర్", hi="मैनेजिंग डायरेक्टर"),
    "Director": dict(en="Director", te="డైరెక్టర్", hi="डायरेक्टर"),
    "What we would not put on a page": dict(en="What we would not put on a page", te="పేజీలో పెట్టనివి", hi="जो पन्ने पर नहीं लिखेंगे"),
    "No invented prices, no awards we have not won, no countdown timers. The site this concept replaces said \"40 branches across 36 locations\" in one place and \"25 branches in 23 cities\" in another; a shop this size should be able to say one true number. Twenty-five, in 23 towns.":
        dict(en="No invented prices, no awards we have not won, no countdown timers. The site this concept replaces said \"40 branches across 36 locations\" in one place and \"25 branches in 23 cities\" in another; a shop this size should be able to say one true number. Twenty-five, in 23 towns.",
             te="ఊహించిన ధరలు లేవు, తెచ్చుకోని అవార్డులు లేవు, కౌంట్‌డౌన్ గడియారాలు లేవు. పాత సైట్ ఒక చోట “36 ప్రాంతాల్లో 40 శాఖలు”, మరో చోట “23 నగరాల్లో 25 శాఖలు” అని చెప్పింది. నిజం ఒక్కటే ఉండాలి — 23 ఊళ్లలో 25 షాపులు.",
             hi="बनावटी दाम नहीं, बिना जीते पुरस्कार नहीं, काउंटडाउन नहीं. पुरानी साइट ने कहीं “36 जगहों पर 40 शाखाएँ” लिखा, कहीं “23 शहरों में 25 शाखाएँ”. सच एक ही होना चाहिए — 23 शहरों में 25 दुकानें."),
    "Figures on this page come from the company's own public website, read in October 2026.":
        dict(en="Figures on this page come from the company's own public website, read in October 2026.",
             te="ఇక్కడి లెక్కలు కంపెనీ సైట్ నుంచే, అక్టోబర్ 2026లో చూసినవి.",
             hi="यहाँ के आँकड़े कंपनी की साइट से, अक्टूबर 2026 में देखे गए."),

    # --------------------------------------------------------------- contact
    "Contact · a person answers": dict(en="Contact · a person answers", te="సంప్రదించండి · మనిషే మాట్లాడతారు", hi="संपर्क · इंसान जवाब देता है"),
    "Talk to a person.": dict(en="Talk to a person.", te="మనిషితో మాట్లాడండి.", hi="किसी इंसान से बात करें."),
    "The helpline is answered at the branch, not by a call centre. Tell us the model and your town and you get today's price, stock and a delivery date — in one call.":
        dict(en="The helpline is answered at the branch, not by a call centre. Tell us the model and your town and you get today's price, stock and a delivery date — in one call.",
             te="ఫోన్ షాపులోనే ఎత్తుతారు, కాల్ సెంటర్‌లో కాదు. మోడల్, మీ ఊరు చెప్పండి — ఈరోజు ధర, స్టాక్, డెలివరీ తేదీ ఒకే కాల్‌లో.",
             hi="फ़ोन दुकान पर उठता है, कॉल सेंटर पर नहीं. मॉडल और अपना शहर बताइए — आज का दाम, स्टॉक और डिलीवरी की तारीख़ एक ही कॉल में."),
    "Send an enquiry": dict(en="Send an enquiry", te="విచారణ పంపండి", hi="पूछताछ भेजें"),
    "Your name": dict(en="Your name", te="మీ పేరు", hi="आपका नाम"),
    "Mobile number": dict(en="Mobile number", te="మొబైల్ నంబర్", hi="मोबाइल नंबर"),
    "What are you looking for?": dict(en="What are you looking for?", te="మీకు ఏం కావాలి?", hi="आपको क्या चाहिए?"),
    "Send enquiry": dict(en="Send enquiry", te="పంపండి", hi="भेजें"),
    "What happens next": dict(en="What happens next", te="తర్వాత ఏం జరుగుతుంది", hi="आगे क्या होगा"),
    "We read it": dict(en="We read it", te="మేం చదువుతాం", hi="हम पढ़ते हैं"),
    "A person at the nearest branch, not a queue.": dict(en="A person at the nearest branch, not a queue.", te="దగ్గరి షాపులో ఒకరు, క్యూ కాదు.", hi="नज़दीकी दुकान का एक व्यक्ति, कोई कतार नहीं."),
    "We price it": dict(en="We price it", te="ధర చెప్తాం", hi="दाम बताते हैं"),
    "You decide": dict(en="You decide", te="మీరు నిర్ణయించండి", hi="फ़ैसला आपका"),
    "Nothing is charged from this site and no account is needed.":
        dict(en="Nothing is charged from this site and no account is needed.",
             te="ఈ సైట్ నుంచి డబ్బు వసూలు ఉండదు, అకౌంట్ అవసరం లేదు.",
             hi="इस साइट से कोई भुगतान नहीं, खाता बनाने की ज़रूरत नहीं."),
    "Or just call": dict(en="Or just call", te="లేదా ఫోన్ చేయండి", hi="या सीधे फ़ोन करें"),
    "Flagship": dict(en="Flagship", te="ప్రధాన షాపు", hi="मुख्य दुकान"),

    # ------------------------------------------------------------------ home
    "WHYNOT Electronics · Tanuku": dict(en="WHYNOT Electronics · Tanuku", te="WHYNOT ఎలక్ట్రానిక్స్ · తనుకు", hi="WHYNOT इलेक्ट्रॉनिक्स · तनुकू"),
    "The shop, not the app.": dict(en="The shop, not the app.", te="యాప్ కాదు, షాపు.", hi="ऐप नहीं, दुकान."),
    "Twenty-five showrooms across the Godavari districts and Visakhapatnam. Pick what you want, send the list, and someone from your nearest branch comes back with today's price and stock.":
        dict(en="Twenty-five showrooms across the Godavari districts and Visakhapatnam. Pick what you want, send the list, and someone from your nearest branch comes back with today's price and stock.",
             te="గోదావరి జిల్లాలు, విశాఖపట్నంలో కలిపి 25 షాపులు. నచ్చినవి ఎంచుకోండి, జాబితా పంపండి — దగ్గరి షాపు నుంచి ఈరోజు ధర, స్టాక్ చెప్పడానికి ఫోన్ వస్తుంది.",
             hi="गोदावरी ज़िलों और विशाखापट्टनम में 25 दुकानें. पसंद का सामान चुनें, सूची भेजें — नज़दीकी दुकान से आज का दाम और स्टॉक बताने फ़ोन आएगा."),
    "Find your showroom": dict(en="Find your showroom", te="మీ షాపు కనుగొనండి", hi="अपनी दुकान खोजें"),
    "Stand-in photograph, generated for this concept — not a real branch.":
        dict(en="Stand-in photograph, generated for this concept — not a real branch.",
             te="నమూనా ఫోటో — ఇది నిజమైన షాపు కాదు.",
             hi="नमूना तस्वीर — असली दुकान नहीं."),
    "Where we are": dict(en="Where we are", te="మేమెక్కడ", hi="हम कहाँ हैं"),
    "Fifteen in West Godavari, nine in East Godavari, one in Visakhapatnam.":
        dict(en="Fifteen in West Godavari, nine in East Godavari, one in Visakhapatnam.",
             te="పశ్చిమ గోదావరిలో 15, తూర్పు గోదావరిలో 9, విశాఖలో 1.",
             hi="पश्चिम गोदावरी में 15, पूर्वी गोदावरी में 9, विशाखा में 1."),
    "Schematic — dots mark towns, not boundaries.":
        dict(en="Schematic — dots mark towns, not boundaries.",
             te="పటం సూచనమాత్రం — చుక్కలు ఊళ్లు.",
             hi="नक्शा सांकेतिक — बिंदु शहर हैं."),
    "a showroom": dict(en="a showroom", te="ఒక షాపు", hi="एक दुकान"),
    # gaps _tools/missing07.py found: text the pages show that the table had no
    # entry for, so it would have stayed English in Telugu and Hindi
    "Browse the catalogue": dict(en="Browse the catalogue", te="జాబితా చూడండి", hi="सूची देखें"),
    "25 showrooms": dict(en="25 showrooms", te="25 షాపులు", hi="25 दुकानें"),
    "23 towns": dict(en="23 towns", te="23 ఊళ్లు", hi="23 शहर"),
    "Nothing matches that": dict(en="Nothing matches that", te="అలా ఏదీ దొరకలేదు", hi="ऐसा कुछ नहीं मिला"),
    "All 25 showrooms": dict(en="All 25 showrooms", te="25 షాపులూ", hi="सभी 25 दुकानें"),
    "Open 10 am to 9 pm": dict(en="Open 10 am to 9 pm", te="ఉదయం 10 నుంచి రాత్రి 9 వరకు", hi="सुबह 10 से रात 9 तक"),
    "the flagship": dict(en="the flagship", te="ప్రధాన షాపు", hi="मुख्य दुकान"),
    "20 brands": dict(en="20 brands", te="20 బ్రాండ్లు", hi="20 ब्रांड"),
    "open 10 to 9": dict(en="open 10 to 9", te="10 నుంచి 9 వరకు తెరిచి", hi="10 से 9 तक खुला"),
    "delivery and installation": dict(en="delivery and installation", te="డెలివరీ, ఇన్‌స్టాలేషన్", hi="डिलीवरी और इंस्टॉलेशन"),
    "All 17 items": dict(en="All 17 items", te="17 వస్తువులూ", hi="सभी 17 सामान"),
    "see list": dict(en="see list", te="జాబితా", hi="सूची"),
    "Add what you like": dict(en="Add what you like", te="నచ్చినవి జోడించండి", hi="पसंद का जोड़ें"),
    "Build a list while you browse. Nothing is charged and no account is needed.":
        dict(en="Build a list while you browse. Nothing is charged and no account is needed.",
             te="చూస్తూనే జాబితా చేసుకోండి. డబ్బు ఏమీ కట్టాల్సిన అవసరం లేదు, అకౌంట్ లేదు.",
             hi="देखते-देखते सूची बनाइए. कोई भुगतान नहीं, कोई खाता नहीं."),
    "Send it to us": dict(en="Send it to us", te="మాకు పంపండి", hi="हमें भेजिए"),
    "One tap opens WhatsApp with your whole list written out, or dials the helpline.":
        dict(en="One tap opens WhatsApp with your whole list written out, or dials the helpline.",
             te="ఒక్క నొక్కు — జాబితా మొత్తం WhatsApp లో సిద్ధంగా ఉంటుంది, లేదా హెల్ప్‌లైన్‌కు కాల్ అవుతుంది.",
             hi="एक टैप से पूरी सूची WhatsApp पर तैयार, या हेल्पलाइन पर कॉल."),
    "We call with the price": dict(en="We call with the price", te="ధర చెప్పి ఫోన్ చేస్తాం", hi="दाम बताकर फ़ोन करेंगे"),
    "Today's price, which branch has it, EMI if you want it, and a delivery date.":
        dict(en="Today's price, which branch has it, EMI if you want it, and a delivery date.",
             te="ఈరోజు ధర, ఏ షాపులో ఉంది, కావాలంటే EMI, డెలివరీ తేదీ.",
             hi="आज का दाम, किस दुकान में है, चाहें तो EMI, और डिलीवरी की तारीख़."),
    "How buying works here": dict(en="How buying works here", te="ఇక్కడ కొనడం ఎలా", hi="यहाँ खरीदना कैसे होता है"),
    "Popular this week": dict(en="Popular this week", te="ఈ వారం జనం అడిగేవి", hi="इस हफ़्ते लोकप्रिय"),
    "See the list": dict(en="See the list", te="జాబితా చూడు", hi="सूची देखें"),
    "What you get in writing": dict(en="What you get in writing", te="రాతిపై ఏం ఉంటుంది", hi="लिखित में क्या मिलेगा"),
    "Service, honestly": dict(en="Service, honestly", te="సర్వీస్ — నిజం", hi="सर्विस — सच में"),
    "Brand warranty runs through each manufacturer's authorised network and we coordinate it for you.":
        dict(en="Brand warranty runs through each manufacturer's authorised network and we coordinate it for you.",
             te="వారంటీ కంపెనీ అధికారిక సర్వీస్ నెట్‌వర్క్‌ ద్వారానే. మేం సమన్వయం చేస్తాం.",
             hi="वारंटी कंपनी के अधिकृत नेटवर्क से ही चलती है. समन्वय हम करते हैं."),
    "Prices are not invented on this page. Ask for today's and you get the number we can actually sell at.":
        dict(en="Prices are not invented on this page. Ask for today's and you get the number we can actually sell at.",
             te="ఈ పేజీలో ధరలు ఊహించి రాయలేదు. ఈరోజు ధర అడిగితే, నిజంగా అమ్మగలిగే ధర చెప్తాం.",
             hi="इस पन्ने पर दाम बनावटी नहीं. आज का पूछें, जिस दाम पर बेच सकते हैं वही मिलेगा."),
    "About this build:": dict(en="About this build:", te="ఈ నమూనా గురించి:", hi="इस डिज़ाइन के बारे में:"),
    "a design concept for whynotindia.in, made as portfolio work. It is not affiliated with WHYNOT Electronics and is not deployed anywhere. The artwork is AI-generated stand-in art, and the enquiry form does not send anything — there is no server behind it.":
        dict(en="a design concept for whynotindia.in, made as portfolio work. It is not affiliated with WHYNOT Electronics and is not deployed anywhere. The artwork is AI-generated stand-in art, and the enquiry form does not send anything — there is no server behind it.",
             te="whynotindia.in కోసం చేసిన డిజైన్ నమూనా. WHYNOT కంపెనీకి సంబంధం లేదు, ఎక్కడా లైవ్‌లో లేదు. బొమ్మలు AI తో చేసినవి, ఫారం ఎక్కడికీ పంపదు.",
             hi="whynotindia.in के लिए बनाया डिज़ाइन नमूना. WHYNOT कंपनी से संबंध नहीं, कहीं लाइव नहीं. तस्वीरें AI से, फ़ॉर्म कहीं कुछ नहीं भेजता."),

    # ------------------------------------------------------------- catalogue
    "Catalogue · 17 items · 10 categories": dict(en="Catalogue · 17 items · 10 categories", te="జాబితా · 17 వస్తువులు · 10 విభాగాలు", hi="सूची · 17 सामान · 10 श्रेणियाँ"),
    "The catalogue, as a list.": dict(en="The catalogue, as a list.", te="జాబితా — వరుసలో.", hi="सूची — एक-एक पंक्ति में."),
    "Seventeen things people actually ask for, in the categories the showrooms stock. Add what you want to <strong>my list</strong>, send it in one tap, and a person from your nearest branch replies with today's price and stock. No card details, no account, nothing charged.":
        dict(html=True,
             en="Seventeen things people actually ask for, in the categories the showrooms stock. Add what you want to <strong>my list</strong>, send it in one tap, and a person from your nearest branch replies with today's price and stock. No card details, no account, nothing charged.",
             te="జనం అడిగే 17 వస్తువులు, షాపుల్లో ఉన్న విభాగాల్లోనే. నచ్చినవి <strong>నా జాబితా</strong>లో పెట్టి ఒక్క నొక్కుతో పంపండి — దగ్గరి షాపు నుంచి ఈరోజు ధర, స్టాక్ చెప్పడానికి ఫోన్ వస్తుంది. కార్డు వివరాలు, అకౌంట్, డబ్బు — ఏదీ అవసరం లేదు.",
             hi="लोग जो माँगते हैं वही 17 सामान, दुकानों वाली श्रेणियों में. पसंद का सामान <strong>मेरी सूची</strong> में डालकर एक टैप में भेजें — नज़दीकी दुकान से आज का दाम और स्टॉक बताने फ़ोन आएगा. कार्ड, खाता, भुगतान — कुछ नहीं चाहिए."),
    "Search the catalogue": dict(en="Search the catalogue", te="జాబితాలో వెతకండి", hi="सूची में खोजें"),
    "Town": dict(en="Town", te="ఊరు", hi="शहर"),
    "17 products": dict(en="17 products", te="17 వస్తువులు", hi="17 सामान"),
    "Line list": dict(en="Line list", te="వరుస జాబితా", hi="पंक्ति सूची"),
    "price on request": dict(en="price on request", te="ధర అడిగితే", hi="दाम पूछने पर"),
    "Item": dict(en="Item", te="వస్తువు", hi="सामान"),
    "Category": dict(en="Category", te="విభాగం", hi="श्रेणी"),
    "Specification": dict(en="Specification", te="వివరాలు", hi="विवरण"),
    "Available at": dict(en="Available at", te="ఎక్కడ ఉంది", hi="कहाँ उपलब्ध"),
    "List": dict(en="List", te="జాబితా", hi="सूची"),
    "My list": dict(en="My list", te="నా జాబితా", hi="मेरी सूची"),
    "Close": dict(en="Close", te="మూసివేయి", hi="बंद करें"),
    "This is a concept build with no server attached. Sending the list opens WhatsApp or your mail app with the items written out — nothing is submitted from this page.":
        dict(en="This is a concept build with no server attached. Sending the list opens WhatsApp or your mail app with the items written out — nothing is submitted from this page.",
             te="ఇది నమూనా మాత్రమే, వెనుక సర్వర్ లేదు. జాబితా పంపితే WhatsApp లేదా మెయిల్ యాప్ తెరుచుకుంటుంది — ఈ పేజీ నుంచి ఏదీ సబ్మిట్ అవ్వదు.",
             hi="यह नमूना है, पीछे कोई सर्वर नहीं. सूची भेजने पर WhatsApp या मेल ऐप खुलता है — इस पन्ने से कुछ सबमिट नहीं होता."),

    # -------------------------------------------------------------- showrooms
    "Showrooms · 25 doors · 23 towns": dict(en="Showrooms · 25 doors · 23 towns", te="షాపులు · 25 తలుపులు · 23 ఊళ్లు", hi="दुकानें · 25 दरवाज़े · 23 शहर"),
    "Twenty-five doors.": dict(en="Twenty-five doors.", te="ఇరవై ఐదు తలుపులు.", hi="पच्चीस दरवाज़े."),
    "Every branch with its address, a map link and the phone number that reaches it. The flagship is in Tanuku; the rest are in the towns the company has traded in since 1994.":
        dict(en="Every branch with its address, a map link and the phone number that reaches it. The flagship is in Tanuku; the rest are in the towns the company has traded in since 1994.",
             te="ప్రతి షాపు చిరునామా, మ్యాప్ లింక్, ఫోన్ నంబర్‌తో. ప్రధాన షాపు తనుకులో; మిగతావి 1994 నుంచి కంపెనీ వ్యాపారం చేస్తున్న ఊళ్లలో.",
             hi="हर शाखा का पता, मैप लिंक और फ़ोन नंबर. मुख्य दुकान तनुकू में; बाकी उन शहरों में जहाँ 1994 से कारोबार है."),
    "Open now": dict(en="Open now", te="ఇప్పుడు తెరిచి ఉంది", hi="अभी खुला है"),
    "Closed now": dict(en="Closed now", te="ఇప్పుడు మూసి ఉంది", hi="अभी बंद है"),
    "Today · 10 am to 9 pm": dict(en="Today · 10 am to 9 pm", te="ఈరోజు · 10 నుంచి 9", hi="आज · 10 से 9"),
    "West Godavari": dict(en="West Godavari", te="పశ్చిమ గోదావరి", hi="पश्चिम गोदावरी"),
    "East Godavari": dict(en="East Godavari", te="తూర్పు గోదావరి", hi="पूर्वी गोदावरी"),
    "Visakhapatnam": dict(en="Visakhapatnam", te="విశాఖపట్నం", hi="विशाखापट्टनम"),
    "15 showrooms": dict(en="15 showrooms", te="15 షాపులు", hi="15 दुकानें"),
    "Anakapalle": dict(en="Anakapalle", te="అనకాపల్లి", hi="अनकापल्ली"),
    "Search the showrooms": dict(en="Search the showrooms", te="షాపుల్లో వెతకండి", hi="दुकानें खोजें"),
    "Clear": dict(en="Clear", te="తీసేయి", hi="हटाएँ"),
    "All 25": dict(en="All 25", te="అన్నీ 25", hi="सभी 25"),
    "Try a town, a road or a pincode — or call the helpline and ask.":
        dict(en="Try a town, a road or a pincode — or call the helpline and ask.",
             te="ఊరు, రోడ్డు లేదా పిన్ కోడ్ ప్రయత్నించండి — లేదా హెల్ప్‌లైన్‌కు కాల్ చేయండి.",
             hi="शहर, सड़क या पिन कोड डालें — या हेल्पलाइन पर फ़ोन करें."),
    "Open until 9 pm today.": dict(en="Open until 9 pm today.", te="ఈరోజు రాత్రి 9 వరకు తెరిచి ఉంది.", hi="आज रात 9 बजे तक खुला है."),

    # ------------------------------------------------------------ categories
    "Televisions": dict(en="Televisions", te="టెలివిజన్లు", hi="टेलीविज़न"),
    "Refrigerators": dict(en="Refrigerators", te="ఫ్రిజ్‌లు", hi="फ्रिज"),
    "Air conditioners": dict(en="Air conditioners", te="ఏసీలు", hi="एयर कंडीशनर"),
    "Washing machines": dict(en="Washing machines", te="వాషింగ్ మెషీన్లు", hi="वॉशिंग मशीन"),
    "Kitchen": dict(en="Kitchen", te="వంటగది", hi="रसोई"),
    "Water & geysers": dict(en="Water & geysers", te="నీళ్లు, గీజర్లు", hi="पानी और गीज़र"),
    "Lighting": dict(en="Lighting", te="లైటింగ్", hi="लाइटिंग"),
    "Audio": dict(en="Audio", te="ఆడియో", hi="ऑडियो"),
    "Mobiles": dict(en="Mobiles", te="మొబైల్స్", hi="मोबाइल"),
    "Cleaning": dict(en="Cleaning", te="క్లీనింగ్", hi="सफ़ाई"),
    "QLED · 4K · smart": dict(en="QLED · 4K · smart", te="QLED · 4K · స్మార్ట్", hi="QLED · 4K · स्मार्ट"),
    "Single & double door": dict(en="Single & double door", te="సింగిల్, డబుల్ డోర్", hi="सिंगल और डबल दरवाज़ा"),
    "Split · inverter": dict(en="Split · inverter", te="స్ప్లిట్ · ఇన్వర్టర్", hi="स्प्लिट · इनवर्टर"),
    "Semi & automatic": dict(en="Semi & automatic", te="సెమీ, ఆటోమేటిక్", hi="सेमी और ऑटोमैटिक"),
    "Mixers · grinders": dict(en="Mixers · grinders", te="మిక్సీలు · గ్రైండర్లు", hi="मिक्सर · ग्राइंडर"),
    "Purifiers · heaters": dict(en="Purifiers · heaters", te="ప్యూరిఫైయర్లు · హీటర్లు", hi="प्यूरिफ़ायर · हीटर"),
    "LED · strips": dict(en="LED · strips", te="LED · స్ట్రిప్‌లు", hi="LED · स्ट्रिप"),
    "Speakers · bars": dict(en="Speakers · bars", te="స్పీకర్లు · బార్లు", hi="स्पीकर · बार"),
    "5G · budget to flagship": dict(en="5G · budget to flagship", te="5G · బడ్జెట్ నుంచి టాప్ వరకు", hi="5G · बजट से टॉप तक"),
    "Vacuum · mops": dict(en="Vacuum · mops", te="వాక్యూమ్ · మాప్‌లు", hi="वैक्यूम · मॉप"),
    "Warranty & service": dict(en="Warranty & service", te="వారంటీ, సర్వీస్", hi="वारंटी और सर्विस"),
    "EMI & exchange": dict(en="EMI & exchange", te="EMI, పాత వస్తువు మార్పిడి", hi="EMI और एक्सचेंज"),
    "Delivery & installation": dict(en="Delivery & installation", te="డెలివరీ, ఇన్‌స్టాలేషన్", hi="डिलीवरी और इंस्टॉलेशन"),
    "Ask a human": dict(en="Ask a human", te="మనిషిని అడగండి", hi="इंसान से पूछें"),
    "Card and Bajaj-style EMI is available at the counter on most large appliances. Old product exchange value is quoted before you buy.":
        dict(en="Card and Bajaj-style EMI is available at the counter on most large appliances. Old product exchange value is quoted before you buy.",
             te="పెద్ద వస్తువులపై కార్డు, బజాజ్ EMI కౌంటర్‌లోనే. పాత వస్తువు మార్పిడి విలువ కొనే ముందే చెప్తాం.",
             hi="बड़े सामान पर कार्ड और बजाज EMI काउंटर पर ही. पुराने सामान का एक्सचेंज मूल्य खरीदने से पहले बता देते हैं."),
    "Fixed at the counter: what it costs, when it arrives, who installs it. No surprises on the bill.":
        dict(en="Fixed at the counter: what it costs, when it arrives, who installs it. No surprises on the bill.",
             te="కౌంటర్‌లోనే ఖరారు: ఎంత, ఎప్పుడు వస్తుంది, ఎవరు అమర్చుతారు. బిల్లులో ఆశ్చర్యాలు ఉండవు.",
             hi="काउंटर पर तय: कितना खर्च, कब आएगा, कौन लगाएगा. बिल में कोई झटका नहीं."),

    # ------------------------------------------------------- leftovers + form
    "items in my list": dict(en="items in my list", te="వస్తువులు జాబితాలో", hi="सामान सूची में"),
    "Search: TV, fridge, 1.5 ton": dict(en="Search: TV, fridge, 1.5 ton", te="వెతకండి: టీవీ, ఫ్రిజ్, 1.5 టన్", hi="खोजें: टीवी, फ्रिज, 1.5 टन"),
    "Search: TV, fridge, 1.5 ton, mixer": dict(en="Search: TV, fridge, 1.5 ton, mixer", te="వెతకండి: టీవీ, ఫ్రిజ్, 1.5 టన్, మిక్సీ", hi="खोजें: टीवी, फ्रिज, 1.5 टन, मिक्सर"),
    "Search town, road or pincode": dict(en="Search town, road or pincode", te="ఊరు, రోడ్డు, పిన్ కోడ్ వెతకండి", hi="शहर, सड़क या पिन कोड खोजें"),
    "Model, size, room — anything that helps us price it":
        dict(en="Model, size, room — anything that helps us price it",
             te="మోడల్, సైజు, గది — ధర చెప్పడానికి సహాయపడే ఏదైనా",
             hi="मॉडल, साइज़, कमरा — दाम बताने में मदद करने वाली कोई भी बात"),
    "This concept build has no server: nothing is submitted. In a live build this would reach the branch you pick.":
        dict(en="This concept build has no server: nothing is submitted. In a live build this would reach the branch you pick.",
             te="ఇది నమూనా, సర్వర్ లేదు: ఏదీ సబ్మిట్ అవ్వదు. నిజంగా ఉంటే మీరు ఎంచుకున్న షాపుకు చేరేది.",
             hi="यह नमूना है, सर्वर नहीं: कुछ सबमिट नहीं होता. असली बिल्ड में यह आपकी चुनी दुकान तक पहुँचता."),
    "Today's price, stock, EMI and exchange if you want it.":
        dict(en="Today's price, stock, EMI and exchange if you want it.",
             te="ఈరోజు ధర, స్టాక్, కావాలంటే EMI, మార్పిడి.",
             hi="आज का दाम, स्टॉक, चाहें तो EMI और एक्सचेंज."),
    "Brand warranty runs through each manufacturer's authorised service network, and WHYNOT coordinates it for you.":
        dict(en="Brand warranty runs through each manufacturer's authorised service network, and WHYNOT coordinates it for you.",
             te="వారంటీ కంపెనీ అధికారిక సర్వీస్ నెట్‌వర్క్ ద్వారానే నడుస్తుంది. సమన్వయం WHYNOT చేస్తుంది.",
             hi="वारंटी हर कंपनी के अधिकृत सर्विस नेटवर्क से चलती है. समन्वय WHYNOT करता है."),
    "Brand warranty runs through each manufacturer's authorised network and we coordinate it for you. Installation and delivery are fixed at the counter — the price you agree is the price on the bill.":
        dict(en="Brand warranty runs through each manufacturer's authorised network and we coordinate it for you. Installation and delivery are fixed at the counter — the price you agree is the price on the bill.",
             te="వారంటీ కంపెనీ అధికారిక నెట్‌వర్క్ ద్వారానే; సమన్వయం మేం చేస్తాం. ఇన్‌స్టాలేషన్, డెలివరీ కౌంటర్‌లోనే ఖరారు — ఒప్పుకున్న ధరే బిల్లులో ఉంటుంది.",
             hi="वारंटी कंपनी के अधिकृत नेटवर्क से, समन्वय हम करते हैं. इंस्टॉलेशन और डिलीवरी काउंटर पर तय — जो दाम तय हुआ वही बिल में."),
    "Unsure between two models? Call the helpline and describe the room. We do this all day.":
        dict(en="Unsure between two models? Call the helpline and describe the room. We do this all day.",
             te="రెండు మోడళ్ల మధ్య సందిగ్ధమా? హెల్ప్‌లైన్‌కు కాల్ చేసి గది వివరాలు చెప్పండి. ఇదే మా పని.",
             hi="दो मॉडल में उलझन? हेल्पलाइन पर फ़ोन करके कमरे के बारे में बताइए. यही हमारा रोज़ का काम है."),
}

# Strings the scripts build at runtime that Trial 07 needs and the other trials
# never used.
JS = {
    "All": ("all", dict(en="All", te="అన్నీ", hi="सभी")),
    "Call": ("callShort", dict(en="Call", te="కాల్", hi="कॉल")),
    "categories": ("categories", dict(en="categories", te="విభాగాలు", hi="श्रेणियाँ")),
    "products": ("products", dict(en="products", te="వస్తువులు", hi="सामान")),
    "showrooms": ("showrooms", dict(en="showrooms", te="షాపులు", hi="दुकानें")),
    "23 towns": ("twentyThreeTowns", dict(en="23 towns", te="23 ఊళ్లు", hi="23 शहर")),
    "1 helpline": ("oneHelpline", dict(en="1 helpline", te="ఒకే హెల్ప్‌లైన్", hi="एक हेल्पलाइन")),
    "ask for today's price": ("askPrice", dict(en="ask for today's price", te="ఈరోజు ధర అడగండి", hi="आज का दाम पूछें")),
    "we will price it and call you": ("weWillPrice", dict(en="we will price it and call you", te="ధర చెప్పి ఫోన్ చేస్తాం", hi="दाम बताकर फ़ोन करेंगे")),
    "Try a shorter word, or clear the filters.": ("noMatchHelp", dict(en="Try a shorter word, or clear the filters.", te="చిన్న మాటతో ప్రయత్నించండి, లేదా ఫిల్టర్లు తీసేయండి.", hi="छोटा शब्द डालें, या फ़िल्टर हटाएँ.")),
    "Add anything you want priced. It stays on this device until you send it.":
        ("emptyHelp", dict(en="Add anything you want priced. It stays on this device until you send it.",
                           te="ధర కావాల్సినవి జోడించండి. పంపే వరకు ఇదే ఫోన్‌లో ఉంటుంది.",
                           hi="जिसका दाम चाहिए वह जोड़ें. भेजने तक यहीं इस फ़ोन में रहता है.")),
    "No card details, no account, nothing charged. A person from your nearest branch replies with today's price.":
        ("conceptNote2", dict(en="No card details, no account, nothing charged. A person from your nearest branch replies with today's price.",
                              te="కార్డు వివరాలు, అకౌంట్, డబ్బు — ఏదీ అవసరం లేదు. దగ్గరి షాపు నుంచి ఈరోజు ధరతో ఫోన్ వస్తుంది.",
                              hi="कार्ड, खाता, भुगतान — कुछ नहीं. नज़दीकी दुकान से आज के दाम के साथ फ़ोन आएगा.")),
    "Copied": ("copied", dict(en="Copied", te="కాపీ అయింది", hi="कॉपी हो गया")),
    "Open now": ("openNow", dict(en="Open now", te="ఇప్పుడు తెరిచి ఉంది", hi="अभी खुला है")),
    "Closed now": ("closedNow", dict(en="Closed now", te="ఇప్పుడు మూసి ఉంది", hi="अभी बंद है")),
    "Open until 9 pm today — walk in and ask for a demo.":
        ("openNote", dict(en="Open until 9 pm today — walk in and ask for a demo.",
                          te="ఈరోజు రాత్రి 9 వరకు తెరిచి ఉంది — వచ్చి చూడండి.",
                          hi="आज रात 9 तक खुला है — आकर देख लीजिए.")),
    "We open at 10 am. Leave your number and we'll ring you back.":
        ("closedNote", dict(en="We open at 10 am. Leave your number and we'll ring you back.",
                            te="ఉదయం 10కి తెరుస్తాం. నంబర్ ఇవ్వండి, మేం కాల్ చేస్తాం.",
                            hi="सुबह 10 बजे खोलेंगे. नंबर छोड़ जाइए, हम फ़ोन करेंगे.")),
}

# Phrases the page builds that carry a number.
PATTERNS = [
    dict(re=r"^([0-9]+) products$", en="$1 products", te="$1 వస్తువులు", hi="$1 सामान"),
    dict(re=r"^([0-9]+) items?$", en="$1 items", te="$1 వస్తువులు", hi="$1 सामान"),
    dict(re=r"^([0-9]+) showrooms$", en="$1 showrooms", te="$1 షాపులు", hi="$1 दुकानें"),
    dict(re=r"^([0-9]+) towns$", en="$1 towns", te="$1 ఊళ్లు", hi="$1 शहर"),
    dict(re=r"^(Showing) ([0-9]+) of ([0-9]+)$", en="Showing $2 of $3", te="చూపిస్తున్నాం: $2 / $3", hi="दिखा रहे हैं: $2 / $3"),
]
