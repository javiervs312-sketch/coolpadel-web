# -*- coding: utf-8 -*-
"""
dataset_rest_europe.py
Cadenas multiclub y franquicias de Francia, Italia, Benelux, DACH, Países Nórdicos y Portugal.
"""

FR_LIST = [
    {
        "id": "all-in-padel",
        "nombre": "All In Padel",
        "pais": "Francia",
        "pais_codigo": "FR",
        "region_filtro": "FR",
        "bandera": "🇫🇷",
        "ciudad_sede": "Lyon / Grasse",
        "coords": [45.7640, 4.8357],
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
        "coords": [48.8566, 2.3522],
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
        "coords": [50.6292, 3.0573],
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
        "coords": [49.1828, -0.3707],
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
        "coords": [48.9200, 2.3600],
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
        "coords": [48.7711, 2.5233],
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
        "coords": [43.6047, 1.4442],
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
        "coords": [45.6961, 4.9450],
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
        "coords": [43.6261, 7.0722],
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
        "coords": [43.4350, 5.3400],
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
        "coords": [43.5283, 3.9317],
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
        "coords": [48.8319, 2.2778],
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
    }
]

print(f"Cargadas {len(FR_LIST)} cadenas de Francia.")


# =========================================================================
# 🇮🇹 ITALIA (10 Cadenas y Franquicias)
# =========================================================================
IT_LIST = [
    {
        "id": "spector-padel-house",
        "nombre": "Spector Padel House (SPH)",
        "pais": "Italia",
        "pais_codigo": "IT",
        "region_filtro": "IT",
        "bandera": "🇮🇹",
        "ciudad_sede": "Milano / Firenze / Venezia",
        "coords": [45.4642, 9.1900],
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
        "coords": [45.5786, 9.1258],
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
        "coords": [45.4950, 9.2150],
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
        "coords": [45.4780, 9.1550],
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
        "coords": [45.4642, 9.1900],
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
        "coords": [45.3600, 9.1600],
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
        "coords": [43.9100, 12.9100],
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
        "coords": [41.9028, 12.4964],
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
        "coords": [41.8300, 12.4700],
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
        "coords": [45.4064, 11.8768],
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
    }
]

print(f"Cargadas {len(IT_LIST)} cadenas de Italia.")


# =========================================================================
# 🇳🇱 BÉLGICA Y PAÍSES BAJOS (9 Cadenas y Franquicias)
# =========================================================================
BE_NL_LIST = [
    {
        "id": "arenal-padel",
        "nombre": "Arenal Padel",
        "pais": "Bélgica",
        "pais_codigo": "BE",
        "region_filtro": "NL",
        "bandera": "🇧🇪",
        "ciudad_sede": "Mechelen / Brugge / Antwerpen",
        "coords": [51.0257, 4.4776],
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
        "coords": [51.0543, 3.7174],
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
        "coords": [52.3676, 4.9041],
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
        "coords": [52.3370, 4.9200],
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
        "coords": [52.3700, 4.8900],
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
        "coords": [51.0500, 3.7300],
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
        "coords": [52.3000, 4.8600],
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
        "coords": [52.3750, 4.8500],
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
        "coords": [50.9300, 5.3300],
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
    }
]

print(f"Cargadas {len(BE_NL_LIST)} cadenas de Benelux.")


# =========================================================================
# 🇩🇪 DACH: ALEMANIA, AUSTRIA Y SUIZA (9 Cadenas y Franquicias)
# =========================================================================
DACH_LIST = [
    {
        "id": "padelzone-austria",
        "nombre": "PadelZone Austria",
        "pais": "Austria",
        "pais_codigo": "AT",
        "region_filtro": "DE",
        "bandera": "🇦🇹",
        "ciudad_sede": "Viena / Graz / Wiener Neustadt",
        "coords": [48.2082, 16.3738],
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
        "coords": [48.1900, 16.4100],
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
        "coords": [48.1351, 11.5820],
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
        "coords": [50.9375, 6.9603],
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
        "coords": [51.2277, 6.7735],
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
        "coords": [48.1400, 11.5700],
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
        "coords": [46.2044, 6.1432],
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
        "coords": [47.5596, 7.5886],
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
        "coords": [47.5186, 8.5408],
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
    }
]

print(f"Cargadas {len(DACH_LIST)} cadenas de DACH.")


# =========================================================================
# 🇸🇪 ESCANDINAVIA Y PAÍSES NÓRDICOS (14 Cadenas y Franquicias)
# =========================================================================
NORDIC_LIST = [
    {
        "id": "interpadel-norway",
        "nombre": "InterPadel Norway",
        "pais": "Noruega",
        "pais_codigo": "NO",
        "region_filtro": "SE",
        "bandera": "🇳🇴",
        "ciudad_sede": "Oslo / Bergen / Stavanger",
        "coords": [59.9139, 10.7522],
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
        "coords": [58.1599, 8.0182],
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
        "coords": [59.7400, 10.4200],
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
        "coords": [55.4038, 10.4024],
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
        "coords": [55.6761, 12.5683],
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
        "coords": [55.6700, 12.6000],
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
        "coords": [57.0488, 9.9217],
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
        "coords": [59.3293, 18.0686],
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
        "coords": [59.3350, 18.0500],
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
        "coords": [57.7089, 11.9746],
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
        "coords": [59.2900, 18.0300],
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
        "coords": [60.2055, 24.6559],
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
        "coords": [60.1900, 24.9600],
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
        "coords": [60.1700, 24.9400],
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
    }
]

print(f"Cargadas {len(NORDIC_LIST)} cadenas de Países Nórdicos.")

# =========================================================================
# 🇵🇹 PORTUGAL (4 Cadenas y Franquicias)
# =========================================================================
PT_LIST = [
    {
        "id": "rackets-pro",
        "nombre": "Rackets Pro",
        "pais": "Portugal",
        "pais_codigo": "PT",
        "region_filtro": "PT",
        "bandera": "🇵🇹",
        "ciudad_sede": "Lisboa (EUL)",
        "coords": [38.7550, -9.1580],
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
        "coords": [41.1579, -8.6291],
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
        "coords": [38.7555, -9.1550],
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
        "coords": [41.5454, -8.4265],
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
    }
]

print(f"Cargadas {len(PT_LIST)} cadenas de Portugal.")
