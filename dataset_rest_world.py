# -*- coding: utf-8 -*-
"""
dataset_rest_world.py
Cadenas multiclub y franquicias de Estados Unidos, Latinoamérica, Oriente Medio, Sudáfrica y Australia.
"""

# =========================================================================
# 🇺🇸 ESTADOS UNIDOS (9 Cadenas y Franquicias)
# =========================================================================
US_LIST = [
    {
        "id": "padel-haus",
        "nombre": "Padel Haus",
        "pais": "Estados Unidos",
        "pais_codigo": "US",
        "region_filtro": "US",
        "bandera": "🇺🇸",
        "ciudad_sede": "Nueva York / Nashville",
        "coords": [40.7144, -73.9600],
        "modelo": "Boutique & Ultra-Lujo",
        "modelo_badge": "bg-purple-100 text-purple-800 border-purple-200",
        "tipo_categoria": "boutique",
        "escala": "macro",
        "num_clubs": "4 centros de diseño",
        "num_pistas": "24+ pistas cubiertas",
        "software": "App Propia Padel Haus / Playtomic",
        "fundadores": "Santiago Gomez (ex-banquero de inversión y restaurador de éxito)",
        "web": "https://padel.haus",
        "tagline": "El club que introdujo el pádel a la élite financiera y creativa de Nueva York.",
        "resumen": "Padel Haus es la marca de mayor estatus de Norteamérica. Fundada por el empresario Santiago Gomez en Williamsburg (Brooklyn), se ha expandido a DUMBO, Greenpoint y Nashville (Tennessee). Sus clubes combinan pistas indoor de 10 metros de altura con saunas, baños fríos, cafeterías de matcha orgánico y espacios de coworking.",
        "sedes_principales": [
            "Padel Haus Williamsburg (Brooklyn NY - 4 pistas cubiertas y juice bar)",
            "Padel Haus DUMBO (Brooklyn NY)",
            "Padel Haus Greenpoint (Brooklyn NY)",
            "Padel Haus Nashville (Green Hills, Tennessee)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de competición con cristal templado de 12mm y moqueta azul",
            "software": "App Padel Haus y Playtomic",
            "domotica": "Acceso QR, taquillas electrónicas y climatización de lujo",
            "grabacion": "Sistemas de vídeo en pista para socios VIP",
            "restauracion": "Juice Bar orgánico con batidos proteicos, matcha latte y pro-shop de ropa de diseño"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena corporativa respaldada por fondos de capital riesgo de Wall Street",
            "perfil_club": "Almacenes industriales de diseño en distritos de renta per cápita máxima",
            "canon_royalties": "Operación directa",
            "inversion_media": "2.500.000$ a 5.000.000$ por club"
        },
        "diferencial": "El público más exclusivo de Nueva York: socios de firmas de capital riesgo, moda, arte y modelos internacionales."
    },
    {
        "id": "reserve-padel",
        "nombre": "Reserve Padel",
        "pais": "Estados Unidos",
        "pais_codigo": "US",
        "region_filtro": "US",
        "bandera": "🇺🇸",
        "ciudad_sede": "Miami / Nueva York",
        "coords": [25.7617, -80.1918],
        "modelo": "Boutique & Ultra-Lujo",
        "modelo_badge": "bg-purple-100 text-purple-800 border-purple-200",
        "tipo_categoria": "boutique",
        "escala": "macro",
        "num_clubs": "4 centros de ultra-lujo",
        "num_pistas": "22+ pistas",
        "software": "Reserve Padel App / Playtomic",
        "fundadores": "Wayne Boich (magnate financiero de Miami)",
        "web": "https://reservepadel.com",
        "tagline": "El club más exclusivo del planeta: hidroaviones, yates y celebridades en Miami y Manhattan.",
        "resumen": "Reserve Padel es el club de las superestrellas mundiales. Creado por Wayne Boich, opera en ubicaciones de ensueño: Miami Seaplane Base (con acceso en hidroavión y yate frente a la bahía de Biscayne), SoLé Mia (complejo masivo con pistas de cristal cubiertas), Miami Design District y su instalación en Hudson Yards (Nueva York).",
        "sedes_principales": [
            "Reserve Miami Seaplane Base (Biscayne Bay - acceso en hidroavión y barco)",
            "Reserve SoLé Mia (North Miami - megacomplejo indoor y outdoor)",
            "Reserve Hudson Yards (Manhattan, Nueva York)",
            "Reserve Miami Design District"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de edición limitada con acabados en negro y cristal templado ultra-óptico",
            "software": "Reserve Padel App para socios exclusivos y reservas VIP",
            "domotica": "Acceso restringido biométrico y concierge privado",
            "grabacion": "Producción de televisión 4K para torneos de leyendas mundiales como Reserve Cup",
            "restauracion": "Gastronomía con caviar, champán, baristas de autor y wellness lounge"
        },
        "modelo_expansion": {
            "tipo_contrato": "Red corporativa ultralujosa en enclaves de turismo y finanzas globales",
            "perfil_club": "Las localizaciones costeras o urbanas más deseadas de Estados Unidos",
            "canon_royalties": "Operación directa",
            "inversion_media": "Más de 4.000.000$ por club"
        },
        "diferencial": "Clientes como Jimmy Butler, David Beckham, Dwyane Wade y eventos benéficos de primer nivel mundial."
    },
    {
        "id": "ultra-padel-miami",
        "nombre": "Ultra Padel Miami",
        "pais": "Estados Unidos",
        "pais_codigo": "US",
        "region_filtro": "US",
        "bandera": "🇺🇸",
        "ciudad_sede": "Miami (Magic City)",
        "coords": [25.8200, -80.1900],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "2 megacomplejos en Florida",
        "num_pistas": "38+ pistas",
        "software": "Playtomic",
        "fundadores": "Ultra Padel Group Miami",
        "web": "https://ultrapadel.com",
        "tagline": "El macrocomplejo de pádel cubierto y exterior más grande de todo Estados Unidos.",
        "resumen": "Situado en el distrito de innovación de Magic City en Miami (Little Haiti), Ultra Padel cuenta con 38 pistas (combinando naves cubiertas climatizadas y pistas panorámicas exteriores), siendo el epicentro de la comunidad hispana y estadounidense de Florida.",
        "sedes_principales": [
            "Ultra Padel Magic City (Miami - 38 pistas y gran casa club)",
            "Instalaciones de expansión en Florida Sur"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de última generación con césped texturizado monofilamento",
            "software": "Playtomic",
            "domotica": "Control digital de iluminación LED y climatización",
            "grabacion": "Sistemas para torneos del circuito profesional de Estados Unidos (USPA)",
            "restauracion": "Terraza caribeña con comida latina, batidos tropicales y tienda deportiva gigante"
        },
        "modelo_expansion": {
            "tipo_contrato": "Megacentros en suelo terciario e industrial",
            "perfil_club": "Parcelas de más de 20.000 m²",
            "canon_royalties": "Operación directa",
            "inversion_media": "Más de 5.000.000$"
        },
        "diferencial": "Capacidad sin parangón en Norteamérica para albergar torneos masivos de más de 500 participantes."
    },
    {
        "id": "taktika-padel",
        "nombre": "Taktika Padel",
        "pais": "Estados Unidos",
        "pais_codigo": "US",
        "region_filtro": "US",
        "bandera": "🇺🇸",
        "ciudad_sede": "San Diego / Los Ángeles",
        "coords": [32.7157, -117.1611],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "3 clubes en California",
        "num_pistas": "20+ pistas",
        "software": "Playtomic",
        "fundadores": "Gabriel Pérez Krieb, Ryan Redondo y Armando Rodiel",
        "web": "https://taktikapadel.com",
        "tagline": "El líder indiscutible del pádel en California: San Diego y el estadio del LA Galaxy.",
        "resumen": "Taktika Padel ha liderado la implantación del deporte en la Costa Oeste estadounidense. Destaca su buque insignia en el Barnes Tennis Center de San Diego y su instalación en el Dignity Health Sports Park del LA Galaxy en Carson (Los Ángeles), combinando academias y torneos oficiales USPA.",
        "sedes_principales": [
            "Taktika San Diego (Barnes Tennis Center - 8 pistas de competición)",
            "Taktika Carson / Los Ángeles (Dignity Health Sports Park - LA Galaxy)",
            "Taktika Silicon Valley (en desarrollo)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de torneo con césped azul WPT",
            "software": "Playtomic",
            "domotica": "Acceso QR y reserva autónoma",
            "grabacion": "Pistas con cámaras de streaming para el circuito estadounidense",
            "restauracion": "Clubhouse californiano con bowls saludables, café de especialidad y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Alianzas en complejos deportivos universitarios y estadios de la MLS",
            "perfil_club": "Centros de tenis consolidados y franquicias deportivas",
            "canon_royalties": "Operación directa y joint ventures",
            "inversion_media": "700.000$ a 1.800.000$ por sede"
        },
        "diferencial": "Alianza con el LA Galaxy y ser el primer gran operador en conquistar el gigantesco mercado californiano."
    },
    {
        "id": "park-padel",
        "nombre": "Park Padel",
        "pais": "Estados Unidos",
        "pais_codigo": "US",
        "region_filtro": "US",
        "bandera": "🇺🇸",
        "ciudad_sede": "San Francisco",
        "coords": [37.7749, -122.4194],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 centros emblemáticos",
        "num_pistas": "10+ pistas",
        "software": "Playtomic",
        "fundadores": "Jessica Shu, Katie Mintz y Neil Preeth",
        "web": "https://parkpadel.com",
        "tagline": "El club urbano pionero de San Francisco: del Embarcadero al Palace of Fine Arts.",
        "resumen": "Park Padel es la cadena femenina y tech-friendly que conquistó San Francisco. Sus pistas en el histórico muelle de Embarcadero y en el Palace of Fine Arts son icónicas, congregando a fundadores de startups, ingenieros de IA de Silicon Valley y aficionados locales.",
        "sedes_principales": [
            "Park Padel Embarcadero (San Francisco Pier)",
            "Park Padel Palace of Fine Arts (Presidio SF)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas all-weather preparadas para la bruma de la bahía de San Francisco",
            "software": "Playtomic",
            "domotica": "Acceso por código QR digital 100% automatizado",
            "grabacion": "Sistemas para repetición de puntos en redes sociales",
            "restauracion": "Food trucks locales con comida orgánica y café tostado en San Francisco"
        },
        "modelo_expansion": {
            "tipo_contrato": "Concesiones en edificios históricos y muelles portuarios",
            "perfil_club": "Emplazamientos urbanos icónicos con gran valor arquitectónico",
            "canon_royalties": "Operación directa",
            "inversion_media": "600.000$ a 1.200.000$"
        },
        "diferencial": "La comunidad de fundadores de Silicon Valley y ubicaciones turísticas inigualables en la bahía de SF."
    },
    {
        "id": "wynwood-padel-club",
        "nombre": "Wynwood Padel Club",
        "pais": "Estados Unidos",
        "pais_codigo": "US",
        "region_filtro": "US",
        "bandera": "🇺🇸",
        "ciudad_sede": "Miami (Wynwood Arts District)",
        "coords": [25.8000, -80.1980],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 centros artísticos",
        "num_pistas": "12+ pistas",
        "software": "Playtomic",
        "fundadores": "Wynwood Sports Management",
        "web": "https://wynwoodpadelclub.com",
        "tagline": "Pádel entre los grafitis y galerías de arte más famosos del mundo.",
        "resumen": "Situado en pleno distrito artístico de Wynwood en Miami, el club integra el arte urbano y los murales con 8 pistas panorámicas, café social, terraza de eventos con DJ y torneos after-work muy frecuentados.",
        "sedes_principales": [
            "Wynwood Padel Club (NW 5th Ave Miami - 8 pistas)",
            "Centro satélite en Miami Arts District"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de cristal decoradas con murales de artistas urbanos",
            "software": "Playtomic",
            "domotica": "Acceso QR y reservas digitales",
            "grabacion": "Cámaras para eventos y directos de creadores de contenido",
            "restauracion": "Cafetería con matcha, empanadas artesanales, cerveza fría y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Clubes urbanos propios",
            "perfil_club": "Suelos industriales reconvertidos en distritos de moda",
            "canon_royalties": "Operación propia",
            "inversion_media": "800.000$ a 1.500.000$"
        },
        "diferencial": "El club con la estética más fotografiada de Miami, en el corazón cultural de Wynwood."
    },
    {
        "id": "diez-por-veinte-padel",
        "nombre": "10by20 Padel",
        "pais": "Estados Unidos",
        "pais_codigo": "US",
        "region_filtro": "US",
        "bandera": "🇺🇸",
        "ciudad_sede": "Texas (Austin / Dallas)",
        "coords": [30.2672, -97.7431],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 centros en Texas",
        "num_pistas": "14+ pistas cubiertas",
        "software": "Playtomic",
        "fundadores": "10by20 Sports Texas",
        "web": "https://10by20padel.com",
        "tagline": "Pádel cubierto y climatizado para el calor extremo de Austin y Dallas.",
        "resumen": "Cadena que toma su nombre de las medidas reglamentarias de una pista de pádel (10x20 metros). En Texas, donde el calor estival supera los 40 grados, opera naves 100% climatizadas que se han convertido en el refugio deportivo del cinturón solar.",
        "sedes_principales": [
            "10by20 Austin (8 pistas indoor climatizadas)",
            "10by20 Dallas Urban Hub"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas de competición con césped monofilamento azul y aire acondicionado potente",
            "software": "Playtomic",
            "domotica": "Acceso 100% automatizado",
            "grabacion": "Pistas con cámaras cenitales para análisis",
            "restauracion": "Clubhouse tejano con barbacoa, cerveza local y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios en el Sunbelt estadounidense",
            "perfil_club": "Naves de más de 2.500m² con altura libre y buen aislamiento térmico",
            "canon_royalties": "Operación directa",
            "inversion_media": "900.000$ a 1.800.000$"
        },
        "diferencial": "Confort climático absoluto en Texas y comunidad muy ligada al auge tecnológico de Austin."
    },
    {
        "id": "padel-x-usa",
        "nombre": "PadelX USA",
        "pais": "Estados Unidos",
        "pais_codigo": "US",
        "region_filtro": "US",
        "bandera": "🇺🇸",
        "ciudad_sede": "Boca Raton / Miami",
        "coords": [26.3683, -80.1289],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 centros inteligentes",
        "num_pistas": "12+ pistas",
        "software": "Playtomic / App Propia",
        "fundadores": "PadelX International USA",
        "web": "https://padelx.com",
        "tagline": "Pistas de pádel conectadas con pantallas interactivas y análisis de IA.",
        "resumen": "Cadena innovadora que incorpora analítica digital a pie de pista en Florida (Boca Raton y Miami), ofreciendo repetición instantánea de jugadas en pantalla táctil en pista y ranking digitalizado.",
        "sedes_principales": [
            "PadelX Boca Raton",
            "PadelX Miami Beach"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con tótem táctil interactivo en cada pista",
            "software": "App PadelX y Playtomic",
            "domotica": "Acceso QR y luces inteligentes",
            "grabacion": "Grabación de partidos con descarga de clips en el smartphone",
            "restauracion": "Smart café y venta de palas"
        },
        "modelo_expansion": {
            "tipo_contrato": "Franquicia de pistas inteligentes",
            "perfil_club": "Naves de diseño y clubes privados de tenis",
            "canon_royalties": "Canon SaaS de analítica",
            "inversion_media": "700.000$ a 1.300.000$"
        },
        "diferencial": "La tecnología de repetición y clips para Instagram en tiempo real integrada en el partido."
    },
    {
        "id": "smart-padel-usa",
        "nombre": "SmartPadel USA",
        "pais": "Estados Unidos",
        "pais_codigo": "US",
        "region_filtro": "US",
        "bandera": "🇺🇸",
        "ciudad_sede": "Miami / Doral",
        "coords": [25.8100, -80.3500],
        "modelo": "Club 100% Automatizado 24/7",
        "modelo_badge": "bg-emerald-100 text-emerald-800 border-emerald-200",
        "tipo_categoria": "automatizado",
        "escala": "media",
        "num_clubs": "2 naves autónomas",
        "num_pistas": "10+ pistas",
        "software": "Playtomic / IoT Propio",
        "fundadores": "SmartPadel Automation",
        "web": "https://smartpadelusa.com",
        "tagline": "El modelo 100% autónomo 24/7 adaptado a las naves comerciales del sur de Florida.",
        "resumen": "Cadena que opera naves cubiertas 24/7 sin empleados en Doral y el condado de Miami-Dade. La puerta se abre por Bluetooth con la reserva de Playtomic y los focos se activan automáticamente.",
        "sedes_principales": [
            "SmartPadel Doral (Miami)",
            "SmartPadel Kendall"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas cubiertas reforzadas",
            "software": "Playtomic integrado con IoT",
            "domotica": "Acceso Bluetooth / QR, encendido automático de proyectores y aire acondicionado",
            "grabacion": "CCTV con inteligencia artificial para seguridad 24h",
            "restauracion": "Vending inteligente de bebidas y bolas"
        },
        "modelo_expansion": {
            "tipo_contrato": "Franquicia tecnológica",
            "perfil_club": "Almacenes en polígonos urbanos de Miami",
            "canon_royalties": "Cuota de mantenimiento de software",
            "inversion_media": "400.000$ a 750.000$"
        },
        "diferencial": "Márgenes operativos muy superiores gracias al coste laboral cero."
    }
]

print(f"Cargadas {len(US_LIST)} cadenas de Estados Unidos.")

# =========================================================================
# 🇲🇽 LATINOAMÉRICA: MÉXICO, CHILE, ARGENTINA Y BRASIL (12 Cadenas)
# =========================================================================
LATAM_LIST = [
    {
        "id": "padel-co",
        "nombre": "Padel Co México",
        "pais": "México",
        "pais_codigo": "MX",
        "region_filtro": "MX",
        "bandera": "🇲🇽",
        "ciudad_sede": "Ciudad de México (Polanco / Reforma)",
        "coords": [19.4326, -99.1332],
        "modelo": "Boutique & Ultra-Lujo",
        "modelo_badge": "bg-purple-100 text-purple-800 border-purple-200",
        "tipo_categoria": "boutique",
        "escala": "macro",
        "num_clubs": "4 centros en CDMX",
        "num_pistas": "24+ pistas",
        "software": "Playtomic / App Propia",
        "fundadores": "Padel Co Lifestyle Group",
        "web": "https://padelco.mx",
        "tagline": "El club boutique de pádel de referencia para la alta sociedad mexicana en Polanco y Reforma.",
        "resumen": "Padel Co es la cúspide del pádel social en la capital mexicana. Con clubes en las colonias más cotizadas de la Ciudad de México (Polanco, Paseo de la Reforma, Santa Fe e Interlomas), cuenta con pistas panorámicas de cristal templado, baristas especializados, terrazas lounge y una vibrante vida social y de negocios.",
        "sedes_principales": [
            "Padel Co Polanco (CDMX)",
            "Padel Co Reforma / Lomas",
            "Padel Co Santa Fe",
            "Padel Co Interlomas"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de 12mm de cristal, césped de competición azul y graderíos lounge",
            "software": "Playtomic y app exclusiva Padel Co",
            "domotica": "Acceso QR autónomo y vigilancia digital",
            "grabacion": "Pantallas en el bar para repetición instantánea de jugadas",
            "restauracion": "Terraza lounge gourmet con mixología, café de especialidad y pro-shop de ropa técnica de autor"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena de clubes propios en ubicaciones prime",
            "perfil_club": "Suelos y azoteas en las zonas corporativas y residenciales de mayor renta de México",
            "canon_royalties": "Operación directa",
            "inversion_media": "800.000$ a 1.800.000$ por club"
        },
        "diferencial": "Exclusividad, networking empresarial y un ambiente social de altísimo poder adquisitivo en la cuna mundial del pádel."
    },
    {
        "id": "altapadel",
        "nombre": "Altapadel México",
        "pais": "México",
        "pais_codigo": "MX",
        "region_filtro": "MX",
        "bandera": "🇲🇽",
        "ciudad_sede": "CDMX / Querétaro / Puebla",
        "coords": [19.3000, -99.2000],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "4 macrocentros",
        "num_pistas": "30+ pistas",
        "software": "Playtomic",
        "fundadores": "Altapadel Sports Group",
        "web": "https://altapadel.com.mx",
        "tagline": "Grandes complejos de pádel en el Pedregal de CDMX y las capitales del Bajío.",
        "resumen": "Cadena que opera instalaciones de gran escala en el Pedregal de San Ángel (sur de CDMX), Querétaro Juriquilla y Puebla, con torneos de fin de semana con más de 200 parejas.",
        "sedes_principales": [
            "Altapadel Pedregal (CDMX - 10 pistas panorámicas)",
            "Altapadel Querétaro Juriquilla",
            "Altapadel Puebla Angelópolis",
            "Altapadel Bosques"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con césped texturizado y gradas",
            "software": "Playtomic",
            "domotica": "Control digital de iluminación y tornos",
            "grabacion": "Sistemas para torneos oficiales FEMEPA",
            "restauracion": "Restaurante con taquería gourmet, cervezas artesanales y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios en el centro y Bajío de México",
            "perfil_club": "Parcelas de más de 5.000 m²",
            "canon_royalties": "Operación directa",
            "inversion_media": "900.000$ a 2.000.000$"
        },
        "diferencial": "Capacidad organizativa de torneos masivos en el centro de México con ambiente familiar."
    },
    {
        "id": "contrapared",
        "nombre": "Contrapared México",
        "pais": "México",
        "pais_codigo": "MX",
        "region_filtro": "MX",
        "bandera": "🇲🇽",
        "ciudad_sede": "CDMX / Guadalajara",
        "coords": [19.3600, -99.2600],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "3 clubes",
        "num_pistas": "18+ pistas",
        "software": "Playtomic",
        "fundadores": "Contrapared Padel Club",
        "web": "https://contrapared.com.mx",
        "tagline": "Pádel de competición y clínicas de tecnificación en Santa Fe y Guadalajara.",
        "resumen": "Cadena enfocada en el pádel técnico y de competición con clubes en Santa Fe (CDMX), Bosques de las Lomas y Zapopan (Guadalajara).",
        "sedes_principales": [
            "Contrapared Santa Fe (CDMX)",
            "Contrapared Bosques",
            "Contrapared Guadalajara Zapopan"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de competición WPT",
            "software": "Playtomic",
            "domotica": "Acceso QR automatizado",
            "grabacion": "Vídeo para análisis técnico de clases",
            "restauracion": "Clubhouse con terraza y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios",
            "perfil_club": "Naves y suelos urbanos de 2.000m² a 4.000m²",
            "canon_royalties": "Operación directa",
            "inversion_media": "700.000$ a 1.400.000$"
        },
        "diferencial": "El alto nivel competitivo de sus jugadores y escuela de tecnificación."
    },
    {
        "id": "club-padel-pro-mexico",
        "nombre": "Club Padel Pro México",
        "pais": "México",
        "pais_codigo": "MX",
        "region_filtro": "MX",
        "bandera": "🇲🇽",
        "ciudad_sede": "Monterrey / San Pedro Garza García",
        "coords": [25.6667, -100.3500],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "3 macrocentros",
        "num_pistas": "24+ pistas",
        "software": "Playtomic",
        "fundadores": "Padel Pro Monterrey",
        "web": "https://padelpromexico.com",
        "tagline": "El gigante del norte de México en el municipio más rico del país: San Pedro Garza García.",
        "resumen": "Operador líder en el estado de Nuevo León. Con centros en San Pedro Garza García y Monterrey, ofrece pistas cubiertas con aire acondicionado para combatir el calor extremo del norte de México.",
        "sedes_principales": [
            "Club Padel Pro San Pedro (10 pistas climatizadas)",
            "Club Padel Pro Monterrey Cumbres",
            "Club Padel Pro Valle Oriente"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas en naves de gran altura con climatización extrema",
            "software": "Playtomic",
            "domotica": "Acceso biométrico e iluminación inteligente",
            "grabacion": "Streaming de torneos empresariales",
            "restauracion": "Terraza con asador regiomontano (carnes asadas), bar deportivo y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios en el norte de México",
            "perfil_club": "Naves industriales climatizadas en Monterrey",
            "canon_royalties": "Operación directa",
            "inversion_media": "1.000.000$ a 2.200.000$"
        },
        "diferencial": "Ubicación en el polo industrial de Monterrey y tradición de torneos con asados."
    },
    {
        "id": "padel-park-chile",
        "nombre": "Padel Park Chile",
        "pais": "Chile",
        "pais_codigo": "CL",
        "region_filtro": "MX",
        "bandera": "🇨🇱",
        "ciudad_sede": "Santiago (Huechuraba / Peñalolén)",
        "coords": [-33.3700, -70.6700],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "4 macrocomplejos en Chile",
        "num_pistas": "35+ pistas",
        "software": "EasyCanchas / Playtomic",
        "fundadores": "Padel Park Chile Group",
        "web": "https://padelpark.cl",
        "tagline": "La mayor red de parques deportivos de pádel de Santiago y el Biobío.",
        "resumen": "Cadena pionera del auge del pádel en Chile con complejos en Huechuraba, Peñalolén, Concepción y Viña del Mar, con pistas panorámicas, quincho para asados chilenos y academias federadas.",
        "sedes_principales": [
            "Padel Park Huechuraba (Santiago Norte - 10 pistas)",
            "Padel Park Peñalolén (Santiago Oriente)",
            "Padel Park Concepción (Biobío)",
            "Padel Park Viña del Mar"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con césped texturizado azul",
            "software": "EasyCanchas (plataforma número uno de reservas en Chile) y Playtomic",
            "domotica": "Control digital de iluminación y acceso automatizado",
            "grabacion": "Pistas con cámaras para torneos del circuito FEPANCHI",
            "restauracion": "Zona de quinchos para asados de tercer tiempo, cafetería y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena de clubes propios en parcelas deportivas",
            "perfil_club": "Suelos periurbanos de más de 6.000m² con gran espacio social",
            "canon_royalties": "Operación directa",
            "inversion_media": "600.000$ a 1.500.000$ por club"
        },
        "diferencial": "El concepto chileno de 'tercer tiempo' con quinchos familiares y reserva masiva vía EasyCanchas."
    },
    {
        "id": "club-conecta-chile",
        "nombre": "Club Conecta Chile",
        "pais": "Chile",
        "pais_codigo": "CL",
        "region_filtro": "MX",
        "bandera": "🇨🇱",
        "ciudad_sede": "Santiago (La Dehesa / Las Condes)",
        "coords": [-33.3600, -70.5200],
        "modelo": "Boutique & Ultra-Lujo",
        "modelo_badge": "bg-purple-100 text-purple-800 border-purple-200",
        "tipo_categoria": "boutique",
        "escala": "macro",
        "num_clubs": "3 clubes en el sector oriente de Santiago",
        "num_pistas": "24+ pistas",
        "software": "EasyCanchas",
        "fundadores": "Inversionistas del sector oriente de Santiago",
        "web": "https://clubconecta.cl",
        "tagline": "El club social más exclusivo de Santiago en La Dehesa y Las Condes.",
        "resumen": "Cadena que opera en los distritos de mayor renta de la capital chilena (La Dehesa, Las Condes y Chicureo). Cuenta con pistas de calidad WPT, gimnasio de preparación funcional, cafeterías de autor y una escuela de menores de primer nivel.",
        "sedes_principales": [
            "Club Conecta La Dehesa (Lo Barnechea)",
            "Club Conecta Las Condes",
            "Club Conecta Chicureo"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas de competición con cubiertas y exteriores panorámicas",
            "software": "EasyCanchas",
            "domotica": "Acceso digital y control lumínico",
            "grabacion": "Grabación de partidos de liga de honor",
            "restauracion": "Restaurante bistró, bar de cócteles y pro-shop de lujo"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios en el sector oriente de Santiago",
            "perfil_club": "Parcelas residenciales prime",
            "canon_royalties": "Operación directa",
            "inversion_media": "1.200.000$ a 2.500.000$"
        },
        "diferencial": "El club social más cotizado de la élite empresarial santiaguina."
    },
    {
        "id": "capital-padel-chile",
        "nombre": "Capital Padel Chile",
        "pais": "Chile",
        "pais_codigo": "CL",
        "region_filtro": "MX",
        "bandera": "🇨🇱",
        "ciudad_sede": "Santiago Centro / Maipú",
        "coords": [-33.4500, -70.6600],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "3 centros metropolitanos",
        "num_pistas": "20+ pistas",
        "software": "EasyCanchas",
        "fundadores": "Capital Sports Chile",
        "web": "https://capitalpadel.cl",
        "tagline": "Pádel accesible y torneos masivos en el corazón del Gran Santiago.",
        "resumen": "Cadena enfocada en democratizar el pádel en las comunas céntricas y poniente de Santiago (Santiago Centro, Maipú y La Florida), con alta rotación de pistas y ligas nocturnas.",
        "sedes_principales": [
            "Capital Padel Santiago Centro",
            "Capital Padel Maipú",
            "Capital Padel La Florida"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con iluminación LED",
            "software": "EasyCanchas",
            "domotica": "Acceso QR",
            "grabacion": "Vídeo en torneos",
            "restauracion": "Café, bebidas y tienda de accesorios"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios",
            "perfil_club": "Suelos urbanos con metro cercano",
            "canon_royalties": "Operación directa",
            "inversion_media": "450.000$ a 900.000$"
        },
        "diferencial": "Conectividad total en transporte público y precios accesibles."
    },
    {
        "id": "mas-padel-chile",
        "nombre": "Más Padel Chile",
        "pais": "Chile",
        "pais_codigo": "CL",
        "region_filtro": "MX",
        "bandera": "🇨🇱",
        "ciudad_sede": "Santiago (Providencia / Vitacura)",
        "coords": [-33.4200, -70.6000],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 centros en Providencia y Vitacura",
        "num_pistas": "14+ pistas",
        "software": "EasyCanchas",
        "fundadores": "Más Padel Group",
        "web": "https://maspadel.cl",
        "tagline": "Pistas de alta competición en las zonas comerciales más dinámicas de Santiago.",
        "resumen": "Centros muy concurridos en Providencia y Vitacura por su ubicación estratégica junto a oficinas y centros de negocios, con ligas after-office muy activas.",
        "sedes_principales": [
            "Más Padel Providencia",
            "Más Padel Vitacura"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas de cristal templado de alta calidad",
            "software": "EasyCanchas",
            "domotica": "Control digital",
            "grabacion": "Streaming de torneos",
            "restauracion": "Bar terraza y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios",
            "perfil_club": "Suelos urbanos prime",
            "canon_royalties": "Operación directa",
            "inversion_media": "500.000$ a 1.000.000$"
        },
        "diferencial": "Público ejecutivo y ligas corporativas entresemana."
    },
    {
        "id": "el-monasterio",
        "nombre": "El Monasterio Padel",
        "pais": "Argentina",
        "pais_codigo": "AR",
        "region_filtro": "MX",
        "bandera": "🇦🇷",
        "ciudad_sede": "Buenos Aires (Flores / Caballito)",
        "coords": [-34.6280, -58.4550],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 clubes históricos",
        "num_pistas": "16+ pistas",
        "software": "Playtomic / PadelClick",
        "fundadores": "Familia Gattiker y pioneros del pádel argentino",
        "web": "https://elmonasteriopadel.com.ar",
        "tagline": "El templo sagrado del pádel mundial: donde entrenaron Bela, Juan Martín Díaz y Lamperti.",
        "resumen": "El Monasterio en Buenos Aires no es un club cualquiera: es la cuna de los mejores jugadores de la historia del pádel. Por sus pistas pasaron Fernando Belasteguín, Juan Martín Díaz, Miguel Lamperti y Sanyo Gutiérrez. Opera como escuela de alto rendimiento y sede de los torneos más competitivos de Argentina.",
        "sedes_principales": [
            "El Monasterio Flores (Buenos Aires - 8 pistas cubiertas históricas)",
            "Centro anexo de entrenamiento en la provincia de Buenos Aires"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas de muro clásico y de cristal con césped de alta densidad",
            "software": "Playtomic y sistema propio de torneos por categorías",
            "domotica": "Iluminación LED de bajo consumo",
            "grabacion": "Cámaras para análisis de técnica de jugadores de circuito profesional",
            "restauracion": "Cantina tradicional argentina con empanadas, asado y museo de palas históricas"
        },
        "modelo_expansion": {
            "tipo_contrato": "Club propio histórico y academia de exportación de talentos a Europa",
            "perfil_club": "Naves urbanas tradicionales",
            "canon_royalties": "Operación directa",
            "inversion_media": "400.000$ a 800.000$"
        },
        "diferencial": "El valor místico y la mística competitiva: el club más legendario de la historia del pádel sudamericano."
    },
    {
        "id": "premium-padel-center",
        "nombre": "Premium Padel Center",
        "pais": "Argentina",
        "pais_codigo": "AR",
        "region_filtro": "MX",
        "bandera": "🇦🇷",
        "ciudad_sede": "Buenos Aires (Pilar / Vicente López)",
        "coords": [-34.4600, -58.9100],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "2 macrocentros en Zona Norte",
        "num_pistas": "20+ pistas",
        "software": "Playtomic",
        "fundadores": "Premium Sports Argentina",
        "web": "https://premiumpadelcenter.com.ar",
        "tagline": "Instalaciones de clase mundial en la cotizada Zona Norte del Gran Buenos Aires.",
        "resumen": "Cadena de gran envergadura en Pilar y Vicente López con pistas panorámicas cubiertas de última generación que han traído los estándares europeos de vuelta a Argentina.",
        "sedes_principales": [
            "Premium Padel Pilar (12 pistas cubiertas)",
            "Premium Padel Vicente López"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de cristal templado y techos de nave industrial de 10 metros",
            "software": "Playtomic",
            "domotica": "Acceso QR digital",
            "grabacion": "Streaming de torneos de la APA (Asociación Padel Argentino)",
            "restauracion": "Parrilla argentina, cafetería y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios",
            "perfil_club": "Naves industriales en Zona Norte",
            "canon_royalties": "Operación directa",
            "inversion_media": "800.000$ a 1.600.000$"
        },
        "diferencial": "Las mejores pistas cubiertas de cristal de Argentina con comodidades europeas."
    },
    {
        "id": "brava-padel",
        "nombre": "Brava Padel Brasil",
        "pais": "Brasil",
        "pais_codigo": "BR",
        "region_filtro": "MX",
        "bandera": "🇧🇷",
        "ciudad_sede": "Santa Catarina (Balneário Camboriú / Itajaí)",
        "coords": [-26.9800, -48.6300],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "3 clubes en el sur de Brasil",
        "num_pistas": "22+ pistas",
        "software": "Playtomic / App Propia",
        "fundadores": "Brava Sports Group",
        "web": "https://bravapadel.com.br",
        "tagline": "El gigante del pádel brasileño en la meca del lujo costero de Balneário Camboriú.",
        "resumen": "Brava Padel es la cadena de referencia en el estado de Santa Catarina, el epicentro del pádel brasileño. Con complejos en Praia Brava (Itajaí), Balneário Camboriú y Curitiba, combina pistas cubiertas climatizadas de última generación con hostelería de playa y torneos del circuito COBRAPA.",
        "sedes_principales": [
            "Brava Padel Praia Brava (Itajaí - 8 pistas cubiertas)",
            "Brava Padel Balneário Camboriú",
            "Brava Padel Curitiba (Paraná)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas oficiales con césped azul WPT",
            "software": "Playtomic y Brava App",
            "domotica": "Acceso por código QR digital y climatización inteligente",
            "grabacion": "Cámaras con IA para torneos profesionales de Brasil",
            "restauracion": "Beach club lounge con açai orgánico, caipirinhas, parrilla y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena propia financiada por grupos inmobiliarios del sur de Brasil",
            "perfil_club": "Naves de diseño cerca de las playas más cotizadas de Santa Catarina",
            "canon_royalties": "Operación directa",
            "inversion_media": "800.000$ a 1.800.000$ por club"
        },
        "diferencial": "Localización en la zona de mayor crecimiento inmobiliario de Brasil y sinergia con el estilo de vida playero."
    },
    {
        "id": "delta-padel",
        "nombre": "Delta Padel Brasil",
        "pais": "Brasil",
        "pais_codigo": "BR",
        "region_filtro": "MX",
        "bandera": "🇧🇷",
        "ciudad_sede": "Porto Alegre / Caxias do Sul",
        "coords": [-30.0346, -51.2177],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 macrocentros gauchos",
        "num_pistas": "16+ pistas cubiertas",
        "software": "Playtomic",
        "fundadores": "Delta Sports Rio Grande do Sul",
        "web": "https://deltapadel.com.br",
        "tagline": "Pistas cubiertas de alta competición en el corazón gaucho de Rio Grande do Sul.",
        "resumen": "Cadena gaúcha en Porto Alegre y la sierra de Caxias do Sul con naves cubiertas que han formado a varias de las mejores palas de la selección brasileña de pádel.",
        "sedes_principales": [
            "Delta Padel Porto Alegre (8 pistas cubiertas)",
            "Delta Padel Caxias do Sul"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de cristal con climatización",
            "software": "Playtomic",
            "domotica": "Acceso inteligente",
            "grabacion": "Vídeo en torneos",
            "restauracion": "Churrasquería lounge y tienda especializada"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios",
            "perfil_club": "Naves industriales",
            "canon_royalties": "Operación directa",
            "inversion_media": "600.000$ a 1.200.000$"
        },
        "diferencial": "Tradición histórica del pádel en el estado más padelero de Brasil (Rio Grande do Sul)."
    }
]

print(f"Cargadas {len(LATAM_LIST)} cadenas de Latinoamérica.")

# =========================================================================
# 🇦🇪 ORIENTE MEDIO: EAU, QATAR, ARABIA SAUDÍ Y KUWAIT (7 Cadenas)
# =========================================================================
ME_LIST = [
    {
        "id": "padel-in",
        "nombre": "Padel IN",
        "pais": "Catar",
        "pais_codigo": "QA",
        "region_filtro": "AE",
        "bandera": "🇶🇦",
        "ciudad_sede": "Doha / Kuwait / Riad",
        "coords": [25.2854, 51.5310],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "12 macrocomplejos climatizados",
        "num_pistas": "70+ pistas cubiertas",
        "software": "Padel IN App / Playtomic",
        "fundadores": "Empresarios de la familia real qatarí y socios saudíes",
        "web": "https://thepadelin.com",
        "tagline": "El gigante de Oriente Medio con macrocomplejos climatizados en Doha, Kuwait y Riad.",
        "resumen": "Padel IN es la mayor cadena de pádel del Golfo Pérsico. Nació en Doha (Aspire Zone y City Center) y se expandió con enorme fuerza a Kuwait y Arabia Saudí (Riad y Al Khobar). Cada centro es un megapabellón 100% climatizado a 21°C para jugar en pleno desierto a 50°C en el exterior.",
        "sedes_principales": [
            "Padel IN Aspire Zone (Doha - 10 pistas cubiertas climatizadas)",
            "Padel IN City Center Doha",
            "Padel IN Kuwait Shuwaikh",
            "Padel IN Riad (Arabia Saudí)",
            "Padel IN Al Khobar (Arabia Saudí)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas oficiales de cristal templado de 12mm y aire acondicionado monumental",
            "software": "App propia Padel IN integrada con torneos del Golfo",
            "domotica": "Acceso VIP automatizado y climatización industrial continua",
            "grabacion": "Cámaras 4K en todas las pistas para descarga de partidos",
            "restauracion": "Cafetería de lujo con café arábica y de especialidad, zumos naturales y pro-shop con palas doradas y ediciones limitadas"
        },
        "modelo_expansion": {
            "tipo_contrato": "Megacomplejos corporativos propios con capital institucional del Golfo",
            "perfil_club": "Pabellones gigantescos de más de 5.000 m² con techos de 12 metros",
            "canon_royalties": "Operación directa",
            "inversion_media": "3.000.000$ a 7.000.000$ por club"
        },
        "diferencial": "Infraestructura monumental para combatir el calor extremo del desierto y patrocinios millonarios."
    },
    {
        "id": "world-padel-academy",
        "nombre": "World Padel Academy (WPA)",
        "pais": "Emiratos Árabes",
        "pais_codigo": "AE",
        "region_filtro": "AE",
        "bandera": "🇦🇪",
        "ciudad_sede": "Dubái (Al Quoz) / Sharjah / Baréin",
        "coords": [25.1300, 55.2300],
        "modelo": "Academia & Pro-Shop",
        "modelo_badge": "bg-amber-100 text-amber-800 border-amber-200",
        "tipo_categoria": "academia",
        "escala": "macro",
        "num_clubs": "4 macroacademias",
        "num_pistas": "45+ pistas cubiertas",
        "software": "WPA App / Playtomic",
        "fundadores": "World Padel Academy Management Dubai",
        "web": "https://worldpadelacademy.ae",
        "tagline": "El centro de alto rendimiento de pádel más avanzado de Dubái y los Emiratos.",
        "resumen": "World Padel Academy opera macrocentros climatizados en Dubái (Al Quoz), Sharjah y Baréin. Cuentan con entrenadores españoles certificados de élite, pistas con gradas para torneos internacionales de la FIP y preparación física específica.",
        "sedes_principales": [
            "WPA Al Quoz (Dubái - 10 pistas cubiertas climatizadas)",
            "WPA Sharjah",
            "WPA Baréin",
            "WPA Mansoura"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de competición con moqueta oficial Premier Padel",
            "software": "App propia WPA y Playtomic",
            "domotica": "Acceso digital automatizado",
            "grabacion": "Sistemas de biomecánica y vídeo en todas las pistas",
            "restauracion": "Healthy bar, cafetería de especialidad y pro-shop de 200m²"
        },
        "modelo_expansion": {
            "tipo_contrato": "Academias corporativas propias en países del Consejo de Cooperación del Golfo",
            "perfil_club": "Naves de 4.000 a 7.000 m²",
            "canon_royalties": "Operación directa",
            "inversion_media": "2.500.000$ a 5.000.000$ por academia"
        },
        "diferencial": "La calidad formativa de su cuerpo técnico español y la organización de torneos FIP de primer nivel."
    },
    {
        "id": "padel-pro-uae",
        "nombre": "Padel Pro UAE",
        "pais": "Emiratos Árabes",
        "pais_codigo": "AE",
        "region_filtro": "AE",
        "bandera": "🇦🇪",
        "ciudad_sede": "Dubái (One Central / Jumeirah Park)",
        "coords": [25.2200, 55.2800],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "3 clubes en Dubái",
        "num_pistas": "20+ pistas",
        "software": "Playtomic",
        "fundadores": "Padel Pro UAE Group",
        "web": "https://padelpro.ae",
        "tagline": "Pistas panorámicas en el distrito financiero One Central del Dubai World Trade Centre.",
        "resumen": "Cadena pionera en Dubái con pistas en One Central (frente al Museo del Futuro en el World Trade Centre), Jumeirah Park y Al Quoz, reuniendo a la élite corporativa de los Emiratos.",
        "sedes_principales": [
            "Padel Pro One Central (DWTC Dubái - vistas al Museo del Futuro)",
            "Padel Pro Jumeirah Park",
            "Padel Pro Al Quoz"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de cristal templado",
            "software": "Playtomic",
            "domotica": "Acceso QR y taquillas electrónicas",
            "grabacion": "Vídeo en torneos",
            "restauracion": "Lounge café corporativo y tienda técnica"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios en ubicaciones prime",
            "perfil_club": "Distritos financieros y residenciales de alto standing",
            "canon_royalties": "Operación directa",
            "inversion_media": "1.500.000$ a 3.000.000$"
        },
        "diferencial": "Vistas icónicas a los rascacielos de Dubái en la sede de One Central."
    },
    {
        "id": "just-padel-uae",
        "nombre": "Just Padel UAE",
        "pais": "Emiratos Árabes",
        "pais_codigo": "AE",
        "region_filtro": "AE",
        "bandera": "🇦🇪",
        "ciudad_sede": "Dubái (Mina Rashid / Kite Beach)",
        "coords": [25.2600, 55.2700],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "4 centros en Dubái y Abu Dhabi",
        "num_pistas": "25+ pistas",
        "software": "Playtomic",
        "fundadores": "Just Padel Sports UAE",
        "web": "https://justpadel.ae",
        "tagline": "Pistas frente al mar en Kite Beach y en el puerto de Mina Rashid en Dubái.",
        "resumen": "Cadena con localizaciones costeras espectaculares en Kite Beach (junto a la playa con vistas al Burj Al Arab), Mina Rashid Marina y Abu Dhabi Yas Island.",
        "sedes_principales": [
            "Just Padel Mina Rashid (Dubái Puerto)",
            "Just Padel Kite Beach (Dubái)",
            "Just Padel Abu Dhabi Yas Island"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas al aire libre y cubiertas tratadas contra la salinidad",
            "software": "Playtomic",
            "domotica": "Acceso QR automatizado",
            "grabacion": "Sistemas para streaming en redes",
            "restauracion": "Juice bars, cafetería de playa y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Concesiones en puertos deportivos y playas de Dubái",
            "perfil_club": "Emplazamientos turísticos icónicos",
            "canon_royalties": "Operación directa",
            "inversion_media": "1.000.000$ a 2.500.000$"
        },
        "diferencial": "El placer de jugar al pádel frente a la playa de Dubái al atardecer."
    },
    {
        "id": "padelx-dubai",
        "nombre": "PADELX Floating Club Dubai",
        "pais": "Emiratos Árabes",
        "pais_codigo": "AE",
        "region_filtro": "AE",
        "bandera": "🇦🇪",
        "ciudad_sede": "Dubái (JLT - Jumeirah Lakes Towers)",
        "coords": [25.0700, 55.1400],
        "modelo": "Boutique & Ultra-Lujo",
        "modelo_badge": "bg-purple-100 text-purple-800 border-purple-200",
        "tipo_categoria": "boutique",
        "escala": "boutique",
        "num_clubs": "2 clubes flotantes y urbanos",
        "num_pistas": "8+ pistas flotantes",
        "software": "Playtomic",
        "fundadores": "PADELX International (Sofie & Christian)",
        "web": "https://padelx.com",
        "tagline": "La primera pista de pádel flotante del mundo sobre el lago urbano de JLT en Dubái.",
        "resumen": "PADELX revolucionó las redes sociales construyendo la primera pista de pádel flotante del mundo sobre el lago de Jumeirah Lakes Towers (JLT) en Dubái. Rodeada de rascacielos y agua, jugar allí es una de las experiencias más virales del deporte mundial.",
        "sedes_principales": [
            "PADELX Floating Club JLT (Dubái - pistas flotantes sobre el lago)",
            "PADELX Dubai Harbour"
        ],
        "tecnologia_pistas": {
            "pistas": "Estructuras flotantes marítimas reforzadas con cristal templado de 12mm",
            "software": "Playtomic",
            "domotica": "Acceso por pasarela flotante y control digital",
            "grabacion": "Cámaras aéreas para vídeos virales de los jugadores",
            "restauracion": "Lounge flotante con zumos naturales, café y tienda boutique"
        },
        "modelo_expansion": {
            "tipo_contrato": "Instalaciones flotantes patentadas en lagos urbanos y puertos deportivos",
            "perfil_club": "Lagos y marinas de alto impacto visual",
            "canon_royalties": "Operación directa",
            "inversion_media": "1.500.000$ a 3.000.000$"
        },
        "diferencial": "La imagen icónica de jugar flotando sobre el agua rodeado de los rascacielos de Dubái."
    },
    {
        "id": "smash-padel-dubai",
        "nombre": "Smash Padel Dubai",
        "pais": "Emiratos Árabes",
        "pais_codigo": "AE",
        "region_filtro": "AE",
        "bandera": "🇦🇪",
        "ciudad_sede": "Dubái (Palm Jumeirah / Al Wasl)",
        "coords": [25.1100, 55.1300],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 centros en Dubái",
        "num_pistas": "12+ pistas",
        "software": "Playtomic",
        "fundadores": "Smash Sports UAE",
        "web": "https://smashpadel.ae",
        "tagline": "Pádel y fitness de diseño en Palm Jumeirah y Al Wasl.",
        "resumen": "Cadena con instalaciones en la icónica isla de la palmera (Palm Jumeirah) y en Al Wasl, integrando pádel cubierto y exterior con gimnasio boutique y cafetería saludable.",
        "sedes_principales": [
            "Smash Padel Palm Jumeirah (Dubái)",
            "Smash Padel Al Wasl"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de calidad de torneo",
            "software": "Playtomic",
            "domotica": "Acceso QR",
            "grabacion": "Vídeo en torneos",
            "restauracion": "Healthy café, batidos de proteínas y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios",
            "perfil_club": "Zonas residenciales prime en Dubái",
            "canon_royalties": "Operación directa",
            "inversion_media": "1.200.000$ a 2.000.000$"
        },
        "diferencial": "Ubicación codiciada en Palm Jumeirah y clientela VIP."
    },
    {
        "id": "padel-26-kuwait",
        "nombre": "Padel 26 Kuwait",
        "pais": "Kuwait",
        "pais_codigo": "KW",
        "region_filtro": "AE",
        "bandera": "🇰🇼",
        "ciudad_sede": "Kuwait City (Shuwaikh)",
        "coords": [29.3500, 47.9500],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "3 macrocomplejos climatizados",
        "num_pistas": "26+ pistas cubiertas",
        "software": "App Propia / Playtomic",
        "fundadores": "Padel 26 Sports Kuwait",
        "web": "https://padel26.com",
        "tagline": "El templo indoor de Kuwait: 26 pistas climatizadas para la fiebre del pádel kuwaití.",
        "resumen": "Kuwait es uno de los países con mayor densidad de jugadores de pádel del mundo per cápita. Padel 26 opera los mayores pabellones climatizados de Shuwaikh y Sabah Al Salem, con canchas repletas hasta las 3 de la madrugada.",
        "sedes_principales": [
            "Padel 26 Shuwaikh (Kuwait City - 14 pistas climatizadas)",
            "Padel 26 Sabah Al Salem"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con aire acondicionado a máxima potencia y moqueta azul",
            "software": "Padel 26 App",
            "domotica": "Control digital de accesos e iluminación",
            "grabacion": "Cámaras 4K en todas las pistas",
            "restauracion": "Coffee lounge kuwaití con postres de autor, té y pro-shop de lujo"
        },
        "modelo_expansion": {
            "tipo_contrato": "Macrocomplejos en propiedad",
            "perfil_club": "Naves de más de 6.000 m²",
            "canon_royalties": "Operación directa",
            "inversion_media": "Más de 4.000.000$"
        },
        "diferencial": "La pasión fanática de los kuwaitíes por el pádel con torneos multitudinarios que reparten premios en metálico sustanciosos."
    }
]

print(f"Cargadas {len(ME_LIST)} cadenas de Oriente Medio.")

# =========================================================================
# 🇿🇦 SUDÁFRICA Y AUSTRALIA (5 Cadenas y Franquicias)
# =========================================================================
ZA_AU_LIST = [
    {
        "id": "virgin-active-padel",
        "nombre": "Virgin Active Padel Club",
        "pais": "Sudáfrica",
        "pais_codigo": "ZA",
        "region_filtro": "ZA",
        "bandera": "🇿🇦",
        "ciudad_sede": "Ciudad del Cabo / Johannesburgo",
        "coords": [-33.9249, 18.4241],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "12+ centros en Sudáfrica",
        "num_pistas": "65+ pistas",
        "software": "Playtomic / Virgin Active App",
        "fundadores": "Sir Richard Branson (Virgin Group)",
        "web": "https://virginactive.co.za",
        "tagline": "El gigante mundial del fitness llevando el pádel a cada rincón de Sudáfrica.",
        "resumen": "Virgin Active ha liderado la explosión del pádel en el continente africano. Tras la adquisición estratégica de Epic Padel, ha instalado decenas de pistas en sus clubes premium de Ciudad del Cabo (Green Point, Paarden Eiland Epicentre, Woodstock, The Glen Country Club Clifton, Durbanville) y Johannesburgo (Randpark Club, Bedfordview, Lonehill Sandton, Huddle Park).",
        "sedes_principales": [
            "Virgin Active Green Point (Ciudad del Cabo)",
            "Virgin Active Epicentre Paarden Eiland (Ciudad del Cabo indoor)",
            "The Glen Country Club Clifton (Ciudad del Cabo con vistas al océano)",
            "Virgin Active Randpark Club (Johannesburgo)",
            "Virgin Active Bedfordview y Lonehill Sandton"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de competición con cristal templado y cubiertas tensoestáticas",
            "software": "Playtomic integrado con los beneficios del carnet Virgin Active",
            "domotica": "Acceso biométrico / RFID de socio Virgin y reserva en app",
            "grabacion": "Cámaras en torneos nacionales",
            "restauracion": "Kauai Juice Bar saludable, piscinas olímpicas, spas y vestuarios de lujo de Virgin Active"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena corporativa con implantación en todos los gimnasios Virgin Active de Sudáfrica",
            "perfil_club": "Gimnasios y clubes de golf con suelo disponible",
            "canon_royalties": "Operación directa corporativa",
            "inversion_media": "500.000$ a 1.500.000$ por instalación"
        },
        "diferencial": "El respaldo y la base de socios del mayor operador de fitness de Sudáfrica (Virgin Active)."
    },
    {
        "id": "africa-padel",
        "nombre": "Africa Padel",
        "pais": "Sudáfrica",
        "pais_codigo": "ZA",
        "region_filtro": "ZA",
        "bandera": "🇿🇦",
        "ciudad_sede": "Ciudad del Cabo / Sandton",
        "coords": [-33.9500, 18.3800],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "12 centros en Sudáfrica",
        "num_pistas": "60+ pistas",
        "software": "Playtomic",
        "fundadores": "Africa Padel Operations",
        "web": "https://africapadel.com",
        "tagline": "Pistas espectaculares en Camps Bay, V&A Waterfront y los mejores enclaves sudafricanos.",
        "resumen": "Africa Padel es la cadena independiente más grande de África. Sus clubes están ubicados en los lugares más turísticos y exclusivos del país: Camps Bay (a los pies de los Doce Apóstoles y la playa), V&A Waterfront (puerto de Ciudad del Cabo), Claremont, Stellenbosch, Sandton German Club y Pretoria.",
        "sedes_principales": [
            "Africa Padel Camps Bay (frente a la playa de Camps Bay)",
            "Africa Padel V&A Waterfront (puerto de Ciudad del Cabo)",
            "Africa Padel Claremont (Herschel Close)",
            "Africa Padel Sandton / Paulshof (German Country Club)",
            "Africa Padel Pretoria Brooklyn y Stellenbosch"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de cristal con césped texturizado azul",
            "software": "Playtomic",
            "domotica": "Acceso QR y taquillas seguras",
            "grabacion": "Streaming de torneos africanos",
            "restauracion": "Clubhouse con café barista, batidos frescos, cervezas sudafricanas y tienda pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena de clubes propios en lugares de alta atracción turística",
            "perfil_club": "Parcelas costeras y clubes de tenis emblemáticos",
            "canon_royalties": "Operación directa",
            "inversion_media": "600.000$ a 1.400.000$ por club"
        },
        "diferencial": "Las vistas inolvidables de Camps Bay y la mejor atmósfera social de Ciudad del Cabo."
    },
    {
        "id": "indoor-padel-australia",
        "nombre": "Indoor Padel Australia",
        "pais": "Australia",
        "pais_codigo": "AU",
        "region_filtro": "ZA",
        "bandera": "🇦🇺",
        "ciudad_sede": "Sídney (Alexandria / Cromer)",
        "coords": [-33.9000, 151.1900],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "2 macrocentros en Sídney",
        "num_pistas": "16+ pistas",
        "software": "Playtomic",
        "fundadores": "Indoor Padel Australia Group",
        "web": "https://indoorpadel.com.au",
        "tagline": "El pionero de los macrocomplejos cubiertos en Australia: 10 pistas en Sídney Alexandria.",
        "resumen": "Indoor Padel Australia trajo la revolución del pádel a Sídney. Su buque insignia en Alexandria es uno de los mayores complejos de Australia con 10 pistas (8 indoor y 2 outdoor), además de su centro cubierto en Cromer (Northern Beaches).",
        "sedes_principales": [
            "Indoor Padel Alexandria (Sídney - 10 pistas de competición)",
            "Indoor Padel Cromer (Northern Beaches de Sídney - 4 pistas cubiertas)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas cubiertas en naves de gran altura y césped azul Premier Padel",
            "software": "Playtomic",
            "domotica": "Acceso autónomo con código digital",
            "grabacion": "Sistemas para ligas federadas de Padel Australia",
            "restauracion": "Clubhouse australiano con café flat white de barista, cervezas artesanales y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena corporativa pionera en Australia",
            "perfil_club": "Naves industriales urbanas de más de 3.500m² en Sídney y Melbourne",
            "canon_royalties": "Operación directa",
            "inversion_media": "1.200.000$ a 2.500.000$ por centro"
        },
        "diferencial": "El primer gran centro cubierto de Sídney (Alexandria) que protege del sol abrasador y las lluvias torrenciales australianas."
    },
    {
        "id": "tribe-padel",
        "nombre": "Tribe Padel & Wellness",
        "pais": "Australia",
        "pais_codigo": "AU",
        "region_filtro": "ZA",
        "bandera": "🇦🇺",
        "ciudad_sede": "Sídney / Melbourne",
        "coords": [-33.7900, 151.1300],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 centros interestatales",
        "num_pistas": "10+ pistas",
        "software": "Playtomic",
        "fundadores": "Tribe Padel Australia",
        "web": "https://tribepadel.com.au",
        "tagline": "Pádel y bienestar integral en las dos mayores ciudades de Australia.",
        "resumen": "Operador que combina el pádel con actividades de bienestar y yoga en Tennis World North Ryde (Sídney) y en Cheltenham (Melbourne).",
        "sedes_principales": [
            "Tribe Padel North Ryde (Sídney)",
            "Tribe Padel Melbourne (Cheltenham)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con césped texturizado",
            "software": "Playtomic",
            "domotica": "Control digital de pistas",
            "grabacion": "Vídeo en torneos",
            "restauracion": "Café orgánico, kombucha y zona wellness"
        },
        "modelo_expansion": {
            "tipo_contrato": "Alianzas en complejos de tenis tradicionales",
            "perfil_club": "Centros de raqueta consolidados",
            "canon_royalties": "Operación directa",
            "inversion_media": "500.000$ a 1.000.000$"
        },
        "diferencial": "Presencia interestatal simultánea en Nueva Gales del Sur y Victoria."
    },
    {
        "id": "one-padel-australia",
        "nombre": "One Padel Australia",
        "pais": "Australia",
        "pais_codigo": "AU",
        "region_filtro": "ZA",
        "bandera": "🇦🇺",
        "ciudad_sede": "Sídney / Brisbane",
        "coords": [-33.8688, 151.2093],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 centros",
        "num_pistas": "12+ pistas",
        "software": "Playtomic",
        "fundadores": "One Padel Management",
        "web": "https://onepadel.com.au",
        "tagline": "Pistas panorámicas de torneo en la costa este australiana.",
        "resumen": "Cadena en rápida expansión con pistas panorámicas de última generación y escuelas dirigidas por entrenadores hispano-australianos en Sídney y Queensland.",
        "sedes_principales": [
            "One Padel Sídney",
            "One Padel Brisbane"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas de competición panorámicas",
            "software": "Playtomic",
            "domotica": "Acceso QR y reserva autónoma",
            "grabacion": "Cámaras en torneos",
            "restauracion": "Bar terraza y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios",
            "perfil_club": "Suelos deportivos periurbanos",
            "canon_royalties": "Operación directa",
            "inversion_media": "550.000$ a 1.100.000$"
        },
        "diferencial": "Comunidad muy activa de expatriados y tenistas locales reconvertidos al pádel."
    }
]

print(f"Cargadas {len(ZA_AU_LIST)} cadenas de Sudáfrica y Australia.")
