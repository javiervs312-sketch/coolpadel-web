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


def render_html():
    total_franquicias = len(FRANQUICIAS)
    paises_unicos = len(set(f["pais"] for f in FRANQUICIAS))

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
        <article class="franchise-card group bg-white rounded-3xl p-6 border border-slate-200/90 shadow-xs hover:shadow-xl hover:border-[#f2920b]/40 transition-all duration-300 flex flex-col justify-between cursor-pointer relative"
                 data-id="{fid}"
                 data-region="{region_f}"
                 data-model="{tipo_cat}"
                 data-budget="{budget_tier}"
                 data-facility="{facility_type}"
                 data-search="{nombre.lower()} {pais.lower()} {ciudad.lower()} {modelo.lower()}"
                 onclick="openDrawer('{fid}')">
          <div>
            <div class="flex items-start justify-between gap-3 mb-4">
              <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold border {badge_cls}">
                {modelo}
              </span>
              <div class="flex items-center gap-2" onclick="event.stopPropagation()">
                <button onclick="toggleCompare('{fid}')" id="compare-btn-{fid}"
                        class="compare-card-btn inline-flex items-center gap-1 px-2.5 py-1 rounded-lg text-[11px] font-bold border border-slate-200 bg-white text-slate-600 hover:border-[#f2920b] hover:text-[#f2920b] transition">
                  <i data-lucide="scale" class="w-3.5 h-3.5"></i>
                  <span class="compare-label">Comparar</span>
                </button>
                <span class="text-2xl" title="{pais}">{bandera}</span>
              </div>
            </div>

            <h3 class="font-heading font-black text-2xl text-slate-950 group-hover:text-[#f2920b] transition-colors mb-1.5 flex items-center justify-between">
              <span>{nombre}</span>
              <i data-lucide="chevron-right" class="w-5 h-5 text-slate-400 group-hover:text-[#f2920b] group-hover:translate-x-1 transition-all"></i>
            </h3>
            
            <p class="text-xs font-semibold text-slate-500 mb-3 flex items-center gap-1.5">
              <i data-lucide="map-pin" class="w-3.5 h-3.5 text-slate-400"></i>
              <span>{ciudad}, {pais}</span>
            </p>

            <p class="text-slate-600 text-sm leading-relaxed mb-5 line-clamp-2">
              {tagline}
            </p>

            <!-- Grid de métricas clave -->
            <div class="grid grid-cols-3 gap-2 py-3 px-3.5 bg-slate-50 rounded-2xl border border-slate-100 mb-5">
              <div>
                <span class="block text-[10px] uppercase font-bold text-slate-400">Clubes</span>
                <span class="font-heading font-black text-sm text-slate-900">{num_clubs}</span>
              </div>
              <div>
                <span class="block text-[10px] uppercase font-bold text-slate-400">Pistas</span>
                <span class="font-heading font-black text-sm text-slate-900">{num_pistas}</span>
              </div>
              <div>
                <span class="block text-[10px] uppercase font-bold text-slate-400">Software</span>
                <span class="font-heading font-bold text-xs text-slate-800 truncate block" title="{software}">{software.split('/')[0].strip()}</span>
              </div>
            </div>
          </div>

          <div class="pt-2 border-t border-slate-100 flex items-center justify-between">
            <span class="text-xs font-bold text-slate-500 group-hover:text-slate-900 transition">Ver Ficha & Dossier</span>
            <span class="inline-flex items-center justify-center w-8 h-8 rounded-full bg-slate-100 group-hover:bg-[#f2920b] group-hover:text-white transition">
              <i data-lucide="arrow-up-right" class="w-4 h-4"></i>
            </span>
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
          <td class="py-4 px-4 text-right">
            <button class="inline-flex items-center gap-1 text-xs font-bold text-[#f2920b] hover:text-[#d97f08] transition">
              <span>Dossier</span>
              <i data-lucide="chevron-right" class="w-3.5 h-3.5"></i>
            </button>
          </td>
        </tr>
        """

    full_html = f"""<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Directorio y Comparador de Franquicias y Cadenas de Pádel (+1 Club) | CoolPadel Studios</title>
  <meta name="description" content="Directorio interactivo, mapa y comparador cara a cara de {total_franquicias} cadenas de clubs y franquicias de pádel (+1 club abierto). Requisitos de nave, inversión CAPEX, royalties, software y retorno para inversores.">
  <link rel="canonical" href="https://coolpadelstudios.com/franquicias-padel/">

  <!-- Favicon -->
  <link rel="icon" type="image/png" href="../assets/images/coolpadel-mascot-hd.png">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:locale" content="es_ES">
  <meta property="og:site_name" content="CoolPadel Studios">
  <meta property="og:url" content="https://coolpadelstudios.com/franquicias-padel/">
  <meta property="og:title" content="Directorio y Comparador B2B de Cadenas y Franquicias de Pádel | {total_franquicias} Operadores">
  <meta property="og:description" content="Guía y comparador cara a cara para inversores y clubes: contrasta royalties, requisitos de nave, software y modelos de negocio en {paises_unicos} países.">
  <meta property="og:image" content="https://coolpadelstudios.com/assets/images/savemyplay-1.jpg">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Directorio y Comparador de Franquicias de Pádel | CoolPadel Studios">
  <meta name="twitter:description" content="Censo internacional de {total_franquicias} cadenas de pádel con varias sedes bajo el mismo nombre y franquicias en más de 20 países.">
  <meta name="twitter:image" content="https://coolpadelstudios.com/assets/images/savemyplay-1.jpg">

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
    #franchiseMap {{
      height: 480px;
      width: 100%;
      border-radius: 1.5rem;
      z-index: 10;
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
    .leaflet-popup-content-wrapper {{
      border-radius: 1rem;
      padding: 0.25rem;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
    }}
    .drawer-open {{
      overflow: hidden;
    }}
  </style>
</head>
<body class="bg-[#f8fafc] text-slate-800 antialiased selection:bg-[#f2920b] selection:text-slate-950 min-h-screen flex flex-col">

  <!-- NAVBAR BLANCA UNIFICADA COOLPADEL -->
  <header class="sticky top-0 z-40 bg-white text-slate-900 border-b border-slate-200 shadow-sm w-full">
    <div class="w-full max-w-[1700px] mx-auto px-3 sm:px-6 lg:px-10 py-1.5 sm:py-0 h-auto sm:h-16 lg:h-18">
      
      <!-- DESKTOP NAVBAR (3 COLUMNAS: IZQUIERDA + CENTRO 100% + DERECHA) -->
      <div class="hidden sm:grid grid-cols-[1fr_auto_1fr] items-center h-full w-full gap-2 lg:gap-4">
        
        <!-- COLUMNA 1: OJOS + LLAVEROS, CÁMARAS PISTAS Y BLOG A LA IZQUIERDA DEL LOGO -->
        <div class="flex items-center justify-between min-w-0 h-full">
          <a href="../" class="group py-1 inline-flex items-center shrink-0">
            <img src="../assets/images/eyes-thumb.png?v=fixed_eyes" alt="CoolPadel Eyes" style="height: 24px; max-height: 24px; width: auto;" class="object-contain group-hover:scale-110 transition duration-300">
          </a>
          <div class="flex-1 flex items-center justify-center px-2 gap-3.5 lg:gap-6">
            <a href="../#llaveros" class="font-heading font-black text-xs lg:text-[13px] tracking-wider uppercase text-slate-950 hover:text-[#f2920b] transition select-none whitespace-nowrap">
              Llaveros
            </a>
            <a href="../camaras/" class="font-heading font-black text-xs lg:text-[13px] tracking-wider uppercase text-slate-950 hover:text-[#f2920b] transition select-none whitespace-nowrap">
              Cámaras pistas
            </a>
            <a href="../blog/" class="font-heading font-black text-xs lg:text-[13px] tracking-wider uppercase text-slate-950 hover:text-[#f2920b] transition select-none whitespace-nowrap">
              Blog
            </a>
          </div>
        </div>

        <!-- COLUMNA 2: MASCOTA + COOLPADEL CENTRADO -->
        <div class="flex items-center justify-center shrink-0 px-2 lg:px-4">
          <a href="../" class="flex items-center justify-center gap-2 sm:gap-3 group py-1">
            <img src="../assets/images/coolpadel-mascot-hd.png" alt="Mascota CoolPadel" style="height: 46px; max-height: 46px; width: auto;" class="object-contain group-hover:scale-105 transition">
            <img src="../assets/images/coolpadel-typography-hd.png" alt="CoolPadel" style="height: 26px; max-height: 26px; width: auto;" class="object-contain">
          </a>
        </div>

        <!-- COLUMNA 3: CADENAS DE CLUBS + [CONTACTAR DESPLAZADO A LA DERECHA DEL TODO] -->
        <div class="flex items-center justify-between min-w-0 h-full gap-2 sm:gap-3 lg:gap-4">
          <div class="flex items-center pl-1 sm:pl-2">
            <a href="./" class="font-heading font-black text-xs lg:text-[13px] tracking-wider uppercase text-[#f2920b] transition select-none whitespace-nowrap border-b-2 border-[#f2920b] pb-0.5">
              Cadenas de clubs
            </a>
          </div>

          <!-- BLOQUE A LA DERECHA DEL TODO: CONTACTAR (SIN OJOS) -->
          <div class="flex items-center ml-auto">
            <a href="https://wa.me/34680317486?text=Hola%20Javier%2C%20estoy%20viendo%20el%20directorio%20global%20de%20franquicias%20de%20p%C3%A1del" target="_blank" class="group relative inline-flex items-center gap-1.5 px-3.5 sm:px-4 py-1.5 sm:py-2 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] active:bg-[#76d3f6] text-slate-950 active:scale-95 font-heading font-black text-xs sm:text-xs lg:text-sm tracking-wider uppercase transition-all duration-300 shadow-[0_4px_12px_rgba(242,146,11,0.2)] hover:scale-105 shrink-0 overflow-hidden">
              <span class="font-black">Contactar</span>
              <div class="w-4 h-4 sm:w-5 sm:h-5 rounded-full bg-slate-950/10 group-hover:bg-slate-950 group-hover:text-white flex items-center justify-center transition-all duration-300 shrink-0">
                <i data-lucide="arrow-up-right" class="w-2.5 h-2.5 sm:w-3 sm:h-3 stroke-[3]"></i>
              </div>
            </a>
          </div>
        </div>
      </div>

      <!-- MÓVIL NAVBAR -->
      <div class="flex sm:hidden flex-col gap-1.5 py-1.5 w-full">
        <!-- FILA 1: LOGO CENTRADO (SIN OJOS A LA DERECHA) -->
        <div class="flex items-center justify-between w-full px-2">
          <a href="../" class="py-0.5 inline-flex items-center shrink-0">
            <img src="../assets/images/eyes-thumb.png?v=fixed_eyes" alt="CoolPadel Eyes" style="height: 18px; max-height: 18px; width: auto;" class="object-contain">
          </a>
          <a href="../" class="flex items-center justify-center gap-1.5 py-0.5">
            <img src="../assets/images/coolpadel-mascot-hd.png" alt="Mascota CoolPadel" style="height: 28px; max-height: 28px; width: auto;" class="object-contain">
            <img src="../assets/images/coolpadel-typography-hd.png" alt="CoolPadel" style="height: 18px; max-height: 18px; width: auto;" class="object-contain">
          </a>
          <div class="w-[18px]"></div>
        </div>
        <!-- FILA 2: LLAVEROS + CÁMARAS PISTAS + BLOG + CADENAS DE CLUBS + CONTACTAR -->
        <div class="flex items-center justify-between w-full gap-1 pt-1 border-t border-slate-100 px-1 overflow-x-auto">
          <div class="flex items-center gap-2 shrink-0">
            <a href="../#llaveros" class="font-heading font-black text-[10px] tracking-wider uppercase text-slate-950 hover:text-[#f2920b] transition whitespace-nowrap">
              Llaveros
            </a>
            <a href="../camaras/" class="font-heading font-black text-[10px] tracking-wider uppercase text-slate-950 hover:text-[#f2920b] transition whitespace-nowrap">
              Cámaras pistas
            </a>
            <a href="../blog/" class="font-heading font-black text-[10px] tracking-wider uppercase text-slate-950 hover:text-[#f2920b] transition whitespace-nowrap">
              Blog
            </a>
            <a href="./" class="font-heading font-black text-[10px] tracking-wider uppercase text-[#f2920b] whitespace-nowrap border-b border-[#f2920b]">
              Cadenas de clubs
            </a>
          </div>
          <a href="https://wa.me/34680317486?text=Hola%20Javier%2C%20estoy%20viendo%20el%20directorio%20global%20de%20franquicias%20de%20p%C3%A1del" target="_blank" class="group relative inline-flex items-center justify-center gap-1 px-2.5 py-1 rounded-full bg-[#f2920b] active:bg-[#76d3f6] text-slate-950 active:scale-95 font-heading font-black text-[10px] uppercase tracking-wider transition shadow-xs shrink-0">
            <span class="font-black">Contactar</span>
            <div class="w-3 h-3 rounded-full bg-slate-950/10 flex items-center justify-center">
              <i data-lucide="arrow-up-right" class="w-2 h-2 stroke-[3]"></i>
            </div>
        </div>
      </div>

    </div>
  </header>

  <!-- MAIN -->
  <main class="flex-1">

    <!-- HERO SECTION (ESPACIADO COMPACTO SIN VACÍO INEXPLICABLE) -->
    <section class="pt-8 pb-4 sm:pt-10 sm:pb-6 bg-gradient-to-b from-white via-slate-50 to-[#f8fafc] border-b border-slate-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div class="max-w-4xl space-y-4">
          <h1 class="font-heading font-black text-3xl sm:text-5xl lg:text-6xl text-slate-950 leading-[1.08] uppercase tracking-tight">
            Directorio y Comparador de Franquicias de Pádel
          </h1>

          <p class="text-base sm:text-xl text-slate-600 font-medium leading-relaxed">
            El directorio para operadores y clubes que quieren franquiciarse:<br>
            Ponte en contacto con más de 153 cadenas y franquicias de más de 25 países.<br>
            Infórmate, compara y encuentra el modelo que tu club necesita.
          </p>

          <!-- Acciones Principales Hero: Botón Alta de Franquicia fuera de la barra -->
          <div class="pt-2">
            <button onclick="openOnboardingModal()" class="inline-flex items-center gap-2 px-6 py-3.5 rounded-2xl bg-[#f2920b] hover:bg-[#d97f08] text-slate-950 font-heading font-black text-xs sm:text-sm uppercase tracking-wider transition shadow-md hover:scale-105 active:scale-95">
              <i data-lucide="plus-circle" class="w-4 h-4 stroke-[2.5]"></i>
              <span>¿Tienes una Franquicia? Date de Alta / Reclama tu Ficha</span>
            </button>
          </div>
        </div>

        <!-- KPI BANNER (3 TARJETAS) -->
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 sm:gap-6 mt-6 pt-5 border-t border-slate-200/80">
          <div class="bg-white p-5 sm:p-6 rounded-2xl border border-slate-200/80 shadow-xs">
            <span class="block text-xs font-bold uppercase tracking-wider text-slate-400 mb-1">Cadenas / Franquicias</span>
            <span class="font-heading font-black text-3xl sm:text-4xl text-slate-950">+153</span>
            <span class="text-xs text-slate-500 font-medium block mt-1">Con +1 club abierto</span>
          </div>
          
          <div class="bg-white p-5 sm:p-6 rounded-2xl border border-slate-200/80 shadow-xs">
            <span class="block text-xs font-bold uppercase tracking-wider text-slate-400 mb-1">Pistas Totales</span>
            <span class="font-heading font-black text-3xl sm:text-4xl text-slate-950">+8.500 pistas</span>
            <span class="text-xs text-slate-500 font-medium block mt-1">Bajo gestión analizada</span>
          </div>

          <div class="bg-white p-5 sm:p-6 rounded-2xl border border-slate-200/80 shadow-xs">
            <span class="block text-xs font-bold uppercase tracking-wider text-slate-400 mb-1">Presencia Global</span>
            <span class="font-heading font-black text-3xl sm:text-4xl text-slate-950">+25 países</span>
            <span class="text-xs text-slate-500 font-medium block mt-1">Europa, América, Oriente Medio, África y Oceanía</span>
          </div>
        </div>

      </div>
    </section>

    <!-- INTERACTIVE SECTION (CONECTADO SIN SALTO EXCESIVO) -->
    <section class="pt-4 pb-12 sm:pt-6 sm:pb-16 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- CONTROLES Y FILTROS -->
      <div class="bg-white rounded-3xl p-5 sm:p-7 border border-slate-200/90 shadow-sm mb-8 space-y-5" id="filtrosContainer">
        
        <!-- Barra de búsqueda y vista -->
        <div class="flex flex-col md:flex-row gap-4 items-stretch md:items-center justify-between">
          <div class="relative flex-1">
            <i data-lucide="search" class="w-5 h-5 text-slate-400 absolute left-4 top-1/2 -translate-y-1/2"></i>
            <input type="text" id="searchInput" placeholder="Buscar por cadena, club, ciudad o país (ej. PadelStars, The Padel Hub, Barcelona, Londres, Madrid)..."
                   class="w-full pl-12 pr-4 py-3.5 rounded-2xl bg-slate-50 border border-slate-200 text-slate-950 placeholder-slate-400 font-medium text-sm focus:outline-none focus:ring-2 focus:ring-[#f2920b] focus:bg-white transition"
                   oninput="applyFilters()">
          </div>

          <div class="flex items-center gap-2 self-end md:self-auto shrink-0">
            <button id="viewGridBtn" onclick="switchView('grid')" class="px-4 py-2.5 rounded-xl text-xs font-bold font-heading uppercase tracking-wider bg-slate-900 text-white transition flex items-center gap-1.5 shadow-xs">
              <i data-lucide="map" class="w-4 h-4"></i>
              <span>Mapa</span>
            </button>
            <button id="viewTableBtn" onclick="switchView('table')" class="px-4 py-2.5 rounded-xl text-xs font-bold font-heading uppercase tracking-wider bg-slate-100 text-slate-700 hover:bg-slate-200 transition flex items-center gap-1.5">
              <i data-lucide="table" class="w-4 h-4"></i>
              <span>Tabla</span>
            </button>
          </div>
        </div>

        <!-- Filtro Modelo / Tipo de Operador -->
        <div class="flex items-center gap-1.5 flex-wrap pt-3 border-t border-slate-100">
          <span class="text-xs font-bold uppercase text-slate-400 mr-1 flex items-center gap-1">
            <i data-lucide="tag" class="w-3.5 h-3.5"></i>
            <span>Modelo:</span>
          </span>
          <button onclick="setModelFilter('all')" class="filter-model-btn active px-3 py-1 rounded-lg text-xs font-bold bg-slate-900 text-white transition" data-model="all">Todos</button>
          <button onclick="setModelFilter('cadena')" class="filter-model-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-model="cadena">Cadena Multiclub (Mismo Nombre)</button>
          <button onclick="setModelFilter('corporativo')" class="filter-model-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-model="corporativo">Red Corporativa Propia</button>
          <button onclick="setModelFilter('franquicia')" class="filter-model-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-model="franquicia">Franquicia Llave en Mano</button>
          <button onclick="setModelFilter('automatizado')" class="filter-model-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-model="automatizado">Club Automatizado 24/7</button>
          <button onclick="setModelFilter('boutique')" class="filter-model-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-model="boutique">Boutique & Lujo</button>
        </div>

        <!-- Contador de resultados y Tip -->
        <div class="flex items-center justify-between text-xs font-semibold text-slate-500 pt-2 border-t border-slate-100">
          <span id="resultsCount">Mostrando {total_franquicias} cadenas y franquicias</span>
          <span class="text-slate-500 hidden sm:inline flex items-center gap-1">
            <i data-lucide="info" class="w-3.5 h-3.5 text-[#f2920b]"></i>
            Pulsa el botón <strong>'Comparar'</strong> en cualquier ficha para contrastar hasta 3 franquicias cara a cara
          </span>
        </div>

      </div>

      <!-- MAPA INTERACTIVO -->
      <div id="mapContainer" class="bg-white p-3 sm:p-4 rounded-3xl border border-slate-200/90 shadow-sm mb-10 relative">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 px-3 py-2 mb-2">
          <div class="flex items-center gap-2">
            <span class="w-2.5 h-2.5 rounded-full bg-[#f2920b]"></span>
            <h2 class="font-heading font-black text-sm sm:text-base text-slate-900 uppercase tracking-wider">
              Mapa mundial de principales cadenas de clubs
            </h2>
          </div>

          <!-- SELECTOR DE REGIÓN MODERNO A LA DERECHA (ESTILO DESPLEGABLE DE IDIOMAS) -->
          <div class="relative inline-block text-left" id="region-dropdown-container">
            <button type="button" onclick="toggleRegionDropdown(event)" id="region-dropdown-btn" class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 border border-slate-200 text-xs font-bold text-slate-900 shadow-xs transition cursor-pointer" aria-expanded="false" aria-haspopup="true">
              <span id="current-region-flag">🌍</span>
              <span id="current-region-label" class="font-black text-slate-900">Todas las regiones</span>
              <i data-lucide="chevron-down" class="w-3.5 h-3.5 stroke-[2.5] text-slate-600 transition-transform duration-200" id="region-dropdown-arrow"></i>
            </button>

            <!-- MENÚ DESPLEGABLE FLOTANTE -->
            <div id="region-dropdown-menu" class="hidden absolute right-0 mt-2 w-64 max-h-80 overflow-y-auto bg-white rounded-2xl shadow-[0_12px_30px_rgba(0,0,0,0.15)] border border-slate-200 p-1.5 z-50 transition-all">
              {region_dropdown_items_html}
            </div>
          </div>
        </div>

        <div id="franchiseMap"></div>
        
        <!-- Leyenda del mapa -->
        <div class="flex items-center gap-3 sm:gap-6 px-3 py-2.5 mt-2 text-[11px] font-bold text-slate-600 flex-wrap border-t border-slate-100">
          <span class="text-slate-400 uppercase">Tipología:</span>
          <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-full bg-[#0284c7]"></span> Cadena Multiclub</span>
          <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-full bg-[#2563eb]"></span> Red Corporativa</span>
          <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-full bg-[#4f46e5]"></span> Franquicia</span>
          <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-full bg-[#059669]"></span> Automatizado 24/7</span>
          <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-full bg-[#9333ea]"></span> Boutique Lujo</span>
        </div>
      </div>

      <!-- VISTA GRID (TARJETAS) -->
      <div id="gridView" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
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
              <div class="w-12 h-12 rounded-2xl bg-[#f2920b]/20 text-[#f2920b] flex items-center justify-center mb-6">
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

            <a href="../camaras/" class="inline-flex items-center justify-between px-6 py-3.5 rounded-2xl bg-[#76d3f6] hover:bg-[#f2920b] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition group">
              <span>Ver Tecnología de Cámaras Save My Play</span>
              <i data-lucide="arrow-right" class="w-4 h-4 group-hover:translate-x-1 transition-transform"></i>
            </a>
          </div>

        </div>

      </div>
    </section>

  </main>

  <!-- FOOTER -->
  <footer class="bg-slate-950 text-slate-400 py-12 border-t border-slate-800 text-xs">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col md:flex-row items-center justify-between gap-6">
      <div class="flex items-center gap-3">
        <img src="../assets/images/coolpadel-mascot-hd.png" alt="CoolPadel Studios" class="h-8 w-auto">
        <span class="font-heading font-black text-white text-sm">CoolPadel Studios</span>
        <span class="text-slate-600">|</span>
        <span>Censo Internacional de Franquicias y Cadenas de Pádel</span>
      </div>

      <div class="flex items-center gap-6">
        <a href="../" class="hover:text-white transition">Inicio</a>
        <a href="../#llaveros" class="hover:text-white transition">Llaveros</a>
        <a href="../camaras/" class="hover:text-white transition">Cámaras Pistas</a>
        <a href="../blog/" class="hover:text-white transition">Blog</a>
        <button onclick="openOnboardingModal()" class="text-[#f2920b] hover:underline font-bold">Alta de Franquicia</button>
        <a href="https://wa.me/34680317486" target="_blank" class="text-white hover:underline font-bold">WhatsApp: +34 680 31 74 86</a>
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
          <div class="w-10 h-10 rounded-2xl bg-[#f2920b]/20 text-[#f2920b] flex items-center justify-center shrink-0">
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
        <h2 id="drawerTitle" class="font-heading font-black text-2xl sm:text-3xl text-slate-950"></h2>
        <p id="drawerCity" class="text-xs font-semibold text-slate-500 flex items-center gap-1"></p>
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
    <div class="p-5 border-t border-slate-200/90 bg-slate-50 flex items-center justify-between gap-3">
      <a id="drawerWebBtn" href="#" target="_blank" class="inline-flex items-center gap-1.5 px-4 py-2.5 rounded-xl bg-white border border-slate-200 hover:bg-slate-100 text-slate-800 text-xs font-bold transition">
        <span>Visitar Web Oficial</span>
        <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
      </a>

      <a id="drawerWaBtn" href="#" target="_blank" class="inline-flex items-center gap-1.5 px-5 py-2.5 rounded-xl bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 text-xs font-heading font-black uppercase tracking-wider transition">
        <span>Consultar con Javier</span>
        <i data-lucide="message-circle" class="w-3.5 h-3.5 stroke-[2.5]"></i>
      </a>
    </div>

  </div>

  <!-- MODAL ONBOARDING / RECLAMAR FICHA (4 PASOS B2B) -->
  <div id="onboardingModalOverlay" class="fixed inset-0 bg-slate-950/80 backdrop-blur-sm z-50 transition-opacity opacity-0 pointer-events-none flex items-center justify-center p-3 sm:p-6" onclick="closeOnboardingModal()">
    <div id="onboardingModal" class="bg-white w-full max-w-2xl max-h-[94vh] rounded-3xl shadow-2xl border border-slate-200 overflow-hidden flex flex-col transform scale-95 transition-transform duration-300" onclick="event.stopPropagation()">
      
      <!-- Modal Header -->
      <div class="p-6 bg-slate-900 text-white flex items-start justify-between border-b border-slate-800 shrink-0">
        <div>
          <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-[#f2920b]/20 text-[#f2920b] text-[11px] font-bold uppercase tracking-wider mb-2">
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
            <a id="successWaBtn" href="#" target="_blank" class="px-5 py-2.5 rounded-xl bg-[#f2920b] hover:bg-[#d97f08] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition inline-flex items-center gap-2">
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
    let markersById = {{}};

    let selectedFranchises = [];
    let currentStep = 1;
    let currentDrawerId = null;

    const WEBHOOK_URL = 'https://script.google.com/macros/s/AKfycbxnF9JmVrikeAW7PdLc02r_1kkuSJVz1Ncl71ZeVGT37H0ji5DQ3DVw60122pcuYnxCgA/exec';

    // Bounding boxes / centros y zoom por región geográfica
    const REGION_BOUNDS = {{
      'all': {{ center: [46.0, 4.0], zoom: 4 }},
      'GB': {{ center: [53.5, -2.0], zoom: 6 }},
      'ES': {{ center: [40.2, -3.7], zoom: 6 }},
      'FR': {{ center: [46.6, 2.3], zoom: 6 }},
      'IT': {{ center: [42.5, 12.5], zoom: 6 }},
      'NL': {{ center: [52.1, 5.3], zoom: 7 }},
      'DE': {{ center: [50.5, 10.0], zoom: 6 }},
      'SE': {{ center: [60.1, 16.0], zoom: 5 }},
      'PT': {{ center: [39.5, -8.0], zoom: 7 }},
      'US': {{ center: [37.0, -96.0], zoom: 4 }},
      'MX': {{ center: [20.0, -99.0], zoom: 4 }},
      'AE': {{ center: [24.5, 54.5], zoom: 7 }},
      'ZA': {{ center: [-29.0, 25.0], zoom: 5 }}
    }};

    // Inicializar mapa con Esri World Street Map (nombres locales, sin API key, sin contorno de costa)
    function initMap() {{
      if (map) return;
      
      map = L.map('franchiseMap', {{
        center: [48.0, 5.0],
        zoom: 4,
        scrollWheelZoom: false
      }});

      L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{{z}}/{{y}}/{{x}}', {{
        attribution: 'Tiles &copy; Esri &mdash; Fuentes: Esri, DeLorme, NAVTEQ, USGS, Intermap, iPC, METI, TomTom | CoolPadel Studios',
        maxZoom: 18
      }}).addTo(map);

      markersLayer = L.layerGroup().addTo(map);
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
        markersById[f.id] = marker;
        markersLayer.addLayer(marker);
      }});
    }}

    // Vistas de mapa
    function resetMapView() {{ map.setView([46.0, 4.0], 4); }}

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
    }});

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

      applyFilters();

      // Animación fluida de zoom al país/región seleccionado
      if (map && REGION_BOUNDS[code]) {{
        map.flyTo(REGION_BOUNDS[code].center, REGION_BOUNDS[code].zoom, {{
          animate: true,
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

        const textToSearch = `${{f.nombre}} ${{f.pais}} ${{f.ciudad_sede}} ${{f.tagline}} ${{f.modelo}}`.toLowerCase();
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
      const mapContainer = document.getElementById('mapContainer');
      const viewGridBtn = document.getElementById('viewGridBtn');
      const viewTableBtn = document.getElementById('viewTableBtn');

      if (view === 'grid') {{
        gridView.classList.remove('hidden');
        tableView.classList.add('hidden');
        mapContainer.classList.remove('hidden');
        
        viewGridBtn.className = "px-4 py-2.5 rounded-xl text-xs font-bold font-heading uppercase tracking-wider bg-slate-900 text-white transition flex items-center gap-1.5 shadow-xs";
        viewTableBtn.className = "px-4 py-2.5 rounded-xl text-xs font-bold font-heading uppercase tracking-wider bg-slate-100 text-slate-700 hover:bg-slate-200 transition flex items-center gap-1.5";
        
        setTimeout(() => {{ if (map) map.invalidateSize(); }}, 100);
      }} else {{
        gridView.classList.add('hidden');
        tableView.classList.remove('hidden');
        mapContainer.classList.add('hidden');

        viewGridBtn.className = "px-4 py-2.5 rounded-xl text-xs font-bold font-heading uppercase tracking-wider bg-slate-100 text-slate-700 hover:bg-slate-200 transition flex items-center gap-1.5";
        viewTableBtn.className = "px-4 py-2.5 rounded-xl text-xs font-bold font-heading uppercase tracking-wider bg-slate-900 text-white transition flex items-center gap-1.5 shadow-xs";
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
                   class="w-full py-3 rounded-xl bg-[#f2920b] hover:bg-[#d97f08] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition text-center flex items-center justify-center gap-1.5 shadow-xs">
                  <i data-lucide="file-text" class="w-4 h-4"></i>
                  <span>Solicitar Dossier de Inversión</span>
                </a>
                <a href="${{f.web}}" target="_blank" class="w-full py-2.5 rounded-xl bg-white border border-slate-300 hover:bg-slate-100 text-slate-700 font-bold text-xs transition text-center flex items-center justify-center gap-1">
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
    // SLIDE-OVER DRAWER LOGIC
    // =========================================================================
    function openDrawer(id) {{
      const f = FRANQUICIAS.find(item => item.id === id);
      if (!f) return;
      currentDrawerId = id;

      // Zoom dinámico fluido sobre la coordenada de la cadena en el mapa
      if (f.coords && f.coords.length === 2 && map) {{
        map.flyTo(f.coords, 8, {{ animate: true, duration: 1.2 }});
        if (markersById && markersById[id]) {{
          markersById[id].openPopup();
        }}
      }}

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

      // Sedes
      const sedesList = document.getElementById('drawerSedes');
      sedesList.innerHTML = f.sedes_principales.map(s => `<li class="flex items-start gap-2"><span class="text-[#f2920b] font-bold">•</span><span>${{s}}</span></li>`).join('');

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

    // Inicializar mapa al cargar
    document.addEventListener('DOMContentLoaded', function() {{
      initMap();
    }});
  </script>
</body>
</html>
"""
    return full_html


def main():
    target_dir = os.path.join(os.path.dirname(__file__), "franquicias-padel")
    os.makedirs(target_dir, exist_ok=True)
    target_file = os.path.join(target_dir, "index.html")

    html_content = render_html()
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Directorio de franquicias y cadenas generado con exito en: {target_file}")
    print(f"Total de entidades incluidas: {len(FRANQUICIAS)}")


if __name__ == "__main__":
    main()
