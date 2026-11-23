const { execFileSync } = require('node:child_process');
const fs = require('node:fs');
const path = require('node:path');
const postcss = require('postcss');
const tailwind = require('tailwindcss');
const { loadAutoprefixer, loadCssNano } = require('tailwindcss/lib/cli/build/deps');

const root = __dirname;
const cssDirectory = path.join(root, 'assets/css');
const cdnScript = /<script\b[^>]*\bsrc=["']https:\/\/cdn\.tailwindcss\.com\/?["'][^>]*>\s*<\/script>/i;
const inlineConfig = /<script>\s*tailwind\.config\s*=\s*([\s\S]*?)<\/script>/i;
const cdnPrefetch = /^[ \t]*<link rel="dns-prefetch" href="https:\/\/cdn\.tailwindcss\.com">\r?\n/gm;
const staticLink = /<link rel="stylesheet" href="[^"]*assets\/css\/tailwind-(site|markets|directory)\.css">/i;
const whitespaceAfterLink = /(<link rel="stylesheet" href="[^"]*assets\/css\/tailwind-(?:site|markets|directory)\.css">\r?\n)[ \t]+\r?\n/i;

const groups = {
  site: { extend: {}, pages: [] },
  markets: {
    extend: { fontFamily: { heading: ['Outfit', 'sans-serif'], body: ['Plus Jakarta Sans', 'sans-serif'] } },
    pages: [],
  },
  directory: {
    extend: {
      fontFamily: { heading: ['Outfit', 'sans-serif'], sans: ['Plus Jakarta Sans', 'sans-serif'] },
      colors: { brand: { orange: '#f2920b', blue: '#76d3f6', dark: '#0b1626' } },
    },
    pages: [],
  },
};

async function build() {
  const files = execFileSync('git', ['ls-files', '-z', '--cached', '--others', '--exclude-standard', '--', '*.html'], {
    cwd: root,
    encoding: 'utf8',
  }).split('\0').filter(Boolean);
  for (const file of new Set(files)) {
    const absolute = path.join(root, file);
    if (!fs.existsSync(absolute) || file === 'manual-marca.html') continue;
    const html = fs.readFileSync(absolute, 'utf8');
    const existing = html.match(staticLink);
    if (!existing && !cdnScript.test(html)) continue;

    const config = html.match(inlineConfig);
    let group = existing?.[1] || 'site';
    if (config) {
      if (config[1].includes('brand:')) group = 'directory';
      else if (config[1].includes('body:')) group = 'markets';
      else throw new Error(`Unknown Tailwind configuration in ${file}`);
    }
    const relativeCss = path.relative(path.dirname(absolute), cssDirectory).replaceAll(path.sep, '/');
    const link = `<link rel="stylesheet" href="${relativeCss}/tailwind-${group}.css">`;
    let updated = html.replace(cdnScript, link).replace(inlineConfig, '')
      .replace(whitespaceAfterLink, '$1').replace(cdnPrefetch, '');
    if (file.endsWith('herramientas/generador-americana-padel/index.html')) {
      updated = updated.replace(/<html\b[^>]*>/i, (tag) => {
        if (tag.includes('cp-americana')) return tag;
        return / class="/i.test(tag)
          ? tag.replace(/ class="/i, ' class="cp-americana ')
          : tag.replace(/>$/, ' class="cp-americana">');
      });
    }
    groups[group].pages.push({ absolute, html, updated });
  }

  const input = path.join(cssDirectory, 'input.css');
  const directives = fs.readFileSync(input, 'utf8') + '\n'
    + fs.readFileSync(path.join(cssDirectory, 'responsive.css'), 'utf8');
  for (const [name, { extend, pages }] of Object.entries(groups)) {
    if (!pages.length) continue;
    const output = path.join(cssDirectory, `tailwind-${name}.css`);
    const result = await postcss([
      tailwind({
        content: [
          ...pages.map(({ updated }) => ({ raw: updated, extension: 'html' })),
          path.join(root, 'assets/js/**/*.js').replaceAll(path.sep, '/'),
        ],
        theme: { extend },
      }),
      loadAutoprefixer(),
      loadCssNano(),
    ]).process(directives, { from: input, to: output });
    fs.writeFileSync(output, result.css + '\n');
    for (const { absolute, html, updated } of pages) {
      if (updated !== html) fs.writeFileSync(absolute, updated);
    }
    console.log(`${name}: ${pages.length} pages, ${Buffer.byteLength(result.css)} CSS bytes`);
  }
}

build().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
