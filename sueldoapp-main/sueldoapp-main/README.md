# Calculadora Salarial Docente (DGCyE)

Una aplicación web moderna diseñada para leer recibos de sueldo en formato PDF de la Dirección General de Cultura y Educación (DGCyE) de la Provincia de Buenos Aires. 

La herramienta extrae inteligentemente los haberes y descuentos específicos, mostrando un desglose detallado y calculando automáticamente el 20% del haber neto.

## Características

- **Procesamiento 100% Local (Frontend)**: Utiliza `pdf.js` para extraer y procesar el texto del recibo directamente en la memoria de tu navegador. Tu PDF nunca sale de tu computadora o celular, garantizando total privacidad.
- **Detección Precisa por Códigos**: Extrae haberes y descuentos buscando los códigos numéricos estandarizados por la DGCyE (ej. 0220 para Antigüedad, 1060 para IPS, etc.), evadiendo errores visuales del PDF.
- **Desglose de Cálculo**: Muestra exactamente qué ítems fueron sumados como haberes y cuáles fueron restados como deducciones (IOMA e IPS), aportando transparencia total al cálculo final.
- **Diseño Premium**: Interfaz moderna en modo oscuro, con estética 'Glassmorphism' y diseño completamente adaptado para uso en teléfonos celulares.

## Cómo Usarlo

1. Abre el archivo `index.html` en cualquier navegador web moderno.
2. Selecciona o arrastra tu recibo de sueldo en formato PDF.
3. Haz clic en "Procesar PDF".
4. Visualiza el desglose exacto y el resultado del 20%.

## Despliegue en la Nube

El proyecto está diseñado con arquitectura estática (HTML/CSS/JS), por lo que está listo para ser alojado de forma gratuita y rápida en plataformas como **Cloudflare Pages**, GitHub Pages o Vercel, permitiéndote acceder desde tu celular en cualquier lugar sin necesidad de alquilar un servidor.
