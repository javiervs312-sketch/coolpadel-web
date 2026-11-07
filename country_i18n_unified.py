# -*- coding: utf-8 -*-
"""
Full native dictionary with all sections unified:
- Nav header
- Hero (H1 in 3 lines)
- Why choose Save My Play (exact 3 reasons)
- Pricing table (3 rows matching the requested pricing model: 180 HW, 45 Recording, 136 AI)
- Real Court Demonstration (4 videos with responsive grid)
- Collapsible FAQs (<details><summary>)
- Direct Contact Cards (WhatsApp with QR + Email with QR)
- Full Textured-Blue Footer with 4 SEO silos and legal links
"""

ALL_LANGS_UNIFIED = {
    "es": {
        "nav_home": "Inicio", "nav_camaras": "Cámaras", "nav_llaveros": "Llaveros", "nav_calc": "Calculadoras", "nav_blog": "Blog",
        "title": "Cámaras para Pistas de Pádel en {country}: Grabación, Highlights y Estadísticas con IA",
        "meta_desc": "Cámaras para pistas de pádel en {country}: {hw} hardware en propiedad, grabación automática por {rec} y estadísticas con IA por {ai}. Solicita demo en directo.",
        "badge": "CÁMARA OFICIAL USA PADEL Y USTA • +1500 PISTAS",
        "h1": "Cámaras para Pistas de Pádel:<br class=\"hidden sm:inline\"> Grabación Partidos, Highlights<br class=\"hidden sm:inline\"> y Estadísticas con IA",
        "sub": "La cámara oficial de USA Padel y USTA, ya en más de 1.500 pistas. Inversión de {hw} en propiedad, planes desde {rec}, montaje en 5 minutos sin obras y sin permanencias.",
        "p1_label": "Hardware Pista", "p1_val": "{hw} en propiedad",
        "p2_label": "Cuota Software", "p2_val": "{rec} (Grabación) • {ai} (Estadísticas con IA)",
        "p3_label": "Permanencia", "p3_val": "0 meses (Cancelación libre)",
        "p4_label": "Instalación", "p4_val": "5 minutos sin obras",
        "quick_p": "Save My Play es el sistema oficial de grabación de partidos y estadísticas con IA para pistas de pádel y tenis. Calidad deportiva profesional, instalación en 5 minutos y cancelación libre mes a mes.",
        "why_title": "¿Por qué elegir Save My Play para tu club?",
        "why_sub": "La tecnología de grabación y analítica en pista más ágil, sin obras ni costes ocultos",
        "f1_title": "No son cámaras de vigilancia: máxima calidad de imagen",
        "f1_desc": "Diseñadas exclusivamente para pádel y tenis. Grabación nítida deportiva, gran angular sin deformar la pista y retransmisión directa sin cortes.",
        "f2_title": "Planes mensuales por pista",
        "f2_desc": "Grabación de partidos, highlights y directos por {rec}. Estadísticas con IA por {ai} que incluyen análisis completo de tu juego.",
        "f3_title": "Fácil de usar y sin obras",
        "f3_desc": "Inversión hardware de {hw} en propiedad. Se instala en 5 minutos en el poste de la red o iluminación, y sin permanencias.",
        "demo_btn": "Solicitar Demo 15 min por WhatsApp",
        "rates_btn": "Ver Tarifas",
        
        # Pricing
        "pricing_th_plan": "Concepto / Plan", "pricing_th_invest": "Inversión / Cuota", "pricing_th_mod": "Modalidad", "pricing_th_serv": "Servicios Incluidos",
        "tbl_hw_title": "Inversión Hardware en Propiedad", "tbl_hw_mod": "Pago único (+20€ envío int.)", "tbl_hw_desc": "1 cámara deportiva rectilínea por pista (sin efecto pez) + fijación de seguridad a poste",
        "tbl_rec_title": "Grabación, Highlights & Streaming", "tbl_rec_mod": "0 permanencia • Cancelación libre", "tbl_rec_desc": "Grabación de partidos en nube privada, generación de mejores jugadas y retransmisión oficial en YouTube",
        "tbl_ai_title": "Estadísticas con IA y Análisis Táctico", "tbl_ai_mod": "0 permanencia • Opcional", "tbl_ai_desc": "Análisis de golpes, mapas de calor, velocidad de bola y estadísticas individuales por jugador",
        "pricing_footnote": "* Precios sin IVA. Sin permanencia ni penalizaciones. Instalación en 5 min.",

        # Videos
        "vid_badge": "Demostración en Pista Real",
        "vid_title": "Comprueba la Calidad de Grabación y Streaming",
        "vid_sub": "Partidos oficiales FIP en directo, repeticiones automáticas y herramientas de análisis táctico.",
        "vid1_t": "FIP Miami Padel Open", "vid1_d": "Streaming oficial en directo y multipantalla",
        "vid2_t": "Repetición Automática", "vid2_d": "Grabación automática y descarga directa de highlights por código QR sin apps",
        "vid3_t": "Análisis Táctico", "vid3_d": "Herramientas para entrenadores y academias",
        "vid4_t": "Torneo de Club", "vid4_d": "Retransmisión multicámara en YouTube",

        # FAQs
        "faq_title": "Preguntas Frecuentes",
        "faq_sub": "Resolvemos todas tus dudas sobre el sistema de grabación Save My Play sin obras",
        "faq1_q": "¿Se necesitan obras o canalizaciones en el suelo?",
        "faq1_a": "No, cero obras. El sistema se ancla directamente al poste de la pista y la instalación dura solo 5 minutos por pista.",
        "faq2_q": "¿Cuál es el precio y qué planes hay?",
        "faq2_a": "{hw} por cámara en propiedad. Planes mensuales: {rec} por pista para grabación, highlights y directos; o planes de estadísticas con IA por {ai} con análisis completo de juego.",
        "faq3_q": "¿Cómo procesa la IA los mejores puntos?",
        "faq3_a": "Las cámaras utilizan IA para procesar la señal de vídeo en tiempo real, elegir los mejores puntos y generar vídeos listos para compartir al móvil al instante.",
        "faq4_q": "¿Hay permanencia en el servicio?",
        "faq4_a": "Ninguna permanencia. Cancelación libre mes a mes sin penalizaciones.",

        # Contact
        "contact_badge": "Contacto Directo", "contact_title": "Contáctanos", "contact_sub": "Respuesta directa para consultas de clubes, torneos y demostraciones.",
        "contact_wa_btn": "Enviar WhatsApp", "contact_mail_btn": "Enviar Correo",

        # Footer
        "footer_b2b": "Soluciones B2B", "footer_tech": "Tecnología en Pista", "footer_tools": "Herramientas Gratuitas", "footer_corp": "Corporativo y Legal",
        "wa_msg": "Hola Javier, me interesa ver una demo de Save My Play para pistas de pádel en {country}"
    },

    "nl": {
        "nav_home": "Home", "nav_camaras": "Camera's", "nav_llaveros": "Sleutelhangers", "nav_calc": "Calculators", "nav_blog": "Blog",
        "title": "Padelcamera's in {country}: Wedstrijdopname, Highlights en AI-Statistieken",
        "meta_desc": "Padelcamera's in {country}: {hw} hardware in eigendom, automatische opname vanaf {rec} en AI-statistieken voor {ai}. Vraag een live demo aan.",
        "badge": "OFFICIËLE CAMERA VAN USA PADEL & USTA • +1500 BANEN",
        "h1": "Padelcamera's voor Banen:<br class=\"hidden sm:inline\"> Wedstrijdopname, Highlights<br class=\"hidden sm:inline\"> en AI-Statistieken",
        "sub": "De officiële camera van USA Padel en USTA, reeds op meer dan 1.500 banen. {hw} investering in eigen hardware, maandplannen vanaf {rec}, installatie in 5 minuten zonder bouwwerkzaamheden en zonder contractbinding.",
        "p1_label": "Hardware per baan", "p1_val": "{hw} in eigendom (eenmalig)",
        "p2_label": "Software-tarief", "p2_val": "{rec} (Opname) • {ai} (AI-statistieken)",
        "p3_label": "Contractbinding", "p3_val": "0 maanden (Maandelijks opzegbaar)",
        "p4_label": "Installatie", "p4_val": "5 minuten zonder bouwwerk",
        "quick_p": "Save My Play is het officiële videosysteem voor wedstrijdopname en AI-analyse op padel- en tennisbanen. Haarscherpe sportbeeldkwaliteit, montage in 5 minuten en maandelijks vrij opzegbaar.",
        "why_title": "Waarom kiezen voor Save My Play in jouw club?",
        "why_sub": "De slimste en snelste video- en analysetechnologie voor padelbanen, zonder graafwerk of verborgen kosten",
        "f1_title": "Geen beveiligingscamera's: echte sportoptiek",
        "f1_desc": "Exclusief ontworpen voor padel en tennis. Heldere sportopnamen, groothoeklens zonder vervorming van de baan en storingsvrije livestreaming.",
        "f2_title": "Duidelijke maandelijkse tarieven per baan",
        "f2_desc": "Wedstrijdopname, highlights en livestreams voor {rec}. AI-statistieken voor {ai} inclusief complete analyse van je spel.",
        "f3_title": "Eenvoudig in gebruik en zonder verbouwing",
        "f3_desc": "{hw} eigen hardware. Binnen 5 minuten gemonteerd op de netpaal of lichtmast, volledig zonder verplichtingen.",
        "demo_btn": "Vraag 15 min demo aan via WhatsApp",
        "rates_btn": "Bekijk tarieven",
        
        # Pricing
        "pricing_th_plan": "Pakket / Specificatie", "pricing_th_invest": "Investering / Tarief", "pricing_th_mod": "Vorm", "pricing_th_serv": "Inbegrepen diensten",
        "tbl_hw_title": "Hardware-investering in Eigendom", "tbl_hw_mod": "Eenmalige aankoop", "tbl_hw_desc": "1 sportcamera per baan (rechte lens zonder fisheye) + veilige paalbevestiging",
        "tbl_rec_title": "Opname, Highlights & Streaming", "tbl_rec_mod": "0 contractbinding • Maandelijks opzegbaar", "tbl_rec_desc": "Opname in privé-cloud, automatische actieclips en livestreaming op YouTube",
        "tbl_ai_title": "AI-Statistieken en Tactische Analyse", "tbl_ai_mod": "0 contractbinding • Optioneel", "tbl_ai_desc": "Slaganalyse, heatmaps, balsnelheidsmeting en individuele spelersstatistieken",
        "pricing_footnote": "* Prijzen excl. btw. Geen langetermijncontracten. Montage in 5 minuten.",

        # Videos
        "vid_badge": "Demonstratie op de Baan",
        "vid_title": "Ervaar de Opname- en Streamingkwaliteit",
        "vid_sub": "Officiële FIP-wedstrijden live, automatische highlight-clips en tactische analysetools.",
        "vid1_t": "FIP Miami Padel Open", "vid1_d": "Officiële livestream en multi-court weergave",
        "vid2_t": "Automatische Highlights", "vid2_d": "Directe QR-download op de mobiel zonder apps te installeren",
        "vid3_t": "Tactische Coaching", "vid3_d": "Videotools voor trainers en academies",
        "vid4_t": "Clubtoernooi", "vid4_d": "Live uitzending op YouTube met clublogo",

        # FAQs
        "faq_title": "Veelgestelde Vragen",
        "faq_sub": "Alles wat je moet weten over het Save My Play camerasysteem voor padelclubs",
        "faq1_q": "Zijn er graafwerkzaamheden of grondkabels nodig?",
        "faq1_a": "Nee, nul bouwwerkzaamheden. De camera wordt binnen 5 minuten rechtstreeks aan de netpaal bevestigd.",
        "faq2_q": "Wat zijn de kosten en welke pakketten zijn er?",
        "faq2_a": "{hw} per camera in eigen bezit. Maandelijkse plannen: {rec} per baan voor opname, highlights en streaming; of {ai} voor AI-statistieken met tactische analyse.",
        "faq3_q": "Hoe selecteert de AI de beste punten?",
        "faq3_a": "De camera's analyseren het videosignaal in realtime met kunstmatige intelligentie, knippen de beste rally's direct uit en maken ze deelbaar.",
        "faq4_q": "Zit ik vast aan een lang contract?",
        "faq4_a": "Geen enkel lang contract. Maandelijks flexibel opzegbaar.",

        # Contact
        "contact_badge": "Direct Contact", "contact_title": "Neem Contact Op", "contact_sub": "Direct antwoord voor clubs, toernooiorganisatoren en live demo's.",
        "contact_wa_btn": "Stuur WhatsApp", "contact_mail_btn": "Stuur E-mail",

        # Footer
        "footer_b2b": "B2B Oplossingen", "footer_tech": "Baantechnologie", "footer_tools": "Gratis Tools", "footer_corp": "Bedrijf & Juridisch",
        "wa_msg": "Hallo Javier, ik wil graag een demo zien van Save My Play voor padelbanen in {country}"
    },

    "sv": {
        "nav_home": "Hem", "nav_camaras": "Kameror", "nav_llaveros": "Nyckelringar", "nav_calc": "Kalkylatorer", "nav_blog": "Blogg",
        "title": "Padelkameror i {country}: Matchinspelning, Höjdpunkter och AI-Statistik",
        "meta_desc": "Padelkameror i {country}: {hw} hårdvara i ägo, automatisk inspelning från {rec} och AI-statistik för {ai}. Boka en direktdemo.",
        "badge": "OFFICIELL KAMERA FÖR USA PADEL OCH USTA • +1500 BANOR",
        "h1": "Padelkameror för Banor:<br class=\"hidden sm:inline\"> Matchinspelning, Höjdpunkter<br class=\"hidden sm:inline\"> och AI-Statistik",
        "sub": "Den officiella kameran för USA Padel och USTA, redan på fler än 1 500 banor. Investering på {hw} i hårdvara i ägo, månadsplaner från {rec}, montering på 5 minuter utan byggarbete och utan bindningstid.",
        "p1_label": "Hårdvara per bana", "p1_val": "{hw} (engångsköp i ägo)",
        "p2_label": "Månadsavgift", "p2_val": "{rec} (Inspelning) • {ai} (AI-statistik)",
        "p3_label": "Bindningstid", "p3_val": "0 månader (Fri uppsägning)",
        "p4_label": "Installation", "p4_val": "5 minuter utan byggarbete",
        "quick_p": "Save My Play är det officiella kamerasystemet för matchinspelning och AI-statistik på padel- och tennisbanor. Professionell sportbildkvalitet, 5 minuters montering och fri uppsägning månad för månad.",
        "why_title": "Varför välja Save My Play till din klubb?",
        "why_sub": "Den smidigaste inspelnings- och analystekniken för padelbanor, utan byggnation eller dolda avgifter",
        "f1_title": "Inga övervakningskameror: maximal sportbildkvalitet",
        "f1_desc": "Utvecklade uteslutande för padel och tennis. Knivskarp sportinspelning, vidvinkel utan förvrängning och livestreaming utan avbrott.",
        "f2_title": "Tydliga månadsplaner per bana",
        "f2_desc": "Matchinspelning, höjdpunkter och livestreaming för {rec}. AI-statistik för {ai} som inkluderar fullständig analys av ditt spel.",
        "f3_title": "Enkel att använda och utan byggarbete",
        "f3_desc": "Hårdvaruinvestering på {hw} i egen ägo. Installeras på 5 minuter på nätstolpen eller belysningen, helt utan bindningstid.",
        "demo_btn": "Boka 15 min demo via WhatsApp",
        "rates_btn": "Se priser",
        
        # Pricing
        "pricing_th_plan": "Plan / Koncept", "pricing_th_invest": "Investering / Avgift", "pricing_th_mod": "Avtalsform", "pricing_th_serv": "Ingående tjänster",
        "tbl_hw_title": "Hårdvaruinvestering i Ägo", "tbl_hw_mod": "Engångsbetalning", "tbl_hw_desc": "1 sportkamera per bana (rak lins utan fisheye) + säkerhetsfäste för stolpe",
        "tbl_rec_title": "Inspelning, Höjdpunkter & Streaming", "tbl_rec_mod": "0 bindningstid • Månad för månad", "tbl_rec_desc": "Inspelning i privat moln, automatiska höjdpunkter och direktsändning på YouTube med klubbens logotyp",
        "tbl_ai_title": "AI-Statistik och Taktisk Spelaranalys", "tbl_ai_mod": "0 bindningstid • Valfri", "tbl_ai_desc": "Slaganalys, värmekartor, bollhastighet och individuell statistik per spelare",
        "pricing_footnote": "* Priser exkl. moms. Ingen bindningstid. 5 minuters installation.",

        # Videos
        "vid_badge": "Demonstration på Riktig Bana",
        "vid_title": "Upplev Inspelnings- och Streamingkvaliteten",
        "vid_sub": "Officiella FIP-matcher live, automatiska höjdpunkter och taktiska analysverktyg.",
        "vid1_t": "FIP Miami Padel Open", "vid1_d": "Officiell livestreaming och flerkameravy",
        "vid2_t": "Automatisk Höjdpunktsvideo", "vid2_d": "Direkt QR-skanning till mobilen utan appnedladdning",
        "vid3_t": "Taktisk Tränaranalys", "vid3_d": "Verktyg för tränare och akademi",
        "vid4_t": "Klubbturnering", "vid4_d": "Livestream på YouTube med klubbens varumärke",

        # FAQs
        "faq_title": "Vanliga Frågor",
        "faq_sub": "Allt du behöver veta om Save My Play kamerasystem för padelklubbar",
        "faq1_q": "Krävs det markarbeten eller kabeldragning i marken?",
        "faq1_a": "Nej, noll byggarbete. Systemet fästs direkt på banans nätstolpe på 5 minuter.",
        "faq2_q": "Vad kostar det och vilka abonnemang finns?",
        "faq2_a": "{hw} per kamera i egen ägo. Månadsplaner: {rec} per bana för inspelning, höjdpunkter och livestreaming; eller {ai} för AI-statistik med taktisk analys.",
        "faq3_q": "Hur väljer AI ut de bästa bollarna?",
        "faq3_a": "Kamerorna analyserar videosignalen i realtid med AI, klipper ut de bästa poängen och genererar delningsklara klipp.",
        "faq4_q": "Finns det någon bindningstid?",
        "faq4_a": "Ingen bindningstid alls. Fri uppsägning månad för månad.",

        # Contact
        "contact_badge": "Direktkontakt", "contact_title": "Kontakta Oss", "contact_sub": "Snabbt svar för klubbar, turneringar och livedemo.",
        "contact_wa_btn": "Skicka WhatsApp", "contact_mail_btn": "Skicka E-post",

        # Footer
        "footer_b2b": "B2B Lösningar", "footer_tech": "Banteknologi", "footer_tools": "Gratis Verktyg", "footer_corp": "Företag & Juridik",
        "wa_msg": "Hej Javier! Jag är intresserad av en demo av Save My Play för padelbanor i {country}"
    },

    "en": {
        "nav_home": "Home", "nav_camaras": "Cameras", "nav_llaveros": "Keychains", "nav_calc": "Calculators", "nav_blog": "Blog",
        "title": "Padel Court Cameras in {country}: Match Recording, Highlights & AI Stats",
        "meta_desc": "Padel court cameras in {country}: {hw} owned hardware, automated recording from {rec}, and AI stats for {ai} with deep game analysis. Request live demo.",
        "badge": "OFFICIAL CAMERA OF USA PADEL & USTA • +1,500 COURTS",
        "h1": "Padel Court Cameras:<br class=\"hidden sm:inline\"> Match Recording, Highlights<br class=\"hidden sm:inline\"> & AI Game Statistics",
        "sub": "The official camera of USA Padel & USTA, already powering 1,500+ courts worldwide. {hw} one-time hardware investment (owned), plans from {rec}, 5-minute setup with zero construction works and 0 lock-in.",
        "p1_label": "Court Hardware", "p1_val": "{hw} (owned equipment)",
        "p2_label": "Software Plan", "p2_val": "{rec} (Recording) • {ai} (AI Stats)",
        "p3_label": "Lock-in", "p3_val": "0 months (Cancel or pause anytime)",
        "p4_label": "Installation", "p4_val": "5 minutes with zero works",
        "quick_p": "Save My Play is the official match recording and AI performance system for padel and tennis courts. Crystal-clear sports video quality, 5-minute setup and flexible month-to-month cancellation.",
        "why_title": "Why choose Save My Play for your club?",
        "why_sub": "The most agile court video recording and tactical analytics system, free from civil works or hidden fees",
        "f1_title": "Not surveillance cameras: dedicated sports optics",
        "f1_desc": "Built exclusively for padel and tennis. Ultra-sharp sports recording, wide angle without court distortion, and smooth live streaming.",
        "f2_title": "Clear monthly plans per court",
        "f2_desc": "Match recording, highlights, and live streaming for {rec}. AI stats plans for {ai} including complete breakdown of your game.",
        "f3_title": "Effortless setup with zero civil works",
        "f3_desc": "{hw} owned hardware. Installs in 5 minutes directly onto the net post or lighting pole, completely contract-free.",
        "demo_btn": "Request 15-Min Demo via WhatsApp",
        "rates_btn": "View Pricing",
        
        # Pricing
        "pricing_th_plan": "Plan / Specification", "pricing_th_invest": "Investment / Fee", "pricing_th_mod": "Terms", "pricing_th_serv": "Included Features",
        "tbl_hw_title": "Hardware Investment (Owned)", "tbl_hw_mod": "One-time payment", "tbl_hw_desc": "1 rectilinear sports camera per court (no fish-eye distortion) + security post mount",
        "tbl_rec_title": "Match Recording, Highlights & Streaming", "tbl_rec_mod": "0 lock-in • Month-to-month", "tbl_rec_desc": "Private cloud recording, instant mobile highlights, and official YouTube live streaming with club branding",
        "tbl_ai_title": "AI Match Statistics & Tactical Analysis", "tbl_ai_mod": "0 lock-in • Optional", "tbl_ai_desc": "Shot breakdown, court heatmaps, ball speed tracking, and individual player performance analytics",
        "pricing_footnote": "* Prices exclude VAT. Zero contract lock-in. 5-minute setup.",

        # Videos
        "vid_badge": "Real Court Demonstration",
        "vid_title": "Experience Recording and Streaming Quality",
        "vid_sub": "Official FIP live broadcasts, automated highlights, and tactical coaching analysis tools.",
        "vid1_t": "FIP Miami Padel Open", "vid1_d": "Official live stream and multi-court broadcasting",
        "vid2_t": "Automated Match Highlights", "vid2_d": "Direct mobile QR download without installing apps",
        "vid3_t": "Tactical Coaching Video", "vid3_d": "Performance analysis tools for coaches and academies",
        "vid4_t": "Club Tournament Broadcast", "vid4_d": "YouTube live streaming with club branding overlay",

        # FAQs
        "faq_title": "Frequently Asked Questions",
        "faq_sub": "Everything you need to know about Save My Play camera system for padel clubs",
        "faq1_q": "Are civil works, cabling, or floor trenches required?",
        "faq1_a": "No, absolutely zero works. The camera mounts directly onto the court net post or light column in just 5 minutes.",
        "faq2_q": "What is the pricing model and what plans exist?",
        "faq2_a": "{hw} per camera owned outright. Monthly subscriptions: {rec} per court for recording, highlights, and live streaming; or {ai} for AI statistics and tactical analysis.",
        "faq3_q": "How does the AI process the best shots?",
        "faq3_a": "The cameras use AI to process the video stream in real time, automatically extracting top rallies ready to share on mobile.",
        "faq4_q": "Is there any long-term contract or lock-in?",
        "faq4_a": "Zero contract lock-in. Cancel or pause month-to-month without penalty.",

        # Contact
        "contact_badge": "Direct Contact", "contact_title": "Contact Us", "contact_sub": "Fast response for club managers, tournaments, and live demos.",
        "contact_wa_btn": "Send WhatsApp", "contact_mail_btn": "Send Email",

        # Footer
        "footer_b2b": "B2B Solutions", "footer_tech": "Court Technology", "footer_tools": "Free Tools", "footer_corp": "Corporate & Legal",
        "wa_msg": "Hello Javier, I would like to schedule a demo of Save My Play for padel courts in {country}"
    },

    "fr": {
        "nav_home": "Accueil", "nav_camaras": "Caméras", "nav_llaveros": "Porte-clés", "nav_calc": "Calculateurs", "nav_blog": "Blog",
        "title": "Caméras pour Terrains de Padel en {country}: Enregistrement, Highlights et Stats IA",
        "meta_desc": "Caméras pour terrains de padel en {country}: {hw} matériel possédé, enregistrement dès {rec} et statistiques avec IA à {ai}. Demandez une démo en direct.",
        "badge": "CAMÉRA OFFICIELLE USA PADEL & USTA • +1500 TERRAINS",
        "h1": "Caméras pour Terrains de Padel:<br class=\"hidden sm:inline\"> Enregistrement Matchs, Highlights<br class=\"hidden sm:inline\"> et Statistiques avec IA",
        "sub": "La caméra officielle de USA Padel et de l'USTA, déjà présente sur plus de 1 500 terrains. Investissement de {hw} en matériel en pleine propriété, forfaits dès {rec}, installation en 5 minutes sans travaux ni engagement.",
        "p1_label": "Matériel par piste", "p1_val": "{hw} possédé (achat unique)",
        "p2_label": "Abonnement Logiciel", "p2_val": "{rec} (Enregistrement) • {ai} (Statistiques IA)",
        "p3_label": "Engagement", "p3_val": "0 mois (Résiliation libre)",
        "p4_label": "Installation", "p4_val": "5 minutes sans travaux",
        "quick_p": "Save My Play est le système officiel d'enregistrement de matchs et d'analyse par intelligence artificielle pour les clubs de padel et tennis. Qualité d'image sportive haute définition, montage en 5 minutes et liberté mensuelle.",
        "why_title": "Pourquoi choisir Save My Play pour votre club ?",
        "why_sub": "La technologie de captation vidéo et d'analyse tactique la plus agile, sans travaux lourds ni coûts cachés",
        "f1_title": "Pas de caméras de surveillance: optique sportive dédiée",
        "f1_desc": "Conçues exclusivement pour le padel et le tennis. Image sportive nette, grand angle sans distorsion du terrain et diffusion en direct fluide.",
        "f2_title": "Des forfaits mensuels clairs par terrain",
        "f2_desc": "Enregistrement de matchs, highlights et streaming en direct pour {rec}. Forfaits de statistiques IA à {ai} incluant l'analyse complète de votre jeu.",
        "f3_title": "Simple à utiliser et sans travaux",
        "f3_desc": "Investissement matériel de {hw} en pleine propriété. Se fixe en 5 minutes sur le poteau du filet ou de l'éclairage, sans aucun engagement.",
        "demo_btn": "Demander une démo de 15 min via WhatsApp",
        "rates_btn": "Voir les tarifs",
        
        # Pricing
        "pricing_th_plan": "Forfait / Concept", "pricing_th_invest": "Investissement / Tarif", "pricing_th_mod": "Modalité", "pricing_th_serv": "Services Inclus",
        "tbl_hw_title": "Investissement Matériel en Pleine Propriété", "tbl_hw_mod": "Paiement unique", "tbl_hw_desc": "1 caméra sportive rectilinéaire par terrain (sans déformation fisheye) + fixation poteau",
        "tbl_rec_title": "Enregistrement, Highlights & Streaming", "tbl_rec_mod": "0 engagement • Mois par mois", "tbl_rec_desc": "Enregistrement cloud privé, génération instantanée des meilleures actions et diffusion en direct sur YouTube",
        "tbl_ai_title": "Statistiques avec IA et Analyse Tactique", "tbl_ai_mod": "0 engagement • Optionnel", "tbl_ai_desc": "Analyse des coups, cartes thermiques, vitesse de balle et données de performance individuelles",
        "pricing_footnote": "* Tarifs hors taxes. Aucun engagement de durée. Installation en 5 minutes.",

        # Videos
        "vid_badge": "Démonstration sur Piste Réelle",
        "vid_title": "Vérifiez la Qualité d'Enregistrement et de Streaming",
        "vid_sub": "Matches officiels FIP en direct, replays automatiques et outils d'analyse tactique.",
        "vid1_t": "FIP Miami Padel Open", "vid1_d": "Streaming officiel en direct et affichage multi-pistes",
        "vid2_t": "Replays Automatiques", "vid2_d": "Scan QR immédiat sur mobile sans téléchargement d'application",
        "vid3_t": "Analyse Tactique Entraîneur", "vid3_d": "Outils vidéo pour entraîneurs et académies",
        "vid4_t": "Tournoi de Club", "vid4_d": "Diffusion en direct sur YouTube aux couleurs du club",

        # FAQs
        "faq_title": "Questions Fréquentes",
        "faq_sub": "Tout ce que vous devez savoir sur le système d'enregistrement vidéo Save My Play",
        "faq1_q": "Faut-il réaliser des travaux ou des tranchées au sol ?",
        "faq1_a": "Non, zéro travaux. Le boîtier se fixe directement au poteau du filet en 5 minutes.",
        "faq2_q": "Quel est le tarif et quels forfaits existent ?",
        "faq2_a": "{hw} par caméra en propriété. Abonnements mensuels: {rec} par piste pour l'enregistrement, highlights et direct; ou {ai} pour les statistiques par IA et analyse du jeu.",
        "faq3_q": "Comment l'IA sélectionne-t-elle les meilleurs points ?",
        "faq3_a": "Les caméras traitent le signal vidéo en temps réel grâce à l'IA pour extraire automatiquement les meilleurs échanges prêts à partager.",
        "faq4_q": "Y a-t-il un engagement de durée ?",
        "faq4_a": "Aucun engagement. Résiliation libre mois par mois.",

        # Contact
        "contact_badge": "Contact Direct", "contact_title": "Contactez-nous", "contact_sub": "Réponse directe pour les clubs, tournois et démonstrations en direct.",
        "contact_wa_btn": "Envoyer un WhatsApp", "contact_mail_btn": "Envoyer un E-mail",

        # Footer
        "footer_b2b": "Solutions B2B", "footer_tech": "Technologie Court", "footer_tools": "Outils Gratuits", "footer_corp": "Entreprise & Légal",
        "wa_msg": "Bonjour Javier, je souhaite voir une démonstration de Save My Play pour les pistes de padel en {country}"
    },

    "it": {
        "nav_home": "Home", "nav_camaras": "Telecamere", "nav_llaveros": "Portachiavi", "nav_calc": "Calcolatori", "nav_blog": "Blog",
        "title": "Telecamere per Campi da Padel in {country}: Registrazione, Highlights e Statistiche con IA",
        "meta_desc": "Telecamere per campi da padel in {country}: {hw} hardware di proprietà, registrazione automatica da {rec} e statistiche con IA per {ai}. Richiedi demo dal vivo.",
        "badge": "TELECAMERA UFFICIALE USA PADEL E USTA • +1500 CAMPI",
        "h1": "Telecamere per Campi da Padel:<br class=\"hidden sm:inline\"> Registrazione Partite, Highlights<br class=\"hidden sm:inline\"> e Statistiche con IA",
        "sub": "La telecamera ufficiale di USA Padel e USTA, già installata su oltre 1.500 campi. Investimento di {hw} in hardware di proprietà, piani da {rec}, montaggio in 5 minuti senza opere edili e senza vincoli.",
        "p1_label": "Hardware Campo", "p1_val": "{hw} di proprietà (acquisto unico)",
        "p2_label": "Quota Software", "p2_val": "{rec} (Registrazione) • {ai} (Statistiche IA)",
        "p3_label": "Vincolo contrattuale", "p3_val": "0 mesi (Cancellazione libera)",
        "p4_label": "Installazione", "p4_val": "5 minuti senza opere edili",
        "quick_p": "Save My Play è il sistema ufficiale di registrazione partite e statistiche con intelligenza artificiale per campi da padel e tennis. Qualità ottica sportiva, installazione rapida in 5 minuti e rinnovo mensile libero.",
        "why_title": "Perché scegliere Save My Play per il tuo circolo?",
        "why_sub": "La tecnologia di registrazione e analisi più rapida ed efficiente sul campo, senza lavori invasivi né costi nascosti",
        "f1_title": "Non sono telecamere di videosorveglianza: massima qualità sportiva",
        "f1_desc": "Progettate esclusivamente per padel e tennis. Registrazione sportiva nitida, grandangolo senza distorsione del campo e live streaming fluido.",
        "f2_title": "Piani mensili chiari per campo",
        "f2_desc": "Registrazione partite, highlights e dirette a {rec}. Piani di statistiche con IA a {ai} con analisi tattica completa del gioco.",
        "f3_title": "Facile da usare e senza opere edili",
        "f3_desc": "Investimento hardware di {hw} di proprietà. Si installa in 5 minuti sul palo della rete o sull'illuminazione, senza vincoli di permanenza.",
        "demo_btn": "Richiedi Demo di 15 min su WhatsApp",
        "rates_btn": "Vedi Tariffe",
        
        # Pricing
        "pricing_th_plan": "Piano / Specifica", "pricing_th_invest": "Investimento / Quota", "pricing_th_mod": "Modalità", "pricing_th_serv": "Servizi Inclusi",
        "tbl_hw_title": "Investimento Hardware di Proprietà", "tbl_hw_mod": "Pagamento unico", "tbl_hw_desc": "1 telecamera sportiva rettilinea per campo (senza effetto fish-eye) + attacco rapido al palo",
        "tbl_rec_title": "Registrazione, Highlights e Streaming", "tbl_rec_mod": "0 vincoli • Rinnovo mensile", "tbl_rec_desc": "Registrazione su cloud privato, generazione istantanea dei migliori punti e diretta ufficiale su YouTube",
        "tbl_ai_title": "Statistiche con IA e Analisi Tattica", "tbl_ai_mod": "0 vincoli • Opzionale", "tbl_ai_desc": "Analisi dei colpi, mappe di calore, velocità di palla e statistiche individuali per giocatore",
        "pricing_footnote": "* Prezzi IVA esclusa. Nessun vincolo di durata. Montaggio in 5 minuti.",

        # Videos
        "vid_badge": "Dimostrazione su Campo Reale",
        "vid_title": "Verifica la Qualità di Registrazione e Streaming",
        "vid_sub": "Partite ufficiali FIP in diretta, replay automatici e strumenti di analisi tattica.",
        "vid1_t": "FIP Miami Padel Open", "vid1_d": "Live streaming ufficiale e visualizzazione multi-campo",
        "vid2_t": "Replay Automatici", "vid2_d": "Download QR immediato sullo smartphone senza installare app",
        "vid3_t": "Analisi Tattica per Maestri", "vid3_d": "Strumenti video professionali per scuole e maestri",
        "vid4_t": "Torneo di Circolo", "vid4_d": "Diretta streaming YouTube con logo del circolo",

        # FAQs
        "faq_title": "Domande Frequenti",
        "faq_sub": "Tutto quello che c'è da sapere sulle telecamere Save My Play per campi da padel",
        "faq1_q": "Sono necessari lavori edili o canaline nel terreno?",
        "faq1_a": "No, zero lavori edili. Il dispositivo si fissa direttamente al palo della rete in 5 minuti.",
        "faq2_q": "Qual è il costo e quali piani sono disponibili?",
        "faq2_a": "{hw} a telecamera di proprietà. Piani mensili: {rec} a campo per registrazione, highlights e streaming; oppure {ai} per statistiche con IA e analisi tattica.",
        "faq3_q": "In che modo l'IA seleziona i punti migliori?",
        "faq3_a": "Le telecamere elaborano il segnale video in tempo reale con l'IA, estraendo automaticamente i migliori scambi pronti per essere condivisi.",
        "faq4_q": "Ci sono vincoli o contratti a lungo termine?",
        "faq4_a": "Nessun vincolo. Disdetta libera mese per mese.",

        # Contact
        "contact_badge": "Contatto Diretto", "contact_title": "Contattaci", "contact_sub": "Risposta diretta per circoli, tornei e dimostrazioni dal vivo.",
        "contact_wa_btn": "Invia WhatsApp", "contact_mail_btn": "Invia E-mail",

        # Footer
        "footer_b2b": "Soluzioni B2B", "footer_tech": "Tecnologia Campo", "footer_tools": "Strumenti Gratuiti", "footer_corp": "Azienda & Legale",
        "wa_msg": "Ciao Javier, vorrei prenotare una demo di Save My Play per campi da padel in {country}"
    },

    "de": {
        "nav_home": "Startseite", "nav_camaras": "Kameras", "nav_llaveros": "Schlüsselanhänger", "nav_calc": "Rechner", "nav_blog": "Blog",
        "title": "Padel-Kameras in {country}: Spielaufzeichnung, Highlights und KI-Statistiken",
        "meta_desc": "Padel-Kameras in {country}: {hw} Hardware-Eigentum, automatische Spielaufzeichnung ab {rec} und KI-Statistiken für {ai}. Live-Demo anfordern.",
        "badge": "OFFIZIELLE KAMERA VON USA PADEL & USTA • +1500 PLÄTZE",
        "h1": "Padel-Kameras für Plätze:<br class=\"hidden sm:inline\"> Spielaufzeichnung, Highlights<br class=\"hidden sm:inline\"> und KI-Statistiken",
        "sub": "Die offizielle Kamera von USA Padel und USTA, bereits auf über 1.500 Plätzen im Einsatz. {hw} Hardware-Investition im Eigentum, Tarife ab {rec}, 5 Minuten Montage ohne Bauarbeiten und ohne Vertragsbindung.",
        "p1_label": "Hardware pro Platz", "p1_val": "{hw} im Eigentum (Einmalkauf)",
        "p2_label": "Software-Tarif", "p2_val": "{rec} (Aufzeichnung) • {ai} (KI-Statistiken)",
        "p3_label": "Vertragslaufzeit", "p3_val": "0 Monate (Monatlich kündbar)",
        "p4_label": "Installation", "p4_val": "5 Minuten ohne Bauarbeiten",
        "quick_p": "Save My Play ist das offizielle Kamerasystem für Spielaufzeichnung und KI-Leistungsanalyse auf Padel- und Tennisplätzen. Professionelle Sportbildqualität, blitzschnelle 5-Minuten-Montage und freie monatliche Kündigung.",
        "why_title": "Warum Save My Play für Ihren Club wählen?",
        "why_sub": "Die agilste Aufzeichnungs- und Analysetechnik für Padelplätze, ohne Erdarbeiten und ohne versteckte Gebühren",
        "f1_title": "Keine Überwachungskameras: echte Sportoptik",
        "f1_desc": "Exklusiv für Padel und Tennis entwickelt. Gestochen scharfe Sportaufnahmen, Weitwinkel ohne Platzverzerrung und flüssiges Livestreaming.",
        "f2_title": "Transparente Monatstarife pro Platz",
        "f2_desc": "Spielaufzeichnung, Highlights und Livestreaming ab {rec}. KI-Statistikpläne für {ai} inklusive vollständiger Spielanalyse.",
        "f3_title": "Einfach zu bedienen und ohne Bauarbeiten",
        "f3_desc": "{hw} Hardware-Eigentum. Montage in nur 5 Minuten direkt am Netzpfosten oder Lichtmast, völlig ohne Vertragsbindung.",
        "demo_btn": "15-Min-Demo per WhatsApp anfordern",
        "rates_btn": "Preise ansehen",
        
        # Pricing
        "pricing_th_plan": "Plan / Spezifikation", "pricing_th_invest": "Investition / Gebühr", "pricing_th_mod": "Modell", "pricing_th_serv": "Enthaltene Leistungen",
        "tbl_hw_title": "Hardware-Investition im Eigentum", "tbl_hw_mod": "Einmalzahlung", "tbl_hw_desc": "1 Sportkamera pro Platz (gerades Objektiv ohne Fischaugen-Verzerrung) + Pfostenhalterung",
        "tbl_rec_title": "Aufzeichnung, Highlights & Streaming", "tbl_rec_mod": "0 Vertragsbindung • Monatlich kündbar", "tbl_rec_desc": "Aufzeichnung in privater Cloud, automatische Highlight-Erstellung und Livestreaming auf YouTube",
        "tbl_ai_title": "KI-Statistiken und Taktikanalyse", "tbl_ai_mod": "0 Vertragsbindung • Optional", "tbl_ai_desc": "Schlaganalyse, Heatmaps, Ballgeschwindigkeitsmessung und individuelle Spielerdaten",
        "pricing_footnote": "* Preise zzgl. MwSt. Keine Mindestvertragslaufzeit. 5 Minuten Montage.",

        # Videos
        "vid_badge": "Live-Demonstration auf dem Platz",
        "vid_title": "Überzeugen Sie sich von Bild- und Streamingqualität",
        "vid_sub": "Offizielle FIP-Turniere live, automatisierte Highlight-Clips und Taktikanalyse.",
        "vid1_t": "FIP Miami Padel Open", "vid1_d": "Offizieller Livestream und Multi-Court Übertragung",
        "vid2_t": "Automatische Highlights", "vid2_d": "Direkter QR-Download auf das Smartphone ohne App-Installation",
        "vid3_t": "Taktisches Video-Coaching", "vid3_d": "Analysewerkzeuge für Trainer und Akademien",
        "vid4_t": "Club-Turnier", "vid4_d": "YouTube-Livestream mit Club-Logo Einblendung",

        # FAQs
        "faq_title": "Häufig Gestellte Fragen",
        "faq_sub": "Alles Wichtige zum Save My Play Kamerasystem für Padelclubs",
        "faq1_q": "Sind Erdarbeiten oder Kabelkanäle im Boden erforderlich?",
        "faq1_a": "Nein, null Bauarbeiten. Das Kamerasystem wird in 5 Minuten direkt am Netzpfosten des Platzes fixiert.",
        "faq2_q": "Wie hoch sind die Kosten und welche Pläne gibt es?",
        "faq2_a": "{hw} pro Kamera im Club-Eigentum. Monatliche Tarife: {rec} pro Platz für Aufzeichnung, Highlights und Direct-Stream; oder {ai} für KI-Statistiken mit Spielanalyse.",
        "faq3_q": "Wie verarbeitet die KI die besten Ballwechsel?",
        "faq3_a": "Die Kameras analysieren das Videosignal in Echtzeit mittels KI, schneiden spektakuläre Ballwechsel automatisch heraus und stellen sie bereit.",
        "faq4_q": "Gibt es eine Mindestvertragslaufzeit?",
        "faq4_a": "Keinerlei Vertragsbindung. Monatlich flexibel kündbar.",

        # Contact
        "contact_badge": "Direkter Kontakt", "contact_title": "Kontaktieren Sie Uns", "contact_sub": "Direkte Antworten für Clubbetreiber, Turnierausrichter und Live-Demos.",
        "contact_wa_btn": "WhatsApp Senden", "contact_mail_btn": "E-Mail Senden",

        # Footer
        "footer_b2b": "B2B Lösungen", "footer_tech": "Platz-Technologie", "footer_tools": "Kostenlose Tools", "footer_corp": "Unternehmen & Rechtliches",
        "wa_msg": "Hallo Javier, ich interessiere mich für eine Demo von Save My Play für Padelplätze in {country}"
    }
}
