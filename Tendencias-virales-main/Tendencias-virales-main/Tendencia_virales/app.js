const promptType = document.getElementById('prompt-type');
const locationInput = document.getElementById('location');
const promptDisplay = document.getElementById('prompt-text');
const copyBtn = document.getElementById('copy-btn');
const boomVerdict = document.getElementById('boom-verdict');

const promptTemplates = {
    ceramica: (loc) => `Actúa como un experto en diseño de objetos y arte contemporáneo. Identifica tendencias visuales y estéticas (formas, texturas, personajes) que estén siendo virales en redes sociales y que posean un alto potencial para ser traducidas a piezas de cerámica o escultura física. Busca formas orgánicas, personajes 'kawaii' con volúmenes interesantes o accesorios decorativos que cumplan con la premisa de bajo costo y alto impacto visual en [${loc}].`,
    consumo: (loc) => `Actúa como un analista de tendencias de consumo. Identifica objetos, accesorios o fenómenos estéticos 'micro-virales' que estén teniendo un crecimiento explosivo en redes sociales (TikTok/Instagram) en [${loc}] durante el último mes. Busca artículos de bajo costo o accesorios 'kawaii' similares al fenómeno de los patitos con hélice.`,
    cultural: (loc) => `Resume los temas de conversación dominantes, memes emergentes y 'slang' que se han vuelto virales en el ecosistema digital de habla hispana en las últimas dos semanas en [${loc}]. Clasifícalos por nivel de popularidad y explica brevemente el origen de cada uno.`,
    mercado: (loc) => `Analiza las búsquedas crecientes en plataformas de e-commerce en la región de [${loc}]. ¿Qué productos de regalo o 'gadgets' curiosos muestran un aumento puntual de demanda superior al 50% este mes? Ignora productos estacionales estándar y enfócate en novedades virales.`
};

function updatePrompt() {
    const type = promptType.value;
    const loc = locationInput.value || 'Argentina';
    promptDisplay.innerText = promptTemplates[type](loc);
}

promptType.addEventListener('change', updatePrompt);
locationInput.addEventListener('input', updatePrompt);

copyBtn.addEventListener('click', () => {
    const text = promptDisplay.innerText;
    navigator.clipboard.writeText(text).then(() => {
        const originalText = copyBtn.innerText;
        copyBtn.innerText = '¡Copiado!';
        copyBtn.style.background = '#00f2ff';
        copyBtn.style.color = '#000';
        setTimeout(() => {
            copyBtn.innerText = originalText;
            copyBtn.style.background = '';
            copyBtn.style.color = '';
        }, 2000);
    });
});

// Identification Logic
let activeChecks = 0;

function toggleCheck(el) {
    el.classList.toggle('active');
    
    if (el.classList.contains('active')) {
        activeChecks++;
    } else {
        activeChecks--;
    }

    updateVerdict();
}

function updateVerdict() {
    boomVerdict.style.display = 'block';
    if (activeChecks === 3) {
        boomVerdict.innerHTML = '<strong style="color: #00f2ff;">PROBABLE BOOM:</strong> Esto tiene todas las señales de ser el nuevo "patito".';
        boomVerdict.style.background = 'rgba(0, 242, 255, 0.1)';
        boomVerdict.style.border = '1px solid rgba(0, 242, 255, 0.3)';
    } else if (activeChecks > 0) {
        boomVerdict.innerHTML = '<strong style="color: #ff3d81;">INTERESANTE:</strong> Tiene potencial, pero le faltan factores de viralidad.';
        boomVerdict.style.background = 'rgba(255, 61, 129, 0.1)';
        boomVerdict.style.border = '1px solid rgba(255, 61, 129, 0.3)';
    } else {
        boomVerdict.style.display = 'none';
    }
}

// Initial Call
updatePrompt();
