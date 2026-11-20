# Portafolio de Vera Martín

Portafolio estático en español, centrado en análisis de datos. HTML semántico, CSS responsive y JavaScript nativo. Sin dependencias de ejecución, CDN ni fuentes remotas.

## Uso local

Requiere Node.js 18 o posterior y Python 3 para el servidor de vista previa. En PowerShell se puede usar `npm.cmd` si la política de ejecución bloquea `npm.ps1`.

```powershell
npm.cmd test
npm.cmd run build
npm.cmd run dev
```

Abrir http://127.0.0.1:4173. `dist/` contiene únicamente los archivos destinados a producción. También se puede abrir `index.html` directamente: el contenido, menú, fichas y descarga no requieren un backend.

No se necesita ejecutar `npm install` para trabajar con los archivos fuente.

## Despliegue automático

Un `git push origin main` ejecuta `.github/workflows/firebase-hosting-merge.yml`: instala dependencias con `npm ci`, ejecuta las pruebas, construye `dist/` y publica el target `portfolio` del proyecto `cvdataanalyst-bc66b` en el canal `live` de Firebase Hosting. El sitio correspondiente es `https://cvveramartin.web.app/`. Se puede iniciar también desde la pestaña Actions con `workflow_dispatch`.

El repositorio debe tener el secreto `FIREBASE_SERVICE_ACCOUNT_CVDATAANALYST_BC66B` con una cuenta de servicio autorizada para desplegar Hosting en ese proyecto. El workflow falla si falta el secreto o el PDF en `dist/`. Después de publicar, comprueba que `https://cvveramartin.web.app/deployment.json` contiene el commit y el ID de la ejecución actual. Si el job aparece verde, esa versión ya se sirve desde el sitio indicado.

Los pull requests del mismo repositorio crean una vista previa para el mismo target; no publican en `live`.

## Contenido y recursos

Los logos de MS Wisdom Press, VeraFlow y Lima Kallpa se colocan en `img/logos/`. Consulta los nombres en [img/logos/README.md](img/logos/README.md). El build los integra automáticamente cuando existen.

- `index.html`: contenido, datos estructurados y fichas expandibles.
- `index.css`: diseño, puntos de adaptación, estados de foco, impresión y movimiento reducido.
- `index.js`: menú responsive y sección activa. El contenido sigue disponible sin JavaScript.
- `img/cv_veramartin.pdf`: CV publicado, con texto seleccionable y enlaces.
- `img/*.webp`: retrato y capturas reales optimizadas. Los recursos originales permanecen en el repositorio.
- `docs/INFORME.md`: auditoría, fuentes, decisiones, pruebas y pendientes.

## Comprobaciones adicionales

Las herramientas Python se instalaron únicamente en `.venv/`, excluido de Git. No son dependencias del sitio.

```powershell
.venv/Scripts/python scripts/create_cv.py
.venv/Scripts/python scripts/browser_qa.py
.venv/Scripts/python scripts/check_links.py
```

Para recrear ese entorno: `python -m venv .venv` y `.venv/Scripts/python -m pip install reportlab pypdf playwright`. La auditoría de navegador usa Chromium instalado en `C:/Users/SISO/AppData/Local/ms-playwright/chromium-1248/chrome-win64/chrome.exe`; adaptar esa ruta en el script para otros equipos. `browser_qa.py` ejecuta axe si existe `.audit/axe.min.js`; si falta, no ejecuta esa parte. No descarga herramientas ni navegadores por sí mismo.

`scripts/prepare.py` optimiza el retrato y genera la imagen social con Pillow; `scripts/create_cv.py` usa las fuentes Arial de Windows. Las capturas finales ya están incluidas y no necesitan regeneración. Los scripts `verify_sources.py` y `finish_evidence.py` registran las fuentes públicas y capturas en `.audit/`; requieren conexión a Internet. Las evidencias temporales y capturas de QA se guardan en directorios ignorados.

El dominio canónico es `https://cvveramartin.web.app/`.
