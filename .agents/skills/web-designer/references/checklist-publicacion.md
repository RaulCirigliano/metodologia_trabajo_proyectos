# Checklist de Publicación (se suma al Base si el sitio va a internet)

Agnóstico al proveedor (hosting estático, VPS con servidor propio, etc.). Si algo depende
del hosting concreto, identificar el hosting real del proyecto antes de afirmar nada.
Ítems ilustrativos: manda el principio. Sin poder ejecutarlo = **NO VERIFICADO**.

## 1. Transporte y seguridad
- HTTPS obligatorio con redirección desde HTTP; HSTS cuando el dominio ya sea estable.
- Cabeceras de seguridad revisadas: `Content-Security-Policy`, `X-Content-Type-Options`,
  `Referrer-Policy`, `Permissions-Policy`, protección contra clickjacking
  (`frame-ancestors` / `X-Frame-Options`).
- Cookies con `Secure`, `HttpOnly` y `SameSite` cuando existan.
- Sin secretos en el repositorio ni en el cliente. Dependencias sin vulnerabilidades
  conocidas.
- CORS restrictivo; nada de `*` donde haya datos o credenciales.

## 2. Rendimiento medible
- Core Web Vitals en objetivo (LCP, INP, CLS). Medir con Lighthouse o equivalente y
  registrar el valor, no estimarlo.
- Compresión (gzip/brotli), caché con política explícita (assets versionados con caché
  larga; HTML con caché corta o revalidación).
- Recursos críticos priorizados; JS y CSS no usados eliminados; fuentes con
  `font-display` y precarga cuando corresponda.

## 3. Descubrimiento y metadatos
- `title`, `meta description`, URL canónica, Open Graph/Twitter Cards.
- `robots.txt`, `sitemap.xml`, favicon e iconos; `404` y `500` propios.
- Datos estructurados donde aporten valor.

## 4. Operación y resiliencia
- Entorno de producción separado del desarrollo (variables de entorno, sin modo debug).
- Registro y monitoreo de errores; plan de respaldo y de reversión (rollback).
- Despliegue reproducible y documentado (comandos o pipeline).
- Dominio, DNS y certificados con renovación automática.

## 5. Legal y privacidad (según corresponda)
- Política de privacidad y manejo de consentimiento si hay cookies o analítica.
- Revisar si el sitio recolecta datos personales y dónde se almacenan.

## 6. Verificación previa a publicar
- Probar en al menos dos navegadores y en móvil real o emulado.
- Pasar validadores (HTML, accesibilidad, enlaces rotos) y registrar el resultado.
- Documentar en `contexto.md` el hosting, el dominio y el procedimiento de despliegue.
