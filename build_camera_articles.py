"""Build the simple camera article hub from Javier's source DOCX."""

from __future__ import annotations

import html
import re
import subprocess
from pathlib import Path

from docx import Document


ROOT = Path(__file__).resolve().parent
DOCX = Path(r"C:\Users\javie\OneDrive\Documentos\Impresión 3D\Palas definitivo\Clubs\Contacto clubs\CoolPadel Branding\Save My Play They ask, you answer.docx")
CAMERAS = ROOT / "camaras"
ARTICLES = CAMERAS / "articulos"
CALENDLY = "https://calendly.com/javier-vs-312/demo-save-my-play?locale=es"
ASSET_DIR = ROOT / "assets" / "images" / "camaras"

ARTICLE_IMAGES = {
    "por-donde-empezar-si-estoy-pensando-en-poner-camaras": "camera-01.jpg",
    "errores-clubs-se-arrepienten-de-poner-camaras": "camera-05.jpg",
    "camaras-de-padel-o-videovigilancia": "camera-05.jpg",
    "cuanto-cuesta-poner-camaras": "camera-02.jpg",
    "inversion-inicial-camaras-180-euros": "camera-02.jpg",
    "es-caro-save-my-play": "camera-06.jpg",
    "es-rentable-poner-camaras": "camera-02.jpg",
    "por-que-no-recomiendo-plan-analytics": "camera-06.jpg",
    "que-pasa-si-cancelo": "camera-02.jpg",
    "como-montar-camara-save-my-play": "camera-04.jpg",
    "problemas-con-las-camaras": "camera-04.jpg",
    "camaras-en-exterior-lluvia-nieve-viento": "camera-06.jpg",
    "como-ver-highlights-sin-app": "camera-08.jpg",
    "mejores-empresas-camaras-padel-espana": "camera-03.jpg",
    "por-que-no-conocia-save-my-play": "camera-01.jpg",
    "save-my-play-en-pocas-palabras": "camera-07.jpg",
    "por-que-coolpadel-colabora-con-save-my-play": "camera-03.jpg",
    "he-comprado-camaras-que-pasa-ahora": "camera-02.jpg",
    "por-que-no-me-interesa-venderte-una-camara": "camera-02.jpg",
}


ARTICLE_SPECS = [
    ("por-donde-empezar-si-estoy-pensando-en-poner-camaras", "Estoy pensando poner cámaras en mi club, ¿por dónde empiezo?", 83, 87),
    ("errores-clubs-se-arrepienten-de-poner-camaras", "Los 3 errores de los clubs que se arrepienten de poner cámaras", 26, 59),
    ("camaras-de-padel-o-videovigilancia", "¿Cómo saber si mis cámaras son de pádel o de videovigilancia?", 64, 65),
    ("cuanto-cuesta-poner-camaras", "¿Cuánto cuesta poner cámaras en mi club?", 89, 95),
    ("inversion-inicial-camaras-180-euros", "¿Por qué hay una inversión inicial de 180 € por las cámaras?", 18, 24),
    ("es-caro-save-my-play", "¿Es caro Save My Play?", 67, 68),
    ("es-rentable-poner-camaras", "¿Es rentable poner cámaras en mis pistas?", 78, 82),
    ("por-que-no-recomiendo-plan-analytics", "¿Por qué no recomiendo el plan de 136 € al mes al 95 % de los clubs?", 100, 101),
    ("que-pasa-si-cancelo", "¿Qué pasa si cancelo mi suscripción? ¿Me quedo con las cámaras?", 69, 71),
    ("como-montar-camara-save-my-play", "¿Cuánto se tarda en montar una cámara de Save My Play?", 108, 109),
    ("problemas-con-las-camaras", "¿Qué pasa si hay problemas con las cámaras?", 111, 113),
    ("camaras-en-exterior-lluvia-nieve-viento", "¿Aguantan las cámaras en pistas al exterior?", 114, 115),
    ("como-ver-highlights-sin-app", "¿Por qué no hay app de Save My Play? ¿Cómo veo mis highlights?", 116, 121),
    ("mejores-empresas-camaras-padel-espana", "¿Cuáles son las mejores empresas de cámaras de pádel de España?", 123, 132),
    ("por-que-no-conocia-save-my-play", "¿Por qué no había oído hablar nunca de Save My Play?", 134, 135),
    ("save-my-play-en-pocas-palabras", "Ahora toca hablar de lo buenos que somos en Save My Play", 137, 147),
    ("por-que-coolpadel-colabora-con-save-my-play", "¿Por qué CoolPadel colabora con Save My Play?", 160, 161),
    ("he-comprado-camaras-que-pasa-ahora", "He comprado unas cámaras de Save My Play. ¿Cuál es el proceso ahora?", 72, 75),
    ("por-que-no-me-interesa-venderte-una-camara", "¿Por qué no me interesa venderte una cámara si no estás convencido?", 88, 88),
]


def clean_title(title: str) -> str:
    return title.replace("pistas?", "pistas?").replace("padel", "pádel")


def clean_body(text: str) -> str:
    replacements = {
        "padel": "pádel",
        "Pádel": "Pádel",
        "Cúanto": "Cuánto",
        "por donde": "por dónde",
        "mas formada": "más formada",
        "Esta más que probado": "Está más que probado",
        "que servicios": "qué servicios",
        "las demás clubs": "los demás clubs",
        "2 horas": "2 horas",
        "Youtube": "YouTube",
        "5 mins": "5 minutos",
        "4 semanas aprox.": "4 semanas aproximadamente",
        "a pérdidas. Este": "a pérdidas. Este",
        "precios.Es": "precios. Es",
        "una cámara buena": "una cámara buena",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"\bA que suena chula", "¿A que suena chula", text)
    text = text.replace("?", "?")
    return text.strip()


def load_articles() -> list[dict]:
    paragraphs = [p.text.strip() for p in Document(DOCX).paragraphs]
    articles = []
    for slug, title, start, end in ARTICLE_SPECS:
        chunks = [clean_body(p) for p in paragraphs[start : end + 1] if p.strip()]
        if chunks:
            title_prefix = title.lstrip("¿¡").rstrip("?").strip()
            if chunks[0].startswith(title_prefix):
                chunks[0] = chunks[0][len(title_prefix):].lstrip(" ?\n")
                if not chunks[0]:
                    chunks.pop(0)
            elif chunks[0].startswith("Preguntas:"):
                chunks[0] = chunks[0].split("\n", 1)[-1].lstrip()
        articles.append({"slug": slug, "title": clean_title(title), "paragraphs": chunks})
    return articles


def inline_links(text: str, current_slug: str) -> str:
    text = text.replace(" xxxx", "").replace(" xxx", "")
    if "Plan A:" in text and "(Link)" in text:
        text = text.replace("(Link)", "[[LINK:por-que-no-recomiendo-plan-analytics|más sobre el plan de 136 €]]")
    elif "Inversión Inicial" in text and "(Link)" in text:
        text = text.replace("(Link)", "[[LINK:inversion-inicial-camaras-180-euros|más sobre la inversión inicial]]")
    text = text.replace("Link a ", "")
    links = {
        "este artículo": ("camaras-de-padel-o-videovigilancia", "¿Cómo saber si mis cámaras son de pádel o de videovigilancia?"),
        "artículo de los 3 errores que cometen los clubs": ("errores-clubs-se-arrepienten-de-poner-camaras", "Los 3 errores de los clubs que se arrepienten de poner cámaras"),
        "clubs que se arrepienten de poner cámaras": ("errores-clubs-se-arrepienten-de-poner-camaras", "Los 3 errores de los clubs que se arrepienten de poner cámaras"),
        "por qué no conoces Save My Play": ("por-que-no-conocia-save-my-play", "¿Por qué no había oído hablar nunca de Save My Play?"),
    }
    for needle, (slug, label) in links.items():
        if slug != current_slug and needle in text:
            text = text.replace(needle, f'[[LINK:{slug}|{label}]]', 1)
    text = html.escape(text, quote=False)
    text = re.sub(r"\[\[LINK:([^|]+)\|([^]]+)\]\]", r'<a href="../\1/">\2</a>', text)
    return text.replace("\n", "<br>\n")


def article_body(article: dict) -> str:
    parts = []
    for paragraph in article["paragraphs"]:
        # Preserve numbered lists and paragraph breaks without adding blog-style cards.
        parts.append(f'<p>{inline_links(paragraph, article["slug"])}</p>')
    return "\n".join(parts)


def header(prefix: str = "../../") -> str:
    return f'''<header class="fixed top-0 left-0 w-full z-50 bg-white/95 backdrop-blur-md border-b border-slate-200/80 shadow-xs w-full"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 sm:h-20 flex items-center justify-between"><a href="{prefix}" class="flex items-center gap-2 group shrink-0" aria-label="CoolPadel Home"><img src="{prefix}assets/images/coolpadel-mascot-hd.png" alt="Mascota CoolPadel" width="44" height="44" class="h-8 sm:h-11 w-auto object-contain group-hover:scale-105 transition" fetchpriority="high"><img src="{prefix}assets/images/coolpadel-typography-hd.png" alt="CoolPadel" width="140" height="28" class="h-5 sm:h-7 w-auto object-contain" fetchpriority="high"></a><div class="flex items-center gap-2 sm:gap-4 lg:gap-6"><a href="{prefix}#llaveros" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">LLAVEROS</a><a href="{prefix}camaras/" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">CÁMARAS</a><a href="{prefix}blog/" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">Blog</a><a href="{prefix}franquicias-padel/" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">Cadenas de clubs</a><div class="relative inline-block text-left"><button type="button" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 border border-slate-200 text-xs font-black text-slate-900 shadow-xs transition cursor-pointer">ES <span aria-hidden="true">⌄</span></button><div class="hidden absolute right-0 mt-2 w-24 bg-white rounded-2xl shadow-lg border border-slate-200 py-1.5 z-50"><a href="/camaras/" class="block text-center px-4 py-2 text-xs">ES</a><a href="/en/camaras/" class="block text-center px-4 py-2 text-xs">EN</a><a href="/fr/camaras/" class="block text-center px-4 py-2 text-xs">FR</a><a href="/it/camaras/" class="block text-center px-4 py-2 text-xs">IT</a></div></div><a href="{prefix}#contacto" class="inline-flex items-center gap-1.5 px-3.5 sm:px-4 py-1.5 sm:py-2 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition shadow-sm hover:scale-105 active:scale-95 cursor-pointer">Contactar <span aria-hidden="true">↓</span></a><a href="{prefix}" class="group py-1 inline-flex items-center shrink-0 pl-1" aria-label="CoolPadel Eyes"><img src="{prefix}assets/images/eyes-thumb.png?v=fixed_eyes" alt="CoolPadel Eyes" width="28" height="28" style="height:26px;max-height:26px;width:auto" class="object-contain group-hover:scale-110 transition duration-300"></a></div></div></header><div class="h-16 sm:h-20 w-full shrink-0" aria-hidden="true"></div>'''


CSS = """
* { box-sizing: border-box; }
body { margin: 0; background: #fff; color: #0f172a; font-family: Arial, sans-serif; line-height: 1.7; }
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
main { max-width: 1050px; margin: 0 auto; padding: 54px 20px 90px; }
h1, h2, h3 { line-height: 1.15; letter-spacing: -.03em; }
h1 { max-width: 820px; font-size: clamp(34px, 5vw, 62px); margin: 0 0 22px; }
h2 { font-size: clamp(28px, 4vw, 42px); margin: 0 0 16px; }
h3 { font-size: 24px; margin: 0 0 12px; }
.intro { max-width: 720px; color: #475569; font-size: 19px; }
.article-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; margin-top: 34px; }
.article-card { display: block; padding: 22px; min-height: 150px; color: #0f172a; text-decoration: none; border: 1px solid #cbd5e1; border-radius: 14px; transition: .2s ease; }
.article-card img { display: block; width: 100%; height: 125px; object-fit: cover; border-radius: 10px; margin: -2px 0 16px; }
.article-card:hover { border-color: #f2920b; transform: translateY(-2px); }
.article-card span { display: block; margin-top: 12px; color: #f2920b; font-size: 13px; font-weight: 700; }
.article { max-width: 760px; margin: 0 auto; }
.article p { margin: 0 0 24px; font-size: 18px; line-height: 1.78; }
.article a { color: #3478a6; font-weight: 700; text-decoration: underline; text-underline-offset: 3px; }
.article-hero { display: block; width: 100%; max-height: 230px; object-fit: cover; border-radius: 14px; margin: 0 auto 28px; border: 1px solid #e2e8f0; }
.next-step { margin: 44px 0 42px; padding-top: 26px; border-top: 2px solid #f2920b; }
.next-step p { margin: 8px 0; }
.calendly-inline-widget { min-width: 320px; height: 680px; margin-top: 22px; border-radius: 16px; overflow: hidden; border: 1px solid #e2e8f0; }
.related { margin-top: 42px; }
.related-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px; }
.related a { display: block; padding: 16px; color: #0f172a; text-decoration: none; border: 1px solid #cbd5e1; border-radius: 12px; font-weight: 700; }
.related a:hover { border-color: #f2920b; }
@media (max-width: 900px) { .official-nav > a:not(.nav-contact), .lang-links { display: none; } }
@media (max-width: 760px) { .logo-wordmark { height: 22px; } .logo-mascot { height: 34px; } .article-grid, .related-grid { grid-template-columns: 1fr; } main { padding-top: 36px; } .article p { font-size: 17px; } .calendly-inline-widget { height: 640px; } }
"""

HUB_CSS = """
.intro { max-width: 760px; color: #334155; font-size: 19px; line-height: 1.75; }
.hub-logo { width: 140px; height: auto; margin: 0 0 22px; }
.article-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; margin: 34px 0 0; }
.article-card { display: block; padding: 22px; min-height: 150px; color: #0f172a; text-decoration: none; border: 1px solid #cbd5e1; border-radius: 14px; transition: .2s ease; }
.article-card img { display: block; width: 100%; height: 125px; object-fit: cover; border-radius: 10px; margin: -2px 0 16px; }
.article-card:hover { border-color: #f2920b; transform: translateY(-2px); }
.article-card h3 { margin: 0; }
.article-card span { display: block; margin-top: 12px; color: #f2920b; font-size: 13px; font-weight: 700; }
.next-step { margin: 44px 0 42px; padding-top: 26px; border-top: 2px solid #f2920b; }
.next-step p { margin: 8px 0; }
.calendly-inline-widget { min-width: 320px; height: 680px; margin-top: 22px; border-radius: 16px; overflow: hidden; border: 1px solid #e2e8f0; }
@media (max-width: 760px) { .article-grid { grid-template-columns: 1fr; } }
"""


def page(title: str, content: str, prefix: str = "../../") -> str:
    return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{html.escape(title)} | CoolPadel</title><meta name="description" content="{html.escape(title)}"><script src="https://cdn.tailwindcss.com"></script><link rel="preconnect" href="https://assets.calendly.com"><style>{CSS}</style></head><body>{header(prefix)}{content}<script src="https://assets.calendly.com/assets/external/widget.js" async></script></body></html>'''


def build(articles: list[dict]) -> None:
    ARTICLES.mkdir(parents=True, exist_ok=True)
    cards = "\n".join(f'<a class="article-card" href="articulos/{a["slug"]}/"><img src="../assets/images/camaras/{ARTICLE_IMAGES[a["slug"]]}" alt="{html.escape(a["title"])}" loading="lazy"><h3>{html.escape(a["title"])}</h3><span>Leer artículo →</span></a>' for a in articles)
    intro = '''<p>Si estás pensando en poner cámaras, aquí tienes información directa para entender el sistema, comparar opciones y decidir con calma. He reunido las preguntas que más me hacen los clubs y lo que he aprendido hablando con ellos.</p><p>Sabemos que queréis tomar la mejor decisión sobre las cámaras.<br>La experiencia nos dice que los clubs agradecen tener información útil a su disposición.<br>Y que si no tenéis interés en informaros, no merece la pena hacer la demo online.</p><p>Por eso, hemos tratado de ser lo más sinceros y transparentes posible.<br>Aquí está todo lo que tenéis que saber por nuestra parte, no solo los precios.</p><p>Por el camino os iréis dando cuenta de si es buena idea poner cámaras o no.<br>Y si queréis ponerlas de Save My Play o de otra empresa.<br>Sea cual sea la decisión, será mejor para vosotros y para nosotros.</p><p>En caso de hacer la demo, tendréis mejores preguntas y los dos aprovecharemos mejor el tiempo.</p>'''
    hub = f'''<main><img class="hub-logo" src="../assets/images/save-my-play-logo.jpg" alt="Save My Play"><h1>Cámaras para clubs de pádel</h1><div class="intro">{intro}</div><section><h2>Artículos sobre cámaras</h2><div class="article-grid">{cards}</div></section><section class="next-step"><h2>Siguiente paso</h2><p>Si todavía no lo ves claro, te dejo abajo más artículos sobre cámaras que te ayudarán.</p><p>Si tienes alguna pregunta y quieres que te enseñe bien cómo funciona todo, busca tu hueco para la demo.</p><div class="calendly-inline-widget" data-url="{CALENDLY}&hide_landing_page_details=1&hide_gdpr_banner=1"></div></section></main>'''
    # Keep the existing page head, analytics, and Calendly assets, replacing only its main content.
    source = (CAMERAS / "index.html").read_text(encoding="utf-8")
    hub_style = f"<style>/* Camera article hub */{HUB_CSS}</style>"
    if "/* Camera article hub */" in source:
        source = re.sub(r"<style>/\* Camera article hub \*/.*?</style>", hub_style, source, count=1, flags=re.S)
    else:
        source = source.replace("</head>", hub_style + "\n</head>", 1)
    source = re.sub(r"<main>.*?</main>", hub, source, count=1, flags=re.S)
    source = re.sub(r"<header\b.*?</header>", "", source, count=1, flags=re.S)
    source = re.sub(r'<div class="header-spacer"[^>]*></div>', "", source)
    source = source.replace("<body>", f"<body>{header('../')}", 1)
    if "assets/external/widget.js" not in source:
        source = source.replace("</body>", '<script src="https://assets.calendly.com/assets/external/widget.js" async></script></body>', 1)
    (CAMERAS / "index.html").write_text(source, encoding="utf-8")

    for index, article in enumerate(articles):
        related = [articles[(index + offset) % len(articles)] for offset in (1, 2, 3)]
        related_html = "\n".join(f'<a href="../{a["slug"]}/">{html.escape(a["title"])}</a>' for a in related)
        image_name = ARTICLE_IMAGES[article["slug"]]
        content = f'''<main><article class="article"><h1>{html.escape(article["title"])}</h1><img class="article-hero" src="../../../assets/images/camaras/{image_name}" alt="{html.escape(article["title"])}" loading="lazy">{article_body(article)}<section class="next-step"><h2>Siguiente paso</h2><p>Si todavía no lo ves claro, te dejo abajo más artículos sobre cámaras que te ayudarán.</p><p>Si tienes alguna pregunta y quieres que te enseñe bien cómo funciona todo, busca tu hueco para la demo.</p><div class="calendly-inline-widget" data-url="{CALENDLY}&hide_landing_page_details=1&hide_gdpr_banner=1"></div></section><section class="related"><h2>Más artículos sobre cámaras</h2><div class="related-grid">{related_html}</div></section></article></main>'''
        out = ARTICLES / article["slug"]
        out.mkdir(parents=True, exist_ok=True)
        (out / "index.html").write_text(page(article["title"], content), encoding="utf-8")


if __name__ == "__main__":
    build(load_articles())
