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
        "hw": "$199 USD", "rec": "$49 USD/mes", "ai": "$150 USD/mes"
    },
    {
        "rank": 4, "country_es": "Suecia", "country_local": "Sverige", "lang": "sv",
        "courts": 4220, "curr_code": "SEK", "curr_symbol": "kr", "slug": "suecia", "slug_local": "sverige",
        "hw": "2.050 kr", "rec": "515 kr/mån", "ai": "1.550 kr/mån"
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
        "hw": "$3.950 MXN", "rec": "$990 MXN/mes", "ai": "$2.980 MXN/mes"
    },
    {
        "rank": 8, "country_es": "Chile", "country_local": "Chile", "lang": "es",
        "courts": 2300, "curr_code": "CLP", "curr_symbol": "$", "slug": "chile", "slug_local": "chile",
        "hw": "$190.000 CLP", "rec": "$47.500 CLP/mes", "ai": "$143.000 CLP/mes"
    },
    {
        "rank": 9, "country_es": "Bélgica", "country_local": "Belgique", "lang": "fr",
        "courts": 2150, "curr_code": "EUR", "curr_symbol": "€", "slug": "belgica", "slug_local": "belgique",
        "hw": "180 €", "rec": "45 €/mois", "ai": "136 €/mois"
    },
    {
        "rank": 10, "country_es": "Paraguay", "country_local": "Paraguay", "lang": "es",
        "courts": 2000, "curr_code": "PYG", "curr_symbol": "$", "slug": "paraguay", "slug_local": "paraguay",
        "hw": "Gs. 1.500.000", "rec": "Gs. 375.000/mes", "ai": "Gs. 1.130.000/mes"
    },
    {
        "rank": 11, "country_es": "Dinamarca", "country_local": "Danmark", "lang": "da",
        "courts": 1575, "curr_code": "DKK", "curr_symbol": "kr", "slug": "dinamarca", "slug_local": "danmark",
        "hw": "1.350 kr", "rec": "340 kr/md", "ai": "1.020 kr/md"
    },
    {
        "rank": 12, "country_es": "Portugal", "country_local": "Portugal", "lang": "pt",
        "courts": 1560, "curr_code": "EUR", "curr_symbol": "€", "slug": "portugal", "slug_local": "portugal",
        "hw": "180 €", "rec": "45 €/mês", "ai": "136 €/mês"
    },
    {
        "rank": 13, "country_es": "Egipto", "country_local": "مصر", "lang": "ar",
        "courts": 1500, "curr_code": "EGP", "curr_symbol": "$", "slug": "egipto", "slug_local": "egypt",
        "hw": "9.200 ج.م", "rec": "2.300 ج.م/شهرياً", "ai": "6.950 ج.م/شهرياً"
    },
    {
        "rank": 14, "country_es": "Sudáfrica", "country_local": "South Africa", "lang": "en",
        "courts": 1210, "curr_code": "ZAR", "curr_symbol": "R", "slug": "sudafrica", "slug_local": "south-africa",
        "hw": "R3,600", "rec": "R900/mo", "ai": "R2,700/mo"
    },
    {
        "rank": 15, "country_es": "Arabia Saudí", "country_local": "المملكة العربية السعودية", "lang": "ar",
        "courts": 1130, "curr_code": "SAR", "curr_symbol": "$", "slug": "arabia-saudi", "slug_local": "saudi-arabia",
        "hw": "750 ر.س", "rec": "185 ر.س/شهرياً", "ai": "565 ر.س/شهرياً"
    },
    {
        "rank": 16, "country_es": "Finlandia", "country_local": "Suomi", "lang": "fi",
        "courts": 1100, "curr_code": "EUR", "curr_symbol": "€", "slug": "finlandia", "slug_local": "suomi",
        "hw": "180 €", "rec": "45 €/kk", "ai": "136 €/kk"
    },
    {
        "rank": 17, "country_es": "Gran Bretaña", "country_local": "United Kingdom", "lang": "en",
        "courts": 1080, "curr_code": "GBP", "curr_symbol": "£", "slug": "gran-bretana", "slug_local": "united-kingdom",
        "hw": "£155", "rec": "£39/mo", "ai": "£118/mo"
    },
    {
        "rank": 18, "country_es": "Brasil", "country_local": "Brasil", "lang": "pt-br",
        "courts": 1000, "curr_code": "BRL", "curr_symbol": "R$", "slug": "brasil", "slug_local": "brasil",
        "hw": "R$ 1.150", "rec": "R$ 290/mês", "ai": "R$ 870/mês"
    },
    {
        "rank": 19, "country_es": "Emiratos Árabes Unidos", "country_local": "الإمارات العربية المتحدة", "lang": "ar",
        "courts": 950, "curr_code": "AED", "curr_symbol": "$", "slug": "emiratos-arabes-unidos", "slug_local": "uae",
        "hw": "730 AED", "rec": "180 AED/شهرياً", "ai": "550 AED/شهرياً"
    },
    {
        "rank": 20, "country_es": "Alemania", "country_local": "Deutschland", "lang": "de",
        "courts": 875, "curr_code": "EUR", "curr_symbol": "€", "slug": "alemania", "slug_local": "deutschland",
        "hw": "180 €", "rec": "45 €/Monat", "ai": "136 €/Monat"
    },
    {
        "rank": 21, "country_es": "Estados Unidos", "country_local": "United States", "lang": "en",
        "courts": 770, "curr_code": "USD", "curr_symbol": "$", "slug": "estados-unidos", "slug_local": "united-states",
        "hw": "$199", "rec": "$49/mo", "ai": "$150/mo"
    },
    {
        "rank": 22, "country_es": "Noruega", "country_local": "Norge", "lang": "no",
        "courts": 700, "curr_code": "NOK", "curr_symbol": "kr", "slug": "noruega", "slug_local": "norge",
        "hw": "2.100 kr", "rec": "530 kr/mnd", "ai": "1.600 kr/mnd"
    },
    {
        "rank": 23, "country_es": "Austria", "country_local": "Österreich", "lang": "de",
        "courts": 650, "curr_code": "EUR", "curr_symbol": "€", "slug": "austria", "slug_local": "oesterreich",
        "hw": "180 €", "rec": "45 €/Monat", "ai": "136 €/Monat"
    },
    {
        "rank": 24, "country_es": "Suiza", "country_local": "Schweiz", "lang": "de",
        "courts": 600, "curr_code": "CHF", "curr_symbol": "CHF", "slug": "suiza", "slug_local": "schweiz",
        "hw": "175 CHF", "rec": "44 CHF/Monat", "ai": "132 CHF/Monat"
    },
    {
        "rank": 25, "country_es": "Polonia", "country_local": "Polska", "lang": "pl",
        "courts": 550, "curr_code": "PLN", "curr_symbol": "zł", "slug": "polonia", "slug_local": "polska",
        "hw": "780 zł", "rec": "195 zł/mies.", "ai": "590 zł/mies."
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
        "hw": "725 QAR", "rec": "180 QAR/شهرياً", "ai": "545 QAR/شهرياً"
    },
    {
        "rank": 29, "country_es": "Colombia", "country_local": "Colombia", "lang": "es",
        "courts": 400, "curr_code": "COP", "curr_symbol": "$", "slug": "colombia", "slug_local": "colombia",
        "hw": "$790.000 COP", "rec": "$198.000 COP/mes", "ai": "$595.000 COP/mes"
    },
    {
        "rank": 30, "country_es": "Kuwait", "country_local": "الكويت", "lang": "ar",
        "courts": 400, "curr_code": "KWD", "curr_symbol": "$", "slug": "kuwait", "slug_local": "kuwait",
        "hw": "61 KWD", "rec": "15 KWD/شهرياً", "ai": "46 KWD/شهرياً"
    },
    {
        "rank": 31, "country_es": "Croacia", "country_local": "Hrvatska", "lang": "hr",
        "courts": 350, "curr_code": "EUR", "curr_symbol": "€", "slug": "croacia", "slug_local": "hrvatska",
        "hw": "180 €", "rec": "45 €/mjesec", "ai": "136 €/mjesec"
    },
    {
        "rank": 32, "country_es": "Indonesia", "country_local": "Indonesia", "lang": "id",
        "courts": 350, "curr_code": "IDR", "curr_symbol": "$", "slug": "indonesia", "slug_local": "indonesia",
        "hw": "Rp 3.6jt", "rec": "Rp 900rb/bln", "ai": "Rp 2.7jt/bln"
    },
    {
        "rank": 33, "country_es": "Marruecos", "country_local": "Maroc", "lang": "fr",
        "courts": 300, "curr_code": "EUR", "curr_symbol": "€", "slug": "marruecos", "slug_local": "maroc",
        "hw": "1.950 DH", "rec": "490 DH/mois", "ai": "1.480 DH/mois"
    },
    {
        "rank": 34, "country_es": "Irlanda", "country_local": "Ireland", "lang": "en",
        "courts": 300, "curr_code": "EUR", "curr_symbol": "€", "slug": "irlanda", "slug_local": "ireland",
        "hw": "€180", "rec": "€45/mo", "ai": "€136/mo"
    },
    {
        "rank": 35, "country_es": "Turquía", "country_local": "Türkiye", "lang": "tr",
        "courts": 250, "curr_code": "TRY", "curr_symbol": "$", "slug": "turquia", "slug_local": "turkiye",
        "hw": "10.000 ₺", "rec": "2.500 ₺/ay", "ai": "7.550 ₺/ay"
    },
    {
        "rank": 36, "country_es": "Túnez", "country_local": "Tunisie", "lang": "fr",
        "courts": 250, "curr_code": "EUR", "curr_symbol": "€", "slug": "tunez", "slug_local": "tunisie",
        "hw": "600 DT", "rec": "150 DT/mois", "ai": "450 DT/mois"
    },
    {
        "rank": 37, "country_es": "Uruguay", "country_local": "Uruguay", "lang": "es",
        "courts": 250, "curr_code": "UYU", "curr_symbol": "$", "slug": "uruguay", "slug_local": "uruguay",
        "hw": "$8.300 UYU", "rec": "$2.080 UYU/mes", "ai": "$6.250 UYU/mes"
    },
    {
        "rank": 38, "country_es": "Venezuela", "country_local": "Venezuela", "lang": "es",
        "courts": 220, "curr_code": "VES", "curr_symbol": "$", "slug": "venezuela", "slug_local": "venezuela",
        "hw": "199 USD", "rec": "49 USD/mes", "ai": "150 USD/mes"
    },
    {
        "rank": 39, "country_es": "Costa Rica", "country_local": "Costa Rica", "lang": "es",
        "courts": 200, "curr_code": "CRC", "curr_symbol": "$", "slug": "costa-rica", "slug_local": "costa-rica",
        "hw": "₡102.000", "rec": "₡25.500/mes", "ai": "₡77.000/mes"
    },
    {
        "rank": 40, "country_es": "República Dominicana", "country_local": "República Dominicana", "lang": "es",
        "courts": 200, "curr_code": "DOP", "curr_symbol": "$", "slug": "republica-dominicana", "slug_local": "republica-dominicana",
        "hw": "RD$ 12.000", "rec": "RD$ 3.000/mes", "ai": "RD$ 9.100/mes"
    },
    {
        "rank": 41, "country_es": "Panamá", "country_local": "Panamá", "lang": "es",
        "courts": 180, "curr_code": "PAB", "curr_symbol": "$", "slug": "panama", "slug_local": "panama",
        "hw": "199 USD", "rec": "49 USD/mes", "ai": "150 USD/mes"
    },
    {
        "rank": 42, "country_es": "Ecuador", "country_local": "Ecuador", "lang": "es",
        "courts": 180, "curr_code": "USD", "curr_symbol": "$", "slug": "ecuador", "slug_local": "ecuador",
        "hw": "199 USD", "rec": "49 USD/mes", "ai": "150 USD/mes"
    },
    {
        "rank": 43, "country_es": "Australia", "country_local": "Australia", "lang": "en",
        "courts": 150, "curr_code": "AUD", "curr_symbol": "A$", "slug": "australia", "slug_local": "australia",
        "hw": "A$295", "rec": "A$74/mo", "ai": "A$220/mo"
    },
    {
        "rank": 44, "country_es": "Japón", "country_local": "日本", "lang": "ja",
        "courts": 140, "curr_code": "JPY", "curr_symbol": "¥", "slug": "japon", "slug_local": "japan",
        "hw": "¥31.700", "rec": "¥7.900/月", "ai": "¥23.900/月"
    },
    {
        "rank": 45, "country_es": "Líbano", "country_local": "لبنان", "lang": "ar",
        "courts": 130, "curr_code": "LBP", "curr_symbol": "$", "slug": "libano", "slug_local": "lebanon",
        "hw": "$199 USD", "rec": "$49 USD/شهرياً", "ai": "$150 USD/شهرياً"
    },
    {
        "rank": 46, "country_es": "Bahréin", "country_local": "البحرين", "lang": "ar",
        "courts": 120, "curr_code": "BHD", "curr_symbol": "$", "slug": "bahrein", "slug_local": "bahrain",
        "hw": "75 BHD", "rec": "18.5 BHD/شهرياً", "ai": "56.5 BHD/شهرياً"
    },
    {
        "rank": 47, "country_es": "Omán", "country_local": "عُمان", "lang": "ar",
        "courts": 100, "curr_code": "OMR", "curr_symbol": "$", "slug": "oman", "slug_local": "oman",
        "hw": "77 OMR", "rec": "19 OMR/شهرياً", "ai": "58 OMR/شهرياً"
    },
    {
        "rank": 48, "country_es": "India", "country_local": "India", "lang": "en",
        "courts": 100, "curr_code": "INR", "curr_symbol": "₹", "slug": "india", "slug_local": "india",
        "hw": "₹18.641", "rec": "₹4.660/mo", "ai": "₹14.084/mo"
    },
    {
        "rank": 49, "country_es": "República Checa", "country_local": "Česká republika", "lang": "cs",
        "courts": 90, "curr_code": "CZK", "curr_symbol": "Kč", "slug": "republica-checa", "slug_local": "ceska-republika",
        "hw": "4.500 Kč", "rec": "1.130 Kč/měs", "ai": "3.400 Kč/měs"
    },
    {
        "rank": 50, "country_es": "Rumanía", "country_local": "România", "lang": "ro",
        "courts": 80, "curr_code": "RON", "curr_symbol": "lei", "slug": "rumania", "slug_local": "romania",
        "hw": "900 lei", "rec": "225 lei/lună", "ai": "680 lei/lună"
    }
]
