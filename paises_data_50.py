# -*- coding: utf-8 -*-
"""
50 Países con pistas de pádel en el mundo.
Incluye el nombre en español, nombre local en su propio idioma, código de idioma nativo,
moneda local (símbolo y código), estimación de precios con divisa local y slug nativo en su idioma.
"""

COUNTRIES_50 = [
    {
        "rank": 1, "country_es": "España", "country_local": "España", "lang": "es",
        "courts": 17300, "curr_code": "EUR", "curr_symbol": "€", "slug": "espana", "slug_local": "espana",
        "hw": "180 €", "rec": "45 €/mes", "ai": "136 €/mes"
    },
    {
        "rank": 2, "country_es": "Italia", "country_local": "Italia", "lang": "it",
        "courts": 10220, "curr_code": "EUR", "curr_symbol": "€", "slug": "italia", "slug_local": "italia",
        "hw": "180 €", "rec": "45 €/mese", "ai": "136 €/mese"
    },
    {
        "rank": 3, "country_es": "Argentina", "country_local": "Argentina", "lang": "es",
        "courts": 7000, "curr_code": "ARS", "curr_symbol": "$", "slug": "argentina", "slug_local": "argentina",
        "hw": "180 $", "rec": "45 $/mes", "ai": "136 $/mes"
    },
    {
        "rank": 4, "country_es": "Suecia", "country_local": "Sverige", "lang": "sv",
        "courts": 4220, "curr_code": "SEK", "curr_symbol": "kr", "slug": "suecia", "slug_local": "sverige",
        "hw": "2.050 kr (180 €)", "rec": "515 kr/mån (45 €)", "ai": "1.550 kr/mån (136 €)"
    },
    {
        "rank": 5, "country_es": "Francia", "country_local": "France", "lang": "fr",
        "courts": 4000, "curr_code": "EUR", "curr_symbol": "€", "slug": "francia", "slug_local": "france",
        "hw": "180 €", "rec": "45 €/mois", "ai": "136 €/mois"
    },
    {
        "rank": 6, "country_es": "Países Bajos", "country_local": "Nederland", "lang": "nl",
        "courts": 3570, "curr_code": "EUR", "curr_symbol": "€", "slug": "paises-bajos", "slug_local": "nederland",
        "hw": "180 €", "rec": "45 €/mnd", "ai": "136 €/mnd"
    },
    {
        "rank": 7, "country_es": "México", "country_local": "México", "lang": "es",
        "courts": 2560, "curr_code": "MXN", "curr_symbol": "$", "slug": "mexico", "slug_local": "mexico",
        "hw": "180 $", "rec": "45 $/mes", "ai": "136 $/mes"
    },
    {
        "rank": 8, "country_es": "Chile", "country_local": "Chile", "lang": "es",
        "courts": 2300, "curr_code": "CLP", "curr_symbol": "$", "slug": "chile", "slug_local": "chile",
        "hw": "180 $", "rec": "45 $/mes", "ai": "136 $/mes"
    },
    {
        "rank": 9, "country_es": "Bélgica", "country_local": "Belgique", "lang": "fr",
        "courts": 2150, "curr_code": "EUR", "curr_symbol": "€", "slug": "belgica", "slug_local": "belgique",
        "hw": "180 €", "rec": "45 €/mois", "ai": "136 €/mois"
    },
    {
        "rank": 10, "country_es": "Paraguay", "country_local": "Paraguay", "lang": "es",
        "courts": 2000, "curr_code": "PYG", "curr_symbol": "$", "slug": "paraguay", "slug_local": "paraguay",
        "hw": "180 $", "rec": "45 $/mes", "ai": "136 $/mes"
    },
    {
        "rank": 11, "country_es": "Dinamarca", "country_local": "Danmark", "lang": "da",
        "courts": 1575, "curr_code": "DKK", "curr_symbol": "kr", "slug": "dinamarca", "slug_local": "danmark",
        "hw": "1.350 kr (180 €)", "rec": "340 kr/md (45 €)", "ai": "1.020 kr/md (136 €)"
    },
    {
        "rank": 12, "country_es": "Portugal", "country_local": "Portugal", "lang": "pt",
        "courts": 1560, "curr_code": "EUR", "curr_symbol": "€", "slug": "portugal", "slug_local": "portugal",
        "hw": "180 €", "rec": "45 €/mês", "ai": "136 €/mês"
    },
    {
        "rank": 13, "country_es": "Egipto", "country_local": "مصر", "lang": "ar",
        "courts": 1500, "curr_code": "EGP", "curr_symbol": "$", "slug": "egipto", "slug_local": "egypt",
        "hw": "$180", "rec": "$45 / شهرياً", "ai": "$136 / شهرياً"
    },
    {
        "rank": 14, "country_es": "Sudáfrica", "country_local": "South Africa", "lang": "en",
        "courts": 1210, "curr_code": "ZAR", "curr_symbol": "R", "slug": "sudafrica", "slug_local": "south-africa",
        "hw": "R3,600 ($180)", "rec": "R900/mo ($45)", "ai": "R2,700/mo ($136)"
    },
    {
        "rank": 15, "country_es": "Arabia Saudí", "country_local": "المملكة العربية السعودية", "lang": "ar",
        "courts": 1130, "curr_code": "SAR", "curr_symbol": "$", "slug": "arabia-saudi", "slug_local": "saudi-arabia",
        "hw": "$180 (675 ر.س)", "rec": "$45/شهرياً (170 ر.س)", "ai": "$136/شهرياً (510 ر.س)"
    },
    {
        "rank": 16, "country_es": "Finlandia", "country_local": "Suomi", "lang": "fi",
        "courts": 1100, "curr_code": "EUR", "curr_symbol": "€", "slug": "finlandia", "slug_local": "suomi",
        "hw": "180 €", "rec": "45 €/kk", "ai": "136 €/kk"
    },
    {
        "rank": 17, "country_es": "Gran Bretaña", "country_local": "United Kingdom", "lang": "en",
        "courts": 1080, "curr_code": "GBP", "curr_symbol": "£", "slug": "gran-bretana", "slug_local": "united-kingdom",
        "hw": "£155 (180 €)", "rec": "£39/mo (45 €)", "ai": "£118/mo (136 €)"
    },
    {
        "rank": 18, "country_es": "Brasil", "country_local": "Brasil", "lang": "pt",
        "courts": 1000, "curr_code": "BRL", "curr_symbol": "R$", "slug": "brasil", "slug_local": "brasil",
        "hw": "R$ 1.100 ($180)", "rec": "R$ 275/mês ($45)", "ai": "R$ 830/mês ($136)"
    },
    {
        "rank": 19, "country_es": "Emiratos Árabes Unidos", "country_local": "الإمارات العربية المتحدة", "lang": "ar",
        "courts": 950, "curr_code": "AED", "curr_symbol": "$", "slug": "emiratos-arabes-unidos", "slug_local": "uae",
        "hw": "$180 (660 AED)", "rec": "$45/شهرياً (165 AED)", "ai": "$136/شهرياً (500 AED)"
    },
    {
        "rank": 20, "country_es": "Alemania", "country_local": "Deutschland", "lang": "de",
        "courts": 875, "curr_code": "EUR", "curr_symbol": "€", "slug": "alemania", "slug_local": "deutschland",
        "hw": "180 €", "rec": "45 €/Monat", "ai": "136 €/Monat"
    },
    {
        "rank": 21, "country_es": "Estados Unidos", "country_local": "United States", "lang": "en",
        "courts": 770, "curr_code": "USD", "curr_symbol": "$", "slug": "estados-unidos", "slug_local": "united-states",
        "hw": "$180", "rec": "$45/mo", "ai": "$136/mo"
    },
    {
        "rank": 22, "country_es": "Noruega", "country_local": "Norge", "lang": "no",
        "courts": 700, "curr_code": "NOK", "curr_symbol": "kr", "slug": "noruega", "slug_local": "norge",
        "hw": "2.100 kr (180 €)", "rec": "530 kr/mnd (45 €)", "ai": "1.600 kr/mnd (136 €)"
    },
    {
        "rank": 23, "country_es": "Austria", "country_local": "Österreich", "lang": "de",
        "courts": 650, "curr_code": "EUR", "curr_symbol": "€", "slug": "austria", "slug_local": "oesterreich",
        "hw": "180 €", "rec": "45 €/Monat", "ai": "136 €/Monat"
    },
    {
        "rank": 24, "country_es": "Suiza", "country_local": "Schweiz", "lang": "de",
        "courts": 600, "curr_code": "CHF", "curr_symbol": "CHF", "slug": "suiza", "slug_local": "schweiz",
        "hw": "175 CHF (180 €)", "rec": "44 CHF/Monat (45 €)", "ai": "132 CHF/Monat (136 €)"
    },
    {
        "rank": 25, "country_es": "Polonia", "country_local": "Polska", "lang": "pl",
        "courts": 550, "curr_code": "PLN", "curr_symbol": "zł", "slug": "polonia", "slug_local": "polska",
        "hw": "780 zł (180 €)", "rec": "195 zł/mies. (45 €)", "ai": "590 zł/mies. (136 €)"
    },
    {
        "rank": 26, "country_es": "Andorra", "country_local": "Andorra", "lang": "ca",
        "courts": 500, "curr_code": "EUR", "curr_symbol": "€", "slug": "andorra", "slug_local": "andorra",
        "hw": "180 €", "rec": "45 €/mes", "ai": "136 €/mes"
    },
    {
        "rank": 27, "country_es": "Grecia", "country_local": "Ελλάδα", "lang": "el",
        "courts": 450, "curr_code": "EUR", "curr_symbol": "€", "slug": "grecia", "slug_local": "ellada",
        "hw": "180 €", "rec": "45 €/μήνα", "ai": "136 €/μήνα"
    },
    {
        "rank": 28, "country_es": "Qatar", "country_local": "قطر", "lang": "ar",
        "courts": 450, "curr_code": "QAR", "curr_symbol": "$", "slug": "qatar", "slug_local": "qatar",
        "hw": "$180 (655 QAR)", "rec": "$45/شهرياً (165 QAR)", "ai": "$136/شهرياً (495 QAR)"
    },
    {
        "rank": 29, "country_es": "Colombia", "country_local": "Colombia", "lang": "es",
        "courts": 400, "curr_code": "COP", "curr_symbol": "$", "slug": "colombia", "slug_local": "colombia",
        "hw": "180 $", "rec": "45 $/mes", "ai": "136 $/mes"
    },
    {
        "rank": 30, "country_es": "Kuwait", "country_local": "الكويت", "lang": "ar",
        "courts": 400, "curr_code": "KWD", "curr_symbol": "$", "slug": "kuwait", "slug_local": "kuwait",
        "hw": "$180 (55 KWD)", "rec": "$45/شهرياً (14 KWD)", "ai": "$136/شهرياً (42 KWD)"
    },
    {
        "rank": 31, "country_es": "Croacia", "country_local": "Hrvatska", "lang": "hr",
        "courts": 350, "curr_code": "EUR", "curr_symbol": "€", "slug": "croacia", "slug_local": "hrvatska",
        "hw": "180 €", "rec": "45 €/mjesec", "ai": "136 €/mjesec"
    },
    {
        "rank": 32, "country_es": "Indonesia", "country_local": "Indonesia", "lang": "id",
        "courts": 350, "curr_code": "IDR", "curr_symbol": "$", "slug": "indonesia", "slug_local": "indonesia",
        "hw": "$180 (Rp 2.9jt)", "rec": "$45/bln (Rp 720rb)", "ai": "$136/bln (Rp 2.2jt)"
    },
    {
        "rank": 33, "country_es": "Marruecos", "country_local": "Maroc", "lang": "fr",
        "courts": 300, "curr_code": "EUR", "curr_symbol": "€", "slug": "marruecos", "slug_local": "maroc",
        "hw": "180 € (1.950 DH)", "rec": "45 €/mois (490 DH)", "ai": "136 €/mois (1.480 DH)"
    },
    {
        "rank": 34, "country_es": "Irlanda", "country_local": "Ireland", "lang": "en",
        "courts": 300, "curr_code": "EUR", "curr_symbol": "€", "slug": "irlanda", "slug_local": "ireland",
        "hw": "€180", "rec": "€45/mo", "ai": "€136/mo"
    },
    {
        "rank": 35, "country_es": "Turquía", "country_local": "Türkiye", "lang": "tr",
        "courts": 250, "curr_code": "TRY", "curr_symbol": "$", "slug": "turquia", "slug_local": "turkiye",
        "hw": "$180 (6.500 ₺)", "rec": "$45/ay (1.600 ₺)", "ai": "$136/ay (4.900 ₺)"
    },
    {
        "rank": 36, "country_es": "Túnez", "country_local": "Tunisie", "lang": "fr",
        "courts": 250, "curr_code": "EUR", "curr_symbol": "€", "slug": "tunez", "slug_local": "tunisie",
        "hw": "180 € (600 DT)", "rec": "45 €/mois (150 DT)", "ai": "136 €/mois (450 DT)"
    },
    {
        "rank": 37, "country_es": "Uruguay", "country_local": "Uruguay", "lang": "es",
        "courts": 250, "curr_code": "UYU", "curr_symbol": "$", "slug": "uruguay", "slug_local": "uruguay",
        "hw": "180 $", "rec": "45 $/mes", "ai": "136 $/mes"
    },
    {
        "rank": 38, "country_es": "Venezuela", "country_local": "Venezuela", "lang": "es",
        "courts": 220, "curr_code": "VES", "curr_symbol": "$", "slug": "venezuela", "slug_local": "venezuela",
        "hw": "180 $", "rec": "45 $/mes", "ai": "136 $/mes"
    },
    {
        "rank": 39, "country_es": "Costa Rica", "country_local": "Costa Rica", "lang": "es",
        "courts": 200, "curr_code": "CRC", "curr_symbol": "$", "slug": "costa-rica", "slug_local": "costa-rica",
        "hw": "180 $", "rec": "45 $/mes", "ai": "136 $/mes"
    },
    {
        "rank": 40, "country_es": "República Dominicana", "country_local": "República Dominicana", "lang": "es",
        "courts": 200, "curr_code": "DOP", "curr_symbol": "$", "slug": "republica-dominicana", "slug_local": "republica-dominicana",
        "hw": "180 $", "rec": "45 $/mes", "ai": "136 $/mes"
    },
    {
        "rank": 41, "country_es": "Panamá", "country_local": "Panamá", "lang": "es",
        "courts": 180, "curr_code": "PAB", "curr_symbol": "$", "slug": "panama", "slug_local": "panama",
        "hw": "180 $", "rec": "45 $/mes", "ai": "136 $/mes"
    },
    {
        "rank": 42, "country_es": "Ecuador", "country_local": "Ecuador", "lang": "es",
        "courts": 180, "curr_code": "USD", "curr_symbol": "$", "slug": "ecuador", "slug_local": "ecuador",
        "hw": "180 $", "rec": "45 $/mes", "ai": "136 $/mes"
    },
    {
        "rank": 43, "country_es": "Australia", "country_local": "Australia", "lang": "en",
        "courts": 150, "curr_code": "AUD", "curr_symbol": "A$", "slug": "australia", "slug_local": "australia",
        "hw": "A$280 ($180)", "rec": "A$70/mo ($45)", "ai": "A$210/mo ($136)"
    },
    {
        "rank": 44, "country_es": "Japón", "country_local": "日本", "lang": "ja",
        "courts": 140, "curr_code": "JPY", "curr_symbol": "¥", "slug": "japon", "slug_local": "japan",
        "hw": "¥27,000 ($180)", "rec": "¥6,800/月 ($45)", "ai": "¥20,500/月 ($136)"
    },
    {
        "rank": 45, "country_es": "Líbano", "country_local": "لبنان", "lang": "ar",
        "courts": 130, "curr_code": "LBP", "curr_symbol": "$", "slug": "libano", "slug_local": "lebanon",
        "hw": "$180", "rec": "$45 / شهرياً", "ai": "$136 / شهرياً"
    },
    {
        "rank": 46, "country_es": "Bahréin", "country_local": "البحرين", "lang": "ar",
        "courts": 120, "curr_code": "BHD", "curr_symbol": "$", "slug": "bahrein", "slug_local": "bahrain",
        "hw": "$180 (68 BHD)", "rec": "$45/شهرياً (17 BHD)", "ai": "$136/شهرياً (51 BHD)"
    },
    {
        "rank": 47, "country_es": "Omán", "country_local": "عُمان", "lang": "ar",
        "courts": 100, "curr_code": "OMR", "curr_symbol": "$", "slug": "oman", "slug_local": "oman",
        "hw": "$180 (70 OMR)", "rec": "$45/شهرياً (17 OMR)", "ai": "$136/شهرياً (52 OMR)"
    },
    {
        "rank": 48, "country_es": "India", "country_local": "India", "lang": "en",
        "courts": 100, "curr_code": "INR", "curr_symbol": "₹", "slug": "india", "slug_local": "india",
        "hw": "₹15,000 ($180)", "rec": "₹3,800/mo ($45)", "ai": "₹11,500/mo ($136)"
    },
    {
        "rank": 49, "country_es": "República Checa", "country_local": "Česká republika", "lang": "cs",
        "courts": 90, "curr_code": "CZK", "curr_symbol": "Kč", "slug": "republica-checa", "slug_local": "ceska-republika",
        "hw": "4.500 Kč (180 €)", "rec": "1.130 Kč/měs (45 €)", "ai": "3.400 Kč/měs (136 €)"
    },
    {
        "rank": 50, "country_es": "Rumanía", "country_local": "România", "lang": "ro",
        "courts": 80, "curr_code": "RON", "curr_symbol": "lei", "slug": "rumania", "slug_local": "romania",
        "hw": "900 lei (180 €)", "rec": "225 lei/lună (45 €)", "ai": "680 lei/lună (136 €)"
    }
]
