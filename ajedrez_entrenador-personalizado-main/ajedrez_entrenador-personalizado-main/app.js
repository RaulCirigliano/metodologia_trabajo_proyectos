/**
 * Chess Openings Trainer - Main Application Controller
 * Handles study mode, interactive practice mode, openings navigation,
 * hint system, and feedback.
 */

document.addEventListener('DOMContentLoaded', () => {


// --- ELO AND GAME OVER LOGIC ---
let gameProcessed = false;

function processGameOverElo() {
  if (!state.engine.isGameOver() || state.currentMode !== 'free' || gameProcessed) return;

  const isCheckmate = state.engine.isCheckmate();
  const isDraw = !isCheckmate;
  const userIsWhite = state.boardUI.orientation === 'w';
  const lastMoveWhite = state.engine.turn === 'b'; // the turn has already flipped after the last move

  let result = 0.5; // Draw
  let resultText = "Empate";
  if (isCheckmate) {
    const userWon = (userIsWhite && lastMoveWhite) || (!userIsWhite && !lastMoveWhite);
    result = userWon ? 1 : 0;
    resultText = userWon ? "¡Ganaste!" : "Perdiste";
  }

  // Calculate ELO
  const aiEloMap = { 1: 600, 2: 900, 3: 1200, 4: 1500, 5: 1800, 6: 2200 };
  const aiElo = aiEloMap[state.aiLevelId] || 1200;
  
  const expectedScore = 1 / (1 + Math.pow(10, (aiElo - userProfile.elo) / 400));
  const K = 32;
  const eloChange = Math.round(K * (result - expectedScore));
  
  const oldElo = userProfile.elo;
  userProfile.elo = Math.max(400, userProfile.elo + eloChange); // Minimum 400 ELO
  
  userProfile.gamesPlayed = (userProfile.gamesPlayed || 0) + 1;
  if (result === 1) userProfile.wins = (userProfile.wins || 0) + 1;
  else if (result === 0) userProfile.losses = (userProfile.losses || 0) + 1;
  else userProfile.draws = (userProfile.draws || 0) + 1;

  // Record opening-specific stats
  if (!userProfile.openingStats) userProfile.openingStats = {};
  const opId = (state.currentOpening && state.currentOpening.id) || 'libre';
  const opName = (state.currentOpening && state.currentOpening.name) || 'Tablero Libre';
  if (!userProfile.openingStats[opId]) userProfile.openingStats[opId] = { wins: 0, losses: 0, draws: 0 };
  if (result === 1) userProfile.openingStats[opId].wins++;
  else if (result === 0) userProfile.openingStats[opId].losses++;
  else userProfile.openingStats[opId].draws++;

  // Record match history
  if (!userProfile.history) userProfile.history = [];
  userProfile.history.unshift({
    date: new Date().toISOString(),
    openingId: opId,
    openingName: opName,
    aiLevelId: state.aiLevelId,
    aiElo: aiElo,
    result: result === 1 ? 'win' : (result === 0 ? 'loss' : 'draw'),
    resultText: resultText,
    userEloBefore: oldElo,
    userEloAfter: userProfile.elo,
    eloChange: eloChange
  });
  if (userProfile.history.length > 50) userProfile.history.pop();
  
  saveProfile();
  gameProcessed = true;

  showEloNotification(resultText, oldElo, userProfile.elo, eloChange, aiElo);
}

function showEloNotification(resultText, oldElo, newElo, eloChange, aiElo) {
  const sign = eloChange > 0 ? '+' : '';
  const color = eloChange > 0 ? '#10b981' : (eloChange < 0 ? '#ef4444' : '#f59e0b');
  
  // Create a modal dynamic
  const modalHTML = `
    <div id="elo-modal" class="modal-overlay open" style="z-index: 2000;">
      <div class="modal-content" style="max-width: 350px; text-align: center; padding: 2rem;">
        <h2 style="font-size: 1.8rem; margin-bottom: 0.5rem; color: ${color};">${resultText}</h2>
        <p style="color: var(--text-muted); margin-bottom: 1.5rem;">Jugaste contra la IA (Nivel ${state.aiLevelId} - ELO ${aiElo})</p>
        
        <div style="font-size: 3rem; font-weight: bold; margin-bottom: 0.5rem;">
          ${newElo}
        </div>
        <div style="font-size: 1.2rem; color: ${color}; font-weight: bold; margin-bottom: 2rem;">
          ${sign}${eloChange}
        </div>
        
        <button id="btn-close-elo" class="btn btn-primary" style="width: 100%;">Aceptar</button>
      </div>
    </div>
  `;
  
  document.body.insertAdjacentHTML('beforeend', modalHTML);
  document.getElementById('btn-close-elo').addEventListener('click', () => {
    document.getElementById('elo-modal').remove();
  });
}


// --- OLLAMA VIRTUAL COACH ---
const btnAskCoach = document.getElementById('btn-ask-coach');
if (btnAskCoach) {
  btnAskCoach.addEventListener('click', async () => {
    const modelName = document.getElementById('input-ollama-model').value || 'llama3';
    const container = document.getElementById('coach-response-container');
    const textEl = document.getElementById('coach-response-text');
    
    container.style.display = 'block';
    textEl.innerHTML = `<i>Analizando tu perfil y conectando con Ollama (${modelName})...</i>`;

    const practiceStats = getProgressStats();
    const gameStats = userProfile.openingStats || {};
    
    // Create a readable summary of stats for the prompt
    let statsSummary = "";
    const interactedIds = new Set([...Object.keys(practiceStats), ...Object.keys(gameStats)]);
    interactedIds.forEach(id => {
      const p = practiceStats[id] || { perfectRuns: 0 };
      const g = gameStats[id] || { wins: 0, losses: 0, draws: 0 };
      statsSummary += `- Apertura ID '${id}': ${p.perfectRuns} prácticas perfectas, ${g.wins} victorias, ${g.draws} empates, ${g.losses} derrotas.\n`;
    });
    
    if (!statsSummary) statsSummary = "Aún no tengo estadísticas de aperturas, soy nuevo.";

    const prompt = `Eres un Gran Maestro de Ajedrez y mi coach personal. Te hablo desde mi aplicación local de entrenamiento.
Mi nombre es ${userProfile.name} y mi ELO actual es ${userProfile.elo}.
He jugado un total de ${userProfile.gamesPlayed || 0} partidas: ${userProfile.wins || 0} victorias, ${userProfile.draws || 0} empates y ${userProfile.losses || 0} derrotas.

Mi historial detallado por apertura es el siguiente:
${statsSummary}

Analiza brevemente mis datos. Identifica en qué soy bueno y en qué estoy fallando. Dame un consejo de máximo 2 o 3 párrafos cortos en español sobre qué debo estudiar a continuación o cómo mejorar. Sé directo, estratégico y motivador. No uses formato markdown complejo, solo texto claro.`;

    try {
      const response = await fetch('http://localhost:11434/api/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          model: modelName,
          prompt: prompt,
          stream: false
        })
      });
      
      if (!response.ok) throw new Error('Error HTTP: ' + response.status);
      
      const data = await response.json();
      textEl.innerHTML = data.response.replace(/\n/g, '<br>');
      
    } catch (err) {
      textEl.innerHTML = `<span style="color:#ef4444;"><b>Error de conexión con Ollama:</b> No se pudo conectar a localhost:11434.</span><br><br>
      <small style="color:var(--text-muted)">1. Asegúrate de que Ollama esté instalado y ejecutándose.<br>
      2. Asegúrate de haber descargado el modelo (ej: <code>ollama run llama3</code>).<br>
      3. <b>Importante:</b> Para que la web pueda conectarse, debes iniciar Ollama habilitando los permisos CORS. Si usas Linux, ejecuta este comando en la terminal antes de iniciar Ollama:<br><br>
      <code>OLLAMA_ORIGINS="*" ollama serve</code></small>`;
      console.error("Ollama Error:", err);
    }
  });
}
// --- END OLLAMA COACH ---

// --- USER PROFILE SYSTEM ---
const btnProfile = document.getElementById('btn-profile');
const profileModal = document.getElementById('profile-modal');
const btnCloseProfile = document.getElementById('btn-close-profile');
const btnSaveProfile = document.getElementById('btn-save-profile');
const inputProfileName = document.getElementById('input-profile-name');
const inputProfileElo = document.getElementById('input-profile-elo');
const profileNameDisplay = document.getElementById('profile-name-display');
const profileEloDisplay = document.getElementById('profile-elo-display');

let userProfile = {
  name: 'Jugador',
  elo: 1200,
  gamesPlayed: 0,
  wins: 0,
  losses: 0,
  draws: 0,
  history: [],
  openingStats: {},
  practiceStats: {},
  lastUpdated: null
};

async function loadProfile() {
  // 1. Cargar desde localStorage para disponibilidad instantánea en UI
  let localData = null;
  const rawLocal = localStorage.getItem('chessUserProfile') || localStorage.getItem('chess_coach_profile');
  if (rawLocal) {
    try {
      localData = JSON.parse(rawLocal);
    } catch (e) {
      console.error("Error al leer perfil de localStorage", e);
    }
  }

  // Compatibilidad: migrar ELO antiguo si existía
  const oldElo = localStorage.getItem('chess_user_elo');
  if (!localData && oldElo) {
    localData = {
      name: 'Jugador',
      elo: parseInt(oldElo, 10) || 1200,
      gamesPlayed: 0,
      wins: 0,
      losses: 0,
      draws: 0,
      history: [],
      openingStats: {},
      practiceStats: {}
    };
  }

  if (localData) {
    userProfile = Object.assign({}, userProfile, localData);
    if (!userProfile.history) userProfile.history = [];
    if (!userProfile.openingStats) userProfile.openingStats = {};
    if (!userProfile.practiceStats) userProfile.practiceStats = {};
    updateProfileUI();
  }

  // 2. Cargar perfil_jugador.json desde el servidor/archivo para sincronizar entre máquinas
  try {
    const res = await fetch(`perfil_jugador.json?t=${Date.now()}`);
    if (res.ok) {
      const fileData = await res.json();
      if (fileData && typeof fileData === 'object') {
        const fileGames = fileData.gamesPlayed || 0;
        const localGames = (localData && localData.gamesPlayed) || 0;
        const fileTime = fileData.lastUpdated ? new Date(fileData.lastUpdated).getTime() : 0;
        const localTime = (localData && localData.lastUpdated) ? new Date(localData.lastUpdated).getTime() : 0;

        let shouldUseFile = false;
        if (!localData) {
          shouldUseFile = true;
        } else if (fileGames > localGames) {
          shouldUseFile = true;
        } else if (fileTime > localTime && fileGames >= localGames) {
          shouldUseFile = true;
        }

        // Evitar que el archivo por defecto de git sobreescriba un ELO local migrado
        if (shouldUseFile && fileGames === 0 && (!fileData.history || fileData.history.length === 0) && localData && (localData.elo !== 1200 || localGames > 0)) {
          shouldUseFile = false;
        }

        if (shouldUseFile) {
          userProfile = Object.assign({}, userProfile, fileData);
          if (!userProfile.history) userProfile.history = [];
          if (!userProfile.openingStats) userProfile.openingStats = {};
          if (!userProfile.practiceStats) userProfile.practiceStats = {};

          // Actualizar localStorage con los datos del repositorio
          localStorage.setItem('chessUserProfile', JSON.stringify(userProfile));
          localStorage.setItem('chess_coach_profile', JSON.stringify(userProfile));

          // Sincronizar estadísticas de práctica si vienen en el archivo
          if (fileData.practiceStats && Object.keys(fileData.practiceStats).length > 0) {
            try {
              const currentPract = getProgressStats();
              const mergedPract = Object.assign({}, fileData.practiceStats, currentPract);
              localStorage.setItem('chess_openings_stats', JSON.stringify(mergedPract));
            } catch (err) {}
          }
        } else if (localData && (localGames > fileGames || localTime > fileTime)) {
          // El navegador tiene cambios más recientes no guardados en el archivo: sincronizar al archivo
          saveProfile();
        }
      }
    }
  } catch (err) {
    console.log("No se pudo conectar con perfil_jugador.json (modo offline), usando localStorage.");
  }

  updateProfileUI();
  populateDashboard();
}

async function saveProfile() {
  userProfile.lastUpdated = new Date().toISOString();

  // Guardar también las estadísticas de práctica en el perfil
  try {
    userProfile.practiceStats = getProgressStats();
  } catch (e) {}

  // 1. Guardar en localStorage bajo ambas claves para compatibilidad absoluta
  localStorage.setItem('chessUserProfile', JSON.stringify(userProfile));
  localStorage.setItem('chess_coach_profile', JSON.stringify(userProfile));

  updateProfileUI();

  // 2. Guardar en perfil_jugador.json mediante el backend de server.py
  try {
    const res = await fetch('/api/save-profile', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(userProfile)
    });
    const syncStatusEl = document.getElementById('sync-status');
    if (syncStatusEl) {
      if (res.ok) {
        syncStatusEl.textContent = '● Guardado en perfil_jugador.json (listo para Git)';
        syncStatusEl.style.color = '#10b981';
      } else {
        syncStatusEl.textContent = '○ Guardado localmente (Servidor no respondió)';
        syncStatusEl.style.color = '#f59e0b';
      }
    }
  } catch (e) {
    const syncStatusEl = document.getElementById('sync-status');
    if (syncStatusEl) {
      syncStatusEl.textContent = '○ Guardado en navegador (Servidor Python inactivo)';
      syncStatusEl.style.color = '#f59e0b';
    }
  }
}

function populateDashboard() {
  // Update Global Stats
  document.getElementById('stat-games').textContent = userProfile.gamesPlayed || 0;
  document.getElementById('stat-wins').textContent = userProfile.wins || 0;
  document.getElementById('stat-draws').textContent = userProfile.draws || 0;
  document.getElementById('stat-losses').textContent = userProfile.losses || 0;

  // Update Openings Table
  const tbody = document.getElementById('dashboard-openings-body');
  if (tbody) {
    tbody.innerHTML = '';

    const practiceStats = getProgressStats(); // from existing practice mode
    const gameStats = userProfile.openingStats || {};

    // Find all openings the user has interacted with
    const interactedIds = new Set([...Object.keys(practiceStats), ...Object.keys(gameStats)]);
    
    if (interactedIds.size === 0) {
      tbody.innerHTML = `<tr><td colspan="3" style="text-align:center; padding: 1rem; color: var(--text-muted);">Aún no tienes registros. ¡Completa una práctica o juega una partida!</td></tr>`;
    } else {
      // Sort by total games + practices
      const rowsData = Array.from(interactedIds).map(id => {
        const opening = OPENINGS_DATA.find(o => o.id === id);
        const pStat = practiceStats[id] || { perfectRuns: 0 };
        const gStat = gameStats[id] || { wins: 0, losses: 0, draws: 0 };
        return {
          name: opening ? opening.name : id,
          eco: opening ? opening.eco : '?',
          perfect: pStat.perfectRuns,
          wins: gStat.wins,
          draws: gStat.draws,
          losses: gStat.losses,
          totalActivity: pStat.perfectRuns + gStat.wins + gStat.draws + gStat.losses
        };
      });

      rowsData.sort((a, b) => b.totalActivity - a.totalActivity);

      rowsData.forEach(row => {
        const tr = document.createElement('tr');
        tr.style.borderBottom = '1px solid var(--border-color)';
        tr.innerHTML = `
          <td style="padding: 0.8rem;">
            <div style="font-weight: bold;">${row.name}</div>
            <div style="font-size: 0.75rem; color: var(--text-muted);">${row.eco}</div>
          </td>
          <td style="padding: 0.8rem; text-align: center; font-weight: bold; color: #3b82f6;">
            ${row.perfect > 0 ? row.perfect : '-'}
          </td>
          <td style="padding: 0.8rem; text-align: center;">
            <span style="color: #10b981; font-weight: bold;">${row.wins}</span> /
            <span style="color: #f59e0b;">${row.draws}</span> /
            <span style="color: #ef4444;">${row.losses}</span>
          </td>
        `;
        tbody.appendChild(tr);
      });
    }
  }

  // Update Match History Table
  const historyTbody = document.getElementById('dashboard-history-body');
  if (historyTbody) {
    historyTbody.innerHTML = '';
    const historyList = userProfile.history || [];
    if (historyList.length === 0) {
      historyTbody.innerHTML = `<tr><td colspan="4" style="text-align:center; padding: 1rem; color: var(--text-muted);">Aún no has jugado partidas puntuadas en Modo Libre.</td></tr>`;
    } else {
      historyList.slice(0, 15).forEach(item => {
        const tr = document.createElement('tr');
        tr.style.borderBottom = '1px solid var(--border-color)';
        const dateStr = item.date ? new Date(item.date).toLocaleDateString(undefined, { day: '2-digit', month: '2-digit', hour: '2-digit', minute: '2-digit' }) : '-';
        const color = item.result === 'win' ? '#10b981' : (item.result === 'loss' ? '#ef4444' : '#f59e0b');
        const sign = item.eloChange > 0 ? '+' : '';
        tr.innerHTML = `
          <td style="padding: 0.6rem 0.8rem; font-size: 0.8rem; color: var(--text-muted); white-space: nowrap;">${dateStr}</td>
          <td style="padding: 0.6rem 0.8rem;">
            <div style="font-weight: 600; font-size: 0.85rem;">${item.openingName || 'Partida Libre'}</div>
            <div style="font-size: 0.75rem; color: var(--text-muted);">IA Nivel ${item.aiLevelId || '?'} (${item.aiElo || '?'} ELO)</div>
          </td>
          <td style="padding: 0.6rem 0.8rem; font-weight: bold; color: ${color}; text-align: center;">${item.resultText || item.result}</td>
          <td style="padding: 0.6rem 0.8rem; text-align: right; font-weight: bold; color: ${color}; white-space: nowrap;">
            ${sign}${item.eloChange} <span style="font-size:0.75rem; color:var(--text-muted); font-weight:normal;">(${item.userEloAfter})</span>
          </td>
        `;
        historyTbody.appendChild(tr);
      });
    }
  }
}

function updateProfileUI() {
  if (profileNameDisplay) profileNameDisplay.textContent = userProfile.name;
  if (profileEloDisplay) profileEloDisplay.textContent = userProfile.elo;
}

if (btnProfile) {
  btnProfile.addEventListener('click', () => {
    inputProfileName.value = userProfile.name;
    inputProfileElo.value = userProfile.elo;
    populateDashboard();
    profileModal.classList.add('open');
    profileModal.style.display = 'flex';
  });
}

if (btnCloseProfile) {
  btnCloseProfile.addEventListener('click', () => {
    profileModal.classList.remove('open');
    profileModal.style.display = 'none';
  });
}

if (btnSaveProfile) {
  btnSaveProfile.addEventListener('click', () => {
    userProfile.name = inputProfileName.value || 'Jugador';
    userProfile.elo = parseInt(inputProfileElo.value, 10) || 1200;
    saveProfile();
    profileModal.classList.remove('open');
    profileModal.style.display = 'none';
    if (typeof chessSound !== 'undefined' && chessSound.playSuccess) {
      chessSound.playSuccess();
    }
  });
}
// --- END USER PROFILE SYSTEM ---

const btnGitPush = document.getElementById('btn-git-push');
if (btnGitPush) {
  btnGitPush.addEventListener('click', async () => {
    const originalText = btnGitPush.textContent;
    btnGitPush.textContent = 'Subiendo...';
    btnGitPush.disabled = true;
    
    // Primero guardar localmente
    userProfile.name = inputProfileName.value || 'Jugador';
    userProfile.elo = parseInt(inputProfileElo.value, 10) || 1200;
    await saveProfile();

    try {
      const res = await fetch('/api/git-push', { method: 'POST' });
      const data = await res.json();
      if (res.ok) {
        alert("✅ " + data.message);
      } else {
        alert("❌ Error: " + data.message);
      }
    } catch (e) {
      alert("❌ No se pudo conectar al servidor local para subir a Git. Asegúrate de ejecutar 'python3 server.py' y estar en http://localhost:8080");
    } finally {
      btnGitPush.textContent = originalText;
      btnGitPush.disabled = false;
    }
  });
}


  // Application State
  const state = {
    engine: new ChessEngine(),
    aiClient: typeof ChessAIClient !== 'undefined' ? new ChessAIClient() : null,
    evalClient: typeof ChessAIClient !== 'undefined' ? new ChessAIClient() : null,
    aiLevelId: 3, // 0 = off, 1-6 = AI (default 3: Aficionado)
    aiThinking: false,
    boardUI: null,
    currentOpening: OPENINGS_DATA[0],
    currentMode: 'study', // 'study', 'practice', 'free'
    studyStep: 0, // 0 = start position, 1..N
    practiceStep: 0, // current expected move index in practice mode
    practiceSide: 'w', // 'w' or 'b'
    practiceAttempts: 0,
    practiceMistakes: 0,
    autoPlayInterval: null,
    soundEnabled: true
  };

  // DOM Elements
  const openingSelect = document.getElementById('opening-select');
  const openingNameEl = document.getElementById('opening-name');
  const openingEcoEl = document.getElementById('opening-eco');
  const openingSideEl = document.getElementById('opening-side');
  const openingDiffEl = document.getElementById('opening-diff');
  const openingSummaryEl = document.getElementById('opening-summary');

  // Tabs
  const tabStudy = document.getElementById('tab-study');
  const tabPractice = document.getElementById('tab-practice');
  const tabFree = document.getElementById('tab-free');

  // Study Mode Elements
  const studyPanel = document.getElementById('study-panel');
  const moveTagEl = document.getElementById('move-tag');
  const moveTitleEl = document.getElementById('move-title');
  const moveExplanationEl = document.getElementById('move-explanation');
  const plansWhiteList = document.getElementById('plans-white-list');
  const plansBlackList = document.getElementById('plans-black-list');
  const btnPrev = document.getElementById('btn-prev');
  const btnNext = document.getElementById('btn-next');
  const btnFirst = document.getElementById('btn-first');
  const btnLast = document.getElementById('btn-last');
  const btnAutoplay = document.getElementById('btn-autoplay');
  const chkAutoreply = document.getElementById('chk-autoreply');
  const lblAutoreply = document.getElementById('lbl-autoreply');
  const btnUndo = document.getElementById('btn-undo');
  const btnFreeHint = document.getElementById('btn-free-hint');
  const btnRestart = document.getElementById('btn-restart');
  const movesListEl = document.getElementById('moves-list');

  // Practice Mode Elements
  const practicePanel = document.getElementById('practice-panel');
  const practiceStatusBanner = document.getElementById('practice-status-banner');
  const practiceProgressBar = document.getElementById('practice-progress-bar');
  const practiceProgressText = document.getElementById('practice-progress-text');
  const btnPracticeHint = document.getElementById('btn-practice-hint');
  const btnPracticeShow = document.getElementById('btn-practice-show');
  const btnPracticeRestart = document.getElementById('btn-practice-restart');

  // Header and Toolbar Controls
  const btnFlip = document.getElementById('btn-flip');
  const btnSound = document.getElementById('btn-sound');
  const selectTheme = document.getElementById('select-theme');
  const selectAiLevel = document.getElementById('select-ai-level');
  const trapsContainer = document.getElementById('traps-container');

  // Player labels
  const topPlayerLabel = document.getElementById('top-player-name');
  const bottomPlayerLabel = document.getElementById('bottom-player-name');
  const topPlayerAvatar = document.getElementById('top-player-avatar');
  const bottomPlayerAvatar = document.getElementById('bottom-player-avatar');

  // Initialize Board UI
  state.boardUI = new ChessboardUI('#chessboard-container', {
    orientation: state.currentOpening.side || 'w',
    engine: state.engine,
    onMove: handleUserBoardMove
  });

  // Progress/Stats Logic
  function getProgressStats() {
    try {
      const stats = localStorage.getItem('chess_openings_stats');
      return stats ? JSON.parse(stats) : {};
    } catch (e) {
      return {};
    }
  }

  function saveProgress(openingId, mistakes) {
    const stats = getProgressStats();
    if (!stats[openingId]) {
      stats[openingId] = { completions: 0, perfectRuns: 0, bestMistakes: mistakes };
    }
    stats[openingId].completions += 1;
    if (mistakes === 0) stats[openingId].perfectRuns += 1;
    if (mistakes < stats[openingId].bestMistakes) stats[openingId].bestMistakes = mistakes;
    
    try {
      localStorage.setItem('chess_openings_stats', JSON.stringify(stats));
    } catch (e) {
      console.error("No se pudo guardar el progreso", e);
    }

    // Sincronizar estadísticas en perfil_jugador.json
    saveProfile();
  }

  function renderOpeningStatsUI() {
    const stats = getProgressStats();
    const stat = stats[state.currentOpening.id];
    let statsHtml = '';
    if (stat && stat.completions > 0) {
      statsHtml = `<div style="margin-top: 0.5rem; font-size: 0.85rem; color: #10b981; font-weight: bold;">
        ✅ Completada ${stat.completions} vez/veces (Perfectas: ${stat.perfectRuns})
      </div>`;
    }
    
    // We can append this to the summary
    const existingStats = openingSummaryEl.parentNode.querySelector('.opening-stats-ui');
    if (existingStats) existingStats.remove();
    
    if (statsHtml) {
      const statsContainer = document.createElement('div');
      statsContainer.className = 'opening-stats-ui';
      statsContainer.innerHTML = statsHtml;
      openingSummaryEl.parentNode.insertBefore(statsContainer, openingSummaryEl.nextSibling);
    }
  }

  // Populate Openings Select
  function populateOpenings() {
    const currentVal = openingSelect.value;
    openingSelect.innerHTML = '';
    
    // We will keep the native select hidden to trigger its change events, 
    // but build an accessible DOM list that supports keyboard navigation.
    let customContainer = document.getElementById('a11y-opening-container');
    if (!customContainer) {
        customContainer = document.createElement('div');
        customContainer.id = 'a11y-opening-container';
        customContainer.className = 'a11y-select-container';
        
        const display = document.createElement('div');
        display.id = 'a11y-opening-display';
        display.className = 'a11y-select-display';
        display.tabIndex = 0; // Keyboard focusable
        display.innerHTML = `<span id="a11y-opening-text">Seleccionar Apertura...</span>
                             <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>`;
        
        const dropdown = document.createElement('div');
        dropdown.id = 'a11y-opening-dropdown';
        dropdown.className = 'a11y-select-dropdown';
        
        customContainer.appendChild(display);
        customContainer.appendChild(dropdown);
        openingSelect.parentNode.insertBefore(customContainer, openingSelect);
        openingSelect.style.display = 'none';

        // Critical styles inline (independent of a cached styles.css)
        customContainer.style.position = 'relative';
        customContainer.style.width = '100%';
        Object.assign(dropdown.style, {
            position: 'absolute', top: 'calc(100% + 4px)', left: '0', width: '100%',
            overflowY: 'scroll', zIndex: '1000', boxSizing: 'border-box',
            scrollbarWidth: 'thin', scrollbarColor: '#64748b #131b2e'
        });
        
        // Fit the dropdown so it never goes below the base of the board
        // (nor below the visible window); the list scrolls internally.
        const fitDropdown = () => {
            if (!dropdown.classList.contains('open')) return;
            const top = display.getBoundingClientRect().bottom + 4;
            let limit = window.innerHeight - 8;
            const boardEl = document.getElementById('chessboard-container');
            if (boardEl) {
                const boardBottom = boardEl.getBoundingClientRect().bottom;
                if (boardBottom > top + 120) limit = Math.min(limit, boardBottom);
            }
            dropdown.style.maxHeight = Math.max(120, limit - top) + 'px';
        };
        window.addEventListener('resize', fitDropdown);
        window.addEventListener('scroll', fitDropdown, true);

        // Interaction Logic
        display.addEventListener('click', (e) => {
            e.stopPropagation();
            const isOpen = dropdown.classList.toggle('open');
            if (isOpen) {
                fitDropdown();
                dropdown.querySelector('.a11y-select-option')?.focus({ preventScroll: true });
                const sel = dropdown.querySelector('.a11y-select-option.selected');
                if (sel) sel.scrollIntoView({ block: 'nearest' });
            }
        });
        
        display.addEventListener('keydown', (e) => {
            if (e.key === ' ' || e.key === 'Enter') {
                e.preventDefault();
                display.click();
            } else if (e.key === 'ArrowDown') {
                e.preventDefault();
                if (!dropdown.classList.contains('open')) display.click();
                else dropdown.querySelector('.a11y-select-option')?.focus();
            }
        });
        
        dropdown.addEventListener('keydown', (e) => {
            if (!dropdown.classList.contains('open')) return;
            const options = Array.from(dropdown.querySelectorAll('.a11y-select-option'));
            const index = options.indexOf(document.activeElement);
            
            if (e.key === 'ArrowDown') {
                e.preventDefault();
                if (index < options.length - 1) options[index + 1].focus();
            } else if (e.key === 'ArrowUp') {
                e.preventDefault();
                if (index > 0) options[index - 1].focus();
                else display.focus();
            } else if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                document.activeElement.click();
            } else if (e.key === 'Escape') {
                dropdown.classList.remove('open');
                display.focus();
            }
        });
        
        // Close on outside click or board click
        document.addEventListener('mousedown', (e) => {
            if (!customContainer.contains(e.target)) {
                dropdown.classList.remove('open');
            }
        }, true);
    }
    
    const dropdown = document.getElementById('a11y-opening-dropdown');
    dropdown.innerHTML = '';
    const displaySpan = document.getElementById('a11y-opening-text');
    
    const categories = {};
    const stats = getProgressStats();

    OPENINGS_DATA.forEach(op => {
      if (!categories[op.category]) categories[op.category] = [];
      categories[op.category].push(op);
    });

    for (const [catName, ops] of Object.entries(categories)) {
      const optgroup = document.createElement('optgroup');
      optgroup.label = catName;
      
      const groupTitle = document.createElement('div');
      groupTitle.className = 'a11y-select-optgroup';
      groupTitle.textContent = catName;
      dropdown.appendChild(groupTitle);

      ops.forEach(op => {
        const isCompleted = stats[op.id] && stats[op.id].completions > 0;
        const mark = isCompleted ? "✅ " : "";
        const textContent = `${mark}${op.eco} - ${op.name}`;
        
        // Native
        const opt = document.createElement('option');
        opt.value = op.id;
        opt.textContent = textContent;
        optgroup.appendChild(opt);
        
        // Custom
        const divOpt = document.createElement('div');
        divOpt.className = 'a11y-select-option' + (currentVal === op.id ? ' selected' : '');
        divOpt.textContent = textContent;
        divOpt.tabIndex = -1;
        
        if (currentVal === op.id) {
            displaySpan.textContent = textContent;
        }
        
        divOpt.addEventListener('click', (e) => {
            openingSelect.value = op.id;
            displaySpan.textContent = textContent;
            dropdown.classList.remove('open');
            
            dropdown.querySelectorAll('.a11y-select-option').forEach(el => el.classList.remove('selected'));
            divOpt.classList.add('selected');
            
            const event = new Event('change');
            openingSelect.dispatchEvent(event);
            document.getElementById('a11y-opening-display').focus();
        });
        
        dropdown.appendChild(divOpt);
      });
      openingSelect.appendChild(optgroup);
    }
    
    if (currentVal) {
      openingSelect.value = currentVal;
    } else if (OPENINGS_DATA.length > 0) {
      displaySpan.textContent = `${OPENINGS_DATA[0].eco} - ${OPENINGS_DATA[0].name}`;
    }
  }

  function loadOpening(openingId) {
    const found = OPENINGS_DATA.find(o => o.id === openingId);
    if (!found) return;

    state.currentOpening = found;
    state.practiceSide = found.side;

    // Stop autoplay if running
    stopAutoplay();

    // Update Header Meta
    if (openingNameEl) openingNameEl.textContent = found.name;
    openingEcoEl.textContent = found.eco;
    openingDiffEl.textContent = found.difficulty;
    openingSummaryEl.textContent = found.summary;

    openingSideEl.textContent = found.side === 'w' ? 'Blancas' : 'Negras';
    openingSideEl.className = `badge ${found.side === 'w' ? 'badge-side-w' : 'badge-side-b'}`;

    // Render Stats
    renderOpeningStatsUI();

    // Update Plans
    plansWhiteList.innerHTML = found.plansWhite.map(p => `<li>${p}</li>`).join('');
    plansBlackList.innerHTML = found.plansBlack.map(p => `<li>${p}</li>`).join('');

    // Update Traps
    if (found.traps && found.traps.length > 0) {
      trapsContainer.style.display = 'block';
      trapsContainer.innerHTML = `
        <div class="traps-header">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/>
            <line x1="12" y1="9" x2="12" y2="13"/>
            <line x1="12" y1="17" x2="12.01" y2="17"/>
          </svg>
          Trampas y Errores Típicos
        </div>
        ${found.traps.map(t => `
          <div class="trap-item">
            <strong>${t.title}</strong>
            <p>${t.desc}</p>
            ${t.moves ? `<p style="margin-top:0.3rem;font-family:monospace;font-size:0.75rem;opacity:0.85">${t.moves}</p>` : ''}
          </div>
        `).join('')}
      `;
    } else {
      trapsContainer.style.display = 'none';
    }

    // Set board orientation to opening side
    state.boardUI.setOrientation(found.side);
    updatePlayerLabels();

    // Render Moves List
    renderMovesList();

    // Reset mode
    if (typeof gameProcessed !== 'undefined') gameProcessed = false;
    if (state.currentMode === 'practice') {
      startPracticeMode();
    } else {
      setStudyStep(0);
      triggerStudyAutoReply();
    }
  }

  // Render Move List
  function renderMovesList() {
    movesListEl.innerHTML = '';
    const moves = state.currentOpening.moves;

    for (let i = 0; i < moves.length; i++) {
      const m = moves[i];
      const moveItem = document.createElement('div');
      moveItem.className = 'move-item';
      moveItem.dataset.step = i + 1;

      const isWhiteMove = i % 2 === 0;
      const moveNumber = Math.floor(i / 2) + 1;

      if (isWhiteMove) {
        moveItem.innerHTML = `<span class="move-number">${moveNumber}.</span> ${m.san}`;
      } else {
        moveItem.innerHTML = `<span class="move-number">${moveNumber}...</span> ${m.san}`;
      }

      moveItem.addEventListener('click', () => {
        if (state.currentMode === 'study') {
          setStudyStep(i + 1);
        }
      });

      movesListEl.appendChild(moveItem);
    }
  }

  // Update Player Strip Labels based on orientation
  function updatePlayerLabels() {
    const isWhiteBottom = state.boardUI.orientation === 'w';
    if (isWhiteBottom) {
      topPlayerLabel.textContent = 'Negras (Oponente)';
      topPlayerAvatar.className = 'player-avatar black';
      topPlayerAvatar.textContent = '♚';

      bottomPlayerLabel.textContent = 'Blancas (Tú)';
      bottomPlayerAvatar.className = 'player-avatar white';
      bottomPlayerAvatar.textContent = '♔';
    } else {
      topPlayerLabel.textContent = 'Blancas (Oponente)';
      topPlayerAvatar.className = 'player-avatar white';
      topPlayerAvatar.textContent = '♔';

      bottomPlayerLabel.textContent = 'Negras (Tú)';
      bottomPlayerAvatar.className = 'player-avatar black';
      bottomPlayerAvatar.textContent = '♚';
    }
  }

  // Study Mode: Go to specific step
  
  let autoReplyTimeout = null;
  function triggerStudyAutoReply() {
    if (state.currentMode !== 'study' || !chkAutoreply || !chkAutoreply.checked) return;
    if (state.autoPlayInterval) return;
    if (state.studyStep >= state.currentOpening.moves.length) return;

    const isWhiteTurn = state.studyStep % 2 === 0;
    const userIsWhite = state.boardUI.orientation === 'w';

    if (autoReplyTimeout) clearTimeout(autoReplyTimeout);

    // If it is the machine's turn
    if ((isWhiteTurn && !userIsWhite) || (!isWhiteTurn && userIsWhite)) {
      autoReplyTimeout = setTimeout(() => {
        if (state.currentMode === 'study' && chkAutoreply.checked && state.studyStep < state.currentOpening.moves.length) {
          // Check turn again in case user manually advanced during timeout
          const isWT = state.studyStep % 2 === 0;
          if ((isWT && !userIsWhite) || (!isWT && userIsWhite)) {
            setStudyStep(state.studyStep + 1);
            if (typeof chessSound !== 'undefined' && chessSound.playMove) chessSound.playMove();
          }
        }
      }, 600);
    }
  }

  if (chkAutoreply) {
    chkAutoreply.addEventListener('change', triggerStudyAutoReply);
  }

  function setStudyStep(stepIndex) {
    state.studyStep = Math.max(0, Math.min(stepIndex, state.currentOpening.moves.length));

    // Reset engine and play moves up to step
    state.engine.reset();
    let lastMoveRecord = null;

    for (let i = 0; i < state.studyStep; i++) {
      const m = state.currentOpening.moves[i];
      lastMoveRecord = state.engine.makeMove({ from: m.from, to: m.to });
    }

    state.boardUI.setLastMove(lastMoveRecord);

    // Update explanations
    if (state.studyStep === 0) {
      moveTagEl.textContent = 'Posición Inicial';
      moveTitleEl.textContent = state.currentOpening.name;
      moveExplanationEl.textContent = state.currentOpening.summary;
      
      state.boardUI.setCustomHighlights(state.currentOpening.keySquares || []);
    } else {
      const currentMove = state.currentOpening.moves[state.studyStep - 1];
      const isWhite = (state.studyStep - 1) % 2 === 0;
      const moveNum = Math.floor((state.studyStep - 1) / 2) + 1;
      const notationStr = isWhite ? `${moveNum}. ${currentMove.san}` : `${moveNum}... ${currentMove.san}`;

      moveTagEl.textContent = notationStr;
      moveTitleEl.textContent = currentMove.name || '';
      moveExplanationEl.textContent = currentMove.comment || '';

      // Arrows and highlights
      state.boardUI.setArrows(currentMove.arrows || []);
      state.boardUI.setCustomHighlights(currentMove.highlightSquares || []);
    }

    // Update active move in moves list
    const allMoveItems = movesListEl.querySelectorAll('.move-item');
    allMoveItems.forEach((el, idx) => {
      if (idx + 1 === state.studyStep) {
        el.classList.add('active');
        // Solo hacer scrollIntoView si estamos en escritorio, en móvil causa saltos molestos
        if (window.innerWidth > 768) {
          el.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        } else {
          // Scroll manual suave del contenedor para no afectar la ventana
          if (movesListEl) movesListEl.scrollTop = el.offsetTop - 50;
        }
      } else {
        el.classList.remove('active');
      }
    });

    state.boardUI.render();
    triggerStudyAutoReply();
  }

  // Autoplay functionality
  function toggleAutoplay() {
    if (state.autoPlayInterval) {
      stopAutoplay();
    } else {
      startAutoplay();
    }
  }

  function startAutoplay() {
    btnAutoplay.innerHTML = `
      <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
        <rect x="6" y="4" width="4" height="16"/>
        <rect x="14" y="4" width="4" height="16"/>
      </svg>
      Pausar
    `;
    btnAutoplay.classList.add('btn-primary');

    state.autoPlayInterval = setInterval(() => {
      if (state.studyStep < state.currentOpening.moves.length) {
        setStudyStep(state.studyStep + 1);
        chessSound.playMove();
      } else {
        stopAutoplay();
      }
    }, 1800);
  }

  function stopAutoplay() {
    if (state.autoPlayInterval) {
      clearInterval(state.autoPlayInterval);
      state.autoPlayInterval = null;
    }
    btnAutoplay.innerHTML = `
      <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
        <polygon points="5 3 19 12 5 21 5 3"/>
      </svg>
      Auto
    `;
    btnAutoplay.classList.remove('btn-primary');
  }

  // Practice Mode Initialization
  function startPracticeMode() {
    stopAutoplay();
    state.practiceStep = 0;
    state.practiceMistakes = 0;
    state.engine.reset();
    
    state.boardUI.clearHighlights();
    state.boardUI.setLastMove(null);

    // If practicing as black, the opponent (white) makes the first move automatically
    if (state.practiceSide === 'b') {
      const firstWhiteMove = state.currentOpening.moves[0];
      state.engine.makeMove({ from: firstWhiteMove.from, to: firstWhiteMove.to });
      state.boardUI.setLastMove(firstWhiteMove);
      state.practiceStep = 1;
    }

    updatePracticeUI();
    state.boardUI.render();
  }

  function updatePracticeUI() {
    const totalUserMoves = state.currentOpening.moves.filter((_, i) =>
      state.practiceSide === 'w' ? i % 2 === 0 : i % 2 === 1
    ).length;

    const completedUserMoves = Math.floor(
      (state.practiceStep + (state.practiceSide === 'b' ? 0 : 1)) / 2
    );

    const percent = Math.min(100, Math.round((completedUserMoves / totalUserMoves) * 100));
    practiceProgressBar.style.width = `${percent}%`;
    practiceProgressText.textContent = `${completedUserMoves} de ${totalUserMoves} jugadas (${percent}%)`;

    // Check if training finished
    if (state.practiceStep >= state.currentOpening.moves.length) {
      saveProgress(state.currentOpening.id, state.practiceMistakes);
      loadProfile();
  populateOpenings();
      renderOpeningStatsUI();
      practiceStatusBanner.className = 'practice-status-banner completed';
      practiceStatusBanner.innerHTML = `
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/>
        </svg>
        <span>¡Completado! Has practicado con éxito toda la línea principal de ${state.currentOpening.name}.</span>
      `;
      chessSound.playSuccess();
      return;
    }

    // Prompt user
    const currentExpected = state.currentOpening.moves[state.practiceStep];
    const isWhiteTurn = state.practiceStep % 2 === 0;
    const moveNumber = Math.floor(state.practiceStep / 2) + 1;
    const turnName = isWhiteTurn ? `Jugada ${moveNumber} de Blancas` : `Jugada ${moveNumber}... de Negras`;

    practiceStatusBanner.className = 'practice-status-banner turn-prompt';
    practiceStatusBanner.innerHTML = `
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 14 14"/>
      </svg>
      <span>Tu turno (${turnName}). Encuentra la mejor jugada teórica.</span>
    `;
  }

  // Handle Board Move Event (Called when user drops/clicks a move on board)
  function handleUserBoardMove(moveData) {
    state.boardUI.clearArrows();
    if (state.aiThinking) return false;
    
    if (state.currentMode === 'free') {
      // In free mode, all legal moves are allowed
      // The engine applies the move AFTER this callback returns true.
      // So we must check for game over slightly after.
      setTimeout(() => {
        checkGameOver();
        if (!state.engine.isGameOver()) {
          checkAIMove();
        }
      }, 50);
      return true;
    }

    if (state.currentMode === 'study') {
      // If user is at the end of the line
      if (state.studyStep >= state.currentOpening.moves.length) {
        moveExplanationEl.innerHTML = `
          <div style="background:rgba(56,189,248,0.15);padding:0.75rem;border-radius:8px;border:1px solid rgba(56,189,248,0.3);margin-top:0.5rem;">
            <strong>¡Línea teórica de estudio completada!</strong> Has llegado al final de la línea registrada para esta apertura.
            Puedes usar la pestaña <strong>'Tablero Libre'</strong> para seguir probando jugadas libremente, o <strong>'Práctica Activa'</strong> para entrenar.
          </div>
        `;
        return false;
      }

      // In study mode, clicking moves can auto-advance if it matches the next step!
      const nextExpected = state.currentOpening.moves[state.studyStep];
      const isNext = nextExpected && moveData.from === nextExpected.from && moveData.to === nextExpected.to;
      const isNextAlt = nextExpected && nextExpected.acceptedAlternatives
        ? nextExpected.acceptedAlternatives.some(a => a.from === moveData.from && a.to === moveData.to)
        : false;

      if (isNext || isNextAlt) {
        setStudyStep(state.studyStep + 1);
        
        triggerStudyAutoReply();
        
        return false; // already applied by setStudyStep
      }

      // Legal chess move, but not the expected theoretical study step
      if (nextExpected) {
        chessSound.playError();
        const inCheck = state.engine.isInCheck();
        let checkPrefix = inCheck ? "¡Estás en jaque! " : "";
        moveExplanationEl.innerHTML = `
          <div style="background:rgba(239,68,68,0.15);padding:0.6rem;border-radius:8px;border:1px solid rgba(239,68,68,0.3);margin-top:0.4rem;font-size:0.85rem;">
            ⚠️ ${checkPrefix}Esa jugada se desvía de la línea teórica de estudio. La jugada recomendada es <strong>${nextExpected.san}</strong> (${nextExpected.from} ➔ ${nextExpected.to}).
          </div>
          <p style="margin-top:0.4rem;">${state.currentOpening.moves[state.studyStep - 1]?.comment || ''}</p>
        `;
      }
      return false;
    }

    if (state.currentMode === 'practice') {
      // If practice is already completed: allow free moves!
      if (state.practiceStep >= state.currentOpening.moves.length) {
        practiceStatusBanner.className = 'practice-status-banner completed';
        practiceStatusBanner.innerHTML = `
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <polyline points="20 6 9 17 4 12"/>
          </svg>
          <span>¡Apertura completada! Estás en modo de juego libre explorando la posición.</span>
        `;
        setTimeout(checkAIMove, 200);
        return true; // allow engine to execute move
      }

      const expectedMove = state.currentOpening.moves[state.practiceStep];
      if (!expectedMove) return true;

      // Check if move matches main line or accepted alternative
      const isMainMove = moveData.from === expectedMove.from && moveData.to === expectedMove.to;
      const matchedAlt = expectedMove.acceptedAlternatives
        ? expectedMove.acceptedAlternatives.find(alt => alt.from === moveData.from && alt.to === moveData.to)
        : null;

      if (isMainMove || matchedAlt) {
        // Correct move!
        const playedInfo = matchedAlt || expectedMove;
        state.practiceStep++;

        practiceStatusBanner.className = 'practice-status-banner correct';
        practiceStatusBanner.innerHTML = `
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <polyline points="20 6 9 17 4 12"/>
          </svg>
          <span><strong>¡Excelente! ${playedInfo.san}:</strong> ${playedInfo.comment}</span>
        `;

        // Opponent auto-reply if not finished
        if (state.practiceStep < state.currentOpening.moves.length && !matchedAlt) {
          setTimeout(() => {
            const oppMove = state.currentOpening.moves[state.practiceStep];
            if (oppMove) {
              state.engine.makeMove({ from: oppMove.from, to: oppMove.to });
              state.boardUI.setLastMove(oppMove);
              chessSound.playMove();
              state.practiceStep++;
              state.boardUI.render();
              updatePracticeUI();
              
              if (state.practiceStep >= state.currentOpening.moves.length) {
                 setTimeout(checkAIMove, 200);
              }
            }
          }, 450);
        } else if (matchedAlt) {
          state.practiceStep = state.currentOpening.moves.length; // Force end of practice
          updatePracticeUI();
          practiceStatusBanner.className = 'practice-status-banner correct';
          practiceStatusBanner.innerHTML = `
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="20 6 9 17 4 12"/>
            </svg>
            <span><strong>¡Excelente alternativa! ${matchedAlt.san}:</strong> ${matchedAlt.comment || ''}</span>
            <div style="margin-top:0.4rem;font-size:0.8rem;opacity:0.9;">
              Has elegido una variante teórica muy válida. La práctica de esta línea concluye aquí y el motor IA tomará el control.
            </div>
          `;
          setTimeout(checkAIMove, 200);
        } else {
          updatePracticeUI();
          if (state.practiceStep >= state.currentOpening.moves.length) {
             setTimeout(checkAIMove, 200);
          }
        }

        return true; // allow engine to make move
      } else {
        // Wrong move in practice mode
        state.practiceMistakes++;
        chessSound.playError();

        const inCheck = state.engine.isInCheck();
        let checkMsg = inCheck ? "¡Tu Rey está en jaque! Debes cubrir o resolver el jaque con una jugada teórica. " : "";

        practiceStatusBanner.className = 'practice-status-banner incorrect';
        practiceStatusBanner.innerHTML = `
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/>
          </svg>
          <span>${checkMsg}Esa no es la jugada teórica de esta apertura. ¡Inténtalo de nuevo o pide una pista!</span>
        `;
        return false; // reject illegal/non-theoretical move
      }
    }

    return true;
  }

  // Practice Hint Handler
  btnPracticeHint.addEventListener('click', () => {
    if (state.practiceStep >= state.currentOpening.moves.length) return;
    const expected = state.currentOpening.moves[state.practiceStep];
    if (!expected) return;

    // Show hint: highlight source square and give idea
    const highlightSq = [expected.from];
    if (expected.acceptedAlternatives) {
      expected.acceptedAlternatives.forEach(a => highlightSq.push(a.from));
    }
    state.boardUI.setCustomHighlights(highlightSq);

    let altMsg = '';
    if (expected.acceptedAlternatives && expected.acceptedAlternatives.length > 0) {
      const altNames = expected.acceptedAlternatives.map(a => a.san).join(' o ');
      altMsg = ` (También es válida ${altNames})`;
    }

    practiceStatusBanner.className = 'practice-status-banner turn-prompt';
    practiceStatusBanner.innerHTML = `
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/>
      </svg>
      <span><strong>Pista:</strong> Mueve la pieza en <strong>${expected.from.toUpperCase()}</strong>${altMsg}. Idea: ${expected.comment.substring(0, 85)}...</span>
    `;
  });

  // Practice Show Solution Handler
  btnPracticeShow.addEventListener('click', () => {
    if (state.practiceStep >= state.currentOpening.moves.length) return;
    const expected = state.currentOpening.moves[state.practiceStep];
    if (!expected) return;

    // Draw tactical arrow directly
    const arrows = [{ from: expected.from, to: expected.to, color: '#f59e0b' }];
    const highlights = [expected.from, expected.to];

    let altNote = '';
    if (expected.acceptedAlternatives && expected.acceptedAlternatives.length > 0) {
      expected.acceptedAlternatives.forEach(a => {
        arrows.push({ from: a.from, to: a.to, color: '#38bdf8' });
        highlights.push(a.from, a.to);
      });
      const altsText = expected.acceptedAlternatives.map(a => `${a.san} (${a.from}➔${a.to})`).join(', ');
      altNote = `<br><span style="font-size:0.8rem;opacity:0.9;">Variantes alternativas aceptadas: <strong>${altsText}</strong></span>`;
    }

    state.boardUI.setArrows(arrows);
    state.boardUI.setCustomHighlights(highlights);

    practiceStatusBanner.className = 'practice-status-banner turn-prompt';
    practiceStatusBanner.innerHTML = `
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/>
      </svg>
      <span><strong>Solución:</strong> La jugada teórica principal es <strong>${expected.san}</strong> (${expected.from} ➔ ${expected.to}).${altNote}</span>
    `;
  });

  // Practice Restart Handler
  btnPracticeRestart.addEventListener('click', () => {
    startPracticeMode();
  });

  // Navigation Button Handlers (Study Mode)
  btnFirst.addEventListener('click', () => {
    stopAutoplay();
    setStudyStep(0);
      triggerStudyAutoReply();
  });

  btnPrev.addEventListener('click', () => {
    stopAutoplay();
    if (state.studyStep > 0) {
      setStudyStep(state.studyStep - 1);
    }
  });

  btnNext.addEventListener('click', () => {
    stopAutoplay();
    if (state.studyStep < state.currentOpening.moves.length) {
      setStudyStep(state.studyStep + 1);
    }
  });

  btnLast.addEventListener('click', () => {
    stopAutoplay();
    setStudyStep(state.currentOpening.moves.length);
  });


  // Free Mode Hint Handler
  if (btnFreeHint) {
    btnFreeHint.addEventListener('click', () => {
      if (state.currentMode !== 'free' || state.aiThinking || !state.evalClient) return;
      
      const originalHtml = btnFreeHint.innerHTML;
      btnFreeHint.innerHTML = 'Pensando...';
      state.aiThinking = true;
      
      const fen = state.engine.getFen();
      state.evalClient.think({ fen, depth: 6, timeMs: 500 }).then(res => {
          state.aiThinking = false;
          btnFreeHint.innerHTML = originalHtml;
          
          if (res.bestmove) {
            const from = res.bestmove.substring(0, 2);
            const to = res.bestmove.substring(2, 4);
            const promotion = res.bestmove.length > 4 ? res.bestmove[4] : undefined;
            
            state.boardUI.setCustomHighlights([from, to]);
            state.boardUI.setArrows([{from, to, color: 'blue'}]);
            
            const isCapture = state.engine.getPiece(to) !== null;
            state.engine.makeMove({from, to, promotion});
            const isCheck = state.engine.isInCheck();
            const isCheckmate = state.engine.isCheckmate();
            state.engine.undoMove();
            
            let objective = "Desarrolla o mejora la posición de la pieza.";
            if (isCheckmate) {
                objective = "¡Da Jaque Mate!";
            } else if (isCheck) {
                objective = "Ataca al rey enemigo (Jaque).";
            } else if (isCapture) {
                objective = "Captura material enemigo.";
            } else if (['e4','d4','e5','d5'].includes(to)) {
                objective = "Lucha por el control del centro.";
            } else if (res.score && res.score > 200) {
                objective = "Aprovecha una ventaja táctica o material.";
            }
            
            let evalStr = res.score !== undefined ? (res.score / 100).toFixed(2) : "?";
            if (res.score && res.score > 20000) evalStr = "Mate a favor";
            if (res.score && res.score < -20000) evalStr = "Mate en contra";
            
            moveExplanationEl.textContent = `Sugerencia IA: Mover de ${from} a ${to}. Objetivo: ${objective} (Evaluación: ${evalStr})`;
          }
      }).catch(err => {
          state.aiThinking = false;
          btnFreeHint.innerHTML = originalHtml;
          console.error(err);
      });
    });
  }

  btnUndo.addEventListener('click', () => {
    if (state.currentMode !== 'free' || state.aiThinking) return;
    
    let undone = state.engine.undoMove();
    if (undone && state.aiLevelId > 0 && state.aiClient) {
      const isWhiteTurn = state.engine.turn === 'w';
      const userSide = state.boardUI.orientation;
      const isAITurnNow = (isWhiteTurn && userSide === 'b') || (!isWhiteTurn && userSide === 'w');
      
      if (isAITurnNow && state.engine.history.length > 0) {
        // Deshacer también el movimiento del jugador para no dejar a la IA jugando sola
        undone = state.engine.undoMove();
      }
    }
    
    if (undone) {
      const last = state.engine.history[state.engine.history.length - 1];
      state.boardUI.setLastMove(last || null);
      state.boardUI.clearSelection();
      state.boardUI.render();
    }
    updateEvalBar();
  });

  btnRestart.addEventListener('click', () => {
    stopAutoplay();
    if (state.currentMode === 'study') {
      setStudyStep(0);
      triggerStudyAutoReply();
    } else if (state.currentMode === 'practice') {
      startPracticeMode();
    } else if (state.currentMode === 'free') {
      // Reiniciar desde el inicio de la variante
      state.engine.reset();
      if (typeof gameProcessed !== 'undefined') gameProcessed = false;
      
      state.boardUI.clearHighlights();
      state.boardUI.setLastMove(null);
      state.boardUI.render();
      checkAIMove();
    }
      updateEvalBar();
  });

  btnAutoplay.addEventListener('click', () => {
    toggleAutoplay();
  });

  // Keyboard navigation
  window.addEventListener('keydown', (e) => {
    if (state.currentMode !== 'study') return;
    if (e.key === 'ArrowRight') {
      stopAutoplay();
      if (state.studyStep < state.currentOpening.moves.length) {
        setStudyStep(state.studyStep + 1);
      }
    } else if (e.key === 'ArrowLeft') {
      stopAutoplay();
      if (state.studyStep > 0) {
        setStudyStep(state.studyStep - 1);
      }
    } else if (e.key === 'Home') {
      stopAutoplay();
      setStudyStep(0);
      triggerStudyAutoReply();
    } else if (e.key === 'End') {
      stopAutoplay();
      setStudyStep(state.currentOpening.moves.length);
    }
  });

  // Tab switching
  tabStudy.addEventListener('click', () => {
    state.currentMode = 'study';
    tabStudy.classList.add('active');
    tabPractice.classList.remove('active');
    tabFree.classList.remove('active');
    studyPanel.style.display = 'flex';
    practicePanel.style.display = 'none';
    document.getElementById('nav-group').style.display = 'flex';
    btnUndo.style.display = 'none';
    if (btnFreeHint) btnFreeHint.style.display = 'none';
    btnAutoplay.style.display = 'flex';
    if (lblAutoreply) lblAutoreply.style.display = 'flex';
    setStudyStep(state.studyStep);
  });

  tabPractice.addEventListener('click', () => {
    state.currentMode = 'practice';
    tabPractice.classList.add('active');
    tabStudy.classList.remove('active');
    tabFree.classList.remove('active');
    studyPanel.style.display = 'none';
    practicePanel.style.display = 'flex';
    document.getElementById('nav-group').style.display = 'none';
    btnUndo.style.display = 'none';
    if (btnFreeHint) btnFreeHint.style.display = 'none';
    btnAutoplay.style.display = 'none';
    if (lblAutoreply) lblAutoreply.style.display = 'none';
    startPracticeMode();
  });

  tabFree.addEventListener('click', () => {
    state.currentMode = 'free';
    tabFree.classList.add('active');
    tabStudy.classList.remove('active');
    tabPractice.classList.remove('active');
    studyPanel.style.display = 'flex';
    practicePanel.style.display = 'none';
    moveTagEl.textContent = 'Tablero Libre';
    moveTitleEl.textContent = 'Modo Análisis / Experimentación';
    moveExplanationEl.textContent = 'Mueve libremente cualquier pieza para probar variantes o ideas personales.';
    document.getElementById('nav-group').style.display = 'none';
    btnUndo.style.display = 'flex';
    if (btnFreeHint) btnFreeHint.style.display = 'flex';
    btnAutoplay.style.display = 'none';
    if (lblAutoreply) lblAutoreply.style.display = 'none';
    
    state.boardUI.clearHighlights();
    checkAIMove();
  });

  // Flip board handler
  btnFlip.addEventListener('click', () => {
    state.boardUI.flip();
    updatePlayerLabels();
    updateEvalBar();
    checkAIMove();
  });

  // Theme change handler
  selectTheme.addEventListener('change', (e) => {
    state.boardUI.setTheme(e.target.value);
  });

  // Sound toggle handler
  btnSound.addEventListener('click', () => {
    state.soundEnabled = chessSound.toggleSound();
    btnSound.innerHTML = state.soundEnabled ? `
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>
        <path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/>
      </svg>
    ` : `
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>
        <line x1="23" y1="9" x2="17" y2="15"/>
        <line x1="17" y1="9" x2="23" y2="15"/>
      </svg>
    `;
    btnSound.title = state.soundEnabled ? 'Silenciar sonido' : 'Activar sonido';
  });

  // Opening selector change handler
  openingSelect.addEventListener('change', (e) => {
    loadOpening(e.target.value);
  });

  // AI move handler
  function checkAIMove() {
    if (state.aiLevelId === 0 || !state.aiClient || state.aiThinking) return;
    if (state.engine.isGameOver()) return;

    // Determine whose turn it is
    const isWhiteTurn = state.engine.turn === 'w';
    // AI should play if it's AI's turn based on orientation
    const userSide = state.boardUI.orientation; // 'w' or 'b'
    if ((isWhiteTurn && userSide === 'w') || (!isWhiteTurn && userSide === 'b')) {
      return; // It's user's turn
    }

    // Only play if in Free mode, OR in Practice mode AFTER completion
    if (state.currentMode === 'study') return;
    if (state.currentMode === 'practice' && state.practiceStep < state.currentOpening.moves.length) return;

    const level = AI_LEVELS.find(l => l.id === state.aiLevelId);
    if (!level) return;

    state.aiThinking = true;
    practiceStatusBanner.className = 'practice-status-banner turn-prompt';
    practiceStatusBanner.innerHTML = `
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 14 14"/>
      </svg>
      <span>El motor IA (${level.name}) está pensando...</span>
    `;

    const fen = state.engine.getFen();
    state.aiClient.think({ fen, depth: level.depth, timeMs: level.timeMs, noise: level.noise })
      .then(res => {
        state.aiThinking = false;
        if (res.bestmove) {
          const from = res.bestmove.substring(0, 2);
          const to = res.bestmove.substring(2, 4);
          const promotion = res.bestmove.length > 4 ? res.bestmove[4] : undefined;
          
          const moveData = { from, to, promotion };
          state.boardUI.clearArrows();
          const result = state.engine.makeMove(moveData);
          if (result) {
            state.boardUI.setLastMove(result);
            chessSound.playMove();
            state.boardUI.render();
            updateEvalBar();
            checkGameOver();
          }
        }
      })
      .catch(err => {
        state.aiThinking = false;
        console.warn("AI error/cancelled:", err);
      });
  }

  function checkGameOver() {
    if (state.engine.isGameOver()) {
      let msg = "¡Juego terminado! ";
      if (state.engine.isCheckmate()) msg += "Jaque Mate.";
      else msg += "Tablas.";
      
      practiceStatusBanner.className = 'practice-status-banner completed';
      practiceStatusBanner.innerHTML = `
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <polyline points="20 6 9 17 4 12"/>
        </svg>
        <span>${msg}</span>
      `;
      
      if (state.currentMode === 'free') {
        processGameOverElo();
      }
    }
  }

  // AI Level change handler
  selectAiLevel.addEventListener('change', (e) => {
    state.aiLevelId = parseInt(e.target.value, 10);
    if (state.aiClient) state.aiClient.cancelAll();
    checkAIMove();
  });

  // Initial Boot
  if (window.location.protocol === 'file:') {
    const warning = document.createElement('div');
    warning.style = 'background: #ef4444; color: white; padding: 12px; text-align: center; font-weight: bold; position: fixed; top: 0; left: 0; right: 0; z-index: 9999; box-shadow: 0 4px 6px rgba(0,0,0,0.3); font-size: 1.1rem;';
    warning.innerHTML = '⚠️ ATENCIÓN: ESTÁS EJECUTANDO EL JUEGO SIN SERVIDOR LOCAL (file://) ⚠️<br><span style="font-size: 0.9rem; font-weight: normal;">Tu ELO y partidas <b>no se guardarán de forma permanente</b> en el archivo <code>perfil_jugador.json</code>.<br>Debes iniciar <code>python3 server.py</code> en tu terminal y abrir <b>http://localhost:8080</b> en tu navegador.</span>';
    document.body.appendChild(warning);
    // Push content down to avoid overlapping with the fixed banner
    document.body.style.paddingTop = '60px';
  }

  state.aiLevelId = parseInt(selectAiLevel.value, 10) || 3;
  loadProfile();
  populateOpenings();
  loadOpening(OPENINGS_DATA[0].id);
});
