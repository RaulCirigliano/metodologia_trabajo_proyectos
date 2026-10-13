const state = {
    items: [],
    audio: null,
    globalDuration: 3,
    currentIndex: 0,
    isPlaying: false,
    startTime: 0,
    editingIndex: null,
    transitionDuration: 0.5 // seconds
};

// DOM Elements
const canvas = document.getElementById('video-canvas');
const ctx = canvas.getContext('2d');
const dropzone = document.getElementById('dropzone');
const fileInput = document.getElementById('file-input');
const audioBtn = document.getElementById('audio-btn');
const audioInput = document.getElementById('audio-input');
const addTextBtn = document.getElementById('add-text-btn');
const timelineTrack = document.getElementById('timeline-track');
const timelineStats = document.getElementById('timeline-stats');
const playBtn = document.getElementById('play-btn');
const exportBtn = document.getElementById('export-btn');
const globalDurationInput = document.getElementById('global-duration');

// Editor DOM
const editorOverlay = document.getElementById('editor-overlay');
const editTitleInput = document.getElementById('edit-title-input');
const editDurationInput = document.getElementById('edit-duration-input');
const editTransitionInput = document.getElementById('edit-transition-input');
const saveEditBtn = document.getElementById('save-edit');
const cancelEditBtn = document.getElementById('cancel-edit');

// Initialize
function init() {
    setupEventListeners();
    renderTimeline();
    requestAnimationFrame(renderLoop);
}

function setupEventListeners() {
    dropzone.onclick = () => fileInput.click();
    fileInput.onchange = (e) => handleFiles(e.target.files);
    
    audioBtn.onclick = () => audioInput.click();
    audioInput.onchange = (e) => handleAudio(e.target.files[0]);

    addTextBtn.onclick = addTextSlide;

    globalDurationInput.oninput = (e) => {
        state.globalDuration = parseFloat(e.target.value) || 3;
        updateItemDurations();
    };

    playBtn.onclick = togglePlay;
    exportBtn.onclick = exportVideo;

    // Drag and Drop
    dropzone.ondragover = (e) => { e.preventDefault(); dropzone.style.borderColor = 'var(--primary)'; };
    dropzone.ondragleave = () => { dropzone.style.borderColor = 'var(--border)'; };
    dropzone.ondrop = (e) => {
        e.preventDefault();
        dropzone.style.borderColor = 'var(--border)';
        handleFiles(e.dataTransfer.files);
    };

    // Editor
    saveEditBtn.onclick = saveSlideSettings;
    cancelEditBtn.onclick = () => editorOverlay.style.display = 'none';
}

async function handleFiles(files) {
    const newItems = [];
    for (const file of files) {
        if (!file.type.startsWith('image/')) continue;
        
        const url = URL.createObjectURL(file);
        const img = await loadImage(url);
        
        newItems.push({
            id: Math.random().toString(36).substr(2, 9),
            type: 'image',
            file,
            url,
            img,
            title: '',
            duration: state.globalDuration,
            transition: 'fade'
        });
    }
    
    state.items = [...state.items, ...newItems];
    renderTimeline();
}

function addTextSlide() {
    state.items.push({
        id: Math.random().toString(36).substr(2, 9),
        type: 'text',
        title: 'Nueva Diapositiva',
        duration: state.globalDuration,
        transition: 'fade',
        bgColor: '#1e1e24'
    });
    renderTimeline();
}

function handleAudio(file) {
    if (!file) return;
    state.audioFile = file;
    state.audioUrl = URL.createObjectURL(file);
    state.audio = new Audio(state.audioUrl);
    
    document.getElementById('audio-name').textContent = file.name;
    document.getElementById('audio-info').style.display = 'block';
}

function loadImage(url) {
    return new Promise((resolve) => {
        const img = new Image();
        img.onload = () => resolve(img);
        img.src = url;
    });
}

function updateItemDurations() {
    state.items.forEach(item => item.duration = state.globalDuration);
    renderTimeline();
}

function renderTimeline() {
    timelineTrack.innerHTML = '';
    let totalTime = 0;

    if (state.items.length === 0) {
        timelineTrack.innerHTML = `
            <div id="empty-timeline" style="display: flex; align-items: center; justify-content: center; width: 100%; color: var(--text-muted); font-size: 0.9rem; gap: 10px;">
                <i data-lucide="image"></i>
                Añade fotos o diapositivas de texto
            </div>
        `;
        lucide.createIcons();
    } else {
        state.items.forEach((item, index) => {
            const card = document.createElement('div');
            card.className = `image-card animate-in ${state.currentIndex === index ? 'active' : ''}`;
            card.draggable = true; // Enable dragging
            
            const thumb = item.type === 'image' ? 
                `<img src="${item.url}" class="image-thumb">` :
                `<div class="image-thumb" style="background:${item.bgColor}; display:flex; align-items:center; justify-content:center; font-size:10px; padding:10px; text-align:center;">${item.title}</div>`;

            card.innerHTML = `
                ${thumb}
                <div class="card-info">
                    <div class="card-title">${item.title || (item.type === 'image' ? 'Sin título' : 'Texto')}</div>
                    <div style="display: flex; align-items: center; gap: 4px;">
                        <input type="number" value="${item.duration}" step="0.5" min="0.5" 
                            style="width: 45px; background: rgba(255,255,255,0.05); border: 1px solid var(--border); color: var(--primary); font-size: 10px; padding: 2px 4px; border-radius: 4px;"
                            onclick="event.stopPropagation()"
                            onchange="state.items[${index}].duration = parseFloat(this.value); renderTimeline();">
                        <span style="font-size: 10px; color: var(--text-muted);">s • ${item.transition}</span>
                    </div>
                </div>
                <div style="position: absolute; top: 5px; right: 5px; display: flex; gap: 4px;">
                    <button class="btn-icon" onclick="event.stopPropagation(); openEditor(${index})">✎</button>
                    <button class="btn-icon" onclick="event.stopPropagation(); removeItem(${index})">✕</button>
                </div>
            `;

            // Drag and Drop Logic
            card.ondragstart = (e) => {
                e.dataTransfer.setData('text/plain', index);
                card.style.opacity = '0.4';
                card.classList.add('dragging');
            };

            card.ondragend = () => {
                card.style.opacity = '1';
                card.classList.remove('dragging');
            };

            card.ondragover = (e) => {
                e.preventDefault();
                card.classList.add('drag-over');
            };

            card.ondragleave = () => {
                card.classList.remove('drag-over');
            };

            card.ondrop = (e) => {
                e.preventDefault();
                card.classList.remove('drag-over');
                const fromIndex = parseInt(e.dataTransfer.getData('text/plain'));
                const toIndex = index;
                
                if (fromIndex !== toIndex) {
                    const movedItem = state.items.splice(fromIndex, 1)[0];
                    state.items.splice(toIndex, 0, movedItem);
                    renderTimeline();
                }
            };

            card.onclick = () => {
                state.currentIndex = index;
                state.isPlaying = false;
                if (state.audio) state.audio.pause();
                renderTimeline();
            };

            timelineTrack.appendChild(card);
            totalTime += item.duration;
        });
    }

    timelineStats.textContent = `${state.items.length} items | ${totalTime.toFixed(1)}s`;
}

function removeItem(index) {
    state.items.splice(index, 1);
    renderTimeline();
}

function openEditor(index) {
    state.editingIndex = index;
    const item = state.items[index];
    editTitleInput.value = item.title;
    editDurationInput.value = item.duration;
    editTransitionInput.value = item.transition;
    editorOverlay.style.display = 'flex';
}

function saveSlideSettings() {
    if (state.editingIndex !== null) {
        const item = state.items[state.editingIndex];
        item.title = editTitleInput.value;
        item.duration = parseFloat(editDurationInput.value) || state.globalDuration;
        item.transition = editTransitionInput.value;
        
        state.editingIndex = null;
        editorOverlay.style.display = 'none';
        renderTimeline();
    }
}

function togglePlay() {
    if (state.items.length === 0) return;
    
    state.isPlaying = !state.isPlaying;
    playBtn.innerHTML = state.isPlaying ? 
        '<i data-lucide="pause"></i> Pausar' : 
        '<i data-lucide="play"></i> Vista Previa';
    lucide.createIcons();

    if (state.isPlaying) {
        state.startTime = performance.now();
        if (state.audio) {
            state.audio.currentTime = getSeekTime();
            state.audio.play();
        }
    } else {
        if (state.audio) state.audio.pause();
    }
}

function getSeekTime() {
    let time = 0;
    for (let i = 0; i < state.currentIndex; i++) {
        time += state.items[i].duration;
    }
    return time;
}

function renderLoop(now) {
    if (state.items.length > 0) {
        let elapsed = 0;
        if (state.isPlaying) {
            elapsed = (now - state.startTime) / 1000;
            const currentItem = state.items[state.currentIndex];
            
            if (elapsed >= currentItem.duration) {
                state.currentIndex++;
                state.startTime = now;
                
                if (state.currentIndex >= state.items.length) {
                    state.currentIndex = 0;
                    state.isPlaying = false;
                    if (state.audio) state.audio.pause();
                    togglePlay();
                }
                renderTimeline();
            }
        }
        
        drawFrame(elapsed);
    }
    requestAnimationFrame(renderLoop);
}

function drawFrame(elapsed = 0) {
    const item = state.items[state.currentIndex];
    const nextItem = state.items[state.currentIndex + 1];
    
    if (!item) return;

    // Clear
    ctx.globalAlpha = 1.0;
    ctx.fillStyle = '#000';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    const isTransitioning = nextItem && (item.duration - elapsed) < state.transitionDuration && item.transition !== 'none';
    const progress = isTransitioning ? (state.transitionDuration - (item.duration - elapsed)) / state.transitionDuration : 0;

    if (isTransitioning) {
        drawItem(item, 1 - progress, item.transition, progress, 'out');
        drawItem(nextItem, progress, item.transition, progress, 'in');
    } else {
        drawItem(item, 1.0);
    }
}

function drawItem(item, alpha, effect = 'none', progress = 0, dir = 'in') {
    ctx.save();
    ctx.globalAlpha = alpha;

    if (effect === 'slide') {
        const offset = dir === 'in' ? (1 - progress) * canvas.width : -progress * canvas.width;
        ctx.translate(offset, 0);
    } else if (effect === 'zoom') {
        const scale = dir === 'in' ? 0.8 + 0.2 * progress : 1.0 + 0.2 * progress;
        ctx.translate(canvas.width/2, canvas.height/2);
        ctx.scale(scale, scale);
        ctx.translate(-canvas.width/2, -canvas.height/2);
    }

    if (item.type === 'image') {
        const img = item.img;
        const ratio = Math.min(canvas.width / img.width, canvas.height / img.height);
        const x = (canvas.width - img.width * ratio) / 2;
        const y = (canvas.height - img.height * ratio) / 2;
        ctx.drawImage(img, x, y, img.width * ratio, img.height * ratio);
        
        // Overlay Title if present
        if (item.title) {
            ctx.fillStyle = 'rgba(0,0,0,0.5)';
            ctx.fillRect(0, canvas.height - 80, canvas.width, 80);
            ctx.fillStyle = '#fff';
            ctx.font = '700 32px Inter';
            ctx.textAlign = 'center';
            ctx.fillText(item.title, canvas.width / 2, canvas.height - 30);
        }
    } else {
        // Text Slide
        ctx.fillStyle = item.bgColor || '#1e1e24';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#fff';
        ctx.font = '700 64px Inter';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(item.title, canvas.width / 2, canvas.height / 2);
    }
    ctx.restore();
}

async function exportVideo() {
    if (state.items.length === 0) return;
    
    const originalIndex = state.currentIndex;
    state.isPlaying = false;
    state.currentIndex = 0;
    
    const stream = canvas.captureStream(30);
    let combinedStream = stream;
    if (state.audio && state.audioFile) {
        const audioCtx = new AudioContext();
        const dest = audioCtx.createMediaStreamDestination();
        const source = audioCtx.createMediaElementSource(state.audio);
        source.connect(dest);
        const audioTrack = dest.stream.getAudioTracks()[0];
        combinedStream.addTrack(audioTrack);
    }

    const recorder = new MediaRecorder(combinedStream, {
        mimeType: 'video/webm;codecs=vp9',
        videoBitsPerSecond: 5000000
    });

    const chunks = [];
    recorder.ondataavailable = (e) => chunks.push(e.data);
    recorder.onstop = () => {
        const blob = new Blob(chunks, { type: 'video/webm' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'presentacion_premium.webm';
        a.click();
        state.currentIndex = originalIndex;
    };

    recorder.start();
    if (state.audio) { state.audio.currentTime = 0; state.audio.play(); }

    for (let i = 0; i < state.items.length; i++) {
        state.currentIndex = i;
        const duration = state.items[i].duration;
        const frames = duration * 30;
        for (let f = 0; f < frames; f++) {
            drawFrame((f / 30));
            await new Promise(r => setTimeout(r, 1000 / 30));
        }
    }

    recorder.stop();
    if (state.audio) state.audio.pause();
    alert('Exportación completada.');
}

init();

async function exportVideo() {
    if (state.items.length === 0) return;

    const originalIndex = state.currentIndex;
    const originalPlaying = state.isPlaying;
    
    state.isPlaying = false;
    state.currentIndex = 0;
    
    const stream = canvas.captureStream(30); // 30 FPS
    
    // Combine with audio if available
    let combinedStream = stream;
    if (state.audio && state.audioFile) {
        const audioCtx = new AudioContext();
        const dest = audioCtx.createMediaStreamDestination();
        const source = audioCtx.createMediaElementSource(state.audio);
        source.connect(dest);
        source.connect(audioCtx.destination);
        
        const audioTrack = dest.stream.getAudioTracks()[0];
        combinedStream.addTrack(audioTrack);
    }

    const recorder = new MediaRecorder(combinedStream, {
        mimeType: 'video/webm;codecs=vp9',
        videoBitsPerSecond: 5000000 // 5Mbps
    });

    const chunks = [];
    recorder.ondataavailable = (e) => chunks.push(e.data);
    recorder.onstop = () => {
        const blob = new Blob(chunks, { type: 'video/webm' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'presentacion_visualflow.webm';
        a.click();
        
        // Restore
        state.currentIndex = originalIndex;
        state.isPlaying = originalPlaying;
    };

    // Recording process
    recorder.start();
    
    if (state.audio) {
        state.audio.currentTime = 0;
        state.audio.play();
    }

    for (let i = 0; i < state.items.length; i++) {
        state.currentIndex = i;
        drawFrame();
        await new Promise(r => setTimeout(r, state.items[i].duration * 1000));
    }

    recorder.stop();
    if (state.audio) state.audio.pause();
    alert('Exportación completada. Se descargará el archivo .webm');
}

init();
