# Portafolio de Inés Torrent 🎨

Sitio web oficial y portafolio virtual de la destacada artista plástica y pintora contemporánea argentina, **Inés Torrent**.

Este proyecto está diseñado con un enfoque minimalista y elegante para cederle todo el protagonismo a las obras de arte, asegurando al mismo tiempo una excelente experiencia de usuario y optimización para motores de búsqueda (SEO).

## ✨ Características Principales

- **Diseño Minimalista:** Interfaz limpia, con líneas rectas y fondos neutros, emulando la experiencia de una galería de arte real.
- **Galería Dinámica offline:** Las obras se inyectan en el DOM mediante Vanilla JavaScript desde un listado estructurado, permitiendo actualizar la galería fácilmente sin tocar el HTML.
- **Visor de Imágenes (Lightbox):** Modal integrado personalizado para ampliar las obras y navegar entre ellas cómodamente sin salir de la página.
- **Carrusel a Pantalla Completa:** Página de inicio (`index.html`) con un pase de diapositivas que ocupa todo el marco de la pantalla y utiliza transiciones suaves de opacidad.
- **SEO Optimizado:** Etiquetas semánticas, Open Graph y archivo `sitemap.xml` integrados para indexación rápida en Google Search Console y previsualizaciones perfectas en WhatsApp/Redes Sociales.
- **Rendimiento (Performance):** Imágenes estandarizadas y convertidas a formato `.webp`, cargando decenas de obras en un abrir y cerrar de ojos.

## 🛠️ Tecnologías Utilizadas

- **HTML5:** Estructura modular y accesible.
- **CSS3:** Variables globales, Flexbox, CSS Grid y diseño completamente responsivo (adaptable a dispositivos móviles).
- **JavaScript (ES6):** Toda la lógica es "Vanilla" (sin frameworks ni librerías como jQuery). Incluye un script general para inyectar dinámicamente la barra de navegación (Navbar) en todas las páginas, reduciendo la redundancia de código.

## 📂 Estructura del Proyecto

```text
/
├── index.html            # Inicio (Carrusel a pantalla completa)
├── sobre_mi.html         # Biografía y trayectoria con foto de perfil
├── sobre_mi_obra.html    # Reseña de su concepto artístico
├── galeria.html          # Cuadrícula de obras
├── carrusel.html         # presentacion de obras seleccionadas
├── contacto.html         # Datos directos, redes sociales y Google Maps
├── estilos.css           # Hoja de estilos global y unificada
├── script.js             # Lógica del navbar y carrusel de inicio
├── galeria.js            # Listado de obras y lógica del Lightbox
├── sitemap.xml           # Mapa del sitio para indexación web
└── imagenes/             # Directorio con todas las fotografías locales (.webp)
```

## 🚀 Ejecución y Despliegue

Este es un sitio web estático sin dependencias (Serverless/Static Site). No requiere instalación de Node.js, NPM, ni bases de datos.

**Para ejecutarlo localmente:**
Basta con clonar el repositorio y abrir el archivo `index.html` en cualquier navegador web.

**Para publicarlo en producción:**
El proyecto está estructurado para ser desplegado instantáneamente en plataformas de alojamiento modernas como **Cloudflare Pages** (recomendado para aprovechar su CDN global), GitHub Pages o Netlify.

---

*© Proyecto desarrollado para la difusión y apreciación del trabajo de Ines Torrent por Raúl Cirigliano.*
