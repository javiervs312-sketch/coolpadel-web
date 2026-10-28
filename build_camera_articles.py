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
        "este artículo": ("camaras-de-padel-o-videovigilancia", "este artículo"),
        "artículo de los 3 errores que cometen los clubs": ("errores-clubs-se-arrepienten-de-poner-camaras", "artículo de los 3 errores que cometen los clubs"),
        "clubs que se arrepienten de poner cámaras": ("errores-clubs-se-arrepienten-de-poner-camaras", "clubs que se arrepienten de poner cámaras"),
        "por qué no conoces Save My Play": ("por-que-no-conocia-save-my-play", "por qué no conoces Save My Play"),
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
    return f'''<header class="site-header"><a href="{prefix}" class="brand">CoolPadel</a><nav><a href="{prefix}camaras/">Cámaras</a><a href="{prefix}#contacto">Contactar</a></nav></header>'''


CSS = """
* { box-sizing: border-box; }
body { margin: 0; background: #fff; color: #0f172a; font-family: Arial, sans-serif; line-height: 1.7; }
.site-header { position: sticky; top: 0; z-index: 10; display: flex; justify-content: space-between; align-items: center; padding: 16px max(20px, calc((100% - 1120px)/2)); background: rgba(255,255,255,.96); border-bottom: 1px solid #e2e8f0; }
.site-header a { color: #0f172a; text-decoration: none; font-weight: 700; }
.site-header nav { display: flex; gap: 20px; font-size: 14px; }
.brand { font-size: 20px; letter-spacing: -.03em; }
main { max-width: 1050px; margin: 0 auto; padding: 70px 20px 90px; }
h1, h2, h3 { line-height: 1.15; letter-spacing: -.03em; }
h1 { max-width: 820px; font-size: clamp(34px, 5vw, 62px); margin: 0 0 22px; }
h2 { font-size: clamp(28px, 4vw, 42px); margin: 0 0 16px; }
h3 { font-size: 24px; margin: 0 0 12px; }
.intro { max-width: 720px; color: #475569; font-size: 19px; }
.article-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; margin-top: 34px; }
.article-card { display: block; padding: 22px; min-height: 150px; color: #0f172a; text-decoration: none; border: 1px solid #cbd5e1; border-radius: 14px; transition: .2s ease; }
.article-card:hover { border-color: #f2920b; transform: translateY(-2px); }
.article-card span { display: block; margin-top: 12px; color: #f2920b; font-size: 13px; font-weight: 700; }
.article { max-width: 760px; margin: 0 auto; }
.article p { margin: 0 0 20px; font-size: 18px; }
.article a { color: #3478a6; font-weight: 700; }
.next-step { margin: 44px 0 42px; padding-top: 26px; border-top: 2px solid #f2920b; }
.next-step p { margin: 8px 0; }
.calendly-link { display: inline-block; margin-top: 12px; padding: 12px 18px; border-radius: 999px; background: #f2920b; color: #0f172a !important; text-decoration: none; }
.related { margin-top: 42px; }
.related-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px; }
.related a { display: block; padding: 16px; color: #0f172a; text-decoration: none; border: 1px solid #cbd5e1; border-radius: 12px; font-weight: 700; }
.related a:hover { border-color: #f2920b; }
@media (max-width: 760px) { .article-grid, .related-grid { grid-template-columns: 1fr; } main { padding-top: 44px; } .article p { font-size: 17px; } }
"""

HUB_CSS = """
.intro { max-width: 720px; color: #475569; font-size: 19px; }
.article-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; margin: 34px 0 0; }
.article-card { display: block; padding: 22px; min-height: 150px; color: #0f172a; text-decoration: none; border: 1px solid #cbd5e1; border-radius: 14px; transition: .2s ease; }
.article-card:hover { border-color: #f2920b; transform: translateY(-2px); }
.article-card h3 { margin: 0; }
.article-card span { display: block; margin-top: 12px; color: #f2920b; font-size: 13px; font-weight: 700; }
.next-step { margin: 44px 0 42px; padding-top: 26px; border-top: 2px solid #f2920b; }
.next-step p { margin: 8px 0; }
.calendly-link { display: inline-block; margin-top: 12px; padding: 12px 18px; border-radius: 999px; background: #f2920b; color: #0f172a !important; text-decoration: none; }
@media (max-width: 760px) { .article-grid { grid-template-columns: 1fr; } }
"""


def page(title: str, content: str, prefix: str = "../../") -> str:
    return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{html.escape(title)} | CoolPadel</title><meta name="description" content="{html.escape(title)}"><style>{CSS}</style></head><body>{header(prefix)}{content}</body></html>'''


def build(articles: list[dict]) -> None:
    ARTICLES.mkdir(parents=True, exist_ok=True)
    cards = "\n".join(f'<a class="article-card" href="articulos/{a["slug"]}/"><h3>{html.escape(a["title"])}</h3><span>Leer artículo →</span></a>' for a in articles)
    hub = f'''<main><h1>Cámaras para clubs de pádel</h1><p class="intro">Si estás pensando en poner cámaras, aquí tienes información directa para entender el sistema, comparar opciones y decidir con calma. He reunido las preguntas que más me hacen los clubs y lo que he aprendido hablando con ellos.</p><section><h2>Artículos sobre cámaras</h2><div class="article-grid">{cards}</div></section><section class="next-step"><h2>Siguiente paso</h2><p>Si todavía no lo ves claro, te dejo abajo más artículos sobre cámaras que te ayudarán.</p><p>Si tienes alguna pregunta y quieres que te enseñe bien cómo funciona todo, busca tu hueco para la demo.</p><a class="calendly-link" href="{CALENDLY}" target="_blank" rel="noopener noreferrer">Agendar una demo</a></section></main>'''
    # Keep the existing page head, analytics, and Calendly assets, replacing only its main content.
    source = (CAMERAS / "index.html").read_text(encoding="utf-8")
    if "/* Camera article hub */" not in source:
        source = source.replace("</head>", f"<style>/* Camera article hub */{HUB_CSS}</style>\n</head>", 1)
    source = re.sub(r"<main>.*?</main>", hub, source, count=1, flags=re.S)
    (CAMERAS / "index.html").write_text(source, encoding="utf-8")

    for index, article in enumerate(articles):
        related = [articles[(index + offset) % len(articles)] for offset in (1, 2, 3)]
        related_html = "\n".join(f'<a href="../{a["slug"]}/">{html.escape(a["title"])}</a>' for a in related)
        content = f'''<main><article class="article"><h1>{html.escape(article["title"])}</h1>{article_body(article)}<section class="next-step"><h2>Siguiente paso</h2><p>Si todavía no lo ves claro, te dejo abajo más artículos sobre cámaras que te ayudarán.</p><p>Si tienes alguna pregunta y quieres que te enseñe bien cómo funciona todo, busca tu hueco para la demo.</p><a class="calendly-link" href="{CALENDLY}" target="_blank" rel="noopener noreferrer">Agendar una demo</a></section><section class="related"><h2>Más artículos sobre cámaras</h2><div class="related-grid">{related_html}</div></section></article></main>'''
        out = ARTICLES / article["slug"]
        out.mkdir(parents=True, exist_ok=True)
        (out / "index.html").write_text(page(article["title"], content), encoding="utf-8")


if __name__ == "__main__":
    build(load_articles())
