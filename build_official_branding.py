import os

def build_site_with_official_branding():
    html = """<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CoolPadel | Llaveros Personalizados & Soluciones para Clubs de Pádel</title>
  <meta name="description" content="Ecosistema de merchandising y tecnología para clubes de pádel: llaveros personalizados, Save my Play y consultoría del sector de raqueta.">
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
              navy: '#091322',
              dark: '#0e1d33',
              card: '#132845',
              blue: '#0284c7',
              cyan: '#38bdf8',
              orange: '#f97316',
              amber: '#fb923c'
            }
          },
          animation: {
            'ticker-slow': 'tickerSlow 30s linear infinite',
            'ticker-trusted': 'tickerSlow 25s linear infinite',
          },
          keyframes: {
            tickerSlow: {
              '0%': { transform: 'translateX(0%)' },
              '100%': { transform: 'translateX(-50%)' }
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
    
    .ticker-wrap {
      width: 100%;
      overflow: hidden;
      white-space: nowrap;
    }
    .ticker-content {
      display: inline-flex;
      white-space: nowrap;
    }

    /* Nike style slider */
    .slider-track {
      display: flex;
      transition: transform 0.6s cubic-bezier(0.25, 1, 0.5, 1);
    }
    .slide-item {
      min-width: 100%;
      flex-shrink: 0;
    }

    .glass-card-clean {
      background: rgba(14, 29, 51, 0.75);
      backdrop-filter: blur(12px);
      border: 1px solid rgba(56, 189, 248, 0.18);
    }
  </style>
</head>
<body class="bg-[#0b1626] text-slate-100 min-h-screen relative selection:bg-cool-orange selection:text-white overflow-x-hidden">

  <!-- 1. TOP BAR NEGRA: SOLO INFORME EN BUCLE ESPACIADO -->
  <div class="bg-black border-b border-neutral-800 py-2.5 ticker-wrap text-xs text-neutral-200 tracking-wider z-50 relative">
    <div class="ticker-content animate-ticker-slow flex items-center font-medium">
      
      <a href="#informe" class="inline-flex items-center hover:text-white transition px-8">
        <span class="w-1.5 h-1.5 rounded-full bg-cool-orange mr-3"></span>
        <span>Descarga el informe exclusivo sobre la industria del padel</span>
      </a>
      <span class="text-neutral-600">·</span>

      <a href="#informe" class="inline-flex items-center hover:text-white transition px-8">
        <span class="w-1.5 h-1.5 rounded-full bg-cool-cyan mr-3"></span>
        <span>Descarga el informe exclusivo sobre la industria del padel</span>
      </a>
      <span class="text-neutral-600">·</span>

      <a href="#informe" class="inline-flex items-center hover:text-white transition px-8">
        <span class="w-1.5 h-1.5 rounded-full bg-cool-orange mr-3"></span>
        <span>Descarga el informe exclusivo sobre la industria del padel</span>
      </a>
      <span class="text-neutral-600">·</span>

      <a href="#informe" class="inline-flex items-center hover:text-white transition px-8">
        <span class="w-1.5 h-1.5 rounded-full bg-cool-cyan mr-3"></span>
        <span>Descarga el informe exclusivo sobre la industria del padel</span>
      </a>
      <span class="text-neutral-600">·</span>

      <!-- DUPLICADO EXACTO PARA BUCLE INFINITO SUAVE -->
      <a href="#informe" class="inline-flex items-center hover:text-white transition px-8">
        <span class="w-1.5 h-1.5 rounded-full bg-cool-orange mr-3"></span>
        <span>Descarga el informe exclusivo sobre la industria del padel</span>
      </a>
      <span class="text-neutral-600">·</span>

      <a href="#informe" class="inline-flex items-center hover:text-white transition px-8">
        <span class="w-1.5 h-1.5 rounded-full bg-cool-cyan mr-3"></span>
        <span>Descarga el informe exclusivo sobre la industria del padel</span>
      </a>
      <span class="text-neutral-600">·</span>

      <a href="#informe" class="inline-flex items-center hover:text-white transition px-8">
        <span class="w-1.5 h-1.5 rounded-full bg-cool-orange mr-3"></span>
        <span>Descarga el informe exclusivo sobre la industria del padel</span>
      </a>
      <span class="text-neutral-600">·</span>

      <a href="#informe" class="inline-flex items-center hover:text-white transition px-8">
        <span class="w-1.5 h-1.5 rounded-full bg-cool-cyan mr-3"></span>
        <span>Descarga el informe exclusivo sobre la industria del padel</span>
      </a>
      <span class="text-neutral-600">·</span>

    </div>
  </div>

  <!-- 2. NAVBAR BLANCA ESTILO NIKE: MASCOTA + LETRAS OFICIALES -->
  <header class="sticky top-0 z-40 bg-white text-slate-900 border-b border-slate-200 shadow-md">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
      
      <!-- LOGO: MASCOTA A LA IZQUIERDA Y LETRAS A LA DERECHA -->
      <a href="#" class="flex items-center gap-2 sm:gap-3 group py-2">
        <img src="assets/images/coolpadel-mascot.png" alt="Mascota CoolPadel" class="h-11 sm:h-12 w-auto object-contain group-hover:scale-105 transition">
        <img src="assets/images/coolpadel-typography.png" alt="CoolPadel" class="h-6 sm:h-7 w-auto object-contain">
      </a>

      <!-- NAV LINKS (CENTRADOS) -->
      <nav class="hidden md:flex items-center gap-8 text-sm font-bold text-slate-800">
        <a href="#llaveros" class="hover:text-cool-orange transition flex items-center gap-1.5">
          <i data-lucide="key" class="w-4 h-4 text-cool-orange"></i> Llaveros Clubs
        </a>
        <a href="#savemyplay" class="hover:text-cool-orange transition flex items-center gap-1.5">
          <i data-lucide="video" class="w-4 h-4 text-emerald-600"></i> Save my Play (IA)
        </a>
        <a href="#informe" class="hover:text-cool-orange transition flex items-center gap-1.5">
          <i data-lucide="file-text" class="w-4 h-4 text-yellow-600"></i> Blog & Informe
        </a>
        <a href="#sobre-javier" class="hover:text-cool-orange transition flex items-center gap-1.5">
          <i data-lucide="user" class="w-4 h-4 text-cool-blue"></i> Sobre Javier
        </a>
      </nav>

      <!-- CTA BUTTON -->
      <div class="flex items-center gap-3">
        <a href="https://wa.me/34680317486?text=Hola%20Javier" 
           target="_blank" 
           class="px-5 py-2.5 rounded-full font-heading font-black text-xs sm:text-sm bg-black text-white hover:bg-neutral-800 active:scale-95 shadow-md transition flex items-center gap-2">
          <i data-lucide="sparkles" class="w-4 h-4 text-cool-orange"></i> Pedir Muestra Gratis
        </a>
        <button id="mobile-menu-btn" class="md:hidden p-2 text-slate-800 hover:text-black">
          <i data-lucide="menu" class="w-6 h-6"></i>
        </button>
      </div>

    </div>

    <!-- Mobile Menu Dropdown -->
    <div id="mobile-menu" class="hidden md:hidden bg-white border-t border-slate-200 px-6 py-4 space-y-3 font-bold text-sm">
      <a href="#llaveros" class="block py-1 text-slate-800 hover:text-cool-orange">🎾 Llaveros Clubs</a>
      <a href="#savemyplay" class="block py-1 text-slate-800 hover:text-cool-orange">📹 Save my Play (IA)</a>
      <a href="#informe" class="block py-1 text-slate-800 hover:text-cool-orange">📊 Blog & Informe</a>
      <a href="#sobre-javier" class="block py-1 text-slate-800 hover:text-cool-orange">👤 Sobre Javier</a>
    </div>
  </header>

  <!-- 3. HERO SLIDER ESTILO NIKE (3 PANTALLAS ROTANDO) -->
  <section class="relative bg-black overflow-hidden select-none">
    
    <div id="slider-container" class="relative w-full overflow-hidden">
      
      <!-- Slider Track -->
      <div id="slider-track" class="slider-track">
        
        <!-- SLIDE 1: LLAVEROS PARA CLUBS -->
        <div class="slide-item relative h-[600px] sm:h-[700px] lg:h-[760px] cursor-pointer" onclick="document.querySelector('#llaveros').scrollIntoView({behavior: 'smooth'})">
          <img src="assets/images/llaveros-padel-azul.png" alt="Llaveros de pádel CoolPadel" class="w-full h-full object-cover">
          <div class="absolute inset-0 bg-gradient-to-t from-black via-black/35 to-transparent"></div>
          <div class="absolute inset-0 bg-gradient-to-r from-black/80 via-black/20 to-transparent"></div>

          <!-- Slide Content (Bottom Left Nike Layout) -->
          <div class="absolute bottom-12 sm:bottom-16 left-6 sm:left-12 lg:left-20 max-w-2xl space-y-4">
            <span class="inline-block px-3 py-1 rounded bg-cool-orange text-white text-[11px] font-black uppercase tracking-widest">
              Merchandising Exclusivo
            </span>
            <h1 class="text-4xl sm:text-6xl lg:text-7xl font-black font-heading text-white uppercase tracking-tight leading-[1.05]">
              LLAVEROS QUE CREAN <br>
              <span class="text-cool-cyan">COMUNIDAD DE CLUB</span>
            </h1>
            <p class="text-sm sm:text-lg text-neutral-200 font-medium max-w-lg leading-relaxed">
              El detalle con el escudo y colores de tu club que tus jugadores llevarán siempre en el paletero.
            </p>
            <div class="pt-2">
              <a href="#llaveros" class="inline-flex items-center gap-2 px-7 py-3.5 rounded-full bg-white text-black font-heading font-black text-sm hover:bg-neutral-200 transition shadow-2xl">
                Ver Llaveros y Pedir Muestra <i data-lucide="arrow-right" class="w-4 h-4"></i>
              </a>
            </div>
          </div>
        </div>

        <!-- SLIDE 2: SAVE MY PLAY (CÁMARAS IA) -->
        <div class="slide-item relative h-[600px] sm:h-[700px] lg:h-[760px] cursor-pointer" onclick="document.querySelector('#savemyplay').scrollIntoView({behavior: 'smooth'})">
          <img src="assets/images/background-fair.jpg" alt="Save my Play cámaras inteligentes de pádel" class="w-full h-full object-cover filter brightness-90">
          <div class="absolute inset-0 bg-gradient-to-t from-black via-black/40 to-transparent"></div>
          <div class="absolute inset-0 bg-gradient-to-r from-black/85 via-black/25 to-transparent"></div>

          <div class="absolute bottom-12 sm:bottom-16 left-6 sm:left-12 lg:left-20 max-w-2xl space-y-4">
            <span class="inline-block px-3 py-1 rounded bg-emerald-500 text-white text-[11px] font-black uppercase tracking-widest">
              Smart Courts & Partner Oficial
            </span>
            <h2 class="text-4xl sm:text-6xl lg:text-7xl font-black font-heading text-white uppercase tracking-tight leading-[1.05]">
              SAVE MY PLAY: <br>
              <span class="text-emerald-400">CÁMARAS CON IA</span>
            </h2>
            <p class="text-sm sm:text-lg text-neutral-200 font-medium max-w-lg leading-relaxed">
              Tus jugadores graban sus mejores puntos con un clic y los comparten en redes llenando tus pistas en horas valle.
            </p>
            <div class="pt-2">
              <a href="#savemyplay" class="inline-flex items-center gap-2 px-7 py-3.5 rounded-full bg-emerald-500 text-white font-heading font-black text-sm hover:bg-emerald-600 transition shadow-2xl">
                Descubrir Save my Play <i data-lucide="arrow-right" class="w-4 h-4"></i>
              </a>
            </div>
          </div>
        </div>

        <!-- SLIDE 3: BLOG & INFORME DEL NEGOCIO DEL PÁDEL -->
        <div class="slide-item relative h-[600px] sm:h-[700px] lg:h-[760px] cursor-pointer" onclick="document.querySelector('#informe').scrollIntoView({behavior: 'smooth'})">
          <img src="assets/images/background-fair.jpg" alt="Informe de la industria del pádel" class="w-full h-full object-cover filter contrast-110 brightness-75">
          <div class="absolute inset-0 bg-gradient-to-t from-black via-black/50 to-transparent"></div>
          <div class="absolute inset-0 bg-gradient-to-r from-black/90 via-black/30 to-transparent"></div>

          <div class="absolute bottom-12 sm:bottom-16 left-6 sm:left-12 lg:left-20 max-w-2xl space-y-4">
            <span class="inline-block px-3 py-1 rounded bg-yellow-400 text-black text-[11px] font-black uppercase tracking-widest">
              Industry Insights & Análisis
            </span>
            <h2 class="text-4xl sm:text-6xl lg:text-7xl font-black font-heading text-white uppercase tracking-tight leading-[1.05]">
              CÓMO ESTÁ EL <br>
              <span class="text-yellow-400">NEGOCIO DEL PÁDEL</span>
            </h2>
            <p class="text-sm sm:text-lg text-neutral-200 font-medium max-w-lg leading-relaxed">
              Conclusiones del Padel World Summit y RacquetX Miami: qué funciona y qué errores evitar en tu club.
            </p>
            <div class="pt-2">
              <a href="#informe" class="inline-flex items-center gap-2 px-7 py-3.5 rounded-full bg-yellow-400 text-black font-heading font-black text-sm hover:bg-yellow-500 transition shadow-2xl">
                Descargar Informe en PDF <i data-lucide="download" class="w-4 h-4"></i>
              </a>
            </div>
          </div>
        </div>

      </div>

      <!-- CONTROLES DEL SLIDER -->
      <div class="absolute bottom-8 right-6 sm:right-12 z-30 flex items-center gap-4">
        <!-- Dots -->
        <div class="flex items-center gap-2">
          <button class="slider-dot w-3 h-3 rounded-full bg-white transition-all" data-index="0"></button>
          <button class="slider-dot w-3 h-3 rounded-full bg-white/40 transition-all" data-index="1"></button>
          <button class="slider-dot w-3 h-3 rounded-full bg-white/40 transition-all" data-index="2"></button>
        </div>

        <!-- Arrows -->
        <div class="flex items-center gap-2">
          <button id="prev-slide-btn" class="w-10 h-10 rounded-full bg-neutral-900/80 hover:bg-neutral-800 text-white flex items-center justify-center border border-neutral-700 backdrop-blur-sm transition">
            <i data-lucide="chevron-left" class="w-5 h-5"></i>
          </button>
          <button id="next-slide-btn" class="w-10 h-10 rounded-full bg-neutral-900/80 hover:bg-neutral-800 text-white flex items-center justify-center border border-neutral-700 backdrop-blur-sm transition">
            <i data-lucide="chevron-right" class="w-5 h-5"></i>
          </button>
        </div>
      </div>

    </div>

  </section>

  <!-- 4. CARROUSEL PASARELA "TRUSTED BY" -->
  <section class="py-8 bg-neutral-950 border-b border-neutral-800 overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 mb-3 text-center">
      <p class="text-[11px] uppercase tracking-widest font-black text-neutral-400">
        TRUSTED BY · MÁS DE 30 CLUBS, MARCAS Y FEDERACIONES
      </p>
    </div>

    <div class="ticker-wrap py-2">
      <div class="ticker-content animate-ticker-trusted flex items-center gap-12 text-slate-300 text-sm font-black font-heading tracking-wider">
        
        <div class="flex items-center gap-3 px-5 py-2.5 rounded-xl bg-neutral-900 border border-neutral-800">
          <i data-lucide="shield" class="w-5 h-5 text-cool-orange"></i>
          <span>AUSTRIAN PADEL UNION</span>
        </div>
        <div class="flex items-center gap-3 px-5 py-2.5 rounded-xl bg-neutral-900 border border-neutral-800">
          <i data-lucide="trophy" class="w-5 h-5 text-cool-cyan"></i>
          <span>CLUB PADEL VILAMALLA</span>
        </div>
        <div class="flex items-center gap-3 px-5 py-2.5 rounded-xl bg-neutral-900 border border-neutral-800">
          <i data-lucide="activity" class="w-5 h-5 text-yellow-400"></i>
          <span>RETCL TENNIS CLUB</span>
        </div>
        <div class="flex items-center gap-3 px-5 py-2.5 rounded-xl bg-neutral-900 border border-neutral-800">
          <i data-lucide="award" class="w-5 h-5 text-emerald-400"></i>
          <span>PADEL ADDICT</span>
        </div>
        <div class="flex items-center gap-3 px-5 py-2.5 rounded-xl bg-neutral-900 border border-neutral-800">
          <i data-lucide="play" class="w-5 h-5 text-emerald-400"></i>
          <span>SAVE MY PLAY</span>
        </div>
        <div class="flex items-center gap-3 px-5 py-2.5 rounded-xl bg-neutral-900 border border-neutral-800">
          <i data-lucide="star" class="w-5 h-5 text-cool-orange"></i>
          <span>USA PADEL EXPANSION</span>
        </div>

        <!-- DUPLICATE -->
        <div class="flex items-center gap-3 px-5 py-2.5 rounded-xl bg-neutral-900 border border-neutral-800">
          <i data-lucide="shield" class="w-5 h-5 text-cool-orange"></i>
          <span>AUSTRIAN PADEL UNION</span>
        </div>
        <div class="flex items-center gap-3 px-5 py-2.5 rounded-xl bg-neutral-900 border border-neutral-800">
          <i data-lucide="trophy" class="w-5 h-5 text-cool-cyan"></i>
          <span>CLUB PADEL VILAMALLA</span>
        </div>
        <div class="flex items-center gap-3 px-5 py-2.5 rounded-xl bg-neutral-900 border border-neutral-800">
          <i data-lucide="activity" class="w-5 h-5 text-yellow-400"></i>
          <span>RETCL TENNIS CLUB</span>
        </div>
        <div class="flex items-center gap-3 px-5 py-2.5 rounded-xl bg-neutral-900 border border-neutral-800">
          <i data-lucide="award" class="w-5 h-5 text-emerald-400"></i>
          <span>PADEL ADDICT</span>
        </div>
        <div class="flex items-center gap-3 px-5 py-2.5 rounded-xl bg-neutral-900 border border-neutral-800">
          <i data-lucide="play" class="w-5 h-5 text-emerald-400"></i>
          <span>SAVE MY PLAY</span>
        </div>
        <div class="flex items-center gap-3 px-5 py-2.5 rounded-xl bg-neutral-900 border border-neutral-800">
          <i data-lucide="star" class="w-5 h-5 text-cool-orange"></i>
          <span>USA PADEL EXPANSION</span>
        </div>

      </div>
    </div>
  </section>

  <!-- 5. SECCIÓN DETALLADA: LLAVEROS PARA CLUBS -->
  <section id="llaveros" class="py-24 bg-cool-navy relative border-b border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-4">
        <span class="inline-block px-3 py-1 rounded-full bg-cool-orange/20 text-cool-orange text-xs font-bold uppercase tracking-wider">
          Pilar 01 · Merchandising Premium
        </span>
        <h2 class="text-3xl sm:text-5xl font-black font-heading text-white">
          Llaveros Personalizados con el Escudo de tu Club
        </h2>
        <p class="text-slate-300 text-base sm:text-lg">
          Tus socios lo usarán a diario en las llaves o en el paletero. Resistentes, ligeros y con relieve 3D.
        </p>
      </div>

      <!-- GALERÍA DE 4 FOTOS REALES -->
      <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-16">
        
        <div class="glass-card-clean rounded-2xl p-4 group transition duration-300 hover:-translate-y-1">
          <div class="aspect-square rounded-xl overflow-hidden mb-3 bg-slate-900">
            <img src="assets/images/llaveros-padel-azul.png" alt="Llaveros de pádel para clubs" class="w-full h-full object-cover group-hover:scale-110 transition duration-500">
          </div>
          <span class="text-[10px] font-bold text-cool-cyan uppercase tracking-wider">Pádel Custom</span>
          <h3 class="font-bold text-white text-base">Pala Pádel Doble Cara</h3>
          <p class="text-xs text-slate-400 mt-1">Escudo en relieve, micro-perforaciones y marco protector.</p>
        </div>

        <div class="glass-card-clean rounded-2xl p-4 group transition duration-300 hover:-translate-y-1">
          <div class="aspect-square rounded-xl overflow-hidden mb-3 bg-slate-900">
            <img src="assets/images/llavero-austrian-padel.jpg" alt="Llavero Austrian Padel Union" class="w-full h-full object-cover group-hover:scale-110 transition duration-500">
          </div>
          <span class="text-[10px] font-bold text-cool-orange uppercase tracking-wider">Federaciones</span>
          <h3 class="font-bold text-white text-base">Austrian Padel Union</h3>
          <p class="text-xs text-slate-400 mt-1">Colores oficiales y acabado suave al tacto de larga duración.</p>
        </div>

        <div class="glass-card-clean rounded-2xl p-4 group transition duration-300 hover:-translate-y-1">
          <div class="aspect-square rounded-xl overflow-hidden mb-3 bg-slate-900">
            <img src="assets/images/llaveros-tenis-azul-blanco.jpg" alt="Llaveros de raqueta de tenis" class="w-full h-full object-cover group-hover:scale-110 transition duration-500">
          </div>
          <span class="text-[10px] font-bold text-cool-cyan uppercase tracking-wider">Tenis & Raqueta</span>
          <h3 class="font-bold text-white text-base">Cordaje Detallado Pro</h3>
          <p class="text-xs text-slate-400 mt-1">Perfecto para clubes polideportivos y academias de tenis.</p>
        </div>

        <div class="glass-card-clean rounded-2xl p-4 group transition duration-300 hover:-translate-y-1">
          <div class="aspect-square rounded-xl overflow-hidden mb-3 bg-slate-900">
            <img src="assets/images/llaveros-tenis-rojo-morado.jpg" alt="Llaveros personalizados para torneos" class="w-full h-full object-cover group-hover:scale-110 transition duration-500">
          </div>
          <span class="text-[10px] font-bold text-yellow-400 uppercase tracking-wider">Edición Torneo</span>
          <h3 class="font-bold text-white text-base">Grips y Colores Flúor</h3>
          <p class="text-xs text-slate-400 mt-1">Personalización completa en tiradas desde 50 unidades.</p>
        </div>

      </div>

      <!-- CALCULADORA DE PRESUPUESTO EXPRESS -->
      <div class="max-w-3xl mx-auto glass-card-clean rounded-3xl p-8 sm:p-10 border border-cool-orange/40 shadow-2xl">
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
            <div class="bg-cool-dark p-3 rounded-xl border border-slate-700">
              <span class="text-[10px] text-slate-400 block">Diseño 3D</span>
              <strong class="text-emerald-400 text-sm">GRATIS</strong>
            </div>
            <div class="bg-cool-dark p-3 rounded-xl border border-slate-700">
              <span class="text-[10px] text-slate-400 block">Plazo</span>
              <strong class="text-white text-sm">10-14 días</strong>
            </div>
            <div class="bg-cool-dark p-3 rounded-xl border border-slate-700">
              <span class="text-[10px] text-slate-400 block">Envío</span>
              <strong class="text-cool-cyan text-sm">Toda Europa</strong>
            </div>
            <div class="bg-cool-dark p-3 rounded-xl border border-slate-700">
              <span class="text-[10px] text-slate-400 block">Mínimo</span>
              <strong class="text-yellow-400 text-sm">50 uds</strong>
            </div>
          </div>

          <a id="calc-wa-btn" href="https://wa.me/34680317486?text=Hola%20Javier,%20quiero%20muestra%203D%20para%20100%20llaveros%20de%20mi%20club" target="_blank" class="w-full py-4 rounded-xl font-heading font-black text-sm sm:text-base bg-gradient-to-r from-cool-orange to-cool-amber text-white shadow-xl flex items-center justify-center gap-2 hover:scale-[1.01] transition">
            <i data-lucide="send" class="w-5 h-5"></i> Pedir Simulación 3D de mi Escudo por WhatsApp
          </a>
        </div>
      </div>

    </div>
  </section>

  <!-- 6. SECCIÓN DETALLADA: SAVE MY PLAY -->
  <section id="savemyplay" class="py-24 bg-cool-dark relative border-b border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="glass-card-clean rounded-3xl p-8 sm:p-12 border border-emerald-500/40">
        <div class="grid lg:grid-cols-12 gap-8 items-center">
          
          <div class="lg:col-span-8 space-y-5">
            <span class="px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-400 text-xs font-bold uppercase tracking-wider">
              Pilar 02 · Smart Courts & IA en Pista
            </span>

            <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black font-heading text-white">
              Cámaras con IA para tus pistas: <span class="text-emerald-400">Save my Play</span>
            </h2>

            <p class="text-slate-300 text-base leading-relaxed">
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

          <div class="lg:col-span-4 bg-cool-navy p-6 sm:p-8 rounded-2xl border border-slate-700 text-center space-y-4">
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

  <!-- 7. SECCIÓN DETALLADA: INFORME DEL NEGOCIO DEL PÁDEL & BLOG -->
  <section id="informe" class="py-24 bg-cool-navy relative border-b border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-8">
      
      <div class="max-w-3xl mx-auto space-y-3">
        <span class="px-3 py-1 rounded-full bg-yellow-500/20 text-yellow-400 text-xs font-bold uppercase tracking-wider">
          Pilar 03 · Padel World Summit & RacquetX Miami
        </span>
        <h2 class="text-3xl sm:text-5xl font-black font-heading text-white">
          "How is the Padel Business playing out?"
        </h2>
        <p class="text-slate-300 text-base">
          Conclusiones reales tras conversar con más de 116 stands del sector: pistas inteligentes, expansión en EEUU, modelo de clubs lifestyle y claves para marcas.
        </p>
      </div>

      <div class="max-w-xl mx-auto glass-card-clean rounded-3xl p-8 border border-cool-cyan/40 text-center space-y-4 shadow-2xl">
        <i data-lucide="file-check-2" class="w-12 h-12 text-cool-orange mx-auto"></i>
        <h3 class="font-heading font-black text-2xl text-white">Descarga el Informe en PDF</h3>
        <p class="text-xs text-slate-300">Documento completo con todas las diapositivas y recomendaciones para clubs y marcas deportivas.</p>
        <a href="assets/padel-industry-report-coolpadel.pdf" download target="_blank" class="inline-flex items-center gap-2 px-8 py-3.5 rounded-xl font-heading font-bold text-sm bg-gradient-to-r from-cool-orange to-cool-amber text-white shadow-xl hover:scale-105 transition">
          <i data-lucide="download" class="w-4 h-4"></i> Descargar PDF Gratis (8.5 MB)
        </a>
      </div>

    </div>
  </section>

  <!-- 8. SECCIÓN: SOBRE JAVIER VILLORIA -->
  <section id="sobre-javier" class="py-24 bg-cool-dark relative border-b border-slate-800">
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
  <footer class="bg-black border-t border-neutral-800 py-10 text-center text-xs text-neutral-400">
    <div class="max-w-7xl mx-auto px-4 flex flex-col items-center space-y-4">
      <div class="flex items-center gap-2">
        <img src="assets/images/coolpadel-mascot.png" alt="CoolPadel" class="h-8 w-auto object-contain">
        <img src="assets/images/coolpadel-typography.png" alt="CoolPadel" class="h-5 w-auto object-contain brightness-125">
      </div>
      <p>© 2026 CoolPadel. Ecosistema de Merchandising y Soluciones para Clubs de Pádel.</p>
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

    // Mobile menu toggle
    const mobileBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    mobileBtn.addEventListener('click', () => {
      mobileMenu.classList.toggle('hidden');
    });

    // NIKE SLIDER SCRIPT
    const track = document.getElementById('slider-track');
    const dots = document.querySelectorAll('.slider-dot');
    const prevBtn = document.getElementById('prev-slide-btn');
    const nextBtn = document.getElementById('next-slide-btn');
    let currentSlide = 0;
    const totalSlides = 3;
    let autoSlideInterval;

    function goToSlide(index) {
      currentSlide = (index + totalSlides) % totalSlides;
      track.style.transform = `translateX(-${currentSlide * 100}%)`;
      
      dots.forEach((dot, idx) => {
        if (idx === currentSlide) {
          dot.classList.remove('bg-white/40');
          dot.classList.add('bg-white', 'w-6');
        } else {
          dot.classList.remove('bg-white', 'w-6');
          dot.classList.add('bg-white/40', 'w-3');
        }
      });
    }

    function nextSlide() {
      goToSlide(currentSlide + 1);
    }

    function prevSlide() {
      goToSlide(currentSlide - 1);
    }

    nextBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      nextSlide();
      resetAutoSlide();
    });

    prevBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      prevSlide();
      resetAutoSlide();
    });

    dots.forEach(dot => {
      dot.addEventListener('click', (e) => {
        e.stopPropagation();
        goToSlide(parseInt(dot.dataset.index));
        resetAutoSlide();
      });
    });

    function startAutoSlide() {
      autoSlideInterval = setInterval(nextSlide, 5000);
    }

    function resetAutoSlide() {
      clearInterval(autoSlideInterval);
      startAutoSlide();
    }

    startAutoSlide();

    // Calculadora presupuesto
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

    out_file = os.path.join(os.getcwd(), "coolpadel-web", "index.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print("Site with official branding updated successfully in coolpadel-web/index.html")

if __name__ == "__main__":
    build_site_with_official_branding()
