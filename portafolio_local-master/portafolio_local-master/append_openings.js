const fs = require('fs');
const file = '/home/raul/.gemini/antigravity/scratch/chess-openings-trainer/openings-data.js';
let content = fs.readFileSync(file, 'utf8');

const endOfArray = content.lastIndexOf('];');
if (endOfArray === -1) {
  console.log("Could not find end of array");
  process.exit(1);
}

// Ensure we don't duplicate. Wait, the user wants me to add these explicitly.
const newOpenings = `
  ,
  {
    id: "defensa-siciliana-dragon",
    category: "Semi-abiertas (1.e4 c5)",
    name: "Defensa Siciliana: Variante Dragón",
    eco: "B70",
    side: "b",
    difficulty: "Avanzado",
    style: "Táctico / Ataque en Flancos Opuestos",
    ratingRange: "1400 - 2800",
    summary: "Una de las variantes más agudas del ajedrez. Las negras fianchettan su alfil en g7 (cuya estructura de peones recuerda a la constelación del Dragón) para controlar la gran diagonal y contraatacar en el flanco de dama.",
    plansWhite: [
      "El Ataque Yugoslavo: f3, Ae3, Dd2, O-O-O.",
      "Lanzar una tormenta de peones con h4 y h5 para abrir la columna 'h'.",
      "Cambiar el fuerte alfil de g7 con Ah6."
    ],
    plansBlack: [
      "Aprovechar la columna semiabierta 'c' para atacar el rey blanco enrocado largo.",
      "Fuerte presión en la diagonal h8-a1 con el alfil Dragón.",
      "Sacrificio de calidad temático ...Txc3 para destruir el enroque blanco."
    ],
    keySquares: ["g7", "c5", "d4", "c3"],
    moves: [
      { san: "e4", from: "e2", to: "e4", name: "Peón de Rey", comment: "Ocupa el centro." },
      { san: "c5", from: "c7", to: "c5", name: "La Siciliana", comment: "Lucha asimétrica por d4." },
      { san: "Nf3", from: "g1", to: "f3", name: "Preparación", comment: "Prepara d4." },
      { san: "d6", from: "d7", to: "d6", name: "Control central", comment: "Controla e5 y prepara el desarrollo." },
      { san: "d4", from: "d2", to: "d4", name: "Ruptura blanca", comment: "Las blancas abren el centro." },
      { san: "cxd4", from: "c5", to: "d4", name: "Cambio de peones", comment: "Las negras abren la columna c." },
      { san: "Nxd4", from: "f3", to: "d4", name: "Caballo centralizado", comment: "Dominio central blanco." },
      { san: "Nf6", from: "g8", to: "f6", name: "Desarrollo", comment: "Ataca e4." },
      { san: "Nc3", from: "b1", to: "c3", name: "Defensa de e4", comment: "Sostiene el peón central." },
      { san: "g6", from: "g7", to: "g6", name: "El Dragón", comment: "¡La jugada que define la variante! Prepara el fianchetto en g7 para que el alfil domine la gran diagonal.", highlightSquares: ["g7"], arrows: [{from:"f8", to:"g7", color:"#38bdf8"}] }
    ],
    traps: []
  },
  {
    id: "defensa-francesa-winawer",
    category: "Semi-abiertas (1.e4 e6)",
    name: "Defensa Francesa: Variante Winawer",
    eco: "C15",
    side: "b",
    difficulty: "Avanzado",
    style: "Complejo / Bloqueado",
    ratingRange: "1500 - 2800",
    summary: "Las negras clavan el caballo blanco en c3 con ...Ab4, dispuestas a entregar su pareja de alfiles a cambio de dañar la estructura de peones blancos en el flanco de dama (peones doblados en c).",
    plansWhite: [
      "Aprovechar la pareja de alfiles y el espacio en el flanco de rey con Qg4.",
      "Explotar las debilidades negras en las casillas oscuras."
    ],
    plansBlack: [
      "Atacar los peones doblados blancos en la columna c.",
      "Cerrar la posición para minimizar el impacto de la pareja de alfiles blancos.",
      "Contragolpear en el centro con ...c5."
    ],
    keySquares: ["b4", "c3", "g7", "c5"],
    moves: [
      { san: "e4", from: "e2", to: "e4", name: "Peón de Rey", comment: "Ocupa el centro." },
      { san: "e6", from: "e7", to: "e6", name: "La Francesa", comment: "Prepara d5." },
      { san: "d4", from: "d2", to: "d4", name: "Centro ideal", comment: "Las blancas dominan e4 y d4." },
      { san: "d5", from: "d7", to: "d5", name: "Golpe al centro", comment: "Ataca e4 directamente." },
      { san: "Nc3", from: "b1", to: "c3", name: "Defensa natural", comment: "Defiende e4 y mantiene la tensión." },
      { san: "Bb4", from: "f8", to: "b4", name: "La Winawer", comment: "Clava el caballo y amenaza indirectamente a e4. Se prepara para destruir la estructura blanca en c3.", highlightSquares: ["b4", "c3"], arrows: [{from:"b4", to:"c3", color:"#ef4444"}] }
    ],
    traps: []
  },
  {
    id: "apertura-escocesa",
    category: "Abiertas (1.e4 e5)",
    name: "Apertura Escocesa",
    eco: "C45",
    side: "w",
    difficulty: "Intermedio",
    style: "Juego Abierto / Combate Central",
    ratingRange: "1000 - 2700",
    summary: "Las blancas rompen el centro inmediatamente con d4 en la jugada 3, buscando abrir líneas para un juego táctico y evitar las complejas maniobras de la Apertura Española.",
    plansWhite: [
      "Ganar espacio en el centro y presionar rápido con Ac4 o Cxc6.",
      "Evitar estructuras estáticas y buscar posiciones abiertas."
    ],
    plansBlack: [
      "Atacar e4 y presionar el caballo en d4 con ...Ac5 o ...Cf6.",
      "Preparar la reacción d5 para igualar en el centro."
    ],
    keySquares: ["d4", "e4", "e5", "c6"],
    moves: [
      { san: "e4", from: "e2", to: "e4", name: "Peón de Rey", comment: "Ocupa el centro." },
      { san: "e5", from: "e7", to: "e5", name: "Defensa Clásica", comment: "Controla d4." },
      { san: "Nf3", from: "g1", to: "f3", name: "Ataque a e5", comment: "Desarrollo con ganancia de tiempo." },
      { san: "Nc6", from: "b8", to: "c6", name: "Defensa de e5", comment: "Desarrolla y defiende." },
      { san: "d4", from: "d2", to: "d4", name: "La Escocesa", comment: "¡Ruptura inmediata! Las blancas exigen una resolución inmediata de la tensión central.", highlightSquares: ["d4", "e5"], arrows: [{from:"d4", to:"e5", color:"#ef4444"}] },
      { san: "exd4", from: "e5", to: "d4", name: "Captura obligada", comment: "Mantener el peón es imposible." },
      { san: "Nxd4", from: "f3", to: "d4", name: "Recuperación central", comment: "El caballo domina el centro, listo para el combate." }
    ],
    traps: []
  },
  {
    id: "gambito-de-rey-aceptado",
    category: "Abiertas (1.e4 e5)",
    name: "Gambito de Rey Aceptado",
    eco: "C33",
    side: "w",
    difficulty: "Avanzado",
    style: "Ultra Agresivo / Táctico",
    ratingRange: "1000 - 2400",
    summary: "La apertura de los románticos del siglo XIX. Las blancas sacrifican un peón de flanco para desviar el peón central negro y conseguir un masivo centro de peones y ataques fulminantes por la columna f semiabierta.",
    plansWhite: [
      "Sacrificar material por desarrollo rápido y ataque al rey.",
      "Dominar el centro con d4.",
      "Abrir la columna 'f' para la torre tras el enroque."
    ],
    plansBlack: [
      "Devolver el peón en el momento justo (ej. ...d5) para igualar el desarrollo.",
      "Aprovechar la diagonal débil g1-a7 del rey blanco.",
      "Sostener el peón extra con ...g5 si se busca la máxima complicación."
    ],
    keySquares: ["f4", "e5", "d4", "f7"],
    moves: [
      { san: "e4", from: "e2", to: "e4", name: "Peón de Rey", comment: "Dominio central." },
      { san: "e5", from: "e7", to: "e5", name: "Respuesta central", comment: "Disputa d4 y f4." },
      { san: "f4", from: "f2", to: "f4", name: "El Gambito de Rey", comment: "Las blancas ofrecen un peón para desviar al defensor del centro y abrir la columna f.", highlightSquares: ["f4", "e5"], arrows: [{from:"f4", to:"e5", color:"#ef4444"}] },
      { san: "exf4", from: "e5", to: "f4", name: "Gambito Aceptado", comment: "Las negras aceptan el desafío. ¡Empieza la fiesta táctica!" },
      { san: "Nf3", from: "g1", to: "f3", name: "Desarrollo y Prevención", comment: "Desarrolla una pieza y previene el molesto ...Dh4+ de las negras." }
    ],
    traps: []
  },
  {
    id: "ataque-fegatello",
    category: "Abiertas (1.e4 e5)",
    name: "Ataque Fegatello (Fried Liver Attack)",
    eco: "C57",
    side: "w",
    difficulty: "Intermedio",
    style: "Sacrificio Violento / Ataque al Rey",
    ratingRange: "800 - 2000",
    summary: "Una de las líneas más espectaculares de la Defensa de los Dos Caballos. Las blancas sacrifican un caballo en f7 para arrastrar al rey negro al centro del tablero y someterlo a un ataque demoledor.",
    plansWhite: [
      "Sacrificar en f7 (Cxf7) para exponer al rey negro.",
      "Dar jaque rápido con Df3+ forzando al rey negro a defender d5.",
      "Aumentar la presión sobre la pieza clavada en d5 con Cc3."
    ],
    plansBlack: [
      "Llevar el rey a e6 para defender el caballo en d5.",
      "Tratar de devolver material para salvar al rey y terminar el desarrollo."
    ],
    keySquares: ["f7", "d5", "e6", "f3"],
    moves: [
      { san: "e4", from: "e2", to: "e4", name: "Peón de Rey", comment: "Ocupación central." },
      { san: "e5", from: "e7", to: "e5", name: "Respuesta Clásica", comment: "Control central." },
      { san: "Nf3", from: "g1", to: "f3", name: "Desarrollo y Ataque", comment: "Ataca e5." },
      { san: "Nc6", from: "b8", to: "c6", name: "Defensa", comment: "Defiende e5." },
      { san: "Bc4", from: "f1", to: "c4", name: "Apertura Italiana", comment: "Apunta a la débil f7." },
      { san: "Nf6", from: "g8", to: "f6", name: "Defensa de los Dos Caballos", comment: "Contraataca en e4 en lugar de Ac5." },
      { san: "Ng5", from: "f3", to: "g5", name: "Ataque a f7", comment: "¡Agresividad temprana! Amenaza Cxf7 o Axf7+ apoyado por el alfil y el caballo.", highlightSquares: ["f7"], arrows: [{from:"g5", to:"f7", color:"#ef4444"}] },
      { san: "d5", from: "d7", to: "d5", name: "Bloqueo obligatorio", comment: "La única forma de detener la amenaza sobre f7." },
      { san: "exd5", from: "e4", to: "d5", name: "Captura", comment: "Abre la columna e." },
      { san: "Nxd5", from: "f6", to: "d5", name: "El error fatal", comment: "Las negras recapturan de inmediato, permitiendo el sacrificio. (Lo correcto es ...Ca5 o ...b5).", highlightSquares: ["d5", "g5"] },
      { san: "Nxf7", from: "g5", to: "f7", name: "¡El Ataque Fegatello!", comment: "¡Un sacrificio espectacular! Ataca la Dama y la Torre simultáneamente.", arrows: [{from:"f7", to:"d8", color:"#f97316"}, {from:"f7", to:"h8", color:"#f97316"}] },
      { san: "Kxf7", from: "e8", to: "f7", name: "Rey forzado", comment: "El rey debe salir a defenderse." },
      { san: "Qf3+", from: "d1", to: "f3", name: "Ataque doble", comment: "Jaque al rey y ataca al caballo clavado en d5." },
      { san: "Ke6", from: "f7", to: "e6", name: "El Rey al centro", comment: "La única manera de defender d5. ¡El rey negro queda expuesto en el medio del tablero!" }
    ],
    traps: []
  },
  {
    id: "defensa-nimzoindia",
    category: "Cerradas (1.d4 Nf6)",
    name: "Defensa Nimzoindia",
    eco: "E20",
    side: "b",
    difficulty: "Avanzado",
    style: "Hipermoderno / Estratégico",
    ratingRange: "1600 - 2850",
    summary: "Una de las defensas más respetadas contra 1.d4. Las negras permiten a las blancas controlar el centro con peones temporalmente, pero desarrollan su alfil a b4 para clavar el caballo de c3 y controlar la vital casilla e4.",
    plansWhite: [
      "Conseguir la pareja de alfiles tras Axc3+.",
      "Dominar el centro con e4 si se permite.",
      "Atacar en el flanco de rey con una fuerte presencia central."
    ],
    plansBlack: [
      "Dañar la estructura de peones blanca con ...Axc3+ creando peones doblados.",
      "Bloquear las casillas de color de su propio alfil (casillas oscuras).",
      "Maniobrar ágilmente con los caballos aprovechando las debilidades blancas."
    ],
    keySquares: ["e4", "c3", "d5", "c5"],
    moves: [
      { san: "d4", from: "d2", to: "d4", name: "Peón de Dama", comment: "Control central." },
      { san: "Nf6", from: "g8", to: "f6", name: "Defensa India", comment: "Previene e4." },
      { san: "c4", from: "c2", to: "c4", name: "Expansión blanca", comment: "Control de d5 y espacio en el flanco de dama." },
      { san: "e6", from: "e7", to: "e6", name: "Soporte y preparación", comment: "Prepara d5 o b4." },
      { san: "Nc3", from: "b1", to: "c3", name: "Control central", comment: "Prepara e4." },
      { san: "Bb4", from: "f8", to: "b4", name: "La Nimzoindia", comment: "Clava el caballo y controla la casilla e4 de forma indirecta y muy eficaz.", highlightSquares: ["b4", "c3", "e4"], arrows: [{from:"b4", to:"c3", color:"#ef4444"}] }
    ],
    traps: []
  },
  {
    id: "apertura-inglesa",
    category: "Flanco (1.c4)",
    name: "Apertura Inglesa",
    eco: "A10",
    side: "w",
    difficulty: "Avanzado",
    style: "Posicional / Flexibilidad",
    ratingRange: "1400 - 2800",
    summary: "Una apertura de flanco muy sólida y flexible. Las blancas controlan la casilla d5 desde un costado con 1.c4, evitando las líneas teóricas forzadas de 1.e4 o 1.d4 y trasladando la lucha al medio juego.",
    plansWhite: [
      "Controlar la casilla d5.",
      "Fianchettar el alfil de rey en g2 (g3, Ag2) para presionar la gran diagonal.",
      "Atacar en el flanco de dama con a3, b4, Tb1 (Ataque de minorías)."
    ],
    plansBlack: [
      "Ocupar el centro con ...e5 (Inglesa Simétrica) o ...c5.",
      "Construir un esquema similar a la Defensa India de Rey o Grunfeld."
    ],
    keySquares: ["d5", "c4", "g2", "b4"],
    moves: [
      { san: "c4", from: "c2", to: "c4", name: "Apertura Inglesa", comment: "Controla el centro (d5) desde el flanco.", highlightSquares: ["d5"], arrows: [{from:"c4", to:"d5", color:"#38bdf8"}] },
      { san: "e5", from: "e7", to: "e5", name: "Siciliana Invertida", comment: "Las negras reclaman el centro. La posición se parece a una Siciliana con colores invertidos." },
      { san: "Nc3", from: "b1", to: "c3", name: "Desarrollo y Control", comment: "Aumenta la presión sobre d5." },
      { san: "Nf6", from: "g8", to: "f6", name: "Desarrollo", comment: "Prepara d5." },
      { san: "g3", from: "g2", to: "g3", name: "Preparando el Fianchetto", comment: "El alfil en g2 será una pieza poderosísima." }
    ],
    traps: []
  }
`;

const newContent = content.substring(0, endOfArray) + newOpenings + content.substring(endOfArray);
fs.writeFileSync(file, newContent);
console.log('Openings updated successfully');
