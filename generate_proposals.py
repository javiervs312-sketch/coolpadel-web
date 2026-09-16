import os

def build_proposals():
    # Common shared switcher bar
    switcher_html = """
    <!-- PROPOSALS SELECTOR BAR -->
    <div class="fixed top-0 inset-x-0 z-[100] bg-slate-950/95 backdrop-blur-md border-b border-cool-cyan/30 py-2 px-4 flex flex-wrap items-center justify-between text-xs text-white shadow-xl">
      <div class="flex items-center gap-2">
        <span class="inline-block w-2.5 h-2.5 rounded-full bg-cool-orange animate-ping"></span>
        <span class="font-bold text-cool-cyan">EXPLORADOR DE PROPUESTAS COOLPADEL:</span>
        <span class="text-slate-400 hidden sm:inline">Haz clic para comparar estilos en tiempo real</span>
      </div>
      <div class="flex items-center gap-2 mt-1 sm:mt-0">
        <a href="index.html" class="px-3 py-1 rounded-lg font-bold transition {{active_1}}">
          1. Editorial & PWS Style
        </a>
        <a href="propuesta-2.html" class="px-3 py-1 rounded-lg font-bold transition {{active_2}}">
          2. B2B Club & Merch Pro
        </a>
        <a href="propuesta-3.html" class="px-3 py-1 rounded-lg font-bold transition {{active_3}}">
          3. Tech & Smart Padel
        </a>
      </div>
    </div>
    <div class="h-10"></div>
    """

    # PROPOSAL 1: EDITORIAL & TRANSLUCENT PWS STYLE (As in user image)
    p1_content = """<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CoolPadel | Editorial PWS & Ecosistema Clubs de Pádel</title>
  <meta name="description" content="Ecosistema de negocio para clubes de pádel: llaveros personalizados, tecnología Save my Play y análisis de la industria.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            outfit: ['Outfit', 'sans-serif'],
            jakarta: ['Plus Jakarta Sans', 'sans-serif'],
          },
          colors: {
            cool: {
              navy: '#0b192c',
              dark: '#0f243d',
              card: '#132d4e',
              blue: '#0284c7',
              cyan: '#38bdf8',
              orange: '#f97316',
              amber: '#fb923c'
            }
          }
        }
      }
    }
  </script>
  <script src="https://unpkg.com/lucide@latest"></script>
  <style>
    body { font-family: 'Plus Jakarta Sans', sans-serif; }
    h1, h2, h3, h4, .font-heading { font-family: 'Outfit', sans-serif; }
    
    /* Background with textured real fair photo + translucent dark blue overlay */
    .bg-pws-textured {
      background: linear-gradient(180deg, rgba(11, 25, 44, 0.88) 0%, rgba(15, 36, 61, 0.92) 50%, rgba(11, 25, 44, 0.96) 100%),
                  url('assets/images/background-fair.jpg');
      background-size: cover;
      background-position: center top;
      background-attachment: fixed;
    }
    
    .glass-editorial {
      background: rgba(19, 45, 78, 0.65);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid rgba(56, 189, 248, 0.2);
    }
    .glass-editorial:hover {
      border-color: rgba(249, 115, 22, 0.45);
    }
    .banner-highlight {
      background: rgba(15, 36, 61, 0.85);
      backdrop-filter: blur(8px);
      border-top: 2px solid #f97316;
      border-bottom: 2px solid #38bdf8;
    }
  </style>
</head>
<body class="bg-pws-textured text-slate-100 min-h-screen relative selection:bg-cool-orange selection:text-white">

  {{SWITCHER}}

  <!-- TOP HEADER -->
  <header class="sticky top-10 z-40 bg-cool-navy/80 backdrop-blur-md border-b border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
      
      <!-- LOGO -->
      <a href="#" class="flex items-center gap-3 group">
        <div class="relative w-11 h-11 bg-gradient-to-tr from-cool-blue to-cool-cyan rounded-full flex items-center justify-center p-1 shadow-lg shadow-cool-blue/20">
          <svg viewBox="0 0 100 100" class="w-full h-full">
            <circle cx="50" cy="50" r="46" fill="#f97316"/>
            <path d="M 50 10 A 40 40 0 0 1 90 50 A 40 40 0 0 1 50 90 A 40 40 0 0 1 35 15 Z" fill="#38bdf8" opacity="0.4"/>
            <circle cx="38" cy="48" r="6" fill="#091426"/>
            <circle cx="62" cy="48" r="6" fill="#091426"/>
            <circle cx="40" cy="46" r="2" fill="#ffffff"/>
            <circle cx="64" cy="46" r="2" fill="#ffffff"/>
            <path d="M 44 62 Q 50 68 56 62" stroke="#091426" stroke-width="3" fill="none" stroke-linecap="round"/>
          </svg>
        </div>
        <div>
          <span class="font-heading font-black text-2xl tracking-tight text-white flex items-center">
            COOL<span class="text-cool-orange">PADEL</span>
          </span>
          <span class="text-[10px] tracking-wider uppercase text-cool-cyan font-bold block -mt-1">Padel Hub & Club Solutions</span>
        </div>
      </a>

      <!-- NAV -->
      <nav class="hidden md:flex items-center gap-8 text-sm font-semibold text-slate-300">
        <a href="#llaveros" class="hover:text-cool-cyan transition">Llaveros Clubs</a>
        <a href="#savemyplay" class="hover:text-cool-cyan transition">Save my Play (IA)</a>
        <a href="#informe" class="hover:text-cool-cyan transition">Industry Insights</a>
        <a href="#sobre-javier" class="hover:text-cool-cyan transition">Sobre Javier</a>
      </nav>

      <!-- CTA -->
      <a href="https://wa.me/34680317486?text=Hola%20Javier,%20quiero%20informaci%C3%B3n%20sobre%20CoolPadel%20para%20mi%20club" target="_blank" class="px-5 py-2.5 rounded-xl font-heading font-bold text-sm bg-gradient-to-r from-cool-orange to-cool-amber text-white shadow-lg shadow-cool-orange/20 hover:scale-105 transition flex items-center gap-2">
        <i data-lucide="message-circle" class="w-4 h-4"></i> Contactar en WhatsApp
      </a>
    </div>
  </header>

  <!-- HERO SECTION WITH EDITORIAL TITLE -->
  <section class="py-16 sm:py-24 relative overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- Center Banner in the Style of "HIGHLIGHTS #01 / STARTUP RECAP" -->
      <div class="max-w-4xl mx-auto text-center space-y-6">
        
        <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-cool-card/90 border border-cool-cyan/30 text-xs font-bold text-cool-cyan uppercase tracking-widest shadow-lg">
          <i data-lucide="award" class="w-3.5 h-3.5 text-cool-orange"></i> Ecosistema Exclusivo para Gerentes de Club
        </div>

        <h1 class="text-4xl sm:text-6xl lg:text-7xl font-black font-heading tracking-tight text-white leading-tight uppercase">
          Llaveros que Crean <br>
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-cool-cyan via-white to-cool-orange">Comunidad de Club</span>
        </h1>

        <p class="text-base sm:text-xl text-slate-200 max-w-2xl mx-auto font-normal leading-relaxed drop-shadow-md">
          Fabricamos llaveros personalizados de alta calidad que tus socios conservarán durante años en su paletero. Y conectamos tu club con tecnologías de vanguardia como <strong>Save my Play</strong>.
        </p>

        <!-- CTA Buttons -->
        <div class="flex flex-col sm:flex-row items-center justify-center gap-4 pt-4">
          <a href="#llaveros" class="w-full sm:w-auto px-8 py-4 rounded-2xl font-heading font-extrabold text-base bg-gradient-to-r from-cool-orange to-cool-amber text-white shadow-xl shadow-cool-orange/30 hover:scale-105 transition flex items-center justify-center gap-2">
            <i data-lucide="palette" class="w-5 h-5"></i> Ver Llaveros para Clubs
          </a>
          <a href="#informe" class="w-full sm:w-auto px-7 py-4 rounded-2xl font-heading font-bold text-base bg-cool-navy/90 border border-slate-700 hover:border-cool-cyan text-white transition flex items-center justify-center gap-2">
            <i data-lucide="file-text" class="w-5 h-5 text-yellow-400"></i> Descargar Informe Pádel
          </a>
        </div>

      </div>

      <!-- PHOTO CARDS SHOWCASE -->
      <div class="mt-16 grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
        
        <div class="glass-editorial rounded-2xl overflow-hidden p-4 group transition duration-300 hover:-translate-y-2">
          <div class="aspect-square rounded-xl overflow-hidden mb-3 bg-slate-900">
            <img src="assets/images/llaveros-padel-azul.png" alt="Llavero Pádel Club" class="w-full h-full object-cover group-hover:scale-110 transition duration-500">
          </div>
          <span class="text-[10px] font-bold text-cool-cyan uppercase tracking-wider">Pádel Custom</span>
          <h3 class="font-bold text-white text-base">Pala con Relieve 3D</h3>
          <p class="text-xs text-slate-300 mt-1">Logo a dos caras, textura fiel y orificios de pala real.</p>
        </div>

        <div class="glass-editorial rounded-2xl overflow-hidden p-4 group transition duration-300 hover:-translate-y-2">
          <div class="aspect-square rounded-xl overflow-hidden mb-3 bg-slate-900">
            <img src="assets/images/llavero-austrian-padel.jpg" alt="Austrian Padel Union" class="w-full h-full object-cover group-hover:scale-110 transition duration-500">
          </div>
          <span class="text-[10px] font-bold text-cool-orange uppercase tracking-wider">Federación Oficial</span>
          <h3 class="font-bold text-white text-base">Austrian Padel Union</h3>
          <p class="text-xs text-slate-300 mt-1">Colores de marca de máxima precisión y resistencia al roce.</p>
        </div>

        <div class="glass-editorial rounded-2xl overflow-hidden p-4 group transition duration-300 hover:-translate-y-2">
          <div class="aspect-square rounded-xl overflow-hidden mb-3 bg-slate-900">
            <img src="assets/images/llaveros-tenis-azul-blanco.jpg" alt="Llaveros Tenis" class="w-full h-full object-cover group-hover:scale-110 transition duration-500">
          </div>
          <span class="text-[10px] font-bold text-cool-cyan uppercase tracking-wider">Tenis & Raqueta</span>
          <h3 class="font-bold text-white text-base">Cordaje Detallado</h3>
          <p class="text-xs text-slate-300 mt-1">Ideal para torneos y academias de raqueta.</p>
        </div>

        <div class="glass-editorial rounded-2xl overflow-hidden p-4 group transition duration-300 hover:-translate-y-2">
          <div class="aspect-square rounded-xl overflow-hidden mb-3 bg-slate-900">
            <img src="assets/images/llaveros-tenis-rojo-morado.jpg" alt="Llaveros Edición Especial" class="w-full h-full object-cover group-hover:scale-110 transition duration-500">
          </div>
          <span class="text-[10px] font-bold text-yellow-400 uppercase tracking-wider">Torneos Especiales</span>
          <h3 class="font-bold text-white text-base">Grips y Colores Flúor</h3>
          <p class="text-xs text-slate-300 mt-1">El detalle estrella para la bolsa de bienvenida del jugador.</p>
        </div>

      </div>

    </div>
  </section>

  <!-- SECCIÓN SAVE MY PLAY -->
  <section id="savemyplay" class="py-20 relative border-t border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="glass-editorial rounded-3xl p-8 sm:p-12 border border-emerald-500/30">
        <div class="grid lg:grid-cols-12 gap-8 items-center">
          <div class="lg:col-span-8 space-y-4">
            <span class="px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-400 text-xs font-bold uppercase tracking-wider">
              Tecnología para Clubes
            </span>
            <h2 class="text-3xl sm:text-4xl font-black font-heading text-white">
              Cámaras con IA para tus pistas: <span class="text-emerald-400">Save my Play</span>
            </h2>
            <p class="text-slate-300 text-sm sm:text-base leading-relaxed">
              Tus jugadores pulsan un botón y reciben sus mejores jugadas en su smartphone para compartirlas en redes sociales mencionando a tu club. Dinamiza tus pistas y llena las horas valle.
            </p>
            <div class="flex flex-wrap gap-4 pt-2">
              <a href="https://wa.me/34680317486?text=Hola%20Javier,%20quiero%20conocer%20Save%20my%20Play%20para%20mi%20club" target="_blank" class="px-6 py-3 rounded-xl font-bold text-sm bg-emerald-500 hover:bg-emerald-600 text-white transition flex items-center gap-2">
                <i data-lucide="play" class="w-4 h-4"></i> Pedir Demo para mi Club
              </a>
            </div>
          </div>
          <div class="lg:col-span-4 bg-cool-navy/90 p-6 rounded-2xl border border-slate-700 text-center space-y-2">
            <div class="text-3xl font-black text-emerald-400 font-heading">100% Viral</div>
            <p class="text-xs text-slate-400">Genera contenido diario para tu club sin coste de grabación profesional.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECCIÓN INFORME DEL NEGOCIO DEL PÁDEL -->
  <section id="informe" class="py-20 relative border-t border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-8">
      
      <div class="max-w-3xl mx-auto space-y-3">
        <span class="px-3 py-1 rounded-full bg-yellow-500/20 text-yellow-400 text-xs font-bold uppercase tracking-wider">
          Padel World Summit & RacquetX Miami
        </span>
        <h2 class="text-3xl sm:text-5xl font-black font-heading text-white">
          "How is the Padel Business playing out?"
        </h2>
        <p class="text-slate-300 text-sm sm:text-base">
          Conclusiones tras hablar con más de 116 empresas del sector: pistas inteligentes, expansión en EEUU, sostenibilidad y claves para marcas.
        </p>
      </div>

      <div class="inline-block p-8 rounded-3xl glass-editorial border border-cool-cyan/30 text-center max-w-xl mx-auto space-y-4">
        <i data-lucide="file-check-2" class="w-12 h-12 text-cool-orange mx-auto"></i>
        <h3 class="font-heading font-black text-xl text-white">Informe Completo en PDF</h3>
        <p class="text-xs text-slate-300">Descarga gratuita con todas las diapositivas y análisis de Javier Villoria Soleto.</p>
        <a href="assets/padel-industry-report-coolpadel.pdf" download target="_blank" class="inline-flex items-center gap-2 px-6 py-3 rounded-xl font-bold bg-gradient-to-r from-cool-orange to-cool-amber text-white shadow-lg transition hover:scale-105">
          <i data-lucide="download" class="w-4 h-4"></i> Descargar Informe (PDF)
        </a>
      </div>

    </div>
  </section>

  <!-- FOOTER -->
  <footer class="bg-cool-navy/90 border-t border-slate-800 py-10 text-center text-xs text-slate-400">
    <p>© 2026 CoolPadel. Ecosistema de Merchandising y Soluciones para Clubs de Pádel. Fundado por Javier Villoria Soleto.</p>
  </footer>

  <script>lucide.createIcons();</script>
</body>
</html>"""

    # PROPOSAL 2: B2B CLUB & MERCHANDISING FOCUS
    p2_content = """<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CoolPadel | Propuesta 2: B2B Club & Merch Pro</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            outfit: ['Outfit', 'sans-serif'],
            jakarta: ['Plus Jakarta Sans', 'sans-serif'],
          },
          colors: {
            cool: {
              navy: '#060d17',
              dark: '#0a1728',
              card: '#0f223a',
              blue: '#0284c7',
              cyan: '#38bdf8',
              orange: '#f97316',
              amber: '#fb923c'
            }
          }
        }
      }
    }
  </script>
  <script src="https://unpkg.com/lucide@latest"></script>
  <style>
    body { font-family: 'Plus Jakarta Sans', sans-serif; }
    h1, h2, h3, h4, .font-heading { font-family: 'Outfit', sans-serif; }
    .bg-pro-texture {
      background: linear-gradient(180deg, rgba(6, 13, 23, 0.90) 0%, rgba(10, 23, 40, 0.94) 100%),
                  url('assets/images/background-fair.jpg');
      background-size: cover;
      background-attachment: fixed;
    }
  </style>
</head>
<body class="bg-pro-texture text-slate-100 min-h-screen relative selection:bg-cool-orange selection:text-white">

  {{SWITCHER}}

  <header class="sticky top-10 z-40 bg-cool-navy/90 backdrop-blur-md border-b border-slate-800 py-4 px-6">
    <div class="max-w-7xl mx-auto flex items-center justify-between">
      <span class="font-heading font-black text-2xl text-white">COOL<span class="text-cool-orange">PADEL</span> <span class="text-xs uppercase px-2 py-0.5 rounded bg-cool-blue/30 text-cool-cyan ml-2">B2B Club Pro</span></span>
      <a href="https://wa.me/34680317486?text=Hola%20Javier" target="_blank" class="px-4 py-2 rounded-xl bg-cool-orange font-bold text-xs text-white">Pedir Simulación 3D Gratis</a>
    </div>
  </header>

  <section class="py-20 px-4 text-center max-w-4xl mx-auto space-y-6">
    <div class="inline-block px-3 py-1 rounded-full bg-cool-orange/20 text-cool-orange text-xs font-bold uppercase">
      Venta Directa a Clubs y Marcas
    </div>
    <h1 class="text-4xl sm:text-6xl font-black font-heading text-white">
      Llaveros Personalizados con Margen Pro-Shop y Fidelización
    </h1>
    <p class="text-slate-300 text-lg">
      El regalo de bienvenida para tus socios y el merchandising más rentable en el mostrador del club.
    </p>

    <!-- Table of benefits & volumes -->
    <div class="grid sm:grid-cols-3 gap-6 pt-8 text-left">
      <div class="bg-cool-card/80 p-6 rounded-2xl border border-slate-700">
        <h3 class="font-bold text-white text-lg">Tiradas Cortas (50-100 uds)</h3>
        <p class="text-xs text-slate-400 mt-2">Ideal para torneos de fin de semana o bienvenida de nuevas parejas.</p>
        <div class="mt-4 text-emerald-400 font-bold text-sm">Muestra 3D Gratis</div>
      </div>
      <div class="bg-cool-card/80 p-6 rounded-2xl border border-cool-orange/50 relative">
        <span class="absolute -top-3 right-4 px-2 py-0.5 rounded bg-cool-orange text-white text-[10px] font-bold">RECOMENDADO</span>
        <h3 class="font-bold text-white text-lg">Club Regular (250-500 uds)</h3>
        <p class="text-xs text-slate-400 mt-2">Pack temporada de socios y venta directa en recepción con +60% margen.</p>
        <div class="mt-4 text-cool-orange font-bold text-sm">Envío Prioritario</div>
      </div>
      <div class="bg-cool-card/80 p-6 rounded-2xl border border-slate-700">
        <h3 class="font-bold text-white text-lg">Grandes Clubs & Marcas</h3>
        <p class="text-xs text-slate-400 mt-2">+1000 unidades con colores especiales, relieves dobles y packaging a medida.</p>
        <div class="mt-4 text-cool-cyan font-bold text-sm">Tarifa Especial B2B</div>
      </div>
    </div>
  </section>

  <footer class="py-8 text-center text-xs text-slate-500 border-t border-slate-800">
    CoolPadel B2B Pro Edition · Javier Villoria Soleto
  </footer>

  <script>lucide.createIcons();</script>
</body>
</html>"""

    # PROPOSAL 3: MODERN TECH & SMART PADEL
    p3_content = """<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CoolPadel | Propuesta 3: Tech & Smart Padel</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            outfit: ['Outfit', 'sans-serif'],
            jakarta: ['Plus Jakarta Sans', 'sans-serif'],
          },
          colors: {
            cool: {
              navy: '#07111e',
              dark: '#0c1a2e',
              card: '#112540',
              blue: '#0284c7',
              cyan: '#38bdf8',
              orange: '#f97316',
              amber: '#fb923c'
            }
          }
        }
      }
    }
  </script>
  <script src="https://unpkg.com/lucide@latest"></script>
  <style>
    body { font-family: 'Plus Jakarta Sans', sans-serif; }
    h1, h2, h3, h4, .font-heading { font-family: 'Outfit', sans-serif; }
    .bg-tech-texture {
      background: linear-gradient(180deg, rgba(7, 17, 30, 0.88) 0%, rgba(12, 26, 46, 0.94) 100%),
                  url('assets/images/background-fair.jpg');
      background-size: cover;
      background-attachment: fixed;
    }
  </style>
</head>
<body class="bg-tech-texture text-slate-100 min-h-screen relative selection:bg-cool-orange selection:text-white">

  {{SWITCHER}}

  <header class="sticky top-10 z-40 bg-cool-navy/90 backdrop-blur-md border-b border-slate-800 py-4 px-6">
    <div class="max-w-7xl mx-auto flex items-center justify-between">
      <span class="font-heading font-black text-2xl text-white">COOL<span class="text-cool-cyan">PADEL</span> <span class="text-xs uppercase px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-400 ml-2">Smart Courts & Merch Hub</span></span>
      <a href="https://wa.me/34680317486?text=Hola%20Javier" target="_blank" class="px-4 py-2 rounded-xl bg-cool-cyan text-cool-navy font-bold text-xs">Hablar con Javier</a>
    </div>
  </header>

  <section class="py-20 px-4 text-center max-w-4xl mx-auto space-y-6">
    <div class="inline-block px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-400 text-xs font-bold uppercase">
      Innovación & Comunidad de Pádel
    </div>
    <h1 class="text-4xl sm:text-6xl font-black font-heading text-white">
      Tecnología Save my Play + Merchandising de Alta Fidelidad
    </h1>
    <p class="text-slate-300 text-lg">
      La combinación perfecta para convertir tu club en una referencia: grabaciones con IA en pista y llaveros custom con los que los socios presumirán de club.
    </p>

    <!-- Tech Grid -->
    <div class="grid sm:grid-cols-2 gap-6 pt-8 text-left">
      <div class="bg-cool-card/90 p-6 rounded-2xl border border-emerald-500/30">
        <i data-lucide="video" class="w-8 h-8 text-emerald-400 mb-3"></i>
        <h3 class="font-bold text-white text-xl">Save my Play (Cámaras IA)</h3>
        <p class="text-xs text-slate-300 mt-2">Graba partidos sin esfuerzo. Los jugadores se llevan su mejor punto con un clic en el reloj/botón de pista.</p>
      </div>
      <div class="bg-cool-card/90 p-6 rounded-2xl border border-cool-cyan/30">
        <i data-lucide="tag" class="w-8 h-8 text-cool-cyan mb-3"></i>
        <h3 class="font-bold text-white text-xl">Llaveros Custom CoolPadel</h3>
        <p class="text-xs text-slate-300 mt-2">Fabricación rápida con materiales premium y relieve para federaciones y clubes.</p>
      </div>
    </div>
  </section>

  <footer class="py-8 text-center text-xs text-slate-500 border-t border-slate-800">
    CoolPadel Smart Edition · Javier Villoria Soleto
  </footer>

  <script>lucide.createIcons();</script>
</body>
</html>"""

    # Apply switcher substitutions
    sw_1 = switcher_html.replace("{{active_1}}", "bg-cool-orange text-white").replace("{{active_2}}", "bg-slate-800 text-slate-300 hover:text-white").replace("{{active_3}}", "bg-slate-800 text-slate-300 hover:text-white")
    sw_2 = switcher_html.replace("{{active_1}}", "bg-slate-800 text-slate-300 hover:text-white").replace("{{active_2}}", "bg-cool-orange text-white").replace("{{active_3}}", "bg-slate-800 text-slate-300 hover:text-white")
    sw_3 = switcher_html.replace("{{active_1}}", "bg-slate-800 text-slate-300 hover:text-white").replace("{{active_2}}", "bg-slate-800 text-slate-300 hover:text-white").replace("{{active_3}}", "bg-cool-orange text-white")

    out_dir = os.path.join(os.getcwd(), "coolpadel-web")
    os.makedirs(out_dir, exist_ok=True)

    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(p1_content.replace("{{SWITCHER}}", sw_1))

    with open(os.path.join(out_dir, "propuesta-2.html"), "w", encoding="utf-8") as f:
        f.write(p2_content.replace("{{SWITCHER}}", sw_2))

    with open(os.path.join(out_dir, "propuesta-3.html"), "w", encoding="utf-8") as f:
        f.write(p3_content.replace("{{SWITCHER}}", sw_3))

    print("All 3 proposals built successfully!")

if __name__ == "__main__":
    build_proposals()
