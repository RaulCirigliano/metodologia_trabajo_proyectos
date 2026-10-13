document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('prompt-form');
    const resultsContainer = document.getElementById('results-container');
    const loadingState = document.getElementById('loading-state');

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        
        // Mostrar estado de carga
        resultsContainer.innerHTML = '';
        resultsContainer.classList.add('hidden');
        loadingState.classList.remove('hidden');

        // Capturar datos
        const projectName = document.getElementById('projectName').value.trim();
        const mainGoal = document.getElementById('mainGoal').value;
        const docCategoriesRaw = document.getElementById('docCategories').value;
        const tone = document.getElementById('tone').value;

        // Procesar categorías (una por línea, eliminar vacías)
        const categories = docCategoriesRaw
            .split('\n')
            .map(cat => cat.trim())
            .filter(cat => cat.length > 0);

        // Simular tiempo de procesamiento para el efecto UI
        setTimeout(() => {
            generarPrompts(projectName, mainGoal, categories, tone);
        }, 1200);
    });

    function generarPrompts(projectName, mainGoal, categories, tone) {
        loadingState.classList.add('hidden');
        resultsContainer.classList.remove('hidden');
        resultsContainer.classList.remove('empty-state');
        
        let htmlContent = '';

        // 1. Generar Prompt Maestro
        const masterPrompt = generarPromptMaestro(projectName, mainGoal, categories, tone);
        htmlContent += crearTarjetaPrompt('Prompt Maestro del Sistema', masterPrompt, 'master', 'Instrucción General');

        // 2. Generar Prompts Específicos basados en categorías
        const specificPrompts = generarPromptsEspecificos(projectName, mainGoal, categories, tone);
        
        specificPrompts.forEach(sp => {
            htmlContent += crearTarjetaPrompt(`Análisis de: ${sp.categoria}`, sp.prompt, 'specific', 'Consulta Específica');
        });

        // 3. Prompt de Síntesis
        const sintesisPrompt = generarPromptSintesis(categories);
        htmlContent += crearTarjetaPrompt('Síntesis Cruzada', sintesisPrompt, 'specific', 'Cruce de Datos');

        resultsContainer.innerHTML = htmlContent;

        // Añadir listeners para los botones de copiar
        document.querySelectorAll('.copy-btn').forEach(btn => {
            btn.addEventListener('click', function() {
                const textToCopy = this.getAttribute('data-clipboard-text');
                navigator.clipboard.writeText(textToCopy).then(() => {
                    const originalHTML = this.innerHTML;
                    this.innerHTML = `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> ¡Copiado!`;
                    this.classList.add('success');
                    
                    setTimeout(() => {
                        this.innerHTML = originalHTML;
                        this.classList.remove('success');
                    }, 2000);
                });
            });
        });
    }

    function generarPromptMaestro(projectName, mainGoal, categories, tone) {
        const tonos = {
            academico: "un tono académico, riguroso y formal",
            creativo: "un tono creativo, narrativo y cautivador",
            objetivo: "un tono completamente objetivo, neutral y directo",
            didactico: "un tono didáctico, explicando los conceptos complejos de forma sencilla (como un excelente profesor)"
        };

        const objetivos = {
            analisis_profundo: "realizar un análisis profundo, temático y exhaustivo de todos los materiales.",
            resumen: "generar resúmenes precisos y estructurados que capturen las ideas principales sin perder el contexto clave.",
            guia_estudio: "crear una guía de estudio estructurada, identificando conceptos clave, posibles preguntas y respuestas fundamentales.",
            creacion_contenido: "extraer ideas fascinantes y redactar material listo para usarse en la creación de contenido (como guiones de podcast o artículos de blog).",
            extraccion_datos: "extraer datos, fechas, nombres y hechos específicos, presentándolos de forma estructurada."
        };

        const catsTexto = categories.join(", ");

        return `Actúa como un analista experto y asistente personal para el proyecto "${projectName}". 
He subido varios documentos que están categorizados de la siguiente manera: [${catsTexto}].

Tu objetivo principal es ${objetivos[mainGoal]}
Debes responder siempre utilizando ${tonos[tone]}.

Reglas estrictas:
1. Basa tus respuestas ÚNICA Y EXCLUSIVAMENTE en los documentos proporcionados. Si la respuesta no está en los textos, indica claramente que no tienes esa información.
2. Cuando hagas una afirmación, intenta citar explícitamente a qué categoría de documento (ej. "${categories[0]}") pertenece la información.
3. Mantén la coherencia con el contexto global del proyecto "${projectName}".

Por favor, confirma que has entendido estas instrucciones respondiendo con un breve resumen de cómo vas a abordar el análisis.`;
    }

    function generarPromptsEspecificos(projectName, mainGoal, categories, tone) {
        const prompts = [];
        
        categories.forEach(cat => {
            let promptText = "";
            
            if (mainGoal === 'resumen') {
                promptText = `Enfócate exclusivamente en los documentos de la categoría "${cat}". 
Por favor, genera un resumen estructurado con viñetas destacando los 5 puntos más importantes que se abordan en esta sección. Ignora los demás documentos por ahora.`;
            } else if (mainGoal === 'analisis_profundo') {
                promptText = `Analiza críticamente la información contenida en los documentos de la categoría "${cat}". 
Identifica los temas subyacentes, los posibles sesgos (si los hay) y cómo esta información contribuye al panorama general de "${projectName}".`;
            } else if (mainGoal === 'guia_estudio') {
                promptText = `Utilizando los documentos de la categoría "${cat}", elabora 5 preguntas de opción múltiple y 3 preguntas de desarrollo que evaluarían la comprensión profunda de esta sección. Proporciona las respuestas correctas al final.`;
            } else if (mainGoal === 'creacion_contenido') {
                promptText = `Revisa los documentos de la categoría "${cat}" y extrae las 3 "pepitas de oro" o hechos más sorprendentes/interesantes. 
Escribe un breve gancho (hook) para un guión de podcast o hilo de Twitter basado en esos hallazgos.`;
            } else {
                promptText = `Extrae todas las entidades clave (personas, lugares, fechas, conceptos técnicos) mencionadas específicamente en los documentos de la categoría "${cat}" y preséntalas en formato de tabla.`;
            }
            
            prompts.push({ categoria: cat, prompt: promptText });
        });

        return prompts;
    }

    function generarPromptSintesis(categories) {
        if (categories.length < 2) {
            return `Revisa todos los documentos proporcionados y genera una conclusión unificada que conecte los puntos principales.`;
        }

        const cat1 = categories[0];
        const cat2 = categories[1];

        return `Ahora necesito que cruces información. Analiza las conexiones, similitudes o contradicciones entre lo expuesto en los documentos de la categoría "${cat1}" y los de la categoría "${cat2}". 
¿Cómo cambia nuestra comprensión del tema al analizar ambas fuentes en conjunto en lugar de por separado?`;
    }

    function crearTarjetaPrompt(titulo, contenido, tipoClass, badgeText) {
        // Escapar comillas para el atributo de datos
        const contenidoEscapado = contenido.replace(/"/g, '&quot;');
        
        return `
            <div class="prompt-card ${tipoClass}">
                <div class="prompt-header">
                    <span class="prompt-title">${titulo}</span>
                    <span class="prompt-badge">${badgeText}</span>
                </div>
                <div class="prompt-content">${contenido}</div>
                <div class="clearfix">
                    <button class="copy-btn" data-clipboard-text="${contenidoEscapado}">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                        Copiar Prompt
                    </button>
                </div>
            </div>
        `;
    }
});
