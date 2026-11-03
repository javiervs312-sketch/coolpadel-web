# -*- coding: utf-8 -*-
"""
Builder unificado multilingüe para el Hub y los 20 artículos de cámaras de Save My Play
en todos los idiomas: ES, FR, EN, IT, DE.

Aplica estrictamente las directrices aprobadas:
1. Textura táctil azul con fondo azul profundo #3478a6, overlay 0.40 y textura_editorial_coolpadel.webp
   con ruta absoluta `/assets/images/branding/textura_editorial_coolpadel.webp`.
2. Texto del banner intro en blanco puro (#ffffff), tamaño uniforme 19px, interlineado amplio y espaciado de 28px.
3. Artículos con espaciado de 56px entre bloques (.article-block) y 12px entre párrafos.
4. Negritas clave preservadas sin saturar.
5. Recomendaciones rotativas (el siguiente de la lista en primer lugar + 2 variados).
6. Calendly embebido con el parámetro `locale=<lang>` correspondiente.
7. Cero consumo de tokens en compilaciones recurrentes.
"""

from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
from build_camera_articles import ARTICLE_IMAGES, RELATED_MAP, load_articles
from camaras_fr_data import FR_ARTICLES_DATA, FR_VIDEOS
try:
    from camaras_aeo_data import AEO_FAQS_AND_DESCS
except ImportError:
    AEO_FAQS_AND_DESCS = {}

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

# Textura azul táctil idéntica al blog oficial
TEXTURE_CSS = """
.intro-full-band {
  width: 100vw;
  position: relative;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
  background-color: #3478a6;
  background-image: linear-gradient(rgba(52, 120, 166, 0.40), rgba(52, 120, 166, 0.40)), url('/assets/images/branding/textura_editorial_coolpadel.webp');
  background-blend-mode: normal, soft-light;
  background-size: cover;
  background-position: center;
  padding: 44px 20px;
  border-top: 1px solid rgba(255, 255, 255, 0.15);
  border-bottom: 1px solid rgba(255, 255, 255, 0.15);
  box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.08);
}
.intro { max-width: 880px; margin: 0 auto; color: #ffffff; font-size: 19px; line-height: 1.6; text-align: center; }
.intro p { margin: 0 0 28px; color: #ffffff !important; font-size: 19px !important; font-weight: 500; }
.intro p:last-child { margin-bottom: 0; }
"""

ARTICLE_CSS = """
:root { --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif; --font-heading: 'Outfit', sans-serif; }
body { margin: 0; font-family: var(--font-sans); color: #0f172a; background: #ffffff; line-height: 1.7; -webkit-font-smoothing: antialiased; }
.article-container { max-width: 820px; margin: 0 auto; padding: 48px 20px 80px; }
.article-header { margin-bottom: 32px; }
.back-link { display: inline-flex; items-center: center; gap: 8px; color: #64748b; font-size: 14px; font-weight: 600; text-decoration: none; margin-bottom: 24px; transition: color .2s; }
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
.video-wrapper { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; border-radius: 16px; margin: 32px 0; border: 1px solid #e2e8f0; }
.video-wrapper iframe { position: absolute; top:0; left: 0; width: 100%; height: 100%; border: 0; }
.related-section { margin-top: 64px; padding-top: 40px; border-top: 1px solid #e2e8f0; }
.related-title { font-family: var(--font-heading); font-size: 22px; font-weight: 800; color: #0f172a; margin: 0 0 20px; }
.related-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; }
.related-card { display: block; text-decoration: none; border-radius: 12px; padding: 12px; border: 1px solid #e2e8f0; background: #fff; transition: all .2s; }
.related-card:hover { border-color: #f2920b; transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
.related-card img { width: 100%; aspect-ratio: 16/9; object-fit: cover; border-radius: 8px; margin-bottom: 10px; }
.related-card-title { font-size: 14px; font-weight: 700; color: #0f172a; line-height: 1.35; margin: 0; }
.cta-box { margin-top: 56px; padding: 32px; border-radius: 16px; background: #f8fafc; border: 2px solid #f2920b; text-align: center; }
.cta-box h3 { font-family: var(--font-heading); font-size: 24px; font-weight: 800; color: #0f172a; margin: 0 0 12px; }
.cta-box p { font-size: 16px; color: #475569; margin: 0 0 24px; }
@media (max-width: 768px) {
  .related-grid { grid-template-columns: 1fr; }
  .article-block { margin: 0 0 40px; }
}
"""

HUB_BASE_CSS = """
.hub-hero { max-width: 1200px; margin: 30px auto 36px; text-align: center; }
.hub-eyebrow { margin: 0 0 14px; color: #f2920b; font-size: 13px; font-weight: 900; letter-spacing: .04em; text-transform: uppercase; }
.hub-title { max-width: none !important; margin: 0 0 16px !important; font-size: clamp(42px, 3.5vw, 58px) !important; font-weight: 900 !important; line-height: 1.05 !important; color: #0f172a !important; white-space: nowrap; text-transform: uppercase; letter-spacing: -.04em; }
.article-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 18px; margin: 34px 0 0; }
.article-card { color: #0f172a; text-decoration: none; }
.article-card img { display: block; }
.card-action:active { background: #76d3f6; transform: scale(.98); }
.next-step { margin: 54px 0 48px; padding: 32px 34px 34px; border: 2px solid #f2920b; border-radius: 20px; background: #ffffff; box-shadow: 0 10px 30px rgba(15,23,42,.04); }
.next-step h2 { color: #0f172a; font-size: clamp(28px, 4vw, 36px); font-weight: 900; margin: 0 0 16px; letter-spacing: -0.02em; }
.next-step p { margin: 8px 0; font-size: 17px; line-height: 1.7; color: #334155; }
.calendly-inline-widget { min-width: 320px; height: 680px; margin-top: 24px; border-radius: 16px; overflow: hidden; border: 1px solid #e2e8f0; }
@media (max-width: 1050px) { .article-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
@media (max-width: 760px) { .hub-hero { margin: 18px auto 38px; text-align: left; } .hub-title { white-space: normal; } .intro { margin: 0; } .article-grid { grid-template-columns: 1fr; } }
""" + TEXTURE_CSS

def get_header(lang: str, prefix: str, slug: str = None) -> str:
    """Genera cabecera con selector multilingüe y URLs canónicas de idiomas."""
    home_url = "/" if lang == "es" else f"/{lang}/"
    llaveros_url = f"/{lang}/llaveros-padel-personalizados/" if lang != "es" else "/llaveros-padel-personalizados/"
    camaras_url = f"/{lang}/camaras/" if lang != "es" else "/camaras/"
    blog_url = f"/{lang}/blog/" if lang != "es" else "/blog/"
    franquicias_url = f"/{lang}/franquicias-padel/" if lang != "es" else "/franquicias-padel/"
    contact_url = f"/{lang}/#contacto" if lang != "es" else "/#contacto"

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
      <a href="{camaras_url}" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">{nav_camaras}</a>
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
    calendly_locale = lang if lang in ["es", "fr", "en", "it", "de"] else "en"
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

    if not meta_desc:
        meta_desc = f"{title} - CoolPadel Studios y Save my Play. Descubre costes, rentabilidad y grabacion inteligente en pista."
    clean_desc = re.sub(r'\s+', ' ', meta_desc).strip()
    safe_desc = html.escape(clean_desc)[:160]

    schema_parts = []
    if slug:
        # AEO direct answer
        aeo_entry = AEO_FAQS_AND_DESCS.get(lang, {}).get(slug, {})
        if not aeo_entry and lang != "es":
            aeo_entry = AEO_FAQS_AND_DESCS.get("es", {}).get(slug, {})
        faq_answer = aeo_entry.get("answer", safe_desc) if aeo_entry else safe_desc

        home_label = "Inicio" if lang == "es" else ("Accueil" if lang == "fr" else "Home")
        camaras_label = "Cámaras" if lang == "es" else ("Caméras" if lang == "fr" else ("Kameras" if lang == "de" else ("Telecamere" if lang == "it" else "Cameras")))
        canonical_base = "https://coolpadelstudios.com/"
        camaras_cat_url = f"{canonical_base}camaras/" if lang == "es" else f"{canonical_base}{lang}/camaras/"

        schema_parts.append(f"""    {{
      "@type": "Article",
      "headline": {json.dumps(title)},
      "description": {json.dumps(safe_desc)},
      "mainEntityOfPage": "{canonical_url}",
      "inLanguage": "{lang}",
      "speakable": {{
        "@type": "SpeakableSpecification",
        "cssSelector": [".article-title", ".article-body p:first-of-type"]
      }},
      "author": {{
        "@type": "Person",
        "name": "Javier Villoria",
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
          "item": "{canonical_base}{lang + '/' if lang != 'es' else ''}"
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
      "thumbnailUrl": ["https://coolpadelstudios.com/assets/images/camaras/{ARTICLE_IMAGES.get(slug, 'camera-01.jpg')}"],
      "embedUrl": "{vu}",
      "uploadDate": "2026-10-20T08:00:00+02:00"
    }}""")
    else:
        home_label = "Inicio" if lang == "es" else ("Accueil" if lang == "fr" else "Home")
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
      "name": {json.dumps(title)},
      "description": {json.dumps(safe_desc)},
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
          "item": "{canonical_base}{lang + '/' if lang != 'es' else ''}"
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
      "description": {json.dumps(safe_desc)},
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
    og_image = f"https://coolpadelstudios.com/assets/images/camaras/{ARTICLE_IMAGES.get(slug, 'camera-01.jpg')}" if slug else "https://coolpadelstudios.com/assets/images/savemyplay-1.jpg"
    og_type = "article" if slug else "website"

    header_html = get_header(lang, prefix, slug=slug)
    seo_title = f"{title} | CoolPadel" if len(title) <= 55 else title

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
        import camaras_i18n_data
        i18n_dict = camaras_i18n_data.CAMARAS_I18N
    except Exception:
        i18n_dict = {}

    # Soporte fallback para ES y FR
    for lang in ["es", "fr", "en", "it", "de"]:
        print(f"\n================ Compilando idioma: {lang.upper()} ================")
        if lang == "es":
            base_dir = ROOT / "camaras"
            articles_data = {
                a["slug"]: {"title": a["title"], "blocks": [[p for p in b.split("\n") if p.strip()] for b in a["blocks"]]}
                for a in articles_es
            }
            hub_title = "Cámaras para clubs de pádel"
            hub_eyebrow = "Todo lo que necesitas saber antes de poner cámaras"
            hub_intro_paras = [
                "Sabemos que queréis tomar la mejor decisión sobre las cámaras<br>La experiencia nos dice que los clubs agradecen tener información útil a su disposición<br>Y que si no tenéis interés en informaros, no merece la pena hacer la demo online",
                "Por eso, hemos tratado de ser lo más sinceros y transparentes posible",
                "Por el camino os iréis dando cuenta de si es buena idea poner cámaras o no<br>Y si queréis ponerlas de Save My Play o de otra empresa<br>Sea cual sea la decisión, será mejor para vosotros y para nosotros",
                "Así si hacemos la demo, tenéis mejores preguntas y aprovechamos mejor el tiempo"
            ]
            next_step_title = "Siguiente paso"
            next_step_p1 = "Si todavía no lo ves claro, te dejo arriba más artículos sobre cámaras que te ayudarán."
            next_step_p2 = "Si tienes alguna pregunta y quieres que te enseñe bien cómo funciona todo, busca tu hueco para la demo."
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
            articles_data = FR_ARTICLES_DATA
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
      <h3 class="font-sans font-extrabold text-sm sm:text-base lg:text-lg text-slate-900 leading-snug tracking-tight transition-colors">{html.escape(art_title)}</h3>
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

        intro_p_html = "\n".join([f"<p>{p}</p>" for p in hub_intro_paras])
        calendly_locale = lang if lang in ["es", "fr", "en", "it", "de"] else "en"

        hub_content = f'''<main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 sm:py-12">
  <section class="hub-hero">
    <p class="hub-eyebrow">{html.escape(hub_eyebrow)}</p>
    <h1 class="hub-title">{html.escape(hub_title)}</h1>
  </section>

  <div class="intro-full-band">
    <div class="intro">
      {intro_p_html}
    </div>
  </div>

  <section>
    <div class="article-grid">
      {"\n".join(cards_html)}
    </div>
  </section>

  <section class="next-step">
    <h2>{html.escape(next_step_title)}</h2>
    <p>{html.escape(next_step_p1)}</p>
    <p>{html.escape(next_step_p2)}</p>
    <div class="calendly-inline-widget" data-url="https://calendly.com/javier-vs-312/demo-save-my-play?locale={calendly_locale}&hide_landing_page_details=1&hide_gdpr_banner=1"></div>
  </section>
</main>'''

        hub_file = base_dir / "index.html"
        hub_file.write_text(render_page(hub_title, hub_content, lang, prefix="../../" if lang != "es" else "../", slug=None, meta_desc=hub_eyebrow + ". " + hub_title), encoding="utf-8")
        print(f"  [OK] Hub generado: {hub_file}")

        # 2. Construir 20 Artículos
        for i, slug in enumerate(ARTICLE_ORDER):
            art = articles_data.get(slug, articles_by_slug_es.get(slug, {}))
            title = art.get("title", slug)
            blocks = art.get("blocks", [])
            img_name = ARTICLE_IMAGES.get(slug, "camera-01.jpg")

            # Formatear cuerpo con espaciado doble (.article-block)
            body_html_parts = []
            for block in blocks:
                # Cada bloque contiene uno o varios párrafos
                if isinstance(block, list):
                    block_paragraphs = "\n".join([f"<p>{p}</p>" for p in block if p.strip()])
                else:
                    block_paragraphs = f"<p>{block}</p>"
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

            # Inyección de tabla comparativa o herramienta de ROI
            if slug == "cuanto-cuesta-poner-camaras" or slug == "es-rentable-poner-camaras":
                roi_card_title = "Calcula el retorno de inversión exacto para tu club" if lang == "es" else ("Calculate exact court camera ROI" if lang == "en" else "Calculez le retour sur investissement")
                roi_card_desc = "Prueba nuestra calculadora interactiva con el desglose de amortización mensual según tu número de pistas y reservas." if lang == "es" else "Use our free interactive tool to simulate monthly break-even and margins."
                roi_btn_label = "Abrir Calculadora ROI" if lang == "es" else ("Open ROI Calculator" if lang == "en" else "Ouvrir le calculateur")
                tool_url = "/herramientas/calculadora-roi-camaras-padel/" if lang == "es" else f"/{lang}/herramientas/calculadora-roi-camaras-padel/"
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

            # Recomendaciones rotativas (el siguiente en la lista en primer lugar + 2 variados)
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

            home_url = "/" if lang == "es" else f"/{lang}/"
            back_text = {
                "es": "Volver a Cámaras", "fr": "Retour aux caméras", "en": "Back to Cameras", "it": "Torna alle telecamere", "de": "Zurück zu Kameras"
            }.get(lang, "Volver")

            article_page_content = f'''<main class="article-container">
  <!-- BREADCRUMB VISUAL -->
  <nav class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-slate-100 border border-slate-200/80 text-xs font-semibold text-slate-600 mb-6 flex-wrap" aria-label="Breadcrumb">
    <a href="{home_url}" class="hover:text-[#f2920b] transition">Home</a>
    <i data-lucide="chevron-right" class="w-3.5 h-3.5 text-slate-400"></i>
    <a href="../" class="hover:text-[#f2920b] transition">{back_text}</a>
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
    <h3>{html.escape(next_step_title)}</h3>
    <p>{html.escape(next_step_p2)}</p>
    <div class="calendly-inline-widget" data-url="https://calendly.com/javier-vs-312/demo-save-my-play?locale={calendly_locale}&hide_landing_page_details=1&hide_gdpr_banner=1"></div>
  </div>

  <div class="related-section">
    <h3 class="related-title">{html.escape(related_heading)}</h3>
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
            
            # Prioritize dedicated AEO meta description
            aeo_info = AEO_FAQS_AND_DESCS.get(lang, {}).get(slug, {})
            if not aeo_info and lang != "es":
                aeo_info = AEO_FAQS_AND_DESCS.get("es", {}).get(slug, {})
            if aeo_info and "desc" in aeo_info:
                chosen_desc = aeo_info["desc"]
            else:
                chosen_desc = ""
                for p in all_paras:
                    if len(p) >= 50:
                        chosen_desc = p
                        break
                if not chosen_desc and all_paras:
                    chosen_desc = " ".join(all_paras[:2])
                if not chosen_desc or len(chosen_desc) < 40:
                    chosen_desc = f"{title}. Guia de instalacion, costes y funcionamiento de Save my Play para clubs de padel."

            v_meta = videos_data.get(slug)
            art_file.write_text(render_page(title, article_page_content, lang, prefix="../../../../" if lang != "es" else "../../../", slug=slug, meta_desc=chosen_desc, video_meta=v_meta), encoding="utf-8")

        print(f"  [OK] 20 articulos generados para {lang.upper()} en {art_dir}")

    print("\n[COMPLETADO] Todos los idiomas (ES, FR, EN, IT, DE) generados y sincronizados con éxito.")

if __name__ == "__main__":
    build_all()
