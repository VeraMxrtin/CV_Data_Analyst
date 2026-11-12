# Logos de los proyectos

Coloca aquí tus logos reales con estos nombres:

- `ms-wisdom-press.png`
- `veraflow.png`
- `lima-kallpa.png`

También se admiten `.webp` o `.svg` con los mismos nombres base. Si hay varias versiones, el build elige PNG, después WebP y después SVG.

Para PNG o WebP, usa preferiblemente fondo transparente y al menos 400 px de ancho. No recortes partes del logo ni añadas márgenes excesivos. Se conservarán sus proporciones.

Ejecuta `npm.cmd run build`: los logos se incorporarán automáticamente a las tarjetas en `dist/`. Después usa `npm.cmd run dev` para verlos. No necesitas modificar HTML ni JavaScript.

Mientras no exista el archivo, la tarjeta muestra únicamente sus iniciales como marcador temporal, sin imágenes rotas ni solicitudes a archivos inexistentes. El HTML fuente conserva esos marcadores; la versión de producción usa los logos disponibles.
