#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador Maestro del Directorio Global de Franquicias y Cadenas de Pádel (+1 Club)
para CoolPadel Studios (https://coolpadelstudios.com/franquicias-padel/).

Incluye:
1. Directorio exhaustivo de 153 cadenas multiclub y franquicias en más de 20 países.
2. Comparador interactivo Cara a Cara (Side-by-Side Matrix) para inversores y clubes.
3. Formulario interactivo multi-paso de Onboarding y Homologación B2B ("Reclamar Ficha").
4. Barra flotante de selección y filtros avanzados por Presupuesto (CAPEX) e Instalación.
5. Mapa interactivo Leaflet y Drawer lateral con especificaciones técnicas completas.
"""

import os
import json
import urllib.parse
from datetime import datetime

# Importar dataset maestro unificado
from dataset_franquicias import FRANQUICIAS

REGIONES_CONFIG = [
    ("all", "Todos", "🌍"),
    ("GB", "Reino Unido", "🇬🇧"),
    ("ES", "España", "🇪🇸"),
    ("FR", "Francia", "🇫🇷"),
    ("IT", "Italia", "🇮🇹"),
    ("NL", "Benelux", "🇳🇱"),
    ("DE", "Alemania, AT & CH", "🇩🇪"),
    ("SE", "Nórdicos", "🇸🇪"),
    ("PT", "Portugal", "🇵🇹"),
    ("US", "Estados Unidos", "🇺🇸"),
    ("MX", "Latinoamérica", "🇲🇽"),
    ("AE", "Oriente Medio", "🇦🇪"),
    ("ZA", "Sudáfrica & Australia", "🇿🇦"),
]


def get_budget_tier(inv_str):
    if not inv_str:
        return "mid"
    s = inv_str.lower()
    import re
    nums = [int(n.replace('.', '')) for n in re.findall(r'\d+(?:\.\d+)?', s.replace('€', '').replace('$', '').replace('£', ''))]
    max_num = max(nums) if nums else 500000
    if max_num < 400000:
        return "low"
    elif max_num <= 850000:
        return "mid"
    else:
        return "high"


def get_facility_type(tech_dict):
    pistas_str = tech_dict.get("pistas", "").lower() if isinstance(tech_dict, dict) else ""
    if "outdoor" in pistas_str or "exterior" in pistas_str or "descubiert" in pistas_str:
        if "indoor" in pistas_str or "cubiert" in pistas_str or "nave" in pistas_str:
            return "hybrid"
        return "outdoor"
    return "indoor"


def render_html(lang="es"):
    t_nav = {
        "es": {"llaveros": "LLAVEROS", "camaras": "CÁMARAS", "blog": "BLOG", "franquicias": "CADENAS DE CLUBS", "contacto": "CONTACTAR"},
        "en": {"llaveros": "KEYCHAINS", "camaras": "CAMERAS", "blog": "BLOG", "franquicias": "CLUB CHAINS", "contacto": "CONTACT"},
        "fr": {"llaveros": "PORTE-CLÉS", "camaras": "CAMÉRAS", "blog": "BLOG", "franquicias": "CHAÎNES DE CLUBS", "contacto": "CONTACTER"},
        "it": {"llaveros": "PORTACHIAVI", "camaras": "TELECAMERE", "blog": "BLOG", "franquicias": "CATENE DI CLUB", "contacto": "CONTATTARE"}
    }.get(lang, {"llaveros": "LLAVEROS", "camaras": "CÁMARAS", "blog": "BLOG", "franquicias": "CADENAS DE CLUBS", "contacto": "CONTACTAR"})
    total_franquicias = len(FRANQUICIAS)
    paises_unicos = len(set(f["pais"] for f in FRANQUICIAS))
    path_prefix = "" if lang == "es" else f"{lang}/"
    asset_prefix = "../" if lang == "es" else "../../"
    page_url = f"https://coolpadelstudios.com/{path_prefix}franquicias-padel/"
    og_locale = {"es": "es_ES", "en": "en_US", "fr": "fr_FR", "it": "it_IT"}.get(lang, "es_ES")
    home_url = "/" if lang == "es" else f"/{lang}/"
    franquicias_hub_url = "/franquicias-padel/" if lang == "es" else f"/{lang}/franquicias-padel/"

    meta_titles = {
        "es": f"Franquicias y Cadenas de Pádel ({total_franquicias} Operadores) | CoolPadel",
        "en": f"Padel Club Networks & Franchises Directory ({total_franquicias} Operators) | CoolPadel",
        "fr": f"Annuaire des Franchises et Réseaux de Padel ({total_franquicias} Opérateurs) | CoolPadel",
        "it": f"Directory delle Franchigie e Catene di Padel ({total_franquicias} Operatori) | CoolPadel"
    }
    meta_descs = {
        "es": f"Directorio y comparador de {total_franquicias} cadenas y franquicias de pádel: requisitos de nave, inversión, royalties, software y modelos para inversores.",
        "en": f"Directory and side-by-side comparison of {total_franquicias} padel club networks and franchises: facility criteria, investment, royalties, and booking software.",
        "fr": f"Annuaire et comparateur de {total_franquicias} réseaux et franchises de padel: critères d'implantation, investissement, royalties et logiciels de réservation.",
        "it": f"Directory e confronto di {total_franquicias} catene e franchigie di padel: requisiti delle strutture, investimenti, royalties e software gestionali."
    }
    page_title = meta_titles.get(lang, meta_titles["es"])
    page_desc = meta_descs.get(lang, meta_descs["es"])

    # Generación dinámica de opciones para el desplegable moderno de región
    region_dropdown_items_html = ""
    for reg_code, reg_label, reg_flag in REGIONES_CONFIG:
        if reg_code == "all":
            cnt = total_franquicias
            label_text = "Todas las regiones"
        else:
            cnt = sum(1 for f in FRANQUICIAS if f.get("region_filtro") == reg_code)
            label_text = reg_label
        region_dropdown_items_html += f"""
              <button type="button" onclick="selectRegion('{reg_code}', '{label_text}', '{reg_flag}')" data-reg-opt="{reg_code}" class="region-opt w-full text-left px-3.5 py-2 text-xs font-bold text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 transition flex items-center justify-between cursor-pointer rounded-xl">
                <span class="flex items-center gap-2">
                  <span class="text-base">{reg_flag}</span>
                  <span>{label_text}</span>
                </span>
                <span class="text-[11px] font-mono opacity-60 bg-slate-100 px-1.5 py-0.5 rounded-md">{cnt}</span>
              </button>"""

    # Labels CTA adaptados
    txt_cta_view = {
        "es": "Ver ficha y clubes",
        "en": "View profile & clubs",
        "fr": "Voir la fiche & clubs",
        "it": "Vedi scheda e club"
    }.get(lang, "Ver ficha y clubes")
    txt_dossier = "Dossier"
    txt_compare = {
        "es": "Comparar",
        "en": "Compare",
        "fr": "Comparer",
        "it": "Confronta"
    }.get(lang, "Comparar")

    # Cards HTML para el grid
    cards_html = ""
    for f in FRANQUICIAS:
        fid = f["id"]
        nombre = f["nombre"]
        pais = f["pais"]
        bandera = f["bandera"]
        ciudad = f["ciudad_sede"]
        modelo = f["modelo"]
        badge_cls = f["modelo_badge"]
        tagline = f["tagline"]
        num_clubs = f["num_clubs"]
        num_pistas = f["num_pistas"]
        software = f["software"]
        tipo_cat = f["tipo_categoria"]
        region_f = f.get("region_filtro", f["pais_codigo"])
        
        # Filtros adicionales calculados
        budget_tier = get_budget_tier(f.get("modelo_expansion", {}).get("inversion_media", ""))
        facility_type = get_facility_type(f.get("tecnologia_pistas", {}))

        cards_html += f"""
        <article class="franchise-card group bg-white rounded-2xl p-4 sm:p-5 border-2 border-slate-200/90 shadow-2xs hover:shadow-xl hover:border-[#f2920b] hover:ring-4 hover:ring-[#f2920b]/20 hover:-translate-y-1.5 active:scale-[0.99] transition-all duration-300 flex flex-col justify-between cursor-pointer relative"
                 data-id="{fid}"
                 data-region="{region_f}"
                 data-model="{tipo_cat}"
                 data-budget="{budget_tier}"
                 data-facility="{facility_type}"
                 data-search="{nombre.lower()} {pais.lower()} {ciudad.lower()} {modelo.lower()}"
                 onclick="openDrawer('{fid}')">
          <div>
            <div class="flex items-start justify-between gap-2 mb-2.5">
              <span class="text-[11px] font-bold text-slate-500 uppercase tracking-wider">
                {modelo.replace('(Mismo Nombre)', '').strip()}
              </span>
              <div class="flex items-center gap-1.5" onclick="event.stopPropagation()">
                <button onclick="toggleCompare('{fid}')" id="compare-btn-{fid}"
                        class="compare-card-btn inline-flex items-center gap-1 px-2 py-0.5 rounded-lg text-[10px] font-bold border border-slate-200 bg-white text-slate-600 hover:border-[#f2920b] hover:text-[#f2920b] transition">
                  <i data-lucide="scale" class="w-3 h-3"></i>
                  <span class="compare-label">{txt_compare}</span>
                </button>
                <span class="text-xl" title="{pais}">{bandera}</span>
              </div>
            </div>

            <h3 class="font-heading font-black text-lg sm:text-xl text-slate-950 group-hover:text-[#f2920b] transition-colors mb-1 flex items-center justify-between">
              <span>{nombre}</span>
              <span class="w-7 h-7 rounded-full bg-slate-100 group-hover:bg-[#f2920b] group-hover:text-slate-950 flex items-center justify-center transition-all shrink-0">
                <i data-lucide="arrow-up-right" class="w-4 h-4"></i>
              </span>
            </h3>
            
            <p class="text-[11px] font-semibold text-slate-500 mb-2 flex items-center gap-1">
              <i data-lucide="map-pin" class="w-3 h-3 text-slate-400"></i>
              <span>{ciudad}, {pais}</span>
            </p>

            <p class="text-slate-600 text-xs leading-relaxed mb-3 line-clamp-2">
              {tagline}
            </p>

            <!-- Grid de métricas clave compacto -->
            <div class="grid grid-cols-3 gap-1.5 py-2 px-2.5 bg-slate-50 rounded-xl border border-slate-100 mb-3">
              <div>
                <span class="block text-[9px] uppercase font-bold text-slate-400">Clubes</span>
                <span class="font-heading font-black text-xs sm:text-sm text-slate-900">{num_clubs}</span>
              </div>
              <div>
                <span class="block text-[9px] uppercase font-bold text-slate-400">Pistas</span>
                <span class="font-heading font-black text-xs sm:text-sm text-slate-900">{num_pistas}</span>
              </div>
              <div>
                <span class="block text-[9px] uppercase font-bold text-slate-400">Software</span>
                <span class="font-heading font-bold text-[11px] text-slate-800 truncate block" title="{software}">{software.split('/')[0].strip()}</span>
              </div>
            </div>
          </div>

          <div class="pt-3 border-t border-slate-100 flex items-center gap-2">
            <a href="./{fid}/" onclick="event.stopPropagation()" class="flex-1 py-2 px-3 rounded-xl bg-slate-900 group-hover:bg-[#f2920b] text-white group-hover:text-slate-950 font-heading font-black text-xs uppercase tracking-wider flex items-center justify-center gap-1.5 transition-all duration-200 shadow-xs hover:scale-[1.02] active:scale-[0.98] cursor-pointer">
              <span>{txt_cta_view}</span>
              <i data-lucide="arrow-right" class="w-3.5 h-3.5 group-hover:translate-x-0.5 transition-transform"></i>
            </a>
            <button type="button" onclick="event.stopPropagation(); openDrawer('{fid}')" class="px-3 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs uppercase tracking-wider transition flex items-center gap-1 cursor-pointer" title="Vista rápida de {nombre}">
              <i data-lucide="eye" class="w-3.5 h-3.5"></i>
              <span>{txt_dossier}</span>
            </button>
          </div>
        </article>
        """

    # Filas para tabla comparativa
    table_rows_html = ""
    for f in FRANQUICIAS:
        fid = f["id"]
        table_rows_html += f"""
        <tr class="hover:bg-slate-50/80 transition-colors cursor-pointer border-b border-slate-200/70" onclick="openDrawer('{fid}')">
          <td class="py-4 px-3 text-center" onclick="event.stopPropagation()">
            <button onclick="toggleCompare('{fid}')" id="table-compare-btn-{fid}" class="compare-card-btn inline-flex items-center gap-1 px-2.5 py-1 rounded-lg text-[11px] font-bold border border-slate-200 bg-white text-slate-600 hover:border-[#f2920b] hover:text-[#f2920b] transition">
              <i data-lucide="scale" class="w-3.5 h-3.5"></i>
              <span class="compare-label">Comparar</span>
            </button>
          </td>
          <td class="py-4 px-4 font-heading font-black text-slate-950 flex items-center gap-2">
            <span class="text-lg">{f['bandera']}</span>
            <span>{f['nombre']}</span>
          </td>
          <td class="py-4 px-4 text-xs font-semibold text-slate-600">
            <span class="inline-block px-2.5 py-0.5 rounded-full border {f['modelo_badge']} text-[11px]">
              {f['modelo']}
            </span>
          </td>
          <td class="py-4 px-4 text-xs font-bold text-slate-700">{f['ciudad_sede']} ({f['pais']})</td>
          <td class="py-4 px-4 text-sm font-bold text-slate-800">{f['num_clubs']}</td>
          <td class="py-4 px-4 text-sm font-bold text-slate-800">{f['num_pistas']}</td>
          <td class="py-4 px-4 text-xs font-semibold text-slate-600">{f['software']}</td>
          <td class="py-4 px-4 text-xs text-slate-600 max-w-xs truncate">{f['tagline']}</td>
          <td class="py-4 px-4 text-right" onclick="event.stopPropagation()">
            <a href="./{fid}/" class="inline-flex items-center gap-1 text-xs font-bold text-[#f2920b] hover:text-[#d97f08] transition">
              <span>Ficha</span>
              <i data-lucide="chevron-right" class="w-3.5 h-3.5"></i>
            </a>
          </td>
        </tr>
        """

    full_html = f"""<!DOCTYPE html>
<html lang="{lang}" class="scroll-smooth overflow-x-hidden">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>{page_title}</title>
  <meta name="description" content="{page_desc}">
  <link rel="canonical" href="{page_url}">

  <!-- SEO Multilingüe Hreflang -->
  <link rel="alternate" hreflang="es" href="https://coolpadelstudios.com/franquicias-padel/">
  <link rel="alternate" hreflang="en" href="https://coolpadelstudios.com/en/franquicias-padel/">
  <link rel="alternate" hreflang="fr" href="https://coolpadelstudios.com/fr/franquicias-padel/">
  <link rel="alternate" hreflang="it" href="https://coolpadelstudios.com/it/franquicias-padel/">
  <link rel="alternate" hreflang="x-default" href="https://coolpadelstudios.com/franquicias-padel/">
  <meta name="language" content="{lang}">

  <!-- LLM & AI Discovery -->
  <link rel="alternate" type="text/markdown" href="https://coolpadelstudios.com/llms.txt" title="LLMs.txt">
  <link rel="alternate" type="text/markdown" href="https://coolpadelstudios.com/llms-full.txt" title="LLMs-Full.txt">


  <!-- Favicon -->
  <link rel="icon" type="image/png" href="{asset_prefix}assets/images/coolpadel-mascot-hd.png">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:locale" content="{og_locale}">
  <meta property="og:site_name" content="CoolPadel Studios">
  <meta property="og:url" content="{page_url}">
  <meta property="og:title" content="{page_title}">
  <meta property="og:description" content="{page_desc}">
  <meta property="og:image" content="https://coolpadelstudios.com/assets/images/savemyplay-1.jpg">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{page_title}">
  <meta name="twitter:description" content="{page_desc}">
  <meta name="twitter:image" content="https://coolpadelstudios.com/assets/images/savemyplay-1.jpg">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">

  <!-- Schema.org Dataset & CollectionPage JSON-LD -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "Organization",
        "@id": "https://coolpadelstudios.com/#organization",
        "name": "CoolPadel Studios",
        "url": "https://coolpadelstudios.com",
        "logo": "https://coolpadelstudios.com/assets/images/coolpadel-mascot-hd.png"
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
          }}
        ]
      }},
      {{
        "@type": "Dataset",
        "@id": "https://coolpadelstudios.com/franquicias-padel/#dataset",
        "name": "Directorio y Comparador Global de Franquicias y Cadenas de Pádel (+1 Club)",
        "description": "Censo y matriz comparativa cara a cara de {total_franquicias} cadenas de clubes de pádel en {paises_unicos} países con datos técnicos de naves, inversión requerida, royalties y software de gestión.",
        "url": "https://coolpadelstudios.com/franquicias-padel/",
        "isAccessibleForFree": true,
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "creator": {{
          "@type": "Organization",
          "name": "CoolPadel Studios"
        }},
        "keywords": ["franquicias padel", "cadenas clubs padel", "inversion pistas padel", "comparativa franquicias padel", "abrir club padel"],
        "inLanguage": "es"
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "¿Cuántas cadenas y franquicias de pádel existen en el directorio de CoolPadel?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "El directorio oficial de CoolPadel Studios reúne {total_franquicias} cadenas, operadores multiclub y franquicias de pádel verificadas que gestionan más de 828 clubes y 8.500 pistas en {paises_unicos} países."
            }}
          }},
          {{
            "@type": "Question",
            "name": "¿Qué modelos de negocio de clubes de pádel se comparan?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Se analizan 5 modelos principales: Cadena Multiclub (operadores propios con varias sedes), Red Corporativa, Franquicia Llave en Mano, Club Automatizado 24/7 y Club Boutique de lujo, detallando inversión estimada, requisitos de nave, software de reservas y royalties."
            }}
          }},
          {{
            "@type": "Question",
            "name": "¿Qué soluciones B2B ofrece CoolPadel Studios para cadenas y franquicias de pádel?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "CoolPadel Studios equipa a cadenas y clubes con llaveros personalizados en goma 3D (desde 100 uds, muestra física en ~15 días laborables por 15€ descontables y entrega del pedido en ~1 mes) y cámaras de grabación en pista Save My Play sin obras (180 €/pista hardware y desde 45 €/mes software sin permanencia)."
            }}
          }}
        ]
      }}
    ]
  }}
  </script>

  <!-- Fuentes & Estilos -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          fontFamily: {{
            heading: ['Outfit', 'sans-serif'],
            sans: ['Plus Jakarta Sans', 'sans-serif'],
          }},
          colors: {{
            brand: {{
              orange: '#f2920b',
              blue: '#76d3f6',
              dark: '#0b1626',
            }}
          }}
        }}
      }}
    }}
  </script>

  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <!-- Leaflet CSS & JS para Mapa Interactivo -->
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin=""/>
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>

  <style>
    .bg-textured-blue {{
      background-color: #3478a6;
      background-image: linear-gradient(rgba(52, 120, 166, 0.40), rgba(52, 120, 166, 0.40)), url('/assets/images/branding/textura_editorial_coolpadel.webp');
      background-blend-mode: normal, soft-light;
      background-size: cover;
      background-position: center;
    }}
    #franchiseMap {{
      height: 360px;
      width: 100%;
      border-radius: 1.25rem;
      z-index: 10;
      touch-action: none !important;
      -webkit-user-select: none;
      user-select: none;
      -webkit-touch-callout: none;
    }}
    #franchiseMap,
    #franchiseMap *,
    #franchiseMap .leaflet-pane,
    #franchiseMap .leaflet-tile-pane,
    #franchiseMap .leaflet-map-pane,
    #franchiseMap .leaflet-container {{
      touch-action: none !important;
    }}
    .custom-marker {{
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 9999px;
      color: #fff;
      font-weight: 900;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
      border: 2px solid #ffffff;
      transition: transform 0.2s ease;
    }}
    .custom-marker:hover {{
      transform: scale(1.2);
    }}
    .sub-club-marker {{
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 9999px;
      color: #fff;
      font-weight: 900;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.35);
      transition: transform 0.2s ease;
      cursor: pointer;
    }}
    .sub-club-marker:hover {{
      transform: scale(1.35) !important;
      z-index: 999;
    }}
    .leaflet-popup-content-wrapper {{
      border-radius: 1rem;
      padding: 0.25rem;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
    }}
    .drawer-open {{
      overflow: hidden;
    }}
    .lang-opt-active {{
      background-color: #f2920b;
      color: #0b1626;
      font-weight: 800;
    }}
  </style>
  <!-- Microsoft Clarity -->
  <script type="text/javascript">
    (function(c,l,a,r,i,t,y){{
      c[a]=c[a]||function(){{(c[a].q=c[a].q||[]).push(arguments)}};
      t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
      y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    }})(window, document, "clarity", "script", "q7p8g52y9e");
  </script>
</head>
<body class="bg-[#f8fafc] text-slate-800 antialiased selection:bg-[#f2920b] selection:text-slate-950 min-h-screen flex flex-col overflow-x-hidden">

  <!-- NAVBAR BLANCA UNIFICADA COOLPADEL -->
  <header class="fixed top-0 left-0 w-full z-50 bg-white/95 backdrop-blur-md border-b border-slate-200/80 shadow-xs w-full">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 sm:h-20 flex items-center justify-between">
      
      <!-- LOGO: MASCOTA + TIPOGRAFÍA -->
      <a href="{home_url}" class="flex items-center gap-2 group shrink-0" aria-label="CoolPadel Home">
        <img src="{asset_prefix}assets/images/coolpadel-mascot-hd.png" alt="Mascota CoolPadel" width="44" height="44" class="h-8 sm:h-11 w-auto object-contain group-hover:scale-105 transition" fetchpriority="high">
        <img src="{asset_prefix}assets/images/coolpadel-typography-hd.png" alt="CoolPadel" width="140" height="28" class="h-5 sm:h-7 w-auto object-contain" fetchpriority="high">
      </a>

      <!-- BLOQUE DE NAVEGACIÓN Y ACCIONES A LA DERECHA (ESTILO EXACTO LANDINGS) -->
      <div class="flex items-center gap-2 sm:gap-4 lg:gap-6">
        <a href="{home_url}llaveros-padel-personalizados/" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">{t_nav['llaveros']}</a>
        <a href="{home_url}camaras/" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">{"CAMERAS" if lang=="en" else "CAMÉRAS" if lang=="fr" else "TELECAMERE" if lang=="it" else "CÁMARAS"}</a>
        <a href="{home_url}blog/" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">{t_nav['blog']}</a>
        <a href="{franquicias_hub_url}" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-[#f2920b] transition whitespace-nowrap">{t_nav['franquicias']}</a>

        <!-- SELECTOR DE IDIOMA EN DESPLEGABLE COMPACTO -->
        <div class="relative inline-block text-left" id="lang-dropdown-container">
          <button type="button" onclick="toggleLangDropdown(event)" id="lang-dropdown-btn" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 border border-slate-200 text-xs font-black text-slate-900 shadow-xs transition cursor-pointer" aria-expanded="false" aria-haspopup="true">
            <span class="uppercase font-black">{lang.upper()}</span>
            <i data-lucide="chevron-down" class="w-3.5 h-3.5 stroke-[2.5] text-slate-600 transition-transform duration-200" id="lang-dropdown-arrow"></i>
          </button>
          <div id="lang-dropdown-menu" class="hidden absolute right-0 mt-2 w-24 bg-white rounded-2xl shadow-[0_12px_30px_rgba(0,0,0,0.15)] border border-slate-200 py-1.5 z-50 transition-all overflow-hidden">
            <a href="/franquicias-padel/" class="lang-opt block {'lang-opt-active' if lang=='es' else 'text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold'} w-full text-center px-4 py-2 text-xs transition duration-150">ES</a>
            <a href="/en/franquicias-padel/" class="lang-opt block {'lang-opt-active' if lang=='en' else 'text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold'} w-full text-center px-4 py-2 text-xs transition duration-150">EN</a>
            <a href="/fr/franquicias-padel/" class="lang-opt block {'lang-opt-active' if lang=='fr' else 'text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold'} w-full text-center px-4 py-2 text-xs transition duration-150">FR</a>
            <a href="/it/franquicias-padel/" class="lang-opt block {'lang-opt-active' if lang=='it' else 'text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold'} w-full text-center px-4 py-2 text-xs transition duration-150">IT</a>
          </div>
        </div>

        <!-- BOTÓN CONTACTAR (ESTILO EXACTO LANDINGS) -->
        <a href="{home_url}#contacto" class="inline-flex items-center gap-1.5 px-3.5 sm:px-4 py-1.5 sm:py-2 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition shadow-sm hover:scale-105 active:scale-95 cursor-pointer">
          <span>{t_nav['contacto']}</span>
          <i data-lucide="arrow-down" class="w-3 h-3 stroke-[3]"></i>
        </a>

        <!-- OJOS DEL LOGO A LA DERECHA DEL TODO -->
        <a href="{home_url}" class="group py-1 inline-flex items-center shrink-0 pl-1" aria-label="CoolPadel Eyes">
          <img src="{asset_prefix}assets/images/eyes-thumb.png?v=fixed_eyes" alt="CoolPadel Eyes" width="28" height="28" style="height: 26px; max-height: 26px; width: auto;" class="object-contain group-hover:scale-110 transition duration-300">
        </a>
      </div>
    </div>
  </header>
  <div class="h-16 sm:h-20 w-full shrink-0" aria-hidden="true"></div>


  <!-- MAIN -->
  <main class="flex-1">

    <!-- HERO SECTION (PROPORCIONADO, ELEGANTE Y LEGIBLE) -->
    <section class="pt-14 pb-8 sm:pt-18 sm:pb-10 lg:pt-20 lg:pb-10 bg-gradient-to-b from-white via-slate-50 to-[#f8fafc] border-b border-slate-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-6">
          <div class="max-w-3xl space-y-2.5">
            <h1 class="font-heading font-black text-2xl sm:text-3xl lg:text-4xl text-slate-950 uppercase tracking-tight leading-tight">
              Directorio y Comparador de Franquicias de Pádel
            </h1>

            <p class="text-base sm:text-lg text-slate-700 font-semibold leading-relaxed">
              El directorio para operadores y clubes que quieren franquiciarse
            </p>
          </div>

          <!-- Botón Alta de Franquicia fuera de la barra -->
          <div class="shrink-0">
            <button onclick="openOnboardingModal()" class="inline-flex items-center text-left gap-2 px-4 py-2.5 rounded-xl bg-[#f2920b] hover:bg-[#d97f08] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition shadow-md hover:scale-105 active:scale-95 cursor-pointer ml-auto">
              <i data-lucide="plus-circle" class="w-4 h-4 stroke-[2.5] shrink-0"></i>
              <span class="leading-tight">¿Tienes una Franquicia?<br><span class="text-[11px] font-bold">Date de Alta / Reclama tu Ficha</span></span>
            </button>
          </div>
        </div>

        <!-- KPI BANNER FORMATO TEXTURA -->
        <div class="mt-6 p-6 sm:p-8 rounded-3xl bg-textured-blue text-white shadow-lg">
          <div class="grid grid-cols-2 lg:grid-cols-4 gap-6 text-center">
            <div>
              <div class="font-heading font-black text-2xl sm:text-3xl lg:text-4xl text-white">+165</div>
              <div class="text-xs sm:text-sm font-bold uppercase tracking-wider text-white/90 mt-1">Franquicias y Cadenas</div>
            </div>
            <div>
              <div class="font-heading font-black text-2xl sm:text-3xl lg:text-4xl text-[#76d3f6]">+5.500</div>
              <div class="text-xs sm:text-sm font-bold uppercase tracking-wider text-white/90 mt-1">Pistas Gestionadas</div>
            </div>
            <div>
              <div class="font-heading font-black text-2xl sm:text-3xl lg:text-4xl text-white">+25</div>
              <div class="text-xs sm:text-sm font-bold uppercase tracking-wider text-white/90 mt-1">Países con Presencia</div>
            </div>
            <div>
              <div class="font-heading font-black text-2xl sm:text-3xl lg:text-4xl text-[#f2920b]">7</div>
              <div class="text-xs sm:text-sm font-bold uppercase tracking-wider text-white/90 mt-1">Modelos de Expansión</div>
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- INTERACTIVE SECTION (CONECTADO SIN SALTO EXCESIVO) -->
    <section class="pt-4 pb-12 sm:pt-6 sm:pb-16 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- MAPA INTERACTIVO CON BUSCADOR Y FILTROS INTEGRADOS (COMPACTO) -->
      <div id="mapContainer" class="bg-white p-3 sm:p-4 rounded-2xl border border-slate-200/90 shadow-2xs mb-5 relative">
        <div id="filtrosContainer">
          <!-- FILA SUPERIOR: TÍTULO + BUSCADOR INTEGRADO + REGIONES + VISTA MAPA/TABLA -->
          <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-3 mb-3">
            <div class="flex items-center gap-2 shrink-0">
              <span class="w-2.5 h-2.5 rounded-full bg-[#f2920b]"></span>
              <h2 class="font-heading font-black text-sm sm:text-base text-slate-900 uppercase tracking-wider whitespace-nowrap">
                Mapa mundial de principales cadenas de clubs
              </h2>
            </div>

            <!-- BUSCADOR INTEGRADO DENTRO DE LA PARTE DEL MAPA MUNDIAL -->
            <div class="relative flex-1 max-w-xl min-w-[240px]" id="searchContainer">
              <i data-lucide="search" class="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2 pointer-events-none"></i>
              <input type="text" id="searchInput" placeholder="Buscar cadenas, clubs, países o ciudades..."
                     class="w-full pl-9 pr-9 py-2 rounded-xl bg-slate-50 border border-slate-200 text-slate-950 placeholder-slate-400 font-medium text-xs sm:text-sm focus:outline-none focus:ring-2 focus:ring-[#f2920b] focus:bg-white transition"
                     autocomplete="off"
                     oninput="handleSearchInput(event)"
                     onfocus="handleSearchFocus(event)"
                     onkeydown="handleSearchKeyDown(event)">
              <button type="button" id="searchClearBtn" onclick="clearSearchInput()" class="hidden absolute right-2.5 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-700 p-1 rounded-full hover:bg-slate-200 transition cursor-pointer" title="Borrar búsqueda">
                <i data-lucide="x" class="w-3.5 h-3.5"></i>
              </button>

              <!-- MENÚ DESPLEGABLE DE SUGERENCIAS / AUTOCOMPLETADO TÍPICO DE BUSCADOR -->
              <div id="searchSuggestionsMenu" class="hidden absolute left-0 right-0 top-full mt-2 bg-white rounded-2xl shadow-[0_18px_45px_rgba(0,0,0,0.18)] border border-slate-200/90 overflow-hidden z-[1000] max-h-80 overflow-y-auto transition-all">
                <!-- Generado dinámicamente -->
              </div>
            </div>

            <div class="flex items-center gap-2 self-start lg:self-auto shrink-0">
              <!-- SELECTOR DE FORMATO / ESTILO DE MAPA -->
              <div class="relative inline-block text-left" id="mapstyle-dropdown-container">
                <button type="button" onclick="toggleMapStyleDropdown(event)" id="mapstyle-dropdown-btn" class="inline-flex items-center gap-1.5 px-3 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 border border-slate-200 text-xs font-bold text-slate-900 shadow-xs transition cursor-pointer" aria-expanded="false" aria-haspopup="true" title="Cambiar formato visual del mapa">
                  <span id="current-mapstyle-icon">⛰️</span>
                  <span id="current-mapstyle-label" class="font-black text-slate-900">Google Relieve</span>
                  <i data-lucide="chevron-down" class="w-3.5 h-3.5 stroke-[2.5] text-slate-600 transition-transform duration-200" id="mapstyle-dropdown-arrow"></i>
                </button>

                <!-- MENÚ DESPLEGABLE ESTILOS (100% LIMPIOS SIN MARCAS) -->
                <div id="mapstyle-dropdown-menu" class="hidden absolute right-0 mt-2 w-64 bg-white rounded-2xl shadow-[0_12px_30px_rgba(0,0,0,0.15)] border border-slate-200 p-2 z-50 transition-all">
                  <div class="px-2.5 py-1 text-[10px] font-black uppercase tracking-wider text-slate-400 border-b border-slate-100 mb-1.5 flex items-center justify-between">
                    <span>Propuestas de diseño</span>
                    <span class="text-[9px] text-emerald-600 bg-emerald-50 px-1.5 py-0.5 rounded font-bold">100% Limpio</span>
                  </div>
                  <button type="button" onclick="setMapStyle('terrain')" class="w-full flex items-center justify-between px-2.5 py-2 text-xs font-bold text-slate-800 hover:bg-amber-50 hover:text-amber-900 rounded-xl transition text-left cursor-pointer">
                    <span class="flex items-center gap-2"><span>⛰️</span> Google Relieve</span>
                    <span class="text-[9px] font-extrabold uppercase px-1.5 py-0.5 rounded bg-emerald-100 text-emerald-800">Activo</span>
                  </button>
                  <button type="button" onclick="setMapStyle('google')" class="w-full flex items-center justify-between px-2.5 py-2 text-xs font-bold text-slate-800 hover:bg-amber-50 hover:text-amber-900 rounded-xl transition text-left cursor-pointer">
                    <span class="flex items-center gap-2"><span>🗺️</span> Google Maps Clásico</span>
                    <span class="text-[9px] font-bold text-slate-500 bg-slate-100 px-1.5 py-0.5 rounded">Oficial</span>
                  </button>
                  <button type="button" onclick="setMapStyle('satellite')" class="w-full flex items-center justify-between px-2.5 py-2 text-xs font-bold text-slate-800 hover:bg-amber-50 hover:text-amber-900 rounded-xl transition text-left cursor-pointer">
                    <span class="flex items-center gap-2"><span>🛰️</span> Satélite Híbrido HD</span>
                    <span class="text-[9px] font-bold text-slate-500 bg-slate-100 px-1.5 py-0.5 rounded">Aéreo</span>
                  </button>
                  <button type="button" onclick="setMapStyle('osm_hot')" class="w-full flex items-center justify-between px-2.5 py-2 text-xs font-bold text-slate-800 hover:bg-amber-50 hover:text-amber-900 rounded-xl transition text-left cursor-pointer">
                    <span class="flex items-center gap-2"><span>🎨</span> OpenStreetMap Pastel</span>
                    <span class="text-[9px] font-bold text-slate-500 bg-slate-100 px-1.5 py-0.5 rounded">Moderno</span>
                  </button>
                  <button type="button" onclick="setMapStyle('esri_light')" class="w-full flex items-center justify-between px-2.5 py-2 text-xs font-bold text-slate-800 hover:bg-amber-50 hover:text-amber-900 rounded-xl transition text-left cursor-pointer">
                    <span class="flex items-center gap-2"><span>⚪</span> Blanco Minimal B2B</span>
                    <span class="text-[9px] font-bold text-slate-500 bg-slate-100 px-1.5 py-0.5 rounded">Limpio</span>
                  </button>
                  <button type="button" onclick="setMapStyle('osm_std')" class="w-full flex items-center justify-between px-2.5 py-2 text-xs font-bold text-slate-800 hover:bg-amber-50 hover:text-amber-900 rounded-xl transition text-left cursor-pointer">
                    <span class="flex items-center gap-2"><span>🌐</span> OpenStreetMap Estándar</span>
                    <span class="text-[9px] font-bold text-slate-500 bg-slate-100 px-1.5 py-0.5 rounded">Global</span>
                  </button>
                </div>
              </div>

              <!-- SELECTOR DE REGIÓN MODERNO A LA DERECHA (ESTILO DESPLEGABLE DE IDIOMAS) -->
              <div class="relative inline-block text-left" id="region-dropdown-container">
                <button type="button" onclick="toggleRegionDropdown(event)" id="region-dropdown-btn" class="inline-flex items-center gap-2 px-3.5 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 border border-slate-200 text-xs font-bold text-slate-900 shadow-xs transition cursor-pointer" aria-expanded="false" aria-haspopup="true">
                  <span id="current-region-flag">🌍</span>
                  <span id="current-region-label" class="font-black text-slate-900">Todas las regiones</span>
                  <i data-lucide="chevron-down" class="w-3.5 h-3.5 stroke-[2.5] text-slate-600 transition-transform duration-200" id="region-dropdown-arrow"></i>
                </button>

                <!-- MENÚ DESPLEGABLE FLOTANTE -->
                <div id="region-dropdown-menu" class="hidden absolute right-0 mt-2 w-64 max-h-80 overflow-y-auto bg-white rounded-2xl shadow-[0_12px_30px_rgba(0,0,0,0.15)] border border-slate-200 p-1.5 z-50 transition-all">
                  {region_dropdown_items_html}
                </div>
              </div>

              <!-- BOTONES VISTA: MAPA / TABLA -->
              <button id="viewGridBtn" onclick="switchView('grid')" class="px-3.5 py-2 rounded-xl text-xs font-bold font-heading uppercase tracking-wider bg-slate-900 text-white transition flex items-center gap-1.5 shadow-xs">
                <i data-lucide="map" class="w-4 h-4"></i>
                <span>Mapa</span>
              </button>
              <button id="viewTableBtn" onclick="switchView('table')" class="px-3.5 py-2 rounded-xl text-xs font-bold font-heading uppercase tracking-wider bg-slate-100 text-slate-700 hover:bg-slate-200 transition flex items-center gap-1.5">
                <i data-lucide="table" class="w-4 h-4"></i>
                <span>Tabla</span>
              </button>
            </div>
          </div>

          <!-- FILTRO MODELO Y CONTADOR INTEGRADOS -->
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 pt-2.5 pb-2.5 border-t border-slate-100">
            <div class="flex items-center gap-1.5 flex-wrap">
              <span class="text-[11px] font-bold uppercase text-slate-400 mr-1 flex items-center gap-1">
                <i data-lucide="tag" class="w-3 h-3"></i>
                <span>Modelo:</span>
              </span>
              <button onclick="setModelFilter('all')" class="filter-model-btn active px-2.5 py-1 rounded-lg text-xs font-bold bg-slate-900 text-white transition" data-model="all">Todos</button>
              <button onclick="setModelFilter('cadena')" class="filter-model-btn px-2.5 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-model="cadena">Cadena Multiclub</button>
              <button onclick="setModelFilter('corporativo')" class="filter-model-btn px-2.5 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-model="corporativo">Red Corporativa</button>
              <button onclick="setModelFilter('franquicia')" class="filter-model-btn px-2.5 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-model="franquicia">Franquicia Llave en Mano</button>
              <button onclick="setModelFilter('automatizado')" class="filter-model-btn px-2.5 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-model="automatizado">Club 24/7</button>
              <button onclick="setModelFilter('boutique')" class="filter-model-btn px-2.5 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-model="boutique">Boutique</button>
            </div>
            <span id="resultsCount" class="text-xs font-bold text-slate-500 whitespace-nowrap">Mostrando {total_franquicias} cadenas y franquicias</span>
          </div>
        </div>

        <!-- ÁREA DEL MAPA (CONTIENE EL MAPA Y SU LEYENDA) -->
        <div id="mapArea" class="relative">
          <div id="franchiseMap"></div>
          
          <!-- Badge flotante de clubes desplegados de la cadena seleccionada -->
          <div id="subClubsBadge" class="hidden absolute top-4 right-4 z-[400] bg-slate-900/90 backdrop-blur-md text-white text-xs px-3.5 py-1.5 rounded-full shadow-lg border border-slate-700 flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-[#f2920b] animate-pulse"></span>
            <span id="subClubsBadgeText" class="font-bold">Desplegados clubes</span>
            <button onclick="clearSubClubs()" title="Quitar subsedes" class="ml-1 text-slate-400 hover:text-white font-black text-sm cursor-pointer leading-none">&times;</button>
          </div>
          
          <!-- Leyenda del mapa -->
          <div class="flex items-center gap-3 sm:gap-6 px-3 py-2 mt-2 text-[11px] font-bold text-slate-600 flex-wrap border-t border-slate-100">
            <span class="text-slate-400 uppercase">Tipología:</span>
            <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-full bg-[#0284c7]"></span> Cadena Multiclub</span>
            <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-full bg-[#2563eb]"></span> Red Corporativa</span>
            <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-full bg-[#4f46e5]"></span> Franquicia</span>
            <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-full bg-[#059669]"></span> Automatizado 24/7</span>
            <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-full bg-[#9333ea]"></span> Boutique Lujo</span>
          </div>
        </div>
      </div>

      <!-- VISTA GRID (TARJETAS COMPACTAS CON FONDO TEXTURADO PARA RESALTAR) -->
      <div id="gridView" class="bg-textured-blue rounded-3xl p-5 sm:p-7 shadow-inner grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 sm:gap-5">
        {cards_html}
      </div>

      <!-- VISTA TABLA (COMPARATIVA) -->
      <div id="tableView" class="hidden bg-white rounded-3xl border border-slate-200/90 shadow-sm overflow-hidden">
        <div class="overflow-x-auto">
          <table class="w-full text-left text-sm">
            <thead class="bg-slate-900 text-white font-heading font-black text-xs uppercase tracking-wider">
              <tr>
                <th class="py-4 px-3 text-center">Comparar</th>
                <th class="py-4 px-4">Operador / Cadena</th>
                <th class="py-4 px-4">Modelo</th>
                <th class="py-4 px-4">Sede Principal</th>
                <th class="py-4 px-4">Clubes</th>
                <th class="py-4 px-4">Pistas</th>
                <th class="py-4 px-4">Software</th>
                <th class="py-4 px-4">Enfoque</th>
                <th class="py-4 px-4 text-right">Dossier</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-100">
              {table_rows_html}
            </tbody>
          </table>
        </div>
      </div>

    </section>

    <!-- BLOQUE B2B COOLPADEL: SERVICIOS PARA FRANQUICIAS Y CADENAS -->
    <section class="py-16 bg-slate-900 text-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div class="max-w-3xl mb-12">
          <span class="text-xs font-bold text-[#f2920b] uppercase tracking-wider block mb-2">CoolPadel B2B Solutions</span>
          <h2 class="font-heading font-black text-3xl sm:text-4xl text-white uppercase tracking-tight">
            ¿Gestionas una Cadena de Clubs o estás creando una Franquicia de Pádel?
          </h2>
          <p class="text-slate-400 text-base sm:text-lg mt-3 leading-relaxed">
            Ayudamos a operadores multiclub de toda Europa a monetizar su masa social y diferenciar sus pistas con merchandising oficial de alta rentabilidad y sistemas de grabación inteligentes sin obras.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          
          <!-- Solución 1: Llaveros Merchandising -->
          <div class="bg-slate-800/80 rounded-3xl p-8 border border-slate-700/80 flex flex-col justify-between">
            <div>
              <div class="text-[#f2920b] flex items-center justify-start mb-4">
                <i data-lucide="sparkles" class="w-6 h-6 stroke-[2.5]"></i>
              </div>
              <h3 class="font-heading font-black text-2xl text-white uppercase mb-3">
                Merchandising Oficial Personalizado en 3D
              </h3>
              <p class="text-slate-300 text-sm leading-relaxed mb-6">
                Fabricamos llaveros de goma 3D con relieve exacto de tu logotipo o pala corporativa. El producto de bienvenida perfecto para torneos, welcome packs de socios y venta en el mostrador pro-shop con un margen superior al 250%.
              </p>
              <ul class="space-y-2.5 text-xs text-slate-300 font-medium mb-6">
                <li class="flex items-center gap-2"><i data-lucide="check-circle" class="w-4 h-4 text-emerald-400"></i> Diseño 3D digital gratuito antes de producir</li>
                <li class="flex items-center gap-2"><i data-lucide="check-circle" class="w-4 h-4 text-emerald-400"></i> Pedido mínimo desde solo 100 unidades</li>
                <li class="flex items-center gap-2"><i data-lucide="check-circle" class="w-4 h-4 text-emerald-400"></i> Muestra física real disponible para cadenas</li>
              </ul>
            </div>

            <a href="../#llaveros" class="inline-flex items-center justify-between px-6 py-3.5 rounded-2xl bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition group">
              <span>Descubrir Llaveros de Pádel 3D</span>
              <i data-lucide="arrow-right" class="w-4 h-4 group-hover:translate-x-1 transition-transform"></i>
            </a>
          </div>

          <!-- Solución 2: Save My Play Grabación -->
          <div class="bg-slate-800/80 rounded-3xl p-8 border border-slate-700/80 flex flex-col justify-between">
            <div>
              <div class="w-12 h-12 rounded-2xl bg-[#76d3f6]/20 text-[#76d3f6] flex items-center justify-center mb-6">
                <i data-lucide="video" class="w-6 h-6 stroke-[2.5]"></i>
              </div>
              <h3 class="font-heading font-black text-2xl text-white uppercase mb-3">
                Cámaras de Grabación en Pista 'Save My Play'
              </h3>
              <p class="text-slate-300 text-sm leading-relaxed mb-6">
                El sistema de grabación inteligente diseñado para pistas de pádel sin necesidad de obras ni zanjas en el cristal. Botón pulsador en red para guardar los mejores puntos y descarga instantánea en el smartphone del jugador.
              </p>
              <ul class="space-y-2.5 text-xs text-slate-300 font-medium mb-6">
                <li class="flex items-center gap-2"><i data-lucide="check-circle" class="w-4 h-4 text-[#76d3f6]"></i> Instalación no invasiva Plug & Play en menos de 2 horas</li>
                <li class="flex items-center gap-2"><i data-lucide="check-circle" class="w-4 h-4 text-[#76d3f6]"></i> Monetización directa por descarga de vídeo o cuota de socio</li>
                <li class="flex items-center gap-2"><i data-lucide="check-circle" class="w-4 h-4 text-[#76d3f6]"></i> Viralidad orgánica en TikTok e Instagram con el logo de tu cadena</li>
              </ul>
            </div>

            <a href="{home_url}save-my-play/" class="inline-flex items-center justify-between px-6 py-3.5 rounded-2xl bg-[#76d3f6] hover:bg-[#f2920b] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition group">
              <span>Ver Tecnología de Cámaras Save My Play</span>
              <i data-lucide="arrow-right" class="w-4 h-4 group-hover:translate-x-1 transition-transform"></i>
            </a>
          </div>

        </div>

      </div>
    </section>

  </main>

  <!-- FOOTER INFERIOR (COLOR CELESTE LLAVEROS #3478a6 CON TEXTURA CANVA: BRANDING COOLPADEL, SILOS TEMÁTICOS SEO Y COPYRIGHT) -->
  <footer class="relative z-20 bg-[#3478a6] bg-textured-blue text-white pt-14 pb-10 border-t border-sky-700/40 text-xs">
    <div class="max-w-[1700px] mx-auto px-4 sm:px-8 space-y-10">
      
      <!-- TOP: BRANDING Y DESCRIPCIÓN B2B -->
      <div class="flex flex-col sm:flex-row items-center justify-between gap-4 pb-8 border-b border-white/20">
        <div class="flex items-center gap-3.5">
          <img src="../assets/images/coolpadel-mascot-hd.png" alt="CoolPadel Mascota" width="60" height="60" class="h-10 sm:h-12 w-auto object-contain drop-shadow-sm" loading="lazy">
          <img src="../assets/images/coolpadel-typography-hd.png" alt="CoolPadel" width="160" height="32" class="h-5 sm:h-6 w-auto object-contain drop-shadow-sm" loading="lazy">
        </div>
        <p class="text-white/80 text-xs text-center sm:text-right max-w-md font-medium">
          Fabricación de llaveros de pádel personalizados 3D y sistemas de cámaras de grabación en pista Save my Play.
        </p>
      </div>

      <!-- 4 COLUMNAS DE SILOS TEMÁTICOS SEO -->
      <nav aria-label="Estructura y Silos SEO de CoolPadel" class="grid grid-cols-2 lg:grid-cols-4 gap-8 text-left">
        
        <!-- COLUMNA 1: SOLUCIONES B2B -->
        <div class="space-y-3">
          <div class="font-heading font-black text-sm uppercase tracking-wider text-white">
            Soluciones B2B
          </div>
          <ul class="space-y-2 text-white/80 font-normal">
            <li><a href="/llaveros-padel-personalizados/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Llaveros de Pádel 3D</a></li>
            <li><a href="/llaveros-tenis-personalizados/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Llaveros de Tenis y Pickleball</a></li>
            <li><a href="/welcome-packs-torneos-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Welcome Packs para Torneos</a></li>
            <li><a href="/llaveros-personalizados-clubs-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Merchandising para Clubs</a></li>
            <li><a href="/save-my-play/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Cámaras Save my Play</a></li>
            <li><a href="/camaras-grabacion-pistas-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Grabación en Pista de Pádel</a></li>
          </ul>
        </div>

        <!-- COLUMNA 2: INTEGRACIONES SAAS & PISTAS -->
        <div class="space-y-3">
          <div class="font-heading font-black text-sm uppercase tracking-wider text-white">
            Software &amp; Pistas
          </div>
          <ul class="space-y-2 text-white/80 font-normal">
            <li><a href="/camaras-padel-playtomic/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Integración con Playtomic</a></li>
            <li><a href="/camaras-padel-matchi/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Compatibilidad Matchi</a></li>
            <li><a href="/camaras-padel-resasports/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Conexión Resasports &amp; Syltek</a></li>
            <li><a href="/blog/smart-courts-pistas-inteligentes-padel-horas-valle/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Smart Courts y Domótica</a></li>
            <li><a href="/blog/retransmitir-torneos-padel-streaming-youtube-camaras/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Streaming en Directo YouTube</a></li>
          </ul>
        </div>

        <!-- COLUMNA 3: HERRAMIENTAS GRATIS & DIRECTORIO -->
        <div class="space-y-3">
          <div class="font-heading font-black text-sm uppercase tracking-wider text-white">
            Herramientas &amp; Hubs
          </div>
          <ul class="space-y-2 text-white/80 font-normal">
            <li><a href="/herramientas/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition font-bold text-[#f2920b]">Suite Herramientas Gratis</a></li>
            <li><a href="/herramientas/generador-americana-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Generador de Americana Pádel</a></li>
            <li><a href="/herramientas/generador-cuadros-torneo-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Sorteo de Cuadros de Torneo</a></li>
            <li><a href="/herramientas/calculadora-coste-pistas-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Calculadora Coste Pistas</a></li>
            <li><a href="/herramientas/calculadora-roi-camaras-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Calculadora ROI Cámaras</a></li>
            <li><a href="/franquicias-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Directorio Franquicias (+167)</a></li>
            <li><a href="/camaras-padel-madrid/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Clubes Pádel Madrid</a></li>
            <li><a href="/camaras-padel-barcelona/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Clubes Pádel Barcelona</a></li>
          </ul>
        </div>

        <!-- COLUMNA 4: GUÍAS DEL SECTOR -->
        <div class="space-y-3">
          <div class="font-heading font-black text-sm uppercase tracking-wider text-white">
            Guías &amp; Blog B2B
          </div>
          <ul class="space-y-2 text-white/80 font-normal">
            <li><a href="/blog/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition font-bold text-white">Índice del Blog &amp; Estudios</a></li>
            <li><a href="/blog/barometro-camaras-padel-2026/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Barómetro Cámaras Pádel 2026</a></li>
            <li><a href="/blog/como-organizar-torneo-padel-americana-reglas-cuadros/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Cómo Organizar una Americana</a></li>
            <li><a href="/blog/cuanto-cuesta-montar-pista-padel-presupuesto-rentabilidad/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Cuánto Cuesta Montar una Pista</a></li>
            <li><a href="/blog/rentabilidad-camaras-pistas-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Precios y ROI de Cámaras</a></li>
            <li><a href="/blog/sistemas-grabacion-pistas-padel-comparativa/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Cámaras Fijas vs Trípodes (RGPD)</a></li>
            <li><a href="/blog/welcome-pack-torneo-padel-ideas/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Ideas de Welcome Pack</a></li>
          </ul>
        </div>

      </nav>

      <!-- BOTTOM: COPYRIGHT Y ENLACES LEGALES -->
      <div class="pt-8 border-t border-white/20 flex flex-col sm:flex-row items-center justify-between gap-3 text-white/75 text-center sm:text-left">
        <span id="admin-toggle-trigger" class="hover:text-white/90 transition cursor-pointer" title="Modo Administrador">
          © 2026 CoolPadel Studios · All rights reserved
        </span>
        <div class="flex items-center gap-3">
          <a href="/politica-de-devoluciones.html" class="hover:text-white/90 underline decoration-white/30 underline-offset-2 transition" title="Política de Devoluciones y Garantía">Política de Devoluciones</a>
          <span class="opacity-40">·</span>
          <a href="https://www.instagram.com/coolpadel_/" target="_blank" rel="noopener noreferrer" class="opacity-75 hover:opacity-100 transition text-white" title="Instagram CoolPadel">@coolpadel_</a>
        </div>
      </div>

    </div>
  </footer>

  <!-- BARRA FLOTANTE DE COMPARACIÓN CARA A CARA (BOTTOM BAR) -->
  <div id="compareFloatingBar" class="fixed bottom-6 left-1/2 -translate-x-1/2 z-40 w-[95%] max-w-4xl bg-slate-950/95 backdrop-blur-md text-white rounded-3xl p-4 sm:p-5 border border-slate-700 shadow-2xl transition-all duration-300 transform translate-y-32 opacity-0 pointer-events-none flex flex-col sm:flex-row items-center justify-between gap-4">
    <div class="flex items-center gap-3 flex-wrap">
      <div class="flex items-center gap-1.5 px-3 py-1.5 bg-[#f2920b] text-slate-950 rounded-xl font-heading font-black text-xs uppercase tracking-wider">
        <i data-lucide="scale" class="w-4 h-4"></i>
        <span id="compareCountPill">0 / 3</span>
      </div>
      <span class="text-xs font-bold text-slate-300 hidden md:inline">Seleccionadas:</span>
      <div id="compareChips" class="flex items-center gap-2 flex-wrap">
        <!-- Chips dinámicos -->
      </div>
    </div>

    <div class="flex items-center gap-2.5 w-full sm:w-auto justify-end">
      <button onclick="clearCompare()" class="px-3 py-2 rounded-xl text-xs font-bold text-slate-400 hover:text-white transition">
        Limpiar
      </button>
      <button onclick="openCompareModal()" class="px-5 py-2.5 rounded-xl bg-[#f2920b] hover:bg-[#d97f08] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition shadow-md flex items-center gap-1.5 hover:scale-105 active:scale-95">
        <span>Comparar Cara a Cara</span>
        <i data-lucide="arrow-right" class="w-4 h-4"></i>
      </button>
    </div>
  </div>

  <!-- MODAL COMPARADOR CARA A CARA (SIDE-BY-SIDE MATRIX) -->
  <div id="compareModalOverlay" class="fixed inset-0 bg-slate-950/80 backdrop-blur-sm z-50 transition-opacity opacity-0 pointer-events-none flex items-center justify-center p-3 sm:p-6" onclick="closeCompareModal()">
    <div id="compareModal" class="bg-white w-full max-w-6xl max-h-[92vh] rounded-3xl shadow-2xl border border-slate-200 overflow-hidden flex flex-col transform scale-95 transition-transform duration-300" onclick="event.stopPropagation()">
      
      <!-- Header Modal -->
      <div class="p-5 sm:p-6 bg-slate-900 text-white flex items-center justify-between border-b border-slate-800 shrink-0">
        <div class="flex items-center gap-3">
          <div class="text-[#f2920b] flex items-center justify-center shrink-0">
            <i data-lucide="scale" class="w-5 h-5"></i>
          </div>
          <div>
            <h2 class="font-heading font-black text-xl sm:text-2xl text-white uppercase tracking-tight">Comparativa Cara a Cara de Franquicias</h2>
            <p class="text-xs text-slate-400 font-medium">Contraste de requisitos inmobiliarios, cánones económicos, tecnología y retorno para inversores y clubes</p>
          </div>
        </div>
        <button onclick="closeCompareModal()" class="w-9 h-9 rounded-full bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white flex items-center justify-center transition shrink-0">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>

      <!-- Body Modal: Dynamic Matrix Table -->
      <div id="compareModalContent" class="p-4 sm:p-8 overflow-y-auto overflow-x-auto flex-1 space-y-6 text-sm">
        <!-- Se inyecta la tabla comparativa por JS -->
      </div>

    </div>
  </div>

  <!-- SLIDE-OVER DRAWER MODAL (DOSSIER COMPLETO DE LA FRANQUICIA) -->
  <div id="drawerOverlay" class="fixed inset-0 bg-slate-950/60 backdrop-blur-xs z-50 transition-opacity opacity-0 pointer-events-none" onclick="closeDrawer()"></div>

  <div id="franchiseDrawer" class="fixed top-0 right-0 h-full w-full max-w-2xl bg-white shadow-2xl z-50 transform translate-x-full transition-transform duration-300 ease-in-out flex flex-col overflow-hidden">
    
    <!-- Drawer Header -->
    <div class="p-6 border-b border-slate-200/90 flex items-start justify-between bg-slate-50">
      <div class="space-y-1">
        <div class="flex items-center gap-2">
          <span id="drawerFlag" class="text-2xl"></span>
          <span id="drawerBadge" class="inline-block px-2.5 py-0.5 rounded-full text-xs font-bold border"></span>
        </div>
        <h2 id="drawerTitle" class="font-heading font-black text-2xl sm:text-3xl text-slate-950">Ficha Técnica de Cadena de Pádel</h2>
        <div class="flex items-center gap-2.5 pt-1 flex-wrap">
          <p id="drawerCity" class="text-xs font-semibold text-slate-500 flex items-center gap-1"></p>
          <button type="button" onclick="focusClubOnMap(currentDrawerId, true, true)" class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-slate-200/80 hover:bg-[#f2920b] hover:text-slate-950 text-xs font-bold text-slate-800 transition cursor-pointer shadow-2xs" title="Ver en el mapa interactivo">
            <i data-lucide="map" class="w-3.5 h-3.5"></i>
            <span>Ver en el mapa</span>
          </button>
        </div>
      </div>

      <button onclick="closeDrawer()" class="w-10 h-10 rounded-full bg-white hover:bg-slate-200 flex items-center justify-center text-slate-500 hover:text-slate-900 transition border border-slate-200">
        <i data-lucide="x" class="w-5 h-5"></i>
      </button>
    </div>

    <!-- Drawer Body -->
    <div class="p-6 sm:p-8 overflow-y-auto flex-1 space-y-6 text-sm">
      
      <!-- Banner Reclamar Ficha dentro del Drawer -->
      <div class="p-4 bg-gradient-to-r from-amber-50 to-orange-50 border border-amber-200/80 rounded-2xl flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 shadow-2xs">
        <div class="space-y-0.5">
          <div class="flex items-center gap-1.5 text-xs font-bold text-amber-950">
            <i data-lucide="shield-check" class="w-4 h-4 text-[#f2920b]"></i>
            <span>¿Eres el Responsable de Expansión de esta Cadena?</span>
          </div>
          <p class="text-[11px] text-amber-800 leading-tight">
            Reclama tu ficha, actualiza tus requisitos de nave y cánones, y recibe solicitudes directas de inversores cualificados.
          </p>
        </div>
        <button onclick="claimCurrentFranchise()" class="shrink-0 inline-flex items-center gap-1 px-3.5 py-2 rounded-xl bg-[#f2920b] hover:bg-[#d97f08] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition shadow-xs">
          <span>Reclamar Ficha</span>
          <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
        </button>
      </div>

      <!-- Tagline -->
      <div class="p-4 bg-amber-50/70 border border-amber-200 rounded-2xl text-amber-900 font-semibold italic text-sm" id="drawerTagline">
      </div>

      <!-- Resumen -->
      <div>
        <h3 class="font-heading font-black text-sm uppercase text-slate-400 tracking-wider mb-2">Visión General</h3>
        <p class="text-slate-700 leading-relaxed text-sm" id="drawerResumen"></p>
      </div>

      <!-- Métricas Clave Grid -->
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 p-4 bg-slate-50 rounded-2xl border border-slate-200">
        <div>
          <span class="block text-[11px] font-bold uppercase text-slate-400">Clubes</span>
          <span class="font-heading font-black text-base text-slate-950" id="drawerClubs"></span>
        </div>
        <div>
          <span class="block text-[11px] font-bold uppercase text-slate-400">Pistas</span>
          <span class="font-heading font-black text-base text-slate-950" id="drawerPistas"></span>
        </div>
        <div>
          <span class="block text-[11px] font-bold uppercase text-slate-400">Software</span>
          <span class="font-heading font-black text-xs text-slate-900" id="drawerSoftware"></span>
        </div>
        <div>
          <span class="block text-[11px] font-bold uppercase text-slate-400">Fundadores</span>
          <span class="font-heading font-bold text-xs text-slate-800 truncate block" id="drawerFundadores"></span>
        </div>
      </div>

      <!-- Sedes Principales -->
      <div>
        <h3 class="font-heading font-black text-sm uppercase text-slate-400 tracking-wider mb-2">Sedes & Complejos Principales</h3>
        <ul id="drawerSedes" class="space-y-1.5 text-slate-700 font-medium"></ul>
      </div>

      <!-- Tecnología y Pistas -->
      <div class="p-5 bg-slate-50 rounded-2xl border border-slate-200 space-y-2 text-xs">
        <h4 class="font-heading font-black text-xs uppercase text-slate-900 tracking-wider mb-2">Especificaciones de Instalación</h4>
        <div id="drawerTech" class="space-y-1.5 text-slate-600"></div>
      </div>

      <!-- Modelo de Expansión / Inversión -->
      <div class="p-5 bg-blue-50/60 rounded-2xl border border-blue-200 space-y-2 text-xs">
        <h4 class="font-heading font-black text-xs uppercase text-blue-900 tracking-wider mb-2">Modelo de Negocio & Expansión</h4>
        <div id="drawerExpansion" class="space-y-1.5 text-blue-800"></div>
      </div>

      <!-- Factor Diferencial -->
      <div>
        <h3 class="font-heading font-black text-sm uppercase text-slate-400 tracking-wider mb-2">Ventaja Competitiva / Diferencial</h3>
        <p class="text-slate-700 leading-relaxed text-sm bg-slate-50 p-4 rounded-2xl border border-slate-200" id="drawerDiferencial"></p>
      </div>

    </div>

    <!-- Drawer Footer (Acciones) -->
    <div class="p-5 border-t border-slate-200/90 bg-slate-50 flex items-center justify-between gap-2 sm:gap-3 flex-wrap">
      <div class="flex items-center gap-2">
        <a id="drawerPageBtn" href="#" class="inline-flex items-center gap-1.5 px-3.5 sm:px-4 py-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-white text-xs font-bold transition">
          <span>Ver Ficha Completa</span>
          <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
        </a>
        <a id="drawerWebBtn" href="#" target="_blank" class="inline-flex items-center gap-1.5 px-3 sm:px-3.5 py-2.5 rounded-xl bg-white border border-slate-200 hover:bg-slate-100 text-slate-800 text-xs font-bold transition" rel="noopener noreferrer">
          <span>Web</span>
          <i data-lucide="external-link" class="w-3 h-3 text-slate-400"></i>
        </a>
      </div>

      <a id="drawerWaBtn" href="#" target="_blank" class="inline-flex items-center gap-1.5 px-4 sm:px-5 py-2.5 rounded-xl bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 text-xs font-heading font-black uppercase tracking-wider transition" rel="noopener noreferrer">
        <span>Consultar</span>
        <i data-lucide="message-circle" class="w-3.5 h-3.5 stroke-[2.5]"></i>
      </a>
    </div>

  </div>

  <!-- BANNER FLOTANTE DATA GUARD (ESTILO PADEL GENIE - ACTIVIDAD INUSUAL) -->
  <div id="dataGuardBanner" class="fixed bottom-6 left-1/2 -translate-x-1/2 z-50 max-w-xl w-[calc(100vw-2rem)] bg-slate-950 text-white rounded-2xl shadow-2xl border border-amber-500/30 p-4 sm:p-5 flex flex-col sm:flex-row items-center justify-between gap-4 transition-all duration-300 opacity-0 pointer-events-none translate-y-8" role="alert">
    <div class="flex items-start gap-3 text-left">
      <div class="w-10 h-10 rounded-xl bg-amber-500/20 text-[#f2920b] flex items-center justify-center shrink-0 border border-amber-500/30 text-lg">
        🛡️
      </div>
      <div>
        <div class="flex items-center gap-2 mb-1">
          <span class="text-xs font-black uppercase tracking-wider text-[#f2920b]" id="dataGuardTag">Acceso de Datos en Pausa</span>
          <span class="w-1.5 h-1.5 rounded-full bg-amber-400 animate-pulse"></span>
        </div>
        <p class="text-xs sm:text-sm text-slate-300 leading-snug" id="dataGuardMsg">
          Hemos detectado una tasa inusual de consultas en el visor de cadenas. Si necesitas la base de datos o análisis de mercado a escala, contáctanos directamente.
        </p>
      </div>
    </div>
    <div class="flex items-center gap-2 shrink-0 w-full sm:w-auto">
      <a href="https://wa.me/34623976697?text=Hola%20Javier,%20me%20gustar%C3%ADa%20solicitar%20el%20censo%20completo%20de%20franquicias%20y%20cadenas%20de%20p%C3%A1del%20para%20un%20estudio%20de%20mercado."
         target="_blank" rel="noopener noreferrer"
         class="flex-1 sm:flex-initial inline-flex items-center justify-center gap-1.5 px-4 py-2.5 rounded-xl bg-[#f2920b] hover:bg-[#d97f08] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition shadow-md shadow-amber-500/20 whitespace-nowrap">
        <span>Hablar por WhatsApp</span>
        <i data-lucide="message-circle" class="w-3.5 h-3.5 stroke-[2.5]"></i>
      </a>
      <button onclick="dismissDataGuard()" class="w-8 h-8 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-slate-400 hover:text-white flex items-center justify-center transition shrink-0" title="Cerrar">
        <i data-lucide="x" class="w-4 h-4"></i>
      </button>
    </div>
  </div>

  <!-- MODAL ONBOARDING / RECLAMAR FICHA (4 PASOS B2B) -->
  <div id="onboardingModalOverlay" class="fixed inset-0 bg-slate-950/80 backdrop-blur-sm z-50 transition-opacity opacity-0 pointer-events-none flex items-center justify-center p-3 sm:p-6" onclick="closeOnboardingModal()">
    <div id="onboardingModal" class="bg-white w-full max-w-2xl max-h-[94vh] rounded-3xl shadow-2xl border border-slate-200 overflow-hidden flex flex-col transform scale-95 transition-transform duration-300" onclick="event.stopPropagation()">
      
      <!-- Modal Header -->
      <div class="p-6 bg-slate-900 text-white flex items-start justify-between border-b border-slate-800 shrink-0">
        <div>
          <div class="inline-flex items-center gap-1.5 text-[#f2920b] text-[11px] font-bold uppercase tracking-wider mb-2">
            <i data-lucide="badge-check" class="w-3.5 h-3.5"></i>
            <span>Homologación B2B Censo Oficial 2026</span>
          </div>
          <h2 id="onboardingModalTitle" class="font-heading font-black text-2xl text-white uppercase tracking-tight">
            Alta / Reclamar Ficha de Franquicia
          </h2>
          <p class="text-xs text-slate-400 mt-1">
            Completa los requisitos clave para contrastar tu modelo frente a inversores y clubes candidatos.
          </p>
        </div>
        <button onclick="closeOnboardingModal()" class="w-9 h-9 rounded-full bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white flex items-center justify-center transition shrink-0">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>

      <!-- Steps Indicator -->
      <div class="px-6 py-3 bg-slate-100 border-b border-slate-200 grid grid-cols-4 gap-2 text-[11px] font-bold shrink-0">
        <div id="step-indicator-1" class="text-center py-1 rounded-lg bg-[#f2920b] text-slate-950 transition">1. Responsable</div>
        <div id="step-indicator-2" class="text-center py-1 rounded-lg bg-slate-200 text-slate-600 transition">2. Espacio & Nave</div>
        <div id="step-indicator-3" class="text-center py-1 rounded-lg bg-slate-200 text-slate-600 transition">3. Cánones & ROI</div>
        <div id="step-indicator-4" class="text-center py-1 rounded-lg bg-slate-200 text-slate-600 transition">4. Tecnología</div>
      </div>

      <!-- Modal Form Content -->
      <form id="onboardingForm" onsubmit="submitOnboarding(event)" class="p-6 sm:p-8 overflow-y-auto flex-1 space-y-6">
        
        <!-- PASO 1: RESPONSABLE & MARCA -->
        <div id="onboardingStep1" class="space-y-4">
          <h3 class="font-heading font-black text-base text-slate-900 uppercase">1. Identificación y Contacto de Expansión</h3>
          
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label class="block text-xs font-bold text-slate-700 mb-1">Nombre de la Franquicia / Cadena *</label>
              <input type="text" id="ob_nombre" required placeholder="Ej. Bela Padel Center" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:ring-2 focus:ring-[#f2920b] focus:outline-none">
            </div>
            <div>
              <label class="block text-xs font-bold text-slate-700 mb-1">Sitio Web Oficial *</label>
              <input type="url" id="ob_web" required placeholder="https://..." class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:ring-2 focus:ring-[#f2920b] focus:outline-none">
            </div>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label class="block text-xs font-bold text-slate-700 mb-1">País y Ciudad Sede *</label>
              <input type="text" id="ob_sede" required placeholder="Ej. Madrid, España" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:ring-2 focus:ring-[#f2920b] focus:outline-none">
            </div>
            <div>
              <label class="block text-xs font-bold text-slate-700 mb-1">Nº Actual de Clubes Operativos *</label>
              <input type="number" id="ob_num_clubs" min="1" required placeholder="Ej. 6" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:ring-2 focus:ring-[#f2920b] focus:outline-none">
            </div>
          </div>

          <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200 space-y-3">
            <span class="text-xs font-bold uppercase text-slate-600 block">Datos del Responsable de Expansión (Para Inversores)</span>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
              <div>
                <label class="block text-[11px] font-bold text-slate-600 mb-1">Responsable *</label>
                <input type="text" id="ob_contacto_nombre" required placeholder="Nombre y Apellidos" class="w-full px-3 py-2 rounded-lg border border-slate-300 text-xs focus:ring-2 focus:ring-[#f2920b] focus:outline-none">
              </div>
              <div>
                <label class="block text-[11px] font-bold text-slate-600 mb-1">Cargo *</label>
                <input type="text" id="ob_contacto_cargo" required placeholder="Director de Expansión" class="w-full px-3 py-2 rounded-lg border border-slate-300 text-xs focus:ring-2 focus:ring-[#f2920b] focus:outline-none">
              </div>
              <div>
                <label class="block text-[11px] font-bold text-slate-600 mb-1">Email Corporativo *</label>
                <input type="email" id="ob_contacto_email" required placeholder="expansion@marca.com" class="w-full px-3 py-2 rounded-lg border border-slate-300 text-xs focus:ring-2 focus:ring-[#f2920b] focus:outline-none">
              </div>
            </div>
            <div>
              <label class="block text-[11px] font-bold text-slate-600 mb-1">Teléfono Directo / WhatsApp de Expansión *</label>
              <input type="tel" id="ob_contacto_tel" required placeholder="+34 600 000 000" class="w-full px-3 py-2 rounded-lg border border-slate-300 text-xs focus:ring-2 focus:ring-[#f2920b] focus:outline-none">
            </div>
          </div>
        </div>

        <!-- PASO 2: ESPACIO & NAVE -->
        <div id="onboardingStep2" class="space-y-4 hidden">
          <h3 class="font-heading font-black text-base text-slate-900 uppercase">2. Requisitos de Espacio e Instalación</h3>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label class="block text-xs font-bold text-slate-700 mb-1">Tipo de Instalación Admitida *</label>
              <select id="ob_tipo_instalacion" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:ring-2 focus:ring-[#f2920b] focus:outline-none">
                <option value="indoor">Exclusivamente Nave Indoor Cubierta</option>
                <option value="outdoor">Outdoor / Cubierta Ligera Tensada</option>
                <option value="hibrido">Híbrido (Indoor + Outdoor)</option>
                <option value="ambos">Abierto a cualquier formato viable</option>
              </select>
            </div>
            <div>
              <label class="block text-xs font-bold text-slate-700 mb-1">Altura Libre Mínima de Techo *</label>
              <select id="ob_altura_minima" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:ring-2 focus:ring-[#f2920b] focus:outline-none">
                <option value="8.0m">8.0 metros (mínimo estándar)</option>
                <option value="8.5m">8.5 metros</option>
                <option value="9.0m">9.0 metros (recomendado competición)</option>
                <option value="10.0m+">10.0 metros o más (World Padel standard)</option>
              </select>
            </div>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label class="block text-xs font-bold text-slate-700 mb-1">Número Mínimo de Pistas por Club *</label>
              <input type="number" id="ob_pistas_minimas" min="2" max="30" value="4" required class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:ring-2 focus:ring-[#f2920b] focus:outline-none">
            </div>
            <div>
              <label class="block text-xs font-bold text-slate-700 mb-1">Metros Cuadrados Mínimos de Parcela/Nave</label>
              <input type="text" id="ob_m2_minimos" placeholder="Ej. 1.800 m² nave + parking" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:ring-2 focus:ring-[#f2920b] focus:outline-none">
            </div>
          </div>

          <div>
            <label class="block text-xs font-bold text-slate-700 mb-1">Ubicación Preferente</label>
            <input type="text" id="ob_ubicacion_perfil" placeholder="Ej. Polígono periurbano con accesos rápidos, retail parks o clubes deportivos consolidados" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:ring-2 focus:ring-[#f2920b] focus:outline-none">
          </div>
        </div>

        <!-- PASO 3: CÁNONES & INVERSIÓN -->
        <div id="onboardingStep3" class="space-y-4 hidden">
          <h3 class="font-heading font-black text-base text-slate-900 uppercase">3. Condiciones Económicas y Modelo de Franquicia</h3>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label class="block text-xs font-bold text-slate-700 mb-1">Canon de Entrada (Franchise Fee) *</label>
              <input type="text" id="ob_canon_entrada" required placeholder="Ej. 18.000 € o Sin canon inicial" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:ring-2 focus:ring-[#f2920b] focus:outline-none">
            </div>
            <div>
              <label class="block text-xs font-bold text-slate-700 mb-1">Royalty Mensual de Operación *</label>
              <input type="text" id="ob_royalty_mensual" required placeholder="Ej. 5% de facturación bruta o 400€/pista/mes" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:ring-2 focus:ring-[#f2920b] focus:outline-none">
            </div>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label class="block text-xs font-bold text-slate-700 mb-1">Canon de Marketing Corporativo</label>
              <input type="text" id="ob_canon_marketing" placeholder="Ej. 1% facturación o Incluido en el royalty" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:ring-2 focus:ring-[#f2920b] focus:outline-none">
            </div>
            <div>
              <label class="block text-xs font-bold text-slate-700 mb-1">Inversión Media Llave en Mano (CAPEX) *</label>
              <input type="text" id="ob_inversion_media" required placeholder="Ej. 450.000 € a 850.000 € para 6 pistas" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:ring-2 focus:ring-[#f2920b] focus:outline-none">
            </div>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label class="block text-xs font-bold text-slate-700 mb-1">Plazo de Retorno Estimado (Payback)</label>
              <input type="text" id="ob_payback" placeholder="Ej. 24 a 36 meses" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:ring-2 focus:ring-[#f2920b] focus:outline-none">
            </div>
            <div>
              <label class="block text-xs font-bold text-slate-700 mb-1">Exclusividad Territorial Garantizada *</label>
              <input type="text" id="ob_exclusividad" required placeholder="Ej. 10 km de radio o término municipal protegido" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:ring-2 focus:ring-[#f2920b] focus:outline-none">
            </div>
          </div>
        </div>

        <!-- PASO 4: TECNOLOGÍA & SERVICIOS -->
        <div id="onboardingStep4" class="space-y-4 hidden">
          <h3 class="font-heading font-black text-base text-slate-900 uppercase">4. Tecnología, Domótica y Operativa</h3>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label class="block text-xs font-bold text-slate-700 mb-1">Software de Reservas Obligatorio *</label>
              <input type="text" id="ob_software" required placeholder="Ej. Playtomic, Matchi, App Propia o Libre" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:ring-2 focus:ring-[#f2920b] focus:outline-none">
            </div>
            <div>
              <label class="block text-xs font-bold text-slate-700 mb-1">Nivel de Domótica & Accesos</label>
              <input type="text" id="ob_domotica" placeholder="Ej. Tornos QR automáticos, encendido domótico de focos" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:ring-2 focus:ring-[#f2920b] focus:outline-none">
            </div>
          </div>

          <div>
            <label class="block text-xs font-bold text-slate-700 mb-1">Cámaras de Grabación en Pista / Streaming</label>
            <input type="text" id="ob_camaras" placeholder="Ej. Homologado para Save my Play / CoolPadel o cámaras en pistas centrales" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:ring-2 focus:ring-[#f2920b] focus:outline-none">
          </div>

          <div>
            <label class="block text-xs font-bold text-slate-700 mb-1">Servicios Centralizados que Aporta la Franquicia</label>
            <textarea id="ob_servicios" rows="2" placeholder="Ej. Central de compras con descuentos en palas y bolas, metodología oficial de escuela, asesoría en licencia de obras" class="w-full px-4 py-2 rounded-xl border border-slate-300 text-sm focus:ring-2 focus:ring-[#f2920b] focus:outline-none"></textarea>
          </div>

          <div>
            <label class="block text-xs font-bold text-slate-700 mb-1">Factor Diferencial / Ventaja Competitiva</label>
            <textarea id="ob_diferencial" rows="2" placeholder="¿Por qué un inversor debería elegir vuestra marca antes que a otra?" class="w-full px-4 py-2 rounded-xl border border-slate-300 text-sm focus:ring-2 focus:ring-[#f2920b] focus:outline-none"></textarea>
          </div>
        </div>

        <!-- PANTALLA DE ÉXITO -->
        <div id="onboardingSuccess" class="space-y-4 py-6 text-center hidden">
          <div class="w-16 h-16 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center mx-auto mb-3">
            <i data-lucide="check" class="w-8 h-8 stroke-[3]"></i>
          </div>
          <h3 class="font-heading font-black text-2xl text-slate-900 uppercase">¡Expediente de Homologación Recibido!</h3>
          <p class="text-sm text-slate-600 max-w-md mx-auto">
            Hemos registrado tu solicitud con el código <strong id="successTicket" class="text-slate-950"></strong>. Nuestro equipo validará el dominio corporativo en menos de 24 horas y tu marca recibirá el distintivo <strong>'Franquicia Verificada 2026'</strong>.
          </p>
          <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200 max-w-md mx-auto text-xs text-slate-600">
            Los datos económicos y de nave introducidos se volcarán automáticamente en el comparador para inversores de tu región.
          </div>
          <div class="pt-4 flex justify-center gap-3">
            <a id="successWaBtn" href="#" target="_blank" class="px-5 py-2.5 rounded-xl bg-[#f2920b] hover:bg-[#d97f08] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition inline-flex items-center gap-2" rel="noopener noreferrer">
              <i data-lucide="message-circle" class="w-4 h-4"></i>
              <span>Confirmar por WhatsApp con Javier</span>
            </a>
            <button type="button" onclick="closeOnboardingModal()" class="px-5 py-2.5 rounded-xl bg-slate-200 hover:bg-slate-300 text-slate-800 font-bold text-xs transition">
              Cerrar
            </button>
          </div>
        </div>

        <!-- BOTONES DE NAVEGACIÓN -->
        <div id="onboardingNavBtns" class="pt-4 border-t border-slate-200 flex items-center justify-between">
          <button type="button" id="obPrevBtn" onclick="prevStep()" class="px-4 py-2 rounded-xl text-xs font-bold text-slate-600 hover:text-slate-900 transition disabled:opacity-30" disabled>
            ← Anterior
          </button>
          
          <div class="flex items-center gap-2">
            <button type="button" id="obNextBtn" onclick="nextStep()" class="px-6 py-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-white font-heading font-black text-xs uppercase tracking-wider transition">
              Siguiente →
            </button>
            <button type="submit" id="obSubmitBtn" class="px-6 py-2.5 rounded-xl bg-[#f2920b] hover:bg-[#d97f08] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition hidden shadow-sm">
              Enviar Homologación Oficial
            </button>
          </div>
        </div>

      </form>

    </div>
  </div>

  <!-- SCRIPT DE FILTRADO, MAPA, COMPARADOR Y ONBOARDING -->
  <script>
    lucide.createIcons();

    const FRANQUICIAS = {json.dumps(FRANQUICIAS, ensure_ascii=False)};

    let currentRegion = 'all';
    let currentModel = 'all';
    let currentBudget = 'all';
    let currentFacility = 'all';
    let currentView = 'grid';
    let map = null;
    let markersLayer = null;
    let subClubsLayer = null;
    let markersById = {{}};
    let currentDeployedChainId = null;

    let selectedFranchises = [];
    let currentStep = 1;
    let currentDrawerId = null;

    const WEBHOOK_URL = 'https://script.google.com/macros/s/AKfycbxnF9JmVrikeAW7PdLc02r_1kkuSJVz1Ncl71ZeVGT37H0ji5DQ3DVw60122pcuYnxCgA/exec';
    const GOOGLE_MAPS_API_KEY = 'AIzaSyDGYdWwepJ-wTOCIp9Y5gSXEteD50Ev24c';

    const MAP_STYLES = {{
      'google': {{
        label: 'Google Maps Clásico',
        icon: '🗺️',
        url: 'https://mt{{s}}.google.com/vt/lyrs=m&x={{x}}&y={{y}}&z={{z}}&key=' + GOOGLE_MAPS_API_KEY,
        options: {{
          subdomains: ['0', '1', '2', '3'],
          maxZoom: 20,
          attribution: '&copy; Google Maps'
        }}
      }},
      'satellite': {{
        label: 'Satélite Híbrido HD',
        icon: '🛰️',
        url: 'https://mt{{s}}.google.com/vt/lyrs=y&x={{x}}&y={{y}}&z={{z}}&key=' + GOOGLE_MAPS_API_KEY,
        options: {{
          subdomains: ['0', '1', '2', '3'],
          maxZoom: 20,
          attribution: '&copy; Google Maps & Satellite'
        }}
      }},
      'terrain': {{
        label: 'Google Relieve',
        icon: '⛰️',
        url: 'https://mt{{s}}.google.com/vt/lyrs=p&x={{x}}&y={{y}}&z={{z}}&key=' + GOOGLE_MAPS_API_KEY,
        options: {{
          subdomains: ['0', '1', '2', '3'],
          maxZoom: 20,
          attribution: '&copy; Google Maps Terrain'
        }}
      }},
      'osm_hot': {{
        label: 'OpenStreetMap Pastel',
        icon: '🎨',
        url: 'https://{{s}}.tile.openstreetmap.fr/hot/{{z}}/{{x}}/{{y}}.png',
        options: {{
          subdomains: ['a', 'b', 'c'],
          maxZoom: 19,
          attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }}
      }},
      'esri_light': {{
        label: 'Blanco Minimal B2B',
        icon: '⚪',
        url: 'https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{{z}}/{{y}}/{{x}}',
        options: {{
          maxZoom: 16,
          attribution: 'Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ'
        }}
      }},
      'osm_std': {{
        label: 'OpenStreetMap Estándar',
        icon: '🌐',
        url: 'https://tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png',
        options: {{
          maxZoom: 19,
          attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }}
      }}
    }};

    let currentTileLayer = null;
    let currentMapStyle = localStorage.getItem('coolpadel_map_style') || 'terrain';
    if (!MAP_STYLES[currentMapStyle] || currentMapStyle === 'google' || currentMapStyle === 'voyager') {{
      currentMapStyle = 'terrain';
      try {{ localStorage.setItem('coolpadel_map_style', 'terrain'); }} catch(e) {{}}
    }}

    function setMapStyle(styleKey) {{
      if (!MAP_STYLES[styleKey]) styleKey = 'terrain';
      currentMapStyle = styleKey;
      try {{
        localStorage.setItem('coolpadel_map_style', styleKey);
      }} catch (e) {{}}

      const styleDef = MAP_STYLES[styleKey];
      const lbl = document.getElementById('current-mapstyle-label');
      const icn = document.getElementById('current-mapstyle-icon');
      if (lbl) lbl.textContent = styleDef.label;
      if (icn) icn.textContent = styleDef.icon;

      const menu = document.getElementById('mapstyle-dropdown-menu');
      const arrow = document.getElementById('mapstyle-dropdown-arrow');
      if (menu) menu.classList.add('hidden');
      if (arrow) arrow.classList.remove('rotate-180');

      if (map) {{
        if (currentTileLayer) {{
          map.removeLayer(currentTileLayer);
        }}
        currentTileLayer = L.tileLayer(styleDef.url, styleDef.options).addTo(map);
        if (currentTileLayer.bringToBack) {{
          currentTileLayer.bringToBack();
        }}
      }}
    }}

    // Bounding boxes calibrados para mostrar el país completo con márgenes (extremos incluidos sin cortar)
    const REGION_BOUNDS = {{
      'all': [[32.0, -18.0], [62.0, 36.0]],
      'ES': [[35.2, -10.2], [44.4, 4.8]],   // España: Galicia, Cantábrico, Cataluña, Baleares, Andalucía y contexto Canarias
      'GB': [[49.6, -8.8], [59.2, 2.4]],    // Reino Unido: Escocia, Gales, Inglaterra e Irlanda
      'FR': [[41.8, -5.5], [51.5, 9.8]],    // Francia: Hexágono completo y Córcega
      'IT': [[35.8, 6.2], [47.4, 18.8]],    // Italia: Desde los Alpes hasta Sicilia y Cerdeña
      'NL': [[49.4, 2.2], [53.8, 7.5]],     // Benelux: Países Bajos, Bélgica y Luxemburgo
      'DE': [[45.5, 5.5], [55.0, 17.2]],    // Alemania, Austria y Suiza (DACH)
      'SE': [[54.3, 4.5], [64.5, 26.0]],    // Nórdicos: Suecia, Noruega, Dinamarca, Finlandia
      'PT': [[36.8, -10.0], [42.4, -6.0]],  // Portugal: Todo el territorio continental
      'US': [[24.0, -125.0], [49.5, -66.5]], // Estados Unidos: Costa a costa
      'MX': [[-36.0, -108.0], [29.0, -34.0]], // Latinoamérica: México, Brasil, Chile, Argentina
      'AE': [[22.0, 46.0], [30.5, 57.0]],   // Oriente Medio: EAU, Arabia, Catar, Kuwait
      'ZA': [[-35.5, 15.5], [-21.5, 34.0]]  // Sudáfrica y región
    }};

    // Bounding boxes calibrados para Comunidades Autónomas de España
    const CCAA_BOUNDS = {{
      'madrid': [[40.00, -4.35], [41.15, -3.20]],
      'catalunya': [[40.50, 0.15], [42.90, 3.35]],
      'andalucia': [[36.00, -7.55], [38.75, -1.60]],
      'valencia': [[37.85, -1.55], [40.80, 0.70]],
      'pais_vasco': [[42.45, -3.45], [43.50, -1.75]],
      'galicia': [[41.80, -9.30], [43.80, -6.70]],
      'aragon': [[39.85, -2.15], [42.95, 0.77]],
      'castilla_leon': [[40.10, -7.10], [43.25, -1.70]],
      'castilla_mancha': [[38.00, -5.40], [41.35, -1.00]],
      'baleares': [[38.60, 1.15], [40.10, 4.35]],
      'canarias': [[27.60, -18.20], [29.50, -13.30]],
      'murcia': [[37.35, -2.35], [38.75, -0.65]],
      'asturias': [[42.85, -7.20], [43.70, -4.50]],
      'cantabria': [[42.75, -4.85], [43.55, -3.15]],
      'navarra': [[41.90, -2.50], [43.35, -0.70]],
      'rioja': [[41.90, -3.15], [42.65, -1.90]],
      'extremadura': [[37.90, -7.55], [40.50, -4.65]]
    }};

    function getClubRegionBounds(f) {{
      if (!f || !f.coords || f.coords.length !== 2) return null;
      const lat = f.coords[0];
      const lng = f.coords[1];
      const ciudad = (f.ciudad_sede || '').toLowerCase();
      const pais = (f.pais || '').toLowerCase();
      const paisCod = (f.pais_codigo || '').toUpperCase();

      // Si es de España o coordenadas en territorio español
      if (paisCod === 'ES' || pais.includes('españa') || (lat >= 27.0 && lat <= 44.5 && lng >= -18.5 && lng <= 4.5)) {{
        if (ciudad.includes('madrid') || (lat >= 40.0 && lat <= 41.2 && lng >= -4.35 && lng <= -3.20)) return CCAA_BOUNDS['madrid'];
        if (ciudad.includes('barcelona') || ciudad.includes('girona') || ciudad.includes('gerona') || ciudad.includes('lleida') || ciudad.includes('lérida') || ciudad.includes('tarragona') || (lat >= 40.5 && lat <= 42.9 && lng >= 0.15 && lng <= 3.4)) return CCAA_BOUNDS['catalunya'];
        if (ciudad.includes('málaga') || ciudad.includes('malaga') || ciudad.includes('sevilla') || ciudad.includes('granada') || ciudad.includes('marbella') || ciudad.includes('córdoba') || ciudad.includes('cordoba') || ciudad.includes('cádiz') || ciudad.includes('cadiz') || ciudad.includes('almería') || ciudad.includes('almeria') || ciudad.includes('jaén') || ciudad.includes('jaen') || ciudad.includes('huelva') || (lat >= 36.0 && lat <= 38.75 && lng >= -7.55 && lng <= -1.60)) return CCAA_BOUNDS['andalucia'];
        if (ciudad.includes('valencia') || ciudad.includes('alicante') || ciudad.includes('castellón') || ciudad.includes('castellon') || ciudad.includes('elche') || (lat >= 37.85 && lat <= 40.8 && lng >= -1.55 && lng <= 0.70)) return CCAA_BOUNDS['valencia'];
        if (ciudad.includes('bilbao') || ciudad.includes('vizcaya') || ciudad.includes('bizkaia') || ciudad.includes('donostia') || ciudad.includes('san sebastián') || ciudad.includes('san sebastian') || ciudad.includes('vitoria') || ciudad.includes('álava') || ciudad.includes('alava') || (lat >= 42.45 && lat <= 43.55 && lng >= -3.45 && lng <= -1.75)) return CCAA_BOUNDS['pais_vasco'];
        if (ciudad.includes('coruña') || ciudad.includes('vigo') || ciudad.includes('pontevedra') || ciudad.includes('ourense') || ciudad.includes('orense') || ciudad.includes('lugo') || (lat >= 41.8 && lat <= 43.8 && lng >= -9.3 && lng <= -6.7)) return CCAA_BOUNDS['galicia'];
        if (ciudad.includes('zaragoza') || ciudad.includes('huesca') || ciudad.includes('teruel') || (lat >= 39.85 && lat <= 42.95 && lng >= -2.15 && lng <= 0.77)) return CCAA_BOUNDS['aragon'];
        if (ciudad.includes('valladolid') || ciudad.includes('burgos') || ciudad.includes('salamanca') || ciudad.includes('león') || ciudad.includes('leon') || ciudad.includes('palencia') || ciudad.includes('zamora') || ciudad.includes('segovia') || ciudad.includes('ávila') || ciudad.includes('avila') || ciudad.includes('soria')) return CCAA_BOUNDS['castilla_leon'];
        if (ciudad.includes('mallorca') || ciudad.includes('palma') || ciudad.includes('ibiza') || ciudad.includes('menorca')) return CCAA_BOUNDS['baleares'];
        if (ciudad.includes('canarias') || ciudad.includes('tenerife') || ciudad.includes('palmas')) return CCAA_BOUNDS['canarias'];
        if (ciudad.includes('murcia') || ciudad.includes('cartagena')) return CCAA_BOUNDS['murcia'];
        if (ciudad.includes('asturias') || ciudad.includes('gijón') || ciudad.includes('gijon') || ciudad.includes('oviedo')) return CCAA_BOUNDS['asturias'];
        if (ciudad.includes('cantabria') || ciudad.includes('santander')) return CCAA_BOUNDS['cantabria'];
        if (ciudad.includes('pamplona') || ciudad.includes('navarra')) return CCAA_BOUNDS['navarra'];
        if (ciudad.includes('logroño') || ciudad.includes('logrono') || ciudad.includes('rioja')) return CCAA_BOUNDS['rioja'];
        if (ciudad.includes('badajoz') || ciudad.includes('cáceres') || ciudad.includes('caceres') || ciudad.includes('extremadura') || ciudad.includes('mérida') || ciudad.includes('merida')) return CCAA_BOUNDS['extremadura'];
        if (ciudad.includes('toledo') || ciudad.includes('albacete') || ciudad.includes('ciudad real') || ciudad.includes('cuenca') || ciudad.includes('guadalajara')) return CCAA_BOUNDS['castilla_mancha'];

        return [[lat - 0.55, lng - 0.75], [lat + 0.55, lng + 0.75]];
      }}

      // Para el resto del mundo, encuadre a escala metropolitana/regional
      return [[lat - 0.50, lng - 0.70], [lat + 0.50, lng + 0.70]];
    }}

    function deploySubClubs(f) {{
      if (!map || !subClubsLayer) return;
      
      // Limpiar siempre la capa para que SOLO se despliegue la cadena seleccionada
      subClubsLayer.clearLayers();
      const badge = document.getElementById('subClubsBadge');

      if (!f || !f.sub_clubs || f.sub_clubs.length === 0) {{
        currentDeployedChainId = null;
        if (badge) badge.classList.add('hidden');
        return;
      }}

      currentDeployedChainId = f.id;
      const color = getMarkerColor(f.tipo_categoria);
      const allCoords = [f.coords];

      f.sub_clubs.forEach((sub, idx) => {{
        if (!sub.coords || sub.coords.length !== 2) return;
        allCoords.push(sub.coords);

        const isHQ = sub.destacado || (idx === 0);

        const subIcon = L.divIcon({{
          className: '',
          html: `<div class="sub-club-marker" style="background-color: ${{isHQ ? color : '#0b1626'}}; border: 2.5px solid ${{isHQ ? '#ffffff' : '#f2920b'}}; color: #ffffff; width: 28px; height: 28px; border-radius: 9999px; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: 900; box-shadow: 0 4px 12px rgba(0,0,0,0.4);">
            <span>${{isHQ ? '⭐' : '🎾'}}</span>
          </div>`,
          iconSize: [28, 28],
          iconAnchor: [14, 14],
          popupAnchor: [0, -14]
        }});

        const subPopupContent = `
          <div style="font-family: 'Plus Jakarta Sans', sans-serif; min-width: 210px; padding: 4px;">
            <div style="font-size: 10px; font-weight: 800; color: #f2920b; text-transform: uppercase;">${{f.nombre}} · Red (${{idx + 1}}/${{f.sub_clubs.length}})</div>
            <div style="font-family: 'Outfit', sans-serif; font-size: 14px; font-weight: 900; color: #0f172a; margin: 2px 0 4px 0;">${{sub.nombre}}</div>
            <div style="display: flex; gap: 6px; font-size: 11px; font-weight: 700; margin-bottom: 6px;">
              <span style="background: #f1f5f9; padding: 2px 6px; border-radius: 6px;">📍 ${{sub.ciudad}}</span>
              <span style="background: #fef3c7; color: #92400e; padding: 2px 6px; border-radius: 6px;">${{sub.pistas || 'Pistas'}}</span>
            </div>
            <button onclick="openDrawer('${{f.id}}')" style="width: 100%; background: #0f172a; color: #ffffff; border: none; padding: 6px 10px; border-radius: 8px; font-size: 11px; font-weight: 800; cursor: pointer;">
              Ver Dossier de ${{f.nombre}} →
            </button>
          </div>
        `;

        const subMarker = L.marker(sub.coords, {{ icon: subIcon }}).bindPopup(subPopupContent);
        subClubsLayer.addLayer(subMarker);
      }});

      if (badge) {{
        document.getElementById('subClubsBadgeText').textContent = `Desplegados ${{f.sub_clubs.length}} clubes de ${{f.nombre}}`;
        badge.classList.remove('hidden');
      }}

      // Encuadre optimizado que abarque todos los clubes desplegados de esa cadena
      if (allCoords.length > 1) {{
        const groupBounds = L.latLngBounds(allCoords);
        map.flyToBounds(groupBounds, {{
          padding: [50, 50],
          maxZoom: 10.5,
          duration: 1.3
        }});
      }}
    }}

    function clearSubClubs() {{
      if (subClubsLayer) {{
        subClubsLayer.clearLayers();
      }}
      currentDeployedChainId = null;
      const badge = document.getElementById('subClubsBadge');
      if (badge) badge.classList.add('hidden');
    }}

    function zoomToClubRegion(f, id) {{
      if (!map || !f || !f.coords || f.coords.length !== 2) return;
      map.invalidateSize();

      // Si tiene sub_clubs definidos, desplegarlos exclusivamente para esta cadena
      if (f.sub_clubs && f.sub_clubs.length > 0) {{
        deploySubClubs(f);
      }} else {{
        // Si no tiene sub_clubs, limpiar cualquier cadena anterior y hacer zoom normal a su CCAA
        clearSubClubs();
        const bounds = getClubRegionBounds(f);
        if (bounds) {{
          map.flyToBounds(bounds, {{
            padding: [30, 30],
            maxZoom: 9.5,
            duration: 1.2
          }});
        }} else {{
          map.flyTo(f.coords, 9, {{ animate: true, duration: 1.2 }});
        }}
      }}

      if (id && markersById && markersById[id]) {{
        setTimeout(() => {{
          markersById[id].openPopup();
        }}, 500);
      }}
    }}

    // Inicializar mapa con soporte multi-estilo y zoom táctil nativo
    function initMap() {{
      if (map) return;
      
      map = L.map('franchiseMap', {{
        center: [40.4168, -3.7038],
        zoom: 5,
        scrollWheelZoom: false,
        doubleClickZoom: true,
        boxZoom: true,
        touchZoom: true,
        bounceAtZoomLimits: false,
        dragging: true
      }});

      setMapStyle(currentMapStyle);

      // Prevenir que gestos de pellizco con 2 dedos en móvil hagan zoom en la página completa en vez de en el mapa
      const mapContainerEl = document.getElementById('franchiseMap');
      if (mapContainerEl) {{
        mapContainerEl.addEventListener('wheel', function(e) {{
          if (e.ctrlKey || e.metaKey) {{
            e.preventDefault();
            e.stopPropagation();
            if (e.deltaY < 0) {{
              map.setZoom(Math.min(18, map.getZoom() + 1));
            }} else if (e.deltaY > 0) {{
              map.setZoom(Math.max(3, map.getZoom() - 1));
            }}
          }}
        }}, {{ capture: true, passive: false }});

        mapContainerEl.addEventListener('touchstart', function(e) {{
          if (e.touches.length > 1) {{
            e.stopPropagation();
          }}
        }}, {{ passive: false }});

        mapContainerEl.addEventListener('touchmove', function(e) {{
          if (e.touches.length > 1) {{
            e.preventDefault();
            e.stopPropagation();
          }}
        }}, {{ passive: false }});

        mapContainerEl.addEventListener('gesturestart', function(e) {{ e.preventDefault(); e.stopPropagation(); }}, {{ passive: false }});
        mapContainerEl.addEventListener('gesturechange', function(e) {{ e.preventDefault(); e.stopPropagation(); }}, {{ passive: false }});
        mapContainerEl.addEventListener('gestureend', function(e) {{ e.preventDefault(); e.stopPropagation(); }}, {{ passive: false }});
      }}

      markersLayer = L.layerGroup().addTo(map);
      subClubsLayer = L.layerGroup().addTo(map);
      renderMarkers(FRANQUICIAS);
    }}

    function getMarkerColor(cat) {{
      switch(cat) {{
        case 'cadena': return '#0284c7';
        case 'red_propia': return '#2563eb';
        case 'franquicia': return '#4f46e5';
        case 'automatizado': return '#059669';
        case 'boutique': return '#9333ea';
        case 'academia': return '#d97706';
        default: return '#f2920b';
      }}
    }}

    function renderMarkers(items) {{
      if (!markersLayer) return;
      markersLayer.clearLayers();
      markersById = {{}};

      items.forEach(f => {{
        if (!f.coords || f.coords.length !== 2) return;
        const color = getMarkerColor(f.tipo_categoria);

        const customIcon = L.divIcon({{
          className: '',
          html: `<div class="custom-marker" style="background-color: ${{color}}; width: 32px; height: 32px; font-size: 13px;">${{f.bandera}}</div>`,
          iconSize: [32, 32],
          iconAnchor: [16, 16],
          popupAnchor: [0, -16]
        }});

        const popupContent = `
          <div style="font-family: 'Plus Jakarta Sans', sans-serif; min-width: 220px; padding: 6px;">
            <div style="font-size: 11px; font-weight: 700; color: #64748b; text-transform: uppercase;">${{f.ciudad_sede}}, ${{f.pais}}</div>
            <div style="font-family: 'Outfit', sans-serif; font-size: 16px; font-weight: 900; color: #0f172a; margin: 2px 0 6px 0;">${{f.nombre}}</div>
            <div style="display: flex; gap: 8px; font-size: 11px; font-weight: 700; margin-bottom: 8px;">
              <span style="background: #f1f5f9; padding: 2px 6px; border-radius: 6px;">${{f.num_clubs}}</span>
              <span style="background: #fef3c7; color: #92400e; padding: 2px 6px; border-radius: 6px;">${{f.num_pistas}}</span>
            </div>
            <p style="font-size: 11px; color: #475569; margin-bottom: 8px; line-height: 1.3;">${{f.tagline}}</p>
            <div style="display: flex; gap: 6px;">
              <button onclick="openDrawer('${{f.id}}')" style="flex: 1; background: #0f172a; color: #ffffff; border: none; padding: 6px 10px; border-radius: 8px; font-size: 11px; font-weight: 800; cursor: pointer;">
                Dossier →
              </button>
              <button onclick="toggleCompare('${{f.id}}')" style="background: #f2920b; color: #0f172a; border: none; padding: 6px 8px; border-radius: 8px; font-size: 11px; font-weight: 800; cursor: pointer;">
                Comparar
              </button>
            </div>
          </div>
        `;

        const marker = L.marker(f.coords, {{ icon: customIcon }})
          .bindPopup(popupContent);
        marker.on('click', () => {{
          zoomToClubRegion(f, f.id);
        }});
        markersById[f.id] = marker;
        markersLayer.addLayer(marker);
      }});
    }}

    // Vistas de mapa
    function resetMapView() {{ map.setView([46.0, 4.0], 4); }}

    // Menú desplegable flotante de estilos de mapa
    function toggleMapStyleDropdown(event) {{
      if (event) event.stopPropagation();
      const menu = document.getElementById('mapstyle-dropdown-menu');
      const arrow = document.getElementById('mapstyle-dropdown-arrow');
      if (!menu) return;
      const isOpen = !menu.classList.contains('hidden');
      if (isOpen) {{
        menu.classList.add('hidden');
        if (arrow) arrow.classList.remove('rotate-180');
      }} else {{
        menu.classList.remove('hidden');
        if (arrow) arrow.classList.add('rotate-180');
        // Cerrar selector de región si está abierto
        const regionMenu = document.getElementById('region-dropdown-menu');
        const regionArrow = document.getElementById('region-dropdown-arrow');
        if (regionMenu) regionMenu.classList.add('hidden');
        if (regionArrow) regionArrow.classList.remove('rotate-180');
      }}
    }}

    // Menú desplegable flotante de región
    function toggleRegionDropdown(event) {{
      if (event) event.stopPropagation();
      const menu = document.getElementById('region-dropdown-menu');
      const arrow = document.getElementById('region-dropdown-arrow');
      if (!menu) return;
      const isOpen = !menu.classList.contains('hidden');
      if (isOpen) {{
        menu.classList.add('hidden');
        if (arrow) arrow.classList.remove('rotate-180');
      }} else {{
        menu.classList.remove('hidden');
        if (arrow) arrow.classList.add('rotate-180');
        // Cerrar selector de estilos si está abierto
        const styleMenu = document.getElementById('mapstyle-dropdown-menu');
        const styleArrow = document.getElementById('mapstyle-dropdown-arrow');
        if (styleMenu) styleMenu.classList.add('hidden');
        if (styleArrow) styleArrow.classList.remove('rotate-180');
      }}
    }}

    document.addEventListener('click', function(e) {{
      const container = document.getElementById('region-dropdown-container');
      const menu = document.getElementById('region-dropdown-menu');
      const arrow = document.getElementById('region-dropdown-arrow');
      if (container && !container.contains(e.target) && menu && !menu.classList.contains('hidden')) {{
        menu.classList.add('hidden');
        if (arrow) arrow.classList.remove('rotate-180');
      }}

      const styleContainer = document.getElementById('mapstyle-dropdown-container');
      const styleMenu = document.getElementById('mapstyle-dropdown-menu');
      const styleArrow = document.getElementById('mapstyle-dropdown-arrow');
      if (styleContainer && !styleContainer.contains(e.target) && styleMenu && !styleMenu.classList.contains('hidden')) {{
        styleMenu.classList.add('hidden');
        if (styleArrow) styleArrow.classList.remove('rotate-180');
      }}

      const searchContainer = document.getElementById('searchContainer');
      const suggestionsMenu = document.getElementById('searchSuggestionsMenu');
      if (searchContainer && !searchContainer.contains(e.target) && suggestionsMenu && !suggestionsMenu.classList.contains('hidden')) {{
        hideSearchSuggestions();
      }}
    }});

    // =========================================================================
    // AUTOCOMPLETADO Y SUGERENCIAS DEL BUSCADOR (TÍPICO DE BUSCADOR)
    // =========================================================================
    let currentRenderedSuggestions = [];
    let selectedSuggestionIndex = -1;

    function handleSearchInput(e) {{
      const query = (e ? e.target.value : document.getElementById('searchInput').value).trim();
      const clearBtn = document.getElementById('searchClearBtn');
      if (clearBtn) {{
        if (query.length > 0) {{
          clearBtn.classList.remove('hidden');
        }} else {{
          clearBtn.classList.add('hidden');
        }}
      }}
      applyFilters();
      renderSearchSuggestions(query);
    }}

    function handleSearchFocus(e) {{
      const query = document.getElementById('searchInput').value.trim();
      renderSearchSuggestions(query);
    }}

    function clearSearchInput() {{
      const input = document.getElementById('searchInput');
      if (input) {{
        input.value = '';
        input.focus();
      }}
      const clearBtn = document.getElementById('searchClearBtn');
      if (clearBtn) clearBtn.classList.add('hidden');
      hideSearchSuggestions();
      applyFilters();
    }}

    function hideSearchSuggestions() {{
      const menu = document.getElementById('searchSuggestionsMenu');
      if (menu) menu.classList.add('hidden');
      selectedSuggestionIndex = -1;
    }}

    let currentSuggestionTab = 'all';

    function setSuggestionTab(tabName, event) {{
      if (event) event.stopPropagation();
      currentSuggestionTab = tabName;
      const q = (document.getElementById('searchInput').value || '').trim();
      renderSearchSuggestions(q);
    }}

    function flyToCity(cityName, coords, sample) {{
      if (!map) return;
      const c = (cityName || '').toLowerCase();

      // Búsqueda en CCAA españolas
      if (c.includes('madrid')) {{ map.flyToBounds(CCAA_BOUNDS['madrid'], {{ padding: [40, 40], maxZoom: 10, duration: 1.2 }}); return; }}
      if (c.includes('barcelona') || c.includes('girona') || c.includes('lleida') || c.includes('tarragona') || c.includes('catalun')) {{ map.flyToBounds(CCAA_BOUNDS['catalunya'], {{ padding: [40, 40], maxZoom: 10, duration: 1.2 }}); return; }}
      if (c.includes('valencia') || c.includes('alicante') || c.includes('castellón') || c.includes('castellon') || c.includes('elche')) {{ map.flyToBounds(CCAA_BOUNDS['valencia'], {{ padding: [40, 40], maxZoom: 10, duration: 1.2 }}); return; }}
      if (c.includes('málaga') || c.includes('malaga') || c.includes('sevilla') || c.includes('granada') || c.includes('córdoba') || c.includes('cordoba') || c.includes('marbella') || c.includes('almería') || c.includes('cadiz') || c.includes('cádiz') || c.includes('jaen') || c.includes('jaén') || c.includes('huelva')) {{ map.flyToBounds(CCAA_BOUNDS['andalucia'], {{ padding: [40, 40], maxZoom: 10, duration: 1.2 }}); return; }}
      if (c.includes('bilbao') || c.includes('donostia') || c.includes('san sebastián') || c.includes('san sebastian') || c.includes('vitoria') || c.includes('bizkaia') || c.includes('vizcaya')) {{ map.flyToBounds(CCAA_BOUNDS['pais_vasco'], {{ padding: [40, 40], maxZoom: 10, duration: 1.2 }}); return; }}
      if (c.includes('vigo') || c.includes('coruña') || c.includes('pontevedra') || c.includes('ourense') || c.includes('lugo') || c.includes('galicia')) {{ map.flyToBounds(CCAA_BOUNDS['galicia'], {{ padding: [40, 40], maxZoom: 10, duration: 1.2 }}); return; }}
      if (c.includes('zaragoza') || c.includes('huesca') || c.includes('teruel') || c.includes('aragon')) {{ map.flyToBounds(CCAA_BOUNDS['aragon'], {{ padding: [40, 40], maxZoom: 10, duration: 1.2 }}); return; }}
      if (c.includes('palma') || c.includes('mallorca') || c.includes('ibiza') || c.includes('menorca') || c.includes('baleares')) {{ map.flyToBounds(CCAA_BOUNDS['baleares'], {{ padding: [40, 40], maxZoom: 10, duration: 1.2 }}); return; }}
      if (c.includes('canarias') || c.includes('tenerife') || c.includes('palmas')) {{ map.flyToBounds(CCAA_BOUNDS['canarias'], {{ padding: [40, 40], maxZoom: 10, duration: 1.2 }}); return; }}
      if (c.includes('murcia') || c.includes('cartagena')) {{ map.flyToBounds(CCAA_BOUNDS['murcia'], {{ padding: [40, 40], maxZoom: 10, duration: 1.2 }}); return; }}
      if (c.includes('asturias') || c.includes('gijón') || c.includes('gijon') || c.includes('oviedo')) {{ map.flyToBounds(CCAA_BOUNDS['asturias'], {{ padding: [40, 40], maxZoom: 10, duration: 1.2 }}); return; }}
      if (c.includes('cantabria') || c.includes('santander')) {{ map.flyToBounds(CCAA_BOUNDS['cantabria'], {{ padding: [40, 40], maxZoom: 10, duration: 1.2 }}); return; }}
      if (c.includes('pamplona') || c.includes('navarra')) {{ map.flyToBounds(CCAA_BOUNDS['navarra'], {{ padding: [40, 40], maxZoom: 10, duration: 1.2 }}); return; }}
      if (c.includes('valladolid') || c.includes('burgos') || c.includes('salamanca') || c.includes('león') || c.includes('leon')) {{ map.flyToBounds(CCAA_BOUNDS['castilla_leon'], {{ padding: [40, 40], maxZoom: 10, duration: 1.2 }}); return; }}
      if (c.includes('toledo') || c.includes('albacete') || c.includes('cuenca') || c.includes('ciudad real')) {{ map.flyToBounds(CCAA_BOUNDS['castilla_mancha'], {{ padding: [40, 40], maxZoom: 10, duration: 1.2 }}); return; }}
      if (c.includes('badajoz') || c.includes('cáceres') || c.includes('caceres') || c.includes('mérida') || c.includes('merida')) {{ map.flyToBounds(CCAA_BOUNDS['extremadura'], {{ padding: [40, 40], maxZoom: 10, duration: 1.2 }}); return; }}

      // Coordenadas directas
      if (coords && coords.length === 2) {{
        map.flyTo(coords, 12, {{ animate: true, duration: 1.2 }});
        return;
      }}

      if (sample && sample.coords) {{
        zoomToClubRegion(sample, sample.id);
      }}
    }}

    function renderSearchSuggestions(query) {{
      const menu = document.getElementById('searchSuggestionsMenu');
      if (!menu) return;

      const q = (query || '').toLowerCase().trim();

      if (!q) {{
        currentSuggestionTab = 'all';
        // Si está vacío al hacer foco: mostrar muestra rápida de las 4 categorías
        const destacadas = FRANQUICIAS.filter(f => f.destacado || (f.clubs_abiertos && f.clubs_abiertos >= 15)).slice(0, 3);
        const subClubSample = [];
        FRANQUICIAS.forEach(f => {{
          if (f.sub_clubs && f.sub_clubs.length > 0 && subClubSample.length < 2) {{
            f.sub_clubs.slice(0, 1).forEach(s => {{
              subClubSample.push({{ parent: f, sub: s }});
            }});
          }}
        }});

        let html = `
          <div class="px-3.5 py-1.5 text-[10px] font-black uppercase tracking-wider text-slate-400 bg-slate-50 border-b border-slate-100 flex items-center justify-between">
            <span>Explorar por Cadenas, Clubs, Países o Ciudades</span>
            <span class="text-slate-400 font-semibold text-[9px]">Sugerencias</span>
          </div>
        `;

        let sampleList = [];
        destacadas.forEach(f => {{
          sampleList.push({{
            type: 'cadena',
            title: f.nombre,
            searchQuery: f.nombre,
            subtitle: `${{f.ciudad_sede ? f.ciudad_sede + ' · ' : ''}}${{f.pais}} (${{f.clubs_abiertos || 1}} clubs)`,
            icon: '🏢',
            badge: 'CADENA',
            badgeClass: 'bg-sky-100 text-sky-800',
            entity: f
          }});
        }});

        subClubSample.forEach(sc => {{
          sampleList.push({{
            type: 'club',
            title: sc.sub.nombre,
            searchQuery: sc.sub.nombre,
            subtitle: `Red ${{sc.parent.nombre}} · ${{sc.sub.ciudad || ''}} (${{sc.sub.pistas || 'Pistas'}})`,
            icon: '🎾',
            badge: 'CLUB',
            badgeClass: 'bg-emerald-100 text-emerald-800',
            coords: sc.sub.coords,
            parent: sc.parent,
            sub: sc.sub
          }});
        }});

        sampleList.push({{
          type: 'pais',
          name: 'España',
          title: 'España 🇪🇸',
          searchQuery: 'España',
          subtitle: 'Más de 115 cadenas y redes activas',
          icon: '🌍',
          badge: 'PAÍS',
          badgeClass: 'bg-purple-100 text-purple-800',
          code: 'ES',
          flag: '🇪🇸'
        }});

        sampleList.push({{
          type: 'ciudad',
          name: 'Madrid',
          title: 'Madrid',
          searchQuery: 'Madrid',
          subtitle: 'Comunidad de Madrid · Mayor concentración de pistas',
          icon: '📍',
          badge: 'CIUDAD',
          badgeClass: 'bg-amber-100 text-amber-900',
          coords: [40.4168, -3.7038]
        }});

        sampleList.forEach((item, idx) => {{
          html += `
            <div class="search-suggestion-item flex items-center justify-between px-3.5 py-2.5 hover:bg-amber-50 cursor-pointer transition border-b border-slate-50 last:border-0"
                 onclick="executeSearchSuggestion(${{idx}})"
                 data-index="${{idx}}">
              <div class="flex items-center gap-2.5 min-w-0">
                <span class="w-7 h-7 rounded-xl bg-slate-100 border border-slate-200 flex items-center justify-center text-xs shrink-0">${{item.icon}}</span>
                <div class="truncate">
                  <div class="text-xs font-bold text-slate-900 truncate flex items-center gap-1.5">
                    <span>${{item.title}}</span>
                    <span class="text-[9px] px-1.5 py-0.2 rounded font-extrabold uppercase ${{item.badgeClass}}">${{item.badge}}</span>
                  </div>
                  <div class="text-[10px] text-slate-500 font-medium truncate">${{item.subtitle}}</div>
                </div>
              </div>
              <span class="text-[11px] font-bold text-amber-600 shrink-0 ml-2">Ver →</span>
            </div>
          `;
        }});

        currentRenderedSuggestions = sampleList;
        menu.innerHTML = html;
        menu.classList.remove('hidden');
        return;
      }}

      // =======================================================================
      // 1. COINCIDENCIAS EN CADENAS (🏢)
      // =======================================================================
      const cadenas = [];
      FRANQUICIAS.forEach(f => {{
        if ((f.nombre && f.nombre.toLowerCase().includes(q)) || 
            (f.tagline && f.tagline.toLowerCase().includes(q)) ||
            (f.software && f.software.toLowerCase().includes(q))) {{
          cadenas.push({{
            type: 'cadena',
            id: f.id,
            title: f.nombre,
            searchQuery: f.nombre,
            subtitle: `${{f.ciudad_sede ? f.ciudad_sede + ' · ' : ''}}${{f.pais}} · ${{f.clubs_abiertos || 1}} clubs · ${{f.pistas_totales || ''}} pistas`,
            icon: '🏢',
            badge: (f.tipo_categoria || 'CADENA').toUpperCase(),
            badgeClass: 'bg-sky-100 text-sky-800',
            entity: f
          }});
        }}
      }});

      // =======================================================================
      // 2. COINCIDENCIAS EN CLUBS Y SEDES (🎾)
      // =======================================================================
      const clubs = [];
      const seenClubs = new Set();
      
      // A) Sub-clubs estructurados con coordenadas
      FRANQUICIAS.forEach(f => {{
        if (f.sub_clubs && f.sub_clubs.length > 0) {{
          f.sub_clubs.forEach(sub => {{
            const nameMatch = sub.nombre && sub.nombre.toLowerCase().includes(q);
            const cityMatch = sub.ciudad && sub.ciudad.toLowerCase().includes(q);
            if (nameMatch || cityMatch) {{
              const key = (sub.nombre || '').toLowerCase();
              if (!seenClubs.has(key)) {{
                seenClubs.add(key);
                clubs.push({{
                  type: 'club',
                  title: sub.nombre,
                  searchQuery: sub.nombre,
                  subtitle: `Red ${{f.nombre}} · ${{sub.ciudad || ''}} (${{sub.pistas || 'Pistas'}})`,
                  icon: '🎾',
                  badge: 'CLUB',
                  badgeClass: 'bg-emerald-100 text-emerald-800',
                  coords: sub.coords,
                  parent: f,
                  sub: sub
                }});
              }}
            }}
          }});
        }}
      }});

      // B) Sedes principales detalladas
      FRANQUICIAS.forEach(f => {{
        if (f.sedes_principales && f.sedes_principales.length > 0) {{
          f.sedes_principales.forEach(sedeStr => {{
            if (sedeStr.toLowerCase().includes(q)) {{
              const cleanTitle = sedeStr.split('(')[0].trim();
              const key = cleanTitle.toLowerCase();
              if (!seenClubs.has(key) && cleanTitle.length > 3) {{
                seenClubs.add(key);
                clubs.push({{
                  type: 'club',
                  title: cleanTitle,
                  searchQuery: cleanTitle,
                  subtitle: `Red ${{f.nombre}} · ${{f.ciudad_sede || f.pais}}`,
                  icon: '🎾',
                  badge: 'SEDE',
                  badgeClass: 'bg-emerald-100 text-emerald-800',
                  coords: f.coords,
                  parent: f,
                  sub: null
                }});
              }}
            }}
          }});
        }}
      }});

      // =======================================================================
      // 3. COINCIDENCIAS EN PAÍSES (🌍)
      // =======================================================================
      const paisesMap = new Map();
      FRANQUICIAS.forEach(f => {{
        const pName = f.pais || '';
        const pCode = (f.pais_codigo || '').toLowerCase();
        if (pName.toLowerCase().includes(q) || pCode === q) {{
          const key = pName.toLowerCase();
          if (!paisesMap.has(key)) {{
            paisesMap.set(key, {{
              type: 'pais',
              name: pName,
              code: f.region_filtro || f.pais_codigo,
              flag: f.bandera || '🌍',
              title: `${{pName}} ${{f.bandera || ''}}`.trim(),
              searchQuery: pName,
              count: 1,
              sample: f
            }});
          }} else {{
            paisesMap.get(key).count++;
          }}
        }}
      }});

      const paises = Array.from(paisesMap.values()).map(p => ({{
        ...p,
        subtitle: `${{p.count}} ${{p.count === 1 ? 'cadena con presencia' : 'cadenas y franquicias con presencia'}}`,
        icon: '🌍',
        badge: 'PAÍS',
        badgeClass: 'bg-purple-100 text-purple-800'
      }}));

      // =======================================================================
      // 4. COINCIDENCIAS EN CIUDADES (📍)
      // =======================================================================
      const ciudadesMap = new Map();
      FRANQUICIAS.forEach(f => {{
        if (f.ciudad_sede && f.ciudad_sede.toLowerCase().includes(q)) {{
          const rawCities = f.ciudad_sede.split(/[\\/,]/).map(c => c.trim()).filter(Boolean);
          rawCities.forEach(cName => {{
            if (cName.toLowerCase().includes(q)) {{
              const key = cName.toLowerCase();
              if (!ciudadesMap.has(key)) {{
                ciudadesMap.set(key, {{
                  type: 'ciudad',
                  name: cName,
                  title: cName,
                  searchQuery: cName,
                  country: f.pais,
                  count: 1,
                  coords: f.coords,
                  sample: f
                }});
              }} else {{
                ciudadesMap.get(key).count++;
              }}
            }}
          }});
        }}

        if (f.sub_clubs) {{
          f.sub_clubs.forEach(sub => {{
            if (sub.ciudad && sub.ciudad.toLowerCase().includes(q)) {{
              const key = sub.ciudad.toLowerCase();
              if (!ciudadesMap.has(key)) {{
                ciudadesMap.set(key, {{
                  type: 'ciudad',
                  name: sub.ciudad,
                  title: sub.ciudad,
                  searchQuery: sub.ciudad,
                  country: f.pais,
                  count: 1,
                  coords: sub.coords,
                  sample: f
                }});
              }} else {{
                ciudadesMap.get(key).count++;
              }}
            }}
          }});
        }}
      }});

      const ciudades = Array.from(ciudadesMap.values()).map(c => ({{
        ...c,
        subtitle: `${{c.country}} · ${{c.count}} ${{c.count === 1 ? 'red/club vinculado' : 'redes/clubs vinculados'}}`,
        icon: '📍',
        badge: 'CIUDAD',
        badgeClass: 'bg-amber-100 text-amber-900'
      }}));

      const totalMatches = cadenas.length + clubs.length + paises.length + ciudades.length;

      if (totalMatches === 0) {{
        menu.innerHTML = `
          <div class="px-4 py-4 text-center">
            <div class="text-sm font-bold text-slate-700 mb-1">No se encontraron resultados para "${{escapeHtml(query)}}"</div>
            <div class="text-xs text-slate-500">Prueba a buscar por <span class="font-bold text-slate-700">cadena</span> (ej: BamVolea), <span class="font-bold text-slate-700">club</span> (ej: Las Rozas), <span class="font-bold text-slate-700">país</span> (ej: España) o <span class="font-bold text-slate-700">ciudad</span> (ej: Madrid).</div>
          </div>
        `;
        menu.classList.remove('hidden');
        currentRenderedSuggestions = [];
        return;
      }}

      // Si la pestaña activa no tiene resultados, volver a 'all'
      if (currentSuggestionTab === 'cadenas' && cadenas.length === 0) currentSuggestionTab = 'all';
      if (currentSuggestionTab === 'clubs' && clubs.length === 0) currentSuggestionTab = 'all';
      if (currentSuggestionTab === 'paises' && paises.length === 0) currentSuggestionTab = 'all';
      if (currentSuggestionTab === 'ciudades' && ciudades.length === 0) currentSuggestionTab = 'all';

      // =======================================================================
      // RENDERIZAR TABS DE CATEGORÍA
      // =======================================================================
      let html = `
        <div class="flex items-center gap-1.5 px-3 py-2 bg-slate-50 border-b border-slate-100 overflow-x-auto text-[10px] font-extrabold">
          <button type="button" onclick="setSuggestionTab('all', event)" class="px-2.5 py-1 rounded-lg shrink-0 transition ${{currentSuggestionTab === 'all' ? 'bg-slate-900 text-white shadow-xs' : 'bg-white text-slate-600 border border-slate-200 hover:bg-slate-100'}}">
            Todos (${{totalMatches}})
          </button>
          ${{cadenas.length > 0 ? `
            <button type="button" onclick="setSuggestionTab('cadenas', event)" class="px-2 py-1 rounded-lg shrink-0 transition flex items-center gap-1 ${{currentSuggestionTab === 'cadenas' ? 'bg-[#f2920b] text-slate-950 font-black shadow-xs' : 'bg-white text-slate-600 border border-slate-200 hover:bg-slate-100'}}">
              <span>🏢 Cadenas</span>
              <span class="text-[9px] opacity-80">(${{cadenas.length}})</span>
            </button>
          ` : ''}}
          ${{clubs.length > 0 ? `
            <button type="button" onclick="setSuggestionTab('clubs', event)" class="px-2 py-1 rounded-lg shrink-0 transition flex items-center gap-1 ${{currentSuggestionTab === 'clubs' ? 'bg-[#f2920b] text-slate-950 font-black shadow-xs' : 'bg-white text-slate-600 border border-slate-200 hover:bg-slate-100'}}">
              <span>🎾 Clubs</span>
              <span class="text-[9px] opacity-80">(${{clubs.length}})</span>
            </button>
          ` : ''}}
          ${{paises.length > 0 ? `
            <button type="button" onclick="setSuggestionTab('paises', event)" class="px-2 py-1 rounded-lg shrink-0 transition flex items-center gap-1 ${{currentSuggestionTab === 'paises' ? 'bg-[#f2920b] text-slate-950 font-black shadow-xs' : 'bg-white text-slate-600 border border-slate-200 hover:bg-slate-100'}}">
              <span>🌍 Países</span>
              <span class="text-[9px] opacity-80">(${{paises.length}})</span>
            </button>
          ` : ''}}
          ${{ciudades.length > 0 ? `
            <button type="button" onclick="setSuggestionTab('ciudades', event)" class="px-2 py-1 rounded-lg shrink-0 transition flex items-center gap-1 ${{currentSuggestionTab === 'ciudades' ? 'bg-[#f2920b] text-slate-950 font-black shadow-xs' : 'bg-white text-slate-600 border border-slate-200 hover:bg-slate-100'}}">
              <span>📍 Ciudades</span>
              <span class="text-[9px] opacity-80">(${{ciudades.length}})</span>
            </button>
          ` : ''}}
        </div>
      `;

      let itemsToRender = [];

      if (currentSuggestionTab === 'all') {{
        // Vista agrupada 'Todos': muestra hasta 3 de cada categoría con encabezados claros
        const sections = [
          {{ key: 'cadenas', title: '🏢 Cadenas y Franquicias', list: cadenas.slice(0, 3) }},
          {{ key: 'clubs', title: '🎾 Clubs y Sedes', list: clubs.slice(0, 3) }},
          {{ key: 'paises', title: '🌍 Países y Mercados', list: paises.slice(0, 2) }},
          {{ key: 'ciudades', title: '📍 Ciudades', list: ciudades.slice(0, 3) }}
        ];

        let globalIndex = 0;
        sections.forEach(sec => {{
          if (sec.list.length > 0) {{
            html += `
              <div class="px-3.5 py-1 text-[9px] font-black uppercase tracking-wider text-slate-400 bg-slate-100/60 border-b border-slate-100 flex items-center justify-between">
                <span>${{sec.title}}</span>
                <span class="text-[9px] font-bold text-slate-400">${{sec.list.length}} sugerencias</span>
              </div>
            `;
            sec.list.forEach(item => {{
              const currentIdx = globalIndex++;
              itemsToRender.push(item);
              const highlightedTitle = highlightMatch(item.title, q);
              html += `
                <div class="search-suggestion-item flex items-center justify-between px-3.5 py-2.5 hover:bg-amber-50 cursor-pointer transition border-b border-slate-50 last:border-0"
                     data-index="${{currentIdx}}"
                     onclick="executeSearchSuggestion(${{currentIdx}})">
                  <div class="flex items-center gap-2.5 min-w-0">
                    <span class="w-7 h-7 rounded-xl bg-slate-100 border border-slate-200 flex items-center justify-center text-xs shrink-0">${{item.icon}}</span>
                    <div class="truncate">
                      <div class="text-xs font-bold text-slate-900 truncate flex items-center gap-1.5">
                        <span>${{highlightedTitle}}</span>
                        <span class="text-[8px] px-1.5 py-0.2 rounded font-extrabold uppercase ${{item.badgeClass}}">${{item.badge}}</span>
                      </div>
                      <div class="text-[10px] text-slate-500 font-medium truncate">${{item.subtitle}}</div>
                    </div>
                  </div>
                  <span class="text-[10px] font-extrabold text-[#f2920b] shrink-0 ml-2">Seleccionar →</span>
                </div>
              `;
            }});
          }}
        }});
      }} else {{
        // Vista filtrada por una categoría específica
        let sourceList = [];
        if (currentSuggestionTab === 'cadenas') sourceList = cadenas;
        else if (currentSuggestionTab === 'clubs') sourceList = clubs;
        else if (currentSuggestionTab === 'paises') sourceList = paises;
        else if (currentSuggestionTab === 'ciudades') sourceList = ciudades;

        itemsToRender = sourceList.slice(0, 10);
        itemsToRender.forEach((item, idx) => {{
          const highlightedTitle = highlightMatch(item.title, q);
          html += `
            <div class="search-suggestion-item flex items-center justify-between px-3.5 py-2.5 hover:bg-amber-50 cursor-pointer transition border-b border-slate-50 last:border-0"
                 data-index="${{idx}}"
                 onclick="executeSearchSuggestion(${{idx}})">
              <div class="flex items-center gap-2.5 min-w-0">
                <span class="w-7 h-7 rounded-xl bg-slate-100 border border-slate-200 flex items-center justify-center text-xs shrink-0">${{item.icon}}</span>
                <div class="truncate">
                  <div class="text-xs font-bold text-slate-900 truncate flex items-center gap-1.5">
                    <span>${{highlightedTitle}}</span>
                    <span class="text-[8px] px-1.5 py-0.2 rounded font-extrabold uppercase ${{item.badgeClass}}">${{item.badge}}</span>
                  </div>
                  <div class="text-[10px] text-slate-500 font-medium truncate">${{item.subtitle}}</div>
                </div>
              </div>
              <span class="text-[10px] font-extrabold text-[#f2920b] shrink-0 ml-2">Seleccionar →</span>
            </div>
          `;
        }});
      }}

      currentRenderedSuggestions = itemsToRender;
      menu.innerHTML = html;
      menu.classList.remove('hidden');
      selectedSuggestionIndex = -1;
    }}

    function executeSearchSuggestion(index) {{
      if (!currentRenderedSuggestions || !currentRenderedSuggestions[index]) return;
      const item = currentRenderedSuggestions[index];
      const searchInput = document.getElementById('searchInput');

      if (searchInput) {{
        searchInput.value = item.searchQuery || item.title;
      }}
      hideSearchSuggestions();
      applyFilters();

      const clearBtn = document.getElementById('searchClearBtn');
      if (clearBtn) clearBtn.classList.remove('hidden');

      if (item.type === 'cadena') {{
        const f = item.entity || FRANQUICIAS.find(x => x.id === item.id);
        if (f) {{
          zoomToClubRegion(f, f.id);
          if (f.sub_clubs && f.sub_clubs.length > 0) {{
            deploySubClubs(f);
          }}
          setTimeout(() => {{
            if (markersById[f.id]) {{
              markersById[f.id].openPopup();
            }}
          }}, 500);
        }}
      }} else if (item.type === 'club') {{
        if (item.parent) {{
          deploySubClubs(item.parent);
          if (item.coords && map) {{
            map.flyTo(item.coords, 14, {{ animate: true, duration: 1.2 }});
          }} else if (item.parent.coords && map) {{
            map.flyTo(item.parent.coords, 13, {{ animate: true, duration: 1.2 }});
          }}
        }}
      }} else if (item.type === 'pais') {{
        if (item.code && REGION_BOUNDS[item.code]) {{
          selectRegion(item.code, item.name, item.flag || '🌍');
        }} else {{
          applyFilters();
          if (item.sample) {{
            zoomToClubRegion(item.sample, item.sample.id);
          }}
        }}
      }} else if (item.type === 'ciudad') {{
        flyToCity(item.name, item.coords, item.sample);
        applyFilters();
      }}
    }}

    function handleSearchKeyDown(e) {{
      const menu = document.getElementById('searchSuggestionsMenu');
      if (!menu || menu.classList.contains('hidden')) {{
        if (e.key === 'Enter') {{
          applyFilters();
        }}
        return;
      }}

      const items = menu.querySelectorAll('.search-suggestion-item');
      if (items.length === 0) return;

      if (e.key === 'ArrowDown') {{
        e.preventDefault();
        selectedSuggestionIndex = (selectedSuggestionIndex + 1) % items.length;
        updateActiveSuggestion(items);
      }} else if (e.key === 'ArrowUp') {{
        e.preventDefault();
        selectedSuggestionIndex = (selectedSuggestionIndex - 1 + items.length) % items.length;
        updateActiveSuggestion(items);
      }} else if (e.key === 'Enter') {{
        e.preventDefault();
        if (selectedSuggestionIndex >= 0 && selectedSuggestionIndex < items.length) {{
          executeSearchSuggestion(selectedSuggestionIndex);
        }} else if (items.length > 0) {{
          executeSearchSuggestion(0);
        }}
      }} else if (e.key === 'Escape') {{
        hideSearchSuggestions();
      }}
    }}

    function updateActiveSuggestion(items) {{
      items.forEach((item, idx) => {{
        if (idx === selectedSuggestionIndex) {{
          item.classList.add('bg-amber-100/70', 'ring-1', 'ring-amber-400');
          item.scrollIntoView({{ block: 'nearest' }});
        }} else {{
          item.classList.remove('bg-amber-100/70', 'ring-1', 'ring-amber-400');
        }}
      }});
    }}

    function highlightMatch(text, query) {{
      if (!query) return text;
      const idx = text.toLowerCase().indexOf(query.toLowerCase());
      if (idx === -1) return text;
      const before = text.substring(0, idx);
      const match = text.substring(idx, idx + query.length);
      const after = text.substring(idx + query.length);
      return `${{before}}<span class="bg-amber-100 text-amber-900 font-extrabold rounded-xs px-0.5">${{match}}</span>${{after}}`;
    }}

    function escapeHtml(str) {{
      if (!str) return '';
      return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    }}

    function selectRegion(code, label, flag) {{
      currentRegion = code;
      const lbl = document.getElementById('current-region-label');
      const flg = document.getElementById('current-region-flag');
      if (lbl) lbl.textContent = label;
      if (flg) flg.textContent = flag;
      
      const menu = document.getElementById('region-dropdown-menu');
      const arrow = document.getElementById('region-dropdown-arrow');
      if (menu) menu.classList.add('hidden');
      if (arrow) arrow.classList.remove('rotate-180');

      clearSubClubs();
      applyFilters();

      // Animación fluida con encuadre calibrado del país completo y sus extremos
      if (map && REGION_BOUNDS[code]) {{
        map.invalidateSize();
        map.flyToBounds(REGION_BOUNDS[code], {{
          padding: [40, 40],
          maxZoom: 5.5,
          duration: 1.2
        }});
      }}
    }}

    function setModelFilter(model) {{
      currentModel = model;
      document.querySelectorAll('.filter-model-btn').forEach(btn => {{
        if (btn.dataset.model === model) {{
          btn.classList.add('bg-slate-900', 'text-white');
          btn.classList.remove('bg-slate-100', 'text-slate-600');
        }} else {{
          btn.classList.remove('bg-slate-900', 'text-white');
          btn.classList.add('bg-slate-100', 'text-slate-600');
        }}
      }});
      applyFilters();
    }}

    function setBudgetFilter(budget) {{
      currentBudget = budget;
      applyFilters();
    }}

    function setFacilityFilter(facility) {{
      currentFacility = facility;
      applyFilters();
    }}

    function applyFilters() {{
      registerUserInteraction();
      const query = document.getElementById('searchInput').value.toLowerCase().trim();
      const cards = document.querySelectorAll('.franchise-card');
      const tableRows = document.querySelectorAll('#tableView tbody tr');
      
      let visibleCount = 0;
      let filteredData = [];

      FRANQUICIAS.forEach((f, idx) => {{
        const regionCode = f.region_filtro || f.pais_codigo;
        const matchRegion = (currentRegion === 'all' || regionCode === currentRegion);
        const matchModel = (currentModel === 'all' || f.tipo_categoria === currentModel);
        
        const cardElem = cards[idx];
        const cardBudget = cardElem ? cardElem.dataset.budget : 'mid';
        const cardFacility = cardElem ? cardElem.dataset.facility : 'indoor';

        const matchBudget = (currentBudget === 'all' || cardBudget === currentBudget);
        const matchFacility = (currentFacility === 'all' || cardFacility === currentFacility);

        const subClubsText = (f.sub_clubs || []).map(s => `${{s.nombre || ''}} ${{s.ciudad || ''}}`).join(' ');
        const sedesText = (f.sedes_principales || []).join(' ');
        const textToSearch = `${{f.nombre}} ${{f.pais}} ${{f.pais_codigo || ''}} ${{f.ciudad_sede || ''}} ${{f.tagline || ''}} ${{f.modelo || ''}} ${{subClubsText}} ${{sedesText}}`.toLowerCase();
        const matchQuery = !query || textToSearch.includes(query);

        const isVisible = matchRegion && matchModel && matchBudget && matchFacility && matchQuery;

        if (cards[idx]) {{
          cards[idx].style.display = isVisible ? 'flex' : 'none';
        }}
        if (tableRows[idx]) {{
          tableRows[idx].style.display = isVisible ? '' : 'none';
        }}

        if (isVisible) {{
          visibleCount++;
          filteredData.push(f);
        }}
      }});

      document.getElementById('resultsCount').textContent = `Mostrando ${{visibleCount}} de ${{FRANQUICIAS.length}} cadenas y franquicias`;
      renderMarkers(filteredData);
    }}

    function switchView(view) {{
      currentView = view;
      const gridView = document.getElementById('gridView');
      const tableView = document.getElementById('tableView');
      const mapArea = document.getElementById('mapArea');
      const viewGridBtn = document.getElementById('viewGridBtn');
      const viewTableBtn = document.getElementById('viewTableBtn');

      if (view === 'grid') {{
        gridView.classList.remove('hidden');
        tableView.classList.add('hidden');
        if (mapArea) mapArea.classList.remove('hidden');
        
        viewGridBtn.className = "px-3.5 py-2 rounded-xl text-xs font-bold font-heading uppercase tracking-wider bg-slate-900 text-white transition flex items-center gap-1.5 shadow-xs";
        viewTableBtn.className = "px-3.5 py-2 rounded-xl text-xs font-bold font-heading uppercase tracking-wider bg-slate-100 text-slate-700 hover:bg-slate-200 transition flex items-center gap-1.5";
        
        setTimeout(() => {{ if (map) map.invalidateSize(); }}, 100);
      }} else {{
        gridView.classList.add('hidden');
        tableView.classList.remove('hidden');
        if (mapArea) mapArea.classList.add('hidden');

        viewGridBtn.className = "px-3.5 py-2 rounded-xl text-xs font-bold font-heading uppercase tracking-wider bg-slate-100 text-slate-700 hover:bg-slate-200 transition flex items-center gap-1.5";
        viewTableBtn.className = "px-3.5 py-2 rounded-xl text-xs font-bold font-heading uppercase tracking-wider bg-slate-900 text-white transition flex items-center gap-1.5 shadow-xs";
      }}
    }}

    // =========================================================================
    // COMPARADOR CARA A CARA (SIDE-BY-SIDE MATRIX)
    // =========================================================================
    function toggleCompare(id) {{
      const index = selectedFranchises.indexOf(id);
      if (index > -1) {{
        selectedFranchises.splice(index, 1);
      }} else {{
        if (selectedFranchises.length >= 3) {{
          alert("Puedes comparar un máximo de 3 franquicias a la vez. Desmarca una de las seleccionadas para añadir otra.");
          return;
        }}
        selectedFranchises.push(id);
      }}
      updateCompareUI();
    }}

    function updateCompareUI() {{
      // Actualizar botones de tarjetas
      document.querySelectorAll('.compare-card-btn').forEach(btn => {{
        const btnId = btn.id.replace('compare-btn-', '').replace('table-compare-btn-', '');
        const isSelected = selectedFranchises.includes(btnId);
        const label = btn.querySelector('.compare-label');
        
        if (isSelected) {{
          btn.classList.add('bg-slate-900', 'text-white', 'border-slate-900');
          btn.classList.remove('bg-white', 'text-slate-600', 'border-slate-200');
          if (label) label.textContent = '✓ Seleccionada';
        }} else {{
          btn.classList.remove('bg-slate-900', 'text-white', 'border-slate-900');
          btn.classList.add('bg-white', 'text-slate-600', 'border-slate-200');
          if (label) label.textContent = 'Comparar';
        }}
      }});

      // Actualizar Barra Flotante
      const bar = document.getElementById('compareFloatingBar');
      const countPill = document.getElementById('compareCountPill');
      const chipsContainer = document.getElementById('compareChips');

      if (selectedFranchises.length > 0) {{
        countPill.textContent = `${{selectedFranchises.length}} / 3`;
        chipsContainer.innerHTML = selectedFranchises.map(fid => {{
          const f = FRANQUICIAS.find(x => x.id === fid);
          if (!f) return '';
          return `
            <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-slate-800 text-slate-200 text-xs font-bold border border-slate-700">
              <span>${{f.bandera}}</span>
              <span class="max-w-[120px] truncate">${{f.nombre}}</span>
              <button onclick="toggleCompare('${{f.id}}')" class="text-slate-400 hover:text-white font-black ml-1">&times;</button>
            </div>
          `;
        }}).join('');

        bar.classList.remove('opacity-0', 'pointer-events-none', 'translate-y-32');
        bar.classList.add('opacity-100', 'pointer-events-auto', 'translate-y-0');
      }} else {{
        bar.classList.add('opacity-0', 'pointer-events-none', 'translate-y-32');
        bar.classList.remove('opacity-100', 'pointer-events-auto', 'translate-y-0');
      }}
      lucide.createIcons();
    }}

    function clearCompare() {{
      selectedFranchises = [];
      updateCompareUI();
    }}

    function focusComparatorTip() {{
      const filtros = document.getElementById('filtrosContainer');
      filtros.scrollIntoView({{ behavior: 'smooth' }});
    }}

    function openCompareModal() {{
      if (selectedFranchises.length === 0) return;
      const items = selectedFranchises.map(fid => FRANQUICIAS.find(x => x.id === fid)).filter(Boolean);

      const modalContent = document.getElementById('compareModalContent');
      
      const gridCols = items.length === 1 ? 'grid-cols-1' : (items.length === 2 ? 'grid-cols-1 md:grid-cols-2' : 'grid-cols-1 md:grid-cols-3');

      modalContent.innerHTML = `
        <div class="grid ${{gridCols}} gap-6">
          ${{items.map(f => `
            <div class="bg-slate-50 rounded-3xl p-6 border border-slate-200 flex flex-col justify-between space-y-6">
              
              <!-- Cabecera Franquicia -->
              <div>
                <div class="flex items-center justify-between gap-2 mb-3">
                  <span class="inline-block px-3 py-1 rounded-full text-xs font-bold border ${{f.modelo_badge}}">
                    ${{f.modelo}}
                  </span>
                  <span class="text-2xl">${{f.bandera}}</span>
                </div>
                <h3 class="font-heading font-black text-2xl text-slate-950 mb-1">${{f.nombre}}</h3>
                <p class="text-xs font-semibold text-slate-500 mb-3 flex items-center gap-1">
                  <i data-lucide="map-pin" class="w-3.5 h-3.5 text-slate-400"></i>
                  <span>${{f.ciudad_sede}}, ${{f.pais}}</span>
                </p>
                <p class="text-xs text-slate-600 italic bg-white p-3 rounded-xl border border-slate-200">
                  "${{f.tagline}}"
                </p>
              </div>

              <!-- Bloque 1: Cánones Económicos y Retorno -->
              <div class="p-4 bg-white rounded-2xl border border-slate-200 space-y-2.5 text-xs">
                <span class="font-heading font-black text-xs uppercase text-slate-900 block border-b pb-1.5 flex items-center gap-1.5">
                  <i data-lucide="coins" class="w-4 h-4 text-[#f2920b]"></i> Cánones & Inversión
                </span>
                <div><strong class="text-slate-500">Inversión Estimada:</strong> <span class="font-bold text-slate-900">${{f.modelo_expansion.inversion_media}}</span></div>
                <div><strong class="text-slate-500">Canon & Royalties:</strong> <span class="font-bold text-slate-900">${{f.modelo_expansion.canon_royalties}}</span></div>
                <div><strong class="text-slate-500">Tipo de Contrato:</strong> <span class="text-slate-800">${{f.modelo_expansion.tipo_contrato}}</span></div>
                <div><strong class="text-slate-500">Perfil Idóneo:</strong> <span class="text-slate-800">${{f.modelo_expansion.perfil_club}}</span></div>
              </div>

              <!-- Bloque 2: Requisitos de Instalación -->
              <div class="p-4 bg-white rounded-2xl border border-slate-200 space-y-2.5 text-xs">
                <span class="font-heading font-black text-xs uppercase text-slate-900 block border-b pb-1.5 flex items-center gap-1.5">
                  <i data-lucide="warehouse" class="w-4 h-4 text-[#f2920b]"></i> Instalación & Pistas
                </span>
                <div><strong class="text-slate-500">Pistas y Cubierta:</strong> <span class="text-slate-800">${{f.tecnologia_pistas.pistas}}</span></div>
                <div><strong class="text-slate-500">Software de Reservas:</strong> <span class="font-bold text-slate-900">${{f.software}}</span></div>
                <div><strong class="text-slate-500">Domótica y Acceso:</strong> <span class="text-slate-800">${{f.tecnologia_pistas.domotica}}</span></div>
                <div><strong class="text-slate-500">Grabación en Pista:</strong> <span class="text-slate-800">${{f.tecnologia_pistas.grabacion}}</span></div>
                <div><strong class="text-slate-500">Restauración:</strong> <span class="text-slate-800">${{f.tecnologia_pistas.restauracion}}</span></div>
              </div>

              <!-- Bloque 3: Diferencial -->
              <div class="p-4 bg-amber-50/70 rounded-2xl border border-amber-200 text-xs space-y-1">
                <span class="font-heading font-black text-[11px] uppercase text-amber-900 block">Ventaja Competitiva</span>
                <p class="text-amber-950 leading-relaxed font-medium">${{f.diferencial}}</p>
              </div>

              <!-- Acciones de Conversión -->
              <div class="pt-2 space-y-2">
                <a href="https://wa.me/34680317486?text=Hola%20Javier%2C%20estoy%20usando%20el%20comparador%20y%20quiero%20el%20dossier%20completo%20de%20inversi%C3%B3n%20de%20${{encodeURIComponent(f.nombre)}}" target="_blank"
                   class="w-full py-3 rounded-xl bg-[#f2920b] hover:bg-[#d97f08] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition text-center flex items-center justify-center gap-1.5 shadow-xs" rel="noopener noreferrer">
                  <i data-lucide="file-text" class="w-4 h-4"></i>
                  <span>Solicitar Dossier de Inversión</span>
                </a>
                <a href="${{f.web}}" target="_blank" class="w-full py-2.5 rounded-xl bg-white border border-slate-300 hover:bg-slate-100 text-slate-700 font-bold text-xs transition text-center flex items-center justify-center gap-1" rel="noopener noreferrer">
                  <span>Web Oficial</span>
                  <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
                </a>
              </div>

            </div>
          `).join('')}}
        </div>
      `;

      document.getElementById('compareModalOverlay').classList.remove('opacity-0', 'pointer-events-none');
      document.getElementById('compareModal').classList.remove('scale-95');
      document.body.classList.add('drawer-open');
      lucide.createIcons();
    }}

    function closeCompareModal() {{
      document.getElementById('compareModalOverlay').classList.add('opacity-0', 'pointer-events-none');
      document.getElementById('compareModal').classList.add('scale-95');
      document.body.classList.remove('drawer-open');
    }}

    // =========================================================================
    // ONBOARDING / RECLAMAR FICHA (WIZARD 4 PASOS)
    // =========================================================================
    function openOnboardingModal(prefillId = null) {{
      const form = document.getElementById('onboardingForm');
      form.reset();
      
      const successBox = document.getElementById('onboardingSuccess');
      const navBtns = document.getElementById('onboardingNavBtns');
      successBox.classList.add('hidden');
      navBtns.classList.remove('hidden');

      if (prefillId) {{
        const f = FRANQUICIAS.find(x => x.id === prefillId);
        if (f) {{
          document.getElementById('onboardingModalTitle').textContent = `Reclamar Ficha: ${{f.nombre}}`;
          document.getElementById('ob_nombre').value = f.nombre;
          document.getElementById('ob_web').value = f.web;
          document.getElementById('ob_sede').value = `${{f.ciudad_sede}}, ${{f.pais}}`;
          document.getElementById('ob_num_clubs').value = parseInt(f.num_clubs) || 2;
          document.getElementById('ob_software').value = f.software;
          document.getElementById('ob_inversion_media').value = f.modelo_expansion.inversion_media;
          document.getElementById('ob_canon_entrada').value = f.modelo_expansion.canon_royalties;
        }}
      }} else {{
        document.getElementById('onboardingModalTitle').textContent = "Alta / Reclamar Ficha de Franquicia";
      }}

      goToStep(1);

      document.getElementById('onboardingModalOverlay').classList.remove('opacity-0', 'pointer-events-none');
      document.getElementById('onboardingModal').classList.remove('scale-95');
      document.body.classList.add('drawer-open');
      lucide.createIcons();
    }}

    function claimCurrentFranchise() {{
      const fid = currentDrawerId;
      closeDrawer();
      setTimeout(() => {{
        openOnboardingModal(fid);
      }}, 200);
    }}

    function closeOnboardingModal() {{
      document.getElementById('onboardingModalOverlay').classList.add('opacity-0', 'pointer-events-none');
      document.getElementById('onboardingModal').classList.add('scale-95');
      document.body.classList.remove('drawer-open');
    }}

    function goToStep(step) {{
      currentStep = step;
      
      for (let i = 1; i <= 4; i++) {{
        const stepDiv = document.getElementById(`onboardingStep${{i}}`);
        const indicator = document.getElementById(`step-indicator-${{i}}`);
        
        if (i === step) {{
          stepDiv.classList.remove('hidden');
          indicator.className = "text-center py-1 rounded-lg bg-[#f2920b] text-slate-950 font-black transition";
        }} else if (i < step) {{
          stepDiv.classList.add('hidden');
          indicator.className = "text-center py-1 rounded-lg bg-emerald-100 text-emerald-800 font-bold transition";
        }} else {{
          stepDiv.classList.add('hidden');
          indicator.className = "text-center py-1 rounded-lg bg-slate-200 text-slate-600 font-bold transition";
        }}
      }}

      const prevBtn = document.getElementById('obPrevBtn');
      const nextBtn = document.getElementById('obNextBtn');
      const submitBtn = document.getElementById('obSubmitBtn');

      prevBtn.disabled = (step === 1);

      if (step === 4) {{
        nextBtn.classList.add('hidden');
        submitBtn.classList.remove('hidden');
      }} else {{
        nextBtn.classList.remove('hidden');
        submitBtn.classList.add('hidden');
      }}
    }}

    function nextStep() {{
      // Validaciones básicas de paso
      if (currentStep === 1) {{
        const nom = document.getElementById('ob_nombre').value.trim();
        const web = document.getElementById('ob_web').value.trim();
        const email = document.getElementById('ob_contacto_email').value.trim();
        const tel = document.getElementById('ob_contacto_tel').value.trim();
        if (!nom || !web || !email || !tel) {{
          alert("Por favor completa los campos obligatorios del Responsable de Expansión.");
          return;
        }}
      }}
      if (currentStep < 4) {{
        goToStep(currentStep + 1);
      }}
    }}

    function prevStep() {{
      if (currentStep > 1) {{
        goToStep(currentStep - 1);
      }}
    }}

    async function submitOnboarding(e) {{
      e.preventDefault();
      
      const submitBtn = document.getElementById('obSubmitBtn');
      submitBtn.disabled = true;
      submitBtn.textContent = "Registrando expediente...";

      const ticketId = `CP-FRQ-2026-${{Math.floor(1000 + Math.random() * 9000)}}`;

      const payload = {{
        tipo: "onboarding_franquicia",
        evento: "alta_homologacion_franquicia",
        ticket: ticketId,
        fecha: new Date().toISOString(),
        nombre_franquicia: document.getElementById('ob_nombre').value,
        web: document.getElementById('ob_web').value,
        sede: document.getElementById('ob_sede').value,
        num_clubs: document.getElementById('ob_num_clubs').value,
        responsable_nombre: document.getElementById('ob_contacto_nombre').value,
        responsable_cargo: document.getElementById('ob_contacto_cargo').value,
        responsable_email: document.getElementById('ob_contacto_email').value,
        responsable_tel: document.getElementById('ob_contacto_tel').value,
        tipo_instalacion: document.getElementById('ob_tipo_instalacion').value,
        altura_minima: document.getElementById('ob_altura_minima').value,
        pistas_minimas: document.getElementById('ob_pistas_minimas').value,
        m2_minimos: document.getElementById('ob_m2_minimos').value,
        canon_entrada: document.getElementById('ob_canon_entrada').value,
        royalty_mensual: document.getElementById('ob_royalty_mensual').value,
        inversion_media: document.getElementById('ob_inversion_media').value,
        payback: document.getElementById('ob_payback').value,
        exclusividad: document.getElementById('ob_exclusividad').value,
        software: document.getElementById('ob_software').value,
        domotica: document.getElementById('ob_domotica').value,
        camaras: document.getElementById('ob_camaras').value,
        servicios: document.getElementById('ob_servicios').value,
        diferencial: document.getElementById('ob_diferencial').value,
      }};

      try {{
        // Envío asíncrono al Webhook oficial de CoolPadel
        fetch(WEBHOOK_URL, {{
          method: 'POST',
          mode: 'no-cors',
          headers: {{ 'Content-Type': 'application/json' }},
          body: JSON.stringify(payload)
        }}).catch(err => console.log('Webhook dispatched:', err));
      }} catch (err) {{
        console.error('Error enviando webhook:', err);
      }}

      // Ocultar pasos y mostrar pantalla de éxito
      for (let i = 1; i <= 4; i++) {{
        document.getElementById(`onboardingStep${{i}}`).classList.add('hidden');
      }}
      document.getElementById('onboardingNavBtns').classList.add('hidden');
      
      const successBox = document.getElementById('onboardingSuccess');
      document.getElementById('successTicket').textContent = ticketId;
      
      const msgWa = `Hola Javier, acabo de registrar la homologación de mi franquicia ${{payload.nombre_franquicia}} con el ticket ${{ticketId}}. Mi email es ${{payload.responsable_email}}`;
      document.getElementById('successWaBtn').href = `https://wa.me/34680317486?text=${{encodeURIComponent(msgWa)}}`;
      
      successBox.classList.remove('hidden');
      lucide.createIcons();
    }}

    // =========================================================================
    // ENFOCAR CLUB EN EL MAPA (DESPLIEGA EL MAPA SI ESTÁ PLEGADO U OCULTO)
    // =========================================================================
    function focusClubOnMap(id) {{
      const f = FRANQUICIAS.find(item => item.id === id);
      if (!f || !f.coords || f.coords.length !== 2) return;

      closeDrawer();

      // Si estamos en vista Tabla, cambiar a vista Mapa para desplegarlo
      if (currentView === 'table') {{
        switchView('grid');
      }}

      const mapContainer = document.getElementById('mapContainer');
      if (mapContainer) {{
        mapContainer.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
      }}

      setTimeout(() => {{
        zoomToClubRegion(f, id);
      }}, 250);
    }}

    // =========================================================================
    // ENFOCAR CLUB CONCRETO EN EL MAPA Y HACER ZOOM A SU MARCADOR
    // =========================================================================
    function focusSpecificClub(id, idx) {{
      const f = FRANQUICIAS.find(item => item.id === id);
      if (!f) return;
      closeDrawer();
      if (currentView === 'table') switchView('grid');

      const mapContainer = document.getElementById('mapContainer');
      if (mapContainer) {{
        mapContainer.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
      }}

      if (f.sub_clubs && f.sub_clubs[idx]) {{
        deploySubClubs(f);
        const sc = f.sub_clubs[idx];
        if (map && sc.coords && sc.coords.length === 2) {{
          setTimeout(() => {{
            map.flyTo(sc.coords, 14, {{ duration: 1.2 }});
          }}, 300);
        }}
      }} else {{
        zoomToClubRegion(f, id);
      }}
    }}

    // =========================================================================
    // SLIDE-OVER DRAWER LOGIC
    // =========================================================================
    function openDrawer(id) {{
      registerUserInteraction();
      const f = FRANQUICIAS.find(item => item.id === id);
      if (!f) return;
      currentDrawerId = id;

      // Si el mapa estaba sin desplegar (ej. vista tabla), desplegarlo
      if (currentView === 'table') {{
        switchView('grid');
      }}

      // Centrar y hacer zoom a la comunidad autónoma del club
      zoomToClubRegion(f, id);

      document.getElementById('drawerTitle').textContent = f.nombre;
      document.getElementById('drawerFlag').textContent = f.bandera;
      document.getElementById('drawerBadge').textContent = f.modelo;
      document.getElementById('drawerBadge').className = `inline-block px-2.5 py-0.5 rounded-full text-xs font-bold border ${{f.modelo_badge}}`;
      document.getElementById('drawerCity').innerHTML = `<i data-lucide="map-pin" class="w-3.5 h-3.5 text-slate-400"></i> Sede: ${{f.ciudad_sede}}, ${{f.pais}}`;
      document.getElementById('drawerTagline').textContent = f.tagline;
      document.getElementById('drawerResumen').textContent = f.resumen;
      document.getElementById('drawerClubs').textContent = f.num_clubs;
      document.getElementById('drawerPistas').textContent = f.num_pistas;
      document.getElementById('drawerSoftware').textContent = f.software;
      document.getElementById('drawerFundadores').textContent = f.fundadores;

      // Sedes interactivas y clickables
      const sedesList = document.getElementById('drawerSedes');
      if (f.sub_clubs && f.sub_clubs.length > 0) {{
        sedesList.innerHTML = `
          <div class="mb-3 p-3 bg-amber-50 rounded-2xl border border-amber-200 text-xs text-amber-950 font-bold flex items-center justify-between shadow-2xs">
            <span class="flex items-center gap-1.5">
              <span>🎾</span>
              <span>${{f.sub_clubs.length}} clubes desplegados en el mapa</span>
            </span>
            <button onclick="closeDrawer(); focusClubOnMap('${{f.id}}');" class="text-[#f2920b] hover:text-[#d97f08] font-black text-xs uppercase tracking-wider cursor-pointer">Ver en Mapa →</button>
          </div>
        ` + f.sub_clubs.slice(0, 12).map((s, i) => `
          <div onclick="focusSpecificClub('${{f.id}}', ${{i}})" class="p-2.5 rounded-xl bg-slate-50 hover:bg-amber-50 hover:border-[#f2920b] border border-slate-200/90 transition-all cursor-pointer flex items-center justify-between gap-2 group/sub mb-2 shadow-2xs">
            <div class="flex items-center gap-2 truncate">
              <span class="w-7 h-7 rounded-lg bg-white border border-slate-200 flex items-center justify-center text-xs group-hover/sub:bg-[#f2920b] group-hover/sub:text-slate-950 shrink-0 shadow-2xs">🎾</span>
              <div class="truncate">
                <span class="text-xs font-black text-slate-950 group-hover/sub:text-[#f2920b] transition block truncate">${{s.nombre}}</span>
                <span class="text-[11px] text-slate-500 font-medium">${{s.ciudad}}${{s.pistas ? ' · ' + s.pistas : ''}}</span>
              </div>
            </div>
            <span class="text-[10px] font-bold text-slate-400 group-hover/sub:text-[#f2920b] flex items-center gap-1 shrink-0">
              <span>Ver mapa</span>
              <i data-lucide="map-pin" class="w-3 h-3"></i>
            </span>
          </div>
        `).join('') + (f.sub_clubs.length > 12 ? `<div class="text-xs font-bold text-slate-500 italic pt-1 text-center">+ ${{f.sub_clubs.length - 12}} clubes adicionales desplegados en el mapa interactivo...</div>` : '');
      }} else {{
        sedesList.innerHTML = f.sedes_principales.map(s => `
          <div onclick="closeDrawer(); focusClubOnMap('${{f.id}}');" class="p-2.5 rounded-xl bg-slate-50 hover:bg-amber-50 hover:border-[#f2920b] border border-slate-200/90 transition-all cursor-pointer flex items-center justify-between gap-2 group/sub mb-2 shadow-2xs">
            <div class="flex items-center gap-2 truncate">
              <span class="w-7 h-7 rounded-lg bg-white border border-slate-200 flex items-center justify-center text-xs group-hover/sub:bg-[#f2920b] group-hover/sub:text-slate-950 shrink-0 shadow-2xs">🎾</span>
              <span class="text-xs font-black text-slate-950 group-hover/sub:text-[#f2920b] transition truncate">${{s}}</span>
            </div>
            <span class="text-[10px] font-bold text-slate-400 group-hover/sub:text-[#f2920b] flex items-center gap-1 shrink-0">
              <span>Ver mapa</span>
              <i data-lucide="map-pin" class="w-3 h-3"></i>
            </span>
          </div>
        `).join('');
      }}

      // Tech
      const techBox = document.getElementById('drawerTech');
      techBox.innerHTML = `
        <div><strong>Pistas y Césped:</strong> ${{f.tecnologia_pistas.pistas}}</div>
        <div><strong>Software y Reservas:</strong> ${{f.tecnologia_pistas.software}}</div>
        <div><strong>Domótica y Accesos:</strong> ${{f.tecnologia_pistas.domotica}}</div>
        <div><strong>Grabación / Vídeo:</strong> ${{f.tecnologia_pistas.grabacion}}</div>
        <div><strong>Restauración / Hospitality:</strong> ${{f.tecnologia_pistas.restauracion}}</div>
      `;

      // Expansion
      const expBox = document.getElementById('drawerExpansion');
      expBox.innerHTML = `
        <div><strong>Tipo de Contrato / Expansión:</strong> ${{f.modelo_expansion.tipo_contrato}}</div>
        <div><strong>Perfil de Club Idóneo:</strong> ${{f.modelo_expansion.perfil_club}}</div>
        <div><strong>Canon & Royalties:</strong> ${{f.modelo_expansion.canon_royalties}}</div>
        <div><strong>Inversión Estimada:</strong> ${{f.modelo_expansion.inversion_media}}</div>
      `;

      // Diferencial
      document.getElementById('drawerDiferencial').textContent = f.diferencial;

      // Botones
      document.getElementById('drawerWebBtn').href = f.web;
      document.getElementById('drawerPageBtn').href = `./${{f.id}}/`;
      document.getElementById('drawerWaBtn').href = `https://wa.me/34680317486?text=Hola%20Javier%2C%20estoy%20viendo%20la%20ficha%20de%20${{encodeURIComponent(f.nombre)}}%20en%20el%20directorio%20y%20quiero%20hacerte%20una%20consulta`;

      // Mostrar
      document.getElementById('drawerOverlay').classList.remove('opacity-0', 'pointer-events-none');
      document.getElementById('franchiseDrawer').classList.remove('translate-x-full');
      document.body.classList.add('drawer-open');
      lucide.createIcons();
    }}

    function closeDrawer() {{
      document.getElementById('drawerOverlay').classList.add('opacity-0', 'pointer-events-none');
      document.getElementById('franchiseDrawer').classList.add('translate-x-full');
      document.body.classList.remove('drawer-open');
    }}

    // Cerrar modales con Escape
    document.addEventListener('keydown', function(e) {{
      if (e.key === 'Escape') {{
        closeDrawer();
        closeCompareModal();
        closeOnboardingModal();
      }}
    }});

    // Gestión de idiomas (Desktop y Móvil)
    function toggleLangDropdown(e) {{
      if (e) e.stopPropagation();
      const menu = document.getElementById('lang-dropdown-menu');
      const arrow = document.getElementById('lang-dropdown-arrow');
      if (!menu) return;
      const isHidden = menu.classList.contains('hidden');
      if (isHidden) {{
        menu.classList.remove('hidden');
        if (arrow) arrow.classList.add('rotate-180');
      }} else {{
        menu.classList.add('hidden');
        if (arrow) arrow.classList.remove('rotate-180');
      }}
    }}

    function toggleLangDropdownMob(e) {{
      if (e) e.stopPropagation();
      const menu = document.getElementById('lang-dropdown-menu-mob');
      const arrow = document.getElementById('lang-dropdown-arrow-mob');
      if (!menu) return;
      const isHidden = menu.classList.contains('hidden');
      if (isHidden) {{
        menu.classList.remove('hidden');
        if (arrow) arrow.classList.add('rotate-180');
      }} else {{
        menu.classList.add('hidden');
        if (arrow) arrow.classList.remove('rotate-180');
      }}
    }}

    function switchLanguage(lang) {{
      try {{
        localStorage.setItem('coolpadel_lang', lang);
      }} catch(e) {{}}
      if (lang === 'es') {{
        const menu = document.getElementById('lang-dropdown-menu');
        if (menu) menu.classList.add('hidden');
        const menuMob = document.getElementById('lang-dropdown-menu-mob');
        if (menuMob) menuMob.classList.add('hidden');
      }} else if (lang === 'en') {{
        window.location.href = '../en/';
      }} else if (lang === 'fr') {{
        window.location.href = '../fr/';
      }} else if (lang === 'it') {{
        window.location.href = '../it/';
      }}
    }}

    // Cerrar desplegables de idioma al hacer click fuera
    document.addEventListener('click', function(e) {{
      const container = document.getElementById('lang-dropdown-container');
      const menu = document.getElementById('lang-dropdown-menu');
      const arrow = document.getElementById('lang-dropdown-arrow');
      if (container && menu && !container.contains(e.target)) {{
        menu.classList.add('hidden');
        if (arrow) arrow.classList.remove('rotate-180');
      }}
      const containerMob = document.getElementById('lang-dropdown-container-mob');
      const menuMob = document.getElementById('lang-dropdown-menu-mob');
      const arrowMob = document.getElementById('lang-dropdown-arrow-mob');
      if (containerMob && menuMob && !containerMob.contains(e.target)) {{
        menuMob.classList.add('hidden');
        if (arrowMob) arrowMob.classList.remove('rotate-180');
      }}
    }});

    // ── DATA GUARD (ANTI-SCRAPING INTELIGENTE CLIENT-SIDE) ──────────────────
    let isDataGuardActive = false;
    let queryTimestamps = [];
    const MAX_QUERIES_PER_10S = 14;

    const DATA_GUARD_TEXTS = {{
      es: {{
        tag: 'Acceso de Datos en Pausa',
        msg: 'Hemos detectado una tasa inusual de consultas en el visor de cadenas. Si necesitas el censo completo o análisis de mercado a escala, contáctanos directamente.',
        btn: 'Hablar por WhatsApp'
      }},
      en: {{
        tag: 'Data Access Paused',
        msg: "We have detected unusual query activity on the chain directory. If you require full census data or market analysis at scale, please contact us directly.",
        btn: 'Chat on WhatsApp'
      }},
      fr: {{
        tag: 'Accès aux Données Suspendu',
        msg: "Une activité inhabituelle de requêtes a été détectée sur le répertoire. Si vous avez besoin de données à grande échelle, veuillez nous contacter directement.",
        btn: 'Contacter sur WhatsApp'
      }},
      it: {{
        tag: 'Accesso Dati in Pausa',
        msg: "È stata rilevata un'attività insolita di consultazione nel catalogo. Se necessiti dell'intero database o di un'analisi di mercato su larga scala, contattaci.",
        btn: 'Chatta su WhatsApp'
      }}
    }};

    function triggerDataGuard(reason) {{
      if (isDataGuardActive) return;
      isDataGuardActive = true;
      const banner = document.getElementById('dataGuardBanner');
      if (!banner) return;

      const lang = '{lang}' || 'es';
      const t = DATA_GUARD_TEXTS[lang] || DATA_GUARD_TEXTS.es;

      const tagEl = document.getElementById('dataGuardTag');
      const msgEl = document.getElementById('dataGuardMsg');
      if (tagEl) tagEl.textContent = t.tag;
      if (msgEl) msgEl.textContent = t.msg;

      banner.classList.remove('opacity-0', 'pointer-events-none', 'translate-y-8');
      banner.classList.add('opacity-100', 'translate-y-0');

      try {{
        if (window.lucide) lucide.createIcons();
      }} catch (e) {{}}
    }}

    function dismissDataGuard() {{
      const banner = document.getElementById('dataGuardBanner');
      if (banner) {{
        banner.classList.add('opacity-0', 'pointer-events-none', 'translate-y-8');
        banner.classList.remove('opacity-100', 'translate-y-0');
      }}
    }}

    function registerUserInteraction() {{
      const now = Date.now();
      queryTimestamps.push(now);
      queryTimestamps = queryTimestamps.filter(t => now - t < 10000);
      if (queryTimestamps.length > MAX_QUERIES_PER_10S) {{
        triggerDataGuard('rate_limit');
      }}
    }}

    // Detección 1: Atajos de teclado de scraping / DevTools (F12, Ctrl+U, Ctrl+Shift+I, etc.)
    document.addEventListener('keydown', function(e) {{
      const k = e.key;
      const isDevTools = (
        k === 'F12' ||
        (e.ctrlKey && e.shiftKey && (k === 'I' || k === 'i' || k === 'J' || k === 'j' || k === 'C' || k === 'c')) ||
        (e.ctrlKey && (k === 'U' || k === 'u' || k === 'S' || k === 's'))
      );
      if (isDevTools) {{
        triggerDataGuard('devtools_shortcut');
      }}
    }});

    // Detección 2: Apertura de consola / DevTools mediante timing loop
    (function detectDevTools() {{
      let devtoolsOpen = false;
      const threshold = 160;
      setInterval(function() {{
        const widthThreshold = window.outerWidth - window.innerWidth > threshold;
        const heightThreshold = window.outerHeight - window.innerHeight > threshold;
        if ((widthThreshold || heightThreshold) && !devtoolsOpen) {{
          devtoolsOpen = true;
          triggerDataGuard('devtools_docked');
        }}
      }}, 1000);
    }})();

    // Detección 3: Copia masiva de texto en el directorio
    document.addEventListener('copy', function(e) {{
      const selection = window.getSelection().toString();
      if (selection && selection.length > 350) {{
        triggerDataGuard('mass_copy');
      }}
    }});

    // Inicializar mapa al cargar
    document.addEventListener('DOMContentLoaded', function() {{
      initMap();
    }});
  </script>
  <script src="/assets/js/cp-analytics.js" defer></script>
</body>
</html>
"""
    return full_html


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    print(">> Generando Directorio de Franquicias en 4 Idiomas (ES, EN, FR, IT)...")
    for lang in ["es", "en", "fr", "it"]:
        if lang == "es":
            target_dir = os.path.join(base_dir, "franquicias-padel")
        else:
            target_dir = os.path.join(base_dir, lang, "franquicias-padel")
        os.makedirs(target_dir, exist_ok=True)
        target_file = os.path.join(target_dir, "index.html")
        html_content = render_html(lang=lang)
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"  [OK] Directorio Hub ({lang.upper()}): {target_file}")

    print(f"Total de entidades incluidas: {len(FRANQUICIAS)}")

    try:
        import generate_franquicias_pages
        generate_franquicias_pages.main()
    except Exception as e:
        print(f"Aviso generando fichas individuales de franquicias: {e}")


if __name__ == "__main__":
    main()
