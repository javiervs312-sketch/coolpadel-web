# -*- coding: utf-8 -*-
"""
Base de datos de 106 cadenas multiclub (+1 club abierto bajo la misma marca) y franquicias de pádel a nivel mundial.
"""

# Total de entidades: 126
FRANQUICIAS = [
    {
        "id": "padelstars-uk",
        "nombre": "PadelStars UK",
        "pais": "Reino Unido",
        "pais_codigo": "GB",
        "region_filtro": "GB",
        "bandera": "🇬🇧",
        "ciudad_sede": "Basildon / South East",
        "coords": [
            51.5761,
            0.4887
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "16+ centros operativos y en obras",
        "num_pistas": "65+ pistas",
        "software": "Padelstars App / Playtomic",
        "fundadores": "PadelStars Leisure Group",
        "web": "https://padelstars.co.uk",
        "tagline": "La mayor red multiclub de pádel con cubiertas all-weather en el sur de Inglaterra.",
        "resumen": "PadelStars opera una de las redes multiclub de crecimiento más rápido del Reino Unido bajo una sola marca. Sus centros combinan pistas cubiertas con carpas tensoras y pistas descubiertas de última generación, con una app propia que ofrece bonos monedero, ligas locales y reserva inmediata.",
        "sedes_principales": [
            "Cockfosters / Barnet (Londres Norte - 6 pistas cubiertas de competición)",
            "Watford Woodside Playing Fields (5 pistas de pádel)",
            "Southampton / Eastleigh Stoneham Lane (4 pistas cubiertas + 2 exteriores)",
            "Guildford Surrey Sports Park (4 pistas panorámicas)",
            "Chigwell / Woodford (4 pistas cubiertas)",
            "Bracknell Binfield (3 cubiertas + 1 exterior)",
            "Chichester College Westgate (3 pistas exteriores)",
            "Basildon, Bournemouth Ferndown, Reading, St Albans, Stratford-upon-Avon, Taunton"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con césped texturizado monofilamento y carpas tensoestáticas anti-lluvia",
            "software": "Padelstars Mobile App y Playtomic",
            "domotica": "Acceso QR autónomo, encendido inteligente de proyectores LED",
            "grabacion": "Torres preparadas para streaming de ligas locales",
            "restauracion": "Clubhouse café, zona social y pro-shop con palas de test"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena propia y acuerdos de concesión en complejos deportivos y colegios",
            "perfil_club": "Centros multideportivos, campus universitarios y naves de 4 a 8 pistas",
            "canon_royalties": "Operación directa corporativa",
            "inversion_media": "350.000£ a 850.000£ por centro"
        },
        "diferencial": "Especialistas en transformar suelo deportivo municipal o universitario en hubs de pádel protegidos contra la climatología británica."
    },
    {
        "id": "lets-go-padel",
        "nombre": "Let's Go Padel",
        "pais": "Reino Unido",
        "pais_codigo": "GB",
        "region_filtro": "GB",
        "bandera": "🇬🇧",
        "ciudad_sede": "Belfast / Carryduff",
        "coords": [
            54.52,
            -5.92
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "10 centros",
        "num_pistas": "35+ pistas",
        "software": "Playtomic / App Propia",
        "fundadores": "Let's Go Group (Peter Boyle)",
        "web": "https://letsgopadel.com",
        "tagline": "El operador número 1 de Irlanda del Norte, famoso por su pista flotante sobre embalse.",
        "resumen": "Cadena pionera de pádel en Irlanda del Norte que ha revolucionado el ocio deportivo británico. Su buque insignia en Let's Go Hydro (Carryduff) cuenta con pistas cubiertas y la primera pista flotante de pádel sobre un lago en las Islas Británicas, además de centros urbanos en Belfast y grandes localidades.",
        "sedes_principales": [
            "Carryduff Flagship (Let's Go Hydro - pistas cubiertas + pista flotante en embalse)",
            "Belfast Hillview Retail Park (Crumlin Road)",
            "Belfast Weavers Cross (Great Victoria Street)",
            "East Belfast Urban Hub",
            "Derry / Londonderry",
            "Ballyclare, Newry, Omagh y Ballygawley"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas all-weather y estructuras flotantes marinas patentadas",
            "software": "Playtomic integrado con el ecosistema de ocio de Let's Go Hydro",
            "domotica": "Acceso contactless, iluminación automática programada",
            "grabacion": "Grabación de partidos en eventos corporativos y torneos",
            "restauracion": "Pizzerías artesanales, cafeterías de especialidad y waterpark resorts"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena corporativa con expansión en parques comerciales y resorts",
            "perfil_club": "Retail parks urbanos y resorts de turismo activo",
            "canon_royalties": "Gestión directa del grupo",
            "inversion_media": "300.000£ a 700.000£ por ubicación"
        },
        "diferencial": "Instalaciones icónicas experienciales (pista flotante) y sinergia con centros comerciales y parques acuáticos."
    },
    {
        "id": "the-padel-hub",
        "nombre": "The Padel Hub (PADELHUB)",
        "pais": "Reino Unido",
        "pais_codigo": "GB",
        "region_filtro": "GB",
        "bandera": "🇬🇧",
        "ciudad_sede": "Slough / Reading",
        "coords": [
            51.5105,
            -0.595
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "9 centros indoor",
        "num_pistas": "55+ pistas indoor",
        "software": "Playtomic",
        "fundadores": "The Padel Hub Ltd",
        "web": "https://padelhub.uk",
        "tagline": "La mayor red de pádel 100% cubierto y climatizado del Home Counties y Londres.",
        "resumen": "The Padel Hub se ha consolidado como el referente indoor de alta gama en Inglaterra. Opera grandes complejos naves logísticas adaptadas con techos de 9 a 11 metros libres, pistas panorámicas de competición, gimnasio para jugadores, coworking y cafeterías de ambiente distendido.",
        "sedes_principales": [
            "Slough (Albion Close - club insignia de 5 pistas cubiertas de gran altura)",
            "Reading (Kenavon Drive / Forbury Business Park)",
            "Fleet (Beacon Hill Logistics Park)",
            "Epsom (Blenheim Road)",
            "Southampton (Adanac Trade Park)",
            "Tunbridge Wells (Chapman Way)",
            "Crawley, North / Northwest London y Bristol"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas cubiertas superpanorámicas con césped Mondo Supercourt XN oficial WPT/Premier",
            "software": "Playtomic integrado con reservas de pista y torneos Americano",
            "domotica": "Climatización industrial inteligente, control de humedad y acceso digital",
            "grabacion": "Cámaras cenitales para análisis técnico de entrenadores",
            "restauracion": "Lounge bar con café barista, batidos proteicos y pro-shop boutique"
        },
        "modelo_expansion": {
            "tipo_contrato": "Red corporativa de clubes propios con inversión institucional",
            "perfil_club": "Naves industriales y parques logísticos de 2.000m² a 4.000m² con altura libre >8m",
            "canon_royalties": "Propiedad y operación directa",
            "inversion_media": "800.000£ a 1.500.000£ por centro"
        },
        "diferencial": "Compromiso absoluto con el pádel cubierto (sin cancelaciones por lluvia) y experiencia club social premium."
    },
    {
        "id": "pure-padel",
        "nombre": "Pure Padel",
        "pais": "Reino Unido",
        "pais_codigo": "GB",
        "region_filtro": "GB",
        "bandera": "🇬🇧",
        "ciudad_sede": "Mánchester",
        "coords": [
            53.49,
            -2.24
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "9 centros",
        "num_pistas": "40+ pistas",
        "software": "Playtomic",
        "fundadores": "Sammy Arora & Pure Padel Group",
        "web": "https://purepadelclubs.co.uk",
        "tagline": "El operador multiclub que está democratizando el pádel en el norte y centro de Inglaterra.",
        "resumen": "Cadena multiclub nacida en el Gran Mánchester enfocada en crear clubes sociales accesibles para todos los niveles, integrando pádel cubierto, academias juveniles y eventos after-work con música en vivo y gastronomía informal.",
        "sedes_principales": [
            "Manchester Cheetham Hill (indoor arena)",
            "Alderley Edge (Cheshire Golden Triangle)",
            "Macclesfield Urban Club",
            "Birmingham",
            "Sheffield",
            "Crewe y Wilmslow"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de cristal templado de 12mm con iluminación LED antideslumbrante",
            "software": "Playtomic",
            "domotica": "Puertas automáticas con código QR en app y taquillas electrónicas",
            "grabacion": "Pistas con soporte para cámaras y retransmisión de torneos locales",
            "restauracion": "Cafetería bistró, cervezas artesanas locales y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Desarrollo multisede propio con capital privado",
            "perfil_club": "Almacenes urbanos y terrenos suburbanos de 4 a 10 pistas",
            "canon_royalties": "Gestión centralizada",
            "inversion_media": "450.000£ a 900.000£"
        },
        "diferencial": "Gran conexión con la comunidad de jugadores locales y dinamización constante de eventos sociales."
    },
    {
        "id": "padel-people-uk",
        "nombre": "Padel People UK",
        "pais": "Reino Unido",
        "pais_codigo": "GB",
        "region_filtro": "GB",
        "bandera": "🇬🇧",
        "ciudad_sede": "Londres / Sur de Inglaterra",
        "coords": [
            51.433,
            -0.198
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "7 centros",
        "num_pistas": "28+ pistas",
        "software": "Playtomic / App Propia",
        "fundadores": "Padel People UK Operations",
        "web": "https://padelpeople.co.uk",
        "tagline": "Pádel accesible integrado en espacios boutique de fitness y clubes locales.",
        "resumen": "Operador británico enfocado en acercar el pádel a poblaciones intermedias y clubes de fitness. Destaca su instalación boutique en Wimbledon (dentro del centro Hybrid Fitness en Plough Lane) y sedes en Hampshire, Wiltshire, Somerset y Dorset.",
        "sedes_principales": [
            "Wimbledon (Londres - Hybrid Fitness Plough Lane)",
            "Basingstoke (Hampshire)",
            "Sedlescombe (East Sussex)",
            "Shepton Mallet (Somerset)",
            "Corsham (Wiltshire)",
            "Wimborne y Cricklade"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con estructura reforzada para viento exterior e interiores compactos",
            "software": "Playtomic y plataforma web directa",
            "domotica": "Control digital de iluminación y accesos",
            "grabacion": "Sistemas para revisión de clases particulares",
            "restauracion": "Espacio social fitness y venta de pelotas y accesorios"
        },
        "modelo_expansion": {
            "tipo_contrato": "Alianzas con operadores de gimnasios y complejos deportivos",
            "perfil_club": "Instalaciones de 2 a 6 pistas optimizando suelo existente",
            "canon_royalties": "Modelo compartido de ingresos",
            "inversion_media": "180.000£ a 450.000£ por centro"
        },
        "diferencial": "Capilaridad en localidades residenciales donde las grandes cadenas no llegan y sinergia directa con gimnasios."
    },
    {
        "id": "smash-padel-uk",
        "nombre": "Smash Padel UK",
        "pais": "Reino Unido",
        "pais_codigo": "GB",
        "region_filtro": "GB",
        "bandera": "🇬🇧",
        "ciudad_sede": "Oxfordshire / Cardiff",
        "coords": [
            51.898,
            -1.155
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "6 centros",
        "num_pistas": "28+ pistas",
        "software": "Playtomic",
        "fundadores": "Smash Padel Ltd",
        "web": "https://smashpadel.co",
        "tagline": "Clubes panorámicos de alta competición y formación de cantera en UK y Gales.",
        "resumen": "Cadena que destaca por la calidad de sus pistas y su apuesta por el pádel juvenil y de competición. Su sede de Cardiff en Llandaff Fields es la referencia galesa (sede de torneos FIP Promises), complementada con clubes en Bicester Golf Resort, Eltham (Londres) y Mid Sussex.",
        "sedes_principales": [
            "Cardiff Llandaff Fields (Pontcanna - sede oficial de torneos FIP Promises)",
            "Bicester Hotel Golf & Spa (pistas panorámicas cubiertas con carpas)",
            "Eltham (Londres - centro indoor con academia)",
            "Mid Sussex (Haywards Heath Whitemans Green en alianza con club de rugby)",
            "Oxford City Club"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de calidad FIP con cubiertas tensadas y césped de competición",
            "software": "Playtomic",
            "domotica": "Acceso QR y gestión de luz automática",
            "grabacion": "Sistemas de retransmisión oficial FIP",
            "restauracion": "Resort lounge en Bicester y cafeterías de club en el resto"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios y partnerships con clubes de golf y rugby",
            "perfil_club": "Resorts deportivos y clubes sociales con 4 a 8 pistas",
            "canon_royalties": "Explotación propia",
            "inversion_media": "350.000£ a 750.000£"
        },
        "diferencial": "Gran prestigio federativo y programas de tecnificación para jóvenes promesas del pádel británico."
    },
    {
        "id": "vida-del-padel",
        "nombre": "Vida Del Padel",
        "pais": "Reino Unido",
        "pais_codigo": "GB",
        "region_filtro": "GB",
        "bandera": "🇬🇧",
        "ciudad_sede": "Londres / Surrey",
        "coords": [
            51.5074,
            -0.1278
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "6 clubes y sedes de liga",
        "num_pistas": "24+ pistas",
        "software": "Vida Del Padel App / Playtomic",
        "fundadores": "Vida Del Padel Ltd",
        "web": "https://vidadelpadel.com",
        "tagline": "La marca de estilo de vida que une la cultura ibérica de club con el pádel británico.",
        "resumen": "Cadena y comunidad lifestyle inspirada en el ambiente social de los clubes de Madrid y Barcelona. Gestiona clubes y ligas unificadas bajo el nombre Vida Del Padel League, destacando por su cuidada dirección artística, ropa técnica y eventos con tapas y música.",
        "sedes_principales": [
            "Londres Suroeste (hubs asociados)",
            "Surrey Padel Center",
            "Bristol Lifestyle Club",
            "Vida Del Padel League venues en el área metropolitana"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas con estética personalizada y acabados en negro y madera",
            "software": "App propia Vida Del Padel con sistema de lealtad y Playtomic",
            "domotica": "Tornos y registro en app móvil",
            "grabacion": "Highlights en video para redes sociales de la comunidad",
            "restauracion": "Tapas españolas, sangría, café premium y terraza social"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena de marca y franquicia de experiencia de club",
            "perfil_club": "Centros urbanos con alta densidad de expatriados y profesionales",
            "canon_royalties": "Royalties de marca y app centralizada",
            "inversion_media": "300.000£ a 600.000£"
        },
        "diferencial": "Potentísima imagen de marca, moda de pádel y ambiente festivo-social mediterráneo."
    },
    {
        "id": "social-sports-society",
        "nombre": "Social Sports Society (S3 Padel)",
        "pais": "Reino Unido",
        "pais_codigo": "GB",
        "region_filtro": "GB",
        "bandera": "🇬🇧",
        "ciudad_sede": "Londres",
        "coords": [
            51.556,
            -0.2795
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "5 centros urbanos",
        "num_pistas": "26+ pistas",
        "software": "Playtomic / S3 App",
        "fundadores": "Social Sports Society Ltd",
        "web": "https://socialsportssociety.com",
        "tagline": "Hubs deportivos urbanos integrados en los mayores desarrollos inmobiliarios de Londres.",
        "resumen": "S3 Padel crea clubes de pádel en emplazamientos urbanos de máximo nivel. Su sede de Wembley Park está situada junto al icónico estadio de fútbol en pleno bulevar peatonal. Cuentan además con centros en el London Cancer Hub (Sutton), Bristol Filton, Derby y Mánchester.",
        "sedes_principales": [
            "Wembley Park (Londres - junto a Wembley Stadium Boulevard)",
            "Sutton (London Cancer Hub / Royal Marsden grounds - 4 pistas)",
            "Bristol Filton Park",
            "Derby (Eagle Market Derbion - gran centro indoor en el centro urbano)",
            "Mánchester Urban Hub"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas iluminadas con focos LED de alta potencia e impacto visual urbano",
            "software": "Playtomic y S3 Community Portal",
            "domotica": "Acceso 100% digital, iluminación de bajo consumo",
            "grabacion": "Cámaras para repetición de puntos clave",
            "restauracion": "Contenedores gastronómicos pop-up, cafetería y chill-out"
        },
        "modelo_expansion": {
            "tipo_contrato": "Alianzas de regeneración urbana con grandes fondos inmobiliarios (placemaking)",
            "perfil_club": "Suelos urbanos en transformación y centros comerciales",
            "canon_royalties": "Operación directa",
            "inversion_media": "500.000£ a 1.200.000£"
        },
        "diferencial": "Ubicaciones icónicas de alta visibilidad (Wembley, centros comerciales) que convierten el pádel en el corazón del barrio."
    },
    {
        "id": "the-padel-club-uk",
        "nombre": "The Padel Club",
        "pais": "Reino Unido",
        "pais_codigo": "GB",
        "region_filtro": "GB",
        "bandera": "🇬🇧",
        "ciudad_sede": "Wilmslow / Mánchester",
        "coords": [
            53.328,
            -2.23
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "5 centros",
        "num_pistas": "35+ pistas",
        "software": "Playtomic",
        "fundadores": "Kris Ball & The Padel Club Investors",
        "web": "https://thepadelclub.co.uk",
        "tagline": "El creador del mayor mega-complejo de pádel cubierto del norte de Inglaterra en TraffordCity.",
        "resumen": "Cadena británica de referencia respaldada por atletas y figuras del fútbol del norte de Inglaterra. Tras su éxito pionero en Wilmslow, construyeron en TraffordCity (Mánchester) un macrocomplejo de 11 pistas indoor de competición con casa club de diseño escandinavo y zona wellness.",
        "sedes_principales": [
            "TraffordCity Mánchester (11 pistas indoor de competición, megadesarrollo)",
            "Wilmslow (Cheshire - buque insignia al aire libre y cubierto)",
            "Gloucester Urban Club",
            "Cheshire East Expansion",
            "North West Regional Hub"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con césped texturizado azul, pistas centrales con grada",
            "software": "Playtomic",
            "domotica": "Check-in biométrico / código digital, climatización eficiente",
            "grabacion": "Sistema de repetición y streaming de torneos nacionales",
            "restauracion": "Clubhouse premium con barista, kombucha, cerveza fría y pro-shop completa"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios financiados con rondas de capital privado de alto nivel",
            "perfil_club": "Macroproyectos en destinos turísticos o comerciales de primer orden",
            "canon_royalties": "Gestión corporativa unificada",
            "inversion_media": "1.000.000£ a 3.000.000£ por megaproyecto"
        },
        "diferencial": "Instalaciones monumentales (TraffordCity) y respaldo de deportistas profesionales de la Premier League."
    },
    {
        "id": "slazenger-padel",
        "nombre": "Slazenger Padel Clubs",
        "pais": "Reino Unido",
        "pais_codigo": "GB",
        "region_filtro": "GB",
        "bandera": "🇬🇧",
        "ciudad_sede": "Leeds / West Yorkshire",
        "coords": [
            53.7997,
            -1.5492
        ],
        "modelo": "Franquicia Llave en Mano",
        "modelo_badge": "bg-indigo-100 text-indigo-800 border-indigo-200",
        "tipo_categoria": "franquicia",
        "escala": "macro",
        "num_clubs": "4 megaplexes indoor",
        "num_pistas": "35+ pistas indoor",
        "software": "Playtomic",
        "fundadores": "Slazenger Heritage Brand Licensing",
        "web": "https://slazengerpadelclubs.com",
        "tagline": "La mítica marca británica de raqueta aplicada a macrocentros cubiertos de pádel.",
        "resumen": "Aprovechando más de 140 años de historia en los deportes de raqueta británicos, Slazenger ha lanzado su división de clubes propios. Su club de Leeds South (Seacroft) es colosal, con 14 pistas de pádel 100% cubiertas bajo una sola nave logística, pro-shop con toda la gama Slazenger Padel y escuela oficial.",
        "sedes_principales": [
            "Leeds South (Seacroft - macrocomplejo de 14 pistas indoor cubiertas)",
            "Leeds North Arena",
            "Blackburn Indoor Club",
            "Yorkshire Central"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas oficiales Slazenger con moqueta de competición",
            "software": "Playtomic",
            "domotica": "Acceso autónomo con tornos y luces LED inteligentes",
            "grabacion": "Cámaras para torneos de la LTA (Lawn Tennis Association)",
            "restauracion": "Slazenger Lounge Bar, zona de restauración y tienda monomarca"
        },
        "modelo_expansion": {
            "tipo_contrato": "Franquicia y centros corporativos con el sello Slazenger",
            "perfil_club": "Naves de gran formato (>3.500m²) con mínimo 10 pistas",
            "canon_royalties": "Canon de marca + royalties de facturación",
            "inversion_media": "1.200.000£ a 2.500.000£"
        },
        "diferencial": "El peso y la confianza de una de las marcas deportivas británicas más legendarias del mundo."
    },
    {
        "id": "rocket-padel",
        "nombre": "Rocket Padel",
        "pais": "Reino Unido",
        "pais_codigo": "GB",
        "region_filtro": "GB",
        "bandera": "🇬🇧",
        "ciudad_sede": "Londres / Bristol",
        "coords": [
            51.4545,
            -2.5879
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "4 macrocentros",
        "num_pistas": "45+ pistas",
        "software": "Playtomic / Matchi",
        "fundadores": "Sebastian Gordon & Fredrik Kristensson",
        "web": "https://rocketpadel.com",
        "tagline": "El gigante escandinavo que construyó el club de pádel más grande de todo Reino Unido.",
        "resumen": "Cadena de origen sueco que ha llevado la escala industrial al Reino Unido. Su centro de Bristol (St Anne's) cuenta con 14 pistas cubiertas y es el mayor del país. En Londres operan el icónico Rocket Padel Battersea (en la Cupra Arena), Ilford (12 pistas) y Beckton.",
        "sedes_principales": [
            "Bristol St Anne's (14 pistas cubiertas - el mayor club del Reino Unido)",
            "Battersea London Cupra Arena (4 pistas panorámicas con vistas al Támesis)",
            "Ilford East London (12 pistas cubiertas)",
            "Beckton Central"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de 10 metros de altura libre, moqueta texturizada azul",
            "software": "Playtomic y Matchi",
            "domotica": "Acceso QR, taquillas electrónicas y climatización",
            "grabacion": "Pistas con cámaras HD y pantallas en pista para repetición",
            "restauracion": "Restaurante con comida saludable, café premium y pro-shop de 200m²"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena de clubes propios con socios institucionales",
            "perfil_club": "Macro-almacenes logísticos urbanos de 3.000m² a 6.000m²",
            "canon_royalties": "Cadena propia",
            "inversion_media": "1.500.000£ a 3.500.000£"
        },
        "diferencial": "Capacidad para absorber torneos internacionales masivos y patrocinios de marcas globales como CUPRA."
    },
    {
        "id": "court-de-padel",
        "nombre": "Court De Padel",
        "pais": "Reino Unido",
        "pais_codigo": "GB",
        "region_filtro": "GB",
        "bandera": "🇬🇧",
        "ciudad_sede": "Norwich / Hull",
        "coords": [
            52.6309,
            1.2974
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "3 centros indoor premium",
        "num_pistas": "18+ pistas",
        "software": "Playtomic",
        "fundadores": "Court De Padel Ltd",
        "web": "https://courtdepadel.com",
        "tagline": "Clubes de pádel superpanorámico integrados con centros de bienestar y pickleball.",
        "resumen": "Cadena especializada en naves cubiertas premium con pistas super-panorámicas sin marcos intermedios de cristal. Su club de Norwich cuenta con 8 pistas (dobles e individuales), zona de pilates y fisioterapia, mientras que en Hull operan el único club indoor de la ciudad junto a pistas de pickleball.",
        "sedes_principales": [
            "Norwich (Whiffler Road - 6 pistas dobles + 2 individuales + centro de bienestar)",
            "Hull (Indoor Arena - único centro cubierto de la ciudad con pickleball)",
            "East Anglia Regional Hub"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas super-panorámicas sin pilares de esquina, cristal templado de 12mm",
            "software": "Playtomic",
            "domotica": "Acceso automatizado y control térmico",
            "grabacion": "Sistemas de grabación para análisis de técnica",
            "restauracion": "Café bar social, zumos cold-pressed y tienda especializada"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena propia con enfoque en ciudades intermedias no saturadas",
            "perfil_club": "Naves de 1.500 a 3.000m²",
            "canon_royalties": "Operación directa",
            "inversion_media": "500.000£ a 1.000.000£"
        },
        "diferencial": "Integración del bienestar integral (fisioterapia, pilates) y pistas individuales para clases."
    },
    {
        "id": "padium-london",
        "nombre": "Padium",
        "pais": "Reino Unido",
        "pais_codigo": "GB",
        "region_filtro": "GB",
        "bandera": "🇬🇧",
        "ciudad_sede": "Londres (Canary Wharf)",
        "coords": [
            51.5054,
            -0.0235
        ],
        "modelo": "Boutique & Ultra-Lujo",
        "modelo_badge": "bg-purple-100 text-purple-800 border-purple-200",
        "tipo_categoria": "boutique",
        "escala": "boutique",
        "num_clubs": "2 centros de ultra-lujo",
        "num_pistas": "15+ pistas",
        "software": "Padel Mates",
        "fundadores": "Martin Rache & Canary Wharf Group",
        "web": "https://padium.com",
        "tagline": "El club de pádel más exclusivo de Londres, con IA en pista y servicio de toallas y spa.",
        "resumen": "Ubicado en el epicentro financiero de Canary Wharf, Padium es el club de mayor estándar del Reino Unido. Diseñado con techos de más de 10 metros, cuenta con 9 pistas AFP panorámicas (7 indoor y 2 exteriores) con tecnología Smart Court de inteligencia artificial, vestuarios con servicio de toallas y un lounge bar de diseño.",
        "sedes_principales": [
            "Londres Canary Wharf (Bank Street - 9 pistas AFP con cámaras de IA y lounge mezzanine)",
            "Cardiff Premium Arena (nueva sede en Gales)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas AFP de máxima gama, césped de competición y cristal óptico",
            "software": "Padel Mates",
            "domotica": "Acceso inteligente, vestuarios con saunas y servicio concierge",
            "grabacion": "Cámaras con IA para análisis automático de velocidad de bola, zonas y repeticiones",
            "restauracion": "Lounge mezzanine con bar de cócteles, café de barista y catering corporativo"
        },
        "modelo_expansion": {
            "tipo_contrato": "Red boutique corporativa en distritos financieros de primer orden mundial",
            "perfil_club": "Emplazamientos prime en rascacielos o naves de arquitectura icónica",
            "canon_royalties": "Operación propia exclusiva",
            "inversion_media": "2.500.000£ a 5.000.000£ por club"
        },
        "diferencial": "El punto de encuentro corporativo definitivo para ejecutivos de banca, tecnología y fondos de inversión en Londres."
    },
    {
        "id": "padelx-uk",
        "nombre": "PadelX UK (Padel X Club)",
        "pais": "Reino Unido",
        "pais_codigo": "GB",
        "region_filtro": "GB",
        "bandera": "🇬🇧",
        "ciudad_sede": "Cotswolds / Londres",
        "coords": [
            51.718,
            -1.968
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "boutique",
        "num_clubs": "4 micro-clubes boutique",
        "num_pistas": "12+ pistas",
        "software": "Padel X App / Playtomic",
        "fundadores": "Padel X Club UK",
        "web": "https://padelx.club",
        "tagline": "Micro-clubes boutique y hubs de pádel rural en enclaves idílicos de la campiña inglesa.",
        "resumen": "Concepto que combina el encanto rural británico con el pádel de alta gama. Su buque insignia en Todenham Barn (Cotswolds) integra pistas panorámicas con el popular Yetz Café, creando micro-clubes de comunidad que sirven de escapada de fin de semana para los londinenses.",
        "sedes_principales": [
            "Todenham Barn (Cotswolds - pistas integradas con Yetz Café)",
            "Cirencester Country Padel",
            "Ponsbourne Park (Hertfordshire)",
            "Burghley Park Estate"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con vallado camuflado con el paisaje natural",
            "software": "Padel X UK App",
            "domotica": "Acceso QR y reserva autónoma",
            "grabacion": "Pistas preparadas para streaming de partidos de exhibición",
            "restauracion": "Yetz Café con repostería artesana local, brunch y vinos ecológicos"
        },
        "modelo_expansion": {
            "tipo_contrato": "Asociaciones con fincas rurales, hoteles con encanto y clubes privados",
            "perfil_club": "Instalaciones boutique de 2 a 4 pistas en entornos pintorescos",
            "canon_royalties": "Joint venture con propietarios del terreno",
            "inversion_media": "200.000£ a 450.000£"
        },
        "diferencial": "La fusión perfecta entre escapada campestre de lujo (Cotswolds) y deporte de moda."
    },
    {
        "id": "game4padel",
        "nombre": "Game4Padel",
        "pais": "Reino Unido",
        "pais_codigo": "GB",
        "region_filtro": "GB",
        "bandera": "🇬🇧",
        "ciudad_sede": "Edimburgo / Londres",
        "coords": [
            55.9533,
            -3.1883
        ],
        "modelo": "Red Corporativa Propia",
        "modelo_badge": "bg-blue-100 text-blue-800 border-blue-200",
        "tipo_categoria": "red_propia",
        "escala": "macro",
        "num_clubs": "18 centros",
        "num_pistas": "65+ pistas",
        "software": "Matchi / Playtomic",
        "fundadores": "Jim McMahon, Michael Gradon y Andy Murray (inversor embajador)",
        "web": "https://game4padel.com",
        "tagline": "La mayor red de pádel de Reino Unido, respaldada por la leyenda Andy Murray.",
        "resumen": "Game4Padel financia, construye y opera pistas en clubes de tenis, centros comerciales y universidades. Cuenta con el respaldo de Andy Murray y Jamie Murray, habiendo instalado clubes en Westfield London, David Lloyd y complejos universitarios en Escocia e Inglaterra.",
        "sedes_principales": [
            "Edinburgh Thistle Padel (sede central escocesa)",
            "Westfield Stratford City London (centro comercial)",
            "David Lloyd Bushey & clubs asociados",
            "The Grange Club (Edimburgo)",
            "Glasgow & Liverpool"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas de cristal templado homologadas LTA, carpas canopy",
            "software": "Matchi para reservas y gestión de socios",
            "domotica": "Acceso por pin o tarjeta RFID y luces automáticas",
            "grabacion": "Sistemas para retransmisión de torneos locales",
            "restauracion": "Integrado con las instalaciones del club anfitrión"
        },
        "modelo_expansion": {
            "tipo_contrato": "Concesión o alquiler a largo plazo (Game4Padel asume 100% de la inversión CAPEX)",
            "perfil_club": "Clubes de tenis, golf, universidades o centros comerciales con espacio libre",
            "canon_royalties": "Reparto de ingresos (revenue share) con la propiedad del suelo",
            "inversion_media": "Game4Padel financia entre 150.000£ y 600.000£ por ubicación"
        },
        "diferencial": "Modelo sin coste de inversión para el club anfitrión y la imagen global de Andy Murray."
    },
    {
        "id": "pdl-padel-united-uk",
        "nombre": "PDL Padel United UK",
        "pais": "Reino Unido",
        "pais_codigo": "GB",
        "region_filtro": "GB",
        "bandera": "🇬🇧",
        "ciudad_sede": "Maldon (Essex) / Londres",
        "coords": [
            51.7311,
            0.6746
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "12 centros",
        "num_pistas": "55+ pistas",
        "software": "Matchi",
        "fundadores": "Padel United Group UK (Dan Troy)",
        "web": "https://padeluniteduk.com",
        "tagline": "La división británica del mayor gigante de clubes cubiertos del norte de Europa.",
        "resumen": "Cadena nacida de la expansión sueca en suelo británico. Desarrolla clubes cubiertos masivos donde prima la formación infantil, las ligas sociales por niveles y la importación de técnicos profesionales españoles y argentinos.",
        "sedes_principales": [
            "Maldon (Essex - 6 pistas indoor y escuela de élite)",
            "Bishop's Stortford",
            "Brentwood Padel Club",
            "Shoreditch London",
            "East Anglia Regional Network"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas cubiertas panorámicas de última generación con césped texturizado",
            "software": "Matchi",
            "domotica": "Acceso inteligente automatizado 24/7",
            "grabacion": "Grabación de partidos y repetición en streaming",
            "restauracion": "Clubhouse nórdico con pro-shop y zona social"
        },
        "modelo_expansion": {
            "tipo_contrato": "Red propia y joint ventures con operadores locales",
            "perfil_club": "Naves industriales y suelos deportivos de 4 a 10 pistas",
            "canon_royalties": "Gestión directa",
            "inversion_media": "500.000£ a 1.200.000£ por centro"
        },
        "diferencial": "Metodología de entrenamiento nórdica contrastada y torneos de gran envergadura."
    },
    {
        "id": "soul-padel",
        "nombre": "Soul Padel",
        "pais": "Reino Unido",
        "pais_codigo": "GB",
        "region_filtro": "GB",
        "bandera": "🇬🇧",
        "ciudad_sede": "Mánchester / Stockport",
        "coords": [
            53.4084,
            -2.1494
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "4 centros",
        "num_pistas": "18+ pistas",
        "software": "Playtomic",
        "fundadores": "Mark Hewlett (ex-director de retail)",
        "web": "https://soulpadel.co.uk",
        "tagline": "Pádel comunitario en alianzas pioneras con gigantes del retail como Decathlon.",
        "resumen": "Cadena que destaca por su acuerdo estratégico nacional con Decathlon para instalar pistas de pádel en los aparcamientos y azoteas de sus megatiendas, combinando tráfico peatonal masivo, venta de equipamiento y deporte para toda la familia.",
        "sedes_principales": [
            "Decathlon Stockport (Gran Mánchester - buque insignia de 4 pistas)",
            "Leeds Urban Hub",
            "Lancashire Network",
            "Midlands Retail Park"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con cubierta de lona de alta resistencia y LED perimetral",
            "software": "Playtomic",
            "domotica": "Reserva rápida y apertura mediante código QR",
            "grabacion": "Sistemas para revisión de puntos",
            "restauracion": "Sinergia con cafeterías del centro comercial y tienda Decathlon"
        },
        "modelo_expansion": {
            "tipo_contrato": "Alianzas de retailtainment en superficies comerciales consolidadas",
            "perfil_club": "Aparcamientos exteriores o interiores de 3 a 6 pistas",
            "canon_royalties": "Alquiler variable o revenue share con el retailer",
            "inversion_media": "250.000£ a 500.000£ por centro"
        },
        "diferencial": "Coste de adquisición de cliente bajísimo gracias al tráfico constante de compradores de Decathlon."
    },
    {
        "id": "padel-7",
        "nombre": "Pàdel 7",
        "pais": "España",
        "pais_codigo": "ES",
        "region_filtro": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Barcelona",
        "coords": [
            41.398,
            2.19
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "5 clubes con el mismo nombre",
        "num_pistas": "45+ pistas",
        "software": "Playtomic / CourtBrain",
        "fundadores": "Grup Pàdel 7 Barcelona",
        "web": "https://padel7santmarti.com",
        "tagline": "La cadena histórica de clubes de pádel urbanos de Barcelona y el Maresme.",
        "resumen": "Pàdel 7 es una de las marcas más reconocidas de Cataluña. Opera múltiples clubes bajo la misma enseña Pàdel 7 en Barcelona capital y comarcas colindantes: Pàdel 7 Glòries (con pistas en azotea rooftop y naves cubiertas), Pàdel 7 Sant Martí/Poblenou (100% indoor en nave industrial), Pàdel 7 Malgrat de Mar (13 pistas en el Maresme), además de sedes en Terrassa y Sant Andreu.",
        "sedes_principales": [
            "Pàdel 7 Glòries (Barcelona - 11 pistas: indoor y rooftop outdoor)",
            "Pàdel 7 Sant Martí / Poblenou (Barcelona - 11 pistas cubiertas)",
            "Pàdel 7 Malgrat (Malgrat de Mar, Maresme - 13 pistas: 8 cubiertas + 5 outdoor)",
            "Pàdel 7 Terrassa (Barcelona)",
            "Pàdel 7 Sant Andreu (Barcelona)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas cubiertas, descubiertas y en azoteas (rooftops urbanos)",
            "software": "Playtomic y CourtBrain para reservas y ligas",
            "domotica": "Acceso por tornos electrónicos y código de socio",
            "grabacion": "Pistas preparadas para streaming en torneos locales",
            "restauracion": "Terrazas chill-out con vistas urbanas, cafetería y venta de material"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena de clubes propios bajo la marca unificada Pàdel 7",
            "perfil_club": "Naves industriales urbanas y parcelas periurbanas de 6 a 14 pistas",
            "canon_royalties": "Operador directo de cadena",
            "inversion_media": "500.000€ a 1.200.000€ por apertura"
        },
        "diferencial": "Ubicación en los barrios más cotizados de Barcelona (Poblenou, Glòries) y comunidad histórica de miles de jugadores habituales."
    },
    {
        "id": "padel-people-madrid",
        "nombre": "Padel People",
        "pais": "España",
        "pais_codigo": "ES",
        "region_filtro": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Torrelodones (Madrid)",
        "coords": [
            40.5756,
            -3.9303
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "boutique",
        "num_clubs": "2 centros con el mismo nombre",
        "num_pistas": "14+ pistas",
        "software": "Playtomic",
        "fundadores": "Padel People Sports Group",
        "web": "https://padelpeopletorrelodones.com",
        "tagline": "Clubes de pádel cubierto de referencia en el noroeste de Madrid.",
        "resumen": "Cadena de centros con la misma marca en la sierra noroeste de Madrid. Su buque insignia en Torrelodones cuenta con 8 pistas (7 cubiertas bajo nave y 1 central exterior), con un fuerte arraigo en escuelas de tecnificación, gimnasio propio y cafetería social con terraza.",
        "sedes_principales": [
            "Padel People Torrelodones (Madrid - 8 pistas: 7 cubiertas + 1 outdoor)",
            "Instalaciones satélites asociadas en la sierra de Guadarrama"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas de cristal con iluminación LED y césped monofilamento azul",
            "software": "Playtomic",
            "domotica": "Check-in digitalizado y reservas automáticas",
            "grabacion": "Grabación de partidos de liga social y torneos de la FMP",
            "restauracion": "Cafetería restaurante con terraza de verano y zona fitness"
        },
        "modelo_expansion": {
            "tipo_contrato": "Explotación propia bajo la marca Padel People",
            "perfil_club": "Centros cubiertos de 6 a 10 pistas en zonas residenciales",
            "canon_royalties": "Gestión directa",
            "inversion_media": "400.000€ a 800.000€"
        },
        "diferencial": "Ambiente social premium en urbanizaciones de renta alta del noroeste madrileño."
    },
    {
        "id": "forus-padel",
        "nombre": "Forus Pádel",
        "pais": "España",
        "pais_codigo": "ES",
        "region_filtro": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Madrid",
        "coords": [
            40.45,
            -3.68
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "15+ centros con pádel",
        "num_pistas": "100+ pistas",
        "software": "App Propia Forus / Resasports",
        "fundadores": "Ignacio Triana (Forus Deporte y Ocio)",
        "web": "https://forus.es",
        "tagline": "El gigante de la gestión deportiva con decenas de pistas de pádel integradas en sus complejos.",
        "resumen": "Forus es uno de los mayores operadores de concesiones deportivas de España y Portugal. Integra pistas de pádel cubiertas y descubiertas en sus grandes complejos familiares, organizando ligas intercentros y ranking unificado bajo la misma marca.",
        "sedes_principales": [
            "Forus Chamartín (Madrid - pistas de pádel cubiertas)",
            "Forus Barceló (Madrid Centro)",
            "Forus Alcalá de Henares",
            "Forus Coslada y Fuenlabrada",
            "Forus Valencia y Andalucía"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas reglamentarias de cristal con césped de alta densidad",
            "software": "App Forus y plataforma Resasports",
            "domotica": "Tornos de acceso con pulsera RFID de socio",
            "grabacion": "Cámaras en torneos sociales",
            "restauracion": "Restaurantes cafetería, spa, piscina y fitness"
        },
        "modelo_expansion": {
            "tipo_contrato": "Concesión administrativa municipal y gestión de complejos privados",
            "perfil_club": "Megacomplejos deportivos con pádel, fitness y aguas",
            "canon_royalties": "Operación corporativa directa",
            "inversion_media": "3.000.000€ a 8.000.000€ por complejo completo"
        },
        "diferencial": "Economías de escala brutales y base de más de 250.000 socios en toda la red."
    },
    {
        "id": "bamvolea",
        "nombre": "BamVolea",
        "pais": "España",
        "pais_codigo": "ES",
        "region_filtro": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Madrid / Pozuelo",
        "coords": [
            40.435,
            -3.815
        ],
        "modelo": "Red Corporativa Propia",
        "modelo_badge": "bg-blue-100 text-blue-800 border-blue-200",
        "tipo_categoria": "red_propia",
        "escala": "macro",
        "num_clubs": "32 complejos",
        "num_pistas": "260+ pistas",
        "software": "Playtomic / Syltek",
        "fundadores": "Fusión estratégica Volea Padel & Bam Sports Management",
        "web": "https://bamvoleapadel.com",
        "tagline": "El mayor operador corporativo de pádel en España tras su histórica fusión multisede.",
        "resumen": "Nacida de la unión de dos de los grupos de gestión de pádel más potentes de la Península, BamVolea gestiona más de 260 pistas en 32 instalaciones deportivas, con un modelo de hostelería de vanguardia, escuela para menores y eventos corporativos para el IBEX 35.",
        "sedes_principales": [
            "Volea Pádel Club (Pozuelo de Alarcón - buque insignia con restaurante gastronómico)",
            "Bam Padel Las Rozas",
            "Complejos concesionados en Comunidad de Madrid, Castilla y León y Levante"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas de competición panorámicas, césped Mondo Supercourt, cubiertas aisladas",
            "software": "Syltek / Playtomic para torneos y ranking",
            "domotica": "Acceso digital automatizado y gestión energética",
            "grabacion": "Sistemas de streaming para partidos de exhibición",
            "restauracion": "Restauración de autor de alto nivel integrada en el club"
        },
        "modelo_expansion": {
            "tipo_contrato": "Gestión integral de instalaciones privadas y concesiones deportivas de alto nivel",
            "perfil_club": "Clubes de mínimo 8 pistas con restauración de calidad",
            "canon_royalties": "Operación directa",
            "inversion_media": "1.000.000€ a 2.500.000€"
        },
        "diferencial": "Capacidad de gestión profesionalizada y hostelería gastronómica de primer nivel."
    },
    {
        "id": "aurial-padel",
        "nombre": "Aurial Padel",
        "pais": "España",
        "pais_codigo": "ES",
        "region_filtro": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Sabadell / Sant Cugat",
        "coords": [
            41.545,
            2.108
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "5 clubes con el mismo nombre",
        "num_pistas": "85+ pistas",
        "software": "Playtomic",
        "fundadores": "Marta Marrero (ex nº1 mundial) & Borja Ferrater",
        "web": "https://aurialpadel.com",
        "tagline": "El imperio catalán de la ex número 1 Marta Marrero: el mayor megaclub de Europa en Sabadell.",
        "resumen": "Aurial Padel opera bajo la misma marca varios de los clubes más grandes de Cataluña: Aurial Padel Sabadell (con 21 pistas cubiertas, uno de los mayores complejos indoor del continente), Aurial Sant Cugat, Aurial Vic, Aurial Terrassa y Aurial Cornellà.",
        "sedes_principales": [
            "Aurial Padel Sabadell (21 pistas cubiertas)",
            "Aurial Sant Cugat (indoor y outdoor)",
            "Aurial Vic (Osona)",
            "Aurial Terrassa",
            "Aurial Cornellà (área metropolitana de Barcelona)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de competición con moqueta World Padel Tour y techos altos",
            "software": "Playtomic integrado con Aurial Academy",
            "domotica": "Control centralizado de iluminación LED y climatización",
            "grabacion": "Pistas centrales con cámaras fijas para análisis de juego",
            "restauracion": "Restaurantes saludables, terrazas y tiendas Pro-Shop de Marta Marrero"
        },
        "modelo_expansion": {
            "tipo_contrato": "Adquisición y reposicionamiento de grandes naves industriales bajo la marca unificada",
            "perfil_club": "Naves de más de 4.000 m² con capacidad para más de 12 pistas",
            "canon_royalties": "Operador directo",
            "inversion_media": "1.500.000€ a 3.000.000€ por club"
        },
        "diferencial": "El reclamo directo de la ex número uno Marta Marrero y torneos masivos de más de 300 parejas."
    },
    {
        "id": "bela-padel-center",
        "nombre": "Bela Padel Center",
        "pais": "España",
        "pais_codigo": "ES",
        "region_filtro": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Alicante / Barcelona",
        "coords": [
            38.36,
            -0.44
        ],
        "modelo": "Academia & Pro-Shop",
        "modelo_badge": "bg-amber-100 text-amber-800 border-amber-200",
        "tipo_categoria": "academia",
        "escala": "macro",
        "num_clubs": "4 centros internacionales",
        "num_pistas": "45+ pistas",
        "software": "Playtomic",
        "fundadores": "Fernando Belasteguín (16 años nº 1) & socios inversores",
        "web": "https://belapadelcenter.com",
        "tagline": "Los templos del pádel creados por el mejor jugador de todos los tiempos.",
        "resumen": "Cadena de centros de élite diseñados con la filosofía deportiva de Fernando Belasteguín. Su buque insignia en Alicante cuenta con 14 pistas de competición, ampliado con sedes en Barcelona, Suecia y México, combinando formación de menores, torneos internacionales y clínicas con Bela.",
        "sedes_principales": [
            "Bela Padel Center Alicante (14 pistas: 9 outdoor + 5 indoor)",
            "Bela Padel Center Barcelona (Sant Cugat)",
            "Bela Padel Center Suecia (Helsingborg)",
            "Bela Padel Center México"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas oficiales Wilson Bela con césped texturizado monofilamento de última generación",
            "software": "Playtomic",
            "domotica": "Tornos inteligentes y sistema acústico anti-eco",
            "grabacion": "Sistemas de vídeo análisis en pista para los alumnos de la academia",
            "restauracion": "Clubhouse con gastronomía mediterránea, zona lounge y pro-shop Wilson Bela"
        },
        "modelo_expansion": {
            "tipo_contrato": "Franquicia de prestigio o centros propios con la marca Bela Padel Center",
            "perfil_club": "Complejos deportivos premium con al menos 10 pistas y zona social cuidada",
            "canon_royalties": "Canon de marca + asesoría técnica del equipo de Belasteguín",
            "inversion_media": "1.800.000€ a 3.500.000€"
        },
        "diferencial": "El valor de marca inigualable de Fernando Belasteguín y su metodología de formación exclusiva."
    },
    {
        "id": "click-and-padel",
        "nombre": "Click & Padel / Padel Time 24/7",
        "pais": "España",
        "pais_codigo": "ES",
        "region_filtro": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Valencia / Madrid",
        "coords": [
            39.4699,
            -0.3763
        ],
        "modelo": "Club 100% Automatizado 24/7",
        "modelo_badge": "bg-emerald-100 text-emerald-800 border-emerald-200",
        "tipo_categoria": "automatizado",
        "escala": "media",
        "num_clubs": "8 naves operativas",
        "num_pistas": "28+ pistas",
        "software": "Playtomic / Domótica IoT Propia",
        "fundadores": "Click & Padel Tech Solutions",
        "web": "https://clickandpadel.com",
        "tagline": "Pistas de pádel cubiertas 100% automatizadas sin empleados ni recepción física.",
        "resumen": "Cadena pionera en España del modelo autónomo: naves industriales de 3 a 5 pistas cubiertas que operan las 24 horas del día sin personal presencial. La puerta se abre con el código de reserva de Playtomic, las luces de la pista se encienden 5 minutos antes y se apagan al terminar.",
        "sedes_principales": [
            "Paterna / Fuente del Jarro (Valencia - 4 pistas)",
            "Ribas / Madrid Sur (4 pistas)",
            "Castellón y Alicante"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas indoor reforzadas",
            "software": "Integración de Playtomic con cerraduras inteligentes y relés IoT",
            "domotica": "Apertura por QR en móvil, encendido automático de LED y clima por presencia",
            "grabacion": "Grabación de seguridad 24/7 con IA para detección de incidencias",
            "restauracion": "Máquinas vending automáticas de bebidas, bolas y grips"
        },
        "modelo_expansion": {
            "tipo_contrato": "Franquicia tecnológica llave en mano y red corporativa propia",
            "perfil_club": "Naves industriales de 1.200m² a 2.000m² con altura >7m en polígonos urbanos",
            "canon_royalties": "Cuota mensual SaaS por integración domótica y soporte 24h",
            "inversion_media": "180.000€ a 320.000€ por nave"
        },
        "diferencial": "Costes operativos (OPEX) mínimos al eliminar salarios de recepción y maximizar márgenes."
    },
    {
        "id": "paquito-navarro-academy",
        "nombre": "Paquito Navarro Academy",
        "pais": "España",
        "pais_codigo": "ES",
        "region_filtro": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Sevilla / Madrid",
        "coords": [
            37.3891,
            -5.9845
        ],
        "modelo": "Academia & Pro-Shop",
        "modelo_badge": "bg-amber-100 text-amber-800 border-amber-200",
        "tipo_categoria": "academia",
        "escala": "media",
        "num_clubs": "6 clubes y academias",
        "num_pistas": "60+ pistas asociadas",
        "software": "Playtomic / Matchi",
        "fundadores": "Paquito Navarro (Campeón del Mundo y figura Premier Padel)",
        "web": "https://paquitonavarroacademy.com",
        "tagline": "La metodología de formación del jugador más carismático del planeta.",
        "resumen": "Cadena de centros y academias licenciadas que aplican el sistema de juego y la garra de Paquito Navarro. Con sede matriz en Sevilla y extensiones en Madrid y Lisboa, atrae tanto a jugadores amateurs que buscan mejorar su bandeja y volea como a promesas internacionales.",
        "sedes_principales": [
            "Sevilla Flagship Academy",
            "Madrid Centro de Formación",
            "Lisboa Academy Center",
            "Centros colaboradores en Andalucía y Levante"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas Bullpadel oficiales con césped de máxima amortiguación",
            "software": "Playtomic para la gestión de pistas y clinics",
            "domotica": "Control digital de accesos y alumbrado de alta eficiencia",
            "grabacion": "Cámaras con software de biomecánica para clinics de Paquito",
            "restauracion": "Cafetería social y Pro-Shop Bullpadel oficial"
        },
        "modelo_expansion": {
            "tipo_contrato": "Licencia de academia oficial e implantación en clubes consolidados",
            "perfil_club": "Clubes de pádel existentes de al menos 6 pistas que buscan prestigio",
            "canon_royalties": "Royalty por alumno y canon anual de licencia de marca",
            "inversion_media": "50.000€ a 150.000€ (adaptación sobre club ya construido)"
        },
        "diferencial": "El carisma inigualable de Paquito Navarro y su método de entrenamiento ofensivo."
    },
    {
        "id": "padel-nuestro-clubs",
        "nombre": "Club Pádel Nuestro",
        "pais": "España",
        "pais_codigo": "ES",
        "region_filtro": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Murcia / Madrid",
        "coords": [
            37.9922,
            -1.1307
        ],
        "modelo": "Franquicia Llave en Mano",
        "modelo_badge": "bg-indigo-100 text-indigo-800 border-indigo-200",
        "tipo_categoria": "franquicia",
        "escala": "macro",
        "num_clubs": "40+ clubes asociados",
        "num_pistas": "500+ pistas",
        "software": "Playtomic / Syltek",
        "fundadores": "Grupo Pádel Nuestro (360 Padel Group)",
        "web": "https://padelnuestro.com",
        "tagline": "El mayor minorista del mundo conectando tiendas de pádel con clubes franquiciados.",
        "resumen": "La división de clubes del mayor distribuidor mundial de pádel. Ofrece a clubes existentes y nuevas aperturas la conversión a la marca 'Club Pádel Nuestro', integrando una pro-shop oficial con más de 50 marcas, material de test directo y patrocinio de torneos.",
        "sedes_principales": [
            "Club Pádel Nuestro Madrid",
            "Club Pádel Nuestro Murcia",
            "Red de 40+ clubes franquiciados en España, Italia y Portugal"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas estándar y panorámicas con césped oficial",
            "software": "Playtomic / Syltek integrado con el stock de Pádel Nuestro",
            "domotica": "Accesos automatizados opcionales",
            "grabacion": "Sistemas para retransmisión de torneos de fin de semana",
            "restauracion": "Pro-shops de hasta 150m² dentro del club y cafetería"
        },
        "modelo_expansion": {
            "tipo_contrato": "Franquicia de tienda Pro-Shop y branding completo del club",
            "perfil_club": "Clubes consolidados de más de 4 pistas con local comercial",
            "canon_royalties": "Canon de adhesión + condiciones preferentes en material deportivo",
            "inversion_media": "30.000€ a 90.000€ para abanderamiento de club existente"
        },
        "diferencial": "Los mejores márgenes en palas, textil y pelotas del mercado gracias a la central de compras global de Pádel Nuestro."
    },
    {
        "id": "duet-sports",
        "nombre": "Duet Sports",
        "pais": "España",
        "pais_codigo": "ES",
        "region_filtro": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Barcelona",
        "coords": [
            41.3851,
            2.1734
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "10+ centros con pádel",
        "num_pistas": "65+ pistas",
        "software": "App Propia / Resasports",
        "fundadores": "Grup Duet",
        "web": "https://duetsports.com",
        "tagline": "Cadena histórica catalana de fitness y raqueta con grandes escuelas de pádel.",
        "resumen": "Cadena multideportiva de prestigio en Cataluña y Baleares. Gestiona centros municipales y privados donde el pádel es un pilar fundamental: Duet Rubí, Duet Sant Boi, Duet Mallorca, etc., con rankings unificados y escuelas de formación continua.",
        "sedes_principales": [
            "Duet Rubí (Barcelona - pistas cubiertas y outdoor)",
            "Duet Sant Boi de Llobregat",
            "Duet Palma de Mallorca",
            "Duet Tiana y centros metropolitanos"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas de cristal templado, césped azul y cubiertas con cerramiento lateral",
            "software": "App Duet y plataforma web de reservas",
            "domotica": "Acceso por pulsera inteligente integrada con vestuarios y piscina",
            "grabacion": "Pistas con soporte para streaming de torneos comarcales",
            "restauracion": "Cafeterías restaurante Duet, zona lounge y terrazas"
        },
        "modelo_expansion": {
            "tipo_contrato": "Concesión de obra y servicio deportivo municipal",
            "perfil_club": "Macrocomplejos deportivos urbanos de 5.000 a 10.000 m²",
            "canon_royalties": "Operación directa",
            "inversion_media": "2.500.000€ a 6.000.000€ por centro completo"
        },
        "diferencial": "La integración perfecta del pádel con actividades de fitness, spa y piscina para toda la familia."
    },
    {
        "id": "vals-sport-malaga",
        "nombre": "Vals Sport Málaga",
        "pais": "España",
        "pais_codigo": "ES",
        "region_filtro": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Málaga",
        "coords": [
            36.7213,
            -4.4214
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "5 macrocomplejos con el mismo nombre",
        "num_pistas": "35+ pistas",
        "software": "Playtomic / Vals Sport App",
        "fundadores": "Grupo Vals Sport",
        "web": "https://valssport.com",
        "tagline": "La cadena multiclub hegemónica de la Costa del Sol con 5 macrocomplejos en Málaga.",
        "resumen": "Vals Sport es el rey absoluto del pádel en la capital malagueña. Con 5 macroinstalaciones que llevan el nombre Vals Sport (Vals Sport Cónsul, Vals Sport Teatinos, Vals Sport Ciudad Jardín, Vals Sport Ave María y Vals Sport Churriana), mueven a decenas de miles de jugadores cada semana.",
        "sedes_principales": [
            "Vals Sport Cónsul (Teatinos - gran complejo de raqueta y fitness)",
            "Vals Sport Teatinos",
            "Vals Sport Ciudad Jardín",
            "Vals Sport Ave María (frente al paseo marítimo)",
            "Vals Sport Churriana"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas de cristal panorámicas y tradicionales con iluminación LED de alta potencia",
            "software": "Playtomic y App Vals Sport",
            "domotica": "Control digital de pistas y accesos con carnet digital",
            "grabacion": "Pistas preparadas para streaming de ligas provinciales",
            "restauracion": "Grandes terrazas cervecerías con gastronomía andaluza y vistas a las pistas"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena propia de centros concesionados y en propiedad",
            "perfil_club": "Grandes parcelas deportivas en los principales distritos residenciales de Málaga",
            "canon_royalties": "Operador directo",
            "inversion_media": "1.000.000€ a 3.000.000€ por complejo"
        },
        "diferencial": "Dominio geográfico absoluto de la ciudad de Málaga y el circuito de torneos amateur más activo de Andalucía."
    },
    {
        "id": "padel-indoor-aragon",
        "nombre": "Pádel Indoor Aragón",
        "pais": "España",
        "pais_codigo": "ES",
        "region_filtro": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Zaragoza",
        "coords": [
            41.6488,
            -0.8891
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "3 clubes en Aragón",
        "num_pistas": "40+ pistas",
        "software": "Playtomic / Syltek",
        "fundadores": "Pádel Indoor Aragón Group",
        "web": "https://padelindooraragon.com",
        "tagline": "El gigante de las naves cubiertas del valle del Ebro: el mejor pádel protegido del cierzo.",
        "resumen": "Cadena de referencia en Aragón creada específicamente para ofrecer pádel de competición 100% resguardado del viento y el frío zaragozano. Opera grandes complejos naves en Zaragoza capital y su cinturón industrial, con pistas centrales con gradas y la mayor escuela de la comunidad.",
        "sedes_principales": [
            "Pádel Indoor Aragón Zaragoza (nave principal con 14 pistas cubiertas)",
            "Pádel Indoor Zaragoza Sur",
            "Centro provincial en Huesca"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas cubiertas con techos de 11 metros, césped monofilamento azul y pistas centrales",
            "software": "Playtomic / Syltek",
            "domotica": "Control automatizado de climatización invernal e iluminación LED",
            "grabacion": "Cámaras cenitales para análisis técnico de escuela",
            "restauracion": "Restaurante asador con menús diarios, zona lounge y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena corporativa con expansión en capitales del noreste español",
            "perfil_club": "Naves industriales de más de 3.500m² sin columnas intermedias",
            "canon_royalties": "Operación directa",
            "inversion_media": "800.000€ a 1.600.000€"
        },
        "diferencial": "La solución perfecta al clima extremo de Zaragoza, garantizando el juego 365 días al año."
    },
    {
        "id": "padel-dos-cero",
        "nombre": "Pádel 2.0",
        "pais": "España",
        "pais_codigo": "ES",
        "region_filtro": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Móstoles / Madrid Sur",
        "coords": [
            40.3222,
            -3.8649
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 macrocentros",
        "num_pistas": "18+ pistas",
        "software": "Playtomic",
        "fundadores": "Padel 2.0 Management",
        "web": "https://padeldoscero.com",
        "tagline": "El templo indoor del sur de Madrid, sede habitual de los mejores jugadores del circuito.",
        "resumen": "Pádel 2.0 es uno de los clubes cubiertos de culto de la Comunidad de Madrid. Con pistas de máxima calidad y una altura extraordinaria en nave diáfana, ha sido durante años centro de entrenamiento de jugadores World Padel Tour y sede de las mejores ligas de empresas.",
        "sedes_principales": [
            "Pádel 2.0 Móstoles (10 pistas cubiertas de gran altura libre)",
            "Instalaciones satélites asociadas en Madrid Sur"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas de competición con moqueta World Padel Tour y tratamiento acústico",
            "software": "Playtomic",
            "domotica": "Acceso QR y taquillas electrónicas",
            "grabacion": "Pistas preparadas para streaming de partidos PRO",
            "restauracion": "Cafetería con platos combinados, terraza y tienda técnica de palas de test"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios en núcleos industriales urbanos",
            "perfil_club": "Naves de 2.000m² a 4.000m²",
            "canon_royalties": "Operación propia",
            "inversion_media": "600.000€ a 1.200.000€"
        },
        "diferencial": "Reputación histórica intachable entre los jugadores de nivel avanzado y profesionales de Madrid."
    },
    {
        "id": "enjoy-wellness",
        "nombre": "Enjoy Wellness",
        "pais": "España",
        "pais_codigo": "ES",
        "region_filtro": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Madrid / Valencia",
        "coords": [
            40.4168,
            -3.7038
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "12+ centros con pistas de pádel",
        "num_pistas": "75+ pistas",
        "software": "App Enjoy / Resasports",
        "fundadores": "Enjoy Wellness SA",
        "web": "https://enjoy.es",
        "tagline": "Grandes resorts familiares con pistas de pádel cubiertas y descubiertas en toda España.",
        "resumen": "Cadena de centros de bienestar y deporte con complejos en Madrid, Valencia, Sevilla, Oviedo, Salamanca y Mérida. Cada centro Enjoy incluye una potente sección de pádel con escuelas para abonados, torneos de fin de semana y reserva digital.",
        "sedes_principales": [
            "Enjoy Samaranch (Madrid)",
            "Enjoy Valencia",
            "Enjoy Getafe",
            "Enjoy Oviedo y Enjoy Salamanca"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas de cristal panorámicas con cubiertas de diseño arquitectónico",
            "software": "App Enjoy para reserva de pistas y clases",
            "domotica": "Acceso integrado con pulsera RFID de socio",
            "grabacion": "Sistemas de vídeo en torneos",
            "restauracion": "Cafeterías saludables, zona de aguas y spa"
        },
        "modelo_expansion": {
            "tipo_contrato": "Concesiones deportivas municipales y suelo terciario propio",
            "perfil_club": "Resorts deportivos de gran formato",
            "canon_royalties": "Operador directo",
            "inversion_media": "4.000.000€ a 9.000.000€ por centro integral"
        },
        "diferencial": "Instalaciones impecables y ambiente familiar multideporte con altísima fidelidad de socios."
    },
    {
        "id": "sportcity-valencia",
        "nombre": "Sportcity Valencia",
        "pais": "España",
        "pais_codigo": "ES",
        "region_filtro": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Valencia / Massanassa",
        "coords": [
            39.412,
            -0.4
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "3 complejos",
        "num_pistas": "30+ pistas",
        "software": "Playtomic",
        "fundadores": "Sportcity Group Valencia",
        "web": "https://sportcity.es",
        "tagline": "La meca del pádel en la Comunidad Valenciana con 30 pistas indoor y outdoor.",
        "resumen": "Uno de los centros más espectaculares de la cuenca mediterránea. Con 30 pistas repartidas entre naves cubiertas y pistas exteriores de alta competición, Sportcity es sede recurrente de fases clasificatorias del circuito profesional y torneos con más de 400 parejas.",
        "sedes_principales": [
            "Sportcity Massanassa (30 pistas de pádel cubiertas y exteriores)",
            "Instalaciones satélites en el área metropolitana de Valencia"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas oficiales Premier Padel con moqueta monofilamento de alta velocidad",
            "software": "Playtomic",
            "domotica": "Sistema de climatización en naves y tornos inteligentes",
            "grabacion": "Pistas con cámaras para retransmisión de streaming federado",
            "restauracion": "Restaurante con paellas a leña, terraza de 1.000m² y tienda técnica"
        },
        "modelo_expansion": {
            "tipo_contrato": "Macrocomplejos en propiedad y alianzas metropolitanas",
            "perfil_club": "Suelos industriales y comerciales de más de 10.000 m²",
            "canon_royalties": "Gestión corporativa",
            "inversion_media": "2.000.000€ a 4.000.000€"
        },
        "diferencial": "Capacidad organizativa insuperable en Valencia para eventos de cientos de jugadores simultáneos."
    },
    {
        "id": "padel-derio",
        "nombre": "Padel Derio Club",
        "pais": "España",
        "pais_codigo": "ES",
        "region_filtro": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Bilbao / Derio (Bizkaia)",
        "coords": [
            43.2928,
            -2.8872
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 centros en el País Vasco",
        "num_pistas": "16+ pistas",
        "software": "Playtomic",
        "fundadores": "Padel Derio Sports Group",
        "web": "https://padelderio.com",
        "tagline": "El buque insignia del pádel cubierto en Bizkaia y cantera histórica del País Vasco.",
        "resumen": "Padel Derio es el club de referencia del Gran Bilbao. Con sus pistas cubiertas que permiten competir sin importar el sirimiri o el temporal cantábrico, cuenta con una de las escuelas de menores más galardonadas de España y un club social muy activo.",
        "sedes_principales": [
            "Padel Derio Club (Derio, Bizkaia - 12 pistas cubiertas)",
            "Centro asociado en la comarca del Txorierri"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas cubiertas con techos altos de nave industrial y moqueta azul",
            "software": "Playtomic",
            "domotica": "Acceso QR automatizado",
            "grabacion": "Grabación en pista central",
            "restauracion": "Txoko social vasco, restaurante con pintxos y tienda especializada"
        },
        "modelo_expansion": {
            "tipo_contrato": "Club propio enfocado en el cliente de Bizkaia",
            "perfil_club": "Naves cubiertas en las proximidades de Bilbao",
            "canon_royalties": "Operación directa",
            "inversion_media": "700.000€ a 1.200.000€"
        },
        "diferencial": "Arraigo insustituible en la comunidad deportiva vizcaína y un ambiente social inmejorable."
    },
    {
        "id": "padel-la-moraleja",
        "nombre": "Club de Pádel La Moraleja",
        "pais": "España",
        "pais_codigo": "ES",
        "region_filtro": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Madrid (Alcobendas)",
        "coords": [
            40.53,
            -3.645
        ],
        "modelo": "Boutique & Ultra-Lujo",
        "modelo_badge": "bg-purple-100 text-purple-800 border-purple-200",
        "tipo_categoria": "boutique",
        "escala": "macro",
        "num_clubs": "2 centros de alta dirección",
        "num_pistas": "33+ pistas",
        "software": "Syltek / App Propia",
        "fundadores": "Inversores Privados La Moraleja",
        "web": "https://clubpadellamoraleja.es",
        "tagline": "El mayor club privado de pádel del mundo y epicentro del networking corporativo madrileño.",
        "resumen": "Situado en la exclusiva urbanización de La Moraleja en Madrid, cuenta con 33 pistas (8 cubiertas, 23 exteriores y 2 individuales), además de un restaurante de alta cocina, salones para eventos corporativos y una escuela de directivos.",
        "sedes_principales": [
            "La Moraleja Alcobendas (33 pistas de pádel, restaurante y centro de congresos)",
            "Anexos de eventos en Madrid Norte"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas de cristal templado homologadas para competiciones FMP y FIP",
            "software": "Syltek y App propia con gestión de ranking de socios",
            "domotica": "Acceso restringido para socios e invitados, iluminación LED de máxima fidelidad cromática",
            "grabacion": "Pistas preparadas para producción audiovisual de torneos benéficos y empresas",
            "restauracion": "Restaurante con bodega de vinos seleccionados, terrazas ajardinadas y salones privados"
        },
        "modelo_expansion": {
            "tipo_contrato": "Club privado exclusivo",
            "perfil_club": "Grandes parcelas en urbanizaciones de máxima renta per cápita",
            "canon_royalties": "Gestión directa del club",
            "inversion_media": "Más de 5.000.000€"
        },
        "diferencial": "El club social con mayor concentración de directivos de multinacionales y personalidades públicas de Europa."
    },
    {
        "id": "padel-indoor-granollers",
        "nombre": "Padel Indoor Granollers & Mataró",
        "pais": "España",
        "pais_codigo": "ES",
        "region_filtro": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Granollers / Mataró",
        "coords": [
            41.608,
            2.288
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 macrocomplejos catalanes",
        "num_pistas": "24+ pistas",
        "software": "Playtomic",
        "fundadores": "Indoor Padel Catalunya",
        "web": "https://padelindoorgranollers.com",
        "tagline": "Referente de competición de naves cubiertas en el Vallès Oriental y Maresme.",
        "resumen": "Cadena que opera instalaciones de gran envergadura en dos de los polos demográficos más dinámicos de Cataluña (Granollers y Mataró), con pistas de alta velocidad, techos sin pilares y escuelas de tecnificación intensiva.",
        "sedes_principales": [
            "Padel Indoor Granollers (12 pistas cubiertas)",
            "Padel Indoor Mataró (12 pistas cubiertas)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de cristal con césped texturizado",
            "software": "Playtomic",
            "domotica": "Acceso QR y taquillas electrónicas",
            "grabacion": "Pistas con cámaras para torneos de fin de semana",
            "restauracion": "Cafetería con bocadillos y tapas, tienda pro-shop y terraza"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena propia de naves industriales",
            "perfil_club": "Naves de más de 3.000 m² con fácil aparcamiento",
            "canon_royalties": "Operación directa",
            "inversion_media": "600.000€ a 1.200.000€"
        },
        "diferencial": "Comunidad de competición muy arraigada entre Granollers, Sabadell y Mataró."
    },
    {
        "id": "all-in-padel",
        "nombre": "All In Padel",
        "pais": "Francia",
        "pais_codigo": "FR",
        "region_filtro": "FR",
        "bandera": "🇫🇷",
        "ciudad_sede": "Lyon / Grasse",
        "coords": [
            45.764,
            4.8357
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "6 clubes con el mismo nombre",
        "num_pistas": "42+ pistas",
        "software": "Gestion Sports / Playtomic",
        "fundadores": "Jo-Wilfried Tsonga, Thierry Ascione & Anthony Lopes",
        "web": "https://allin-padel.com",
        "tagline": "El proyecto deportivo de Jo-Wilfried Tsonga: clubes de pádel de élite en Lyon y la Costa Azul.",
        "resumen": "All In Padel es la división de pádel del prestigioso grupo All In Country Club fundado por las estrellas de tenis Jo-Wilfried Tsonga y Thierry Ascione. Cuentan con complejos de primer nivel en Lyon Décines (OL Vallée junto al estadio del Olympique de Lyon, con 8 pistas indoor climatizadas), Lyon Villefranche, Grasse, Mougins y la región de Auvergne-Rhône-Alpes.",
        "sedes_principales": [
            "All In Country Club Décines (Lyon OL Vallée - 8 pistas indoor climatizadas)",
            "All In Padel Grasse (Costa Azul - 6 pistas panorámicas)",
            "All In Padel Mougins (Costa Azul)",
            "All In Padel Lyon Villefranche",
            "Sedes asociadas en la región Ródano-Alpes"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de 10 metros de altura libre, moqueta texturizada de competición",
            "software": "Gestion Sports y Playtomic",
            "domotica": "Acceso QR autónomo, luces LED de encendido gradual y climatización inteligente",
            "grabacion": "Cámaras HD en todas las pistas para visualización y repetición en pantalla táctil",
            "restauracion": "Restaurante bistronómico, bar deportivo, pro-shop de alta gama y zona spa con piscina"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena propia de centros de alto standing",
            "perfil_club": "Complejos deportivos y naves de gran escala en áreas de alta renta",
            "canon_royalties": "Operación directa",
            "inversion_media": "1.500.000€ a 3.500.000€ por centro"
        },
        "diferencial": "El prestigio mediático de Tsonga y la experiencia de un verdadero country club con tenis, pádel, spa y alta gastronomía."
    },
    {
        "id": "cuatro-padel",
        "nombre": "4PADEL / Le Five",
        "pais": "Francia",
        "pais_codigo": "FR",
        "region_filtro": "FR",
        "bandera": "🇫🇷",
        "ciudad_sede": "París / Toulouse",
        "coords": [
            48.8566,
            2.3522
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "22 centros en Francia",
        "num_pistas": "135+ pistas",
        "software": "App Propia 4PADEL / Doinsport",
        "fundadores": "Grupo Le Five (Guillaume Debelmas y Joseph Viéville)",
        "web": "https://4padel.fr",
        "tagline": "El líder indiscutible del pádel en Francia con más de 20 complejos cubiertos.",
        "resumen": "Nacido de la reconversión de las naves de fútbol 5 de Le Five, 4PADEL se ha convertido en el gigante francés de la raqueta. Opera complejos masivos como 4PADEL Toulouse Colomiers (11 pistas), 4PADEL Strasbourg, Rouen, Burdeos y Marville (París), con torneos de la Federación Francesa (FFT) y ligas de empresas.",
        "sedes_principales": [
            "4PADEL Toulouse-Colomiers (11 pistas indoor de competición)",
            "4PADEL Strasbourg (Estrasburgo - 7 pistas indoor)",
            "4PADEL Bordeaux (Burdeos - 9 pistas)",
            "4PADEL Rouen",
            "4PADEL Marville / París Norte",
            "Centros en Metz, Mulhouse, Valenciennes y La Rochelle"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas cubiertas con aislamiento térmico y césped monofilamento azul",
            "software": "App móvil 4PADEL y Doinsport",
            "domotica": "Acceso integrado con tornos y control automatizado de iluminación",
            "grabacion": "Sistemas de vídeo en pista para torneos P1000 y P2000 FFT",
            "restauracion": "Sports Bar con pantallas gigantes para partidos de fútbol y pro-shop Babolat oficial"
        },
        "modelo_expansion": {
            "tipo_contrato": "Red corporativa propia y expansión vía reconversión de centros Le Five",
            "perfil_club": "Naves industriales de más de 2.500m² con altura superior a 8 metros",
            "canon_royalties": "Operación directa",
            "inversion_media": "800.000€ a 1.800.000€ por club"
        },
        "diferencial": "La mayor red de pistas cubiertas de Francia y acuerdo histórico como centro oficial de la Federación Francesa de Tenis."
    },
    {
        "id": "urbanpadel",
        "nombre": "UrbanPadel (UrbanSoccer)",
        "pais": "Francia",
        "pais_codigo": "FR",
        "region_filtro": "FR",
        "bandera": "🇫🇷",
        "ciudad_sede": "Lille / Nantes / París",
        "coords": [
            50.6292,
            3.0573
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "15 centros con pádel",
        "num_pistas": "75+ pistas",
        "software": "UrbanSoccer App / MyUrban",
        "fundadores": "UrbanSoccer Group",
        "web": "https://urbanpadel.fr",
        "tagline": "La división de pádel del mayor operador de deportes de equipo indoor de Francia.",
        "resumen": "Cadena desarrollada por UrbanSoccer que aprovecha sus centros multideportivos premium en las grandes metrópolis francesas para implantar naves de pádel climatizadas: UrbanPadel Lille-Lezennes, Nantes-Carquefou, Clermont-Ferrand, Toulouse-Montaudran, Evry, Asnières y Estrasburgo.",
        "sedes_principales": [
            "UrbanPadel Lille-Lezennes (6 pistas indoor)",
            "UrbanPadel Nantes-Carquefou (6 pistas)",
            "UrbanPadel Clermont-Ferrand (6 pistas)",
            "UrbanPadel Evry-Courcouronnes",
            "UrbanPadel Asnières / París y Toulouse-Montaudran"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas cubiertas con césped texturizado",
            "software": "MyUrban App",
            "domotica": "Acceso QR, taquillas electrónicas y climatización",
            "grabacion": "Grabación de partidos para ligas corporativas",
            "restauracion": "Clubhouse con barra cervecera, pantallas deportivas y vestuarios de lujo"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena de explotación propia integrada en la infraestructura UrbanSoccer",
            "perfil_club": "Naves de 1.500m² a 3.000m² adyacentes a campos de fútbol 5",
            "canon_royalties": "Operación directa",
            "inversion_media": "500.000€ a 1.200.000€"
        },
        "diferencial": "Sinergia de tráfico con cientos de miles de practicantes de fútbol sala y torneos after-work."
    },
    {
        "id": "padelshot",
        "nombre": "PadelShot",
        "pais": "Francia",
        "pais_codigo": "FR",
        "region_filtro": "FR",
        "bandera": "🇫🇷",
        "ciudad_sede": "Caen / Saint-Étienne / Metz",
        "coords": [
            49.1828,
            -0.3707
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "4 centros en Francia",
        "num_pistas": "36+ pistas",
        "software": "Gestion Sports / Doinsport",
        "fundadores": "Jérôme Doligé (ex-fundador de Mademoiselle Bio)",
        "web": "https://padelshot.fr",
        "tagline": "Clubes de pádel y ocio social con billares, petanca indoor y restauración de calidad.",
        "resumen": "Cadena que concibe el pádel como un verdadero 'tercer lugar' social. En sus complejos en Caen Mondeville, Saint-Étienne, Metz y Lyon Craponne, cada centro cuenta con al menos 8 pistas cubiertas de gran altura, pistas de bádminton, petanca interior, mesas de ping-pong y una cuidada gastronomía.",
        "sedes_principales": [
            "PadelShot Caen Mondeville (10 pistas cubiertas)",
            "PadelShot Saint-Étienne (8 pistas cubiertas)",
            "PadelShot Metz (8 pistas cubiertas)",
            "PadelShot Lyon Craponne (8 pistas cubiertas)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con césped sin arena visible y techos de 9 a 11 metros",
            "software": "Gestion Sports",
            "domotica": "Acceso automatizado y control térmico",
            "grabacion": "Pantallas en el clubhouse con repetición de partidos",
            "restauracion": "Restaurante con cocina casera fresca, barra de cervezas artesanales y terraza"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena propia financiada por fondos familiares de inversión",
            "perfil_club": "Naves de 3.000m² a 5.000m² en zonas periurbanas de fácil acceso",
            "canon_royalties": "Operación directa",
            "inversion_media": "1.200.000€ a 2.200.000€ por club"
        },
        "diferencial": "La dimensión lúdica multideporte (petanca, billar) que atrae a grupos enteros de empresas y familias."
    },
    {
        "id": "casa-padel",
        "nombre": "Casa Padel",
        "pais": "Francia",
        "pais_codigo": "FR",
        "region_filtro": "FR",
        "bandera": "🇫🇷",
        "ciudad_sede": "París (Saint-Denis)",
        "coords": [
            48.92,
            2.36
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "2 macrocentros parisinos",
        "num_pistas": "16+ pistas",
        "software": "Gestion Sports / Playtomic",
        "fundadores": "José Manuel López & Casa Padel Group",
        "web": "https://casapadel.fr",
        "tagline": "El pionero del pádel indoor en París, sede habitual de los grandes torneos del norte de Francia.",
        "resumen": "Casa Padel abrió el camino en la región parisina con su impresionante instalación de 12 pistas cubiertas en Saint-Denis, complementada con su centro de Asnières-sur-Seine. Cuenta con centro de bienestar osteopático, fitness y el restaurante gastronómico 'La Padella'.",
        "sedes_principales": [
            "Casa Padel Saint-Denis (12 pistas indoor de competición y centro osteopático)",
            "Casa Padel Dos Asnières-sur-Seine"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de competición WPT de moqueta azul",
            "software": "Gestion Sports y Playtomic",
            "domotica": "Control digital de pistas e iluminación",
            "grabacion": "Pistas centrales con streaming para la FFT",
            "restauracion": "Restaurante italiano La Padella, spa, masajes y sala de fitness"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena propia de centros integrales de deporte y salud",
            "perfil_club": "Naves diáfanas de más de 4.000 m² en el área metropolitana de París",
            "canon_royalties": "Operación directa",
            "inversion_media": "1.800.000€ a 3.000.000€"
        },
        "diferencial": "Pionero absoluto en París con una atmósfera hispano-francesa y enfoque en la salud y osteopatía deportiva."
    },
    {
        "id": "padel-horizon",
        "nombre": "Padel Horizon",
        "pais": "Francia",
        "pais_codigo": "FR",
        "region_filtro": "FR",
        "bandera": "🇫🇷",
        "ciudad_sede": "París Este (Sucy-en-Brie)",
        "coords": [
            48.7711,
            2.5233
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 centros",
        "num_pistas": "12+ pistas",
        "software": "Gestion Sports",
        "fundadores": "Loïc Revol & Padel Horizon Group",
        "web": "https://padel-horizon.com",
        "tagline": "El club multirraqueta indoor de referencia en el este de París.",
        "resumen": "Instalación de referencia en la comarca del Val-de-Marne con 6 pistas cubiertas de gran altura, 4 pistas de squash y 4 de bádminton, con un club social vibrante y torneos homologados FFT P500 y P1000.",
        "sedes_principales": [
            "Padel Horizon Sucy-en-Brie (6 pistas indoor)",
            "Instalaciones satélites asociadas en Île-de-France"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas de cristal templado panorámicas y cerramiento aislante",
            "software": "Gestion Sports",
            "domotica": "Acceso QR y reservas digitales",
            "grabacion": "Cámaras cenitales para análisis de torneos",
            "restauracion": "Clubhouse con cervezas de abadía, hamburguesas caseras y terraza"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios",
            "perfil_club": "Naves de 2.000 a 4.000 m²",
            "canon_royalties": "Operación directa",
            "inversion_media": "800.000€ a 1.500.000€"
        },
        "diferencial": "Comunidad muy fiel de deportes de raqueta (pádel, squash, bádminton) en el este parisino."
    },
    {
        "id": "padel-tolosa",
        "nombre": "Padel Tolosa",
        "pais": "Francia",
        "pais_codigo": "FR",
        "region_filtro": "FR",
        "bandera": "🇫🇷",
        "ciudad_sede": "Toulouse / Montauban / Albi",
        "coords": [
            43.6047,
            1.4442
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "4 clubes con el mismo nombre",
        "num_pistas": "22+ pistas",
        "software": "Gestion Sports",
        "fundadores": "Jérôme Cauquil & Padel Tolosa Group",
        "web": "https://padeltolosa.fr",
        "tagline": "La cadena de referencia de Occitania: Toulouse, Montauban, Albi y Rodez.",
        "resumen": "Padel Tolosa ha tejido la red más consolidada del suroeste francés. Opera 4 centros bajo la misma marca en ciudades clave de la región de Occitania, ofreciendo naves cubiertas, escuelas de pádel para niños y adultos y una gastronomía regional con tapas y vinos de la tierra.",
        "sedes_principales": [
            "Padel Tolosa Toulouse (nave de 6 pistas cubiertas)",
            "Padel Tolosa Montauban (6 pistas cubiertas)",
            "Padel Tolosa Albi (5 pistas cubiertas)",
            "Padel Tolosa Rodez (5 pistas cubiertas)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con césped monofilamento azul y techos libres de obstáculos",
            "software": "Gestion Sports",
            "domotica": "Acceso autónomo con código en app y encendido de proyectores LED",
            "grabacion": "Sistemas para retransmisión de torneos P250 y P500",
            "restauracion": "Bistró del club con embutidos artesanales del suroeste francés y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena de clubes propios y franquicia regional",
            "perfil_club": "Naves de 1.800m² a 2.500m² en cabeceras de comarca de Occitania",
            "canon_royalties": "Gestión unificada de la marca Padel Tolosa",
            "inversion_media": "450.000€ a 800.000€ por club"
        },
        "diferencial": "Liderazgo incontestable en el suroeste francés (cuna del pádel galo) y fuerte identidad local."
    },
    {
        "id": "esprit-padel",
        "nombre": "Esprit Padel",
        "pais": "Francia",
        "pais_codigo": "FR",
        "region_filtro": "FR",
        "bandera": "🇫🇷",
        "ciudad_sede": "Lyon (Saint-Priest)",
        "coords": [
            45.6961,
            4.945
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 macrocentros",
        "num_pistas": "16+ pistas",
        "software": "Gestion Sports / Playtomic",
        "fundadores": "Sébastien Cornet & Esprit Padel",
        "web": "https://espritpadel.com",
        "tagline": "El templo indoor pionero de Lyon, con 8 pistas cubiertas climatizadas y gran escuela.",
        "resumen": "Referente de calidad en la región de Lyon con 8 pistas de pádel 100% cubiertas y climatizadas en Saint-Priest, césped de competición y una de las academias de entrenamiento técnico más reconocidas del país.",
        "sedes_principales": [
            "Esprit Padel Saint-Priest (Lyon - 8 pistas indoor climatizadas)",
            "Expansión en el cinturón este de Lyon"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con climatización verano/invierno",
            "software": "Gestion Sports",
            "domotica": "Acceso automatizado y control térmico inteligente",
            "grabacion": "Vídeo en pista para análisis de coaching",
            "restauracion": "Restaurante con platos del día frescos, barra y terraza"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios",
            "perfil_club": "Naves industriales de gran formato",
            "canon_royalties": "Operación directa",
            "inversion_media": "1.000.000€ a 1.800.000€"
        },
        "diferencial": "La climatización integral de las naves en Lyon y la calidad docente de su equipo técnico."
    },
    {
        "id": "mouratoglou-padel",
        "nombre": "Mouratoglou Padel Country Club",
        "pais": "Francia",
        "pais_codigo": "FR",
        "region_filtro": "FR",
        "bandera": "🇫🇷",
        "ciudad_sede": "Biot / Sophia Antipolis (Costa Azul)",
        "coords": [
            43.6261,
            7.0722
        ],
        "modelo": "Academia & Pro-Shop",
        "modelo_badge": "bg-amber-100 text-amber-800 border-amber-200",
        "tipo_categoria": "academia",
        "escala": "macro",
        "num_clubs": "2 centros de élite",
        "num_pistas": "14+ pistas",
        "software": "App Propia Mouratoglou / Playtomic",
        "fundadores": "Patrick Mouratoglou (entrenador de Serena Williams, Tsitsipas)",
        "web": "https://mouratoglou.com",
        "tagline": "El centro de excelencia deportiva de Patrick Mouratoglou en el corazón de la Costa Azul.",
        "resumen": "Dentro del resort de tenis de fama mundial en Biot (Sophia Antipolis), la Mouratoglou Academy ha construido una de las mejores instalaciones de pádel de Europa con 8 pistas panorámicas al aire libre y cubiertas, centro de alto rendimiento, hotel de 4 estrellas y clínica médico-deportiva.",
        "sedes_principales": [
            "Mouratoglou Academy Sophia Antipolis (8 pistas panorámicas)",
            "Centros satélites en resorts internacionales Mouratoglou"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas de competición con moqueta World Padel Tour de última generación",
            "software": "Plataforma Mouratoglou y Playtomic",
            "domotica": "Acceso biométrico e iluminación LED de calidad televisiva",
            "grabacion": "Sistemas de biomecánica y vídeo análisis de élite",
            "restauracion": "Resort spa 4 estrellas, restaurante nutricional y tienda de 300m²"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros de alto rendimiento en resorts de lujo internacionales",
            "perfil_club": "Academias de formación y resorts de cinco estrellas",
            "canon_royalties": "Licencia y metodología Mouratoglou",
            "inversion_media": "Más de 3.000.000€"
        },
        "diferencial": "El prestigio del nombre Patrick Mouratoglou y la infraestructura médica y de rendimiento más avanzada del mundo."
    },
    {
        "id": "winwin-padel",
        "nombre": "WinWin Padel",
        "pais": "Francia",
        "pais_codigo": "FR",
        "region_filtro": "FR",
        "bandera": "🇫🇷",
        "ciudad_sede": "Cabriès / Nîmes (Provenza)",
        "coords": [
            43.435,
            5.34
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "2 macrocomplejos",
        "num_pistas": "25+ pistas",
        "software": "Gestion Sports",
        "fundadores": "Sébastien Tendero & WinWin Group",
        "web": "https://winwin-padel.com",
        "tagline": "El mayor club al aire libre de Francia: 15 pistas en el bosque de Cabriès Arbois.",
        "resumen": "WinWin Padel creó el club al aire libre más espectacular de Francia en Cabriès Arbois (15 pistas panorámicas inmersas en un pinar mediterráneo junto a Aix-en-Provence), complementado con su sede de Nîmes Hauts de Nîmes, uniendo deporte y naturaleza.",
        "sedes_principales": [
            "WinWin Padel Cabriès Arbois (15 pistas: cubiertas y exteriores en el bosque)",
            "WinWin Padel Nîmes (Hauts de Nîmes)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de cristal integradas con pérgolas y cubiertas curvas",
            "software": "Gestion Sports",
            "domotica": "Acceso QR automatizado",
            "grabacion": "Cámaras para ligas y torneos P500",
            "restauracion": "Restaurante con terraza de madera en medio del pinar, barbacoas y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Macrocomplejos en enclaves naturales periurbanos",
            "perfil_club": "Parcelas de más de 15.000 m² con abundante arbolado",
            "canon_royalties": "Operación directa",
            "inversion_media": "1.500.000€ a 2.500.000€"
        },
        "diferencial": "Jugar al pádel en un bosque mediterráneo provenzal con una estética inigualable."
    },
    {
        "id": "my-center-padel",
        "nombre": "My Center Padel",
        "pais": "Francia",
        "pais_codigo": "FR",
        "region_filtro": "FR",
        "bandera": "🇫🇷",
        "ciudad_sede": "Palavas-les-Flots / La Grande Motte",
        "coords": [
            43.5283,
            3.9317
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "3 clubes en la costa mediterránea",
        "num_pistas": "18+ pistas",
        "software": "Gestion Sports",
        "fundadores": "Yannick Maurel & My Center Group",
        "web": "https://mycenterpadel.com",
        "tagline": "Pádel frente al mar en los centros turísticos más cotizados de la costa occitana.",
        "resumen": "Cadena especializada en complejos costeros en el litoral mediterráneo francés (Palavas-les-Flots, La Grande Motte y Cap d'Agde), combinando turismo de sol, escuelas de pádel y torneos P1000 durante todo el verano.",
        "sedes_principales": [
            "My Center Palavas-les-Flots (8 pistas junto al puerto)",
            "My Center La Grande Motte (6 pistas)",
            "My Center Cap d'Agde"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas tratadas contra la corrosión marina y salina",
            "software": "Gestion Sports",
            "domotica": "Acceso autónomo con código digital",
            "grabacion": "Pistas centrales con streaming",
            "restauracion": "Chiringuito lounge, cócteles de verano y terraza chill-out"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena propia y concesiones municipales en puertos deportivos",
            "perfil_club": "Zonas turísticas costeras con gran afluencia estacional y residencial",
            "canon_royalties": "Operación directa",
            "inversion_media": "400.000€ a 900.000€"
        },
        "diferencial": "Ubicación privilegiada en los mayores puertos de recreo del sur de Francia."
    },
    {
        "id": "forest-hill-padel",
        "nombre": "Forest Hill",
        "pais": "Francia",
        "pais_codigo": "FR",
        "region_filtro": "FR",
        "bandera": "🇫🇷",
        "ciudad_sede": "París (Aquaboulevard)",
        "coords": [
            48.8319,
            2.2778
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "4 macrocomplejos parisinos con pádel",
        "num_pistas": "30+ pistas",
        "software": "App Propia Forest Hill / Resasports",
        "fundadores": "Grupo Forest Hill (Michel Corbière)",
        "web": "https://forest-hill.fr",
        "tagline": "La histórica red de clubes deportivos de París que ha volcado sus instalaciones al pádel.",
        "resumen": "Forest Hill es una institución en París. Famoso por el parque acuático Aquaboulevard de París (Porte de Versailles), la cadena ha transformado pistas de tenis en auténticos núcleos de pádel cubierto en Nanterre La Défense, Marne-la-Vallée y Villejuif, sumando más de 30 pistas bajo la misma enseña.",
        "sedes_principales": [
            "Forest Hill Aquaboulevard (París Porte de Versailles - pistas cubiertas)",
            "Forest Hill Nanterre City Form (La Défense)",
            "Forest Hill Marne-la-Vallée",
            "Forest Hill Villejuif"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas de cristal templado cubiertas dentro de complejos climatizados",
            "software": "App Forest Hill y tarjeta Pacha Club",
            "domotica": "Tornos de acceso de socios con carnet digital",
            "grabacion": "Sistemas en torneos corporativos de La Défense",
            "restauracion": "Restaurantes, gimnasios de 2.000m², piscinas y saunas"
        },
        "modelo_expansion": {
            "tipo_contrato": "Reconversión de suelo de tenis en centros propios",
            "perfil_club": "Megacomplejos polideportivos en París intramuros y primera corona",
            "canon_royalties": "Operación directa",
            "inversion_media": "Más de 3.000.000€ por complejo"
        },
        "diferencial": "La tarjeta Pacha Forest Hill con acceso ilimitado a pádel, tenis, gimnasio y parques acuáticos en París."
    },
    {
        "id": "spector-padel-house",
        "nombre": "Spector Padel House (SPH)",
        "pais": "Italia",
        "pais_codigo": "IT",
        "region_filtro": "IT",
        "bandera": "🇮🇹",
        "ciudad_sede": "Milano / Firenze / Venezia",
        "coords": [
            45.4642,
            9.19
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "10+ centros en toda Italia",
        "num_pistas": "65+ pistas cubiertas",
        "software": "Playtomic",
        "fundadores": "Gustavo Spector (ex-seleccionador nacional de Italia)",
        "web": "https://spectorhouse.com",
        "tagline": "La mayor cadena multiclub de Italia creada por el legendario seleccionador Gustavo Spector.",
        "resumen": "Spector Padel House (SPH) es la red más prestigiosa de clubes de pádel de Italia. Fundada por el legendario entrenador argentino-italiano Gustavo Spector, opera grandes centros indoor diseñados para crear comunidad: Milano Barona (Via Ovada), Venezia Mestre, Firenze Campi Bisenzio (dentro del complejo Hidron), Monza-Brugherio, Treviso, Lodi y Bolonia.",
        "sedes_principales": [
            "SPH Milano Barona (Via Ovada - 6 pistas cubiertas)",
            "SPH Venezia Mestre (Via Linghindal - 6 pistas indoor)",
            "SPH Firenze / Campi Bisenzio (complejo Hidron)",
            "SPH Monza-Brugherio (Via Magellano)",
            "SPH Treviso / Breda di Piave",
            "SPH Lodi y Bolonia"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas indoor de competición con altura libre >9 metros y césped oficial",
            "software": "Playtomic integrado con el sistema docente Spector Method",
            "domotica": "Acceso QR autónomo y climatización industrial",
            "grabacion": "Cámaras cenitales en pista para corrección técnica de los alumnos",
            "restauracion": "Clubhouse con bistró italiano, café espresso de especialidad y pro-shop completa"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena propia y franquicias asociadas bajo la marca Spector Padel House",
            "perfil_club": "Naves de 2.000 a 4.000m² con mínimo 5 pistas y casa club de diseño",
            "canon_royalties": "Canon de marca + metodología Spector Padel Academy",
            "inversion_media": "800.000€ a 1.600.000€ por club"
        },
        "diferencial": "El método docente 'Spector Method' y la figura de Gustavo Spector, el entrenador más respetado de la historia del pádel en Italia."
    },
    {
        "id": "country-sport-village",
        "nombre": "Country Sport Village",
        "pais": "Italia",
        "pais_codigo": "IT",
        "region_filtro": "IT",
        "bandera": "🇮🇹",
        "ciudad_sede": "Milán (Mirabello di Senago)",
        "coords": [
            45.5786,
            9.1258
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "2 macrocentros",
        "num_pistas": "25+ pistas",
        "software": "Playtomic",
        "fundadores": "Country Sport Village Group",
        "web": "https://countrysportvillage.it",
        "tagline": "El mayor complejo de pádel cubierto de toda Italia: 21 pistas bajo una sola nave.",
        "resumen": "Situado en Mirabello di Senago, en el área metropolitana norte de Milán, es el macrocentro de referencia absoluto en el país transalpino. Alberga 21 pistas cubiertas bajo naves climatizadas, piscina exterior, campos de fútbol y restaurante para 300 comensales.",
        "sedes_principales": [
            "Country Sport Village Senago (21 pistas cubiertas, el récord de Italia)",
            "Instalaciones satélites asociadas en Lombardía"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de cristal templado bajo estructura industrial climatizada",
            "software": "Playtomic",
            "domotica": "Control digital de iluminación y accesos",
            "grabacion": "Sistemas para emisión en streaming de torneos de la FITP",
            "restauracion": "Gran restaurante con pizzería de horno de leña, piscina de verano y lounge bar"
        },
        "modelo_expansion": {
            "tipo_contrato": "Megacentro en propiedad y gestión corporativa",
            "perfil_club": "Suelos industriales y deportivos de más de 15.000 m²",
            "canon_royalties": "Operador directo",
            "inversion_media": "Más de 3.500.000€"
        },
        "diferencial": "Capacidad monumental sin rival en Italia: 21 pistas cubiertas que permiten organizar los torneos más multitudinarios de Europa."
    },
    {
        "id": "padel-palace-milano",
        "nombre": "Padel Palace",
        "pais": "Italia",
        "pais_codigo": "IT",
        "region_filtro": "IT",
        "bandera": "🇮🇹",
        "ciudad_sede": "Milán",
        "coords": [
            45.495,
            9.215
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "boutique",
        "num_clubs": "2 centros milaneses",
        "num_pistas": "10+ pistas",
        "software": "Playtomic",
        "fundadores": "Alessandro Borghese, Diletta Leotta, Max Giusti y Gabriele Corsi",
        "web": "https://padelpalace.it",
        "tagline": "El club de las celebridades en Milán con el restaurante de alta cocina de Alessandro Borghese.",
        "resumen": "Ubicado en Via Privata Flumendosa en Milán, Padel Palace ha unido a las mayores estrellas de la televisión, la gastronomía y el deporte italiano. Cuenta con 5 pistas cubiertas de diseño y el restaurante 'AB – Il Lusso della Semplicità' del chef Alessandro Borghese.",
        "sedes_principales": [
            "Padel Palace Milano (Via Privata Flumendosa)",
            "Padel Palace Pop-Up VIP Arenas"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de cristal templado de 12mm con césped azul de máxima densidad",
            "software": "Playtomic",
            "domotica": "Acceso QR, iluminación LED para televisión",
            "grabacion": "Cámaras en pista para eventos mediáticos",
            "restauracion": "Restaurante gourmet de Alessandro Borghese y lounge bar de cócteles"
        },
        "modelo_expansion": {
            "tipo_contrato": "Clubes boutique en ciudades de alta renta con celebridades locales",
            "perfil_club": "Naves de diseño industrial de 4 a 8 pistas con alta gastronomía",
            "canon_royalties": "Operación directa corporativa",
            "inversion_media": "1.200.000€ a 2.500.000€"
        },
        "diferencial": "La mayor repercusión mediática de Italia gracias a la presencia constante de celebridades y futbolistas del AC Milan e Inter."
    },
    {
        "id": "city-padel-milano",
        "nombre": "City Padel Milano / Golden Goose Arena",
        "pais": "Italia",
        "pais_codigo": "IT",
        "region_filtro": "IT",
        "bandera": "🇮🇹",
        "ciudad_sede": "Milán (CityLife)",
        "coords": [
            45.478,
            9.155
        ],
        "modelo": "Boutique & Ultra-Lujo",
        "modelo_badge": "bg-purple-100 text-purple-800 border-purple-200",
        "tipo_categoria": "boutique",
        "escala": "boutique",
        "num_clubs": "2 centros en CityLife",
        "num_pistas": "10+ pistas",
        "software": "Playtomic",
        "fundadores": "Demetrio Albertini (leyenda del AC Milan) y Pierluigi Casiraghi",
        "web": "https://citypadelmilano.it",
        "tagline": "El club icono de CityLife bajo los rascacielos de Zaha Hadid y Libeskind.",
        "resumen": "Situado en el parque de CityLife, el barrio más moderno y exclusivo de Milán. Fundado por Demetrio Albertini, cuenta con pistas panorámicas con vistas a los tres rascacielos milaneses, patrocinadas por firmas de moda de lujo como Golden Goose.",
        "sedes_principales": [
            "City Padel Milano (CityLife Park - pistas bajo los rascacielos)",
            "Golden Goose Arena CityLife"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de última generación y pista central Golden Goose de diseño",
            "software": "Playtomic",
            "domotica": "Control digital y accesos integrados",
            "grabacion": "Producción de vídeo para torneos de leyendas del fútbol",
            "restauracion": "Clubhouse de diseño italiano, café espresso y pro-shop premium"
        },
        "modelo_expansion": {
            "tipo_contrato": "Emplazamientos urbanos prime icónicos",
            "perfil_club": "Parques urbanos de máximo nivel arquitectónico",
            "canon_royalties": "Operación directa",
            "inversion_media": "1.500.000€ a 3.000.000€"
        },
        "diferencial": "Jugar al pádel a los pies de las tres torres de CityLife en el club más 'fashion' de Milán."
    },
    {
        "id": "ghost-padel",
        "nombre": "Ghost Padel",
        "pais": "Italia",
        "pais_codigo": "IT",
        "region_filtro": "IT",
        "bandera": "🇮🇹",
        "ciudad_sede": "Milano / Roma",
        "coords": [
            45.4642,
            9.19
        ],
        "modelo": "Franquicia Llave en Mano",
        "modelo_badge": "bg-indigo-100 text-indigo-800 border-indigo-200",
        "tipo_categoria": "franquicia",
        "escala": "media",
        "num_clubs": "12 pistas franquiciadas en clubes",
        "num_pistas": "12+ pistas patentadas",
        "software": "Playtomic / Ghost Padel App",
        "fundadores": "Gianluca Vacchi & inventores italianos patentados",
        "web": "https://ghostpadel.com",
        "tagline": "La franquicia patentada mundial que permite jugar al pádel a oscuras con luz ultravioleta.",
        "resumen": "Ghost Padel es una patente internacional revolucionaria nacida en Italia. Transforma cualquier pista indoor en una experiencia inmersiva: el juego se realiza completamente a oscuras, donde solo brillan las líneas fluorescentes de la pista, la red luminosa, la bola reactiva UV y la ropa blanca y neón de los jugadores.",
        "sedes_principales": [
            "Ghost Padel Arena Milano",
            "Ghost Padel Roma",
            "Centros franquiciados en España, Miami y Dubái"
        ],
        "tecnologia_pistas": {
            "pistas": "Cristales tratados anti-reflejo y líneas perimetrales luminiscentes patentadas",
            "software": "Playtomic",
            "domotica": "Sistema domótico de cambio instantáneo de luz blanca a modo UV neón",
            "grabacion": "Cámaras especiales con sensores de infrarrojos y visión nocturna UV",
            "restauracion": "Bares temáticos con cócteles fluorescentes y música electrónica"
        },
        "modelo_expansion": {
            "tipo_contrato": "Licencia tecnológica de franquicia e instalación sobre pista existente",
            "perfil_club": "Clubes de pádel cubiertos que quieren una pista gancho muy viral",
            "canon_royalties": "Kit de reconversión de pista + canon de marca anual",
            "inversion_media": "25.000€ a 45.000€ (kit de conversión por pista)"
        },
        "diferencial": "Viralidad brutal en TikTok e Instagram y tarifa por hora hasta un 40% más cara que una pista convencional."
    },
    {
        "id": "joy-padel-club",
        "nombre": "Joy Padel Club",
        "pais": "Italia",
        "pais_codigo": "IT",
        "region_filtro": "IT",
        "bandera": "🇮🇹",
        "ciudad_sede": "Milano (Tolcinasco)",
        "coords": [
            45.36,
            9.16
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 centros",
        "num_pistas": "14+ pistas",
        "software": "Playtomic",
        "fundadores": "Joy Padel Management",
        "web": "https://joypadelclub.it",
        "tagline": "Pádel premium integrado en castillos históricos y clubes de golf de Lombardía.",
        "resumen": "Ubicado dentro del prestigioso complejo del Castello di Tolcinasco Golf Club (siglo XVI), Joy Padel Club ofrece una experiencia señorial donde el deporte de la pala se practica rodeado de murallas históricas, greens de golf y gastronomía lombarda.",
        "sedes_principales": [
            "Joy Padel Tolcinasco (8 pistas cubiertas de gran altura)",
            "Joy Padel Basiglio"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con cubiertas tensadas de arquitectura integrada",
            "software": "Playtomic",
            "domotica": "Control digital de pistas",
            "grabacion": "Vídeo en torneos de empresas",
            "restauracion": "Restaurante del club de golf Tolcinasco, piscina y sauna"
        },
        "modelo_expansion": {
            "tipo_contrato": "Alianzas en complejos de golf y resorts históricos",
            "perfil_club": "Country clubs exclusivos",
            "canon_royalties": "Operación propia",
            "inversion_media": "600.000€ a 1.200.000€"
        },
        "diferencial": "El entorno monumental único de un castillo lombardo y la tranquilidad de un club de golf privado."
    },
    {
        "id": "smash-padel-italia",
        "nombre": "Smash Padel Pesaro & Fano",
        "pais": "Italia",
        "pais_codigo": "IT",
        "region_filtro": "IT",
        "bandera": "🇮🇹",
        "ciudad_sede": "Pesaro / Fano (Marche)",
        "coords": [
            43.91,
            12.91
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 macrocentros en la costa adriática",
        "num_pistas": "16+ pistas",
        "software": "Playtomic",
        "fundadores": "Smash Sports Group Italia",
        "web": "https://smashpadel.it",
        "tagline": "El gigante del pádel adriático: naves climatizadas y torneos multitudinarios.",
        "resumen": "Smash Padel es el referente de la costa adriática italiana. En sus dos macrocentros de Pesaro y Fano cuenta con pistas cubiertas climatizadas que han formado a los mejores jugadores de la región de Marche.",
        "sedes_principales": [
            "Smash Padel Pesaro (8 pistas indoor climatizadas)",
            "Smash Padel Fano (8 pistas cubiertas)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con césped texturizado monofilamento",
            "software": "Playtomic",
            "domotica": "Acceso QR y gestión lumínica",
            "grabacion": "Pistas con cámaras para torneos regionales",
            "restauracion": "Pizzería bar con aperitivos italianos y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena de centros propios",
            "perfil_club": "Naves de 2.000 a 4.000 m²",
            "canon_royalties": "Operación directa",
            "inversion_media": "700.000€ a 1.400.000€"
        },
        "diferencial": "Dominio regional en el centro de Italia y eventos sociales con música y aperitivos tras cada partido."
    },
    {
        "id": "bola-padel-roma",
        "nombre": "Bola Padel Club",
        "pais": "Italia",
        "pais_codigo": "IT",
        "region_filtro": "IT",
        "bandera": "🇮🇹",
        "ciudad_sede": "Roma (Ostiense / Aurelia)",
        "coords": [
            41.9028,
            12.4964
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "2 centros romanos",
        "num_pistas": "18+ pistas",
        "software": "Playtomic",
        "fundadores": "Bola Sports Roma",
        "web": "https://bolapadelclub.it",
        "tagline": "El club de pádel urbano por excelencia en la capital de Italia.",
        "resumen": "Bola Padel Club es una de las marcas más populares de Roma. Cuenta con pistas panorámicas de última generación repartidas entre naves cubiertas y espacios exteriores con pérgolas ajardinadas, sede de los mayores torneos de la capital.",
        "sedes_principales": [
            "Bola Padel Club Ostiense (Roma)",
            "Bola Padel Aurelia"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con césped oficial de competición",
            "software": "Playtomic",
            "domotica": "Acceso por app y tornos digitales",
            "grabacion": "Sistemas de vídeo en torneos romanos",
            "restauracion": "Lounge bar con cócteles y cafetería con terraza"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios en suelo urbano romano",
            "perfil_club": "Parcelas de al menos 8 pistas con buena conexión de metro o carretera",
            "canon_royalties": "Operación directa",
            "inversion_media": "900.000€ a 1.800.000€"
        },
        "diferencial": "La comunidad de jugadores más activa del centro de Roma y ambiente festivo constante."
    },
    {
        "id": "orange-padel-roma",
        "nombre": "Orange Padel Club",
        "pais": "Italia",
        "pais_codigo": "IT",
        "region_filtro": "IT",
        "bandera": "🇮🇹",
        "ciudad_sede": "Roma (Eur / Grottaferrata)",
        "coords": [
            41.83,
            12.47
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 centros",
        "num_pistas": "14+ pistas",
        "software": "Playtomic",
        "fundadores": "Orange Club Group",
        "web": "https://orangepadelclub.it",
        "tagline": "Instalaciones cubiertas de vanguardia en el cinturón sur de Roma.",
        "resumen": "Cadena que opera en los distritos de mayor renta del sur de Roma (EUR y Castelli Romani / Grottaferrata). Destaca por la calidad de sus pistas indoor, gimnasio específico de preparación física para pádel y escuela de cantera.",
        "sedes_principales": [
            "Orange Padel Club EUR (Roma)",
            "Orange Padel Grottaferrata"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con iluminación LED antideslumbrante",
            "software": "Playtomic",
            "domotica": "Control inteligente de temperatura y accesos",
            "grabacion": "Vídeo en pista para clases",
            "restauracion": "Bistró con ensaladas y platos proteicos y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios",
            "perfil_club": "Naves de 2.000m²",
            "canon_royalties": "Operación directa",
            "inversion_media": "600.000€ a 1.100.000€"
        },
        "diferencial": "Enfoque deportivo muy serio con preparación física adaptada a jugadores amateurs de nivel avanzado."
    },
    {
        "id": "padel-club-padova",
        "nombre": "Padel Club Padova",
        "pais": "Italia",
        "pais_codigo": "IT",
        "region_filtro": "IT",
        "bandera": "🇮🇹",
        "ciudad_sede": "Padova (Véneto)",
        "coords": [
            45.4064,
            11.8768
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 macrocentros en el Véneto",
        "num_pistas": "14+ pistas",
        "software": "Playtomic",
        "fundadores": "Padel Club Padova Group",
        "web": "https://padelclubpadova.it",
        "tagline": "El bastión del pádel cubierto en el noreste italiano.",
        "resumen": "Referente indiscutible en la provincia de Padua y el Véneto, con grandes naves industriales reconvertidas con pistas panorámicas de última generación, césped monofilamento y escuela federativa de la FITP.",
        "sedes_principales": [
            "Padel Club Padova Indoor Arena",
            "Centro satélite en la provincia de Padua"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas cubiertas climatizadas",
            "software": "Playtomic",
            "domotica": "Acceso QR y taquillas electrónicas",
            "grabacion": "Grabación de torneos oficiales FITP",
            "restauracion": "Bar cafetería italiana y zona de descanso"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios",
            "perfil_club": "Naves de 2.500m²",
            "canon_royalties": "Operación directa",
            "inversion_media": "650.000€ a 1.200.000€"
        },
        "diferencial": "Calidad técnica de sus pistas en una de las regiones más ricas e industrializadas de Italia."
    },
    {
        "id": "arenal-padel",
        "nombre": "Arenal Padel",
        "pais": "Bélgica",
        "pais_codigo": "BE",
        "region_filtro": "NL",
        "bandera": "🇧🇪",
        "ciudad_sede": "Mechelen / Brugge / Antwerpen",
        "coords": [
            51.0257,
            4.4776
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "11 centros en Bélgica y Holanda",
        "num_pistas": "70+ pistas",
        "software": "Playtomic",
        "fundadores": "Arenal Sports Parks",
        "web": "https://arenal.be",
        "tagline": "El gigante indiscutible de Flandes: 11 complejos multideporte con pádel, padbol y camas elásticas.",
        "resumen": "Arenal es la mayor red multideportiva de Bélgica y el sur de Holanda bajo la misma marca. Sus centros combinan naves de pádel indoor y outdoor con academias para jóvenes, padbol, campos de fútbol 5 y parques de camas elásticas en Flandes: Mechelen, Antwerpen, Brugge, Roeselare, Verrebroek, Grimbergen, Knokke, Lommel, Waregem, Bree y Meise.",
        "sedes_principales": [
            "Arenal Mechelen (Koningin Astridlaan - gran centro de pádel, trampolines y fútbol 5)",
            "Arenal Brugge (Sint-Kruis)",
            "Arenal Antwerpen",
            "Arenal Knokke (costa belga)",
            "Arenal Grimbergen y Waregem",
            "Arenal Roeselare, Verrebroek, Lommel, Bree y Meise"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de competición en naves de gran altura con moqueta azul WPT",
            "software": "Playtomic para reservas de pista y torneos locales",
            "domotica": "Acceso QR autónomo y climatización programada",
            "grabacion": "Cámaras cenitales en pista central",
            "restauracion": "Clubhouse con barra de cervezas belgas de abadía, snacks calientes y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena propia de centros multideporte familiares",
            "perfil_club": "Naves de 3.000m² a 6.000m² en áreas metropolitanas flamencas",
            "canon_royalties": "Operación directa corporativa",
            "inversion_media": "1.000.000€ a 2.500.000€ por parque deportivo"
        },
        "diferencial": "El concepto de entretenimiento familiar total (pádel + trampolines + padbol) que maximiza la rentabilidad por metro cuadrado."
    },
    {
        "id": "garrincha-padel",
        "nombre": "Garrincha Padel & 5-a-side",
        "pais": "Bélgica",
        "pais_codigo": "BE",
        "region_filtro": "NL",
        "bandera": "🇧🇪",
        "ciudad_sede": "Gante / Amberes / Bruselas",
        "coords": [
            51.0543,
            3.7174
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "4 macrocentros",
        "num_pistas": "28+ pistas",
        "software": "Playtomic",
        "fundadores": "Garrincha Sports Centers",
        "web": "https://garrincha.be",
        "tagline": "El pionero del ocio deportivo urbano en Flandes y Bruselas.",
        "resumen": "Cadena belga muy valorada por la juventud y las empresas. Desarrolla centros cubiertos de diseño contemporáneo que combinan pádel panorámico con fútbol 5 y una hostelería moderna de hamburguesas artesanas y cervezas locales en Gante, Amberes, Bruselas Norte y Charleroi.",
        "sedes_principales": [
            "Garrincha Gent (Gante - 8 pistas de pádel indoor y fútbol)",
            "Garrincha Antwerpen (Amberes)",
            "Garrincha Brussels North",
            "Garrincha Charleroi"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de 10 metros de altura libre en naves industriales recuperadas",
            "software": "Playtomic",
            "domotica": "Acceso 100% digitalizado, gestión de luces con sensores",
            "grabacion": "Sistemas de vídeo y repetición en televisión de la cantina",
            "restauracion": "Cantina urbana de diseño con comida gourmet callejera, cervezas belgas y terraza"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena de clubes propios",
            "perfil_club": "Naves industriales urbanas de 3.000m² a 5.000m²",
            "canon_royalties": "Operación directa",
            "inversion_media": "1.200.000€ a 2.000.000€"
        },
        "diferencial": "Estética industrial muy atractiva para eventos corporativos y ligas de empresas jóvenes."
    },
    {
        "id": "the-padellers",
        "nombre": "The Padellers",
        "pais": "Países Bajos",
        "pais_codigo": "NL",
        "region_filtro": "NL",
        "bandera": "🇳🇱",
        "ciudad_sede": "Ámsterdam / Utrecht",
        "coords": [
            52.3676,
            4.9041
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "26 centros en NL y Alemania",
        "num_pistas": "145+ pistas",
        "software": "Playtomic / App Propia",
        "fundadores": "Philippe van Elsdingen & inversionistas neerlandeses",
        "web": "https://thepadellers.nl",
        "tagline": "El gigante neerlandés en rápida expansión hacia Alemania con más de 25 centros.",
        "resumen": "The Padellers es una de las redes multiclub de crecimiento más agresivo del continente. Con más de 25 centros cubiertos en Ámsterdam (Amstel y Sloterdijk), Utrecht, Breda, Eindhoven, Groningen, Zwolle, Valkenswaard y su salto a Alemania, ofrece pádel indoor, torneos Americano diarios y academias con entrenadores certificados.",
        "sedes_principales": [
            "The Padellers Amsterdam Amstel (8 pistas cubiertas)",
            "The Padellers Amsterdam Sloterdijk",
            "The Padellers Utrecht",
            "The Padellers Breda y Eindhoven",
            "The Padellers Groningen, Zwolle, Geleen y expansión en Alemania"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas cubiertas, moqueta monofilamento de alta durabilidad",
            "software": "Playtomic y The Padellers App",
            "domotica": "Acceso QR, iluminación LED autónoma y ventilación de alta eficiencia",
            "grabacion": "Pantallas en pista y streaming para torneos federados KNLTB",
            "restauracion": "Clubhouse con cervezas de grifo neerlandesas, pizzas caseras y tienda deportiva"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena propia financiada por fondos de capital institucional holandés",
            "perfil_club": "Naves industriales de más de 2.500m² con altura libre >7m",
            "canon_royalties": "Operación directa",
            "inversion_media": "700.000€ a 1.500.000€ por club"
        },
        "diferencial": "Velocidad de ejecución inmobiliaria y expansión internacional probada desde Holanda a Alemania."
    },
    {
        "id": "peakz-padel",
        "nombre": "Peakz Padel",
        "pais": "Países Bajos",
        "pais_codigo": "NL",
        "region_filtro": "NL",
        "bandera": "🇳🇱",
        "ciudad_sede": "Ámsterdam",
        "coords": [
            52.337,
            4.92
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "15+ centros",
        "num_pistas": "110+ pistas",
        "software": "Playtomic",
        "fundadores": "Peakz Padel Management",
        "web": "https://peakzpadel.nl",
        "tagline": "El pionero del pádel en los Países Bajos, famoso por sus clubes en antiguas fábricas de chicles.",
        "resumen": "Peakz Padel es la marca pionera que popularizó el pádel en Holanda. Su sede en la antigua fábrica de chicles de Ámsterdam (Kauwgomballenfabriek) es mítica. Cuenta con más de 15 complejos en las principales ciudades neerlandesas (Ámsterdam, Utrecht, Rotterdam, La Haya, Zwolle, Haarlem, Groningen).",
        "sedes_principales": [
            "Peakz Padel Kauwgomballenfabriek (Ámsterdam - 8 pistas indoor)",
            "Peakz Padel Sloterdijk (Ámsterdam)",
            "Peakz Padel Utrecht Vechtsebanen",
            "Peakz Padel Rotterdam",
            "Peakz Padel Den Haag (La Haya) y Zwolle"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de calidad WPT y naves con altura libre de más de 9 metros",
            "software": "Playtomic",
            "domotica": "Acceso digital automatizado con código QR",
            "grabacion": "Sistemas para emisión en directo de torneos oficiales KNLTB",
            "restauracion": "Bares con diseño holandés contemporáneo, café espresso y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena propia de centros con respaldo de fondos de inversión de ocio",
            "perfil_club": "Edificios industriales históricos y naves logísticas en las 4 grandes ciudades holandesas (Randstad)",
            "canon_royalties": "Operación directa",
            "inversion_media": "900.000€ a 1.800.000€ por centro"
        },
        "diferencial": "El reconocimiento de marca número 1 en el consumidor holandés y sedes en edificios industriales icónicos."
    },
    {
        "id": "plaza-padel",
        "nombre": "Plaza Padel",
        "pais": "Países Bajos",
        "pais_codigo": "NL",
        "region_filtro": "NL",
        "bandera": "🇳🇱",
        "ciudad_sede": "Ámsterdam / Maastricht",
        "coords": [
            52.37,
            4.89
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "6 macrocentros",
        "num_pistas": "42+ pistas",
        "software": "Playtomic",
        "fundadores": "Plaza Padel Group",
        "web": "https://plazapadel.com",
        "tagline": "Grandes naves cubiertas con hostelería española y torneos corporativos masivos.",
        "resumen": "Cadena que destaca por recrear la atmósfera de una 'plaza' mediterránea dentro de naves industriales holandesas en Ámsterdam, Enschede, Heiloo, Maastricht, Waalwijk y Wijchen, con tapas, cerveza fría y pistas de nivel World Padel Tour.",
        "sedes_principales": [
            "Plaza Padel Amsterdam (7 pistas cubiertas)",
            "Plaza Padel Maastricht (6 pistas)",
            "Plaza Padel Enschede y Heiloo",
            "Plaza Padel Waalwijk y Wijchen"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con moqueta azul texturizada y cristal templado",
            "software": "Playtomic",
            "domotica": "Acceso y reserva automatizada",
            "grabacion": "Grabación de partidos para escuelas de adultos",
            "restauracion": "Plaza Lounge con tapas ibéricas, pinchos y cerveza de tirador"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios en núcleos urbanos e industriales",
            "perfil_club": "Naves de 2.500 a 4.000 m²",
            "canon_royalties": "Operación directa",
            "inversion_media": "800.000€ a 1.400.000€"
        },
        "diferencial": "El concepto de Plaza social que alarga la estancia de los jugadores más de dos horas tras el partido."
    },
    {
        "id": "padel-4u2",
        "nombre": "Padel 4U2",
        "pais": "Bélgica",
        "pais_codigo": "BE",
        "region_filtro": "NL",
        "bandera": "🇧🇪",
        "ciudad_sede": "Gante (Flandes)",
        "coords": [
            51.05,
            3.73
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 clubes históricos",
        "num_pistas": "16+ pistas",
        "software": "Playtomic",
        "fundadores": "Padel 4U2 Gent",
        "web": "https://padel4u2.be",
        "tagline": "Uno de los clubes pioneros fundacionales del pádel en Europa continental.",
        "resumen": "Padel 4U2 en Gante es uno de los clubes más antiguos y respetados de Bélgica. Fue fundamental en la introducción del deporte en Centroeuropa y sigue siendo un epicentro de torneos internacionales y formación.",
        "sedes_principales": [
            "Padel 4U2 Gent (10 pistas: cubiertas y exteriores)",
            "Instalaciones satélites en Flandes Oriental"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas de cristal templado y césped de competición",
            "software": "Playtomic",
            "domotica": "Control digital de iluminación y puertas",
            "grabacion": "Cámaras para torneos FIP",
            "restauracion": "Clubhouse tradicional belga con amplia terraza y bar"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios",
            "perfil_club": "Parcelas deportivas periurbanas",
            "canon_royalties": "Operación directa",
            "inversion_media": "600.000€ a 1.200.000€"
        },
        "diferencial": "Historia y solera: el club donde aprendieron a jugar los primeros campeones belgas."
    },
    {
        "id": "padel-mate-club",
        "nombre": "Padel Mate Club",
        "pais": "Países Bajos",
        "pais_codigo": "NL",
        "region_filtro": "NL",
        "bandera": "🇳🇱",
        "ciudad_sede": "Amstelveen / Ámsterdam",
        "coords": [
            52.3,
            4.86
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 centros",
        "num_pistas": "12+ pistas",
        "software": "Playtomic",
        "fundadores": "Padel Mate Group",
        "web": "https://padelmateclub.nl",
        "tagline": "Pádel boutique y comunidad internacional en el sur de Ámsterdam.",
        "resumen": "Cadena de clubes boutique que atrae a la enorme comunidad internacional y expatriada del sur de Ámsterdam y Amstelveen, combinando instalaciones cuidadas con eventos sociales y clínicas de perfeccionamiento.",
        "sedes_principales": [
            "Padel Mate Club Amstelveen (8 pistas cubiertas)",
            "Padel Mate Amsterdam South"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con césped texturizado de alta gama",
            "software": "Playtomic",
            "domotica": "Acceso QR y taquillas electrónicas",
            "grabacion": "Sistemas para revisión de clases",
            "restauracion": "Cafetería de diseño con café de especialidad y terraza"
        },
        "modelo_expansion": {
            "tipo_contrato": "Clubes propios",
            "perfil_club": "Naves urbanas de diseño",
            "canon_royalties": "Operación propia",
            "inversion_media": "650.000€ a 1.100.000€"
        },
        "diferencial": "Perfil de cliente expatriado de muy alto poder adquisitivo y ambiente multilingüe."
    },
    {
        "id": "padel-dam",
        "nombre": "Padel Dam",
        "pais": "Países Bajos",
        "pais_codigo": "NL",
        "region_filtro": "NL",
        "bandera": "🇳🇱",
        "ciudad_sede": "Ámsterdam West",
        "coords": [
            52.375,
            4.85
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 centros",
        "num_pistas": "14+ pistas",
        "software": "Playtomic",
        "fundadores": "Padel Dam Group",
        "web": "https://padeldam.nl",
        "tagline": "Pádel urbano en el corazón cultural del oeste de Ámsterdam.",
        "resumen": "Situado en el área de Ámsterdam West, este operador multiclub destaca por su vinculación con la escena creativa de la ciudad, albergando torneos nocturnos con DJ y eventos de empresas tecnológicas.",
        "sedes_principales": [
            "Padel Dam West (8 pistas cubiertas)",
            "Padel Dam North"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas en naves de estilo loft industrial",
            "software": "Playtomic",
            "domotica": "Acceso inteligente automatizado",
            "grabacion": "Streaming para redes sociales",
            "restauracion": "Bar craft beer y comida callejera saludable"
        },
        "modelo_expansion": {
            "tipo_contrato": "Clubes propios",
            "perfil_club": "Naves industriales creativas",
            "canon_royalties": "Operación directa",
            "inversion_media": "700.000€ a 1.200.000€"
        },
        "diferencial": "Conexión directa con la comunidad creativa y tech de Ámsterdam."
    },
    {
        "id": "planet-padel-be",
        "nombre": "Planet Padel",
        "pais": "Bélgica",
        "pais_codigo": "BE",
        "region_filtro": "NL",
        "bandera": "🇧🇪",
        "ciudad_sede": "Limburg (Hasselt / Genk)",
        "coords": [
            50.93,
            5.33
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 centros",
        "num_pistas": "14+ pistas",
        "software": "Playtomic",
        "fundadores": "Planet Padel Belgium",
        "web": "https://planetpadel.be",
        "tagline": "El bastión del pádel cubierto en la provincia de Limburgo.",
        "resumen": "Cadena de referencia en el este de Bélgica, con pistas panorámicas cubiertas que atraen tanto a jugadores belgas como a aficionados del sur de los Países Bajos y la frontera alemana de Aquisgrán.",
        "sedes_principales": [
            "Planet Padel Hasselt (8 pistas cubiertas)",
            "Planet Padel Genk"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas de cristal templado de 12mm con césped azul WPT",
            "software": "Playtomic",
            "domotica": "Control digital de iluminación y puertas",
            "grabacion": "Grabación de partidos de torneos regionales",
            "restauracion": "Clubhouse con cervezas locales y cafetería"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios",
            "perfil_club": "Naves industriales de más de 2.000m²",
            "canon_royalties": "Operación directa",
            "inversion_media": "600.000€ a 1.100.000€"
        },
        "diferencial": "Ubicación estratégica en la eurorregión Limburgo-Aquisgrán."
    },
    {
        "id": "padelzone-austria",
        "nombre": "PadelZone Austria",
        "pais": "Austria",
        "pais_codigo": "AT",
        "region_filtro": "DE",
        "bandera": "🇦🇹",
        "ciudad_sede": "Viena / Graz / Wiener Neustadt",
        "coords": [
            48.2082,
            16.3738
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "15+ centros en Austria",
        "num_pistas": "65+ pistas",
        "software": "Playtomic",
        "fundadores": "PadelZone Group Austria",
        "web": "https://padelzone.at",
        "tagline": "El líder indiscutible del pádel austríaco con más de 15 complejos en todo el país.",
        "resumen": "PadelZone es la cadena que ha construido el ecosistema de pádel en Austria. Opera más de 15 clubes cubiertos y descubiertos en Viena (Prater, Erdberg), Graz, Wiener Neustadt, Linz, Klagenfurt y Eisenstadt, siendo el patrocinador principal de los torneos de la federación austríaca.",
        "sedes_principales": [
            "PadelZone Viena Prater (pistas centrales junto al parque del Prater)",
            "PadelZone Viena Erdberg",
            "PadelZone Graz",
            "PadelZone Wiener Neustadt",
            "PadelZone Linz, Klagenfurt y Eisenstadt"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de competición en naves industriales y exteriores",
            "software": "Playtomic integrado con el ranking austríaco",
            "domotica": "Acceso QR y taquillas electrónicas autónomas",
            "grabacion": "Cámaras cenitales en pista central",
            "restauracion": "Clubhouse con cervezas austríacas, café vienés y pro-shop oficial"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena propia y concesiones deportivas municipales",
            "perfil_club": "Naves de 1.500m² a 3.500m² y complejos de tenis reconvertidos",
            "canon_royalties": "Operación directa",
            "inversion_media": "400.000€ a 1.200.000€ por club"
        },
        "diferencial": "Monopolio de facto de las grandes competiciones en Austria y presencia en todas las capitales federales."
    },
    {
        "id": "padeldome-austria",
        "nombre": "Padeldome Austria",
        "pais": "Austria",
        "pais_codigo": "AT",
        "region_filtro": "DE",
        "bandera": "🇦🇹",
        "ciudad_sede": "Viena (Erdberg / Alterlaa)",
        "coords": [
            48.19,
            16.41
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "3 macrocentros cubiertos",
        "num_pistas": "24+ pistas indoor",
        "software": "Playtomic",
        "fundadores": "Padeldome Vienna",
        "web": "https://padeldome.at",
        "tagline": "Macrocomplejos cubiertos bajo cúpulas y naves climatizadas en Viena.",
        "resumen": "Padeldome es el templo del pádel cubierto en Viena. Con complejos de techos altísimos en Erdberg, Alterlaa y Süssenbrunn, garantiza partidos sin viento ni nieve durante los duros inviernos alpinos, con una gran escuela infantil.",
        "sedes_principales": [
            "Padeldome Erdberg (Viena)",
            "Padeldome Alterlaa (Viena)",
            "Padeldome Süssenbrunn"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas cubiertas con aislamiento térmico y césped monofilamento azul",
            "software": "Playtomic",
            "domotica": "Apertura automatizada y climatización de bajo consumo",
            "grabacion": "Vídeo en pista para análisis de técnica",
            "restauracion": "Lounge vienés con snacks y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios",
            "perfil_club": "Naves de más de 3.000m²",
            "canon_royalties": "Operación directa",
            "inversion_media": "900.000€ a 1.800.000€"
        },
        "diferencial": "Altura libre de techo insuperable en Viena y confort térmico invernal absoluto."
    },
    {
        "id": "padel-city-germany",
        "nombre": "Padel City Germany",
        "pais": "Alemania",
        "pais_codigo": "DE",
        "region_filtro": "DE",
        "bandera": "🇩🇪",
        "ciudad_sede": "Múnich / Dortmund / Leipzig",
        "coords": [
            48.1351,
            11.582
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "12 centros en Alemania",
        "num_pistas": "50+ pistas",
        "software": "Playtomic",
        "fundadores": "Padel City Leisure Group",
        "web": "https://padelcity.de",
        "tagline": "La cadena multiclub de mayor expansión en las principales metrópolis alemanas.",
        "resumen": "Padel City es la marca de referencia del pádel en Alemania. Con clubes en Múnich, Dortmund, Leipzig, Augsburgo e Ingolstadt, desarrolla centros cubiertos y mixtos donde se potencia la introducción del público alemán al pádel mediante clinics y torneos después del trabajo.",
        "sedes_principales": [
            "Padel City Múnich (varios centros urbanos)",
            "Padel City Dortmund",
            "Padel City Leipzig",
            "Padel City Augsburg e Ingolstadt"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de calidad de torneo con cristal templado de 12mm",
            "software": "Playtomic",
            "domotica": "Acceso QR autónomo y encendido inteligente",
            "grabacion": "Sistemas para torneos oficiales de la DPV (Deutscher Padel Verband)",
            "restauracion": "Biergarten alemán, cafetería y pro-shop multimarca"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena propia financiada por inversores deportivos alemanes",
            "perfil_club": "Naves y parcelas urbanas en las mayores conurbaciones del país",
            "canon_royalties": "Operación directa",
            "inversion_media": "600.000€ a 1.400.000€ por club"
        },
        "diferencial": "Gran presencia en Baviera y Renania del Norte-Westfalia y metodología de iniciación muy eficiente."
    },
    {
        "id": "padelbox-germany",
        "nombre": "padelBOX",
        "pais": "Alemania",
        "pais_codigo": "DE",
        "region_filtro": "DE",
        "bandera": "🇩🇪",
        "ciudad_sede": "Colonia (Köln) / NRW",
        "coords": [
            50.9375,
            6.9603
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "8 centros en Renania",
        "num_pistas": "38+ pistas",
        "software": "Playtomic",
        "fundadores": "padelBOX GmbH (Patrick Phelan)",
        "web": "https://padelbox.de",
        "tagline": "El pionero del pádel comercial en la cuenca del Rin con 8 centros en Renania del Norte-Westfalia.",
        "resumen": "padelBOX fue uno de los auténticos motores del pádel en Alemania. Concentrado en el área metropolitana de Colonia y alrededores (Köln-Lövenich, Köln-Weiden, Köln-Widdersdorf, Frechen, Bergisch Gladbach, Ahlen y Werne), organiza grandes ligas sociales y eventos corporativos para gigantes industriales alemanes.",
        "sedes_principales": [
            "padelBOX Köln-Weiden (Colonia)",
            "padelBOX Köln-Lövenich",
            "padelBOX Frechen",
            "padelBOX Bergisch Gladbach",
            "padelBOX Ahlen y Werne"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas cubiertas en naves climatizadas",
            "software": "Playtomic",
            "domotica": "Acceso por código QR digital y gestión térmica inteligente",
            "grabacion": "Pantallas en la casa club con repetición de partidos",
            "restauracion": "Lounge con comida sana, cerveza Kölsch y pro-shop especializada"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena corporativa multisede",
            "perfil_club": "Naves de 1.800m² a 3.500m² en la región del Rin-Ruhr",
            "canon_royalties": "Operación directa",
            "inversion_media": "550.000€ a 1.100.000€ por club"
        },
        "diferencial": "Densidad imbatible en el área de Colonia y alianzas con los mayores clubes de tenis locales."
    },
    {
        "id": "we-are-padel-germany",
        "nombre": "We Are Padel Germany",
        "pais": "Alemania",
        "pais_codigo": "DE",
        "region_filtro": "DE",
        "bandera": "🇩🇪",
        "ciudad_sede": "Düsseldorf",
        "coords": [
            51.2277,
            6.7735
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "3 macrocentros",
        "num_pistas": "22+ pistas",
        "software": "Matchi / Playtomic",
        "fundadores": "LeDap Group",
        "web": "https://wearepadel.de",
        "tagline": "El gigante escandinavo LeDap implantando el modelo de macrocomplejos en Alemania.",
        "resumen": "División alemana del conglomerado LeDap. Su centro de Düsseldorf es uno de los mayores de Alemania con 10 pistas cubiertas, uniendo la experiencia de gestión escandinava con el potencial del mercado alemán.",
        "sedes_principales": [
            "We Are Padel Düsseldorf (10 pistas cubiertas de gran altura)",
            "Sedes en desarrollo en Renania"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas de competición con moqueta azul texturizada",
            "software": "Matchi / Playtomic",
            "domotica": "Acceso QR automatizado",
            "grabacion": "Grabación en pista central",
            "restauracion": "Clubhouse nórdico con café y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Macrocentros con respaldo de capital riesgo internacional",
            "perfil_club": "Naves de más de 3.500m²",
            "canon_royalties": "Operación directa corporativa",
            "inversion_media": "1.200.000€ a 2.500.000€"
        },
        "diferencial": "El respaldo financiero del mayor grupo europeo de pádel (LeDap)."
    },
    {
        "id": "walls-padel",
        "nombre": "Walls Padel",
        "pais": "Alemania",
        "pais_codigo": "DE",
        "region_filtro": "DE",
        "bandera": "🇩🇪",
        "ciudad_sede": "Múnich / Baviera",
        "coords": [
            48.14,
            11.57
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "3 centros en Baviera",
        "num_pistas": "15+ pistas",
        "software": "Playtomic",
        "fundadores": "Walls Padel Sports",
        "web": "https://wallspadel.de",
        "tagline": "Pádel cubierto de alto nivel para la comunidad bávara.",
        "resumen": "Cadena especializada en el sur de Alemania con pistas panorámicas cubiertas, entrenadores españoles y torneos de fin de semana muy populares entre la comunidad empresarial de Múnich.",
        "sedes_principales": [
            "Walls Padel Múnich",
            "Walls Padel Baviera Sur"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con climatización",
            "software": "Playtomic",
            "domotica": "Acceso digital automatizado",
            "grabacion": "Streaming de torneos locales",
            "restauracion": "Biergarten y cafetería"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios",
            "perfil_club": "Naves industriales urbanas",
            "canon_royalties": "Operación directa",
            "inversion_media": "600.000€ a 1.200.000€"
        },
        "diferencial": "Ubicación en la región con mayor poder adquisitivo de Alemania."
    },
    {
        "id": "padel-first-swiss",
        "nombre": "Padel First",
        "pais": "Suiza",
        "pais_codigo": "CH",
        "region_filtro": "DE",
        "bandera": "🇨🇭",
        "ciudad_sede": "Ginebra / Lausana",
        "coords": [
            46.2044,
            6.1432
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "3 centros en la Suiza francófona",
        "num_pistas": "14+ pistas",
        "software": "Playtomic",
        "fundadores": "Padel First Suisse",
        "web": "https://padelfirst.ch",
        "tagline": "Pádel suizo de alta gama en los cantones de Ginebra y Vaud.",
        "resumen": "Operador líder en la cuenca del lago Lemán. Gestiona instalaciones en clubes de tenis históricos y naves exclusivas en Ginebra (Vernier) y Lausana, con un perfil de socio corporativo de diplomacia y banca privada.",
        "sedes_principales": [
            "Padel First Vernier (Ginebra)",
            "Padel First Country Club Ginebra",
            "Padel First Lausana"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas de competición con cubiertas y exteriores panorámicas",
            "software": "Playtomic",
            "domotica": "Acceso digital y taquillas seguras",
            "grabacion": "Pistas preparadas para vídeo de entrenamiento",
            "restauracion": "Clubhouse suizo con fondue, vinos locales y terraza"
        },
        "modelo_expansion": {
            "tipo_contrato": "Concesiones en clubes de tenis tradicionales",
            "perfil_club": "Suelos premium en Ginebra y Lausana",
            "canon_royalties": "Operación directa",
            "inversion_media": "500.000€ a 1.000.000€"
        },
        "diferencial": "La tarifa por hora de pista más alta de Europa (40€ a 70€ por hora) con ocupación casi total."
    },
    {
        "id": "padel-basel",
        "nombre": "Padel Basel",
        "pais": "Suiza",
        "pais_codigo": "CH",
        "region_filtro": "DE",
        "bandera": "🇨🇭",
        "ciudad_sede": "Basilea",
        "coords": [
            47.5596,
            7.5886
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 centros en Basilea",
        "num_pistas": "10+ pistas",
        "software": "Playtomic",
        "fundadores": "Padel Basel Group",
        "web": "https://padelbasel.ch",
        "tagline": "El referente de la raqueta en la frontera tripartita de Suiza, Alemania y Francia.",
        "resumen": "Situado en el polo farmacéutico mundial de Basilea (Klybeck y Dreispitz), Padel Basel es un club cubierto de diseño que atrae a ejecutivos de Novartis, Roche y deportistas del cantón.",
        "sedes_principales": [
            "Padel Basel Klybeck (naves industriales creativas)",
            "Padel Basel Dreispitz"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas en naves diáfanas climatizadas",
            "software": "Playtomic",
            "domotica": "Acceso QR y gestión autónoma",
            "grabacion": "Vídeo en torneos cantonales",
            "restauracion": "Lounge con cervezas artesanas y comida fresca"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios",
            "perfil_club": "Zonas industriales urbanas de Basilea",
            "canon_royalties": "Operación propia",
            "inversion_media": "600.000€ a 1.200.000€"
        },
        "diferencial": "Público multinacional de la industria farmacéutica y ubicación trifronteriza."
    },
    {
        "id": "unterland-padel",
        "nombre": "Unterland Padel",
        "pais": "Suiza",
        "pais_codigo": "CH",
        "region_filtro": "DE",
        "bandera": "🇨🇭",
        "ciudad_sede": "Zúrich (Bülach)",
        "coords": [
            47.5186,
            8.5408
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 centros en el área de Zúrich",
        "num_pistas": "8+ pistas",
        "software": "Playtomic",
        "fundadores": "Unterland Sports",
        "web": "https://unterlandpadel.ch",
        "tagline": "Pistas cubiertas climatizadas en el cinturón financiero de Zúrich.",
        "resumen": "Ubicado junto al aeropuerto de Zúrich en Bülach, ofrece pistas cubiertas de gran altura para el área metropolitana de Zúrich, con reservas digitales y torneos continuos para el sector bancario.",
        "sedes_principales": [
            "Unterland Padel Bülach (Zúrich Norte)",
            "Instalaciones satélites asociadas"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas de competición panorámicas",
            "software": "Playtomic",
            "domotica": "Acceso autónomo 100%",
            "grabacion": "Grabación de partidos",
            "restauracion": "Bar café y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios",
            "perfil_club": "Naves de 1.500m² en Zúrich",
            "canon_royalties": "Operación directa",
            "inversion_media": "700.000€ a 1.300.000€"
        },
        "diferencial": "Servicio prémium al cliente de Zúrich con la máxima eficiencia suiza."
    },
    {
        "id": "interpadel-norway",
        "nombre": "InterPadel Norway",
        "pais": "Noruega",
        "pais_codigo": "NO",
        "region_filtro": "SE",
        "bandera": "🇳🇴",
        "ciudad_sede": "Oslo / Bergen / Stavanger",
        "coords": [
            59.9139,
            10.7522
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "10+ centros en Noruega",
        "num_pistas": "75+ pistas cubiertas",
        "software": "Matchi / Playtomic",
        "fundadores": "Jan Frode Andersen (ex-tenista Copa Davis)",
        "web": "https://interpadel.no",
        "tagline": "La cadena número uno de Noruega, creada por el tenista Jan Frode Andersen.",
        "resumen": "InterPadel es la mayor red multiclub de Noruega bajo una sola marca. Fundada por la leyenda del tenis noruego Jan Frode Andersen, opera macrocentros cubiertos con pistas panorámicas de última generación en Oslo (Letohallen), Bergen (Os), Stavanger (Forus y Sandnes), Arendal y Sarpsborg, con academias juveniles y eventos corporativos masivos del sector energético.",
        "sedes_principales": [
            "InterPadel Letohallen (Oslo Norte - 10 pistas cubiertas)",
            "InterPadel Os (Bergen - gran centro cubierto)",
            "InterPadel Forus (Stavanger - epicentro industrial)",
            "InterPadel Sandnes (Rogaland)",
            "InterPadel Arendal y Sarpsborg"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de 10 metros de altura libre, moqueta texturizada azul WPT",
            "software": "Matchi y Playtomic",
            "domotica": "Acceso 100% automatizado 24/7 con código digital en el móvil",
            "grabacion": "Cámaras cenitales en todas las pistas para visualización instantánea",
            "restauracion": "Clubhouse nórdico de diseño, café de barista, batidos y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena propia financiada por inversores deportivos noruegos",
            "perfil_club": "Naves de 3.000m² a 6.000m² en las principales ciudades noruegas",
            "canon_royalties": "Operación directa corporativa",
            "inversion_media": "1.200.000€ a 2.500.000€ por club"
        },
        "diferencial": "El prestigio deportivo de Jan Frode Andersen y acuerdos corporativos con las mayores petroleras y multinacionales de Noruega."
    },
    {
        "id": "just-padel-norway",
        "nombre": "Just Padel Norway",
        "pais": "Noruega",
        "pais_codigo": "NO",
        "region_filtro": "SE",
        "bandera": "🇳🇴",
        "ciudad_sede": "Kristiansand / Drammen",
        "coords": [
            58.1599,
            8.0182
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "15+ centros",
        "num_pistas": "70+ pistas cubiertas",
        "software": "Matchi",
        "fundadores": "Jesús Gil Marín & socios inversores noruegos",
        "web": "https://justpadel.no",
        "tagline": "Una de las redes de pádel indoor más extendidas por todo el sur y este de Noruega.",
        "resumen": "Cadena pionera que desplegó el pádel en el sur de Noruega con enorme velocidad. Cuenta con más de 15 centros cubiertos en Kristiansand, Larvik, Skien, Porsgrunn, Lier, Drammen y comarcas adyacentes, con centros 100% automatizados para jugar en pleno invierno nórdico.",
        "sedes_principales": [
            "Just Padel Kristiansand (centro insignia del sur)",
            "Just Padel Drammen",
            "Just Padel Larvik",
            "Just Padel Skien y Porsgrunn",
            "Just Padel Lier"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas cubiertas con iluminación LED de alta potencia",
            "software": "Matchi",
            "domotica": "Acceso autónomo con código en app, iluminación programada y climatización",
            "grabacion": "Sistemas para revisión de partidos en torneos",
            "restauracion": "Zona lounge de autoservicio y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena corporativa",
            "perfil_club": "Naves de 2.000 a 4.000 m²",
            "canon_royalties": "Operación directa",
            "inversion_media": "700.000€ a 1.500.000€ por centro"
        },
        "diferencial": "Capilaridad territorial en ciudades medianas noruegas donde no existía oferta cubierta."
    },
    {
        "id": "nordic-padel",
        "nombre": "Nordic Padel",
        "pais": "Noruega",
        "pais_codigo": "NO",
        "region_filtro": "SE",
        "bandera": "🇳🇴",
        "ciudad_sede": "Oslo (Røyken)",
        "coords": [
            59.74,
            10.42
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 macrocentros",
        "num_pistas": "16+ pistas",
        "software": "Matchi",
        "fundadores": "Nordic Padel AS",
        "web": "https://nordicpadel.no",
        "tagline": "Instalaciones cubiertas de vanguardia en el área metropolitana de Oslo.",
        "resumen": "Cadena premium noruega con grandes naves industriales reconvertidas para ofrecer la máxima altura libre de juego y moqueta de competición Premier Padel.",
        "sedes_principales": [
            "Nordic Padel Røyken (Oslo Sur)",
            "Centro satélite en Viken"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de 11 metros de altura libre",
            "software": "Matchi",
            "domotica": "Acceso QR y taquillas electrónicas",
            "grabacion": "Grabación de torneos",
            "restauracion": "Lounge café nórdico y tienda especializada"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios",
            "perfil_club": "Naves de más de 3.000m²",
            "canon_royalties": "Operación directa",
            "inversion_media": "900.000€ a 1.600.000€"
        },
        "diferencial": "Ambiente de club social cuidado y torneos Americano semanales muy concurridos."
    },
    {
        "id": "padelpadel-denmark",
        "nombre": "PadelPadel Denmark",
        "pais": "Dinamarca",
        "pais_codigo": "DK",
        "region_filtro": "SE",
        "bandera": "🇩🇰",
        "ciudad_sede": "Odense / Aarhus / Aalborg",
        "coords": [
            55.4038,
            10.4024
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "4 macrocentros",
        "num_pistas": "50+ pistas cubiertas",
        "software": "Matchi",
        "fundadores": "PadelPadel Group Denmark",
        "web": "https://padelpadel.dk",
        "tagline": "El coloso danés: megacentros de hasta 16 pistas indoor bajo una sola nave.",
        "resumen": "PadelPadel es el gigante del pádel de gran formato en Dinamarca. Sus complejos en Odense (16 pistas cubiertas), Aarhus (14 pistas) y Aalborg (10 pistas) son monumentales, con casa club escandinava, pistas centrales con gradas y la mayor escuela de Dinamarca.",
        "sedes_principales": [
            "PadelPadel Odense (16 pistas cubiertas - macrocentro nacional)",
            "PadelPadel Aarhus (14 pistas cubiertas)",
            "PadelPadel Aalborg (10 pistas cubiertas)",
            "PadelPadel Copenhague"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de competición con techos de más de 10 metros y suelo aislado",
            "software": "Matchi",
            "domotica": "Acceso autónomo con código en el móvil 24 horas al día",
            "grabacion": "Cámaras con IA para repetición instantánea en pantallas de la cafetería",
            "restauracion": "Lounge escandinavo con cerveza danesa de tirador, café orgánico y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena propia de megacentros industriales",
            "perfil_club": "Naves de 4.000m² a 7.000m²",
            "canon_royalties": "Operación directa",
            "inversion_media": "1.500.000€ a 3.000.000€ por megacentro"
        },
        "diferencial": "La escala: megacentros masivos donde siempre hay pista libre y torneos federados semanales."
    },
    {
        "id": "match-padel-denmark",
        "nombre": "Match Padel Denmark",
        "pais": "Dinamarca",
        "pais_codigo": "DK",
        "region_filtro": "SE",
        "bandera": "🇩🇰",
        "ciudad_sede": "Copenhague / Aarhus / Odense",
        "coords": [
            55.6761,
            12.5683
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "10+ centros en Dinamarca",
        "num_pistas": "60+ pistas cubiertas",
        "software": "Matchi",
        "fundadores": "Match Padel A/S",
        "web": "https://matchpadel.dk",
        "tagline": "La red con mayor implantación en Dinamarca: Copenhague, Aarhus, Silkeborg y Bornholm.",
        "resumen": "Match Padel es una de las marcas más reconocidas por los jugadores daneses. Cuenta con centros en Kløvermarken (Copenhague), Ballerup, Aarhus Risskov, Aalborg, Odense, Silkeborg, Næstved, Hobro y hasta la isla de Bornholm.",
        "sedes_principales": [
            "Match Padel Kløvermarken (Copenhague)",
            "Match Padel Ballerup",
            "Match Padel Aarhus Risskov",
            "Match Padel Silkeborg (Silkeborg C y Silkeborg Syd)",
            "Match Padel Bornholm (Rønne y Svaneke)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas cubiertas con moqueta azul y climatización",
            "software": "Matchi",
            "domotica": "Acceso QR, control de luces automático y climatización programada",
            "grabacion": "Sistemas para retransmisión de torneos locales",
            "restauracion": "Lounge bar con autoservicio y pro-shop con palas de test"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena corporativa con expansión en toda Dinamarca",
            "perfil_club": "Naves de 2.000 a 4.000 m²",
            "canon_royalties": "Operación directa",
            "inversion_media": "600.000€ a 1.400.000€ por centro"
        },
        "diferencial": "Cobertura geográfica inigualable en Dinamarca, desde la capital hasta islas como Bornholm."
    },
    {
        "id": "racket-club-denmark",
        "nombre": "Racket Club Denmark",
        "pais": "Dinamarca",
        "pais_codigo": "DK",
        "region_filtro": "SE",
        "bandera": "🇩🇰",
        "ciudad_sede": "Copenhague (Kløvermarken / Taastrup)",
        "coords": [
            55.67,
            12.6
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "3 macrocentros en Copenhague",
        "num_pistas": "30+ pistas cubiertas",
        "software": "Matchi",
        "fundadores": "Racket Club Copenhagen",
        "web": "https://racketclub.dk",
        "tagline": "El club urbano de diseño más exclusivo de Copenhague.",
        "resumen": "Referente del pádel en la capital danesa. Sus naves en Kløvermarken, Taastrup y Terminalen destacan por una arquitectura interior cuidada con madera nórdica, lounges con sofás de diseño y pistas de máxima especificación.",
        "sedes_principales": [
            "Racket Club Kløvermarken (Copenhague)",
            "Racket Club Taastrup",
            "Racket Club Terminalen"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas super-panorámicas con iluminación LED difusa de alta fidelidad",
            "software": "Matchi",
            "domotica": "Acceso y reserva autónoma",
            "grabacion": "Pantallas en el bar con repetición de puntos",
            "restauracion": "Bar café de diseño nórdico con brunch y pro-shop boutique"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios en el área de Copenhague",
            "perfil_club": "Naves urbanas con excelente interiorismo",
            "canon_royalties": "Operación directa",
            "inversion_media": "1.000.000€ a 2.000.000€"
        },
        "diferencial": "Estética escandinava impecable y el punto de encuentro de los jóvenes profesionales de Copenhague."
    },
    {
        "id": "padel-lounge-denmark",
        "nombre": "Padel Lounge Denmark",
        "pais": "Dinamarca",
        "pais_codigo": "DK",
        "region_filtro": "SE",
        "bandera": "🇩🇰",
        "ciudad_sede": "Aalborg / Esbjerg / Herning",
        "coords": [
            57.0488,
            9.9217
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "4 centros en Jutlandia",
        "num_pistas": "24+ pistas cubiertas",
        "software": "Matchi",
        "fundadores": "Padel Lounge ApS",
        "web": "https://padellounge.dk",
        "tagline": "El confort del pádel indoor en la península de Jutlandia.",
        "resumen": "Cadena especializada en naves cubiertas acogedoras en Jutlandia (Aalborg, Esbjerg, Herning y Holstebro), con ambiente relajado y ligas de fin de semana.",
        "sedes_principales": [
            "Padel Lounge Aalborg",
            "Padel Lounge Esbjerg",
            "Padel Lounge Herning",
            "Padel Lounge Holstebro"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas cubiertas panorámicas",
            "software": "Matchi",
            "domotica": "Acceso QR automatizado",
            "grabacion": "Vídeo en torneos",
            "restauracion": "Lounge con autoservicio y café"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios",
            "perfil_club": "Naves de 2.000m²",
            "canon_royalties": "Operación directa",
            "inversion_media": "500.000€ a 1.000.000€"
        },
        "diferencial": "Presencia consolidada en las principales ciudades de Jutlandia."
    },
    {
        "id": "ledap-we-are-padel",
        "nombre": "LeDap / We Are Padel (WAP)",
        "pais": "Suecia",
        "pais_codigo": "SE",
        "region_filtro": "SE",
        "bandera": "🇸🇪",
        "ciudad_sede": "Estocolmo",
        "coords": [
            59.3293,
            18.0686
        ],
        "modelo": "Red Corporativa Propia",
        "modelo_badge": "bg-blue-100 text-blue-800 border-blue-200",
        "tipo_categoria": "red_propia",
        "escala": "macro",
        "num_clubs": "90+ centros en Europa",
        "num_pistas": "650+ pistas",
        "software": "Matchi / Playtomic",
        "fundadores": "Triton Private Equity Partners (Pontus Gustafsson)",
        "web": "https://ledap.com",
        "tagline": "El mayor conglomerado mundial de clubes de pádel, nacido de la consolidación sueca.",
        "resumen": "LeDap es el gigante paneuropeo creado por el fondo Triton. Agrupa más de 90 centros y 650 pistas bajo marcas como We Are Padel (WAP) en Suecia, Finlandia, Alemania, Polonia, Emiratos Árabes y Reino Unido, liderando la profesionalización y el software del sector.",
        "sedes_principales": [
            "WAP Stockholm (múltiples centros cubiertos)",
            "WAP Göteborg",
            "WAP Malmö",
            "Centros en Alemania, Finlandia y Austria"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de alta especificación y techos de hasta 12 metros",
            "software": "Matchi / Playtomic y plataforma interna LeDap",
            "domotica": "Acceso 100% digitalizado 24/7 sin recepcionista",
            "grabacion": "Sistemas de vídeo cenitales integrados",
            "restauracion": "Pro-shops de última generación, zonas lounge y bar"
        },
        "modelo_expansion": {
            "tipo_contrato": "Consolidación y adquisiciones de clubes independientes a escala europea",
            "perfil_club": "Macrocomplejos de más de 8 pistas cubiertas",
            "canon_royalties": "Operación directa",
            "inversion_media": "Más de 100 millones de euros invertidos por el fondo Triton"
        },
        "diferencial": "El mayor músculo financiero del mundo del pádel y la mayor base de pistas en propiedad."
    },
    {
        "id": "pdl-padel-united",
        "nombre": "PDL Center / Padel United",
        "pais": "Suecia",
        "pais_codigo": "SE",
        "region_filtro": "SE",
        "bandera": "🇸🇪",
        "ciudad_sede": "Estocolmo",
        "coords": [
            59.335,
            18.05
        ],
        "modelo": "Red Corporativa Propia",
        "modelo_badge": "bg-blue-100 text-blue-800 border-blue-200",
        "tipo_categoria": "red_propia",
        "escala": "macro",
        "num_clubs": "75+ centros",
        "num_pistas": "500+ pistas",
        "software": "Matchi",
        "fundadores": "Jonas Björkman, Måns Zelmerlöw y Markus Hellkvist",
        "web": "https://padelunited.se",
        "tagline": "El gigante resultante de la fusión de los dos pioneros de la revolución sueca.",
        "resumen": "Nacido de la unión histórica entre PDL Center (fundado por el ex número 1 de dobles de tenis Jonas Björkman y el cantante Måns Zelmerlöw) y Padel United. Cuentan con más de 500 pistas en Suecia, Noruega y Reino Unido.",
        "sedes_principales": [
            "PDL Center Frihamnen (Estocolmo - megacentro cubierto)",
            "PDL Center Kvarnholmen",
            "Padel United Göteborg",
            "Sedes en Malmö, Uppsala y Reino Unido"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con césped texturizado y gradas para torneos",
            "software": "Matchi",
            "domotica": "Acceso por código en app 24 horas al día",
            "grabacion": "Cámaras para ligas suecas",
            "restauracion": "Clubhouse nórdico, pro-shop y cafetería"
        },
        "modelo_expansion": {
            "tipo_contrato": "Red propia consolidada",
            "perfil_club": "Naves de 3.000m² a 8.000m²",
            "canon_royalties": "Operación directa",
            "inversion_media": "1.500.000€ a 3.500.000€ por club"
        },
        "diferencial": "Los pioneros que iniciaron el boom del pádel en los países nórdicos."
    },
    {
        "id": "every-padel",
        "nombre": "Every Padel",
        "pais": "Suecia",
        "pais_codigo": "SE",
        "region_filtro": "SE",
        "bandera": "🇸🇪",
        "ciudad_sede": "Gotemburgo / Estocolmo",
        "coords": [
            57.7089,
            11.9746
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "5 macrocentros",
        "num_pistas": "70+ pistas cubiertas",
        "software": "Matchi",
        "fundadores": "Every Padel Group",
        "web": "https://everypadel.com",
        "tagline": "El creador del monumental Every Padel Åby Arena en Gotemburgo: 25 pistas cubiertas.",
        "resumen": "Cadena célebre por haber construido en el Åby Arena de Gotemburgo uno de los complejos de pádel cubierto más grandes del mundo con 25 pistas bajo un mismo techo, complementado con sedes en Kista Galleria (Estocolmo) y Jönköping.",
        "sedes_principales": [
            "Every Padel Åby Arena (Gotemburgo - 25 pistas cubiertas)",
            "Every Padel Kista Galleria (Estocolmo)",
            "Every Padel Jönköping"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de competición en recintos feriales con más de 12 metros de altura",
            "software": "Matchi",
            "domotica": "Control digital de iluminación y accesos",
            "grabacion": "Streaming oficial de torneos de la SPT (Swedish Padel Tour)",
            "restauracion": "Restaurantes integrados en el recinto ferial Åby, hotel y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Macrocomplejos en recintos feriales y centros comerciales",
            "perfil_club": "Pabellones de más de 8.000 m²",
            "canon_royalties": "Operación directa",
            "inversion_media": "Más de 4.000.000€"
        },
        "diferencial": "La inmensidad del Åby Arena (25 pistas indoor), sede de los mayores eventos de Europa."
    },
    {
        "id": "padel-zenter",
        "nombre": "Padel Zenter",
        "pais": "Suecia",
        "pais_codigo": "SE",
        "region_filtro": "SE",
        "bandera": "🇸🇪",
        "ciudad_sede": "Estocolmo / Milán",
        "coords": [
            59.29,
            18.03
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "6 macrocentros",
        "num_pistas": "55+ pistas cubiertas",
        "software": "Matchi",
        "fundadores": "Zlatan Ibrahimović y Thomas Sandström",
        "web": "https://padelzenter.se",
        "tagline": "La cadena de centros de máxima altura libre creada por la leyenda Zlatan Ibrahimović.",
        "resumen": "Cadena icónica fundada por el futbolista Zlatan Ibrahimović. Con el lema de no escatimar en altura ni calidad, sus naves en Årsta (Estocolmo), Jönköping, Skövde, Örebro, Uppsala y su salto a Milán (Segrate) cuentan con techos de 12 metros libres y pistas oficiales World Padel Tour.",
        "sedes_principales": [
            "Padel Zenter Årsta (Estocolmo - 9 pistas cubiertas de 12m de altura)",
            "Padel Zenter Segrate (Milán, Italia)",
            "Padel Zenter Jönköping",
            "Padel Zenter Skövde, Örebro y Uppsala"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas homologadas con techos de 12 metros sin columnas ni cables",
            "software": "Matchi",
            "domotica": "Acceso por código digital y clima industrial de máxima eficiencia",
            "grabacion": "Cámaras con IA para análisis de juego",
            "restauracion": "Lounge con diseño negro mate Zlatan, pro-shop y zona de preparación física"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios construidos desde cero o naves de arquitectura a medida",
            "perfil_club": "Naves de más de 4.000m² con altura vertical récord",
            "canon_royalties": "Operación directa del grupo de Zlatan",
            "inversion_media": "2.000.000€ a 4.500.000€ por club"
        },
        "diferencial": "La marca Zlatan Ibrahimović y la obsesión por la altura de techo perfecta para el juego de globos."
    },
    {
        "id": "padel-club-finland",
        "nombre": "Padel Club Finland",
        "pais": "Finlandia",
        "pais_codigo": "FI",
        "region_filtro": "SE",
        "bandera": "🇫🇮",
        "ciudad_sede": "Espoo / Vantaa / Tampere",
        "coords": [
            60.2055,
            24.6559
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "8 centros en Finlandia",
        "num_pistas": "45+ pistas cubiertas",
        "software": "Playtomic / Padelution",
        "fundadores": "Padel Club Finland Oy",
        "web": "https://padelclub.fi",
        "tagline": "La red pionera que llevó el pádel indoor a cada rincón de Finlandia.",
        "resumen": "Cadena pionera del pádel finés con instalaciones cubiertas y climatizadas en Espoo (Suomenoja), Vantaa, Alajärvi y Tampere, con sauna tradicional finlandesa en cada vestuario y ligas activas durante los meses polares.",
        "sedes_principales": [
            "Padel Club Finland Espoo Suomenoja",
            "Padel Club Finland Vantaa",
            "Padel Club Finland Tampere",
            "Padel Club Finland Alajärvi"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas cubiertas con aislamiento térmico contra temperaturas de -20ºC",
            "software": "Playtomic y Padelution",
            "domotica": "Acceso QR automatizado 24/7",
            "grabacion": "Grabación de partidos de torneos de la Federación Finlandesa",
            "restauracion": "Sauna finlandesa en vestuarios, cafetería y tienda técnica"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios",
            "perfil_club": "Naves de 2.000 a 4.000 m² con aislamiento térmico reforzado",
            "canon_royalties": "Operación directa",
            "inversion_media": "800.000€ a 1.600.000€"
        },
        "diferencial": "Instalaciones diseñadas a prueba del invierno nórdico con saunas finlandesas auténticas."
    },
    {
        "id": "billebeino-padel",
        "nombre": "Billebeino Padel",
        "pais": "Finlandia",
        "pais_codigo": "FI",
        "region_filtro": "SE",
        "bandera": "🇫🇮",
        "ciudad_sede": "Helsinki (Vallila) / Vantaa",
        "coords": [
            60.19,
            24.96
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "3 centros urbanos",
        "num_pistas": "16+ pistas",
        "software": "Playtomic",
        "fundadores": "Ville Leino (ex-estrella NHL de hockey sobre hielo)",
        "web": "https://billebeinopadel.com",
        "tagline": "Pádel urbano y ropa de moda callejera creado por la estrella de la NHL Ville Leino.",
        "resumen": "Cadena de clubes nacida de la famosa marca de ropa streetwear finlandesa Billebeino, fundada por el ex-jugador de la NHL Ville Leino. Sus centros en Helsinki Vallila y Vantaa combinan pistas cubiertas de diseño con tiendas de moda y eventos de música.",
        "sedes_principales": [
            "Billebeino Padel Vallila (Helsinki)",
            "Billebeino Padel Vantaa"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con estética monocromática urbana de diseño",
            "software": "Playtomic",
            "domotica": "Acceso inteligente automatizado",
            "grabacion": "Sistemas para contenidos de redes sociales",
            "restauracion": "Café de diseño, cerveza artesanal y tienda monomarca Billebeino"
        },
        "modelo_expansion": {
            "tipo_contrato": "Clubes propios urbanos",
            "perfil_club": "Naves industriales creativas en Helsinki",
            "canon_royalties": "Operación directa",
            "inversion_media": "700.000€ a 1.300.000€"
        },
        "diferencial": "La fusión única entre la cultura del hockey NHL, la moda urbana finlandesa y el pádel."
    },
    {
        "id": "open-padel-finland",
        "nombre": "Open Padel",
        "pais": "Finlandia",
        "pais_codigo": "FI",
        "region_filtro": "SE",
        "bandera": "🇫🇮",
        "ciudad_sede": "Helsinki / Espoo / Kauniainen",
        "coords": [
            60.17,
            24.94
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "3 centros metropolitanos",
        "num_pistas": "18+ pistas",
        "software": "Playtomic",
        "fundadores": "Open Padel Oy",
        "web": "https://openpadel.fi",
        "tagline": "Clubes cubiertos accesibles en la conurbación de la capital finlandesa.",
        "resumen": "Cadena enfocada en hacer el pádel fácil y accesible en la capital finlandesa mediante reservas por Playtomic, escuelas para principiantes y pistas cubiertas de gran altura.",
        "sedes_principales": [
            "Open Padel Helsinki",
            "Open Padel Espoo",
            "Open Padel Kauniainen"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas cubiertas",
            "software": "Playtomic",
            "domotica": "Acceso autónomo con código digital",
            "grabacion": "Vídeo en torneos",
            "restauracion": "Lounge con café y autoservicio"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios",
            "perfil_club": "Naves industriales de 2.000m²",
            "canon_royalties": "Operación directa",
            "inversion_media": "650.000€ a 1.200.000€"
        },
        "diferencial": "Excelente relación calidad-precio y gran facilidad de reserva en el área metropolitana de Helsinki."
    },
    {
        "id": "rackets-pro",
        "nombre": "Rackets Pro",
        "pais": "Portugal",
        "pais_codigo": "PT",
        "region_filtro": "PT",
        "bandera": "🇵🇹",
        "ciudad_sede": "Lisboa (EUL)",
        "coords": [
            38.755,
            -9.158
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "5 centros de prestigio",
        "num_pistas": "45+ pistas",
        "software": "AirCourts / Playtomic",
        "fundadores": "Rackets Pro Management (Paulo Martins)",
        "web": "https://racketspro.pt",
        "tagline": "La cadena número uno de Portugal: 12 pistas en el Estádio Universitário de Lisboa.",
        "resumen": "Rackets Pro es la marca de referencia indiscutible de Portugal. Opera grandes clubes en Lisboa y Cascais: el emblemático Rackets Pro EUL (Estádio Universitário de Lisboa con 12 pistas), Nacional Padel, Quinta da Marinha (Cascais) y Nova Sports.",
        "sedes_principales": [
            "Rackets Pro EUL (Estádio Universitário de Lisboa - 12 pistas)",
            "Rackets Pro Quinta da Marinha (Cascais)",
            "Rackets Pro Nacional Padel",
            "Rackets Pro Nova Sports Club",
            "Rackets Pro Alvito"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de competición cubiertas y outdoor con césped Mondo Supercourt",
            "software": "AirCourts (la plataforma líder en Portugal) y Playtomic",
            "domotica": "Acceso inteligente automatizado",
            "grabacion": "Pistas con cámaras de streaming para el circuito de la Federação Portuguesa de Padel",
            "restauracion": "Restaurante terraza con comida saludable portuguesa y pro-shop completa"
        },
        "modelo_expansion": {
            "tipo_contrato": "Concesiones deportivas de alto nivel y clubes propios",
            "perfil_club": "Suelos universitarios y country clubs de lujo en Lisboa y Cascais",
            "canon_royalties": "Operación directa",
            "inversion_media": "800.000€ a 2.000.000€ por club"
        },
        "diferencial": "Sedes en los lugares más prestigiosos de Lisboa y ser la academia de los mejores jugadores de la selección lusa."
    },
    {
        "id": "top-padel-az",
        "nombre": "Top-Padel / AZ Padel",
        "pais": "Portugal",
        "pais_codigo": "PT",
        "region_filtro": "PT",
        "bandera": "🇵🇹",
        "ciudad_sede": "Oporto (Industrial / Fluvial)",
        "coords": [
            41.1579,
            -8.6291
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "macro",
        "num_clubs": "5 clubes con el mismo nombre",
        "num_pistas": "40+ pistas",
        "software": "AirCourts / Playtomic",
        "fundadores": "Top-Padel Group Porto",
        "web": "https://top-padel.pt",
        "tagline": "El gigante del norte de Portugal: pistas míticas a orillas del río Duero en Oporto.",
        "resumen": "Top-Padel es la cadena que domina el norte portugués. Sus clubes en Oporto son míticos: Top-Padel Fluvial (situado junto al río Duero en la Foz do Douro), Top-Padel Industrial (9 pistas cubiertas de gran altura), Top-Padel Maia, Gaia y Vila Nova de Famalicão.",
        "sedes_principales": [
            "Top-Padel Fluvial (Oporto Foz - pistas junto al río Duero)",
            "Top-Padel Industrial (Oporto - 9 pistas cubiertas)",
            "Top-Padel Maia",
            "Top-Padel Vila Nova de Gaia",
            "Top-Padel Famalicão"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas cubiertas y descubiertas con vistas panorámicas al río",
            "software": "AirCourts y Playtomic",
            "domotica": "Acceso QR automatizado",
            "grabacion": "Sistemas para streaming de torneos nacionales de la FPP",
            "restauracion": "Terrazas chill-out con vistas fluviales, vinos de Oporto y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena de clubes propios",
            "perfil_club": "Naves industriales y suelos ribereños en el Gran Oporto",
            "canon_royalties": "Operación directa",
            "inversion_media": "600.000€ a 1.500.000€ por club"
        },
        "diferencial": "La belleza paisajística de la sede Fluvial en Oporto y su dominio absoluto en el norte luso."
    },
    {
        "id": "padel-campo-grande",
        "nombre": "Padel Campo Grande",
        "pais": "Portugal",
        "pais_codigo": "PT",
        "region_filtro": "PT",
        "bandera": "🇵🇹",
        "ciudad_sede": "Lisboa (Jardim do Campo Grande)",
        "coords": [
            38.7555,
            -9.155
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 centros emblemáticos",
        "num_pistas": "15+ pistas",
        "software": "AirCourts",
        "fundadores": "Clube de Padel Lisboa",
        "web": "https://padelcampogrande.com",
        "tagline": "El corazón verde del pádel en el jardín central más grande de Lisboa.",
        "resumen": "Ubicado en el Jardim do Campo Grande de Lisboa, es uno de los clubes urbanos más animados de Portugal con 10 pistas al aire libre y cubiertas rodeadas de árboles centenarios y una enorme vida social estudiantil y corporativa.",
        "sedes_principales": [
            "Padel Campo Grande (Lisboa Centro - 10 pistas)",
            "Centro satélite en el área metropolitana"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de cristal con cubiertas y césped azul",
            "software": "AirCourts",
            "domotica": "Acceso digital y reserva autónoma",
            "grabacion": "Cámaras en torneos locales",
            "restauracion": "Terraza quiosco en el parque con café portugués, pasteles de nata y cerveza"
        },
        "modelo_expansion": {
            "tipo_contrato": "Concesión de parque municipal urbano",
            "perfil_club": "Parques y jardines históricos",
            "canon_royalties": "Operación directa",
            "inversion_media": "500.000€ a 1.000.000€"
        },
        "diferencial": "Jugar en medio del parque más transitado de Lisboa con acceso directo en metro."
    },
    {
        "id": "padel-inn-portugal",
        "nombre": "Padel Inn Portugal",
        "pais": "Portugal",
        "pais_codigo": "PT",
        "region_filtro": "PT",
        "bandera": "🇵🇹",
        "ciudad_sede": "Braga / Guimarães",
        "coords": [
            41.5454,
            -8.4265
        ],
        "modelo": "Cadena Multiclub (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "2 clubes en el Miño",
        "num_pistas": "12+ pistas cubiertas",
        "software": "AirCourts",
        "fundadores": "Padel Inn Sports",
        "web": "https://padelinn.pt",
        "tagline": "Pistas cubiertas de alta calidad en la pujante región del Miño.",
        "resumen": "Cadena de naves cubiertas en las ciudades históricas de Braga y Guimarães con pistas panorámicas y escuelas de competición que nutren los torneos del norte de Portugal.",
        "sedes_principales": [
            "Padel Inn Braga (6 pistas cubiertas)",
            "Padel Inn Guimarães"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de cristal en naves climatizadas",
            "software": "AirCourts",
            "domotica": "Acceso QR y taquillas electrónicas",
            "grabacion": "Vídeo en torneos regionales",
            "restauracion": "Bar lounge con aperitivos y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Centros propios",
            "perfil_club": "Naves de 1.800m² a 2.500m²",
            "canon_royalties": "Operación directa",
            "inversion_media": "450.000€ a 850.000€"
        },
        "diferencial": "Presencia destacada en el motor industrial del norte de Portugal (Braga y Guimarães)."
    },
    {
        "id": "padel-haus",
        "nombre": "Padel Haus",
        "pais": "Estados Unidos",
        "pais_codigo": "US",
        "region_filtro": "US",
        "bandera": "🇺🇸",
        "ciudad_sede": "Nueva York / Nashville",
        "coords": [
            40.7144,
            -73.96
        ],
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
        "coords": [
            25.7617,
            -80.1918
        ],
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
        "coords": [
            25.82,
            -80.19
        ],
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
        "coords": [
            32.7157,
            -117.1611
        ],
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
        "coords": [
            37.7749,
            -122.4194
        ],
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
        "coords": [
            25.8,
            -80.198
        ],
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
        "coords": [
            30.2672,
            -97.7431
        ],
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
        "coords": [
            26.3683,
            -80.1289
        ],
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
        "coords": [
            25.81,
            -80.35
        ],
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
    },
    {
        "id": "padel-co",
        "nombre": "Padel Co México",
        "pais": "México",
        "pais_codigo": "MX",
        "region_filtro": "MX",
        "bandera": "🇲🇽",
        "ciudad_sede": "Ciudad de México (Polanco / Reforma)",
        "coords": [
            19.4326,
            -99.1332
        ],
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
        "coords": [
            19.3,
            -99.2
        ],
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
        "coords": [
            19.36,
            -99.26
        ],
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
        "coords": [
            25.6667,
            -100.35
        ],
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
        "coords": [
            -33.37,
            -70.67
        ],
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
        "coords": [
            -33.36,
            -70.52
        ],
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
        "coords": [
            -33.45,
            -70.66
        ],
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
        "coords": [
            -33.42,
            -70.6
        ],
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
        "coords": [
            -34.628,
            -58.455
        ],
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
        "coords": [
            -34.46,
            -58.91
        ],
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
        "coords": [
            -26.98,
            -48.63
        ],
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
        "coords": [
            -30.0346,
            -51.2177
        ],
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
    },
    {
        "id": "padel-in",
        "nombre": "Padel IN",
        "pais": "Catar",
        "pais_codigo": "QA",
        "region_filtro": "AE",
        "bandera": "🇶🇦",
        "ciudad_sede": "Doha / Kuwait / Riad",
        "coords": [
            25.2854,
            51.531
        ],
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
        "coords": [
            25.13,
            55.23
        ],
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
        "coords": [
            25.22,
            55.28
        ],
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
        "coords": [
            25.26,
            55.27
        ],
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
        "coords": [
            25.07,
            55.14
        ],
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
        "coords": [
            25.11,
            55.13
        ],
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
        "coords": [
            29.35,
            47.95
        ],
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
    },
    {
        "id": "virgin-active-padel",
        "nombre": "Virgin Active Padel Club",
        "pais": "Sudáfrica",
        "pais_codigo": "ZA",
        "region_filtro": "ZA",
        "bandera": "🇿🇦",
        "ciudad_sede": "Ciudad del Cabo / Johannesburgo",
        "coords": [
            -33.9249,
            18.4241
        ],
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
        "coords": [
            -33.95,
            18.38
        ],
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
        "coords": [
            -33.9,
            151.19
        ],
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
        "coords": [
            -33.79,
            151.13
        ],
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
        "coords": [
            -33.8688,
            151.2093
        ],
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
