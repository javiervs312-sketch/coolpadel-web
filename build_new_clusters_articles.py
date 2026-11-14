# -*- coding: utf-8 -*-
"""
Compilador Maestro de los Nuevos Artículos de Cámaras (Clústeres A, C e Integraciones).
Genera páginas bajo /camaras/{slug}/ y enlaza con el hub canónico.
"""

import json
import os
import re
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from new_clusters_articles_data import NEW_ARTICLES_CONTENT
from build_blog import get_silo_footer_html

ROOT = os.path.dirname(os.path.abspath(__file__))
SAMPLE_ARTICLE_PATH = os.path.join(ROOT, 'camaras', 'articulos', 'cuanto-cuesta-poner-camaras', 'index.html')

with open(SAMPLE_ARTICLE_PATH, 'r', encoding='utf-8') as f:
    sample_html = f.read()

header_match = re.search(r'(<!doctype html>.*?)(<main.*?>)', sample_html, re.DOTALL | re.IGNORECASE)
orig_header = header_match.group(1)
footer_match = re.search(r'(</main>.*</html>)', sample_html, re.DOTALL | re.IGNORECASE)
orig_footer = footer_match.group(1)

def build_article_page(art):
    slug = art["slug"]
    title = art["title"]
    meta_title = art["meta_title"]
    meta_desc = art["meta_desc"]
    h1 = art["h1"]
    hero_img = art["hero_img"]
    canonical_url = f"https://coolpadelstudios.com/camaras/{slug}/"

    # Preparar el Header adaptando canonicals, títulos y schema
    h = orig_header
    h = h.replace('https://coolpadelstudios.com/camaras/articulos/cuanto-cuesta-poner-camaras/', canonical_url)
    h = re.sub(r'<title>.*?</title>', f'<title>{meta_title} | Save My Play</title>', h)
    h = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{meta_desc}">', h)
    h = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{meta_title} | Save My Play">', h)
    h = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{meta_desc}">', h)
    h = re.sub(r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="{canonical_url}">', h)
    h = re.sub(r'<meta property="og:image" content=".*?">', f'<meta property="og:image" content="https://coolpadelstudios.com{hero_img}">', h)
    h = re.sub(r'<meta name="twitter:title" content=".*?">', f'<meta name="twitter:title" content="{meta_title} | Save My Play">', h)
    h = re.sub(r'<meta name="twitter:description" content=".*?">', f'<meta name="twitter:description" content="{meta_desc}">', h)
    h = re.sub(r'<meta name="twitter:image" content=".*?">', f'<meta name="twitter:image" content="https://coolpadelstudios.com{hero_img}">', h)
    
    # Adaptar Schema JSON-LD completo sin residuos de plantilla
    clean_intro = re.sub(r'<[^>]+>', '', art["intro_p"]).strip()
    schema_obj = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Article",
                "headline": meta_title,
                "alternativeHeadline": title,
                "description": meta_desc,
                "image": [f"https://coolpadelstudios.com{hero_img}"],
                "datePublished": "2026-10-15T09:00:00+02:00",
                "dateModified": "2026-11-11T09:00:00+01:00",
                "mainEntityOfPage": canonical_url,
                "inLanguage": "es",
                "speakable": {
                    "@type": "SpeakableSpecification",
                    "cssSelector": [".article-title", ".article-body p:first-of-type"]
                },
                "author": {
                    "@type": "Person",
                    "name": "Javier Villoria",
                    "jobTitle": "Founder & B2B Director",
                    "url": "https://www.linkedin.com/in/javier-villoria-soleto-606737298/"
                },
                "publisher": {
                    "@type": "Organization",
                    "name": "CoolPadel Studios",
                    "url": "https://coolpadelstudios.com",
                    "logo": "https://coolpadelstudios.com/assets/images/coolpadel-mascot-hd.png",
                    "sameAs": [
                        "https://www.instagram.com/coolpadel_/",
                        "https://www.linkedin.com/in/javier-villoria-soleto-606737298/",
                        "https://maps.google.com/?cid=5000443597205028051"
                    ]
                }
            },
            {
                "@type": "BreadcrumbList",
                "@id": f"{canonical_url}#breadcrumb",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://coolpadelstudios.com/"},
                    {"@type": "ListItem", "position": 2, "name": "Cámaras", "item": "https://coolpadelstudios.com/camaras/"},
                    {"@type": "ListItem", "position": 3, "name": title, "item": canonical_url}
                ]
            },
            {
                "@type": "FAQPage",
                "mainEntity": [{
                    "@type": "Question",
                    "name": h1,
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": f"{meta_desc} {clean_intro}"
                    }
                }]
            }
        ]
    }
    schema_script = f'<script type="application/ld+json">\n{json.dumps(schema_obj, ensure_ascii=False, indent=2)}\n</script>'
    h = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda _: schema_script, h, count=1, flags=re.DOTALL)
    
    # Alternates canónicos en otros idiomas hacia el hub
    h = re.sub(r'<link rel="alternate" hreflang="es".*?>', f'<link rel="alternate" hreflang="es" href="{canonical_url}">', h)
    h = re.sub(r'<link rel="alternate" hreflang="en".*?>', f'<link rel="alternate" hreflang="en" href="https://coolpadelstudios.com/en/camaras/">', h)
    h = re.sub(r'<link rel="alternate" hreflang="fr".*?>', f'<link rel="alternate" hreflang="fr" href="https://coolpadelstudios.com/fr/camaras/">', h)
    h = re.sub(r'<link rel="alternate" hreflang="it".*?>', f'<link rel="alternate" hreflang="it" href="https://coolpadelstudios.com/it/camaras/">', h)
    h = re.sub(r'<link rel="alternate" hreflang="de".*?>', f'<link rel="alternate" hreflang="de" href="https://coolpadelstudios.com/de/camaras/">', h)
    h = re.sub(r'<link rel="alternate" hreflang="x-default".*?>', f'<link rel="alternate" hreflang="x-default" href="{canonical_url}">', h)

    # Reemplazar enlaces del menú desplegable de idioma
    h = h.replace('/en/camaras/articulos/cuanto-cuesta-poner-camaras/', '/en/camaras/')
    h = h.replace('/fr/camaras/articulos/cuanto-cuesta-poner-camaras/', '/fr/camaras/')
    h = h.replace('/it/camaras/articulos/cuanto-cuesta-poner-camaras/', '/it/camaras/')
    h = h.replace('/de/camaras/articulos/cuanto-cuesta-poner-camaras/', '/de/camaras/')
    h = h.replace('/camaras/articulos/cuanto-cuesta-poner-camaras/', f'/camaras/{slug}/')

    # Cuerpo del artículo
    body_blocks_html = "\n".join(art["blocks"])

    # Artículos recomendados rotativos entre los 8 clústeres y artículos core
    all_cluster_items = list(NEW_ARTICLES_CONTENT.values())
    other_clusters = [item for item in all_cluster_items if item["slug"] != slug]
    idx_self = next((idx for idx, item in enumerate(all_cluster_items) if item["slug"] == slug), 0)
    picked = [
        other_clusters[idx_self % len(other_clusters)],
        other_clusters[(idx_self + 2) % len(other_clusters)],
        other_clusters[(idx_self + 4) % len(other_clusters)],
    ]
    related_cards = "\n".join(
        f'''      <a href="../{p["slug"]}/" class="related-card">
        <img src="{p["hero_img"]}" alt="{p["title"]}" loading="lazy">
        <p class="related-card-title">{p["title"]}</p>
      </a>'''
        for p in picked
    )

    main_html = f"""<main class="article-container">
  <!-- BREADCRUMB VISUAL -->
  <nav class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-slate-100 border border-slate-200/80 text-xs font-semibold text-slate-600 mb-6 flex-wrap" aria-label="Breadcrumb">
    <a href="/" class="hover:text-[#f2920b] transition">Home</a>
    <i data-lucide="chevron-right" class="w-3.5 h-3.5 text-slate-400"></i>
    <a href="/camaras/" class="hover:text-[#f2920b] transition">Volver a Cámaras</a>
    <i data-lucide="chevron-right" class="w-3.5 h-3.5 text-slate-400"></i>
    <span class="text-slate-900 font-bold truncate max-w-[240px] sm:max-w-none">{title}</span>
  </nav>

  <div class="article-header">
    <h1 class="article-title">{h1}</h1>
    <img src="{hero_img}" alt="{title}" class="article-hero-img" width="800" height="450">
  </div>

  <div class="article-body">
    <div class="article-block">
      <p class="text-base sm:text-lg font-medium text-slate-700 leading-relaxed">{art["intro_p"]}</p>
    </div>
    {body_blocks_html}
  </div>

  <div class="cta-box">
    <h2>Siguiente paso:</h2>
    <p>Si tienes alguna pregunta y quieres que te enseñe bien cómo funciona todo, escríbeme directamente y lo vemos.</p>
    <div class="mt-4 flex justify-center">
      <a href="https://wa.me/34680317486?text=Hola%20Javier%2C%20%C2%BFpuedo%20agendar%20una%20demo%20para%20las%20c%C3%A1maras%20de%20mi%20club%3F" target="_blank" rel="noopener noreferrer" class="inline-flex items-center justify-center gap-2.5 px-8 py-3.5 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-sm uppercase tracking-wider transition-all duration-300 shadow-md hover:scale-105 active:scale-95 group">
        <i data-lucide="message-circle" class="w-5 h-5 text-slate-950 stroke-[2.5]"></i>
        <span>¿Puedo agendar una demo?</span>
      </a>
    </div>
  </div>

  <div class="related-section">
    <h2 class="related-title">Artículos recomendados</h2>
    <div class="related-grid">
{related_cards}
    </div>
  </div>
</main>"""

    # Footer actualizado desde get_silo_footer_html
    footer_Html = get_silo_footer_html(root_prefix="/")
    f_html = re.sub(r'<footer.*?</footer>', lambda _: footer_Html.strip(), orig_footer, count=1, flags=re.DOTALL)

    return f"{h}\n{main_html}\n{f_html}"

def build_all_new_articles():
    out_dir = os.path.join(ROOT, 'camaras')
    built = 0
    urls = []
    
    for slug, art in NEW_ARTICLES_CONTENT.items():
        target_dir = os.path.join(out_dir, slug)
        os.makedirs(target_dir, exist_ok=True)
        html = build_article_page(art)
        file_path = os.path.join(target_dir, 'index.html')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)
        built += 1
        url = f"https://coolpadelstudios.com/camaras/{slug}/"
        urls.append(url)
        print(f"OK [Artículo] -> /camaras/{slug}/")

    print(f"\n¡Completados {built} nuevos artículos estratégicos de cámaras!")
    return urls

if __name__ == '__main__':
    build_all_new_articles()
