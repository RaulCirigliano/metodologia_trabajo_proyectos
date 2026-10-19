# Checklist Base (todo proyecto web, incluso en localhost)

Los ítems son ilustrativos del principio que los encabeza. Para cada uno: buscar evidencia
en el código real y verificar ejecutando. Ítem no verificable = **NO VERIFICADO**.

## 1. Estructura y semántica
- Documento válido: `<!doctype html>`, `lang`, `charset`, `viewport`, `<title>` único.
- Landmarks y jerarquía de encabezados coherente (`header/nav/main/footer`, un `h1`).
- Elementos correctos para cada función (botón = `<button>`, enlace = `<a>`).

## 2. Interacción y componentes
- Sin diálogos nativos bloqueantes del navegador para flujos de la app (`alert`,
  `confirm`, `prompt`); usar componentes no bloqueantes propios (modal, toast).
- **Un solo patrón por tipo de componente en toda la interfaz** (desplegables, modales,
  botones, formularios). Detectar con grep todas las instancias del patrón viejo.
- Controles personalizados con teclado completo, foco visible y roles/atributos ARIA
  correctos; si un control nativo alcanza, preferirlo.
- Estados explícitos: carga, vacío, error, éxito.

## 3. Accesibilidad (mínimo WCAG 2.2 AA como objetivo)
- Contraste suficiente, tamaño de objetivo táctil, foco visible, orden de tabulación lógico.
- Texto alternativo en imágenes informativas; etiquetas asociadas a cada campo.
- No transmitir información solo por color. Respetar `prefers-reduced-motion`.

## 4. Responsive y diseño
- Se ve y funciona de móvil a escritorio sin scroll horizontal ni elementos cortados.
- Sistema de diseño coherente: variables/tokens de color, espaciado y tipografía.
- Listas largas y contenedores con desborde controlado (scroll propio, sin recortes).

## 5. Rendimiento y recursos
- Nada de compiladores o builds "de desarrollo" cargados en el navegador del usuario final
  (por ejemplo un CDN de utilidades que genera CSS al vuelo).
- Imágenes dimensionadas, formatos modernos, `loading="lazy"` donde corresponda.
- Polling/timers respetan la visibilidad de la pestaña y se limpian al salir; sin
  llamadas periódicas ciegas.
- Sin trabajo pesado en el hilo principal; sin `innerHTML` con datos sin sanear.

## 6. Mantenibilidad y caché
- Código modular, sin variables globales innecesarias; archivos de tamaño razonable.
- Recursos estáticos con versionado o hash para evitar caché obsoleta.
- Sin dependencias externas innecesarias; las que existan, fijadas a versión.

## 7. Robustez
- Errores de red y de API manejados con mensaje claro al usuario (sin fallo silencioso).
- Entradas del usuario validadas y saneadas antes de insertarse en el DOM.
- Sin secretos ni tokens en el código del cliente.
