
def get_llaveros_calculator_html(lang="es", asset_prefix="../"):
    return f'''
    <div class="max-w-4xl mx-auto w-full bg-white rounded-3xl p-5 sm:p-8 border border-slate-200/90 shadow-xl text-slate-950">
      <div class="text-center mb-6 space-y-1">
        <h3 class="text-xl sm:text-3xl font-black font-heading text-slate-950 uppercase tracking-tight">
          Calcula tu pedido
        </h3>
        <p class="text-xs sm:text-sm text-slate-500 font-medium">
          Muestra 15€ reembolsable · Tarifa directa de fábrica
        </p>
      </div>

      <div class="space-y-6">
        <div class="flex justify-between items-end pb-3 border-b border-slate-100">
          <div>
            <span class="text-[11px] font-bold text-slate-500 uppercase tracking-wider block">Nº de llaveros:</span>
            <span id="landing-calc-qty" class="text-xl sm:text-3xl font-black font-heading text-slate-950">100 unidades</span>
          </div>
          <div class="text-right">
            <span class="text-[11px] font-bold text-slate-500 uppercase tracking-wider block">Importe estimado:</span>
            <div class="flex items-baseline justify-end gap-1.5">
              <span id="landing-calc-price" class="text-xl sm:text-3xl font-black font-heading text-[#f2920b]">300 €</span>
              <span id="landing-calc-unit" class="text-xs font-bold text-slate-500">(3,00 €/ud)</span>
            </div>
          </div>
        </div>

        <!-- Slider -->
        <div class="py-2">
          <div class="relative w-full h-3 bg-slate-200 rounded-full cursor-pointer" id="landing-slider-track" onclick="handleLandingSliderClick(event)">
            <div id="landing-slider-prog" class="absolute top-0 left-0 h-full bg-[#f2920b] rounded-full" style="width: 0%;"></div>
            <div id="landing-slider-thumb" class="absolute top-1/2 -translate-x-1/2 -translate-y-1/2 w-8 h-4 flex items-center justify-center cursor-grab active:cursor-grabbing hover:scale-110 transition-transform" style="left: 0%;">
              <img src="{asset_prefix}assets/images/eyes-thumb.png" alt="Selector" width="36" height="18" class="w-full h-full object-contain drop-shadow-sm select-none">
            </div>
          </div>
          <div class="relative w-full text-[11px] font-extrabold text-slate-500 h-6 mt-3">
            <button type="button" onclick="setLandingTier(0)" class="absolute left-0 hover:text-[#f2920b] transition">100 uds</button>
            <button type="button" onclick="setLandingTier(1)" class="absolute left-[33.3%] -translate-x-1/2 hover:text-[#f2920b] transition">250 uds</button>
            <button type="button" onclick="setLandingTier(2)" class="absolute left-[66.6%] -translate-x-1/2 hover:text-[#f2920b] transition">500 uds</button>
            <button type="button" onclick="setLandingTier(3)" class="absolute right-0 hover:text-[#f2920b] transition">1.500 uds</button>
          </div>
        </div>

        <div class="flex flex-wrap items-center justify-center gap-3 pt-2 text-xs font-bold">
          <span class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-emerald-50 text-emerald-800 border border-emerald-200/80">
            <i data-lucide="check-circle" class="w-4 h-4 text-emerald-600"></i>
            Muestra 15€ reembolsable
          </span>
          <span class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-slate-100 text-slate-700 border border-slate-200">
            IVA no incluido
          </span>
        </div>

        <div class="pt-2">
          <a href="#contacto" class="w-full py-3.5 rounded-2xl font-heading font-black text-sm uppercase tracking-wider bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 shadow-md hover:shadow-lg hover:scale-[1.01] active:scale-[0.98] flex items-center justify-center gap-2 transition-all">
            <span>Contactar</span>
            <i data-lucide="arrow-down" class="w-4 h-4 stroke-[3]"></i>
          </a>
        </div>
      </div>
    </div>'''

#!/usr/bin/env python3

"""

Generador de Landings B2B Transaccionales para CoolPadel:

1. /llaveros-padel-personalizados/ -> Core B2B Llaveros de Pádel 3D

2. /llaveros-tenis-personalizados/ -> Llaveros de Tenis y Academias

3. /welcome-packs-torneos-padel/   -> Welcome Packs y Regalos para Torneos

4. /llaveros-personalizados-clubs-padel/ -> Merchandising y Llaveros para Clubs de Pádel

"""



import os
import urllib.parse
from datetime import datetime
try:
    from translations_landings import LANDINGS_I18N, COMMON_UI
except ImportError:
    import sys
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from translations_landings import LANDINGS_I18N, COMMON_UI




WEBHOOK_URL = 'https://script.google.com/macros/s/AKfycbxnF9JmVrikeAW7PdLc02r_1kkuSJVz1Ncl71ZeVGT37H0ji5DQ3DVw60122pcuYnxCgA/exec'



LANDINGS = [

    {

        "slug": "llaveros-padel-personalizados",

        "title": "Llaveros Pádel Personalizados 3D [Desde 1,50€] | CoolPadel",

        "meta_desc": "Fabricante de llaveros de pádel personalizados en goma 3D con forma de pala y logo oficial. Pedidos desde 100 uds y muestra física real por 15€.",

        "badge": "",

        "breadcrumb_leaf": "Llaveros Pádel 3D",

        "h1": "Llaveros de Pádel Personalizados con Forma de Pala y Logo Oficial",

        "subtitle": "El detalle que tus jugadores llevan siempre en su paletero.",

        "hero_img": "assets/images/llaveros-padel-personalizados-clubs.jpg",

        "hero_img_alt": "Llaveros de pádel personalizados con forma de pala de goma 3D con logo oficial para clubes",

        "wa_msg": "Hola Javier, quiero información y presupuesto para llaveros de pádel personalizados para mi club",

        "price_anchor": "Desde 1,50 € / ud · Pedido mínimo 100 uds",

        "target_audience": "",

        "quick_summary": {

            "label_1": "Tarifa B2B", "val_1": "Desde 1,50 € a 3,00 € / ud",

            "label_2": "Pedido Mínimo", "val_2": "100 unidades (Tirada inicial)",

            "label_3": "Muestra Física", "val_3": "15 € con logo real (~15 días, 100% deducible)",

            "label_4": "Plazo Entrega", "val_4": "~1 mes con envíos incluidos a España, Europa y USA",

            "p": "CoolPadel es fabricante directo B2B de llaveros de pádel personalizados en goma PVC 3D microinyectada con relieve y logo oficial para clubes y torneos. Pedidos desde 100 unidades con tarifa directa de fábrica, muestra física real previa y envíos incluidos."

        },

        "benefits": [

            ("Relieve 3D Microinyectado", "Goma PVC flexible de alta densidad, resistente a caídas, agua y rozaduras dentro del paletero."),

            ("Muestra Física Previa 15€", "Fabricamos una muestra real con tu logo antes de confirmar la tirada completa. Reembolsable 100% con el pedido."),

            ("Tarifa Directa de Fábrica", "Desde 1,50€ a 3,00€ por unidad con envíos incluidos a España, Europa y Estados Unidos.")

        ],

        "faqs": [

            ("¿Cuál es el pedido mínimo y los plazos de entrega?", "El pedido mínimo de producción es de 100 unidades. El plazo de entrega de la muestra física real es de unos 15 días laborables y la entrega del pedido final se sitúa en torno a un mes según volumen."),

            ("¿Cómo solicitamos la muestra física de 15€?", "Solo tienes que enviarnos el logo de tu club en cualquier formato (vectorial, PNG, JPG). Preparamos el diseño 3D y fabricamos una muestra real enviada a tu dirección por 15€ (100% descontables del pedido final)."),

            ("¿Se puede personalizar el reverso del llavero?", "Sí, podemos añadir el logo de un patrocinador, la página web del club o las redes sociales en el reverso."),
            ("¿Los precios incluyen IVA? ¿Cómo se realiza el pago y la facturación?", "Los precios mostrados no incluyen IVA. Emitimos factura oficial a nombre del club o empresa y el pago se realiza por adelantado mediante transferencia o tarjeta tras recibir la muestra."),
            ("¿Se descuenta el coste de la muestra física de 15 €?", "Sí. Los 15 € abonados para producir la muestra física real se descuentan al 100% del importe total del pedido final."),
            ("¿Qué tamaño tienen los llaveros de pádel personalizados?", "Unos 70 mm de largo: tamaño equilibrado, ligero e ideal para paleteros, mochilas o llaves."),
            ("¿Puedo vender los llaveros en la tienda o recepción de mi club?", "Sí, claro. Los clubs los suelen vender fácilmente en recepción o en su tienda en torno a 5-6 € cada uno."),
            ("¿Para qué ocasiones o usos sirven los llaveros de pádel?", "Welcome packs de torneos, regalos en cenas de socios de fin de temporada, activaciones de patrocinadores del club, inscripciones a torneos y escuelas, o como detalle institucional en eventos corporativos y aperturas."),
            ("¿Qué clubes y torneos confían ya en CoolPadel?", "Más de 30 clubs en España, Italia, Francia, Bélgica y Estados Unidos. Consulta el mapa interactivo en nuestra página principal."),
            ("¿A qué países realizáis envíos?", "Envíos directos en toda España, la Unión Europea y Estados Unidos. Consultar condiciones para el resto de países.")


        ]

    },

    {

        "slug": "llaveros-tenis-personalizados",

        "title": "Llaveros Tenis Personalizados 3D [Desde 1,50€] | CoolPadel",

        "meta_desc": "Llaveros de tenis personalizados en relieve 3D con el escudo de tu club o torneo. Goma flexible de calidad, pedidos desde 100 uds y muestra física por 15€.",

        "badge": "",

        "breadcrumb_leaf": "Llaveros de Tenis",

        "h1": "Llaveros de Tenis Personalizados con tu Escudo Oficial",

        "subtitle": "Diseñamos y fabricamos llaveros de tenis en relieve 3D para escuelas de tenis, torneos sociales, clubes históricos y welcome packs. Un obsequio elegante y duradero.",

        "hero_img": "assets/images/llaveros-tenis-personalizados-clubs.jpg",

        "hero_img_alt": "Llaveros de tenis personalizados con relieve 3D para clubs y escuelas deportivas",

        "wa_msg": "Hola Javier, quiero presupuesto para llaveros de tenis personalizados para nuestro club/academia",

        "price_anchor": "Desde 1,50 € / ud · Muestra física real 15 €",

        "target_audience": "Clubes de tenis, academias de alto rendimiento, escuelas deportivas y eventos de tenis federados o sociales.",

        "quick_summary": {

            "label_1": "Tarifa B2B", "val_1": "Desde 1,50 € a 3,00 € / ud",

            "label_2": "Pedido Mínimo", "val_2": "100 unidades (Escuelas y torneos)",

            "label_3": "Muestra Física", "val_3": "15 € con escudo oficial (100% deducible)",

            "label_4": "Plazo Entrega", "val_4": "~15 días muestra · ~1 mes pedido final",

            "p": "Fabricación oficial de llaveros de tenis personalizados en relieve 3D de PVC microinyectado flexible. No raya raquetas ni fundas, pedidos desde 100 unidades para academias y clubes tradicionales con muestra física previa por 15€."

        },

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

        "title": "Welcome Packs Torneos Pádel [Desde 1,50€] | CoolPadel",

        "meta_desc": "Regalos originales y detalles para welcome packs de torneos de pádel. Llaveros de goma 3D personalizados con logo. Tiradas desde 100 uds y muestra por 15€.",

        "badge": "TORNEOS, CIRCUITOS & WELCOME PACKS",

        "breadcrumb_leaf": "Welcome Packs Torneos",

        "h1": "Welcome Packs y Regalos de Pádel para Torneos y Eventos",

        "subtitle": "Olvídate de las camisetas o toallas genéricas que acaban olvidadas en un cajón. Un llavero 3D personalizado con forma de pala y el logo del torneo es el regalo y detalle de pádel que los participantes lucen todo el año en su paletero.",

        "hero_img": "assets/images/slide-1.jpg",

        "hero_img_alt": "Welcome packs y llaveros 3D para torneos de pádel oficiales",

        "wa_msg": "Hola Javier, estoy organizando un torneo de pádel y busco regalos/welcome packs para los jugadores",

        "price_anchor": "Especial torneos: 100 a 1.500+ uds · Tarifa directa de fábrica",

        "target_audience": "Directores de torneos, organizadores de circuitos de pádel, patrocinadores y empresas que buscan un regalo publicitario de alto valor percibido.",

        "quick_summary": {

            "label_1": "Coste Jugador", "val_1": "Desde 1,50 € / participante",

            "label_2": "Tirada Torneo", "val_2": "100 a 1.500+ unidades según cuadros",

            "label_3": "Muestra Física", "val_3": "15 € con logo del torneo (100% deducible)",

            "label_4": "Planificación", "val_4": "Muestra ~15 días · Pedido completo en ~1 mes",

            "p": "Regalos y detalles de bienvenida para torneos y circuitos de pádel. Llaveros en relieve 3D con forma de pala personalizada con el logo del torneo en el anverso y patrocinador en el reverso. Factura desglosada con IVA deducible para organizaciones."

        },

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

        "title": "Llaveros Personalizados Clubs Pádel [Muestra 15€]",

        "meta_desc": "Llaveros oficiales y merchandising para clubes de pádel. Detalles de goma 3D para socios, escuelas y venta en pro-shop con +60% de margen. Más de 30 clubes.",

        "badge": "MERCHANDISING OFICIAL DE CLUB",

        "breadcrumb_leaf": "Llaveros Clubs Pádel",

        "h1": "Merchandising Oficial y Llaveros para Clubs de Pádel",

        "subtitle": "Refuerza la identidad y el sentido de pertenencia de tu comunidad. Más de 30 clubes en España, Europa y EE. UU. ya equipan a sus socios y pro-shops con llaveros y merchandising CoolPadel.",

        "hero_img": "assets/images/llaveros-padel-personalizados-clubs.jpg",

        "hero_img_alt": "Llaveros oficiales personalizados para clubes de pádel y escuelas",

        "wa_msg": "Hola Javier, soy responsable de un club de pádel y quiero información para hacer los llaveros de nuestros socios",

        "price_anchor": "Tarifa club desde 1,50 € / ud · Muestra previa 15 €",

        "target_audience": "Gerentes de clubes, directores deportivos, comités de socios y responsables de pro-shop que desean merchandising oficial rentable y atractivo.",

        "quick_summary": {

            "label_1": "Tarifa Club", "val_1": "Desde 1,50 € a 3,00 € / ud (PVP 5-6€)",

            "label_2": "Margen Tienda", "val_2": "+60% de rentabilidad en recepción",

            "label_3": "Muestra Física", "val_3": "15 € con el escudo del club (100% deducible)",

            "label_4": "Reposiciones", "val_4": "Molde guardado sin coste para pedidos futuros",

            "p": "Merchandising oficial de fidelización para socios y venta en pro-shop de clubes de pádel. Fabricación en goma 3D con relieve de escudo oficial, tiradas desde 100 unidades y entrega en ~1 mes con soporte de Javier Villoria."

        },

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

        "title": "Cámaras con IA para Pistas de Pádel [Sin Obras] | Save My Play",

        "meta_desc": "Cámaras con IA para pistas de pádel: grabación automática con pulsador, clips en 25s al móvil y sin obras. Desde 45 €/mes. Pide tu demo para tu club.",

        "badge": "TECNOLOGÍA DE CLUB · SAVE MY PLAY",

        "breadcrumb_leaf": "Grabación sin Obras",

        "h1": "Cámaras Inteligentes para Pistas de Pádel sin Obras",

        "subtitle": "La tecnología de repetición y analítica en pista que fideliza a tus jugadores y genera ingresos recurrentes para tu club de pádel o tenis. Sin permanencia, sin zanjas y montado en 5 minutos.",

        "hero_img": "assets/images/savemyplay-1.jpg",

        "hero_img_alt": "Sistema de cámaras inteligentes de grabación para pistas de pádel Save My Play",

        "wa_msg": "Hola Javier, quiero información sobre el sistema de cámaras y grabación Save My Play para las pistas de mi club",

        "price_anchor": "Hardware 180 € / pista · Software desde 45 €/mes · Sin obras",

        "target_audience": "Gerentes de clubes de pádel y tenis, directores de academias e inversores deportivos que buscan modernizar sus pistas con vídeo de alta definición.",

        "quick_summary": {

            "label_1": "Hardware Pista", "val_1": "180 € / cámara en propiedad (Pago único)",

            "label_2": "Cuota Software", "val_2": "Desde 45 € / mes por pista (Plan B Highlights)",

            "label_3": "Permanencia", "val_3": "0 meses (Cancelación libre mes a mes)",

            "label_4": "Instalación", "val_4": "5 minutos sin obras ni zanjas en pista",

            "p": "Save My Play es el sistema autónomo de grabación de partidos y highlights en pista de pádel y tenis sin obras civiles. Pulsador físico en red, descarga instantánea por QR sin apps y retransmisión por YouTube en Full HD."

        },

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

        "title": "Cámaras Pistas Pádel Playtomic [45€/mes] | Save My Play",

        "meta_desc": "Cámaras Save my Play para pistas de pádel en Playtomic. Grabación con pulsador en red, repeticiones por QR y monetización sin obras ni permanencia.",

        "badge": "INTEGRACIÓN PLAYTOMIC & SAVE MY PLAY",

        "breadcrumb_leaf": "Integración Playtomic",

        "h1": "Cámaras Inteligentes Save my Play para Clubes en Playtomic",

        "subtitle": "El complemento perfecto para tu gestión en Playtomic: añade grabación de partidos con pulsador en pista, repeticiones instantáneas y streaming en YouTube sin obras ni permanencias.",

        "hero_img": "assets/images/savemyplay-1.jpg",

        "hero_img_alt": "Cámaras Save my Play compatibles con pistas Playtomic",

        "wa_msg": "Hola Javier, gestionamos nuestro club con Playtomic y queremos información de cámaras Save my Play para las pistas",

        "price_anchor": "Hardware 180 € / pista · Cuota 45 €/mes · 0 permanencia",

        "target_audience": "Gerentes y directores deportivos de clubes que gestionan sus pistas y reservas con Playtomic.",

        "quick_summary": {

            "label_1": "Hardware Pista", "val_1": "180 € / cámara en propiedad (Pago único)",

            "label_2": "Cuota Software", "val_2": "45 € / mes por pista · Sin permanencia",

            "label_3": "Compatibilidad", "val_3": "100% independiente de Playtomic, sin tocar reservas",

            "label_4": "Instalación", "val_4": "Montaje en 5 min sin cortes en tus reservas",

            "p": "Cámaras en pista Save My Play para clubes con sistema de reservas Playtomic. Los jugadores juegan su reserva habitual y descargan highlights por QR con pulsador en la red, sin obras ni contratos de permanencia."

        },

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

        "title": "Cámaras Pádel para Clubs Matchi [45€/mes] | Save My Play",

        "meta_desc": "Sistema de grabación autónomo Save my Play para instalaciones de pádel con Matchi. Replay instantáneo con QR, 0 obras y hardware en propiedad por 180 €.",

        "badge": "INTEGRACIÓN MATCHI & SAVE MY PLAY",

        "breadcrumb_leaf": "Integración Matchi",

        "h1": "Grabación en Pista y Replay para Clubes que Usan Matchi",

        "subtitle": "Equipa tus pistas Matchi con la tecnología Save my Play. Descarga de mejores jugadas por código QR sin necesidad de descargar apps pesadas ni contratos de permanencia.",

        "hero_img": "assets/images/savemyplay-2.jpg",

        "hero_img_alt": "Sistema de cámaras Save my Play para clubes que usan Matchi",

        "wa_msg": "Hola Javier, usamos Matchi en nuestro club y queremos poner cámaras Save my Play en las pistas",

        "price_anchor": "Hardware 180 € / pista · Software desde 45 €/mes · Sin permanencia",

        "target_audience": "Operadores y clubes en España, Suecia, Noruega y Reino Unido que gestionan sus pistas con la plataforma Matchi.",

        "quick_summary": {

            "label_1": "Hardware Pista", "val_1": "180 € en propiedad por pista",

            "label_2": "Cuota Software", "val_2": "Desde 45 € / mes · 0 permanencia",

            "label_3": "Autonomía", "val_3": "Ideal para clubes 24/7 sin personal",

            "label_4": "Instalación", "val_4": "Fijación homologada a poste en 5 minutos",

            "p": "Solución de grabación y repetición instantánea Save My Play para clubes con software Matchi. Visualización y descarga por código QR en visor web multilenguaje sin descargas de apps ni permanencias de 3 a 5 años."

        },

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

        "title": "Cámaras Pádel Resasports [0 Obras · 45€/mes] | Save My Play",

        "meta_desc": "Grabación para centros deportivos y clubes con software Resasports. Montaje en 5 minutos, pulsador en red y cuota desde 45€/mes sin permanencia.",

        "badge": "INTEGRACIÓN RESASPORTS & SAVE MY PLAY",

        "breadcrumb_leaf": "Integración Resasports",

        "h1": "Grabación Inteligente en Pista para Clubes con Resasports",

        "subtitle": "Potencia la experiencia de tus abonados en Resasports con repetición instantánea en pista, retransmisión por YouTube y cero costes de obra civil.",

        "hero_img": "assets/images/savemyplay-3.jpg",

        "hero_img_alt": "Cámaras Save my Play para instalaciones deportivas con Resasports",

        "wa_msg": "Hola Javier, gestionamos nuestro centro con Resasports y nos interesa la grabación Save my Play",

        "price_anchor": "Hardware 180 € / pista · Cuota 45 €/mes · Cero obras",

        "target_audience": "Centros municipales, clubes de tenis/pádel y complejos deportivos que operan con Resasports.",

        "quick_summary": {

            "label_1": "Inversión Hardware", "val_1": "180 € por pista (Frente a +2.500€ de otros)",

            "label_2": "Cuota Software", "val_2": "45 € / mes por pista · Sin permanencia",

            "label_3": "Legalidad RGPD", "val_3": "Consentimiento en pulsador y buffer cerrado",

            "label_4": "Instalación", "val_4": "5 min sin permisos de obra pública ni zanjas",

            "p": "Grabación en pista Save My Play para polideportivos y concesiones deportivas que operan con Resasports. Montaje limpio sin obras civiles, cumplimiento íntegro del RGPD europeo y coste de hardware de 180€ en propiedad."

        },

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

        "title": "Cámaras Pistas Pádel Madrid [Demo Gratis] | Save My Play",

        "meta_desc": "Cámaras inteligentes Save my Play en Madrid (Pozuelo, Las Rozas, Alcobendas, La Moraleja). Grabación HD en 5 min, sin obras ni contratos de permanencia.",

        "badge": "COMUNIDAD DE MADRID · SAVE MY PLAY",

        "breadcrumb_leaf": "Pistas Madrid",

        "h1": "Cámaras Inteligentes para Pistas de Pádel en Madrid",

        "subtitle": "La tecnología en pista que eligen clubes referentes en la Comunidad de Madrid: grabación de partidos, pulsador en poste y retransmisión por YouTube sin cables ni zanjas.",

        "hero_img": "assets/images/savemyplay-1.jpg",

        "hero_img_alt": "Cámaras para pistas de pádel en clubes de Madrid",

        "wa_msg": "Hola Javier, tenemos pistas de pádel en Madrid y queremos presupuesto para cámaras Save My Play",

        "price_anchor": "Visita y demo presencial en Madrid · 180 € hardware · 45 €/mes",

        "target_audience": "Directores de clubes de pádel, complejos indoor y urbanizaciones de la Comunidad de Madrid.",

        "quick_summary": {

            "label_1": "Hardware Pista", "val_1": "180 € en propiedad · 45 €/mes software",

            "label_2": "Demostración", "val_2": "Visita presencial y demo técnica en Madrid",

            "label_3": "Contrato", "val_3": "0 permanencia (Mes a mes sin ataduras)",

            "label_4": "Instalación", "val_4": "Montaje en 5 min en pistas indoor o descubiertas",

            "p": "Instalación de cámaras de grabación Save My Play para clubes de pádel en la Comunidad de Madrid (Pozuelo, Las Rozas, Alcobendas, Majadahonda). Visita técnica presencial, montaje en 5 minutos y repeticiones por QR."

        },

        "benefits": [

            ("Soporte y Demostración Presencial en Madrid", "Sede de CoolPadel en Madrid: podemos visitarte y hacer una demostración real en tus instalaciones."),

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

        "title": "Cámaras Pistas Pádel Barcelona [0 Obras] | Save My Play",

        "meta_desc": "Cámaras Save my Play en Barcelona y Cataluña (Sant Cugat, Badalona, Sabadell). Grabación con pulsador en red, repeticiones QR y streaming sin obras.",

        "badge": "BARCELONA & CATALUNYA · SAVE MY PLAY",

        "breadcrumb_leaf": "Pistas Barcelona",

        "h1": "Cámaras y Grabación de Partidos de Pádel en Barcelona",

        "subtitle": "La solución de vídeo más ágil para clubes indoor y outdoor en Barcelona y Cataluña: repetición instantánea en móvil, retransmisión de torneos y cero permanencia.",

        "hero_img": "assets/images/savemyplay-2.jpg",

        "hero_img_alt": "Cámaras Save my Play para pistas de pádel en Barcelona y Cataluña",

        "wa_msg": "Hola Javier, tenemos un club de pádel en Barcelona y queremos presupuesto para cámaras Save My Play",

        "price_anchor": "Hardware 180 € / pista · Software 45 €/mes · Envíos inmediatos",

        "target_audience": "Gerentes y clubes de pádel en Barcelona, área metropolitana y provincias de Girona, Tarragona y Lleida.",

        "quick_summary": {

            "label_1": "Hardware Pista", "val_1": "180 € en propiedad por pista",

            "label_2": "Cuota Software", "val_2": "45 € / mes por pista · Sin permanencia",

            "label_3": "Resistencia", "val_3": "Carcasa sellada IP para clima costero e indoor",

            "label_4": "Puesta en Marcha", "val_4": "Envío configurado en 48h con montaje en 5 min",

            "p": "Sistemas de grabación inteligente en pista Save My Play para clubes de pádel en Barcelona, Badalona, Sant Cugat, Sabadell y Cataluña. Pulsador físico en red, descarga inmediata por código QR y retransmisión por YouTube sin permanencias."

        },

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

    },

    {

        "slug": "save-my-play",

        "title": "Save my Play España: Cámaras con IA Oficiales para Pistas de Pádel",

        "meta_desc": "Save my Play España (+1.500 cámaras): cámara oficial USTA y USA Padel. 180 € hardware, cuota desde 27-45 €/mes, 0 obras y sin permanencia.",

        "badge": "CÁMARA OFICIAL USTA Y USA PADEL · +1.500 PISTAS",

        "breadcrumb_leaf": "Save my Play España",

        "h1": "Save my Play España: Sistema Oficial de Grabación y Cámaras para Pistas de Pádel",

        "subtitle": "La tecnología de grabación en pista líder mundial: más de 1.500 cámaras en todo el mundo. Hardware propio a 180 €, cuota desde 27 € a 45 €/mes, 0 obras y sin contratos de permanencia.",

        "hero_img": "assets/images/savemyplay-1.jpg",

        "hero_img_alt": "Cámaras oficiales para pistas de pádel y tenis Save My Play en España",

        "wa_msg": "Hola Javier, quiero información sobre el sistema oficial de cámaras Save My Play para mi club",

        "price_anchor": "Hardware 180 € / pista · Software desde 27 € a 45 €/mes · 0 permanencia",

        "target_audience": "Gerentes y directores de clubes de pádel y tenis, academias de alto rendimiento e inversores deportivos en España y Europa.",

        "quick_summary": {

            "label_1": "Hardware en Propiedad", "val_1": "180 € / cámara (Pago único, 1 por pista)",

            "label_2": "Cuota por Volumen", "val_2": "Desde 27 € a 45 € / mes por pista",

            "label_3": "Credenciales", "val_3": "Oficial USTA & USA PADEL (+1.500 cámaras)",

            "label_4": "Instalación", "val_4": "5 minutos (WiFi + enchufe, sin servidores)",

            "p": "Save My Play es el sistema oficial de grabación automática de partidos y highlights en pista de pádel y tenis, socio tecnológico de la USTA y USA Padel con más de 1.500 cámaras en todo el mundo. Hardware en propiedad por 180 €, cuotas mensuales por volumen desde 27 € a 45 €/mes y sin contratos de permanencia."

        },

        "benefits": [

            ("Cámara Oficial de las Federaciones Americanas (USTA y USA PADEL)", "Tecnología homologada y contrastada en más de 1.500 cámaras en todo el mundo, equipando sedes como el USTA National Campus en Florida y retransmisiones oficiales del circuito FIP de Miami."),

            ("Óptica Rectilínea Sin Efecto Pez (1 Cámara por Pista)", "La imagen y las líneas de pista no se ven curvadas. Cubrimos los 20x10 metros a la perfección con una sola cámara a 4 metros, ahorrando costes de hardware y cableados."),

            ("Sin Apps ni Registros Obligatorios (Cero Fricción)", "Los jugadores no necesitan descargar apps pesadas ni crearse cuentas: pulsan el botón en red y escanean el código QR para tener sus jugadas en 25 segundos en su móvil."),

            ("Tarifas Transparentes por Volumen sin Permanencia", "De 180 € de hardware único a cuotas escalonadas de 45 € (<5 pistas), 41 € (5-14), 36 € (15-24) y 27 € (>25 pistas). Cancelación libre mes a mes.")

        ],

        "faqs": [

            ("¿Por qué Save my Play solo necesita 1 cámara por pista mientras otros sistemas exigen 2?", "Porque nuestra cámara está calibrada específicamente con lente rectilínea para deportes de raqueta instalada a 4 metros de altura (poste o reja). Cubre el 100% de la pista (20x10 m) sin deformaciones ni efecto pez, ahorrando al club la mitad del coste en hardware y evitando zanjas complejas."),

            ("¿Ofrecéis también análisis de partido y estadísticas con IA?", "Sí, disponemos del módulo completo de analítica IA y coaching tools por 136 € al mes todo incluido. No obstante, para la mayoría de clubes recomendamos el plan de 45 €/mes, ya que el 90% de los jugadores amateurs solo busca guardar sus mejores puntos (highlights) para compartir en WhatsApp e Instagram."),

            ("¿Qué infraestructura necesita mi club para instalarlo?", "Únicamente una toma de corriente convencional y conexión WiFi estándar. No se necesitan servidores locales, zanjas en el suelo ni abrir rozas en el césped. Se ancla a la reja o poste en 5 minutos."),

            ("¿Quién gestiona Save my Play en España?", "Javier Villoria es el director de Save my Play en España y fundador de CoolPadel. Puedes contactar directamente por teléfono o WhatsApp en el +34 680 31 74 86 o por email en javier@coolpadelstudios.com.")

        ]

    }

]



def render_landing(landing, lang="es"):
    is_camaras = landing["slug"].startswith("camaras-") or landing["slug"] in ["camaras-grabacion-pistas-padel", "save-my-play"]

    # Localized data lookup
    if lang != "es":
        trans = LANDINGS_I18N.get(lang, {}).get(landing["slug"], {})
    else:
        trans = {}

    ui = COMMON_UI.get(lang, COMMON_UI["es"])

    # Overridden fields
    l_title = trans.get("title", landing["title"])
    l_meta_desc = trans.get("meta_desc", landing["meta_desc"])
    l_badge = trans.get("badge", landing["badge"])
    l_leaf = trans.get("breadcrumb_leaf", landing["breadcrumb_leaf"])
    l_h1 = trans.get("h1", landing["h1"])
    l_subtitle = trans.get("subtitle", landing["subtitle"])
    l_hero_alt = trans.get("hero_img_alt", landing["hero_img_alt"])
    l_wa_msg = trans.get("wa_msg", landing["wa_msg"])
    l_price_anchor = trans.get("price_anchor", landing["price_anchor"])
    l_target = trans.get("target_audience", landing["target_audience"])
    l_quick = trans.get("quick_summary", landing.get("quick_summary", {}))
    l_benefits = trans.get("benefits", landing["benefits"])
    l_faqs = trans.get("faqs", landing["faqs"])

    wa_encoded = urllib.parse.quote(l_wa_msg)
    hero_img_encoded = urllib.parse.quote(landing["hero_img"])

    # Path & asset prefixes
    path_prefix = "" if lang == "es" else f"{lang}/"
    asset_prefix = "../" if lang == "es" else "../../"
    page_url = f"https://coolpadelstudios.com/{path_prefix}{landing['slug']}/"
    og_locale = {"es": "es_ES", "en": "en_US", "fr": "fr_FR", "it": "it_IT"}.get(lang, "es_ES")
    home_url = "/" if lang == "es" else f"/{lang}/"
    camaras_url = "/camaras/" if lang == "es" else f"/{lang}/camaras/"
    blog_url = "/blog/" if lang == "es" else f"/{lang}/blog/"
    franquicias_url = "/franquicias-padel/" if lang == "es" else f"/{lang}/franquicias-padel/"
    llaveros_url = "/llaveros-padel-personalizados/" if lang == "es" else f"/{lang}/llaveros-padel-personalizados/"
    contacto_url = "#contacto" if lang == "es" else f"/{lang}/#contacto" 

    # FAQ Schema
    faq_schema_items = []
    for q, a in l_faqs:
        q_clean = q.replace('"', '\"')
        a_clean = a.replace('"', '\"')
        faq_schema_items.append(f"""
          {{
            "@type": "Question",
            "name": "{q_clean}",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{a_clean}"
            }}
          }}""")
    faq_schema_json = ",".join(faq_schema_items)

    # Benefits HTML
    benefits_html = ""
    for title, desc in l_benefits:
        benefits_html += f"""
        <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200/90 shadow-sm hover:shadow-md transition">
          <div class="text-[#f2920b] flex items-center justify-start mb-4 font-black text-2xl">
            ✓
          </div>
          <h3 class="font-heading font-black text-xl sm:text-2xl text-slate-950 mb-2">{title}</h3>
          <p class="text-slate-600 text-sm sm:text-base leading-relaxed">{desc}</p>
        </div>"""

    # Breadcrumb names
    parent_names = {
        "es": ("Cámaras de Pádel", "https://coolpadelstudios.com/save-my-play/", "Merchandising Pádel", "https://coolpadelstudios.com/#llaveros"),
        "en": ("Padel Court Cameras", "https://coolpadelstudios.com/en/save-my-play/", "Padel Merchandising", "https://coolpadelstudios.com/en/#llaveros"),
        "fr": ("Caméras Terrains Padel", "https://coolpadelstudios.com/fr/save-my-play/", "Merchandising Padel", "https://coolpadelstudios.com/fr/#llaveros"),
        "it": ("Telecamere Campi Padel", "https://coolpadelstudios.com/it/save-my-play/", "Merchandising Padel", "https://coolpadelstudios.com/it/#llaveros")
    }
    p_cam, p_cam_url, p_merch, p_merch_url = parent_names.get(lang, parent_names["es"])
    parent_breadcrumb_name = p_cam if is_camaras else p_merch
    parent_breadcrumb_url = p_cam_url if is_camaras else p_merch_url
    parent_breadcrumb_rel_url = f"{asset_prefix}save-my-play/" if is_camaras else f"{asset_prefix}#llaveros"
    leaf_breadcrumb_name = l_leaf

    # Quick summary items
    quick_label_1 = l_quick.get("label_1", "Tarifa B2B" if lang=="es" else "B2B Rate")
    quick_val_1 = l_quick.get("val_1", l_price_anchor)
    quick_label_2 = l_quick.get("label_2", "Pedido Mínimo" if lang=="es" else "Minimum Order")
    quick_val_2 = l_quick.get("val_2", "100 unidades" if lang=="es" else "100 units")
    quick_label_3 = l_quick.get("label_3", "Muestra Física" if lang=="es" else "Physical Sample")
    quick_val_3 = l_quick.get("val_3", "15 € con logo real" if lang=="es" else "€15 with real logo")
    quick_label_4 = l_quick.get("label_4", "Plazo Entrega" if lang=="es" else "Delivery Time")
    quick_val_4 = l_quick.get("val_4", "~1 mes con envíos" if lang=="es" else "~1 month shipping incl.")
    quick_p = l_quick.get("p", l_subtitle)

    # Section headers and buttons from UI
    why_title = ui["why_camaras"] if is_camaras else ui["why_llaveros"]
    why_sub = ui["why_camaras_sub"] if is_camaras else ui["why_llaveros_sub"]
    precios_title = ui["precios_camaras"] if is_camaras else ui["precios_llaveros"]
    precios_sub = ui["precios_camaras_sub"] if is_camaras else ui["precios_llaveros_sub"]
    faq_sub = ui["faq_camaras_sub"] if is_camaras else ui["faq_llaveros_sub"]
    cta_sub = ui["cta_camaras_sub"] if is_camaras else ui["cta_llaveros_sub"]
    footer_tagline = ui["footer_camaras"] if is_camaras else ui["footer_llaveros"]
    cta_btn_text = ui["btn_demo_wa"] if is_camaras else ui["btn_calc_wa"]

    if is_camaras:
        badge_badges = {
            "es": ('0 obras · Montaje 5 min', '0 permanencia', 'Descarga instantánea QR'),
            "en": ('0 construction works · 5 min setup', '0 lock-in contract', 'Instant mobile QR download'),
            "fr": ('0 travaux · Pose en 5 min', '0 engagement de durée', 'Téléchargement QR instantané'),
            "it": ('0 opere murarie · Montaggio 5 min', '0 vincoli contrattuali', 'Download istantaneo con QR')
        }.get(lang, ('0 obras', '0 permanencia', 'QR'))

        hero_badges_html = f"""
              <span class="flex items-center gap-1.5"><i data-lucide="check-circle" class="w-4 h-4 text-[#f2920b]"></i> {badge_badges[0]}</span>
              <span class="flex items-center gap-1.5"><i data-lucide="check-circle" class="w-4 h-4 text-[#f2920b]"></i> {badge_badges[1]}</span>
              <span class="flex items-center gap-1.5"><i data-lucide="check-circle" class="w-4 h-4 text-[#f2920b]"></i> {badge_badges[2]}</span>"""

        tbl_hdrs = {
            "es": ("Concepto / Plan", "Inversión / Cuota", "Modalidad", "Servicios Incluidos", "* Precios sin IVA. Sin permanencia ni penalizaciones. Instalación en 5 min.", "Contactar / Solicitar Presupuesto"),
            "en": ("Concept / Plan", "Investment / Fee", "Terms", "Included Services", "* Prices without VAT. Zero lock-in contracts or penalties. 5-min installation.", "Contact / Request Quote"),
            "fr": ("Concept / Formule", "Investissement / Tarif", "Modalité", "Services Inclus", "* Tarifs hors taxes. Sans engagement de durée ni pénalités. Pose en 5 min.", "Contacter / Demander un devis"),
            "it": ("Concetto / Piano", "Investimento / Canone", "Modalità", "Servizi Inclusi", "* Prezzi IVA esclusa. Nessun vincolo o penale. Montaggio in 5 min.", "Contatta / Richiedi preventivo")
        }.get(lang, ("Concepto", "Precio", "Modalidad", "Servicios", "", "Contactar"))

        table_html = f"""
          <div class="overflow-x-auto">
            <table class="w-full text-left text-sm sm:text-base">
              <thead>
                <tr class="border-b border-slate-200 text-xs uppercase tracking-wider text-slate-500">
                  <th class="py-3 px-3">{tbl_hdrs[0]}</th>
                  <th class="py-3 px-3">{tbl_hdrs[1]}</th>
                  <th class="py-3 px-3">{tbl_hdrs[2]}</th>
                  <th class="py-3 px-3">{tbl_hdrs[3]}</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100 font-bold">
                <tr>
                  <td class="py-4 px-3 text-slate-900">{"Inversión Hardware en Propiedad" if lang=="es" else "Owned Hardware Investment" if lang=="en" else "Investissement Matériel Possédé" if lang=="fr" else "Investimento Hardware di Proprietà"}</td>
                  <td class="py-4 px-3 text-[#f2920b]">180 € / {"pista" if lang in ["es","fr"] else "court" if lang=="en" else "campo"}</td>
                  <td class="py-4 px-3 text-slate-700">{"Pago único (+20€ envío int.)" if lang=="es" else "One-time payment (+€20 int. shipping)" if lang=="en" else "Paiement unique (+20€ port int.)" if lang=="fr" else "Pagamento unico (+20€ sped. int.)"}</td>
                  <td class="py-4 px-3 text-slate-600 text-xs font-medium">{"1 cámara rectilínea por pista (sin efecto pez) + fijación a poste + pulsador físico en red" if lang=="es" else "1 rectilinear camera per court (no fish-eye) + post mount + smart net push button" if lang=="en" else "1 caméra rectilinéaire par terrain (sans fisheye) + fixation poteau + bouton filet" if lang=="fr" else "1 telecamera rettilinea per campo (no fish-eye) + attacco a palo + tasto a rete"}</td>
                </tr>
                <tr>
                  <td class="py-4 px-3 text-slate-900">{"Software Highlights & Streaming (< 5 pistas)" if lang=="es" else "Software Highlights & Streaming (< 5 courts)" if lang=="en" else "Logiciel Highlights & Streaming (< 5 pistes)" if lang=="fr" else "Software Highlights & Streaming (< 5 campi)"}</td>
                  <td class="py-4 px-3 text-[#f2920b]">45 € / {"mes / pista" if lang=="es" else "month / court" if lang=="en" else "mois / piste" if lang=="fr" else "mese / campo"}</td>
                  <td class="py-4 px-3 text-emerald-600">{"0 permanencia · Cancelación libre" if lang=="es" else "0 lock-in · Free cancellation" if lang=="en" else "0 engagement · Résiliation libre" if lang=="fr" else "0 vincoli · Disdetta libera"}</td>
                  <td class="py-4 px-3 text-slate-600 text-xs font-medium">{"Grabación de partidos, repeticiones botón en red, clips en 25s, streaming YouTube y descarga QR" if lang=="es" else "Match recording, net button replays, 25s clips, YouTube streaming and instant QR download" if lang=="en" else "Enregistrement de matches, replays bouton filet, clips 25s, streaming YouTube et téléchargement QR" if lang=="fr" else "Registrazione partite, replay tasto a rete, clip in 25s, streaming YouTube e download QR"}</td>
                </tr>
                <tr>
                  <td class="py-4 px-3 text-slate-900">{"Software Highlights & Streaming (5 a 14 pistas)" if lang=="es" else "Software Highlights & Streaming (5 to 14 courts)" if lang=="en" else "Logiciel Highlights & Streaming (5 à 14 pistes)" if lang=="fr" else "Software Highlights & Streaming (da 5 a 14 campi)"}</td>
                  <td class="py-4 px-3 text-[#f2920b]">41 € / {"mes / pista" if lang=="es" else "month / court" if lang=="en" else "mois / piste" if lang=="fr" else "mese / campo"}</td>
                  <td class="py-4 px-3 text-emerald-600">{"0 permanencia · Descuento volumen" if lang=="es" else "0 lock-in · Volume discount" if lang=="en" else "0 engagement · Remise de volume" if lang=="fr" else "0 vincoli · Sconto volume"}</td>
                  <td class="py-4 px-3 text-slate-600 text-xs font-medium">{"Tarifa optimizada para clubes medianos con ahorro directo en cada pista" if lang=="es" else "Optimized rate for medium clubs with direct savings per court" if lang=="en" else "Tarif optimisé pour clubs moyens avec économie directe par piste" if lang=="fr" else "Tariffa ottimizzata per circoli medi con risparmio diretto per campo"}</td>
                </tr>
                <tr>
                  <td class="py-4 px-3 text-slate-900">{"Software Highlights & Streaming (15 a 24 pistas)" if lang=="es" else "Software Highlights & Streaming (15 to 24 courts)" if lang=="en" else "Logiciel Highlights & Streaming (15 à 24 pistes)" if lang=="fr" else "Software Highlights & Streaming (da 15 a 24 campi)"}</td>
                  <td class="py-4 px-3 text-[#f2920b]">36 € / {"mes / pista" if lang=="es" else "month / court" if lang=="en" else "mois / piste" if lang=="fr" else "mese / campo"}</td>
                  <td class="py-4 px-3 text-emerald-600">{"0 permanencia · Descuento volumen" if lang=="es" else "0 lock-in · Volume discount" if lang=="en" else "0 engagement · Remise de volume" if lang=="fr" else "0 vincoli · Sconto volume"}</td>
                  <td class="py-4 px-3 text-slate-600 text-xs font-medium">{"Tarifa club grande: mayor margen por pista para complejos y academias" if lang=="es" else "Large club rate: higher margin per court for academies and large complexes" if lang=="en" else "Tarif grand club: marge supérieure par piste pour complexes et académies" if lang=="fr" else "Tariffa grandi circoli: maggiore margine per campo per complessi e scuole"}</td>
                </tr>
                <tr>
                  <td class="py-4 px-3 text-slate-900">{"Software Highlights & Streaming (> 25 pistas)" if lang=="es" else "Software Highlights & Streaming (> 25 courts)" if lang=="en" else "Logiciel Highlights & Streaming (> 25 pistes)" if lang=="fr" else "Software Highlights & Streaming (> 25 campi)"}</td>
                  <td class="py-4 px-3 text-[#f2920b]">27 € / {"mes / pista" if lang=="es" else "month / court" if lang=="en" else "mois / piste" if lang=="fr" else "mese / campo"}</td>
                  <td class="py-4 px-3 text-emerald-600">{"0 permanencia · Tarifa Franquicia" if lang=="es" else "0 lock-in · Franchise rate" if lang=="en" else "0 engagement · Tarif Franchise" if lang=="fr" else "0 vincoli · Tariffa Franchigia"}</td>
                  <td class="py-4 px-3 text-slate-600 text-xs font-medium">{"Tarifa especial para cadenas, federaciones y franquicias (+1.500 cámaras activas)" if lang=="es" else "Special rate for chains, federations, and franchises (+1,500 active cameras)" if lang=="en" else "Tarif spécial chaînes, fédérations et franchises (+1 500 caméras actives)" if lang=="fr" else "Tariffa speciale per catene, federazioni e franchigie (+1.500 telecamere attive)"}</td>
                </tr>
                <tr class="bg-amber-50/50">
                  <td class="py-4 px-3 text-slate-900">{"Módulo Extra: Analítica IA & Coaching Tools" if lang=="es" else "Optional Add-on: AI Analytics & Coaching Tools" if lang=="en" else "Module Optionnel: Analyse IA & Outils Coaching" if lang=="fr" else "Modulo Opzionale: Analitica IA & Strumenti Coaching"}</td>
                  <td class="py-4 px-3 text-[#f2920b]">136 € / {"mes / pista" if lang=="es" else "month / court" if lang=="en" else "mois / piste" if lang=="fr" else "mese / campo"}</td>
                  <td class="py-4 px-3 text-slate-700">{"Opcional todo incluido" if lang=="es" else "Optional all-inclusive" if lang=="en" else "Option tout inclus" if lang=="fr" else "Opzionale tutto incluso"}</td>
                  <td class="py-4 px-3 text-slate-600 text-xs font-medium">{"Todo el plan básico + estadísticas tácticas, mapas de calor, velocidad de bola y slow-motion" if lang=="es" else "All basic features + tactical stats, heat maps, ball speed, and slow-motion replays" if lang=="en" else "Tout le plan de base + statistiques tactiques, cartes de chaleur, vitesse de balle et ralenti" if lang=="fr" else "Tutto il piano base + statistiche tattiche, mappe di calore, velocità palla e slow-motion"}</td>
                </tr>
              </tbody>
            </table>
          </div>
          
          <div class="mt-6 pt-5 border-t border-slate-100 flex flex-col sm:flex-row items-center justify-between gap-4">
            <span class="text-xs text-slate-500">{tbl_hdrs[4]}</span>
            <a href="#contacto" class="px-6 py-3 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition">
              {tbl_hdrs[5]}
            </a>
          </div>"""

        step_titles = {
            "es": ("Demo Online (15 min)", "Te mostramos en vivo cómo funciona la cámara, el pulsador y la descarga QR.", "Instalación en 5 min", "Se fija directamente al poste de la pista sin obras y sin zanjas.", "Activación y Sin Permanencia", "Tus jugadores disfrutan de sus mejores jugadas con cancelación libre."),
            "en": ("Online Demo (15 min)", "Live screen-share demo of the camera feed, net button, and instant QR downloads.", "5-Min Installation", "Clamps directly onto the court post without civil works, trenching, or court closures.", "Activation & Zero Lock-in", "Players enjoy highlights immediately with complete month-to-month freedom."),
            "fr": ("Démo en Ligne (15 min)", "Démonstration en direct de la caméra, du bouton au filet et du téléchargement QR.", "Pose en 5 min", "Fixation directe sur le poteau du terrain sans tranchée ni interruption d'activité.", "Activation Sans Engagement", "Vos joueurs profitent de leurs meilleurs coups avec résiliation libre."),
            "it": ("Demo Online (15 min)", "Ti mostriamo dal vivo la telecamera, il tasto a rete e il download con QR code.", "Montaggio in 5 min", "Si fissa direttamente al palo del campo senza scavi né interruzione delle partite.", "Attivazione Senza Vincoli", "I giocatori scaricano le loro giocate con totale libertà di disdetta.")
        }.get(lang, ("Demo", "", "Instalación", "", "Activación", ""))

        pasos_html = f"""
        <div class="grid sm:grid-cols-3 gap-6 text-center">
          <div class="space-y-2">
            <div class="w-10 h-10 rounded-full bg-white/20 text-white font-heading font-black text-base flex items-center justify-center mx-auto">1</div>
            <h3 class="font-heading font-black text-lg">{step_titles[0]}</h3>
            <p class="text-white/80 text-xs">{step_titles[1]}</p>
          </div>
          <div class="space-y-2">
            <div class="w-10 h-10 rounded-full bg-white/20 text-white font-heading font-black text-base flex items-center justify-center mx-auto">2</div>
            <h3 class="font-heading font-black text-lg">{step_titles[2]}</h3>
            <p class="text-white/80 text-xs">{step_titles[3]}</p>
          </div>
          <div class="space-y-2">
            <div class="w-10 h-10 rounded-full bg-white/20 text-white font-heading font-black text-base flex items-center justify-center mx-auto">3</div>
            <h3 class="font-heading font-black text-lg">{step_titles[4]}</h3>
            <p class="text-white/80 text-xs">{step_titles[5]}</p>
          </div>
        </div>"""

        vid_headers = {
            "es": ("Demostración en Pista Real", "Comprueba la Calidad de Grabación y Streaming", "Partidos oficiales FIP en directo, repeticiones automáticas con pulsador y herramientas de análisis táctico.", "Ver en YouTube"),
            "en": ("Real Court Demonstration", "Experience Recording and Streaming Quality", "Official FIP live broadcasts, automated net button replays, and tactical coaching analysis tools.", "Watch on YouTube"),
            "fr": ("Démonstration sur Piste Réelle", "Vérifiez la Qualité d'Enregistrement et de Streaming", "Matches officiels FIP en direct, replays automatiques au filet et outils d'analyse tactique.", "Voir sur YouTube"),
            "it": ("Dimostrazione su Campo Reale", "Verifica la Qualità di Registrazione e Streaming", "Partite ufficiali FIP in diretta, replay automatici con tasto a rete e strumenti tattici.", "Guarda su YouTube")
        }.get(lang, ("Demo", "Calidad", "Partidos", "YouTube"))

        videos_html = f"""
    <!-- DEMOSTRACIÓN EN VÍDEO Y REPETICIONES REALES -->
    <section class="py-14 sm:py-20 bg-slate-50 border-b border-slate-200">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center max-w-2xl mx-auto mb-10 sm:mb-14 space-y-2">
          <span class="inline-block text-[#f2920b] font-heading font-black text-xs uppercase tracking-wider">
            {vid_headers[0]}
          </span>
          <h2 class="font-heading font-black text-2xl sm:text-4xl text-slate-950 uppercase tracking-tight">
            {vid_headers[1]}
          </h2>
          <p class="text-sm sm:text-base text-slate-600 font-medium">
            {vid_headers[2]}
          </p>
        </div>

        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-xs hover:shadow-md transition flex flex-col">
            <div class="aspect-video bg-slate-900 relative">
              <iframe class="w-full h-full" src="https://www.youtube-nocookie.com/embed/4xwrrveDZxg?start=5623" title="FIP Miami Live Streaming Save My Play" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
            </div>
            <div class="p-4 flex-1 flex flex-col justify-between">
              <div>
                <span class="text-[10px] font-heading font-black uppercase text-[#d97706] tracking-wider">Streaming Live</span>
                <h3 class="font-heading font-bold text-sm text-slate-900 mt-1">FIP Miami YouTube Live</h3>
                <p class="text-xs text-slate-600 mt-1">{"Retransmisión en directo en 1080p sin cortes con imagen rectilínea." if lang=="es" else "Live 1080p broadcast with crisp rectilinear court view." if lang=="en" else "Diffusion 1080p en direct sans déformation fisheye." if lang=="fr" else "Diretta streaming 1080p nitida senza distorsioni ottiche."}</p>
              </div>
              <a href="https://www.youtube.com/live/4xwrrveDZxg?si=Tw56yNEB9KWwlkbr&t=5623" target="_blank" rel="noopener" class="mt-3 inline-flex items-center gap-1 text-xs font-bold text-[#f2920b] hover:underline">
                <span>{vid_headers[3]}</span>
                <i data-lucide="external-link" class="w-3 h-3"></i>
              </a>
            </div>
          </div>

          <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-xs hover:shadow-md transition flex flex-col">
            <div class="aspect-video bg-slate-900 relative">
              <iframe class="w-full h-full" src="https://www.youtube-nocookie.com/embed/LuzDvB5Umfs" title="Demo Save My Play" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
            </div>
            <div class="p-4 flex-1 flex flex-col justify-between">
              <div>
                <span class="text-[10px] font-heading font-black uppercase text-emerald-600 tracking-wider">{"Jugador" if lang=="es" else "Player Experience" if lang=="en" else "Expérience Joueur" if lang=="fr" else "Esperienza Giocatore"}</span>
                <h3 class="font-heading font-bold text-sm text-slate-900 mt-1">{"Cómo se Juega y Descarga" if lang=="es" else "How to Play & Download" if lang=="en" else "Comment Jouer & Télécharger" if lang=="fr" else "Come Giocare e Scaricare"}</h3>
                <p class="text-xs text-slate-600 mt-1">{"Pulsador en red y escaneo QR inmediato sin descargar apps." if lang=="es" else "Net button tap and instant QR scan without downloading apps." if lang=="en" else "Pression bouton au filet et scan QR immédiat sans application." if lang=="fr" else "Pulsante a rete e scansione QR istantanea senza app."}</p>
              </div>
              <a href="https://www.youtube.com/watch?v=LuzDvB5Umfs" target="_blank" rel="noopener" class="mt-3 inline-flex items-center gap-1 text-xs font-bold text-[#f2920b] hover:underline">
                <span>{vid_headers[3]}</span>
                <i data-lucide="external-link" class="w-3 h-3"></i>
              </a>
            </div>
          </div>

          <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-xs hover:shadow-md transition flex flex-col">
            <div class="aspect-video bg-slate-900 relative">
              <iframe class="w-full h-full" src="https://www.youtube-nocookie.com/embed/Z0vnvyrUbPQ" title="Highlights Save My Play" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
            </div>
            <div class="p-4 flex-1 flex flex-col justify-between">
              <div>
                <span class="text-[10px] font-heading font-black uppercase text-sky-600 tracking-wider">{"Clip Automático" if lang=="es" else "Automatic Clip" if lang=="en" else "Clip Automatique" if lang=="fr" else "Clip Automatica"}</span>
                <h3 class="font-heading font-bold text-sm text-slate-900 mt-1">{"Highlights de 25 Segundos" if lang=="es" else "25-Second Highlights" if lang=="en" else "Highlights de 25 Secondes" if lang=="fr" else "Highlights di 25 Secondi"}</h3>
                <p class="text-xs text-slate-600 mt-1">{"Calidad Full HD lista para Instagram, TikTok o WhatsApp." if lang=="es" else "Full HD quality ready to share on Instagram, TikTok, or WhatsApp." if lang=="en" else "Qualité Full HD prête à partager sur Instagram, TikTok ou WhatsApp." if lang=="fr" else "Qualità Full HD pronta da condividere su Instagram, TikTok o WhatsApp."}</p>
              </div>
              <a href="https://youtu.be/Z0vnvyrUbPQ" target="_blank" rel="noopener" class="mt-3 inline-flex items-center gap-1 text-xs font-bold text-[#f2920b] hover:underline">
                <span>{vid_headers[3]}</span>
                <i data-lucide="external-link" class="w-3 h-3"></i>
              </a>
            </div>
          </div>

          <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-xs hover:shadow-md transition flex flex-col">
            <div class="aspect-video bg-slate-900 relative">
              <iframe class="w-full h-full" src="https://www.youtube-nocookie.com/embed/FcnCWaYahP8" title="Coaching tools Save My Play" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
            </div>
            <div class="p-4 flex-1 flex flex-col justify-between">
              <div>
                <span class="text-[10px] font-heading font-black uppercase text-purple-600 tracking-wider">{"Coaching" if lang=="en" else "Monitores" if lang=="es" else "Entraîneurs" if lang=="fr" else "Maestri"}</span>
                <h3 class="font-heading font-bold text-sm text-slate-900 mt-1">{"Coaching Tools & Táctica" if lang=="es" else "Coaching Tools & Tactics" if lang=="en" else "Outils Coaching & Tactique" if lang=="fr" else "Strumenti Coaching & Tattica"}</h3>
                <p class="text-xs text-slate-600 mt-1">{"Repetición instantánea para corrección técnica en clases." if lang=="es" else "Instant replay for technical correction in coaching sessions." if lang=="en" else "Ralenti instantané pour correction technique pendant les cours." if lang=="fr" else "Replay istantaneo per correzioni tecniche durante le lezioni."}</p>
              </div>
              <a href="https://www.youtube.com/watch?v=FcnCWaYahP8" target="_blank" rel="noopener" class="mt-3 inline-flex items-center gap-1 text-xs font-bold text-[#f2920b] hover:underline">
                <span>{vid_headers[3]}</span>
                <i data-lucide="external-link" class="w-3 h-3"></i>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>
"""
    else:
        videos_html = ""
        badge_badges = {
            "es": ('Muestra 15€ (~15 días lab.)', 'Pedido mín. 100 uds', 'Entrega pedido ~1 mes'),
            "en": ('€15 sample (~15 business days)', 'Min. order 100 pcs', 'Bulk delivery ~1 month'),
            "fr": ('Échantillon 15€ (~15 j. ouvrés)', 'Commande min. 100 pcs', 'Livraison série ~1 mois'),
            "it": ('Campione 15€ (~15 gg lavorativi)', 'Ordine min. 100 pz', 'Consegna lotto ~1 mese')
        }.get(lang, ('Muestra 15€', '100 uds', '~1 mes'))

        hero_badges_html = f"""
              <span class="flex items-center gap-1.5"><i data-lucide="check-circle" class="w-4 h-4 text-[#f2920b]"></i> {badge_badges[0]}</span>
              <span class="flex items-center gap-1.5"><i data-lucide="check-circle" class="w-4 h-4 text-[#f2920b]"></i> {badge_badges[1]}</span>
              <span class="flex items-center gap-1.5"><i data-lucide="check-circle" class="w-4 h-4 text-[#f2920b]"></i> {badge_badges[2]}</span>"""

        tbl_hdrs = {
            "es": ("Tirada", "Precio Unitario", "Total Estimado", "Muestra Física Previa", "* Precios sin IVA. Muestra física en ~15 días laborables y entrega en ~1 mes.", "Contactar / Solicitar Presupuesto"),
            "en": ("Batch Tier", "Unit Price", "Estimated Total", "Pre-Production Sample", "* Prices without VAT. Real sample in ~15 business days, serial delivery in ~1 month.", "Contact / Request Quote"),
            "fr": ("Palier de volume", "Prix unitaire", "Montant estimé", "Échantillon physique", "* Tarifs hors taxes. Échantillon réel sous ~15 jours ouvrés, série en ~1 mois.", "Contacter / Demander un devis"),
            "it": ("Lotto", "Prezzo unitario", "Totale stimato", "Campione fisico", "* Prezzi IVA esclusa. Campione reale in ~15 giorni lavorativi, fornitura in ~1 mese.", "Contatta / Richiedi preventivo")
        }.get(lang, ("Tirada", "Precio", "Total", "Muestra", "", "Contactar"))

        table_html = f"""
          <div class="overflow-x-auto">
            <table class="w-full text-left text-sm sm:text-base">
              <thead>
                <tr class="border-b border-slate-200 text-xs uppercase tracking-wider text-slate-500">
                  <th class="py-3 px-3">{tbl_hdrs[0]}</th>
                  <th class="py-3 px-3">{tbl_hdrs[1]}</th>
                  <th class="py-3 px-3">{tbl_hdrs[2]}</th>
                  <th class="py-3 px-3">{tbl_hdrs[3]}</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100 font-bold">
                <tr>
                  <td class="py-4 px-3 text-slate-900">{"100 unidades (Mínimo)" if lang=="es" else "100 units (Minimum)" if lang=="en" else "100 unités (Minimum)" if lang=="fr" else "100 unità (Minimo)"}</td>
                  <td class="py-4 px-3 text-[#f2920b]">3,00 € / {"ud" if lang in ["es","fr"] else "unit" if lang=="en" else "pz"}</td>
                  <td class="py-4 px-3 text-slate-700">300 € (+{"IVA" if lang in ["es","it"] else "VAT" if lang=="en" else "TVA"})</td>
                  <td class="py-4 px-3 text-slate-500 text-xs">{"15 € (100% deducible)" if lang in ["es","fr","it"] else "€15 (100% deductible)"}</td>
                </tr>
                <tr>
                  <td class="py-4 px-3 text-slate-900">250 {"unidades" if lang=="es" else "units" if lang=="en" else "unités" if lang=="fr" else "unità"}</td>
                  <td class="py-4 px-3 text-[#f2920b]">2,50 € / {"ud" if lang in ["es","fr"] else "unit" if lang=="en" else "pz"}</td>
                  <td class="py-4 px-3 text-slate-700">625 € (+{"IVA" if lang in ["es","it"] else "VAT" if lang=="en" else "TVA"})</td>
                  <td class="py-4 px-3 text-slate-500 text-xs">{"Muestra física deducible · Entrega ~1 mes" if lang=="es" else "Deductible sample · Delivery ~1 month" if lang=="en" else "Échantillon déductible · Délai ~1 mois" if lang=="fr" else "Campione deducibile · Consegna ~1 mese"}</td>
                </tr>
                <tr>
                  <td class="py-4 px-3 text-slate-900">500 {"unidades" if lang=="es" else "units" if lang=="en" else "unités" if lang=="fr" else "unità"}</td>
                  <td class="py-4 px-3 text-[#f2920b]">2,00 € / {"ud" if lang in ["es","fr"] else "unit" if lang=="en" else "pz"}</td>
                  <td class="py-4 px-3 text-slate-700">1.000 € (+{"IVA" if lang in ["es","it"] else "VAT" if lang=="en" else "TVA"})</td>
                  <td class="py-4 px-3 text-slate-500 text-xs">{"Muestra deducible y envíos incluidos" if lang=="es" else "Deductible sample & shipping included" if lang=="en" else "Échantillon déductible et port inclus" if lang=="fr" else "Campione deducibile e spedizione inclusa"}</td>
                </tr>
                <tr>
                  <td class="py-4 px-3 text-slate-900">1.500 {"unidades" if lang=="es" else "units" if lang=="en" else "unités" if lang=="fr" else "unità"}</td>
                  <td class="py-4 px-3 text-[#f2920b]">1,50 € / {"ud" if lang in ["es","fr"] else "unit" if lang=="en" else "pz"}</td>
                  <td class="py-4 px-3 text-slate-700">2.250 € (+{"IVA" if lang in ["es","it"] else "VAT" if lang=="en" else "TVA"})</td>
                  <td class="py-4 px-3 text-slate-500 text-xs">{"Tarifa directa de fábrica gran volumen" if lang=="es" else "Direct factory wholesale bulk rate" if lang=="en" else "Tarif direct usine grand volume" if lang=="fr" else "Tariffa diretta di fabbrica grande volume"}</td>
                </tr>
              </tbody>
            </table>
          </div>
          
          <div class="mt-6 pt-5 border-t border-slate-100 flex flex-col sm:flex-row items-center justify-between gap-4">
            <span class="text-xs text-slate-500">{tbl_hdrs[4]}</span>
            <a href="#contacto" class="px-6 py-3 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition">
              {tbl_hdrs[5]}
            </a>
          </div>"""

        step_titles = {
            "es": ("Envías tu Logotipo", "Preparamos el diseño digital 3D sin coste para validar proporciones y colores.", "Muestra Física (15€)", "Fabricamos y enviamos una muestra real en ~15 días laborables (100% deducible).", "Producción y Entrega", "Fabricación en serie desde 100 uds y entrega en torno a un mes."),
            "en": ("Send Your Logo", "We prepare your 3D digital mockup free of charge to validate colors and proportions.", "Physical Sample (€15)", "We manufacture and ship an actual sample in ~15 business days (100% deductible).", "Production & Delivery", "Serial production from 100 units and delivery in ~1 month."),
            "fr": ("Envoi du Logo", "Maquette 3D numérique offerte pour valider proportions et couleurs.", "Échantillon Physique (15€)", "Fabrication et expédition d'un échantillon réel en ~15 jours ouvrés (100% remboursable).", "Production et Livraison", "Production série dès 100 unités et livraison en environ un mois."),
            "it": ("Invia il Tuo Logo", "Bozza digitale 3D gratuita per confermare proporzioni e tinte.", "Campione Fisico (15€)", "Produzione e spedizione di un campione reale in ~15 giorni lavorativi (100% deducibile).", "Produzione e Consegna", "Produzione in serie da 100 pezzi con consegna in circa un mese.")
        }.get(lang, ("Logo", "", "Muestra", "", "Entrega", ""))

        pasos_html = f"""
        <div class="grid sm:grid-cols-3 gap-6 text-center">
          <div class="space-y-2">
            <div class="w-10 h-10 rounded-full bg-white/20 text-white font-heading font-black text-base flex items-center justify-center mx-auto">1</div>
            <h3 class="font-heading font-black text-lg">{step_titles[0]}</h3>
            <p class="text-white/80 text-xs">{step_titles[1]}</p>
          </div>
          <div class="space-y-2">
            <div class="w-10 h-10 rounded-full bg-white/20 text-white font-heading font-black text-base flex items-center justify-center mx-auto">2</div>
            <h3 class="font-heading font-black text-lg">{step_titles[2]}</h3>
            <p class="text-white/80 text-xs">{step_titles[3]}</p>
          </div>
          <div class="space-y-2">
            <div class="w-10 h-10 rounded-full bg-white/20 text-white font-heading font-black text-base flex items-center justify-center mx-auto">3</div>
            <h3 class="font-heading font-black text-lg">{step_titles[4]}</h3>
            <p class="text-white/80 text-xs">{step_titles[5]}</p>
          </div>
        </div>"""

    # Dynamic Product / Service Schema
    if is_camaras:
        product_schema_json = f"""{{
        "@type": ["Product", "Service"],
        "name": "{l_h1} - Save My Play",
        "description": "{l_meta_desc}",
        "image": [
          "https://coolpadelstudios.com/{hero_img_encoded}",
          "https://coolpadelstudios.com/assets/images/savemyplay-1.jpg",
          "https://coolpadelstudios.com/assets/images/savemyplay-2.jpg"
        ],
        "sku": "SMP-COURT-CAM-2026",
        "brand": {{
          "@type": "Brand",
          "name": "Save my Play",
          "url": "https://savemyplay.com",
          "sameAs": "https://savemyplay.com"
        }},
        "offers": [
          {{
            "@type": "Offer",
            "name": "Inversión Hardware en Propiedad",
            "priceCurrency": "EUR",
            "price": "180.00",
            "priceValidUntil": "2027-12-31",
            "availability": "https://schema.org/InStock"
          }},
          {{
            "@type": "Offer",
            "name": "Highlights & Streaming (< 5 courts)",
            "priceCurrency": "EUR",
            "price": "45.00",
            "priceValidUntil": "2027-12-31",
            "availability": "https://schema.org/InStock"
          }}
        ]
      }}"""
    else:
        product_schema_json = f"""{{
        "@type": "Product",
        "name": "{l_h1} - CoolPadel",
        "description": "{l_meta_desc}",
        "image": "https://coolpadelstudios.com/{hero_img_encoded}",
        "sku": "CP-{landing['slug'].upper()[:18]}",
        "brand": {{
          "@type": "Brand",
          "name": "CoolPadel"
        }},
        "offers": [
          {{
            "@type": "Offer",
            "name": "100 units batch",
            "priceCurrency": "EUR",
            "price": "3.00",
            "priceValidUntil": "2027-12-31",
            "availability": "https://schema.org/MadeToOrder"
          }},
          {{
            "@type": "Offer",
            "name": "500 units batch",
            "priceCurrency": "EUR",
            "price": "2.00",
            "priceValidUntil": "2027-12-31",
            "availability": "https://schema.org/MadeToOrder"
          }}
        ]
      }}"""

    # FAQ HTML (Desplegable y compacto)
    faq_html = ""
    for q, a in l_faqs:
        faq_html += f"""
        <details class="group bg-white rounded-2xl p-4 sm:p-5 border border-slate-200/90 shadow-2xs transition hover:border-[#f2920b]">
          <summary class="flex items-center justify-between font-heading font-black text-sm sm:text-base text-slate-950 cursor-pointer list-none select-none">
            <span>{q}</span>
            <span class="w-6 h-6 rounded-full bg-slate-100 text-slate-700 group-open:rotate-180 group-open:bg-[#f2920b] group-open:text-slate-950 flex items-center justify-center transition-transform text-xs shrink-0 ml-3">▼</span>
          </summary>
          <p class="mt-3 text-slate-600 text-xs sm:text-sm leading-relaxed border-t border-slate-100 pt-3">{a}</p>
        </details>"""

    # Language Switcher dropdown (matching home page)
    lang_opts = []
    for l_code, l_label in [("es", "ES"), ("en", "EN"), ("fr", "FR"), ("it", "IT")]:
        target_url = f"/{landing['slug']}/" if l_code == "es" else f"/{l_code}/{landing['slug']}/"
        active_cls = "lang-opt-active bg-[#f2920b] text-slate-950 font-black" if l_code == lang else "text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold"
        lang_opts.append(f'<a href="{target_url}" class="lang-opt block {active_cls} w-full text-center px-4 py-2 text-xs transition duration-150">{l_label}</a>')
    lang_switcher_html = f'''
        <div class="relative inline-block text-left" id="lang-dropdown-container">
          <button type="button" onclick="toggleLangDropdown(event)" id="lang-dropdown-btn" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 border border-slate-200 text-xs font-black text-slate-900 shadow-xs transition cursor-pointer" aria-expanded="false" aria-haspopup="true">
            <span id="current-lang-code" class="uppercase font-black">{lang.upper()}</span>
            <i data-lucide="chevron-down" class="w-3.5 h-3.5 stroke-[2.5] text-slate-600 transition-transform duration-200" id="lang-dropdown-arrow"></i>
          </button>
          <div id="lang-dropdown-menu" class="hidden absolute right-0 mt-2 w-24 bg-white rounded-2xl shadow-[0_12px_30px_rgba(0,0,0,0.15)] border border-slate-200 py-1.5 z-50 transition-all overflow-hidden">
            {"".join(lang_opts)}
          </div>
        </div>'''

    html = f"""<!DOCTYPE html>
<html lang="{lang}" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>{l_title}</title>
  <meta name="description" content="{l_meta_desc}">
  <meta name="author" content="CoolPadel">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <link rel="canonical" href="{page_url}">

  <!-- SEO Multilingüe Hreflang -->
  <link rel="alternate" hreflang="es" href="https://coolpadelstudios.com/{landing['slug']}/">
  <link rel="alternate" hreflang="en" href="https://coolpadelstudios.com/en/{landing['slug']}/">
  <link rel="alternate" hreflang="fr" href="https://coolpadelstudios.com/fr/{landing['slug']}/">
  <link rel="alternate" hreflang="it" href="https://coolpadelstudios.com/it/{landing['slug']}/">
  <link rel="alternate" hreflang="x-default" href="https://coolpadelstudios.com/{landing['slug']}/">
  <meta name="language" content="{lang}">

  <link rel="icon" type="image/png" href="{asset_prefix}assets/images/favicon_transparente.png?v=transp3">
  <link rel="apple-touch-icon" sizes="180x180" href="{asset_prefix}assets/images/favicon_transparente.png?v=transp3">
  <meta name="theme-color" content="#0b1626">

  <!-- Resource Hints & Core Web Vitals -->
  <link rel="dns-prefetch" href="https://fonts.googleapis.com">
  <link rel="dns-prefetch" href="https://fonts.gstatic.com">
  <link rel="dns-prefetch" href="https://cdn.tailwindcss.com">
  <link rel="dns-prefetch" href="https://unpkg.com">
  <link rel="dns-prefetch" href="https://www.clarity.ms">

  <!-- LLM & AI Discovery -->
  <link rel="alternate" type="text/markdown" href="https://coolpadelstudios.com/llms.txt" title="LLMs.txt">
  <link rel="alternate" type="text/markdown" href="https://coolpadelstudios.com/llms-full.txt" title="LLMs-Full.txt">

  <!-- GEO Tags -->
  <meta name="geo.region" content="ES-MD">
  <meta name="geo.placename" content="Madrid">
  <meta name="geo.position" content="40.4168;-3.7038">
  <meta name="ICBM" content="40.4168, -3.7038">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:locale" content="{og_locale}">
  <meta property="og:site_name" content="CoolPadel">
  <meta property="og:url" content="{page_url}">
  <meta property="og:title" content="{l_title}">
  <meta property="og:description" content="{l_meta_desc}">
  <meta property="og:image" content="https://coolpadelstudios.com/{hero_img_encoded}">
  <meta property="og:image:secure_url" content="https://coolpadelstudios.com/{hero_img_encoded}">
  <meta property="og:image:width" content="1000">
  <meta property="og:image:height" content="1000">
  <meta property="og:image:type" content="image/jpeg">
  <meta property="og:image:alt" content="{l_hero_alt}">
  <link rel="image_src" href="https://coolpadelstudios.com/{hero_img_encoded}">

  <!-- Twitter Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{l_title}">
  <meta name="twitter:description" content="{l_meta_desc}">
  <meta name="twitter:image" content="https://coolpadelstudios.com/{hero_img_encoded}">
  <meta name="twitter:image:alt" content="{l_hero_alt}">

  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "ImageObject",
        "@id": "{page_url}#primaryimage",
        "url": "https://coolpadelstudios.com/{hero_img_encoded}",
        "contentUrl": "https://coolpadelstudios.com/{hero_img_encoded}",
        "width": 1000,
        "height": 1000,
        "caption": "{l_hero_alt}",
        "representativeOfPage": true,
        "creator": {{
          "@type": "Organization",
          "name": "CoolPadel"
        }},
        "copyrightNotice": "© CoolPadel",
        "creditText": "CoolPadel Studios",
        "license": "https://coolpadelstudios.com/politica-de-devoluciones.html",
        "acquireLicensePage": "{page_url}"
      }},
      {{
        "@type": "Organization",
        "@id": "https://coolpadelstudios.com/#organization",
        "name": "CoolPadel",
        "alternateName": "CoolPadel",
        "url": "https://coolpadelstudios.com",
        "logo": "https://coolpadelstudios.com/assets/images/coolpadel-mascot-hd.png"
      }},
      {{
        "@type": "BreadcrumbList",
        "@id": "{page_url}#breadcrumb",
        "itemListElement": [
          {{
            "@type": "ListItem",
            "position": 1,
            "name": "{ui['nav_home']}",
            "item": "https://coolpadelstudios.com/{path_prefix}"
          }},
          {{
            "@type": "ListItem",
            "position": 2,
            "name": "{parent_breadcrumb_name}",
            "item": "{parent_breadcrumb_url}"
          }},
          {{
            "@type": "ListItem",
            "position": 3,
            "name": "{leaf_breadcrumb_name}",
            "item": "{page_url}"
          }}
        ]
      }},
      {product_schema_json},
      {{
        "@type": "FAQPage",
        "@id": "{page_url}#faq",
        "mainEntity": [
          {faq_schema_json}
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
      background-image: linear-gradient(rgba(52, 120, 166, 0.40), rgba(52, 120, 166, 0.40)), url('{asset_prefix}assets/images/branding/textura_editorial_coolpadel.webp');
      background-blend-mode: normal, soft-light;
      background-size: cover;
      background-position: center;
    }}
  </style>
</head>
<body class="bg-[#f8fafc] text-slate-800 antialiased selection:bg-[#f2920b] selection:text-slate-950 min-h-screen flex flex-col">

  <!-- HEADER OFICIAL -->
  <header class="fixed top-0 left-0 w-full z-50 bg-white/95 backdrop-blur-md border-b border-slate-200/80 shadow-xs">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 sm:h-20 flex items-center justify-between">
      <a href="{home_url}" class="flex items-center gap-2 group">
        <img src="{asset_prefix}assets/images/coolpadel-mascot-hd.png" alt="Mascota CoolPadel" width="44" height="44" class="h-8 sm:h-11 w-auto object-contain">
        <img src="{asset_prefix}assets/images/coolpadel-typography-hd.png" alt="CoolPadel" width="140" height="28" class="h-5 sm:h-7 w-auto object-contain">
      </a>
      
      <div class="flex items-center gap-2 sm:gap-4 lg:gap-6">
        <a href="{llaveros_url}" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition">{ui['nav_llaveros']}</a>
        <a href="{camaras_url}" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">{"CAMERAS" if lang=="en" else "CAMÉRAS" if lang=="fr" else "TELECAMERE" if lang=="it" else "CÁMARAS"}</a>
        <a href="{blog_url}" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition">{ui['nav_blog']}</a>
        <a href="{franquicias_url}" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition">{"Franchises" if lang=="en" else "Franchises" if lang=="fr" else "Franchigie" if lang=="it" else "Cadenas de clubs"}</a>
        
        {lang_switcher_html}

        <a href="{contacto_url}" class="inline-flex items-center gap-1.5 px-3.5 sm:px-4 py-1.5 sm:py-2 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition shadow-sm hover:scale-105 active:scale-95">
          <span>{ui['nav_contacto']}</span>
          <i data-lucide="arrow-down" class="w-3 h-3 stroke-[3]"></i>
        </a>

        <!-- OJOS DEL LOGO A LA DERECHA DEL TODO -->
        <a href="{home_url}" class="group py-1 inline-flex items-center shrink-0 pl-1" aria-label="CoolPadel Eyes">
          <img src="{asset_prefix}assets/images/eyes-thumb.png?v=fixed_eyes" alt="CoolPadel Eyes" width="28" height="28" style="height: 26px; max-height: 26px; width: auto;" class="object-contain group-hover:scale-110 transition duration-300">
        </a>
      </div>
    </div>
  </header>
  <div class="h-16 sm:h-20 w-full shrink-0" aria-hidden="true"></div>


  <!-- HERO SECTION -->
  <main class="flex-1">
    <section class="py-12 sm:py-20 bg-gradient-to-b from-white via-slate-50 to-[#f8fafc] border-b border-slate-200">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <!-- Breadcrumbs Navigation -->
        <nav aria-label="Ruta de navegación" class="flex items-center gap-2 text-xs font-bold text-slate-500 mb-6 uppercase tracking-wider">
          <a href="{asset_prefix}" class="hover:text-slate-900 transition">{ui['nav_home']}</a>
          <span>/</span>
          <a href="{parent_breadcrumb_rel_url}" class="hover:text-slate-900 transition">{parent_breadcrumb_name}</a>
          <span>/</span>
          <span class="text-[#f2920b]">{leaf_breadcrumb_name}</span>
        </nav>

        <div class="grid lg:grid-cols-12 gap-8 sm:gap-12 items-center">
          
          <div class="lg:col-span-7 space-y-6">
            <div class="inline-flex items-center gap-2 text-[#f2920b] font-heading font-black text-xs uppercase tracking-wider">
              <i data-lucide="award" class="w-4 h-4"></i>
              <span>{l_badge}</span>
            </div>

            <h1 class="font-heading font-black text-3xl sm:text-5xl lg:text-6xl text-slate-950 uppercase tracking-tight leading-[1.08]">
              {l_h1}
            </h1>

            <p class="text-base sm:text-lg text-slate-600 leading-relaxed font-normal">
              {l_subtitle}
            </p>

            <div class="flex flex-wrap items-center gap-3 pt-2 text-xs sm:text-sm font-bold text-slate-700">
              {hero_badges_html}
            </div>

            <div class="pt-4 flex flex-col sm:flex-row items-stretch sm:items-center gap-3 sm:gap-4">
              <a href="https://api.whatsapp.com/send?phone=34680317486&text={wa_encoded}" target="_blank" rel="noopener" class="inline-flex items-center justify-center gap-2.5 px-7 py-4 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-sm uppercase tracking-wider transition shadow-md hover:scale-105 active:scale-95 group">
                <i data-lucide="message-circle" class="w-5 h-5 text-slate-950"></i>
                <span>{cta_btn_text}</span>
              </a>

              <a href="#precios" class="inline-flex items-center justify-center gap-2 px-6 py-4 rounded-full bg-white hover:bg-slate-100 text-slate-900 border border-slate-200 font-heading font-black text-sm uppercase tracking-wider transition">
                <span>{"Ver Tarifas y Muestra" if lang=="es" else "View Rates & Samples" if lang=="en" else "Voir Tarifs & Échantillons" if lang=="fr" else "Vedi Tariffe e Campioni"}</span>
                <i data-lucide="arrow-down" class="w-4 h-4 text-slate-500"></i>
              </a>
            </div>

            <p class="text-xs text-slate-500 italic">
              <strong>{"Ideal para:" if lang=="es" else "Ideal for:" if lang=="en" else "Idéal pour:" if lang=="fr" else "Ideale per:"}</strong> {l_target}
            </p>
          </div>

          <div class="lg:col-span-5">
            <div class="relative mx-auto max-w-md lg:max-w-none">
              <div class="absolute -inset-1 bg-gradient-to-r from-[#f2920b] to-[#76d3f6] rounded-3xl blur-xl opacity-30"></div>
              <div class="relative bg-white p-3 sm:p-4 rounded-3xl border border-slate-200/90 shadow-xl overflow-hidden group">
                <img src="{asset_prefix}{landing['hero_img']}" alt="{l_hero_alt}" width="800" height="800" class="w-full h-auto rounded-2xl object-cover group-hover:scale-105 transition duration-500" loading="eager" decoding="async">
                
                <div class="mt-4 p-4 rounded-2xl bg-slate-50 border border-slate-200/80">
                  <div class="grid grid-cols-2 gap-3 text-left">
                    <div>
                      <span class="text-[10px] font-heading font-black uppercase text-slate-400 tracking-wider block">{quick_label_1}</span>
                      <span class="text-xs sm:text-sm font-bold text-slate-900">{quick_val_1}</span>
                    </div>
                    <div>
                      <span class="text-[10px] font-heading font-black uppercase text-slate-400 tracking-wider block">{quick_label_2}</span>
                      <span class="text-xs sm:text-sm font-bold text-slate-900">{quick_val_2}</span>
                    </div>
                    <div>
                      <span class="text-[10px] font-heading font-black uppercase text-slate-400 tracking-wider block">{quick_label_3}</span>
                      <span class="text-xs sm:text-sm font-bold text-[#f2920b]">{quick_val_3}</span>
                    </div>
                    <div>
                      <span class="text-[10px] font-heading font-black uppercase text-slate-400 tracking-wider block">{quick_label_4}</span>
                      <span class="text-xs sm:text-sm font-bold text-emerald-700">{quick_val_4}</span>
                    </div>
                  </div>
                  <p class="mt-3 text-xs text-slate-500 border-t border-slate-200/60 pt-2 font-medium">
                    {quick_p}
                  </p>
                </div>
              </div>
            </div>
          </div>

        </div>

      </div>
    </section>

    <!-- VENTAJAS / DIFERENCIALES -->
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

    {videos_html}

    <!-- TABLA DE PRECIOS O CALCULADORA INTERACTIVA -->
    <section id="precios" class="py-14 sm:py-20 bg-slate-50 border-b border-slate-200 scroll-mt-20">
      <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
        {table_html if is_camaras else get_llaveros_calculator_html(lang, asset_prefix)}
      </div>
    </section>

{"" if is_camaras else f'''
    <!-- CÓMO FUNCIONA / PROCESO (FORMATO TEXTURA) -->
    <section class="py-14 sm:py-20 bg-[#3478a6] bg-textured-blue text-white border-b border-sky-700/40">
      <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center max-w-2xl mx-auto mb-10 space-y-2">
          <span class="inline-block px-3.5 py-1 rounded-full bg-white/20 text-white font-heading font-black text-xs uppercase tracking-wider">
            {"Paso a Paso" if lang=="es" else "Step by Step" if lang=="en" else "Étape par Étape" if lang=="fr" else "Passo dopo Passo"}
          </span>
          <h2 class="font-heading font-black text-2xl sm:text-4xl uppercase tracking-tight">
            {"¿Cómo pedir para tu club?" if lang=="es" else "How to order for your club?"}
          </h2>
        </div>

        <!-- 3 PASOS CON TEXTURA Y TARJETAS BLANCAS DESTACADAS -->
        <div class="grid sm:grid-cols-3 gap-6 text-left">
          <div class="bg-white/95 rounded-2xl p-6 text-slate-900 shadow-md border border-white/40 space-y-2.5">
            <div class="w-9 h-9 rounded-full bg-[#f2920b] text-slate-950 font-heading font-black text-sm flex items-center justify-center">1</div>
            <h3 class="font-heading font-black text-lg text-slate-950">Envíanos tu logo</h3>
            <p class="text-slate-600 text-xs sm:text-sm leading-relaxed">Envíanos el logo de tu club en cualquier formato y preparamos tu diseño digital 3D gratuito.</p>
          </div>

          <div class="bg-white/95 rounded-2xl p-6 text-slate-900 shadow-md border border-white/40 space-y-2.5">
            <div class="w-9 h-9 rounded-full bg-[#f2920b] text-slate-950 font-heading font-black text-sm flex items-center justify-center">2</div>
            <h3 class="font-heading font-black text-lg text-slate-950">Diseño 3D y Muestra Física Previa 15€</h3>
            <p class="text-slate-600 text-xs sm:text-sm leading-relaxed">Fabricamos una muestra real con tu logo antes de confirmar la tirada completa. 15 € reembolsables al confirmar el pedido.</p>
          </div>

          <div class="bg-white/95 rounded-2xl p-6 text-slate-900 shadow-md border border-white/40 space-y-2.5">
            <div class="w-9 h-9 rounded-full bg-[#f2920b] text-slate-950 font-heading font-black text-sm flex items-center justify-center">3</div>
            <h3 class="font-heading font-black text-lg text-slate-950">Producción y Entrega</h3>
            <p class="text-slate-600 text-xs sm:text-sm leading-relaxed">Pedido mínimo 100 unidades y entrega en torno a un mes con envíos incluidos.</p>
          </div>
        </div>
      </div>
    </section>
'''}

    <!-- PREGUNTAS FRECUENTES -->
    <section class="py-14 sm:py-20 bg-white border-b border-slate-200">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center max-w-2xl mx-auto mb-10 space-y-2">
          <h2 class="font-heading font-black text-2xl sm:text-4xl text-slate-950 uppercase tracking-tight">
            {"Preguntas Frecuentes" if lang=="es" else "Frequently Asked Questions" if lang=="en" else "Questions Fréquentes" if lang=="fr" else "Domande Frequenti"}
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

        <!-- 6. SECCIÓN CONTACTO OFICIAL COOLPADEL (IDÉNTICA A LA HOME) -->
    <section id="contacto" class="py-10 sm:py-14 bg-slate-50 relative border-t border-slate-200 text-slate-900 overflow-hidden">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 relative z-10 text-center">
        
        <div class="max-w-2xl mx-auto text-center mb-6">
          <span class="inline-block text-[#f2920b] text-xs font-bold uppercase tracking-wider mb-2">
            Contacto Directo
          </span>
          <h2 class="text-2xl sm:text-4xl font-black font-heading text-slate-950 uppercase tracking-tight leading-tight">
            {"Contáctanos" if lang=="es" else "Contact Us" if lang=="en" else "Contactez-nous" if lang=="fr" else "Contattaci"}
          </h2>
          <p class="text-slate-600 text-xs sm:text-sm mt-2">
            {"Respuesta directa para consultas de clubes, torneos y muestras físicas." if lang=="es" else "Direct answer for clubs, tournaments inquiries and physical samples." if lang=="en" else "Réponse directe pour les clubs, tournois et échantillons physiques." if lang=="fr" else "Risposta diretta per club, tornei e campioni fisici."}
          </p>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 sm:gap-6 max-w-2xl mx-auto text-left">
          <!-- WhatsApp Card -->
          <a id="landing-contact-wa" href="https://api.whatsapp.com/send?phone=34680317486&text={wa_encoded}" target="_blank" rel="noopener noreferrer"
             class="bg-white border border-slate-200 hover:border-[#25D366] rounded-2xl p-5 shadow-xs hover:shadow-lg transition-all duration-300 flex flex-col justify-between items-center text-center group cursor-pointer block no-underline text-inherit">
            <div class="flex flex-col items-center space-y-2 w-full">
              <div class="w-11 h-11 rounded-xl bg-emerald-50 text-[#25D366] flex items-center justify-center shadow-inner group-hover:scale-105 group-hover:bg-[#25D366] group-hover:text-white transition-all duration-300">
                <i data-lucide="message-circle" class="w-6 h-6 stroke-[2.2]"></i>
              </div>
              <h3 class="font-heading font-black text-base sm:text-lg text-slate-950">WhatsApp Directo</h3>
              <p class="font-mono font-bold text-xs sm:text-sm text-emerald-600 tracking-wide">+34 680 31 74 86</p>
              <div class="pt-1">
                <div class="p-1.5 bg-white border border-slate-200 rounded-xl shadow-2xs inline-block group-hover:border-emerald-300 transition">
                  <img src="{asset_prefix}assets/images/qr_whatsapp_coolpadel.png" alt="WhatsApp CoolPadel" width="80" height="80" class="w-16 h-16 sm:w-20 sm:h-20 object-contain" loading="lazy">
                </div>
              </div>
            </div>
            <div class="w-full pt-3 border-t border-slate-100 mt-3">
              <div class="w-full inline-flex items-center justify-center px-4 py-2 sm:py-2.5 rounded-full bg-[#25D366] group-hover:bg-[#20ba59] text-white font-sans font-black text-xs uppercase tracking-wider shadow-sm transition">
                <span>{"Chatear por WhatsApp" if lang=="es" else "Chat on WhatsApp"}</span>
              </div>
            </div>
          </a>

          <!-- Email Card -->
          <a id="landing-contact-mail" href="mailto:javier@coolpadelstudios.com?subject=Consulta%20CoolPadel%20/%20Save%20my%20Play"
             class="bg-white border border-slate-200 hover:border-[#3478a6] rounded-2xl p-5 shadow-xs hover:shadow-lg transition-all duration-300 flex flex-col justify-between items-center text-center group cursor-pointer block no-underline text-inherit">
            <div class="flex flex-col items-center space-y-2 w-full">
              <div class="w-11 h-11 rounded-xl bg-sky-50 text-[#3478a6] flex items-center justify-center shadow-inner group-hover:scale-105 group-hover:bg-[#3478a6] group-hover:text-white transition-all duration-300">
                <i data-lucide="mail" class="w-6 h-6 stroke-[2.2]"></i>
              </div>
              <h3 class="font-heading font-black text-base sm:text-lg text-slate-950">Correo Electrónico</h3>
              <p class="font-sans font-bold text-xs sm:text-sm text-sky-800 tracking-normal break-all">javier@coolpadelstudios.com</p>
              <div class="pt-1">
                <div class="p-1.5 bg-white border border-slate-200 rounded-xl shadow-2xs inline-block group-hover:border-sky-300 transition">
                  <img src="{asset_prefix}assets/images/qr_email_coolpadel.png" alt="Email CoolPadel" width="80" height="80" class="w-16 h-16 sm:w-20 sm:h-20 object-contain" loading="lazy">
                </div>
              </div>
            </div>
            <div class="w-full pt-3 border-t border-slate-100 mt-3">
              <div class="w-full inline-flex items-center justify-center px-4 py-2 sm:py-2.5 rounded-full bg-[#3478a6] group-hover:bg-[#2c668d] text-white font-sans font-black text-xs uppercase tracking-wider shadow-sm transition">
                <span>{"Enviar Email" if lang=="es" else "Send Email"}</span>
              </div>
            </div>
          </a>
        </div>

      </div>
    </section>
  </main>

  <!-- FOOTER OFICIAL (FORMATO EXACTO HOME) -->
  <footer class="relative z-20 bg-[#3478a6] bg-textured-blue text-white pt-14 pb-10 border-t border-sky-700/40 text-xs">
    <div class="max-w-[1700px] mx-auto px-4 sm:px-8 space-y-10">
      <div class="flex flex-col sm:flex-row items-center justify-between gap-4 pb-8 border-b border-white/20">
        <div class="flex items-center gap-3.5">
          <img src="{asset_prefix}assets/images/coolpadel-mascot-hd.png" alt="CoolPadel Mascota" width="60" height="60" class="h-10 sm:h-12 w-auto object-contain drop-shadow-sm" loading="lazy">
          <img src="{asset_prefix}assets/images/coolpadel-typography-hd.png" alt="CoolPadel" width="160" height="32" class="h-5 sm:h-6 w-auto object-contain drop-shadow-sm" loading="lazy">
        </div>
      </div>

      <nav aria-label="Estructura y Silos SEO de CoolPadel" class="grid grid-cols-2 lg:grid-cols-4 gap-8 text-left">
        <div class="space-y-3">
          <div class="font-heading font-black text-sm uppercase tracking-wider text-white">Soluciones B2B</div>
          <ul class="space-y-2 text-white/80 font-normal">
            <li><a href="/llaveros-padel-personalizados/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Llaveros de Pádel 3D</a></li>
            <li><a href="/llaveros-tenis-personalizados/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Llaveros de Tenis</a></li>
            <li><a href="/welcome-packs-torneos-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Welcome Packs para Torneos</a></li>
            <li><a href="/save-my-play/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Cámaras Save my Play</a></li>
          </ul>
        </div>
        <div class="space-y-3">
          <div class="font-heading font-black text-sm uppercase tracking-wider text-white">Herramientas</div>
          <ul class="space-y-2 text-white/80 font-normal">
            <li><a href="/herramientas/generador-americana-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Generador de Americana</a></li>
            <li><a href="/herramientas/generador-cuadros-torneo-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Sorteo de Cuadros</a></li>
            <li><a href="/herramientas/calculadora-coste-pistas-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Calculadora Coste Pistas</a></li>
            <li><a href="/herramientas/calculadora-roi-camaras-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Calculadora ROI Cámaras</a></li>
          </ul>
        </div>
        <div class="space-y-3">
          <div class="font-heading font-black text-sm uppercase tracking-wider text-white">Ecosistema</div>
          <ul class="space-y-2 text-white/80 font-normal">
            <li><a href="/franquicias-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Cadenas de Clubs</a></li>
            <li><a href="/blog/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Blog & Newsletter</a></li>
            <li><a href="/blog/highlights-03/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Highlights #03</a></li>
          </ul>
        </div>
        <div class="space-y-3">
          <div class="font-heading font-black text-sm uppercase tracking-wider text-white">Legal & Contacto</div>
          <p class="text-white/80">Javier Villoria Soleto<br>España<br>WhatsApp: +34 680 31 74 86</p>
        </div>
      </nav>
      <div class="border-t border-white/20 pt-6 text-center text-white/60">
        <p>© 2026 CoolPadel. Todos los derechos reservados.</p>
      </div>
    </div>
  </footer>

  <script>
    if (typeof lucide !== 'undefined') {{
      lucide.createIcons();
    }}
  </script>
  <script src="/assets/js/cp-analytics.js" defer></script>
</body>
</html>
"""
    return html


def build_all_landings():
    print(">> Generando Landings B2B Transaccionales en 4 Idiomas (ES, EN, FR, IT)...")
    for lang in ["es", "en", "fr", "it"]:
        for l in LANDINGS:
            slug = l["slug"]
            if lang == "es":
                out_dir = f"coolpadel-web/{slug}"
            else:
                out_dir = f"coolpadel-web/{lang}/{slug}"
            os.makedirs(out_dir, exist_ok=True)
            html_content = render_landing(l, lang=lang)
            with open(f"{out_dir}/index.html", "w", encoding="utf-8") as f:
                f.write(html_content)
        print(f"  [OK] Generadas 11 landings para {lang.upper()}")


if __name__ == "__main__":

    build_all_landings()

