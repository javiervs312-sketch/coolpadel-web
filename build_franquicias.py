#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador Maestro del Directorio Global de Franquicias y Cadenas de Pádel (+1 Club)
para CoolPadel Studios (https://coolpadelstudios.com/franquicias-padel/).

Censo exhaustivo de 126 cadenas de clubes con varias sedes abiertas bajo el mismo nombre
y franquicias de pádel en más de 20 países:
Reino Unido, España, Francia, Italia, Portugal, Suecia, Noruega, Dinamarca, Finlandia,
Países Bajos, Bélgica, Alemania, Austria, Suiza, Estados Unidos, México, Chile, Argentina,
Brasil, Catar, Emiratos Árabes Unidos, Kuwait, Sudáfrica y Australia.
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


def render_html():
    total_franquicias = len(FRANQUICIAS)
    paises_unicos = len(set(f["pais"] for f in FRANQUICIAS))

    # Generación dinámica de botones de región con recuento exacto
    region_buttons_html = ""
    for reg_code, reg_label, reg_flag in REGIONES_CONFIG:
        if reg_code == "all":
            cnt = total_franquicias
            btn_cls = "filter-region-btn active px-3 py-1 rounded-lg text-xs font-bold bg-[#f2920b] text-slate-950 transition"
        else:
            cnt = sum(1 for f in FRANQUICIAS if f.get("region_filtro") == reg_code)
            btn_cls = "filter-region-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition"
        region_buttons_html += f'<button onclick="setRegionFilter(\'{reg_code}\')" class="{btn_cls}" data-region="{reg_code}">{reg_flag} {reg_label} ({cnt})</button>\n'

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

        cards_html += f"""
        <article class="franchise-card group bg-white rounded-3xl p-6 border border-slate-200/90 shadow-xs hover:shadow-xl hover:border-[#f2920b]/40 transition-all duration-300 flex flex-col justify-between cursor-pointer"
                 data-id="{fid}"
                 data-region="{region_f}"
                 data-model="{tipo_cat}"
                 data-search="{nombre.lower()} {pais.lower()} {ciudad.lower()} {software.lower()} {modelo.lower()}"
                 onclick="openDrawer('{fid}')">
          <div>
            <div class="flex items-start justify-between gap-3 mb-4">
              <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold border {badge_cls}">
                {modelo}
              </span>
              <span class="text-2xl" title="{pais}">{bandera}</span>
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
        table_rows_html += f"""
        <tr class="hover:bg-slate-50/80 transition-colors cursor-pointer border-b border-slate-200/70" onclick="openDrawer('{f['id']}')">
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
  <title>Directorio de Cadenas de Clubs y Franquicias de Pádel (+1 Club) | CoolPadel Studios</title>
  <meta name="description" content="Directorio y mapa de las mayores cadenas de clubs con varias sedes abiertas bajo el mismo nombre y franquicias de pádel (+1 club). Datos de sedes, modelos, software e inversión.">
  <meta name="author" content="CoolPadel Studios">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://coolpadelstudios.com/franquicias-padel/">
  <link rel="icon" type="image/png" href="../assets/images/favicon_transparente.png?v=transp3">
  <link rel="apple-touch-icon" sizes="180x180" href="../assets/images/favicon_transparente.png?v=transp3">
  <meta name="theme-color" content="#0b1626">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:locale" content="es_ES">
  <meta property="og:site_name" content="CoolPadel Studios">
  <meta property="og:url" content="https://coolpadelstudios.com/franquicias-padel/">
  <meta property="og:title" content="Directorio de Cadenas de Clubs y Franquicias de Pádel (+1 Club) | Censo Mundial">
  <meta property="og:description" content="Guía de operadores multi-club y cadenas con varias sedes abiertas bajo el mismo nombre en España, Reino Unido, Europa, América y Golfo Pérsico.">
  <meta property="og:image" content="https://coolpadelstudios.com/assets/images/savemyplay-1.jpg">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Directorio de Cadenas de Clubs y Franquicias de Pádel | CoolPadel Studios">
  <meta name="twitter:description" content="Censo internacional de 153 cadenas de pádel con varias sedes bajo el mismo nombre y franquicias en más de 20 países.">
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

  <!-- HEADER OFICIAL -->
  <header class="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-slate-200/80 shadow-xs">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 sm:h-20 flex items-center justify-between">
      <a href="../" class="flex items-center gap-2 group">
        <img src="../assets/images/coolpadel-mascot-hd.png" alt="Mascota CoolPadel Studios" class="h-8 sm:h-11 w-auto object-contain">
        <img src="../assets/images/coolpadel-typography-hd.png" alt="CoolPadel Studios" class="h-5 sm:h-7 w-auto object-contain">
      </a>
      
      <div class="flex items-center gap-2.5 sm:gap-6">
        <a href="../#llaveros" class="hidden md:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition">Llaveros</a>
        <a href="../camaras/" class="hidden md:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition">Cámaras Pistas</a>
        <a href="../blog/" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition">Blog</a>
        <span class="inline-block px-3 py-1 rounded-full bg-[#f2920b]/15 text-[#f2920b] font-heading font-black text-[11px] sm:text-xs uppercase tracking-wider border border-[#f2920b]/20">
          Directorio Global
        </span>
        
        <a href="https://wa.me/34680317486?text=Hola%20Javier%2C%20estoy%20viendo%20el%20directorio%20global%20de%20cadenas%20de%20p%C3%A1del%20y%20me%20gustar%C3%ADa%20hacerte%20una%20consulta" target="_blank" class="inline-flex items-center gap-2 px-3.5 sm:px-5 py-2 sm:py-2.5 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs sm:text-sm tracking-wider uppercase transition shadow-sm hover:scale-105 active:scale-95">
          <span>Consultar</span>
          <i data-lucide="message-circle" class="w-3.5 h-3.5 stroke-[3]"></i>
        </a>
      </div>
    </div>
  </header>

  <!-- MAIN -->
  <main class="flex-1">

    <!-- HERO SECTION -->
    <section class="py-12 sm:py-16 bg-gradient-to-b from-white via-slate-50 to-[#f8fafc] border-b border-slate-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <!-- Breadcrumbs -->
        <nav class="flex items-center gap-2 text-xs font-bold text-slate-500 mb-6 uppercase tracking-wider">
          <a href="../" class="hover:text-slate-900 transition">Inicio</a>
          <span>/</span>
          <span class="text-[#f2920b]">Cadenas y Franquicias de Pádel</span>
        </nav>

        <div class="max-w-4xl space-y-4">
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-slate-900 text-white font-heading font-bold text-xs uppercase tracking-wider">
            <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
            <span>CENSO MUNDIAL B2B · CADENAS DE CLUBS CON EL MISMO NOMBRE Y FRANQUICIAS (+1 SEDE)</span>
          </div>

          <h1 class="font-heading font-black text-3xl sm:text-5xl lg:text-6xl text-slate-950 leading-[1.08] uppercase tracking-tight">
            Directorio de Cadenas de Clubs y Franquicias de Pádel
          </h1>

          <p class="text-base sm:text-xl text-slate-600 font-medium leading-relaxed">
            El censo internacional más exhaustivo para operadores y propietarios: <strong>{total_franquicias} cadenas de clubes con varios centros abiertos bajo el mismo nombre</strong> y franquicias analizadas en {paises_unicos} países. Sedes activas, requisitos de inversión, software de gestión y modelos de rentabilidad.
          </p>
        </div>

        <!-- KPI BANNER -->
        <div class="grid grid-cols-2 lg:grid-cols-4 gap-3.5 sm:gap-6 mt-8 sm:mt-10 pt-8 border-t border-slate-200/80">
          <div class="bg-white p-5 rounded-2xl border border-slate-200/80 shadow-xs">
            <span class="block text-xs font-bold uppercase tracking-wider text-slate-400 mb-1">Cadenas / Franquicias</span>
            <span class="font-heading font-black text-3xl sm:text-4xl text-slate-950">{total_franquicias}</span>
            <span class="text-xs text-slate-500 font-medium">Con +1 club abierto</span>
          </div>
          
          <div class="bg-white p-5 rounded-2xl border border-slate-200/80 shadow-xs">
            <span class="block text-xs font-bold uppercase tracking-wider text-slate-400 mb-1">Pistas Totales</span>
            <span class="font-heading font-black text-3xl sm:text-4xl text-slate-950">+8.500</span>
            <span class="text-xs text-slate-500 font-medium">Bajo gestión analizada</span>
          </div>

          <div class="bg-white p-5 rounded-2xl border border-slate-200/80 shadow-xs">
            <span class="block text-xs font-bold uppercase tracking-wider text-slate-400 mb-1">Presencia Global</span>
            <span class="font-heading font-black text-3xl sm:text-4xl text-slate-950">{paises_unicos} Países</span>
            <span class="text-xs text-slate-500 font-medium">Europa, América, Oriente Medio, África y Oceanía</span>
          </div>

          <div class="bg-white p-5 rounded-2xl border border-slate-200/80 shadow-xs">
            <span class="block text-xs font-bold uppercase tracking-wider text-slate-400 mb-1">Tipologías</span>
            <span class="font-heading font-black text-3xl sm:text-4xl text-[#f2920b]">Mismo Nombre</span>
            <span class="text-xs text-slate-500 font-medium">Cadenas multiclub y franquicias</span>
          </div>
        </div>

      </div>
    </section>

    <!-- INTERACTIVE SECTION -->
    <section class="py-10 sm:py-14 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- CONTROLES Y FILTROS -->
      <div class="bg-white rounded-3xl p-5 sm:p-7 border border-slate-200/90 shadow-sm mb-8 space-y-5">
        
        <!-- Barra de búsqueda y vista -->
        <div class="flex flex-col md:flex-row gap-4 items-stretch md:items-center justify-between">
          <div class="relative flex-1">
            <i data-lucide="search" class="w-5 h-5 text-slate-400 absolute left-4 top-1/2 -translate-y-1/2"></i>
            <input type="text" id="searchInput" placeholder="Buscar por cadena, club, ciudad, país o software (ej. PadelStars, The Padel Hub, Playtomic, Spector, Arenal, Pàdel 7)..."
                   class="w-full pl-12 pr-4 py-3.5 rounded-2xl bg-slate-50 border border-slate-200 text-slate-900 placeholder-slate-400 font-medium text-sm focus:outline-none focus:ring-2 focus:ring-[#f2920b] focus:bg-white transition"
                   oninput="applyFilters()">
          </div>

          <div class="flex items-center gap-2 self-end md:self-auto">
            <button id="viewGridBtn" onclick="switchView('grid')" class="px-4 py-2.5 rounded-xl text-xs font-bold font-heading uppercase tracking-wider bg-slate-900 text-white transition flex items-center gap-1.5 shadow-xs">
              <i data-lucide="layout-grid" class="w-4 h-4"></i>
              <span>Tarjetas & Mapa</span>
            </button>
            <button id="viewTableBtn" onclick="switchView('table')" class="px-4 py-2.5 rounded-xl text-xs font-bold font-heading uppercase tracking-wider bg-slate-100 text-slate-700 hover:bg-slate-200 transition flex items-center gap-1.5">
              <i data-lucide="table" class="w-4 h-4"></i>
              <span>Tabla Comparativa</span>
            </button>
          </div>
        </div>

        <!-- Filtros por Región/País y Categoría -->
        <div class="flex flex-col gap-4 pt-3 border-t border-slate-100">
          
          <!-- Filtro Región / País -->
          <div class="flex items-center gap-1.5 flex-wrap">
            <span class="text-xs font-bold uppercase text-slate-400 mr-1 flex items-center gap-1">
              <i data-lucide="globe" class="w-3.5 h-3.5"></i>
              <span>Región:</span>
            </span>
            {region_buttons_html}
          </div>

          <!-- Filtro Modelo / Tipo de Operador -->
          <div class="flex items-center gap-1.5 flex-wrap">
            <span class="text-xs font-bold uppercase text-slate-400 mr-1 flex items-center gap-1">
              <i data-lucide="tag" class="w-3.5 h-3.5"></i>
              <span>Tipo de Operador:</span>
            </span>
            <button onclick="setModelFilter('all')" class="filter-model-btn active px-3 py-1 rounded-lg text-xs font-bold bg-slate-900 text-white transition" data-model="all">Todos</button>
            <button onclick="setModelFilter('cadena')" class="filter-model-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-model="cadena">Cadena Multiclub (Mismo Nombre)</button>
            <button onclick="setModelFilter('corporativo')" class="filter-model-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-model="corporativo">Red Corporativa Propia</button>
            <button onclick="setModelFilter('franquicia')" class="filter-model-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-model="franquicia">Franquicia Llave en Mano</button>
            <button onclick="setModelFilter('automatizado')" class="filter-model-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-model="automatizado">Club 100% Automatizado 24/7</button>
            <button onclick="setModelFilter('boutique')" class="filter-model-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-model="boutique">Boutique & Ultra-Lujo</button>
            <button onclick="setModelFilter('licencia')" class="filter-model-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-100 text-slate-600 hover:bg-slate-200 transition" data-model="licencia">Academia / Pro-Shop</button>
          </div>

        </div>

        <!-- Contador de resultados -->
        <div class="flex items-center justify-between text-xs font-semibold text-slate-500 pt-2 border-t border-slate-100">
          <span id="resultsCount">Mostrando {total_franquicias} cadenas y franquicias</span>
          <span class="text-slate-400 hidden sm:inline">Haz clic en cualquier tarjeta o chincheta del mapa para ver el dossier completo</span>
        </div>

      </div>

      <!-- MAPA INTERACTIVO -->
      <div id="mapContainer" class="bg-white p-3 sm:p-4 rounded-3xl border border-slate-200/90 shadow-sm mb-10 relative">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between px-3 py-2 mb-2 gap-2">
          <div class="flex items-center gap-2">
            <span class="w-2.5 h-2.5 rounded-full bg-[#f2920b]"></span>
            <h2 class="font-heading font-black text-sm sm:text-base text-slate-900 uppercase tracking-wider">
              Mapa Mundial de Sedes Principales & Cadenas
            </h2>
          </div>
          <div class="flex items-center gap-1.5 text-xs font-bold flex-wrap">
            <button onclick="resetMapView()" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 transition">
              Mundo
            </button>
            <button onclick="zoomToUK()" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 transition">
              🇬🇧 UK
            </button>
            <button onclick="zoomToSpain()" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 transition">
              🇪🇸 España
            </button>
            <button onclick="zoomToFrance()" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 transition">
              🇫🇷 Francia
            </button>
            <button onclick="zoomToItaly()" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 transition">
              🇮🇹 Italia
            </button>
            <button onclick="zoomToBenelux()" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 transition">
              🇳🇱 Benelux
            </button>
            <button onclick="zoomToDACH()" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 transition">
              🇩🇪 DACH
            </button>
            <button onclick="zoomToNordics()" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 transition">
              🇸🇪 Nórdicos
            </button>
            <button onclick="zoomToUSA()" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 transition">
              🇺🇸 EE.UU.
            </button>
            <button onclick="zoomToLatam()" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 transition">
              🇲🇽 Latam
            </button>
            <button onclick="zoomToMiddleEast()" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 transition">
              🇦🇪 Oriente Medio
            </button>
            <button onclick="zoomToSouthAfrica()" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 transition">
              🇿🇦 Sudáfrica
            </button>
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
          <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-full bg-[#9333ea]"></span> Boutique / Lujo</span>
          <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-full bg-[#d97706]"></span> Academia / Pro-Shop</span>
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
        <a href="https://wa.me/34680317486" target="_blank" class="text-[#f2920b] hover:underline font-bold">WhatsApp: +34 680 31 74 86</a>
      </div>
    </div>
  </footer>

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

  <!-- SCRIPT DE FILTRADO, MAPA Y MODAL -->
  <script>
    lucide.createIcons();

    const FRANQUICIAS = {json.dumps(FRANQUICIAS, ensure_ascii=False)};

    let currentRegion = 'all';
    let currentModel = 'all';
    let currentView = 'grid';
    let map = null;
    let markersLayer = null;

    // Inicializar mapa
    function initMap() {{
      if (map) return;
      
      map = L.map('franchiseMap', {{
        center: [48.0, 5.0],
        zoom: 4,
        scrollWheelZoom: false
      }});

      L.tileLayer('https://{{s}}.basemaps.cartocdn.com/rastertiles/voyager/{{z}}/{{x}}/{{y}}{{r}}.png', {{
        attribution: '&copy; <a href="https://carto.com/">CARTO</a> | CoolPadel Studios',
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
            <button onclick="openDrawer('${{f.id}}')" style="width: 100%; background: #0f172a; color: #ffffff; border: none; padding: 6px 10px; border-radius: 8px; font-size: 11px; font-weight: 800; cursor: pointer;">
              Ver Dossier Completo →
            </button>
          </div>
        `;

        const marker = L.marker(f.coords, {{ icon: customIcon }})
          .bindPopup(popupContent);
        markersLayer.addLayer(marker);
      }});
    }}

    function resetMapView() {{
      map.setView([35.0, 10.0], 3);
    }}

    function zoomToUK() {{
      map.setView([53.0, -1.8], 6);
    }}

    function zoomToSpain() {{
      map.setView([40.2, -3.7], 6);
    }}

    function zoomToFrance() {{
      map.setView([46.5, 2.5], 6);
    }}

    function zoomToItaly() {{
      map.setView([42.5, 12.5], 6);
    }}

    function zoomToBenelux() {{
      map.setView([51.5, 4.5], 7);
    }}

    function zoomToDACH() {{
      map.setView([48.5, 11.0], 6);
    }}

    function zoomToNordics() {{
      map.setView([60.0, 15.0], 5);
    }}

    function zoomToUSA() {{
      map.setView([37.0, -95.0], 4);
    }}

    function zoomToLatam() {{
      map.setView([-15.0, -60.0], 3);
    }}

    function zoomToMiddleEast() {{
      map.setView([25.0, 50.0], 5);
    }}

    function zoomToSouthAfrica() {{
      map.setView([-29.0, 24.0], 5);
    }}

    function setRegionFilter(region) {{
      currentRegion = region;
      document.querySelectorAll('.filter-region-btn').forEach(btn => {{
        if (btn.dataset.region === region) {{
          btn.classList.add('bg-[#f2920b]', 'text-slate-950');
          btn.classList.remove('bg-slate-100', 'text-slate-600');
        }} else {{
          btn.classList.remove('bg-[#f2920b]', 'text-slate-950');
          btn.classList.add('bg-slate-100', 'text-slate-600');
        }}
      }});
      applyFilters();
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
        
        const textToSearch = `${{f.nombre}} ${{f.pais}} ${{f.ciudad_sede}} ${{f.software}} ${{f.tagline}} ${{f.modelo}}`.toLowerCase();
        const matchQuery = !query || textToSearch.includes(query);

        const isVisible = matchRegion && matchModel && matchQuery;

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

    function openDrawer(id) {{
      const f = FRANQUICIAS.find(item => item.id === id);
      if (!f) return;

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

    // Cerrar con Escape
    document.addEventListener('keydown', function(e) {{
      if (e.key === 'Escape') closeDrawer();
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

    print(f"Directorio de franquicias y cadenas generado con éxito en: {target_file}")
    print(f"Total de entidades incluidas: {len(FRANQUICIAS)}")


if __name__ == "__main__":
    main()
