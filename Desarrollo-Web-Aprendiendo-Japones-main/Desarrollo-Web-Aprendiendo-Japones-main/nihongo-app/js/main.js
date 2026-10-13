/**
 * Maneja la lógica de los ejercicios en las lecciones
 */

document.addEventListener('DOMContentLoaded', () => {
    // Inicializar todos los ejercicios de la página
    const questionBlocks = document.querySelectorAll('.question-block');

    questionBlocks.forEach(block => {
        const options = block.querySelectorAll('.option-btn');
        const feedbackEl = block.querySelector('.feedback-msg');
        let solved = false;
        
        options.forEach(option => {
            option.addEventListener('click', function() {
                if (solved) return; // Si ya se resolvió, no hacer nada

                const isCorrect = this.dataset.correct === 'true';

                if (isCorrect) {
                    this.classList.add('correct');
                    feedbackEl.textContent = '¡Correcto! (正解 / Seikai)';
                    feedbackEl.className = 'feedback-msg success';
                    solved = true;
                    
                    // Deshabilitar todos los botones después de acertar
                    options.forEach(opt => {
                        opt.disabled = true;
                        opt.style.cursor = 'default';
                    });
                } else {
                    this.classList.add('incorrect');
                    feedbackEl.textContent = 'Incorrecto. Intenta de nuevo.';
                    feedbackEl.className = 'feedback-msg error';
                    
                    // Deshabilitar solo el botón incorrecto que se presionó
                    this.disabled = true;
                    this.style.cursor = 'not-allowed';
                }
            });
        });
    });
});
