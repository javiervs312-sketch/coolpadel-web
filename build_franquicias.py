#!/usr/bin/env python3
"""
Generador Maestro del Directorio Global de Franquicias y Cadenas de Pádel (+1 Club)
para CoolPadel Studios (https://coolpadelstudios.com/franquicias-padel/).

Censo exhaustivo de 67 cadenas de clubes con varias sedes abiertas bajo el mismo nombre
y franquicias de pádel en 18 países:
España, Francia, Italia, Portugal, Suecia, Noruega, Dinamarca, Finlandia,
Países Bajos, Bélgica, Alemania, Austria, Reino Unido, Estados Unidos, México,
Chile, Argentina, Brasil, Emiratos Árabes Unidos, Catar y Kuwait.
"""

import os
import json
import urllib.parse
from datetime import datetime

FRANQUICIAS = [
    # ─────────────────────────────────────────────────────────────
    # 🇪🇸 ESPAÑA (13 Cadenas y Franquicias)
    # ─────────────────────────────────────────────────────────────
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
        "id": "padel-people",
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
        "diferencial": "Excelente reputación formativa en la sierra de Madrid y ambiente familiar y acogedor."
    },
    {
        "id": "forus-padel",
        "nombre": "Forus Padel",
        "pais": "España y Portugal",
        "pais_codigo": "ES",
        "region_filtro": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Madrid",
        "coords": [40.4500, -3.6800],
        "modelo": "Cadena de Complejos Multideporte y Pádel",
        "modelo_badge": "bg-blue-100 text-blue-800 border-blue-200",
        "tipo_categoria": "corporativo",
        "escala": "mega",
        "num_clubs": "15+ centros con pádel bajo la misma marca",
        "num_pistas": "50+ pistas",
        "software": "Resasports / Playtomic",
        "fundadores": "Ignacio Triana (Forus Deporte y Ocio)",
        "web": "https://forus.es",
        "tagline": "Uno de los mayores operadores deportivos de la península ibérica.",
        "resumen": "Forus opera más de 60 centros en España, Portugal e Italia. En más de 15 de sus mayores complejos cuenta con secciones especializadas de pádel con múltiples pistas cubiertas y exteriores bajo la misma marca Forus, combinando el pádel con gimnasio, spa y piscinas.",
        "sedes_principales": [
            "Forus Chamartín (Madrid)",
            "Forus Alcalá de Henares (Madrid)",
            "Forus Coslada (Madrid)",
            "Forus Jaén (Andalucía)",
            "Forus Elche (Alicante)",
            "Forus Segovia, Forus Valencia y centros en Oporto (Portugal)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de cristal y césped sintético",
            "software": "Resasports y Playtomic",
            "domotica": "Tornos de acceso con pulsera RFID para abonados",
            "grabacion": "Grabación en finales de ligas internas",
            "restauracion": "Cafeterías Forus con menús saludables para deportistas"
        },
        "modelo_expansion": {
            "tipo_contrato": "Concesiones administrativas a 25-40 años y centros privados",
            "perfil_club": "Macrocomplejos de ocio y fitness con área de raqueta",
            "canon_royalties": "Operador institucional",
            "inversion_media": "3M€ a 7M€ por complejo deportivo"
        },
        "diferencial": "Alianza con ayuntamientos y más de 200.000 abonados en su red que alimentan las pistas de pádel."
    },
    {
        "id": "bamvolea",
        "nombre": "BamVolea",
        "pais": "España",
        "pais_codigo": "ES",
        "region_filtro": "ES",
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
        "resumen": "Nacido de la integración de centros de Olympia Sports, Ciudad de la Raqueta (Madrid) y Sportcity (Valencia), BamVolea es el mayor gigante de la gestión deportiva en España. Centraliza compras, patrocinios y su circuito 'BamVolea Tour', asociándose a clubes consolidados de más de 10-15 pistas.",
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
            "domotica": "Control centralizado, climatización industrial y control de iluminación",
            "grabacion": "Sistemas de streaming para pistas centrales y eventos federados",
            "restauracion": "Grandes restaurantes, terrazas lounge y sports bars de alta facturación"
        },
        "modelo_expansion": {
            "tipo_contrato": "Adquisición, integración patrimonial o gestión delegada de grandes complejos",
            "perfil_club": "Clubes consolidados de más de 10-15 pistas con alta ocupación y área social/restauración",
            "canon_royalties": "No es franquicia abierta minorista; operan como grupo corporativo y fondo de inversión",
            "inversion_media": "Macrocomplejos de 1M€ a 5M€ de valoración patrimonial"
        },
        "diferencial": "Poder de negociación masivo, circuito propio 'BamVolea Tour' y academias oficiales de Paquito Navarro y Feliciano López."
    },
    {
        "id": "aurial-padel",
        "nombre": "Aurial Padel by Marta Marrero",
        "pais": "España",
        "pais_codigo": "ES",
        "region_filtro": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Sant Cugat del Vallès (Barcelona)",
        "coords": [41.4674, 2.0818],
        "modelo": "Cadena Multiclub Boutique (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "7+ centros con el mismo nombre",
        "num_pistas": "85+ pistas",
        "software": "Playtomic",
        "fundadores": "Marta Marrero (ex Nº 1 mundial), Jon Grau, Daniel Osés",
        "web": "https://aurialpadel.com",
        "tagline": "Clubes de pádel experienciales de alta gama con metodología de Nº 1 del mundo.",
        "resumen": "Cadena de clubes bajo el mismo nombre Aurial Padel en Cataluña. Combina pistas de competición con gimnasios boutique, su propia marca gastronómica 'Desbario' y la Aurial Padel Academy.",
        "sedes_principales": [
            "Aurial Augusta Sant Cugat (Sant Cugat, Barcelona - 14 pistas)",
            "Aurial Pàdel Cornellà (Cornellà, Barcelona - 14 pistas)",
            "Aurial Indoor Padel Sabadell (Sabadell - centro indoor y Academy)",
            "Aurial Vic, Aurial Lleida, Aurial Terrassa, Aurial Reus",
            "Expansión internacional: Proyectos en Bratislava (Eslovaquia)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas WPT panorámicas con césped texturizado de competición",
            "software": "Playtomic para la gestión integral de reservas",
            "domotica": "Instalaciones ecoeficientes con climatización inteligente e iluminación LED",
            "grabacion": "Sistemas de vídeo en pista para tecnificación y clínics",
            "restauracion": "Restaurantes 'Desbario': gastronomía cuidada, menú saludable y cócteles"
        },
        "modelo_expansion": {
            "tipo_contrato": "Gestión directa corporativa bajo la misma enseña",
            "perfil_club": "Instalaciones de alto nivel de 8 a 15 pistas con espacio para gimnasio y restaurante",
            "canon_royalties": "Acuerdos individualizados de marca y metodología",
            "inversion_media": "600.000€ a 1.800.000€"
        },
        "diferencial": "Metodología directa de Marta Marrero, diseño arquitectónico impecable y restauración propia de alto margen."
    },
    {
        "id": "bela-padel-center",
        "nombre": "Bela Padel Center",
        "pais": "España, Argentina e Internacional",
        "pais_codigo": "ES",
        "region_filtro": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Barcelona",
        "coords": [41.3879, 2.1699],
        "modelo": "Cadena de Centros Insignia (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "4 centros con el mismo nombre",
        "num_pistas": "45+ pistas",
        "software": "Playtomic",
        "fundadores": "Fernando Belasteguín (16 años Nº 1 del mundo), One16 Sports",
        "web": "https://belapadelcenter.com",
        "tagline": "La escuela y templo del mayor jugador de la historia del pádel.",
        "resumen": "Grandes clubes propios de alta gama (BPC Barcelona con 20 pistas, BPC Alicante con 14) combinados con la exportación internacional de su metodología Bela-Sciorilli a clubes licenciatarios en Argentina, México e Italia.",
        "sedes_principales": [
            "Bela Padel Center Barcelona (20 pistas indoor/outdoor)",
            "Bela Padel Center Alicante (Playa de San Juan - 14 pistas)",
            "Bela Padel Center Buenos Aires (Argentina)",
            "Centros licenciados en expansión en México y Oriente Medio"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de competición con césped texturizado azul",
            "software": "Playtomic para gestión de reservas y ligas",
            "domotica": "Domótica de control de iluminación y climatización de pistas",
            "grabacion": "Cámaras en pistas dedicadas para corrección biomecánica y clínics",
            "restauracion": "Clubhouse con tienda oficial Wilson x Bela y cafetería deportiva"
        },
        "modelo_expansion": {
            "tipo_contrato": "Licencia metodológica Bela Padel Academy y franquicia de marca",
            "perfil_club": "Clubes de más de 8 pistas con vocación formativa y alto estándar",
            "canon_royalties": "Canon de marca anual + royalty por alumnos en escuela",
            "inversion_media": "600.000€ a 1.500.000€"
        },
        "diferencial": "El prestigio inigualable de Fernando Belasteguín y su alianza estratégica global con Wilson."
    },
    {
        "id": "click-and-padel",
        "nombre": "Click & Padel / Padel Time Sport",
        "pais": "España",
        "pais_codigo": "ES",
        "region_filtro": "ES",
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
        "fundadores": "Pioneros de la domótica deportiva en España",
        "web": "https://clickandpadel.com",
        "tagline": "El modelo de club desatendido que reduce el 70% del coste operativo.",
        "resumen": "Naves de 2 a 4 pistas que operan 365 días al año sin recepcionista. El usuario reserva por app, recibe un código QR que abre puertas, enciende las luces 5 min antes y activa climatización. Venta robotizada de bolas y palas.",
        "sedes_principales": [
            "Centros en Castilla-La Mancha (Albacete, Hellín, La Roda)",
            "Comunidad Valenciana y Murcia",
            "Implantaciones periurbanas en Andalucía"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas reforzadas con estructura de acero autoportante",
            "software": "Motor domótico conectado vía API con Playtomic y pasarelas bancarias",
            "domotica": "Cerraduras electromagnéticas, relés IoT para iluminación LED, climatización temporizada",
            "grabacion": "Circuito cerrado CCTV 24h conectado a Central Receptora de Alarmas",
            "restauracion": "Vending robotizado de bebidas isotónicas, bolas y accesorios"
        },
        "modelo_expansion": {
            "tipo_contrato": "Franquicia llave en mano para inversores patrimoniales",
            "perfil_club": "Naves industriales en polígonos o parcelas de 1.000 a 2.500 m²",
            "canon_royalties": "Canon de entrada ~15.000€ y royalty técnico del 4%",
            "inversion_media": "180.000€ a 350.000€ (payback estimado en 3-4 años)"
        },
        "diferencial": "Margen neto superior al 55% sobre facturación gracias a la eliminación casi total del coste de personal."
    },
    {
        "id": "paquito-navarro-academy",
        "nombre": "Paquito Navarro Academy / PSA",
        "pais": "España e Internacional",
        "pais_codigo": "ES",
        "region_filtro": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Sevilla / Madrid",
        "coords": [37.3891, -5.9845],
        "modelo": "Franquicia de Academia y Metodología",
        "modelo_badge": "bg-amber-100 text-amber-800 border-amber-200",
        "tipo_categoria": "licencia",
        "escala": "media",
        "num_clubs": "12+ clubes afiliados",
        "num_pistas": "60+ pistas asociadas",
        "software": "Plataforma de Gestión de Escuela",
        "fundadores": "Paquito Navarro (Campeón del Mundo)",
        "web": "https://paquitonavarroacademy.com",
        "tagline": "La metodología ganadora del jugador más carismático del planeta.",
        "resumen": "Permite a clubes existentes franquiciar su escuela oficial con el sello de Paquito Navarro para llenar horas valle (mañanas y tardes iniciales). Metodología formativa, formación de monitores y clínics presenciales.",
        "sedes_principales": [
            "Centros adheridos en Madrid (integrado en BamVolea)",
            "Andalucía (Sevilla, Málaga)",
            "Centros homologados en Italia, Kuwait, México y Suecia"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas homologadas según estándares de la FIP",
            "software": "Plataforma de seguimiento de progresión técnica para alumnos y familias",
            "domotica": "Cobro recurrente de cuotas de escuela automatizado",
            "grabacion": "Uso de vídeo para análisis y corrección de golpes en pista",
            "restauracion": "Co-branding con el restaurante del club"
        },
        "modelo_expansion": {
            "tipo_contrato": "Franquicia y licencia con exclusividad de zona geográfica",
            "perfil_club": "Clubes de 6 a 15 pistas que deseen potenciar su escuela con más de 150 alumnos",
            "canon_royalties": "Canon de entrada (12.000€ - 25.000€) y cuota mensual por alumno",
            "inversion_media": "Inversión inicial muy baja (15.000€ - 40.000€) al montarse sobre clubes ya operativos"
        },
        "diferencial": "Atracción inmediata de alumnos por la imagen de Paquito Navarro y material técnico Bullpadel."
    },
    {
        "id": "club-padel-nuestro",
        "nombre": "Club Padel Nuestro (Pro-Shops & Corners)",
        "pais": "España e Internacional",
        "pais_codigo": "ES",
        "region_filtro": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Murcia",
        "coords": [37.9922, -1.1307],
        "modelo": "Franquicia de Retail y Pro-Shops para Clubes",
        "modelo_badge": "bg-amber-100 text-amber-800 border-amber-200",
        "tipo_categoria": "licencia",
        "escala": "mega",
        "num_clubs": "45+ tiendas físicas / 120+ clubes",
        "num_pistas": "500+ pistas asociadas",
        "software": "ERP Pádel Nuestro / TPV Integrado",
        "fundadores": "Grupo Pádel Nuestro (Líder mundial de distribución)",
        "web": "https://clubpadelnuestro.com",
        "tagline": "La mayor central de compras y red de tiendas de pádel del mundo para clubes.",
        "resumen": "Resuelve la gestión comercial de la tienda del club. El club instala un corner oficial con acceso directo a miles de referencias (Bullpadel, Siux, Nox, Head, Babolat) con condiciones de central de compras.",
        "sedes_principales": [
            "España: Tiendas en Madrid, Barcelona, Valencia, Murcia, Sevilla, Bilbao",
            "Portugal: Lisboa, Oporto",
            "Italia: Milán, Roma",
            "Presencia en Suecia, Francia y Países Bajos"
        ],
        "tecnologia_pistas": {
            "pistas": "Compatible con cualquier instalación deportiva",
            "software": "TPV conectado en tiempo real con el stock del almacén central",
            "domotica": "Sistemas antirrobo y expositores con palas de prueba",
            "grabacion": "Zonas de test de palas en pista",
            "restauracion": "Sinergia con el mostrador de recepción"
        },
        "modelo_expansion": {
            "tipo_contrato": "Franquicia de retail en formato Corner (15-30 m²) o Tienda Completa (50-150 m²)",
            "perfil_club": "Clubes de más de 6 pistas y afluencia mínima de 300 jugadores semanales",
            "canon_royalties": "Canon de entrada reducido (6.000€ - 12.000€) y margen comercial garantizado",
            "inversion_media": "30.000€ a 60.000€ para mobiliario y stock inicial"
        },
        "diferencial": "Disponibilidad del 100% de marcas mundiales sin negociar una a una y Click & Collect."
    },
    {
        "id": "duet-sports-padel",
        "nombre": "Duet Sports / Duet Padel",
        "pais": "España",
        "pais_codigo": "ES",
        "region_filtro": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Barcelona",
        "coords": [41.3851, 2.1734],
        "modelo": "Cadena Multideporte y Pádel en Concesión",
        "modelo_badge": "bg-blue-100 text-blue-800 border-blue-200",
        "tipo_categoria": "corporativo",
        "escala": "media",
        "num_clubs": "10+ complejos con pádel",
        "num_pistas": "65+ pistas",
        "software": "Resasports / Playtomic",
        "fundadores": "Grupo Duet",
        "web": "https://duetsports.com",
        "tagline": "Operador consolidado de grandes complejos municipales y privados de fitness y pádel.",
        "resumen": "Cadena histórica de complejos deportivos en Cataluña, Baleares y Madrid. Integra pistas de pádel cubiertas y exteriores junto a grandes gimnasios y piscinas, generando una base de decenas de miles de abonados cruzados.",
        "sedes_principales": [
            "Duet Pàdel Las Rozas (Madrid)",
            "Duet Sports Rubí (Barcelona)",
            "Duet Sports Sant Boi (Barcelona)",
            "Duet Portitxol (Palma de Mallorca)",
            "Duet Sports Tiana y Esplugues"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de cristal templado y césped monofilamento azul",
            "software": "Resasports integrado con tornos de acceso biométrico",
            "domotica": "Iluminación automatizada ligada a la ficha de reserva",
            "grabacion": "Grabación de partidos de liga social",
            "restauracion": "Cafeterías saludables y zonas wellness con spa"
        },
        "modelo_expansion": {
            "tipo_contrato": "Concesiones administrativas municipales a 25-40 años y centros propios",
            "perfil_club": "Complejos deportivos integrales de más de 5.000 m²",
            "canon_royalties": "Gestión corporativa",
            "inversion_media": "3M€ a 8M€ por complejo multideporte"
        },
        "diferencial": "Cross-selling masivo: sus usuarios de fitness se convierten en jugadores de pádel regulares."
    },
    {
        "id": "vals-sport",
        "nombre": "Vals Sport",
        "pais": "España",
        "pais_codigo": "ES",
        "region_filtro": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Málaga",
        "coords": [36.7213, -4.4214],
        "modelo": "Cadena Multiclub Provincial (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "5 grandes complejos con el mismo nombre",
        "num_pistas": "35+ pistas",
        "software": "Playtomic",
        "fundadores": "Grupo Vals Sport Málaga",
        "web": "https://valssport.com",
        "tagline": "El operador deportivo de referencia en la Costa del Sol y la provincia de Málaga.",
        "resumen": "Vals Sport es el dominador del pádel y la raqueta en Málaga. Con cinco grandes centros bajo la misma marca Vals Sport en la capital, vertebran la mayor liga interclubes de Andalucía y escuelas formativas con cientos de alumnos.",
        "sedes_principales": [
            "Vals Sport Cónsul (Teatinos - 10 pistas de pádel + fitness)",
            "Vals Sport Teatinos (Málaga)",
            "Vals Sport Churriana (Málaga)",
            "Vals Sport Ave María (Málaga)",
            "Vals Sport Ciudad Jardín"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas de cristal con iluminación LED y cubiertas térmicas",
            "software": "Playtomic para torneos abiertos y reservas libres",
            "domotica": "Acceso con pulsera RFID para socios",
            "grabacion": "Pistas centrales preparadas para torneos de la Federación Andaluza",
            "restauracion": "Restaurantes con terrazas exteriores y menús deportivos"
        },
        "modelo_expansion": {
            "tipo_contrato": "Concesiones de parcelas deportivas públicas y recintos propios",
            "perfil_club": "Centros polideportivos de 6 a 12 pistas con piscina y gimnasio",
            "canon_royalties": "Operación directa",
            "inversion_media": "1M€ a 3M€ por complejo"
        },
        "diferencial": "Monopolio de comunidad en Málaga capital: todo el aficionado malagueño juega en Vals Sport."
    },
    {
        "id": "padel-indoor-aragon",
        "nombre": "Pádel Indoor Aragón / Pádel Zaragoza",
        "pais": "España",
        "pais_codigo": "ES",
        "region_filtro": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Zaragoza",
        "coords": [41.6488, -0.8891],
        "modelo": "Red de Macrocomplejos Cubiertos",
        "modelo_badge": "bg-blue-100 text-blue-800 border-blue-200",
        "tipo_categoria": "corporativo",
        "escala": "media",
        "num_clubs": "3 macrocomplejos",
        "num_pistas": "40+ pistas",
        "software": "Playtomic",
        "fundadores": "Operadores pioneros del pádel indoor en el Valle del Ebro",
        "web": "https://padelindooraragon.com",
        "tagline": "Los pioneros del pádel indoor en Aragón con instalaciones de escala monumental.",
        "resumen": "Aragón sufre inviernos gélidos y veranos tórridos con cierzo constante. Esta red de macrocomplejos indoor climatizados (Pádel Indoor Aragón, Pádel Zaragoza y centros asociados) concentra más de 40 pistas cubiertas de gran altura.",
        "sedes_principales": [
            "Pádel Indoor Aragón (Cuarte de Huerva, Zaragoza - 14 pistas indoor)",
            "Pádel Zaragoza (14 pistas cubiertas y semicubiertas)",
            "Pádel Plaza Indoor (Plataforma Logística PLA-ZA, Zaragoza - 12 pistas)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas indoor protegidas contra el cierzo con 10 metros de altura libre",
            "software": "Playtomic",
            "domotica": "Sistemas de calefacción radiante industrial para el invierno",
            "grabacion": "Grabación de finales del circuito aragonés",
            "restauracion": "Grandes zonas de restauración con menú del día y asados"
        },
        "modelo_expansion": {
            "tipo_contrato": "Consolidación de naves logísticas e industriales de gran formato",
            "perfil_club": "Naves de más de 4.000 m² con techos sin vigas intermedias",
            "canon_royalties": "Operador integrado",
            "inversion_media": "800.000€ a 1.500.000€"
        },
        "diferencial": "Instalaciones 100% blindadas climáticamente con altísima ocupación en meses invernales."
    },
    {
        "id": "padel-dos-cero",
        "nombre": "Pádel 2.0",
        "pais": "España",
        "pais_codigo": "ES",
        "region_filtro": "ES",
        "bandera": "🇪🇸",
        "ciudad_sede": "Móstoles (Madrid)",
        "coords": [40.3232, -3.8649],
        "modelo": "Cadena Multiclub Indoor (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "boutique",
        "num_clubs": "2 centros con el mismo nombre",
        "num_pistas": "18+ pistas",
        "software": "Playtomic",
        "fundadores": "Entrenadores y promotores madrileños",
        "web": "https://padeldospuntocero.com",
        "tagline": "Clubes indoor de alto rendimiento y tecnificación en el sur de Madrid.",
        "resumen": "Pádel 2.0 es uno de los clubes más respetados de la Comunidad de Madrid por el altísimo nivel de sus escuelas y torneos. Pistas cubiertas con el mismo nombre Pádel 2.0 en Móstoles y Alcorcón, cuidadas al milímetro.",
        "sedes_principales": [
            "Pádel 2.0 Móstoles (Madrid - 9 pistas indoor)",
            "Pádel 2.0 Alcorcón (Madrid - 9 pistas indoor)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas de competición con arena de sílice invisible y moqueta texturizada",
            "software": "Playtomic",
            "domotica": "Control automático de acceso y climatización de naves",
            "grabacion": "Cámaras para análisis técnico de pádel profesional",
            "restauracion": "Bar deportivo con comidas rápidas y venta de material"
        },
        "modelo_expansion": {
            "tipo_contrato": "Operación propia bajo marca unificada",
            "perfil_club": "Naves en polígonos del área metropolitana de Madrid de 8 a 10 pistas",
            "canon_royalties": "Gestión directa",
            "inversion_media": "500.000€ a 900.000€"
        },
        "diferencial": "Nivel de juego medio-alto: es la cantera de decenas de jugadores que compiten en previas de Premier Padel."
    },

    # ─────────────────────────────────────────────────────────────
    # 🇫🇷 FRANCIA (7 Cadenas y Franquicias)
    # ─────────────────────────────────────────────────────────────
    {
        "id": "all-in-padel",
        "nombre": "All In Padel (Jo-Wilfried Tsonga)",
        "pais": "Francia",
        "pais_codigo": "FR",
        "region_filtro": "FR",
        "bandera": "🇫🇷",
        "ciudad_sede": "Lyon / Grasse",
        "coords": [45.7640, 4.8357],
        "modelo": "Cadena de Clubs de Alto Nivel (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "6 complejos con el mismo nombre",
        "num_pistas": "40+ pistas",
        "software": "Doinsport",
        "fundadores": "Jo-Wilfried Tsonga (ex Top 5 ATP) y Thierry Ascione (All In Group)",
        "web": "https://allin-padel.com",
        "tagline": "La cadena de pádel de élite creada por leyendas del tenis francés.",
        "resumen": "All In Group es una potencia deportiva en Francia fundada por el extenista Jo-Wilfried Tsonga y Thierry Ascione. Cuentan con centros de pádel premium bajo la enseña All In Padel en Lyon OL Vallée (junto al estadio del Olympique de Lyon), Grasse en la Costa Azul, Mougins, Mâcon, Villefranche y Portes-lès-Valence.",
        "sedes_principales": [
            "All In Country Club Lyon (OL Vallée, Décines - macrocomplejo de pádel y tenis)",
            "All In Padel Grasse (Côte d'Azur - uno de los mayores complejos de Francia)",
            "All In Padel Mougins (Grasse)",
            "All In Padel Mâcon",
            "All In Padel Villefranche-sur-Saône",
            "All In Padel Portes-lès-Valence"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas cubiertas y exteriores con moqueta WPT de alta densidad",
            "software": "Doinsport",
            "domotica": "Acceso digitalizado, climatización y domótica de iluminación",
            "grabacion": "Cámaras profesionales para tecnificación y streaming",
            "restauracion": "Bistrot deportivo con cocina gourmet francesa, spa, piscina y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Desarrollo propio del grupo All In bajo la misma marca",
            "perfil_club": "Macrocomplejos de raqueta de más de 6 a 12 pistas con academia",
            "canon_royalties": "Cadena propia",
            "inversion_media": "1M€ a 3M€ por complejo"
        },
        "diferencial": "El carisma e implicación de Jo-Wilfried Tsonga y estándares dignos del circuito ATP/Premier Padel."
    },
    {
        "id": "casa-padel",
        "nombre": "Casa Padel",
        "pais": "Francia",
        "pais_codigo": "FR",
        "region_filtro": "FR",
        "bandera": "🇫🇷",
        "ciudad_sede": "París (Saint-Denis / Asnières)",
        "coords": [48.9244, 2.3431],
        "modelo": "Cadena Multiclub Urbana (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "boutique",
        "num_clubs": "2 centros emblemáticos",
        "num_pistas": "18+ pistas",
        "software": "Doinsport",
        "fundadores": "Loïc Le Panse y socios parisinos",
        "web": "https://casapadel.fr",
        "tagline": "Pioneros del pádel indoor en el norte de París con gastronomía mediterránea.",
        "resumen": "Casa Padel abrió en Saint-Denis el primer macrocomplejo cubierto del Gran París (12 pistas indoor). Posteriormente ampliaron la marca a Casa Padel Dos en Asnières-sur-Seine. Se distinguen por su restaurante mediterráneo, salas de osteopatía y torneos de empresas.",
        "sedes_principales": [
            "Casa Padel Uno (Saint-Denis, París - 12 pistas indoor)",
            "Casa Padel Dos (Asnières-sur-Seine, París - 6 pistas cubiertas)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas cubiertas con 10 metros de altura libre",
            "software": "Doinsport",
            "domotica": "Control digital de iluminación y clima",
            "grabacion": "Cámaras de streaming para torneos FFT",
            "restauracion": "Restaurante de cocina española e italiana, terraza y espacio wellness"
        },
        "modelo_expansion": {
            "tipo_contrato": "Operación directa",
            "perfil_club": "Naves periurbanas de gran tamaño conectadas con el metro de París",
            "canon_royalties": "Propiedad privada",
            "inversion_media": "1M€ a 2M€"
        },
        "diferencial": "Marca de culto en París por ser la pionera y por su ambiente festivo tras el partido."
    },
    {
        "id": "esprit-padel",
        "nombre": "Esprit Padel",
        "pais": "Francia",
        "pais_codigo": "FR",
        "region_filtro": "FR",
        "bandera": "🇫🇷",
        "ciudad_sede": "Lyon (Saint-Priest)",
        "coords": [45.6960, 4.9450],
        "modelo": "Cadena Multiclub de Especialidad (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "boutique",
        "num_clubs": "2 centros con el mismo nombre",
        "num_pistas": "14+ pistas",
        "software": "Doinsport",
        "fundadores": "Sébastien Cornet",
        "web": "https://espritpadel.com",
        "tagline": "El club cubierto de pura pasión y escuela de competición en la región de Lyon.",
        "resumen": "Cadena lionesa dedicada al pádel cubierto. Su centro en Saint-Priest es un referente nacional francés por la calidad de su escuela, su bistrot con productos frescos locales y sus torneos P1000 y P2000.",
        "sedes_principales": [
            "Esprit Padel Lyon (Saint-Priest - 8 pistas indoor)",
            "Esprit Padel Lyon 2 (centro anexo)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas cubiertas con moqueta azul de competición",
            "software": "Doinsport",
            "domotica": "Gestión automática de iluminación",
            "grabacion": "Cámaras de partido y corrección en pista",
            "restauracion": "Bistrot gastronómico con platos caseros y cervezas de barril"
        },
        "modelo_expansion": {
            "tipo_contrato": "Operación directa",
            "perfil_club": "Naves de 6 a 10 pistas en el área metropolitana de Lyon",
            "canon_royalties": "Gestión directa",
            "inversion_media": "600.000€ a 1.200.000€"
        },
        "diferencial": "Fuerte identidad comunitaria y el club con mayor ratio de fidelidad de jugadores de Lyon."
    },
    {
        "id": "4padel",
        "nombre": "4PADEL (Groupe LE FIVE)",
        "pais": "Francia",
        "pais_codigo": "FR",
        "region_filtro": "FR",
        "bandera": "🇫🇷",
        "ciudad_sede": "París",
        "coords": [48.9100, 2.3300],
        "modelo": "Cadena Multiclub Líder (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "grande",
        "num_clubs": "22+ centros con el mismo nombre",
        "num_pistas": "135+ pistas",
        "software": "Doinsport / My4Padel",
        "fundadores": "Damien Pelle, Guillaume Debelmas, Joseph Viéville",
        "web": "https://4padel.fr",
        "tagline": "El líder indiscutible del pádel indoor en Francia con ADN deportivo y festivo.",
        "resumen": "División de pádel de LE FIVE, líder del fútbol 5 en Francia. 22 centros operativos todos con la misma marca 4PADEL: Burdeos, Estrasburgo, Toulouse, Ruan, París. Pistas Babolat oficiales y torneos homologados FFT P100 a P2000.",
        "sedes_principales": [
            "4PADEL Estrasburgo (14 pistas indoor)",
            "4PADEL Burdeos (Bordeaux-Lac - 7 pistas)",
            "4PADEL Toulouse-Colomiers (11 pistas)",
            "4PADEL París-Marville y Montreuil",
            "4PADEL Ruan, Limoges, Metz, Valenciennes, Dunkerque"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas Babolat de última generación, césped texturizado y pistas individuales",
            "software": "App My4Padel sobre motor Doinsport",
            "domotica": "Marcadores digitales y control de pistas",
            "grabacion": "Sistemas de vídeo en pista para descarga de highlights",
            "restauracion": "Sports Bar con cervezas artesanales y pantallas para partidos"
        },
        "modelo_expansion": {
            "tipo_contrato": "Explotación propia bajo la misma marca 4PADEL",
            "perfil_club": "Superficies de 2.500 a 5.000 m² con techos de más de 8 metros",
            "canon_royalties": "Operador integrado",
            "inversion_media": "1M€ a 2.5M€ por complejo"
        },
        "diferencial": "Sinergia con los miles de futbolistas de LE FIVE y ambiente social inmejorable."
    },
    {
        "id": "urbanpadel",
        "nombre": "UrbanPadel (Groupe UrbanSoccer)",
        "pais": "Francia",
        "pais_codigo": "FR",
        "region_filtro": "FR",
        "bandera": "🇫🇷",
        "ciudad_sede": "París",
        "coords": [48.8566, 2.3522],
        "modelo": "Cadena Multiclub Urbana (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "16+ centros con el mismo nombre",
        "num_pistas": "75+ pistas",
        "software": "UrbanPadel App",
        "fundadores": "UrbanSoccer (Compagnie des Alpes)",
        "web": "https://urbanpadel.fr",
        "tagline": "El gigante francés del fútbol reducido llevando el pádel a las periferias urbanas.",
        "resumen": "Brazo de pádel de UrbanSoccer con 16 centros todos con la marca UrbanPadel: Lille, Lyon, Nantes, Puteaux. Pistas cubiertas dentro de sus complejos multideporte en grandes ciudades con academias formativas y ligas de empresa.",
        "sedes_principales": [
            "UrbanPadel Lille-Lezennes",
            "UrbanPadel Lyon-Baraban",
            "UrbanPadel Nantes-Carquefou",
            "UrbanPadel Toulouse-Montaudran",
            "UrbanPadel Rennes (Vern-sur-Seiche)",
            "UrbanPadel París-Puteaux (Île de Puteaux)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas indoor cubiertas con césped monofilamento azul",
            "software": "App oficial de reservas UrbanPadel",
            "domotica": "Control de acceso sincronizado con la reserva",
            "grabacion": "Cámaras para análisis de entrenamiento y clínics",
            "restauracion": "Clubhouse con restauración rápida y pantallas deportivas"
        },
        "modelo_expansion": {
            "tipo_contrato": "Desarrollo propio sobre activos inmobiliarios de UrbanSoccer",
            "perfil_club": "Centros multideporte de 3 a 8 pistas anexas al fútbol",
            "canon_royalties": "Operación directa",
            "inversion_media": "300.000€ a 700.000€"
        },
        "diferencial": "Ubicaciones metropolitanas clave y bases de datos consolidadas de deportistas corporativos."
    },
    {
        "id": "padelshot",
        "nombre": "PadelShot",
        "pais": "Francia",
        "pais_codigo": "FR",
        "region_filtro": "FR",
        "bandera": "🇫🇷",
        "ciudad_sede": "Caen",
        "coords": [49.1828, -0.3707],
        "modelo": "Cadena Multiactividad (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "5 centros con el mismo nombre",
        "num_pistas": "36+ pistas",
        "software": "Doinsport",
        "fundadores": "Jérôme Doligé",
        "web": "https://padelshot.fr",
        "tagline": "El concepto 'Lieu de Vie' donde el pádel convive con el bádminton, la petanca y el ocio social.",
        "resumen": "5 centros todos bajo la marca PadelShot: Caen, Saint-Étienne, Metz, Lyon Craponne, Reims. Combina pádel cubierto con bádminton, petanca interior y billar, con restaurante deportivo donde la hostelería genera más del 40% de ingresos.",
        "sedes_principales": [
            "PadelShot Caen (Mondeville - centro insignia)",
            "PadelShot Saint-Étienne",
            "PadelShot Metz",
            "PadelShot Lyon (Craponne)",
            "PadelShot Reims"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con salidas de pista autorizadas y moqueta WPT",
            "software": "Doinsport para reservas cruzadas multideporte",
            "domotica": "Marcadores digitales en pista",
            "grabacion": "Cámaras para torneos FFT P500 y P1000",
            "restauracion": "Restaurante con platos del día y zonas de seminario para empresas"
        },
        "modelo_expansion": {
            "tipo_contrato": "Desarrollo propio corporativo",
            "perfil_club": "Naves de 3.000 a 6.000 m² con capacidad para 6-10 pistas más ocio",
            "canon_royalties": "Operador directo",
            "inversion_media": "1M€ a 2M€ por complejo"
        },
        "diferencial": "Excepcional facturación en hostelería y eventos corporativos para grupos grandes."
    },
    {
        "id": "padel-tolosa",
        "nombre": "Padel Tolosa",
        "pais": "Francia",
        "pais_codigo": "FR",
        "region_filtro": "FR",
        "bandera": "🇫🇷",
        "ciudad_sede": "Toulouse / Montauban",
        "coords": [43.6047, 1.4442],
        "modelo": "Cadena Multiclub Regional (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "boutique",
        "num_clubs": "4 complejos con el mismo nombre",
        "num_pistas": "20+ pistas",
        "software": "Doinsport",
        "fundadores": "Jérôme Cauchy y socios",
        "web": "https://padeltolosa.fr",
        "tagline": "La cadena de referencia en el suroeste de Francia.",
        "resumen": "Cadena de clubes bajo el nombre Padel Tolosa en Toulouse, Montauban, Albi y Rodez combinando deporte con gastronomía regional del suroeste (tapas y pato).",
        "sedes_principales": [
            "Padel Tolosa Toulouse",
            "Padel Tolosa Montauban",
            "Padel Tolosa Albi",
            "Padel Tolosa Rodez"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas indoor y semicubiertas homologadas por la FFT",
            "software": "Doinsport",
            "domotica": "Check-in móvil y taquillas",
            "grabacion": "Sistemas de vídeo en pista",
            "restauracion": "Tapas bar con embutidos locales y vinos de la región"
        },
        "modelo_expansion": {
            "tipo_contrato": "Franquicia regional y clubes propios",
            "perfil_club": "Ciudades medianas del sur de Francia con 4 a 6 pistas",
            "canon_royalties": "Canon de adhesión ~15.000€ y 4% royalties",
            "inversion_media": "300.000€ a 600.000€"
        },
        "diferencial": "Conocimiento exhaustivo del mercado del sur de Francia y cultura de club muy cercana."
    },

    # ─────────────────────────────────────────────────────────────
    # 🇬🇧 REINO UNIDO (6 Cadenas y Franquicias)
    # ─────────────────────────────────────────────────────────────
    {
        "id": "rocket-padel",
        "nombre": "Rocket Padel",
        "pais": "Reino Unido y Dinamarca",
        "pais_codigo": "GB",
        "region_filtro": "GB",
        "bandera": "🇬🇧",
        "ciudad_sede": "Bristol / Londres",
        "coords": [51.4545, -2.5879],
        "modelo": "Cadena de Macroarenas Cubiertas (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "5 macrocentros con el mismo nombre",
        "num_pistas": "45+ pistas indoor",
        "software": "Matchi / Padel Mates",
        "fundadores": "Rocket Padel Group (UK & Escandinavia)",
        "web": "https://rocketpadel.com",
        "tagline": "Las macroarenas cubiertas más monumentales del Reino Unido.",
        "resumen": "Rocket Padel opera bajo su misma marca algunos de los mayores complejos indoor de Gran Bretaña. Su sede de Bristol (St. Annes Park) cuenta con 14 pistas cubiertas, bistro y gimnasio. En Londres operan en Battersea Power Station (CUPRA Arena), Ilford (12 pistas panorámicas) y Beckton.",
        "sedes_principales": [
            "Rocket Padel Bristol (14 pistas panorámicas cubiertas, bistro y gimnasio)",
            "Rocket Padel Battersea London (CUPRA Arena, Battersea Power Station)",
            "Rocket Padel Ilford (Londres - 12 pistas indoor panorámicas)",
            "Rocket Padel Beckton (Londres - con 'The Lab' gym y coworking)",
            "Rocket Padel Dinamarca (Copenhague)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de competición con alturas libres de más de 10 metros",
            "software": "Matchi y Padel Mates",
            "domotica": "Check-in digitalizado, apertura automática e iluminación LED inteligente",
            "grabacion": "Sistemas de vídeo en pista para clínics y streaming",
            "restauracion": "Bistros con café artesanal, cerveza de grifo, comida saludable y pro-shop"
        },
        "modelo_expansion": {
            "tipo_contrato": "Desarrollo propio corporativo bajo la marca Rocket Padel",
            "perfil_club": "Macroarenas industriales de 10 a 16 pistas cubiertas",
            "canon_royalties": "Cadena propia",
            "inversion_media": "1.5M£ a 3.5M£ por macrocentro"
        },
        "diferencial": "Escala monumental bajo techo (14 pistas en un solo centro) y alianzas con marcas como CUPRA."
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
        "resumen": "Asumen el 100% del capital (CAPEX) para diseñar, tramitar licencias y construir pistas en clubes de tenis tradicionales, universidades y centros comerciales a cambio de concesiones con reparto de ingresos.",
        "sedes_principales": [
            "Westfield London (Centro comercial en Shepherd's Bush, Londres)",
            "Edimburgo (Thistle Tennis Club)",
            "Glasgow y Aberdeen",
            "Windsor, Shropshire, Cardiff (Gales)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas con cubiertas tensadas resistentes al clima británico",
            "software": "Matchi",
            "domotica": "Acceso desasistido 24/7 con código PIN e iluminación sincronizada",
            "grabacion": "Cámaras conectadas para torneos corporativos",
            "restauracion": "Aprovechan hostelería del club anfitrión o quioscos"
        },
        "modelo_expansion": {
            "tipo_contrato": "Concesión de terreno con reparto de ingresos (Revenue Share)",
            "perfil_club": "Clubes de tenis con espacio para 2 a 6 pistas",
            "canon_royalties": "El club no gasta dinero; Game4Padel financia la obra",
            "inversion_media": "150.000€ a 450.000€ financiado por Game4Padel"
        },
        "diferencial": "Respaldo de Sir Andy Murray, sin riesgo financiero para el club anfitrión."
    },
    {
        "id": "the-padel-club-uk",
        "nombre": "The Padel Club",
        "pais": "Reino Unido",
        "pais_codigo": "GB",
        "region_filtro": "GB",
        "bandera": "🇬🇧",
        "ciudad_sede": "Wilmslow / Mánchester",
        "coords": [53.3283, -2.2295],
        "modelo": "Cadena Multiclub Boutique (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "boutique",
        "num_clubs": "3 centros con el mismo nombre",
        "num_pistas": "20+ pistas",
        "software": "Playtomic / Matchi",
        "fundadores": "Kristopher Ball",
        "web": "https://thepadelclub.co.uk",
        "tagline": "El club de pádel boutique de diseño y gastronomía de referencia en Mánchester.",
        "resumen": "Cadena boutique bajo el nombre The Padel Club. Centro en TraffordCity (Mánchester) con 11 pistas cubiertas, techos acristalados, bar con cócteles y eventos sociales con DJ.",
        "sedes_principales": [
            "The Padel Club TraffordCity (Mánchester - 11 pistas indoor)",
            "The Padel Club Wilmslow (Cheshire - 4 pistas)",
            "The Padel Club Gloucester (en desarrollo)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de cristal templado continuo",
            "software": "Playtomic y Matchi",
            "domotica": "Sonido envolvente Bose en pistas y lounge",
            "grabacion": "Grabación de partidos en alta definición",
            "restauracion": "Clubhouse con cafetería de autor y batidos energéticos"
        },
        "modelo_expansion": {
            "tipo_contrato": "Crecimiento propio en grandes destinos de ocio",
            "perfil_club": "Grandes recintos de alto tráfico y zonas prémium",
            "canon_royalties": "Operación directa",
            "inversion_media": "1.5M£ a 3M£"
        },
        "diferencial": "Experiencia premium de juego, ocio y ambiente social sofisticado."
    },
    {
        "id": "soul-padel",
        "nombre": "Soul Padel",
        "pais": "Reino Unido",
        "pais_codigo": "GB",
        "region_filtro": "GB",
        "bandera": "🇬🇧",
        "ciudad_sede": "Mánchester / Stockport",
        "coords": [53.4808, -2.2426],
        "modelo": "Cadena Multiclub Comunitaria (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "boutique",
        "num_clubs": "4 centros con el mismo nombre",
        "num_pistas": "18+ pistas",
        "software": "Matchi",
        "fundadores": "Mark Hewlett",
        "web": "https://soulpadel.co.uk",
        "tagline": "Pádel accesible y amigable en el corazón de las comunidades del norte de Inglaterra.",
        "resumen": "Cadena que opera bajo la marca Soul Padel en parques comerciales y polideportivos (Wigan, Mánchester). Precios asequibles y alquiler gratuito para novatos.",
        "sedes_principales": [
            "Soul Padel Mánchester (Urban Exchange)",
            "Soul Padel Wigan (Robin Park Sports Zone)",
            "Soul Padel Preston",
            "Soul Padel Cheshire"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con cubiertas resistentes al viento",
            "software": "Matchi",
            "domotica": "Iluminación eficiente LED y apertura digital",
            "grabacion": "Grabación de jugadas en torneos locales",
            "restauracion": "Puntos de café y snacks saludables"
        },
        "modelo_expansion": {
            "tipo_contrato": "Alianzas y franquicia con consejos municipales",
            "perfil_club": "Suelos en desuso de 1.000 a 2.500 m² para 3 a 5 pistas",
            "canon_royalties": "Modelo flexible de franquicia social",
            "inversion_media": "180.000£ a 350.000£"
        },
        "diferencial": "Atracción masiva de británicos novatos mediante programas comunitarios."
    },
    {
        "id": "pure-padel-uk",
        "nombre": "Pure Padel",
        "pais": "Reino Unido",
        "pais_codigo": "GB",
        "region_filtro": "GB",
        "bandera": "🇬🇧",
        "ciudad_sede": "Mánchester / Cheshire",
        "coords": [53.3031, -2.2350],
        "modelo": "Cadena Multiclub Indoor Pura (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "boutique",
        "num_clubs": "3 centros con el mismo nombre",
        "num_pistas": "15+ pistas",
        "software": "Playtomic",
        "fundadores": "Sammy Arora",
        "web": "https://purepadelclubs.co.uk",
        "tagline": "La nueva ola de clubes 100% dedicados al pádel indoor en el Reino Unido.",
        "resumen": "Cadena en el noroeste inglés que opera centros indoor dedicados exclusivamente al pádel bajo la marca Pure Padel con cafetería social, zona de calentamiento y pro-shop.",
        "sedes_principales": [
            "Pure Padel Alderley Edge (Cheshire - centro insignia)",
            "Pure Padel Mánchester Centro",
            "Pure Padel Birmingham"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de cristal de 12 mm y moqueta WPT",
            "software": "Playtomic",
            "domotica": "Apertura por código QR y check-in digital",
            "grabacion": "Cámaras inteligentes en pista",
            "restauracion": "Café de barista y batidos de proteínas"
        },
        "modelo_expansion": {
            "tipo_contrato": "Desarrollo propio corporativo",
            "perfil_club": "Naves de 4 a 8 pistas en áreas residenciales del noroeste inglés",
            "canon_royalties": "Operación directa",
            "inversion_media": "400.000£ a 800.000£"
        },
        "diferencial": "Compromiso de juego garantizado los 365 días bajo techo climatizado."
    },
    {
        "id": "pdl-united-uk",
        "nombre": "PDL Padel United UK",
        "pais": "Reino Unido",
        "pais_codigo": "GB",
        "region_filtro": "GB",
        "bandera": "🇬🇧",
        "ciudad_sede": "Maldon, Essex",
        "coords": [51.7311, 0.6749],
        "modelo": "Cadena de Clubes Comunitarios (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "14+ centros con el mismo nombre",
        "num_pistas": "55+ pistas",
        "software": "Matchi / Playtomic",
        "fundadores": "Richard Jackson (CEO UK), bajo paraguas Padel United",
        "web": "https://padeluniteduk.com",
        "tagline": "Construyendo comunidades de pádel inclusivas en todo el Reino Unido.",
        "resumen": "Operador británico con mayor arraigo social. Clubes dedicados con programación intensiva de dinamización: clínics de novatos, mañanas de veteranos y torneos amateur constantes.",
        "sedes_principales": [
            "Padel United Maldon (Essex - centro insignia)",
            "Padel United Bushey (North London - Bushey Grove Leisure Centre)",
            "Padel United Colchester y Chelmsford",
            "Padel United The Wirral (Port Sunlight)",
            "Padel United Torbay, Plymouth, Cambridge"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas cubiertas con naves o marquesinas para lluvia",
            "software": "Matchi y Playtomic",
            "domotica": "Control de accesos y material automático",
            "grabacion": "Dispositivos para grabaciones técnicas",
            "restauracion": "Cafetería social y tienda con palas de prueba"
        },
        "modelo_expansion": {
            "tipo_contrato": "Franquicia de gestión y clubes propios",
            "perfil_club": "Zonas urbanas o suburbanas británicas de más de 3 pistas",
            "canon_royalties": "Canon ~15.000£ y royalties operativos del 5%",
            "inversion_media": "200.000£ a 600.000£"
        },
        "diferencial": "Retención comunitaria récord con alta ocupación matinal entre semana."
    },

    # ─────────────────────────────────────────────────────────────
    # 🇸🇪 SUECIA Y NÓRDICOS (8 Cadenas y Franquicias)
    # ─────────────────────────────────────────────────────────────
    {
        "id": "interpadel-norway",
        "nombre": "InterPadel",
        "pais": "Noruega",
        "pais_codigo": "NO",
        "region_filtro": "SE",
        "bandera": "🇳🇴",
        "ciudad_sede": "Oslo / Stavanger",
        "coords": [59.9139, 10.7522],
        "modelo": "Cadena Multiclub Líder en Noruega (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "6 macrocentros con el mismo nombre",
        "num_pistas": "45+ pistas",
        "software": "Matchi",
        "fundadores": "Jan Frode Andersen (Exjugador de Copa Davis noruego)",
        "web": "https://interpadel.no",
        "tagline": "Norges største padel kjede: La mayor cadena de centros de pádel de Noruega.",
        "resumen": "InterPadel es la cadena nacional noruega por excelencia. Fundada por el extenista Jan Frode Andersen, opera grandes centros indoor todos con la marca InterPadel en Oslo, Forus, Sandnes, Letohallen (con una altura de techo récord de 15 metros) y Os en Bergen.",
        "sedes_principales": [
            "InterPadel Oslo (8 pistas: 6 dobles + 2 individuales, 9m de altura)",
            "InterPadel Letohallen (8 pistas con 15 metros de altura libre récord)",
            "InterPadel Os (Bergen - 13 pistas: 10 dobles + 3 individuales)",
            "InterPadel Forus (Stavanger - 7 pistas)",
            "InterPadel Sandnes (Trim Towers)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas dobles e individuales de competición con techos de 9 a 15 metros",
            "software": "Matchi",
            "domotica": "Acceso desatendido 24/7 y calefacción automatizada",
            "grabacion": "Cámaras táctiles en pista para análisis de juego",
            "restauracion": "Pro-shops completas con las mejores marcas y zonas de descanso"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena corporativa con la misma marca InterPadel",
            "perfil_club": "Macroarenas de 6 a 14 pistas en ciudades clave noruegas",
            "canon_royalties": "Cadena unificada",
            "inversion_media": "800.000€ a 1.800.000€"
        },
        "diferencial": "Alturas de techo incomparables (hasta 15 metros) y el liderazgo de Jan Frode Andersen."
    },
    {
        "id": "padelpadel-denmark",
        "nombre": "PadelPadel",
        "pais": "Dinamarca",
        "pais_codigo": "DK",
        "region_filtro": "SE",
        "bandera": "🇩🇰",
        "ciudad_sede": "Odense / Aarhus",
        "coords": [55.4038, 10.4024],
        "modelo": "Cadena Multiclub Danesa (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "3 macrocentros con el mismo nombre",
        "num_pistas": "26+ pistas",
        "software": "Matchi",
        "fundadores": "PadelPadel ApS",
        "web": "https://padelpadel.dk",
        "tagline": "Pistas cubiertas de diseño nórdico en las mayores ciudades de Dinamarca.",
        "resumen": "Cadena de clubes danesa que opera centros cubiertos modernos bajo la marca PadelPadel en Odense, Aarhus y Aalborg. Foco en la comodidad del jugador: aparcamiento gratuito, taquillas electrónicas, calefacción y pistas de nivel WPT.",
        "sedes_principales": [
            "PadelPadel Odense (10 pistas indoor)",
            "PadelPadel Aarhus (8 pistas indoor)",
            "PadelPadel Aalborg (8 pistas indoor)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con césped texturizado de competición y techos altos",
            "software": "Matchi",
            "domotica": "Acceso 100% digitalizado por código",
            "grabacion": "Cámaras conectadas para partidos",
            "restauracion": "Lounge nórdico con café y bebidas isotónicas"
        },
        "modelo_expansion": {
            "tipo_contrato": "Operación directa bajo la marca PadelPadel",
            "perfil_club": "Naves de 8 a 12 pistas cubiertas",
            "canon_royalties": "Cadena unificada",
            "inversion_media": "700.000€ a 1.400.000€"
        },
        "diferencial": "Estandarización absoluta de la experiencia de juego en las tres grandes ciudades danesas fuera de Copenhague."
    },
    {
        "id": "ledap-wap",
        "nombre": "LeDap / We Are Padel (WAP)",
        "pais": "Internacional (Suecia / Europa)",
        "pais_codigo": "SE",
        "region_filtro": "SE",
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
        "fundadores": "Triton Partners / Pontus Gustafsson",
        "web": "https://ledap.com",
        "tagline": "El gigante pan-europeo del pádel indoor respaldado por capital institucional.",
        "resumen": "La mayor plataforma internacional de pádel: integró We Are Padel (Suecia y Alemania), Just Padel (Noruega), Padel Club Finland y Padel Zone (Austria), con presencia en UK, Polonia y España.",
        "sedes_principales": [
            "Suecia: Más de 40 centros en Estocolmo, Gotemburgo, Malmö",
            "Alemania: Berlín, Bremen, Düsseldorf",
            "Reino Unido: Derby, Bristol",
            "Finlandia y Noruega: Red en Helsinki, Tampere, Oslo",
            "Austria: Viena y Graz (Padel Zone)",
            "España: LeDap Madrid"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas indoor de 8 a 12 metros de altura",
            "software": "App propia LeDap integrada con Matchi y Playtomic",
            "domotica": "Check-in digital, apertura remota con código PIN",
            "grabacion": "Cámaras conectadas en pistas seleccionadas",
            "restauracion": "Lounge corners con vending automatizado y cafetería"
        },
        "modelo_expansion": {
            "tipo_contrato": "Consolidación corporativa y aperturas propias",
            "perfil_club": "Instalaciones indoor con mínimo 6 a 12 pistas",
            "canon_royalties": "Operación directa corporativa",
            "inversion_media": "600.000€ a 1.500.000€"
        },
        "diferencial": "Capacidad de escala paneuropea, estandarización y app unificada."
    },
    {
        "id": "pdl-center-united",
        "nombre": "PDL Center / Padel United",
        "pais": "Suecia y Reino Unido",
        "pais_codigo": "SE",
        "region_filtro": "SE",
        "bandera": "🇸🇪",
        "ciudad_sede": "Estocolmo",
        "coords": [59.3400, 18.0700],
        "modelo": "Cadena de Megacentros Nórdicos (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "mega",
        "num_clubs": "80+ centros",
        "num_pistas": "500+ pistas",
        "software": "Matchi",
        "fundadores": "Henrik Söderberg, Jonas Björkman (Extenista), Måns Zelmerlöw / Markus Hellqvist",
        "web": "https://padelunited.se",
        "tagline": "Pioneros del pádel en Suecia que fusionaron dos imperios para dominar el norte de Europa.",
        "resumen": "PDL Center (fundado por la leyenda del tenis Jonas Björkman y el cantante Måns Zelmerlöw) opera decenas de complejos bajo la marca PDL Center en Suecia y Padel United en UK. Cuentan con centros insignia de más de 20 pistas como PDL Frihamnen en Estocolmo.",
        "sedes_principales": [
            "PDL Center Frihamnen (Estocolmo - 22 pistas)",
            "PDL Center Kvarnholmen y Västberga",
            "Gotemburgo, Malmö, Jönköping",
            "Red en Reino Unido bajo PDL Padel United UK"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas de fabricantes líderes europeos con moqueta Mondo Supercourt",
            "software": "Matchi (el estándar sueco)",
            "domotica": "Acceso 100% automatizado fuera de horario de recepción",
            "grabacion": "Sistemas de cámaras con pantalla táctil en pista para repeticiones",
            "restauracion": "Clubhouse con cafetería, zonas de calentamiento y pro-shop completa"
        },
        "modelo_expansion": {
            "tipo_contrato": "Propiedad corporativa y adquisiciones selectas",
            "perfil_club": "Centros de más de 8 pistas cubiertas",
            "canon_royalties": "Grupo integrado",
            "inversion_media": "800.000€ a 2M€"
        },
        "diferencial": "El prestigio de Jonas Björkman y la implantación de la cultura del pádel en toda la sociedad sueca."
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
        "modelo": "Cadena de Macroarenas de Medios (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "5 macroarenas con el mismo nombre",
        "num_pistas": "60+ pistas",
        "software": "Matchi",
        "fundadores": "Everysport Media Group (ESMG)",
        "web": "https://everypadel.com",
        "tagline": "Grandes recintos de pádel integrados con el mayor grupo de medios deportivos sueco.",
        "resumen": "Cadena bajo la marca Every Padel. Construyeron una de las instalaciones de pádel más espectaculares del planeta dentro de la Åby Arena en Gotemburgo (con 25 pistas bajo un mismo techo), además de centros en Kista (Estocolmo) y Norrköping.",
        "sedes_principales": [
            "Every Padel Åby Arena (Gotemburgo - 25 pistas)",
            "Every Padel Kista (Estocolmo)",
            "Every Padel Norrköping",
            "Every Padel Jönköping"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas WPT dentro de arenas feriales y hoteleras",
            "software": "Matchi",
            "domotica": "Sistemas acústicos especiales y control de flujo de jugadores",
            "grabacion": "Streaming profesional integrado con portales de noticias deportivas",
            "restauracion": "Sinergia con los hoteles y restaurantes de la arena"
        },
        "modelo_expansion": {
            "tipo_contrato": "Explotación en grandes recintos feriales y deportivos",
            "perfil_club": "Grandes complejos de más de 12 pistas",
            "canon_royalties": "Operación corporativa",
            "inversion_media": "1.5M€ a 3.5M€"
        },
        "diferencial": "Cobertura mediática en prensa sueca y capacidad para organizar los torneos más multitudinarios."
    },
    {
        "id": "padel-zenter",
        "nombre": "Padel Zenter",
        "pais": "Suecia e Italia",
        "pais_codigo": "SE",
        "region_filtro": "SE",
        "bandera": "🇸🇪",
        "ciudad_sede": "Estocolmo",
        "coords": [59.2970, 18.0820],
        "modelo": "Cadena de Macrocomplejos de Ultra-Lujo (Mismo Nombre)",
        "modelo_badge": "bg-purple-100 text-purple-800 border-purple-200",
        "tipo_categoria": "boutique",
        "escala": "media",
        "num_clubs": "6 macrocentros con el mismo nombre",
        "num_pistas": "65+ pistas",
        "software": "Matchi / Proprietary",
        "fundadores": "Zlatan Ibrahimović y Thomas Sandström",
        "web": "https://padelzenter.se",
        "tagline": "La experiencia arquitectónica y de juego más exigente del mundo del pádel.",
        "resumen": "Creado por Zlatan Ibrahimović todos bajo la marca Padel Zenter con especificaciones extremas: alturas de 12 metros sin columnas, moqueta oficial WPT, insonorización acústica e iluminación indirecta sin deslumbramiento. Macrocomplejo en Milán-Segrate.",
        "sedes_principales": [
            "Padel Zenter Milán (Segrate, Italia - 9 pistas)",
            "Padel Zenter Estocolmo (Ársta)",
            "Padel Zenter Jönköping y Skövde",
            "Padel Zenter Örebro y Uppsala"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas AFP Courts aprobadas por la FIP, cristal templado de 12 mm y césped WPT",
            "software": "Matchi en Suecia y reservas online en Milán",
            "domotica": "Climatización y control inteligente de ventilación",
            "grabacion": "Sistemas de televisión y streaming para torneos",
            "restauracion": "Restaurantes de calidad superior y pro-shop PZ"
        },
        "modelo_expansion": {
            "tipo_contrato": "Propiedad directa y alianzas selectas",
            "perfil_club": "Macrocomplejos diseñados desde cimientos con mínimo 8 a 15 pistas",
            "canon_royalties": "No es franquicia abierta al público",
            "inversion_media": "3M€ a 8M€"
        },
        "diferencial": "El carisma y exigencia de Zlatan, acabados de hotel 5 estrellas y acústica sin eco."
    },
    {
        "id": "just-padel-norway",
        "nombre": "Just Padel Norway",
        "pais": "Noruega",
        "pais_codigo": "NO",
        "region_filtro": "SE",
        "bandera": "🇳🇴",
        "ciudad_sede": "Kristiansand / Oslo",
        "coords": [58.1467, 7.9956],
        "modelo": "Cadena Multiclub en Noruega (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "12+ centros con el mismo nombre",
        "num_pistas": "60+ pistas",
        "software": "Matchi",
        "fundadores": "Jesper Mathisen (Exfutbolista) y socios (adquirido por LeDap)",
        "web": "https://justpadel.no",
        "tagline": "El operador que introdujo y consolidó el pádel indoor en Noruega.",
        "resumen": "Just Padel es una de las principales cadenas noruegas con centros cubiertos todos operando bajo el nombre Just Padel en Oslo, Kristiansand, Stavanger y Bergen con calefacción optimizada para el invierno nórdico.",
        "sedes_principales": [
            "Just Padel Kristiansand (centro insignia)",
            "Just Padel Oslo y Drammen",
            "Just Padel Stavanger y Sandnes",
            "Just Padel Bergen y Skien"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con climatización de alto rendimiento",
            "software": "Matchi",
            "domotica": "Acceso desatendido por código PIN e iluminación sincronizada",
            "grabacion": "Cámaras en pistas centrales",
            "restauracion": "Lounge con máquinas de autoservicio y café noruego"
        },
        "modelo_expansion": {
            "tipo_contrato": "Operación directa bajo el paraguas del grupo LeDap",
            "perfil_club": "Naves industriales aisladas de 4 a 8 pistas",
            "canon_royalties": "Corporativo",
            "inversion_media": "500.000€ a 1.200.000€"
        },
        "diferencial": "Adaptación técnica al frío extremo de Noruega y gran capilaridad en ciudades costeras."
    },
    {
        "id": "racket-club-denmark",
        "nombre": "Racket Club",
        "pais": "Dinamarca",
        "pais_codigo": "DK",
        "region_filtro": "SE",
        "bandera": "🇩🇰",
        "ciudad_sede": "Copenhague",
        "coords": [55.6761, 12.5683],
        "modelo": "Cadena de Diseño Escandinavo (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "boutique",
        "num_clubs": "4 complejos con el mismo nombre",
        "num_pistas": "30+ pistas",
        "software": "Matchi",
        "fundadores": "Emprendedores daneses del diseño y el deporte",
        "web": "https://racketclub.dk",
        "tagline": "Pádel de estética puramente escandinava en el corazón de Copenhague.",
        "resumen": "Cadena bajo la marca Racket Club en antiguas naves industriales de Copenhague (Kløvermarken, Taastrup, Dragør) con diseño minimalista danés: maderas claras, iluminación cálida y café de especialidad.",
        "sedes_principales": [
            "Racket Club Kløvermarken (Copenhague)",
            "Racket Club Taastrup (Copenhague)",
            "Racket Club Dragør",
            "Racket Club Slagelse"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas WPT con estructuras en gris antracita y césped azul nórdico",
            "software": "Matchi",
            "domotica": "Check-in sin contacto por smartphone",
            "grabacion": "Cámaras discretas para análisis de juego",
            "restauracion": "Cafetería nórdica con bollería danesa artesanal, smørrebrød y zumos naturales"
        },
        "modelo_expansion": {
            "tipo_contrato": "Crecimiento propio en áreas urbanas de alta densidad danesas",
            "perfil_club": "Naves de valor arquitectónico de 6 a 10 pistas",
            "canon_royalties": "Propiedad privada",
            "inversion_media": "800.000€ a 1.800.000€"
        },
        "diferencial": "El concepto estético más elegante de Dinamarca con atmósfera hygge incomparable."
    },

    # ─────────────────────────────────────────────────────────────
    # 🇳🇱 PAÍSES BAJOS, BÉLGICA, ALEMANIA Y AUSTRIA (6 Cadenas)
    # ─────────────────────────────────────────────────────────────
    {
        "id": "padel-zone-austria",
        "nombre": "Padel Zone Austria",
        "pais": "Austria",
        "pais_codigo": "AT",
        "region_filtro": "NL",
        "bandera": "🇦🇹",
        "ciudad_sede": "Viena / Graz",
        "coords": [48.2082, 16.3738],
        "modelo": "Cadena Multiclub Líder en Austria (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "6 centros con el mismo nombre",
        "num_pistas": "35+ pistas",
        "software": "Playtomic / Matchi",
        "fundadores": "Padel Zone GmbH (Grupo LeDap)",
        "web": "https://padelzone.at",
        "tagline": "La cadena pionera y líder absoluta del pádel en Austria.",
        "resumen": "Padel Zone es la marca de referencia indiscutible en Austria. Opera complejos cubiertos bajo la misma enseña Padel Zone en Viena, Graz, Wiener Neustadt, Traiskirchen y Eisenstadt. Fueron adquiridos por el grupo europeo LeDap manteniendo su identidad de marca líder austríaca.",
        "sedes_principales": [
            "Padel Zone Wien Süssenbrunn (Viena)",
            "Padel Zone Graz",
            "Padel Zone Wiener Neustadt",
            "Padel Zone Traiskirchen",
            "Padel Zone Eisenstadt"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas cubiertas preparadas para temperaturas invernales bajo cero",
            "software": "Playtomic y Matchi",
            "domotica": "Acceso desatendido por código PIN fuera de horas de recepción",
            "grabacion": "Grabación en torneos de la Federación Austríaca",
            "restauracion": "Lounge austríaco con cafetería y venta de material"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena propia integrada en la red europea LeDap",
            "perfil_club": "Naves de 4 a 8 pistas en áreas urbanas austríacas",
            "canon_royalties": "Cadena unificada",
            "inversion_media": "500.000€ a 1.200.000€"
        },
        "diferencial": "Pioneros absolutos en Austria con casi el 50% de la cuota de mercado del pádel indoor nacional."
    },
    {
        "id": "the-padellers",
        "nombre": "The Padellers",
        "pais": "Países Bajos y Alemania",
        "pais_codigo": "NL",
        "region_filtro": "NL",
        "bandera": "🇳🇱",
        "ciudad_sede": "Ámsterdam",
        "coords": [52.3676, 4.9041],
        "modelo": "Cadena Multiclub en Expansión (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "grande",
        "num_clubs": "26+ centros con el mismo nombre",
        "num_pistas": "145+ pistas",
        "software": "BookaBall / Playtomic",
        "fundadores": "Philippe van Ellis, Bas Smit",
        "web": "https://thepadellers.nl",
        "tagline": "La cadena más dinámica de Países Bajos en plena conquista de Alemania.",
        "resumen": "Democratización del pádel sin cuotas obligatorias con enorme foco en el tercer tiempo ('borrel'). 26 clubes todos bajo el nombre The Padellers en Holanda y Alemania (Essen, Frankfurt, Herdecke).",
        "sedes_principales": [
            "The Padellers Ámsterdam (Amstelpark, West, Zuid)",
            "The Padellers Breda (2 complejos)",
            "The Padellers Groningen (2 complejos)",
            "The Padellers Hengelo, Roermond, Valkenswaard, Venlo",
            "The Padellers Alemania: Essen, Frankfurt, Herdecke, Troisdorf"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con iluminación LED optimizada",
            "software": "BookaBall con integración en Playtomic",
            "domotica": "Apertura por QR y check-in automatizado",
            "grabacion": "Cámaras en pistas centrales para eventos de empresa",
            "restauracion": "Bares temáticos con cervezas locales y snacks calientes"
        },
        "modelo_expansion": {
            "tipo_contrato": "Franquicia operativa, joint-venture y centros propios",
            "perfil_club": "Naves de mínimo 5 pistas cubiertas con zona lounge",
            "canon_royalties": "Canon ~25.000€ y 4-5% de royalty sobre facturación",
            "inversion_media": "350.000€ a 800.000€"
        },
        "diferencial": "Marketing viral en Países Bajos, eventos corporativos de gran escala y ambiente social."
    },
    {
        "id": "peakz-padel",
        "nombre": "Peakz Padel",
        "pais": "Países Bajos y Alemania",
        "pais_codigo": "NL",
        "region_filtro": "NL",
        "bandera": "🇳🇱",
        "ciudad_sede": "Utrecht",
        "coords": [52.0907, 5.1214],
        "modelo": "Cadena Multiclub Comunitaria (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "grande",
        "num_clubs": "17+ centros con el mismo nombre",
        "num_pistas": "110+ pistas",
        "software": "Playtomic",
        "fundadores": "Marc Kuijpers",
        "web": "https://peakzpadel.nl",
        "tagline": "Pioneros del concepto 'Pay & Play' comunitario con diseño nórdico e industrial.",
        "resumen": "Cadena de clubes bajo la marca Peakz Padel en naves de alta densidad. Sin cuotas de socio; famoso por su torneo semanal 'King of the Court'.",
        "sedes_principales": [
            "Peakz Padel Ámsterdam Zuidoost (14 pistas)",
            "Peakz Padel Ámsterdam Olympiaplein",
            "Peakz Padel Utrecht Vechtsebanen (14 pistas indoor)",
            "Peakz Padel Utrecht Zeehaenkade",
            "Peakz Padel Róterdam, Eindhoven",
            "Peakz Padel Alemania: Kleve (7 pistas), Hagen (10), Paderborn (8), Tönisvorst (10)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas dobles e individuales ('singles') de alta competición",
            "software": "Playtomic",
            "domotica": "Taquillas electrónicas, check-in digital y quioscos táctiles",
            "grabacion": "Streaming en torneos 'Peakz Tour'",
            "restauracion": "Clubhouse con café de especialidad y cervezas locales"
        },
        "modelo_expansion": {
            "tipo_contrato": "Crecimiento corporativo y alianzas con dueños de naves",
            "perfil_club": "Recintos industriales de mínimo 6 a 12 pistas",
            "canon_royalties": "Operación directa",
            "inversion_media": "500.000€ a 1.200.000€"
        },
        "diferencial": "Cultura de club consolidada y torneos King of the Court semanales masivos."
    },
    {
        "id": "plaza-padel",
        "nombre": "Plaza Padel",
        "pais": "Países Bajos",
        "pais_codigo": "NL",
        "region_filtro": "NL",
        "bandera": "🇳🇱",
        "ciudad_sede": "Ámsterdam",
        "coords": [52.3888, 4.8450],
        "modelo": "Cadena de Clubes de Negocios (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "5 complejos con el mismo nombre",
        "num_pistas": "42+ pistas",
        "software": "Playtomic",
        "fundadores": "John van Lottum (Extenista ATP)",
        "web": "https://plazapadel.com",
        "tagline": "El punto de encuentro entre el pádel de alto nivel y el networking empresarial.",
        "resumen": "Cadena de clubes bajo el nombre Plaza Padel en Ámsterdam, Almelo, Enschede, Heiloo y Waalwijk. Salas de reuniones de empresa, catering de negocios y clínics impartidos por exprofesionales.",
        "sedes_principales": [
            "Plaza Padel Ámsterdam (Rhoneweg - 9 pistas)",
            "Plaza Padel Almelo",
            "Plaza Padel Enschede",
            "Plaza Padel Heiloo",
            "Plaza Padel Waalwijk"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas indoor homologadas con alturas libres de más de 9 metros",
            "software": "Playtomic con paquetes B2B",
            "domotica": "Check-in digital y pantallas de torneos",
            "grabacion": "Grabación para análisis de clínics y eventos de empresa",
            "restauracion": "Restaurante con menú ejecutivo y terrazas cubiertas"
        },
        "modelo_expansion": {
            "tipo_contrato": "Crecimiento corporativo en parques empresariales",
            "perfil_club": "Complejos de 7 a 10 pistas con salas de conferencias",
            "canon_royalties": "Operación directa",
            "inversion_media": "700.000€ a 1.400.000€"
        },
        "diferencial": "Liderazgo de John van Lottum y gran cartera de patrocinadores corporativos."
    },
    {
        "id": "garrincha-belgium",
        "nombre": "Garrincha",
        "pais": "Bélgica",
        "pais_codigo": "BE",
        "region_filtro": "NL",
        "bandera": "🇧🇪",
        "ciudad_sede": "Gante / Amberes",
        "coords": [51.0543, 3.7174],
        "modelo": "Cadena Multiclub Urbana (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "4 grandes centros con el mismo nombre",
        "num_pistas": "25+ pistas",
        "software": "Playtomic",
        "fundadores": "Garrincha Sports NV",
        "web": "https://garrincha.be",
        "tagline": "Los macrocomplejos deportivos urbanos más vanguardistas de Flandes y Bruselas.",
        "resumen": "Cadena que opera bajo la enseña Garrincha en Gante, Amberes y Bruselas. Combinan fútbol reducido con pádel indoor de diseño industrial contemporáneo y terrazas cerveceras con cervezas de abadía.",
        "sedes_principales": [
            "Garrincha Gent (Gante - 8 pistas indoor)",
            "Garrincha Antwerpen (Amberes)",
            "Garrincha Brussels (Bruselas)",
            "Garrincha Charleroi"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de competición cubiertas",
            "software": "Playtomic",
            "domotica": "Control digital de iluminación por pista y tornos automáticos",
            "grabacion": "Cámaras en pista para torneos corporativos",
            "restauracion": "Gran Sports Bar belga con amplia carta de cervezas y hamburguesas gourmet"
        },
        "modelo_expansion": {
            "tipo_contrato": "Desarrollo propio corporativo",
            "perfil_club": "Naves de más de 3.000 m² en accesos a grandes ciudades belgas",
            "canon_royalties": "Operador integrado",
            "inversion_media": "1M€ a 2.5M€"
        },
        "diferencial": "Fusión del fútbol urbano y el pádel en un ambiente belga cervecero de máxima rentabilidad."
    },
    {
        "id": "padel-city",
        "nombre": "Padel City",
        "pais": "Alemania",
        "pais_codigo": "DE",
        "region_filtro": "DE",
        "bandera": "🇩🇪",
        "ciudad_sede": "Fürth / Múnich",
        "coords": [49.4774, 10.9886],
        "modelo": "Cadena Multiclub en Alemania (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "12+ centros con el mismo nombre",
        "num_pistas": "50+ pistas",
        "software": "Playtomic / CourtBrain",
        "fundadores": "PadelCity Deutschland GmbH",
        "web": "https://padelcity.de",
        "tagline": "La cadena alemana de mayor capilaridad y crecimiento rápido.",
        "resumen": "12 complejos cubiertos todos bajo la marca Padel City: Dortmund, Frankfurt, Fürth, Leipzig, Múnich. Pistas cubiertas y semicubiertas asociándose con polideportivos o rehabilitando naves logísticas.",
        "sedes_principales": [
            "Padel City Dortmund (Indoor y outdoor)",
            "Padel City Frankfurt am Main",
            "Padel City Fürth y Heilsbronn (Baviera)",
            "Padel City Leipzig y Múnich",
            "Centros en Renania del Norte-Westfalia"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas homologadas con cubiertas para nieve e invierno",
            "software": "Playtomic y CourtBrain",
            "domotica": "Acceso 100% digitalizado por código numérico",
            "grabacion": "Preparadas para análisis técnico en escuelas",
            "restauracion": "Clubhouse funcional con bebidas y vestuarios"
        },
        "modelo_expansion": {
            "tipo_contrato": "Franquicia de marca y gestión de instalaciones",
            "perfil_club": "Centros de 3 a 6 pistas con automatización",
            "canon_royalties": "Canon ~18.000€ y 4% de royalties sobre pistas",
            "inversion_media": "250.000€ a 550.000€"
        },
        "diferencial": "Pioneros en Alemania, adaptación al frío y modelo eficiente de costes."
    },

    # ─────────────────────────────────────────────────────────────
    # 🇮🇹 ITALIA (5 Cadenas y Franquicias)
    # ─────────────────────────────────────────────────────────────
    {
        "id": "country-sport-village",
        "nombre": "Country Sport Village",
        "pais": "Italia",
        "pais_codigo": "IT",
        "region_filtro": "IT",
        "bandera": "🇮🇹",
        "ciudad_sede": "Milán (Paderno Dugnano)",
        "coords": [45.5714, 9.1678],
        "modelo": "El Mayor Megacomplejo Indoor de Italia",
        "modelo_badge": "bg-blue-100 text-blue-800 border-blue-200",
        "tipo_categoria": "corporativo",
        "escala": "grande",
        "num_clubs": "1 macrocomplejo insignia (+ expansión)",
        "num_pistas": "21+ pistas",
        "software": "Playtomic",
        "fundadores": "Familia Colombo / Country Sport Village Srl",
        "web": "https://countrysportvillage.it",
        "tagline": "El macrocomplejo de pádel cubierto más grande y laureado de Italia.",
        "resumen": "Situado en el área metropolitana de Milán, es el coloso indiscutible del pádel italiano. Cuenta con más de 20 pistas de pádel indoor cubiertas (incluyendo pistas individuales 1vs1), pistas de vóley playa, fútbol 5 y su famoso RistoPub & Pizza Pepe 68. Citado como modelo de éxito europeo por Playtomic.",
        "sedes_principales": [
            "Paderno Dugnano (Milán - 21 pistas cubiertas)",
            "Polos asociados en Lombardía"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas cubiertas bajo cubiertas tensadas y naves industriales de 10 metros",
            "software": "Playtomic (caso de éxito con miles de reservas mensuales)",
            "domotica": "Iluminación automatizada y control de aforo",
            "grabacion": "Pistas de exhibición con torretas de vídeo",
            "restauracion": "RistoPub Pepe 68: pizzería con horno de leña, cervecería artesanal y terraza"
        },
        "modelo_expansion": {
            "tipo_contrato": "Operación directa corporativa",
            "perfil_club": "Megaterrenos de más de 20.000 m²",
            "canon_royalties": "Propiedad privada",
            "inversion_media": "3M€ a 6M€"
        },
        "diferencial": "Escala masiva: ningún otro club en Italia concentra tal volumen de pistas bajo techo."
    },
    {
        "id": "padel-palace",
        "nombre": "Padel Palace",
        "pais": "Italia",
        "pais_codigo": "IT",
        "region_filtro": "IT",
        "bandera": "🇮🇹",
        "ciudad_sede": "Milán",
        "coords": [45.4930, 9.2150],
        "modelo": "Cadena Boutique & Gastronómica (Mismo Nombre)",
        "modelo_badge": "bg-purple-100 text-purple-800 border-purple-200",
        "tipo_categoria": "boutique",
        "escala": "boutique",
        "num_clubs": "2 centros con el mismo nombre",
        "num_pistas": "12+ pistas",
        "software": "Playtomic",
        "fundadores": "Alessandro Borghese (Chef), Diletta Leotta, Max Giusti, Junior Cally",
        "web": "https://padelpalace.it",
        "tagline": "Donde el pádel milanés se fusiona con la alta gastronomía y el espectáculo.",
        "resumen": "Cadena de clubes bajo el nombre Padel Palace en Milán. Fundado por el chef Alessandro Borghese (con su bistrot interno ABKS Break Time), Diletta Leotta y artistas italianos. Pistas cubiertas dobles e individuales con una estética elegante y cocina gourmet.",
        "sedes_principales": [
            "Padel Palace Milano (Via Flumendosa, Crescenzago)",
            "Padel Palace 2 (Milán metropolitana)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas cubiertas y climatizadas todo el año",
            "software": "Playtomic",
            "domotica": "Check-in táctil en recepción y control digital de reservas",
            "grabacion": "Cámaras inteligentes para compartir puntos en redes sociales",
            "restauracion": "ABKS Break Time by Alessandro Borghese: alta cocina informal italiana y cócteles de autor"
        },
        "modelo_expansion": {
            "tipo_contrato": "Desarrollo propio respaldado por socios mediáticos",
            "perfil_club": "Naves urbanas en Milán de 5 a 10 pistas con bistrot integrado",
            "canon_royalties": "Club cerrado",
            "inversion_media": "1.5M€ a 3M€"
        },
        "diferencial": "Tirón mediático incomparable en Italia y una oferta culinaria supervisada por uno de los chefs más famosos de la televisión."
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
        "modelo": "Club de Ultra-Lujo & Moda Urbana",
        "modelo_badge": "bg-purple-100 text-purple-800 border-purple-200",
        "tipo_categoria": "boutique",
        "escala": "boutique",
        "num_clubs": "2 centros exclusivos",
        "num_pistas": "10+ pistas",
        "software": "Playtomic",
        "fundadores": "Demetrio Albertini, Pierluigi Casiraghi / Alianza Golden Goose",
        "web": "https://citypadelmilano.it",
        "tagline": "Premiado como el Mejor Club de Italia en los Italian Padel Awards.",
        "resumen": "Ubicado junto a los rascacielos de CityLife en Milán, City Padel Milano (promovido por Demetrio Albertini) se unió a la marca de lujo veneciana Golden Goose para crear la 'Golden Goose Arena'. Estética minimalista total black, vestuarios de mármol y clientela de élite.",
        "sedes_principales": [
            "CityLife Viale Duilio (Milán)",
            "Polos satélites de entrenamiento"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas customizadas en negro mate con iluminación indirecta",
            "software": "Playtomic",
            "domotica": "Concierge VIP y control de acceso inteligente",
            "grabacion": "Grabación broadcast para torneos de leyendas",
            "restauracion": "Lounge bar de diseño con café espresso de especialidad y champán"
        },
        "modelo_expansion": {
            "tipo_contrato": "Explotación propia y patrocinios de lujo",
            "perfil_club": "Localizaciones urbanas exclusivas en el centro financiero",
            "canon_royalties": "Operación directa",
            "inversion_media": "2M€ a 4M€"
        },
        "diferencial": "Alianza con el mundo de la moda y ubicación inmejorable en el distrito más moderno de Milán."
    },
    {
        "id": "joy-padel-club",
        "nombre": "Joy Padel Club / Tolcinasco",
        "pais": "Italia",
        "pais_codigo": "IT",
        "region_filtro": "IT",
        "bandera": "🇮🇹",
        "ciudad_sede": "Milán / Lombardía",
        "coords": [45.3667, 9.1833],
        "modelo": "Cadena Multiclub en Campos de Golf (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "3 centros con el mismo nombre",
        "num_pistas": "18+ pistas",
        "software": "Playtomic",
        "fundadores": "Joy Padel Group",
        "web": "https://joypadelclub.it",
        "tagline": "Clubes de pádel integrados en entornos residenciales y de golf de alto poder adquisitivo.",
        "resumen": "Cadena bajo la enseña Joy Padel en el Castello di Tolcinasco Golf Club y otras zonas selectas del sur de Milán. Combina la elegancia de los clubes de golf con naves cubiertas para jugar todo el año.",
        "sedes_principales": [
            "Joy Padel Castello di Tolcinasco (Milán - 8 pistas)",
            "Joy Padel Rozzano",
            "Joy Padel San Donato"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas cubiertas con estructuras geodésicas y césped azul WPT",
            "software": "Playtomic",
            "domotica": "Acceso por app y reservas corporativas",
            "grabacion": "Pistas para clinics con entrenadores españoles",
            "restauracion": "Acceso al clubhouse de golf con restaurante y piscina"
        },
        "modelo_expansion": {
            "tipo_contrato": "Concesión y explotación en clubes de campo existentes",
            "perfil_club": "Clubes de golf o tenis que desean revitalizar sus ingresos con pádel",
            "canon_royalties": "Revenue share con el club anfitrión",
            "inversion_media": "400.000€ a 900.000€"
        },
        "diferencial": "Entornos verdes espectaculares, fácil aparcamiento y sinergia con el golf."
    },
    {
        "id": "ghost-padel",
        "nombre": "Ghost Padel (Franquicia Internacional)",
        "pais": "Italia e Internacional",
        "pais_codigo": "IT",
        "region_filtro": "IT",
        "bandera": "🇮🇹",
        "ciudad_sede": "Bérgamo / Milán",
        "coords": [45.6983, 9.6773],
        "modelo": "Franquicia de Concepto Tecnológico Luminiscente",
        "modelo_badge": "bg-indigo-100 text-indigo-800 border-indigo-200",
        "tipo_categoria": "franquicia",
        "escala": "boutique",
        "num_clubs": "10+ pistas franquiciadas en clubes",
        "num_pistas": "15+ pistas instaladas",
        "software": "Playtomic / Ghost App",
        "fundadores": "Gianluca Vacchi y emprendedores italianos",
        "web": "https://ghostpadel.it",
        "tagline": "El juego a oscuras con líneas y bolas de neón: la experiencia de ocio nocturno más viral.",
        "resumen": "Ghost Padel es una patente y franquicia italiana revolucionaria: se juega en completa oscuridad. La pista cuenta con líneas perimetrales LED fluorescentes, red luminiscente, bolas que brillan en la oscuridad y ropa reactiva con luz ultravioleta. Se franquicia a clubes existentes como pista de atracción estrella.",
        "sedes_principales": [
            "Pistas instaladas en Milán, Roma y Nápoles",
            "Licencias en España, Dubái y Estados Unidos"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas con sistema patentado de luminiscencia LED integrada en marcos y cristal",
            "software": "Software propio para encendido del show de luces",
            "domotica": "Cambio de pista convencional a 'Modo Ghost' con un solo botón",
            "grabacion": "Cámaras ultravioleta para vídeos hiper-virales en TikTok e Instagram",
            "restauracion": "Cócteles de neón y eventos nocturnos con DJ"
        },
        "modelo_expansion": {
            "tipo_contrato": "Franquicia y paquete de conversión de pista para clubes existentes",
            "perfil_club": "Cualquier club indoor que quiera rentabilizar noches de fin de semana",
            "canon_royalties": "Paquete de conversión tecnológica (~30.000€ - 45.000€) y royalties de marca",
            "inversion_media": "35.000€ por pista adaptada"
        },
        "diferencial": "Viralidad absoluta en redes sociales y tarifa por hora multiplicada por 2 o 3 para eventos nocturnos."
    },

    # ─────────────────────────────────────────────────────────────
    # 🇵🇹 PORTUGAL (2 Cadenas)
    # ─────────────────────────────────────────────────────────────
    {
        "id": "rackets-pro",
        "nombre": "Rackets Pro",
        "pais": "Portugal",
        "pais_codigo": "PT",
        "region_filtro": "PT",
        "bandera": "🇵🇹",
        "ciudad_sede": "Lisboa",
        "coords": [38.7223, -9.1393],
        "modelo": "Cadena Multiclub en Lisboa (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "6 grandes complejos con el mismo nombre",
        "num_pistas": "45+ pistas",
        "software": "AirCourts / Playtomic",
        "fundadores": "Rackets Pro Gestão de Clubes",
        "web": "https://racketspro.pt",
        "tagline": "El operador deportivo de raqueta más prestigioso de Lisboa y Cascais.",
        "resumen": "Cadena de clubes bajo la marca Rackets Pro: el Estádio Universitário (EUL, con 12 pistas), Nacional Padel en pleno centro lisboeta, Quinta da Marinha en Cascais y centros universitarios.",
        "sedes_principales": [
            "Rackets Pro EUL - Estádio Universitário de Lisboa (12 pistas)",
            "Rackets Pro Nacional Padel (Lisboa Centro)",
            "Rackets Pro Quinta da Marinha (Cascais)",
            "Rackets Pro Saldanha (Lisboa Centro)",
            "Rackets Pro Nova - Campus Nova FCT (Caparica - 10 pistas cubiertas)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas cubiertas y exteriores con moqueta WPT",
            "software": "AirCourts (la app de reservas número uno en Portugal)",
            "domotica": "Control de accesos y tornos automatizados",
            "grabacion": "Cámaras en pistas centrales para el circuito de la FPP",
            "restauracion": "Clubhouses con terrazas soleadas, cafeterías saludables y tiendas técnicas"
        },
        "modelo_expansion": {
            "tipo_contrato": "Concesión de gestión deportiva en universidades y clubes náuticos",
            "perfil_club": "Instalaciones de primer orden en Lisboa y costa de Estoril",
            "canon_royalties": "Gestión corporativa",
            "inversion_media": "500.000€ a 1.500.000€"
        },
        "diferencial": "Ubicaciones privilegiadas en la capital portuguesa y exclusividad en campus universitarios."
    },
    {
        "id": "top-padel",
        "nombre": "Top-Padel / A-Z Padel",
        "pais": "Portugal",
        "pais_codigo": "PT",
        "region_filtro": "PT",
        "bandera": "🇵🇹",
        "ciudad_sede": "Oporto",
        "coords": [41.1579, -8.6291],
        "modelo": "Cadena Multiclub del Norte de Portugal (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "5 centros con el mismo nombre",
        "num_pistas": "35+ pistas",
        "software": "AirCourts / Playtomic",
        "fundadores": "Pioneros del pádel en el Gran Oporto",
        "web": "https://top-padel.pt",
        "tagline": "Pioneros absolutos del pádel indoor en el norte de Portugal.",
        "resumen": "Cadena pionera que opera bajo la enseña Top-Padel / AZ Padel. Abrieron el primer club indoor de Portugal junto a la desembocadura del río Duero (Top-Padel Fluvial) y macrocentros en la Zona Industrial de Oporto y Maia.",
        "sedes_principales": [
            "Top-Padel Industrial (Zona Industrial do Porto)",
            "Top-Padel Fluvial (Foz do Douro, junto al río Duero)",
            "AZ Padel Quinta do Fojo (Gaia)",
            "AZ Padel Maia (junto a la estación de metro)",
            "Polos asociados en Guimarães y Famalicão"
        ],
        "tecnologia_pistas": {
            "pistas": "Campos indoor con césped azul texturizado y alturas superiores a 9 metros",
            "software": "AirCourts",
            "domotica": "Acceso por app y reservas online sincronizadas",
            "grabacion": "Grabación en torneos de la Federación Portuguesa de Pádel",
            "restauracion": "Bares con menú ejecutivo, cervezas y terrazas con vistas al río"
        },
        "modelo_expansion": {
            "tipo_contrato": "Operación directa corporativa y alianzas inmobiliarias",
            "perfil_club": "Naves industriales y clubes fluviales en el área metropolitana de Oporto",
            "canon_royalties": "Gestión directa",
            "inversion_media": "600.000€ a 1.200.000€"
        },
        "diferencial": "Marca de referencia en el norte luso con la mayor comunidad de jugadores de Oporto."
    },

    # ─────────────────────────────────────────────────────────────
    # 🇺🇸 ESTADOS UNIDOS (6 Cadenas y Franquicias)
    # ─────────────────────────────────────────────────────────────
    {
        "id": "park-padel",
        "nombre": "Park Padel",
        "pais": "Estados Unidos",
        "pais_codigo": "US",
        "region_filtro": "US",
        "bandera": "🇺🇸",
        "ciudad_sede": "San Francisco (California)",
        "coords": [37.7749, -122.4194],
        "modelo": "Cadena Urbana en San Francisco (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "boutique",
        "num_clubs": "2 centros con el mismo nombre",
        "num_pistas": "8+ pistas",
        "software": "Playtomic USA",
        "fundadores": "Katie Blodgett y Jessica Talbert (Empresarias californianas)",
        "web": "https://parkpadel.com",
        "tagline": "Pioneras en llevar el pádel al corazón de San Francisco y Silicon Valley.",
        "resumen": "Park Padel es la primera cadena de pádel de San Francisco, fundada por mujeres empresarias en localizaciones icónicas frente a la bahía: en el histórico Palace of Fine Arts y en el Embarcadero Plaza. Foco en la comunidad tecnológica y clases de iniciación.",
        "sedes_principales": [
            "Park Padel Embarcadero Plaza (San Francisco)",
            "Park Padel Palace of Fine Arts (Marina District, San Francisco)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas de cristal de diseño integradas en monumentos históricos",
            "software": "Playtomic USA",
            "domotica": "Check-in digitalizado y reserva por app",
            "grabacion": "Grabación de jugadas para compartir en redes",
            "restauracion": "Puntos de café artesanal californiano y refrescos orgánicos"
        },
        "modelo_expansion": {
            "tipo_contrato": "Concesiones de espacios emblemáticos con autoridades portuarias y parques de SF",
            "perfil_club": "Suelos urbanos icónicos en San Francisco y el Área de la Bahía",
            "canon_royalties": "Cadena propia",
            "inversion_media": "500.000$ a 1.200.000$"
        },
        "diferencial": "Ubicación en los lugares más turísticos y exclusivos de San Francisco con un público tech de alto poder adquisitivo."
    },
    {
        "id": "padel-haus",
        "nombre": "Padel Haus",
        "pais": "Estados Unidos",
        "pais_codigo": "US",
        "region_filtro": "US",
        "bandera": "🇺🇸",
        "ciudad_sede": "Nueva York",
        "coords": [40.7128, -73.9600],
        "modelo": "Cadena Social & Athletic Club (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "5 centros en NY con el mismo nombre (+3 en obras)",
        "num_pistas": "32+ pistas",
        "software": "Padel Haus App",
        "fundadores": "Santiago Gomez (Empresario hostelero)",
        "web": "https://padel.haus",
        "tagline": "El club social de pádel que está conquistando Nueva York y las grandes urbes de EE.UU.",
        "resumen": "Cadena bajo la marca Padel Haus creada por Santiago Gomez. Pionero en NY con posicionamiento atlético y social: pistas de diseño, cafetería orgánica Juice Haus, saunas de contraste y vestuarios estilo Equinox.",
        "sedes_principales": [
            "Padel Haus Williamsburg South (Brooklyn, NY - insignia)",
            "Padel Haus Williamsburg North (Brooklyn, NY)",
            "Padel Haus DUMBO (Washington St, Brooklyn)",
            "Padel Haus Greenpoint (Berry St, Brooklyn - macrocentro)",
            "Padel Haus Nashville, Denver y Atlanta (en obras)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas de diseño AFP Courts personalizadas con colores de marca",
            "software": "App nativa Padel Haus con pasarela Stripe",
            "domotica": "Acceso biométrico y móvil para miembros",
            "grabacion": "Cámaras inteligentes en pista",
            "restauracion": "Juice Haus: café de especialidad, zumos cold-pressed y smoothies"
        },
        "modelo_expansion": {
            "tipo_contrato": "Desarrollo propio corporativo con rondas de capital riesgo",
            "perfil_club": "Naves urbanas de 2.000 a 4.500 m² en distritos de alta renta",
            "canon_royalties": "Capital institucional",
            "inversion_media": "2.5M$ a 5M$ por club"
        },
        "diferencial": "Estética impecable, comunidad influyente de Wall Street y tarifa de 50$-70$/hora."
    },
    {
        "id": "reserve-padel",
        "nombre": "Reserve Padel",
        "pais": "Estados Unidos",
        "pais_codigo": "US",
        "region_filtro": "US",
        "bandera": "🇺🇸",
        "ciudad_sede": "Miami",
        "coords": [25.7617, -80.1918],
        "modelo": "Cadena de Ultra-Lujo (Mismo Nombre)",
        "modelo_badge": "bg-purple-100 text-purple-800 border-purple-200",
        "tipo_categoria": "boutique",
        "escala": "boutique",
        "num_clubs": "4 centros exclusivos con el mismo nombre",
        "num_pistas": "22+ pistas",
        "software": "Reserve Padel App",
        "fundadores": "Wayne Boich",
        "web": "https://reservepadel.com",
        "tagline": "El epicentro del pádel de ultra-lujo, celebridades y la Reserve Cup.",
        "resumen": "Cadena bajo el nombre Reserve Padel creada por Wayne Boich en Miami y NY. Pop-ups y centros fijos en Miami Design District, Seaplane Base y Hudson Yards Manhattan, atrayendo a Beckham o Jimmy Butler. Organizan la Reserve Cup.",
        "sedes_principales": [
            "Reserve Padel SoLé Mia (North Miami, FL - permanente)",
            "Reserve Padel Miami Design District (Miami)",
            "Reserve Padel Miami Seaplane Base (MacArthur Causeway)",
            "Reserve Padel Hudson Yards (Manhattan, NY - 360 10th Ave)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas 'all black' con iluminación de diseño",
            "software": "App propia con membresía privada y lista de espera",
            "domotica": "Concierge VIP presencial",
            "grabacion": "Cobertura televisiva y grabación en alta definición",
            "restauracion": "Catering gourmet, champagne bar y lounge privado"
        },
        "modelo_expansion": {
            "tipo_contrato": "Explotación propia y desarrolladores inmobiliarios de lujo",
            "perfil_club": "Ubicaciones icónicas con vistas espectaculares",
            "canon_royalties": "Club cerrado",
            "inversion_media": "3M$ a 7M$"
        },
        "diferencial": "Exclusividad absoluta, presencia de estrellas mundiales y sponsors como Bentley y Hublot."
    },
    {
        "id": "ultra-padel",
        "nombre": "Ultra Padel Club",
        "pais": "Estados Unidos",
        "pais_codigo": "US",
        "region_filtro": "US",
        "bandera": "🇺🇸",
        "ciudad_sede": "Miami",
        "coords": [25.8290, -80.1900],
        "modelo": "Cadena de Macrocomplejos (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "grande",
        "num_clubs": "2 macrocomplejos con el mismo nombre",
        "num_pistas": "38+ pistas",
        "software": "Playtomic USA",
        "fundadores": "Moisés Cohen",
        "web": "https://ultrapadelclub.com",
        "tagline": "El macrocomplejo de pádel más grande de los Estados Unidos.",
        "resumen": "Cadena bajo la marca Ultra Padel en Magic City y Biscayne (Miami). Casi 30 pistas en una sola sede al aire libre y cubiertas, motor de la explosión del pádel en Florida y sede oficial de torneos USPA.",
        "sedes_principales": [
            "Ultra Padel Little River (Magic City, Miami - 29 pistas)",
            "Ultra Padel Biscayne (Miami, Florida)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con cubiertas térmicas tropicales",
            "software": "Playtomic USA",
            "domotica": "Torres de iluminación LED de competición y sonido envolvente",
            "grabacion": "Torretas de streaming para retransmisiones",
            "restauracion": "Restaurante mediterráneo, food trucks y terraza chill-out"
        },
        "modelo_expansion": {
            "tipo_contrato": "Operación directa e inversión inmobiliaria comercial",
            "perfil_club": "Parcelas de más de 15.000 m² para más de 15 pistas",
            "canon_royalties": "Gestión corporativa",
            "inversion_media": "2.5M$ a 4M$"
        },
        "diferencial": "Volumen masivo de pistas en un solo lugar y ambiente festivo latino-americano."
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
        "modelo": "Cadena Multiclub en California (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "3 centros con el mismo nombre",
        "num_pistas": "18+ pistas",
        "software": "Playtomic USA",
        "fundadores": "Gabriel Pérez Krieb, Armando Rodiel, Ryan Redondo",
        "web": "https://taktikapadel.com",
        "tagline": "Llevando el pádel a los mayores centros de tenis de California.",
        "resumen": "Cadena bajo la marca Taktika Padel en California. Instalaron complejos en el Barnes Tennis Center de San Diego y en el Dignity Health Sports Park de Los Ángeles (sede de LA Galaxy), atrayendo a público tech y de Hollywood.",
        "sedes_principales": [
            "Taktika Padel Barnes Tennis Center (San Diego, CA - 7 pistas)",
            "Taktika Padel Dignity Health Sports Park (Carson, Los Ángeles, CA)",
            "Taktika Padel Pacific Beach (San Diego)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con césped texturizado Mondo azul",
            "software": "Playtomic USA",
            "domotica": "Control digital de iluminación y check-in",
            "grabacion": "Streaming de campeonatos Pro Padel League (PPL)",
            "restauracion": "Cafeterías al aire libre y tiendas de material"
        },
        "modelo_expansion": {
            "tipo_contrato": "Alianzas estratégicas con macrocomplejos de tenis y estadios deportivos",
            "perfil_club": "Grandes recintos deportivos ya consolidados en California",
            "canon_royalties": "Concesión de espacio",
            "inversion_media": "600.000$ a 1.500.000$"
        },
        "diferencial": "Pioneros en el mercado californiano y sede oficial de franquicias de la Pro Padel League (PPL)."
    },
    {
        "id": "wynwood-padel-club",
        "nombre": "Wynwood Padel Club",
        "pais": "Estados Unidos",
        "pais_codigo": "US",
        "region_filtro": "US",
        "bandera": "🇺🇸",
        "ciudad_sede": "Miami (Wynwood)",
        "coords": [25.8042, -80.1989],
        "modelo": "Club Cultural & Urbano de Pádel",
        "modelo_badge": "bg-purple-100 text-purple-800 border-purple-200",
        "tipo_categoria": "boutique",
        "escala": "boutique",
        "num_clubs": "2 centros",
        "num_pistas": "12+ pistas",
        "software": "Playtomic USA",
        "fundadores": "Real Padel Miami / Wynwood Arts",
        "web": "https://wynwoodpadelclub.com",
        "tagline": "El club pionero que convirtió el arte urbano de Wynwood en la cuna del pádel de Miami.",
        "resumen": "Rodeado por los famosos murales de grafiti de Wynwood Arts District en Miami, fue uno de los primeros clubes en demostrar que el pádel en EE.UU. podía ser un fenómeno 'lifestyle'. Pistas de cristal rodeadas de arte urbano, cafetería con zumos naturales y torneos nocturnos.",
        "sedes_principales": [
            "Wynwood Arts District (NW 5th Ave, Miami - 8 pistas)",
            "Sede satélite en North Miami"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas de competición con murales de artistas locales en paredes perimetrales",
            "software": "Playtomic USA",
            "domotica": "Iluminación de discoteca y sonido envolvente para eventos",
            "grabacion": "Grabación de partidos para creadores de contenido",
            "restauracion": "Café restaurante con acai bowls, comida orgánica y cerveza artesanal"
        },
        "modelo_expansion": {
            "tipo_contrato": "Operación directa",
            "perfil_club": "Parcelas urbanas en distritos de moda",
            "canon_royalties": "Club privado",
            "inversion_media": "1M$ a 2M$"
        },
        "diferencial": "Auténtico corazón hipster y artístico del pádel en Florida con visibilidad mundial."
    },

    # ─────────────────────────────────────────────────────────────
    # 🇲🇽 MÉXICO Y SUDAMÉRICA (8 Cadenas)
    # ─────────────────────────────────────────────────────────────
    {
        "id": "padel-park-chile",
        "nombre": "Padel Park Chile",
        "pais": "Chile",
        "pais_codigo": "CL",
        "region_filtro": "MX",
        "bandera": "🇨🇱",
        "ciudad_sede": "Santiago de Chile",
        "coords": [-33.3800, -70.6600],
        "modelo": "Cadena Multiclub Recreativa (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "4 centros con el mismo nombre",
        "num_pistas": "24+ pistas",
        "software": "EasyCanchas",
        "fundadores": "Padel Park Chile SpA",
        "web": "https://padelpark.cl",
        "tagline": "Complejos deportivos familiares y escuelas con el mismo sello en Santiago y regiones.",
        "resumen": "Cadena de recintos bajo la misma marca Padel Park en comunas clave de Santiago (Huechuraba, Peñalolén) y centros en regiones como Concepción. Canchas panorámicas cubiertas y exteriores con un enfoque familiar y quinchos para asados.",
        "sedes_principales": [
            "Padel Park Huechuraba (Santiago - 8 canchas)",
            "Padel Park Peñalolén (Santiago)",
            "Padel Park Concepción",
            "Padel Park Viña del Mar"
        ],
        "tecnologia_pistas": {
            "pistas": "Canchas panorámicas de cristal templado y césped azul",
            "software": "EasyCanchas",
            "domotica": "Control digital de iluminación nocturna",
            "grabacion": "Grabación en torneos locales",
            "restauracion": "Quinchos para celebraciones familiares y bar deportivo"
        },
        "modelo_expansion": {
            "tipo_contrato": "Cadena propia bajo la marca Padel Park",
            "perfil_club": "Parcelas periurbanas de 4 a 8 canchas",
            "canon_royalties": "Cadena unificada",
            "inversion_media": "350.000$ a 700.000$"
        },
        "diferencial": "Excelente ambiente familiar y torneos de fin de semana para jugadores amateur de todos los niveles."
    },
    {
        "id": "brava-padel-brasil",
        "nombre": "Brava Padel",
        "pais": "Brasil",
        "pais_codigo": "BR",
        "region_filtro": "MX",
        "bandera": "🇧🇷",
        "ciudad_sede": "Balneário Camboriú / Itajaí",
        "coords": [-26.9926, -48.6352],
        "modelo": "Cadena Costera de Alto Nivel (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "boutique",
        "num_clubs": "2 macrocentros con el mismo nombre",
        "num_pistas": "16+ pistas",
        "software": "Let's Padel / WhatsApp",
        "fundadores": "Emprendedores de Santa Catarina",
        "web": "https://bravapadel.com.br",
        "tagline": "La cadena de pádel más famosa y vibrante del litoral sur de Brasil.",
        "resumen": "Balneário Camboriú y Praia Brava son el epicentro del lujo costero en Brasil. Brava Padel opera dos macrocomplejos con el mismo nombre donde el pádel convive con música en directo, comida brasileña de playa y torneos con los mejores jugadores del país.",
        "sedes_principales": [
            "Brava Padel Balneário Camboriú (Santa Catarina - 10 canchas)",
            "Brava Padel Itajaí (Praia Brava - 6 canchas panorámicas)"
        ],
        "tecnologia_pistas": {
            "pistas": "Canchas panorámicas cubiertas bajo naves de madera laminada y lonas tensadas",
            "software": "Let's Padel",
            "domotica": "Iluminación de discoteca y sonido profesional en canchas",
            "grabacion": "Cámaras para transmisión en streaming de torneos de la COBRAPA",
            "restauracion": "Bar de playa con açai, caipirinhas, sushi y carnes a la brasa"
        },
        "modelo_expansion": {
            "tipo_contrato": "Operación directa",
            "perfil_club": "Emplazamientos costeros y turísticos en el sur de Brasil",
            "canon_royalties": "Cadena privada",
            "inversion_media": "600.000$ a 1.200.000$"
        },
        "diferencial": "Ambiente festivo de playa único en el mundo con altísima asistencia de turistas y deportistas de élite."
    },
    {
        "id": "padel-co-mexico",
        "nombre": "Padel Co (Padel Company)",
        "pais": "México",
        "pais_codigo": "MX",
        "region_filtro": "MX",
        "bandera": "🇲🇽",
        "ciudad_sede": "Ciudad de México",
        "coords": [19.4326, -99.1332],
        "modelo": "Cadena Multiclub Urbana (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "4 centros con el mismo nombre (+3 en obras)",
        "num_pistas": "22+ pistas",
        "software": "Playtomic",
        "fundadores": "Padel Company México",
        "web": "https://padelco.mx",
        "tagline": "La cadena de pádel más moderna y concurrida de la capital mexicana.",
        "resumen": "Padel Co lidera la profesionalización en CDMX con clubes todos bajo la marca Padel Co en Polanco, Reforma y Santa Fe, combinando canchas cubiertas y semi-indoor con servicio de bar y terraza social.",
        "sedes_principales": [
            "Padel Co Polanco (CDMX)",
            "Padel Co Reforma (CDMX)",
            "Padel Co Santa Fe (CDMX)",
            "Padel Co San Miguel Chapultepec y Tacubaya"
        ],
        "tecnologia_pistas": {
            "pistas": "Canchas panorámicas con cubiertas térmicas de lona tensada",
            "software": "Playtomic",
            "domotica": "Check-in móvil y taquillas electrónicas",
            "grabacion": "Cámaras en canchas centrales",
            "restauracion": "Restaurante con comida mexicana de autor, micheladas y coctelería"
        },
        "modelo_expansion": {
            "tipo_contrato": "Desarrollo propio corporativo bajo la misma marca",
            "perfil_club": "Terrenos urbanos en colonias de alto poder adquisitivo de CDMX",
            "canon_royalties": "Operación directa",
            "inversion_media": "800.000$ a 1.800.000$ por club"
        },
        "diferencial": "Presencia en las mejores zonas de la capital mexicana y una comunidad de ejecutivos de primer nivel."
    },
    {
        "id": "altapadel-mexico",
        "nombre": "Altapadel",
        "pais": "México",
        "pais_codigo": "MX",
        "region_filtro": "MX",
        "bandera": "🇲🇽",
        "ciudad_sede": "Ciudad de México / Querétaro",
        "coords": [19.3089, -99.2014],
        "modelo": "Cadena Nacional de Competición (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "4 centros con el mismo nombre",
        "num_pistas": "20+ pistas",
        "software": "Playtomic",
        "fundadores": "Altapadel Group México",
        "web": "https://altapadel.com.mx",
        "tagline": "Canchas avaladas por federaciones con la mejor escuela técnica de México.",
        "resumen": "Cadena bajo la marca Altapadel en el Pedregal de San Ángel (CDMX), Interlomas, Querétaro y Puebla. Estándares federativos de la FEMEPA, canchas con cristal de 12 mm y preparación de promesas.",
        "sedes_principales": [
            "Altapadel Pedregal (CDMX - 6 canchas)",
            "Altapadel Interlomas",
            "Altapadel Querétaro",
            "Altapadel Puebla"
        ],
        "tecnologia_pistas": {
            "pistas": "Canchas avaladas por la FEMEPA con pasto sintético texturizado",
            "software": "Playtomic",
            "domotica": "Iluminación LED sin sombras para juego nocturno",
            "grabacion": "Grabación de partidos para torneos de circuito nacional",
            "restauracion": "Terraza lounge con asador y pro-shop con marcas europeas"
        },
        "modelo_expansion": {
            "tipo_contrato": "Franquicia de gestión y clubes propios",
            "perfil_club": "Instalaciones de 4 a 8 canchas en zonas residenciales",
            "canon_royalties": "Canon de marca ~20.000$ y royalties del 5%",
            "inversion_media": "350.000$ a 750.000$"
        },
        "diferencial": "Fuerte enfoque en torneos competitivos y escuela de menores con entrenadores certificados."
    },
    {
        "id": "contrapared-mexico",
        "nombre": "Contrapared",
        "pais": "México",
        "pais_codigo": "MX",
        "region_filtro": "MX",
        "bandera": "🇲🇽",
        "ciudad_sede": "Ciudad de México (Santa Fe)",
        "coords": [19.3580, -99.2610],
        "modelo": "Cadena Boutique de Estilo de Vida (Mismo Nombre)",
        "modelo_badge": "bg-purple-100 text-purple-800 border-purple-200",
        "tipo_categoria": "boutique",
        "escala": "boutique",
        "num_clubs": "2 centros con el mismo nombre",
        "num_pistas": "12+ pistas",
        "software": "Playtomic",
        "fundadores": "Contrapared Club SAPI",
        "web": "https://contrapared.mx",
        "tagline": "La experiencia de pádel más sofisticada y social del poniente de CDMX.",
        "resumen": "Cadena en Santa Fe e Interlomas. Canchas cubiertas de primer orden, bar de mixología, vestuarios con spa y pro shop.",
        "sedes_principales": [
            "Contrapared Santa Fe (CDMX - 6 canchas)",
            "Contrapared Bosques (CDMX - 6 canchas)"
        ],
        "tecnologia_pistas": {
            "pistas": "Canchas panorámicas con alturas superiores a 9 metros",
            "software": "Playtomic",
            "domotica": "Control digital de iluminación y clima",
            "grabacion": "Cámaras en cancha para descarga en el móvil",
            "restauracion": "Restaurante con terraza grill, coctelería y pantallas para eventos"
        },
        "modelo_expansion": {
            "tipo_contrato": "Operación directa",
            "perfil_club": "Terrenos prémium en el poniente de Ciudad de México",
            "canon_royalties": "Club privado",
            "inversion_media": "1.2M$ a 2.5M$"
        },
        "diferencial": "Exclusividad, diseño arquitectónico contemporáneo y clientela corporativa de Santa Fe."
    },
    {
        "id": "club-conecta-chile",
        "nombre": "Club Conecta",
        "pais": "Chile",
        "pais_codigo": "CL",
        "region_filtro": "MX",
        "bandera": "🇨🇱",
        "ciudad_sede": "Santiago de Chile",
        "coords": [-33.4489, -70.6693],
        "modelo": "Cadena Multiclub Líder en Chile (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "5 grandes complejos con el mismo nombre",
        "num_pistas": "32+ pistas",
        "software": "EasyCanchas",
        "fundadores": "Conecta Padel Group Chile",
        "web": "https://clubconecta.cl",
        "tagline": "La red de clubes multisede líder indiscutible en el mercado chileno.",
        "resumen": "Cadena con la misma marca Club Conecta en el sector oriente de Santiago (La Dehesa, Las Condes, Chicureo). El 40% del tiempo se pasa en el quincho de asados tras el partido.",
        "sedes_principales": [
            "Club Conecta La Dehesa (Santiago - 10 canchas)",
            "Club Conecta Las Condes (Santiago)",
            "Club Conecta Chicureo (Colina)",
            "Club Conecta Lo Barnechea",
            "Sedes en regiones"
        ],
        "tecnologia_pistas": {
            "pistas": "Canchas panorámicas con césped texturizado azul y cubiertas para la lluvia de invierno",
            "software": "EasyCanchas (la plataforma dominante de reservas en Chile)",
            "domotica": "Control automático de encendido de iluminación LED",
            "grabacion": "Cámaras en canchas centrales para transmisión de torneos",
            "restauracion": "Quincho chileno para asados, cafetería y pro-shop con marcas internacionales"
        },
        "modelo_expansion": {
            "tipo_contrato": "Desarrollo propio corporativo y franquicias asociadas",
            "perfil_club": "Parcelas de 4 a 10 canchas en comunas de alta renta",
            "canon_royalties": "Operación directa",
            "inversion_media": "500.000$ a 1.200.000$"
        },
        "diferencial": "La mayor comunidad de jugadores de Santiago y los mejores quinchos para el tercer tiempo."
    },
    {
        "id": "capital-padel-chile",
        "nombre": "Capital Padel",
        "pais": "Chile",
        "pais_codigo": "CL",
        "region_filtro": "MX",
        "bandera": "🇨🇱",
        "ciudad_sede": "Santiago de Chile",
        "coords": [-33.4500, -70.6800],
        "modelo": "Cadena Multiclub Urbana (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "3 centros con el mismo nombre",
        "num_pistas": "18+ pistas",
        "software": "EasyCanchas",
        "fundadores": "Capital Padel SpA",
        "web": "https://capitalpadel.cl",
        "tagline": "Pádel cubierto en el corazón urbano de Santiago de Chile.",
        "resumen": "Cadena bajo la marca Capital Padel en el centro neurálgico de Santiago (Santiago Centro, Estación Central, Maipú). Canchas cubiertas para jugar con lluvia o calor estival con tarifas accesibles.",
        "sedes_principales": [
            "Capital Padel Santiago Centro (8 canchas cubiertas)",
            "Capital Padel Estación Central",
            "Capital Padel Maipú"
        ],
        "tecnologia_pistas": {
            "pistas": "Canchas techadas de estructura metálica con cristal de 10 y 12 mm",
            "software": "EasyCanchas",
            "domotica": "Iluminación automatizada por cancha",
            "grabacion": "Sistemas de vídeo para clínics",
            "restauracion": "Cafetería y tienda de arriendo de palas"
        },
        "modelo_expansion": {
            "tipo_contrato": "Operación propia",
            "perfil_club": "Naves y galpones urbanos de 4 a 8 canchas",
            "canon_royalties": "Gestión directa",
            "inversion_media": "300.000$ a 600.000$"
        },
        "diferencial": "Pioneros en masificar el pádel en el centro urbano de Santiago con altísima tasa de ocupación."
    },
    {
        "id": "el-monasterio-argentina",
        "nombre": "El Monasterio Padel",
        "pais": "Argentina",
        "pais_codigo": "AR",
        "region_filtro": "MX",
        "bandera": "🇦🇷",
        "ciudad_sede": "Buenos Aires",
        "coords": [-34.6037, -58.3816],
        "modelo": "La Cuna Histórica del Pádel Mundial",
        "modelo_badge": "bg-blue-100 text-blue-800 border-blue-200",
        "tipo_categoria": "corporativo",
        "escala": "boutique",
        "num_clubs": "2 sedes históricas",
        "num_pistas": "14+ pistas",
        "software": "Padel Network / WhatsApp",
        "fundadores": "Pioneros históricos del pádel argentino en los años 90",
        "web": "https://elmonasteriopadel.com.ar",
        "tagline": "El templo donde se forjaron las mayores leyendas mundiales del pádel.",
        "resumen": "El Monasterio es una institución mítica en Buenos Aires con dos sedes históricas bajo el mismo nombre. De aquí salieron leyendas mundiales; canchas de cristal y cantera inagotable.",
        "sedes_principales": [
            "El Monasterio Almagro (Buenos Aires - 8 pistas)",
            "El Monasterio Norte (Buenos Aires - 6 pistas)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas de cristal templado y césped sintético rápido de competición",
            "software": "Sistemas locales de reserva digital",
            "domotica": "Iluminación LED de alta potencia",
            "grabacion": "Grabación de finales de circuito AJPP",
            "restauracion": "Parrilla argentina tradicional con asados post-partido y buffet de club"
        },
        "modelo_expansion": {
            "tipo_contrato": "Operación histórica propia",
            "perfil_club": "Centros urbanos bonaerenses",
            "canon_royalties": "Club histórico",
            "inversion_media": "200.000$ a 500.000$"
        },
        "diferencial": "El misticismo y la historia viva del deporte: todo jugador profesional argentino ha pisado sus pistas."
    },

    # ─────────────────────────────────────────────────────────────
    # 🇦🇪 ORIENTE MEDIO (4 Cadenas y Franquicias)
    # ─────────────────────────────────────────────────────────────
    {
        "id": "padel-in-gulf",
        "nombre": "Padel IN",
        "pais": "Catar, Kuwait y Arabia Saudí",
        "pais_codigo": "QA",
        "region_filtro": "AE",
        "bandera": "🇶🇦",
        "ciudad_sede": "Doha / Kuwait / Riad",
        "coords": [25.2854, 51.5310],
        "modelo": "Cadena Multiclub del Golfo (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "grande",
        "num_clubs": "15+ centros con el mismo nombre",
        "num_pistas": "70+ pistas cubiertas",
        "software": "App Propia Padel IN",
        "fundadores": "Empresarios cataríes y kuwaitíes vinculados al deporte",
        "web": "https://padelin.com",
        "tagline": "La red de clubes cubiertos climatizados más extensa de Oriente Medio.",
        "resumen": "Cadena que opera bajo la marca Padel IN en Catar, Kuwait y Arabia Saudí. Naves monumentales climatizadas a 21°C para jugar bajo los 48°C del desierto. Sede insignia en Aspire Zone (Doha).",
        "sedes_principales": [
            "Padel IN Aspire Zone (Doha, Catar - sede insignia de torneos)",
            "Padel IN Al Khor y Al Wakrah (Catar)",
            "Padel IN Kuwait (Mishref / Yarmouk Club)",
            "Padel IN Riad y Yeda (Arabia Saudí)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas WPT climatizadas a 21°C con sistemas HVAC de alta capacidad",
            "software": "App nativa Padel IN para reservas y torneos",
            "domotica": "Sistemas inteligentes de control de temperatura y luz",
            "grabacion": "Transmisión televisiva en directo y pantallas gigantes en clubhouse",
            "restauracion": "Cafeterías premium con zumos naturales, café árabe de especialidad y zonas VIP"
        },
        "modelo_expansion": {
            "tipo_contrato": "Máster franquicia nacional y centros propios con el mismo nombre",
            "perfil_club": "Megagolfos y naves industriales de 6 a 12 pistas con gran altura",
            "canon_royalties": "Canon de máster franquicia regional y 5% de royalties",
            "inversion_media": "1.5M$ a 4M$ por complejo"
        },
        "diferencial": "Dominio absoluto del mercado institucional y residencial en Catar, Kuwait y Arabia Saudí."
    },
    {
        "id": "world-padel-academy-uae",
        "nombre": "World Padel Academy (WPA)",
        "pais": "Emiratos Árabes Unidos y Bahréin",
        "pais_codigo": "AE",
        "region_filtro": "AE",
        "bandera": "🇦🇪",
        "ciudad_sede": "Dubái (Al Quoz)",
        "coords": [25.1430, 55.2280],
        "modelo": "Cadena de Academias de Alto Rendimiento (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "4 grandes academias con el mismo nombre",
        "num_pistas": "35+ pistas",
        "software": "Playtomic / WPA App",
        "fundadores": "Ali Al-Arif y socios emiratíes",
        "web": "https://worldpadelacademy.com",
        "tagline": "El estándar de oro en academias de pádel y pistas cubiertas en Dubái.",
        "resumen": "Cadena de academias bajo el nombre World Padel Academy (WPA) en Dubái (Al Quoz), Sharjah y Bahréin. Pistas cubiertas de alta competición climatizadas y entrenadores españoles de élite.",
        "sedes_principales": [
            "WPA Dubai Flagship (Al Quoz 1, Dubái - 10 pistas indoor)",
            "WPA Sharjah (Emiratos Árabes Unidos)",
            "WPA Bahréin (Manama)",
            "Centros corporativos en Abu Dabi"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas con césped Mondo Supercourt WPT y salidas de pista reglamentarias",
            "software": "Playtomic y app propia WPA",
            "domotica": "Climatización industrial a prueba del verano de Dubái",
            "grabacion": "Pistas con cámaras HD y análisis biomecánico de golpes",
            "restauracion": "Match Point Café: comida saludable, batidos energéticos y pro-shop completa"
        },
        "modelo_expansion": {
            "tipo_contrato": "Franquicia de academia y gestión de complejos deportivos",
            "perfil_club": "Naves de 6 a 12 pistas con espacio para escuela de tecnificación",
            "canon_royalties": "Canon de adhesión ~30.000$ y royalties del 5%",
            "inversion_media": "1M$ a 2.5M$"
        },
        "diferencial": "El mejor cuerpo técnico de entrenadores españoles en Oriente Medio y sede de eventos institucionales."
    },
    {
        "id": "padel-pro-uae",
        "nombre": "Padel Pro UAE",
        "pais": "Emiratos Árabes Unidos",
        "pais_codigo": "AE",
        "region_filtro": "AE",
        "bandera": "🇦🇪",
        "ciudad_sede": "Dubái",
        "coords": [25.2048, 55.2708],
        "modelo": "Cadena Multiclub Urbana en Dubái (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "4 clubes con el mismo nombre",
        "num_pistas": "20+ pistas",
        "software": "Playtomic",
        "fundadores": "Hussein El-Reda y socios",
        "web": "https://padelpro.ae",
        "tagline": "Pioneros del pádel en Dubái con sedes en los distritos financieros y residenciales.",
        "resumen": "Cadena con 4 clubes todos bajo la marca Padel Pro en Dubái: Al Quoz, One Central (junto al World Trade Centre), Jumeirah Park y Mirdif. Destino de expatriados y profesionales.",
        "sedes_principales": [
            "Padel Pro Al Quoz (Dubái)",
            "Padel Pro One Central (DWTCA - World Trade Centre, Dubái)",
            "Padel Pro Jumeirah Park (Dubái)",
            "Padel Pro Sports Society (Mirdif, Dubái)"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas cubiertas y descubiertas con césped azul texturizado",
            "software": "Playtomic",
            "domotica": "Check-in móvil rápido y control de climatización",
            "grabacion": "Grabación en torneos de fin de semana",
            "restauracion": "Zonas chill-out con bebidas frías y pro-shop oficial"
        },
        "modelo_expansion": {
            "tipo_contrato": "Operación directa y colaboraciones con desarrolladores de Dubái",
            "perfil_club": "Centros de 4 a 6 pistas en comunidades residenciales de alta renta",
            "canon_royalties": "Gestión propia",
            "inversion_media": "600.000$ a 1.500.000$"
        },
        "diferencial": "Ubicaciones céntricas inmejorables en los principales centros de negocios y residencias de Dubái."
    },
    {
        "id": "just-padel-uae",
        "nombre": "Just Padel UAE",
        "pais": "Emiratos Árabes Unidos",
        "pais_codigo": "AE",
        "region_filtro": "AE",
        "bandera": "🇦🇪",
        "ciudad_sede": "Dubái",
        "coords": [25.2600, 55.3000],
        "modelo": "Cadena de Clubs en Destinos de Ocio (Mismo Nombre)",
        "modelo_badge": "bg-sky-100 text-sky-800 border-sky-200",
        "tipo_categoria": "cadena",
        "escala": "media",
        "num_clubs": "5 ubicaciones con el mismo nombre",
        "num_pistas": "22+ pistas",
        "software": "Playtomic / Padel Mates",
        "fundadores": "Just Padel Sports Services",
        "web": "https://justpadel.ae",
        "tagline": "Pistas en los destinos costeros y de compras más vibrantes de Dubái.",
        "resumen": "Cadena bajo la marca Just Padel en lugares icónicos de Dubái como el puerto de Mina Rashid, Dubai Festival City y Ripe Market, integrando el deporte en planes familiares.",
        "sedes_principales": [
            "Just Padel Mina Rashid (Dubái)",
            "Just Padel Dubai Festival City",
            "Just Padel Ripe Market / Police Academy",
            "Just Padel Kite Beach"
        ],
        "tecnologia_pistas": {
            "pistas": "Pistas panorámicas al aire libre y cubiertas con cubiertas ligeras",
            "software": "Playtomic y Padel Mates",
            "domotica": "Iluminación sincronizada",
            "grabacion": "Grabaciones para contenido en redes sociales",
            "restauracion": "Sinergia con food trucks, cafeterías de playa y mercados al aire libre"
        },
        "modelo_expansion": {
            "tipo_contrato": "Concesiones temporales y permanentes en destinos de ocio",
            "perfil_club": "Zonas de alto tráfico peatonal y turístico en Dubái",
            "canon_royalties": "Gestión corporativa",
            "inversion_media": "400.000$ a 900.000$"
        },
        "diferencial": "Ambiente relajado junto al mar y los destinos turísticos más concurridos de los Emiratos."
    }
]

def render_html():
    franquicias_json = json.dumps(FRANQUICIAS, ensure_ascii=False)
    
    total_franquicias = len(FRANQUICIAS)
    paises_unicos = len(set(f["pais"] for f in FRANQUICIAS))
    
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
        region = f.get("region_filtro", f["pais_codigo"])
        escala = f["escala"]
        
        cards_html += f"""
        <article class="franchise-card bg-white rounded-3xl p-6 sm:p-7 border border-slate-200/90 shadow-sm hover:shadow-xl hover:border-slate-300 transition-all duration-300 flex flex-col justify-between group cursor-pointer"
                 data-id="{fid}"
                 data-nombre="{nombre.lower()}"
                 data-region="{region}"
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
          <td class="py-4 px-4 text-xs font-bold text-slate-700">{f['ciudad_sede']} ({f['pais']})</td>
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
  <title>Directorio de Cadenas de Clubs y Franquicias de Pádel (+1 Club) | CoolPadel Studios</title>
  <meta name="description" content="Directorio y mapa de las mayores cadenas de clubs con varias sedes abiertas bajo el mismo nombre y franquicias de pádel (+1 club). Datos de sedes, modelos, software e inversión.">
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
  <meta property="og:title" content="Directorio de Cadenas de Clubs y Franquicias de Pádel (+1 Club) | Censo Mundial">
  <meta property="og:description" content="Guía de operadores multi-club y cadenas con varias sedes abiertas bajo el mismo nombre en España, Europa, América y Golfo Pérsico.">
  <meta property="og:image" content="https://coolpadelstudios.com/assets/images/savemyplay-1.jpg">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Directorio de Cadenas y Franquicias de Pádel (+1 Club)">
  <meta name="twitter:description" content="Censo mundial de cadenas de clubs con varias sedes abiertas con el mismo nombre y franquicias en 18 países.">
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
            "name": "Cadenas y Franquicias de Pádel",
            "item": "https://coolpadelstudios.com/franquicias-padel/"
          }}
        ]
      }},
      {{
        "@type": "ItemList",
        "name": "Directorio de Cadenas de Clubs y Franquicias de Pádel (+1 Club)",
        "description": "Censo internacional exhaustivo de {total_franquicias} cadenas de clubes con varios centros abiertos bajo el mismo nombre y franquicias en 18 países.",
        "numberOfItems": {total_franquicias}
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "¿Qué cuenta como cadena de clubs de pádel?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Incluye tanto franquicias tradicionales como operadores y cadenas de clubes que tienen más de un club abierto y en funcionamiento bajo el mismo nombre comercial o enseña de marca (ej. Pàdel 7, All In Padel, Rocket Padel, InterPadel, PadelHaus, etc.)."
            }}
          }},
          {{
            "@type": "Question",
            "name": "¿Cuáles son las mayores cadenas de pádel del mundo?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Entre las cadenas más grandes destacan LeDap / We Are Padel (+650 pistas), BamVolea (+260 pistas), PDL Padel United (+500 pistas), The Padellers (+145 pistas), 4PADEL (+135 pistas), Peakz Padel (+110 pistas) y Padel IN (+70 pistas cubiertas)."
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
    #map {{ height: 530px; width: 100%; border-radius: 1.5rem; z-index: 10; }}
    @media (max-width: 640px) {{
      #map {{ height: 400px; border-radius: 1rem; }}
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
          Directorio Global
        </span>
        
        <a href="https://wa.me/34680317486?text=Hola%20Javier%2C%20estoy%20viendo%20el%20directorio%20global%20de%20cadenas%20de%20p%C3%A1del%20y%20me%20gustar%C3%ADa%20hacerte%20una%20consulta" target="_blank" class="inline-flex items-center gap-2 px-3.5 sm:px-5 py-2 sm:py-2.5 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs sm:text-sm tracking-wider uppercase transition shadow-sm hover:scale-105 active:scale-95">
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
          <span class="text-[#f2920b]">Cadenas y Franquicias de Pádel</span>
        </nav>

        <div class="max-w-4xl space-y-4">
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-slate-900 text-white font-heading font-bold text-xs uppercase tracking-wider">
            <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
            <span>CENSO MUNDIAL B2B · CADENAS DE CLUBS CON EL MISMO NOMBRE Y FRANQUICIAS (+1 SEDE)</span>
          </div>

          <h1 class="font-heading font-black text-3xl sm:text-5xl lg:text-6xl text-slate-950 leading-[1.08] uppercase tracking-tight">
            Directorio de Cadenas de Clubs y Franquicias de Pádel
          </h1>

          <p class="text-base sm:text-xl text-slate-600 font-medium leading-relaxed">
            El censo internacional más exhaustivo para operadores y propietarios: <strong>{total_franquicias} cadenas de clubes con varios centros abiertos bajo el mismo nombre</strong> y franquicias analizadas en 18 países. Sedes activas, requisitos de inversión, software de gestión y modelos de rentabilidad.
          </p>
        </div>

        <!-- KPI BANNER -->
        <div class="grid grid-cols-2 lg:grid-cols-4 gap-3.5 sm:gap-6 mt-8 sm:mt-10 pt-8 border-t border-slate-200/80">
          <div class="bg-white p-5 rounded-2xl border border-slate-200/80 shadow-xs">
            <span class="block text-xs font-bold uppercase tracking-wider text-slate-400 mb-1">Cadenas / Franquicias</span>
            <span class="font-heading font-black text-3xl sm:text-4xl text-slate-950">{total_franquicias}</span>
            <span class="text-xs text-slate-500 font-medium">Con +1 club abierto</span>
          </div>
          
          <div class="bg-white p-5 rounded-2xl border border-slate-200/80 shadow-xs">
            <span class="block text-xs font-bold uppercase tracking-wider text-slate-400 mb-1">Pistas Totales</span>
            <span class="font-heading font-black text-3xl sm:text-4xl text-slate-950">+3.750</span>
            <span class="text-xs text-slate-500 font-medium">Bajo gestión analizada</span>
          </div>

          <div class="bg-white p-5 rounded-2xl border border-slate-200/80 shadow-xs">
            <span class="block text-xs font-bold uppercase tracking-wider text-slate-400 mb-1">Presencia Global</span>
            <span class="font-heading font-black text-3xl sm:text-4xl text-slate-950">{paises_unicos} Países</span>
            <span class="text-xs text-slate-500 font-medium">Europa, América y Oriente Medio</span>
          </div>

          <div class="bg-white p-5 rounded-2xl border border-slate-200/80 shadow-xs">
            <span class="block text-xs font-bold uppercase tracking-wider text-slate-400 mb-1">Tipologías</span>
            <span class="font-heading font-black text-3xl sm:text-4xl text-[#f2920b]">Mismo Nombre</span>
            <span class="text-xs text-slate-500 font-medium">Cadenas de marca y franquicias</span>
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
            <input type="text" id="searchInput" placeholder="Buscar por cadena, club, ciudad, país o software (ej. Padel 7, Playtomic, Tsonga, Bristol, EasyCanchas)..."
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

        <!-- Filtros por Región/País y Categoría -->
        <div class="flex flex-col gap-4 pt-3 border-t border-slate-100">
          
          <!-- Filtro Región / País -->
          <div class="flex items-center gap-1.5 flex-wrap">
            <span class="text-xs font-bold uppercase text-slate-400 mr-1 flex items-center gap-1">
              <i data-lucide="globe" class="w-3.5 h-3.5"></i>
              <span>Región:</span>
            </span>
            <button onclick="setRegionFilter('all')" class="filter-region-btn active px-3 py-1 rounded-lg text-xs font-bold bg-[#f2920b] text-slate-950 transition" data-region="all">Todos ({total_franquicias})</button>
            <button onclick="setRegionFilter('ES')" class="filter-region-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-region="ES">🇪🇸 España (13)</button>
            <button onclick="setRegionFilter('FR')" class="filter-region-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-region="FR">🇫🇷 Francia (7)</button>
            <button onclick="setRegionFilter('IT')" class="filter-region-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-region="IT">🇮🇹 Italia (5)</button>
            <button onclick="setRegionFilter('PT')" class="filter-region-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-region="PT">🇵🇹 Portugal (2)</button>
            <button onclick="setRegionFilter('SE')" class="filter-region-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-region="SE">🇸🇪 Nórdicos (8)</button>
            <button onclick="setRegionFilter('NL')" class="filter-region-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-region="NL">🇳🇱 Países Bajos, BE & AT (5)</button>
            <button onclick="setRegionFilter('DE')" class="filter-region-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-region="DE">🇩🇪 Alemania (1)</button>
            <button onclick="setRegionFilter('GB')" class="filter-region-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-region="GB">🇬🇧 Reino Unido (6)</button>
            <button onclick="setRegionFilter('US')" class="filter-region-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-region="US">🇺🇸 EE.UU. (6)</button>
            <button onclick="setRegionFilter('MX')" class="filter-region-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-region="MX">🇲🇽 México, CL, AR, BR (8)</button>
            <button onclick="setRegionFilter('AE')" class="filter-region-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-region="AE">🇦🇪 Oriente Medio (4)</button>
          </div>

          <!-- Filtro Modelo / Tipo de Operador -->
          <div class="flex items-center gap-1.5 flex-wrap">
            <span class="text-xs font-bold uppercase text-slate-400 mr-1 flex items-center gap-1">
              <i data-lucide="tag" class="w-3.5 h-3.5"></i>
              <span>Tipo de Operador:</span>
            </span>
            <button onclick="setModelFilter('all')" class="filter-model-btn active px-3 py-1 rounded-lg text-xs font-bold bg-slate-900 text-white transition" data-model="all">Todos</button>
            <button onclick="setModelFilter('cadena')" class="filter-model-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-model="cadena">Cadena Multiclub (Mismo Nombre)</button>
            <button onclick="setModelFilter('corporativo')" class="filter-model-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-model="corporativo">Red Corporativa Propia</button>
            <button onclick="setModelFilter('franquicia')" class="filter-model-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-model="franquicia">Franquicia Llave en Mano</button>
            <button onclick="setModelFilter('automatizado')" class="filter-model-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-model="automatizado">Club 100% Automatizado 24/7</button>
            <button onclick="setModelFilter('boutique')" class="filter-model-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-model="boutique">Boutique & Ultra-Lujo</button>
            <button onclick="setModelFilter('licencia')" class="filter-model-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-model="licencia">Academia / Pro-Shop</button>
          </div>

        </div>

        <!-- Contador de resultados -->
        <div class="flex items-center justify-between text-xs font-semibold text-slate-500 pt-2 border-t border-slate-100">
          <span id="resultsCount">Mostrando {total_franquicias} cadenas y franquicias</span>
          <span class="text-slate-400 hidden sm:inline">Haz clic en cualquier tarjeta o chincheta del mapa para ver el dossier completo</span>
        </div>

      </div>

      <!-- MAPA INTERACTIVO -->
      <div id="mapContainer" class="bg-white p-3 sm:p-4 rounded-3xl border border-slate-200/90 shadow-sm mb-10 relative">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between px-3 py-2 mb-2 gap-2">
          <div class="flex items-center gap-2">
            <span class="w-2.5 h-2.5 rounded-full bg-[#f2920b]"></span>
            <h2 class="font-heading font-black text-sm sm:text-base text-slate-900 uppercase tracking-wider">
              Mapa Mundial de Sedes Principales & Cadenas
            </h2>
          </div>
          <div class="flex items-center gap-1.5 text-xs font-bold flex-wrap">
            <button onclick="resetMapView()" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 transition">
              Europa
            </button>
            <button onclick="zoomToSpain()" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 transition">
              España
            </button>
            <button onclick="zoomToFrance()" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 transition">
              Francia
            </button>
            <button onclick="zoomToItaly()" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 transition">
              Italia
            </button>
            <button onclick="zoomToUSA()" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 transition">
              EE.UU.
            </button>
            <button onclick="zoomToLatam()" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 transition">
              México/Latam
            </button>
            <button onclick="zoomToMiddleEast()" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 transition">
              Oriente Medio
            </button>
          </div>
        </div>

        <div id="map"></div>

        <div class="flex items-center justify-center gap-4 flex-wrap pt-3 text-[11px] font-bold text-slate-500">
          <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-full bg-[#0284c7]"></span> Cadena Mismo Nombre</span>
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
                <th class="py-4 px-4">Cadena / Franquicia</th>
                <th class="py-4 px-4">Modelo</th>
                <th class="py-4 px-4">Sede / País</th>
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
            ¿Qué Modelo de Cadena o Franquicia es el Más Rentable?
          </h2>
          <p class="text-slate-600 text-sm sm:text-base leading-relaxed">
            El sector del pádel ha dejado atrás la era amateur. Hoy existen modelos consolidados para operar múltiples clubes con alta rentabilidad sobre el capital invertido (ROIC).
          </p>
        </div>

        <div class="grid md:grid-cols-2 gap-6 sm:gap-8">
          
          <!-- Bloque 1 -->
          <div class="bg-slate-50 p-6 sm:p-8 rounded-3xl border border-slate-200/90 hover:shadow-md transition">
            <div class="w-10 h-10 rounded-xl bg-sky-600 text-white flex items-center justify-center font-heading font-black text-lg mb-4">
              1
            </div>
            <h3 class="font-heading font-black text-xl text-slate-950 mb-2">Cadena Multiclub con el Mismo Nombre</h3>
            <p class="text-slate-600 text-sm leading-relaxed mb-4">
              Cadenas como <strong>Pàdel 7</strong> en Barcelona, <strong>All In Padel</strong> en Francia o <strong>InterPadel</strong> en Noruega abren varios centros bajo su propia marca comercial. No cobran royalties a terceros; reinvierten su flujo de caja en abrir nuevas naves en barrios estratégicos para dominar una provincia o país.
            </p>
            <div class="text-xs font-bold text-sky-700 bg-sky-50 p-3 rounded-xl border border-sky-100">
              💡 Ventaja: Control absoluto de la experiencia de marca y economías de escala locales en personal y marketing.
            </div>
          </div>

          <!-- Bloque 2 -->
          <div class="bg-slate-50 p-6 sm:p-8 rounded-3xl border border-slate-200/90 hover:shadow-md transition">
            <div class="w-10 h-10 rounded-xl bg-emerald-600 text-white flex items-center justify-center font-heading font-black text-lg mb-4">
              2
            </div>
            <h3 class="font-heading font-black text-xl text-slate-950 mb-2">Club Automatizado 24/7 sin Personal</h3>
            <p class="text-slate-600 text-sm leading-relaxed mb-4">
              Franquicias como <strong>Click & Padel</strong> o <strong>Padel Time</strong> reducen el personal presencial mediante cerraduras electromagnéticas, códigos QR temporales, encendido automático de luces e integración directa con Playtomic.
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
              Modelos como <strong>Padel Haus</strong> o <strong>Reserve</strong> en EE.UU., <strong>Padel Palace</strong> o <strong>City Padel</strong> en Milán, y <strong>The Padellers</strong> en Países Bajos entienden que el pádel es un fenómeno social y de estatus. El 35% al 50% de la facturación proviene del bar, restaurante, cafetería orgánica, eventos de empresa y torneos afterwork.
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
              Marcas como la <strong>Paquito Navarro Academy</strong>, <strong>Bela Padel Center</strong> o la red de corners <strong>Club Pádel Nuestro</strong> permiten a clubes ya en marcha franquiciar solo una sección (la escuela o la tienda del club), disparando los ingresos por alumno y profesionalizando el inventario de material.
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
          TECNOLOGÍA & MERCHANDISING PARA CADENAS Y FRANQUICIAS
        </span>

        <h2 class="font-heading font-black text-2xl sm:text-4xl lg:text-5xl uppercase tracking-tight max-w-3xl mx-auto">
          ¿Gestionas Varios Clubs o Estás Expandiendo tu Marca?
        </h2>

        <p class="text-slate-300 text-base sm:text-lg max-w-2xl mx-auto font-medium leading-relaxed">
          En <strong>CoolPadel Studios</strong> ayudamos a operadores multi-club y cadenas con dos soluciones probadas en más de 25 complejos deportivos de Europa:
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
              Fabricación directa de llaveros de goma en relieve 3D con el logo oficial de tu cadena para la pro-shop, abonados y torneos del club. Muestra física previa 15€.
            </p>
            <a href="../llaveros-padel-personalizados/" class="inline-flex items-center gap-1.5 text-xs font-bold text-[#f2920b] hover:underline mt-3">
              <span>Ver llaveros para clubs</span>
              <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
            </a>
          </div>
        </div>

        <div class="pt-4 flex flex-col sm:flex-row items-center justify-center gap-4">
          <a href="https://wa.me/34680317486?text=Hola%20Javier%2C%20tengo%20una%20cadena%20de%20clubs%20de%20p%C3%A1del%20(o%20varios%20centros)%20y%20quiero%20hablar%20contigo%20sobre%20tecnolog%C3%ADa%20y%20merchandising" target="_blank"
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
  
  <aside id="franchiseDrawer" class="fixed top-0 right-0 w-full sm:w-[540px] lg:w-[620px] h-full bg-white z-50 shadow-2xl transform translate-x-full transition-transform duration-300 flex flex-col">
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
          <span>Modelo de Cadena, Inversión & Expansión</span>
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
    let currentRegion = 'all';
    let currentModel = 'all';
    let currentView = 'grid';

    // Inicializar Iconos Lucide
    document.addEventListener("DOMContentLoaded", function() {{
      lucide.createIcons();
      initMap();
    }});

    function getMarkerColor(categoria) {{
      switch(categoria) {{
        case 'cadena': return '#0284c7'; // Azul cielo intenso para cadenas con el mismo nombre
        case 'corporativo': return '#2563eb';
        case 'franquicia': return '#4f46e5';
        case 'automatizado': return '#059669';
        case 'boutique': return '#9333ea';
        case 'licencia': return '#d97706';
        default: return '#f2920b';
      }}
    }}

    function initMap() {{
      // Centro por defecto: Vista Global / Europa
      map = L.map('map', {{
        center: [38.0, 5.0],
        zoom: 3,
        minZoom: 2,
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
          <div style="font-family: 'Plus Jakarta Sans', sans-serif; min-width: 220px; padding: 6px;">
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

    function zoomToFrance() {{
      map.setView([46.5, 2.5], 6);
    }}

    function zoomToItaly() {{
      map.setView([42.5, 12.5], 6);
    }}

    function zoomToUSA() {{
      map.setView([37.0, -95.0], 4);
    }}

    function zoomToLatam() {{
      map.setView([-15.0, -70.0], 3);
    }}

    function zoomToMiddleEast() {{
      map.setView([25.0, 50.0], 5);
    }}

    function setRegionFilter(region) {{
      currentRegion = region;
      document.querySelectorAll('.filter-region-btn').forEach(btn => {{
        if (btn.dataset.region === region) {{
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
        const regionCode = f.region_filtro || f.pais_codigo;
        const matchRegion = (currentRegion === 'all' || regionCode === currentRegion);
        const matchModel = (currentModel === 'all' || f.tipo_categoria === currentModel);
        
        const textToSearch = `${{f.nombre}} ${{f.pais}} ${{f.ciudad_sede}} ${{f.software}} ${{f.tagline}} ${{f.modelo}}`.toLowerCase();
        const matchQuery = !query || textToSearch.includes(query);

        const isVisible = matchRegion && matchModel && matchQuery;

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

      document.getElementById('resultsCount').textContent = `Mostrando ${{visibleCount}} de ${{FRANQUICIAS.length}} cadenas y franquicias`;
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
        <div><strong>Tipo de Contrato / Expansión:</strong> ${{f.modelo_expansion.tipo_contrato}}</div>
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

    print(f"Directorio de franquicias y cadenas generado con éxito en: {target_file}")
    print(f"Total de entidades incluidas: {len(FRANQUICIAS)}")


if __name__ == "__main__":
    main()
