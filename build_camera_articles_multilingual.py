# -*- coding: utf-8 -*-
"""
Builder unificado multilingüe para el Hub y los 20 artículos de cámaras de Save My Play
en todos los idiomas: ES, FR, EN, IT, DE.

Aplica estrictamente las directrices aprobadas:
1. Textura táctil azul con fondo azul profundo #3478a6, overlay 0.40 y textura_editorial_coolpadel.webp
   con ruta absoluta `/assets/images/branding/textura_editorial_coolpadel.webp`.
2. Texto del banner intro en blanco puro (#ffffff), tamaño uniforme 19px, interlineado amplio y espaciado de 28px.
3. Artículos con espaciado de 56px entre bloques (.article-block) y 12px entre párrafos.
4. Negritas clave preservadas sin saturar y subtítulos semánticos <h2> para SEO/GEO.
5. Recomendaciones rotativas (el siguiente de la lista en primer lugar + 2 variados).
6. Calendly embebido con el parámetro `locale=<lang>` correspondiente.
7. Footer oficial de silos SEO (CoolPadel) integrado para enlazado interno.
8. Cero consumo de tokens en compilaciones recurrentes.
"""

from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
from build_camera_articles import (
    ARTICLE_IMAGES,
    RELATED_MAP,
    format_sentence_item,
    inline_links,
    load_articles,
    split_into_sentences,
)
from build_blog import get_silo_footer_html
from camaras_fr_data import FR_ARTICLES_DATA, FR_VIDEOS
try:
    from camaras_aeo_data import AEO_FAQS_AND_DESCS, HUB_SEO_META
except ImportError:
    AEO_FAQS_AND_DESCS = {}
    HUB_SEO_META = {}

# Cargar diccionarios i18n si existen
try:
    from camaras_i18n_data import CAMARAS_I18N
except ImportError:
    CAMARAS_I18N = {}

ARTICLE_ORDER = [
    "por-donde-empezar-si-estoy-pensando-en-poner-camaras",
    "errores-clubs-se-arrepienten-de-poner-camaras",
    "camaras-de-padel-o-videovigilancia",
    "cuanto-cuesta-poner-camaras",
    "inversion-inicial-camaras-180-euros",
    "es-caro-save-my-play",
    "es-rentable-poner-camaras",
    "por-que-no-recomiendo-plan-analytics",
    "que-pasa-si-cancelo",
    "como-montar-camara-save-my-play",
    "problemas-con-las-camaras",
    "que-son-las-coaching-tools",
    "camaras-en-exterior-lluvia-nieve-viento",
    "como-ver-highlights-sin-app",
    "mejores-empresas-camaras-padel-espana",
    "por-que-no-conocia-save-my-play",
    "save-my-play-en-pocas-palabras",
    "por-que-coolpadel-colabora-con-save-my-play",
    "he-comprado-camaras-que-pasa-ahora",
    "por-que-no-me-interesa-venderte-una-camara",
]

# Textura azul táctil idéntica al blog oficial y al footer
TEXTURE_CSS = """
.intro-full-band {
  width: 100vw;
  position: relative;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
  margin-top: 20px;
  margin-bottom: 2px;
  background-color: #3478a6;
  background-image: linear-gradient(rgba(52, 120, 166, 0.40), rgba(52, 120, 166, 0.40)), url('/assets/images/branding/textura_editorial_coolpadel.webp');
  background-blend-mode: normal, soft-light;
  background-size: cover;
  background-position: center;
  padding: 20px 20px;
  border-top: 1px solid rgba(255, 255, 255, 0.15);
  border-bottom: 1px solid rgba(255, 255, 255, 0.15);
  box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.08);
}
.bg-textured-blue {
  background-color: #3478a6;
  background-image: linear-gradient(rgba(52, 120, 166, 0.40), rgba(52, 120, 166, 0.40)), url('/assets/images/branding/textura_editorial_coolpadel.webp');
  background-blend-mode: normal, soft-light;
  background-size: cover;
  background-position: center;
}
.intro { max-width: 740px; margin: 0 auto; color: #ffffff; font-size: 17px; line-height: 1.55; text-align: center; }
.intro p { margin: 0 0 14px; color: #ffffff !important; font-size: 17px !important; font-weight: 500; }
.intro p:last-child { margin-bottom: 0; }
"""

ARTICLE_CSS = """
:root { --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif; --font-heading: 'Outfit', sans-serif; }
body { margin: 0; font-family: var(--font-sans); color: #0f172a; background: #ffffff; line-height: 1.7; -webkit-font-smoothing: antialiased; }
h1, h2, h3, h4, .font-heading { font-family: var(--font-heading) !important; }
.article-container { max-width: 820px; margin: 0 auto; padding: 48px 20px 80px; }
.article-header { margin-bottom: 32px; }
.back-link { display: inline-flex; align-items: center; gap: 8px; color: #64748b; font-size: 14px; font-weight: 600; text-decoration: none; margin-bottom: 24px; transition: color .2s; }
.back-link:hover { color: #f2920b; }
.article-title { font-family: var(--font-heading); font-size: clamp(30px, 4vw, 44px); font-weight: 900; line-height: 1.15; color: #0f172a; margin: 0 0 24px; letter-spacing: -0.02em; }
.article-hero-img { width: 100%; aspect-ratio: 16/9; object-fit: cover; border-radius: 16px; margin: 0 0 36px; border: 1px solid #e2e8f0; }
.article-body { font-size: 18px; color: #334155; line-height: 1.75; }
.article-body p { margin: 0 0 12px; }
.article-block { margin: 0 0 56px; }
.article-block:last-child { margin-bottom: 0; }
.article-body strong { color: #0f172a; font-weight: 700; }
.article-body a { color: #0284c7; text-decoration: underline; text-underline-offset: 3px; font-weight: 600; }
.article-body a:hover { color: #0369a1; }
.article-subheading {
  font-family: var(--font-heading);
  margin: 32px 0 14px;
  font-size: clamp(21px, 2.8vw, 26px);
  font-weight: 900;
  color: #0f172a;
  letter-spacing: -0.02em;
  line-height: 1.25;
}
.article-subheading:first-child { margin-top: 0; }
.article-subheading .subheading-title {
  display: inline-block;
  border-bottom: 3px solid #f2920b;
  padding-bottom: 4px;
}
.list-item-line { margin: 8px 0; font-size: 18px; }
.list-badge {
  display: inline-block;
  min-width: 28px;
  font-weight: 900;
  color: #f2920b;
}
.video-wrapper { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; border-radius: 16px; margin: 32px 0; border: 1px solid #e2e8f0; }
.video-wrapper iframe { position: absolute; top:0; left: 0; width: 100%; height: 100%; border: 0; }
.related-section { margin-top: 64px; padding-top: 40px; border-top: 1px solid #e2e8f0; }
.related-title { font-family: var(--font-heading); font-size: 22px; font-weight: 800; color: #0f172a; margin: 0 0 20px; }
.related-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; }
.related-card { display: block; text-decoration: none; border-radius: 12px; padding: 12px; border: 1px solid #e2e8f0; background: #fff; transition: all .2s; }
.related-card:hover { border-color: #f2920b; transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
.related-card img { width: 100%; aspect-ratio: 16/9; object-fit: cover; border-radius: 8px; margin-bottom: 10px; }
.related-card-title { font-size: 14px; font-weight: 700; color: #0f172a; line-height: 1.35; margin: 0; }
.cta-box { max-width: 860px; margin: 32px auto 0; padding: 20px 24px; border-radius: 16px; background: #ffffff; border: 2px solid #f2920b; box-shadow: 0 4px 16px rgba(15,23,42,.04); text-align: center; }
.cta-box h2, .cta-box h3 { font-family: var(--font-heading); font-size: 23px; font-weight: 800; color: #0f172a; margin: 0 0 6px; }
.cta-box p { max-width: 820px; margin: 2px auto 6px; font-size: 15px; color: #475569; line-height: 1.45; }

.calendly-wrapper { max-width: 440px; margin: 8px auto 0; height: 282px; overflow: hidden; border-radius: 12px; border: 1px solid #e2e8f0; position: relative; }
.calendly-inline-widget { width: 133% !important; height: 450px !important; min-width: 300px; margin-top: -55px !important; margin-left: 0 !important; border: 0 !important; transform: scale(0.75); transform-origin: top left; }
@media (max-width: 768px) {
  .related-grid { grid-template-columns: 1fr; }
  .article-block { margin: 0 0 40px; }
}
"""

HUB_BASE_CSS = """
.hub-hero { max-width: 1200px; margin: 8px auto 18px; text-align: center; }
.hub-title { font-family: 'Outfit', Arial, sans-serif !important; max-width: none !important; margin: 0 0 6px !important; font-size: clamp(30px, 3.2vw, 45px) !important; font-weight: 900 !important; line-height: 1.08 !important; color: #0f172a !important; text-transform: uppercase; letter-spacing: -.04em; }
.hub-eyebrow { margin: 0; color: #f2920b; font-size: 12px; font-weight: 900; letter-spacing: .04em; text-transform: uppercase; }
.article-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; margin: 20px 0 0; }
.article-card { color: #0f172a; text-decoration: none; }
.article-card img { display: block; }
.card-action:active { background: #76d3f6; transform: scale(.98); }
.next-step { max-width: 860px; margin: 28px auto 24px; padding: 20px 24px; border: 2px solid #f2920b; border-radius: 16px; background: #ffffff; box-shadow: 0 6px 20px rgba(15,23,42,.04); text-align: center; }
.next-step h2 { color: #0f172a; font-size: 23px; font-weight: 900; margin: 0 0 6px; letter-spacing: -0.02em; }
.next-step p { max-width: 820px; margin: 2px auto 6px; font-size: 15px; line-height: 1.45; color: #334155; }
.calendly-wrapper { max-width: 440px; margin: 8px auto 0; height: 282px; overflow: hidden; border-radius: 12px; border: 1px solid #e2e8f0; position: relative; }
.calendly-inline-widget { width: 133% !important; height: 450px !important; min-width: 300px; margin-top: -55px !important; margin-left: 0 !important; border: 0 !important; transform: scale(0.75); transform-origin: top left; }
@media (max-width: 1050px) { .article-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
@media (max-width: 760px) { .hub-hero { margin: 18px auto 38px; text-align: left; } .hub-title { white-space: normal; } .intro { margin: 0; } .article-grid { grid-template-columns: 1fr; } }
""" + TEXTURE_CSS


I18N_SUBHEADING_RE = re.compile(
    r"^(Error \d+:|ERROR EXTRA:|Mistake \d+:|EXTRA BUG:|Erreur \d+\s*:|Errore \d+:|ERRORE EXTRA:|Fehler \d+:|EXTRA-FEHLER:|Conclusion\s*:|Conclusione:|Fazit:)\s*(.*)$",
    re.IGNORECASE,
)
I18N_INLINE_HEADING_RE = re.compile(
    r"^<strong>(Plan [A-Z]\s*:[^<]*|Piano [A-Z]\s*:[^<]*|Padmi\s*:|Aiball\s*:|Rackety\s*:|Investissement initial[^<]*|Initial hardware investment[^<]*|Investimento iniziale[^<]*|Einmalige Anfangsinvestition[^<]*)</strong>\s*(.*)$",
    re.IGNORECASE,
)
I18N_LIST_RE = re.compile(r"^(\d+[º°oa\.]\s*)(.*)$")


def format_i18n_paragraph(p: str) -> str:
    """Format an already-translated paragraph (FR, EN, IT, DE) with semantic <h2> subheadings and list badges."""
    p = p.strip()
    if not p:
        return ""
    m_sub = I18N_SUBHEADING_RE.match(p)
    if m_sub:
        label = m_sub.group(1).strip()
        rest = m_sub.group(2).strip()
        if any(label.lower().startswith(k) for k in ("error", "mistake", "erreur", "errore", "fehler", "extra")):
            return f'<h2 class="article-subheading"><span class="subheading-title">{html.escape(p)}</span></h2>'
        else:
            out = f'<h2 class="article-subheading"><span class="subheading-title">{html.escape(label)}</span></h2>'
            if rest:
                out += f"\n<p>{rest}</p>"
            return out

    m_inline = I18N_INLINE_HEADING_RE.match(p)
    if m_inline:
        heading_label = m_inline.group(1).strip()
        rest = m_inline.group(2).strip()
        out = f'<h2 class="article-subheading"><span class="subheading-title">{html.escape(heading_label)}</span></h2>'
        if rest:
            out += f"\n<p>{rest}</p>"
        return out

    m_list = I18N_LIST_RE.match(p)
    if m_list:
        num = m_list.group(1).strip()
        rest = m_list.group(2).strip()
        return f'<p class="list-item-line"><strong class="list-badge">{html.escape(num)}</strong> {rest}</p>'

    return f"<p>{p}</p>"


def format_es_sentence(raw: str, slug: str) -> str:
    """Use build_camera_articles's formatter and upgrade <h3 class="article-subheading"> to semantic <h2>."""
    rendered = format_sentence_item(raw, slug)
    rendered = rendered.replace('<h3 class="article-subheading">', '<h2 class="article-subheading">').replace("</h3>", "</h2>")
    return rendered


def get_header(lang: str, prefix: str, slug: str = None) -> str:
    """Genera cabecera con selector multilingüe y URLs canónicas de idiomas."""
    home_url = "/de/camaras/" if lang == "de" else ("/" if lang == "es" else f"/{lang}/")
    # En alemán (/de/) solo existe el hub de cámaras; las demás secciones enlazan a /en/ o /
    base_nav_lang = "en" if lang == "de" else lang
    llaveros_url = f"/{base_nav_lang}/llaveros-padel-personalizados/" if base_nav_lang != "es" else "/llaveros-padel-personalizados/"
    camaras_url = f"/{lang}/camaras/" if lang != "es" else "/camaras/"
    blog_url = f"/{base_nav_lang}/blog/" if base_nav_lang != "es" else "/blog/"
    franquicias_url = f"/{base_nav_lang}/franquicias-padel/" if base_nav_lang != "es" else "/franquicias-padel/"
    contact_url = f"/{base_nav_lang}/#contacto" if base_nav_lang != "es" else "/#contacto"

    nav_llaveros = {
        "es": "LLAVEROS", "en": "KEYRINGS", "fr": "PORTE-CLÉS", "it": "PORTACHIAVI", "de": "SCHLÜSSELANHÄNGER"
    }.get(lang, "LLAVEROS")

    nav_camaras = {
        "es": "CÁMARAS", "en": "CAMERAS", "fr": "CAMÉRAS", "it": "TELECAMERE", "de": "KAMERAS"
    }.get(lang, "CÁMARAS")

    nav_chains = {
        "es": "Cadenas de clubs", "en": "Franchises", "fr": "Chaînes de clubs", "it": "Franchigie", "de": "Club-Ketten"
    }.get(lang, "Cadenas de clubs")

    nav_contact = {
        "es": "Contactar", "en": "Contact", "fr": "Contacter", "it": "Contatti", "de": "Kontakt"
    }.get(lang, "Contactar")

    subpath = f"camaras/articulos/{slug}/" if slug else "camaras/"
    dropdown_links = "\n".join([
        f'<a href="/{l}/{subpath}" class="block text-center px-4 py-2 text-xs hover:bg-[#f2920b] hover:text-slate-950 transition {"font-black text-[#f2920b]" if l==lang else "font-bold text-slate-700"}">{l.upper()}</a>'
        if l != "es" else
        f'<a href="/{subpath}" class="block text-center px-4 py-2 text-xs hover:bg-[#f2920b] hover:text-slate-950 transition {"font-black text-[#f2920b]" if l==lang else "font-bold text-slate-700"}">ES</a>'
        for l in ["es", "en", "fr", "it", "de"]
    ])

    return f'''<header class="fixed top-0 left-0 w-full z-50 bg-white/95 backdrop-blur-md border-b border-slate-200/80 shadow-xs w-full">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 sm:h-20 flex items-center justify-between">
    <a href="{home_url}" class="flex items-center gap-2 group shrink-0" aria-label="CoolPadel Home">
      <img src="/assets/images/coolpadel-mascot-hd.png" alt="Mascota CoolPadel" width="44" height="44" class="h-8 sm:h-11 w-auto object-contain group-hover:scale-105 transition" fetchpriority="high">
      <img src="/assets/images/coolpadel-typography-hd.png" alt="CoolPadel" width="140" height="28" class="h-5 sm:h-7 w-auto object-contain" fetchpriority="high">
    </a>
    <div class="flex items-center gap-2 sm:gap-4 lg:gap-6">
      <a href="{llaveros_url}" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">{nav_llaveros}</a>
      <a href="{camaras_url}" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-[#f2920b] transition whitespace-nowrap">{nav_camaras}</a>
      <a href="{blog_url}" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">Blog</a>
      <a href="{franquicias_url}" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">{nav_chains}</a>
      <div class="relative inline-block text-left" id="lang-dropdown-container">
        <button type="button" onclick="toggleLangDropdown(event)" id="lang-dropdown-btn" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 border border-slate-200 text-xs font-black text-slate-900 shadow-xs transition cursor-pointer" aria-expanded="false" aria-haspopup="true">
          <span id="current-lang-code" class="uppercase font-black">{lang.upper()}</span>
          <i data-lucide="chevron-down" class="w-3.5 h-3.5 stroke-[2.5] text-slate-600 transition-transform duration-200" id="lang-dropdown-arrow"></i>
        </button>
        <div id="lang-dropdown-menu" class="hidden absolute right-0 mt-2 w-24 bg-white rounded-2xl shadow-[0_12px_30px_rgba(0,0,0,0.15)] border border-slate-200 py-1.5 z-50 transition-all overflow-hidden">
          {dropdown_links}
        </div>
      </div>
      <a href="{contact_url}" class="inline-flex items-center gap-1.5 px-3.5 sm:px-4 py-1.5 sm:py-2 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition shadow-sm hover:scale-105 active:scale-95 cursor-pointer">
        <span>{nav_contact}</span>
        <i data-lucide="arrow-down" class="w-3 h-3 stroke-[3]"></i>
      </a>
      <a href="{home_url}" class="group py-1 inline-flex items-center shrink-0 pl-1" aria-label="CoolPadel Eyes">
        <img src="/assets/images/eyes-thumb.png?v=fixed_eyes" alt="CoolPadel Eyes" width="28" height="28" style="height:26px;max-height:26px;width:auto" class="object-contain group-hover:scale-110 transition duration-300">
      </a>
    </div>
  </div>
</header>
<div class="h-16 sm:h-20 w-full shrink-0" aria-hidden="true"></div>
'''


def render_page(title: str, content: str, lang: str, prefix: str = "/", slug: str = None, meta_desc: str = None, video_meta: tuple = None) -> str:
    lang_seg = f"{lang}/" if lang != "es" else ""
    if slug:
        canonical_url = f"https://coolpadelstudios.com/{lang_seg}camaras/articulos/{slug}/"
        hreflangs = f"""  <link rel="alternate" hreflang="es" href="https://coolpadelstudios.com/camaras/articulos/{slug}/">
  <link rel="alternate" hreflang="en" href="https://coolpadelstudios.com/en/camaras/articulos/{slug}/">
  <link rel="alternate" hreflang="fr" href="https://coolpadelstudios.com/fr/camaras/articulos/{slug}/">
  <link rel="alternate" hreflang="it" href="https://coolpadelstudios.com/it/camaras/articulos/{slug}/">
  <link rel="alternate" hreflang="de" href="https://coolpadelstudios.com/de/camaras/articulos/{slug}/">
  <link rel="alternate" hreflang="x-default" href="https://coolpadelstudios.com/camaras/articulos/{slug}/">"""
    else:
        canonical_url = f"https://coolpadelstudios.com/{lang_seg}camaras/"
        hreflangs = f"""  <link rel="alternate" hreflang="es" href="https://coolpadelstudios.com/camaras/">
  <link rel="alternate" hreflang="en" href="https://coolpadelstudios.com/en/camaras/">
  <link rel="alternate" hreflang="fr" href="https://coolpadelstudios.com/fr/camaras/">
  <link rel="alternate" hreflang="it" href="https://coolpadelstudios.com/it/camaras/">
  <link rel="alternate" hreflang="de" href="https://coolpadelstudios.com/de/camaras/">
  <link rel="alternate" hreflang="x-default" href="https://coolpadelstudios.com/camaras/">"""

    og_image = f"https://coolpadelstudios.com/assets/images/camaras/{ARTICLE_IMAGES.get(slug, 'camera-01.jpg')}" if slug else "https://coolpadelstudios.com/assets/images/savemyplay-1.jpg"
    og_type = "article" if slug else "website"

    # Resolver seo_title y meta_desc desde camaras_aeo_data
    aeo_entry = {}
    if slug:
        aeo_entry = AEO_FAQS_AND_DESCS.get(lang, {}).get(slug, {}) or AEO_FAQS_AND_DESCS.get("es", {}).get(slug, {})
        if not meta_desc and aeo_entry.get("desc"):
            meta_desc = aeo_entry["desc"]
        raw_seo_title = aeo_entry.get("seo_title") or (f"{title} | CoolPadel" if len(title) <= 55 else title)
        if len(raw_seo_title) > 65 and " | CoolPadel" in raw_seo_title:
            raw_seo_title = raw_seo_title.replace(" | CoolPadel", "").strip()
        seo_title = raw_seo_title
    else:
        hub_meta = HUB_SEO_META.get(lang, {}) or HUB_SEO_META.get("es", {})
        if hub_meta.get("desc"):
            meta_desc = hub_meta["desc"]
        raw_hub_title = hub_meta.get("seo_title") or f"{title} | Save my Play & CoolPadel"
        if len(raw_hub_title) > 65 and " | CoolPadel" in raw_hub_title:
            raw_hub_title = raw_hub_title.replace(" | CoolPadel", "").strip()
        seo_title = raw_hub_title

    if not meta_desc:
        meta_desc = f"{title} - CoolPadel Studios y Save my Play. Descubre costes, rentabilidad y grabación inteligente en pista."
    clean_desc = re.sub(r'\s+', ' ', meta_desc).strip()
    safe_desc = html.escape(clean_desc)[:160]

    schema_parts = []
    if slug:
        faq_answer = aeo_entry.get("answer", clean_desc) if aeo_entry else clean_desc

        home_label = "Inicio" if lang == "es" else ("Accueil" if lang == "fr" else ("Startseite" if lang == "de" else "Home"))
        camaras_label = "Cámaras" if lang == "es" else ("Caméras" if lang == "fr" else ("Kameras" if lang == "de" else ("Telecamere" if lang == "it" else "Cameras")))
        canonical_base = "https://coolpadelstudios.com/"
        camaras_cat_url = f"{canonical_base}camaras/" if lang == "es" else f"{canonical_base}{lang}/camaras/"

        schema_parts.append(f"""    {{
      "@type": "Article",
      "headline": {json.dumps(seo_title)},
      "alternativeHeadline": {json.dumps(title)},
      "description": {json.dumps(clean_desc)},
      "image": ["{og_image}"],
      "datePublished": "2026-10-15T09:00:00+02:00",
      "dateModified": "2026-11-04T09:00:00+01:00",
      "mainEntityOfPage": "{canonical_url}",
      "inLanguage": "{lang}",
      "speakable": {{
        "@type": "SpeakableSpecification",
        "cssSelector": [".article-title", ".article-body p:first-of-type"]
      }},
      "author": {{
        "@type": "Person",
        "name": "Javier Villoria",
        "jobTitle": "Founder & B2B Director",
        "url": "https://www.linkedin.com/in/javier-villoria-soleto-606737298/"
      }},
      "publisher": {{
        "@type": "Organization",
        "name": "CoolPadel Studios",
        "url": "https://coolpadelstudios.com",
        "logo": "https://coolpadelstudios.com/assets/images/coolpadel-mascot-hd.png",
        "sameAs": [
          "https://www.instagram.com/coolpadel_/",
          "https://www.linkedin.com/in/javier-villoria-soleto-606737298/",
          "https://maps.google.com/?cid=5000443597205028051"
        ]
      }}
    }}""")
        schema_parts.append(f"""    {{
      "@type": "BreadcrumbList",
      "@id": "{canonical_url}#breadcrumb",
      "itemListElement": [
        {{
          "@type": "ListItem",
          "position": 1,
          "name": "{home_label}",
          "item": "{canonical_base}{lang + '/' if lang not in ('es', 'de') else ''}"
        }},
        {{
          "@type": "ListItem",
          "position": 2,
          "name": "{camaras_label}",
          "item": "{camaras_cat_url}"
        }},
        {{
          "@type": "ListItem",
          "position": 3,
          "name": {json.dumps(title)},
          "item": "{canonical_url}"
        }}
      ]
    }}""")
        schema_parts.append(f"""    {{
      "@type": "FAQPage",
      "mainEntity": [{{
        "@type": "Question",
        "name": {json.dumps(title)},
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": {json.dumps(faq_answer)}
        }}
      }}]
    }}""")
        if video_meta:
            vt, vd, vu = video_meta
            schema_parts.append(f"""    {{
      "@type": "VideoObject",
      "name": {json.dumps(vt)},
      "description": {json.dumps(vd)},
      "thumbnailUrl": ["{og_image}"],
      "embedUrl": "{vu}",
      "uploadDate": "2026-10-20T08:00:00+02:00"
    }}""")
    else:
        home_label = "Inicio" if lang == "es" else ("Accueil" if lang == "fr" else ("Startseite" if lang == "de" else "Home"))
        camaras_label = "Cámaras" if lang == "es" else ("Caméras" if lang == "fr" else ("Kameras" if lang == "de" else ("Telecamere" if lang == "it" else "Cameras")))
        canonical_base = "https://coolpadelstudios.com/"
        item_list_elements = []
        for idx_art, s_art in enumerate(ARTICLE_ORDER, start=1):
            item_url = f"{canonical_url}articulos/{s_art}/"
            item_list_elements.append(f"""        {{
          "@type": "ListItem",
          "position": {idx_art},
          "url": "{item_url}"
        }}""")
        item_list_json = ",\n".join(item_list_elements)

        schema_parts.append(f"""    {{
      "@type": "CollectionPage",
      "name": {json.dumps(seo_title)},
      "description": {json.dumps(clean_desc)},
      "url": "{canonical_url}",
      "inLanguage": "{lang}",
      "mainEntity": {{
        "@type": "ItemList",
        "numberOfItems": {len(ARTICLE_ORDER)},
        "itemListElement": [
{item_list_json}
        ]
      }}
    }}""")
        schema_parts.append(f"""    {{
      "@type": "BreadcrumbList",
      "@id": "{canonical_url}#breadcrumb",
      "itemListElement": [
        {{
          "@type": "ListItem",
          "position": 1,
          "name": "{home_label}",
          "item": "{canonical_base}{lang + '/' if lang not in ('es', 'de') else ''}"
        }},
        {{
          "@type": "ListItem",
          "position": 2,
          "name": "{camaras_label}",
          "item": "{canonical_url}"
        }}
      ]
    }}""")
        schema_parts.append(f"""    {{
      "@type": "Product",
      "name": {json.dumps(title + " - Save my Play")},
      "description": {json.dumps(clean_desc)},
      "image": "https://coolpadelstudios.com/assets/images/savemyplay-1.jpg",
      "sku": "SMP-CAM-180",
      "brand": {{
        "@type": "Brand",
        "name": "Save my Play"
      }},
      "offers": [
        {{
          "@type": "Offer",
          "name": "Save my Play Court Camera Hardware",
          "priceCurrency": "EUR",
          "price": "180.00",
          "priceValidUntil": "2027-12-31",
          "availability": "https://schema.org/InStock",
          "hasMerchantReturnPolicy": {{
            "@type": "MerchantReturnPolicy",
            "applicableCountry": "ES",
            "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
            "merchantReturnDays": 14,
            "returnMethod": "https://schema.org/ReturnByMail",
            "returnFees": "https://schema.org/FreeReturn",
            "merchantReturnLink": "https://coolpadelstudios.com/politica-de-devoluciones.html"
          }},
          "shippingDetails": {{
            "@type": "OfferShippingDetails",
            "shippingRate": {{
              "@type": "MonetaryAmount",
              "value": "0.00",
              "currency": "EUR"
            }},
            "shippingDestination": {{
              "@type": "DefinedRegion",
              "addressCountry": ["ES", "FR", "IT", "PT", "DE", "BE", "GB", "US"]
            }}
          }}
        }},
        {{
          "@type": "Offer",
          "name": "Monthly Software Subscription (from 27 EUR/month)",
          "priceCurrency": "EUR",
          "price": "45.00",
          "priceValidUntil": "2027-12-31",
          "availability": "https://schema.org/InStock"
        }}
      ]
    }}""")

    schema_json = '<script type="application/ld+json">\n{\n  "@context": "https://schema.org",\n  "@graph": [\n' + ',\n'.join(schema_parts) + '\n  ]\n}\n</script>'

    header_html = get_header(lang, prefix, slug=slug)
    footer_html = get_silo_footer_html(root_prefix="/")

    html_out = f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(seo_title)}</title>
  <meta name="description" content="{safe_desc}">
  <link rel="canonical" href="{canonical_url}">
{hreflangs}
  <meta property="og:type" content="{og_type}">
  <meta property="og:title" content="{html.escape(seo_title)}">
  <meta property="og:description" content="{safe_desc}">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:image" content="{og_image}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{html.escape(seo_title)}">
  <meta name="twitter:description" content="{safe_desc}">
  <meta name="twitter:image" content="{og_image}">
  <link rel="alternate" type="text/markdown" href="https://coolpadelstudios.com/llms.txt" title="LLMs.txt">
  <link rel="alternate" type="text/markdown" href="https://coolpadelstudios.com/llms-full.txt" title="LLMs-Full.txt">
  {schema_json}
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/lucide@0.468.0/dist/umd/lucide.min.js"></script>
  <link rel="preconnect" href="https://assets.calendly.com">
  <style>
{ARTICLE_CSS}
{HUB_BASE_CSS}
  </style>
  <script>
    function toggleLangDropdown(event) {{
      event.stopPropagation();
      const menu = document.getElementById('lang-dropdown-menu');
      const arrow = document.getElementById('lang-dropdown-arrow');
      if (menu) {{
        menu.classList.toggle('hidden');
        if (arrow) arrow.classList.toggle('rotate-180');
      }}
    }}
    document.addEventListener('click', function(e) {{
      const container = document.getElementById('lang-dropdown-container');
      const menu = document.getElementById('lang-dropdown-menu');
      const arrow = document.getElementById('lang-dropdown-arrow');
      if (container && !container.contains(e.target) && menu && !menu.classList.contains('hidden')) {{
        menu.classList.add('hidden');
        if (arrow) arrow.classList.remove('rotate-180');
      }}
    }});
  </script>
</head>
<body>
  {header_html}
  {content}
  {footer_html}
  <script>if (window.lucide) lucide.createIcons();</script>
  <script src="https://assets.calendly.com/assets/external/widget.js" async></script>
  <script src="/assets/js/cp-analytics.js" defer></script>
</body>
</html>"""
    return html_out


def build_all():
    print("Iniciando compilacion unificada multilingue de Camaras...")
    articles_es = load_articles()
    articles_by_slug_es = {a["slug"]: a for a in articles_es}

    # Recargar CAMARAS_I18N por si acaba de generarse
    try:
        import importlib
        import camaras_i18n_data
        importlib.reload(camaras_i18n_data)
        i18n_dict = camaras_i18n_data.CAMARAS_I18N
    except Exception:
        i18n_dict = {}

    for lang in ["es", "fr", "en", "it", "de"]:
        print(f"\n================ Compilando idioma: {lang.upper()} ================")
        if lang == "es":
            base_dir = ROOT / "camaras"
            articles_data = {
                a["slug"]: {"title": a["title"], "blocks": a["blocks"]}
                for a in articles_es
            }
            hub_title = "Cámaras para clubs de pádel"
            hub_eyebrow = "Lo que necesitas saber"
            hub_intro_paras = [
                "Sabemos que queréis tomar la mejor decisión sobre las cámaras<br>La experiencia nos dice que los clubs agradecen tener información útil a su disposición",
                "Y que si no tenéis interés en informaros, no merece la pena hacer la demo online",
                "Por eso, hemos tratado de ser lo más sinceros y transparentes posible",
                "Por el camino os iréis dando cuenta de si es buena idea poner cámaras o no<br>Y si queréis ponerlas de Save My Play o de otra empresa",
                "Sea cual sea la decisión, será mejor para vosotros y para nosotros",
                "Así si hacemos la demo, tenéis mejores preguntas y aprovechamos mejor el tiempo"
            ]
            next_step_title = "Siguiente paso:"
            next_step_p1 = "Si todavía no lo ves claro, te dejo arriba más artículos sobre cámaras que te ayudarán."
            next_step_p2 = "Si tienes alguna pregunta y quieres que te enseñe bien cómo funciona todo, escríbeme directamente y lo vemos."
            read_article_btn = "Leer artículo"
            related_heading = "Artículos recomendados"
            videos_data = {
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
                    "Herramientas de entrenamiento en pista",
                    "Con las coaching tools puedes pausar la jugada en la tablet, dibujar trayectorias y grabar notas de voz para tus alumnos.",
                    "https://www.youtube-nocookie.com/embed/FcnCWaYahP8",
                ),
            }
        elif lang == "fr":
            base_dir = ROOT / "fr" / "camaras"
            lang_entry = i18n_dict.get("fr", {})
            articles_data = lang_entry.get("articles", FR_ARTICLES_DATA)
            hub_title = "Caméras pour clubs de padel"
            hub_eyebrow = "Tout ce que vous devez savoir avant d'installer des caméras"
            hub_intro_paras = [
                "Nous savons que vous voulez prendre la meilleure décision concernant les caméras<br>L'expérience nous montre que les clubs apprécient d'avoir des informations utiles et transparentes à disposition<br>Et que si vous n'avez aucun intérêt à vous informer, cela ne vaut pas la peine de faire une démo en ligne",
                "C'est pourquoi nous avons voulu être les plus sincères et transparents possible",
                "Au fil de vos lectures, vous vous rendrez compte par vous-même si c'est une bonne idée d'installer des caméras ou non<br>Et si vous souhaitez les prendre chez Save My Play ou chez un confrère<br>Quelle que soit votre décision, ce sera la meilleure pour vous comme pour nous",
                "Ainsi, si nous faisons la démo, vous aurez de bien meilleures questions et nous rentabiliserons au mieux notre temps d'échange"
            ]
            next_step_title = "Étape suivante"
            next_step_p1 = "Si vous hésitez encore, découvrez ci-dessus nos guides détaillés sur les caméras de padel."
            next_step_p2 = "Si vous avez des questions précises et souhaitez voir concrètement le système en direct, réservez votre créneau pour la démo."
            read_article_btn = "Lire l'article"
            related_heading = "Articles recommandés"
            videos_data = FR_VIDEOS
        else:
            base_dir = ROOT / lang / "camaras"
            lang_entry = i18n_dict.get(lang, {})
            articles_data = lang_entry.get("articles", {})
            videos_data = lang_entry.get("videos", {})
            hub_title = lang_entry.get("hub_title", "Cameras for padel clubs")
            hub_eyebrow = lang_entry.get("hub_eyebrow", "Everything you need to know before installing cameras")
            hub_intro_paras = lang_entry.get("hub_intro", [])
            next_step_title = lang_entry.get("next_step_title", "Next step")
            next_step_p1 = lang_entry.get("next_step_p1", "If you're still not sure, check out our guides above on padel court cameras.")
            next_step_p2 = lang_entry.get("next_step_p2", "If you have questions and want to see how it all works live, book a demo call.")
            read_article_btn = lang_entry.get("read_article", "Read article")
            related_heading = lang_entry.get("related_title", "Recommended articles")

        art_dir = base_dir / "articulos"
        art_dir.mkdir(parents=True, exist_ok=True)

        # 1. Construir Hub
        cards_html = []
        for slug in ARTICLE_ORDER:
            art = articles_data.get(slug, articles_by_slug_es.get(slug, {}))
            art_title = art.get("title", slug)
            img_name = ARTICLE_IMAGES.get(slug, "camera-01.jpg")
            card = f'''<a href="articulos/{slug}/" class="article-card bg-white border-2 border-slate-200/90 hover:border-[#f2920b] rounded-2xl p-4 sm:p-5 shadow-2xs hover:shadow-lg transition-all duration-300 flex flex-col justify-between group hover:-translate-y-0.5 cursor-pointer block">
  <div class="space-y-3">
    <div class="aspect-[16/9] rounded-xl overflow-hidden bg-slate-900 border border-slate-200/90 shadow-sm relative">
      <img src="/assets/images/camaras/{img_name}" alt="{html.escape(art_title)}" width="800" height="450" class="w-full h-full object-cover group-hover:scale-105 transition duration-500" loading="lazy" decoding="async">
    </div>
    <div>
      <h2 class="font-sans font-extrabold text-sm sm:text-base lg:text-lg text-slate-900 leading-snug tracking-tight transition-colors m-0">{html.escape(art_title)}</h2>
    </div>
  </div>
  <div class="pt-3.5 border-t border-slate-100 mt-4">
    <div class="card-action group relative w-full inline-flex items-center justify-center gap-2 px-4 py-2.5 rounded-full bg-[#f2920b] group-hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition-all duration-300 shadow-xs group-hover:shadow-md group-hover:scale-[1.01] overflow-hidden active:scale-[.98]">
      <span class="font-black">{read_article_btn}</span>
      <div class="w-4 h-4 rounded-full bg-slate-950/10 group-hover:bg-slate-950 group-hover:text-white flex items-center justify-center transition-all duration-300">
        <i data-lucide="arrow-right" class="w-3 h-3 stroke-[3] group-hover:translate-x-0.5 transition-transform duration-300"></i>
      </div>
    </div>
  </div>
</a>'''
            cards_html.append(card)

        calendly_locale = lang if lang in ["es", "fr", "en", "it", "de"] else "en"

        # Formato intercalado universal para todos los idiomas: 3 articulos -> parrafo -> 3 articulos...
        sections_parts = []
        # 1. Primeros 3 articulos inmediatamente tras el hero
        g0 = "\n      ".join(cards_html[0:3])
        sections_parts.append(f'''  <section>
    <div class="article-grid">
      {g0}
    </div>
  </section>''')
        
        # 2. Intercalar parrafos de texto con grupos de articulos
        art_idx = 3
        num_paras = len(hub_intro_paras)
        for p_idx, p_text in enumerate(hub_intro_paras):
            if not p_text.strip():
                continue
            band_html = f'''  <div class="intro-full-band">
    <div class="intro">
      <p>{p_text}</p>
    </div>
  </div>'''
            sections_parts.append(band_html)

            if p_idx < num_paras - 1:
                art_group = cards_html[art_idx:art_idx+3]
                art_idx += 3
            else:
                # Ultimo bloque con todos los articulos restantes
                art_group = cards_html[art_idx:]

            if art_group:
                g_html = "\n      ".join(art_group)
                sections_parts.append(f'''  <section>
    <div class="article-grid">
      {g_html}
    </div>
  </section>''')

        body_sections_html = "\n\n".join(sections_parts)
        if lang == "es":
            hero_btn_html = '''    <div class="mt-5 flex justify-center">
      <a href="https://wa.me/34680317486?text=Hola%20Javier%2C%20quiero%20informaci%C3%B3n%20sobre%20las%20c%C3%A1maras%20de%20p%C3%A1del%20para%20mi%20club" target="_blank" rel="noopener noreferrer" class="inline-flex items-center justify-center gap-2.5 px-6 py-3 rounded-full bg-[#25D366] hover:bg-[#20ba59] text-white font-heading font-black text-xs uppercase tracking-wider transition-all duration-300 shadow-md hover:scale-105 active:scale-95 group">
        <i data-lucide="message-circle" class="w-4 h-4 stroke-[2.5]"></i>
        <span>Contactar por WhatsApp</span>
      </a>
    </div>'''
            next_step_action_html = '''    <div class="mt-4 flex justify-center">
      <a href="https://wa.me/34680317486?text=Hola%20Javier%2C%20quiero%20informaci%C3%B3n%20sobre%20las%20c%C3%A1maras%20de%20p%C3%A1del%20para%20mi%20club" target="_blank" rel="noopener noreferrer" class="inline-flex items-center justify-center gap-2.5 px-8 py-3.5 rounded-full bg-[#25D366] hover:bg-[#20ba59] text-white font-heading font-black text-sm uppercase tracking-wider transition-all duration-300 shadow-md hover:scale-105 active:scale-95 group">
        <i data-lucide="message-circle" class="w-5 h-5 stroke-[2.5]"></i>
        <span>Contactar por WhatsApp</span>
      </a>
    </div>'''
        else:
            hero_btn_html = ''
            next_step_action_html = f'    <div class="calendly-wrapper"><div class="calendly-inline-widget" data-url="https://calendly.com/javier-vs-312/demo-save-my-play?locale={calendly_locale}&hide_landing_page_details=1&hide_gdpr_banner=1&hide_event_type_details=1&primary_color=f2920b"></div></div>'

        hub_content = f'''<main class="max-w-[1216px] mx-auto px-4 sm:px-6 lg:px-8 pt-2 sm:pt-3 pb-8 sm:pb-12">
  <section class="hub-hero">
    <h1 class="hub-title">{html.escape(hub_title)}</h1>
    <p class="hub-eyebrow">{html.escape(hub_eyebrow)}</p>
{hero_btn_html}
  </section>

{body_sections_html}

  <section class="next-step">
    <h2>{html.escape(next_step_title)}</h2>
    <p>{html.escape(next_step_p1)}</p>
    <p>{html.escape(next_step_p2)}</p>
{next_step_action_html}
  </section>
</main>'''

        hub_file = base_dir / "index.html"
        hub_meta_desc = HUB_SEO_META.get(lang, {}).get("desc") or (hub_eyebrow + ". " + hub_title)
        hub_file.write_text(render_page(hub_title, hub_content, lang, prefix="../../" if lang != "es" else "../", slug=None, meta_desc=hub_meta_desc), encoding="utf-8")
        print(f"  [OK] Hub generado: {hub_file}")

        # 2. Construir 20 Artículos
        for i, slug in enumerate(ARTICLE_ORDER):
            art = articles_data.get(slug, articles_by_slug_es.get(slug, {}))
            title = art.get("title", slug)
            blocks = art.get("blocks", [])
            img_name = ARTICLE_IMAGES.get(slug, "camera-01.jpg")

            # Formatear cuerpo con espaciado doble (.article-block), enlaces internos, negritas y <h2>
            body_html_parts = []
            if lang == "es":
                for block in blocks:
                    raw_block = "\n".join(block) if isinstance(block, list) else str(block)
                    sentences = split_into_sentences(raw_block)
                    if not sentences:
                        continue
                    items_html = [format_es_sentence(s, slug) for s in sentences]
                    block_paragraphs = "\n".join(items_html)
                    body_html_parts.append(f'<div class="article-block">\n{block_paragraphs}\n</div>')
            else:
                for block in blocks:
                    if isinstance(block, list):
                        rendered_items = [format_i18n_paragraph(p) for p in block if p.strip()]
                        block_paragraphs = "\n".join(rendered_items)
                    else:
                        block_paragraphs = format_i18n_paragraph(str(block))
                    if block_paragraphs.strip():
                        body_html_parts.append(f'<div class="article-block">\n{block_paragraphs}\n</div>')

            # Inyección de imagen de ejemplo en artículo de cámaras de pádel vs videovigilancia
            if slug == "camaras-de-padel-o-videovigilancia":
                caption_text = {
                    "es": "Ejemplo real de cámara de videovigilancia adaptada a pista de pádel: distorsión ojo de pez y líneas claramente curvadas.",
                    "en": "Real example of a surveillance camera on a padel court: fisheye distortion and visibly curved court lines.",
                    "fr": "Exemple réel d'une caméra de surveillance adaptée au padel : distorsion œil-de-bœuf et lignes de terrain incurvées.",
                    "it": "Esempio reale di telecamera di videosorveglianza adattata al campo da padel: distorsione a occhio di pesce e linee curve.",
                    "de": "Reales Beispiel einer Überwachungskamera auf dem Padel-Platz: Fisheye-Verzerrung und sichtbar gekrümmte Linien.",
                }.get(lang, "Ejemplo de cámara de videovigilancia adaptada a pista de pádel.")

                example_img_block = f'''<div class="article-block">
  <div class="rounded-2xl overflow-hidden border border-slate-200/90 shadow-sm bg-slate-950">
    <img src="/assets/images/camaras/ejemplo-camara-vigilancia-padel.jpg" alt="{html.escape(caption_text)}" width="1280" height="720" class="w-full h-auto object-cover" loading="lazy">
  </div>
  <p class="text-xs sm:text-sm text-slate-500 text-center italic mt-2.5">{caption_text}</p>
</div>'''
                if len(body_html_parts) >= 1:
                    body_html_parts.insert(1, example_img_block)
                else:
                    body_html_parts.append(example_img_block)

            # Inyección de herramienta interactiva de ROI
            if slug == "cuanto-cuesta-poner-camaras" or slug == "es-rentable-poner-camaras":
                roi_card_title = {
                    "es": "Calcula el retorno de inversión exacto para tu club",
                    "en": "Calculate the exact court camera ROI for your club",
                    "fr": "Calculez le retour sur investissement exact pour votre club",
                    "it": "Calcola il ritorno sull'investimento esatto per il tuo circolo",
                    "de": "Berechnen Sie den genauen Kamera-ROI für Ihren Club",
                }.get(lang, "Calculate exact court camera ROI")
                roi_card_desc = {
                    "es": "Prueba nuestra calculadora interactiva con el desglose de amortización mensual según tu número de pistas y reservas.",
                    "en": "Use our free interactive calculator to simulate monthly break-even and revenue based on your courts and bookings.",
                    "fr": "Testez notre calculateur interactif gratuit avec le détail d'amortissement mensuel selon votre nombre de pistes.",
                    "it": "Prova il nostro calcolatore interattivo gratuito con il dettaglio di ammortamento mensile in base al numero di campi.",
                    "de": "Nutzen Sie unseren kostenlosen interaktiven Rechner, um Amortisation und monatliche Einnahmen für Ihre Plätze zu simulieren.",
                }.get(lang, "Use our free interactive tool to simulate monthly break-even and margins.")
                roi_btn_label = {
                    "es": "Abrir Calculadora ROI",
                    "en": "Open ROI Calculator",
                    "fr": "Ouvrir le calculateur ROI",
                    "it": "Apri Calcolatore ROI",
                    "de": "ROI-Rechner öffnen",
                }.get(lang, "Open ROI Calculator")
                tool_url = (
                    "/herramientas/calculadora-roi-camaras-padel/"
                    if lang == "es"
                    else (
                        "/en/herramientas/calculadora-roi-camaras-padel/"
                        if lang == "de"
                        else f"/{lang}/herramientas/calculadora-roi-camaras-padel/"
                    )
                )
                body_html_parts.append(f'''<div class="article-block">
  <div class="bg-gradient-to-br from-amber-500/10 via-slate-100 to-slate-50 border-2 border-[#f2920b]/40 rounded-2xl p-6 sm:p-7 shadow-xs">
    <div class="flex items-start gap-3 sm:gap-4">
      <div class="w-10 h-10 rounded-xl bg-[#f2920b] text-slate-950 flex items-center justify-center shrink-0 shadow-sm mt-0.5">
        <i data-lucide="calculator" class="w-5 h-5 stroke-[2.5]"></i>
      </div>
      <div class="space-y-2 flex-grow">
        <h3 class="font-heading font-black text-base sm:text-lg text-slate-950 m-0">{roi_card_title}</h3>
        <p class="text-sm text-slate-600 m-0 leading-relaxed">{roi_card_desc}</p>
        <div class="pt-2">
          <a href="{tool_url}" class="inline-flex items-center gap-2 px-4 py-2 rounded-xl bg-[#f2920b] hover:bg-[#d98006] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition shadow-sm hover:scale-105 active:scale-95">
            <span>{roi_btn_label}</span>
            <i data-lucide="arrow-right" class="w-3.5 h-3.5 stroke-[3]"></i>
          </a>
        </div>
      </div>
    </div>
  </div>
</div>''')

            # Ejemplo en vivo de analíticas IA Save My Play para el artículo correspondiente
            if slug == "por-que-no-recomiendo-plan-analytics":
                analytics_card_title = {
                    "es": "Ejemplo en directo de analíticas y estadísticas con IA",
                    "en": "Live Demo: AI Court Analytics & Heatmaps in Action",
                    "fr": "Exemple en direct d'analyses et statistiques IA sur piste",
                    "it": "Esempio live di statistiche e analisi IA sul campo",
                    "de": "Live-Demo: KI-Statistiken & Heatmaps auf dem Platz",
                }.get(lang, "Live Demo: AI Court Analytics & Heatmaps")
                analytics_card_desc = {
                    "es": "Puedes ver un informe interactivo real con mapa de calor y análisis de golpeo generado automáticamente por la IA en este enlace:",
                    "en": "Explore a real interactive match report with AI-generated heatmaps, stroke analysis, and tracking stats directly on Save My Play:",
                    "fr": "Découvrez un rapport interactif réel avec cartes de chaleur et analyse des frappes généré par l'IA sur Save My Play :",
                    "it": "Esplora un report interattivo reale con mappe di calore e analisi dei colpi generato dall'IA direttamente su Save My Play:",
                    "de": "Erkunden Sie einen echten interaktiven Spielbericht mit KI-Heatmaps und Schlaganalysen direkt auf Save My Play:",
                }.get(lang, "Explore a real interactive match report with AI stats.")
                analytics_btn_label = {
                    "es": "Ver ejemplo en directo en Save My Play",
                    "en": "View Live Example on Save My Play",
                    "fr": "Voir l'exemple en direct sur Save My Play",
                    "it": "Vedi esempio live su Save My Play",
                    "de": "Live-Beispiel auf Save My Play ansehen",
                }.get(lang, "View Live Example on Save My Play")
                body_html_parts.append(f'''<div class="article-block">
  <div class="bg-gradient-to-br from-cyan-500/10 via-slate-100 to-slate-50 border-2 border-cyan-500/40 rounded-2xl p-6 sm:p-7 shadow-xs">
    <div class="flex items-start gap-3 sm:gap-4">
      <div class="w-10 h-10 rounded-xl bg-cyan-500 text-slate-950 flex items-center justify-center shrink-0 shadow-sm mt-0.5">
        <i data-lucide="bar-chart-3" class="w-5 h-5 stroke-[2.5]"></i>
      </div>
      <div class="space-y-2 flex-grow">
        <h3 class="font-heading font-black text-base sm:text-lg text-slate-950 m-0">{analytics_card_title}</h3>
        <p class="text-sm text-slate-600 m-0 leading-relaxed">{analytics_card_desc}</p>
        <div class="pt-2">
          <a href="https://savemyplay.com/replays/634779-ni9DexZC-the-club-at-monroe/analytics" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 px-4 py-2 rounded-xl bg-[#f2920b] hover:bg-[#d98006] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition shadow-sm hover:scale-105 active:scale-95">
            <span>{analytics_btn_label}</span>
            <i data-lucide="external-link" class="w-3.5 h-3.5 stroke-[3]"></i>
          </a>
        </div>
      </div>
    </div>
  </div>
</div>''')

            # Video embed si corresponde
            if slug in videos_data:
                v_title, v_desc, v_url = videos_data[slug]
                vid_html = f'''<div class="article-block">
  <div class="video-wrapper">
    <iframe src="{v_url}" title="{html.escape(v_title)}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
  </div>
  <p class="text-sm text-slate-500 text-center italic mt-2">{html.escape(v_desc)}</p>
</div>'''
                body_html_parts.append(vid_html)

            # Recomendaciones semánticas uniformes (grafo 3-regular balanceado)
            related_slugs = RELATED_MAP.get(slug)
            if not related_slugs or len(related_slugs) != 3:
                next_idx = (i + 1) % len(ARTICLE_ORDER)
                var_idx1 = (i + 5) % len(ARTICLE_ORDER)
                var_idx2 = (i + 11) % len(ARTICLE_ORDER)
                related_slugs = [ARTICLE_ORDER[next_idx], ARTICLE_ORDER[var_idx1], ARTICLE_ORDER[var_idx2]]

            related_cards_html = []
            for r_slug in related_slugs:
                r_art = articles_data.get(r_slug, articles_by_slug_es.get(r_slug, {}))
                r_title = r_art.get("title", r_slug)
                r_img = ARTICLE_IMAGES.get(r_slug, "camera-01.jpg")
                r_card = f'''<a href="../{r_slug}/" class="related-card">
  <img src="/assets/images/camaras/{r_img}" alt="{html.escape(r_title)}" loading="lazy">
  <p class="related-card-title">{html.escape(r_title)}</p>
</a>'''
                related_cards_html.append(r_card)

            home_url = "/" if lang in ("es", "de") else f"/{lang}/"
            camaras_hub_url = f"/{lang}/camaras/" if lang != "es" else "/camaras/"
            back_text = {
                "es": "Volver a Cámaras", "fr": "Retour aux caméras", "en": "Back to Cameras", "it": "Torna alle telecamere", "de": "Zurück zu Kameras"
            }.get(lang, "Volver")

            if lang == "es":
                article_cta_html = '''    <div class="mt-4 flex justify-center">
      <a href="https://wa.me/34680317486?text=Hola%20Javier%2C%20quiero%20informaci%C3%B3n%20sobre%20las%20c%C3%A1maras%20de%20p%C3%A1del%20para%20mi%20club" target="_blank" rel="noopener noreferrer" class="inline-flex items-center justify-center gap-2.5 px-8 py-3.5 rounded-full bg-[#25D366] hover:bg-[#20ba59] text-white font-heading font-black text-sm uppercase tracking-wider transition-all duration-300 shadow-md hover:scale-105 active:scale-95 group">
        <i data-lucide="message-circle" class="w-5 h-5 stroke-[2.5]"></i>
        <span>Contactar por WhatsApp</span>
      </a>
    </div>'''
            else:
                article_cta_html = f'    <div class="calendly-wrapper"><div class="calendly-inline-widget" data-url="https://calendly.com/javier-vs-312/demo-save-my-play?locale={calendly_locale}&hide_landing_page_details=1&hide_gdpr_banner=1&hide_event_type_details=1&primary_color=f2920b"></div></div>'

            article_page_content = f'''<main class="article-container">
  <!-- BREADCRUMB VISUAL -->
  <nav class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-slate-100 border border-slate-200/80 text-xs font-semibold text-slate-600 mb-6 flex-wrap" aria-label="Breadcrumb">
    <a href="{home_url}" class="hover:text-[#f2920b] transition">Home</a>
    <i data-lucide="chevron-right" class="w-3.5 h-3.5 text-slate-400"></i>
    <a href="{camaras_hub_url}" class="hover:text-[#f2920b] transition">{back_text}</a>
    <i data-lucide="chevron-right" class="w-3.5 h-3.5 text-slate-400"></i>
    <span class="text-slate-900 font-bold truncate max-w-[240px] sm:max-w-none">{html.escape(title)}</span>
  </nav>

  <div class="article-header">
    <h1 class="article-title">{html.escape(title)}</h1>
    <img src="/assets/images/camaras/{img_name}" alt="{html.escape(title)}" class="article-hero-img" width="800" height="450">
  </div>

  <div class="article-body">
    {"\n".join(body_html_parts)}
  </div>

  <div class="cta-box">
    <h2>{html.escape(next_step_title)}</h2>
    <p>{html.escape(next_step_p2)}</p>
{article_cta_html}
  </div>

  <div class="related-section">
    <h2 class="related-title">{html.escape(related_heading)}</h2>
    <div class="related-grid">
      {"\n".join(related_cards_html)}
    </div>
  </div>
</main>'''

            slug_dir = art_dir / slug
            slug_dir.mkdir(parents=True, exist_ok=True)
            art_file = slug_dir / "index.html"
            all_paras = []
            for b in blocks:
                if isinstance(b, list):
                    all_paras.extend([re.sub(r'<[^>]+>', '', p).strip() for p in b if p.strip()])
                elif isinstance(b, str) and b.strip():
                    all_paras.append(re.sub(r'<[^>]+>', '', b).strip())

            aeo_info = AEO_FAQS_AND_DESCS.get(lang, {}).get(slug, {}) or AEO_FAQS_AND_DESCS.get("es", {}).get(slug, {})
            if aeo_info and "desc" in aeo_info:
                chosen_desc = aeo_info["desc"]
            else:
                chosen_desc = " ".join(all_paras[:2]) if all_paras else f"{title}. Save my Play & CoolPadel."

            v_meta = videos_data.get(slug)
            art_file.write_text(render_page(title, article_page_content, lang, prefix="../../../../" if lang != "es" else "../../../", slug=slug, meta_desc=chosen_desc, video_meta=v_meta), encoding="utf-8")

        print(f"  [OK] 20 articulos generados para {lang.upper()} en {art_dir}")

    print("\n[COMPLETADO] Todos los idiomas (ES, FR, EN, IT, DE) generados y sincronizados con éxito.")


if __name__ == "__main__":
    build_all()
