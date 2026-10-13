# 💰 BalanceApp - Gestión Financiera y de Proyectos

![Versión](https://img.shields.io/badge/version-1.2.0-blue.svg)
![Licencia](https://img.shields.io/badge/license-MIT-green.svg)
![Tecnologías](https://img.shields.io/badge/tech-HTML|CSS|JS|Python-orange.svg)

**BalanceApp** es una herramienta integral diseñada para el control total de finanzas personales y la gestión de proyectos creativos. Con una interfaz moderna basada en **Glassmorphism**, permite visualizar el balance mensual, proyectar cuotas de tarjetas de crédito y administrar procesos de taller de manera eficiente.

> **Transforma tus finanzas y organiza tu taller con una interfaz moderna y automatización inteligente.**

---

## 🚀 Características Principales

### 📊 Gestión Financiera
- **Balance Mensual:** Visualización clara de ingresos vs. egresos con indicadores de saldo en tiempo real.
- **Control de Cuotas:** Seguimiento automatizado de consumos con tarjeta (Visa/Mastercard) con proyección de cuotas a meses futuros.
- **Ingresos Recurrentes:** Configuración de sueldos o ingresos fijos para una proyección financiera automática.
- **Comparativa Anual:** Gráficos dinámicos e interactivos para analizar la evolución de tus gastos mes a mes.
- **Ajuste de Efectivo:** Herramienta inteligente para cuadrar el saldo teórico del sistema con el dinero real en mano.

### 🔨 Gestión de Proyectos (Taller)
- **Control de Piezas:** Registro detallado de proyectos con estados personalizables (Iniciado, En Proyecto, Finalizado).
- **Bitácora Visual:** Galería fotográfica integrada por proyecto para documentar cada etapa del progreso.
- **Informe de Costos:** Cálculo automático de materiales, mano de obra y horas hombre invertidas.
- **Calendario de Entrega:** Integración visual de cronogramas y plazos para una mejor organización.

### 📱 Experiencia de Usuario Premium
- **Diseño Glassmorphism:** Estética oscura y moderna con efectos de desenfoque, transparencias y gradientes vibrantes.
- **Mobile First:** Navegación optimizada para dispositivos móviles mediante una barra inferior intuitiva y gestos.
- **Privacidad Local:** Tus datos te pertenecen. El almacenamiento es local (`localStorage`) y permite exportación/importación total vía JSON.

---

## 🤖 Automatización: Extracción de Datos

BalanceApp incluye un potente motor de procesamiento de datos en Python para evitar la carga manual de gastos:

1. **Coloca tus resúmenes:** Guarda tus resúmenes bancarios en formato `.pdf` (Visa o Mastercard) en la carpeta raíz del proyecto.
2. **Procesa la información:** Ejecuta el script de automatización:
   ```bash
   python importar_pdfs.py
   ```
3. **Importación Directa:** El script generará un archivo `nuevos_gastos.json`. Desde la sección de **Configuración** de la App, selecciona "Importar" y selecciona este archivo para actualizar tu balance al instante.

---

## 🛠️ Tecnologías Utilizadas

- **Frontend:** HTML5, Vanilla CSS3 (Glassmorphism), JavaScript (ES6+).
- **Visualización:** [Chart.js](https://www.chartjs.org/) con plugins para etiquetas dinámicas.
- **Automatización:** Python 3.10+, [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/) para extracción de datos.
- **Iconografía:** [FontAwesome 6](https://fontawesome.com/).
- **Tipografía:** [Google Fonts (Outfit)](https://fonts.google.com/specimen/Outfit).

---

## 📦 Instalación y Uso

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/RaulCirigliano/agregado_backup_completo.git
   ```
2. **Requisitos de Python (opcional para automatización):**
   ```bash
   pip install pymupdf
   ```
3. **Lanzar la App:**
   - Simplemente abre `balance-app/index.html` en tu navegador.
   - O usa el archivo `abrir_balance.bat` si estás en Windows para un acceso rápido.

---

## 📂 Estructura del Proyecto

- `/balance-app`: Código fuente de la aplicación web (Dashboard).
- `importar_pdfs.py`: Script de Python para extraer gastos de resúmenes bancarios.
- `extract.py`: Utilidades de procesamiento de texto y limpieza de datos.
- `abrir_balance.bat`: Lanzador rápido para el entorno local.
- `balance_completo_*.json`: Archivos de copia de seguridad de datos.

---

## 🚀 Hoja de Ruta (Roadmap)

- [ ] Implementación de un modo oscuro/claro automático.
- [ ] Exportación de reportes detallados en PDF.
- [ ] Integración con APIs bancarias (donde sea posible).
- [ ] Sistema de notificaciones para vencimientos de cuotas.

---
Desarrollado con ❤️ por [Raúl Cirigliano](https://github.com/RaulCirigliano)
