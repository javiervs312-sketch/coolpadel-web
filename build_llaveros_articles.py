"""
Generador de las secciones de Llaveros (Pádel y Tenis) con formato idéntico a /camaras/.
- Calculadora de precios funcional (slider y botones de 100, 250, 500, 1500 uds).
- Paso a paso con textura editorial #3478a6.
- Rejilla de artículos generados a partir de las FAQs y contenido oficial de CoolPadel.
- Páginas de artículo individuales (/articulos/<slug>/) con foto de cabecera, navegación y 'Siguiente paso' directo a WhatsApp/Demo.
"""

from __future__ import annotations

import html
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PADEL_DIR = ROOT / "llaveros-padel-personalizados"
TENIS_DIR = ROOT / "llaveros-tenis-personalizados"

PADEL_IMG_REL_ROOT = "assets/images/llaveros-padel-personalizados-clubs.jpg"
TENIS_IMG_REL_ROOT = "assets/images/llaveros-tenis-personalizados-clubs.jpg"

PADEL_ARTICLES = [
    {
        "slug": "pedido-minimo-plazos-entrega-llaveros-padel",
        "title": "¿Cuál es el pedido mínimo y los plazos de entrega de los llaveros de pádel?",
        "paragraphs": [
            "Si estás pensando en encargar llaveros personalizados con forma de pala para tu club o torneo, una de las primeras preguntas que surgen siempre es cuántos hay que pedir como mínimo y cuándo los tendrás en el club.",
            "En CoolPadel el pedido mínimo de producción es de 100 unidades. No fabricamos tiradas inferiores porque cada modelo requiere crear una matriz o molde 3D exclusivo con el relieve exacto de tu logo, y por debajo de 100 unidades el coste unitario se dispararía.",
            "En cuanto a los plazos, el proceso tiene dos fases muy claras:",
            "1º Fase de muestra física previa: tarda unos 15 días laborables desde que validas el diseño digital en 3D hasta que recibes en la dirección del club una muestra física real para tocar el material, ver la fidelidad de los colores y comprobar el relieve en mano.",
            "2º Fase de producción completa: una vez que nos das el visto bueno con la muestra en la mano, la fabricación de la tirada completa (100, 250, 500 o más unidades) se sitúa en torno a un mes según el volumen del pedido.",
            "Si tienes una fecha límite inamovible (como un torneo de fin de semana, una inauguración o la cena de socios de fin de temporada), te recomendamos iniciar el diseño con 5 o 6 semanas de antelación para ir con total tranquilidad."
        ]
    },
    {
        "slug": "como-pedir-muestra-fisica-15-euros",
        "title": "¿Cómo solicitar la muestra física de 15 € y cómo se descuenta?",
        "paragraphs": [
            "Pedir merchandising o regalos para el club a ciegas, viendo solo un boceto en la pantalla de un ordenador, siempre da respeto. Es muy fácil equivocarse con el tamaño, la dureza del material o el tono exacto de los colores corporativos.",
            "Por eso en CoolPadel nunca te pediremos que encargues 100 o 500 unidades sin haber tocado antes tu llavero real. Hemos creado un sistema de muestra física previa por solo 15 €.",
            "¿Cómo funciona el proceso?",
            "1º Nos envías el escudo o logotipo de tu club por WhatsApp o correo en cualquier formato (vectorial AI, SVG, PDF o incluso un JPG/PNG de buena calidad).",
            "2º Preparamos un render digital 3D gratuito para que veas cómo quedará la distribución del relieve y los colores en la pala.",
            "3º Fabricamos una muestra física real inyectada en molde y te la enviamos a la dirección de tu club por 15 €.",
            "Lo mejor de todo: esos 15 € son 100% deducibles y reembolsables. En el momento en que confirmes el pedido final de la tirada de tu club, restamos automáticamente los 15 € de la factura total. De este modo, la muestra física previa te sale completamente gratis."
        ]
    },
    {
        "slug": "personalizar-reverso-patrocinador-redes",
        "title": "¿Se puede personalizar el reverso del llavero con patrocinadores o redes sociales?",
        "paragraphs": [
            "La respuesta corta es sí, por supuesto. De hecho, es una de las opciones más utilizadas por los clubes que quieren rentabilizar al máximo su merchandising o incluso financiar la totalidad del pedido.",
            "La cara delantera del llavero siempre lleva la forma de la pala de pádel en relieve 3D con el escudo y colores principales del club. Pero el reverso ofrece una superficie trasera perfecta para personalizar:",
            "• Logotipo del patrocinador principal del club (por ejemplo, el concesionario, la aseguradora o el restaurante colaborador).",
            "• El usuario oficial de Instagram del club (@nombreclub) o la dirección de la página web oficial.",
            "• El claim del club, fecha de aniversario o el hashtag oficial del circuito o torneo.",
            "Muchos directores de club nos comentan que, al ofrecerle al patrocinador aparecer en el reverso de cientos de paleteros de los socios durante todo el año, la empresa patrocinadora asume gustosa el coste íntegro de la tirada. Así el club regala un detalle premium a sus jugadores a coste cero."
        ]
    },
    {
        "slug": "precios-facturacion-iva-formas-pago",
        "title": "¿Los precios incluyen IVA? ¿Cómo se realiza la facturación y el pago?",
        "paragraphs": [
            "Queremos que todo sea transparente desde el primer minuto, sin sorpresas ni letra pequeña cuando recibas la factura.",
            "Todos los precios que ves en nuestra calculadora y tarifas (desde 1,50 € hasta 3,00 € por unidad según volumen) se muestran con base imponible, es decir, sin IVA. Al emitir la factura oficial se aplicará el tipo de IVA correspondiente conforme a la normativa fiscal vigente.",
            "¿Cómo emitimos la facturación?",
            "Emitimos factura fiscal oficial a nombre del club, de la sociedad gestora o del autónomo responsable, con todos los datos fiscales (CIF/NIF, razón social, dirección y desglose).",
            "¿Cuáles son las condiciones y formas de pago?",
            "El pago de la muestra física (15 €) se realiza al iniciar el molde mediante transferencia bancaria o tarjeta. Para el pedido de producción final, el abono se formaliza por transferencia una vez validada la muestra física real. Al ser pedidos totalmente personalizados bajo molde para cada club, la fabricación en serie se inicia con la factura confirmada."
        ]
    },
    {
        "slug": "tamano-peso-material-goma-3d-microinyectada",
        "title": "¿Qué tamaño, peso y material tienen los llaveros de pádel personalizados?",
        "paragraphs": [
            "Un llavero para jugadores de pádel tiene que cumplir dos condiciones indispensables: ser muy resistente y no dañar nada de lo que lleva alrededor en el paletero o en la mochila.",
            "Los llaveros metálicos o de plástico rígido suelen rayar los marcos de las palas, golpear los móviles o desgastar los bolsillos. Por eso en CoolPadel fabricamos exclusivamente con goma PVC flexible de alta densidad microinyectada en relieve 3D.",
            "Características técnicas del llavero:",
            "• Longitud: aproximadamente 70 mm de largo. Un tamaño óptimo, con presencia visual contundente pero sin resultar pesado ni incómodo en el bolsillo.",
            "• Tacto: flexible, agradable y con relieve volumétrico real donde los bordes y letras se sienten al tacto.",
            "• Resistencia: es totalmente impermeable, aguanta caídas, roces continuos, sudor y cambios bruscos de temperatura sin decolorarse ni agrietarse.",
            "• Herraje: anilla metálica reforzada con eslabón de alta resistencia para enganchar con total seguridad a la cremallera del paletero o a las llaves de casa."
        ]
    },
    {
        "slug": "vender-llaveros-tienda-recepcion-club",
        "title": "¿Puedo vender los llaveros en la tienda o recepción del club? Rentabilidad real",
        "paragraphs": [
            "Muchos clubes encargan llaveros como detalle institucional o regalo para sus socios, pero un porcentaje muy elevado de nuestros clientes los utiliza como una vía de ingresos recurrente y de altísimo margen.",
            "Hagamos los números con un caso real de un club de 4 pistas:",
            "• Coste de compra de 250 unidades: 2,50 € por unidad (625 € de inversión total, con envíos incluidos y muestra previa descontada).",
            "• Precio de venta al público en recepción o tienda: habitualmente los clubes los comercializan a 5,00 € o 6,00 € cada uno.",
            "• Ingreso generado: vendiendo las 250 unidades a 5,50 € obtienes 1.375 € brutos.",
            "• Beneficio neto para el club: 750 € limpios de margen, lo que supone más de un 100% de rentabilidad sobre el capital invertido.",
            "Además, al colocarlos junto al mostrador de recepción en una bandeja o soporte visible, es una compra por impulso clásica: los jugadores que vienen a jugar la partida o recoger botes de pelotas se llevan el llavero de recuerdo para su paletero."
        ]
    },
    {
        "slug": "ocasiones-usos-llaveros-padel-torneos-socios",
        "title": "¿Para qué ocasiones y eventos sirven los llaveros de pádel personalizados?",
        "paragraphs": [
            "La versatilidad de los llaveros 3D los convierte en uno de los artículos promocionales más apreciados del sector del pádel. A diferencia de las típicas camisetas de talla única que acaban olvidadas en un cajón, el llavero acompaña al jugador durante años.",
            "Las aplicaciones más habituales entre nuestros clubes clientes son:",
            "1. Welcome packs de torneos y campeonatos: regalar un llavero 3D con el logo del torneo y de los patrocinadores eleva de inmediato la percepción de calidad del evento.",
            "2. Regalo de bienvenida o renovación de socios: entregar el llavero oficial al darse de alta o en las cenas anuales de fin de temporada crea un sentido de pertenencia enorme en la comunidad.",
            "3. Escuelas de pádel y menores: detalle para los alumnos de la escuela deportiva al finalizar el trimestre o en campamentos de verano.",
            "4. Inauguraciones y aperturas de nuevas pistas: detalle institucional para autoridades, prensa, patrocinadores y primeros visitantes.",
            "5. Merchandising oficial del club: producto estrella en la pro-shop para venta directa a visitantes y jugadores locales."
        ]
    },
    {
        "slug": "paises-envio-cobertura-internacional",
        "title": "¿A qué países realizáis envíos de llaveros de pádel?",
        "paragraphs": [
            "CoolPadel nació en España pero hoy en día fabricamos y distribuimos merchandising deportivo para clubes de todo el mundo.",
            "Nuestra red logística cubre habitualmente:",
            "• España: envíos a toda la Península, Islas Baleares e Islas Canarias con seguimiento puerta a puerta.",
            "• Unión Europea: envíos regulares y directos a clubes de Italia, Francia, Bélgica, Países Bajos, Portugal, Alemania y Austria.",
            "• Estados Unidos: servicio logístico directo para clubes, complejos indoor y academias en crecimiento en Florida, Texas, California y Nueva York.",
            "En todos los pedidos de producción estándar los gastos de envío a la Península, Europa y USA están ya contemplados en la tarifa o cotizados de forma clara antes del encargo, sin tasas sorpresa ni recargos en la aduana."
        ]
    },
    {
        "slug": "reutilizar-molde-pedidos-futuros-reposiciones",
        "title": "¿Podemos repetir pedidos en el futuro con el mismo molde sin pagar diseño?",
        "paragraphs": [
            "Rotundamente sí. Cuando fabricas por primera vez con nosotros, creamos una matriz de inyección metálica exclusiva para tu club con el relieve y proporciones aprobadas.",
            "Ese molde queda registrado y custodiado en fábrica para tu uso exclusivo. Esto significa que cuando se te agoten las unidades en recepción o prepares el siguiente torneo:",
            "• No tendrás que volver a abonar ningún coste de diseño ni muestra previa.",
            "• El plazo de producción es más ágil porque el molde ya está listo y calibrado.",
            "• Puedes pedir reposiciones cómodamente de 100 en 100 unidades siempre que lo necesites a la misma tarifa de fábrica.",
            "Es la fórmula más económica y cómoda para mantener el stock de merchandising de tu club durante años."
        ]
    }
]

TENIS_ARTICLES = [
    {
        "slug": "llaveros-de-tenis-vs-padel-diferencias-materiales",
        "title": "¿Fabricáis llaveros tanto de tenis como de pádel? Diferencias de diseño",
        "paragraphs": [
            "Muchos de los clubes con los que trabajamos son entidades con una larga trayectoria polideportiva: cuentan con pistas de tenis tradicionales de tierra batida o resina, y también con pistas de pádel cubiertas o descubiertas.",
            "En CoolPadel diseñamos y fabricamos modelos específicos adaptados a cada disciplina:",
            "• Llaveros de Tenis: siluetas en relieve 3D con forma de raqueta tradicional, encordado detallado o directamente el escudo heráldico y la tipografía clásica del club de tenis.",
            "• Llaveros de Pádel: siluetas con la morfología de pala moderna de pádel, perforaciones en relieve y relieve perimetral del marco.",
            "Si tu club tiene ambas secciones, puedes encargar pedidos combinados o crear una línea de merchandising unificada que respete la identidad de socios de tenis y de pádel por igual."
        ]
    },
    {
        "slug": "formatos-logotipo-escudo-para-llaveros-tenis",
        "title": "¿Qué formatos de logotipo o escudo aceptáis para fabricar llaveros de tenis?",
        "paragraphs": [
            "Los clubes de tenis históricos suelen tener escudos muy elaborados, con coronas, raquetas cruzadas, banderas o tipografías tradicionales que no siempre están digitalizadas en alta resolución.",
            "No te preocupes si no tienes el archivo en formato vectorial (AI o SVG). Nuestro equipo de diseño gráfico se encarga de todo:",
            "1º Puedes enviarnos cualquier imagen que tengas: un archivo PDF, un PNG, un JPG e incluso una foto clara de una camiseta, cartel o membrete del club.",
            "2º Nuestro equipo vectorializa y modela el escudo en relieve volumétrico 3D, ajustando grosores para que cada línea quede limpia y perfectamente definida en el caucho inyectado.",
            "3º Te presentamos la propuesta digital en 3D para tu revisión y aprobación sin coste alguno antes de fundir el molde físico."
        ]
    },
    {
        "slug": "vender-llaveros-tenis-pro-shop-escuelas-rentabilidad",
        "title": "¿Sirven para vender en la pro-shop o escuela del club de tenis? Margen comercial",
        "paragraphs": [
            "En los clubes de tenis el merchandising con escudo oficial tiene una acogida extraordinaria entre los alumnos de la escuela infantil, veteranos y socios de fin de semana.",
            "Al fabricarse en goma PVC 3D microinyectada, el llavero tiene una gran ventaja frente a los llaveros de metal: no raya las raquetas ni estropea las fundas térmicas cuando se guarda dentro del raquetero.",
            "Desde el punto de vista comercial, el margen para el club es muy atractivo:",
            "• Con una tirada de 100 a 250 unidades el coste se sitúa entre 2,50 € y 3,00 € por unidad.",
            "• En la tienda del club o recepción se suelen vender a 5,00 € - 6,00 €.",
            "• Cada lote vendido genera entre un 50% y un 100% de beneficio neto para el club, además de proyectar la imagen y el escudo de la entidad por todos los torneos donde viajen los jugadores."
        ]
    },
    {
        "slug": "llaveros-tenis-regalos-torneos-welcome-packs",
        "title": "Llaveros de tenis para torneos sociales, circuitos juveniles y welcome packs",
        "paragraphs": [
            "Organizar un torneo de tenis federado o un torneo social de socios implica buscar detalles de bienvenida que realmente agraden a los participantes sin disparar el presupuesto del evento.",
            "Un llavero de tenis en relieve 3D personalizado con el nombre del torneo y el logo del patrocinador:",
            "• Ocupa poco espacio y se entrega cómodamente en el welcome pack junto a las bolas y la botella de agua.",
            "• Permite incluir en el reverso la marca del patrocinador que financia el torneo, ofreciéndole una visibilidad que dura años y no solo el fin de semana de partidos.",
            "• Es un recuerdo duradero que los jugadores conservan colgado de sus raqueteros."
        ]
    }
]

CSS = """
* { box-sizing: border-box; }
body { margin: 0; background: #fff; color: #0f172a; font-family: 'Plus Jakarta Sans', Arial, sans-serif; line-height: 1.7; }
.official-header a { text-decoration: none; }
.header-inner { width: 100%; }
.logo-link { display: flex; align-items: center; gap: 8px; flex-shrink: 0; }
.logo-mascot { height: 44px; width: auto; object-fit: contain; }
.logo-wordmark { height: 28px; width: auto; object-fit: contain; }
.official-nav { display: flex; align-items: center; gap: 18px; font-size: 11px; font-weight: 900; letter-spacing: .07em; text-transform: uppercase; }
.official-nav > a { color: #334155; white-space: nowrap; }
.official-nav > a:hover { color: #f2920b; }
.lang-links { display: flex; gap: 5px; padding: 5px 8px; border-radius: 999px; background: #f1f5f9; border: 1px solid #e2e8f0; }
.lang-links a { color: #475569; font-size: 10px; }
.lang-links a:first-child { color: #f2920b; }
.nav-contact { display: inline-flex; align-items: center; gap: 5px; padding: 9px 14px; border-radius: 999px; background: #f2920b; color: #0f172a !important; }
.nav-contact:hover { background: #76d3f6; color: #0f172a !important; }
.eyes-thumb { height: 26px; width: auto; }
.header-spacer { height: 80px; }
main { max-width: 1700px; margin: 0 auto; padding: 40px 20px 80px; }
h1, h2, h3, .font-heading { font-family: 'Outfit', Arial, sans-serif; line-height: 1.15; letter-spacing: -.03em; }
h1 { max-width: 900px; font-size: clamp(34px, 5vw, 56px); margin: 0 0 24px; font-weight: 900; color: #0f172a; }
.article h1 { padding: 0 0 24px; margin-bottom: 0; font-size: clamp(34px, 4.5vw, 52px); font-weight: 900; line-height: 1.1; }
h2 { font-size: clamp(26px, 3.5vw, 38px); margin: 0 0 16px; }
h3 { font-size: 22px; margin: 0 0 12px; }
.article { max-width: 760px; margin: 0 auto; }
.article p { margin: 0 0 22px; font-size: 18px; line-height: 1.75; color: #334155; }
.article a { color: #3478a6; font-weight: 700; text-decoration: underline; text-underline-offset: 3px; }
.article-hero { display: block; width: 100%; max-height: 440px; height: auto; object-fit: cover; object-position: center; background: #f8fafc; border-radius: 16px; margin: 0 auto 32px; border: 1px solid #e2e8f0; }
.next-step { margin: 48px 0 40px; padding: 28px 30px 30px; border: 2px solid #f2920b; border-radius: 18px; background: #fffaf2; box-shadow: 0 8px 24px rgba(15,23,42,.06); }
.next-step h2 { color: #0f172a; font-weight: 900; margin-bottom: 14px; }
.next-step p { margin: 8px 0; font-size: 16px; color: #334155; }
.related { margin-top: 48px; }
.related h2 { font-weight: 900; padding-bottom: 12px; border-bottom: 3px solid #f2920b; }
.related-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px; }
.related a { display: block; padding: 16px; color: #0f172a; text-decoration: none; border: 1px solid #cbd5e1; border-radius: 12px; font-weight: 700; background: #fff; }
.related a:hover { border-color: #f2920b; }
@media (max-width: 900px) { .official-nav > a:not(.nav-contact), .lang-links { display: none; } }
@media (max-width: 1050px) { .article-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
@media (max-width: 760px) { .logo-wordmark { height: 22px; } .logo-mascot { height: 34px; } .article-grid, .related-grid { grid-template-columns: 1fr; } main { padding-top: 24px; } .article p { font-size: 16px; } .article-hero { max-height: none; } }

.hub-hero { max-width: 1200px; margin: 20px auto 40px; text-align: center; }
.hub-eyebrow { margin: 0 0 12px; color: #f2920b; font-size: 13px; font-weight: 900; letter-spacing: .04em; text-transform: uppercase; }
.hub-title { max-width: none !important; margin: 0 0 16px !important; font-size: clamp(38px, 4vw, 56px) !important; font-weight: 900 !important; line-height: 1.08 !important; color: #0f172a !important; text-transform: uppercase; letter-spacing: -.04em; }
.intro { max-width: 820px; margin: 0 auto; color: #334155; font-size: 18px; line-height: 1.6; }
.intro p { margin: 0 0 14px; }
.article-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 18px; margin: 34px 0 0; }
.article-card { color: #0f172a; text-decoration: none; }
.article-card img { display: block; }
.card-action:active { background: #76d3f6; transform: scale(.98); }
.bg-textured-blue {
  background-color: #3478a6;
  background-image: linear-gradient(rgba(52, 120, 166, 0.40), rgba(52, 120, 166, 0.40)), url('../assets/images/branding/textura_editorial_coolpadel.webp');
  background-blend-mode: normal, soft-light;
  background-size: cover;
  background-position: center;
}
"""


def get_header(prefix: str = "../") -> str:
    return f'''<header class="fixed top-0 left-0 w-full z-50 bg-white/95 backdrop-blur-md border-b border-slate-200/80 shadow-xs w-full"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 sm:h-20 flex items-center justify-between"><a href="{prefix}" class="flex items-center gap-2 group shrink-0" aria-label="CoolPadel Home"><img src="{prefix}assets/images/coolpadel-mascot-hd.png" alt="Mascota CoolPadel" width="44" height="44" class="h-8 sm:h-11 w-auto object-contain group-hover:scale-105 transition" fetchpriority="high"><img src="{prefix}assets/images/coolpadel-typography-hd.png" alt="CoolPadel" width="140" height="28" class="h-5 sm:h-7 w-auto object-contain" fetchpriority="high"></a><div class="flex items-center gap-2 sm:gap-4 lg:gap-6"><a href="{prefix}llaveros-padel-personalizados/" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">LLAVEROS</a><a href="{prefix}camaras/" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">CÁMARAS</a><a href="{prefix}blog/" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">Blog</a><a href="{prefix}franquicias-padel/" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">Cadenas de clubs</a><div class="relative inline-block text-left" id="lang-dropdown-container"><button type="button" onclick="toggleLangDropdown(event)" id="lang-dropdown-btn" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 border border-slate-200 text-xs font-black text-slate-900 shadow-xs transition cursor-pointer" aria-expanded="false" aria-haspopup="true"><span id="current-lang-code" class="uppercase font-black">ES</span><i data-lucide="chevron-down" class="w-3.5 h-3.5 stroke-[2.5] text-slate-600 transition-transform duration-200" id="lang-dropdown-arrow"></i></button><div id="lang-dropdown-menu" class="hidden absolute right-0 mt-2 w-24 bg-white rounded-2xl shadow-[0_12px_30px_rgba(0,0,0,0.15)] border border-slate-200 py-1.5 z-50 transition-all overflow-hidden"><a href="/llaveros-padel-personalizados/" class="block text-center px-4 py-2 text-xs">ES</a><a href="/en/llaveros-padel-personalizados/" class="block text-center px-4 py-2 text-xs">EN</a><a href="/fr/llaveros-padel-personalizados/" class="block text-center px-4 py-2 text-xs">FR</a><a href="/it/llaveros-padel-personalizados/" class="block text-center px-4 py-2 text-xs">IT</a></div></div><a href="{prefix}#contacto" class="inline-flex items-center gap-1.5 px-3.5 sm:px-4 py-1.5 sm:py-2 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition shadow-sm hover:scale-105 active:scale-95 cursor-pointer"><span>Contactar</span><i data-lucide="arrow-down" class="w-3 h-3 stroke-[3]"></i></a><a href="{prefix}" class="group py-1 inline-flex items-center shrink-0 pl-1" aria-label="CoolPadel Eyes"><img src="{prefix}assets/images/eyes-thumb.png?v=fixed_eyes" alt="CoolPadel Eyes" width="28" height="28" style="height:26px;max-height:26px;width:auto" class="object-contain group-hover:scale-110 transition duration-300"></a></div></div></header><div class="h-16 sm:h-20 w-full shrink-0" aria-hidden="true"></div>'''


def get_calculator_html(prefix: str = "../") -> str:
    return f'''
    <!-- CALCULADORA DE PRECIOS INTERACTIVA -->
    <div id="precios" class="max-w-4xl mx-auto w-full text-white">
      <div class="text-center mb-8 space-y-1">
        <h2 class="text-2xl sm:text-3xl lg:text-4xl font-black font-heading text-white uppercase tracking-tight">
          Calcula tu pedido
        </h2>
        <p class="text-sm sm:text-base text-white/90 font-medium">
          Envíos incluidos a toda España y Europa
        </p>
      </div>

      <div class="space-y-6">
        <div class="flex justify-between items-end pb-4 border-b border-white/20">
          <div>
            <span class="text-sm sm:text-base font-bold text-white/80 uppercase tracking-wider block mb-1">Nº de llaveros:</span>
            <span id="calc-qty-badge" class="text-2xl sm:text-4xl lg:text-5xl font-black font-heading text-white">100 unidades</span>
          </div>
          <div class="text-right">
            <span class="text-sm sm:text-base font-bold text-white/80 uppercase tracking-wider block mb-1">Importe estimado:</span>
            <div class="flex items-baseline justify-end gap-2">
              <span id="calc-price-badge" class="text-2xl sm:text-4xl lg:text-5xl font-black font-heading text-[#f2920b]">300 €</span>
              <span id="calc-unit-badge" class="text-sm sm:text-lg font-bold text-white/85">(3,00 €/ud)</span>
            </div>
          </div>
        </div>

        <!-- Slider de selección -->
        <div class="py-3" id="calc-slider-box">
          <div class="relative w-full h-3.5 bg-white/20 rounded-full cursor-pointer select-none" id="slider-track">
            <div id="slider-progress" class="absolute top-0 left-0 h-full bg-[#f2920b] rounded-full pointer-events-none" style="width: 0%;"></div>
            <div id="slider-thumb" class="absolute top-1/2 -translate-x-1/2 -translate-y-1/2 w-10 h-5 flex items-center justify-center cursor-grab active:cursor-grabbing hover:scale-110 transition-transform" style="left: 0%;">
              <img src="{prefix}assets/images/eyes-thumb.png" alt="Selector" width="40" height="20" class="w-full h-full object-contain drop-shadow select-none pointer-events-none">
            </div>
          </div>
          <div class="relative w-full text-xs sm:text-sm font-extrabold text-white/90 h-6 mt-3.5 select-none">
            <button type="button" onclick="setTier(0)" class="absolute left-0 hover:text-[#f2920b] transition cursor-pointer">100 uds</button>
            <button type="button" onclick="setTier(1)" class="absolute left-[33.3%] -translate-x-1/2 hover:text-[#f2920b] transition cursor-pointer">250 uds</button>
            <button type="button" onclick="setTier(2)" class="absolute left-[66.6%] -translate-x-1/2 hover:text-[#f2920b] transition cursor-pointer">500 uds</button>
            <button type="button" onclick="setTier(3)" class="absolute right-0 hover:text-[#f2920b] transition cursor-pointer">1.500 uds</button>
          </div>
        </div>

        <div class="flex flex-wrap items-center justify-center gap-4 sm:gap-6 pt-3 text-sm sm:text-base font-bold text-white">
          <span class="inline-flex items-center gap-1.5">
            <i data-lucide="check-circle" class="w-4 h-4 text-[#f2920b] shrink-0"></i>
            Muestra física 15 €
          </span>
          <span class="inline-flex items-center gap-1.5">
            <i data-lucide="check-circle" class="w-4 h-4 text-[#f2920b] shrink-0"></i>
            IVA no incluido
          </span>
          <span class="inline-flex items-center gap-1.5">
            <i data-lucide="check-circle" class="w-4 h-4 text-[#f2920b] shrink-0"></i>
            Entrega ~1 mes
          </span>
        </div>

        <div class="pt-3">
          <a id="calc-wa-btn" href="https://api.whatsapp.com/send?phone=34680317486&text=Hola%20Javier%2C%20me%20interesa%20solicitar%20presupuesto%20de%20100%20llaveros%20para%20mi%20club" target="_blank" rel="noopener noreferrer" class="w-full py-3.5 rounded-2xl font-heading font-black text-sm uppercase tracking-wider bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 shadow-md hover:shadow-lg hover:scale-[1.01] active:scale-[0.98] flex items-center justify-center gap-2 transition-all cursor-pointer">
            <i data-lucide="message-circle" class="w-4 h-4 stroke-[2.5]"></i>
            <span>Contactar</span>
          </a>
        </div>
      </div>
    </div>
'''


def get_paso_a_paso_html() -> str:
    return '''
    <!-- PASO A PASO -->
    <div class="max-w-4xl mx-auto w-full text-white pt-10 mt-10 border-t border-white/20">
      <div class="text-center max-w-2xl mx-auto mb-6 sm:mb-8 space-y-1">
        <span class="inline-block px-3.5 py-1 rounded-full bg-white/20 text-white font-heading font-black text-xs uppercase tracking-wider">
          Paso a Paso
        </span>
        <h2 class="font-heading font-black text-2xl sm:text-3xl uppercase tracking-tight text-white">
          ¿Cómo pedir para tu club?
        </h2>
      </div>

      <div class="grid sm:grid-cols-3 gap-4 sm:gap-6 text-left">
        <div class="bg-white/95 rounded-2xl p-5 text-slate-900 shadow-md border border-white/40 space-y-2">
          <div class="w-8 h-8 rounded-full bg-[#f2920b] text-slate-950 font-heading font-black text-xs flex items-center justify-center">1</div>
          <h3 class="font-heading font-black text-base text-slate-950">Envíanos tu logo</h3>
          <p class="text-slate-600 text-xs sm:text-sm leading-relaxed">Envíanos el logo de tu club en cualquier formato (vectorial, PNG o JPG) y preparamos tu diseño digital 3D gratuito.</p>
        </div>

        <div class="bg-white/95 rounded-2xl p-5 text-slate-900 shadow-md border border-white/40 space-y-2">
          <div class="w-8 h-8 rounded-full bg-[#f2920b] text-slate-950 font-heading font-black text-xs flex items-center justify-center">2</div>
          <h3 class="font-heading font-black text-base text-slate-950">Muestra Física 15 €</h3>
          <p class="text-slate-600 text-xs sm:text-sm leading-relaxed">Fabricamos una muestra física real para que la toques antes de producir la tirada completa. 15 € 100% reembolsables con el pedido.</p>
        </div>

        <div class="bg-white/95 rounded-2xl p-5 text-slate-900 shadow-md border border-white/40 space-y-2">
          <div class="w-8 h-8 rounded-full bg-[#f2920b] text-slate-950 font-heading font-black text-xs flex items-center justify-center">3</div>
          <h3 class="font-heading font-black text-base text-slate-950">Producción y Entrega</h3>
          <p class="text-slate-600 text-xs sm:text-sm leading-relaxed">Pedido mínimo de 100 unidades y entrega en torno a un mes con envíos incluidos a España, Europa y USA.</p>
        </div>
      </div>
    </div>
'''


def get_calculator_script() -> str:
    return '''
  <script>
    const tiers = [
      { qty: '100', price: '300', unit: '3,00', pct: 0 },
      { qty: '250', price: '625', unit: '2,50', pct: 33.333 },
      { qty: '500', price: '1.000', unit: '2,00', pct: 66.666 },
      { qty: '1.500', price: '2.250', unit: '1,50', pct: 100 }
    ];

    let currentTierIdx = 0;
    const qtyBadge = document.getElementById('calc-qty-badge');
    const priceBadge = document.getElementById('calc-price-badge');
    const unitBadge = document.getElementById('calc-unit-badge');
    const waBtn = document.getElementById('calc-wa-btn');
    const sliderThumb = document.getElementById('slider-thumb');
    const sliderProgress = document.getElementById('slider-progress');
    const sliderTrack = document.getElementById('slider-track');
    const sliderBox = document.getElementById('calc-slider-box');

    function updateCalculator(idx, isLiveDrag) {
      if (!qtyBadge) return;
      currentTierIdx = idx;
      const tier = tiers[idx];
      qtyBadge.textContent = tier.qty + ' unidades';
      priceBadge.textContent = tier.price + ' €';
      unitBadge.textContent = '(' + tier.unit + ' €/ud)';

      if (sliderThumb && sliderProgress) {
        if (isLiveDrag) {
          sliderThumb.style.transition = 'none';
          sliderProgress.style.transition = 'none';
        } else {
          sliderThumb.style.transition = 'left 0.25s cubic-bezier(0.25, 1, 0.5, 1)';
          sliderProgress.style.transition = 'width 0.25s cubic-bezier(0.25, 1, 0.5, 1)';
        }
        sliderThumb.style.left = tier.pct + '%';
        sliderProgress.style.width = tier.pct + '%';
      }

      if (waBtn) {
        const msg = encodeURIComponent('Hola Javier, me interesa solicitar presupuesto de ' + tier.qty + ' llaveros para mi club (' + tier.price + ' €, ' + tier.unit + ' €/ud).');
        waBtn.href = 'https://api.whatsapp.com/send?phone=34680317486&text=' + msg;
      }
    }

    window.setTier = function(idx) {
      updateCalculator(idx, false);
    };

    let isDragging = false;
    function handleSliderInteraction(clientX, isLive) {
      if (!sliderTrack) return;
      const rect = sliderTrack.getBoundingClientRect();
      const x = Math.max(0, Math.min(clientX - rect.left, rect.width));
      const ratio = x / rect.width;
      let closestIdx = 0;
      let minDiff = 999;
      tiers.forEach((t, i) => {
        const diff = Math.abs((t.pct / 100) - ratio);
        if (diff < minDiff) {
          minDiff = diff;
          closestIdx = i;
        }
      });
      updateCalculator(closestIdx, isLive);
    }

    if (sliderBox) {
      sliderBox.addEventListener('touchstart', (e) => {
        isDragging = true;
        if (e.touches && e.touches.length > 0) handleSliderInteraction(e.touches[0].clientX, true);
      }, { passive: true });

      sliderBox.addEventListener('touchmove', (e) => {
        if (!isDragging) return;
        if (e.touches && e.touches.length > 0) {
          handleSliderInteraction(e.touches[0].clientX, true);
          if (e.cancelable) e.preventDefault();
        }
      }, { passive: false });

      sliderBox.addEventListener('touchend', () => {
        if (isDragging) {
          isDragging = false;
          updateCalculator(currentTierIdx, false);
        }
      }, { passive: true });

      sliderBox.addEventListener('pointerdown', (e) => {
        isDragging = true;
        handleSliderInteraction(e.clientX, true);
        window.addEventListener('pointermove', onPointerMove);
        window.addEventListener('pointerup', onPointerUp);
      });

      function onPointerMove(e) {
        if (isDragging) handleSliderInteraction(e.clientX, true);
      }
      function onPointerUp() {
        if (isDragging) {
          isDragging = false;
          updateCalculator(currentTierIdx, false);
        }
        window.removeEventListener('pointermove', onPointerMove);
        window.removeEventListener('pointerup', onPointerUp);
      }
    }
    // Inicializar
    updateCalculator(0, false);
  </script>
'''


def render_page(title: str, content: str, prefix: str = "../") -> str:
    return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{html.escape(title)} | CoolPadel</title><meta name="description" content="{html.escape(title)}"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Outfit:wght@600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"><script src="https://cdn.tailwindcss.com"></script><script src="https://unpkg.com/lucide@0.468.0/dist/umd/lucide.min.js"></script><style>{CSS}</style></head><body>{get_header(prefix)}{content}<script>if (window.lucide) lucide.createIcons();</script><script src="{prefix}assets/js/cp-analytics.js" defer></script></body></html>'''


def build_hub(hub_dir: Path, is_padel: bool, articles: list[dict]):
    hub_dir.mkdir(parents=True, exist_ok=True)
    articulos_dir = hub_dir / "articulos"
    articulos_dir.mkdir(parents=True, exist_ok=True)

    eyebrow = "Merchandising oficial para clubes de pádel" if is_padel else "Llaveros y merchandising oficial para clubes de tenis"
    h1_text = "Llaveros de Pádel Personalizados 3D" if is_padel else "Llaveros de Tenis Personalizados con Escudo Oficial"
    intro_p1 = (
        "Fabricante directo de llaveros de pádel personalizados en relieve 3D de goma microinyectada.<br>Pedidos desde 100 unidades, muestra física real por 15 € deducible al 100% y tarifas directas de fábrica para clubes y torneos."
        if is_padel else
        "Diseñamos y fabricamos llaveros de tenis en relieve 3D para escuelas de tenis, clubes históricos y torneos sociales.<br>Material flexible de alta densidad que no raya raquetas ni fundas, pedidos desde 100 unidades y muestra física previa por 15 €."
    )

    image_src = "../" + (PADEL_IMG_REL_ROOT if is_padel else TENIS_IMG_REL_ROOT)

    cards = "\n".join(
        f'''<a href="articulos/{a["slug"]}/" class="article-card bg-white border-2 border-slate-200/90 hover:border-[#f2920b] rounded-2xl p-4 sm:p-5 shadow-2xs hover:shadow-lg transition-all duration-300 flex flex-col justify-between group hover:-translate-y-0.5 cursor-pointer block"><div class="space-y-3"><div class="aspect-[16/9] rounded-xl overflow-hidden bg-slate-100 border border-slate-200/90 shadow-sm relative"><img src="{image_src}" alt="{html.escape(a["title"])}" width="800" height="450" class="w-full h-full object-cover group-hover:scale-105 transition duration-500" loading="lazy" decoding="async"></div><div><h3 class="font-sans font-extrabold text-sm sm:text-base lg:text-lg text-slate-900 leading-snug tracking-tight transition-colors">{html.escape(a["title"])}</h3></div></div><div class="pt-3.5 border-t border-slate-100 mt-4"><div class="card-action group relative w-full inline-flex items-center justify-center gap-2 px-4 py-2.5 rounded-full bg-[#f2920b] group-hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition-all duration-300 shadow-xs group-hover:shadow-md group-hover:scale-[1.01] overflow-hidden active:scale-[.98]"><span class="font-black">Leer artículo</span><div class="w-4 h-4 rounded-full bg-slate-950/10 group-hover:bg-slate-950 group-hover:text-white flex items-center justify-center transition-all duration-300"><i data-lucide="arrow-right" class="w-3 h-3 stroke-[3] group-hover:translate-x-0.5 transition-transform duration-300"></i></div></div></div></a>'''
        for a in articles
    )

    hub_content = f'''
    <main class="!pb-0">
      <section class="hub-hero">
        <p class="hub-eyebrow">{eyebrow}</p>
        <h1 class="hub-title">{h1_text}</h1>
        <div class="intro">
          <p>{intro_p1}</p>
        </div>
      </section>
    </main>

    <!-- SECCIÓN CALCULADORA Y PASO A PASO CON FONDO COMPLETO DE TEXTURA #3478a6 -->
    <section class="w-full bg-[#3478a6] bg-textured-blue text-white py-10 sm:py-14 border-y border-sky-700/40">
      <div class="max-w-4xl mx-auto px-4 sm:px-6">
        {get_calculator_html(prefix="../")}
        {get_paso_a_paso_html()}
      </div>
    </section>

    <main class="!pt-8 sm:!pt-12">
      <section class="article-grid">{cards}</section>

      <section class="next-step max-w-4xl mx-auto">
        <h2>Siguiente paso</h2>
        <p>¿Quieres ver cómo quedaría el logo de tu club en relieve 3D? Preparamos tu diseño digital y te enviamos la muestra física real.</p>
        <div class="pt-3">
          <a href="https://api.whatsapp.com/send?phone=34680317486&text=Hola%20Javier%2C%20quiero%20ver%20el%20dise%C3%B1o%203D%20y%20pedir%20presupuesto%20de%20llaveros" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 px-7 py-3.5 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition shadow-md hover:scale-105 active:scale-95 cursor-pointer">
            <i data-lucide="message-circle" class="w-4 h-4 stroke-[2.5]"></i>
            <span>Hablar con Javier por WhatsApp</span>
          </a>
        </div>
      </section>
    </main>
    {get_calculator_script()}
'''

    (hub_dir / "index.html").write_text(render_page(h1_text, hub_content, prefix="../"), encoding="utf-8")
    print(f"  [OK] Hub generado: {hub_dir / 'index.html'}")

    # Generar cada artículo individual
    for index, a in enumerate(articles):
        art_dir = articulos_dir / a["slug"]
        art_dir.mkdir(parents=True, exist_ok=True)
        art_img = "../../../" + (PADEL_IMG_REL_ROOT if is_padel else TENIS_IMG_REL_ROOT)

        body_html = "\n".join(f"<p>{p}</p>" for p in a["paragraphs"])

        related = [articles[(index + offset) % len(articles)] for offset in (1, 2, 3)]
        related_html = "\n".join(f'<a href="../{r["slug"]}/">{html.escape(r["title"])}</a>' for r in related)

        article_content = f'''<main>
          <article class="article">
            <nav class="flex items-center gap-2 text-xs font-bold text-slate-500 mb-6 uppercase tracking-wider">
              <a href="../../../" class="hover:text-slate-900 transition">Inicio</a>
              <span>/</span>
              <a href="../../" class="hover:text-slate-900 transition">{"Llaveros Pádel 3D" if is_padel else "Llaveros de Tenis"}</a>
              <span>/</span>
              <span class="text-[#f2920b]">Artículo</span>
            </nav>

            <h1>{html.escape(a["title"])}</h1>
            <img class="article-hero" src="{art_img}" alt="{html.escape(a["title"])}" loading="lazy">
            {body_html}

            <section class="related">
              <h2>Más artículos sobre llaveros</h2>
              <div class="related-grid">{related_html}</div>
            </section>

            <section class="next-step">
              <h2>Siguiente paso</h2>
              <p>Si todavía tienes dudas sobre cómo pedir para tu club o quieres consultar tu diseño digital en 3D, contáctanos directamente por WhatsApp.</p>
              <div class="pt-3">
                <a href="https://api.whatsapp.com/send?phone=34680317486&text=Hola%20Javier%2C%20estoy%20leyendo%20sobre%20los%20llaveros%20y%20quiero%20informaci%C3%B3n%20para%20mi%20club" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition shadow-md hover:scale-105 active:scale-95 cursor-pointer">
                  <i data-lucide="message-circle" class="w-4 h-4 stroke-[2.5]"></i>
                  <span>Hablar con Javier por WhatsApp</span>
                </a>
              </div>
            </section>
          </article>
        </main>
'''
        (art_dir / "index.html").write_text(render_page(a["title"], article_content, prefix="../../../"), encoding="utf-8")
    print(f"  [OK] {len(articles)} artículos generados en: {articulos_dir}")


def build_all():
    print(">> Construyendo Hubs y Artículos de Llaveros (Pádel y Tenis) en Español...")
    build_hub(PADEL_DIR, is_padel=True, articles=PADEL_ARTICLES)
    build_hub(TENIS_DIR, is_padel=False, articles=TENIS_ARTICLES)
    print(">> ¡Completado con éxito!")


if __name__ == "__main__":
    build_all()
