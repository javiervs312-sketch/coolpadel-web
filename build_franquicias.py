#!/usr/bin/env python3
"""
Generador del Directorio Global de Franquicias y Cadenas de Pádel (+1 Club)
para CoolPadel Studios (https://coolpadelstudios.com/franquicias-padel/).

Genera un directorio interactivo con:
- Mapa interactivo con Leaflet.js y CartoDB Positron
- Filtros dinámicos en vivo por país, modelo operativo y escala
- Buscador reactivo por texto (nombre, ciudad, software)
- Ficha técnica completa y dossier desplegable para cada franquicia
- Matriz / tabla comparativa de operadores
- Guía de inversión y modelos de rentabilidad
- Integración comercial B2B con tecnología Save My Play y merchandising CoolPadel Studios
"""

import os
import json
import urllib.parse
from datetime import datetime

FRANQUICIAS = [
    {
        "id": "bamvolea",
        "nombre": "BamVolea",
        "pais": "España",
        "pais_codigo": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Madrid",
        "coords": [40.5050, -3.7000],
        "modelo": "Red Corporativa Propia",
        "modelo_badge": "bg-blue-100 text-blue-800 border-blue-200",
        "tipo_categoria": "corporativo",
        "escala": "mega",
        "num_clubs": "16+ centros",
        "num_pistas": "260+ pistas",
        "software": "Playtomic",
        "fundadores": "Diego Rivas (CEO), Pablo Razquín (Cofundador)",
        "web": "https://bamvolea.com",
        "tagline": "El mayor operador de clubes de pádel del mundo por número de pistas.",
        "resumen": "Nacido de la integración estratégica de centros clave de Olympia Sports, la icónica Ciudad de la Raqueta en Madrid y el macrocomplejo Sportcity en Valencia, BamVolea se ha consolidado como el gigante de la gestión de clubes en España. Su filosofía no busca franquiciar a particulares, sino adquirir o asociarse con los clubes más potentes de cada provincia, centralizando compras, patrocinios y torneos, pero preservando la identidad de cada club local.",
        "sedes_principales": [
            "Ciudad de la Raqueta (Madrid - 20 pistas pádel + 20 tenis)",
            "Sportcity (Massanassa, Valencia - 30 pistas)",
            "Get Indoor BamVolea (Getafe, Madrid)",
            "BamVolea Padel Training (Rivas-Vaciamadrid)",
            "PIC - Padel Indoor Center (Barakaldo, Bilbao)",
            "Hospitalet Padel Indoor (Barcelona)",
            "BamVolea Las Tablas & Punta Chica (Alcalá de Henares)",
            "Centros en Marbella y León"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas oficiales indoor y outdoor con césped Mondo Supercourt",
            "software": "Playtomic (reservas, partidos abiertos y niveles)",
            "domotica": "Control de accesos centralizado, sistemas de climatización industrial en naves indoor",
            "grabacion": "Sistemas de streaming para pistas centrales y eventos federados",
            "restauracion": "Grandes restaurantes, terrazas lounge y sports bars de alta facturación"
        },
        "modelo_expansion": {
            "tipo_contrato": "Adquisición, integración patrimonial o gestión delegada de grandes complejos",
            "perfil_club": "Clubes consolidados de más de 10-15 pistas con alta ocupación y área social/restauración",
            "canon_royalties": "No es franquicia abierta minorista; operan como grupo corporativo y fondo de inversión deportiva",
            "inversion_media": "Macrocomplejos de 1M€ a 5M€ de valoración patrimonial"
        },
        "diferencial": "Poder de negociación masivo con marcas (Bullpadel, Adidas, Babolat), circuito propio 'BamVolea Tour', y academias de prestigio asociadas como la Paquito Navarro Academy y la ESS Feliciano López Academy."
    },
    {
        "id": "ledap-wap",
        "nombre": "LeDap / We Are Padel (WAP)",
        "pais": "Internacional (Suecia / Europa)",
        "pais_codigo": "SE",
        "bandera": "🇸🇪",
        "ciudad_sede": "Estocolmo",
        "coords": [59.3293, 18.0686],
        "modelo": "Red Corporativa Propia",
        "modelo_badge": "bg-blue-100 text-blue-800 border-blue-200",
        "tipo_categoria": "corporativo",
        "escala": "mega",
        "num_clubs": "90+ centros",
        "num_pistas": "650+ pistas",
        "software": "LeDap App / Matchi / Playtomic",
        "fundadores": "Triton Partners / Pontus Gustafsson (WAP)",
        "web": "https://ledap.com",
        "tagline": "El gigante pan-europeo del pádel indoor respaldado por capital institucional.",
        "resumen": "LeDap se constituyó como la mayor plataforma internacional de pádel mediante la adquisición masiva de operadores consolidados: We Are Padel (Suecia y Alemania), Just Padel (Noruega), Padel Club Finland (Finlandia) y Padel Zone (Austria), además de clubes en Reino Unido, Polonia, Dinamarca y España. Su modelo se centra en naves industriales indoor climatizadas de gran altura bajo el concepto Pay & Play.",
        "sedes_principales": [
            "Suecia: Más de 40 centros en Estocolmo, Gotemburgo, Malmö y ciudades medianas",
            "Alemania: Berlín, Bremen, Düsseldorf",
            "Reino Unido: Derby, Bristol",
            "Finlandia y Noruega: Red nacional en Helsinki, Tampere, Oslo",
            "Austria: Viena y Graz (Padel Zone)",
            "España: LeDap Madrid"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas indoor de 8 a 12 metros de altura libre",
            "software": "App propia LeDap integrada con Matchi y Playtomic según país",
            "domotica": "Check-in digitalizado, apertura remota mediante código y luces automatizadas",
            "grabacion": "Cámaras conectadas en pistas seleccionadas para repetición de jugadas",
            "restauracion": "Lounge corners con vending automatizado, cafetería y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Consolidación corporativa y aperturas propias financiadas por el grupo",
            "perfil_club": "Instalaciones indoor con mínimo 6 a 12 pistas para optimizar economías de escala",
            "canon_royalties": "Operación directa corporativa",
            "inversion_media": "600.000€ a 1.500.000€ por apertura de centro nuevo"
        },
        "diferencial": "Capacidad de expansión ultra-rápida, estandarización de la experiencia de juego en toda Europa y fidelización mediante su propia app paneuropea."
    },
    {
        "id": "4padel",
        "nombre": "4PADEL (Groupe LE FIVE)",
        "pais": "Francia",
        "pais_codigo": "FR",
        "bandera": "🇫🇷",
        "ciudad_sede": "París",
        "coords": [48.9100, 2.3300],
        "modelo": "Red Corporativa Propia",
        "modelo_badge": "bg-blue-100 text-blue-800 border-blue-200",
        "tipo_categoria": "corporativo",
        "escala": "grande",
        "num_clubs": "22+ centros",
        "num_pistas": "135+ pistas",
        "software": "Doinsport / My4Padel",
        "fundadores": "Damien Pelle, Guillaume Debelmas, Joseph Viéville",
        "web": "https://4padel.fr",
        "tagline": "El líder indiscutible del pádel indoor en Francia con ADN deportivo y festivo.",
        "resumen": "4PADEL es la división de pádel del Groupe LE FIVE, pionero y líder del fútbol a 5 en Francia. Han liderado la reconversión y ampliación de complejos multideporte hacia el pádel, combinando instalaciones 100% pádel (como Burdeos o Estrasburgo) con complejos híbridos. Cuentan con acuerdo oficial con Babolat y homologación para los torneos oficiales P100 a P2000 de la Federación Francesa de Tenis (FFT).",
        "sedes_principales": [
            "Estrasburgo (14 pistas indoor)",
            "Burdeos (Bordeaux-Lac - complejo insignia con 7 pistas)",
            "Toulouse-Colomiers (11 pistas)",
            "París-Marville y Montreuil",
            "Ruan (Rouen), Limoges, Metz, Valenciennes, Dunkerque, Mulhouse"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas Babolat de última generación, moqueta azul texturizada, pistas individuales (singles)",
            "software": "App My4Padel desarrollada sobre el motor de Doinsport",
            "domotica": "Marcadores digitales interactivos en pista y control de reserva",
            "grabacion": "Sistemas de vídeo en pista para descargar highlights y partidos completos",
            "restauracion": "Sports Bar completo con comida informal, cervezas artesanales y pantallas para retransmisiones"
        },
        "modelo_expansion": {
            "tipo_contrato": "Explotación propia y desarrollo en centros propios del grupo Le Five",
            "perfil_club": "Superficies de 2.500 a 5.000 m² con techos altos de más de 8 metros",
            "canon_royalties": "Operador integrado",
            "inversion_media": "1M€ a 2.5M€ por complejo multideporte"
        },
        "diferencial": "Sinergia brutal con los miles de jugadores de fútbol 5 de LE FIVE, excelente tercer tiempo y ambiente de comunidad joven y corporativa."
    },
    {
        "id": "the-padellers",
        "nombre": "The Padellers",
        "pais": "Países Bajos y Alemania",
        "pais_codigo": "NL",
        "bandera": "🇳🇱",
        "ciudad_sede": "Ámsterdam",
        "coords": [52.3676, 4.9041],
        "modelo": "Red Corporativa y Franquicia",
        "modelo_badge": "bg-indigo-100 text-indigo-800 border-indigo-200",
        "tipo_categoria": "franquicia",
        "escala": "grande",
        "num_clubs": "26+ centros",
        "num_pistas": "145+ pistas",
        "software": "BookaBall / Playtomic",
        "fundadores": "Philippe van Ellis, Bas Smit",
        "web": "https://thepadellers.nl",
        "tagline": "La cadena más dinámica y divertida de los Países Bajos en plena expansión por Alemania.",
        "resumen": "The Padellers nació en Ámsterdam con una premisa clara: democratizar el pádel sin cuotas de socios obligatorias y convirtiendo cada club en un centro social donde el post-partido (el 'borrel' holandés) es tan importante como el juego. Con más de 20 clubes en Holanda, han dado el salto a Alemania (Essen, Frankfurt, Herdecke) combinando centros propios y fórmulas de franquicia e inversión conjunta.",
        "sedes_principales": [
            "Ámsterdam (Amstelpark, West, Zuid)",
            "Breda (Bavelseparklaan y Mijkenbroek)",
            "Groningen (2 grandes complejos)",
            "Hengelo, Roermond, Valkenswaard, Venlo, Zwolle",
            "Alemania: Essen, Frankfurt-Dreieich, Herdecke, Kaltenkirchen, Troisdorf"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con iluminación LED optimizada sin sombras",
            "software": "Sistema propio de reservas BookaBall con integración en agregadores",
            "domotica": "Apertura por código QR y check-in automatizado para jugadores",
            "grabacion": "Integración con cámaras en pistas centrales para eventos corporativos",
            "restauracion": "Bares temáticos con amplia oferta de cervezas, snacks calientes y terrazas"
        },
        "modelo_expansion": {
            "tipo_contrato": "Franquicia operativa, joint-venture y clubes propios corporativos",
            "perfil_club": "Naves de mínimo 5 pistas cubiertas con zona lounge representativa",
            "canon_royalties": "Canon de entrada ~25.000€ y royalty operativo del 4-5% sobre facturación",
            "inversion_media": "350.000€ a 800.000€ según número de pistas y adecuación de nave"
        },
        "diferencial": "Potente estrategia de marketing de guerrilla e influencers en Países Bajos, eventos de empresas de primer nivel y ambiente social inigualable."
    },
    {
        "id": "peakz-padel",
        "nombre": "Peakz Padel",
        "pais": "Países Bajos y Alemania",
        "pais_codigo": "NL",
        "bandera": "🇳🇱",
        "ciudad_sede": "Utrecht",
        "coords": [52.0907, 5.1214],
        "modelo": "Red Corporativa Propia",
        "modelo_badge": "bg-blue-100 text-blue-800 border-blue-200",
        "tipo_categoria": "corporativo",
        "escala": "grande",
        "num_clubs": "17+ centros",
        "num_pistas": "110+ pistas",
        "software": "Playtomic",
        "fundadores": "Marc Kuijpers",
        "web": "https://peakzpadel.nl",
        "tagline": "Pioneros del concepto 'Pay & Play' comunitario con diseño nórdico e industrial.",
        "resumen": "Peakz Padel es uno de los operadores más antiguos y respetados de los Países Bajos. Su modelo de éxito se basa en ubicar naves en zonas estratégicas de alta densidad de población, dotándolas de pistas de máxima calidad y una atmósfera relajada ('gezellig'). No cobran cuotas mensuales de socio; cualquier jugador puede reservar pista y participar en su formato estrella: el 'King of the Court'.",
        "sedes_principales": [
            "Ámsterdam Zuidoost (14 pistas: 10 indoor, 3 outdoor, 1 single)",
            "Ámsterdam Olympiaplein",
            "Utrecht Vechtsebanen (14 pistas indoor)",
            "Utrecht Zeehaenkade",
            "Róterdam, Eindhoven, Maastricht",
            "Alemania: Kleve (7 pistas), Hagen (10 pistas), Paderborn (8 pistas), Tönisvorst (10 pistas)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas dobles e individuales ('singles') de alta competición",
            "software": "Playtomic como motor principal de reservas y cálculo de nivel",
            "domotica": "Taquillas electrónicas, iluminación automatizada y quioscos táctiles",
            "grabacion": "Pistas preparadas para streaming en torneos 'Peakz Tour'",
            "restauracion": "Clubhouse con café de especialidad, bebidas isotónicas y cervezas locales"
        },
        "modelo_expansion": {
            "tipo_contrato": "Crecimiento corporativo directo y alianzas con propietarios de naves industriales",
            "perfil_club": "Grandes recintos industriales de mínimo 6 a 12 pistas con amplio aparcamiento",
            "canon_royalties": "Operación directa",
            "inversion_media": "500.000€ a 1.200.000€ por ubicación"
        },
        "diferencial": "Cultura de club muy arraigada, torneos King of the Court semanales con cientos de participantes y excelente expansión transfronteriza en Alemania."
    },
    {
        "id": "urbanpadel",
        "nombre": "UrbanPadel (Groupe UrbanSoccer)",
        "pais": "Francia",
        "pais_codigo": "FR",
        "bandera": "🇫🇷",
        "ciudad_sede": "París",
        "coords": [48.8566, 2.3522],
        "modelo": "Red Corporativa Propia",
        "modelo_badge": "bg-blue-100 text-blue-800 border-blue-200",
        "tipo_categoria": "corporativo",
        "escala": "media",
        "num_clubs": "16+ centros",
        "num_pistas": "75+ pistas",
        "software": "UrbanPadel App / Proprietary",
        "fundadores": "UrbanSoccer (Compagnie des Alpes)",
        "web": "https://urbanpadel.fr",
        "tagline": "El gigante francés del fútbol reducido llevando el pádel a las periferias urbanas.",
        "resumen": "UrbanPadel es el brazo deportivo de UrbanSoccer, el otro gran operador histórico de complejos deportivos cubiertos en Francia. Al igual que Le Five, UrbanSoccer ha implementado pistas de pádel cubiertas dentro de sus complejos o creando anexos especializados. Su enfoque pone un peso enorme en las escuelas de formación para adultos y niños y las ligas interempresas.",
        "sedes_principales": [
            "Lille-Lezennes",
            "Lyon-Baraban",
            "Nantes-Carquefou",
            "Toulouse-Montaudran",
            "Rennes (Vern-sur-Seiche)",
            "París-Puteaux (Île de Puteaux)",
            "Angers y Clermont-Ferrand"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas indoor cubiertas con césped monofilamento azul",
            "software": "App oficial de reservas UrbanPadel con fidelización",
            "domotica": "Control de acceso sincronizado con la reserva del jugador",
            "grabacion": "Cámaras para análisis de entrenamiento y clínics",
            "restauracion": "Clubhouse espacioso con restauración rápida y pantallas deportivas"
        },
        "modelo_expansion": {
            "tipo_contrato": "Desarrollo propio sobre el parque inmobiliario de UrbanSoccer",
            "perfil_club": "Centros multideporte de 3 a 8 pistas complementarias al fútbol",
            "canon_royalties": "Operación directa",
            "inversion_media": "300.000€ a 700.000€ por implantación"
        },
        "diferencial": "Ubicaciones premium en grandes áreas metropolitanas francesas con bases de datos consolidadas de decenas de miles de deportistas corporativos."
    },
    {
        "id": "aurial-padel",
        "nombre": "Aurial Padel by Marta Marrero",
        "pais": "España",
        "pais_codigo": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Sant Cugat del Vallès (Barcelona)",
        "coords": [41.4674, 2.0818],
        "modelo": "Red Corporativa Propia",
        "modelo_badge": "bg-blue-100 text-blue-800 border-blue-200",
        "tipo_categoria": "boutique",
        "escala": "media",
        "num_clubs": "7+ centros",
        "num_pistas": "85+ pistas",
        "software": "Playtomic",
        "fundadores": "Marta Marrero (ex Nº 1 mundial), Jon Grau, Daniel Osés",
        "web": "https://aurialpadel.com",
        "tagline": "Clubes de pádel experienciales de alta gama con metodología de Nº 1 del mundo.",
        "resumen": "Aurial Padel se ha posicionado como la referencia de clubes boutique y premium en Cataluña. Impulsado por la ex número uno mundial Marta Marrero y su equipo gestor, la cadena combina instalaciones de pádel con academias de alto rendimiento, gimnasios y su propia marca de restauración 'Desbario'. Han demostrado que un club de pádel puede ofrecer una experiencia estética, gastronómica y deportiva de máxima calidad sin perder rentabilidad.",
        "sedes_principales": [
            "Aurial Augusta Sant Cugat (Sant Cugat del Vallès, Barcelona - 14 pistas)",
            "Aurial Pàdel Cornellà (Cornellà de Llobregat, Barcelona - 14 pistas)",
            "Aurial Indoor Padel Sabadell (Sabadell, Barcelona - centro indoor y sede de la Academy)",
            "Aurial Vic, Aurial Lleida, Aurial Terrassa, Aurial Reus",
            "Expansión internacional: Proyectos en Bratislava (Eslovaquia)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas WPT panorámicas con césped texturizado de competición",
            "software": "Playtomic para la gestión integral de reservas",
            "domotica": "Instalaciones ecoeficientes con climatización inteligente e iluminación LED de alta potencia",
            "grabacion": "Sistemas de vídeo en pista para entrenamientos de tecnificación y clínics",
            "restauracion": "Restaurantes 'Desbario': gastronomía cuidada, menú saludable y cócteles"
        },
        "modelo_expansion": {
            "tipo_contrato": "Gestión directa corporativa, joint-ventures y licencias de academia",
            "perfil_club": "Instalaciones de alto nivel de 8 a 15 pistas con espacio para gimnasio y restaurante",
            "canon_royalties": "Acuerdos individualizados de marca y metodología",
            "inversion_media": "600.000€ a 1.800.000€"
        },
        "diferencial": "La imagen, supervisión y metodología de Marta Marrero, excelente oferta culinaria y ambiente social de primer nivel."
    },
    {
        "id": "game4padel",
        "nombre": "Game4Padel",
        "pais": "Reino Unido",
        "pais_codigo": "GB",
        "bandera": "🇬🇧",
        "ciudad_sede": "Edimburgo / Londres",
        "coords": [55.9533, -3.1883],
        "modelo": "Inversión y Franquicia Llave en Mano",
        "modelo_badge": "bg-emerald-100 text-emerald-800 border-emerald-200",
        "tipo_categoria": "franquicia",
        "escala": "media",
        "num_clubs": "25+ sedes",
        "num_pistas": "65+ pistas",
        "software": "Matchi",
        "fundadores": "Jim Fairlie (CEO), Sir Andy Murray (Inversor), Virgil van Dijk (Embajador)",
        "web": "https://game4padel.com",
        "tagline": "El mayor desarrollador de infraestructuras de pádel de Gran Bretaña.",
        "resumen": "Game4Padel ofrece una solución única en el Reino Unido: asumen el 100% de la inversión de capital (CAPEX) para diseñar, tramitar licencias urbanísticas y construir pistas de pádel en clubes de tenis tradicionales, polideportivos, universidades y centros comerciales. A cambio, firman acuerdos de concesión a largo plazo con reparto de ingresos (revenue share) y gestión automatizada.",
        "sedes_principales": [
            "Westfield London (Centro comercial en Shepherd's Bush, Londres)",
            "Edimburgo (Thistle Tennis Club y Craiglockhart)",
            "Glasgow y Aberdeen",
            "Windsor, Shropshire, Cheshire, Cardiff (Gales)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas exteriores e interiores cubiertas con cubiertas ligeras tensadas resistentes al clima británico",
            "software": "Matchi (el software líder en Reino Unido y países nórdicos)",
            "domotica": "Acceso desasistido 24/7 con teclados de código PIN e iluminación LED sincronizada con la reserva",
            "grabacion": "Cámaras conectadas para highlights en torneos corporativos",
            "restauracion": "Aprovechan la hostelería de los clubes anfitriones o quioscos de autoservicio"
        },
        "modelo_expansion": {
            "tipo_contrato": "Concesión de terreno / Alianza con reparto de ingresos (Revenue Share)",
            "perfil_club": "Clubes de tenis o entidades con terreno infrautilizado para 2 a 6 pistas",
            "canon_royalties": "El club no invierte dinero; Game4Padel financia la obra y reparte un porcentaje mensual de los alquileres",
            "inversion_media": "150.000€ a 450.000€ por sede financiado íntegramente por Game4Padel"
        },
        "diferencial": "Respaldo institucional de Sir Andy Murray, eliminación del riesgo financiero para el club anfitrión y tecnología 100% desatendida."
    },
    {
        "id": "pdl-united-uk",
        "nombre": "PDL Padel United UK",
        "pais": "Reino Unido",
        "pais_codigo": "GB",
        "bandera": "🇬🇧",
        "ciudad_sede": "Maldon, Essex",
        "coords": [51.7311, 0.6749],
        "modelo": "Red de Clubes y Franquicias Comunitarias",
        "modelo_badge": "bg-indigo-100 text-indigo-800 border-indigo-200",
        "tipo_categoria": "franquicia",
        "escala": "media",
        "num_clubs": "14+ centros",
        "num_pistas": "55+ pistas",
        "software": "Matchi / Playtomic",
        "fundadores": "Richard Jackson (CEO UK), bajo paraguas Padel United",
        "web": "https://padeluniteduk.com",
        "tagline": "Construyendo comunidades de pádel inclusivas en todo el Reino Unido.",
        "resumen": "PDL Padel United es uno de los operadores con mayor arraigo social en el mercado británico. Con raíces en el modelo nórdico de Padel United, la filial británica ha construido clubes dedicados en Essex, Londres y el suroeste inglés, caracterizándose por una programación intensiva de dinamización: clínics para principiantes, mañanas para jubilados, ligas para jóvenes y torneos amateur constantes.",
        "sedes_principales": [
            "Maldon (Essex - centro insignia)",
            "Bushey (North London - Bushey Grove Leisure Centre)",
            "Colchester y Chelmsford",
            "The Wirral (Port Sunlight)",
            "Torbay, Plymouth, Cambridge, Down Hall"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas cubiertas con naves específicas o marquesinas para lluvia",
            "software": "Matchi y Playtomic",
            "domotica": "Control de accesos y reserva de material automático",
            "grabacion": "Dispositivos para clínics y grabaciones técnicas",
            "restauracion": "Cafetería social y tienda con palas de prueba"
        },
        "modelo_expansion": {
            "tipo_contrato": "Franquicia de gestión, clubes propios y licencias operativas",
            "perfil_club": "Zonas urbanas o suburbanas británicas de más de 3 pistas",
            "canon_royalties": "Canon de adhesión ~15.000£ y royalties operativos del 5%",
            "inversion_media": "200.000£ a 600.000£ por centro"
        },
        "diferencial": "Excepcional retención comunitaria: sus pistas tienen niveles de ocupación récord entre semana gracias a su programa de actividades sociales."
    },
    {
        "id": "padel-zenter",
        "nombre": "Padel Zenter",
        "pais": "Suecia e Italia",
        "pais_codigo": "SE",
        "bandera": "🇸🇪",
        "ciudad_sede": "Estocolmo",
        "coords": [59.2970, 18.0820],
        "modelo": "Macrocomplejos Propios de Ultra-Lujo",
        "modelo_badge": "bg-purple-100 text-purple-800 border-purple-200",
        "tipo_categoria": "boutique",
        "escala": "media",
        "num_clubs": "6 macrocentros",
        "num_pistas": "65+ pistas",
        "software": "Matchi / Proprietary",
        "fundadores": "Zlatan Ibrahimović y Thomas Sandström",
        "web": "https://padelzenter.se",
        "tagline": "La experiencia arquitectónica y de juego más exigente del mundo del pádel.",
        "resumen": "Fundada por la leyenda del fútbol Zlatan Ibrahimović y su socio Thomas Sandström, Padel Zenter rechaza el modelo de pistas apiñadas en naves industriales estándar. Cada centro Padel Zenter se construye a medida con especificaciones técnicas extremas: alturas libres de 12 metros sin columnas intermedias, iluminación LED indirecta sin deslumbramiento, paneles de absorción acústica para eliminar el eco y moqueta oficial World Padel Tour. Su centro en Segrate (Milán) es la joya de la corona del pádel italiano.",
        "sedes_principales": [
            "Milán (Segrate, Italia - 9 pistas panorámicas indoor/outdoor)",
            "Estocolmo (Ársta, Suecia)",
            "Jönköping y Skövde",
            "Örebro y Uppsala"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas AFP Courts aprobadas por la Federación Internacional de Pádel, vidrio templado de 12 mm y césped WPT",
            "software": "Matchi en Suecia y reservas online integradas en Milán",
            "domotica": "Climatización de última generación y control inteligente de ventilación",
            "grabacion": "Sistemas de televisión y streaming para retransmisiones oficiales",
            "restauracion": "Restaurantes italianos y nórdicos de calidad superior con pro-shop oficial PZ"
        },
        "modelo_expansion": {
            "tipo_contrato": "Propiedad directa y alianzas inmobiliarias selectas con inversores estratégicos",
            "perfil_club": "Macrocomplejos diseñados desde los cimientos con mínimo 8 a 15 pistas",
            "canon_royalties": "No es franquicia abierta al público general",
            "inversion_media": "3M€ a 8M€ por macrocomplejo"
        },
        "diferencial": "El carisma global y estándares de exigencia de Zlatan, acabados arquitectónicos dignos de hoteles 5 estrellas y acústica impecable."
    },
    {
        "id": "bela-padel-center",
        "nombre": "Bela Padel Center",
        "pais": "España, Argentina e Internacional",
        "pais_codigo": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Barcelona",
        "coords": [41.3879, 2.1699],
        "modelo": "Centro Insignia y Licencia de Academia",
        "modelo_badge": "bg-purple-100 text-purple-800 border-purple-200",
        "tipo_categoria": "boutique",
        "escala": "media",
        "num_clubs": "4 sedes de referencia",
        "num_pistas": "45+ pistas",
        "software": "Playtomic",
        "fundadores": "Fernando Belasteguín (16 años Nº 1 del mundo), One16 Sports",
        "web": "https://belapadelcenter.com",
        "tagline": "La escuela y templo del mayor jugador de la historia del pádel.",
        "resumen": "Bela Padel Center es el proyecto de vida y legado de Fernando Belasteguín. Combina grandes clubes propios de alta gama (como BPC Barcelona con unas 20 pistas y BPC Alicante con 14 pistas) con la exportación internacional de su metodología de enseñanza (creada junto a Miguel Sciorilli) a través de clubes licenciatarios en Argentina, México, Italia y Oriente Medio.",
        "sedes_principales": [
            "BPC Barcelona (Barcelona - 20 pistas indoor/outdoor)",
            "BPC Alicante (Playa de San Juan, Alicante - 14 pistas)",
            "Buenos Aires (Argentina)",
            "Centros licenciados en expansión en Oriente Medio y México"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de competición oficial con césped texturizado azul",
            "software": "Playtomic para gestión de reservas y ligas",
            "domotica": "Domótica de control de iluminación y climatización de pistas cubiertas",
            "grabacion": "Cámaras en pistas dedicadas para clínics, corrección biomecánica y streaming",
            "restauracion": "Clubhouse con tienda oficial Wilson x Bela y zona de restauración deportiva"
        },
        "modelo_expansion": {
            "tipo_contrato": "Licencia metodológica Bela Padel Academy y franquicia de marca para clubes seleccionados",
            "perfil_club": "Clubes de más de 8 pistas con vocación formativa y alto nivel de instalaciones",
            "canon_royalties": "Canon de marca anual + royalty por alumnos federados en la escuela",
            "inversion_media": "600.000€ a 1.500.000€"
        },
        "diferencial": "El prestigio inigualable de Fernando Belasteguín, metodología de competición probada durante 2 décadas y alianza estratégica con Wilson."
    },
    {
        "id": "padel-haus",
        "nombre": "Padel Haus",
        "pais": "Estados Unidos",
        "pais_codigo": "US",
        "bandera": "🇺🇸",
        "ciudad_sede": "Nueva York",
        "coords": [40.7128, -73.9600],
        "modelo": "Social & Athletic Club Urbano de Diseño",
        "modelo_badge": "bg-purple-100 text-purple-800 border-purple-200",
        "tipo_categoria": "boutique",
        "escala": "media",
        "num_clubs": "5 centros activos + 3 en obras",
        "num_pistas": "32+ pistas",
        "software": "Padel Haus App / Proprietary",
        "fundadores": "Santiago Gomez (Empresario hostelero)",
        "web": "https://padel.haus",
        "tagline": "El club social de pádel que está conquistando Nueva York y las grandes urbes de EE.UU.",
        "resumen": "Fundado por el empresario mexicano Santiago Gomez, Padel Haus ha sido el gran pionero en llevar el pádel a Nueva York con un posicionamiento de club atlético y social de alto standing. Sus centros combinan pistas cubiertas de diseño con su barra orgánica 'Juice Haus', zonas de wellness con baños de agua fría y saunas, espacios de coworking y vestuarios de lujo estilo Equinox.",
        "sedes_principales": [
            "Williamsburg South (Kent Ave, Brooklyn, NY - centro insignia)",
            "Williamsburg North (Brooklyn, NY)",
            "DUMBO (Washington St, Brooklyn, NY)",
            "Greenpoint (Berry St, Brooklyn, NY - su complejo más grande en NY)",
            "Domino Park (Outdoor pop-up)",
            "Aperturas en obras: Nashville, Denver y Atlanta"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas de diseño AFP Courts / Adidas Padel personalizadas con colores de marca",
            "software": "App nativa Padel Haus para iOS y Android con pasarela Stripe",
            "domotica": "Acceso biométrico y móvil para miembros, iluminación regulable",
            "grabacion": "Cámaras inteligentes en pista para descarga de jugadas en el móvil",
            "restauracion": "Juice Haus: cafetería de especialidad, zumos cold-pressed, smoothies de proteínas y snacks saludables"
        },
        "modelo_expansion": {
            "tipo_contrato": "Desarrollo propio corporativo respaldado por rondas de capital riesgo",
            "perfil_club": "Naves industriales urbanas de 2.000 a 4.500 m² en distritos de alta renta",
            "canon_royalties": "No franquicia a particulares; capital institucional",
            "inversion_media": "2.5M$ a 5M$ por club en mercados Tier-1 de EE.UU."
        },
        "diferencial": "Estética impecable, comunidad de emprendedores, creativos y deportistas de Wall Street, y el mejor modelo de membresía híbrida (Socios + Pay & Play a 50$-70$/hora)."
    },
    {
        "id": "reserve-padel",
        "nombre": "Reserve Padel",
        "pais": "Estados Unidos",
        "pais_codigo": "US",
        "bandera": "🇺🇸",
        "ciudad_sede": "Miami",
        "coords": [25.7617, -80.1918],
        "modelo": "Club de Ultra-Lujo y Eventos VIP",
        "modelo_badge": "bg-purple-100 text-purple-800 border-purple-200",
        "tipo_categoria": "boutique",
        "escala": "boutique",
        "num_clubs": "4 centros exclusivos",
        "num_pistas": "22+ pistas",
        "software": "Reserve Padel App",
        "fundadores": "Wayne Boich",
        "web": "https://reservepadel.com",
        "tagline": "El epicentro del pádel de ultra-lujo, celebridades y la Reserve Cup.",
        "resumen": "Reserve Padel es la cúspide del pádel exclusivo en Estados Unidos. Creado por el empresario Wayne Boich, Reserve saltó a la fama mundial con sus pop-ups en el Miami Design District y el Seaplane Base de Miami, atrayendo a celebridades como David Beckham, Jimmy Butler o Dwyane Wade. Organizan la 'Reserve Cup', el torneo de exhibición con la mayor bolsa de premios del planeta.",
        "sedes_principales": [
            "Reserve SoLé Mia (North Miami, FL - centro insignia permanente indoor/outdoor)",
            "Reserve Miami Design District (75 NE 39th St, Miami)",
            "Reserve Miami Seaplane Base (MacArthur Causeway)",
            "Hudson Yards (Manhattan, Nueva York - 360 10th Ave)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas personalizadas 'all black' con iluminación de diseño",
            "software": "App propia Reserve Padel con lista de espera y membresía privada",
            "domotica": "Control de accesos y concierge VIP presencial",
            "grabacion": "Cobertura televisiva y grabación en alta definición de cada sesión",
            "restauracion": "Catering gourmet, champagne bar y lounge privado para socios"
        },
        "modelo_expansion": {
            "tipo_contrato": "Explotación propia y colaboraciones con desarrolladores inmobiliarios de lujo",
            "perfil_club": "Ubicaciones icónicas en Miami y Nueva York con vistas espectaculares",
            "canon_royalties": "Club privado cerrado",
            "inversion_media": "3M$ a 7M$ por emplazamiento"
        },
        "diferencial": "Exclusividad absoluta, asistencia de estrellas mundiales y acuerdos de patrocinio con marcas como Richard Mille, Hublot y Bentley."
    },
    {
        "id": "ultra-padel",
        "nombre": "Ultra Padel Club",
        "pais": "Estados Unidos",
        "pais_codigo": "US",
        "bandera": "🇺🇸",
        "ciudad_sede": "Miami",
        "coords": [25.8290, -80.1900],
        "modelo": "Macrocomplejo y Hub Deportivo",
        "modelo_badge": "bg-blue-100 text-blue-800 border-blue-200",
        "tipo_categoria": "corporativo",
        "escala": "grande",
        "num_clubs": "2 macrocomplejos",
        "num_pistas": "38+ pistas",
        "software": "Playtomic USA",
        "fundadores": "Moisés Cohen",
        "web": "https://ultrapadelclub.com",
        "tagline": "El macrocomplejo de pádel más grande de los Estados Unidos.",
        "resumen": "Situado en el distrito de innovación de Magic City / Little River en Miami, Ultra Padel Club construyó el complejo de pádel al aire libre y cubierto más extenso de Norteamérica. Con cerca de 30 pistas en una sola ubicación, Ultra ha sido el motor de la explosión del pádel en Florida, acogiendo torneos de la USPA y concentrando a miles de jugadores semanales de la comunidad latina y estadounidense.",
        "sedes_principales": [
            "Ultra Padel Little River (Magic City Innovation District, Miami - 29 pistas)",
            "Ultra Padel Biscayne (Miami, Florida)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas exteriores e interiores con cubiertas especiales para el calor tropical",
            "software": "Playtomic para la gestión de reservas, torneos y niveles de juego",
            "domotica": "Torres de iluminación LED de competición y sonido envolvente en todo el complejo",
            "grabacion": "Pistas centrales con torretas de streaming para retransmisiones",
            "restauracion": "Restaurante con comida mediterránea, bar de copas, food trucks y terraza chill-out"
        },
        "modelo_expansion": {
            "tipo_contrato": "Operación directa y alianzas de inversión inmobiliaria comercial",
            "perfil_club": "Parcelas de gran tamaño (más de 15.000 m²) para complejos de más de 15 pistas",
            "canon_royalties": "Gestión corporativa",
            "inversion_media": "2.5M$ a 4M$ por complejo"
        },
        "diferencial": "Volumen masivo de pistas en un solo lugar, ambiente festivo latino-americano y referente indiscutible de torneos en EE.UU."
    },
    {
        "id": "padel-city",
        "nombre": "Padel City",
        "pais": "Alemania",
        "pais_codigo": "DE",
        "bandera": "🇩🇪",
        "ciudad_sede": "Fürth / Múnich",
        "coords": [49.4774, 10.9886],
        "modelo": "Red de Franquicias y Pistas Modulares",
        "modelo_badge": "bg-indigo-100 text-indigo-800 border-indigo-200",
        "tipo_categoria": "franquicia",
        "escala": "media",
        "num_clubs": "12+ centros",
        "num_pistas": "50+ pistas",
        "software": "Playtomic / CourtBrain",
        "fundadores": "PadelCity Deutschland GmbH",
        "web": "https://padelcity.de",
        "tagline": "La cadena alemana de mayor capilaridad y crecimiento rápido.",
        "resumen": "Padel City ha sido uno de los motores de la introducción del pádel en el difícil y tradicional mercado germano. Su propuesta se basa en instalar pistas cubiertas y semicubiertas en ciudades medianas y grandes, asociándose con polideportivos de tenis ya existentes o rehabilitando naves logísticas con un modelo de costes muy controlado.",
        "sedes_principales": [
            "Dortmund (Indoor y outdoor)",
            "Frankfurt am Main",
            "Fürth y Heilsbronn (Baviera)",
            "Leipzig y Múnich",
            "Múltiples centros franquiciados en Renania del Norte-Westfalia"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas de fabricantes españoles homologadas con cubiertas para invierno",
            "software": "Playtomic y CourtBrain",
            "domotica": "Acceso 100% digitalizado por teclado numérico o escaneo de código",
            "grabacion": "Preparadas para análisis técnico en escuelas",
            "restauracion": "Clubhouse funcional con bebidas y vestuarios modernos"
        },
        "modelo_expansion": {
            "tipo_contrato": "Franquicia de marca, máster franquicia regional y gestión de instalaciones",
            "perfil_club": "Centros de 3 a 6 pistas con opción de automatización en horas valle",
            "canon_royalties": "Canon de entrada ~18.000€ y 4% de royalties sobre facturación de pistas",
            "inversion_media": "250.000€ a 550.000€"
        },
        "diferencial": "Pioneros en el mercado alemán, adaptación al clima nórdico/continental y modelo eficiente de costes."
    },
    {
        "id": "padelshot",
        "nombre": "PadelShot",
        "pais": "Francia",
        "pais_codigo": "FR",
        "bandera": "🇫🇷",
        "ciudad_sede": "Caen",
        "coords": [49.1828, -0.3707],
        "modelo": "Complejos Multiactividad y Ocio Indoor",
        "modelo_badge": "bg-blue-100 text-blue-800 border-blue-200",
        "tipo_categoria": "corporativo",
        "escala": "media",
        "num_clubs": "5 centros",
        "num_pistas": "36+ pistas",
        "software": "Doinsport",
        "fundadores": "Jérôme Doligé",
        "web": "https://padelshot.fr",
        "tagline": "El concepto 'Lieu de Vie' donde el pádel convive con el bádminton, la petanca y el ocio social.",
        "resumen": "PadelShot se ha ganado el cariño de los aficionados franceses al crear centros donde el pádel es el plato fuerte, pero se rodea de otros deportes de raqueta (bádminton, squash), petanca interior y billar, todo vertebrado por un restaurante deportivo con cervezas artesanales y cocina local. Su modelo atrae no solo al jugador competitivo, sino a grupos de amigos y empresas enteras.",
        "sedes_principales": [
            "Caen (Mondeville - centro insignia)",
            "Saint-Étienne",
            "Metz",
            "Lyon (Craponne)",
            "Reims"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con salidas de pista autorizadas y moqueta WPT",
            "software": "Doinsport para la reserva multi-deporte",
            "domotica": "Marcadores digitales y control de pistas sincronizado",
            "grabacion": "Cámaras para torneos homologados FFT P500 y P1000",
            "restauracion": "Restaurante con platos del día, cerveza de barril y zonas de seminario para empresas"
        },
        "modelo_expansion": {
            "tipo_contrato": "Desarrollo propio corporativo y alianzas con inversores inmobiliarios",
            "perfil_club": "Naves de 3.000 a 6.000 m² con capacidad para 6-10 pistas de pádel más ocio",
            "canon_royalties": "Operador directo",
            "inversion_media": "1M€ a 2M€ por complejo"
        },
        "diferencial": "Excepcional facturación en hostelería y eventos corporativos que representan más del 40% de los ingresos totales del centro."
    },
    {
        "id": "plaza-padel",
        "nombre": "Plaza Padel",
        "pais": "Países Bajos",
        "pais_codigo": "NL",
        "bandera": "🇳🇱",
        "ciudad_sede": "Ámsterdam",
        "coords": [52.3888, 4.8450],
        "modelo": "Red Corporativa y Club de Negocios",
        "modelo_badge": "bg-blue-100 text-blue-800 border-blue-200",
        "tipo_categoria": "corporativo",
        "escala": "media",
        "num_clubs": "5 complejos",
        "num_pistas": "42+ pistas",
        "software": "Playtomic",
        "fundadores": "John van Lottum (Extenista ATP)",
        "web": "https://plazapadel.com",
        "tagline": "El punto de encuentro entre el pádel de alto nivel y el networking empresarial.",
        "resumen": "Fundado por el extenista holandés John van Lottum, Plaza Padel ha sabido capitalizar la enorme afición por el pádel de la comunidad corporativa de los Países Bajos. Sus clubes están diseñados con salas de reuniones de empresa, catering de negocios y clínics impartidos por extenistas y entrenadores de World Padel Tour.",
        "sedes_principales": [
            "Plaza Padel Ámsterdam (Rhoneweg - 9 pistas indoor)",
            "Plaza Padel Almelo",
            "Plaza Padel Enschede",
            "Plaza Padel Heiloo",
            "Plaza Padel Waalwijk"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas indoor homologadas con alturas libres de más de 9 metros",
            "software": "Playtomic integrado con paquetes corporativos B2B",
            "domotica": "Check-in digital, pantallas de información en recepción",
            "grabacion": "Sistemas de grabación para análisis de clínics y torneos de empresa",
            "restauracion": "Restaurante con menú ejecutivo, cafetería y terrazas cubiertas"
        },
        "modelo_expansion": {
            "tipo_contrato": "Crecimiento corporativo y acuerdos con parques empresariales",
            "perfil_club": "Complejos de 7 a 10 pistas con salas multiusos para conferencias",
            "canon_royalties": "Operación directa",
            "inversion_media": "700.000€ a 1.400.000€"
        },
        "diferencial": "El liderazgo de John van Lottum en los medios holandeses y su gran cartera de patrocinadores corporativos corporativos."
    },
    {
        "id": "click-and-padel",
        "nombre": "Click & Padel / Padel Time Sport",
        "pais": "España",
        "pais_codigo": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Albacete / Levante",
        "coords": [38.9943, -1.8585],
        "modelo": "Franquicia de Club 100% Automatizado 24/7",
        "modelo_badge": "bg-emerald-100 text-emerald-800 border-emerald-200",
        "tipo_categoria": "automatizado",
        "escala": "boutique",
        "num_clubs": "8+ centros",
        "num_pistas": "28+ pistas",
        "software": "Domótica Propia + Playtomic API",
        "fundadores": "Pioneros de la automatización deportiva en España",
        "web": "https://clickandpadel.com",
        "tagline": "El modelo de club desatendido que reduce el 70% del coste operativo.",
        "resumen": "Click & Padel y Padel Time Sport representan la vanguardia de la rentabilidad inmobiliaria en pádel: naves de 2 a 4 pistas que operan los 365 días del año sin personal en recepción. El jugador reserva desde su smartphone, recibe un código QR que abre el portón de entrada 15 minutos antes, las luces de su pista se encienden 5 minutos antes y se apagan solas al terminar el tiempo. La venta de bolas, agua y palas se realiza mediante máquinas expendedoras inteligentes.",
        "sedes_principales": [
            "Centros en Castilla-La Mancha (Albacete, Hellín, La Roda)",
            "Comunidad Valenciana y Murcia",
            "Nuevas implantaciones en polígonos periurbanos de Andalucía"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con cerramientos reforzados",
            "software": "Motor domótico conectado vía API con Playtomic y pasarelas de pago Redsys/Stripe",
            "domotica": "Cerraduras electromagnéticas, relés IoT para iluminación LED pista a pista, climatización temporizada",
            "grabacion": "Circuito cerrado de televisión (CCTV) con videovigilancia 24h conectada a Central Receptora de Alarmas",
            "restauracion": "Vending robotizado de bebidas isotónicas, palas de alquiler y accesorios"
        },
        "modelo_expansion": {
            "tipo_contrato": "Franquicia llave en mano para inversores patrimoniales",
            "perfil_club": "Naves industriales en polígonos o parcelas urbanas de 1.000 a 2.500 m²",
            "canon_royalties": "Canon de entrada ~15.000€ y royalty técnico del 4% (incluye soporte domótico y mantenimiento del software)",
            "inversion_media": "180.000€ a 350.000€ (payback estimado en 3-4 años gracias al ahorro en nóminas)"
        },
        "diferencial": "Margen neto superior al 55% sobre facturación gracias a la eliminación casi total de costes de personal presencial."
    },
    {
        "id": "paquito-navarro-academy",
        "nombre": "Paquito Navarro Academy / PSA",
        "pais": "España e Internacional",
        "pais_codigo": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Sevilla / Madrid",
        "coords": [37.3891, -5.9845],
        "modelo": "Franquicia de Academia y Metodología",
        "modelo_badge": "bg-amber-100 text-amber-800 border-amber-200",
        "tipo_categoria": "licencia",
        "escala": "media",
        "num_clubs": "12+ clubes afiliados",
        "num_pistas": "60+ pistas asociadas",
        "software": "Software Propietario de Gestión de Alumnos",
        "fundadores": "Paquito Navarro (Campeón del Mundo y referente WPT/Premier)",
        "web": "https://paquitonavarroacademy.com",
        "tagline": "La metodología ganadora del jugador más carismático del planeta.",
        "resumen": "La Paquito Navarro Academy (en conjunto con modelos como Padel Sport Academy) ofrece a clubes existentes o de nueva creación una vía directa para maximizar la ocupación de sus pistas en horas valle: transformar su escuela local en una franquicia oficial con el sello del jugador andaluz. Aportan el plan formativo completo (infantil, iniciación, avanzado y competición), formación continua de entrenadores y la visita presencial de Paquito para clínics.",
        "sedes_principales": [
            "Centros adheridos en Madrid (integrado en el circuito BamVolea)",
            "Andalucía (Sevilla, Málaga)",
            "Centros internacionales homologados en Italia, Kuwait, México y Suecia"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas homologadas según estándares de la Federación Española e Internacional",
            "software": "Plataforma de seguimiento de progresión técnica para alumnos y padres",
            "domotica": "Sistemas de reserva y cobro recurrente de cuotas de escuela",
            "grabacion": "Uso de vídeo para corrección de golpes en pista",
            "restauracion": "Co-branding con la pro-shop y el restaurante del club"
        },
        "modelo_expansion": {
            "tipo_contrato": "Franquicia y licencia de marca por exclusividad de zona geográfica",
            "perfil_club": "Clubes de 6 a 15 pistas que deseen potenciar su escuela de pádel con más de 150 alumnos",
            "canon_royalties": "Canon de entrada (12.000€ - 25.000€) y cuota mensual fija o variable por alumno matriculado",
            "inversion_media": "Inversión inicial muy contenida (15.000€ - 40.000€) ya que se implanta sobre clubes existentes"
        },
        "diferencial": "Atracción inmediata de alumnos gracias al tirón mediático de Paquito Navarro, clínics exclusivos y material técnico oficial Bullpadel."
    },
    {
        "id": "club-padel-nuestro",
        "nombre": "Club Padel Nuestro (Corners & Pro-Shops)",
        "pais": "España e Internacional",
        "pais_codigo": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Murcia",
        "coords": [37.9922, -1.1307],
        "modelo": "Franquicia de Tiendas y Pro-Shops para Clubes",
        "modelo_badge": "bg-amber-100 text-amber-800 border-amber-200",
        "tipo_categoria": "licencia",
        "escala": "mega",
        "num_clubs": "45+ tiendas físicas / 120+ clubes",
        "num_pistas": "500+ pistas asociadas",
        "software": "ERP Pádel Nuestro / TPV Integrado",
        "fundadores": "Grupo Pádel Nuestro (Líder mundial de retail de pádel)",
        "web": "https://clubpadelnuestro.com",
        "tagline": "La mayor central de compras y red de tiendas de pádel del mundo para clubes.",
        "resumen": "El Grupo Pádel Nuestro ofrece a los clubes de pádel la solución definitiva para uno de sus mayores quebraderos de cabeza: la gestión de la tienda del club. La mayoría de clubes independientes no pueden asumir el riesgo de comprar stock a decenas de fabricantes (Bullpadel, Siux, Nox, Head, Adidas, Babolat). Con la franquicia Club Pádel Nuestro, el club instala un córner o tienda oficial con acceso directo a miles de referencias con condiciones de central de compras.",
        "sedes_principales": [
            "España: Tiendas y córners en Madrid, Barcelona, Valencia, Murcia, Sevilla, Bilbao",
            "Portugal: Lisboa, Oporto",
            "Italia: Milán, Roma",
            "Suecia, Francia y Países Bajos"
        ],
        "tecnologia_pistas": {
            "pistas": "Se instala en clubes de pádel con cualquier configuración de pistas",
            "software": "TPV conectado en tiempo real con el e-commerce de Pádel Nuestro",
            "domotica": "Sistemas antirrobo y dispensadores de palas de test",
            "grabacion": "Zonas de test de palas en pista",
            "restauracion": "Complementa la recepción y cafetería del club"
        },
        "modelo_expansion": {
            "tipo_contrato": "Franquicia de retail en formato Corner (15-30 m²) o Tienda Completa (50-150 m²)",
            "perfil_club": "Clubes con más de 6 pistas y afluencia mínima de 300 jugadores semanales",
            "canon_royalties": "Canon de entrada reducido (6.000€ - 12.000€) y márgenes comerciales garantizados por la central",
            "inversion_media": "30.000€ a 60.000€ para adecuación de mobiliario corporativo y primer paquete de stock"
        },
        "diferencial": "Disponibilidad del 100% de marcas mundiales sin negociar una a una, precios mínimos garantizados y Click & Collect que atrae jugadores externos al club."
    },
    {
        "id": "soul-padel",
        "nombre": "Soul Padel",
        "pais": "Reino Unido",
        "pais_codigo": "GB",
        "bandera": "🇬🇧",
        "ciudad_sede": "Mánchester",
        "coords": [53.4808, -2.2426],
        "modelo": "Franquicia Comunitaria y Parques Comerciales",
        "modelo_badge": "bg-indigo-100 text-indigo-800 border-indigo-200",
        "tipo_categoria": "franquicia",
        "escala": "boutique",
        "num_clubs": "4 centros",
        "num_pistas": "18+ pistas",
        "software": "Matchi",
        "fundadores": "Mark Hewlett",
        "web": "https://soulpadel.co.uk",
        "tagline": "Pádel accesible y amigable en el corazón de las comunidades del norte de Inglaterra.",
        "resumen": "Soul Padel se enfoca en democratizar este deporte en el norte de Inglaterra, ubicando pistas en parques comerciales, centros universitarios y clubes deportivos comunitarios (como Wigan y Mánchester). Promueven un enfoque inclusivo, con precios asequibles en horas no punta y alquiler gratuito de palas para novatos.",
        "sedes_principales": [
            "Mánchester (Urban exchange)",
            "Wigan (Robin Park Sports Zone)",
            "Preston y Cheshire"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas exteriores e interiores con cubiertas resistentes al viento",
            "software": "Matchi",
            "domotica": "Iluminación eficiente LED y apertura por cerradura digital",
            "grabacion": "Grabación de jugadas en torneos locales",
            "restauracion": "Puntos de café y snacks saludables"
        },
        "modelo_expansion": {
            "tipo_contrato": "Desarrollo asociativo y franquicia con consejos municipales y centros de ocio",
            "perfil_club": "Suelos en desuso de 1.000 a 2.500 m² para 3 a 5 pistas",
            "canon_royalties": "Modelo flexible de franquicia social o revenue share",
            "inversion_media": "180.000£ a 350.000£ por sede"
        },
        "diferencial": "Atracción masiva de nuevos jugadores británicos que nunca antes habían tocado una pala mediante programas accesibles y acogedores."
    },
    {
        "id": "the-padel-club-uk",
        "nombre": "The Padel Club",
        "pais": "Reino Unido",
        "pais_codigo": "GB",
        "bandera": "🇬🇧",
        "ciudad_sede": "Wilmslow / Mánchester",
        "coords": [53.3283, -2.2295],
        "modelo": "Club Boutique de Alta Calidad",
        "modelo_badge": "bg-purple-100 text-purple-800 border-purple-200",
        "tipo_categoria": "boutique",
        "escala": "boutique",
        "num_clubs": "3 centros insignia",
        "num_pistas": "20+ pistas",
        "software": "Playtomic / Matchi",
        "fundadores": "Kristopher Ball",
        "web": "https://thepadelclub.co.uk",
        "tagline": "El club de pádel boutique de diseño y gastronomía de referencia en Mánchester.",
        "resumen": "The Padel Club combina la pasión por el deporte con la sofisticación del diseño contemporáneo británico. Su buque insignia en TraffordCity (Mánchester) cuenta con 11 pistas cubiertas de competición, techos acristalados, un bar de autor con cócteles y comida saludable y eventos de fin de semana con DJs en directo.",
        "sedes_principales": [
            "TraffordCity (Mánchester - 11 pistas indoor de alto nivel)",
            "Wilmslow (Cheshire - 4 pistas)",
            "Gloucester (en desarrollo)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de vidrio templado continuo sin marcos metálicos",
            "software": "Playtomic y Matchi",
            "domotica": "Sistema de sonido envolvente Bose en pistas y lounge",
            "grabacion": "Grabación de partidos en alta definición para repetición instantánea",
            "restauracion": "Clubhouse con cafetería de autor, batidos energéticos y terraza exterior"
        },
        "modelo_expansion": {
            "tipo_contrato": "Crecimiento propio y joint-ventures en grandes destinos de ocio británicos",
            "perfil_club": "Grandes recintos de alto tráfico y áreas comerciales prémium",
            "canon_royalties": "Operación directa",
            "inversion_media": "1.5M£ a 3M£ por club"
        },
        "diferencial": "La mejor combinación en Reino Unido entre experiencia de juego profesional, ocio premium y ambiente nocturno sofisticado."
    }
]

def render_html():
    franquicias_json = json.dumps(FRANQUICIAS, ensure_ascii=False)
    
    # Calcular estadísticas generales
    total_franquicias = len(FRANQUICIAS)
    paises_unicos = len(set(f["pais_codigo"] for f in FRANQUICIAS))
    
    # Pre-renderizar tarjetas
    cards_html = ""
    for f in FRANQUICIAS:
        fid = f["id"]
        nombre = f["nombre"]
        bandera = f["bandera"]
        pais = f["pais"]
        ciudad = f["ciudad_sede"]
        modelo = f["modelo"]
        badge_cls = f["modelo_badge"]
        num_clubs = f["num_clubs"]
        num_pistas = f["num_pistas"]
        software = f["software"]
        tagline = f["tagline"]
        cat = f["tipo_categoria"]
        pais_cod = f["pais_codigo"]
        escala = f["escala"]
        
        cards_html += f"""
        <article class="franchise-card bg-white rounded-3xl p-6 sm:p-7 border border-slate-200/90 shadow-sm hover:shadow-xl hover:border-slate-300 transition-all duration-300 flex flex-col justify-between group cursor-pointer"
                 data-id="{fid}"
                 data-nombre="{nombre.lower()}"
                 data-pais="{pais_cod}"
                 data-cat="{cat}"
                 data-escala="{escala}"
                 onclick="openDrawer('{fid}')">
          <div>
            <div class="flex items-start justify-between gap-3 mb-4">
              <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold border {badge_cls}">
                {modelo}
              </span>
              <span class="text-2xl" title="{pais}">{bandera}</span>
            </div>

            <h3 class="font-heading font-black text-2xl text-slate-950 group-hover:text-[#f2920b] transition-colors mb-1.5 flex items-center justify-between">
              <span>{nombre}</span>
              <i data-lucide="chevron-right" class="w-5 h-5 text-slate-400 group-hover:text-[#f2920b] group-hover:translate-x-1 transition-all"></i>
            </h3>
            
            <p class="text-xs font-semibold text-slate-500 mb-3 flex items-center gap-1.5">
              <i data-lucide="map-pin" class="w-3.5 h-3.5 text-slate-400"></i>
              <span>{ciudad}, {pais}</span>
            </p>

            <p class="text-slate-600 text-sm leading-relaxed mb-5 line-clamp-2">
              {tagline}
            </p>

            <!-- Grid de métricas clave -->
            <div class="grid grid-cols-3 gap-2 py-3 px-3.5 bg-slate-50 rounded-2xl border border-slate-100 mb-5">
              <div>
                <span class="block text-[10px] uppercase font-bold text-slate-400">Clubes</span>
                <span class="font-heading font-black text-sm text-slate-900">{num_clubs}</span>
              </div>
              <div>
                <span class="block text-[10px] uppercase font-bold text-slate-400">Pistas</span>
                <span class="font-heading font-black text-sm text-slate-900">{num_pistas}</span>
              </div>
              <div>
                <span class="block text-[10px] uppercase font-bold text-slate-400">Software</span>
                <span class="font-heading font-bold text-xs text-slate-800 truncate block" title="{software}">{software.split('/')[0].strip()}</span>
              </div>
            </div>
          </div>

          <div class="pt-2 border-t border-slate-100 flex items-center justify-between">
            <span class="text-xs font-bold text-slate-500 group-hover:text-slate-900 transition">Ver Ficha & Dossier</span>
            <span class="inline-flex items-center justify-center w-8 h-8 rounded-full bg-slate-100 group-hover:bg-[#f2920b] group-hover:text-white transition">
              <i data-lucide="arrow-up-right" class="w-4 h-4"></i>
            </span>
          </div>
        </article>
        """

    # Filas para tabla comparativa
    table_rows_html = ""
    for f in FRANQUICIAS:
        table_rows_html += f"""
        <tr class="hover:bg-slate-50/80 transition-colors cursor-pointer border-b border-slate-200/70" onclick="openDrawer('{f['id']}')">
          <td class="py-4 px-4 font-heading font-black text-slate-950 flex items-center gap-2">
            <span class="text-lg">{f['bandera']}</span>
            <span>{f['nombre']}</span>
          </td>
          <td class="py-4 px-4 text-xs font-semibold text-slate-600">
            <span class="inline-block px-2.5 py-0.5 rounded-full border {f['modelo_badge']} text-[11px]">
              {f['modelo']}
            </span>
          </td>
          <td class="py-4 px-4 text-sm font-bold text-slate-800">{f['num_clubs']}</td>
          <td class="py-4 px-4 text-sm font-bold text-slate-800">{f['num_pistas']}</td>
          <td class="py-4 px-4 text-xs font-semibold text-slate-600">{f['software']}</td>
          <td class="py-4 px-4 text-xs text-slate-600 max-w-xs truncate">{f['tagline']}</td>
          <td class="py-4 px-4 text-right">
            <button class="inline-flex items-center gap-1 text-xs font-bold text-[#f2920b] hover:text-[#d97f08] transition">
              <span>Dossier</span>
              <i data-lucide="chevron-right" class="w-3.5 h-3.5"></i>
            </button>
          </td>
        </tr>
        """

    full_html = f"""<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Directorio de Franquicias y Cadenas de Pádel (+1 Club) | CoolPadel Studios</title>
  <meta name="description" content="Directorio y mapa de las mayores franquicias y operadores de pádel del mundo con más de 1 club. Datos de sedes, modelos de negocio, inversión, software y tecnología de pista.">
  <meta name="author" content="CoolPadel Studios">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://coolpadelstudios.com/franquicias-padel/">
  <link rel="icon" type="image/png" href="../assets/images/favicon_transparente.png?v=transp3">
  <link rel="apple-touch-icon" sizes="180x180" href="../assets/images/favicon_transparente.png?v=transp3">
  <meta name="theme-color" content="#0b1626">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:locale" content="es_ES">
  <meta property="og:site_name" content="CoolPadel Studios">
  <meta property="og:url" content="https://coolpadelstudios.com/franquicias-padel/">
  <meta property="og:title" content="Directorio de Franquicias y Cadenas de Pádel (+1 Club) | Mapa y Modelos de Negocio">
  <meta property="og:description" content="Guía exhaustiva de los operadores multi-club de pádel en España, Europa y EE.UU. Requisitos de franquicia, tecnología, software de reservas y claves de rentabilidad.">
  <meta property="og:image" content="https://coolpadelstudios.com/assets/images/savemyplay-1.jpg">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Directorio de Franquicias y Cadenas de Pádel (+1 Club)">
  <meta name="twitter:description" content="Guía exhaustiva de los operadores multi-club de pádel en España, Europa y EE.UU. Requisitos de franquicia, tecnología y rentabilidad.">
  <meta name="twitter:image" content="https://coolpadelstudios.com/assets/images/savemyplay-1.jpg">

  <!-- Leaflet CSS -->
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin=""/>

  <!-- Tailwind CSS & Lucide Icons -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/lucide@0.468.0/dist/umd/lucide.min.js"></script>

  <!-- Google Fonts: Plus Jakarta Sans & Outfit -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">

  <!-- Microsoft Clarity -->
  <script type="text/javascript">
    (function(c,l,a,r,i,t,y){{
      c[a]=c[a]||function(){{(c[a].q=c[a].q||[]).push(arguments)}};
      t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
      y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    }})(window, document, "clarity", "script", "q7p8g52y9e");
  </script>

  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{
            "@type": "ListItem",
            "position": 1,
            "name": "Inicio",
            "item": "https://coolpadelstudios.com/"
          }},
          {{
            "@type": "ListItem",
            "position": 2,
            "name": "Franquicias de Pádel",
            "item": "https://coolpadelstudios.com/franquicias-padel/"
          }}
        ]
      }},
      {{
        "@type": "ItemList",
        "name": "Directorio de Franquicias y Cadenas de Pádel (+1 Club)",
        "description": "Recopilación exhaustiva de grandes operadores multi-club, franquicias llave en mano y modelos de gestión de pádel en el mundo.",
        "numberOfItems": {total_franquicias}
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "¿Cuánto cuesta abrir una franquicia de pádel?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "La inversión inicial para un club de pádel franquiciado suele situarse entre 180.000 € y 600.000 € según el número de pistas y si el modelo es 100% automatizado (menor inversión) o club social con hostelería. El canon de entrada medio oscila entre 12.000 € y 30.000 €, con royalties del 3% al 5% sobre la facturación."
            }}
          }},
          {{
            "@type": "Question",
            "name": "¿Cuáles son las mayores cadenas de pádel del mundo?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Entre los mayores operadores destacan BamVolea (España, más de 250 pistas), LeDap / We Are Padel (con más de 600 pistas en Europa), 4PADEL en Francia (más de 135 pistas), The Padellers y Peakz Padel en Países Bajos y Alemania, y Game4Padel en el Reino Unido."
            }}
          }},
          {{
            "@type": "Question",
            "name": "¿Qué software utilizan las franquicias de pádel?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "En España y sur de Europa la plataforma dominante es Playtomic. En Reino Unido y países nórdicos destaca Matchi. En Francia es muy popular Doinsport, y algunos operadores en Estados Unidos desarrollan aplicaciones propias sobre pasarelas bancarias integradas."
            }}
          }}
        ]
      }}
    ]
  }}
  </script>

  <style>
    body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
    h1, h2, h3, h4, .font-heading {{ font-family: 'Outfit', sans-serif; }}
    #map {{ height: 500px; width: 100%; border-radius: 1.5rem; z-index: 10; }}
    @media (max-width: 640px) {{
      #map {{ height: 380px; border-radius: 1rem; }}
    }}
    .custom-marker {{
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 9999px;
      font-weight: 800;
      color: #ffffff;
      box-shadow: 0 4px 14px rgba(0,0,0,0.25);
      border: 2px solid #ffffff;
      transition: transform 0.2s ease;
      cursor: pointer;
    }}
    .custom-marker:hover {{
      transform: scale(1.2);
    }}
    .leaflet-popup-content-wrapper {{
      border-radius: 1rem;
      padding: 0.25rem;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
    }}
    .drawer-open {{
      overflow: hidden;
    }}
  </style>
</head>
<body class="bg-[#f8fafc] text-slate-800 antialiased selection:bg-[#f2920b] selection:text-slate-950 min-h-screen flex flex-col">

  <!-- HEADER OFICIAL -->
  <header class="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-slate-200/80 shadow-xs">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 sm:h-20 flex items-center justify-between">
      <a href="../" class="flex items-center gap-2 group">
        <img src="../assets/images/coolpadel-mascot-hd.png" alt="Mascota CoolPadel Studios" class="h-8 sm:h-11 w-auto object-contain">
        <img src="../assets/images/coolpadel-typography-hd.png" alt="CoolPadel Studios" class="h-5 sm:h-7 w-auto object-contain">
      </a>
      
      <div class="flex items-center gap-2.5 sm:gap-6">
        <a href="../#llaveros" class="hidden md:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition">Llaveros</a>
        <a href="../camaras/" class="hidden md:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition">Cámaras Pistas</a>
        <a href="../blog/" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition">Blog</a>
        <span class="inline-block px-3 py-1 rounded-full bg-[#f2920b]/15 text-[#f2920b] font-heading font-black text-[11px] sm:text-xs uppercase tracking-wider border border-[#f2920b]/20">
          Directorio
        </span>
        
        <a href="https://wa.me/34680317486?text=Hola%20Javier%2C%20estoy%20viendo%20el%20directorio%20de%20franquicias%20de%20p%C3%A1del%20y%20me%20gustar%C3%ADa%20hacerte%20una%20consulta" target="_blank" class="inline-flex items-center gap-2 px-3.5 sm:px-5 py-2 sm:py-2.5 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs sm:text-sm tracking-wider uppercase transition shadow-sm hover:scale-105 active:scale-95">
          <span>Consultar</span>
          <i data-lucide="message-circle" class="w-3.5 h-3.5 stroke-[3]"></i>
        </a>
      </div>
    </div>
  </header>

  <!-- MAIN -->
  <main class="flex-1">

    <!-- HERO SECTION -->
    <section class="py-12 sm:py-16 bg-gradient-to-b from-white via-slate-50 to-[#f8fafc] border-b border-slate-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <!-- Breadcrumbs -->
        <nav class="flex items-center gap-2 text-xs font-bold text-slate-500 mb-6 uppercase tracking-wider">
          <a href="../" class="hover:text-slate-900 transition">Inicio</a>
          <span>/</span>
          <span class="text-[#f2920b]">Franquicias de Pádel</span>
        </nav>

        <div class="max-w-4xl space-y-4">
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-slate-900 text-white font-heading font-bold text-xs uppercase tracking-wider">
            <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
            <span>DIRECTORIO OFICIAL B2B · OPERADORES MULTI-CLUB (+1 SEDE)</span>
          </div>

          <h1 class="font-heading font-black text-3xl sm:text-5xl lg:text-6xl text-slate-950 leading-[1.08] uppercase tracking-tight">
            Directorio de Franquicias y Cadenas de Pádel
          </h1>

          <p class="text-base sm:text-xl text-slate-600 font-medium leading-relaxed">
            Análisis exhaustivo, mapa interactivo y dossier operativo de los mayores operadores de clubes del mundo. Requisitos de inversión, software de reservas, tecnología de pista y modelos de rentabilidad para propietarios e inversores deportivos.
          </p>
        </div>

        <!-- KPI BANNER -->
        <div class="grid grid-cols-2 lg:grid-cols-4 gap-3.5 sm:gap-6 mt-8 sm:mt-10 pt-8 border-t border-slate-200/80">
          <div class="bg-white p-5 rounded-2xl border border-slate-200/80 shadow-xs">
            <span class="block text-xs font-bold uppercase tracking-wider text-slate-400 mb-1">Franquicias / Cadenas</span>
            <span class="font-heading font-black text-3xl sm:text-4xl text-slate-950">{total_franquicias}+</span>
            <span class="text-xs text-slate-500 font-medium">Con más de 1 club operativo</span>
          </div>
          
          <div class="bg-white p-5 rounded-2xl border border-slate-200/80 shadow-xs">
            <span class="block text-xs font-bold uppercase tracking-wider text-slate-400 mb-1">Pistas Totales</span>
            <span class="font-heading font-black text-3xl sm:text-4xl text-slate-950">+1.850</span>
            <span class="text-xs text-slate-500 font-medium">Bajo gestión analizada</span>
          </div>

          <div class="bg-white p-5 rounded-2xl border border-slate-200/80 shadow-xs">
            <span class="block text-xs font-bold uppercase tracking-wider text-slate-400 mb-1">Presencia Global</span>
            <span class="font-heading font-black text-3xl sm:text-4xl text-slate-950">{paises_unicos} Países</span>
            <span class="text-xs text-slate-500 font-medium">Europa, Norteamérica y Latam</span>
          </div>

          <div class="bg-white p-5 rounded-2xl border border-slate-200/80 shadow-xs">
            <span class="block text-xs font-bold uppercase tracking-wider text-slate-400 mb-1">Modelos Operativos</span>
            <span class="font-heading font-black text-3xl sm:text-4xl text-[#f2920b]">4 Vías</span>
            <span class="text-xs text-slate-500 font-medium">Propio, Franquicia, 24/7 y Licencia</span>
          </div>
        </div>

      </div>
    </section>

    <!-- INTERACTIVE SECTION -->
    <section class="py-10 sm:py-14 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- CONTROLES Y FILTROS -->
      <div class="bg-white rounded-3xl p-5 sm:p-7 border border-slate-200/90 shadow-sm mb-8 space-y-5">
        
        <!-- Barra de búsqueda y vista -->
        <div class="flex flex-col md:flex-row gap-4 items-stretch md:items-center justify-between">
          <div class="relative flex-1">
            <i data-lucide="search" class="w-5 h-5 text-slate-400 absolute left-4 top-1/2 -translate-y-1/2"></i>
            <input type="text" id="searchInput" placeholder="Buscar por franquicia, ciudad, país o software (ej. Madrid, Playtomic, 24/7)..."
                   class="w-full pl-12 pr-4 py-3.5 rounded-2xl bg-slate-50 border border-slate-200 text-slate-900 placeholder-slate-400 font-medium text-sm focus:outline-none focus:ring-2 focus:ring-[#f2920b] focus:bg-white transition"
                   oninput="applyFilters()">
          </div>

          <div class="flex items-center gap-2 self-end md:self-auto">
            <button id="viewGridBtn" onclick="switchView('grid')" class="px-4 py-2.5 rounded-xl text-xs font-bold font-heading uppercase tracking-wider bg-slate-900 text-white transition flex items-center gap-1.5 shadow-xs">
              <i data-lucide="layout-grid" class="w-4 h-4"></i>
              <span>Tarjetas & Mapa</span>
            </button>
            <button id="viewTableBtn" onclick="switchView('table')" class="px-4 py-2.5 rounded-xl text-xs font-bold font-heading uppercase tracking-wider bg-slate-100 text-slate-700 hover:bg-slate-200 transition flex items-center gap-1.5">
              <i data-lucide="table" class="w-4 h-4"></i>
              <span>Tabla Comparativa</span>
            </button>
          </div>
        </div>

        <!-- Filtros por Categoría y País -->
        <div class="flex flex-col lg:flex-row gap-4 pt-3 border-t border-slate-100 justify-between items-start lg:items-center">
          
          <!-- Filtro País -->
          <div class="flex items-center gap-1.5 flex-wrap">
            <span class="text-xs font-bold uppercase text-slate-400 mr-1 flex items-center gap-1">
              <i data-lucide="globe" class="w-3.5 h-3.5"></i>
              <span>País:</span>
            </span>
            <button onclick="setCountryFilter('all')" class="filter-country-btn active px-3 py-1 rounded-lg text-xs font-bold bg-[#f2920b] text-slate-950 transition" data-country="all">Todos</button>
            <button onclick="setCountryFilter('ES')" class="filter-country-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-country="ES">🇪🇸 España</button>
            <button onclick="setCountryFilter('FR')" class="filter-country-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-country="FR">🇫🇷 Francia</button>
            <button onclick="setCountryFilter('NL')" class="filter-country-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-country="NL">🇳🇱 Países Bajos</button>
            <button onclick="setCountryFilter('GB')" class="filter-country-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-country="GB">🇬🇧 Reino Unido</button>
            <button onclick="setCountryFilter('US')" class="filter-country-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-country="US">🇺🇸 EE.UU.</button>
            <button onclick="setCountryFilter('DE')" class="filter-country-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-country="DE">🇩🇪 Alemania</button>
            <button onclick="setCountryFilter('SE')" class="filter-country-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-country="SE">🇸🇪 Nórdicos</button>
          </div>

          <!-- Filtro Modelo de Negocio -->
          <div class="flex items-center gap-1.5 flex-wrap">
            <span class="text-xs font-bold uppercase text-slate-400 mr-1 flex items-center gap-1">
              <i data-lucide="tag" class="w-3.5 h-3.5"></i>
              <span>Modelo:</span>
            </span>
            <button onclick="setModelFilter('all')" class="filter-model-btn active px-3 py-1 rounded-lg text-xs font-bold bg-slate-900 text-white transition" data-model="all">Todos</button>
            <button onclick="setModelFilter('corporativo')" class="filter-model-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-model="corporativo">Red Propia</button>
            <button onclick="setModelFilter('franquicia')" class="filter-model-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-model="franquicia">Franquicia</button>
            <button onclick="setModelFilter('automatizado')" class="filter-model-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-model="automatizado">24/7 Automatizado</button>
            <button onclick="setModelFilter('boutique')" class="filter-model-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-model="boutique">Boutique & Lujo</button>
            <button onclick="setModelFilter('licencia')" class="filter-model-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-model="licencia">Academia / Retail</button>
          </div>

        </div>

        <!-- Contador de resultados -->
        <div class="flex items-center justify-between text-xs font-semibold text-slate-500 pt-2 border-t border-slate-100">
          <span id="resultsCount">Mostrando {total_franquicias} franquicias y operadores</span>
          <span class="text-slate-400 hidden sm:inline">Haz clic en cualquier tarjeta o chincheta para ver el dossier completo</span>
        </div>

      </div>

      <!-- MAPA INTERACTIVO -->
      <div id="mapContainer" class="bg-white p-3 sm:p-4 rounded-3xl border border-slate-200/90 shadow-sm mb-10 relative">
        <div class="flex items-center justify-between px-3 py-2 mb-2">
          <div class="flex items-center gap-2">
            <span class="w-2.5 h-2.5 rounded-full bg-[#f2920b]"></span>
            <h2 class="font-heading font-black text-sm sm:text-base text-slate-900 uppercase tracking-wider">
              Mapa de Sedes Principales & Sedes Corporativas
            </h2>
          </div>
          <div class="flex items-center gap-2 text-xs font-bold">
            <button onclick="resetMapView()" class="px-3 py-1 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 transition">
              Centrar Europa
            </button>
            <button onclick="zoomToSpain()" class="px-3 py-1 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 transition">
              España
            </button>
            <button onclick="zoomToUSA()" class="px-3 py-1 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 transition">
              EE.UU.
            </button>
          </div>
        </div>

        <div id="map"></div>

        <div class="flex items-center justify-center gap-4 flex-wrap pt-3 text-[11px] font-bold text-slate-500">
          <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-full bg-[#2563eb]"></span> Red Corporativa</span>
          <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-full bg-[#4f46e5]"></span> Franquicia</span>
          <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-full bg-[#059669]"></span> 24/7 Automatizado</span>
          <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-full bg-[#9333ea]"></span> Boutique / Lujo</span>
          <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-full bg-[#d97706]"></span> Academia / Retail</span>
        </div>
      </div>

      <!-- GRID DE TARJETAS -->
      <div id="gridView" class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {cards_html}
      </div>

      <!-- TABLA COMPARATIVA (OCULTA POR DEFECTO) -->
      <div id="tableView" class="hidden bg-white rounded-3xl border border-slate-200/90 shadow-sm overflow-hidden">
        <div class="overflow-x-auto">
          <table class="w-full text-left border-collapse">
            <thead>
              <tr class="bg-slate-900 text-white text-[11px] uppercase font-heading font-black tracking-wider">
                <th class="py-4 px-4">Franquicia / Operador</th>
                <th class="py-4 px-4">Modelo</th>
                <th class="py-4 px-4">Clubes</th>
                <th class="py-4 px-4">Pistas</th>
                <th class="py-4 px-4">Software</th>
                <th class="py-4 px-4">Enfoque / Diferencial</th>
                <th class="py-4 px-4 text-right">Detalle</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-100">
              {table_rows_html}
            </tbody>
          </table>
        </div>
      </div>

    </section>

    <!-- GUÍA DE NEGOCIO Y MODELOS DE FRANQUICIA -->
    <section class="py-14 sm:py-20 bg-white border-t border-b border-slate-200">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div class="text-center max-w-3xl mx-auto mb-12 space-y-3">
          <span class="inline-block px-3 py-1 rounded-full bg-[#f2920b]/15 text-[#f2920b] font-heading font-black text-xs uppercase tracking-wider">
            ANÁLISIS ESTRATÉGICO PARA INVERSORES
          </span>
          <h2 class="font-heading font-black text-2xl sm:text-4xl text-slate-950 uppercase tracking-tight">
            ¿Qué Modelo de Franquicia de Pádel es el Más Rentable?
          </h2>
          <p class="text-slate-600 text-sm sm:text-base leading-relaxed">
            El sector del pádel ha dejado atrás la era amateur. Hoy existen 4 fórmulas consolidadas para operar múltiples clubes con alta rentabilidad sobre el capital invertido (ROIC).
          </p>
        </div>

        <div class="grid md:grid-cols-2 gap-6 sm:gap-8">
          
          <!-- Bloque 1 -->
          <div class="bg-slate-50 p-6 sm:p-8 rounded-3xl border border-slate-200/90 hover:shadow-md transition">
            <div class="w-10 h-10 rounded-xl bg-blue-600 text-white flex items-center justify-center font-heading font-black text-lg mb-4">
              1
            </div>
            <h3 class="font-heading font-black text-xl text-slate-950 mb-2">Red Corporativa / Alianza de Escala</h3>
            <p class="text-slate-600 text-sm leading-relaxed mb-4">
              Ejemplos como <strong>BamVolea</strong> o <strong>LeDap</strong> no franquician a inversores noveles: compran instalaciones existentes o integran clubes de más de 10-15 pistas. La ventaja es el poder de negociación en patrocinios, compras centralizadas de palas y pelotas, y circuitos unificados de torneos.
            </p>
            <div class="text-xs font-bold text-blue-700 bg-blue-50 p-3 rounded-xl border border-blue-100">
              💡 Ideal para: Propietarios de clubes grandes que buscan liquidez o asociarse a un operador dominante.
            </div>
          </div>

          <!-- Bloque 2 -->
          <div class="bg-slate-50 p-6 sm:p-8 rounded-3xl border border-slate-200/90 hover:shadow-md transition">
            <div class="w-10 h-10 rounded-xl bg-emerald-600 text-white flex items-center justify-center font-heading font-black text-lg mb-4">
              2
            </div>
            <h3 class="font-heading font-black text-xl text-slate-950 mb-2">Club Automatizado 24/7 sin Personal</h3>
            <p class="text-slate-600 text-sm leading-relaxed mb-4">
              Franquicias como <strong>Click & Padel</strong> o <strong>Padel Time</strong> reducen el personal presencial mediante cerraduras electromagnéticas, códigos QR, encendido automático de luces e integración directa con Playtomic. 
            </p>
            <div class="text-xs font-bold text-emerald-700 bg-emerald-50 p-3 rounded-xl border border-emerald-100">
              💡 Margen neto > 50%: El coste laboral (nóminas de recepción) suele suponer el 40% del gasto de un club convencional.
            </div>
          </div>

          <!-- Bloque 3 -->
          <div class="bg-slate-50 p-6 sm:p-8 rounded-3xl border border-slate-200/90 hover:shadow-md transition">
            <div class="w-10 h-10 rounded-xl bg-purple-600 text-white flex items-center justify-center font-heading font-black text-lg mb-4">
              3
            </div>
            <h3 class="font-heading font-black text-xl text-slate-950 mb-2">Club Boutique, Social & Hospitality</h3>
            <p class="text-slate-600 text-sm leading-relaxed mb-4">
              Modelos como <strong>Padel Haus</strong> en EE.UU., <strong>The Padellers</strong> en Países Bajos o <strong>Aurial Padel</strong> en España entienden que el pádel es un fenómeno social. El 30% al 45% de la facturación proviene del bar, restaurante, cafetería orgánica, eventos de empresa y torneos afterwork.
            </p>
            <div class="text-xs font-bold text-purple-700 bg-purple-50 p-3 rounded-xl border border-purple-100">
              💡 Clave: El alquiler de pista amortiza el CAPEX; el bar y los eventos generan el beneficio neto líquido.
            </div>
          </div>

          <!-- Bloque 4 -->
          <div class="bg-slate-50 p-6 sm:p-8 rounded-3xl border border-slate-200/90 hover:shadow-md transition">
            <div class="w-10 h-10 rounded-xl bg-amber-600 text-white flex items-center justify-center font-heading font-black text-lg mb-4">
              4
            </div>
            <h3 class="font-heading font-black text-xl text-slate-950 mb-2">Franquicia de Academia & Pro-Shop en Club</h3>
            <p class="text-slate-600 text-sm leading-relaxed mb-4">
              Marcas como la <strong>Paquito Navarro Academy</strong> o la red de corners <strong>Club Pádel Nuestro</strong> permiten a clubes ya en marcha franquiciar solo una sección (la escuela o la tienda del club), disparando los ingresos por alumno y profesionalizando el inventario de material.
            </p>
            <div class="text-xs font-bold text-amber-700 bg-amber-50 p-3 rounded-xl border border-amber-100">
              💡 Inversión muy baja: No exige obra civil nueva y monetiza las horas valle (mañanas y primeras horas de la tarde).
            </div>
          </div>

        </div>

      </div>
    </section>

    <!-- BANNER B2B COOLPADEL / SAVE MY PLAY -->
    <section class="py-14 sm:py-20 bg-slate-950 text-white relative overflow-hidden">
      <div class="absolute inset-0 bg-[radial-gradient(circle_at_top_right,rgba(242,146,11,0.15),transparent_50%)]"></div>
      
      <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center space-y-6">
        <span class="inline-block px-3.5 py-1 rounded-full bg-[#f2920b]/20 text-[#f2920b] font-heading font-black text-xs uppercase tracking-wider border border-[#f2920b]/30">
          TECNOLOGÍA & MERCHANDISING PARA FRANQUICIAS Y CLUBES
        </span>

        <h2 class="font-heading font-black text-2xl sm:text-4xl lg:text-5xl uppercase tracking-tight max-w-3xl mx-auto">
          ¿Tienes Más de un Club o Quieres Franquiciar tu Marca?
        </h2>

        <p class="text-slate-300 text-base sm:text-lg max-w-2xl mx-auto font-medium leading-relaxed">
          En <strong>CoolPadel Studios</strong> ayudamos a operadores multi-club y franquicias con dos soluciones probadas en más de 25 complejos deportivos de Europa:
        </p>

        <div class="grid sm:grid-cols-2 gap-6 text-left max-w-3xl mx-auto pt-4">
          <div class="bg-white/5 backdrop-blur-md p-6 rounded-2xl border border-white/10 hover:border-[#f2920b]/40 transition">
            <div class="flex items-center gap-2 mb-2 font-heading font-black text-lg text-white">
              <i data-lucide="video" class="w-5 h-5 text-[#f2920b]"></i>
              <span>Cámaras Save My Play</span>
            </div>
            <p class="text-sm text-slate-300 leading-relaxed">
              Grabación en pista y repetición en vídeo con pulsador físico en poste. Montaje en 5 minutos sin zanjas ni obras, y sin cuotas abusivas de permanencia.
            </p>
            <a href="../camaras/" class="inline-flex items-center gap-1.5 text-xs font-bold text-[#f2920b] hover:underline mt-3">
              <span>Ver sistema de cámaras</span>
              <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
            </a>
          </div>

          <div class="bg-white/5 backdrop-blur-md p-6 rounded-2xl border border-white/10 hover:border-[#f2920b]/40 transition">
            <div class="flex items-center gap-2 mb-2 font-heading font-black text-lg text-white">
              <i data-lucide="shield" class="w-5 h-5 text-[#f2920b]"></i>
              <span>Llaveros 3D Oficiales</span>
            </div>
            <p class="text-sm text-slate-300 leading-relaxed">
              Fabricación directa de llaveros de goma en relieve 3D con el logo oficial de tu franquicia para la pro-shop, abonados y torneos del club. Muestra física previa 15€.
            </p>
            <a href="../llaveros-padel-personalizados/" class="inline-flex items-center gap-1.5 text-xs font-bold text-[#f2920b] hover:underline mt-3">
              <span>Ver llaveros para clubs</span>
              <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
            </a>
          </div>
        </div>

        <div class="pt-4 flex flex-col sm:flex-row items-center justify-center gap-4">
          <a href="https://wa.me/34680317486?text=Hola%20Javier%2C%20tengo%20un%20club%20de%20p%C3%A1del%20(o%20varios)%20y%20quiero%20hablar%20contigo%20sobre%20tecnolog%C3%ADa%20y%20merchandising" target="_blank"
             class="inline-flex items-center justify-center gap-2.5 px-8 py-4 rounded-2xl bg-[#25D366] hover:bg-[#20ba59] text-white font-heading font-black text-base uppercase tracking-wider shadow-lg hover:scale-105 active:scale-95 transition w-full sm:w-auto">
            <i data-lucide="message-circle" class="w-5 h-5"></i>
            <span>Hablar con Javier por WhatsApp</span>
          </a>
          <a href="mailto:hola@coolpadelstudios.com" class="inline-flex items-center justify-center gap-2 px-6 py-4 rounded-2xl bg-white/10 hover:bg-white/20 text-white font-heading font-bold text-sm transition w-full sm:w-auto">
            <i data-lucide="mail" class="w-4 h-4"></i>
            <span>hola@coolpadelstudios.com</span>
          </a>
        </div>

      </div>
    </section>

  </main>

  <!-- FOOTER OFICIAL -->
  <footer class="bg-white border-t border-slate-200 py-12">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col md:flex-row items-center justify-between gap-6">
        <div class="flex items-center gap-3">
          <img src="../assets/images/coolpadel-mascot-hd.png" alt="Mascota CoolPadel Studios" class="h-9 w-auto object-contain">
          <div class="text-left">
            <span class="block font-heading font-black text-slate-900 text-sm">CoolPadel Studios</span>
            <span class="text-xs text-slate-500">Tecnología en pista, merchandising y desarrollo para clubes de pádel</span>
          </div>
        </div>

        <div class="flex items-center gap-6 text-xs font-bold text-slate-600">
          <a href="../" class="hover:text-slate-900 transition">Inicio</a>
          <a href="../#llaveros" class="hover:text-slate-900 transition">Llaveros Personalizados</a>
          <a href="../camaras/" class="hover:text-slate-900 transition">Cámaras Save My Play</a>
          <a href="../blog/" class="hover:text-slate-900 transition">Blog</a>
          <a href="https://wa.me/34680317486" target="_blank" class="text-[#f2920b] hover:underline">Contacto</a>
        </div>
      </div>

      <div class="mt-8 pt-6 border-t border-slate-100 flex flex-col sm:flex-row items-center justify-between text-xs text-slate-400 gap-2">
        <span>&copy; {datetime.now().year} CoolPadel Studios. Todos los derechos reservados.</span>
        <span>Información recopilada con fines informativos y de análisis de la industria deportiva.</span>
      </div>
    </div>
  </footer>

  <!-- DRAWER / MODAL LATERAL DE DOSSIER DE FRANQUICIA -->
  <div id="drawerOverlay" class="fixed inset-0 bg-slate-950/60 backdrop-blur-xs z-50 opacity-0 pointer-events-none transition-opacity duration-300" onclick="closeDrawer()"></div>
  
  <aside id="franchiseDrawer" class="fixed top-0 right-0 w-full sm:w-[540px] lg:w-[600px] h-full bg-white z-50 shadow-2xl transform translate-x-full transition-transform duration-300 flex flex-col">
    <!-- Header Drawer -->
    <div class="p-6 border-b border-slate-200 flex items-start justify-between bg-slate-50/80">
      <div>
        <div class="flex items-center gap-2 mb-1.5">
          <span id="drawerBadge" class="inline-block px-2.5 py-0.5 rounded-full text-xs font-bold border"></span>
          <span id="drawerFlag" class="text-xl"></span>
        </div>
        <h3 id="drawerTitle" class="font-heading font-black text-2xl sm:text-3xl text-slate-950"></h3>
        <p id="drawerCity" class="text-xs font-bold text-slate-500 flex items-center gap-1 mt-1"></p>
      </div>
      <button onclick="closeDrawer()" class="w-9 h-9 rounded-full bg-white border border-slate-200 hover:bg-slate-100 flex items-center justify-center text-slate-500 hover:text-slate-900 transition shadow-xs">
        <i data-lucide="x" class="w-5 h-5"></i>
      </button>
    </div>

    <!-- Contenido Scrollable Drawer -->
    <div class="flex-1 overflow-y-auto p-6 space-y-6 text-sm text-slate-700">
      
      <!-- Tagline -->
      <div class="p-4 rounded-2xl bg-amber-50/60 border border-amber-200/70 text-amber-900 font-semibold text-sm" id="drawerTagline"></div>

      <!-- Resumen y Filosofía -->
      <div>
        <h4 class="font-heading font-black text-sm uppercase text-slate-400 tracking-wider mb-2 flex items-center gap-1.5">
          <i data-lucide="info" class="w-4 h-4 text-[#f2920b]"></i>
          <span>Resumen Ejecutivo & Filosofía Operativa</span>
        </h4>
        <p id="drawerResumen" class="leading-relaxed text-slate-600 text-sm"></p>
      </div>

      <!-- Métricas Clave -->
      <div class="grid grid-cols-2 gap-3 p-4 bg-slate-50 rounded-2xl border border-slate-100">
        <div>
          <span class="block text-[11px] font-bold uppercase text-slate-400">Clubes Operativos</span>
          <span id="drawerClubs" class="font-heading font-black text-base text-slate-950"></span>
        </div>
        <div>
          <span class="block text-[11px] font-bold uppercase text-slate-400">Pistas Totales</span>
          <span id="drawerPistas" class="font-heading font-black text-base text-slate-950"></span>
        </div>
        <div>
          <span class="block text-[11px] font-bold uppercase text-slate-400">Software / ERP</span>
          <span id="drawerSoftware" class="font-heading font-black text-base text-slate-950"></span>
        </div>
        <div>
          <span class="block text-[11px] font-bold uppercase text-slate-400">Fundadores / Dirección</span>
          <span id="drawerFundadores" class="font-heading font-bold text-xs text-slate-800"></span>
        </div>
      </div>

      <!-- Sedes Principales -->
      <div>
        <h4 class="font-heading font-black text-sm uppercase text-slate-400 tracking-wider mb-2.5 flex items-center gap-1.5">
          <i data-lucide="map" class="w-4 h-4 text-[#f2920b]"></i>
          <span>Sedes y Complejos Principales</span>
        </h4>
        <ul id="drawerSedes" class="space-y-1.5 text-xs text-slate-600 bg-slate-50 p-4 rounded-2xl border border-slate-100"></ul>
      </div>

      <!-- Pila Tecnológica & Pistas -->
      <div>
        <h4 class="font-heading font-black text-sm uppercase text-slate-400 tracking-wider mb-2.5 flex items-center gap-1.5">
          <i data-lucide="cpu" class="w-4 h-4 text-[#f2920b]"></i>
          <span>Tecnología en Pista & Experiencia de Juego</span>
        </h4>
        <div class="space-y-2 text-xs bg-slate-50 p-4 rounded-2xl border border-slate-100" id="drawerTech"></div>
      </div>

      <!-- Modelo de Franquicia & Expansión -->
      <div>
        <h4 class="font-heading font-black text-sm uppercase text-slate-400 tracking-wider mb-2.5 flex items-center gap-1.5">
          <i data-lucide="briefcase" class="w-4 h-4 text-[#f2920b]"></i>
          <span>Modelo de Franquicia, Inversión & Expansión</span>
        </h4>
        <div class="space-y-2 text-xs bg-slate-50 p-4 rounded-2xl border border-slate-100" id="drawerExpansion"></div>
      </div>

      <!-- Diferencial -->
      <div>
        <h4 class="font-heading font-black text-sm uppercase text-slate-400 tracking-wider mb-1.5 flex items-center gap-1.5">
          <i data-lucide="sparkles" class="w-4 h-4 text-[#f2920b]"></i>
          <span>Factor Clave de Éxito / Diferencial</span>
        </h4>
        <p id="drawerDiferencial" class="text-xs text-slate-600 italic bg-amber-50/40 p-3.5 rounded-xl border border-amber-100"></p>
      </div>

    </div>

    <!-- Footer Drawer -->
    <div class="p-4 border-t border-slate-200 bg-slate-50 flex items-center justify-between gap-3">
      <a id="drawerWebBtn" href="#" target="_blank" rel="noopener noreferrer"
         class="flex-1 inline-flex items-center justify-center gap-2 px-4 py-3 rounded-xl bg-slate-900 hover:bg-slate-800 text-white font-heading font-bold text-xs uppercase tracking-wider transition">
        <span>Visitar Web Oficial</span>
        <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
      </a>

      <a id="drawerWaBtn" href="#" target="_blank"
         class="inline-flex items-center justify-center gap-2 px-4 py-3 rounded-xl bg-[#f2920b] hover:bg-[#d97f08] text-slate-950 font-heading font-bold text-xs uppercase tracking-wider transition">
        <i data-lucide="message-circle" class="w-4 h-4"></i>
        <span>Preguntar a Javier</span>
      </a>
    </div>
  </aside>

  <!-- Leaflet JS -->
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>

  <!-- SCRIPT APLICACIÓN -->
  <script>
    const FRANQUICIAS = {franquicias_json};
    let map = null;
    let markersLayer = null;
    let currentCountry = 'all';
    let currentModel = 'all';
    let currentView = 'grid';

    // Inicializar Iconos Lucide
    document.addEventListener("DOMContentLoaded", function() {{
      lucide.createIcons();
      initMap();
    }});

    function getMarkerColor(categoria) {{
      switch(categoria) {{
        case 'corporativo': return '#2563eb';
        case 'franquicia': return '#4f46e5';
        case 'automatizado': return '#059669';
        case 'boutique': return '#9333ea';
        case 'licencia': return '#d97706';
        default: return '#f2920b';
      }}
    }}

    function initMap() {{
      // Centro por defecto: Europa Occidental
      map = L.map('map', {{
        center: [48.0, 5.0],
        zoom: 4,
        minZoom: 3,
        maxZoom: 16,
        scrollWheelZoom: false
      }});

      // CartoDB Positron: rápido, minimalista y libre
      L.tileLayer('https://{{s}}.basemaps.cartocdn.com/light_all/{{z}}/{{x}}/{{y}}{{r}}.png', {{
        attribution: '&copy; <a href="https://carto.com/">CARTO</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
        subdomains: 'abcd',
        maxZoom: 19
      }}).addTo(map);

      markersLayer = L.layerGroup().addTo(map);
      renderMarkers(FRANQUICIAS);
    }}

    function renderMarkers(items) {{
      markersLayer.clearLayers();

      items.forEach(f => {{
        if (!f.coords || f.coords.length !== 2) return;
        const color = getMarkerColor(f.tipo_categoria);

        const customIcon = L.divIcon({{
          className: '',
          html: `<div class="custom-marker" style="background-color: ${{color}}; width: 32px; height: 32px; font-size: 13px;">${{f.bandera}}</div>`,
          iconSize: [32, 32],
          iconAnchor: [16, 16],
          popupAnchor: [0, -16]
        }});

        const popupContent = `
          <div style="font-family: 'Plus Jakarta Sans', sans-serif; min-width: 200px; padding: 6px;">
            <div style="font-size: 11px; font-weight: 700; color: #64748b; text-transform: uppercase;">${{f.ciudad_sede}}, ${{f.pais}}</div>
            <div style="font-family: 'Outfit', sans-serif; font-size: 16px; font-weight: 900; color: #0f172a; margin: 2px 0 6px 0;">${{f.nombre}}</div>
            <div style="display: flex; gap: 8px; font-size: 11px; font-weight: 700; margin-bottom: 8px;">
              <span style="background: #f1f5f9; padding: 2px 6px; border-radius: 6px;">${{f.num_clubs}}</span>
              <span style="background: #fef3c7; color: #92400e; padding: 2px 6px; border-radius: 6px;">${{f.num_pistas}}</span>
            </div>
            <p style="font-size: 11px; color: #475569; margin-bottom: 8px; line-height: 1.3;">${{f.tagline}}</p>
            <button onclick="openDrawer('${{f.id}}')" style="width: 100%; background: #0f172a; color: #ffffff; border: none; padding: 6px 10px; border-radius: 8px; font-size: 11px; font-weight: 800; cursor: pointer;">
              Ver Dossier Completo →
            </button>
          </div>
        `;

        const marker = L.marker(f.coords, {{ icon: customIcon }})
          .bindPopup(popupContent);
        markersLayer.addLayer(marker);
      }});
    }}

    function resetMapView() {{
      map.setView([48.0, 5.0], 4);
    }}

    function zoomToSpain() {{
      map.setView([40.2, -3.7], 6);
    }}

    function zoomToUSA() {{
      map.setView([33.0, -85.0], 4);
    }}

    function setCountryFilter(country) {{
      currentCountry = country;
      document.querySelectorAll('.filter-country-btn').forEach(btn => {{
        if (btn.dataset.country === country) {{
          btn.classList.add('bg-[#f2920b]', 'text-slate-950');
          btn.classList.remove('bg-slate-100', 'text-slate-600');
        }} else {{
          btn.classList.remove('bg-[#f2920b]', 'text-slate-950');
          btn.classList.add('bg-slate-100', 'text-slate-600');
        }}
      }});
      applyFilters();
    }}

    function setModelFilter(model) {{
      currentModel = model;
      document.querySelectorAll('.filter-model-btn').forEach(btn => {{
        if (btn.dataset.model === model) {{
          btn.classList.add('bg-slate-900', 'text-white');
          btn.classList.remove('bg-slate-100', 'text-slate-600');
        }} else {{
          btn.classList.remove('bg-slate-900', 'text-white');
          btn.classList.add('bg-slate-100', 'text-slate-600');
        }}
      }});
      applyFilters();
    }}

    function applyFilters() {{
      const query = document.getElementById('searchInput').value.toLowerCase().trim();
      
      const cards = document.querySelectorAll('.franchise-card');
      const tableRows = document.querySelectorAll('#tableView tbody tr');
      
      let visibleCount = 0;
      let filteredData = [];

      FRANQUICIAS.forEach((f, idx) => {{
        const matchCountry = (currentCountry === 'all' || f.pais_codigo === currentCountry);
        const matchModel = (currentModel === 'all' || f.tipo_categoria === currentModel);
        
        const textToSearch = `${{f.nombre}} ${{f.pais}} ${{f.ciudad_sede}} ${{f.software}} ${{f.tagline}} ${{f.modelo}}`.toLowerCase();
        const matchQuery = !query || textToSearch.includes(query);

        const isVisible = matchCountry && matchModel && matchQuery;

        if (cards[idx]) {{
          cards[idx].style.display = isVisible ? 'flex' : 'none';
        }}
        if (tableRows[idx]) {{
          tableRows[idx].style.display = isVisible ? '' : 'none';
        }}

        if (isVisible) {{
          visibleCount++;
          filteredData.push(f);
        }}
      }});

      document.getElementById('resultsCount').textContent = `Mostrando ${{visibleCount}} de ${{FRANQUICIAS.length}} franquicias y operadores`;
      renderMarkers(filteredData);
    }}

    function switchView(view) {{
      currentView = view;
      const gridView = document.getElementById('gridView');
      const tableView = document.getElementById('tableView');
      const mapContainer = document.getElementById('mapContainer');
      const viewGridBtn = document.getElementById('viewGridBtn');
      const viewTableBtn = document.getElementById('viewTableBtn');

      if (view === 'grid') {{
        gridView.classList.remove('hidden');
        tableView.classList.add('hidden');
        mapContainer.classList.remove('hidden');
        
        viewGridBtn.className = "px-4 py-2.5 rounded-xl text-xs font-bold font-heading uppercase tracking-wider bg-slate-900 text-white transition flex items-center gap-1.5 shadow-xs";
        viewTableBtn.className = "px-4 py-2.5 rounded-xl text-xs font-bold font-heading uppercase tracking-wider bg-slate-100 text-slate-700 hover:bg-slate-200 transition flex items-center gap-1.5";
        
        setTimeout(() => {{ if (map) map.invalidateSize(); }}, 100);
      }} else {{
        gridView.classList.add('hidden');
        tableView.classList.remove('hidden');
        mapContainer.classList.add('hidden');

        viewGridBtn.className = "px-4 py-2.5 rounded-xl text-xs font-bold font-heading uppercase tracking-wider bg-slate-100 text-slate-700 hover:bg-slate-200 transition flex items-center gap-1.5";
        viewTableBtn.className = "px-4 py-2.5 rounded-xl text-xs font-bold font-heading uppercase tracking-wider bg-slate-900 text-white transition flex items-center gap-1.5 shadow-xs";
      }}
    }}

    function openDrawer(id) {{
      const f = FRANQUICIAS.find(item => item.id === id);
      if (!f) return;

      document.getElementById('drawerTitle').textContent = f.nombre;
      document.getElementById('drawerFlag').textContent = f.bandera;
      document.getElementById('drawerBadge').textContent = f.modelo;
      document.getElementById('drawerBadge').className = `inline-block px-2.5 py-0.5 rounded-full text-xs font-bold border ${{f.modelo_badge}}`;
      document.getElementById('drawerCity').innerHTML = `<i data-lucide="map-pin" class="w-3.5 h-3.5 text-slate-400"></i> Sede: ${{f.ciudad_sede}}, ${{f.pais}}`;
      document.getElementById('drawerTagline').textContent = f.tagline;
      document.getElementById('drawerResumen').textContent = f.resumen;
      document.getElementById('drawerClubs').textContent = f.num_clubs;
      document.getElementById('drawerPistas').textContent = f.num_pistas;
      document.getElementById('drawerSoftware').textContent = f.software;
      document.getElementById('drawerFundadores').textContent = f.fundadores;

      // Sedes
      const sedesList = document.getElementById('drawerSedes');
      sedesList.innerHTML = f.sedes_principales.map(s => `<li class="flex items-start gap-2"><span class="text-[#f2920b] font-bold">•</span><span>${{s}}</span></li>`).join('');

      // Tech
      const techBox = document.getElementById('drawerTech');
      techBox.innerHTML = `
        <div><strong>Pistas y Césped:</strong> ${{f.tecnologia_pistas.pistas}}</div>
        <div><strong>Software y Reservas:</strong> ${{f.tecnologia_pistas.software}}</div>
        <div><strong>Domótica y Accesos:</strong> ${{f.tecnologia_pistas.domotica}}</div>
        <div><strong>Grabación / Vídeo:</strong> ${{f.tecnologia_pistas.grabacion}}</div>
        <div><strong>Restauración / Hospitality:</strong> ${{f.tecnologia_pistas.restauracion}}</div>
      `;

      // Expansion
      const expBox = document.getElementById('drawerExpansion');
      expBox.innerHTML = `
        <div><strong>Tipo de Contrato:</strong> ${{f.modelo_expansion.tipo_contrato}}</div>
        <div><strong>Perfil de Club Idóneo:</strong> ${{f.modelo_expansion.perfil_club}}</div>
        <div><strong>Canon & Royalties:</strong> ${{f.modelo_expansion.canon_royalties}}</div>
        <div><strong>Inversión Estimada:</strong> ${{f.modelo_expansion.inversion_media}}</div>
      `;

      // Diferencial
      document.getElementById('drawerDiferencial').textContent = f.diferencial;

      // Botones
      document.getElementById('drawerWebBtn').href = f.web;
      document.getElementById('drawerWaBtn').href = `https://wa.me/34680317486?text=Hola%20Javier%2C%20estoy%20viendo%20la%20ficha%20de%20${{encodeURIComponent(f.nombre)}}%20en%20el%20directorio%20y%20quiero%20hacerte%20una%20consulta`;

      // Mostrar
      document.getElementById('drawerOverlay').classList.remove('opacity-0', 'pointer-events-none');
      document.getElementById('franchiseDrawer').classList.remove('translate-x-full');
      document.body.classList.add('drawer-open');
      lucide.createIcons();
    }}

    function closeDrawer() {{
      document.getElementById('drawerOverlay').classList.add('opacity-0', 'pointer-events-none');
      document.getElementById('franchiseDrawer').classList.add('translate-x-full');
      document.body.classList.remove('drawer-open');
    }}

    // Cerrar con Escape
    document.addEventListener('keydown', function(e) {{
      if (e.key === 'Escape') closeDrawer();
    }});
  </script>
</body>
</html>
"""
    return full_html


def main():
    target_dir = os.path.join(os.path.dirname(__file__), "franquicias-padel")
    os.makedirs(target_dir, exist_ok=True)
    target_file = os.path.join(target_dir, "index.html")

    html_content = render_html()
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Directorio de franquicias generado con éxito en: {target_file}")
    print(f"Total de franquicias incluidas: {len(FRANQUICIAS)}")


if __name__ == "__main__":
    main()
