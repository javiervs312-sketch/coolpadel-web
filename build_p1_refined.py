import os

def build_p1_refined():
    html = """<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CoolPadel | Llaveros Personalizados & Soluciones para Clubs de Pádel</title>
  <meta name="description" content="Ecosistema de negocio para clubes de pádel: llaveros personalizados de alta calidad, tecnología Save my Play y análisis de la industria.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
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
              navy: '#071324',
              dark: '#0c1e36',
              card: '#102747',
              blue: '#0284c7',
              cyan: '#38bdf8',
              orange: '#f97316',
              amber: '#fb923c'
            }
          },
          animation: {
            'ticker': 'ticker 28s linear infinite',
            'ticker-reverse': 'tickerReverse 30s linear infinite',
          },
          keyframes: {
            ticker: {
              '0%': { transform: 'translateX(0%)' },
              '100%': { transform: 'translateX(-50%)' }
            },
            tickerReverse: {
              '0%': { transform: 'translateX(-50%)' },
              '100%': { transform: 'translateX(0%)' }
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
    
    /* Imagen de fondo mucho más visible con overlay translúcido suave */
    .bg-pws-visible {
      background: linear-gradient(180deg, rgba(7, 19, 36, 0.50) 0%, rgba(12, 30, 54, 0.60) 45%, rgba(7, 19, 36, 0.85) 100%),
                  url('assets/images/background-fair.jpg');
      background-size: cover;
      background-position: center top;
      background-attachment: fixed;
    }
    
    .glass-box {
      background: rgba(12, 30, 54, 0.65);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border: 1px solid rgba(56, 189, 248, 0.25);
    }
    .glass-box:hover {
      border-color: rgba(249, 115, 22, 0.6);
      transform: translateY(-6px);
      box-shadow: 0 20px 35px -10px rgba(249, 115, 22, 0.25);
    }

    .ticker-wrap {
      width: 100%;
      overflow: hidden;
      white-space: nowrap;
    }
    .ticker-content {
      display: inline-flex;
      white-space: nowrap;
    }
    .ticker-item {
      display: inline-flex;
      align-items: center;
    }
  </style>
</head>
<body class="bg-pws-visible text-slate-100 min-h-screen relative selection:bg-cool-orange selection:text-white overflow-x-hidden">

  <!-- 1. TICKER SUPERIOR ESTILO BOLSA EN CONTINUO MOVIMIENTO -->
  <div class="sticky top-0 z-50 bg-slate-950/90 backdrop-blur-md border-b border-cool-cyan/30 py-2.5 ticker-wrap text-xs text-white shadow-xl">
    <div class="ticker-content animate-ticker flex items-center gap-8 font-semibold">
      
      <!-- Loop Items 1 -->
      <a href="#informe" class="ticker-item gap-2 hover:text-cool-cyan transition">
        <span class="px-2 py-0.5 rounded bg-cool-orange text-white font-bold text-[10px]">INFORME EXCLUSIVO</span>
        <span>"How is the Padel Business playing out?" por Javier Villoria</span>
        <span class="text-cool-cyan underline font-bold flex items-center gap-1">Descargar PDF <i data-lucide="download" class="w-3 h-3"></i></span>
      </a>
      <span class="text-slate-600">●</span>
      <span class="ticker-item gap-2 text-slate-300">
        <i data-lucide="trending-up" class="w-3.5 h-3.5 text-emerald-400"></i>
        <span>116 Empresas analizadas en PWS Barcelona & RacquetX Miami</span>
      </span>
      <span class="text-slate-600">●</span>
      <a href="#llaveros" class="ticker-item gap-2 hover:text-cool-orange transition">
        <i data-lucide="sparkles" class="w-3.5 h-3.5 text-yellow-400"></i>
        <span>Llaveros Personalizados para Clubs: Muestra 3D 100% Gratis</span>
      </a>
      <span class="text-slate-600">●</span>
      <a href="#savemyplay" class="ticker-item gap-2 hover:text-emerald-400 transition">
        <i data-lucide="video" class="w-3.5 h-3.5 text-emerald-400"></i>
        <span>Save my Play: Cámaras IA para llenar tus pistas en horas valle</span>
      </a>
      <span class="text-slate-600">●</span>

      <!-- Duplicate for seamless infinite loop -->
      <a href="#informe" class="ticker-item gap-2 hover:text-cool-cyan transition">
        <span class="px-2 py-0.5 rounded bg-cool-orange text-white font-bold text-[10px]">INFORME EXCLUSIVO</span>
        <span>"How is the Padel Business playing out?" por Javier Villoria</span>
        <span class="text-cool-cyan underline font-bold flex items-center gap-1">Descargar PDF <i data-lucide="download" class="w-3 h-3"></i></span>
      </a>
      <span class="text-slate-600">●</span>
      <span class="ticker-item gap-2 text-slate-300">
        <i data-lucide="trending-up" class="w-3.5 h-3.5 text-emerald-400"></i>
        <span>116 Empresas analizadas en PWS Barcelona & RacquetX Miami</span>
      </span>
      <span class="text-slate-600">●</span>
      <a href="#llaveros" class="ticker-item gap-2 hover:text-cool-orange transition">
        <i data-lucide="sparkles" class="w-3.5 h-3.5 text-yellow-400"></i>
        <span>Llaveros Personalizados para Clubs: Muestra 3D 100% Gratis</span>
      </a>
      <span class="text-slate-600">●</span>
      <a href="#savemyplay" class="ticker-item gap-2 hover:text-emerald-400 transition">
        <i data-lucide="video" class="w-3.5 h-3.5 text-emerald-400"></i>
        <span>Save my Play: Cámaras IA para llenar tus pistas en horas valle</span>
      </a>
      <span class="text-slate-600">●</span>

    </div>
  </div>

  <!-- NAVBAR -->
  <header class="bg-cool-navy/80 backdrop-blur-lg border-b border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
      
      <!-- LOGO -->
      <a href="#" class="flex items-center gap-3 group">
        <div class="relative w-12 h-12 bg-gradient-to-tr from-cool-blue to-cool-cyan rounded-full flex items-center justify-center p-1 shadow-lg shadow-cool-blue/30 group-hover:scale-105 transition">
          <svg viewBox="0 0 100 100" class="w-full h-full">
            <circle cx="50" cy="50" r="46" fill="#f97316"/>
            <path d="M 50 10 A 40 40 0 0 1 90 50 A 40 40 0 0 1 50 90 A 40 40 0 0 1 35 15 Z" fill="#38bdf8" opacity="0.45"/>
            <circle cx="38" cy="48" r="6" fill="#071324"/>
            <circle cx="62" cy="48" r="6" fill="#071324"/>
            <circle cx="40" cy="46" r="2" fill="#ffffff"/>
            <circle cx="64" cy="46" r="2" fill="#ffffff"/>
            <path d="M 44 62 Q 50 68 56 62" stroke="#071324" stroke-width="3.5" fill="none" stroke-linecap="round"/>
          </svg>
        </div>
        <div>
          <span class="font-heading font-black text-2xl sm:text-3xl tracking-tight text-white flex items-center">
            COOL<span class="text-cool-orange">PADEL</span>
          </span>
          <span class="text-[10px] tracking-wider uppercase text-cool-cyan font-bold block -mt-1">Padel Hub & Club Solutions</span>
        </div>
      </a>

      <!-- NAV LINKS -->
      <nav class="hidden md:flex items-center gap-8 text-sm font-bold text-slate-200">
        <a href="#llaveros" class="hover:text-cool-orange transition flex items-center gap-1.5">
          <i data-lucide="key" class="w-4 h-4 text-cool-orange"></i> Llaveros Clubs
        </a>
        <a href="#savemyplay" class="hover:text-emerald-400 transition flex items-center gap-1.5">
          <i data-lucide="video" class="w-4 h-4 text-emerald-400"></i> Save my Play
        </a>
        <a href="#informe" class="hover:text-yellow-400 transition flex items-center gap-1.5">
          <i data-lucide="file-text" class="w-4 h-4 text-yellow-400"></i> Informe Pádel
        </a>
        <a href="#sobre-javier" class="hover:text-cool-cyan transition flex items-center gap-1.5">
          <i data-lucide="user" class="w-4 h-4 text-cool-cyan"></i> Sobre Javier
        </a>
      </nav>

      <!-- CTA WHATSAPP -->
      <a href="https://wa.me/34680317486?text=Hola%20Javier" 
         target="_blank" 
         class="px-5 py-2.5 rounded-xl font-heading font-black text-xs sm:text-sm bg-gradient-to-r from-cool-orange to-cool-amber text-white shadow-lg shadow-cool-orange/30 hover:scale-105 active:scale-95 transition flex items-center gap-2">
        <i data-lucide="message-circle" class="w-4 h-4"></i> Pedir Muestra Gratis
      </a>

    </div>
  </header>

  <!-- HERO PRINCIPAL -->
  <section class="pt-12 pb-16 lg:pt-16 lg:pb-24 relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-10">
      
      <!-- TÍTULO PRINCIPAL EXACTO -->
      <div class="max-w-4xl mx-auto space-y-4">
        <h1 class="text-4xl sm:text-6xl lg:text-7xl font-black font-heading tracking-tight text-white uppercase leading-[1.08] drop-shadow-xl">
          Llaveros que Crean <br>
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-cool-cyan via-white to-cool-orange">
            Comunidad de Club
          </span>
        </h1>
        <p class="text-base sm:text-xl text-slate-200 max-w-2xl mx-auto font-normal leading-relaxed drop-shadow-md">
          El merchandising que tus jugadores llevarán siempre en su paletero y la tecnología inteligente para llevar tu club al siguiente nivel.
        </p>
      </div>

      <!-- 2 GRANDES FOTOS INTERACTIVAS QUE LLEVAN A SUS SECCIONES -->
      <div class="grid md:grid-cols-2 gap-8 max-w-5xl mx-auto text-left">
        
        <!-- CARD 1: LLAVEROS PARA CLUBS (Click lleva a #llaveros) -->
        <a href="#llaveros" class="group relative rounded-3xl overflow-hidden glass-box p-5 sm:p-6 transition duration-300 block cursor-pointer">
          <div class="relative aspect-[16/10] rounded-2xl overflow-hidden mb-5 bg-slate-900 shadow-2xl">
            <img src="assets/images/llaveros-padel-azul.png" alt="Llaveros personalizados para clubs de pádel" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
            <div class="absolute inset-0 bg-gradient-to-t from-cool-navy/95 via-cool-navy/20 to-transparent"></div>
            
            <div class="absolute top-4 left-4">
              <span class="px-3 py-1 rounded-full bg-cool-orange text-white font-heading font-black text-xs uppercase tracking-wider shadow-lg">
                Pilar 01 · Merchandising
              </span>
            </div>

            <div class="absolute bottom-4 left-4 right-4 flex items-center justify-between">
              <div>
                <span class="text-[11px] font-bold text-cool-cyan uppercase tracking-wider">Diseño 100% a medida</span>
                <h3 class="text-xl sm:text-2xl font-black font-heading text-white">Llaveros Custom para Clubs</h3>
              </div>
              <div class="w-10 h-10 rounded-full bg-cool-orange text-white flex items-center justify-center group-hover:translate-x-1 transition shadow-lg flex-shrink-0">
                <i data-lucide="arrow-down" class="w-5 h-5"></i>
              </div>
            </div>
          </div>

          <p class="text-slate-300 text-sm leading-relaxed mb-4">
            Palas de pádel y raquetas de tenis personalizadas con el escudo y colores exactos de tu club. Ideal para <strong>welcome packs de torneos</strong>, <strong>regalo a socios</strong> y <strong>venta en recepción</strong>.
          </p>

          <div class="flex items-center gap-2 text-cool-orange font-bold text-xs group-hover:underline">
            <span>Ver catálogo, ejemplos reales y calculadora de pedidos</span>
            <i data-lucide="arrow-down-right" class="w-4 h-4"></i>
          </div>
        </a>

        <!-- CARD 2: SAVE MY PLAY (Click lleva a #savemyplay) -->
        <a href="#savemyplay" class="group relative rounded-3xl overflow-hidden glass-box p-5 sm:p-6 transition duration-300 block cursor-pointer">
          <div class="relative aspect-[16/10] rounded-2xl overflow-hidden mb-5 bg-slate-900 shadow-2xl flex items-center justify-center">
            <img src="assets/images/background-fair.jpg" alt="Save my Play cámaras inteligentes" class="w-full h-full object-cover group-hover:scale-105 transition duration-500 filter brightness-75">
            <div class="absolute inset-0 bg-gradient-to-t from-cool-navy/95 via-cool-navy/30 to-transparent"></div>
            
            <div class="absolute top-4 left-4">
              <span class="px-3 py-1 rounded-full bg-emerald-500 text-white font-heading font-black text-xs uppercase tracking-wider shadow-lg">
                Pilar 02 · Smart Courts
              </span>
            </div>

            <div class="absolute inset-0 flex items-center justify-center p-4 text-center">
              <div class="bg-slate-950/80 backdrop-blur-md px-6 py-4 rounded-2xl border border-emerald-500/40 shadow-2xl">
                <div class="w-12 h-12 rounded-xl bg-emerald-500 text-white flex items-center justify-center mx-auto mb-2 shadow-lg">
                  <i data-lucide="play" class="w-6 h-6 fill-current"></i>
                </div>
                <h4 class="text-xl font-heading font-black text-white">Save my Play</h4>
                <p class="text-[11px] text-emerald-400 font-bold uppercase tracking-wider">Cámaras con IA para Pistas</p>
              </div>
            </div>

            <div class="absolute bottom-4 left-4 right-4 flex items-center justify-between">
              <div>
                <span class="text-[11px] font-bold text-emerald-400 uppercase tracking-wider">Partner Oficial para Clubs</span>
                <h3 class="text-xl sm:text-2xl font-black font-heading text-white">Grabación Automática de Puntos</h3>
              </div>
              <div class="w-10 h-10 rounded-full bg-emerald-500 text-white flex items-center justify-center group-hover:translate-x-1 transition shadow-lg flex-shrink-0">
                <i data-lucide="arrow-down" class="w-5 h-5"></i>
              </div>
            </div>
          </div>

          <p class="text-slate-300 text-sm leading-relaxed mb-4">
            Instalamos cámaras deportivas con inteligencia artificial para que tus jugadores revivan y compartan sus mejores puntos en Instagram y TikTok, aumentando la recurrencia en horas valle.
          </p>

          <div class="flex items-center gap-2 text-emerald-400 font-bold text-xs group-hover:underline">
            <span>Conocer cómo funciona y pedir demostración para tu club</span>
            <i data-lucide="arrow-down-right" class="w-4 h-4"></i>
          </div>
        </a>

      </div>

    </div>
  </section>

  <!-- 3. PASARELA / CARROUSEL DE LOGOS "TRUSTED BY" -->
  <section class="py-8 bg-slate-950/70 border-y border-slate-800/80 overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 mb-3 text-center">
      <p class="text-xs uppercase tracking-widest font-black text-cool-cyan">
        TRUSTED BY · MÁS DE 30 CLUBS, MARCAS Y FEDERACIONES
      </p>
    </div>

    <!-- CARROUSEL CONTINUO DE LOGOS -->
    <div class="ticker-wrap py-2">
      <div class="ticker-content animate-ticker-reverse flex items-center gap-12 text-slate-300 text-sm font-black font-heading tracking-wider">
        
        <!-- Logo 1 -->
        <div class="flex items-center gap-3 px-4 py-2 rounded-xl bg-cool-card/60 border border-slate-700/80">
          <i data-lucide="shield" class="w-5 h-5 text-cool-orange"></i>
          <span>AUSTRIAN PADEL UNION</span>
        </div>
        <!-- Logo 2 -->
        <div class="flex items-center gap-3 px-4 py-2 rounded-xl bg-cool-card/60 border border-slate-700/80">
          <i data-lucide="trophy" class="w-5 h-5 text-cool-cyan"></i>
          <span>CLUB PADEL VILAMALLA</span>
        </div>
        <!-- Logo 3 -->
        <div class="flex items-center gap-3 px-4 py-2 rounded-xl bg-cool-card/60 border border-slate-700/80">
          <i data-lucide="activity" class="w-5 h-5 text-yellow-400"></i>
          <span>RETCL TENNIS CLUB</span>
        </div>
        <!-- Logo 4 -->
        <div class="flex items-center gap-3 px-4 py-2 rounded-xl bg-cool-card/60 border border-slate-700/80">
          <i data-lucide="award" class="w-5 h-5 text-emerald-400"></i>
          <span>PADEL ADDICT</span>
        </div>
        <!-- Logo 5 -->
        <div class="flex items-center gap-3 px-4 py-2 rounded-xl bg-cool-card/60 border border-slate-700/80">
          <i data-lucide="play" class="w-5 h-5 text-emerald-400"></i>
          <span>SAVE MY PLAY</span>
        </div>
        <!-- Logo 6 -->
        <div class="flex items-center gap-3 px-4 py-2 rounded-xl bg-cool-card/60 border border-slate-700/80">
          <i data-lucide="star" class="w-5 h-5 text-cool-orange"></i>
          <span>USA PADEL EXPANSION</span>
        </div>

        <!-- DUPLICATE FOR INFINITE LOOP -->
        <div class="flex items-center gap-3 px-4 py-2 rounded-xl bg-cool-card/60 border border-slate-700/80">
          <i data-lucide="shield" class="w-5 h-5 text-cool-orange"></i>
          <span>AUSTRIAN PADEL UNION</span>
        </div>
        <div class="flex items-center gap-3 px-4 py-2 rounded-xl bg-cool-card/60 border border-slate-700/80">
          <i data-lucide="trophy" class="w-5 h-5 text-cool-cyan"></i>
          <span>CLUB PADEL VILAMALLA</span>
        </div>
        <div class="flex items-center gap-3 px-4 py-2 rounded-xl bg-cool-card/60 border border-slate-700/80">
          <i data-lucide="activity" class="w-5 h-5 text-yellow-400"></i>
          <span>RETCL TENNIS CLUB</span>
        </div>
        <div class="flex items-center gap-3 px-4 py-2 rounded-xl bg-cool-card/60 border border-slate-700/80">
          <i data-lucide="award" class="w-5 h-5 text-emerald-400"></i>
          <span>PADEL ADDICT</span>
        </div>
        <div class="flex items-center gap-3 px-4 py-2 rounded-xl bg-cool-card/60 border border-slate-700/80">
          <i data-lucide="play" class="w-5 h-5 text-emerald-400"></i>
          <span>SAVE MY PLAY</span>
        </div>
        <div class="flex items-center gap-3 px-4 py-2 rounded-xl bg-cool-card/60 border border-slate-700/80">
          <i data-lucide="star" class="w-5 h-5 text-cool-orange"></i>
          <span>USA PADEL EXPANSION</span>
        </div>

      </div>
    </div>
  </section>

  <!-- SECCIÓN DETALLADA: LLAVEROS PARA CLUBS -->
  <section id="llaveros" class="py-20 relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-4">
        <span class="inline-block px-3 py-1 rounded-full bg-cool-orange/20 text-cool-orange text-xs font-bold uppercase tracking-wider">
          Catálogo & Fabricación a Medida
        </span>
        <h2 class="text-3xl sm:text-5xl font-black font-heading text-white">
          Llaveros Personalizados con los Colores de tu Club
        </h2>
        <p class="text-slate-200 text-base sm:text-lg">
          Tus socios lo usarán a diario en las llaves o en la cremallera del paletero. Resistentes, ligeros y con relieve 3D.
        </p>
      </div>

      <!-- GALERÍA DE 4 FOTOS REALES -->
      <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-16">
        
        <div class="glass-box rounded-2xl p-4 group transition duration-300">
          <div class="aspect-square rounded-xl overflow-hidden mb-3 bg-slate-900">
            <img src="assets/images/llaveros-padel-azul.png" alt="Llaveros de pádel para clubs" class="w-full h-full object-cover group-hover:scale-110 transition duration-500">
          </div>
          <span class="text-[10px] font-bold text-cool-cyan uppercase tracking-wider">Pádel Custom</span>
          <h3 class="font-bold text-white text-base">Pala Pádel Doble Cara</h3>
          <p class="text-xs text-slate-300 mt-1">Escudo en relieve, micro-perforaciones y marco protector.</p>
        </div>

        <div class="glass-box rounded-2xl p-4 group transition duration-300">
          <div class="aspect-square rounded-xl overflow-hidden mb-3 bg-slate-900">
            <img src="assets/images/llavero-austrian-padel.jpg" alt="Llavero Austrian Padel Union" class="w-full h-full object-cover group-hover:scale-110 transition duration-500">
          </div>
          <span class="text-[10px] font-bold text-cool-orange uppercase tracking-wider">Federaciones</span>
          <h3 class="font-bold text-white text-base">Austrian Padel Union</h3>
          <p class="text-xs text-slate-300 mt-1">Colores oficiales y acabado suave al tacto de larga duración.</p>
        </div>

        <div class="glass-box rounded-2xl p-4 group transition duration-300">
          <div class="aspect-square rounded-xl overflow-hidden mb-3 bg-slate-900">
            <img src="assets/images/llaveros-tenis-azul-blanco.jpg" alt="Llaveros de raqueta de tenis" class="w-full h-full object-cover group-hover:scale-110 transition duration-500">
          </div>
          <span class="text-[10px] font-bold text-cool-cyan uppercase tracking-wider">Tenis & Raqueta</span>
          <h3 class="font-bold text-white text-base">Cordaje Detallado Pro</h3>
          <p class="text-xs text-slate-300 mt-1">Perfecto para clubes polideportivos y academias de tenis.</p>
        </div>

        <div class="glass-box rounded-2xl p-4 group transition duration-300">
          <div class="aspect-square rounded-xl overflow-hidden mb-3 bg-slate-900">
            <img src="assets/images/llaveros-tenis-rojo-morado.jpg" alt="Llaveros personalizados para torneos" class="w-full h-full object-cover group-hover:scale-110 transition duration-500">
          </div>
          <span class="text-[10px] font-bold text-yellow-400 uppercase tracking-wider">Edición Torneo</span>
          <h3 class="font-bold text-white text-base">Grips y Colores Flúor</h3>
          <p class="text-xs text-slate-300 mt-1">Personalización completa en tiradas desde 50 unidades.</p>
        </div>

      </div>

      <!-- CALCULADORA DE PRESUPUESTO EXPRESS -->
      <div class="max-w-3xl mx-auto glass-box rounded-3xl p-8 sm:p-10 border border-cool-orange/40 shadow-2xl">
        <div class="text-center space-y-2 mb-8">
          <h3 class="text-2xl sm:text-3xl font-black font-heading text-white">Calcula el pedido de tu Club</h3>
          <p class="text-xs sm:text-sm text-slate-300">Muestra digital 3D 100% gratuita y sin compromiso antes de fabricar.</p>
        </div>

        <div class="space-y-6">
          <div>
            <div class="flex justify-between items-center mb-2">
              <label class="text-sm font-bold text-white">Cantidad estimada:</label>
              <span id="calc-qty-badge" class="px-3 py-1 rounded-lg bg-cool-orange text-white font-black text-sm">100 unidades</span>
            </div>
            <input type="range" id="calc-slider" min="50" max="1000" step="50" value="100" class="w-full h-2.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-cool-orange">
          </div>

          <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 text-center">
            <div class="bg-cool-navy/80 p-3 rounded-xl border border-slate-700">
              <span class="text-[10px] text-slate-400 block">Diseño 3D</span>
              <strong class="text-emerald-400 text-sm">GRATIS</strong>
            </div>
            <div class="bg-cool-navy/80 p-3 rounded-xl border border-slate-700">
              <span class="text-[10px] text-slate-400 block">Plazo</span>
              <strong class="text-white text-sm">10-14 días</strong>
            </div>
            <div class="bg-cool-navy/80 p-3 rounded-xl border border-slate-700">
              <span class="text-[10px] text-slate-400 block">Envío</span>
              <strong class="text-cool-cyan text-sm">Toda Europa</strong>
            </div>
            <div class="bg-cool-navy/80 p-3 rounded-xl border border-slate-700">
              <span class="text-[10px] text-slate-400 block">Mínimo</span>
              <strong class="text-yellow-400 text-sm">50 uds</strong>
            </div>
          </div>

          <a id="calc-wa-btn" href="https://wa.me/34680317486?text=Hola%20Javier,%20quiero%20muestra%203D%20para%20100%20llaveros%20de%20mi%20club" target="_blank" class="w-full py-4 rounded-xl font-heading font-black text-sm sm:text-base bg-gradient-to-r from-cool-orange to-cool-amber text-white shadow-xl flex items-center justify-center gap-2 hover:scale-[1.02] transition">
            <i data-lucide="send" class="w-5 h-5"></i> Pedir Simulación 3D de mi Escudo por WhatsApp
          </a>
        </div>
      </div>

    </div>
  </section>

  <!-- SECCIÓN DETALLADA: SAVE MY PLAY -->
  <section id="savemyplay" class="py-20 bg-slate-950/60 relative border-t border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="glass-box rounded-3xl p-8 sm:p-12 border border-emerald-500/40">
        <div class="grid lg:grid-cols-12 gap-8 items-center">
          
          <div class="lg:col-span-8 space-y-5">
            <span class="px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-400 text-xs font-bold uppercase tracking-wider">
              Smart Courts & IA en Pista
            </span>

            <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black font-heading text-white">
              Cámaras con IA para tus pistas: <span class="text-emerald-400">Save my Play</span>
            </h2>

            <p class="text-slate-200 text-base leading-relaxed">
              Como partner oficial de <strong>Save my Play</strong>, ayudamos a los gerentes de club a instalar tecnología que fideliza: cámaras inteligentes que graban partidos en directo y permiten a los jugadores descargar sus mejores jugadas en segundos con un clic.
            </p>

            <div class="grid sm:grid-cols-2 gap-4 pt-2">
              <div class="flex items-center gap-3 text-sm text-slate-200">
                <i data-lucide="check-circle-2" class="w-5 h-5 text-emerald-400 flex-shrink-0"></i>
                <span>Viralidad en Instagram & TikTok</span>
              </div>
              <div class="flex items-center gap-3 text-sm text-slate-200">
                <i data-lucide="check-circle-2" class="w-5 h-5 text-emerald-400 flex-shrink-0"></i>
                <span>Aumenta ocupación en horas valle</span>
              </div>
              <div class="flex items-center gap-3 text-sm text-slate-200">
                <i data-lucide="check-circle-2" class="w-5 h-5 text-emerald-400 flex-shrink-0"></i>
                <span>Instalación rápida sin obras</span>
              </div>
              <div class="flex items-center gap-3 text-sm text-slate-200">
                <i data-lucide="check-circle-2" class="w-5 h-5 text-emerald-400 flex-shrink-0"></i>
                <span>Integración con SportAI</span>
              </div>
            </div>

            <div class="pt-4 flex flex-wrap gap-4">
              <a href="https://wa.me/34680317486?text=Hola%20Javier" 
                 target="_blank" 
                 class="px-6 py-3.5 rounded-xl font-heading font-bold text-sm bg-emerald-500 hover:bg-emerald-600 text-white shadow-lg transition flex items-center gap-2">
                <i data-lucide="message-square" class="w-4 h-4"></i> Solicitar Demo para mi Club
              </a>
            </div>
          </div>

          <div class="lg:col-span-4 bg-cool-navy/90 p-6 sm:p-8 rounded-2xl border border-slate-700 text-center space-y-4">
            <div class="w-16 h-16 rounded-2xl bg-emerald-500 text-white flex items-center justify-center mx-auto shadow-xl">
              <i data-lucide="video" class="w-8 h-8"></i>
            </div>
            <h3 class="font-heading font-black text-xl text-white">¿Quieres ver cómo funciona en directo?</h3>
            <p class="text-xs text-slate-300">Te mostramos vídeos reales de jugadas grabadas en clubes con Save my Play.</p>
            <a href="https://wa.me/34680317486?text=Hola%20Javier,%20p%C3%A1same%20un%20v%C3%ADdeo%20de%20ejemplo%20de%20Save%20my%20Play" target="_blank" class="block w-full py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-cool-cyan text-xs font-bold transition">
              Ver Vídeos de Ejemplo
            </a>
          </div>

        </div>
      </div>

    </div>
  </section>

  <!-- SECCIÓN: INFORME DEL NEGOCIO DEL PÁDEL -->
  <section id="informe" class="py-20 relative border-t border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-8">
      
      <div class="max-w-3xl mx-auto space-y-3">
        <span class="px-3 py-1 rounded-full bg-yellow-500/20 text-yellow-400 text-xs font-bold uppercase tracking-wider">
          Padel World Summit & RacquetX Miami
        </span>
        <h2 class="text-3xl sm:text-5xl font-black font-heading text-white">
          "How is the Padel Business playing out?"
        </h2>
        <p class="text-slate-200 text-base">
          Conclusiones reales tras conversar con más de 116 stands del sector: pistas inteligentes, expansión en EEUU, modelo de clubs lifestyle y claves para marcas.
        </p>
      </div>

      <div class="max-w-xl mx-auto glass-box rounded-3xl p-8 border border-cool-cyan/40 text-center space-y-4 shadow-2xl">
        <i data-lucide="file-check-2" class="w-12 h-12 text-cool-orange mx-auto"></i>
        <h3 class="font-heading font-black text-2xl text-white">Descarga el Informe en PDF</h3>
        <p class="text-xs text-slate-300">Documento completo con todas las diapositivas y recomendaciones para clubs y marcas deportivas.</p>
        <a href="assets/padel-industry-report-coolpadel.pdf" download target="_blank" class="inline-flex items-center gap-2 px-8 py-3.5 rounded-xl font-heading font-bold text-sm bg-gradient-to-r from-cool-orange to-cool-amber text-white shadow-xl hover:scale-105 transition">
          <i data-lucide="download" class="w-4 h-4"></i> Descargar PDF Gratis (8.5 MB)
        </a>
      </div>

    </div>
  </section>

  <!-- SECCIÓN: SOBRE JAVIER VILLORIA -->
  <section id="sobre-javier" class="py-20 bg-slate-950/60 relative border-t border-slate-800">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-6">
      <div class="w-20 h-20 rounded-full bg-gradient-to-tr from-cool-orange to-cool-amber text-white font-heading font-black text-2xl flex items-center justify-center mx-auto shadow-xl">
        JV
      </div>
      <h2 class="text-3xl font-black font-heading text-white">Javier Villoria Soleto</h2>
      <p class="text-xs font-bold text-cool-cyan uppercase tracking-widest -mt-4">Fundador de CoolPadel · Consultor de Ecosistema Pádel</p>
      <p class="text-slate-300 text-base leading-relaxed max-w-2xl mx-auto">
        "Fundé CoolPadel combinando mi pasión por el deporte con la fabricación de merchandising de máxima calidad. Hoy trabajamos con más de 30 clubes y marcas en Europa y colaboro con Save my Play para acercar la innovación a cada pista."
      </p>
      <div class="pt-2">
        <a href="https://wa.me/34680317486?text=Hola%20Javier,%20me%20gustar%C3%ADa%20hablar%20contigo" target="_blank" class="inline-flex items-center gap-2 px-6 py-3 rounded-xl font-bold text-sm bg-cool-card border border-slate-700 hover:border-cool-cyan text-white transition">
          <i data-lucide="message-circle" class="w-4 h-4 text-cool-cyan"></i> Hablar directamente con Javier
        </a>
      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="bg-slate-950 border-t border-slate-800 py-10 text-center text-xs text-slate-500">
    <div class="max-w-7xl mx-auto px-4 space-y-2">
      <p>© 2026 CoolPadel. Ecosistema de Merchandising y Soluciones para Clubs de Pádel.</p>
      <p>Diseñado con pasión por el pádel.</p>
    </div>
  </footer>

  <!-- BOTÓN FLOTANTE DE WHATSAPP -->
  <a href="https://wa.me/34680317486?text=Hola%20Javier" 
     target="_blank" 
     class="fixed bottom-6 right-6 z-50 p-4 rounded-full bg-emerald-500 text-white shadow-2xl hover:bg-emerald-600 hover:scale-110 active:scale-95 transition flex items-center justify-center group"
     title="Hablar por WhatsApp con Javier">
    <i data-lucide="message-circle" class="w-7 h-7"></i>
    <span class="max-w-0 overflow-hidden whitespace-nowrap group-hover:max-w-xs transition-all duration-300 ease-in-out text-xs font-bold px-0 group-hover:px-2">
      ¿Hablamos de tu club?
    </span>
  </a>

  <!-- SCRIPTS -->
  <script>
    lucide.createIcons();

    const slider = document.getElementById('calc-slider');
    const badge = document.getElementById('calc-qty-badge');
    const waBtn = document.getElementById('calc-wa-btn');

    slider.addEventListener('input', (e) => {
      const val = e.target.value;
      badge.textContent = `${val} unidades`;
      const msg = `Hola Javier, quiero muestra 3D gratuita para ${val} llaveros de mi club.`;
      waBtn.href = `https://wa.me/34680317486?text=${encodeURIComponent(msg)}`;
    });
  </script>
</body>
</html>"""

    out_dir = os.path.join(os.getcwd(), "coolpadel-web")
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Propuesta 1 refinada generada exitosamente en index.html")

if __name__ == "__main__":
    build_p1_refined()
