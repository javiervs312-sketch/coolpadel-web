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
        "title": "Llaveros de Pádel Personalizados en Goma 3D para Clubs | CoolPadel Studios",
        "meta_desc": "Fabricante directo de llaveros de pádel personalizados de goma 3D con relieve y logo oficial para clubs, escuelas y torneos. Pedidos desde 100 uds y muestra previa por 15€.",
        "badge": "FABRICACIÓN DIRECTA B2B",
        "h1": "Llaveros de Pádel Personalizados en Relieve 3D",
        "subtitle": "Fabricamos los llaveros oficiales de tu club o torneo en microinyección de PVC blando 3D con tus colores Pantone y relieve exacto. El detalle que tus jugadores llevan siempre en el paletero.",
        "hero_img": "assets/images/llaveros 1.jpg",
        "hero_img_alt": "Llaveros de pádel personalizados de goma 3D con logo oficial para clubes",
        "wa_msg": "Hola Javier, quiero información y presupuesto para llaveros de pádel personalizados para mi club",
        "price_anchor": "Desde 1,50 € / ud · Pedido mínimo 100 uds",
        "target_audience": "Clubes de pádel, federaciones, organizadores de torneos y escuelas deportivas que buscan merchandising de alta calidad con el escudo de su club.",
        "benefits": [
            ("Relieve 3D Microinyectado", "Goma PVC flexible de alta densidad, resistente a caídas, agua y rozaduras dentro del paletero."),
            ("Muestra Física Previa 15€", "Fabricamos una muestra real con tu logo antes de confirmar la tirada completa. Reembolsable 100% con el pedido."),
            ("Tarifa Directa de Fábrica", "Desde 1,50€ a 3,00€ por unidad con envíos incluidos a España, Europa y Estados Unidos.")
        ],
        "faqs": [
            ("¿Cuál es el pedido mínimo y los plazos de entrega?", "El pedido mínimo de producción es de 100 unidades. El plazo de fabricación y entrega estándar es de 7 a 10 días laborables tras la aprobación de la muestra física."),
            ("¿Cómo solicitamos la muestra física de 15€?", "Solo tienes que enviarnos el logo de tu club en cualquier formato (vectorial, PNG, JPG). Preparamos el diseño 3D y fabricamos una muestra real enviada a tu dirección por 15€."),
            ("¿Se puede personalizar el reverso del llavero?", "Sí, podemos añadir el logo de un patrocinador, la página web del club o las redes sociales en el reverso.")
        ]
    },
    {
        "slug": "llaveros-tenis-personalizados",
        "title": "Llaveros de Tenis Personalizados para Clubs y Academias | CoolPadel Studios",
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
            ("Sin Gastos Ocultos", "Diseño digital sin coste, muestra previa enviada por 15€ y envíos incluidos en el pedido final.")
        ],
        "faqs": [
            ("¿Fabricáis llaveros tanto de tenis como de pádel?", "Sí. Muchos de nuestros clubes clientes son entidades polideportivas (tenis + pádel) y fabricamos los modelos para ambas secciones o torneos mixtos."),
            ("¿Qué formatos de logotipo aceptáis?", "Aceptamos cualquier formato (AI, PDF, SVG, PNG, JPG). Nuestro equipo adapta el diseño al molde 3D para tu validación."),
            ("¿Sirven para vender en la tienda del club?", "Totalmente. Muchos clubes los comercializan en recepción o pro-shop a 5€-6€, generando un margen del 50-70% para el club.")
        ]
    },
    {
        "slug": "welcome-packs-torneos-padel",
        "title": "Welcome Packs y Regalos para Torneos de Pádel | CoolPadel Studios",
        "meta_desc": "Regalos originales para welcome packs de torneos de pádel. Llaveros de goma 3D personalizados con el logo del torneo y patrocinadores. Tiradas desde 100 uds con entrega rápida.",
        "badge": "TORNEOS, CIRCUITOS & WELCOME PACKS",
        "h1": "Welcome Packs y Regalos Oficiales para Torneos de Pádel",
        "subtitle": "Olvídate de las camisetas o toallas que acaban olvidadas en un cajón. Un llavero 3D personalizado con el logo del torneo y del patrocinador es el recuerdo que los participantes lucen todo el año en su paletero.",
        "hero_img": "assets/images/slide-1.jpg",
        "hero_img_alt": "Welcome packs y llaveros 3D para torneos de pádel oficiales",
        "wa_msg": "Hola Javier, estoy organizando un torneo de pádel y busco regalos/welcome packs para los jugadores",
        "price_anchor": "Especial torneos: 100 a 1.500+ uds · Tarifa directa de fábrica",
        "target_audience": "Directores de torneos, organizadores de circuitos de pádel, patrocinadores y empresas que buscan un regalo publicitario de alto valor percibido.",
        "benefits": [
            ("Máxima Visibilidad para Patrocinadores", "Posibilidad de personalizar anverso con el torneo y reverso con la marca o patrocinador principal."),
            ("Alto Valor Percibido y Bajo Coste", "Desde 1,50€ por jugador, ofreciendo un regalo que se percibe como producto premium de tienda oficial."),
            ("Plazos Rápidos para tu Fecha de Torneo", "Entrega garantizada antes del fin de semana de competición tras aprobar la muestra física.")
        ],
        "faqs": [
            ("¿Con cuánta antelación debo encargar los llaveros para el torneo?", "Recomendamos solicitar la muestra entre 3 y 4 semanas antes del torneo para poder enviarte la muestra física y producir la tirada con tranquilidad."),
            ("¿Qué cantidades se suelen pedir para torneos?", "Dependiendo de los cuadros de juego, los torneos suelen solicitar entre 100 y 250 unidades para torneos locales de fin de semana, o 500 a 1.500 unidades para circuitos y másters."),
            ("¿Emitís factura oficial para la organización o patrocinador?", "Sí, emitimos factura oficial desglosada con IVA deducible para clubes, empresas organizadoras o patrocinadores del torneo.")
        ]
    },
    {
        "slug": "llaveros-personalizados-clubs-padel",
        "title": "Llaveros Personalizados para Clubs de Pádel | CoolPadel Studios",
        "meta_desc": "Llaveros oficiales personalizados para clubes de pádel. Merchandising B2B de goma 3D para socios, bienvenida a escuelas y venta en pro-shop. Más de 26 clubes en Europa.",
        "badge": "MERCHANDISING OFICIAL DE CLUB",
        "h1": "Llaveros Oficiales para Clubs de Pádel y Socios",
        "subtitle": "Refuerza la identidad y el sentido de pertenencia de tu comunidad. Más de 26 clubes en España, Italia, Francia y Bélgica ya equipan a sus socios con llaveros CoolPadel Studios.",
        "hero_img": "assets/images/llaveros 1.jpg",
        "hero_img_alt": "Llaveros oficiales personalizados para clubes de pádel y escuelas",
        "wa_msg": "Hola Javier, soy responsable de un club de pádel y quiero información para hacer los llaveros de nuestros socios",
        "price_anchor": "Tarifa club desde 1,50 € / ud · Muestra previa 15 €",
        "target_audience": "Gerentes de clubes, directores deportivos, comités de socios y responsables de pro-shop que desean merchandising oficial rentable y atractivo.",
        "benefits": [
            ("Fidelización de Socios y Alumnos", "El regalo perfecto para la cuota anual, bienvenida a la escuela de menores o cenas de fin de temporada."),
            ("Margen de Venta en Recepción", "Con un coste de fabricación de 1,50€-3,00€ y un PVP recomendado de 5€-6€, el club rentabiliza la inversión en pocas semanas."),
            ("Experiencia Demostrada en +26 Clubs", "Trabajamos con clubes referentes en España y Europa con acabados profesionales y soporte personalizado.")
        ],
        "faqs": [
            ("¿Cómo gestionamos el pedido para nuestro club?", "Contactas directamente con Javier por WhatsApp o correo. Nos mandas el escudo del club, te presentamos el render digital 3D y fabricamos la muestra física para que la toques en persona."),
            ("¿Podemos repetir pedidos en el futuro con el mismo molde?", "Sí. Guardamos tu molde de producción para que puedas pedir reposiciones de 100 en 100 unidades cuando lo necesites sin coste adicional de diseño."),
            ("¿Cuáles son las formas de pago para clubes?", "Transferencia bancaria oficial contra factura proforma tras validar la muestra física.")
        ]
    },
    {
        "slug": "camaras-grabacion-pistas-padel",
        "title": "Cámaras y Grabación de Partidos para Pistas de Pádel | Save My Play",
        "meta_desc": "Sistema de grabación inteligente y repetición en vídeo para pistas de pádel. Instalación en 5 minutos sin obras ni zanjas, pulsador físico en poste y entrega vía WhatsApp.",
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
    }
]

def render_landing(landing):
    wa_encoded = urllib.parse.quote(landing["wa_msg"])
    
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
  <meta property="og:image" content="https://coolpadelstudios.com/{landing['hero_img']}">

  <!-- Twitter Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{landing['title']}">
  <meta name="twitter:description" content="{landing['meta_desc']}">
  <meta name="twitter:image" content="https://coolpadelstudios.com/{landing['hero_img']}">

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
        "logo": "https://coolpadelstudios.com/assets/images/coolpadel-mascot-hd.png"
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
      {{
        "@type": "Product",
        "name": "{landing['h1']} - CoolPadel Studios",
        "description": "{landing['meta_desc']}",
        "image": "https://coolpadelstudios.com/{landing['hero_img']}",
        "brand": {{
          "@type": "Brand",
          "name": "CoolPadel Studios"
        }},
        "offers": [
          {{
            "@type": "Offer",
            "name": "Tirada oficial para clubes (desde 100 unidades)",
            "priceCurrency": "EUR",
            "price": "3.00",
            "priceValidUntil": "2027-12-31",
            "availability": "https://schema.org/MadeToOrder"
          }},
          {{
            "@type": "Offer",
            "name": "Muestra física previa con logo real",
            "priceCurrency": "EUR",
            "price": "15.00",
            "priceValidUntil": "2027-12-31",
            "availability": "https://schema.org/InStock"
          }}
        ]
      }},
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
  </style>
</head>
<body class="bg-[#f8fafc] text-slate-800 antialiased selection:bg-[#f2920b] selection:text-slate-950 min-h-screen flex flex-col">

  <!-- HEADER OFICIAL -->
  <header class="sticky top-0 z-50 bg-white/95 backdrop-blur-md border-b border-slate-200/80 shadow-xs">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 sm:h-20 flex items-center justify-between">
      <a href="../" class="flex items-center gap-2 group">
        <img src="../assets/images/coolpadel-mascot-hd.png" alt="Mascota CoolPadel Studios" class="h-8 sm:h-11 w-auto object-contain">
        <img src="../assets/images/coolpadel-typography-hd.png" alt="CoolPadel Studios" class="h-5 sm:h-7 w-auto object-contain">
      </a>
      
      <div class="flex items-center gap-3 sm:gap-6">
        <a href="../#llaveros" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition">Llaveros</a>
        <a href="../blog/" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition">Blog</a>
        
        <a href="https://wa.me/34680317486?text={wa_encoded}" target="_blank" class="inline-flex items-center gap-2 px-4 sm:px-5 py-2 sm:py-2.5 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs sm:text-sm tracking-wider uppercase transition shadow-sm hover:scale-105 active:scale-95">
          <span>Pedir Presupuesto</span>
          <i data-lucide="arrow-up-right" class="w-3.5 h-3.5 stroke-[3]"></i>
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
          <span class="text-[#f2920b]">Llaveros Personalizados</span>
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
              <a href="https://wa.me/34680317486?text={wa_encoded}" target="_blank" class="inline-flex items-center justify-center gap-2.5 px-7 py-4 rounded-2xl bg-[#25D366] hover:bg-[#20ba59] text-white font-heading font-black text-base uppercase tracking-wider shadow-lg hover:scale-105 active:scale-95 transition">
                <i data-lucide="message-circle" class="w-5 h-5"></i>
                <span>Solicitar Muestra / Cotización</span>
              </a>
              <a href="#precios" class="inline-flex items-center justify-center gap-2 px-6 py-4 rounded-2xl bg-white hover:bg-slate-100 border border-slate-300 text-slate-900 font-heading font-bold text-base transition">
                <span>Ver Tarifas</span>
                <i data-lucide="arrow-down" class="w-4 h-4"></i>
              </a>
            </div>

            <div class="pt-3 flex items-center gap-4 text-xs font-bold text-slate-500">
              <span class="flex items-center gap-1.5"><i data-lucide="check-circle" class="w-4 h-4 text-[#f2920b]"></i> Muestra 15€ con envío</span>
              <span class="flex items-center gap-1.5"><i data-lucide="check-circle" class="w-4 h-4 text-[#f2920b]"></i> Pedido mín. 100 uds</span>
              <span class="flex items-center gap-1.5"><i data-lucide="check-circle" class="w-4 h-4 text-[#f2920b]"></i> Fabricación 7-10 días</span>
            </div>
          </div>

          <div class="lg:col-span-5">
            <div class="aspect-[4/3] rounded-3xl overflow-hidden bg-white shadow-xl border border-slate-200 p-2">
              <img src="../{landing['hero_img']}" alt="{landing['hero_img_alt']}" class="w-full h-full object-cover rounded-2xl">
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
            ¿Por qué elegir CoolPadel Studios?
          </h2>
          <p class="text-sm sm:text-base text-slate-600 font-medium">
            Acabado profesional de tienda oficial para elevar la imagen de tu club o evento
          </p>
        </div>

        <div class="grid md:grid-cols-3 gap-6 sm:gap-8">
          {benefits_html}
        </div>
      </div>
    </section>

    <!-- TARIFAS & PROCESO -->
    <section id="precios" class="py-14 sm:py-20 bg-[#3478a6] text-white border-b border-sky-700/40">
      <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div class="text-center max-w-2xl mx-auto mb-10 space-y-2">
          <h2 class="font-heading font-black text-2xl sm:text-4xl uppercase tracking-tight">
            Tarifas Directas de Fabricación B2B
          </h2>
          <p class="text-white/80 text-sm sm:text-base">
            Precios sin intermediarios adaptados al volumen de socios o jugadores
          </p>
        </div>

        <!-- Tabla de Tarifas -->
        <div class="bg-white rounded-3xl p-6 sm:p-8 text-slate-950 shadow-2xl mb-12">
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
                  <td class="py-4 px-3 text-[#f2920b]">2,40 € / ud</td>
                  <td class="py-4 px-3 text-slate-700">600 € (+IVA)</td>
                  <td class="py-4 px-3 text-slate-500 text-xs">Incluida y deducible</td>
                </tr>
                <tr>
                  <td class="py-4 px-3 text-slate-900">500 unidades</td>
                  <td class="py-4 px-3 text-[#f2920b]">2,00 € / ud</td>
                  <td class="py-4 px-3 text-slate-700">1.000 € (+IVA)</td>
                  <td class="py-4 px-3 text-slate-500 text-xs">Incluida y deducible</td>
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
            <span class="text-xs text-slate-500">* Precios sin IVA. Envíos incluidos a toda España peninsular y Unión Europea.</span>
            <a href="https://wa.me/34680317486?text={wa_encoded}" target="_blank" class="px-6 py-3 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition">
              Pedir Presupuesto por WhatsApp
            </a>
          </div>
        </div>

        <!-- Proceso en 3 pasos -->
        <div class="grid sm:grid-cols-3 gap-6 text-center">
          <div class="space-y-2">
            <div class="w-10 h-10 rounded-full bg-white/20 text-white font-heading font-black text-base flex items-center justify-center mx-auto">1</div>
            <h3 class="font-heading font-black text-lg">Envías tu Logotipo</h3>
            <p class="text-white/80 text-xs">Preparamos el diseño digital 3D sin coste para validar proporciones y colores.</p>
          </div>
          <div class="space-y-2">
            <div class="w-10 h-10 rounded-full bg-white/20 text-white font-heading font-black text-base flex items-center justify-center mx-auto">2</div>
            <h3 class="font-heading font-black text-lg">Muestra Física (15€)</h3>
            <p class="text-white/80 text-xs">Fabricamos una muestra real enviada a tu dirección. Los 15€ se descuentan del pedido.</p>
          </div>
          <div class="space-y-2">
            <div class="w-10 h-10 rounded-full bg-white/20 text-white font-heading font-black text-base flex items-center justify-center mx-auto">3</div>
            <h3 class="font-heading font-black text-lg">Producción y Entrega</h3>
            <p class="text-white/80 text-xs">Fabricación final desde 100 uds y entrega en 7-10 días hábiles.</p>
          </div>
        </div>

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
            Resolvemos todas tus dudas antes de encargar los llaveros
          </p>
        </div>

        <div class="space-y-4">
          {faq_html}
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
          Escríbeme directamente por WhatsApp. Te respondo personalmente para ver tu diseño y enviarte la muestra física.
        </p>
        <div class="pt-2 flex flex-col sm:flex-row items-center justify-center gap-4">
          <a href="https://wa.me/34680317486?text={wa_encoded}" target="_blank" class="inline-flex items-center gap-2.5 px-8 py-4 rounded-full bg-[#25D366] hover:bg-[#20ba59] text-white font-heading font-black text-base uppercase tracking-wider shadow-lg hover:scale-105 active:scale-95 transition">
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

  <!-- FOOTER -->
  <footer class="bg-[#0b1626] text-white/60 py-8 border-t border-slate-800 text-center text-xs">
    <div class="max-w-7xl mx-auto px-4 space-y-3">
      <div class="flex items-center justify-center gap-2">
        <a href="../" class="text-white hover:text-[#f2920b] font-bold transition">CoolPadel Studios</a>
        <span>·</span>
        <a href="../#llaveros" class="hover:text-white transition">Llaveros</a>
        <span>·</span>
        <a href="../blog/" class="hover:text-white transition">Blog</a>
        <span>·</span>
        <a href="../politica-de-devoluciones.html" class="hover:text-white transition">Política de Devoluciones</a>
      </div>
      <p>© 2026 CoolPadel Studios · Fabricante B2B de Llaveros de Pádel y Tenis en Goma 3D · Madrid, España</p>
    </div>
  </footer>

  <script>
    lucide.createIcons();
    const GOOGLE_SHEETS_WEBHOOK_URL = '{WEBHOOK_URL}';
    function trackEvent(nombreEvento, metadata) {{
      try {{
        fetch(GOOGLE_SHEETS_WEBHOOK_URL, {{
          method: 'POST',
          mode: 'no-cors',
          headers: {{ 'Content-Type': 'application/json' }},
          body: JSON.stringify({{
            tipo: 'evento',
            evento: nombreEvento,
            url: window.location.href,
            path: window.location.pathname,
            timestamp: new Date().toISOString(),
            metadata: metadata || {{}}
          }})
        }});
      }} catch(e) {{}}
    }}
    trackEvent('page_view_landing', {{ landing: '{landing['slug']}' }});
  </script>
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
