#!/usr/bin/env python3
"""
Generador de Landings B2B Transaccionales para CoolPadel Studios:
1. /llaveros-padel-personalizados/ -> Core B2B Llaveros de Pádel 3D
2. /llaveros-tenis-personalizados/ -> Llaveros de Tenis y Academias
3. /welcome-packs-torneos-padel/   -> Welcome Packs y Regalos para Torneos
4. /llaveros-personalizados-clubs-padel/ -> Merchandising y Llaveros para Clubs de Pádel
"""

import os
import urllib.parse
from datetime import datetime

WEBHOOK_URL = 'https://script.google.com/macros/s/AKfycbxnF9JmVrikeAW7PdLc02r_1kkuSJVz1Ncl71ZeVGT37H0ji5DQ3DVw60122pcuYnxCgA/exec'

LANDINGS = [
    {
        "slug": "llaveros-padel-personalizados",
        "title": "Llaveros de Pádel Personalizados 3D para Clubs | CoolPadel",
        "meta_desc": "Fabricante de llaveros de pádel personalizados con forma de pala y logo oficial para clubs, torneos y tiendas. Pedidos desde 100 uds y muestra previa por 15€.",
        "badge": "FABRICACIÓN DIRECTA B2B",
        "h1": "Llaveros de Pádel Personalizados con Forma de Pala y Logo Oficial",
        "subtitle": "Fabricamos los llaveros oficiales de tu club o torneo en microinyección de PVC blando 3D con forma de pala o tu escudo exacto. El detalle de merchandising de pádel que tus jugadores llevan siempre en el paletero.",
        "hero_img": "assets/images/llaveros 1.jpg",
        "hero_img_alt": "Llaveros de pádel personalizados con forma de pala de goma 3D con logo oficial para clubes",
        "wa_msg": "Hola Javier, quiero información y presupuesto para llaveros de pádel personalizados para mi club",
        "price_anchor": "Desde 1,50 € / ud · Pedido mínimo 100 uds",
        "target_audience": "Clubes de pádel, federaciones, organizadores de torneos y escuelas deportivas que buscan merchandising de alta calidad con el escudo de su club.",
        "benefits": [
            ("Relieve 3D Microinyectado", "Goma PVC flexible de alta densidad, resistente a caídas, agua y rozaduras dentro del paletero."),
            ("Muestra Física Previa 15€", "Fabricamos una muestra real con tu logo antes de confirmar la tirada completa. Reembolsable 100% con el pedido."),
            ("Tarifa Directa de Fábrica", "Desde 1,50€ a 3,00€ por unidad con envíos incluidos a España, Europa y Estados Unidos.")
        ],
        "faqs": [
            ("¿Cuál es el pedido mínimo y los plazos de entrega?", "El pedido mínimo de producción es de 100 unidades. El plazo de entrega de la muestra física real es de unos 15 días laborables y la entrega del pedido final se sitúa en torno a un mes según volumen."),
            ("¿Cómo solicitamos la muestra física de 15€?", "Solo tienes que enviarnos el logo de tu club en cualquier formato (vectorial, PNG, JPG). Preparamos el diseño 3D y fabricamos una muestra real enviada a tu dirección por 15€ (100% descontables del pedido final)."),
            ("¿Se puede personalizar el reverso del llavero?", "Sí, podemos añadir el logo de un patrocinador, la página web del club o las redes sociales en el reverso.")
        ]
    },
    {
        "slug": "llaveros-tenis-personalizados",
        "title": "Llaveros de Tenis Personalizados 3D para Clubs | CoolPadel",
        "meta_desc": "Llaveros de tenis personalizados en relieve 3D con el escudo oficial de tu club, escuela o torneo. Goma flexible de alta calidad, pedidos desde 100 unidades y muestra previa.",
        "badge": "ESPECIAL CLUBS & ACADEMIAS DE TENIS",
        "h1": "Llaveros de Tenis Personalizados con tu Escudo Oficial",
        "subtitle": "Diseñamos y fabricamos llaveros de tenis en relieve 3D para escuelas de tenis, torneos sociales, clubes históricos y welcome packs. Un obsequio elegante y duradero.",
        "hero_img": "assets/images/llaveros 2.jpg",
        "hero_img_alt": "Llaveros de tenis personalizados con relieve 3D para clubs y escuelas deportivas",
        "wa_msg": "Hola Javier, quiero presupuesto para llaveros de tenis personalizados para nuestro club/academia",
        "price_anchor": "Desde 1,50 € / ud · Muestra física real 15 €",
        "target_audience": "Clubes de tenis, academias de alto rendimiento, escuelas deportivas y eventos de tenis federados o sociales.",
        "benefits": [
            ("Diseño Fiel a tu Escudo", "Reproducimos con fidelidad los detalles, tipografías y colores tradicionales de tu club de tenis."),
            ("Material Duradero y Flexible", "Goma 3D ligera que no raya las raquetas, mochilas ni bolsillos. Anilla metálica reforzada."),
            ("Sin Gastos Ocultos", "Diseño digital sin coste, muestra previa enviada en ~15 días laborables por 15€ (100% descontable) y envíos incluidos en el pedido final.")
        ],
        "faqs": [
            ("¿Fabricáis llaveros tanto de tenis como de pádel?", "Sí. Muchos de nuestros clubes clientes son entidades polideportivas (tenis + pádel) y fabricamos los modelos para ambas secciones o torneos mixtos."),
            ("¿Qué formatos de logotipo aceptáis?", "Aceptamos cualquier formato (AI, PDF, SVG, PNG, JPG). Nuestro equipo adapta el diseño al molde 3D para tu validación."),
            ("¿Sirven para vender en la tienda del club?", "Totalmente. Muchos clubes los comercializan en recepción o pro-shop a 5€-6€, generando un margen del 50-70% para el club.")
        ]
    },
    {
        "slug": "welcome-packs-torneos-padel",
        "title": "Welcome Packs y Regalos para Torneos de Pádel | CoolPadel",
        "meta_desc": "Regalos originales y cosas de pádel para welcome packs de torneos. Llaveros de goma 3D personalizados con el logo del torneo y patrocinadores. Tiradas desde 100 uds con muestra previa.",
        "badge": "TORNEOS, CIRCUITOS & WELCOME PACKS",
        "h1": "Welcome Packs y Regalos de Pádel para Torneos y Eventos",
        "subtitle": "Olvídate de las camisetas o toallas genéricas que acaban olvidadas en un cajón. Un llavero 3D personalizado con forma de pala y el logo del torneo es el regalo y detalle de pádel que los participantes lucen todo el año en su paletero.",
        "hero_img": "assets/images/slide-1.jpg",
        "hero_img_alt": "Welcome packs y llaveros 3D para torneos de pádel oficiales",
        "wa_msg": "Hola Javier, estoy organizando un torneo de pádel y busco regalos/welcome packs para los jugadores",
        "price_anchor": "Especial torneos: 100 a 1.500+ uds · Tarifa directa de fábrica",
        "target_audience": "Directores de torneos, organizadores de circuitos de pádel, patrocinadores y empresas que buscan un regalo publicitario de alto valor percibido.",
        "benefits": [
            ("Máxima Visibilidad para Patrocinadores", "Posibilidad de personalizar anverso con el torneo y reverso con la marca o patrocinador principal."),
            ("Alto Valor Percibido y Bajo Coste", "Desde 1,50€ por jugador, ofreciendo un regalo que se percibe como producto premium de tienda oficial."),
            ("Planificación Segura para tu Torneo", "Muestra física real en ~15 días laborables y entrega del pedido completo en torno a un mes según volumen.")
        ],
        "faqs": [
            ("¿Con cuánta antelación debo encargar los llaveros para el torneo?", "La muestra física tarda unos 15 días laborables y la entrega del pedido completo se sitúa en torno a un mes según volumen, por lo que recomendamos iniciar el proceso con unas 5-6 semanas de antelación."),
            ("¿Qué cantidades se suelen pedir para torneos?", "Dependiendo de los cuadros de juego, los torneos suelen solicitar entre 100 y 250 unidades para torneos locales de fin de semana, o 500 a 1.500 unidades para circuitos y másters."),
            ("¿Emitís factura oficial para la organización o patrocinador?", "Sí, emitimos factura oficial desglosada con IVA deducible para clubes, empresas organizadoras o patrocinadores del torneo.")
        ]
    },
    {
        "slug": "llaveros-personalizados-clubs-padel",
        "title": "Merchandising y Llaveros para Clubs de Pádel | CoolPadel",
        "meta_desc": "Llaveros oficiales y merchandising B2B para clubes de pádel. Productos y detalles de goma 3D para socios, bienvenida a escuelas y venta en pro-shop con +60% de margen. Más de 30 clubes clientes.",
        "badge": "MERCHANDISING OFICIAL DE CLUB",
        "h1": "Merchandising Oficial y Llaveros para Clubs de Pádel",
        "subtitle": "Refuerza la identidad y el sentido de pertenencia de tu comunidad. Más de 30 clubes en España, Europa y EE. UU. ya equipan a sus socios y pro-shops con llaveros y merchandising CoolPadel Studios.",
        "hero_img": "assets/images/llaveros 1.jpg",
        "hero_img_alt": "Llaveros oficiales personalizados para clubes de pádel y escuelas",
        "wa_msg": "Hola Javier, soy responsable de un club de pádel y quiero información para hacer los llaveros de nuestros socios",
        "price_anchor": "Tarifa club desde 1,50 € / ud · Muestra previa 15 €",
        "target_audience": "Gerentes de clubes, directores deportivos, comités de socios y responsables de pro-shop que desean merchandising oficial rentable y atractivo.",
        "benefits": [
            ("Fidelización de Socios y Alumnos", "El regalo perfecto para la cuota anual, bienvenida a la escuela de menores o cenas de fin de temporada."),
            ("Margen de Venta en Recepción", "Con un coste de fabricación de 1,50€-3,00€ y un PVP recomendado de 5€-6€, el club rentabiliza la inversión en pocas semanas."),
            ("Experiencia Demostrada en +30 Clubs", "Trabajamos con clubes referentes en España, Europa y EE. UU. con acabados profesionales y soporte personalizado.")
        ],
        "faqs": [
            ("¿Cómo gestionamos el pedido para nuestro club?", "Contactas directamente con Javier por WhatsApp o correo. Nos mandas el escudo del club, te presentamos el render digital 3D y fabricamos la muestra física en ~15 días laborables para que la toques en persona antes del pedido (entrega en ~1 mes)."),
            ("¿Podemos repetir pedidos en el futuro con el mismo molde?", "Sí. Guardamos tu molde de producción para que puedas pedir reposiciones de 100 en 100 unidades cuando lo necesites sin coste adicional de diseño."),
            ("¿Cuáles son las formas de pago para clubes?", "Transferencia bancaria o tarjeta contra factura oficial a nombre del club o empresa tras recibir y validar la muestra física.")
        ]
    },
    {
        "slug": "camaras-grabacion-pistas-padel",
        "title": "Cámaras de Grabación para Pistas de Pádel | Save My Play",
        "meta_desc": "Sistema de grabación inteligente y repetición en vídeo para pistas de pádel Save My Play. Instalación en 5 minutos sin obras, pulsador físico en poste y descarga por código QR.",
        "badge": "TECNOLOGÍA DE CLUB · SAVE MY PLAY",
        "h1": "Cámaras Inteligentes para Pistas de Pádel sin Obras",
        "subtitle": "La tecnología de repetición y analítica en pista que fideliza a tus jugadores y genera ingresos recurrentes para tu club de pádel o tenis. Sin permanencia, sin zanjas y montado en 5 minutos.",
        "hero_img": "assets/images/savemyplay-1.jpg",
        "hero_img_alt": "Sistema de cámaras inteligentes de grabación para pistas de pádel Save My Play",
        "wa_msg": "Hola Javier, quiero información sobre el sistema de cámaras y grabación Save My Play para las pistas de mi club",
        "price_anchor": "Hardware 180 € / pista · Software desde 45 €/mes · Sin obras",
        "target_audience": "Gerentes de clubes de pádel y tenis, directores de academias e inversores deportivos que buscan modernizar sus pistas con vídeo de alta definición.",
        "benefits": [
            ("Cero Obras y Montaje en 5 Minutos", "Se instala directamente en el poste de la pista sin necesidad de abrir zanjas, tirar tubos ni obras de albañilería."),
            ("Pulsador Físico de Highlights en Pista", "Los jugadores pulsan un botón físico tras un gran punto y descargan sus mejores jugadas al instante mediante código QR."),
            ("Sin Contratos de Permanencia", "Máxima flexibilidad. Pruébalo en tus pistas centrales y amplía cuando compruebes la satisfacción de los socios.")
        ],
        "faqs": [
            ("¿Se necesitan obras o canalizaciones en el suelo?", "No. El sistema se ancla directamente al poste de la pista y no requiere zanjas ni obras civiles. La instalación dura solo 5 minutos por pista."),
            ("¿Cuál es el precio y modelo de suscripción?", "Inversión única en hardware de 180 € por pista. La cuota mensual es de 45 €/mes (Plan Básico Highlights) o 136 €/mes (Plan Analítica IA Avanzada), sin permanencia."),
            ("¿Cómo reciben los jugadores sus jugadas?", "El jugador pulsa el botón tras una jugada y al finalizar el partido escanea el QR en pista para tener el vídeo en su móvil al instante."),
            ("¿Cumple con la normativa RGPD de protección de datos?", "Totalmente. El sistema cumple los estándares europeos de privacidad: los clips se almacenan temporalmente y solo los jugadores que activan su sesión acceden a sus grabaciones.")
        ]
    },
    {
        "slug": "camaras-padel-playtomic",
        "title": "Cámaras Save my Play para Clubs en Playtomic | Grabación",
        "meta_desc": "Integra cámaras Save my Play en tus pistas de pádel gestionadas con Playtomic. Grabación con pulsador en red, repeticiones QR y monetización sin obras ni permanencia.",
        "badge": "INTEGRACIÓN PLAYTOMIC & SAVE MY PLAY",
        "h1": "Cámaras Inteligentes Save my Play para Clubes en Playtomic",
        "subtitle": "El complemento perfecto para tu gestión en Playtomic: añade grabación de partidos con pulsador en pista, repeticiones instantáneas y streaming en YouTube sin obras ni permanencias.",
        "hero_img": "assets/images/savemyplay-1.jpg",
        "hero_img_alt": "Cámaras Save my Play compatibles con pistas Playtomic",
        "wa_msg": "Hola Javier, gestionamos nuestro club con Playtomic y queremos información de cámaras Save my Play para las pistas",
        "price_anchor": "Hardware 180 € / pista · Cuota 45 €/mes · 0 permanencia",
        "target_audience": "Gerentes y directores deportivos de clubes que gestionan sus pistas y reservas con Playtomic.",
        "benefits": [
            ("Compatibilidad Total con Playtomic", "No interfiere con tu sistema de reservas. Los jugadores reservan su pista en Playtomic como siempre y disfrutan de grabación HD con pulsador físico."),
            ("Monetización Complementaria para el Club", "Genera un ingreso extra mensual mediante recargo de reserva, patrocinadores en pantalla o cobro por descarga de clips."),
            ("Montaje en 5 Minutos sin Obras", "Fijación directa al poste de la pista sin canalizaciones, zanjas ni cortes de juego.")
        ],
        "faqs": [
            ("¿Save my Play requiere modificar la configuración de Playtomic?", "No. El sistema Save my Play opera de forma autónoma en pista. Los jugadores entran a la pista reservada en Playtomic, juegan y pulsan el botón de poste para guardar sus mejores puntos."),
            ("¿Cómo reciben los jugadores los vídeos si reservan por Playtomic?", "Al terminar el partido, los jugadores escanean el código QR ubicado en el poste de la pista con la cámara de su móvil y descargan sus clips de 25 segundos al instante sin necesidad de registrarse."),
            ("¿Podemos transmitir torneos organizados en Playtomic en directo por YouTube?", "Sí. La cámara Save my Play emite directamente a YouTube Live en Full HD 1080p, permitiendo añadir marcadores y patrocinadores locales a las finales.")
        ]
    },
    {
        "slug": "camaras-padel-matchi",
        "title": "Cámaras Save my Play para Clubs con Matchi | Vídeo Pista",
        "meta_desc": "Sistema de grabación autónomo Save my Play para instalaciones de pádel con Matchi. Replay instantáneo con QR, 0 obras y hardware en propiedad por 180 €.",
        "badge": "INTEGRACIÓN MATCHI & SAVE MY PLAY",
        "h1": "Grabación en Pista y Replay para Clubes que Usan Matchi",
        "subtitle": "Equipa tus pistas Matchi con la tecnología Save my Play. Descarga de mejores jugadas por código QR sin necesidad de descargar apps pesadas ni contratos de permanencia.",
        "hero_img": "assets/images/savemyplay-2.jpg",
        "hero_img_alt": "Sistema de cámaras Save my Play para clubes que usan Matchi",
        "wa_msg": "Hola Javier, usamos Matchi en nuestro club y queremos poner cámaras Save my Play en las pistas",
        "price_anchor": "Hardware 180 € / pista · Software desde 45 €/mes · Sin permanencia",
        "target_audience": "Operadores y clubes en España, Suecia, Noruega y Reino Unido que gestionan sus pistas con la plataforma Matchi.",
        "benefits": [
            ("Fácil Adopción Internacional", "Especialmente pensado para clubes con Matchi y público multicultural: el código QR abre un visor web instantáneo en cualquier idioma sin apps."),
            ("0 Obras y Fijación Universal", "Compatible con todas las estructuras de pista habituales en clubes Matchi (panorámicas, de marco o muro)."),
            ("Flexibilidad Contractual", "Sin permanencias de 3 a 5 años como otros sistemas tradicionales de cámaras. Pruébalo y mantén el control.")
        ],
        "faqs": [
            ("¿Funciona en clubes Matchi con acceso automatizado 24/7?", "Sí, Save my Play está diseñado para operar de forma 100% autónoma. La cámara se enciende y graba automáticamente sin requerir personal de recepción."),
            ("¿Qué conexión a Internet necesita cada pista?", "Solo requiere cobertura Wi-Fi estándar o conexión Ethernet y una toma de 220V. La cámara gestiona localmente el buffer y sube los clips a la nube de forma segura."),
            ("¿Podemos usar los vídeos para clases de los monitores del club?", "Totalmente. Los entrenadores utilizan el Plan B o Plan A para repasar golpes en cámara lenta con sus alumnos en clinics matinales.")
        ]
    },
    {
        "slug": "camaras-padel-resasports",
        "title": "Cámaras Save my Play y Resasports | Grabación en Pista",
        "meta_desc": "Automatización de grabación para centros deportivos y clubes con software Resasports. Instalación en 5 minutos, pulsador en red y tarifa plana sin permanencia.",
        "badge": "INTEGRACIÓN RESASPORTS & SAVE MY PLAY",
        "h1": "Grabación Inteligente en Pista para Clubes con Resasports",
        "subtitle": "Potencia la experiencia de tus abonados en Resasports con repetición instantánea en pista, retransmisión por YouTube y cero costes de obra civil.",
        "hero_img": "assets/images/savemyplay-3.jpg",
        "hero_img_alt": "Cámaras Save my Play para instalaciones deportivas con Resasports",
        "wa_msg": "Hola Javier, gestionamos nuestro centro con Resasports y nos interesa la grabación Save my Play",
        "price_anchor": "Hardware 180 € / pista · Cuota 45 €/mes · Cero obras",
        "target_audience": "Centros municipales, clubes de tenis/pádel y complejos deportivos que operan con Resasports.",
        "benefits": [
            ("Cero Obra Civil en Instalaciones Públicas o Concesionales", "No requiere permisos de obra ni zanjas en pistas existentes. Se sujeta con fijación homologada al poste."),
            ("Cumplimiento RGPD Estricto", "Ideal para polideportivos y clubes con exigencias legales estrictas: buffer cerrado y borrado programado."),
            ("Económico y Sostenible", "Hardware de solo 180 € en propiedad frente a presupuestos de más de 2.500 € por pista de otras soluciones.")
        ],
        "faqs": [
            ("¿Es apto para concesiones administrativas y polideportivos?", "Sí. Al no requerir obra civil ni modificar la estructura de la pista, se aprueba con máxima agilidad en instalaciones públicas o concesionales."),
            ("¿Cómo se garantiza la privacidad de los menores en la instalación?", "El sistema solo almacena el clip de 25 segundos cuando el jugador acciona el pulsador voluntariamente en la red, evitando la grabación indiscriminada continua."),
            ("¿Cuánto tiempo tarda la instalación en varias pistas?", "Al tardar solo 5 minutos por pista, un club de 6 pistas queda completamente equipado y funcionando en menos de una mañana.")
        ]
    },
    {
        "slug": "camaras-padel-madrid",
        "title": "Cámaras para Pistas de Pádel en Madrid | Save my Play",
        "meta_desc": "Instalación de cámaras inteligentes Save my Play en Madrid: Pozuelo, Alcobendas, Las Rozas, Majadahonda, La Moraleja. Grabación HD en 5 min, sin obras ni permanencia.",
        "badge": "COMUNIDAD DE MADRID · SAVE MY PLAY",
        "h1": "Cámaras Inteligentes para Pistas de Pádel en Madrid",
        "subtitle": "La tecnología en pista que eligen clubes referentes en la Comunidad de Madrid: grabación de partidos, pulsador en poste y retransmisión por YouTube sin cables ni zanjas.",
        "hero_img": "assets/images/savemyplay-1.jpg",
        "hero_img_alt": "Cámaras para pistas de pádel en clubes de Madrid",
        "wa_msg": "Hola Javier, tenemos pistas de pádel en Madrid y queremos presupuesto para cámaras Save my Play",
        "price_anchor": "Visita y demo presencial en Madrid · 180 € hardware · 45 €/mes",
        "target_audience": "Directores de clubes de pádel, complejos indoor y urbanizaciones de la Comunidad de Madrid.",
        "benefits": [
            ("Soporte y Demostración Presencial en Madrid", "Sede de CoolPadel Studios en Madrid: podemos visitarte y hacer una demostración real en tus instalaciones."),
            ("Ideal para Naves Indoor y Urbanizaciones", "Montaje limpio sin rozas ni cableado que interfiera con la iluminación o la insonorización de naves industriales."),
            ("Amortización Rápida con Socios de Madrid", "Alta demanda de contenidos para redes sociales entre jugadores y ligas corporativas madrileñas.")
        ],
        "faqs": [
            ("¿En qué zonas de Madrid ofrecéis servicio e instalación?", "Damos cobertura completa a toda la Comunidad de Madrid: Madrid Capital, Pozuelo de Alarcón, Las Rozas, Majadahonda, Alcobendas, San Sebastián de los Reyes, Boadilla del Monte, Getafe, Leganés, Alcorcón, etc."),
            ("¿Podéis venir a enseñarnos el sistema antes de contratar?", "Por supuesto. Coordinamos una visita de 20 minutos con Javier Villoria para que conozcas la cámara, el pulsador y la calidad de la lente deportiva."),
            ("¿Cómo funciona en pistas de urbanizaciones privadas en Madrid?", "Se puede instalar en urbanizaciones que deseen ofrecer valor añadido a sus vecinos, controlando el acceso mediante pulsador o QR.")
        ]
    },
    {
        "slug": "camaras-padel-barcelona",
        "title": "Cámaras para Pistas de Pádel en Barcelona | Save my Play",
        "meta_desc": "Cámaras autónomas para pistas de pádel en Barcelona y Cataluña (Hospitalet, Sant Cugat, Badalona, Sabadell). Grabación con pulsador en red y streaming sin obras.",
        "badge": "BARCELONA & CATALUNYA · SAVE MY PLAY",
        "h1": "Cámaras y Grabación de Partidos de Pádel en Barcelona",
        "subtitle": "La solución de vídeo más ágil para clubes indoor y outdoor en Barcelona y Cataluña: repetición instantánea en móvil, retransmisión de torneos y cero permanencia.",
        "hero_img": "assets/images/savemyplay-2.jpg",
        "hero_img_alt": "Cámaras Save my Play para pistas de pádel en Barcelona y Cataluña",
        "wa_msg": "Hola Javier, tenemos un club de pádel en Barcelona y queremos presupuesto para cámaras Save my Play",
        "price_anchor": "Hardware 180 € / pista · Software 45 €/mes · Envíos inmediatos",
        "target_audience": "Gerentes y clubes de pádel en Barcelona, área metropolitana y provincias de Girona, Tarragona y Lleida.",
        "benefits": [
            ("Retransmisión de Circuitos y Ligas Catalanas", "Emite en directo por YouTube con marcadores las fases finales de torneos catalanes federados y sociales."),
            ("Resistencia a Ambientes Costeros e Indoor", "Carcasa sellada IP resistente a la humedad marina y condensación habitual en centros deportivos del litoral."),
            ("Autonomía 100% Digital", "Los jugadores descargan en segundos escaneando el código QR con cualquier smartphone.")
        ],
        "faqs": [
            ("¿En qué municipios de Barcelona dais cobertura?", "Enviamos e instalamos en Barcelona capital, Hospitalet de Llobregat, Badalona, Sant Cugat del Vallès, Sabadell, Terrassa, Mataró, Cornellà, Castelldefels y toda Cataluña."),
            ("¿Cuánto tarda el envío y puesta en marcha?", "Enviamos el equipo configurado en 48 horas. Solo necesitas atornillar la fijación al poste (5 minutos) y conectar a 220V."),
            ("¿Se pueden personalizar los vídeos con el escudo del club catalán?", "Sí, cada clip descargado o emitido en streaming incluye el logo oficial del club y de los patrocinadores locales.")
        ]
    }
]

def render_landing(landing):
    wa_encoded = urllib.parse.quote(landing["wa_msg"])
    hero_img_encoded = urllib.parse.quote(landing["hero_img"])
    
    # JSON-LD Schemas
    faq_schema_items = []
    for q, a in landing["faqs"]:
        faq_schema_items.append(f"""
          {{
            "@type": "Question",
            "name": "{q}",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{a}"
            }}
          }}""")
    faq_schema_json = ",".join(faq_schema_items)

    benefits_html = ""
    for title, desc in landing["benefits"]:
        benefits_html += f"""
        <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200/90 shadow-sm hover:shadow-md transition">
          <div class="w-12 h-12 rounded-2xl bg-[#f2920b]/15 text-[#f2920b] flex items-center justify-center mb-5 font-black text-xl">
            ✓
          </div>
          <h3 class="font-heading font-black text-xl sm:text-2xl text-slate-950 mb-2">{title}</h3>
          <p class="text-slate-600 text-sm sm:text-base leading-relaxed">{desc}</p>
        </div>"""

    is_camaras = landing["slug"].startswith("camaras-") or landing["slug"] == "camaras-grabacion-pistas-padel"
    breadcrumb_name = "Cámaras en Pista" if is_camaras else "Llaveros Personalizados"
    cta_hero_text = "Solicitar Demo / Presupuesto" if is_camaras else "Solicitar Muestra / Cotización"

    if is_camaras:
        hero_badges_html = """
              <span class="flex items-center gap-1.5"><i data-lucide="check-circle" class="w-4 h-4 text-[#f2920b]"></i> 0 obras · Montaje 5 min</span>
              <span class="flex items-center gap-1.5"><i data-lucide="check-circle" class="w-4 h-4 text-[#f2920b]"></i> 0 permanencia</span>
              <span class="flex items-center gap-1.5"><i data-lucide="check-circle" class="w-4 h-4 text-[#f2920b]"></i> Descarga instantánea QR</span>"""
        why_title = "¿Por qué elegir Save My Play para tu club?"
        why_sub = "La tecnología de grabación y analítica en pista más ágil, sin obras ni costes ocultos"
        precios_title = "Tarifas Oficiales Save My Play B2B"
        precios_sub = "Hardware en propiedad sin permanencia y cuota mensual de software por pista"
        faq_sub = "Resolvemos todas tus dudas sobre el sistema de grabación Save My Play sin obras"
        cta_sub = "Escríbeme directamente por WhatsApp. Te respondo personalmente para agendar una demo online de 15 minutos o preparar el presupuesto de tus pistas."
        footer_tagline = "© 2026 CoolPadel Studios · Partner Oficial Save My Play en España y Europa · Madrid, España"
        table_html = f"""
          <div class="overflow-x-auto">
            <table class="w-full text-left text-sm sm:text-base">
              <thead>
                <tr class="border-b border-slate-200 text-xs uppercase tracking-wider text-slate-500">
                  <th class="py-3 px-3">Concepto / Plan</th>
                  <th class="py-3 px-3">Inversión / Cuota</th>
                  <th class="py-3 px-3">Modalidad</th>
                  <th class="py-3 px-3">Servicios Incluidos</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100 font-bold">
                <tr>
                  <td class="py-4 px-3 text-slate-900">Inversión Hardware por Pista</td>
                  <td class="py-4 px-3 text-[#f2920b]">180 € / pista</td>
                  <td class="py-4 px-3 text-slate-700">Pago único (en propiedad)</td>
                  <td class="py-4 px-3 text-slate-600 text-xs font-medium">Cámara deportiva panorámica HD + fijación a poste + pulsador físico</td>
                </tr>
                <tr>
                  <td class="py-4 px-3 text-slate-900">Plan B · Highlights &amp; Streaming (Recomendado)</td>
                  <td class="py-4 px-3 text-[#f2920b]">45 € / mes</td>
                  <td class="py-4 px-3 text-emerald-600">0 permanencia · Cancelación libre</td>
                  <td class="py-4 px-3 text-slate-600 text-xs font-medium">Grabación de partidos, repeticiones botón en poste, clips automáticos, streaming YouTube y descarga QR</td>
                </tr>
                <tr>
                  <td class="py-4 px-3 text-slate-900">Plan A · Analítica IA Avanzada</td>
                  <td class="py-4 px-3 text-[#f2920b]">136 € / mes</td>
                  <td class="py-4 px-3 text-emerald-600">0 permanencia · Cancelación libre</td>
                  <td class="py-4 px-3 text-slate-600 text-xs font-medium">Todo el Plan B + AI Analytics táctico, mapas de calor, recuento de golpes y métricas</td>
                </tr>
              </tbody>
            </table>
          </div>
          
          <div class="mt-6 pt-5 border-t border-slate-100 flex flex-col sm:flex-row items-center justify-between gap-4">
            <span class="text-xs text-slate-500">* Precios sin IVA. Sin contratos de permanencia ni penalizaciones. Instalación en 5 minutos sin obras civiles.</span>
            <a href="https://wa.me/34680317486?text={wa_encoded}" target="_blank" rel="noopener noreferrer" class="px-6 py-3 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition">
              Pedir Presupuesto / Demo por WhatsApp
            </a>
          </div>"""
        pasos_html = """
        <div class="grid sm:grid-cols-3 gap-6 text-center">
          <div class="space-y-2">
            <div class="w-10 h-10 rounded-full bg-white/20 text-white font-heading font-black text-base flex items-center justify-center mx-auto">1</div>
            <h3 class="font-heading font-black text-lg">Demo Online (15 min)</h3>
            <p class="text-white/80 text-xs">Te mostramos en vivo cómo funciona la cámara, el pulsador y la descarga instantánea por QR.</p>
          </div>
          <div class="space-y-2">
            <div class="w-10 h-10 rounded-full bg-white/20 text-white font-heading font-black text-base flex items-center justify-center mx-auto">2</div>
            <h3 class="font-heading font-black text-lg">Instalación en 5 min</h3>
            <p class="text-white/80 text-xs">Se fija directamente al poste de la pista sin obras, sin zanjas y sin cortar horas de juego.</p>
          </div>
          <div class="space-y-2">
            <div class="w-10 h-10 rounded-full bg-white/20 text-white font-heading font-black text-base flex items-center justify-center mx-auto">3</div>
            <h3 class="font-heading font-black text-lg">Activación y Sin Permanencia</h3>
            <p class="text-white/80 text-xs">Tus jugadores disfrutan de sus mejores jugadas. Puedes darte de baja en cualquier momento.</p>
          </div>
        </div>"""
    else:
        hero_badges_html = """
              <span class="flex items-center gap-1.5"><i data-lucide="check-circle" class="w-4 h-4 text-[#f2920b]"></i> Muestra 15€ (~15 días lab.)</span>
              <span class="flex items-center gap-1.5"><i data-lucide="check-circle" class="w-4 h-4 text-[#f2920b]"></i> Pedido mín. 100 uds</span>
              <span class="flex items-center gap-1.5"><i data-lucide="check-circle" class="w-4 h-4 text-[#f2920b]"></i> Entrega pedido ~1 mes</span>"""
        why_title = "¿Por qué elegir CoolPadel Studios?"
        why_sub = "Acabado profesional de tienda oficial para elevar la imagen de tu club o evento"
        precios_title = "Tarifas Directas de Fabricación B2B"
        precios_sub = "Precios sin intermediarios adaptados al volumen de socios o jugadores"
        faq_sub = "Resolvemos todas tus dudas antes de encargar los llaveros personalizados de tu club"
        cta_sub = "Escríbeme directamente por WhatsApp. Te respondo personalmente para ver tu diseño y enviarte la muestra física."
        footer_tagline = "© 2026 CoolPadel Studios · Fabricante B2B de Llaveros de Pádel y Tenis en Goma 3D · Madrid, España"
        table_html = f"""
          <div class="overflow-x-auto">
            <table class="w-full text-left text-sm sm:text-base">
              <thead>
                <tr class="border-b border-slate-200 text-xs uppercase tracking-wider text-slate-500">
                  <th class="py-3 px-3">Tirada</th>
                  <th class="py-3 px-3">Precio Unitario</th>
                  <th class="py-3 px-3">Total Estimado</th>
                  <th class="py-3 px-3">Muestra Física Previa</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100 font-bold">
                <tr>
                  <td class="py-4 px-3 text-slate-900">100 unidades (Mínimo)</td>
                  <td class="py-4 px-3 text-[#f2920b]">3,00 € / ud</td>
                  <td class="py-4 px-3 text-slate-700">300 € (+IVA)</td>
                  <td class="py-4 px-3 text-slate-500 text-xs">15 € (100% deducible)</td>
                </tr>
                <tr>
                  <td class="py-4 px-3 text-slate-900">250 unidades</td>
                  <td class="py-4 px-3 text-[#f2920b]">2,50 € / ud</td>
                  <td class="py-4 px-3 text-slate-700">625 € (+IVA)</td>
                  <td class="py-4 px-3 text-slate-500 text-xs">15 € (100% deducible)</td>
                </tr>
                <tr>
                  <td class="py-4 px-3 text-slate-900">500 unidades</td>
                  <td class="py-4 px-3 text-[#f2920b]">2,00 € / ud</td>
                  <td class="py-4 px-3 text-slate-700">1.000 € (+IVA)</td>
                  <td class="py-4 px-3 text-slate-500 text-xs">15 € (100% deducible)</td>
                </tr>
                <tr>
                  <td class="py-4 px-3 text-slate-900">1.500 unidades</td>
                  <td class="py-4 px-3 text-[#f2920b]">1,50 € / ud</td>
                  <td class="py-4 px-3 text-slate-700">2.250 € (+IVA)</td>
                  <td class="py-4 px-3 text-slate-500 text-xs">Tarifa directa gran volumen</td>
                </tr>
              </tbody>
            </table>
          </div>
          
          <div class="mt-6 pt-5 border-t border-slate-100 flex flex-col sm:flex-row items-center justify-between gap-4">
            <span class="text-xs text-slate-500">* Precios sin IVA. Muestra física en ~15 días laborables y entrega del pedido en ~1 mes según volumen.</span>
            <a href="https://wa.me/34680317486?text={wa_encoded}" target="_blank" rel="noopener noreferrer" class="px-6 py-3 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition">
              Pedir Presupuesto por WhatsApp
            </a>
          </div>"""
        pasos_html = """
        <div class="grid sm:grid-cols-3 gap-6 text-center">
          <div class="space-y-2">
            <div class="w-10 h-10 rounded-full bg-white/20 text-white font-heading font-black text-base flex items-center justify-center mx-auto">1</div>
            <h3 class="font-heading font-black text-lg">Envías tu Logotipo</h3>
            <p class="text-white/80 text-xs">Preparamos el diseño digital 3D sin coste para validar proporciones y colores.</p>
          </div>
          <div class="space-y-2">
            <div class="w-10 h-10 rounded-full bg-white/20 text-white font-heading font-black text-base flex items-center justify-center mx-auto">2</div>
            <h3 class="font-heading font-black text-lg">Muestra Física (15€)</h3>
            <p class="text-white/80 text-xs">Fabricamos y enviamos una muestra real en ~15 días laborables. Los 15€ se descuentan al 100% del pedido.</p>
          </div>
          <div class="space-y-2">
            <div class="w-10 h-10 rounded-full bg-white/20 text-white font-heading font-black text-base flex items-center justify-center mx-auto">3</div>
            <h3 class="font-heading font-black text-lg">Producción y Entrega</h3>
            <p class="text-white/80 text-xs">Fabricación final desde 100 uds y entrega en torno a un mes según volumen.</p>
          </div>
        </div>"""

    # Dynamic Product / Service Schema per landing type
    if is_camaras:
        product_schema_json = f"""{{
        "@type": ["Product", "Service"],
        "name": "{landing['h1']} - Save My Play",
        "description": "{landing['meta_desc']}",
        "image": "https://coolpadelstudios.com/{hero_img_encoded}",
        "sku": "SMP-COURT-CAM-2026",
        "brand": {{
          "@type": "Brand",
          "name": "Save My Play"
        }},
        "offers": [
          {{
            "@type": "Offer",
            "name": "Hardware Cámara de Pista (Inversión inicial única)",
            "priceCurrency": "EUR",
            "price": "180.00",
            "priceValidUntil": "2027-12-31",
            "availability": "https://schema.org/InStock"
          }},
          {{
            "@type": "Offer",
            "name": "Plan B - Highlights & Streaming (Cuota mensual)",
            "priceCurrency": "EUR",
            "price": "45.00",
            "priceValidUntil": "2027-12-31",
            "availability": "https://schema.org/InStock"
          }},
          {{
            "@type": "Offer",
            "name": "Plan A - Analítica IA Avanzada (Cuota mensual)",
            "priceCurrency": "EUR",
            "price": "136.00",
            "priceValidUntil": "2027-12-31",
            "availability": "https://schema.org/InStock"
          }}
        ]
      }}"""
    else:
        product_schema_json = f"""{{
        "@type": "Product",
        "name": "{landing['h1']} - CoolPadel Studios",
        "description": "{landing['meta_desc']}",
        "image": "https://coolpadelstudios.com/{hero_img_encoded}",
        "sku": "CP-{landing['slug'].upper()[:18]}",
        "brand": {{
          "@type": "Brand",
          "name": "CoolPadel Studios"
        }},
        "offers": [
          {{
            "@type": "Offer",
            "name": "Tramo 100 unidades (Pedido mínimo - 3,00 €/ud)",
            "priceCurrency": "EUR",
            "price": "3.00",
            "priceValidUntil": "2027-12-31",
            "availability": "https://schema.org/MadeToOrder"
          }},
          {{
            "@type": "Offer",
            "name": "Tramo 250 unidades (2,50 €/ud - 625 € total)",
            "priceCurrency": "EUR",
            "price": "2.50",
            "priceValidUntil": "2027-12-31",
            "availability": "https://schema.org/MadeToOrder"
          }},
          {{
            "@type": "Offer",
            "name": "Tramo 500 unidades (2,00 €/ud - 1.000 € total)",
            "priceCurrency": "EUR",
            "price": "2.00",
            "priceValidUntil": "2027-12-31",
            "availability": "https://schema.org/MadeToOrder"
          }},
          {{
            "@type": "Offer",
            "name": "Tramo 1.500 unidades (1,50 €/ud - 2.250 € total)",
            "priceCurrency": "EUR",
            "price": "1.50",
            "priceValidUntil": "2027-12-31",
            "availability": "https://schema.org/MadeToOrder"
          }},
          {{
            "@type": "Offer",
            "name": "Muestra física previa con logo real (~15 días laborables, 100% descontable)",
            "priceCurrency": "EUR",
            "price": "15.00",
            "priceValidUntil": "2027-12-31",
            "availability": "https://schema.org/InStock"
          }}
        ]
      }}"""

    faq_html = ""
    for idx, (q, a) in enumerate(landing["faqs"]):
        faq_html += f"""
        <div class="bg-white rounded-2xl p-6 border border-slate-200 shadow-xs space-y-2">
          <h3 class="font-heading font-black text-lg sm:text-xl text-slate-950">{q}</h3>
          <p class="text-slate-600 text-sm sm:text-base leading-relaxed">{a}</p>
        </div>"""

    html = f"""<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{landing['title']}</title>
  <meta name="description" content="{landing['meta_desc']}">
  <meta name="author" content="CoolPadel Studios">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
  <link rel="canonical" href="https://coolpadelstudios.com/{landing['slug']}/">
  <link rel="icon" type="image/png" href="../assets/images/favicon_transparente.png?v=transp3">
  <link rel="apple-touch-icon" sizes="180x180" href="../assets/images/favicon_transparente.png?v=transp3">
  <meta name="theme-color" content="#0b1626">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:locale" content="es_ES">
  <meta property="og:site_name" content="CoolPadel Studios">
  <meta property="og:url" content="https://coolpadelstudios.com/{landing['slug']}/">
  <meta property="og:title" content="{landing['title']}">
  <meta property="og:description" content="{landing['meta_desc']}">
  <meta property="og:image" content="https://coolpadelstudios.com/{hero_img_encoded}">
  <meta property="og:image:alt" content="{landing['hero_img_alt']}">

  <!-- Twitter Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{landing['title']}">
  <meta name="twitter:description" content="{landing['meta_desc']}">
  <meta name="twitter:image" content="https://coolpadelstudios.com/{hero_img_encoded}">

  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "Organization",
        "@id": "https://coolpadelstudios.com/#organization",
        "name": "CoolPadel Studios",
        "alternateName": "CoolPadel",
        "url": "https://coolpadelstudios.com",
        "logo": "https://coolpadelstudios.com/assets/images/coolpadel-mascot-hd.png",
        "knowsAbout": [
          "Grabación automática de partidos de pádel con IA",
          "Sistemas de cámaras fijas para pistas de pádel sin obras",
          "Llaveros de pádel personalizados de goma 3D",
          "Welcome packs y merchandising para torneos de pádel",
          "Directorio de franquicias y cadenas de clubes de pádel",
          "Normativa RGPD para cámaras en instalaciones deportivas",
          "Modelos de rentabilidad y amortización de clubes de pádel",
          "Integración de software de reservas de pádel (Playtomic, Matchi, Resasports)"
        ]
      }},
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
            "name": "{landing['h1']}",
            "item": "https://coolpadelstudios.com/{landing['slug']}/"
          }}
        ]
      }},
      {product_schema_json},
      {{
        "@type": "FAQPage",
        "mainEntity": [{faq_schema_json}
        ]
      }}
    ]
  }}
  </script>

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

  <style>
    body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
    h1, h2, h3, h4, .font-heading {{ font-family: 'Outfit', sans-serif; }}
    .bg-textured-blue {{
      background-color: #3478a6;
      background-image: linear-gradient(rgba(52, 120, 166, 0.40), rgba(52, 120, 166, 0.40)), url('../assets/images/branding/textura_editorial_coolpadel.webp');
      background-blend-mode: normal, soft-light;
      background-size: cover;
      background-position: center;
    }}
  </style>
</head>
<body class="bg-[#f8fafc] text-slate-800 antialiased selection:bg-[#f2920b] selection:text-slate-950 min-h-screen flex flex-col">

  <!-- HEADER OFICIAL -->
  <header class="sticky top-0 z-50 bg-white/95 backdrop-blur-md border-b border-slate-200/80 shadow-xs">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 sm:h-20 flex items-center justify-between">
      <a href="../" class="flex items-center gap-2 group">
        <img src="../assets/images/coolpadel-mascot-hd.png" alt="Mascota CoolPadel Studios" width="44" height="44" class="h-8 sm:h-11 w-auto object-contain">
        <img src="../assets/images/coolpadel-typography-hd.png" alt="CoolPadel Studios" width="140" height="28" class="h-5 sm:h-7 w-auto object-contain">
      </a>
      
      <div class="flex items-center gap-2 sm:gap-4 lg:gap-6">
        <a href="../#llaveros" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition">Llaveros</a>
        <a href="../camaras/" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition">Cámaras pistas</a>
        <a href="../blog/" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition">Blog</a>
        <a href="../franquicias-padel/" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition">Cadenas de clubs</a>
        
        <a href="https://wa.me/34680317486?text={wa_encoded}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-1.5 px-3.5 sm:px-4 py-1.5 sm:py-2 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition shadow-sm hover:scale-105 active:scale-95">
          <span>Pedir Presupuesto</span>
          <i data-lucide="arrow-up-right" class="w-3 h-3 stroke-[3]"></i>
        </a>
      </div>
    </div>
  </header>

  <!-- HERO SECTION -->
  <main class="flex-1">
    <section class="py-12 sm:py-20 bg-gradient-to-b from-white via-slate-50 to-[#f8fafc] border-b border-slate-200">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <!-- Breadcrumbs -->
        <nav class="flex items-center gap-2 text-xs font-bold text-slate-500 mb-6 uppercase tracking-wider">
          <a href="../" class="hover:text-slate-900 transition">Inicio</a>
          <span>/</span>
          <span class="text-[#f2920b]">{breadcrumb_name}</span>
        </nav>

        <div class="grid lg:grid-cols-12 gap-8 sm:gap-12 items-center">
          
          <div class="lg:col-span-7 space-y-5">
            <span class="inline-block px-3.5 py-1 rounded-full bg-[#f2920b]/15 text-[#f2920b] font-heading font-black text-xs uppercase tracking-wider">
              {landing['badge']}
            </span>
            <h1 class="font-heading font-black text-3xl sm:text-5xl lg:text-6xl text-slate-950 leading-[1.1] uppercase tracking-tight">
              {landing['h1']}
            </h1>
            <p class="text-base sm:text-lg text-slate-600 font-medium leading-relaxed">
              {landing['subtitle']}
            </p>

            <div class="pt-2 flex flex-col sm:flex-row items-stretch sm:items-center gap-3.5">
              <a href="https://wa.me/34680317486?text={wa_encoded}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center justify-center gap-2.5 px-7 py-4 rounded-2xl bg-[#25D366] hover:bg-[#20ba59] text-white font-heading font-black text-base uppercase tracking-wider shadow-lg hover:scale-105 active:scale-95 transition">
                <i data-lucide="message-circle" class="w-5 h-5"></i>
                <span>{cta_hero_text}</span>
              </a>
              <a href="#precios" class="inline-flex items-center justify-center gap-2 px-6 py-4 rounded-2xl bg-white hover:bg-slate-100 border border-slate-300 text-slate-900 font-heading font-bold text-base transition">
                <span>Ver Tarifas</span>
                <i data-lucide="arrow-down" class="w-4 h-4"></i>
              </a>
            </div>

            <div class="pt-3 flex items-center gap-4 text-xs font-bold text-slate-500">
              {hero_badges_html}
            </div>
          </div>

          <div class="lg:col-span-5">
            <div class="aspect-[4/3] rounded-3xl overflow-hidden bg-white shadow-xl border border-slate-200 p-2">
              <img src="../{landing['hero_img']}" alt="{landing['hero_img_alt']}" width="1200" height="800" class="w-full h-full object-cover rounded-2xl">
            </div>
            <div class="mt-3 text-center text-xs font-bold text-slate-500 uppercase tracking-wider">
              {landing['price_anchor']}
            </div>
          </div>

        </div>

      </div>
    </section>

    <!-- BENEFICIOS & ESPECIFICACIONES -->
    <section class="py-14 sm:py-20 bg-white border-b border-slate-200">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center max-w-2xl mx-auto mb-10 sm:mb-14 space-y-2">
          <h2 class="font-heading font-black text-2xl sm:text-4xl text-slate-950 uppercase tracking-tight">
            {why_title}
          </h2>
          <p class="text-sm sm:text-base text-slate-600 font-medium">
            {why_sub}
          </p>
        </div>

        <div class="grid md:grid-cols-3 gap-6 sm:gap-8">
          {benefits_html}
        </div>
      </div>
    </section>

    <!-- TARIFAS & PROCESO (FONDO AZUL TEXTURIZADO CANVA) -->
    <section id="precios" class="py-14 sm:py-20 bg-[#3478a6] bg-textured-blue text-white border-b border-sky-700/40">
      <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div class="text-center max-w-2xl mx-auto mb-10 space-y-2">
          <h2 class="font-heading font-black text-2xl sm:text-4xl uppercase tracking-tight">
            {precios_title}
          </h2>
          <p class="text-white/80 text-sm sm:text-base">
            {precios_sub}
          </p>
        </div>

        <!-- Tabla de Tarifas -->
        <div class="bg-white rounded-3xl p-6 sm:p-8 text-slate-950 shadow-2xl mb-12">
          {table_html}
        </div>

        <!-- Proceso en 3 pasos -->
        {pasos_html}

      </div>
    </section>

    <!-- FAQS -->
    <section class="py-14 sm:py-20 bg-slate-50 border-b border-slate-200">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center max-w-2xl mx-auto mb-10 space-y-2">
          <h2 class="font-heading font-black text-2xl sm:text-4xl text-slate-950 uppercase tracking-tight">
            Preguntas Frecuentes
          </h2>
          <p class="text-sm sm:text-base text-slate-600 font-medium">
            {faq_sub}
          </p>
        </div>

        <div class="space-y-4">
          {faq_html}
        </div>
      </div>
    </section>

    <!-- HERRAMIENTAS GRATUITAS PARA DIRECTORES DE CLUB -->
    <section class="py-12 sm:py-16 bg-white border-b border-slate-200">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center max-w-2xl mx-auto mb-8 space-y-1.5">
          <span class="text-[#f2920b] font-heading font-black text-xs uppercase tracking-widest">Recursos Interactivos Gratuitos</span>
          <h2 class="font-heading font-black text-2xl sm:text-3xl text-slate-950 uppercase tracking-tight">
            Calculadoras y Generadores para tu Club
          </h2>
        </div>
        <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <a href="/herramientas/generador-americana-padel/" class="group bg-slate-50 hover:bg-slate-100 border border-slate-200 hover:border-[#f2920b] rounded-2xl p-5 transition flex flex-col justify-between">
            <div>
              <span class="text-[10px] font-black uppercase tracking-widest text-[#f2920b]">Torneos Sociales</span>
              <h3 class="font-heading font-black text-base text-slate-950 group-hover:text-[#f2920b] transition mt-1">Generador Americana</h3>
              <p class="text-xs text-slate-600 mt-1">Cuadros y rotaciones para 8 a 24 jugadores en WhatsApp.</p>
            </div>
            <span class="text-xs font-bold text-slate-900 mt-4 inline-flex items-center gap-1">Abrir gratis →</span>
          </a>
          <a href="/herramientas/generador-cuadros-torneo-padel/" class="group bg-slate-50 hover:bg-slate-100 border border-slate-200 hover:border-[#76d3f6] rounded-2xl p-5 transition flex flex-col justify-between">
            <div>
              <span class="text-[10px] font-black uppercase tracking-widest text-[#3478a6]">Eliminatoria + Consolación</span>
              <h3 class="font-heading font-black text-base text-slate-950 group-hover:text-[#3478a6] transition mt-1">Generador Cuadros</h3>
              <p class="text-xs text-slate-600 mt-1">Sorteo de cabezas de serie, byes y horarios de pista.</p>
            </div>
            <span class="text-xs font-bold text-slate-900 mt-4 inline-flex items-center gap-1">Abrir gratis →</span>
          </a>
          <a href="/herramientas/calculadora-coste-pistas-padel/" class="group bg-slate-50 hover:bg-slate-100 border border-slate-200 hover:border-emerald-500 rounded-2xl p-5 transition flex flex-col justify-between">
            <div>
              <span class="text-[10px] font-black uppercase tracking-widest text-emerald-600">Simulador Inversión</span>
              <h3 class="font-heading font-black text-base text-slate-950 group-hover:text-emerald-600 transition mt-1">Coste Pistas Pádel</h3>
              <p class="text-xs text-slate-600 mt-1">Presupuesto de obra civil, cristal, césped y amortización.</p>
            </div>
            <span class="text-xs font-bold text-slate-900 mt-4 inline-flex items-center gap-1">Calcular presupuesto →</span>
          </a>
          <a href="/herramientas/calculadora-roi-camaras-padel/" class="group bg-slate-50 hover:bg-slate-100 border border-slate-200 hover:border-[#f2920b] rounded-2xl p-5 transition flex flex-col justify-between">
            <div>
              <span class="text-[10px] font-black uppercase tracking-widest text-[#f2920b]">Monetización Pistas</span>
              <h3 class="font-heading font-black text-base text-slate-950 group-hover:text-[#f2920b] transition mt-1">ROI Cámaras IA</h3>
              <p class="text-xs text-slate-600 mt-1">Calcula el beneficio mensual neto con Save my Play.</p>
            </div>
            <span class="text-xs font-bold text-slate-900 mt-4 inline-flex items-center gap-1">Simular retorno →</span>
          </a>
        </div>
      </div>
    </section>

    <!-- CTA FINAL -->
    <section class="py-14 sm:py-20 bg-white text-center">
      <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 space-y-6">
        <h2 class="font-heading font-black text-3xl sm:text-5xl text-slate-950 uppercase tracking-tight">
          ¿Hablamos de tu club o torneo?
        </h2>
        <p class="text-slate-600 text-base sm:text-lg">
          {cta_sub}
        </p>
        <div class="pt-2 flex flex-col sm:flex-row items-center justify-center gap-4">
          <a href="https://wa.me/34680317486?text={wa_encoded}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2.5 px-8 py-4 rounded-full bg-[#25D366] hover:bg-[#20ba59] text-white font-heading font-black text-base uppercase tracking-wider shadow-lg hover:scale-105 active:scale-95 transition">
            <i data-lucide="message-circle" class="w-5 h-5"></i>
            <span>Hablar por WhatsApp</span>
          </a>
          <a href="mailto:javier@coolpadelstudios.com" class="inline-flex items-center gap-2 px-6 py-4 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-800 font-heading font-bold text-sm transition">
            <i data-lucide="mail" class="w-4 h-4"></i>
            <span>javier@coolpadelstudios.com</span>
          </a>
        </div>
      </div>
    </section>
  </main>

  <!-- FOOTER INFERIOR (COLOR CELESTE LLAVEROS #3478a6 CON TEXTURA CANVA: BRANDING COOLPADEL, SILOS TEMÁTICOS SEO Y COPYRIGHT) -->
  <footer class="relative z-20 bg-[#3478a6] bg-textured-blue text-white pt-14 pb-10 border-t border-sky-700/40 text-xs">
    <div class="max-w-[1700px] mx-auto px-4 sm:px-8 space-y-10">
      
      <!-- TOP: BRANDING Y DESCRIPCIÓN B2B -->
      <div class="flex flex-col sm:flex-row items-center justify-between gap-4 pb-8 border-b border-white/20">
        <div class="flex items-center gap-3.5">
          <img src="../assets/images/coolpadel-mascot-hd.png" alt="CoolPadel Mascota" width="60" height="60" class="h-10 sm:h-12 w-auto object-contain drop-shadow-sm" loading="lazy">
          <img src="../assets/images/coolpadel-typography-hd.png" alt="CoolPadel" width="160" height="32" class="h-5 sm:h-6 w-auto object-contain drop-shadow-sm" loading="lazy">
        </div>
        <p class="text-white/80 text-xs text-center sm:text-right max-w-md font-medium">
          Fabricación de llaveros de pádel personalizados 3D y sistemas de cámaras de grabación en pista Save my Play.
        </p>
      </div>

      <!-- 4 COLUMNAS DE SILOS TEMÁTICOS SEO -->
      <nav aria-label="Estructura y Silos SEO de CoolPadel" class="grid grid-cols-2 lg:grid-cols-4 gap-8 text-left">
        
        <!-- COLUMNA 1: SOLUCIONES B2B -->
        <div class="space-y-3">
          <div class="font-heading font-black text-sm uppercase tracking-wider text-white">
            Soluciones B2B
          </div>
          <ul class="space-y-2 text-white/80 font-normal">
            <li><a href="/llaveros-padel-personalizados/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Llaveros de Pádel 3D</a></li>
            <li><a href="/llaveros-tenis-personalizados/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Llaveros de Tenis y Pickleball</a></li>
            <li><a href="/welcome-packs-torneos-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Welcome Packs para Torneos</a></li>
            <li><a href="/llaveros-personalizados-clubs-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Merchandising para Clubs</a></li>
            <li><a href="/camaras/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Cámaras Save my Play</a></li>
            <li><a href="/camaras-grabacion-pistas-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Grabación en Pista de Pádel</a></li>
          </ul>
        </div>

        <!-- COLUMNA 2: HERRAMIENTAS & SOFTWARE -->
        <div class="space-y-3">
          <div class="font-heading font-black text-sm uppercase tracking-wider text-white">
            Herramientas &amp; SaaS
          </div>
          <ul class="space-y-2 text-white/80 font-normal">
            <li><a href="/herramientas/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition font-bold text-white">Hub Herramientas B2B</a></li>
            <li><a href="/herramientas/generador-americana-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Generador Americana Pádel</a></li>
            <li><a href="/herramientas/generador-cuadros-torneo-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Generador Cuadros Torneo</a></li>
            <li><a href="/herramientas/calculadora-coste-pistas-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Calculadora Coste Pistas</a></li>
            <li><a href="/herramientas/calculadora-roi-camaras-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Calculadora ROI Cámaras</a></li>
            <li><a href="/camaras-padel-playtomic/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Integración con Playtomic</a></li>
            <li><a href="/camaras-padel-matchi/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Compatibilidad Matchi</a></li>
            <li><a href="/camaras-padel-resasports/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Conexión Resasports</a></li>
          </ul>
        </div>

        <!-- COLUMNA 3: DIRECTORIO & HUBS LOCALES -->
        <div class="space-y-3">
          <div class="font-heading font-black text-sm uppercase tracking-wider text-white">
            Directorio &amp; Hubs
          </div>
          <ul class="space-y-2 text-white/80 font-normal">
            <li><a href="/franquicias-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Directorio Franquicias (+167)</a></li>
            <li><a href="/blog/barometro-camaras-padel-2026/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Barómetro del Pádel 2026</a></li>
            <li><a href="/camaras-padel-madrid/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Clubes Pádel Madrid</a></li>
            <li><a href="/camaras-padel-barcelona/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Clubes Pádel Barcelona</a></li>
            <li><a href="/#cobertura" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Envíos España, USA y Europa</a></li>
            <li><a href="/#mapa" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Mapa de Clientes Oficiales</a></li>
          </ul>
        </div>

        <!-- COLUMNA 4: GUÍAS DEL SECTOR -->
        <div class="space-y-3">
          <div class="font-heading font-black text-sm uppercase tracking-wider text-white">
            Guías &amp; Blog B2B
          </div>
          <ul class="space-y-2 text-white/80 font-normal">
            <li><a href="/blog/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition font-bold text-white">Índice del Blog &amp; Newsletter</a></li>
            <li><a href="/blog/como-organizar-torneo-padel-americana-reglas-cuadros/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Cómo Organizar una Americana</a></li>
            <li><a href="/blog/cuanto-cuesta-montar-pista-padel-presupuesto-rentabilidad/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Cuánto Cuesta una Pista 2026</a></li>
            <li><a href="/blog/rentabilidad-camaras-pistas-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Precios y ROI de Cámaras</a></li>
            <li><a href="/blog/welcome-pack-torneo-padel-ideas/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Ideas de Welcome Pack</a></li>
            <li><a href="/blog/sistemas-grabacion-pistas-padel-comparativa/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Cámaras fijas vs Trípodes (RGPD)</a></li>
          </ul>
        </div>

      </nav>

      <!-- BOTTOM: COPYRIGHT Y ENLACES LEGALES -->
      <div class="pt-8 border-t border-white/20 flex flex-col sm:flex-row items-center justify-between gap-3 text-white/75 text-center sm:text-left">
        <span id="admin-toggle-trigger" class="hover:text-white/90 transition cursor-pointer" title="Modo Administrador">
          © 2026 CoolPadel Studios · All rights reserved
        </span>
        <div class="flex items-center gap-3">
          <a href="/politica-de-devoluciones.html" class="hover:text-white/90 underline decoration-white/30 underline-offset-2 transition" title="Política de Devoluciones y Garantía">Política de Devoluciones</a>
          <span class="opacity-40">·</span>
          <a href="https://www.instagram.com/coolpadel_/" target="_blank" rel="noopener noreferrer" class="opacity-75 hover:opacity-100 transition text-white" title="Instagram CoolPadel">@coolpadel_</a>
        </div>
      </div>

    </div>
  </footer>

  <script>
    lucide.createIcons();
  </script>
  <script src="/assets/js/cp-analytics.js" defer></script>
</body>
</html>
"""
    return html

def build_all_landings():
    print(">> Generando Landings B2B Transaccionales...")
    for l in LANDINGS:
        slug = l["slug"]
        out_dir = f"coolpadel-web/{slug}"
        os.makedirs(out_dir, exist_ok=True)
        html_content = render_landing(l)
        with open(f"{out_dir}/index.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"  [OK] coolpadel-web/{slug}/index.html")

if __name__ == "__main__":
    build_all_landings()
