# -*- coding: utf-8 -*-
"""
dataset_scraper_new.py
Nuevas cadenas multiclub y franquicias de pádel (+1 club abierto con la misma marca)
descubiertas a partir de la auditoría de directorios de federaciones oficiales
(FEP, FPP, FEMEPA, EasyCancha, KNLTB, FITP, DPV, Padel Nordics, TenUp FFT y Playtomic).
"""

# =========================================================================
# 🇬🇧 REINO UNIDO E IRLANDA (Nuevos descubrimientos verificados)
# =========================================================================
NEW_UK_LIST = [
    {
        "id": "surge-padel",
        "nombre": "Surge Padel",
        "pais": "Reino Unido",
        "pais_codigo": "GB",
        "region_filtro": "GB",
        "bandera": "🇬🇧",
        "ciudad_sede": "Harrogate / Bristol / Cheshire",
        "coords": [53.9921, -1.5418],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "3 centros flagship en UK",
        "num_pistas": "17+ pistas indoor",
        "software": "Playtomic",
        "fundadores": "Stuart Perrins & Alistair Brown",
        "web": "https://surgepadel.co.uk",
        "tagline": "Complejos cubiertos premium con pistas Adidas panorámicas y bar deportivo en Inglaterra.",
        "resumen": "Surge Padel opera centros indoor de gran escala en Harrogate (6 pistas), Bristol Fishponds (8 pistas) y Fairmont The Mere en Cheshire, ofreciendo vestuarios de lujo, tienda pro-shop, bar cafetería y academias oficiales LTA.",
        "sedes_principales": [
            "Surge Padel Harrogate (Hornbeam Park)",
            "Surge Padel Bristol (Fishponds)",
            "Surge Padel Cheshire (Fairmont The Mere)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas Adidas Indoor con césped monofilamento texturizado",
            "software": "Playtomic",
            "domotica": "Iluminación LED de competición y climatización para invierno británico",
            "grabacion": "Cámaras en pista para ligas y streaming",
            "restauracion": "Sports Lounge bar con cerveza artesanal, batidos y cafetería"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios e inversión directa en naves comerciales",
            "perfil_club": "Naves industriales y parques comerciales de 2.000 a 4.000 m²",
            "canon_royalties": "Operación directa",
            "inversion_media": "600.000£ a 1.200.000£ por centro"
        },
        "diferencial": "Instalaciones cubiertas de altura reglamentaria pensadas para jugar los 365 días del año sin depender del clima británico."
    },
    {
        "id": "true-padel-uk",
        "nombre": "True Padel",
        "pais": "Reino Unido",
        "pais_codigo": "GB",
        "region_filtro": "GB",
        "bandera": "🇬🇧",
        "ciudad_sede": "Durham / Sunderland (North East)",
        "coords": [54.7761, -1.5733],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 macrocomplejos indoor",
        "num_pistas": "20 pistas cubiertas",
        "software": "Playtomic",
        "fundadores": "True Padel Sports Group",
        "web": "https://truepadel.co.uk",
        "tagline": "El gigante del pádel indoor en el noreste británico con 20 pistas y heated lounge.",
        "resumen": "True Padel es la referencia del pádel en el norte de Inglaterra con dos megacentros: True Padel Durham (9 pistas panorámicas en New Ferens Park) y True Padel Sunderland (11 pistas mixtas en Thomsen Retail Park), con lounge climatizado, ligas LTA y eventos corporativos.",
        "sedes_principales": [
            "True Padel Durham (Belmont Industrial Estate, New Ferens Park - 9 pistas)",
            "True Padel Sunderland (Thomsen Retail Park - 11 pistas)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de competición con cristal de 12 mm y césped texturizado",
            "software": "Playtomic",
            "domotica": "Control domótico de acceso, taquillas electrónicas y climatización",
            "grabacion": "Sistemas de videoanálisis para clases y ligas",
            "restauracion": "Heated sports lounge & bar, cafetería y pro-shop completa"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios en retail parks y parques logísticos",
            "perfil_club": "Naves de gran volumen con más de 8 pistas",
            "canon_royalties": "Operación directa",
            "inversion_media": "750.000£ a 1.500.000£ por instalación"
        },
        "diferencial": "Macrocomplejos con el mayor número de pistas bajo techo de todo el norte de Inglaterra."
    },
    {
        "id": "david-lloyd-padel",
        "nombre": "David Lloyd Clubs Padel",
        "pais": "Reino Unido",
        "pais_codigo": "GB",
        "region_filtro": "GB",
        "bandera": "🇬🇧",
        "ciudad_sede": "Londres / Mánchester / Birmingham",
        "coords": [51.4080, -0.2370],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "gran_operador",
        "num_clubs": "35+ clubes con pádel en UK",
        "num_pistas": "100+ pistas",
        "software": "David Lloyd App Propietaria",
        "fundadores": "David Lloyd Leisure Group",
        "web": "https://www.davidlloyd.co.uk/sports/padel/",
        "tagline": "La mayor red de salud y raqueta del Reino Unido integrando pádel premium en sus clubes.",
        "resumen": "David Lloyd Leisure, el operador líder europeo de clubes de fitness y raqueta, ha desplegado más de 100 pistas de pádel en más de 35 complejos británicos (Raynes Park, Cheadle, Chigwell, Bristol, Milton Keynes, Finchley, etc.), con instructores certificados, ligas sociales y zonas spa.",
        "sedes_principales": [
            "David Lloyd Raynes Park (Londres)",
            "David Lloyd Cheadle (Mánchester)",
            "David Lloyd Chigwell (Essex)",
            "David Lloyd Bristol Westbury",
            "David Lloyd Milton Keynes",
            "David Lloyd Finchley"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas y cubiertas con cubierta estacional retráctil",
            "software": "David Lloyd App (reserva para socios e invitados)",
            "domotica": "Iluminación LED sincronizada con reservas del club",
            "grabacion": "Pistas con cámaras para academias junior y torneos",
            "restauracion": "Clubroom restaurante, terrazas solárium, spa y piscina"
        },
        "modelo_expansion": {
            "tipo_contrato": "Implantación directa en sus propios clubes premium de socios",
            "perfil_club": "Clubs de salud con piscina, tenis, fitness y pádel",
            "canon_royalties": "Operación directa corporativa",
            "inversion_media": "Inversión de capital multimillonaria en su red europea"
        },
        "diferencial": "Sinergia insuperable entre raqueta, bienestar, spa, restauración y comunidad de socios de alto poder adquisitivo."
    },
    {
        "id": "house-of-padel-ireland",
        "nombre": "House of Padel (HOP)",
        "pais": "Irlanda",
        "pais_codigo": "IE",
        "region_filtro": "GB",
        "bandera": "🇮🇪",
        "ciudad_sede": "Dublín (Cookstown / Belgard)",
        "coords": [53.2950, -6.3750],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 sedes en Dublín y expansión",
        "num_pistas": "12+ pistas indoor",
        "software": "Playtomic",
        "fundadores": "House of Padel Ireland Ltd",
        "web": "https://houseofpadel.co",
        "tagline": "El club indoor de pádel y bienestar boutique de referencia en Dublín.",
        "resumen": "House of Padel combina pistas panorámicas indoor de competición con zonas de recuperación activa (sauna nórdica de madera, baños de agua helada ice-bath), café de especialidad y la primera pista indoor de pickleball de Dublín en Cookstown Industrial Estate.",
        "sedes_principales": [
            "House of Padel Cookstown (Old Belgard Rd, Dublín)",
            "House of Padel South Dublin (Próxima apertura)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de calidad World Padel Tour techadas y aisladas térmicamente",
            "software": "Playtomic",
            "domotica": "Acceso QR, taquillas electrónicas y reserva de recuperación integrada",
            "grabacion": "Cámaras inteligentes para repeticiones de puntos y eventos corporativos",
            "restauracion": "Espresso bar de especialidad, zumos cold-pressed y zona lounge"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios boutique",
            "perfil_club": "Naves de techos altos en cinturones empresariales y deportivos",
            "canon_royalties": "Operación directa",
            "inversion_media": "600.000€ a 1.100.000€ por club"
        },
        "diferencial": "Concepto híbrido de pádel de élite con zona de recovery y baños fríos único en Irlanda."
    }
]

# =========================================================================
# 🇸🇪 ESCANDINAVIA Y NÓRDICOS (Nuevos descubrimientos del Scraper)
# =========================================================================
NEW_NORDIC_LIST = [
    {
        "id": "nordic-wellness-padel",
        "nombre": "Nordic Wellness Padel",
        "pais": "Suecia",
        "pais_codigo": "SE",
        "region_filtro": "SE",
        "bandera": "🇸🇪",
        "ciudad_sede": "Gotemburgo / Estocolmo",
        "coords": [57.7089, 11.9746],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "25+ centros con pádel en Suecia",
        "num_pistas": "120+ pistas cubiertas",
        "software": "Matchi / Nordic Wellness App",
        "fundadores": "Magnus Wilhelmsson (Nordic Wellness Group)",
        "web": "https://nordicwellness.se",
        "tagline": "La mayor cadena de gimnasios de Suecia con más de 25 complejos de pádel integrados.",
        "resumen": "Nordic Wellness es uno de los mayores operadores de fitness y deporte de los países nórdicos (+300 gimnasios). Ha integrado naves cubiertas de pádel bajo su marca en Örnsköldsvik, Timrå, Gävle Valbo, Gotemburgo, Halmstad y Malmö, con tarifas unificadas para sus abonados.",
        "sedes_principales": [
            "Nordic Wellness Örnsköldsvik Padel",
            "Nordic Wellness Timrå Padel",
            "Nordic Wellness Gävle Valbo Padel",
            "Nordic Wellness Gotemburgo",
            "Nordic Wellness Halmstad y Malmö"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas cubiertas en complejos con fitness de última generación",
            "software": "Matchi y App Nordic Wellness",
            "domotica": "Acceso integrado con pulsera de socio y tornos inteligentes",
            "grabacion": "Sistemas de vídeo en torneos locales",
            "restauracion": "Batidos de proteínas, comida fitness, spa y sauna sueca"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios dentro de la red corporativa de fitness",
            "perfil_club": "Macrocomplejos de 3.000m² a 6.000m²",
            "canon_royalties": "Operación directa",
            "inversion_media": "1.000.000€ a 2.500.000€ por centro"
        },
        "diferencial": "Base cautiva de cientos de miles de socios de fitness que llenan las pistas a diario."
    },
    {
        "id": "we-love-padel-se",
        "nombre": "We Love Padel",
        "pais": "Suecia",
        "pais_codigo": "SE",
        "region_filtro": "SE",
        "bandera": "🇸🇪",
        "ciudad_sede": "Helsingborg / Skövde",
        "coords": [56.0465, 12.6945],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "6 centros en Suecia",
        "num_pistas": "30+ pistas cubiertas",
        "software": "Matchi",
        "fundadores": "We Love Padel Sweden",
        "web": "https://welovepadel.se",
        "tagline": "Pistas cubiertas luminosas con diseño y ambiente social en el sur sueco.",
        "resumen": "Cadena que opera en Helsingborg, Skövde Commerce, Kristinehamn y comarcas del sur sueco, con pistas panorámicas de competición y ligas de Americano muy activas.",
        "sedes_principales": [
            "We Love Padel Helsingborg",
            "We Love Padel Skövde Commerce",
            "We Love Padel Kristinehamns GK"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de 10 metros de altura libre",
            "software": "Matchi",
            "domotica": "Acceso QR y taquillas electrónicas",
            "grabacion": "Vídeo en pista para análisis",
            "restauracion": "Lounge café nórdico y tienda de palas"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios",
            "perfil_club": "Naves industriales",
            "canon_royalties": "Operación directa",
            "inversion_media": "600.000€ a 1.200.000€"
        },
        "diferencial": "Ambiente de club muy cercano y dinamización continua de torneos amateur."
    },
    {
        "id": "pro-padel-norway",
        "nombre": "Pro Padel Norway",
        "pais": "Noruega",
        "pais_codigo": "NO",
        "region_filtro": "SE",
        "bandera": "🇳🇴",
        "ciudad_sede": "Bergen (Paradis / Åsane / Askøy)",
        "coords": [60.3913, 5.3221],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "3 centros en Vestland",
        "num_pistas": "18+ pistas cubiertas",
        "software": "Matchi",
        "fundadores": "Pro Padel AS",
        "web": "https://propadel.no",
        "tagline": "La cadena multiclub de referencia en los fiordos de Bergen y la costa oeste noruega.",
        "resumen": "Pro Padel opera tres macrocentros cubiertos en el área de Bergen (Paradis, Åsane y Askøy), proporcionando pistas de alta gama resguardadas del clima lluvioso de la costa atlántica noruega.",
        "sedes_principales": [
            "Pro Padel Paradis (Bergen)",
            "Pro Padel Åsane",
            "Pro Padel Askøy"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas de competición panorámicas con moqueta azul y calefacción",
            "software": "Matchi",
            "domotica": "Acceso automatizado por app",
            "grabacion": "Cámaras en torneos",
            "restauracion": "Clubhouse escandinavo y tienda de palas"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios en Vestland",
            "perfil_club": "Naves de 2.000m² a 3.500m²",
            "canon_royalties": "Operación directa",
            "inversion_media": "800.000€ a 1.500.000€"
        },
        "diferencial": "Dominio absoluto del mercado de Bergen y alta fidelidad de jugadores locales."
    },
    {
        "id": "vamoz-padel-dk",
        "nombre": "Vamoz Padel",
        "pais": "Dinamarca",
        "pais_codigo": "DK",
        "region_filtro": "SE",
        "bandera": "🇩🇰",
        "ciudad_sede": "Copenhague (DTU / Field's / Fisketorvet)",
        "coords": [55.6761, 12.5683],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "3 centros urbanos",
        "num_pistas": "16+ pistas",
        "software": "Matchi",
        "fundadores": "Vamoz Padel Denmark",
        "web": "https://vamozpadel.dk",
        "tagline": "Pistas urbanas integradas en centros comerciales y campus universitarios de Copenhague.",
        "resumen": "Cadena danesa con centros en localizaciones de tráfico masivo: en la Universidad Técnica de Dinamarca (DTU), en el centro comercial Field's y en el centro comercial Fisketorvet de Copenhague.",
        "sedes_principales": [
            "Vamoz Padel DTU Science Park",
            "Vamoz Padel Field's Shopping Center",
            "Vamoz Padel Fisketorvet"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas en azoteas y pabellones comerciales",
            "software": "Matchi",
            "domotica": "Acceso digital automatizado",
            "grabacion": "Vídeo en torneos",
            "restauracion": "Sinergia con la restauración del centro comercial"
        },
        "modelo_expansion": {
            "tipo_contrato": "Alianzas de retailtainment en superficies comerciales",
            "perfil_club": "Centros comerciales y campus",
            "canon_royalties": "Operación directa",
            "inversion_media": "400.000€ a 850.000€"
        },
        "diferencial": "Flujo peatonal incesante en los mayores centros comerciales de Copenhague."
    },
    {
        "id": "suomen-ulkopadel",
        "nombre": "Suomen Ulkopadel",
        "pais": "Finlandia",
        "pais_codigo": "FI",
        "region_filtro": "SE",
        "bandera": "🇫🇮",
        "ciudad_sede": "Lohja / Hamina / Tammisaari",
        "coords": [60.2500, 24.0667],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "4 centros en Finlandia",
        "num_pistas": "16+ pistas",
        "software": "Playtomic / Padelution",
        "fundadores": "Suomen Ulkopadel Oy",
        "web": "https://ulkopadel.fi",
        "tagline": "Pistas exteriores de alta resistencia para el verano finlandés en lagos y costas.",
        "resumen": "Cadena finlandesa especializada en pistas al aire libre en entornos naturales y costeros (Lohja, Hamina, Tammisaari), donde los jugadores aprovechan las largas horas de luz solar del verano nórdico.",
        "sedes_principales": [
            "Suomen Ulkopadel Lohja",
            "Suomen Ulkopadel Hamina",
            "Suomen Ulkopadel Tammisaari"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas exteriores tratadas para resistir nieve y hielo en invierno",
            "software": "Playtomic",
            "domotica": "Acceso QR",
            "grabacion": "Vídeo de torneos de verano",
            "restauracion": "Kiosco de verano y café"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios en municipios turísticos finlandeses",
            "perfil_club": "Zonas de recreo lacustres",
            "canon_royalties": "Operación directa",
            "inversion_media": "200.000€ a 450.000€"
        },
        "diferencial": "El encanto de jugar bajo el 'sol de medianoche' junto a los lagos de Finlandia."
    },
    {
        "id": "bueno-padel-fi",
        "nombre": "Bueno Padel",
        "pais": "Finlandia",
        "pais_codigo": "FI",
        "region_filtro": "SE",
        "bandera": "🇫🇮",
        "ciudad_sede": "Ostrobotnia (Seinäjoki / Kurikka)",
        "coords": [62.7900, 22.8400],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "3 centros cubiertos",
        "num_pistas": "14+ pistas",
        "software": "Playtomic",
        "fundadores": "Bueno Padel Oy",
        "web": "https://buenopadel.fi",
        "tagline": "Pádel cubierto y climatizado en la región de Ostrobotnia del Sur.",
        "resumen": "Cadena de naves industriales climatizadas en Kauhajoki, Kurikka y Seinäjoki que ofrece un refugio deportivo con pistas panorámicas y sauna para la comunidad local.",
        "sedes_principales": [
            "Bueno Padel Seinäjoki",
            "Bueno Padel Kurikka",
            "Bueno Padel Kauhajoki"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas en naves aisladas térmicamente",
            "software": "Playtomic",
            "domotica": "Acceso automatizado",
            "grabacion": "Vídeo en pista",
            "restauracion": "Sauna en vestuarios y autoservicio"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios",
            "perfil_club": "Naves de 1.500m² a 2.500m²",
            "canon_royalties": "Operación directa",
            "inversion_media": "450.000€ a 850.000€"
        },
        "diferencial": "Presencia destacada en el oeste finlandés con instalaciones a prueba del frío."
    }
]

# =========================================================================
# 🇩🇪 AUSTRIA Y DACH (Nuevos descubrimientos del Scraper)
# =========================================================================
NEW_DACH_LIST = [
    {
        "id": "padelbase-austria",
        "nombre": "PADELBASE",
        "pais": "Austria",
        "pais_codigo": "AT",
        "region_filtro": "DE",
        "bandera": "🇦🇹",
        "ciudad_sede": "Viena / Linz",
        "coords": [48.2082, 16.3738],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "9 centros en Austria",
        "num_pistas": "40+ pistas",
        "software": "Playtomic",
        "fundadores": "PADELBASE Austria GmbH",
        "web": "https://padelbase.at",
        "tagline": "La gran red multiclub austríaca con presencia en Viena y la Alta Austria.",
        "resumen": "PADELBASE opera 9 complejos cubiertos y mixtos bajo la misma enseña en Viena (Marswiese), Neunkirchen (PiNK), Linz (Halle, Kleinmünchen y Pichling) y Salzburgo, con escuelas juveniles y ligas de fin de semana.",
        "sedes_principales": [
            "PADELBASE Wien Marswiese",
            "PADELBASE PiNK Neunkirchen",
            "PADELBASE Linz Halle",
            "PADELBASE Linz Pichling",
            "PADELBASE Linz Kleinmünchen"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de calidad de torneo con moqueta azul",
            "software": "Playtomic",
            "domotica": "Acceso QR y taquillas electrónicas",
            "grabacion": "Cámaras en torneos austríacos",
            "restauracion": "Clubhouse con cerveza austríaca, café y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios y concesiones",
            "perfil_club": "Naves de 1.800 a 3.500 m²",
            "canon_royalties": "Operación directa",
            "inversion_media": "600.000€ a 1.200.000€ por club"
        },
        "diferencial": "El principal competidor de PadelZone en Viena y el dominador absoluto del pádel en Linz."
    },
    {
        "id": "padel4fun-austria",
        "nombre": "Padel4Fun",
        "pais": "Austria",
        "pais_codigo": "AT",
        "region_filtro": "DE",
        "bandera": "🇦🇹",
        "ciudad_sede": "Viena / Baden / Tattendorf",
        "coords": [48.0050, 16.2300],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "4 centros en Baja Austria y Viena",
        "num_pistas": "16+ pistas",
        "software": "Playtomic",
        "fundadores": "Padel4Fun Sportverein",
        "web": "https://padel4fun.at",
        "tagline": "Clubes sociales familiares en la región termal y vinícola al sur de Viena.",
        "resumen": "Cadena de referencia en la comarca de Baden y el sur vienés (La Ville Wien, Baden, Tattendorf), combinando pádel con tenis y eventos gastronómicos entre viñedos.",
        "sedes_principales": [
            "Padel4Fun La Ville Wien",
            "Padel4Fun Baden",
            "Padel4Fun Tattendorf"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de cristal templado",
            "software": "Playtomic",
            "domotica": "Acceso digital",
            "grabacion": "Vídeo en torneos",
            "restauracion": "Terrazas vinícolas con gastronomía Heuriger austríaca"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios",
            "perfil_club": "Clubes de tenis tradicionales",
            "canon_royalties": "Operación directa",
            "inversion_media": "350.000€ a 700.000€"
        },
        "diferencial": "Ambiente de club social vinícola (Heuriger) muy entrañable y relajado."
    },
    {
        "id": "tapedesign-padel",
        "nombre": "Tapedesign Padelcenter",
        "pais": "Austria",
        "pais_codigo": "AT",
        "region_filtro": "DE",
        "bandera": "🇦🇹",
        "ciudad_sede": "Graz / Viena / Leoben",
        "coords": [47.0707, 15.4395],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "3 macrocentros",
        "num_pistas": "18+ pistas",
        "software": "Playtomic",
        "fundadores": "Tapedesign Sports (marca de calcetines antideslizantes usada por futbolistas)",
        "web": "https://tapedesign-padel.at",
        "tagline": "Complejos de competición nacidos de la marca de calcetines técnicos de la Champions League.",
        "resumen": "Creados por los fundadores de Tapedesign (los calcetines antideslizantes usados por futbolistas profesionales de todo el mundo), operan centros de gran nivel en Graz Messe (recinto ferial), Viena y Leoben.",
        "sedes_principales": [
            "Tapedesign Padelcenter Graz Messe",
            "Tapedesign Padelcenter Wien",
            "Tapedesign Padelcenter Leoben"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas oficiales con césped de máxima amortiguación",
            "software": "Playtomic",
            "domotica": "Acceso QR automatizado",
            "grabacion": "Streaming de torneos austríacos",
            "restauracion": "Sports bar y pro-shop Tapedesign"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros corporativos de marca",
            "perfil_club": "Recintos feriales y naves industriales",
            "canon_royalties": "Operación directa",
            "inversion_media": "700.000€ a 1.400.000€"
        },
        "diferencial": "Conexión directa con futbolistas profesionales austríacos y recintos feriales céntricos."
    }
]

# =========================================================================
# 🇧🇪 BÉLGICA (Nuevos descubrimientos del Scraper)
# =========================================================================
NEW_BENELUX_LIST = [
    {
        "id": "tero-padel",
        "nombre": "Tero Padel",
        "pais": "Bélgica",
        "pais_codigo": "BE",
        "region_filtro": "NL",
        "bandera": "🇧🇪",
        "ciudad_sede": "Waterloo / Bruselas / Limelette",
        "coords": [50.7147, 4.3997],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "6 clubes en Valonia y Bruselas",
        "num_pistas": "35+ pistas",
        "software": "Playtomic",
        "fundadores": "Tero Group (Arthur Dupuis & socios de hospitalidad)",
        "web": "https://tero.be",
        "tagline": "El concepto de hostelería sostenible y pádel premium del prestigioso Grupo Tero.",
        "resumen": "Tero Padel es la división deportiva del célebre grupo hostelero y corporativo belga Tero. Cuenta con instalaciones de gran nivel en Waterloo, Avenue Louise (Bruselas centro), Limelette y Charleroi, combinando pistas de pádel con restaurantes de cocina de granja a la mesa (farm-to-table) y centros de eventos de empresas.",
        "sedes_principales": [
            "Tero Padel Waterloo (8 pistas: cubiertas y exteriores)",
            "Tero Padel Louise (Bruselas intramuros)",
            "Tero Padel Limelette (antiguo club de tenis Justine Henin)",
            "Tero Padel Club Charleroi"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de competición con cristal de 12mm y moqueta azul",
            "software": "Playtomic",
            "domotica": "Acceso digital automatizado",
            "grabacion": "Pistas con cámaras para eventos corporativos",
            "restauracion": "Restaurantes de autor de la cadena Tero, huerto ecológico y salas de reuniones de empresa"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena propia de centros integrados de deporte, gastronomía y eventos",
            "perfil_club": "Fincas históricas y country clubs en el Brabante Valón y Bruselas",
            "canon_royalties": "Operación directa",
            "inversion_media": "1.200.000€ a 3.000.000€ por club"
        },
        "diferencial": "La gastronomía ecológica de primer nivel mundial y los eventos corporativos de empresas belgas y europeas."
    }
]

# =========================================================================
# 🇵🇹 PORTUGAL (Nuevos descubrimientos del Scraper)
# =========================================================================
NEW_PT_LIST = [
    {
        "id": "quinta-de-monserrate",
        "nombre": "Quinta de Monserrate",
        "pais": "Portugal",
        "pais_codigo": "PT",
        "region_filtro": "PT",
        "bandera": "🇵🇹",
        "ciudad_sede": "Oporto / Matosinhos / Braga",
        "coords": [41.1800, -8.6900],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "6 complejos de prestigio",
        "num_pistas": "38+ pistas",
        "software": "AirCourts / Playtomic",
        "fundadores": "Quinta de Monserrate Padel Group",
        "web": "https://quintademonserrate.com",
        "tagline": "La aristocracia del pádel en el norte de Portugal: Oporto Parque, Indoor y Braga.",
        "resumen": "Quinta de Monserrate es uno de los operadores más respetados de Portugal. Creado en asociación con el centenario Sport Club do Porto, opera complejos emblemáticos en Matosinhos (Parque da Cidade), nave indoor de Oporto y Braga, con una escuela de élite que nutre la selección portuguesa.",
        "sedes_principales": [
            "Quinta de Monserrate Parque (Oporto / Matosinhos junto al Parque da Cidade)",
            "Quinta de Monserrate Indoor (Oporto)",
            "Quinta de Monserrate Braga (Sport Club do Porto)",
            "Quinta de Monserrate Norte"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de cristal templado con cubiertas de diseño y exteriores",
            "software": "AirCourts y Playtomic",
            "domotica": "Acceso inteligente digital",
            "grabacion": "Sistemas para streaming de torneos de la FPP",
            "restauracion": "Clubhouse señorial con restaurante, terraza y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios y alianzas con clubes históricos",
            "perfil_club": "Suelos emblemáticos en el Gran Oporto",
            "canon_royalties": "Operación directa",
            "inversion_media": "800.000€ a 1.800.000€"
        },
        "diferencial": "El prestigio histórico de la marca y su ubicación junto al Parque da Cidade de Oporto."
    },
    {
        "id": "arena-playsports",
        "nombre": "Arena PlaySports",
        "pais": "Portugal",
        "pais_codigo": "PT",
        "region_filtro": "PT",
        "bandera": "🇵🇹",
        "ciudad_sede": "Lisboa (Alcântara / Alvalade / Belém)",
        "coords": [38.7071, -9.1764],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "14 complejos en el Gran Lisboa",
        "num_pistas": "50+ pistas",
        "software": "AirCourts / Playtomic",
        "fundadores": "PlaySports Portugal",
        "web": "https://playsports.pt",
        "tagline": "La red con mayor densidad de pistas de Lisboa: Alcântara, Alfragide, Alvalade y Belém.",
        "resumen": "Cadena que opera en los distritos más poblados de Lisboa con pistas panorámicas de última generación en Alcântara, Alfragide, Alvalade, Portela y Belém, siendo el corazón de las ligas de empresas y aficionados lisboetas.",
        "sedes_principales": [
            "Arena PlaySports Alcântara (junto al puente 25 de Abril)",
            "Arena PlaySports Alvalade",
            "Arena PlaySports Belém",
            "Arena PlaySports Alfragide y Portela"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas de competición con nuevo césped monofilamento azul",
            "software": "AirCourts",
            "domotica": "Acceso QR y reservas inmediatas",
            "grabacion": "Vídeo en ligas sociales",
            "restauracion": "Bares deportivos, terraza y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios y concesiones",
            "perfil_club": "Suelos urbanos de fácil acceso en Lisboa",
            "canon_royalties": "Operación directa",
            "inversion_media": "450.000€ a 1.000.000€ por centro"
        },
        "diferencial": "Densidad de centros insuperable en la capital portuguesa: siempre hay una pista a 10 minutos."
    },
    {
        "id": "az-padel-pt",
        "nombre": "A-Z Padel",
        "pais": "Portugal",
        "pais_codigo": "PT",
        "region_filtro": "PT",
        "bandera": "🇵🇹",
        "ciudad_sede": "Sintra / Barcelos / Famalicão",
        "coords": [38.8000, -9.3800],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "5 centros",
        "num_pistas": "25+ pistas",
        "software": "AirCourts",
        "fundadores": "A-Z Padel Group",
        "web": "https://azpadel.pt",
        "tagline": "Pistas cubiertas de alto rendimiento de norte a sur de Portugal.",
        "resumen": "Cadena con centros en Sintra, Barcelos (Elite), Tejo y Vila Nova de Famalicão, destacando por sus naves cubiertas y escuelas de competición federada.",
        "sedes_principales": [
            "A-Z Padel Sintra",
            "A-Z Padel Elite Barcelos",
            "A-Z Padel Tejo",
            "A-Z Padel Famalicão"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas cubiertas",
            "software": "AirCourts",
            "domotica": "Acceso inteligente",
            "grabacion": "Vídeo en torneos",
            "restauracion": "Cafetería y tienda especializada"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios",
            "perfil_club": "Naves industriales",
            "canon_royalties": "Operación directa",
            "inversion_media": "500.000€ a 1.000.000€"
        },
        "diferencial": "Capacidad técnica y cobertura multirregional en Portugal."
    }
]

# =========================================================================
# 🇲🇽 LATINOAMÉRICA (Nuevos descubrimientos del Scraper)
# =========================================================================
NEW_LATAM_LIST = [
    {
        "id": "mundo-padel-mx",
        "nombre": "Mundo Pádel México",
        "pais": "México",
        "pais_codigo": "MX",
        "region_filtro": "MX",
        "bandera": "🇲🇽",
        "ciudad_sede": "Ciudad de México (Acoxpa / Coapa / Lomas Verdes)",
        "coords": [19.2980, -99.1350],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "5 clubes en CDMX y Edomex",
        "num_pistas": "28+ pistas",
        "software": "Playtomic",
        "fundadores": "Mundo Pádel Group",
        "web": "https://mundopadel.com.mx",
        "tagline": "La cadena multiclub más popular del sur y poniente del Valle de México.",
        "resumen": "Mundo Pádel opera cinco centros muy concurridos en el Valle de México: Acoxpa, CB Sport Lomas Verdes, Coapa, Conscripto y Narvarte, combinando torneos nocturnos multitudinarios con clínicas para principiantes.",
        "sedes_principales": [
            "Mundo Pádel Acoxpa (Sur de CDMX)",
            "Mundo Pádel CB Sport Lomas Verdes (Naucalpan)",
            "Mundo Pádel Coapa",
            "Mundo Pádel Conscripto",
            "Mundo Pádel Narvarte"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con césped texturizado de competición",
            "software": "Playtomic",
            "domotica": "Acceso QR y control de luces",
            "grabacion": "Cámaras en torneos locales",
            "restauracion": "Terraza taquería, cerveza mexicana y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios urbanos",
            "perfil_club": "Parcelas y naves en barrios residenciales densos",
            "canon_royalties": "Operación directa",
            "inversion_media": "500.000$ a 1.100.000$ por club"
        },
        "diferencial": "Gran popularidad y accesibilidad en las zonas residenciales más pobladas de la capital mexicana."
    },
    {
        "id": "glass-cube-mx",
        "nombre": "Glass Cube Padel Center",
        "pais": "México",
        "pais_codigo": "MX",
        "region_filtro": "MX",
        "bandera": "🇲🇽",
        "ciudad_sede": "Querétaro (Constituyentes / Juriquilla)",
        "coords": [20.5888, -100.3899],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 macrocentros en Querétaro",
        "num_pistas": "16+ pistas",
        "software": "Playtomic",
        "fundadores": "Glass Cube Sports",
        "web": "https://glasscubepadel.com",
        "tagline": "El cubo de cristal del pádel de competición en el pujante Bajío mexicano.",
        "resumen": "Cadena con centros en Constituyentes y Juriquilla (Querétaro), con pistas panorámicas de última generación, césped monofilamento y una academia con entrenadores argentinos de renombre.",
        "sedes_principales": [
            "Glass Cube Constituyentes (Querétaro)",
            "Glass Cube Juriquilla"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de cristal templado de 12mm",
            "software": "Playtomic",
            "domotica": "Acceso digital",
            "grabacion": "Vídeo en torneos federados",
            "restauracion": "Restaurante bar y tienda deportiva"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios",
            "perfil_club": "Parcelas comerciales en Querétaro",
            "canon_royalties": "Operación directa",
            "inversion_media": "600.000$ a 1.200.000$"
        },
        "diferencial": "Referente de competición y diseño en una de las ciudades con mayor crecimiento económico de México."
    },
    {
        "id": "padel-house-chile",
        "nombre": "Padel House Chile",
        "pais": "Chile",
        "pais_codigo": "CL",
        "region_filtro": "MX",
        "bandera": "🇨🇱",
        "ciudad_sede": "Santiago / Puertecillo / Villarrica",
        "coords": [-33.4800, -70.5200],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "3 clubes en Chile",
        "num_pistas": "18+ pistas",
        "software": "EasyCanchas",
        "fundadores": "Padel House Chile SpA",
        "web": "https://padelhouse.cl",
        "tagline": "Pádel social y de surf en Santiago, Puertecillo y los lagos de Villarrica.",
        "resumen": "Cadena con centros en Las Pircas (Santiago), el famoso spot de surf de Puertecillo y la zona lacustre de Villarrica, combinando deporte de raqueta y turismo al aire libre.",
        "sedes_principales": [
            "Padel House Las Pircas (Santiago Peñalolén)",
            "Padel House Puertecillo (Costa del surf)",
            "Padel House Villarrica (Región de la Araucanía)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas all-weather",
            "software": "EasyCanchas",
            "domotica": "Acceso QR",
            "grabacion": "Vídeo en torneos",
            "restauracion": "Quincho cervecero, comida orgánica y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios en destinos turísticos y urbanos",
            "perfil_club": "Parcelas con entorno natural",
            "canon_royalties": "Operación directa",
            "inversion_media": "350.000$ a 750.000$"
        },
        "diferencial": "La fusión perfecta entre la cultura del surf, la naturaleza chilena y el pádel."
    },
    {
        "id": "speed-padel-chile",
        "nombre": "Speed Padel Chile",
        "pais": "Chile",
        "pais_codigo": "CL",
        "region_filtro": "MX",
        "bandera": "🇨🇱",
        "ciudad_sede": "Santiago (Almirante / Los Cóndores)",
        "coords": [-33.4400, -70.6500],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 centros en Santiago",
        "num_pistas": "14+ pistas",
        "software": "EasyCanchas",
        "fundadores": "Speed Padel Chile",
        "web": "https://speedpadel.cl",
        "tagline": "Pádel dinámico y ligas rápidas en el área urbana de Santiago.",
        "resumen": "Cadena que opera en Sede Almirante y Sede Los Cóndores en Santiago, con formatos de juego ágiles y torneos Americano diarios.",
        "sedes_principales": [
            "Speed Padel Sede Almirante",
            "Speed Padel Sede Los Cóndores"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas de cristal templado",
            "software": "EasyCanchas",
            "domotica": "Acceso digital",
            "grabacion": "Vídeo en torneos",
            "restauracion": "Bar terraza y snacks"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios",
            "perfil_club": "Parcelas deportivas urbanas",
            "canon_royalties": "Operación directa",
            "inversion_media": "300.000$ a 600.000$"
        },
        "diferencial": "Rotación ágil de partidos y ligas muy dinámicas para jugadores activos."
    }
]

# =========================================================================
# 🇿🇦 SUDÁFRICA Y EUROPA (Nuevos descubrimientos del Scraper)
# =========================================================================
NEW_WORLD_LIST = [
    {
        "id": "techno-padel-za",
        "nombre": "Techno Padel",
        "pais": "Sudáfrica",
        "pais_codigo": "ZA",
        "region_filtro": "ZA",
        "bandera": "🇿🇦",
        "ciudad_sede": "Gauteng / Western Cape",
        "coords": [-26.2041, 28.0473],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "5 clubes en Sudáfrica",
        "num_pistas": "20+ pistas",
        "software": "Playtomic",
        "fundadores": "Techno Padel South Africa",
        "web": "https://technopadel.co.za",
        "tagline": "Pistas panorámicas integradas en clubes de golf y resorts históricos sudafricanos.",
        "resumen": "Cadena que ha instalado centros de pádel de gran éxito en clubes de golf y hoteles emblemáticos: Avion Park, ERPM Golf Club, Heidelberg, el histórico Houw Hoek Hotel y Middelburg Country Club.",
        "sedes_principales": [
            "Techno Padel ERPM Golf Club (Boksburg)",
            "Techno Padel Avion Park",
            "Techno Padel Houw Hoek Hotel (Western Cape)",
            "Techno Padel Heidelberg",
            "Techno Padel Middelburg Country Club"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas all-weather con césped texturizado",
            "software": "Playtomic",
            "domotica": "Acceso digital",
            "grabacion": "Cámaras en torneos",
            "restauracion": "Clubhouse de golf, asados sudafricanos (braai) y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Alianzas en clubes de golf y resorts",
            "perfil_club": "Country clubs y resorts de lujo",
            "canon_royalties": "Operación directa",
            "inversion_media": "350.000$ a 750.000$"
        },
        "diferencial": "Instalaciones en el entorno relajado de los mejores campos de golf de Sudáfrica."
    },
    {
        "id": "vamos-padel-eu",
        "nombre": "Vamos Padel",
        "pais": "Alemania",
        "pais_codigo": "DE",
        "region_filtro": "DE",
        "bandera": "🇩🇪",
        "ciudad_sede": "Leipzig / Milán (Cimiano / Corsico)",
        "coords": [51.3397, 12.3731],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "4 centros en Alemania e Italia",
        "num_pistas": "18+ pistas",
        "software": "Playtomic",
        "fundadores": "Vamos Padel International",
        "web": "https://vamospadel.de",
        "tagline": "Pádel cubierto internacional conectando Leipzig con los clubes de Milán.",
        "resumen": "Cadena con presencia transfronteriza en Alemania (Leipzig y Bassum) e Italia (Milán Cimiano y Corsico), combinando naves cubiertas con escuelas dirigidas por entrenadores hispanohablantes.",
        "sedes_principales": [
            "Vamos Padel Club Leipzig",
            "Vamos Padel Bassum",
            "Vamos Padel Cimiano (Milán)",
            "Vamos Padel Corsico"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas cubiertas climatizadas",
            "software": "Playtomic",
            "domotica": "Acceso QR autónomo",
            "grabacion": "Vídeo en torneos",
            "restauracion": "Biergarten y cafetería italiana"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios",
            "perfil_club": "Naves industriales",
            "canon_royalties": "Operación directa",
            "inversion_media": "550.000€ a 1.100.000€"
        },
        "diferencial": "Operación binacional en los dos mercados de mayor crecimiento de Europa continental (Alemania e Italia)."
    }
]

if __name__ == "__main__":
    print(f"[OK] Cargadas {len(NEW_UK_LIST)} cadenas nuevas de UK/IE, {len(NEW_NORDIC_LIST)} nordicas, {len(NEW_DACH_LIST)} DACH, {len(NEW_BENELUX_LIST)} Benelux, {len(NEW_PT_LIST)} Portugal, {len(NEW_LATAM_LIST)} Latam, {len(NEW_WORLD_LIST)} Mundo.")

