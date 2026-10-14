#!/usr/bin/env python3
"""
Generador de la página de Blog & Newsletter de CoolPadel Studios (coolpadelstudios.com/blog/).
Incluye el Reportaje de la Industria 2026 para descargar y los artículos de la Newsletter de Javier Villoria en LinkedIn.
"""
import os

def generate_blog_html():
    html = """<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Blog & Newsletter de la Industria del Pádel | Javier Villoria · CoolPadel</title>
  <meta name="description" content="Artículos, análisis de startups deportivas y descarga exclusiva del Informe de la Industria del Pádel 2026 por Javier Villoria (CoolPadel Studios).">
  <meta name="keywords" content="industria del padel, padel startups, padel world summit 2026, informe industria padel 2026, javier villoria, coolpadel, playtomic, save my play, camaras padel">
  <meta name="author" content="Javier Villoria">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <link rel="canonical" href="https://coolpadelstudios.com/blog/">
  <link rel="icon" type="image/png" href="../assets/images/favicon_transparente.png?v=transp3">
  <link rel="apple-touch-icon" sizes="180x180" href="../assets/images/favicon_transparente.png?v=transp3">
  <meta name="theme-color" content="#0b1626">

  <!-- Open Graph / LinkedIn / WhatsApp -->
  <meta property="og:type" content="website">
  <meta property="og:locale" content="es_ES">
  <meta property="og:site_name" content="CoolPadel Blog">
  <meta property="og:url" content="https://coolpadelstudios.com/blog/">
  <meta property="og:title" content="Blog & Newsletter de la Industria del Pádel | Javier Villoria">
  <meta property="og:description" content="Análisis directo de startups, tecnología en pistas y descarga gratuita del Informe de la Industria del Pádel 2026.">
  <meta property="og:image" content="https://coolpadelstudios.com/assets/images/foto-reportaje.jpg">

  <!-- Twitter / X -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Blog & Newsletter de la Industria del Pádel | Javier Villoria">
  <meta name="twitter:description" content="Análisis directo de startups, tecnología en pistas y descarga gratuita del Informe de la Industria del Pádel 2026.">
  <meta name="twitter:image" content="https://coolpadelstudios.com/assets/images/foto-reportaje.jpg">

  <!-- Tailwind CSS & Lucide Icons -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/lucide@latest"></script>

  <!-- Google Fonts: Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">

  <!-- Microsoft Clarity -->
  <script type="text/javascript">
    (function(c,l,a,r,i,t,y){
      c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
      t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
      y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    })(window, document, "clarity", "script", "q7p8g52y9e");
  </script>

  <style>
    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .font-heading {
      font-family: 'Plus Jakarta Sans', sans-serif;
    }
  </style>

  <!-- Schema.org JSON-LD para GEO y Google -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "Blog",
        "@id": "https://coolpadelstudios.com/blog/#blog",
        "name": "CoolPadel Blog & Newsletter",
        "url": "https://coolpadelstudios.com/blog/",
        "description": "Análisis del mercado del pádel, tendencias de negocio, tecnología de pistas e informes exclusivos por Javier Villoria.",
        "publisher": {
          "@type": "Organization",
          "name": "CoolPadel Studios",
          "url": "https://coolpadelstudios.com"
        }
      },
      {
        "@type": "Person",
        "@id": "https://coolpadelstudios.com/blog/#author",
        "name": "Javier Villoria Soleto",
        "jobTitle": "Director & Fundador",
        "worksFor": {
          "@type": "Organization",
          "name": "CoolPadel Studios"
        },
        "sameAs": [
          "https://www.linkedin.com/in/javier-villoria-soleto-606737298/"
        ]
      }
    ]
  }
  </script>
</head>
<body class="bg-white text-slate-900 antialiased selection:bg-[#f2920b] selection:text-slate-950">

  <!-- 1. TOP TICKER -->
  <div class="bg-slate-950 text-white text-xs sm:text-sm py-2 px-4 border-b border-slate-800">
    <div class="max-w-6xl mx-auto flex items-center justify-between">
      <a href="../" class="inline-flex items-center gap-2 text-neutral-300 hover:text-white transition font-medium">
        <i data-lucide="arrow-left" class="w-4 h-4 text-[#f2920b]"></i>
        <span>Volver a la tienda de Llaveros de Pádel</span>
      </a>
      <a href="https://www.linkedin.com/in/javier-villoria-soleto-606737298/" target="_blank" class="hidden sm:inline-flex items-center gap-1.5 text-neutral-300 hover:text-[#76d3f6] transition font-medium">
        <span>Highlights by CoolPadel en LinkedIn</span>
        <i data-lucide="arrow-up-right" class="w-3.5 h-3.5"></i>
      </a>
    </div>
  </div>

  <!-- 2. NAVBAR -->
  <header class="sticky top-0 z-40 bg-white border-b border-slate-200 shadow-sm">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 h-16 sm:h-18 flex items-center justify-between">
      
      <!-- LOGO -->
      <a href="../" class="flex items-center gap-2.5 group">
        <img src="../assets/images/coolpadel-mascot-hd.png" alt="Mascota CoolPadel" style="height: 42px; width: auto;" class="object-contain group-hover:scale-105 transition">
        <img src="../assets/images/coolpadel-typography-hd.png" alt="CoolPadel" style="height: 24px; width: auto;" class="object-contain">
      </a>

      <!-- NAVEGACIÓN -->
      <nav class="flex items-center gap-4 sm:gap-6">
        <a href="../#llaveros" class="font-heading font-black text-xs sm:text-sm uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition">
          Llaveros
        </a>
        <a href="./" class="font-heading font-black text-xs sm:text-sm uppercase tracking-wider text-[#f2920b] border-b-2 border-[#f2920b] pb-0.5">
          Blog
        </a>
        <a href="https://wa.me/34680317486?text=Hola%20Javier" target="_blank" class="inline-flex items-center gap-1.5 px-4 py-2 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition shadow-sm hover:scale-105">
          <span>Contacto</span>
          <i data-lucide="arrow-up-right" class="w-3.5 h-3.5 stroke-[3]"></i>
        </a>
      </nav>

    </div>
  </header>

  <!-- 3. HERO DEL BLOG -->
  <section class="py-12 sm:py-16 bg-gradient-to-b from-slate-50 to-white border-b border-slate-200">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 text-center space-y-4">
      
      <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-slate-100 border border-slate-200 text-slate-700 text-xs font-bold uppercase tracking-wider">
        <span class="w-2 h-2 rounded-full bg-[#f2920b]"></span>
        <span>Análisis, Startups y Tendencias de Pádel</span>
      </div>

      <h1 class="text-3xl sm:text-5xl font-black font-heading text-slate-950 uppercase tracking-tight leading-tight">
        CoolPadel Blog & Newsletter
      </h1>

      <p class="text-base sm:text-lg text-slate-600 max-w-2xl mx-auto font-medium leading-relaxed">
        Reflexiones directas sobre la industria del pádel, análisis de software para clubes, tecnología de pista e informes exclusivos. Sin rodeos y de tú a tú.
      </p>

      <!-- AUTOR CHIP -->
      <div class="pt-2 flex items-center justify-center gap-3">
        <div class="flex items-center gap-3 px-4 py-2 rounded-2xl bg-white border border-slate-200 shadow-sm">
          <div class="w-10 h-10 rounded-full bg-[#f2920b] text-slate-950 font-black flex items-center justify-center text-sm font-heading">
            JV
          </div>
          <div class="text-left">
            <div class="flex items-center gap-1.5">
              <span class="font-bold text-sm text-slate-950">Javier Villoria</span>
              <a href="https://www.linkedin.com/in/javier-villoria-soleto-606737298/" target="_blank" class="text-sky-600 hover:text-sky-700" title="Ver perfil de LinkedIn">
                <i data-lucide="linkedin" class="w-4 h-4"></i>
              </a>
            </div>
            <span class="text-xs text-slate-500 font-medium">Fundador de CoolPadel Studios</span>
          </div>
        </div>
      </div>

      <div class="pt-2 text-xs font-bold text-slate-400 uppercase tracking-widest">
        Not AI-written · Not sponsored · Straight to the point
      </div>

    </div>
  </section>

  <!-- 4. BLOQUE 1: REPORTAJE OFICIAL INDUSTRIA 2026 (DESCARGA PDF) -->
  <section class="py-12 sm:py-16 bg-white border-b border-slate-200">
    <div class="max-w-6xl mx-auto px-4 sm:px-6">
      
      <div class="bg-gradient-to-br from-slate-900 to-slate-950 rounded-3xl p-6 sm:p-10 text-white shadow-2xl border border-slate-800 grid md:grid-cols-12 gap-8 items-center">
        
        <!-- FOTO PORTADA INFORME -->
        <div class="md:col-span-5 aspect-[16/11] rounded-2xl overflow-hidden border border-slate-700 shadow-xl relative group">
          <img src="../assets/images/foto-reportaje.jpg" alt="Informe Oficial Industria del Padel 2026" class="w-full h-full object-cover group-hover:scale-105 transition duration-700">
          <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent"></div>
          <span class="absolute bottom-3 left-3 text-[11px] font-black uppercase tracking-wider px-3 py-1 rounded-full bg-[#f2920b] text-slate-950 shadow-md">
            Documento Técnico 2026
          </span>
        </div>

        <!-- CONTENIDO Y DESCARGA -->
        <div class="md:col-span-7 space-y-4">
          <div class="space-y-2">
            <span class="text-[#76d3f6] font-heading font-black text-xs uppercase tracking-wider">
              Informe Exclusivo en PDF
            </span>
            <h2 class="text-2xl sm:text-3xl font-black font-heading text-white uppercase tracking-tight">
              El Negocio del Pádel: Informe 2026
            </h2>
            <p class="text-slate-300 text-sm sm:text-base font-normal leading-relaxed">
              Radiografía del mercado global de raqueta tras investigar a más de 116 empresas del sector: pistas inteligentes, software de reservas, adopción en clubes y expansión internacional.
            </p>
          </div>

          <!-- PUNTOS CLAVE -->
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 py-1 text-xs text-slate-300">
            <div class="flex items-center gap-2">
              <i data-lucide="check-circle" class="w-4 h-4 text-[#4bbb81] shrink-0"></i>
              <span>116 empresas analizadas</span>
            </div>
            <div class="flex items-center gap-2">
              <i data-lucide="check-circle" class="w-4 h-4 text-[#4bbb81] shrink-0"></i>
              <span>Ecosistema de reservas & Playtomic</span>
            </div>
            <div class="flex items-center gap-2">
              <i data-lucide="check-circle" class="w-4 h-4 text-[#4bbb81] shrink-0"></i>
              <span>Grabación en pista y tecnología IA</span>
            </div>
            <div class="flex items-center gap-2">
              <i data-lucide="check-circle" class="w-4 h-4 text-[#4bbb81] shrink-0"></i>
              <span>Tendencias de expansión en USA y Europa</span>
            </div>
          </div>

          <!-- FORMULARIO DESCARGA -->
          <div class="pt-3 border-t border-slate-800">
            <form onsubmit="handleBlogReportDownload(event)" class="flex flex-col sm:flex-row gap-2.5">
              <input type="email" id="blog-report-email" required placeholder="Tu correo electrónico..." class="flex-1 px-5 py-3 rounded-full bg-slate-800/90 border border-slate-700 text-white placeholder-slate-400 text-sm focus:outline-none focus:border-[#f2920b] transition">
              <button type="submit" id="blog-report-btn" class="inline-flex items-center justify-center gap-2 px-6 py-3 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition shadow-md hover:scale-105 shrink-0 cursor-pointer">
                <span>Descargar PDF</span>
                <i data-lucide="download" class="w-4 h-4 stroke-[3]"></i>
              </button>
            </form>
            <p id="blog-report-status" class="text-xs text-emerald-400 font-semibold mt-2 hidden">
              ✓ ¡Enlace de descarga listo! Abriendo el informe...
            </p>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- 5. BLOQUE 2: ARTÍCULOS DE LA NEWSLETTER EN LINKEDIN -->
  <section class="py-14 sm:py-20 bg-slate-50 border-b border-slate-200">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 space-y-10">
      
      <div class="text-center space-y-2">
        <h2 class="text-2xl sm:text-4xl font-black font-heading text-slate-950 uppercase tracking-tight">
          Artículos & Ediciones de la Newsletter
        </h2>
        <p class="text-slate-600 text-sm sm:text-base font-medium">
          Publicados originalmente por Javier Villoria en la serie "Highlights by CoolPadel" en LinkedIn.
        </p>
      </div>

      <!-- ARTÍCULO 1 (DESTACADO): PADEL WORLD SUMMIT 2026 -->
      <article class="bg-white rounded-3xl p-6 sm:p-9 border border-slate-200 shadow-lg space-y-6">
        
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-100 pb-4">
          <div class="flex items-center gap-2">
            <span class="px-3 py-1 rounded-full bg-orange-100 text-[#f2920b] text-xs font-bold uppercase tracking-wider">
              Highlights by CoolPadel #01
            </span>
            <span class="text-xs text-slate-400 font-semibold">11 Sep 2026</span>
          </div>
          <a href="https://www.linkedin.com/pulse/padel-world-summit-2026-startup-recap-javier-villoria-soleto-c7hle/" target="_blank" class="inline-flex items-center gap-1 text-xs font-bold text-sky-600 hover:text-sky-700">
            <span>Ver en LinkedIn Pulse</span>
            <i data-lucide="arrow-up-right" class="w-3.5 h-3.5"></i>
          </a>
        </div>

        <div class="space-y-3">
          <h3 class="text-2xl sm:text-3xl font-black font-heading text-slate-950 leading-tight">
            Padel World Summit 2026: Startup Recap
          </h3>
          <p class="text-sm font-semibold text-slate-500 italic">
            Por Javier Villoria Soleto · Not AI-written · Not sponsored · Straight to the point
          </p>
        </div>

        <!-- CUERPO DEL ARTÍCULO -->
        <div class="prose text-slate-700 text-sm sm:text-base leading-relaxed space-y-4">
          <p>
            Hablar con las 20 startups del Innovation Arena, una a una, es mi momento favorito del <strong>Padel World Summit</strong>. Funciona como un termómetro excelente para ver cómo está respirando realmente el sector.
          </p>
          <p>
            A nivel general, el mercado del pádel sigue en una fase muy temprana: está fragmentado, es local y es sumamente dinámico. Cada país tiene sus propios modelos de negocio y a veces cuesta ver la diferencia entre ellos. Sin embargo, en las regiones con más tradición, unas pocas marcas consolidadas dominan la escena. Y para una startup, intentar ganarles en su propio terreno es durísimo.
          </p>
          <p class="p-4 bg-slate-50 rounded-2xl border-l-4 border-[#f2920b] text-slate-900 font-medium">
            "En el mercado de sistemas de reservas, aunque tu software sea algo mejor que <strong>Playtomic</strong>, sustituirlos es extremadamente difícil. Por eso me gustó ver soluciones como <strong>CourtBrain™</strong> o <strong>aun we play</strong>. En lugar de intentar reemplazarlos, construyen por encima aportando un valor tangible y directo a los clubes."
          </p>
          <p>
            Con esto en mente, estas son mis startups favoritas del Innovation Arena en el PWS 2026:
          </p>

          <!-- STARTUPS DESTACADAS -->
          <div class="space-y-3.5 pt-1">
            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-1">
              <h4 class="font-bold text-slate-950 text-base flex items-center gap-2">
                <span class="w-2 h-2 rounded-full bg-[#f2920b]"></span>
                <strong>VAM-OS</strong>
              </h4>
              <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
                Ser propietario de un club significa lidiar con un caos de datos y múltiples plataformas a la vez. VAM-OS integra todos los sistemas que usan los clubes y centraliza los KPIs clave, ayudando con los estados financieros y reuniendo los datos necesarios para tomar mejores decisiones.
              </p>
            </div>

            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-1">
              <h4 class="font-bold text-slate-950 text-base flex items-center gap-2">
                <span class="w-2 h-2 rounded-full bg-[#76d3f6]"></span>
                <strong>Ballid</strong>
              </h4>
              <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
                Tengo la sensación de que las pelotas de pádel duran mucho menos que las de tenis: el bote decae a los pocos partidos. Ballid ha diseñado un presurizador de pelotas que se adapta a cualquier tubo comercial estándar. Es una pieza sencilla que usas con bomba externa (si no quieres bombear a mano, échale un ojo a Preserva).
              </p>
            </div>

            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-1">
              <h4 class="font-bold text-slate-950 text-base flex items-center gap-2">
                <span class="w-2 h-2 rounded-full bg-[#4bbb81]"></span>
                <strong>Infinite Athletic</strong>
              </h4>
              <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
                Un gran ejemplo de economía circular aplicada a los deportes de raqueta. Usando exclusivamente los botes de bolas y los cordajes de raqueta recogidos en clubes, producen ropa deportiva técnica que además vuelve a ser reciclable.
              </p>
            </div>
          </div>
        </div>

        <div class="pt-4 border-t border-slate-100 flex items-center justify-between flex-wrap gap-3">
          <span class="text-xs text-slate-500 font-semibold">📌 Suscríbete para recibir la próxima edición</span>
          <a href="https://www.linkedin.com/pulse/padel-world-summit-2026-startup-recap-javier-villoria-soleto-c7hle/" target="_blank" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition shadow-sm hover:scale-105">
            <span>Leer en LinkedIn Pulse</span>
            <i data-lucide="arrow-up-right" class="w-4 h-4 stroke-[3]"></i>
          </a>
        </div>

      </article>

      <!-- ARTÍCULO 2: CÁMARAS EN PISTAS DE PÁDEL -->
      <article class="bg-white rounded-3xl p-6 sm:p-9 border border-slate-200 shadow-lg space-y-5">
        
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-100 pb-4">
          <div class="flex items-center gap-2">
            <span class="px-3 py-1 rounded-full bg-emerald-100 text-emerald-800 text-xs font-bold uppercase tracking-wider">
              Tecnología en Pista · Save my Play
            </span>
          </div>
          <a href="../camaras/" class="inline-flex items-center gap-1 text-xs font-bold text-emerald-700 hover:text-emerald-800">
            <span>Leer análisis completo</span>
            <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
          </a>
        </div>

        <div class="space-y-2">
          <h3 class="text-2xl sm:text-3xl font-black font-heading text-slate-950 leading-tight">
            Muchos clubs en España se arrepienten de haber puesto cámaras en sus pistas
          </h3>
          <p class="text-sm sm:text-base text-slate-600 font-medium leading-relaxed">
            Las 3 decisiones clave que hacen que muchos clubes de tenis y pádel fracasen al poner cámaras: obras invasivas con zanjas y cableado, software propietario con suscripciones abusivas, y la ausencia de un botón directo para que el jugador se lleve sus jugadas al instante en el móvil.
          </p>
        </div>

        <div class="pt-2">
          <a href="../camaras/" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-slate-900 hover:bg-slate-800 text-white font-heading font-black text-xs uppercase tracking-wider transition shadow-sm hover:scale-105">
            <span>Leer artículo completo</span>
            <i data-lucide="arrow-right" class="w-4 h-4 stroke-[3]"></i>
          </a>
        </div>

      </article>

    </div>
  </section>

  <!-- 6. BLOQUE 3: CONECTA EN LINKEDIN -->
  <section class="py-14 sm:py-20 bg-white">
    <div class="max-w-4xl mx-auto px-4 sm:px-6">
      
      <div class="p-8 sm:p-12 rounded-3xl bg-gradient-to-r from-sky-900 to-slate-950 text-white shadow-xl text-center space-y-5 border border-sky-800/40">
        <div class="w-14 h-14 rounded-2xl bg-white/10 flex items-center justify-center mx-auto text-[#76d3f6]">
          <i data-lucide="linkedin" class="w-7 h-7"></i>
        </div>
        
        <div class="space-y-2 max-w-xl mx-auto">
          <h3 class="text-2xl sm:text-3xl font-black font-heading uppercase tracking-tight">
            Conecta con Javier Villoria en LinkedIn
          </h3>
          <p class="text-slate-300 text-sm sm:text-base font-normal leading-relaxed">
            Suscríbete a la newsletter <strong>Highlights by CoolPadel</strong> para recibir los próximos análisis de mercado, comparativas de producto y resúmenes de ferias internacionales directamente en tu feed.
          </p>
        </div>

        <div class="pt-2">
          <a href="https://www.linkedin.com/in/javier-villoria-soleto-606737298/" target="_blank" class="inline-flex items-center gap-2.5 px-7 py-3.5 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs sm:text-sm uppercase tracking-wider transition shadow-lg hover:scale-105">
            <span>Seguir en LinkedIn</span>
            <i data-lucide="arrow-up-right" class="w-4 h-4 stroke-[3]"></i>
          </a>
        </div>
      </div>

    </div>
  </section>

  <!-- 7. FOOTER OFICIAL -->
  <footer class="bg-slate-950 text-white py-12 border-t border-slate-800 text-xs">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 flex flex-col sm:flex-row items-center justify-between gap-6">
      <div class="flex items-center gap-3">
        <img src="../assets/images/coolpadel-mascot-hd.png" alt="CoolPadel" class="h-8 w-auto">
        <span class="font-bold text-slate-400">© 2026 CoolPadel Studios. Todos los derechos reservados.</span>
      </div>
      <div class="flex items-center gap-6 text-slate-400 font-semibold">
        <a href="../" class="hover:text-white transition">Llaveros de Pádel</a>
        <a href="./" class="hover:text-white transition">Blog</a>
        <a href="../camaras/" class="hover:text-white transition">Cámaras en Pistas</a>
        <a href="https://wa.me/34680317486?text=Hola%20Javier" target="_blank" class="hover:text-[#f2920b] transition">WhatsApp</a>
      </div>
    </div>
  </footer>

  <script>
    lucide.createIcons();

    // Descarga del Informe desde el Blog (con envío de email y descarga del archivo)
    async function handleBlogReportDownload(e) {
      e.preventDefault();
      const email = document.getElementById('blog-report-email').value;
      const btn = document.getElementById('blog-report-btn');
      const status = document.getElementById('blog-report-status');

      btn.disabled = true;
      btn.innerHTML = '<span>Generando...</span>';

      try {
        // Enviar al webhook de Google Apps Script si está disponible
        fetch('https://script.google.com/macros/s/AKfycbzTf3B5WlQo-c_9G9j5M_LwXhJk7_3a/exec', {
          method: 'POST',
          mode: 'no-cors',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email: email, fuente: 'Blog Informe 2026' })
        }).catch(() => {});
      } catch (err) {}

      // Abrir PDF de descarga
      setTimeout(() => {
        status.classList.remove('hidden');
        btn.innerHTML = '<span>¡Descargado!</span>';
        window.open('https://coolpadelstudios.com/assets/images/foto-reportaje.jpg', '_blank');
      }, 600);
    }
  </script>
</body>
</html>
"""
    os.makedirs("coolpadel-web/blog", exist_ok=True)
    with open("coolpadel-web/blog/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("  [OK] coolpadel-web/blog/index.html (Página Blog & Newsletter)")

if __name__ == "__main__":
    generate_blog_html()
