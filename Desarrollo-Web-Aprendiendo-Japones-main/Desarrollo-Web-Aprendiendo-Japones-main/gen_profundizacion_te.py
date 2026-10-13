import os
import subprocess

data = {
    "profundizacion-forma-te": {
        "title": "La Forma TE: Usos Avanzados y Profundización",
        "grammar": [
            "<strong>1. 〜ておく (-te oku): Preparación Activa para el Futuro.</strong> Expresa la realización de una acción con antelación para estar preparado ante un evento futuro. El sujeto actúa intencionadamente. Contracción informal: <em>〜とく (-toku)</em>. Ejemplo: ビールを買っておきます (Compro cervezas de antemano).",
            "<strong>2. 〜てある (-te aru): Estado Resultante de una Preparación.</strong> Describe el estado mantenido en el que ha quedado un objeto tras una acción realizada previamente por alguien. La partícula <em>を</em> cambia obligatoriamente a <em>が</em>. Ejemplo: 本が置いてあります (El libro ya está preparado/colocado).",
            "<strong>3. 〜てみる (-te miru): Probar o Intentar una Experiencia.</strong> Expresa la idea de probar a hacer una acción por primera vez o intentar algo para descubrir cuál es el resultado. Se escribe en hiragana. Ejemplo: パンダを見てみます (Probar a ver un panda).",
            "<strong>4. 〜てしまう (-te shimau): Culminación Total.</strong> Expresa la conclusión total o finalización absoluta de una tarea o acción. A veces implica lamentación. Contracción informal: <em>〜ちゃう (-chau)</em>. Ejemplo: 宿題をしてしまいました (He terminado totalmente los deberes)."
        ],
        "examples": [
            ("明日パーティーがあるので、ビールを買っておきます。", "1. Como mañana hay una fiesta, compro cervezas de antemano.", "あしたパーティーがあるので、ビールをかっておきます"),
            ("授業の前に、本を机の上に置いておきます。", "2. Antes de la clase, dejo el libro preparado sobre el escritorio.", "じゅぎょうのまえに、ほんをつくえのうえにおいとおきます"),
            ("壁にカレンダーが掛けてあります。", "3. El calendario está (ha sido) colgado en la pared.", "かべにカレンダーがかけてあります"),
            ("ここにゴミが捨ててあります。", "4. Aquí la basura ha sido tirada (alguien la tiró y ahí permanece).", "ここにゴミがすててあります"),
            ("日本の着物を着てみたいです。", "5. Me gustaría intentar usar (probar a vestirme con) un kimono japonés.", "にほんのきものをきてみたいです"),
            ("わからない言葉は、先生に聞いてみました。", "6. Las palabras que no entendía, intenté preguntárselas al profesor.", "わからないことばは、せんせいにきいてみました"),
            ("買ったばかりのケーキを全部食べてしまった。", "7. Me he comido por completo el pastel que acabo de comprar.", "かったばかりのケーキをぜんぶたべてしまった"),
            ("彼のことをすっかり忘れてしまった。", "8. Me olvidé completamente de él.", "かれのことをすっかりわすれてしまった"),
            ("晩ご飯を作っておくから、後で食べてね。", "9. Prepararé la cena de antemano, así que cómetela luego. (contracción: つくっとく)", "ばんごはんをつくっておくから、あとでたべてね"),
            ("あ、パスポートを家に忘れちゃった！", "10. ¡Ah, me he olvidado el pasaporte en casa por completo! (-chau / coloquial de -te shimau)", "あ、パスポートをいえにわすれちゃった")
        ],
        "exercises": [
            {"q": "¿Qué expresión describe la realización de una acción CON ANTELACIÓN para estar preparado ante un evento futuro?", "options": [{"text": "〜ておく", "correct": True}, {"text": "〜てある", "correct": False}, {"text": "〜てみる", "correct": False}]},
            {"q": "¿Qué expresión describe el ESTADO MANTENIDO en el que ha quedado un objeto tras la acción de alguien?", "options": [{"text": "〜てある", "correct": True}, {"text": "〜ておく", "correct": False}, {"text": "〜てしまう", "correct": False}]},
            {"q": "¿Cómo se escribe correctamente la expresión para 'Probar o intentar hacer algo por primera vez'?", "options": [{"text": "〜てみる (hiragana)", "correct": True}, {"text": "〜て見る (kanji)", "correct": False}, {"text": "Ambas son correctas", "correct": False}]},
            {"q": "¿Qué expresión indica la conclusión TOTAL o FINALIZACIÓN ABSOLUTA de una tarea (a menudo acompañada de adverbios como 'mou' o 'sukkari')?", "options": [{"text": "〜てしまう", "correct": True}, {"text": "〜ておく", "correct": False}, {"text": "〜てある", "correct": False}]},
            {"q": "La contracción coloquial (callejera) de '〜てしまう' (ej. tabete shimau) es:", "options": [{"text": "〜ちゃう (tabechau)", "correct": True}, {"text": "〜とく (tabetoku)", "correct": False}, {"text": "〜じゃう (tabejau)", "correct": False}]},
            {"q": "¿Qué partícula debe cambiar obligatoriamente cuando usamos '〜てある' con un verbo transitivo?", "options": [{"text": "を cambia a が", "correct": True}, {"text": "が cambia a を", "correct": False}, {"text": "に cambia a で", "correct": False}]},
            {"q": "'El desayuno YA ESTÁ preparado/servido' (Asagohan ___ tsukutte ___):", "options": [{"text": "が / あります", "correct": True}, {"text": "を / おきます", "correct": False}, {"text": "が / おきます", "correct": False}]},
            {"q": "'Me gustaría PROBAR EL TÉ MATCHA' (Maccha o nonde...):", "options": [{"text": "みたいです", "correct": True}, {"text": "おきたいです", "correct": False}, {"text": "しまいます", "correct": False}]},
            {"q": "La contracción coloquial de '〜ておく' (ej. hanashite oku) es:", "options": [{"text": "〜とく (hanashitoku)", "correct": True}, {"text": "〜ちゃう (hanashichau)", "correct": False}, {"text": "〜どく (hanashidoku)", "correct": False}]},
            {"q": "'Ya he terminado los deberes por completo' (Shukudai o shite...):", "options": [{"text": "しまいました", "correct": True}, {"text": "おきました", "correct": False}, {"text": "ありました", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "あ、カレンダーが壁にかけてありますね。誰がかけたんですか？", "Ah, el calendario está (ha sido) colgado en la pared. ¿Quién lo colgó?"),
            ("ja-JP-KeitaNeural", "ああ、それは私が昨日かけておきました。今日の予定を忘れないようにするためです。", "Ah, eso lo colgué yo ayer de antemano. Es para no olvidar los planes de hoy."),
            ("ja-JP-NanamiNeural", "なるほど。準備がいいですね。ところで、その新しいお菓子、食べてみましたか？", "Ya veo. Qué buena preparación. Por cierto, esos dulces nuevos, ¿has intentado probarlos?"),
            ("ja-JP-KeitaNeural", "はい、さっき食べてみました。すごく美味しくて、全部食べてしまいましたよ！", "Sí, intenté probarlos hace un rato. ¡Estaban deliciosos, me los he comido todos por completo!"),
            ("ja-JP-NanamiNeural", "えーっ！私の分も残しておいてって言ったのに... すっかり忘れちゃったんですね。", "¡Eh! Y eso que te dije que dejaras mi parte (preparada de antemano)... Te olvidaste por completo, ¿no?")
        ]
    }
}

base_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\lessons"
audio_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\audio"
os.makedirs(audio_dir, exist_ok=True)

lesson_id = "profundizacion-forma-te"
d = data[lesson_id]
print(f"--- Generating Lesson {lesson_id} ---")

# Audio Gen
final_mp3 = os.path.join(audio_dir, f"dialogue-{lesson_id}.mp3")
if not os.path.exists(final_mp3):
    files = []
    for j, (voice, text_jp, _) in enumerate(d["dialogue"]):
        filename = f"line_{lesson_id}_{j}.mp3"
        safe_text = text_jp.replace('"', '\\"')
        cmd = f'python -m edge_tts --voice {voice} --text "{safe_text}" --rate=-5% --write-media {filename}'
        subprocess.run(cmd, shell=True)
        files.append(filename)

    with open(f"files_{lesson_id}.txt", "w", encoding="utf-8") as f:
        for filename in files:
            f.write(f"file '{filename}'\n")

    subprocess.run(f"ffmpeg -f concat -safe 0 -i files_{lesson_id}.txt -c copy \"{final_mp3}\" -y", shell=True)

    for filename in files:
        if os.path.exists(filename):
            os.remove(filename)
    if os.path.exists(f"files_{lesson_id}.txt"):
        os.remove(f"files_{lesson_id}.txt")
        
# HTML Gen
grammar_html = "".join([f"                <li>{g}</li>\n" for g in d["grammar"]])
examples_html = "".join([f'''        <div class="practice-item"><div class="practice-content"><div class="text-jp">{ex[0]}</div><div class="text-es">{ex[1]}</div></div><button class="audio-btn" onclick="playAudio('{ex[2]}')">🔊</button></div>\n''' for ex in d["examples"]])

exercises_html = ""
for idx, q in enumerate(d["exercises"], 1):
    exercises_html += f'''        <div class="question-block" style="background:#fff; border:1px solid #e2e8f0; padding:1.5rem; border-radius:10px; margin-bottom:1rem;">
        <p style="font-weight:600; margin-bottom:1rem; font-size:1.1rem;">{idx}. {q["q"]}</p>
        <div style="display:grid; gap:10px;">\n'''
    for opt in q["options"]:
        correct_str = "true" if opt["correct"] else "false"
        exercises_html += f'''                <button class="option-btn" data-correct="{correct_str}">{opt["text"]}</button>\n'''
    exercises_html += '''            </div>
        <div class="feedback-msg" style="margin-top:10px; font-weight:600; min-height:24px;"></div>
    </div>\n'''

dialogue_html = f"""<h2 class="section-title">🎧 Práctica de Comprensión Auditiva</h2>
<div class="grammar-note" style="background-color: #eff6ff; border-left-color: #3b82f6;">
    <p>Escucha este diálogo a velocidad casi natural prestando atención al uso de las formas TE.</p>
    
    <div style="text-align: center; margin: 1.5rem 0; background: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border: 1px solid #e2e8f0;">
        <p style="margin-bottom: 15px; font-weight: 600; color: #475569; font-size: 1.1rem;">🎧 Escucha el diálogo (Voces IA):</p>
        <audio controls style="width: 100%; max-width: 450px; outline: none; border-radius: 50px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
            <source src="../audio/dialogue-{lesson_id}.mp3" type="audio/mpeg">
            Tu navegador no soporta el elemento de audio.
        </audio>
    </div>

    <details style="background: white; padding: 1rem; border-radius: 8px; border: 1px solid #e2e8f0; margin-top: 1rem;">
        <summary style="font-weight: 600; cursor: pointer; color: var(--primary-color);">Ver Transcripción y Traducción</summary>
        <div style="margin-top: 1rem; display: grid; gap: 1rem; font-size: 0.95rem;">
"""
for _, text_jp, text_es in d["dialogue"]:
    dialogue_html += f'            <div><div class="text-jp">{text_jp}</div><div class="text-es">{text_es}</div></div>\n'
dialogue_html += """        </div>
    </details>
</div>
"""

html = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Profundización - La Forma TE</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=Noto+Sans+JP:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../css/style.css">
</head>
<body class="iframe-body">
<div class="max-w-4xl">
    <div class="lesson-header-simple" style="background: linear-gradient(135deg, #e0f2fe 0%, #f0f9ff 100%); padding: 2rem; border-radius: 12px; margin-bottom: 2rem; border-left: 6px solid var(--primary-color); border-bottom: none;">
        <span>Profundizaciones</span>
        <h1>{d["title"]}</h1>
        <p class="lesson-desc">Uso avanzado de ~ておく, ~てある, ~てみる, y ~てしまう.</p>
    </div>

    <h2 class="section-title">📚 Gramática Principal</h2>
    <div class="grammar-note">
        <ul>
{grammar_html}            </ul>
    </div>
    
    <h2 class="section-title">🌟 10 Ejemplos de Uso</h2>
    <div class="grammar-note"><p>A continuación, 10 ejemplos clave para dominar este tema.</p></div>
{examples_html}

{dialogue_html}

    <h2 class="section-title">📝 Ejercicios de Práctica</h2>
{exercises_html}
</div>

<script src="../js/main.js"></script>
<script>
    function playAudio(text) {{
        if ('speechSynthesis' in window) {{
            window.speechSynthesis.cancel();
            const utterance = new SpeechSynthesisUtterance(text);
            utterance.lang = 'ja-JP'; 
            utterance.rate = 0.9;     
            window.speechSynthesis.speak(utterance);
        }}
    }}
</script>
</body>
</html>'''

with open(os.path.join(base_dir, f"{lesson_id}.html"), "w", encoding="utf-8") as f:
    f.write(html)
print(f"Generated {lesson_id}.html")

print("Running add_furigana.py...")
subprocess.run("python add_furigana.py", shell=True)
print("ALL TASKS COMPLETED!")
