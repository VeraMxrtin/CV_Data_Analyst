# Informe de implementación

Fecha: 11 de noviembre de 2026. Trabajo local; sin despliegue, commit ni push.

## Ampliación de proyectos solicitada

Se añadieron MS Wisdom Press, VeraFlow y Lima Kallpa a la sección de proyectos, manteniendo los tres casos de datos como contenido principal. Las URLs proporcionadas por el usuario respondieron HTTP 200 en la comprobación con encabezado de navegador: `https://ms-wisdom-press.vercel.app/`, `https://veraflowapp.lovable.app/` y `https://limakallpa-form.vercel.app/`. Lima Kallpa se describe según la información del usuario: agencia que conecta clientes que necesitan servicios con personas y empresas proveedoras. No se añaden cifras comerciales ni funcionalidades no confirmadas.

Los logos reales están pendientes. Sus ubicaciones son `img/logos/ms-wisdom-press.png`, `img/logos/veraflow.png` e `img/logos/lima-kallpa.png`; también se admiten SVG y WebP. El build detecta los archivos disponibles e incorpora sus imágenes a las tarjetas. Mientras faltan se muestran iniciales temporales, sin inventar identidades visuales ni generar solicitudes a archivos inexistentes. No se publicó esta ampliación.

Validación de esta ampliación: tres pruebas Node aprobadas, build correcto, `git diff --check` sin errores y verificación aislada de incorporación de un logo disponible/fallback ausente aprobada. Las capturas actualizadas de escritorio y móvil se generaron y se inspeccionó la de escritorio. La repetición de `browser_qa.py` llegó hasta la descarga tras las comprobaciones de tamaños, imágenes, navegación, fichas y axe, pero Chromium canceló `Download.save_as`; también ocurrió fuera del sandbox. Por ello esta repetición completa no se declara aprobada. El PDF y su enlace no fueron modificados por esta ampliación; la causa de la cancelación no se ha establecido. Los resultados completos de la validación inicial descritos más abajo corresponden a la versión anterior a esta ampliación.

## Auditoría y dirección aplicada

El proyecto original era una web estática de tres archivos con Tailwind servido desde CDN, Font Awesome, fuentes externas, estilos duplicados, degradados animados y un botón de menú sin implementación. No tenía build ni pruebas configuradas. La sección de proyectos tenía etiquetas HTML sin cerrar y no había sección de educación ni contacto completa.

Se conservaron HTML/CSS/JavaScript y el alojamiento de referencia. El nuevo diseño utiliza blanco, gris claro y azul profesional; retrato existente; capturas reales; tipografía del sistema; bordes sutiles; espaciado amplio y animación breve que respeta movimiento reducido. Los proyectos ocupan la primera sección después del hero. Sus fichas usan `details` y `summary`, funcionan con teclado y sin JavaScript, y no cargan librerías.

Se implementaron las siete categorías técnicas, presentación personal, proyectos, trayectoria independiente, formación, correo, perfiles públicos, WhatsApp y descarga de CV. No se asignaron niveles de dominio arbitrarios. Se añadieron metadatos, Open Graph, imagen social local, canonical, sitemap, robots y datos estructurados Person.

## Fuentes y correcciones editoriales

Se revisaron el HTML original y el PDF original al inicio. Durante el trabajo el archivo `img/VeraMartín.pdf` fue eliminado y apareció `img/cv_veramartin.pdf` por un cambio externo a esta implementación. Ese cambio se respetó; el nuevo archivo no se sobrescribió. Aporta el nombre académico **Administración de Sistemas para la Transformación Digital**, el correo y el enfoque profesional actualizado. El nuevo CV generado tiene otra ruta: `img/Vera-Martin-CV.pdf`.

| Información | Evidencia y tratamiento |
| --- | --- |
| Formación en CERTUS | CV actualizado. No se afirma titulación, egreso ni fechas porque faltan. |
| SQL, Power BI, Excel/Power Query | CV actualizado y declaración de proyectos independientes; no se presentan como resultados empresariales auditados. |
| Spotify-YouTube | [Aplicación actual](https://veraspotify.web.app/) y [API pública](https://github.com/VeraMxrtin/Model-Spotify/blob/main/app.py). El código carga un modelo serializado, recibe 10 variables con NumPy y devuelve vistas mediante Flask. No hay código de entrenamiento en ese repositorio; no se inventa dataset ni métrica. Se actualizó el enlace antiguo `sample-firebase-ai-app-27529.web.app`, también accesible. |
| Oro | [Tablero](https://veragoldprice.web.app/) y [documentación](https://veragoldprice.web.app/assets/documentacion_data_web_oro.pdf). El PDF describe Random Forest y menciona Kaggle, LBMA, World Gold Council y FRED sin identificar datasets concretos. El tablero muestra R² 0,952; el PDF, aproximadamente 0,93. Ambos son resultados reportados, no reproducidos. Se expone la discrepancia y se diferencia R² de accuracy. |
| Clasificación médica | [Sitio educativo](https://verapredictbreastcancer.web.app/), [documentación](https://verapredictbreastcancer.web.app/assets/Document_ML_Cancer_mama.pdf) y [código de app](https://github.com/VeraMxrtin/App_breast_cancer/blob/main/streamlit.py). El PDF identifica Breast Cancer Wisconsin (Diagnostic) vía Kaggle y describe revisión de nulos/duplicados, normalización y separación de datos. La app carga un archivo denominado `random_forest_top10.pkl` y grafica importancia con Plotly. SHAP figura en la documentación; no en ese código de interfaz. No se ofrece diagnóstico ni se trasladan métricas ambiguas al portafolio. |
| VeraFlow | Iniciativa independiente de CRM y automatización descrita en ambos CV. Se omiten afirmaciones comerciales de clientes o ingresos sin respaldo adicional. |
| MS Wisdom Press | Iniciativa de contenidos y comercio electrónico descrita en el CV original. Se conserva como emprendimiento y desarrollo; no se afirma empleo, ventas ni número de publicaciones. |
| TIKKY, BPMN, Bizagi y Bonita | Contenido del HTML original, conservado como proyectos complementarios. |
| LinkedIn | Dirección enlazada desde el perfil GitHub público. LinkedIn devuelve HTTP 999 ante la comprobación automatizada; no se certifica su accesibilidad de extremo a extremo. |
| Certificaciones | El CV original mencionaba cursos de SQL y Excel atribuidos a Kaggle sin enlaces de credenciales. No se publican como certificaciones verificadas. Pendientes de evidencia. |

Se retiraron la edad para evitar desactualización, Kaggle como empleador, el ahorro del 70 % sin evidencia y las afirmaciones genéricas de contribuciones open source/competencias sin respaldo. Se conservaron los tres proyectos de datos, desarrollo web, modelado de procesos, iniciativas, datos de contacto y archivos gráficos originales. No se añadió experiencia laboral por cuenta ajena porque no se aportó evidencia.

## CV descargable

Se generó un PDF A4 de una columna, una página, tipografía Arial incrustada, secciones convencionales y ocho enlaces URI. Su texto se puede extraer con pypdf y mantiene un orden de lectura lineal. Incluye habilidades y proyectos coherentes con la web. No contiene una imagen de la página ni reemplaza el PDF actualizado del usuario. El formato facilita el procesamiento por ATS; no se ha probado en un ATS comercial específico.

## Validación ejecutada

- `npm.cmd test`: tres pruebas aprobadas. Comprueban archivos/anclas, IDs únicos, metadatos, datos estructurados válidos, enlaces externos seguros, imágenes con dimensiones y alternativas, casos y PDF.
- `npm.cmd run build`: salida estática generada en `dist/`, sin instalación de paquetes npm ni dependencias de ejecución.
- `node --check index.js`: sintaxis válida.
- `git diff --check`: sin errores de espacios; Git avisa únicamente sobre conversión futura LF/CRLF.
- Chromium real a 1440×1000, 1024×768, 768×1024, 390×844 y 320×740: sin desbordamiento horizontal, imágenes cargadas, fichas expandibles y navegación correctas.
- Teclado: abrir/cerrar fichas con Enter; menú móvil, Escape y devolución del foco al botón; enlace para saltar al contenido.
- Movimiento reducido y funcionamiento sin JavaScript comprobados.
- axe-core 4.10.3, reglas WCAG 2 A/AA y 2.1 AA: cero incidencias automáticas en los cinco tamaños. Esto no sustituye una evaluación manual completa con lectores de pantalla.
- Sin errores de consola JavaScript ni respuestas HTTP de recursos locales de 400 o superiores.
- Descarga desde el botón en navegador: nombre correcto y contenido idéntico al PDF generado. pypdf confirma una página, texto extraíble y ocho enlaces.
- Sitios de proyectos, dos repositorios de código, perfil GitHub, documentación del oro y redirección WhatsApp: HTTP 200. Documentación médica descargada con éxito. LinkedIn bloquea la comprobación con HTTP 999.
- Capturas de escritorio y móvil inspeccionadas visualmente. Las nuevas imágenes de tarjetas proceden de las aplicaciones públicas, no son ilustraciones ni interfaces ficticias.

Las evidencias de ejecución se encuentran en `artifacts/browser-results.json`, `artifacts/link-results.json`, `artifacts/portfolio-*.png` y `.audit/`, excluidos de Git. El tamaño del paquete de producción es aproximadamente 310 KB; puede variar ligeramente al regenerar el PDF. El retrato optimizado ocupa aproximadamente 30 KB frente a 1,66 MB del original.

No se ejecutó Lighthouse ni se midieron Core Web Vitals de campo: no hay nuevo despliegue ni tráfico de usuarios. Se redujeron los factores de carga mediante recursos locales, WebP, carga diferida de imágenes de proyectos, dimensiones explícitas, JavaScript diferido y eliminación de CDN. No se afirma una puntuación Lighthouse, un valor de INP ni cumplimiento de métricas de producción.

## Pendientes antes de publicar

1. Confirmar periodo y estado académico de CERTUS; los marcadores están visibles en web y CV.
2. Facilitar enlaces verificables de certificaciones si se quieren incluir.
3. Resolver la discrepancia R² del oro y aportar fuente/versiones de datos, entrenamiento y partición temporal.
4. Completar la procedencia del dataset y la evaluación reproducible de Spotify.
5. Reproducir el entrenamiento médico y reconciliar sus métricas antes de usarlas como resultados. Revisar también las afirmaciones diagnósticas de la aplicación externa, que este repositorio no controla.
6. Revisar LinkedIn manualmente desde una sesión de navegador normal.

No se alteraron los sitios externos ni se probó el backend predictivo de cada proyecto. Que una demo responda HTTP 200 verifica su página, no garantiza inferencia disponible. No se enviaron mensajes, correos, formularios ni solicitudes de predicción.
