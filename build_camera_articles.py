"""Build the simple camera article hub from Javier's source DOCX."""

from __future__ import annotations

import html
import re
from pathlib import Path

from docx import Document


ROOT = Path(__file__).resolve().parent
DOCX = Path(r"C:\Users\javie\OneDrive\Documentos\Impresión 3D\Palas definitivo\Clubs\Contacto clubs\CoolPadel Branding\Save My Play They ask, you answer.docx")
CAMERAS = ROOT / "camaras"
ARTICLES = CAMERAS / "articulos"
CALENDLY = "https://calendly.com/javier-vs-312/demo-save-my-play?locale=es"
ASSET_DIR = ROOT / "assets" / "images" / "camaras"

ARTICLE_IMAGES = {
    "por-donde-empezar-si-estoy-pensando-en-poner-camaras": "pista-indoor-passion-padel.png",
    "errores-clubs-se-arrepienten-de-poner-camaras": "portada-bandido-highlight.jpg",
    "camaras-de-padel-o-videovigilancia": "camera-05.jpg",
    "cuanto-cuesta-poner-camaras": "pista-moqueta-negra-indoor.png",
    "inversion-inicial-camaras-180-euros": "camera-02.jpg",
    "es-caro-save-my-play": "camera-06.jpg",
    "es-rentable-poner-camaras": "partido-directo-patrocinador-harbor.png",
    "por-que-no-recomiendo-plan-analytics": "portada-mapa-calor-analytics.png",
    "que-pasa-si-cancelo": "portada-mascota-savemyplay.png",
    "como-montar-camara-save-my-play": "camara-instalada-reja-4m-crop.jpg",
    "problemas-con-las-camaras": "camera-04.jpg",
    "camaras-en-exterior-lluvia-nieve-viento": "pista-outdoor-world-sports.png",
    "que-son-las-coaching-tools": "portada-coaching-tools-tablet.png",
    "como-ver-highlights-sin-app": "portada-email-highlights.png",
    "mejores-empresas-camaras-padel-espana": "camera-03.jpg",
    "por-que-no-conocia-save-my-play": "save-email-clip-sportime.png",
    "save-my-play-en-pocas-palabras": "retransmision-usta-national-campus.png",
    "por-que-coolpadel-colabora-con-save-my-play": "portada-coolpadel-savemyplay.jpg",
    "he-comprado-camaras-que-pasa-ahora": "pista-indoor-blue-zone-clean.png",
    "por-que-no-me-interesa-venderte-una-camara": "retransmision-directo-marcador-youtube.png",
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
    ("que-son-las-coaching-tools", "¿Qué son las coaching tools?", 103, 103),
    ("camaras-en-exterior-lluvia-nieve-viento", "¿Aguantan las cámaras en pistas al exterior?", 114, 115),
    ("como-ver-highlights-sin-app", "¿Por qué no hay app de Save My Play? ¿Cómo veo mis highlights?", 116, 121),
    ("mejores-empresas-camaras-padel-espana", "¿Cuáles son las mejores empresas de cámaras de pádel de España?", 123, 132),
    ("por-que-no-conocia-save-my-play", "¿Por qué no había oído hablar nunca de Save My Play?", 134, 135),
    ("save-my-play-en-pocas-palabras", "Ahora toca hablar de lo buenos que somos en Save My Play", 137, 147),
    ("por-que-coolpadel-colabora-con-save-my-play", "¿Por qué CoolPadel colabora con Save My Play?", 160, 161),
    ("he-comprado-camaras-que-pasa-ahora", "He comprado unas cámaras de Save My Play. ¿Cuál es el proceso ahora?", 72, 75),
    ("por-que-no-me-interesa-venderte-una-camara", "¿Por qué no me interesa venderte una cámara si no estás convencido?", 88, 88),
]


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
        "Youtube": "YouTube",
        "5 mins": "5 minutos",
        "4 semanas aprox.": "4 semanas aproximadamente",
        "precios.Es": "precios. Es",
        "en su pistas": "en sus pistas",
        "Muchos clubs se arrepienten": "Algunos clubs se arrepienten",
        # Correcciones gramaticales y erratas
        "tienes que pensas": "tienes que pensar",
        "tiene que pensas": "tienes que pensar",
        "Si no no merece": "Si no, no merece",
        "Aún así no llegamos": "Aún así, no llegamos",
        "Sí has leído": "Si has leído",
        "Aquí esta la respuesta": "Aquí está la respuesta",
        "habitual. retransmisión": "habitual. Retransmisión",
        "En X pistas en España": "En varios clubs de España",
        "En X pistas": "En varios clubs",
        "artículo xxx. las cámaras de padel las fabricamos": "artículo sobre esto. Las cámaras de pádel las fabricamos",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"\bA que suena chula", "¿A que suena chula", text)
    return text.strip()


def load_articles() -> list[dict]:
    """Load articles from DOCX preserving natural paragraphs (blocks)."""
    raw_paragraphs = [p.text for p in Document(DOCX).paragraphs]
    articles = []

    for slug, title, start, end in ARTICLE_SPECS:
        # Reconstruct the section's text with paragraph breaks
        full_text = "\n\n".join(raw_paragraphs[i] for i in range(start, end + 1))
        # Split into real paragraph blocks (separated by empty lines or multiple newlines)
        raw_blocks = [b.strip() for b in re.split(r"\n\s*\n+", full_text) if b.strip()]

        # Strip leading question / title lines from the first block(s)
        while raw_blocks:
            first = raw_blocks[0]
            lines = [l.strip() for l in first.split("\n") if l.strip()]
            new_lines = []
            dropping = True
            for l in lines:
                if dropping and (
                    l == "Preguntas:"
                    or l.endswith("?")
                    or "Los 3 errores" in l
                    or "Ahora toca hablar" in l
                    or "He comprado unas" in l
                ):
                    continue
                else:
                    dropping = False
                    new_lines.append(l)
            if new_lines:
                raw_blocks[0] = "\n".join(new_lines)
                break
            else:
                raw_blocks.pop(0)

        # Coaching tools placeholder if empty in DOCX
        if slug == "que-son-las-coaching-tools" and not raw_blocks:
            raw_blocks = [
                "Próximamente explicaremos al detalle cómo funcionan las coaching tools en pista."
            ]

        # Clean each block
        blocks = [clean_body(b) for b in raw_blocks if b.strip()]
        articles.append({"slug": slug, "title": title, "blocks": blocks})

    return articles


def split_into_sentences(text: str) -> list[str]:
    """Split a paragraph block into individual sentences (one per line, Highlights style)."""
    text = text.strip()
    if not text:
        return []
    # If the text has explicit internal newlines, process line by line
    if "\n" in text:
        result = []
        for line in text.split("\n"):
            line = line.strip()
            if line:
                result.extend(split_into_sentences(line))
        return result
    # Keep numbered list items whole
    if re.match(r"^\d+[ºoa\.]", text):
        return [text]
    # Keep section headers whole
    if re.match(r"^(?:Error \d+:|ERROR EXTRA:|Conclusi[oó]n:|Plan [A-Z]:|Padmi:|Aiball:|Rackety:|Inversi[oó]n Inicial)", text, re.IGNORECASE):
        return [text]
    # Split on sentence-ending punctuation followed by space + uppercase/inverted punct
    parts = re.split(r"(?<=[.?!])\s+(?=[A-ZÁÉÍÓÚÜÑ¿¡\"])", text)
    return [p.strip() for p in parts if p.strip()]


def inline_links(text: str, current_slug: str) -> str:
    text = text.replace(" xxxx", "").replace(" xxx", "")
    if "Plan A:" in text and "(Link)" in text:
        text = text.replace(
            "(Link)",
            "[[LINK:por-que-no-recomiendo-plan-analytics|¿Por qué no recomiendo el plan de 136 € al mes al 95 % de los clubs?]]",
        )
    elif "Inversión Inicial" in text and "(Link)" in text:
        text = text.replace(
            "(Link)",
            "[[LINK:inversion-inicial-camaras-180-euros|¿Por qué hay una inversión inicial de 180 € por las cámaras?]]",
        )
    text = text.replace("Link a ", "")
    links = {
        "este artículo": ("camaras-de-padel-o-videovigilancia", "¿Cómo saber si mis cámaras son de pádel o de videovigilancia?"),
        "artículo de los 3 errores que cometen los clubs": ("errores-clubs-se-arrepienten-de-poner-camaras", "Los 3 errores de los clubs que se arrepienten de poner cámaras"),
        "clubs que se arrepienten de poner cámaras": ("errores-clubs-se-arrepienten-de-poner-camaras", "Los 3 errores de los clubs que se arrepienten de poner cámaras"),
        "por qué no conoces Save My Play": ("por-que-no-conocia-save-my-play", "¿Por qué no había oído hablar nunca de Save My Play?"),
        "cámaras de pádel o de videovigilancia": ("camaras-de-padel-o-videovigilancia", "¿Cómo saber si mis cámaras son de pádel o de videovigilancia?"),
        "los 3 errores que cometen los clubs": ("errores-clubs-se-arrepienten-de-poner-camaras", "Los 3 errores de los clubs que se arrepienten de poner cámaras"),
    }
    for needle, (slug, label) in links.items():
        if slug != current_slug and needle in text:
            text = text.replace(needle, f"[[LINK:{slug}|{label}]]", 1)
    text = html.escape(text, quote=False)
    text = re.sub(r"\[\[LINK:([^|]+)\|([^]]+)\]\]", r'<a href="../\1/">\2</a>', text)
    return text


HEADER_PATTERNS = [
    re.compile(r"^(Error \d+:)\s*(.*)$", re.IGNORECASE),
    re.compile(r"^(ERROR EXTRA:)\s*(.*)$", re.IGNORECASE),
    re.compile(r"^(Conclusi[oó]n:)\s*(.*)$", re.IGNORECASE),
    re.compile(r"^(Plan [A-Z]:)\s*(.*)$", re.IGNORECASE),
    re.compile(r"^(Padmi:)\s*(.*)$", re.IGNORECASE),
    re.compile(r"^(Aiball:)\s*(.*)$", re.IGNORECASE),
    re.compile(r"^(Rackety:)\s*(.*)$", re.IGNORECASE),
    re.compile(r"^(Inversi[oó]n Inicial[^:]*:)\s*(.*)$", re.IGNORECASE),
]

LIST_PATTERN = re.compile(r"^(\d+[ºoa\.]\s*)(.*)$")


def format_sentence_item(raw: str, slug: str) -> str:
    """Format a single item: header (h3 styled), numbered list item, or standard sentence p."""
    # Check if it's a section header (e.g. Error 1:, Conclusión:, etc.)
    for pat in HEADER_PATTERNS:
        m = pat.match(raw)
        if m:
            label = m.group(1).strip()
            rest = m.group(2).strip()
            out = f'<h3 class="article-subheading"><span class="subheading-title">{html.escape(label)}</span></h3>'
            if rest:
                out += f'\n<p>{inline_links(rest, slug)}</p>'
            return out

    # Check if it's a numbered list item (1º, 2º, 1., etc.)
    m_list = LIST_PATTERN.match(raw)
    if m_list:
        num = m_list.group(1).strip()
        rest = m_list.group(2).strip()
        return f'<p class="list-item-line"><strong class="list-badge">{html.escape(num)}</strong> {inline_links(rest, slug)}</p>'

    # Standard sentence
    return f'<p>{inline_links(raw, slug)}</p>'


def article_body(article: dict) -> str:
    """Render article body preserving paragraph block separations (Highlights style)."""
    rendered_blocks = []
    slug = article["slug"]

    for block in article["blocks"]:
        sentences = split_into_sentences(block)
        if not sentences:
            continue
        items_html = [format_sentence_item(s, slug) for s in sentences]
        block_html = "\n".join(items_html)
        rendered_blocks.append(f'<div class="article-block">\n{block_html}\n</div>')

    return "\n".join(rendered_blocks)


def header(prefix: str = "../../") -> str:
    return f'''<header class="fixed top-0 left-0 w-full z-50 bg-white/95 backdrop-blur-md border-b border-slate-200/80 shadow-xs w-full"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 sm:h-20 flex items-center justify-between"><a href="{prefix}" class="flex items-center gap-2 group shrink-0" aria-label="CoolPadel Home"><img src="{prefix}assets/images/coolpadel-mascot-hd.png" alt="Mascota CoolPadel" width="44" height="44" class="h-8 sm:h-11 w-auto object-contain group-hover:scale-105 transition" fetchpriority="high"><img src="{prefix}assets/images/coolpadel-typography-hd.png" alt="CoolPadel" width="140" height="28" class="h-5 sm:h-7 w-auto object-contain" fetchpriority="high"></a><div class="flex items-center gap-2 sm:gap-4 lg:gap-6"><a href="{prefix}llaveros-padel-personalizados/" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">LLAVEROS</a><a href="{prefix}camaras/" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">CÁMARAS</a><a href="{prefix}blog/" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">Blog</a><a href="{prefix}franquicias-padel/" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">Cadenas de clubs</a><div class="relative inline-block text-left" id="lang-dropdown-container"><button type="button" onclick="toggleLangDropdown(event)" id="lang-dropdown-btn" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 border border-slate-200 text-xs font-black text-slate-900 shadow-xs transition cursor-pointer" aria-expanded="false" aria-haspopup="true"><span id="current-lang-code" class="uppercase font-black">ES</span><i data-lucide="chevron-down" class="w-3.5 h-3.5 stroke-[2.5] text-slate-600 transition-transform duration-200" id="lang-dropdown-arrow"></i></button><div id="lang-dropdown-menu" class="hidden absolute right-0 mt-2 w-24 bg-white rounded-2xl shadow-[0_12px_30px_rgba(0,0,0,0.15)] border border-slate-200 py-1.5 z-50 transition-all overflow-hidden"><a href="/camaras/" class="block text-center px-4 py-2 text-xs">ES</a><a href="/en/camaras/" class="block text-center px-4 py-2 text-xs">EN</a><a href="/fr/camaras/" class="block text-center px-4 py-2 text-xs">FR</a><a href="/it/camaras/" class="block text-center px-4 py-2 text-xs">IT</a><a href="/de/camaras/" class="block text-center px-4 py-2 text-xs">DE</a></div></div><a href="{prefix}#contacto" class="inline-flex items-center gap-1.5 px-3.5 sm:px-4 py-1.5 sm:py-2 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition shadow-sm hover:scale-105 active:scale-95 cursor-pointer"><span>Contactar</span><i data-lucide="arrow-down" class="w-3 h-3 stroke-[3]"></i></a><a href="{prefix}" class="group py-1 inline-flex items-center shrink-0 pl-1" aria-label="CoolPadel Eyes"><img src="{prefix}assets/images/eyes-thumb.png?v=fixed_eyes" alt="CoolPadel Eyes" width="28" height="28" style="height:26px;max-height:26px;width:auto" class="object-contain group-hover:scale-110 transition duration-300"></a></div></div></header><div class="h-16 sm:h-20 w-full shrink-0" aria-hidden="true"></div>'''


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
main { max-width: 1700px; margin: 0 auto; padding: 54px 20px 90px; }
h1, h2, h3, .font-heading { font-family: 'Outfit', Arial, sans-serif; line-height: 1.15; letter-spacing: -.03em; }
h1 { max-width: 900px; font-size: clamp(34px, 5vw, 62px); margin: 0 0 34px; font-weight: 900; color: #0f172a; }
.article h1 { padding: 0 0 34px; margin-bottom: 0; font-size: clamp(38px, 5vw, 64px); font-weight: 900; line-height: 1.08; }
h2 { font-size: clamp(28px, 4vw, 42px); margin: 0 0 16px; }
h3 { font-size: 24px; margin: 0 0 12px; }
.intro { max-width: 720px; color: #475569; font-size: 19px; }
.article { max-width: 760px; margin: 0 auto; }

/* Article body and paragraph block spacing */
.article-block { margin: 0 0 28px; }
.article p { margin: 0 0 6px; font-size: 18px; line-height: 1.75; }
.article a { color: #3478a6; font-weight: 700; text-decoration: underline; text-underline-offset: 3px; }

/* Subheadings (Error 1, Plan A, Conclusión, etc.) */
.article-subheading {
  margin: 36px 0 14px;
  font-size: clamp(22px, 3vw, 28px);
  font-weight: 900;
  color: #0f172a;
  letter-spacing: -0.02em;
}
.article-subheading .subheading-title {
  display: inline-block;
  border-bottom: 3px solid #f2920b;
  padding-bottom: 4px;
}

/* Numbered list items */
.list-item-line { margin: 8px 0; font-size: 18px; }
.list-badge {
  display: inline-block;
  min-width: 28px;
  font-weight: 900;
  color: #f2920b;
}

.article-hero { display: block; width: 100%; max-height: 420px; height: auto; object-fit: contain; object-position: center; background: #f8fafc; border-radius: 14px; margin: 0 auto 32px; border: 1px solid #e2e8f0; }

/* Next step section — clean white background with subtle border */
.next-step {
  margin: 54px 0 48px;
  padding: 32px 34px 34px;
  border: 1px solid #e2e8f0;
  border-radius: 20px;
  background: #ffffff;
  box-shadow: 0 10px 30px rgba(15,23,42,.04);
}
.next-step h2 {
  color: #0f172a;
  font-size: clamp(28px, 4vw, 36px);
  font-weight: 900;
  margin: 0 0 16px;
  letter-spacing: -0.02em;
}
.next-step p { margin: 8px 0; font-size: 17px; line-height: 1.7; color: #334155; }
.calendly-inline-widget { min-width: 320px; height: 680px; margin-top: 24px; border-radius: 16px; overflow: hidden; border: 1px solid #e2e8f0; }

.video-section { margin: 42px 0; padding: 24px; border-radius: 18px; background: #f8fafc; border: 1px solid #e2e8f0; }
.video-section h2 { font-size: 30px; margin-bottom: 10px; }
.video-embed { display: block; width: 100%; aspect-ratio: 16 / 9; border: 0; border-radius: 12px; margin-top: 18px; background: #0f172a; }

/* Related articles section */
.related { margin-top: 56px; padding-top: 24px; }
.related h2 {
  font-size: clamp(28px, 4vw, 36px);
  font-weight: 900;
  color: #0f172a;
  margin: 0 0 24px;
  letter-spacing: -0.02em;
}
.related-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 18px;
}
.related-card {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 16px;
  background: #ffffff;
  border: 2px solid #e2e8f0;
  border-radius: 16px;
  text-decoration: none;
  transition: all 0.25s ease;
  box-shadow: 0 2px 8px rgba(15,23,42,.03);
}
.related-card:hover {
  border-color: #f2920b;
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(15,23,42,.08);
}
.related-thumb {
  width: 100%;
  aspect-ratio: 16 / 9;
  border-radius: 10px;
  overflow: hidden;
  background: #0f172a;
  margin-bottom: 12px;
}
.related-thumb img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.related-title {
  font-size: 15px;
  font-weight: 800;
  line-height: 1.35;
  color: #0f172a;
  margin: 0;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

@media (max-width: 900px) { .official-nav > a:not(.nav-contact), .lang-links { display: none; } }
@media (max-width: 1050px) { .article-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
@media (max-width: 760px) {
  .logo-wordmark { height: 22px; }
  .logo-mascot { height: 34px; }
  .article-grid, .related-grid { grid-template-columns: 1fr; }
  main { padding-top: 36px; }
  .article p { font-size: 17px; }
  .article-hero { max-height: none; }
  .calendly-inline-widget { height: 640px; }
  .next-step { padding: 22px 20px; }
}
"""

HUB_CSS = """
.hub-hero { max-width: 1200px; margin: 30px auto 54px; text-align: center; }
.hub-eyebrow { margin: 0 0 14px; color: #f2920b; font-size: 13px; font-weight: 900; letter-spacing: .04em; text-transform: uppercase; }
.hub-title { max-width: none !important; margin: 0 0 16px !important; font-size: clamp(42px, 3.5vw, 58px) !important; font-weight: 900 !important; line-height: 1.05 !important; color: #0f172a !important; white-space: nowrap; text-transform: uppercase; letter-spacing: -.04em; }
.intro { max-width: 760px; margin: 0 auto; color: #334155; font-size: 19px; line-height: 1.55; }
.intro p { margin: 0 0 14px; }
.article-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 18px; margin: 34px 0 0; }
.article-card { color: #0f172a; text-decoration: none; }
.article-card img { display: block; }
.card-action:active { background: #76d3f6; transform: scale(.98); }
.next-step { margin: 54px 0 48px; padding: 32px 34px 34px; border: 1px solid #e2e8f0; border-radius: 20px; background: #ffffff; box-shadow: 0 10px 30px rgba(15,23,42,.04); }
.next-step h2 { color: #0f172a; font-size: clamp(28px, 4vw, 36px); font-weight: 900; margin: 0 0 16px; letter-spacing: -0.02em; }
.next-step p { margin: 8px 0; font-size: 17px; line-height: 1.7; color: #334155; }
.calendly-inline-widget { min-width: 320px; height: 680px; margin-top: 24px; border-radius: 16px; overflow: hidden; border: 1px solid #e2e8f0; }
@media (max-width: 1050px) { .article-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
@media (max-width: 760px) { .hub-hero { margin: 18px auto 38px; text-align: left; } .hub-title { white-space: normal; } .intro { margin: 0; } .article-grid { grid-template-columns: 1fr; } }
"""


def page(title: str, content: str, prefix: str = "../../", extra_css: str = "") -> str:
    return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{html.escape(title)} | CoolPadel</title><meta name="description" content="{html.escape(title)}"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Outfit:wght@600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"><script src="https://cdn.tailwindcss.com"></script><script src="https://unpkg.com/lucide@0.468.0/dist/umd/lucide.min.js"></script><link rel="preconnect" href="https://assets.calendly.com"><style>{CSS}{extra_css}</style></head><body>{header(prefix)}{content}<script>if (window.lucide) lucide.createIcons();</script><script src="https://assets.calendly.com/assets/external/widget.js" async></script><script src="{prefix}assets/js/cp-analytics.js" defer></script></body></html>'''


def build(articles: list[dict]) -> None:
    ARTICLES.mkdir(parents=True, exist_ok=True)
    cards = "\n".join(
        f'''<a href="articulos/{a["slug"]}/" class="article-card bg-white border-2 border-slate-200/90 hover:border-[#f2920b] rounded-2xl p-4 sm:p-5 shadow-2xs hover:shadow-lg transition-all duration-300 flex flex-col justify-between group hover:-translate-y-0.5 cursor-pointer block"><div class="space-y-3"><div class="aspect-[16/9] rounded-xl overflow-hidden bg-slate-900 border border-slate-200/90 shadow-sm relative"><img src="../assets/images/camaras/{ARTICLE_IMAGES[a["slug"]]}" alt="{html.escape(a["title"])}" width="800" height="450" class="w-full h-full object-cover group-hover:scale-105 transition duration-500" loading="lazy" decoding="async"></div><div><h3 class="font-sans font-extrabold text-sm sm:text-base lg:text-lg text-slate-900 leading-snug tracking-tight transition-colors">{html.escape(a["title"])}</h3></div></div><div class="pt-3.5 border-t border-slate-100 mt-4"><div class="card-action group relative w-full inline-flex items-center justify-center gap-2 px-4 py-2.5 rounded-full bg-[#f2920b] group-hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition-all duration-300 shadow-xs group-hover:shadow-md group-hover:scale-[1.01] overflow-hidden active:scale-[.98]"><span class="font-black">Leer artículo</span><div class="w-4 h-4 rounded-full bg-slate-950/10 group-hover:bg-slate-950 group-hover:text-white flex items-center justify-center transition-all duration-300"><i data-lucide="arrow-right" class="w-3 h-3 stroke-[3] group-hover:translate-x-0.5 transition-transform duration-300"></i></div></div></div></a>'''
        for a in articles
    )
    intro = """<p>Sabemos que queréis tomar la mejor decisión sobre las cámaras.<br>La experiencia nos dice que los clubs agradecen tener información útil a su disposición.<br>Y que si no tenéis interés en informaros, no merece la pena hacer la demo online.</p><p>Por eso, hemos tratado de ser lo más sinceros y transparentes posible.</p><p>Por el camino os iréis dando cuenta de si es buena idea poner cámaras o no.<br>Y si queréis ponerlas de Save My Play o de otra empresa.<br>Sea cual sea la decisión, será mejor para vosotros y para nosotros.</p><p>Así si hacemos la demo, tenéis mejores preguntas y aprovechamos mejor el tiempo.</p>"""
    hub = f"""<main><section class="hub-hero"><p class="hub-eyebrow">Todo lo que necesitas saber antes de poner cámaras</p><h1 class="hub-title">Cámaras para clubs de pádel</h1><div class="intro">{intro}</div></section><section><div class="article-grid">{cards}</div></section><section class="next-step"><h2>Siguiente paso</h2><p>Si todavía no lo ves claro, te dejo arriba más artículos sobre cámaras que te ayudarán.</p><p>Si tienes alguna pregunta y quieres que te enseñe bien cómo funciona todo, busca tu hueco para la demo.</p><div class="calendly-inline-widget" data-url="{CALENDLY}&hide_landing_page_details=1&hide_gdpr_banner=1"></div></section></main>"""
    # Generate the hub
    (CAMERAS / "index.html").write_text(page("Cámaras para clubs de pádel", hub, prefix="../", extra_css=HUB_CSS), encoding="utf-8")

    for index, article in enumerate(articles):
        related = [articles[(index + offset) % len(articles)] for offset in (1, 2, 3)]
        related_html = "\n".join(
            f'''<a href="../{a["slug"]}/" class="related-card"><div class="related-thumb"><img src="../../../assets/images/camaras/{ARTICLE_IMAGES[a["slug"]]}" alt="{html.escape(a["title"])}" loading="lazy"></div><p class="related-title">{html.escape(a["title"])}</p></a>'''
            for a in related
        )
        image_name = ARTICLE_IMAGES[article["slug"]]
        article_videos = {
            "como-ver-highlights-sin-app": (
                "Cómo guardar los highlights en pista",
                "Levanta los brazos mirando a la cámara o pulsa el botón verde para guardar tu mejor punto al instante.",
                "https://www.youtube-nocookie.com/embed/Z0vnvyrUbPQ",
            ),
            "como-montar-camara-save-my-play": (
                "Lo fácil que es de usar",
                "En apenas 10 minutos y con solo dos botones tienes la cámara grabando partidos, highlights y directos sin complicaciones.",
                "https://www.youtube-nocookie.com/embed/LuzDvB5Umfs",
            ),
            "save-my-play-en-pocas-palabras": (
                "Retransmisión en directo del torneo FIP de Miami",
                "Así se ve una retransmisión en directo oficial con las cámaras de Save My Play en torneos internacionales FIP.",
                "https://www.youtube-nocookie.com/embed/4xwrrveDZxg?start=5623",
            ),
            "que-son-las-coaching-tools": (
                "Herramientas avanzadas de entrenamiento",
                "Con las coaching tools puedes dibujar sobre la repetición usando una tablet, marcar movimientos y grabar la explicación con voz para tus alumnos.",
                "https://www.youtube-nocookie.com/embed/FcnCWaYahP8",
            ),
        }
        video = ""
        if article["slug"] in article_videos:
            v_title, v_desc, v_src = article_videos[article["slug"]]
            video = f'<section class="video-section"><h2>{html.escape(v_title)}</h2><p>{html.escape(v_desc)}</p><iframe class="video-embed" src="{v_src}" title="{html.escape(v_title)}" loading="lazy" allowfullscreen></iframe></section>'
        elif article["slug"] == "por-que-no-recomiendo-plan-analytics":
            video = '<section class="video-section"><h2>Ejemplo en directo de analíticas y estadísticas con IA</h2><p>Puedes ver un informe interactivo real con mapa de calor y análisis de golpeo generado por la IA en este enlace:</p><div style="margin-top:16px"><a href="https://savemyplay.com/replays/634779-ni9DexZC-the-club-at-monroe/analytics" target="_blank" rel="noopener noreferrer" style="display:inline-flex;align-items:center;gap:8px;padding:12px 20px;border-radius:999px;background:#f2920b;color:#0f172a;font-weight:900;text-decoration:none;font-size:14px;box-shadow:0 2px 8px rgba(0,0,0,0.08);">Ver ejemplo en directo en Save My Play &rarr;</a></div></section>'

        content = f"""<main><article class="article"><h1>{html.escape(article["title"])}</h1><img class="article-hero" src="../../../assets/images/camaras/{image_name}" alt="{html.escape(article["title"])}" loading="lazy">{article_body(article)}{video}<section class="related"><h2>Más artículos sobre cámaras</h2><div class="related-grid">{related_html}</div></section><section class="next-step"><h2>Siguiente paso</h2><p>Si todavía no lo ves claro, te dejo arriba más artículos sobre cámaras que te ayudarán.</p><p>Si tienes alguna pregunta y quieres que te enseñe bien cómo funciona todo, busca tu hueco para la demo.</p><div class="calendly-inline-widget" data-url="{CALENDLY}&hide_landing_page_details=1&hide_gdpr_banner=1"></div></section></article></main>"""
        out = ARTICLES / article["slug"]
        out.mkdir(parents=True, exist_ok=True)
        (out / "index.html").write_text(page(article["title"], content, prefix="../../../"), encoding="utf-8")


if __name__ == "__main__":
    build(load_articles())
