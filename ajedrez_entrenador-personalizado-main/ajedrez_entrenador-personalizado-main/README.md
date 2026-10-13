# ♟️ Ajedrez Maestro: Entrenador Personalizado con IA Local

Este proyecto es una aplicación web interactiva diseñada para el estudio, práctica y dominio de aperturas de ajedrez. Ha evolucionado de un simple visor interactivo a un **Entrenador Virtual Inteligente**, operando de manera **100% offline y privada**.

## ✨ Características Principales

1. **Estudio y Práctica de Aperturas:**
   - **Modo Estudio:** Reproduce automáticamente o paso a paso las líneas teóricas de las aperturas más populares.
   - **Práctica Activa:** El usuario juega contra la máquina siguiendo la línea teórica. El sistema avisa de los errores y lleva un conteo de "Prácticas Perfectas".

2. **Modo Libre Clasificatorio (Ranked):**
   - Juega desde cualquier posición teórica contra un motor de ajedrez integrado (niveles del 1 al 5).
   - **Sistema ELO Local:** Ganar o perder contra la máquina ajustará tu ELO automáticamente usando cálculos oficiales.

3. **Dashboard, Estadísticas y Sincronización:**
   - Panel de control que registra tus Victorias, Empates y Derrotas, además del historial reciente de partidas jugadas con sus variaciones de ELO.
   - Tabla dinámica de **Dominio de Aperturas** que muestra en cuáles fallas y cuáles dominas por completo.
   - **Sincronización Dual (Navegador + Git):** Los datos se guardan en el navegador (`localStorage`) y en el archivo local `perfil_jugador.json` a través de `server.py`. Puedes hacer `git commit` y `git push`/`git pull` para mantener tu ELO y partidas sincronizadas entre varias computadoras (PC y netbook).

4. **Coach Virtual (Integración con Ollama):**
   - Integración nativa con **Ollama** para analizar tus estadísticas.
   - Envía tu ELO, historial de victorias y progreso de aperturas a un modelo de IA local (como `qwen2.5` o `llama3`).
   - El modelo actúa como un Gran Maestro, ofreciendo consejos estratégicos sobre qué debes estudiar a continuación.

---

## 🚀 Cómo Iniciar el Proyecto (Comandos de Consola)

Para usar la aplicación en tu día a día, necesitas levantar dos servicios locales: el servidor web y la IA.

### 1. Iniciar la Aplicación Web
Abre una terminal en esta carpeta (`/home/raul/Escritorio/proyectos/ajedrez_entrenador-personalizado`) y ejecuta el servidor Python nativo:
```bash
python3 server.py
```
*Luego, abre tu navegador web y entra a: `http://localhost:8080`*

### 2. Iniciar el Coach Virtual (Ollama)
Si configuraste Ollama como servicio automático de sistema (`systemd`) con los permisos CORS, **no necesitas hacer nada**, arranca solo. 

**Comandos útiles de Systemd para Ollama:**
```bash
# Reiniciar el servicio (si la IA se queda colgada)
sudo systemctl restart ollama

# Detener el servicio por completo
sudo systemctl stop ollama

# Ver el estado del servicio
sudo systemctl status ollama
```

**Si necesitas ejecutar Ollama manualmente (sin Systemd):**
Es obligatorio pasar la variable de entorno de CORS (`OLLAMA_ORIGINS="*"`) para que la aplicación web tenga permiso de hablar con Ollama.
```bash
OLLAMA_ORIGINS="*" ollama serve
```

---

## 🔒 Arquitectura y Privacidad
Este proyecto está diseñado bajo una estricta filosofía de privacidad total:
- **Sin Nube:** No hay llamadas a APIs externas (ni OpenAI, ni Google, ni Firebase).
- **Git Centralizado:** El archivo `perfil_jugador.json` se versiona en Git para sincronizar tu progreso entre PC y netbook de forma privada y controlada.
- **Frontend Puro:** No requiere instalación de paquetes `npm`, Node.js ni bases de datos SQL. Solo HTML, CSS y Vanilla JavaScript.
