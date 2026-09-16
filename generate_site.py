import os

html_content = """<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CoolPadel | Llaveros Personalizados & Ecosistema para Clubs de Pádel</title>
  <meta name="description" content="Ecosistema para clubes de pádel: llaveros personalizados premium para socios y torneos, tecnología Save my Play y consultoría del sector de raqueta.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
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
              navy: '#091426',
              dark: '#0e1f38',
              card: '#132845',
              blue: '#0284c7',
              cyan: '#38bdf8',
              orange: '#f97316',
              amber: '#fb923c',
              yellow: '#facc15',
              gray: '#94a3b8'
            }
          },
          animation: {
            'float-slow': 'float 5s ease-in-out infinite',
            'pulse-glow': 'pulseGlow 2.5s infinite',
          },
          keyframes: {
            float: {
              '0%, 100%': { transform: 'translateY(0px)' },
              '50%': { transform: 'translateY(-10px)' },
            },
            pulseGlow: {
              '0%, 100%': { opacity: '0.6', transform: 'scale(1)' },
              '50%': { opacity: '0.9', transform: 'scale(1.05)' },
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
    .gradient-text-cool {
      background: linear-gradient(135deg, #38bdf8 0%, #f97316 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .glass-card {
      background: rgba(19, 40, 69, 0.7);
      backdrop-filter: blur(12px);
      border: 1px solid rgba(56, 189, 248, 0.15);
    }
    .glass-card-hover:hover {
      border-color: rgba(249, 115, 22, 0.4);
      transform: translateY(-4px);
      box-shadow: 0 15px 30px -10px rgba(2, 132, 199, 0.25);
    }
    .glow-orange { box-shadow: 0 0 25px rgba(249, 115, 22, 0.35); }
  </style>
</head>
<body class="bg-cool-navy text-slate-100 min-h-screen selection:bg-cool-orange selection:text-white relative overflow-x-hidden">

  <!-- Glow background elements -->
  <div class="fixed top-0 left-1/4 w-96 h-96 bg-cool-blue/15 rounded-full blur-3xl pointer-events-none -z-10 animate-pulse-glow"></div>
  <div class="fixed bottom-1/4 right-10 w-[30rem] h-[30rem] bg-cool-orange/10 rounded-full blur-3xl pointer-events-none -z-10"></div>

  <!-- TOP BAR NOTIFICATION -->
  <div class="bg-gradient-to-r from-cool-dark via-cool-card to-cool-dark border-b border-cool-cyan/15 text-xs text-center py-2 px-4 flex items-center justify-center gap-2">
    <span class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-bold bg-cool-orange text-white">NOVEDAD</span>
    <span class="text-slate-300">Descarga gratis el informe: <strong class="text-white">"How is the Padel Business playing out?"</strong></span>
    <a href="#informe" class="text-cool-cyan underline hover:text-white transition font-medium ml-1 flex items-center gap-1">
      Ver reporte <i data-lucide="arrow-right" class="w-3 h-3"></i>
    </a>
  </div>

  <!-- NAVBAR -->
  <header class="sticky top-0 z-50 bg-cool-navy/90 backdrop-blur-md border-b border-slate-800/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
      
      <!-- LOGO -->
      <a href="#" class="flex items-center gap-3 group">
        <div class="relative w-11 h-11 bg-gradient-to-tr from-cool-blue to-cool-cyan rounded-full flex items-center justify-center p-1 shadow-lg shadow-cool-blue/20 group-hover:scale-105 transition">
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
        <div class="flex flex-col">
          <span class="font-heading font-black text-2xl tracking-tight text-white flex items-center">
            COOL<span class="text-cool-orange">PADEL</span>
          </span>
          <span class="text-[10px] tracking-wider uppercase text-cool-cyan font-bold -mt-1">Ecosistema para Clubs</span>
        </div>
      </a>

      <!-- DESKTOP NAV -->
      <nav class="hidden md:flex items-center gap-8 text-sm font-medium text-slate-300">
        <a href="#llaveros" class="hover:text-cool-cyan transition flex items-center gap-1.5">
          <i data-lucide="key" class="w-4 h-4 text-cool-orange"></i> Llaveros Clubs
        </a>
        <a href="#savemyplay" class="hover:text-cool-cyan transition flex items-center gap-1.5">
          <i data-lucide="video" class="w-4 h-4 text-cool-cyan"></i> Save my Play (IA)
        </a>
        <a href="#informe" class="hover:text-cool-cyan transition flex items-center gap-1.5">
          <i data-lucide="newspaper" class="w-4 h-4 text-yellow-400"></i> Blog & Informe
        </a>
        <a href="#sobre-mi" class="hover:text-cool-cyan transition flex items-center gap-1.5">
          <i data-lucide="user" class="w-4 h-4 text-emerald-400"></i> Sobre Javier
        </a>
      </nav>

      <!-- CTA BUTTON -->
      <div class="flex items-center gap-3">
        <a href="#calculadora" 
           class="hidden sm:inline-flex items-center gap-2 px-4 py-2.5 rounded-xl font-heading font-bold text-sm bg-gradient-to-r from-cool-orange to-cool-amber text-white shadow-lg shadow-cool-orange/25 hover:shadow-cool-orange/40 hover:scale-[1.02] active:scale-[0.98] transition">
          <i data-lucide="sparkles" class="w-4 h-4"></i> Pedir Muestra Gratis
        </a>
        <button id="mobile-menu-btn" class="md:hidden p-2 text-slate-300 hover:text-white rounded-lg bg-cool-card border border-slate-700">
          <i data-lucide="menu" class="w-6 h-6"></i>
        </button>
      </div>
    </div>

    <!-- MOBILE MENU DROPDOWN -->
    <div id="mobile-menu" class="hidden md:hidden bg-cool-dark border-b border-slate-800 px-4 pt-2 pb-6 space-y-3">
      <a href="#llaveros" class="block py-2 text-slate-300 hover:text-cool-cyan">🎾 Llaveros para Clubs</a>
      <a href="#savemyplay" class="block py-2 text-slate-300 hover:text-cool-cyan">📹 Save my Play (Cámaras IA)</a>
      <a href="#informe" class="block py-2 text-slate-300 hover:text-cool-cyan">📊 Blog & Informe del Sector</a>
      <a href="#sobre-mi" class="block py-2 text-slate-300 hover:text-cool-cyan">👤 Sobre Javier</a>
      <a href="#calculadora" class="w-full text-center block py-3 rounded-xl font-bold bg-cool-orange text-white">
        Pedir Muestra Digital Gratis
      </a>
    </div>
  </header>

  <!-- HERO SECTION -->
  <section class="relative pt-12 pb-20 lg:pt-20 lg:pb-32 overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="grid lg:grid-cols-12 gap-12 items-center">
        
        <div class="lg:col-span-7 space-y-6 text-center lg:text-left">
          
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-cool-card border border-cool-cyan/30 text-xs font-semibold text-cool-cyan shadow-sm">
            <span class="w-2 h-2 rounded-full bg-cool-orange animate-ping"></span>
            El Ecosistema para Clubes de Pádel y Tenis
          </div>

          <h1 class="text-4xl sm:text-5xl lg:text-6xl font-black tracking-tight leading-[1.1]">
            Diferencia tu club, <br class="hidden sm:inline">
            fideliza a tus socios y <br>
            <span class="gradient-text-cool">suma innovación</span>.
          </h1>

          <p class="text-lg text-slate-300 max-w-2xl mx-auto lg:mx-0 font-normal leading-relaxed">
            Diseñamos y fabricamos <strong>llaveros personalizados premium</strong> con el escudo y colores de tu club que tus jugadores llevarán con orgullo en su paletero. Además, conectamos a gerentes de club con tecnologías líderes como <strong>Save my Play</strong> para multiplicar el valor de tus pistas.
          </p>

          <div class="pt-2 flex flex-col sm:flex-row items-center justify-center lg:justify-start gap-4">
            <a href="#calculadora" class="w-full sm:w-auto inline-flex items-center justify-center gap-3 px-7 py-4 rounded-2xl font-heading font-extrabold text-base bg-gradient-to-r from-cool-orange to-cool-amber text-white shadow-xl shadow-cool-orange/30 hover:scale-[1.02] active:scale-[0.98] transition">
              <i data-lucide="palette" class="w-5 h-5"></i> Simular Llavero de mi Club
            </a>
            <a href="#savemyplay" class="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-6 py-4 rounded-2xl font-heading font-bold text-base bg-cool-card/90 hover:bg-cool-card border border-slate-700 hover:border-cool-cyan/50 text-slate-200 hover:text-white transition">
              <i data-lucide="play-circle" class="w-5 h-5 text-cool-cyan"></i> Descubrir Save my Play
            </a>
          </div>

          <div class="pt-8 border-t border-slate-800/80 grid grid-cols-3 gap-4 text-center lg:text-left">
            <div>
              <div class="font-heading font-black text-2xl sm:text-3xl text-white">+30</div>
              <div class="text-xs text-slate-400 font-medium">Clubs & Marcas</div>
            </div>
            <div>
              <div class="font-heading font-black text-2xl sm:text-3xl text-cool-orange">100%</div>
              <div class="text-xs text-slate-400 font-medium">Diseño a Medida</div>
            </div>
            <div>
              <div class="font-heading font-black text-2xl sm:text-3xl text-cool-cyan">0 €</div>
              <div class="text-xs text-slate-400 font-medium">Muestra 3D Digital</div>
            </div>
          </div>

        </div>

        <div class="lg:col-span-5 relative">
          <div class="relative mx-auto max-w-md lg:max-w-none">
            <div class="absolute -inset-2 bg-gradient-to-r from-cool-blue via-cool-orange to-cool-cyan rounded-3xl opacity-30 blur-xl"></div>
            
            <div class="relative rounded-3xl overflow-hidden glass-card border border-cool-cyan/30 p-4 shadow-2xl">
              <div class="relative rounded-2xl overflow-hidden aspect-[4/3] bg-slate-900 group">
                <img src="assets/images/llaveros-padel-azul.png" alt="Llaveros personalizados de pádel CoolPadel" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                <div class="absolute inset-0 bg-gradient-to-t from-cool-navy/90 via-transparent to-transparent"></div>
                <div class="absolute bottom-4 left-4 right-4 flex items-center justify-between">
                  <div>
                    <span class="text-[11px] font-bold text-cool-orange uppercase tracking-wider">Edición Club & Marca</span>
                    <h4 class="text-sm font-bold text-white font-heading">Llavero Pala Pádel en Relieve</h4>
                  </div>
                  <span class="px-2.5 py-1 rounded-lg bg-cool-navy/80 border border-cool-cyan/30 text-cool-cyan text-xs font-bold">
                    100% Real
                  </span>
                </div>
              </div>

              <div class="mt-4 grid grid-cols-2 gap-3">
                <div class="rounded-xl p-3 bg-cool-dark/80 border border-slate-700/60 flex items-center gap-3">
                  <div class="w-10 h-10 rounded-lg overflow-hidden flex-shrink-0 bg-slate-800">
                    <img src="assets/images/llavero-austrian-padel.jpg" alt="Austrian Padel Union" class="w-full h-full object-cover">
                  </div>
                  <div class="text-left">
                    <p class="text-xs font-bold text-white leading-tight">Federaciones</p>
                    <p class="text-[10px] text-slate-400">Austrian Padel Union</p>
                  </div>
                </div>

                <div class="rounded-xl p-3 bg-cool-dark/80 border border-slate-700/60 flex items-center gap-3">
                  <div class="w-10 h-10 rounded-lg overflow-hidden flex-shrink-0 bg-slate-800">
                    <img src="assets/images/llaveros-tenis-azul-blanco.jpg" alt="Tenis y Pádel" class="w-full h-full object-cover">
                  </div>
                  <div class="text-left">
                    <p class="text-xs font-bold text-white leading-tight">Tenis & Raqueta</p>
                    <p class="text-[10px] text-slate-400">Detalle Cordaje Pro</p>
                  </div>
                </div>
              </div>

            </div>

          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- SECCIÓN 1: LLAVEROS PARA CLUBS (B2B SHOWCASE) -->
  <section id="llaveros" class="py-20 bg-cool-dark/60 relative border-t border-slate-800/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-4">
        <span class="inline-block px-3 py-1 rounded-full bg-cool-orange/15 text-cool-orange text-xs font-bold uppercase tracking-wider">
          Merchandising Exclusivo para Clubs
        </span>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black font-heading">
          El detalle que tus jugadores <span class="text-cool-orange">no tirarán a la basura</span>
        </h2>
        <p class="text-slate-300 text-base sm:text-lg">
          Los bolígrafos o pulseras baratas se pierden al instante. Un llavero personalizado de pala de pádel o raqueta con los colores exactos de tu club es un regalo con valor percibido altísimo que llevarán colgado en su paletero día tras día.
        </p>
      </div>

      <!-- CASOS DE USO (4 CARDS) -->
      <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-16">
        
        <div class="glass-card rounded-2xl p-6 transition duration-300 glass-card-hover space-y-4">
          <div class="w-12 h-12 rounded-xl bg-cool-blue/20 text-cool-cyan flex items-center justify-center">
            <i data-lucide="gift" class="w-6 h-6"></i>
          </div>
          <h3 class="font-heading font-bold text-xl text-white">Welcome Packs de Torneos</h3>
          <p class="text-slate-400 text-sm leading-relaxed">
            El detalle definitivo en la bolsa de inscripción que hace que los participantes recuerden tu torneo y hablen de tu club.
          </p>
        </div>

        <div class="glass-card rounded-2xl p-6 transition duration-300 glass-card-hover space-y-4">
          <div class="w-12 h-12 rounded-xl bg-cool-orange/20 text-cool-orange flex items-center justify-center">
            <i data-lucide="shield-check" class="w-6 h-6"></i>
          </div>
          <h3 class="font-heading font-bold text-xl text-white">Fidelización de Socios</h3>
          <p class="text-slate-400 text-sm leading-relaxed">
            Regala el llavero al darse de alta o renovar la cuota anual. Fomenta el sentimiento de pertenencia y orgullo de club.
          </p>
        </div>

        <div class="glass-card rounded-2xl p-6 transition duration-300 glass-card-hover space-y-4">
          <div class="w-12 h-12 rounded-xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center">
            <i data-lucide="trending-up" class="w-6 h-6"></i>
          </div>
          <h3 class="font-heading font-bold text-xl text-white">Venta en Tienda (Pro-Shop)</h3>
          <p class="text-slate-400 text-sm leading-relaxed">
            Un producto de compra por impulso en el mostrador con un margen de beneficio superior al 60% para los ingresos del club.
          </p>
        </div>

        <div class="glass-card rounded-2xl p-6 transition duration-300 glass-card-hover space-y-4">
          <div class="w-12 h-12 rounded-xl bg-yellow-500/20 text-yellow-400 flex items-center justify-center">
            <i data-lucide="award" class="w-6 h-6"></i>
          </div>
          <h3 class="font-heading font-bold text-xl text-white">Marcas & Federaciones</h3>
          <p class="text-slate-400 text-sm leading-relaxed">
            Activaciones en stands, regalos VIP a patrocinadores y merchandising corporativo con diseño fiel al milímetro.
          </p>
        </div>

      </div>

      <!-- GALERÍA REAL DE PRODUCTOS -->
      <div class="mb-16">
        <div class="flex items-center justify-between mb-8">
          <div>
            <h3 class="font-heading font-black text-2xl text-white">Trabajos Reales</h3>
            <p class="text-sm text-slate-400">Llaveros creados para federaciones, clubes de pádel, tenis y marcas deportivas</p>
          </div>
          <span class="hidden sm:inline-flex items-center gap-1.5 text-xs text-cool-cyan font-bold bg-cool-card px-3 py-1.5 rounded-lg border border-slate-700">
            <i data-lucide="camera" class="w-4 h-4"></i> Fotos 100% Reales
          </span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          
          <div class="group relative rounded-2xl overflow-hidden glass-card border border-slate-700/60">
            <div class="aspect-[4/3] overflow-hidden">
              <img src="assets/images/llaveros-padel-azul.png" alt="Llaveros de pádel personalizados para clubes" class="w-full h-full object-cover group-hover:scale-110 transition duration-500">
            </div>
            <div class="p-4 bg-cool-card/90">
              <span class="text-[10px] font-bold text-cool-cyan uppercase tracking-wider">Pádel Custom</span>
              <h4 class="font-bold text-white text-sm">Pala Pádel Doble Cara con Logo</h4>
              <p class="text-xs text-slate-400 mt-1">Acabado suave, orificios troquelados y logo en relieve.</p>
            </div>
          </div>

          <div class="group relative rounded-2xl overflow-hidden glass-card border border-slate-700/60">
            <div class="aspect-[4/3] overflow-hidden">
              <img src="assets/images/llavero-austrian-padel.jpg" alt="Llavero Austrian Padel Union" class="w-full h-full object-cover group-hover:scale-110 transition duration-500">
            </div>
            <div class="p-4 bg-cool-card/90">
              <span class="text-[10px] font-bold text-cool-orange uppercase tracking-wider">Federación Oficial</span>
              <h4 class="font-bold text-white text-sm">Austrian Padel Union</h4>
              <p class="text-xs text-slate-400 mt-1">Colores corporativos nacionales y relieve de alta definición.</p>
            </div>
          </div>

          <div class="group relative rounded-2xl overflow-hidden glass-card border border-slate-700/60">
            <div class="aspect-[4/3] overflow-hidden">
              <img src="assets/images/llaveros-tenis-azul-blanco.jpg" alt="Llaveros de raqueta de tenis personalizados" class="w-full h-full object-cover group-hover:scale-110 transition duration-500">
            </div>
            <div class="p-4 bg-cool-card/90">
              <span class="text-[10px] font-bold text-cool-cyan uppercase tracking-wider">Tenis & Rackets</span>
              <h4 class="font-bold text-white text-sm">Raquetas con Cordaje Impreso</h4>
              <p class="text-xs text-slate-400 mt-1">Perfecto para clubes mixtos de tenis y pádel.</p>
            </div>
          </div>

          <div class="group relative rounded-2xl overflow-hidden glass-card border border-slate-700/60">
            <div class="aspect-[4/3] overflow-hidden">
              <img src="assets/images/llaveros-tenis-rojo-morado.jpg" alt="Llaveros personalizados para torneos" class="w-full h-full object-cover group-hover:scale-110 transition duration-500">
            </div>
            <div class="p-4 bg-cool-card/90">
              <span class="text-[10px] font-bold text-yellow-400 uppercase tracking-wider">Ediciones Especiales</span>
              <h4 class="font-bold text-white text-sm">Grip y Detalles a Todo Color</h4>
              <p class="text-xs text-slate-400 mt-1">Personalización completa de mango, marco y cordaje.</p>
            </div>
          </div>

        </div>
      </div>

      <!-- CÓMO TRABAJAMOS: 3 PASOS SENCILLOS -->
      <div class="glass-card rounded-3xl p-8 sm:p-12 border border-cool-cyan/20">
        <h3 class="text-2xl sm:text-3xl font-black font-heading text-center mb-12 text-white">
          Cómo conseguir los llaveros de tu club en <span class="text-cool-orange">3 pasos</span>
        </h3>

        <div class="grid md:grid-cols-3 gap-8 relative">
          
          <div class="text-center space-y-3">
            <div class="w-14 h-14 mx-auto rounded-2xl bg-cool-blue/20 border border-cool-blue/40 text-cool-cyan font-heading font-black text-2xl flex items-center justify-center">
              1
            </div>
            <h4 class="font-bold text-lg text-white">Envíanos tu Logo</h4>
            <p class="text-slate-400 text-sm">
              Mándanos tu escudo o logotipo en cualquier formato (vectorial, PNG, JPG o incluso foto).
            </p>
          </div>

          <div class="text-center space-y-3">
            <div class="w-14 h-14 mx-auto rounded-2xl bg-cool-orange/20 border border-cool-orange/40 text-cool-orange font-heading font-black text-2xl flex items-center justify-center">
              2
            </div>
            <h4 class="font-bold text-lg text-white">Diseño 3D Gratuito</h4>
            <p class="text-slate-400 text-sm">
              Te preparamos una simulación digital realista de cómo quedará el llavero en 24h sin ningún compromiso.
            </p>
          </div>

          <div class="text-center space-y-3">
            <div class="w-14 h-14 mx-auto rounded-2xl bg-emerald-500/20 border border-emerald-500/40 text-emerald-400 font-heading font-black text-2xl flex items-center justify-center">
              3
            </div>
            <h4 class="font-bold text-lg text-white">Producción & Envío</h4>
            <p class="text-slate-400 text-sm">
              Una vez aprobado, los fabricamos con máxima precisión y los enviamos directos a las instalaciones de tu club.
            </p>
          </div>

        </div>

      </div>

    </div>
  </section>

  <!-- CALCULADORA INTERACTIVA DE PRESUPUESTO & MOCKUP -->
  <section id="calculadora" class="py-20 bg-cool-navy relative">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="glass-card rounded-3xl p-8 sm:p-12 border border-cool-orange/30 glow-orange relative overflow-hidden">
        
        <div class="text-center space-y-3 mb-10">
          <span class="text-xs font-bold text-cool-cyan uppercase tracking-widest">Calculadora Rápida para Gerentes</span>
          <h2 class="text-3xl sm:text-4xl font-black font-heading text-white">
            Calcula la inversión para tu Club
          </h2>
          <p class="text-slate-300 text-sm sm:text-base">
            Selecciona la cantidad estimada y obtén una propuesta instantánea con simulación 3D gratuita.
          </p>
        </div>

        <div class="space-y-8">
          
          <div>
            <div class="flex justify-between items-center mb-3">
              <label class="text-sm font-bold text-white flex items-center gap-2">
                <i data-lucide="layers" class="w-4 h-4 text-cool-orange"></i> Cantidad de llaveros:
              </label>
              <span id="cantidad-badge" class="px-4 py-1 rounded-xl bg-cool-orange text-white font-heading font-extrabold text-lg">
                100 unidades
              </span>
            </div>
            <input type="range" id="slider-cantidad" min="50" max="1000" step="50" value="100" class="w-full h-3 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-cool-orange">
            <div class="flex justify-between text-xs text-slate-400 mt-2 font-medium">
              <span>50 uds (Mínimo)</span>
              <span>250 uds (Recomendado)</span>
              <span>500 uds</span>
              <span>1000+ uds</span>
            </div>
          </div>

          <div class="grid grid-cols-3 gap-3">
            <button type="button" class="sport-btn active-sport px-4 py-3 rounded-xl border border-cool-cyan bg-cool-blue/20 text-white font-bold text-xs sm:text-sm flex flex-col items-center gap-1.5 transition" data-sport="Pádel">
              <i data-lucide="circle-dot" class="w-5 h-5 text-cool-cyan"></i> Pala Pádel
            </button>
            <button type="button" class="sport-btn px-4 py-3 rounded-xl border border-slate-700 bg-cool-dark text-slate-300 hover:text-white font-bold text-xs sm:text-sm flex flex-col items-center gap-1.5 transition" data-sport="Tenis">
              <i data-lucide="activity" class="w-5 h-5 text-yellow-400"></i> Raqueta Tenis
            </button>
            <button type="button" class="sport-btn px-4 py-3 rounded-xl border border-slate-700 bg-cool-dark text-slate-300 hover:text-white font-bold text-xs sm:text-sm flex flex-col items-center gap-1.5 transition" data-sport="Pickleball">
              <i data-lucide="box" class="w-5 h-5 text-emerald-400"></i> Pickleball
            </button>
          </div>

          <div class="bg-cool-dark/90 rounded-2xl p-6 border border-slate-700/80 grid sm:grid-cols-3 gap-4 text-center">
            <div>
              <p class="text-xs text-slate-400">Muestra y Diseño 3D</p>
              <p class="text-xl font-black text-emerald-400 font-heading">0,00 € (Gratis)</p>
            </div>
            <div>
              <p class="text-xs text-slate-400">Uso Ideal</p>
              <p id="uso-ideal" class="text-sm font-bold text-cool-cyan font-heading mt-1">Torneo / 25 Parejas</p>
            </div>
            <div>
              <p class="text-xs text-slate-400">Tiempo de Entrega</p>
              <p class="text-sm font-bold text-white font-heading mt-1">10-15 días laborables</p>
            </div>
          </div>

          <form id="form-presupuesto" class="space-y-4 pt-2">
            <div class="grid sm:grid-cols-2 gap-4">
              <div>
                <label class="block text-xs font-semibold text-slate-300 mb-1">Nombre del Club o Marca</label>
                <input type="text" id="club-nombre" required placeholder="Ej. Club Padel Indoor Madrid" class="w-full px-4 py-3 rounded-xl bg-slate-900/90 border border-slate-700 text-white placeholder-slate-500 focus:outline-none focus:border-cool-cyan text-sm">
              </div>
              <div>
                <label class="block text-xs font-semibold text-slate-300 mb-1">Tu Teléfono / WhatsApp</label>
                <input type="tel" id="club-telefono" required placeholder="Ej. +34 600 000 000" class="w-full px-4 py-3 rounded-xl bg-slate-900/90 border border-slate-700 text-white placeholder-slate-500 focus:outline-none focus:border-cool-cyan text-sm">
              </div>
            </div>

            <button type="submit" class="w-full py-4 rounded-xl font-heading font-black text-base bg-gradient-to-r from-cool-orange to-cool-amber text-white shadow-xl shadow-cool-orange/25 hover:shadow-cool-orange/40 hover:scale-[1.01] active:scale-[0.99] transition flex items-center justify-center gap-2">
              <i data-lucide="send" class="w-5 h-5"></i> Solicitar Muestra 3D con mi Escudo (por WhatsApp)
            </button>
            <p class="text-[11px] text-center text-slate-400">
              * Te contactaremos directamente para pedirte el logo y enviarte la simulación 3D sin coste ni compromiso.
            </p>
          </form>

        </div>

      </div>

    </div>
  </section>

  <!-- SECCIÓN 2: ECOSISTEMA & PARTNER SAVE MY PLAY -->
  <section id="savemyplay" class="py-24 bg-gradient-to-b from-cool-navy via-cool-dark to-cool-navy relative border-t border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="grid lg:grid-cols-12 gap-12 items-center">
        
        <div class="lg:col-span-7 space-y-6">
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-emerald-500/15 border border-emerald-500/30 text-xs font-semibold text-emerald-400">
            <i data-lucide="cpu" class="w-3.5 h-3.5"></i> Tecnología & Cámaras Inteligentes
          </div>

          <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black font-heading text-white leading-tight">
            Multiplica el valor de tus pistas con <span class="text-emerald-400">Save my Play</span>
          </h2>

          <p class="text-slate-300 text-base sm:text-lg leading-relaxed">
            Como parte del ecosistema de <strong>CoolPadel</strong>, colaboramos con <strong>Save my Play</strong> ayudando a clubes a instalar cámaras deportivas con inteligencia artificial para que los jugadores puedan grabar y revivir sus mejores jugadas al instante.
          </p>

          <div class="space-y-4 pt-2">
            <div class="flex items-start gap-3">
              <div class="w-6 h-6 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center flex-shrink-0 mt-1">
                <i data-lucide="check" class="w-4 h-4"></i>
              </div>
              <div>
                <h4 class="font-bold text-white text-base">Viralidad Orgánica para tu Club</h4>
                <p class="text-sm text-slate-400">Los jugadores comparten los vídeos de sus mejores puntos en Instagram y TikTok etiquetando a tu club.</p>
              </div>
            </div>

            <div class="flex items-start gap-3">
              <div class="w-6 h-6 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center flex-shrink-0 mt-1">
                <i data-lucide="check" class="w-4 h-4"></i>
              </div>
              <div>
                <h4 class="font-bold text-white text-base">Llenado de Pistas en Horas Valle</h4>
                <p class="text-sm text-slate-400">La experiencia de pista inteligente incentiva más partidas y aumenta el ticket medio por jugador.</p>
              </div>
            </div>

            <div class="flex items-start gap-3">
              <div class="w-6 h-6 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center flex-shrink-0 mt-1">
                <i data-lucide="check" class="w-4 h-4"></i>
              </div>
              <div>
                <h4 class="font-bold text-white text-base">Integración con SportAI</h4>
                <p class="text-sm text-slate-400">Estadísticas avanzadas y análisis técnico de rendimiento para escuelas y torneos.</p>
              </div>
            </div>
          </div>

          <div class="pt-4 flex flex-wrap gap-4">
            <a href="https://wa.me/34680317486?text=Hola%20Javier,%20quiero%20informaci%C3%B3n%20sobre%20c%C3%B3mo%20instalar%20Save%20my%20Play%20en%20mi%20club" 
               target="_blank" 
               class="inline-flex items-center gap-2.5 px-6 py-3.5 rounded-xl font-heading font-bold text-sm bg-emerald-500 hover:bg-emerald-600 text-white shadow-lg shadow-emerald-500/20 transition">
              <i data-lucide="message-square" class="w-4 h-4"></i> Solicitar Demo de Save my Play
            </a>
            <a href="#informe" class="inline-flex items-center gap-2 px-5 py-3.5 rounded-xl font-heading font-semibold text-sm bg-cool-card border border-slate-700 hover:border-slate-500 text-slate-300 hover:text-white transition">
              Leer Análisis de Smart Courts
            </a>
          </div>

        </div>

        <div class="lg:col-span-5">
          <div class="glass-card rounded-3xl p-6 sm:p-8 border border-emerald-500/30 relative">
            <div class="flex items-center justify-between border-b border-slate-700/80 pb-4 mb-6">
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-emerald-500 flex items-center justify-center text-white font-black">
                  <i data-lucide="play" class="w-5 h-5 fill-current"></i>
                </div>
                <div>
                  <h3 class="font-heading font-black text-lg text-white">Save my Play</h3>
                  <p class="text-xs text-slate-400">AI Sports Cameras</p>
                </div>
              </div>
              <span class="text-xs font-bold text-emerald-400 bg-emerald-500/10 px-2.5 py-1 rounded-full border border-emerald-500/20">
                Partner Oficial
              </span>
            </div>

            <div class="space-y-4 text-sm text-slate-300">
              <div class="bg-slate-900/80 rounded-xl p-4 border border-slate-800">
                <span class="text-xs font-bold text-cool-orange">¿Cómo funciona para el club?</span>
                <p class="text-xs text-slate-400 mt-1">
                  1. Instalación rápida sin obras en tu pista de pádel.<br>
                  2. El jugador pulsa un botón tras un gran punto.<br>
                  3. El vídeo se genera en segundos directo a su móvil.
                </p>
              </div>

              <div class="bg-slate-900/80 rounded-xl p-4 border border-slate-800 flex items-center justify-between">
                <div>
                  <span class="text-xs text-slate-400">Alianza Tecnológica</span>
                  <p class="font-bold text-white text-sm">Save my Play × SportAI</p>
                </div>
                <div class="px-2.5 py-1 bg-cool-blue/20 text-cool-cyan text-xs font-bold rounded-lg">
                  IA & Analytics
                </div>
              </div>
            </div>

            <div class="mt-6 pt-4 border-t border-slate-800 text-center">
              <p class="text-xs text-slate-400">¿Eres gerente de club? Te asesoramos sobre el mejor modelo para tus pistas.</p>
            </div>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- SECCIÓN 3: INFORME DEL SECTOR PÁDEL & BLOG -->
  <section id="informe" class="py-24 bg-cool-navy relative border-t border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-4">
        <span class="inline-block px-3 py-1 rounded-full bg-yellow-500/15 text-yellow-400 text-xs font-bold uppercase tracking-wider">
          Industry Insights & Análisis Exclusivo
        </span>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black font-heading text-white">
          ¿Hacia dónde va el <span class="gradient-text-cool">negocio del Pádel</span>?
        </h2>
        <p class="text-slate-300 text-base sm:text-lg">
          Conclusiones reales tras conversar con más de 116 stands en el <strong>Padel World Summit</strong> (Barcelona) y visitar <strong>RacquetX & Premier Padel</strong> (Miami).
        </p>
      </div>

      <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mb-16">
        
        <div class="glass-card rounded-2xl p-6 border border-slate-800 hover:border-cool-cyan/40 transition space-y-3">
          <div class="text-cool-cyan font-heading font-black text-2xl">01</div>
          <h3 class="font-heading font-bold text-lg text-white">Consolidación & Burbujas</h3>
          <p class="text-slate-400 text-xs leading-relaxed">
            La entrada de fondos de inversión y la lección del mercado de Suecia: la importancia de un crecimiento sostenible basado en jugadores aficionados.
          </p>
        </div>

        <div class="glass-card rounded-2xl p-6 border border-slate-800 hover:border-cool-cyan/40 transition space-y-3">
          <div class="text-cool-orange font-heading font-black text-2xl">02</div>
          <h3 class="font-heading font-bold text-lg text-white">Smart Courts & Domótica</h3>
          <p class="text-slate-400 text-xs leading-relaxed">
            Pistas inteligentes con gestión de accesos automatizados, iluminación eficiente, cámaras de repetición y análisis de datos en directo.
          </p>
        </div>

        <div class="glass-card rounded-2xl p-6 border border-slate-800 hover:border-cool-cyan/40 transition space-y-3">
          <div class="text-yellow-400 font-heading font-black text-2xl">03</div>
          <h3 class="font-heading font-bold text-lg text-white">Padel Lifestyle & Clubs</h3>
          <p class="text-slate-400 text-xs leading-relaxed">
            El pádel ya no es solo deporte, es un movimiento cultural. Clubs con coworking, saunas y sinergias con marcas como Babolat x Lamborghini.
          </p>
        </div>

        <div class="glass-card rounded-2xl p-6 border border-slate-800 hover:border-cool-cyan/40 transition space-y-3">
          <div class="text-emerald-400 font-heading font-black text-2xl">04</div>
          <h3 class="font-heading font-bold text-lg text-white">El Fenómeno USA</h3>
          <p class="text-slate-400 text-xs leading-relaxed">
            De 300 pistas en 2022 a más de 1.000 proyectadas. Modelos de membresía premium y la transición natural del Pickleball al Pádel.
          </p>
        </div>

      </div>

      <div class="bg-gradient-to-r from-cool-card via-cool-dark to-cool-card rounded-3xl p-8 sm:p-12 border border-cool-cyan/30 text-center max-w-3xl mx-auto space-y-6 shadow-2xl">
        <div class="w-16 h-16 mx-auto rounded-2xl bg-gradient-to-tr from-cool-orange to-cool-amber text-white flex items-center justify-center shadow-lg shadow-cool-orange/30">
          <i data-lucide="file-text" class="w-8 h-8"></i>
        </div>

        <div class="space-y-2">
          <h3 class="font-heading font-black text-2xl sm:text-3xl text-white">
            Descarga el Informe Completo en PDF
          </h3>
          <p class="text-slate-300 text-sm max-w-xl mx-auto">
            "How is the Padel Business playing out? What your club and brand should know" por Javier Villoria Soleto.
          </p>
        </div>

        <div class="flex flex-col sm:flex-row items-center justify-center gap-4 max-w-md mx-auto">
          <a href="assets/padel-industry-report-coolpadel.pdf" 
             target="_blank" 
             download="CoolPadel_Padel_Business_Report.pdf" 
             class="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-6 py-3.5 rounded-xl font-heading font-bold text-sm bg-gradient-to-r from-cool-orange to-cool-amber text-white shadow-lg hover:scale-105 transition">
            <i data-lucide="download" class="w-4 h-4"></i> Descargar PDF Gratis (8.5 MB)
          </a>
          <a href="https://wa.me/34680317486?text=Hola%20Javier,%20he%20le%C3%ADdo%20tu%20informe%20de%20P%C3%A1del%20y%20me%20gustar%C3%ADa%20comentar%20un%20proyecto" 
             target="_blank" 
             class="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-6 py-3.5 rounded-xl font-heading font-bold text-sm bg-cool-navy border border-slate-700 hover:border-cool-cyan text-slate-200 transition">
            <i data-lucide="message-circle" class="w-4 h-4 text-cool-cyan"></i> Hablar con Javier
          </a>
        </div>
      </div>

    </div>
  </section>

  <!-- SECCIÓN 4: SOBRE JAVIER VILLORIA SOLETO -->
  <section id="sobre-mi" class="py-24 bg-cool-dark/40 relative border-t border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="grid lg:grid-cols-12 gap-12 items-center">
        
        <div class="lg:col-span-5 relative">
          <div class="glass-card rounded-3xl p-6 border border-cool-cyan/20 space-y-4">
            <div class="aspect-square rounded-2xl bg-slate-800 overflow-hidden relative border border-slate-700">
              <div class="w-full h-full bg-gradient-to-tr from-cool-navy via-cool-card to-cool-blue/40 flex flex-col items-center justify-center p-6 text-center">
                <div class="w-24 h-24 rounded-full bg-cool-orange flex items-center justify-center text-white text-3xl font-heading font-black mb-3 shadow-xl">
                  JV
                </div>
                <h3 class="font-heading font-black text-xl text-white">Javier Villoria Soleto</h3>
                <p class="text-cool-cyan text-xs font-bold mt-0.5">Fundador de CoolPadel</p>
                <div class="mt-4 flex items-center justify-center gap-2 text-slate-400 text-xs">
                  <i data-lucide="map-pin" class="w-3.5 h-3.5 text-cool-orange"></i> Barcelona · Miami · Madrid
                </div>
              </div>
            </div>

            <div class="p-4 bg-cool-navy/80 rounded-xl border border-slate-800 space-y-2">
              <span class="text-[10px] font-bold text-slate-400 uppercase tracking-wider">Misión</span>
              <p class="text-xs text-slate-300 leading-relaxed">
                "Ayudar a los clubes de pádel a diferenciarse con productos que enamoren a sus socios y soluciones que hagan más rentable su día a día."
              </p>
            </div>
          </div>
        </div>

        <div class="lg:col-span-7 space-y-6">
          <span class="inline-block px-3 py-1 rounded-full bg-cool-cyan/15 text-cool-cyan text-xs font-bold uppercase tracking-wider">
            La Historia de CoolPadel
          </span>

          <h2 class="text-3xl sm:text-4xl font-black font-heading text-white">
            De jugador apasionado a construir un ecosistema para clubes
          </h2>

          <div class="space-y-4 text-slate-300 text-base leading-relaxed">
            <p>
              Comencé CoolPadel hace más de dos años diseñando y fabricando llaveros personalizados de pádel y tenis para amigos y torneos locales. Lo que empezó como un hobby creció rápidamente al comprobar la emoción de los jugadores al recibir un detalle tan representativo.
            </p>
            <p>
              Hoy en día, hemos trabajado con más de <strong>30 clubes, marcas y federaciones internacionales</strong> (como la <em>Austrian Padel Union</em>), estuvimos presentes en el <strong>Padel World Summit</strong> de Barcelona hablando con más de 116 empresas del sector, y viajamos a Miami a ferias como <strong>RacquetX</strong> para entender de primera mano la expansión global del deporte.
            </p>
            <p>
              Junto a empresas de referencia como <strong>Save my Play</strong>, mi objetivo es ser el aliado de confianza de los gerentes de club: trato personal, calidad sin rodeos y soluciones pensadas para el pádel real.
            </p>
          </div>

          <div class="pt-2 flex items-center gap-4">
            <a href="https://wa.me/34680317486?text=Hola%20Javier,%20me%20gustar%C3%ADa%20hablar%20contigo%20sobre%20CoolPadel" 
               target="_blank" 
               class="inline-flex items-center gap-2 px-6 py-3.5 rounded-xl font-heading font-bold text-sm bg-gradient-to-r from-cool-orange to-cool-amber text-white shadow-lg shadow-cool-orange/20 hover:scale-105 transition">
              <i data-lucide="message-square" class="w-4 h-4"></i> Charlar con Javier
            </a>
          </div>

        </div>

      </div>

    </div>
  </section>

  <!-- FAQ SECTION -->
  <section class="py-20 bg-cool-navy border-t border-slate-800">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center space-y-3 mb-12">
        <h2 class="text-3xl font-black font-heading text-white">Preguntas Frecuentes para Clubs</h2>
        <p class="text-slate-400 text-sm">Todo lo que necesitas saber antes de encargar tus llaveros o soluciones</p>
      </div>

      <div class="space-y-4">
        
        <details class="group glass-card rounded-2xl p-5 border border-slate-800 cursor-pointer">
          <summary class="font-bold text-white flex justify-between items-center list-none">
            <span>¿Cuál es el pedido mínimo de llaveros personalizados?</span>
            <i data-lucide="chevron-down" class="w-5 h-5 text-cool-cyan group-open:rotate-180 transition"></i>
          </summary>
          <p class="text-slate-400 text-sm mt-3 pt-3 border-t border-slate-800">
            El pedido mínimo habitual es de solo 50 unidades, ideal para un torneo mediano o una primera prueba en la recepción de tu club.
          </p>
        </details>

        <details class="group glass-card rounded-2xl p-5 border border-slate-800 cursor-pointer">
          <summary class="font-bold text-white flex justify-between items-center list-none">
            <span>¿Tiene algún coste hacer la simulación 3D de mi logo?</span>
            <i data-lucide="chevron-down" class="w-5 h-5 text-cool-cyan group-open:rotate-180 transition"></i>
          </summary>
          <p class="text-slate-400 text-sm mt-3 pt-3 border-t border-slate-800">
            No, es <strong>100% gratuita y sin ningún compromiso</strong>. Nos envías el escudo y en 24 horas te mostramos cómo quedaría el llavero con relieve y colores reales.
          </p>
        </details>

        <details class="group glass-card rounded-2xl p-5 border border-slate-800 cursor-pointer">
          <summary class="font-bold text-white flex justify-between items-center list-none">
            <span>¿Hacéis envíos fuera de España?</span>
            <i data-lucide="chevron-down" class="w-5 h-5 text-cool-cyan group-open:rotate-180 transition"></i>
          </summary>
          <p class="text-slate-400 text-sm mt-3 pt-3 border-t border-slate-800">
            Sí. Enviamos a toda Europa (Austria, Italia, Suecia, Portugal, etc.) y América con tarifas competitivas de paquetería urgente.
          </p>
        </details>

        <details class="group glass-card rounded-2xl p-5 border border-slate-800 cursor-pointer">
          <summary class="font-bold text-white flex justify-between items-center list-none">
            <span>¿Cómo se integra Save my Play en las pistas?</span>
            <i data-lucide="chevron-down" class="w-5 h-5 text-cool-cyan group-open:rotate-180 transition"></i>
          </summary>
          <p class="text-slate-400 text-sm mt-3 pt-3 border-t border-slate-800">
            La instalación se realiza de forma limpia y rápida en los postes o estructura de la pista. Te asesoramos y gestionamos la demo para que pruebes el sistema en tu club.
          </p>
        </details>

      </div>

    </div>
  </section>

  <!-- FOOTER -->
  <footer class="bg-cool-dark border-t border-slate-800 py-12 text-slate-400 text-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid md:grid-cols-4 gap-8">
      
      <div class="md:col-span-2 space-y-3">
        <div class="flex items-center gap-2">
          <div class="w-8 h-8 rounded-full bg-cool-orange flex items-center justify-center text-white font-bold text-sm">
            CP
          </div>
          <span class="font-heading font-black text-xl text-white">COOL<span class="text-cool-orange">PADEL</span></span>
        </div>
        <p class="text-xs text-slate-400 max-w-sm">
          Ecosistema B2B para clubes de pádel y tenis. Llaveros personalizados premium, tecnología de pista inteligente Save my Play y consultoría del sector.
        </p>
        <p class="text-xs text-slate-500">Fundado por Javier Villoria Soleto.</p>
      </div>

      <div class="space-y-2">
        <h4 class="font-bold text-white text-xs uppercase tracking-wider">Enlaces Rápidos</h4>
        <ul class="space-y-1.5 text-xs">
          <li><a href="#llaveros" class="hover:text-cool-cyan transition">Llaveros para Clubs</a></li>
          <li><a href="#calculadora" class="hover:text-cool-cyan transition">Calculadora de Presupuesto</a></li>
          <li><a href="#savemyplay" class="hover:text-cool-cyan transition">Save my Play (Cámaras IA)</a></li>
          <li><a href="#informe" class="hover:text-cool-cyan transition">Informe del Sector Pádel</a></li>
          <li><a href="#sobre-mi" class="hover:text-cool-cyan transition">Sobre Javier</a></li>
        </ul>
      </div>

      <div class="space-y-2">
        <h4 class="font-bold text-white text-xs uppercase tracking-wider">Contacto Directo</h4>
        <p class="text-xs text-slate-400">Atención personalizada a gerentes y organizadores de torneos.</p>
        <a href="https://wa.me/34680317486?text=Hola%20Javier,%20quiero%20informaci%C3%B3n%20para%20mi%20club" class="inline-flex items-center gap-2 text-xs font-bold text-cool-orange hover:underline">
          <i data-lucide="message-circle" class="w-4 h-4"></i> WhatsApp Directo
        </a>
      </div>

    </div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-10 pt-6 border-t border-slate-800/80 text-center text-xs text-slate-500">
      © 2026 CoolPadel. Todos los derechos reservados. Diseñado para liderar la nueva era del pádel.
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

    const mobileBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    mobileBtn.addEventListener('click', () => {
      mobileMenu.classList.toggle('hidden');
    });

    const slider = document.getElementById('slider-cantidad');
    const badge = document.getElementById('cantidad-badge');
    const usoIdeal = document.getElementById('uso-ideal');
    let selectedSport = 'Pádel';

    const sportButtons = document.querySelectorAll('.sport-btn');
    sportButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        sportButtons.forEach(b => {
          b.classList.remove('active-sport', 'border-cool-cyan', 'bg-cool-blue/20', 'text-white');
          b.classList.add('border-slate-700', 'bg-cool-dark', 'text-slate-300');
        });
        btn.classList.add('active-sport', 'border-cool-cyan', 'bg-cool-blue/20', 'text-white');
        btn.classList.remove('border-slate-700', 'bg-cool-dark', 'text-slate-300');
        selectedSport = btn.dataset.sport;
      });
    });

    slider.addEventListener('input', (e) => {
      const val = e.target.value;
      badge.textContent = `${val} unidades`;
      
      if (val <= 60) {
        usoIdeal.textContent = 'Torneo / 15-25 Parejas';
      } else if (val <= 150) {
        usoIdeal.textContent = 'Torneo Club / Welcome Pack';
      } else if (val <= 300) {
        usoIdeal.textContent = 'Socios Activos del Club';
      } else {
        usoIdeal.textContent = 'Club Grande / Temporada Completa';
      }
    });

    const form = document.getElementById('form-presupuesto');
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const club = document.getElementById('club-nombre').value;
      const telefono = document.getElementById('club-telefono').value;
      const cantidad = slider.value;

      const mensaje = `Hola Javier! Vengo de la web de CoolPadel.
Soy del club/marca: *${club}* (Tel: ${telefono}).
Me gustaría una muestra 3D gratuita para *${cantidad} llaveros* de *${selectedSport}*.`;

      const url = `https://wa.me/34680317486?text=${encodeURIComponent(mensaje)}`;
      window.open(url, '_blank');
    });
  </script>
</body>
</html>"""

out_dir = os.path.join(os.getcwd(), "coolpadel-web")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated coolpadel-web/index.html successfully!")
