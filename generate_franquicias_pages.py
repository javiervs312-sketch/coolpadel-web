#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de Páginas Individuales para cada Franquicia y Cadena de Pádel.
Lee dataset_franquicias.py y genera coolpadel-web/franquicias-padel/<id>/index.html
para cada una de las 167 franquicias.
"""

import os
import sys
import json
import html

if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Importar dataset
from dataset_franquicias import FRANQUICIAS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRANQUICIAS_DIR = os.path.join(BASE_DIR, "franquicias-padel")


def escape_txt(text):
    if not text:
        return ""
    return html.escape(str(text))


def generate_single_page(f):
    fid = f["id"]
    nombre = f["nombre"]
    pais = f["pais"]
    pais_codigo = f.get("pais_codigo", "ES")
    bandera = f.get("bandera", "🎾")
    ciudad = f.get("ciudad_sede", "")
    modelo = f.get("modelo", "Cadena Multiclub")
    badge_cls = f.get("modelo_badge", "bg-sky-100 text-sky-800 border-sky-200")
    num_clubs = f.get("num_clubs", "N/A")
    num_pistas = f.get("num_pistas", "N/A")
    software = f.get("software", "Software estándar")
    fundadores = f.get("fundadores", "N/D")
    web = f.get("web", "https://coolpadelstudios.com/franquicias-padel/")
    tagline = f.get("tagline", "")
    resumen = f.get("resumen", "")
    sedes = f.get("sedes_principales", [])
    sub_clubs = f.get("sub_clubs", [])
    diferencial = f.get("diferencial", "")

    tech = f.get("tecnologia_pistas", {})
    exp = f.get("modelo_expansion", {})

    pistas_desc = tech.get("pistas", "Pistas de pádel reglamentarias")
    software_desc = tech.get("software", software)
    domotica_desc = tech.get("domotica", "Accesos automatizados")
    grabacion_desc = tech.get("grabacion", "Compatible con cámaras fijas autónomas Save my Play")
    restauracion_desc = tech.get("restauracion", "Zona social y cafetería")

    tipo_contrato = exp.get("tipo_contrato", "Cadena propia y/o franquicia")
    perfil_club = exp.get("perfil_club", "Naves industriales y clubes deportivos")
    canon_royalties = exp.get("canon_royalties", "Consultar condiciones")
    inversion_media = exp.get("inversion_media", "A convenir")

    canonical_url = f"https://coolpadelstudios.com/franquicias-padel/{fid}/"
    wa_msg = f"Hola Javier, estoy viendo la ficha de {nombre} en el directorio de franquicias y quiero consultar sobre equipamiento de cámaras Save my Play y llaveros 3D."
    import urllib.parse
    wa_url = f"https://api.whatsapp.com/send?phone=34658145887&text={urllib.parse.quote(wa_msg)}"

    # Sedes HTML
    sedes_items = []
    if sub_clubs:
        for sc in sub_clubs[:12]:
            s_nom = sc.get("nombre", "")
            s_ciu = sc.get("ciudad", "")
            s_pis = sc.get("pistas", "")
            extra = f" ({s_pis})" if s_pis else ""
            sedes_items.append(f'<li class="flex items-start gap-2.5 py-1.5"><i data-lucide="map-pin" class="w-4 h-4 text-[#f2920b] shrink-0 mt-0.5"></i><span><strong>{escape_txt(s_nom)}</strong> ({escape_txt(s_ciu)}){escape_txt(extra)}</span></li>')
        if len(sub_clubs) > 12:
            sedes_items.append(f'<li class="text-xs text-slate-500 font-bold italic pt-2">+ {len(sub_clubs) - 12} centros adicionales verificados en red.</li>')
    elif sedes:
        for s in sedes[:12]:
            sedes_items.append(f'<li class="flex items-start gap-2.5 py-1.5"><i data-lucide="map-pin" class="w-4 h-4 text-[#f2920b] shrink-0 mt-0.5"></i><span>{escape_txt(s)}</span></li>')
    else:
        sedes_items.append(f'<li class="flex items-start gap-2.5 py-1.5"><i data-lucide="map-pin" class="w-4 h-4 text-[#f2920b] shrink-0 mt-0.5"></i><span>Instalaciones en {escape_txt(ciudad)}, {escape_txt(pais)}</span></li>')
    sedes_html = "\n".join(sedes_items)

    meta_desc = f"Ficha oficial de {nombre} ({pais}): {num_clubs}, {num_pistas}, software {software.split('/')[0].strip()}, modelo {modelo} y requisitos técnicos de instalación."
    if len(meta_desc) > 158:
        meta_desc = meta_desc[:155] + "..."

    page_html = f"""<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{escape_txt(nombre)} - Cadena y Franquicia de Pádel ({escape_txt(pais)}) | CoolPadel Studios</title>
  <meta name="description" content="{escape_txt(meta_desc)}">
  <link rel="canonical" href="{canonical_url}">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="CoolPadel Studios">
  <meta property="og:locale" content="es_ES">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:title" content="{escape_txt(nombre)} - Franquicia de Pádel ({escape_txt(pais)})">
  <meta property="og:description" content="{escape_txt(meta_desc)}">
  <meta property="og:image" content="https://coolpadelstudios.com/assets/images/savemyplay-1.jpg">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{escape_txt(nombre)} | Directorio de Franquicias de Pádel">
  <meta name="twitter:description" content="{escape_txt(meta_desc)}">
  <meta name="twitter:image" content="https://coolpadelstudios.com/assets/images/savemyplay-1.jpg">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">

  <!-- Favicon -->
  <link rel="icon" type="image/png" href="../../assets/images/favicon_transparente.png?v=transp3">
  <link rel="apple-touch-icon" sizes="180x180" href="../../assets/images/favicon_transparente.png?v=transp3">
  <meta name="theme-color" content="#0b1626">

  <!-- LLM & AI Discovery -->
  <link rel="alternate" type="text/markdown" href="https://coolpadelstudios.com/llms.txt" title="LLMs.txt">
  <link rel="alternate" type="text/markdown" href="https://coolpadelstudios.com/llms-full.txt" title="LLMs-Full.txt">

  <!-- Tailwind CSS & Lucide Icons -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/lucide@0.468.0/dist/umd/lucide.min.js"></script>

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">

  <!-- Microsoft Clarity -->
  <script type="text/javascript">
    (function(c,l,a,r,i,t,y){{
      c[a]=c[a]||function(){{(c[a].q=c[a].q||[]).push(arguments)}};
      t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
      y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    }})(window, document, "clarity", "script", "q7p8g52y9e");
  </script>

  <!-- Schema.org SportsOrganization, BreadcrumbList & FAQPage -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "SportsOrganization",
        "@id": "{canonical_url}#organization",
        "name": "{escape_txt(nombre)}",
        "description": "{escape_txt(resumen or tagline)}",
        "url": "{web}",
        "address": {{
          "@type": "PostalAddress",
          "addressLocality": "{escape_txt(ciudad)}",
          "addressCountry": "{pais_codigo}"
        }},
        "parentOrganization": {{
          "@type": "Organization",
          "name": "CoolPadel Studios",
          "url": "https://coolpadelstudios.com"
        }}
      }},
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{
            "@type": "ListItem",
            "position": 1,
            "name": "Inicio",
            "item": "https://coolpadelstudios.com/"
          }},
          {{
            "@type": "ListItem",
            "position": 2,
            "name": "Directorio de Franquicias de Pádel",
            "item": "https://coolpadelstudios.com/franquicias-padel/"
          }},
          {{
            "@type": "ListItem",
            "position": 3,
            "name": "{escape_txt(nombre)}",
            "item": "{canonical_url}"
          }}
        ]
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "¿Cuántos centros y pistas opera {escape_txt(nombre)}?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{escape_txt(nombre)} cuenta con una red de {escape_txt(num_clubs)} y un parque total estimado de {escape_txt(num_pistas)} en {escape_txt(pais)}."
            }}
          }},
          {{
            "@type": "Question",
            "name": "¿Qué software de reservas utiliza {escape_txt(nombre)}?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{escape_txt(nombre)} gestiona sus pistas con {escape_txt(software)}, permitiendo reservas para socios y jugadores."
            }}
          }},
          {{
            "@type": "Question",
            "name": "¿Es compatible {escape_txt(nombre)} con las cámaras de grabación Save my Play?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Sí. Save my Play se fija en los postes de las pistas de {escape_txt(nombre)} sin obras ni canalizaciones (180 € hardware y 45 €/mes software), compatible con cualquier software de reservas."
            }}
          }}
        ]
      }}
    ]
  }}
  </script>

  <style>
    body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
    h1, h2, h3, h4, .font-heading {{ font-family: 'Outfit', sans-serif; }}
  </style>
</head>
<body class="bg-slate-50 text-slate-900 antialiased selection:bg-[#f2920b] selection:text-slate-950">

  <!-- Top Nav -->
  <header class="border-b border-slate-200 bg-white sticky top-0 z-50 shadow-2xs">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 h-16 sm:h-20 flex items-center justify-between">
      <a href="/" class="flex items-center gap-2.5 sm:gap-3 group">
        <img src="../../assets/images/coolpadel-mascot-hd.png" alt="CoolPadel Studios" class="w-9 h-9 sm:w-10 sm:h-10 object-contain">
        <div>
          <span class="font-heading font-black text-lg sm:text-xl text-slate-950 tracking-tight flex items-center gap-1">
            COOLPADEL <span class="text-[#f2920b]">STUDIOS</span>
          </span>
          <span class="text-[9px] sm:text-[10px] text-slate-500 block tracking-widest font-bold uppercase">Directorio Oficial de Franquicias</span>
        </div>
      </a>
      <div class="flex items-center gap-3">
        <a href="/franquicias-padel/" class="inline-flex items-center gap-1.5 text-xs sm:text-sm font-bold text-slate-700 hover:text-[#f2920b] transition">
          <i data-lucide="layers" class="w-4 h-4 text-[#f2920b]"></i>
          <span class="hidden sm:inline">Ver +167 Franquicias</span>
          <span class="sm:hidden">Directorio</span>
        </a>
        <a href="{wa_url}" target="_blank" rel="noopener"
           class="inline-flex items-center gap-1.5 bg-[#25D366] hover:bg-[#20ba5a] text-slate-950 font-black px-3.5 py-2 rounded-xl text-xs sm:text-sm transition shadow-sm">
          <i data-lucide="message-circle" class="w-4 h-4"></i>
          <span>Consultar</span>
        </a>
      </div>
    </div>
  </header>

  <!-- Breadcrumbs -->
  <nav class="max-w-5xl mx-auto px-4 sm:px-6 pt-6 pb-2 text-xs text-slate-500 flex items-center gap-2 flex-wrap" aria-label="Breadcrumb">
    <a href="/" class="hover:text-slate-900 transition">Inicio</a>
    <i data-lucide="chevron-right" class="w-3.5 h-3.5 text-slate-400"></i>
    <a href="/franquicias-padel/" class="hover:text-slate-900 transition">Franquicias de Pádel</a>
    <i data-lucide="chevron-right" class="w-3.5 h-3.5 text-slate-400"></i>
    <span class="text-[#f2920b] font-bold">{escape_txt(nombre)}</span>
  </nav>

  <!-- Contenedor Principal -->
  <main class="max-w-5xl mx-auto px-4 sm:px-6 py-6 pb-16">

    <!-- Hero Card -->
    <div class="bg-white rounded-3xl p-6 sm:p-10 border border-slate-200/90 shadow-sm mb-8">
      <div class="flex items-start justify-between gap-4 flex-wrap mb-4">
        <div class="flex items-center gap-2">
          <span class="text-3xl sm:text-4xl">{bandera}</span>
          <span class="inline-block px-3 py-1 rounded-full text-xs font-bold border {badge_cls}">
            {escape_txt(modelo)}
          </span>
          <span class="text-xs font-bold text-slate-400 bg-slate-100 px-2.5 py-1 rounded-md">
            {escape_txt(pais)}
          </span>
        </div>
        <a href="/franquicias-padel/" class="text-xs font-bold text-slate-500 hover:text-slate-900 flex items-center gap-1 transition">
          <i data-lucide="arrow-left" class="w-3.5 h-3.5"></i>
          <span>Volver al Directorio Completo</span>
        </a>
      </div>

      <h1 class="text-3xl sm:text-5xl font-heading font-black text-slate-950 tracking-tight mb-3">
        {escape_txt(nombre)}
      </h1>
      <p class="text-xs sm:text-sm font-semibold text-slate-500 flex items-center gap-1.5 mb-5">
        <i data-lucide="map-pin" class="w-4 h-4 text-[#f2920b]"></i>
        <span>Sede Principal: <strong>{escape_txt(ciudad)}</strong> ({escape_txt(pais)}) · Promotores: {escape_txt(fundadores)}</span>
      </p>

      {f'<p class="text-base sm:text-lg text-slate-700 font-medium leading-relaxed mb-6 border-l-4 border-[#f2920b] pl-4">{escape_txt(tagline)}</p>' if tagline else ''}

      <p class="text-slate-600 text-sm sm:text-base leading-relaxed mb-8">
        {escape_txt(resumen)}
      </p>

      <!-- Métricas Clave Grid -->
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 p-4 bg-slate-50 rounded-2xl border border-slate-200/80 mb-6">
        <div>
          <span class="block text-[11px] uppercase font-bold text-slate-400 mb-0.5">Clubes / Sedes</span>
          <span class="font-heading font-black text-lg sm:text-xl text-slate-950">{escape_txt(num_clubs)}</span>
        </div>
        <div>
          <span class="block text-[11px] uppercase font-bold text-slate-400 mb-0.5">Pistas Totales</span>
          <span class="font-heading font-black text-lg sm:text-xl text-slate-950">{escape_txt(num_pistas)}</span>
        </div>
        <div>
          <span class="block text-[11px] uppercase font-bold text-slate-400 mb-0.5">Software</span>
          <span class="font-heading font-bold text-sm sm:text-base text-slate-800 truncate block" title="{escape_txt(software)}">{escape_txt(software.split('/')[0].strip())}</span>
        </div>
        <div>
          <span class="block text-[11px] uppercase font-bold text-slate-400 mb-0.5">Inversión Media</span>
          <span class="font-heading font-bold text-xs sm:text-sm text-slate-800">{escape_txt(inversion_media)}</span>
        </div>
      </div>

      <!-- Botones de Acción -->
      <div class="flex items-center gap-3 flex-wrap">
        <a href="{wa_url}" target="_blank" rel="noopener"
           class="inline-flex items-center justify-center gap-2 bg-[#25D366] hover:bg-[#20ba5a] text-slate-950 font-black px-6 py-3.5 rounded-xl text-xs sm:text-sm transition shadow-sm">
          <i data-lucide="message-circle" class="w-4 h-4"></i>
          <span>Consultar Equipamiento para {escape_txt(nombre)}</span>
        </a>
        {f'<a href="{web}" target="_blank" rel="noopener nofollow" class="inline-flex items-center justify-center gap-2 bg-slate-100 hover:bg-slate-200 text-slate-800 font-bold px-5 py-3.5 rounded-xl text-xs sm:text-sm border border-slate-200 transition"><i data-lucide="globe" class="w-4 h-4 text-slate-500"></i><span>Web Oficial</span><i data-lucide="external-link" class="w-3.5 h-3.5 text-slate-400"></i></a>' if web and web != "https://coolpadelstudios.com/franquicias-padel/" else ''}
      </div>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8">
      
      <!-- Bloque 1: Sedes Principales -->
      <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200/90 shadow-sm flex flex-col justify-between">
        <div>
          <h2 class="text-xl font-heading font-black text-slate-950 mb-4 flex items-center gap-2">
            <i data-lucide="building-2" class="w-5 h-5 text-[#f2920b]"></i>
            <span>Sedes y Complejos de Referencia</span>
          </h2>
          <ul class="text-slate-700 text-sm divide-y divide-slate-100">
            {sedes_html}
          </ul>
        </div>
        <div class="pt-4 mt-4 border-t border-slate-100 text-xs text-slate-500 flex items-center justify-between">
          <span>Datos auditados en censo continuo 2026</span>
          <a href="/franquicias-padel/" class="text-[#f2920b] font-bold hover:underline">Ver mapa global →</a>
        </div>
      </div>

      <!-- Bloque 2: Modelo de Negocio y Expansión -->
      <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200/90 shadow-sm flex flex-col justify-between">
        <div>
          <h2 class="text-xl font-heading font-black text-slate-950 mb-4 flex items-center gap-2">
            <i data-lucide="briefcase" class="w-5 h-5 text-[#f2920b]"></i>
            <span>Modelo de Expansión & Inversores</span>
          </h2>
          <div class="space-y-3 text-sm text-slate-700">
            <div class="p-3 bg-slate-50 rounded-xl border border-slate-100">
              <span class="block text-[11px] font-bold uppercase text-slate-400 mb-0.5">Tipo de Contrato</span>
              <span class="font-semibold text-slate-900">{escape_txt(tipo_contrato)}</span>
            </div>
            <div class="p-3 bg-slate-50 rounded-xl border border-slate-100">
              <span class="block text-[11px] font-bold uppercase text-slate-400 mb-0.5">Perfil de Club Idóneo</span>
              <span class="text-slate-800">{escape_txt(perfil_club)}</span>
            </div>
            <div class="p-3 bg-slate-50 rounded-xl border border-slate-100">
              <span class="block text-[11px] font-bold uppercase text-slate-400 mb-0.5">Canon & Royalties</span>
              <span class="text-slate-800">{escape_txt(canon_royalties)}</span>
            </div>
            {f'<div class="p-3 bg-amber-50/60 rounded-xl border border-amber-200/60"><span class="block text-[11px] font-bold uppercase text-amber-700 mb-0.5">Diferencial Competitivo</span><span class="text-slate-800">{escape_txt(diferencial)}</span></div>' if diferencial else ''}
          </div>
        </div>
      </div>

    </div>

    <!-- Bloque 3: Especificaciones Técnicas y Compatibilidad de Pista -->
    <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200/90 shadow-sm mb-8">
      <h2 class="text-xl font-heading font-black text-slate-950 mb-6 flex items-center gap-2">
        <i data-lucide="cpu" class="w-5 h-5 text-[#3478a6]"></i>
        <span>Especificaciones Técnicas de Instalación</span>
      </h2>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 text-xs sm:text-sm">
        <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200/70">
          <span class="block font-bold text-slate-900 mb-1 flex items-center gap-1.5">
            <i data-lucide="box" class="w-4 h-4 text-slate-500"></i>
            <span>Pistas y Cubiertas</span>
          </span>
          <span class="text-slate-600 leading-relaxed block">{escape_txt(pistas_desc)}</span>
        </div>
        <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200/70">
          <span class="block font-bold text-slate-900 mb-1 flex items-center gap-1.5">
            <i data-lucide="smartphone" class="w-4 h-4 text-slate-500"></i>
            <span>Software y App</span>
          </span>
          <span class="text-slate-600 leading-relaxed block">{escape_txt(software_desc)}</span>
        </div>
        <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200/70">
          <span class="block font-bold text-slate-900 mb-1 flex items-center gap-1.5">
            <i data-lucide="key" class="w-4 h-4 text-slate-500"></i>
            <span>Domótica y Accesos</span>
          </span>
          <span class="text-slate-600 leading-relaxed block">{escape_txt(domotica_desc)}</span>
        </div>
        <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200/70">
          <span class="block font-bold text-slate-900 mb-1 flex items-center gap-1.5">
            <i data-lucide="video" class="w-4 h-4 text-slate-500"></i>
            <span>Grabación de Partidos</span>
          </span>
          <span class="text-slate-600 leading-relaxed block">{escape_txt(grabacion_desc)}</span>
        </div>
        <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200/70 col-span-1 sm:col-span-2">
          <span class="block font-bold text-slate-900 mb-1 flex items-center gap-1.5">
            <i data-lucide="coffee" class="w-4 h-4 text-slate-500"></i>
            <span>Hospitality & Pro-Shop</span>
          </span>
          <span class="text-slate-600 leading-relaxed block">{escape_txt(restauracion_desc)}</span>
        </div>
      </div>
    </div>

    <!-- Módulo B2B: Soluciones CoolPadel para esta Cadena -->
    <div class="bg-gradient-to-br from-[#0b1626] to-[#152e4d] rounded-3xl p-6 sm:p-10 text-white shadow-xl mb-8">
      <div class="max-w-3xl">
        <span class="inline-block px-3 py-1 rounded-full bg-[#f2920b] text-slate-950 font-black text-xs uppercase tracking-wider mb-4">
          EQUIPAMIENTO B2B OFICIAL
        </span>
        <h2 class="text-2xl sm:text-3xl font-heading font-black mb-3">
          ¿Gestionas o estás abriendo un centro de {escape_txt(nombre)}?
        </h2>
        <p class="text-slate-300 text-sm sm:text-base leading-relaxed mb-6">
          CoolPadel Studios suministra la tecnología de pista y el merchandising oficial para que los clubes de la red aumenten su facturación por partido y fidelicen a sus jugadores:
        </p>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-8">
          <div class="p-4 bg-white/10 rounded-2xl border border-white/15 backdrop-blur">
            <div class="flex items-center gap-2 mb-2 text-[#f2920b] font-bold text-sm">
              <i data-lucide="video" class="w-4 h-4"></i>
              <span>Cámaras Save my Play sin obras</span>
            </div>
            <p class="text-xs text-slate-300 leading-relaxed">
              180 € hardware por pista y 45 €/mes. Pulsador en poste, descarga QR y streaming a YouTube sin tocar cableado ni hacer zanjas.
            </p>
          </div>
          <div class="p-4 bg-white/10 rounded-2xl border border-white/15 backdrop-blur">
            <div class="flex items-center gap-2 mb-2 text-[#f2920b] font-bold text-sm">
              <i data-lucide="tag" class="w-4 h-4"></i>
              <span>Llaveros 3D de Goma Oficiales</span>
            </div>
            <p class="text-xs text-slate-300 leading-relaxed">
              Llaveros de pala en relieve tridimensional con el escudo del club. Muestra previa en 15 días laborables por 15€ descontables del pedido.
            </p>
          </div>
        </div>

        <div class="flex items-center gap-4 flex-wrap">
          <a href="{wa_url}" target="_blank" rel="noopener"
             class="inline-flex items-center justify-center gap-2 bg-[#25D366] hover:bg-[#20ba5a] text-slate-950 font-black px-6 py-3.5 rounded-xl text-xs sm:text-sm transition">
            <i data-lucide="message-circle" class="w-4 h-4"></i>
            <span>Hablar con Javier sobre {escape_txt(nombre)}</span>
          </a>
          <a href="/camaras/" 
             class="inline-flex items-center justify-center gap-2 bg-white/10 hover:bg-white/20 text-white font-bold px-5 py-3.5 rounded-xl text-xs sm:text-sm border border-white/20 transition">
            <span>Ver Especificaciones Save my Play</span>
          </a>
        </div>
      </div>
    </div>

    <!-- Enlaces de Retorno y Directorio -->
    <div class="text-center py-6">
      <a href="/franquicias-padel/" class="inline-flex items-center gap-2 text-sm font-bold text-slate-600 hover:text-[#f2920b] transition">
        <i data-lucide="arrow-left" class="w-4 h-4"></i>
        <span>Volver al Directorio y Comparador de 167 Franquicias de Pádel</span>
      </a>
    </div>

  </main>

  <!-- Footer Oficial -->
  <footer class="border-t border-slate-200 bg-white py-12 text-xs text-slate-500">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 flex flex-col sm:flex-row items-center justify-between gap-6">
      <div class="flex items-center gap-3">
        <img src="../../assets/images/coolpadel-mascot-hd.png" alt="CoolPadel Studios" class="w-8 h-8 object-contain">
        <div>
          <span class="font-heading font-black text-sm text-slate-900">COOLPADEL STUDIOS</span>
          <span class="block text-[11px] text-slate-500">Distribuidor Oficial Save my Play · Madrid (España)</span>
        </div>
      </div>
      <div class="flex flex-wrap justify-center gap-6 text-slate-600">
        <a href="/" class="hover:text-slate-900 transition">Inicio</a>
        <a href="/camaras/" class="hover:text-slate-900 transition">Cámaras Pistas</a>
        <a href="/franquicias-padel/" class="hover:text-slate-900 transition">Directorio Franquicias</a>
        <a href="/blog/barometro-camaras-padel-2026/" class="hover:text-slate-900 transition">Barómetro 2026</a>
        <a href="https://coolpadelstudios.com/llms.txt" class="hover:text-slate-900 transition">LLMs.txt</a>
      </div>
      <p class="text-[11px]">© 2026 CoolPadel Studios. Ficha de operador: {escape_txt(nombre)}.</p>
    </div>
  </footer>

  <script>
    lucide.createIcons();
  </script>
</body>
</html>
"""
    target_dir = os.path.join(FRANQUICIAS_DIR, fid)
    os.makedirs(target_dir, exist_ok=True)
    target_file = os.path.join(target_dir, "index.html")
    with open(target_file, "w", encoding="utf-8") as fp:
        fp.write(page_html)
    return target_file


def main():
    print(f"Generando páginas individuales para {len(FRANQUICIAS)} franquicias...")
    count = 0
    for f in FRANQUICIAS:
        generate_single_page(f)
        count += 1
    print(f"Completado: {count} páginas de franquicias generadas con éxito en coolpadel-web/franquicias-padel/<id>/index.html")


if __name__ == "__main__":
    main()
