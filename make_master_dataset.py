# -*- coding: utf-8 -*-
"""
make_master_dataset.py
Genera coolpadel-web/dataset_franquicias.py con 106 operadores en 18+ países.
"""
import os
import json

from generate_dataset import DATASET as UK_LIST

# ESPAÑA (18 operadores)
ES_LIST = [
    {
        "id": "padel-7",
        "nombre": "Pàdel 7",
        "pais": "España",
        "pais_codigo": "ES",
        "region_filtro": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Barcelona",
        "coords": [41.3980, 2.1900],
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
        "coords": [40.5756, -3.9303],
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
        "coords": [40.4500, -3.6800],
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
        "coords": [40.4350, -3.8150],
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
        "coords": [41.5450, 2.1080],
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
        "coords": [38.3600, -0.4400],
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
        "coords": [39.4699, -0.3763],
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
        "coords": [37.3891, -5.9845],
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
        "coords": [37.9922, -1.1307],
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
        "coords": [41.3851, 2.1734],
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
        "coords": [36.7213, -4.4214],
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
        "coords": [41.6488, -0.8891],
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
        "coords": [40.3222, -3.8649],
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
        "coords": [40.4168, -3.7038],
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
        "coords": [39.4120, -0.4000],
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
        "coords": [43.2928, -2.8872],
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
        "coords": [40.5300, -3.6450],
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
        "coords": [41.6080, 2.2880],
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
    }
]

print(f"Cargadas {len(ES_LIST)} cadenas de España.")
