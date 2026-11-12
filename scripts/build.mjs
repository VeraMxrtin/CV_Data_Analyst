import { mkdir, copyFile, readdir, readFile, writeFile } from 'node:fs/promises';
await mkdir('dist', { recursive: true });
for (const file of ['index.html','index.css','index.js','favicon.svg','robots.txt','sitemap.xml']) await copyFile(file, `dist/${file}`);
await mkdir('dist/img', { recursive: true });
for (const file of ['portrait.webp','spotify.webp','gold.webp','cancer.webp','social.jpg','Vera-Martin-CV.pdf','cv_veramartin.pdf']) await copyFile(`img/${file}`, `dist/img/${file}`);
// Los logos son opcionales: no se solicitan recursos que todavía no existen.
const logoFiles = await readdir('img/logos');
let html = await readFile('index.html', 'utf8');
for (const [slug, name] of [['ms-wisdom-press', 'MS Wisdom Press'], ['veraflow', 'VeraFlow'], ['lima-kallpa', 'Lima Kallpa']]) {
  const file = ['png', 'webp', 'svg'].map(ext => `${slug}.${ext}`).find(candidate => logoFiles.includes(candidate));
  if (!file) continue;
  await mkdir('dist/img/logos', { recursive: true });
  await copyFile(`img/logos/${file}`, `dist/img/logos/${file}`);
  html = html.replace(
    new RegExp(`<div class="initiative-logo" data-logo="${slug}">[\\s\\S]*?</div>`),
    `<div class="initiative-logo" data-logo="${slug}"><img src="img/logos/${file}" alt="Logo de ${name}" width="240" height="78" loading="lazy"></div>`
  );
}
await writeFile('dist/index.html', html);
console.log('Producción lista en dist/ (sin dependencias de ejecución).');
