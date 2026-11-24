# -*- coding: utf-8 -*-
"""
Diccionario y utilidades multilingües de la Variante Asunción (Variante B) para Landings B2B de Cámaras.
Cubre los 50 países y 22 idiomas sin consumo de tokens de IA.
"""

SHIPPING_MAP = {
    # Eurozone
    "ES": "+20 € envío int.",
    "FR": "+20 € livr. int.",
    "IT": "+20 € sped. int.",
    "DE": "+20 € int. Versand",
    "AT": "+20 € int. Versand",
    "BE": "+20 € livr. int.",
    "NL": "+20 € int. verzending",
    "PT": "+20 € envio int.",
    "IE": "+20 € int. shipping",
    "FI": "+20 € int. toimitus",
    "GR": "+20 € διεθνής αποστολή",
    "AD": "+20 € enviament int.",
    # Americas
    "PY": "+Gs. 170.000 envío int.",
    "AR": "+$25 USD envío int.",
    "US": "+$25 USD int. shipping",
    "MX": "+$450 MXN envío int.",
    "CL": "+$25 USD envío int.",
    "CO": "+$25 USD envío int.",
    "UY": "+$25 USD envío int.",
    "BR": "+R$ 130 envio int.",
    "PA": "+$25 USD envío int.",
    "CR": "+$25 USD envío int.",
    "EC": "+$25 USD envío int.",
    "DO": "+$25 USD envío int.",
    "VE": "+$25 USD envío int.",
    # UK & Nordics
    "GB": "+18 £ int. shipping",
    "SE": "+230 kr int. frakt",
    "NO": "+230 kr int. frakt",
    "DK": "+150 kr int. fragt",
    "CH": "+20 CHF int. Versand",
    # Eastern Europe
    "PL": "+90 zł wysyłka międzynar.",
    "CZ": "+500 Kč mezinár. doprava",
    "RO": "+100 lei livrare int.",
    "HR": "+20 € int. dostava",
    # Middle East
    "AE": "+90 AED int. shipping",
    "SA": "+95 SAR int. shipping",
    "QA": "+90 QAR int. shipping",
    "KW": "+8 KWD int. shipping",
    "BH": "+10 BHD int. shipping",
    "OM": "+10 OMR int. shipping",
    "LB": "+$25 USD int. shipping",
    "EG": "+1.200 EGP int. shipping",
    "MA": "+220 MAD livr. int.",
    "TN": "+70 TND livr. int.",
    # Asia & Oceania
    "AU": "+$35 AUD int. shipping",
    "JP": "+¥3.800 国際送料",
    "IN": "+₹2.200 int. shipping",
    "ID": "+Rp 400.000 int. shipping",
    "TR": "+850 ₺ uluslar. kargo",
    "ZA": "+R 450 int. shipping",
}

STAT_CARDS_I18N = {
    "es": {
        "c1_lbl": "Cuota software", "c1_val": "{rec}",
        "c2_lbl": "Inversión Inicial Hardware", "c2_val": "{hw}",
        "c3_lbl": "Permanencia", "c3_val": "0 permanencia",
        "c4_lbl": "Instalación", "c4_val": "Montaje en 5 minutos"
    },
    "en": {
        "c1_lbl": "Software plan", "c1_val": "{rec}",
        "c2_lbl": "Initial Hardware Investment", "c2_val": "{hw}",
        "c3_lbl": "Commitment", "c3_val": "0 lock-in",
        "c4_lbl": "Installation", "c4_val": "5-minute setup"
    },
    "fr": {
        "c1_lbl": "Abonnement logiciel", "c1_val": "{rec}",
        "c2_lbl": "Investissement matériel", "c2_val": "{hw}",
        "c3_lbl": "Engagement", "c3_val": "0 engagement",
        "c4_lbl": "Installation", "c4_val": "Montage en 5 minutes"
    },
    "it": {
        "c1_lbl": "Canone software", "c1_val": "{rec}",
        "c2_lbl": "Investimento hardware", "c2_val": "{hw}",
        "c3_lbl": "Permanenza", "c3_val": "0 vincoli",
        "c4_lbl": "Installazione", "c4_val": "Montaggio in 5 minuti"
    },
    "de": {
        "c1_lbl": "Software-Gebühr", "c1_val": "{rec}",
        "c2_lbl": "Hardware-Investition", "c2_val": "{hw}",
        "c3_lbl": "Laufzeit", "c3_val": "0 Vertragslaufzeit",
        "c4_lbl": "Installation", "c4_val": "Montage in 5 Minuten"
    },
    "pt": {
        "c1_lbl": "Mensalidade software", "c1_val": "{rec}",
        "c2_lbl": "Investimento em hardware", "c2_val": "{hw}",
        "c3_lbl": "Fidelização", "c3_val": "0 fidelização",
        "c4_lbl": "Instalação", "c4_val": "Montagem em 5 minutos"
    },
    "pt-br": {
        "c1_lbl": "Mensalidade software", "c1_val": "{rec}",
        "c2_lbl": "Investimento em hardware", "c2_val": "{hw}",
        "c3_lbl": "Fidelidade", "c3_val": "0 fidelidade",
        "c4_lbl": "Instalação", "c4_val": "Montagem em 5 minutos"
    },
    "nl": {
        "c1_lbl": "Softwaretarief", "c1_val": "{rec}",
        "c2_lbl": "Hardware-investering", "c2_val": "{hw}",
        "c3_lbl": "Verplichting", "c3_val": "0 opzegtermijn",
        "c4_lbl": "Installatie", "c4_val": "Montage in 5 minuten"
    },
    "sv": {
        "c1_lbl": "Månadsavgift software", "c1_val": "{rec}",
        "c2_lbl": "Hårdvaruinvestering", "c2_val": "{hw}",
        "c3_lbl": "Bindningstid", "c3_val": "0 månader bindningstid",
        "c4_lbl": "Installation", "c4_val": "Montering på 5 minuter"
    },
    "no": {
        "c1_lbl": "Månedspris programvare", "c1_val": "{rec}",
        "c2_lbl": "Maskinvareinvestering", "c2_val": "{hw}",
        "c3_lbl": "Bindingstid", "c3_val": "0 månader bindingstid",
        "c4_lbl": "Installasjon", "c4_val": "Montering på 5 minutter"
    },
    "da": {
        "c1_lbl": "Softwareabonnement", "c1_val": "{rec}",
        "c2_lbl": "Hardwareinvestering", "c2_val": "{hw}",
        "c3_lbl": "Binding", "c3_val": "0 måneders binding",
        "c4_lbl": "Installation", "c4_val": "Montering på 5 minutter"
    },
    "fi": {
        "c1_lbl": "Ohjelmistomaksu", "c1_val": "{rec}",
        "c2_lbl": "Laitteistoinvestointi", "c2_val": "{hw}",
        "c3_lbl": "Sitoutumisaika", "c3_val": "0 kuukautta sitoutumisaikaa",
        "c4_lbl": "Asennus", "c4_val": "Asennus 5 minuutissa"
    },
    "pl": {
        "c1_lbl": "Abonament software", "c1_val": "{rec}",
        "c2_lbl": "Inwestycja w sprzęt", "c2_val": "{hw}",
        "c3_lbl": "Umowa", "c3_val": "0 zobowiązań",
        "c4_lbl": "Instalacja", "c4_val": "Montaż w 5 minut"
    },
    "cs": {
        "c1_lbl": "Poplatek za software", "c1_val": "{rec}",
        "c2_lbl": "Investice do hardwaru", "c2_val": "{hw}",
        "c3_lbl": "Vázanost", "c3_val": "0 závazků",
        "c4_lbl": "Instalace", "c4_val": "Montáž za 5 minut"
    },
    "ro": {
        "c1_lbl": "Abonament software", "c1_val": "{rec}",
        "c2_lbl": "Investiție hardware", "c2_val": "{hw}",
        "c3_lbl": "Perioadă minimă", "c3_val": "0 perioadă contractuală",
        "c4_lbl": "Instalare", "c4_val": "Montaj în 5 minute"
    },
    "hr": {
        "c1_lbl": "Mjesečna naknada software", "c1_val": "{rec}",
        "c2_lbl": "Ulaganje u hardver", "c2_val": "{hw}",
        "c3_lbl": "Ugovorna obveza", "c3_val": "0 ugovorne obveze",
        "c4_lbl": "Instalacija", "c4_val": "Montaža u 5 minuta"
    },
    "el": {
        "c1_lbl": "Συνδρομή λογισμικού", "c1_val": "{rec}",
        "c2_lbl": "Αρχική επένδυση hardware", "c2_val": "{hw}",
        "c3_lbl": "Δέσμευση", "c3_val": "0 δεσμεύσεις",
        "c4_lbl": "Εγκατάσταση", "c4_val": "Τοποθέτηση σε 5 λεπτά"
    },
    "tr": {
        "c1_lbl": "Yazılım ücreti", "c1_val": "{rec}",
        "c2_lbl": "Donanım yatırımı", "c2_val": "{hw}",
        "c3_lbl": "Taahhüt", "c3_val": "0 taahhüt",
        "c4_lbl": "Kurulum", "c4_val": "5 dakikada kurulum"
    },
    "ar": {
        "c1_lbl": "اشتراك البرنامج", "c1_val": "{rec}",
        "c2_lbl": "الاستثمار في الأجهزة", "c2_val": "{hw}",
        "c3_lbl": "مدة الالتزام", "c3_val": "بدون أي التزام",
        "c4_lbl": "التركيب", "c4_val": "تركيب خلال 5 دقائق"
    },
    "ja": {
        "c1_lbl": "ソフトウェア月額", "c1_val": "{rec}",
        "c2_lbl": "機器初期費用", "c2_val": "{hw}",
        "c3_lbl": "契約期間", "c3_val": "契約縛りなし",
        "c4_lbl": "設置", "c4_val": "5分で簡単設置"
    },
    "id": {
        "c1_lbl": "Biaya software", "c1_val": "{rec}",
        "c2_lbl": "Investasi hardware", "c2_val": "{hw}",
        "c3_lbl": "Kontrak", "c3_val": "Tanpa komitmen",
        "c4_lbl": "Pemasangan", "c4_val": "Pemasangan 5 menit"
    },
    "ca": {
        "c1_lbl": "Quota programari", "c1_val": "{rec}",
        "c2_lbl": "Inversió maquinari", "c2_val": "{hw}",
        "c3_lbl": "Permanència", "c3_val": "0 permanència",
        "c4_lbl": "Instal·lació", "c4_val": "Muntatge en 5 minuts"
    }
}

AWARD_BADGE_I18N = {
    "es": "Cámara Oficial USA Padel y USTA",
    "en": "Official Camera USA Padel & USTA",
    "fr": "Caméra Officielle USA Padel & USTA",
    "it": "Telecamera Ufficiale USA Padel e USTA",
    "de": "Offizielle Kamera USA Padel & USTA",
    "pt": "Câmera Oficial USA Padel e USTA",
    "pt-br": "Câmera Oficial USA Padel e USTA",
    "nl": "Officiële Camera USA Padel & USTA",
    "sv": "Officiell Kamera USA Padel & USTA",
    "no": "Offisielt Kamera USA Padel & USTA",
    "da": "Officielt Kamera USA Padel & USTA",
    "fi": "Virallinen Kamera USA Padel & USTA",
    "pl": "Oficjalna Kamera USA Padel & USTA",
    "cs": "Oficiální Kamera USA Padel & USTA",
    "ro": "Camera Oficială USA Padel & USTA",
    "hr": "Službena Kamera USA Padel & USTA",
    "el": "Επίσημη Κάμερα USA Padel & USTA",
    "tr": "Resmi Kamera USA Padel & USTA",
    "ar": "الكاميرا الرسمية لـ USA Padel و USTA",
    "ja": "USA Padel & USTA 公式カメラ",
    "id": "Kamera Resmi USA Padel & USTA",
    "ca": "Càmera Oficial USA Padel i USTA"
}

ARTICLES_I18N = {
    "es": {
        "art1_title": "Estoy pensando poner cámaras en mi club, ¿por dónde empiezo?",
        "art2_title": "Los 3 errores de los clubs que se arrepienten de poner cámaras",
        "art3_title": "¿Por qué no recomiendo el plan caro de estadísticas con IA al 95 % de los clubs?",
        "read_btn": "Leer artículo"
    },
    "en": {
        "art1_title": "Thinking about adding cameras to your club? Where to start",
        "art2_title": "The 3 biggest mistakes clubs make when installing cameras",
        "art3_title": "Why I don't recommend the expensive AI stats plan to 95% of clubs",
        "read_btn": "Read article"
    },
    "fr": {
        "art1_title": "Vous envisagez d'installer des caméras dans votre club ? Par où commencer",
        "art2_title": "Les 3 erreurs des clubs qui regrettent d'avoir installé des caméras",
        "art3_title": "Pourquoi je ne recommande pas le forfait IA coûteux à 95 % des clubs",
        "read_btn": "Lire l'article"
    },
    "it": {
        "art1_title": "Stai pensando di installare telecamere nel tuo club? Da dove iniziare",
        "art2_title": "I 3 errori dei club che si pentono di aver installato telecamere",
        "art3_title": "Perché non consiglio il piano avanzato di statistiche IA al 95% dei club",
        "read_btn": "Leggi l'articolo"
    },
    "de": {
        "art1_title": "Kameras für Ihren Padel-Club? Wo Sie anfangen sollten",
        "art2_title": "Die 3 häufigsten Fehler von Clubs beim Kamerakauf",
        "art3_title": "Warum ich 95 % der Clubs vom teuren KI-Analyse-Plan abrate",
        "read_btn": "Artikel lesen"
    },
    "pt": {
        "art1_title": "Pensando em instalar câmeras no seu clube? Por onde começar",
        "art2_title": "Os 3 maiores erros dos clubes que se arrependem de instalar câmeras",
        "art3_title": "Por que não recomendo o plano caro de estatísticas com IA para 95% dos clubes",
        "read_btn": "Ler artigo"
    },
    "pt-br": {
        "art1_title": "Pensando em instalar câmeras no seu clube? Por onde começar",
        "art2_title": "Os 3 maiores erros dos clubes que se arrependem de instalar câmeras",
        "art3_title": "Por que não recomendo o plano caro de estatísticas com IA para 95% dos clubes",
        "read_btn": "Ler artigo"
    },
    "nl": {
        "art1_title": "Denk je na over camera's in je padelclub? Waar te beginnen",
        "art2_title": "De 3 grootste fouten van clubs die spijt kregen van camera's",
        "art3_title": "Waarom ik het dure AI-statistiekenplan afraadt voor 95% van de clubs",
        "read_btn": "Lees artikel"
    },
    "sv": {
        "art1_title": "Funderar du på att installera kameror i din klubb? Var ska du börja",
        "art2_title": "De 3 vanligaste misstagen klubbar gör när de skaffar kameror",
        "art3_title": "Varför jag inte rekommenderar den dyra AI-statistikplanen till 95 % av klubbarna",
        "read_btn": "Läs artikel"
    },
    "no": {
        "art1_title": "Vurderer du å sette opp kameraer i klubben? Hvor bør du starte",
        "art2_title": "De 3 vanligste feilene klubber gjør når de installerer kameraer",
        "art3_title": "Hvorfor jeg fraråder den dyre AI-statistikkplanen til 95 % av klubbene",
        "read_btn": "Les artikkel"
    },
    "da": {
        "art1_title": "Overvejer du at sætte kameraer op i din klub? Hvor skal du starte",
        "art2_title": "De 3 største fejl klubber begår, når de installerer kameraer",
        "art3_title": "Hvorfor jeg fraråder den dyre AI-statistikpakke til 95 % af klubberne",
        "read_btn": "Læs artikel"
    },
    "fi": {
        "art1_title": "Harkitsetko kameroiden asentamista klubillesi? Mistä aloittaa",
        "art2_title": "Kolme yleisintä virhettä, joita klubit tekevät kameroiden asennuksessa",
        "art3_title": "Miksi en suosittele kallista tekoälyanalyysipakettia 95 prosentille klubeista",
        "read_btn": "Lue artikkeli"
    },
    "pl": {
        "art1_title": "Myślisz o kamerach w swoim klubie? Od czego zacząć",
        "art2_title": "3 największe błędy klubów, które żałują instalacji kamer",
        "art3_title": "Dlaczego odradzam drogi pakiet analizy AI 95% klubów",
        "read_btn": "Przeczytaj artykuł"
    },
    "cs": {
        "art1_title": "Přemýšlíte o kamerách ve svém klubu? Kde začít",
        "art2_title": "3 největší chyby klubů, které litují instalace kamer",
        "art3_title": "Proč 95 % klubů nedoporučuji drahý plán s AI statistikami",
        "read_btn": "Přečíst článek"
    },
    "ro": {
        "art1_title": "Te gândești să instalezi camere în clubul tău? De unde să începi",
        "art2_title": "Cele 3 mari greșeli ale cluburilor care regretă instalarea camerelor",
        "art3_title": "De ce nu recomand planul scump de statistici AI pentru 95% dintre cluburi",
        "read_btn": "Citește articolul"
    },
    "hr": {
        "art1_title": "Razmišljate o kamerama u svom klubu? Odakle početi",
        "art2_title": "3 najveće pogreške klubova koji su požalili instalaciju kamera",
        "art3_title": "Zašto ne preporučujem skupi AI paket statistike za 95% klubova",
        "read_btn": "Pročitaj članak"
    },
    "el": {
        "art1_title": "Σκέφτεστε να βάλετε κάμερες στο club σας; Από πού να ξεκινήσετε",
        "art2_title": "Τα 3 μεγαλύτερα λάθη των clubs που μετάνιωσαν για τις κάμερες",
        "art3_title": "Γιατί δεν συστήνω το ακριβό πλάνο στατιστικών AI στο 95% των clubs",
        "read_btn": "Διαβάστε το άρθρο"
    },
    "tr": {
        "art1_title": "Kulübünüze kamera taktırmayı mı düşünüyorsunuz? Nereden başlamalı",
        "art2_title": "Kamera taktıran kulüplerin en çok pişman olduğu 3 hata",
        "art3_title": "Neden kulüplerin %95'ine pahalı yapay zeka analiz paketini önermiyorum",
        "read_btn": "Makaleyi oku"
    },
    "ar": {
        "art1_title": "هل تفكر في تثبيت كاميرات في ناديك؟ من أين تبدأ",
        "art2_title": "الأخطاء الثلاثة الشائعة للأندية التي تندم على اختيار الكاميرات",
        "art3_title": "لماذا لا أنصح بباكيدج إحصائيات الذكاء الاصطناعي الباهظ لـ 95% من الأندية",
        "read_btn": "اقرأ المقال"
    },
    "ja": {
        "art1_title": "クラブにカメラの導入をお考えですか？ まず何をすべきか",
        "art2_title": "カメラを導入して後悔したクラブに共通する3つの失敗",
        "art3_title": "95%のクラブに高額なAI分析プランをおすすめしない理由",
        "read_btn": "記事を読む"
    },
    "id": {
        "art1_title": "Mempertimbangkan kamera untuk klub Anda? Dari mana memulai",
        "art2_title": "3 kesalahan terbesar klub yang menyesal memasang kamera",
        "art3_title": "Mengapa saya tidak merekomendasikan paket statistik AI mahal untuk 95% klub",
        "read_btn": "Baca artikel"
    },
    "ca": {
        "art1_title": "Estic pensant posar càmeres al meu club, per on començo?",
        "art2_title": "Els 3 errors dels clubs que es penedeixen de posar càmeres",
        "art3_title": "Per què no recomano el pla car d'estadístiques amb IA al 95 % dels clubs?",
        "read_btn": "Llegir article"
    }
}

DEMO_BTN_TEXT = {
    "es": "Solicitar Demo 15 min por WhatsApp",
    "en": "Request 15-min WhatsApp Demo",
    "fr": "Demander une Démo 15 min sur WhatsApp",
    "it": "Richiedi Demo 15 min su WhatsApp",
    "de": "15-Min-WhatsApp-Demo anfordern",
    "pt": "Pedir Demo 15 min por WhatsApp",
    "pt-br": "Pedir Demo 15 min por WhatsApp",
    "nl": "Vraag 15-min WhatsApp-demo aan",
    "sv": "Boka 15 min WhatsApp-demo",
    "no": "Bestill 15 min WhatsApp-demo",
    "da": "Bestil 15 min WhatsApp-demo",
    "fi": "Pyydä 15 min WhatsApp-esittely",
    "pl": "Zamów 15-min demo na WhatsApp",
    "cs": "Požádat o 15min demo na WhatsApp",
    "ro": "Solicită Demo 15 min pe WhatsApp",
    "hr": "Zatražite 15-min demo na WhatsAppu",
    "el": "Ζητήστε 15λεπτη επίδειξη στο WhatsApp",
    "tr": "WhatsApp'tan 15 dk Demo İsteyin",
    "ar": "اطلب عرضاً توضيحياً خلال 15 دقيقة عبر واتساب",
    "ja": "WhatsAppで15分デモを申し込む",
    "id": "Minta Demo 15 menit via WhatsApp",
    "ca": "Demanar Demo 15 min per WhatsApp"
}

TARIFS_BTN_TEXT = {
    "es": "Ver Tarifas",
    "en": "View Pricing",
    "fr": "Voir les tarifs",
    "it": "Vedi Tariffe",
    "de": "Preise ansehen",
    "pt": "Ver Tarifas",
    "pt-br": "Ver Tarifas",
    "nl": "Bekijk Tarieven",
    "sv": "Se Priser",
    "no": "Se Priser",
    "da": "Se Priser",
    "fi": "Katso Hinnat",
    "pl": "Zobacz Ceny",
    "cs": "Zobrazit Ceník",
    "ro": "Vezi Tarife",
    "hr": "Pogledajte Cijene",
    "el": "Δείτε Τιμές",
    "tr": "Fiyatları Gör",
    "ar": "عرض الأسعار",
    "ja": "料金プランを見る",
    "id": "Lihat Tarif",
    "ca": "Veure Tarifes"
}

SUBTITLE_I18N = {
    "es": {
        "l1": "La Cámara Nº1 de Tenis y Pádel en Estados Unidos.",
        "l2": "Presente en +600 clubs y +1500 pistas.",
        "l3": "Retransmite partidos, comparte los mejores puntos y analiza estadísticas con IA."
    },
    "en": {
        "l1": "The #1 Tennis & Padel Camera in the United States.",
        "l2": "Live in +600 clubs and +1,500 courts.",
        "l3": "Stream matches, share the best highlights and analyze AI game statistics."
    },
    "fr": {
        "l1": "La Caméra N°1 de Tennis et Padel aux États-Unis.",
        "l2": "Présente dans +600 clubs et +1500 terrains.",
        "l3": "Diffusez les matchs, partagez les meilleurs points et analysez les statistiques avec l'IA."
    },
    "it": {
        "l1": "La Telecamera N°1 di Tennis e Padel negli Stati Uniti.",
        "l2": "Presente in +600 club e +1500 campi.",
        "l3": "Trasmetti partite, condividi i punti migliori e analizza statistiche con IA."
    },
    "de": {
        "l1": "Die Nr. 1 Tennis- und Padel-Kamera in den USA.",
        "l2": "Aktiv in +600 Clubs und +1500 Plätzen.",
        "l3": "Spiele streamen, beste Highlights teilen und KI-Spielstatistiken analysieren."
    },
    "pt": {
        "l1": "A Câmera Nº1 de Tênis e Padel nos Estados Unidos.",
        "l2": "Presente em +600 clubes e +1500 campos.",
        "l3": "Transmita partidas, compartilhe os melhores pontos e analise estatísticas com IA."
    },
    "pt-br": {
        "l1": "A Câmera Nº1 de Tênis e Padel nos Estados Unidos.",
        "l2": "Presente em +600 clubes e +1500 quadras.",
        "l3": "Transmita partidas, compartilhe os melhores pontos e analise estatísticas com IA."
    },
    "nl": {
        "l1": "De #1 Tennis- & Padelcamera in de Verenigde Staten.",
        "l2": "Actief in +600 clubs en +1500 banen.",
        "l3": "Wedstrijden streamen, beste punten delen en AI-statistieken analyseren."
    },
    "sv": {
        "l1": "Den ledande tennis- och padelkameran i USA.",
        "l2": "Aktiv i +600 klubbar och +1500 banor.",
        "l3": "Streama matcher, dela bästa höjdpunkterna och analysera AI-statistik."
    },
    "no": {
        "l1": "Den ledende tennis- og padelkameraet i USA.",
        "l2": "Aktiv i +600 klubber og +1500 baner.",
        "l3": "Strøm kamper, del beste høydepunkter og analyser AI-statistikk."
    },
    "da": {
        "l1": "Det førende tennis- og padelkamera i USA.",
        "l2": "Aktiv i +600 klubber og +1500 baner.",
        "l3": "Stream kampe, del bedste højdepunkter og analysér AI-statistik."
    },
    "fi": {
        "l1": "Yhdysvaltain johtava tennis- ja padelkamera.",
        "l2": "Käytössä yli 600 klubilla ja 1500 kentällä.",
        "l3": "Lähetä otteluita, jaa parhaat kohokohdat ja analysoi tekoälytilastoja."
    },
    "pl": {
        "l1": "Kamera nr 1 do tenisa i padla w Stanach Zjednoczonych.",
        "l2": "Obecna w ponad 600 klubach i na 1500 kortach.",
        "l3": "Transmituj mecze, udostępniaj najlepsze zagrania i analizuj statystyki AI."
    },
    "cs": {
        "l1": "Kamera č. 1 pro tenis a padel ve Spojených státech.",
        "l2": "Aktivní ve více než 600 klubech a na 1500 kurtech.",
        "l3": "Vysílejte zápasy, sdílejte nejlepší body a analyzujte statistiky s AI."
    },
    "ro": {
        "l1": "Camera nr. 1 de tenis și padel din Statele Unite.",
        "l2": "Prezentă în +600 de cluburi și pe +1500 de terenuri.",
        "l3": "Transmite meciuri, partajează cele mai bune puncte și analizează statistici AI."
    },
    "hr": {
        "l1": "Vodeća kamera za tenis i padel u Sjedinjenim Državama.",
        "l2": "Aktivna u više od 600 klubova i na 1500 terena.",
        "l3": "Prenosite mečeve, dijelite najbolje trenutke i analizirajte AI statistiku."
    },
    "el": {
        "l1": "Η Νο1 κάμερα τένις και πάντελ στις Ηνωμένες Πολιτείες.",
        "l2": "Σε περισσότερα από 600 club και 1500 γήπεδα.",
        "l3": "Μεταδώστε αγώνες, μοιραστείτε κορυφαίες φάσεις και αναλύστε στατιστικά με AI."
    },
    "tr": {
        "l1": "Amerika Birleşik Devletleri'nin 1 Numaralı Tenis ve Padel Kamerası.",
        "l2": "+600 kulüpte ve +1500 kortta aktif.",
        "l3": "Maçları yayınlayın, en iyi anları paylaşın ve yapay zeka analizlerini inceleyin."
    },
    "ar": {
        "l1": "الكاميرا الأولى للتنس والبادل في الولايات المتحدة.",
        "l2": "موجودة في أكثر من 600 نادٍ و 1500 ملعب.",
        "l3": "بث المباريات ومشاركة أفضل اللقطات وتحليل الإحصائيات بالذكاء الاصطناعي."
    },
    "ja": {
        "l1": "米国で実績No.1のテニス＆パデル専用カメラシステム。",
        "l2": "+600以上のクラブ、+1500以上のコートで稼働中。",
        "l3": "試合配信、ハイライト共有、AI戦術分析をこれ1台で。"
    },
    "id": {
        "l1": "Kamera Tenis & Padel No. 1 di Amerika Serikat.",
        "l2": "Hadir di +600 klub dan +1500 lapangan.",
        "l3": "Siarkan pertandingan, bagikan momen terbaik, dan analisis statistik AI."
    },
    "ca": {
        "l1": "La Càmera Nº1 de Tennis i Pàdel als Estats Units.",
        "l2": "Present a +600 clubs i +1500 pistes.",
        "l3": "Retransmet partits, comparteix els millors punts i analitza estadístiques amb IA."
    }
}

H1_TEMPLATES_I18N = {
    "es": "Cámaras para clubs de Pádel<br>en {target}:<br>Grabación, Highlights<br>y Estadísticas con IA",
    "en": "Padel Club Cameras<br>in {target}:<br>Match Recording, Highlights<br>& AI Game Statistics",
    "fr": "Caméras pour Clubs de Padel<br>en {target} :<br>Enregistrement Matchs, Highlights<br>et Statistiques avec IA",
    "it": "Telecamere per Club di Padel<br>a {target}:<br>Registrazione Partite, Highlights<br>e Statistiche con IA",
    "de": "Padel-Kameras für Clubs<br>in {target}:<br>Spielaufzeichnung, Highlights<br>und KI-Statistiken",
    "pt": "Câmaras para Clubes de Padel<br>em {target}:<br>Gravação de Jogos, Highlights<br>e Estatísticas com IA",
    "pt-br": "Câmeras para Clubes de Padel<br>no {target}:<br>Gravação de Partidas, Highlights<br>e Estatísticas com IA",
    "nl": "Padelcamera's voor Clubs<br>in {target}:<br>Wedstrijdopname, Highlights<br>en AI-Statistieken",
    "sv": "Padelkameror för klubbar<br>i {target}:<br>Matchinspelning, Höjdpunkter<br>och AI-Statistik",
    "no": "Padelkameraer for klubber<br>i {target}:<br>Kampopptak, Høydepunkter<br>og AI-Statistikk",
    "da": "Padelkameraer til klubber<br>i {target}:<br>Kampoptagelse, Højdepunkter<br>og AI-Statistik",
    "fi": "Padelkamerat klubeille<br>alueella {target}:<br>Ottelutallennus, Kohokohdat<br>ja Tekoälytilastot",
    "pl": "Kamery dla Klubów Padla<br>w {target}:<br>Nagrywanie Meczów, Highlights<br>i Statystyki AI",
    "cs": "Kamery pro padelové kluby<br>v {target}:<br>Záznam zápasů, Highlights<br>a AI statistiky",
    "ro": "Camere pentru Cluburi de Padel<br>în {target}:<br>Înregistrare Meciuri, Highlights<br>și Statistici AI",
    "hr": "Kamere za padel klubove<br>u {target}:<br>Snimanje mečeva, Highlights<br>i AI statistika",
    "el": "Κάμερες για Padel Clubs<br>σε {target}:<br>Καταγραφή Αγώνων, Highlights<br>και Στατιστικά AI",
    "tr": "Padel Kulüpleri İçin Kameralar<br>{target} bölgesinde:<br>Maç Kaydı, Öne Çıkanlar<br>ve Yapay Zeka İstatistikleri",
    "ar": "كاميرات أندية البادل<br>في {target}:<br>تسجيل المباريات واللقطات<br>وإحصائيات الذكاء الاصطناعي",
    "ja": "パデルクラブ専用カメラ<br>{target}:<br>試合録画・ハイライト<br>AI戦術分析システム",
    "id": "Kamera untuk Klub Padel<br>di {target}:<br>Rekaman Pertandingan, Highlights<br>dan Statistik AI",
    "ca": "Càmeres per a clubs de Pàdel<br>a {target}:<br>Gravació, Highlights<br>i Estadístiques amb IA"
}

ASUNCION_CSS_BLOCK = """
    /* --- REGLAS ASUNCIÓN (VARIANTE B) --- */
    .camera-local-hero, .bg-textured-blue {
      background-color: #3478a6 !important;
      background-image: linear-gradient(rgba(52, 120, 166, 0.40), rgba(52, 120, 166, 0.40)), url('/assets/images/branding/textura_editorial_coolpadel.webp') !important;
      background-blend-mode: normal, soft-light !important;
      background-size: cover !important;
      background-position: center !important;
    }
    .hero-btn-row {
      display: flex !important;
      flex-direction: row !important;
      align-items: center !important;
      gap: 16px !important;
      flex-wrap: wrap !important;
      padding-top: 14px !important;
    }
    @media (min-width: 640px) {
      .hero-btn-row {
        padding-top: 21px !important;
      }
    }
    @media (min-width: 1024px) {
      .hero-btn-row {
        padding-top: 25px !important;
      }
    }
    .hero-cities-row {
      display: flex !important;
      flex-direction: row !important;
      flex-wrap: nowrap !important;
      align-items: center !important;
      gap: 8px !important;
      overflow-x: auto !important;
      white-space: nowrap !important;
      -ms-overflow-style: none !important;
      scrollbar-width: none !important;
      padding-top: 14px !important;
    }
    @media (min-width: 640px) {
      .hero-cities-row {
        padding-top: 21px !important;
      }
    }
    @media (min-width: 1024px) {
      .hero-cities-row {
        padding-top: 25px !important;
      }
    }
    .hero-cities-row::-webkit-scrollbar {
      display: none !important;
    }
    .hero-city-pill {
      display: inline-flex !important;
      flex-direction: row !important;
      align-items: center !important;
      gap: 6px !important;
      white-space: nowrap !important;
      flex-shrink: 0 !important;
    }
    .hero-stats-section {
      margin-top: 3.5rem !important;
      position: relative !important;
      z-index: 20 !important;
      margin-bottom: 3.25rem !important;
    }
    @media (min-width: 640px) {
      .hero-stats-section {
        margin-top: 4.5rem !important;
        margin-bottom: 4rem !important;
      }
    }
    @media (min-width: 1024px) {
      .hero-stats-section {
        margin-top: 5rem !important;
        margin-bottom: 4.75rem !important;
      }
    }
    .hero-stat-card {
      border: none !important;
      height: 88px !important;
      display: flex !important;
      flex-direction: column !important;
      justify-content: center !important;
      background-color: #3478a6 !important;
      background-image: linear-gradient(rgba(52, 120, 166, 0.40), rgba(52, 120, 166, 0.40)), url('/assets/images/branding/textura_editorial_coolpadel.webp') !important;
      background-blend-mode: normal, soft-light !important;
      background-size: cover !important;
      background-position: center !important;
      border-radius: 1rem !important;
      box-shadow: 0 10px 20px -3px rgba(52, 120, 166, 0.25), 0 4px 6px -4px rgba(0, 0, 0, 0.1) !important;
      padding: 1rem 1.25rem !important;
      overflow: hidden !important;
    }
    .hero-featured-articles {
      display: grid !important;
      grid-template-columns: 1fr !important;
      gap: 1.25rem !important;
      width: 100% !important;
      box-sizing: border-box !important;
    }
    @media (min-width: 768px) {
      .hero-featured-articles {
        grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
        gap: 1.5rem !important;
      }
    }
    .article-card {
      display: flex !important;
      flex-direction: column !important;
      justify-content: space-between !important;
      background: #ffffff !important;
      border: 2px solid #e2e8f0 !important;
      border-radius: 1rem !important;
      padding: 1.25rem !important;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05) !important;
      text-decoration: none !important;
      color: #0f172a !important;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
      cursor: pointer !important;
      width: 100% !important;
      box-sizing: border-box !important;
    }
    .article-card:hover {
      border-color: #f2920b !important;
      transform: translateY(-2px) !important;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1) !important;
    }
    .article-thumb-wrap {
      width: 100% !important;
      aspect-ratio: 16 / 9 !important;
      border-radius: 0.75rem !important;
      overflow: hidden !important;
      background-color: #0f172a !important;
      border: 1px solid #e2e8f0 !important;
      position: relative !important;
    }
    .article-thumb-wrap img {
      width: 100% !important;
      height: 100% !important;
      object-fit: cover !important;
      display: block !important;
      transition: transform 0.5s ease !important;
    }
    .article-card:hover .article-thumb-wrap img {
      transform: scale(1.05) !important;
    }
    .article-card-title {
      font-family: 'Plus Jakarta Sans', system-ui, sans-serif !important;
      font-weight: 800 !important;
      font-size: 1.05rem !important;
      line-height: 1.35 !important;
      color: #0f172a !important;
      margin: 0.75rem 0 0 0 !important;
      transition: color 0.2s ease !important;
    }
    .article-card:hover .article-card-title {
      color: #f2920b !important;
    }
    .article-card-footer {
      padding-top: 0.875rem !important;
      border-top: 1px solid #f1f5f9 !important;
      margin-top: 1.25rem !important;
    }
    .article-card .card-action {
      position: relative !important;
      width: 100% !important;
      display: inline-flex !important;
      align-items: center !important;
      justify-content: center !important;
      gap: 0.5rem !important;
      padding: 0.625rem 1rem !important;
      border-radius: 9999px !important;
      background-color: #f2920b !important;
      color: #020617 !important;
      font-family: 'Outfit', sans-serif !important;
      font-weight: 900 !important;
      font-size: 0.75rem !important;
      text-transform: uppercase !important;
      letter-spacing: 0.05em !important;
      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05) !important;
      transition: all 0.3s ease !important;
    }
    .article-card:hover .card-action {
      background-color: #76d3f6 !important;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1) !important;
      transform: scale(1.01) !important;
    }
    .article-card .card-action .action-icon {
      width: 1rem !important;
      height: 1rem !important;
      border-radius: 9999px !important;
      background-color: rgba(2, 6, 23, 0.1) !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
      transition: all 0.3s ease !important;
    }
    .article-card:hover .card-action .action-icon {
      background-color: #020617 !important;
      color: #ffffff !important;
    }
    .article-card .card-action .action-icon svg,
    .article-card .card-action .action-icon i {
      width: 0.75rem !important;
      height: 0.75rem !important;
      stroke-width: 3 !important;
      transition: transform 0.3s ease !important;
    }
    .article-card:hover .card-action .action-icon svg,
    .article-card:hover .card-action .action-icon i {
      transform: translateX(2px) !important;
    }
"""
