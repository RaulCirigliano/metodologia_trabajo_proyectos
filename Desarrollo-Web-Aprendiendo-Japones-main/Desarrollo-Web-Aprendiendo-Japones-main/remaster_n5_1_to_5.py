import os
import subprocess

# Datos para JLPT N5, Lecciones 1 a 5
data = {
    "jlpt-n5-1": {
        "id": "jlpt-n5-1",
        "dialogue": [
            ("ja-JP-NanamiNeural", "田中さん、コーヒーを飲みますか？", "¿Señor Tanaka, bebe café? (Uso de 'wo')"),
            ("ja-JP-KeitaNeural", "はい、私は毎日コーヒーを飲みます。", "Sí, en cuanto a mí, todos los días bebo café. (Uso de 'wa' y 'wo')"),
            ("ja-JP-NanamiNeural", "誰がこのケーキを作りましたか？", "¿Quién preparó este pastel? (Uso de 'ga')"),
            ("ja-JP-KeitaNeural", "私が作りました。どうぞ、食べてください。", "Yo (fui quien) lo preparé. Por favor, coma. (Uso de 'ga' enfatizando sujeto)")
        ]
    },
    "jlpt-n5-2": {
        "id": "jlpt-n5-2",
        "dialogue": [
            ("ja-JP-NanamiNeural", "週末、どこへ行きますか？", "¿Adónde vas el fin de semana? (Uso de 'he/e')"),
            ("ja-JP-KeitaNeural", "友達と東京へ行きます。", "Voy a Tokio con un amigo. (Uso de 'to' y 'he/e')"),
            ("ja-JP-NanamiNeural", "東京で何をしますか？", "¿Qué harás en Tokio? (Uso de 'de')"),
            ("ja-JP-KeitaNeural", "レストランで美味しい寿司を食べます。", "Comeré sushi delicioso en un restaurante. (Uso de 'de')")
        ]
    },
    "jlpt-n5-3": {
        "id": "jlpt-n5-3",
        "dialogue": [
            ("ja-JP-NanamiNeural", "すみません、トイレはどこですか？", "Disculpe, ¿dónde está el baño? (Uso de 'doko')"),
            ("ja-JP-KeitaNeural", "あそこです。あの人は誰ですか？", "Está allí. ¿Quién es aquella persona? (Uso de 'dare')"),
            ("ja-JP-NanamiNeural", "木村さんです。木村さんはいつ来ましたか？", "Es el señor Kimura. ¿Cuándo vino el señor Kimura? (Uso de 'itsu')"),
            ("ja-JP-KeitaNeural", "昨日来ました。何をしますか？", "Vino ayer. ¿Qué va a hacer? (Uso de 'nani')")
        ]
    },
    "jlpt-n5-4": {
        "id": "jlpt-n5-4",
        "dialogue": [
            ("ja-JP-NanamiNeural", "今、何時ですか？", "¿Qué hora es ahora?"),
            ("ja-JP-KeitaNeural", "午前１０時半です。会議はいつですか？", "Son las 10 y media de la mañana. ¿Cuándo es la reunión?"),
            ("ja-JP-NanamiNeural", "４月５日の午後２時からです。", "Es desde las 2 de la tarde del 5 de abril."),
            ("ja-JP-KeitaNeural", "わかりました。３日後に会いましょう。", "Entendido. Veámonos en tres días.")
        ]
    },
    "jlpt-n5-5": {
        "id": "jlpt-n5-5",
        "dialogue": [
            ("ja-JP-NanamiNeural", "その赤いかばんは新しいですか？", "¿Ese bolso rojo es nuevo?"),
            ("ja-JP-KeitaNeural", "はい、新しくてとても便利です。", "Sí, es nuevo y muy útil (conveniente)."),
            ("ja-JP-NanamiNeural", "いいですね。私は青いかばんが欲しいです。", "Qué bien. Yo quiero un bolso azul."),
            ("ja-JP-KeitaNeural", "あのお店は安くて有名な店ですよ。", "Aquella tienda es una tienda barata y famosa.")
        ]
    }
}

base_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\lessons"
audio_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\audio"
os.makedirs(audio_dir, exist_ok=True)

for lesson_id, d in data.items():
    print(f"--- Remastering {lesson_id} ---")
    
    html_path = os.path.join(base_dir, f"{lesson_id}.html")
    if not os.path.exists(html_path):
        print(f"File {html_path} not found. Skipping.")
        continue
        
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
        
    if "Práctica de Comprensión Auditiva" in html_content:
        print(f"{lesson_id} ya fue remasterizado. Saltando.")
        continue

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

        list_file = f"files_{lesson_id}.txt"
        with open(list_file, "w", encoding="utf-8") as f:
            for filename in files:
                f.write(f"file '{filename}'\n")

        subprocess.run(f"ffmpeg -f concat -safe 0 -i {list_file} -c copy \"{final_mp3}\" -y", shell=True)

        for filename in files:
            if os.path.exists(filename):
                os.remove(filename)
        if os.path.exists(list_file):
            os.remove(list_file)
            
    # Dialogue HTML
    dialogue_html = f"""<h2 class="section-title">🎧 Práctica de Comprensión Auditiva</h2>
<div class="grammar-note" style="background-color: #eff6ff; border-left-color: #3b82f6;">
    <p>Escucha este diálogo a velocidad natural prestando atención a la gramática de esta lección.</p>
    
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
    # Inyectar el bloque antes de "📝 Ejercicios de Práctica"
    target_string = '<h2 class="section-title">📝 Ejercicios de Práctica'
    
    if target_string in html_content:
        new_content = html_content.replace(target_string, dialogue_html + '\n' + target_string)
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Injected dialogue into {lesson_id}")
    else:
        print(f"Warning: Could not find insert target in {lesson_id}")

print("Running add_furigana.py...")
subprocess.run("python add_furigana.py", shell=True)
print("BATCH COMPLETED!")
