# 🎾 Web Oficial de CoolPadel

Sitio web oficial interactivo y de alto impacto para **CoolPadel**: venta de merchandising / llaveros personalizados para clubes de pádel, federaciones y torneos, partner oficial de **Save my Play** y análisis de negocio del pádel.

---

## 🚀 Cómo previsualizar la web en tu ordenador

1. Puedes hacer doble clic en `index.html` directamente para abrirlo en cualquier navegador (Chrome, Edge, Firefox, Safari).
2. O bien arrancar un servidor local ultra rápido con Python:
```bash
cd coolpadel-web
python -m http.server 8080
```
Luego abre en tu navegador: [http://localhost:8080](http://localhost:8080)

---

## 🌐 Cómo publicar tu web GRATIS en GitHub Pages con tu Dominio

### Opción A: Crear un repositorio nuevo en GitHub (Recomendado)
1. Entra en [github.com/new](https://github.com/new) y crea un repositorio público (ejemplo: `coolpadel-web`).
2. Sube los archivos de esta carpeta a tu repositorio:
```bash
cd coolpadel-web
git init
git add .
git commit -m "Web inicial de CoolPadel"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/coolpadel-web.git
git push -u origin main
```
3. En GitHub, ve a **Settings** > **Pages**:
   * En **Source**, selecciona `Deploy from a branch` y la rama `main` / `root`.
   * En **Custom domain**, escribe tu dominio (ejemplo: `coolpadel.es` o `www.coolpadel.es`).
   * Guarda y activa la casilla **Enforce HTTPS** (el certificado SSL es 100% gratis).

### Opción B: Conectar a Vercel o Cloudflare Pages (En 1 clic)
1. Entra en [vercel.com](https://vercel.com) o [pages.cloudflare.com](https://pages.cloudflare.com).
2. Conecta tu repositorio de GitHub `coolpadel-web`.
3. Añade tu dominio en la sección de dominios y sigue las instrucciones DNS (apuntar un CNAME o registro A).

---

## 📱 Personalización de Datos de Contacto
* Para actualizar el número de WhatsApp al que llegan los mensajes, busca en `index.html` la cadena:
  `34600000000`
  y cámbiala por tu número real con código de país (ejemplo: `34612345678`).
