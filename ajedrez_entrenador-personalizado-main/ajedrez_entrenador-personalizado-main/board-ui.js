/**
 * Interactive Chessboard UI component
 * Features:
 * - Click-to-move and full Drag-and-Drop (mouse + touch)
 * - Flip board (White / Black perspective)
 * - Legal move highlights (dots & capture rings)
 * - Last move highlights
 * - Check alert highlight
 * - Vector SVG Tactical Arrows overlay
 * - Theme customization (Emerald, Wood, Slate, Modern)
 */

class ChessboardUI {
  constructor(containerElement, options = {}) {
    this.container = typeof containerElement === 'string'
      ? document.querySelector(containerElement)
      : containerElement;

    this.options = Object.assign({
      orientation: 'w',
      theme: 'emerald', // emerald, wood, slate, dark
      showCoordinates: true,
      onMove: null, // callback(move)
      engine: null
    }, options);

    this.orientation = this.options.orientation;
    this.engine = this.options.engine;
    this.selectedSquare = null;
    this.legalMovesForSelected = [];
    this.lastMove = null;
    this.highlightSquares = [];
    this.arrows = [];
    this.isDragging = false;
    this.dragPiece = null;
    this.dragStartSquare = null;

    this.init();
  }

  init() {
    this.container.classList.add('chess-board-wrapper');
    this.container.innerHTML = `
      <div class="chess-board ${this.options.theme}" id="board-grid">
        <svg class="board-arrows-svg" id="arrows-layer" viewBox="0 0 800 800"></svg>
      </div>
    `;

    this.boardGrid = this.container.querySelector('#board-grid');
    this.arrowsLayer = this.container.querySelector('#arrows-layer');

    this.render();
    this.attachEvents();
  }

  setOrientation(orientation) {
    if (orientation !== 'w' && orientation !== 'b') return;
    this.orientation = orientation;
    this.render();
  }

  flip() {
    this.setOrientation(this.orientation === 'w' ? 'b' : 'w');
  }

  setTheme(themeName) {
    this.boardGrid.className = `chess-board ${themeName}`;
  }

  setArrows(arrows = []) {
    this.arrows = arrows;
    this.drawArrows();
  }

  clearArrows() {
    this.arrows = [];
    this.drawArrows();
  }

  setCustomHighlights(squares = []) {
    this.highlightSquares = squares;
    this.updateSquareStyles();
  }

  setLastMove(lastMove) {
    this.lastMove = lastMove;
    this.updateSquareStyles();
  }

  clearHighlights() {
    this.selectedSquare = null;
    this.legalMovesForSelected = [];
    this.highlightSquares = [];
    this.updateSquareStyles();
  }

  // Converts coordinate like "e4" to pixel center [x, y] in 800x800 viewBox
  squareToCenterCoords(sq) {
    const coords = ChessEngine.squareToCoords(sq);
    if (!coords) return [0, 0];

    const col = this.orientation === 'w' ? coords.col : 7 - coords.col;
    const row = this.orientation === 'w' ? coords.row : 7 - coords.row;

    const x = col * 100 + 50;
    const y = row * 100 + 50;
    return [x, y];
  }

  drawArrows() {
    if (!this.arrowsLayer) return;

    if (!this.arrows || this.arrows.length === 0) {
      this.arrowsLayer.innerHTML = '';
      return;
    }

    let svgHtml = `
      <defs>
        <marker id="arrowhead-red" markerWidth="6" markerHeight="6" refX="4" refY="3" orient="auto">
          <polygon points="0 0, 6 3, 0 6" fill="#ef4444" />
        </marker>
        <marker id="arrowhead-blue" markerWidth="6" markerHeight="6" refX="4" refY="3" orient="auto">
          <polygon points="0 0, 6 3, 0 6" fill="#38bdf8" />
        </marker>
        <marker id="arrowhead-green" markerWidth="6" markerHeight="6" refX="4" refY="3" orient="auto">
          <polygon points="0 0, 6 3, 0 6" fill="#22c55e" />
        </marker>
        <marker id="arrowhead-orange" markerWidth="6" markerHeight="6" refX="4" refY="3" orient="auto">
          <polygon points="0 0, 6 3, 0 6" fill="#f97316" />
        </marker>
        <marker id="arrowhead-yellow" markerWidth="6" markerHeight="6" refX="4" refY="3" orient="auto">
          <polygon points="0 0, 6 3, 0 6" fill="#eab308" />
        </marker>
      </defs>
    `;

    for (const arr of this.arrows) {
      const [x1, y1] = this.squareToCenterCoords(arr.from);
      const [x2, y2] = this.squareToCenterCoords(arr.to);

      const color = arr.color || '#38bdf8';
      let markerId = 'arrowhead-blue';
      if (color.includes('ef4444') || color.includes('red')) markerId = 'arrowhead-red';
      else if (color.includes('22c55e') || color.includes('green')) markerId = 'arrowhead-green';
      else if (color.includes('f97316') || color.includes('orange')) markerId = 'arrowhead-orange';
      else if (color.includes('eab308') || color.includes('yellow')) markerId = 'arrowhead-yellow';

      // Shorten the end of line slightly so the arrow head sits cleanly centered on square
      const angle = Math.atan2(y2 - y1, x2 - x1);
      const shorten = 26;
      const endX = x2 - Math.cos(angle) * shorten;
      const endY = y2 - Math.sin(angle) * shorten;

      svgHtml += `
        <line x1="${x1}" y1="${y1}" x2="${endX}" y2="${endY}"
          stroke="${color}" stroke-width="14" stroke-linecap="round"
          opacity="0.82" marker-end="url(#${markerId})" />
      `;
    }

    this.arrowsLayer.innerHTML = svgHtml;
  }

  render() {
    if (!this.engine) return;

    // Clear squares (preserve arrows layer)
    const existingSquares = this.boardGrid.querySelectorAll('.board-square');
    existingSquares.forEach(el => el.remove());

    const isWhite = this.orientation === 'w';

    for (let displayRow = 0; displayRow < 8; displayRow++) {
      for (let displayCol = 0; displayCol < 8; displayCol++) {
        const boardRow = isWhite ? displayRow : 7 - displayRow;
        const boardCol = isWhite ? displayCol : 7 - displayCol;
        const sq = ChessEngine.coordsToSquare(boardRow, boardCol);
        const isLight = (boardRow + boardCol) % 2 === 0;

        const squareEl = document.createElement('div');
        squareEl.className = `board-square ${isLight ? 'light' : 'dark'}`;
        squareEl.dataset.square = sq;
        squareEl.dataset.row = boardRow;
        squareEl.dataset.col = boardCol;

        // Coordinates display
        if (this.options.showCoordinates) {
          // Rank coordinate on first column
          if (displayCol === 0) {
            const rankLabel = document.createElement('span');
            rankLabel.className = 'coord coord-rank';
            rankLabel.textContent = 8 - boardRow;
            squareEl.appendChild(rankLabel);
          }
          // File coordinate on bottom row
          if (displayRow === 7) {
            const fileLabel = document.createElement('span');
            fileLabel.className = 'coord coord-file';
            fileLabel.textContent = String.fromCharCode(97 + boardCol);
            squareEl.appendChild(fileLabel);
          }
        }

        // Piece rendering
        const piece = this.engine.board[boardRow][boardCol];
        if (piece) {
          const pieceEl = document.createElement('div');
          pieceEl.className = `board-piece piece-${piece}`;
          pieceEl.dataset.piece = piece;
          pieceEl.innerHTML = renderPieceSvg(piece);
          squareEl.appendChild(pieceEl);
        }

        // Move target indicators (dots and rings)
        const dotEl = document.createElement('div');
        dotEl.className = 'move-indicator-dot';
        squareEl.appendChild(dotEl);

        const ringEl = document.createElement('div');
        ringEl.className = 'move-indicator-ring';
        squareEl.appendChild(ringEl);

        this.boardGrid.appendChild(squareEl);
      }
    }

    this.updateSquareStyles();
    this.drawArrows();
  }

  updateSquareStyles() {
    const squares = this.boardGrid.querySelectorAll('.board-square');
    const inCheck = this.engine ? this.engine.isInCheck() : false;
    const kingCoords = inCheck ? this.engine.findKing(this.engine.turn) : null;
    const kingSquare = kingCoords ? ChessEngine.coordsToSquare(kingCoords.row, kingCoords.col) : null;

    squares.forEach(sqEl => {
      const sq = sqEl.dataset.square;

      // Reset states
      sqEl.classList.remove(
        'is-selected',
        'is-legal-move',
        'is-legal-capture',
        'is-last-move-from',
        'is-last-move-to',
        'is-in-check',
        'is-highlighted-key'
      );

      // Selected square
      if (this.selectedSquare === sq) {
        sqEl.classList.add('is-selected');
      }

      // Legal moves dots / rings
      const legalMove = this.legalMovesForSelected.find(m => m.to === sq);
      if (legalMove) {
        if (legalMove.captured) {
          sqEl.classList.add('is-legal-capture');
        } else {
          sqEl.classList.add('is-legal-move');
        }
      }

      // Last move
      if (this.lastMove) {
        if (this.lastMove.from === sq) sqEl.classList.add('is-last-move-from');
        if (this.lastMove.to === sq) sqEl.classList.add('is-last-move-to');
      }

      // King in check
      if (kingSquare && kingSquare === sq) {
        sqEl.classList.add('is-in-check');
      }

      // Custom opening key squares
      if (this.highlightSquares.includes(sq)) {
        sqEl.classList.add('is-highlighted-key');
      }
    });
  }

  attachEvents() {
    // Click events
    this.boardGrid.addEventListener('click', (e) => {
      if (this.isDragging) return;

      const squareEl = e.target.closest('.board-square');
      if (!squareEl) {
        this.clearSelection();
        return;
      }

      const clickedSquare = squareEl.dataset.square;
      this.handleSquareClick(clickedSquare);
    });

    // Drag and Drop (Mouse + Touch)
    const handleDragStart = (e) => {
      const pieceEl = e.target.closest('.board-piece');
      if (!pieceEl) return;

      const squareEl = pieceEl.closest('.board-square');
      if (!squareEl) return;

      const sq = squareEl.dataset.square;
      const piece = pieceEl.dataset.piece;

      // Only drag pieces for current player
      if (ChessEngine.pieceColor(piece) !== this.engine.turn) {
        return;
      }

      this.isDragging = true;
      this.dragStartSquare = sq;
      this.dragPiece = pieceEl;

      // Select square and calculate legal moves
      this.selectSquare(sq);

      // Create floating drag element
      this.floatingDragEl = pieceEl.cloneNode(true);
      this.floatingDragEl.classList.add('dragging-piece-floating');
      document.body.appendChild(this.floatingDragEl);

      pieceEl.style.opacity = '0.35';

      const point = e.touches ? e.touches[0] : e;
      this.moveFloatingEl(point.clientX, point.clientY);

      e.preventDefault();
    };

    const handleDragMove = (e) => {
      if (!this.isDragging || !this.floatingDragEl) return;
      const point = e.touches ? e.touches[0] : e;
      this.moveFloatingEl(point.clientX, point.clientY);
      e.preventDefault();
    };

    const handleDragEnd = (e) => {
      if (!this.isDragging) return;

      if (this.dragPiece) {
        this.dragPiece.style.opacity = '1';
      }

      if (this.floatingDragEl) {
        this.floatingDragEl.remove();
        this.floatingDragEl = null;
      }

      const point = e.changedTouches ? e.changedTouches[0] : e;
      const targetElement = document.elementFromPoint(point.clientX, point.clientY);
      const targetSquareEl = targetElement ? targetElement.closest('.board-square') : null;

      const fromSq = this.dragStartSquare;
      const toSq = targetSquareEl ? targetSquareEl.dataset.square : null;

      this.isDragging = false;
      this.dragStartSquare = null;
      this.dragPiece = null;

      if (toSq && toSq !== fromSq) {
        const attempted = this.attemptMove(fromSq, toSq);
        if (!attempted) {
          // If move wasn't legal, keep or clear selection
          this.clearSelection();
        }
      } else {
        // Just clicked or dropped in place
        this.updateSquareStyles();
      }
    };

    this.boardGrid.addEventListener('mousedown', handleDragStart);
    window.addEventListener('mousemove', handleDragMove);
    window.addEventListener('mouseup', handleDragEnd);

    this.boardGrid.addEventListener('touchstart', handleDragStart, { passive: false });
    window.addEventListener('touchmove', handleDragMove, { passive: false });
    window.addEventListener('touchend', handleDragEnd);
  }

  moveFloatingEl(clientX, clientY) {
    if (!this.floatingDragEl) return;
    const size = 60;
    this.floatingDragEl.style.left = `${clientX - size / 2}px`;
    this.floatingDragEl.style.top = `${clientY - size / 2}px`;
  }

  handleSquareClick(sq) {
    if (this.selectedSquare) {
      if (this.selectedSquare === sq) {
        // Deselect
        this.clearSelection();
        return;
      }

      // Try move to clicked square
      const success = this.attemptMove(this.selectedSquare, sq);
      if (success) {
        return;
      }
    }

    // Otherwise, select piece on clicked square if it belongs to current player
    const piece = this.engine.getPiece(sq);
    if (piece && ChessEngine.pieceColor(piece) === this.engine.turn) {
      this.selectSquare(sq);
    } else {
      this.clearSelection();
    }
  }

  selectSquare(sq) {
    this.selectedSquare = sq;
    this.legalMovesForSelected = this.engine ? this.engine.getLegalMoves(sq) : [];
    this.updateSquareStyles();
  }

  clearSelection() {
    this.selectedSquare = null;
    this.legalMovesForSelected = [];
    this.updateSquareStyles();
  }

  attemptMove(fromSq, toSq, promoChoice = null) {
    if (!this.engine) return false;

    const legal = this.engine.getLegalMoves(fromSq);
    const validMoves = legal.filter(m => m.to === toSq);
    if (validMoves.length === 0) return false;

    // Check if it's a promotion move
    const isPromotion = validMoves.some(m => m.promotion);

    if (isPromotion && !promoChoice) {
      this.showPromotionDialog(fromSq, toSq);
      // Return true to pretend it's handled (so it doesn't clear selection or flash)
      return true; 
    }

    const valid = isPromotion 
      ? validMoves.find(m => (m.promotion || '').toUpperCase() === promoChoice.toUpperCase())
      : validMoves[0];

    if (!valid) return false;

    // Check if move is handled by callback
    if (this.options.onMove) {
      const handled = this.options.onMove({ from: fromSq, to: toSq, promotion: promoChoice, moveObj: valid });
      if (handled === false) {
        this.clearSelection();
        return false;
      }
    }

    const moveRecord = this.engine.makeMove({ from: fromSq, to: toSq, promotion: promoChoice });
    if (!moveRecord) return false;

    // Play sounds
    if (moveRecord.isCheck) {
      chessSound.playCheck();
    } else if (moveRecord.captured) {
      chessSound.playCapture();
    } else {
      chessSound.playMove();
    }

    this.setLastMove(moveRecord);
    this.clearSelection();
    this.render();
    return true;
  }

  showPromotionDialog(fromSq, toSq) {
    let dialog = this.container.querySelector('#promo-dialog');
    if (!dialog) {
      dialog = document.createElement('div');
      dialog.id = 'promo-dialog';
      dialog.style.position = 'absolute';
      dialog.style.zIndex = '1000';
      dialog.style.background = 'rgba(255,255,255,0.95)';
      dialog.style.border = '2px solid #ccc';
      dialog.style.borderRadius = '8px';
      dialog.style.padding = '10px';
      dialog.style.boxShadow = '0 4px 15px rgba(0,0,0,0.3)';
      dialog.style.display = 'flex';
      dialog.style.flexDirection = 'column';
      dialog.style.gap = '5px';
      
      this.container.style.position = 'relative'; // ensure wrapper is relative
      this.container.appendChild(dialog);
    }

    dialog.innerHTML = '';
    dialog.style.display = 'flex';

    const color = this.engine.turn;
    const pieces = color === 'w' ? ['Q', 'R', 'B', 'N'] : ['q', 'r', 'b', 'n'];

    dialog.style.top = '50%';
    dialog.style.left = '50%';
    dialog.style.transform = 'translate(-50%, -50%)';

    const title = document.createElement('div');
    title.textContent = 'Elige coronación:';
    title.style.fontWeight = 'bold';
    title.style.textAlign = 'center';
    title.style.marginBottom = '5px';
    title.style.color = '#333';
    dialog.appendChild(title);

    const piecesRow = document.createElement('div');
    piecesRow.style.display = 'flex';
    piecesRow.style.gap = '10px';
    dialog.appendChild(piecesRow);

    pieces.forEach(p => {
      const btn = document.createElement('div');
      btn.className = `board-piece piece-${p}`;
      btn.style.width = '60px';
      btn.style.height = '60px';
      btn.style.cursor = 'pointer';
      btn.style.position = 'relative';
      if (typeof renderPieceSvg !== 'undefined') btn.innerHTML = renderPieceSvg(p);
      
      // On click, execute move with this promotion choice
      btn.onclick = (e) => {
        e.stopPropagation(); // prevent triggering other clicks
        dialog.style.display = 'none';
        this.attemptMove(fromSq, toSq, p.toLowerCase());
      };

      piecesRow.appendChild(btn);
    });
    
    // Add a cancel button
    const cancelBtn = document.createElement('button');
    cancelBtn.textContent = 'Cancelar';
    cancelBtn.style.marginTop = '10px';
    cancelBtn.style.padding = '5px';
    cancelBtn.style.cursor = 'pointer';
    cancelBtn.style.color = '#333';
    cancelBtn.style.border = '1px solid #ccc';
    cancelBtn.style.borderRadius = '4px';
    cancelBtn.onclick = (e) => {
      e.stopPropagation();
      dialog.style.display = 'none';
      this.clearSelection();
    };
    dialog.appendChild(cancelBtn);
  }
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { ChessboardUI };
}
