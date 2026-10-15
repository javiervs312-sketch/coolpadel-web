# -*- coding: utf-8 -*-
"""
Script que compila y genera dataset_franquicias.py con 106+ cadenas multiclub y franquicias de pádel.
"""

import json
import os

DATASET = [
    # =========================================================================
    # 🇬🇧 REINO UNIDO (17 Cadenas y Franquicias)
    # =========================================================================
    {
        "id": "padelstars-uk",
        "nombre": "PadelStars UK",
        "pais": "Reino Unido",
        "pais_codigo": "GB",
        "region_filtro": "GB",
        "bandera": "🇬🇧",
        "ciudad_sede": "Basildon / South East",
        "coords": [51.5761, 0.4887],
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
        "coords": [54.5200, -5.9200],
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
        "coords": [51.5105, -0.5950],
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
        "coords": [53.4900, -2.2400],
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
        "coords": [51.4330, -0.1980],
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
        "coords": [51.8980, -1.1550],
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
        "coords": [51.5074, -0.1278],
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
        "coords": [51.5560, -0.2795],
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
        "coords": [53.3280, -2.2300],
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
        "coords": [53.7997, -1.5492],
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
        "coords": [51.4545, -2.5879],
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
        "coords": [52.6309, 1.2974],
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
        "coords": [51.5054, -0.0235],
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
        "coords": [51.7180, -1.9680],
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
        "coords": [55.9533, -3.1883],
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
        "coords": [51.7311, 0.6746],
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
        "coords": [53.4084, -2.1494],
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
    }
]

print(f"Cargadas {len(DATASET)} cadenas de Reino Unido.")
