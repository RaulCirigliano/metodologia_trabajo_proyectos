import os
import subprocess

# Datos para JLPT N5, Lecciones 6 a 10 con diálogos mucho más largos y completos
data = {
    "jlpt-n5-6": {
        "id": "jlpt-n5-6",
        "dialogue": [
            ("ja-JP-NanamiNeural", "田中さん、昨日の夜、晩ご飯を食べましたか？", "¿Señor Tanaka, anoche comió la cena? (Pasado afirmativo)"),
            ("ja-JP-KeitaNeural", "いいえ、昨日はとても忙しかったので、食べませんでした。", "No, como ayer estuve muy ocupado, no comí. (Pasado negativo)"),
            ("ja-JP-NanamiNeural", "ええっ、それは大変ですね。じゃあ、今日の朝ごはんは食べましたか？", "¡Eh! Eso es terrible. Entonces, ¿desayunó hoy? (Pasado)"),
            ("ja-JP-KeitaNeural", "はい、今朝はパンと卵を食べました。牛乳も飲みました。", "Sí, esta mañana comí pan y huevos. También bebí leche. (Pasado afirmativo)"),
            ("ja-JP-NanamiNeural", "よかったです。毎日ちゃんと食べないとだめですよ。夜は何を食べますか？", "Qué bien. Si no comes bien todos los días, será malo. ¿Qué comerá en la noche? (Presente/Futuro)"),
            ("ja-JP-KeitaNeural", "今日は早く帰るので、家でカレーを作ります。そして、たくさん食べます！", "Como hoy volveré temprano, prepararé curry en casa. ¡Y comeré mucho! (Presente/Futuro)"),
            ("ja-JP-NanamiNeural", "いいですね！私はカレーを作りませんが、レストランで食べます。", "¡Qué bien! Yo no preparo curry, pero lo comeré en un restaurante. (Presente negativo y afirmativo)")
        ]
    },
    "jlpt-n5-7": {
        "id": "jlpt-n5-7",
        "dialogue": [
            ("ja-JP-NanamiNeural", "すみません、この近くにコンビニがありますか？", "Disculpe, ¿hay alguna tienda de conveniencia cerca de aquí? (Existencia de cosas inanimadas)"),
            ("ja-JP-KeitaNeural", "はい、ありますよ。あの交差点の右にあります。", "Sí, sí hay. Está a la derecha de aquella intersección. (Posición)"),
            ("ja-JP-NanamiNeural", "ありがとうございます。あ、ポストはどこにありますか？", "Muchas gracias. Ah, ¿y dónde hay un buzón de correo? (Ubicación)"),
            ("ja-JP-KeitaNeural", "ポストはコンビニの前にあります。そして、コンビニの中にATMもありますよ。", "El buzón está enfrente de la tienda. Y dentro de la tienda también hay un cajero automático. (Posiciones múltiples)"),
            ("ja-JP-NanamiNeural", "助かりました。ところで、この辺りに猫がいますか？", "Me ha salvado. Por cierto, ¿hay gatos por esta zona? (Existencia de seres vivos)"),
            ("ja-JP-KeitaNeural", "ええ、公園の中に猫がたくさんいますよ。犬もいます。", "Sí, dentro del parque hay muchos gatos. También hay perros. (Seres vivos en ubicación)"),
            ("ja-JP-NanamiNeural", "そうですか。私の家にはペットがいませんから、公園に見に行きます。", "Ya veo. Como en mi casa no hay mascotas, iré al parque a verlos. (Existencia negativa)")
        ]
    },
    "jlpt-n5-8": {
        "id": "jlpt-n5-8",
        "dialogue": [
            ("ja-JP-NanamiNeural", "素敵な時計ですね！自分で買いましたか？", "¡Qué reloj tan bonito! ¿Lo compró usted mismo?"),
            ("ja-JP-KeitaNeural", "いいえ、これは誕生日に父がくれました。", "No, este me lo dio mi padre en mi cumpleaños. (Uso de 'kureru' - alguien me da a mí)"),
            ("ja-JP-NanamiNeural", "そうですか、いいお父さんですね。田中さんはお父さんに何をあげましたか？", "Ya veo, es un buen padre. ¿Y qué le dio usted a su padre? (Uso de 'ageru' - yo doy a alguien)"),
            ("ja-JP-KeitaNeural", "私は父の誕生日に新しいネクタイをあげました。", "Yo le di una corbata nueva en su cumpleaños. (Ageru)"),
            ("ja-JP-NanamiNeural", "素晴らしいですね。あ、その本は図書館で借りましたか？", "Qué maravilloso. Ah, ¿ese libro lo tomó prestado de la biblioteca?"),
            ("ja-JP-KeitaNeural", "いいえ、昨日、友達にもらいました。とても面白いですよ。", "No, ayer lo recibí (me lo dio) un amigo. Es muy interesante. (Uso de 'morau' - recibir de alguien)"),
            ("ja-JP-NanamiNeural", "じゃあ、読み終わったら、私に貸してください！", "Entonces, cuando termines de leerlo, ¡préstamelo a mí!")
        ]
    },
    "jlpt-n5-9": {
        "id": "jlpt-n5-9",
        "dialogue": [
            ("ja-JP-NanamiNeural", "田中さん、今週末は暇ですか？一緒に映画を見に行きませんか？", "Señor Tanaka, ¿está libre este fin de semana? ¿No le gustaría ir a ver una película juntos? (Invitación con ~masenka)"),
            ("ja-JP-KeitaNeural", "いいですね、行きましょう！何の映画を見ますか？", "¡Qué bien, vayamos! ¿Qué película veremos? (Sugerencia/Aceptación con ~mashou)"),
            ("ja-JP-NanamiNeural", "新しいアクション映画はどうですか？土曜日の午後２時に会いましょう。", "¿Qué le parece la nueva película de acción? Reunámonos a las 2 de la tarde del sábado. (Sugerencia con ~mashou)"),
            ("ja-JP-KeitaNeural", "うーん、土曜日はちょっと予定があります。日曜日に行きませんか？", "Mmm, el sábado tengo un pequeño compromiso. ¿Por qué no vamos el domingo? (Contra-invitación con ~masenka)"),
            ("ja-JP-NanamiNeural", "日曜日ですね。大丈夫です。じゃあ、映画の前に一緒にお昼ご飯を食べましょう。", "Domingo, ¿verdad? Está bien. Entonces, almorcemos juntos antes de la película. (~mashou)"),
            ("ja-JP-KeitaNeural", "賛成です！駅の前のレストランで食べましょうか？", "¡Estoy de acuerdo! ¿Deberíamos comer en el restaurante frente a la estación? (Ofrecimiento con ~mashouka)"),
            ("ja-JP-NanamiNeural", "ええ、そうしましょう。楽しみにしています！", "Sí, hagamos eso. ¡Lo espero con ansias!")
        ]
    },
    "jlpt-n5-10": {
        "id": "jlpt-n5-10",
        "dialogue": [
            ("ja-JP-NanamiNeural", "昨日は雨が降りましたね。だから、私は一日中家にいました。", "Ayer llovió, ¿verdad? Por eso, me quedé en casa todo el día. (Uso de 'dakara')"),
            ("ja-JP-KeitaNeural", "私もです。本を読みました。そして、音楽も聞きました。", "Yo también. Leí un libro. Y además, escuché música. (Uso de 'soshite')"),
            ("ja-JP-NanamiNeural", "いいですね。私は掃除をしました。でも、勉強はしませんでした。", "Qué bien. Yo limpié. Pero, no estudié. (Uso de 'demo')"),
            ("ja-JP-KeitaNeural", "ええ？明日テストがありますよ。だから、今から勉強した方がいいですよ。", "¿Eh? Mañana hay examen. Por eso, es mejor que estudies desde ahora. (Uso de 'dakara')"),
            ("ja-JP-NanamiNeural", "はい、わかっています。今日は疲れていますが、夜少し勉強します。", "Sí, lo sé. Hoy estoy cansada, pero, estudiaré un poco en la noche. (Uso de partícula 'ga' como pero)"),
            ("ja-JP-KeitaNeural", "頑張ってください。私はたくさん勉強しましたから、今日は早く寝ます。", "Esfuérzate. Como yo estudié mucho (porque estudié), hoy me dormiré temprano. (Uso de 'kara')"),
            ("ja-JP-NanamiNeural", "ずるいですね！じゃあ、また明日、学校で会いましょう。", "¡Qué tramposo! Bueno, nos vemos mañana en la escuela. (Uso de 'jaa')")
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
    <p>Escucha este diálogo a velocidad natural prestando atención a cómo se aplican todas las reglas y variaciones de esta lección en una conversación real.</p>
    
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
        dialogue_html += f'            <div style="border-bottom: 1px solid #f1f5f9; padding-bottom: 0.5rem;"><div class="text-jp">{text_jp}</div><div class="text-es" style="color:#64748b; margin-top:0.3rem;">{text_es}</div></div>\n'
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
