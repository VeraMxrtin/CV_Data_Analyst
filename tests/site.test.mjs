import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync, existsSync, statSync } from 'node:fs';
const html = readFileSync('index.html', 'utf8');
test('Todas las anclas y los archivos locales existen', () => {
  const ids = [...html.matchAll(/\bid="([^"]+)"/g)].map(m => m[1]);
  assert.equal(new Set(ids).size, ids.length, 'IDs duplicados');
  for (const [,url] of html.matchAll(/(?:href|src)="([^"]+)"/g)) {
    if (url.startsWith('#')) assert.ok(ids.includes(url.slice(1)), url);
    else if (!/^(https?:|mailto:)/.test(url)) assert.ok(existsSync(url),url);
  }
});
test('Metadatos, estructura y enlaces externos seguros', () => {
  assert.equal([...html.matchAll(/<h1\b/g)].length,1);
  assert.match(html, /<html lang="es">/);
  assert.match(html, /name="description"/);
  assert.match(html, /property="og:image"/);
  assert.match(html, /class="skip-link"/);
  for (const [,attrs] of html.matchAll(/<a\b([^>]+)>/g)) {
    if (attrs.includes('target="_blank"')) assert.match(attrs,/rel="noopener noreferrer"/);
  }
  for (const [,attrs] of html.matchAll(/<img\b([^>]+)>/g)) {
    assert.match(attrs,/alt="[^"]+"/);
    assert.match(attrs,/width="\d+"/);
    assert.match(attrs,/height="\d+"/);
  }
  const json=html.match(/<script type="application\/ld\+json">(.*?)<\/script>/s)[1];
  assert.equal(JSON.parse(json)['@type'],'Person');
});
test('Los tres casos y la descarga PDF están disponibles sin JavaScript', () => {
  assert.equal([...html.matchAll(/<details>/g)].length,3);
  assert.match(html,/R² = 0,952/);
  assert.match(html,/no accuracy/);
  assert.match(html,/no es una herramienta de diagnóstico/);
  const cvLinks = [...html.matchAll(/<a\b[^>]*href="img\/cv_veramartin.pdf"[^>]*>/g)];
  assert.equal(cvLinks.length, 2);
  for (const [link] of cvLinks) {
    assert.match(link, /target="_blank"/);
    assert.match(link, /rel="noopener noreferrer"/);
    assert.doesNotMatch(link, /\bdownload=/);
  }
  const pdf=readFileSync('img/cv_veramartin.pdf');
  assert.equal(pdf.subarray(0,5).toString(),'%PDF-');
  assert.ok(statSync('img/portrait.webp').size < 150000);
});
