# Plan de Implementación: Optimización Móvil Completa y Soporte Multi-idioma (ES, EN, FR, IT)

Este plan detalla la arquitectura para transformar la web de **CoolPadel** (`coolpadelstudios.com`) en una plataforma con **experiencia móvil premium** y **sistema multilingüe completo** para captar clientes en los 4 grandes mercados internacionales del pádel: **Español (ES)**, **Inglés (EN)**, **Francés (FR)** e **Italiano (IT)**.

---

## 📱 1. Optimización y Rediseño de la Versión Móvil (Mobile-First)

### A. Cabecera y Navegación Móvil
- **Prevención de desbordamiento y colisiones**: En pantallas móviles (<640px), la cabecera actual con ojos dobles y textos puede apretarse. Diseñaremos un layout limpio:
  - **Izquierda**: Logo y Mascota CoolPadel HD proporcionados.
  - **Centro/Derecha**: Selector de idioma compacto (`ES | EN | FR | IT`) y botón *"Contactar"* optimizado.
- **Top Ticker**: Ajuste de texto a `text-[10px] sm:text-xs` para lectura fluida en smartphones.

### B. Carrusel Coverflow 3D Táctil (Swipe Gestures)
- **Soporte táctil nativo (Touch Swipe)**: Los usuarios en móvil podrán deslizar el dedo a izquierda/derecha para cambiar de diapositiva.
- **Tipografía adaptable**: Escalar los títulos de los slides (`text-2xl sm:text-5xl`) para que nunca tapen las imágenes ni se corten en pantallas estrechas (iPhone SE, Galaxy, iPhone 14/15/16).

### C. Calculadora Interactiva en Móvil
- **Slider Touch-Friendly**: Aumentar el área táctil del logo de los ojos en la barra deslizadora para que arrastrar con el pulgar sea 100% fluido y preciso.
- **Precios e insignias**: Asegurar que en pantallas estrechas (<380px) los importes y cantidades mantengan legibilidad sin saltos de línea antiestéticos.
- **Evitar Auto-Zoom en iOS**: Configurar los campos de formulario con tamaño mínimo de 16px para evitar que Safari en iPhone haga zoom involuntario al pulsar el email.

### D. Sección de Contacto en Móvil
- Disposición vertical simétrica y centrada:
  1. Mascota y tipografía CoolPadel.
  2. Correo oficial y botón verde de WhatsApp con área táctil cómoda (mínimo 48px de altura).
  3. Logo Save my Play HD en blanco.

---

## 🌍 2. Arquitectura Multi-idioma (ES, EN, FR, IT)

Implementaremos un sistema dual: **Cambio instantáneo en el cliente** + **Páginas estáticas optimizadas para SEO internacional**.

### A. 4 Idiomas Cubiertos
1. 🇪🇸 **Español (ES)**: Mercado principal (España y Latinoamérica).
2. 🇬🇧 **Inglés (EN)**: Mercado global (EE.UU., Reino Unido, Emiratos Árabes / Dubái, Países Nórdicos / Suecia).
3. 🇫🇷 **Francés (FR)**: Francia, Bélgica y Suiza.
4. 🇮🇹 **Italiano (IT)**: Italia (uno de los mayores mercados de pádel de Europa).

### B. Traducción Completa de Componentes
- **Top Bar**: Anuncio del informe de la industria.
- **Hero / Coverflow**: Títulos, subtítulos y botones de los 3 slides.
- **Pasarela**: Texto *"Trabajamos con clubs, marcas y federaciones de todo el mundo"*.
- **Llaveros**: Cabeceras, tarjetas Tenis/Padel, calculadora de presupuesto, tramos de unidades y condiciones (*Muestra 15€*, *Envíos incluidos*, *Pago adelantado*).
- **Save my Play**: Títulos, beneficios (*"Sin dolores de cabeza"*, *"Instalación en 5 minutos"*).
- **Reportaje y Newsletter**: Textos de descarga, botón *"Descargar PDF"* y *"Leer en LinkedIn"*.
- **WhatsApp Dinámico**: Cada idioma abrirá el chat con el saludo nativo:
  - ES: `Hola Javier`
  - EN: `Hello Javier`
  - FR: `Bonjour Javier`
  - IT: `Ciao Javier`

### C. SEO Internacional Multilingüe (`hreflang` y Estructura)
- Inclusión de etiquetas `<link rel="alternate" hreflang="es/en/fr/it/x-default">`.
- Generación de subdirectorios estáticos (`/en/`, `/fr/`, `/it/`) y `sitemap.xml` multilingüe para que Google indexe las versiones en cada país.

---

## 📂 Archivos Involucrados

| Archivo | Acción | Descripción |
|---|---|---|
| `coolpadel-web/index.html` | **[MODIFY]** | Selector de idioma, soporte táctil swipe, optimizaciones móviles CSS/JS |
| `coolpadel-web/assets/js/i18n.js` | **[NEW]** | Diccionario de traducciones completo en ES, EN, FR, IT y lógica de cambio instantáneo |
| `coolpadel-web/en/index.html` | **[NEW]** | Versión estática en inglés para indexación SEO internacional |
| `coolpadel-web/fr/index.html` | **[NEW]** | Versión estática en francés para indexación SEO internacional |
| `coolpadel-web/it/index.html` | **[NEW]** | Versión estática en italiano para indexación SEO internacional |
| `coolpadel-web/sitemap.xml` | **[MODIFY]** | Inclusión de URLs en los 4 idiomas con etiquetas de localización |
| `coolpadel-web/sync_builder.py` | **[MODIFY]** | Sincronización con el generador del proyecto |

---

## 🧪 Plan de Verificación

1. **Pruebas de Responsive Móvil**:
   - Verificar en resoluciones de 360px, 375px (iPhone SE), 390px (iPhone 14/15), 412px (Android) y tabletas (768px).
   - Comprobar que el swipe táctil cambia de slide suavemente.
   - Comprobar que la barra de la calculadora se arrastra con precisión en pantallas táctiles.
2. **Pruebas de Cambio de Idioma**:
   - Conmutar entre ES, EN, FR e IT y verificar que todos los textos, calculadora y botones de WhatsApp cambian al instante sin parpadeos.
   - Comprobar que al recargar la página se recuerda el idioma seleccionado (`localStorage` y URL).
3. **Despliegue a Producción y GitHub**:
   - Subir el repositorio a GitHub (`coolpadel-web`) y verificar que `https://coolpadelstudios.com` se actualiza con la versión móvil y multi-idioma en vivo.
