# -*- coding: utf-8 -*-
"""
dataset_expansion_new.py
Nuevas 14 cadenas y franquicias de pádel (+1 club abierto con la misma marca)
verificadas a través de auditoría internacional en artículos especializados,
directorios de federaciones y plataformas de reservas (Playtomic, MATCHi).
"""

EXPANSION_OPERATORS = [
    # 1. Padel4all (Reino Unido)
    {
        "id": "padel-4-all-uk",
        "nombre": "Padel4all",
        "pais": "Reino Unido",
        "pais_codigo": "GB",
        "region_filtro": "GB",
        "bandera": "🇬🇧",
        "ciudad_sede": "Swindon / Bristol / Bracknell",
        "coords": [51.5280, -1.8250],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "5 centros cubiertos",
        "num_pistas": "18+ pistas con cubierta tensada",
        "software": "Playtomic",
        "fundadores": "Christopher Wilkinson (Padel4all Ltd)",
        "web": "https://padel4all.com",
        "tagline": "Pioneros del pádel comunitario cubierto all-weather en el sur y suroeste de Inglaterra.",
        "resumen": "Padel4all desarrolla centros deportivos comunitarios con cubiertas textiles climatizadas y pistas panorámicas de última generación en Swindon (Basset Down), Bristol (Lockleaze Sports Centre), Southend (Garon Park), Bracknell y Eastbourne.",
        "sedes_principales": [
            "Padel4all Basset Down (Swindon, Wiltshire)",
            "Padel4all Lockleaze Sports Centre (North Bristol)",
            "Padel4all Garon Park (Southend-on-Sea)",
            "Padel4all Bracknell",
            "Padel4all Eastbourne (The Saffrons)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con cubierta textil tensada para lluvia y viento con césped texturizado WPT",
            "software": "Playtomic",
            "domotica": "Acceso QR automatizado, iluminación LED inteligente e integración con ligas LTA",
            "grabacion": "Sistemas de vídeo en pistas centrales para torneos",
            "restauracion": "Clubhouse café, pro-shop especializada y zona social con terraza"
        },
        "modelo_expansion": {
            "tipo_contrato": "Alianzas de suelo con clubes deportivos y complejos comunitarios",
            "perfil_club": "Parcelas deportivas y campos de golf de 3 a 6 pistas",
            "canon_royalties": "Operación directa y revenue share con propietarios de suelo",
            "inversion_media": "350.000£ a 750.000£ por centro"
        },
        "diferencial": "Especialistas en transformar suelo infrautilizado en campos de golf y clubes deportivos en centros cubiertos de pádel altamente rentables."
    },

    # 2. Padelprix (España - Galicia)
    {
        "id": "padelprix-galicia",
        "nombre": "Padelprix",
        "pais": "España",
        "pais_codigo": "ES",
        "region_filtro": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Ourense / A Coruña / Santiago",
        "coords": [42.3358, -7.8639],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "3 macrocomplejos indoor",
        "num_pistas": "26 pistas cubiertas de cristal",
        "software": "Playtomic",
        "fundadores": "Grupo Padelprix Galicia",
        "web": "https://www.padelprix.com",
        "tagline": "La mayor red de pádel indoor de Galicia con 26 pistas de cristal y gimnasio integrado.",
        "resumen": "Padelprix es el operador de referencia del pádel en Galicia, con megacentros en el Polígono San Cibrao das Viñas de Ourense (9 pistas), Arteixo A Coruña junto a Marineda City (11 pistas) y el Polígono Costa Vella de Santiago de Compostela (6 pistas).",
        "sedes_principales": [
            "Padelprix Ourense (San Cibrao das Viñas - 9 pistas indoor)",
            "Padelprix Coruña (Polígono de Barreiros, Arteixo - 11 pistas indoor)",
            "Padelprix Santiago (Polígono Costa Vella - 6 pistas indoor)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de cristal templado indoor con césped monofilamento WPT",
            "software": "Playtomic",
            "domotica": "Control domótico de iluminación LED, climatización nave y taquillas electrónicas",
            "grabacion": "Cámaras para torneos autonómicos y streaming",
            "restauracion": "Terraza cafetería de más de 600 m², gimnasio con entrenadores personales y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios en naves logísticas e industriales de gran volumen",
            "perfil_club": "Naves de más de 3.000 m² con techos altos en polígonos periurbanos gallegos",
            "canon_royalties": "Operación directa",
            "inversion_media": "650.000€ a 1.250.000€ por macrocomplejo"
        },
        "diferencial": "Macrocomplejos protegidos de la climatología gallega con servicios 360º (gimnasio, restauración de gran escala y academias federadas)."
    },

    # 3. Máis que Auga Padel (España - Vigo)
    {
        "id": "mais-que-auga-vigo",
        "nombre": "Máis que Auga Padel",
        "pais": "España",
        "pais_codigo": "ES",
        "region_filtro": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Vigo (Pontevedra)",
        "coords": [42.2150, -8.7650],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 macrocentros de raqueta y salud",
        "num_pistas": "17 pistas cubiertas (12m altura)",
        "software": "Playtomic / App Propia MQA",
        "fundadores": "Máis que Auga Concesiones Deportivas",
        "web": "https://maisqueauga.com/padel/",
        "tagline": "Pistas cubiertas con 12 metros de altura libre en los mayores complejos deportivos de Vigo.",
        "resumen": "Máis que Auga opera dos de las instalaciones cubiertas de pádel más espectaculares del noroeste peninsular: Navia (8 pistas panorámicas con césped WPT) y Barreiro Lavadores (9 pistas cubiertas), con metodología propia Padelglobal, spa urbano, fitness y torneos federados.",
        "sedes_principales": [
            "Máis que Auga Navia (Vigo - 8 pistas cubiertas)",
            "Máis que Auga Barreiro (Lavadores, Vigo - 9 pistas cubiertas)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas cubiertas bajo naves deportivas de 12 metros de altura libre",
            "software": "Playtomic y App de abonados Máis que Auga",
            "domotica": "Acceso por tornos biométricos y pulsera RFID, domótica de luz por reserva",
            "grabacion": "Grabación de partidos en pistas centrales",
            "restauracion": "Cafetería-restaurante, spa balneario urbano, piscinas y zona de hidroterapia"
        },
        "modelo_expansion": {
            "tipo_contrato": "Concesiones público-privadas e inversión en complejos integrales de salud",
            "perfil_club": "Centros polideportivos premium con fitness, agua y pádel",
            "canon_royalties": "Operación directa",
            "inversion_media": "1.500.000€ a 3.500.000€ por complejo completo"
        },
        "diferencial": "Complejos deportivos municipales de gran lujo que combinan pádel de altura profesional con balneario, spa y fitness de élite."
    },

    # 4. PadelShot (Francia)
    {
        "id": "padelshot-france",
        "nombre": "PadelShot",
        "pais": "Francia",
        "pais_codigo": "FR",
        "region_filtro": "FR",
        "bandera": "🇫🇷",
        "ciudad_sede": "Caen / Metz / Saint-Étienne / Lyon",
        "coords": [49.1828, -0.3707],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "4 macrocomplejos indoor",
        "num_pistas": "30+ pistas cubiertas",
        "software": "Playtomic",
        "fundadores": "Jérôme Doligé (PadelShot Group)",
        "web": "https://padelshot.fr",
        "tagline": "Macrocomplejos cubiertos con restaurante 'The Shot', billar y pistas de 10 metros de altura en Francia.",
        "resumen": "PadelShot es una de las redes indoor más dinámicas de Francia, con clubes de gran volumen en Caen (Normandía), Metz Woippy (10 pistas en el Grand Est), Saint-Étienne junto al estadio Geoffroy-Guichard (8 pistas) y Lyon Craponne.",
        "sedes_principales": [
            "PadelShot Caen (Mondeville - 8 pistas dobles e individuales)",
            "PadelShot Metz (Woippy, Parc des Varimonts - 10 pistas)",
            "PadelShot Saint-Étienne (8 pistas cubiertas)",
            "PadelShot Lyon Craponne"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con altura libre de 10 metros y moqueta texturizada azul",
            "software": "Playtomic",
            "domotica": "Acceso QR, pantallas digitales de marcadores y taquillas electrónicas",
            "grabacion": "Cámaras en pista para torneos oficiales FFT P25/P100/P250",
            "restauracion": "Concepto 'The Shot': lounge bar con pizzas artesanales, cervezas locales, billar y ping-pong"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios e inversión en parques de ocio comercial",
            "perfil_club": "Naves comerciales de más de 2.500 m² con parking abundante",
            "canon_royalties": "Operación directa",
            "inversion_media": "750.000€ a 1.400.000€ por club"
        },
        "diferencial": "Fusión de pádel de alta competición con espacios 'After-Work' de ocio y restauración de calidad superior."
    },

    # 5. Padel Hero (Italia)
    {
        "id": "padel-hero-italy",
        "nombre": "Padel Hero",
        "pais": "Italia",
        "pais_codigo": "IT",
        "region_filtro": "IT",
        "bandera": "🇮🇹",
        "ciudad_sede": "Pisa / Versilia / Parma",
        "coords": [43.7228, 10.4017],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "3 clubes premium",
        "num_pistas": "22 pistas indoor y outdoor",
        "software": "Playtomic",
        "fundadores": "Padel Hero Italia S.r.l.",
        "web": "https://padelhero.com",
        "tagline": "La red de clubes de pádel lifestyle y alto rendimiento en Toscana y Emilia-Romaña.",
        "resumen": "Padel Hero destaca por instalaciones de gran diseño en Pisa (10 pistas: 6 outdoor y 4 indoor con bar-bistró), Padel Hero Versilia en Marina di Pietrasanta y Parma, ofreciendo academias para niños y adultos y torneos FITP.",
        "sedes_principales": [
            "Padel Hero Pisa (Via Tiziano Vecellio - 10 pistas)",
            "Padel Hero Versilia (Marina di Pietrasanta)",
            "Padel Hero Parma"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas italianas de cristal templado 12mm y focos LED antirreflejo",
            "software": "Playtomic",
            "domotica": "Reserva automatizada y control de luz sincronizado",
            "grabacion": "Sistemas de vídeo y streaming para competiciones oficiales",
            "restauracion": "Risto-bar italiano con cócteles, desayunos, ensaladas bio y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios y franquicias en el centro y norte de Italia",
            "perfil_club": "Parcelas deportivas y naves en zonas de alto poder adquisitivo",
            "canon_royalties": "Franchise fee 20.000€ + royalty mensual 5%",
            "inversion_media": "500.000€ a 1.100.000€ por club"
        },
        "diferencial": "Diseño italiano de vanguardia, hospitality gastronómica de primer nivel y fuerte presencia en la costa toscana."
    },

    # 6. GARRINCHA Padel (Bélgica)
    {
        "id": "garrincha-belgium",
        "nombre": "GARRINCHA",
        "pais": "Bélgica",
        "pais_codigo": "BE",
        "region_filtro": "NL",
        "bandera": "🇧🇪",
        "ciudad_sede": "Bruselas / Gante / Amberes",
        "coords": [50.8503, 4.3517],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "6 centros urbanos",
        "num_pistas": "35+ pistas cubiertas y outdoor",
        "software": "Playtomic",
        "fundadores": "GARRINCHA Urban Sports Group",
        "web": "https://garrincha.be",
        "tagline": "El gigante belga de los centros deportivos urbanos con techos de 11 metros y Matchi.tv.",
        "resumen": "GARRINCHA opera macrocentros de pádel urbano y fútbol en Bélgica: Diegem junto al aeropuerto de Bruselas (11 pistas: 7 indoor de 11m de altura y 4 outdoor), Gante The Loop (11 pistas), Amberes Sur Hoboken (4 pistas indoor), Amberes Norte y Dilbeek.",
        "sedes_principales": [
            "GARRINCHA Brussels Diegem (11 pistas: 7 indoor + 4 outdoor)",
            "GARRINCHA Ghent - The Loop (11 pistas con 11m de altura)",
            "GARRINCHA Antwerp South (Hoboken - 4 pistas indoor)",
            "GARRINCHA Antwerp North",
            "GARRINCHA Westgate Dilbeek (Rooftop padel)",
            "GARRINCHA Ghent Arsenaal"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con alturas libres récord de 11 metros sin obstáculos",
            "software": "Playtomic",
            "domotica": "Acceso QR, control de iluminación y taquillas inteligentes",
            "grabacion": "Sistemas de repetición de puntos en vídeo integrados con Matchi.tv",
            "restauracion": "Sports Bar con cervezas artesanales belgas, comida sana, terraza soleada y co-working"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios de gran escala en nudos de comunicación",
            "perfil_club": "Naves de más de 3.500 m² en áreas metropolitanas de Flandes y Bruselas",
            "canon_royalties": "Operación directa",
            "inversion_media": "1.000.000€ a 2.200.000€ por centro"
        },
        "diferencial": "Complejos multideporte de techo altísimo (11m) que atraen a corporate events y empresas tecnológicas de Bruselas."
    },

    # 7. PadelCity (Alemania)
    {
        "id": "padelcity-germany",
        "nombre": "PadelCity",
        "pais": "Alemania",
        "pais_codigo": "DE",
        "region_filtro": "DE",
        "bandera": "🇩🇪",
        "ciudad_sede": "Múnich / Dortmund / Leipzig",
        "coords": [48.1351, 11.5820],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "4 macrocentros en Alemania",
        "num_pistas": "26 pistas indoor y outdoor",
        "software": "Playtomic / App Propia PadelCity",
        "fundadores": "Padel City GmbH (Múnich)",
        "web": "https://padelcity.de",
        "tagline": "La cadena alemana de macrocomplejos multideporte y pádel en los principales motores económicos germanos.",
        "resumen": "PadelCity es una de las mayores cadenas de pádel de Alemania, con sede en Múnich. Destaca por PadelCity Dortmund junto al estadio Signal Iduna Park (12 pistas: 6 indoor y 6 outdoor con fútbol indoor y yoga), Múnich Tucherpark (7 pistas outdoor) y Leipzig Alt-West (7 pistas).",
        "sedes_principales": [
            "PadelCity Dortmund (12 pistas: 6 indoor + 6 outdoor)",
            "PadelCity München (Tucherpark - 7 pistas)",
            "PadelCity Leipzig (Alt-West - 7 pistas: 4 indoor + 3 outdoor)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de competición con cristal de 12 mm y césped texturizado",
            "software": "Playtomic y App PadelCity, integrado con Urban Sports Club",
            "domotica": "Acceso QR automatizado y luces LED sincronizadas",
            "grabacion": "Pistas con cámaras para torneos oficiales DPV",
            "restauracion": "Biergarten y restaurante italiano con pizzas caseras, pro-shop y lounge"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios y alianzas con centros deportivos y parques urbanos",
            "perfil_club": "Naves industriales y parques deportivos de 2.500 a 5.000 m²",
            "canon_royalties": "Operación directa",
            "inversion_media": "800.000€ a 1.600.000€ por club"
        },
        "diferencial": "Implantación en las ciudades alemanas de mayor renta per cápita, integrando pádel con ligas de empresas y gimnasios."
    },

    # 8. Padelta (Suiza)
    {
        "id": "padelta-switzerland",
        "nombre": "Padelta",
        "pais": "Suiza",
        "pais_codigo": "CH",
        "region_filtro": "DE",
        "bandera": "🇨🇭",
        "ciudad_sede": "Zúrich / Lucerna / Zug / Berna",
        "coords": [47.3769, 8.5417],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "gran_operador",
        "num_clubs": "12 complejos en Suiza",
        "num_pistas": "50+ pistas de alta gama",
        "software": "Playtomic",
        "fundadores": "Padelta AG (Suiza)",
        "web": "https://padelta.ch",
        "tagline": "El operador número 1 y pionero del pádel en Suiza con más de 12 centros y la Padelta Academy.",
        "resumen": "Padelta es el líder indiscutible del mercado suizo de raqueta. Cuenta con centros de vanguardia en Zúrich Milandia Greifensee (5 pistas indoor, golf y bistró), Lucerna (Rothenburg, Dierikon, Kriens, Emmen), Zug/Baar, Baden (6 pistas), Thun/Uetendorf, Solothurn Biberist (8 pistas) y Chur.",
        "sedes_principales": [
            "Padelta Zürich Milandia (Greifensee - 5 pistas indoor)",
            "Padelta Solothurn / Biberist (8 pistas cubiertas)",
            "Padelta Baden (6 pistas)",
            "Padelta Rothenburg (Lucerna - 5 pistas)",
            "Padelta Zug / Baar (The Padel Club Zug)",
            "Padelta Thun / Uetendorf (5 pistas)",
            "Padelta Chur (Graubünden)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de precisión suiza con cristales acústicos especiales y césped premium",
            "software": "Playtomic y Padelta Winter Pass / Bandeja Card",
            "domotica": "Acceso 100% desatendido mediante app, domótica de clima y taquillas electrónicas",
            "grabacion": "Cámaras inteligentes en pista para alumnos de la Padelta Academy",
            "restauracion": "Bistró suizo con café de especialidad, bebidas isotónicas orgánicas y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios y alianzas con centros de ocio y fitness suizos",
            "perfil_club": "Naves de altura reglamentaria en los principales cantones suizos",
            "canon_royalties": "Operación directa corporativa",
            "inversion_media": "1.200.000 CHF a 2.500.000 CHF por centro"
        },
        "diferencial": "Liderazgo absoluto en el mercado de mayor poder adquisitivo del mundo, con una red unificada mediante el pase nacional Padelta."
    },

    # 9. Taktika Padel (Estados Unidos - California)
    {
        "id": "taktika-padel-california",
        "nombre": "Taktika Padel",
        "pais": "Estados Unidos",
        "pais_codigo": "US",
        "region_filtro": "US",
        "bandera": "🇺🇸",
        "ciudad_sede": "San Diego / Los Ángeles (Carson)",
        "coords": [32.7157, -117.1611],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "3 clubes en California",
        "num_pistas": "16+ pistas panorámicas",
        "software": "Playtomic / PlayByPoint",
        "fundadores": "Gabriel Pérez Krieb, Armando Rodiel & Ryan Redondo",
        "web": "https://taktikapadel.com",
        "tagline": "La cadena líder del sur de California asociada con LA Galaxy y Barnes Tennis Center.",
        "resumen": "Taktika Padel lidera la expansión del pádel en la costa oeste norteamericana con clubes icónicos: Barnes Tennis Center en San Diego (7 pistas panorámicas de fibra de carbono), Dignity Health Sports Park / Galaxy Park en Los Ángeles Carson junto al estadio de la MLS, y Palm Desert.",
        "sedes_principales": [
            "Taktika Padel San Diego (Barnes Tennis Center, Point Loma - 7 pistas)",
            "Taktika Padel Los Angeles (Dignity Health Sports Park / LA Galaxy, Carson)",
            "Taktika Padel Palm Desert"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas all-weather de carbono diseñadas para el clima californiano",
            "software": "Playtomic / PlayByPoint",
            "domotica": "Iluminación LED de nivel profesional para juego nocturno y tornos digitales",
            "grabacion": "Pistas centrales con retransmisión streaming para torneos USPA",
            "restauracion": "Clubhouse café, zona de pro-shop con equipamiento oficial y lounge exterior"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios y alianzas exclusivas con franquicias deportivas de la MLS/AEG",
            "perfil_club": "Grandes parques deportivos e instalaciones universitarias en California",
            "canon_royalties": "Operación directa",
            "inversion_media": "600.000$ a 1.500.000$ por instalación"
        },
        "diferencial": "Alianza estratégica pionera con AEG y LA Galaxy para introducir pádel en los recintos de las grandes ligas estadounidenses."
    },

    # 10. Park Padel (Estados Unidos - San Francisco)
    {
        "id": "park-padel-california",
        "nombre": "Park Padel",
        "pais": "Estados Unidos",
        "pais_codigo": "US",
        "region_filtro": "US",
        "bandera": "🇺🇸",
        "ciudad_sede": "San Francisco (Embarcadero / Oyster Point)",
        "coords": [37.7749, -122.4194],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 clubes en el Área de la Bahía",
        "num_pistas": "9 pistas indoor y outdoor",
        "software": "Playtomic",
        "fundadores": "Jessica Wan, Neil Mehta & Katie Lampert",
        "web": "https://parkpadel.com",
        "tagline": "Pistas icónicas en el Embarcadero frente a la Bahía de San Francisco y nave cubierta en Silicon Valley.",
        "resumen": "Park Padel introdujo el pádel en el corazón de Silicon Valley y San Francisco con dos sedes emblemáticas: las famosas pistas exteriores de Embarcadero Plaza con vistas al Ferry Building y al puente de la bahía, y su megacentro indoor cubierto en South San Francisco Oyster Point.",
        "sedes_principales": [
            "Park Padel Embarcadero Plaza (Waterfront, San Francisco)",
            "Park Padel Oyster Point (South San Francisco - Indoor)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de cristal de 12mm con iluminación LED de alta potencia y césped de torneo",
            "software": "Playtomic",
            "domotica": "Acceso inteligente por app y reservas de iluminación sincronizadas",
            "grabacion": "Sistemas de vídeo para partidos sociales y ligas de startups",
            "restauracion": "Snack-bar con bebidas locales, café de especialidad y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios e intervenciones en espacios públicos urbanos emblemáticos",
            "perfil_club": "Plazas públicas de alta visibilidad y naves logísticas en el Área de la Bahía",
            "canon_royalties": "Operación directa",
            "inversion_media": "500.000$ a 1.200.000$ por sede"
        },
        "diferencial": "Comunidad de alto perfil con miles de fundadores, ingenieros y ejecutivos tecnológicos de San Francisco y Silicon Valley."
    },

    # 11. Padel Park MX (México)
    {
        "id": "padel-park-mexico",
        "nombre": "Padel Park MX",
        "pais": "México",
        "pais_codigo": "MX",
        "region_filtro": "MX",
        "bandera": "🇲🇽",
        "ciudad_sede": "Monterrey / Guadalajara",
        "coords": [25.6866, -100.3161],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 macrocomplejos boutique",
        "num_pistas": "10 pistas de lujo techadas",
        "software": "Playtomic",
        "fundadores": "Padel Park México Group",
        "web": "https://www.instagram.com/padelparkmty/",
        "tagline": "Clubes techados y climatizados de súper lujo en San Pedro Garza García y Zapopan.",
        "resumen": "Padel Park MX opera dos de las instalaciones cubiertas más exclusivas de México: Padel Park Indoor en Monterrey (Prolongación Río Nazas, San Pedro Garza García) con 5 canchas panorámicas climatizadas, vapor y restaurante gourmet, y Padel Park Zona Real en Zapopan Guadalajara.",
        "sedes_principales": [
            "Padel Park Indoor Monterrey (San Pedro Garza García - 5 canchas techadas)",
            "Padel Park Zona Real (Zapopan, Guadalajara - 5 canchas techadas)"
        ],
        "tecnologia_pistas": {
            "pistas": "Canchas panorámicas de última generación bajo nave climatizada para combatir el calor mexicano",
            "software": "Playtomic",
            "domotica": "Control digital de acceso, climatización inteligente y taquillas electrónicas",
            "grabacion": "Cámaras en pista para torneos del circuito nacional mexicano",
            "restauracion": "Restaurante-bar de alta gama, vestidores de mármol con vapor y pro-shop boutique"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios e inversión directa en zonas residenciales de ultra-lujo",
            "perfil_club": "Complejos cubiertos con estacionamiento subterráneo y hospitality de hotel 5 estrellas",
            "canon_royalties": "Operación directa",
            "inversion_media": "800.000$ a 1.800.000$ por club"
        },
        "diferencial": "Experiencia premium VIP con climatización integral, vestidores con spa/vapor y restauración en las zonas más ricas de México."
    },

    # 12. Padel Rush (Arabia Saudí)
    {
        "id": "padel-rush-saudi",
        "nombre": "Padel Rush",
        "pais": "Arabia Saudí",
        "pais_codigo": "SA",
        "region_filtro": "AE",
        "bandera": "🇸🇦",
        "ciudad_sede": "Riad (Boulevard Riyadh City)",
        "coords": [24.7136, 46.6753],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 macroarenas en Riad",
        "num_pistas": "15+ pistas de competición",
        "software": "Playtomic",
        "fundadores": "Padel Rush Sports Investment (KSA)",
        "web": "https://padelrush.sa",
        "tagline": "La sede oficial del Riyadh Season Premier Padel P1 en Boulevard Riyadh City.",
        "resumen": "Padel Rush es el epicentro del pádel profesional en el Reino de Arabia Saudí. Su sede principal en Boulevard Riyadh City cuenta con 11 pistas de competición indoor y outdoor donde compiten las estrellas del Premier Padel, complementado con pro-shop de lujo y cafeterías gourmet.",
        "sedes_principales": [
            "Padel Rush Arena (Boulevard Riyadh City, Hittin District - 11 pistas)",
            "Padel Rush North Riyadh"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas World Padel Tour de cristal blindado y césped monofilamento azul oficial",
            "software": "Playtomic",
            "domotica": "Iluminación de televisión HD de 1.200 lux y control de acceso digital",
            "grabacion": "Sistemas de televisión y cámaras de streaming multicámara en todas las pistas",
            "restauracion": "Specialty coffee lounge, zumos naturales y pro-shop con marcas globales de pala"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros insignia vinculados a megaproyectos de entretenimiento de la Visión 2030 saudí",
            "perfil_club": "Macroarenas de pádel y raqueta en bulevares comerciales de gran afluencia",
            "canon_royalties": "Operación directa",
            "inversion_media": "1.500.000$ a 3.500.000$ por instalación"
        },
        "diferencial": "Sede oficial del circuito mundial Premier Padel en Oriente Medio, con la mayor concentración de jugadores avanzados del Golfo."
    },

    # 13. Sydney Racquet Club (Australia)
    {
        "id": "sydney-racquet-club-australia",
        "nombre": "Sydney Racquet Club",
        "pais": "Australia",
        "pais_codigo": "AU",
        "region_filtro": "ZA",
        "bandera": "🇦🇺",
        "ciudad_sede": "Sídney (Moore Park / Alexandria)",
        "coords": [-33.8688, 151.2093],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 sedes en Sídney",
        "num_pistas": "10+ pistas de pádel y pickleball",
        "software": "Playtomic",
        "fundadores": "Sydney Racquet Club Pty Ltd",
        "web": "https://racquetclub.com.au",
        "tagline": "El club social de pádel de referencia en The Entertainment Quarter junto al centro de Sídney.",
        "resumen": "Sydney Racquet Club opera en el corazón de la vida de ocio de Sídney en Moore Park Entertainment Quarter, muy cerca del distrito financiero (CBD), combinando pistas panorámicas de pádel con canchas de pickleball, eventos sociales de noche y pro-shop.",
        "sedes_principales": [
            "Sydney Racquet Club Moore Park (The Entertainment Quarter - 17 Park Rd North)",
            "Sydney Racquet Club Alexandria (Expansión)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas exteriores con césped azul texturizado y focos LED de competición",
            "software": "Playtomic",
            "domotica": "Acceso automatizado por app y reservas de luz en línea",
            "grabacion": "Cámaras para eventos y torneos nacionales Australian Padel Open",
            "restauracion": "Bar al aire libre, terraza chill-out, barbacoa social y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios en recintos de entretenimiento y deportivos consolidados",
            "perfil_club": "Espacios céntricos urbanos con alto flujo peatonal y facilidades de parking",
            "canon_royalties": "Operación directa",
            "inversion_media": "400.000 AUD a 900.000 AUD por centro"
        },
        "diferencial": "Ubicación inmejorable en el mayor recinto de ocio de Sídney, a minutos del centro de la ciudad."
    },

    # 14. Action Padel (Sudáfrica)
    {
        "id": "action-padel-south-africa",
        "nombre": "Action Padel",
        "pais": "Sudáfrica",
        "pais_codigo": "ZA",
        "region_filtro": "ZA",
        "bandera": "🇿🇦",
        "ciudad_sede": "Ciudad del Cabo / Johannesburgo",
        "coords": [-33.9249, 18.4241],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "3 complejos en Sudáfrica",
        "num_pistas": "14+ pistas de pádel",
        "software": "Playtomic",
        "fundadores": "Action Sports Group South Africa",
        "web": "https://actionsports.co.za",
        "tagline": "Pistas de cristal integradas en los recintos multideportivos Action Sports de Sudáfrica.",
        "resumen": "Action Padel opera centros integrados de pádel en Ciudad del Cabo (Fives Futbol Century City) y en recintos deportivos cubiertos de Gauteng, ofreciendo pistas panorámicas, ligas de empresas semanales y academias comunitarias.",
        "sedes_principales": [
            "Action Padel Century City (Century Boulevard, Ciudad del Cabo)",
            "Action Sports Arena Padel (Johannesburgo)",
            "Action Padel Durbanville"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas de cristal templado panorámicas protegidas del viento sudafricano",
            "software": "Playtomic",
            "domotica": "Acceso digital por app y alquiler automatizado de material",
            "grabacion": "Cámaras en pistas centrales",
            "restauracion": "Action Sports Café, bar social y zona de visionado de partidos"
        },
        "modelo_expansion": {
            "tipo_contrato": "Implantación directa en la red existente de franquicias Action Sports",
            "perfil_club": "Arenas deportivas indoor y campos de fútbol 5 consolidados",
            "canon_royalties": "Modelo franquicia Action Sports",
            "inversion_media": "250.000$ a 600.000$ por instalación"
        },
        "diferencial": "Sinergia directa con la base de datos de más de 100.000 deportistas de la red nacional Action Sports."
    }
]

if __name__ == "__main__":
    print(f"[OK] dataset_expansion_new.py con {len(EXPANSION_OPERATORS)} nuevas franquicias cargadas.")
