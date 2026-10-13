# Metodología de Proyectos

Al iniciar, modificar o crear un proyecto, debes seguir SIEMPRE la siguiente metodología para mantener sincronizadas la PC y la Netbook:

1. **Sincronización Inicial (Pull)**: Si el proyecto ya es un repositorio Git, lo PRIMERO que haré antes de tocar nada es un `git pull` para descargar cualquier cambio que hayas hecho en tu otra computadora.
2. **Nuevos Proyectos (Git Init)**: Si entramos a trabajar en un proyecto que todavía no está en Git, mi primera acción será inicializar el repositorio (`git init`), hacer el primer commit y pedirte que lo subamos a GitHub. Así garantizamos que tu otra PC pueda acceder a él.
3. **Contexto Inicial**: Revisaré si existe un archivo `contexto.md`, `README.md` o similar para entender de qué trata el proyecto y en qué estado se encuentra.
4. **Actualización Constante**: Cada vez que realicemos modificaciones al proyecto, me aseguraré de reflejar esos cambios en el archivo de contexto.
5. **Control de Versiones Automático (Push)**: Al finalizar una tarea o cambio sustancial, realizaré un `git commit` y posteriormente un `git push` para que los cambios queden en la nube listos para tu otra computadora.
6. **Mantenimiento del Portafolio**:
   - Mantendré el portafolio actualizado con los nuevos proyectos.
   - Si detecto cambios en el portafolio, también le haré commit y push.
