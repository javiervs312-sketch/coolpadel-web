# -*- coding: utf-8 -*-
"""
Compilador Maestro de los Nuevos Artículos de Cámaras (Clústeres A, C e Integraciones).
Genera páginas bajo /camaras/{slug}/ y enlaza con el hub canónico.
"""

import os
import re
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from new_clusters_articles_data import NEW_ARTICLES_CONTENT

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
    
    # Adaptar Schema JSON-LD
    h = re.sub(r'"headline":\s*".*?"', f'"headline": "{meta_title}"', h)
    h = re.sub(r'"alternativeHeadline":\s*".*?"', f'"alternativeHeadline": "{title}"', h)
    h = re.sub(r'"image":\s*\[".*?"\]', f'"image": ["https://coolpadelstudios.com{hero_img}"]', h)
    h = re.sub(r'"mainEntityOfPage":\s*".*?"', f'"mainEntityOfPage": "{canonical_url}"', h)
    h = re.sub(r'"@id":\s*".*?#breadcrumb"', f'"@id": "{canonical_url}#breadcrumb"', h)
    
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

    main_html = f"""<main class="article-container">
  <!-- BREADCRUMB VISUAL -->
  <nav class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-slate-100 border border-slate-200/80 text-xs font-semibold text-slate-600 mb-6 flex-wrap" aria-label="Breadcrumb">
    <a href="/" class="hover:text-[#f2920b] transition">Home</a>
    <i data-lucide="chevron-right" class="w-3.5 h-3.5 text-slate-400"></i>
    <a href="../" class="hover:text-[#f2920b] transition">Volver a Cámaras</a>
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
    <p>Si tienes alguna pregunta y quieres que te enseñe bien cómo funciona todo en directo, busca tu hueco para la demo.</p>
    <div class="calendly-wrapper"><div class="calendly-inline-widget" data-url="https://calendly.com/javier-vs-312/demo-save-my-play?locale=es&hide_landing_page_details=1&hide_gdpr_banner=1&hide_event_type_details=1&primary_color=f2920b"></div></div>
  </div>

  <div class="related-section">
    <h2 class="related-title">Artículos recomendados</h2>
    <div class="related-grid">
      <a href="../save-my-play-vs-camaras-vigilancia/" class="related-card">
        <img src="/assets/images/camaras/camera-05.jpg" alt="Cámaras de Pádel vs Videovigilancia CCTV" loading="lazy">
        <p class="related-card-title">Cámaras de Pádel vs Videovigilancia CCTV</p>
      </a>
      <a href="../cuanto-cuesta-poner-camaras-pistas-padel/" class="related-card">
        <img src="/assets/images/camaras/pista-moqueta-negra-indoor.png" alt="¿Cuánto Cuesta Poner Cámaras de Pádel?" loading="lazy">
        <p class="related-card-title">¿Cuánto Cuesta y Qué ROI Tienen las Cámaras?</p>
      </a>
      <a href="../save-my-play-vs-sistemas-con-obras/" class="related-card">
        <img src="/assets/images/camaras/camara-instalada-reja-4m-crop.jpg" alt="Instalación Sin Obras en 5 Minutos" loading="lazy">
        <p class="related-card-title">Sistemas Sin Obras vs Instalaciones Tradicionales</p>
      </a>
    </div>
  </div>
</main>"""

    # Footer
    f_html = orig_footer

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
