# -*- coding: utf-8 -*-
"""
Builder pour le hub et les 20 articles de caméras en français (CoolPadel Studios).
Génère :
  - coolpadel-web/fr/camaras/index.html
  - coolpadel-web/fr/camaras/articulos/<slug>/index.html (20 articles)
Style rigoureusement identique à la version espagnole (/camaras/), avec espacement
doublé des blocs, gras sélectifs, bannière bleue texturée avec texte blanc,
recommandations rotatives et widget Calendly en français.
"""

from __future__ import annotations

import html
import re
from pathlib import Path

from camaras_fr_data import FR_ARTICLES_DATA, FR_VIDEOS
from build_camera_articles import ARTICLE_IMAGES, RELATED_MAP, CSS, HUB_CSS

ROOT = Path(__file__).resolve().parent
CAMERAS_FR = ROOT / "fr" / "camaras"
ARTICLES_FR = CAMERAS_FR / "articulos"
CALENDLY_FR = "https://calendly.com/javier-vs-312/demo-save-my-play?locale=fr"

# Ordre canonique des articles (20)
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


def header_fr(prefix: str = "../../") -> str:
    """Header officiel CoolPadel avec liens en /fr/ et sélecteur de langue FR actif."""
    return f'''<header class="fixed top-0 left-0 w-full z-50 bg-white/95 backdrop-blur-md border-b border-slate-200/80 shadow-xs w-full"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 sm:h-20 flex items-center justify-between"><a href="/fr/" class="flex items-center gap-2 group shrink-0" aria-label="CoolPadel Home"><img src="{prefix}assets/images/coolpadel-mascot-hd.png" alt="Mascota CoolPadel" width="44" height="44" class="h-8 sm:h-11 w-auto object-contain group-hover:scale-105 transition" fetchpriority="high"><img src="{prefix}assets/images/coolpadel-typography-hd.png" alt="CoolPadel" width="140" height="28" class="h-5 sm:h-7 w-auto object-contain" fetchpriority="high"></a><div class="flex items-center gap-2 sm:gap-4 lg:gap-6"><a href="/fr/llaveros-padel-personalizados/" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">PORTE-CLÉS</a><a href="/fr/camaras/" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">CAMÉRAS</a><a href="/fr/blog/" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">Blog</a><a href="/fr/franquicias-padel/" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">Chaînes de clubs</a><div class="relative inline-block text-left" id="lang-dropdown-container"><button type="button" onclick="toggleLangDropdown(event)" id="lang-dropdown-btn" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 border border-slate-200 text-xs font-black text-slate-900 shadow-xs transition cursor-pointer" aria-expanded="false" aria-haspopup="true"><span id="current-lang-code" class="uppercase font-black">FR</span><i data-lucide="chevron-down" class="w-3.5 h-3.5 stroke-[2.5] text-slate-600 transition-transform duration-200" id="lang-dropdown-arrow"></i></button><div id="lang-dropdown-menu" class="hidden absolute right-0 mt-2 w-24 bg-white rounded-2xl shadow-[0_12px_30px_rgba(0,0,0,0.15)] border border-slate-200 py-1.5 z-50 transition-all overflow-hidden"><a href="/camaras/" class="block text-center px-4 py-2 text-xs">ES</a><a href="/en/camaras/" class="block text-center px-4 py-2 text-xs">EN</a><a href="/fr/camaras/" class="block text-center px-4 py-2 text-xs font-bold text-[#f2920b]">FR</a><a href="/it/camaras/" class="block text-center px-4 py-2 text-xs">IT</a><a href="/de/camaras/" class="block text-center px-4 py-2 text-xs">DE</a></div></div><a href="/fr/#contacto" class="inline-flex items-center gap-1.5 px-3.5 sm:px-4 py-1.5 sm:py-2 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition shadow-sm hover:scale-105 active:scale-95 cursor-pointer"><span>Contacter</span><i data-lucide="arrow-down" class="w-3 h-3 stroke-[3]"></i></a><a href="/fr/" class="group py-1 inline-flex items-center shrink-0 pl-1" aria-label="CoolPadel Eyes"><img src="{prefix}assets/images/eyes-thumb.png?v=fixed_eyes" alt="CoolPadel Eyes" width="28" height="28" style="height:26px;max-height:26px;width:auto" class="object-contain group-hover:scale-110 transition duration-300"></a></div></div></header><div class="h-16 sm:h-20 w-full shrink-0" aria-hidden="true"></div>'''


def page_fr(title: str, content: str, prefix: str = "../../", extra_css: str = "") -> str:
    """Génère la structure HTML complète d'une page en français."""
    return f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{html.escape(title)} | CoolPadel</title><meta name="description" content="{html.escape(title)}"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Outfit:wght@600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"><script src="https://cdn.tailwindcss.com"></script><script src="https://unpkg.com/lucide@0.468.0/dist/umd/lucide.min.js"></script><link rel="preconnect" href="https://assets.calendly.com"><style>{CSS}{extra_css}</style></head><body>{header_fr(prefix)}{content}<script>if (window.lucide) lucide.createIcons();</script><script>function toggleLangDropdown(e){{e.stopPropagation();var m=document.getElementById('lang-dropdown-menu');var a=document.getElementById('lang-dropdown-arrow');if(m){{var isHidden=m.classList.contains('hidden');if(isHidden){{m.classList.remove('hidden');if(a)a.classList.add('rotate-180');}}else{{m.classList.add('hidden');if(a)a.classList.remove('rotate-180');}}}}}}document.addEventListener('click',function(e){{var c=document.getElementById('lang-dropdown-container');var m=document.getElementById('lang-dropdown-menu');var a=document.getElementById('lang-dropdown-arrow');if(c&&m&&!c.contains(e.target)){{m.classList.add('hidden');if(a)a.classList.remove('rotate-180');}}}});</script><script src="https://assets.calendly.com/assets/external/widget.js" async></script><script src="{prefix}assets/js/cp-analytics.js" defer></script></body></html>'''


def format_sentence_item_fr(raw: str, slug: str) -> str:
    """Formate une ligne ou un paragraphe de corps d'article."""
    raw = raw.strip()
    if not raw:
        return ""

    # Détection des sous-titres (Error 1:, Plan A:, Conclusion, etc.)
    subhead_patterns = [
        r"^(Error\s+\d+:?\s*.*)$",
        r"^(Erreur\s+\d+:?\s*.*)$",
        r"^(Plan\s+[A-Z]:?\s*.*)$",
        r"^(En résumé\s*:?.*)$",
        r"^(Conclusion\s*:?.*)$",
    ]
    for pat in subhead_patterns:
        m = re.match(pat, raw, flags=re.IGNORECASE)
        if m:
            clean_sub = html.escape(m.group(1))
            return f'<h3 class="article-subheading"><span class="subheading-title">{clean_sub}</span></h3>'

    # Listes numérotées : 1º, 2º, 3º...
    m_num = re.match(r"^(\d+º|\d+\))\s+(.*)$", raw)
    if m_num:
        num_prefix = m_num.group(1)
        rest = m_num.group(2)
        return f'<p class="list-item-line"><strong>{num_prefix}</strong> {rest}</p>'

    return f'<p>{raw}</p>'


def article_body_fr(article: dict) -> str:
    """Génère le corps de l'article avec espacement doublé des blocs Highlights."""
    rendered_blocks = []
    slug = article["slug"]

    for block in article["blocks"]:
        items_html = [format_sentence_item_fr(s, slug) for s in block if s.strip()]
        if not items_html:
            continue
        block_html = "\n".join(items_html)
        rendered_blocks.append(f'<div class="article-block">\n{block_html}\n</div>')

    return "\n".join(rendered_blocks)


def build_fr() -> None:
    """Construit le hub et tous les articles de caméras en français."""
    ARTICLES_FR.mkdir(parents=True, exist_ok=True)

    articles_list = []
    for slug in ARTICLE_ORDER:
        data = FR_ARTICLES_DATA.get(slug)
        if not data:
            continue
        articles_list.append({
            "slug": slug,
            "title": data["title"],
            "blocks": data["blocks"],
        })

    # 1. Cartes pour la grille du Hub
    cards = "\n".join(
        f'''<a href="articulos/{a["slug"]}/" class="article-card bg-white border-2 border-slate-200/90 hover:border-[#f2920b] rounded-2xl p-4 sm:p-5 shadow-2xs hover:shadow-lg transition-all duration-300 flex flex-col justify-between group hover:-translate-y-0.5 cursor-pointer block"><div class="space-y-3"><div class="aspect-[16/9] rounded-xl overflow-hidden bg-slate-900 border border-slate-200/90 shadow-sm relative"><img src="../../assets/images/camaras/{ARTICLE_IMAGES[a["slug"]]}" alt="{html.escape(a["title"])}" width="800" height="450" class="w-full h-full object-cover group-hover:scale-105 transition duration-500" loading="lazy" decoding="async"></div><div><h3 class="font-sans font-extrabold text-sm sm:text-base lg:text-lg text-slate-900 leading-snug tracking-tight transition-colors">{html.escape(a["title"])}</h3></div></div><div class="pt-3.5 border-t border-slate-100 mt-4"><div class="card-action group relative w-full inline-flex items-center justify-center gap-2 px-4 py-2.5 rounded-full bg-[#f2920b] group-hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition-all duration-300 shadow-xs group-hover:shadow-md group-hover:scale-[1.01] overflow-hidden active:scale-[.98]"><span class="font-black">Lire l'article</span><div class="w-4 h-4 rounded-full bg-slate-950/10 group-hover:bg-slate-950 group-hover:text-white flex items-center justify-center transition-all duration-300"><i data-lucide="arrow-right" class="w-3 h-3 stroke-[3] group-hover:translate-x-0.5 transition-transform duration-300"></i></div></div></div></a>'''
        for a in articles_list
    )

    # 2. Bande bleue texturée d'introduction
    intro_fr = """<p>Nous savons que vous voulez prendre la meilleure décision concernant les caméras<br>L'expérience nous montre que les clubs apprécient d'avoir des informations utiles à leur disposition<br>Et que si vous n'avez pas l'envie de vous informer, cela ne vaut pas la peine de faire la démo en ligne</p><p>C'est pourquoi nous nous efforçons d'être le plus sincères et transparents possible</p><p>En cours de route, vous vous rendrez compte si c'est une bonne idée d'installer des caméras ou non<br>Et si vous souhaitez les prendre chez Save My Play ou chez un autre prestataire<br>Quelle que soit votre décision, elle sera meilleure pour vous comme pour nous</p><p>Ainsi, si nous faisons la démo, vous aurez de meilleures questions et nous profiterons mieux de notre temps</p>"""

    hub_content = f"""<main><section class="hub-hero"><p class="hub-eyebrow">Tout ce que vous devez savoir avant d'installer des caméras</p><h1 class="hub-title">Caméras pour clubs de padel</h1></section><div class="intro-full-band"><div class="intro">{intro_fr}</div></div><section><div class="article-grid">{cards}</div></section><section class="next-step"><h2>Étape suivante</h2><p>Si vous hésitez encore, découvrez ci-dessus d'autres articles sur les caméras pour vous guider.</p><p>Si vous avez des questions et souhaitez voir en direct comment tout fonctionne, réservez votre créneau pour la démo.</p><div class="calendly-inline-widget" data-url="{CALENDLY_FR}&hide_landing_page_details=1&hide_gdpr_banner=1"></div></section></main>"""

    # Écriture du Hub FR : coolpadel-web/fr/camaras/index.html
    (CAMERAS_FR / "index.html").write_text(page_fr("Caméras pour clubs de padel", hub_content, prefix="../../", extra_css=HUB_CSS), encoding="utf-8")
    print(f"[OK] Hub FR généré : {CAMERAS_FR / 'index.html'}")

    # 3. Génération des 20 articles FR
    article_by_slug = {a["slug"]: a for a in articles_list}

    for article in articles_list:
        slug = article["slug"]
        rel_slugs = RELATED_MAP.get(slug, [])
        related = [article_by_slug[s] for s in rel_slugs if s in article_by_slug]
        related_html = "\n".join(
            f'''<a href="../{a["slug"]}/" class="related-card"><div class="related-thumb"><img src="../../../../assets/images/camaras/{ARTICLE_IMAGES[a["slug"]]}" alt="{html.escape(a["title"])}" loading="lazy"></div><p class="related-title">{html.escape(a["title"])}</p></a>'''
            for a in related
        )

        image_name = ARTICLE_IMAGES[slug]

        video = ""
        if slug in FR_VIDEOS:
            v_title, v_desc, v_src = FR_VIDEOS[slug]
            video = f'<section class="video-section"><h2>{html.escape(v_title)}</h2><p>{html.escape(v_desc)}</p><iframe class="video-embed" src="{v_src}" title="{html.escape(v_title)}" loading="lazy" allowfullscreen></iframe></section>'
        elif slug == "por-que-no-recomiendo-plan-analytics":
            video = '<section class="video-section"><h2>Exemple en direct d\'analyses et statistiques par IA</h2><p>Vous pouvez consulter un rapport interactif réel avec carte de chaleur et analyse de frappes généré par l\'IA sur ce lien :</p><div style="margin-top:16px"><a href="https://savemyplay.com/replays/634779-ni9DexZC-the-club-at-monroe/analytics" target="_blank" rel="noopener noreferrer" style="display:inline-flex;align-items:center;gap:8px;padding:12px 20px;border-radius:999px;background:#f2920b;color:#0f172a;font-weight:900;text-decoration:none;font-size:14px;box-shadow:0 2px 8px rgba(0,0,0,0.08);">Voir l\'exemple en direct sur Save My Play &rarr;</a></div></section>'

        content = f"""<main><article class="article"><h1>{html.escape(article["title"])}</h1><img class="article-hero" src="../../../../assets/images/camaras/{image_name}" alt="{html.escape(article["title"])}" loading="lazy">{article_body_fr(article)}{video}<section class="related"><h2>Plus d'articles sur les caméras</h2><div class="related-grid">{related_html}</div></section><section class="next-step"><h2>Étape suivante</h2><p>Si vous hésitez encore, découvrez ci-dessus d'autres articles sur les caméras pour vous guider.</p><p>Si vous avez des questions et souhaitez voir en direct comment tout fonctionne, réservez votre créneau pour la démo.</p><div class="calendly-inline-widget" data-url="{CALENDLY_FR}&hide_landing_page_details=1&hide_gdpr_banner=1"></div></section></article></main>"""

        out_dir = ARTICLES_FR / slug
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.html").write_text(page_fr(article["title"], content, prefix="../../../../"), encoding="utf-8")

    print(f"[OK] 20 articles FR générés dans {ARTICLES_FR}")


if __name__ == "__main__":
    build_fr()
