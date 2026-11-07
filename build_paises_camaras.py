# -*- coding: utf-8 -*-
"""
Generador automático de las 50 Landings B2B de Países con pistas de pádel.
Aplica exactamente la estructura requerida por Javier:
- Conexión a la versión en inglés (/en/) en los enlaces del menú si no es ES.
- Sin mención a zanjas ni pulsadores incorrectos.
- Puntos clave: 180 € hardware en propiedad, 45 €/mes, no cámaras de vigilancia, sin obras, 0 permanencia.
- CTA directo a WhatsApp pre-configurado para demo.
"""

import os
import re
import urllib.parse
from paises_data import COUNTRIES
from country_i18n_dict import COUNTRY_I18N

BASE_TEMPLATE_PATH = 'coolpadel-web/camaras-grabacion-pistas-padel/index.html'
with open(BASE_TEMPLATE_PATH, 'r', encoding='utf-8') as f:
    template_raw = f.read()

OUTPUT_ROOT = 'coolpadel-web/camaras'

count_built = 0

for item in COUNTRIES:
    country_name_es = item["country_es"]
    country_local = item["country_local"]
    slug = item["slug"]
    lang = item["lang"]
    courts = item["courts"]
    
    # Get translation dictionary, fallback to 'en'
    t = COUNTRY_I18N.get(lang, COUNTRY_I18N["en"])
    
    country_display = country_local if lang != "es" else country_name_es
    
    title = t["title"].format(country=country_display)
    meta_desc = t["meta_desc"].format(country=country_display)
    h1 = t["h1"].format(country=country_display)
    sub = t["sub"].format(country=country_display)
    pricing_h2 = t["pricing_h2"].format(country=country_display)
    wa_msg = t["wa_msg"].format(country=country_display)
    
    # Target directory: coolpadel-web/camaras/{slug}/index.html
    out_dir = os.path.join(OUTPUT_ROOT, slug)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'index.html')
    
    canonical_url = f"https://coolpadelstudios.com/camaras/{slug}/"
    encoded_wa = urllib.parse.quote(wa_msg)
    wa_url = f"https://api.whatsapp.com/send?phone=34680317486&text={encoded_wa}"
    
    # Generate page HTML from template
    html = template_raw
    
    # Set html lang and dir if arabic
    if lang == 'ar':
        html = re.sub(r'<html lang="[^"]+"', f'<html lang="{lang}" dir="rtl"', html, count=1)
    else:
        html = re.sub(r'<html lang="[^"]+"', f'<html lang="{lang}"', html, count=1)
        
    # Title & Meta
    html = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', html, count=1)
    html = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{meta_desc}">', html, count=1)
    html = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{title}">', html, count=1)
    html = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{meta_desc}">', html, count=1)
    html = re.sub(r'<meta name="twitter:title" content=".*?">', f'<meta name="twitter:title" content="{title}">', html, count=1)
    html = re.sub(r'<meta name="twitter:description" content=".*?">', f'<meta name="twitter:description" content="{meta_desc}">', html, count=1)
    
    # Canonical
    html = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="{canonical_url}">', html, count=1)
    html = re.sub(r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="{canonical_url}">', html, count=1)
    
    # Nav header: If user clicks logo or camaras, link to /en/ if language is not ES
    if lang != 'es':
        html = html.replace('href="/"', 'href="/en/"')
        html = html.replace('href="/camaras/"', 'href="/en/camaras/"')
        html = html.replace('href="/blog/"', 'href="/en/blog/"')
        html = html.replace('href="/llaveros-padel-personalizados/"', 'href="/en/llaveros-padel-personalizados/"')
        html = html.replace('href="/franquicias-padel/"', 'href="/en/franquicias-padel/"')

    # Fix relative paths since page is nested under /camaras/{slug}/ (2 levels down)
    html = html.replace('href="../assets/', 'href="../../assets/')
    html = html.replace('src="../assets/', 'src="../../assets/')
    html = html.replace('url(\'../assets/', 'url(\'../../assets/')

    # Hero Badge, H1 and Subtitle
    html = re.sub(r'<span>TECNOLOGÍA DE CLUB · SAVE MY PLAY</span>', f'<span>{t["badge"]}</span>', html, count=1)
    html = re.sub(r'<h1 class="font-heading font-black text-3xl sm:text-5xl lg:text-6xl text-slate-950 uppercase tracking-tight leading-\[1\.08\]">.*?</h1>',
                  f'<h1 class="font-heading font-black text-3xl sm:text-5xl lg:text-6xl text-slate-950 uppercase tracking-tight leading-[1.08]">\n              {h1}\n            </h1>',
                  html, flags=re.DOTALL, count=1)
    html = re.sub(r'<p class="text-base sm:text-lg text-slate-600 leading-relaxed font-normal">.*?</p>',
                  f'<p class="text-base sm:text-lg text-slate-600 leading-relaxed font-normal">\n              {sub}\n            </p>',
                  html, flags=re.DOTALL, count=1)

    # 4 Points Summary Box
    html = re.sub(r'<span class="text-xs sm:text-sm font-bold text-slate-900">180 € / cámara en propiedad \(Pago único\)</span>',
                  f'<span class="text-xs sm:text-sm font-bold text-slate-900">{t["p1"]}</span>', html)
    html = re.sub(r'<span class="text-xs sm:text-sm font-bold text-slate-900">Desde 45 € / mes por pista \(Plan B Highlights\)</span>',
                  f'<span class="text-xs sm:text-sm font-bold text-slate-900">{t["p2"]}</span>', html)
    html = re.sub(r'<span class="text-xs sm:text-sm font-bold text-\[#f2920b\]">0 meses \(Cancelación libre mes a mes\)</span>',
                  f'<span class="text-xs sm:text-sm font-bold text-[#f2920b]">{t["p3"]}</span>', html)
    html = re.sub(r'<span class="text-xs sm:text-sm font-bold text-emerald-700">5 minutos sin obras ni zanjas en pista</span>',
                  f'<span class="text-xs sm:text-sm font-bold text-emerald-700">{t["p4"]}</span>', html)
                  
    # Clean up any mention of "zanjas"
    html = html.replace('sin zanjas ni obras civiles', 'sin obras')
    html = html.replace('sin zanjas', 'sin obras')
    html = html.replace('zanjas', 'obras')
    # Clean up any mention of "pulsador"
    html = html.replace('grabación automática con pulsador', 'grabación automática de partidos')
    html = html.replace('Pulsador físico de Highlights en Pista', 'Grabación Automática de Highlights')
    html = html.replace('Pulsador físico en red', 'Grabación inteligente')
    html = html.replace('Pulsador en red y escaneo QR inmediato sin descargar apps.', 'Escaneo QR inmediato sin descargar apps.')
    html = html.replace('repeticiones automáticas con pulsador', 'repeticiones automáticas')
    html = html.replace('pulsador en red', 'grabación automática')
    html = html.replace('pulsador', 'sistema')

    
    # WhatsApp links
    html = re.sub(r'href="https://api\.whatsapp\.com/send\?phone=34680317486[^"]*"', f'href="{wa_url}"', html)
    
    # CTA Buttons
    html = re.sub(r'<span>Solicitar Demo 15 min por WhatsApp</span>', f'<span>{t["demo_btn"]}</span>', html)
    html = re.sub(r'<span>Agendar Demo 15 min por WhatsApp</span>', f'<span>{t["demo_btn"]}</span>', html)
    html = re.sub(r'<span>Solicitar Demo en Directo por WhatsApp</span>', f'<span>{t["demo_btn"]}</span>', html)
    
    # Features Section
    html = re.sub(r'¿Por qué elegir Save My Play para tu club\?', t["features_h2"], html)
    html = re.sub(r'<h3 class="font-heading font-black text-xl sm:text-2xl text-slate-950 mb-2">Cero Obras y Montaje en 5 Minutos</h3>',
                  f'<h3 class="font-heading font-black text-xl sm:text-2xl text-slate-950 mb-2">{t["f1_title"]}</h3>', html)
    html = re.sub(r'<h3 class="font-heading font-black text-xl sm:text-2xl text-slate-950 mb-2">Pulsador Físico de Highlights en Pista</h3>',
                  f'<h3 class="font-heading font-black text-xl sm:text-2xl text-slate-950 mb-2">{t["f2_title"]}</h3>', html)
    html = re.sub(r'<h3 class="font-heading font-black text-xl sm:text-2xl text-slate-950 mb-2">Sin Contratos de Permanencia</h3>',
                  f'<h3 class="font-heading font-black text-xl sm:text-2xl text-slate-950 mb-2">{t["f3_title"]}</h3>', html)

    # FAQs
    html = re.sub(r'<span>¿Se necesitan obras o canalizaciones en el suelo\?</span>', f'<span>{t["faq1_q"]}</span>', html)
    html = re.sub(r'No\. El sistema se ancla directamente al poste de la pista.*?</p>', f'{t["faq1_a"]}</p>', html)
    
    html = re.sub(r'<span>¿Cuál es el precio y modelo de suscripción\?</span>', f'<span>{t["faq2_q"]}</span>', html)
    html = re.sub(r'Inversión única en hardware de 180 € por pista.*?</p>', f'{t["faq2_a"]}</p>', html)

    html = re.sub(r'<span>¿Cómo reciben los jugadores sus jugadas\?</span>', f'<span>{t["faq3_q"]}</span>', html)
    html = re.sub(r'El jugador pulsa el botón tras una jugada.*?</p>', f'{t["faq3_a"]}</p>', html)

    with open(out_path, 'w', encoding='utf-8') as f_out:
        f_out.write(html)
        
    count_built += 1
    print(f"[{count_built}/50] Generada landing país: /camaras/{slug}/ ({country_name_es} -> {lang})")

print(f"\n¡Éxito! Generadas las {count_built} landings de países.")
