import os
import subprocess

# Datos para JLPT N5, Lecciones 19 a 25
data = {
    "jlpt-n5-19": {
        "id": "jlpt-n5-19",
        "dialogue": [
            ("ja-JP-NanamiNeural", "田中さん、日本へ行ったことがありますか？", "Señor Tanaka, ¿has ido a Japón alguna vez? (Experiencia con 'ta koto ga arimasu')"),
            ("ja-JP-KeitaNeural", "はい、３回行ったことがあります。去年も行きました。", "Sí, he ido tres veces. Fui el año pasado también. (Experiencia)"),
            ("ja-JP-NanamiNeural", "いいですね！日本で何をしましたか？", "¡Qué bien! ¿Qué hiciste en Japón?"),
            ("ja-JP-KeitaNeural", "温泉に入ったり、美味しい寿司を食べたりしました。", "Entré a aguas termales, comí sushi delicioso, entre otras cosas. (Acciones representativas con '~tari ~tari shimasu')"),
            ("ja-JP-NanamiNeural", "楽しそうですね。日本の温泉はどうでしたか？", "Suena divertido. ¿Qué tal estuvieron las aguas termales japonesas?"),
            ("ja-JP-KeitaNeural", "とても良かったです。毎日温泉に入ったので、体が元気になりました。", "Estuvieron muy bien. Como entré a las termas todos los días, mi cuerpo se volvió enérgico. (Cambio con 'ni naru')"),
            ("ja-JP-NanamiNeural", "うらやましいです。私もいつか行ってみたいです！", "Me da envidia. ¡Yo también quiero intentar ir algún día!")
        ]
    },
    "jlpt-n5-20": {
        "id": "jlpt-n5-20",
        "dialogue": [
            ("ja-JP-NanamiNeural", "ねえ、明日一緒にご飯食べない？", "Oye, ¿no quieres comer juntos mañana? (Estilo informal de 'tabemasen ka')"),
            ("ja-JP-KeitaNeural", "うん、いいね！何食べる？", "¡Sí, suena bien! ¿Qué comemos? (Estilo informal de 'nani o tabemasu ka')"),
            ("ja-JP-NanamiNeural", "ピザはどう？新しくできたお店に行きたいな。", "¿Qué tal pizza? Quiero ir a la tienda que se acaba de abrir. (Informal)"),
            ("ja-JP-KeitaNeural", "ごめん、昨日の夜ピザ食べたんだ。カレーは？", "Perdón, anoche comí pizza. ¿Y curry? (Informal de 'tabemashita')"),
            ("ja-JP-NanamiNeural", "カレーか。うん、わかった。美味しいお店、知ってる？", "Curry, eh. Sí, entiendo. ¿Conoces alguna tienda deliciosa? (Informal de 'shitte imasu ka')"),
            ("ja-JP-KeitaNeural", "うん、駅の近くにあるよ。すごく安いし、美味しいよ。", "Sí, hay una cerca de la estación. Es muy barata y además deliciosa. (Informal de 'arimasu')"),
            ("ja-JP-NanamiNeural", "じゃあ、そこにしよう！明日１２時に駅でね。", "¡Entonces decidamos por esa! Mañana a las 12 en la estación. (Informal de 'ni shimashou')")
        ]
    },
    "jlpt-n5-21": {
        "id": "jlpt-n5-21",
        "dialogue": [
            ("ja-JP-NanamiNeural", "田中さんは、明日の天気はどうなると思いますか？", "Señor Tanaka, ¿cómo crees que estará el clima de mañana? (Pensamiento 'to omoimasu')"),
            ("ja-JP-KeitaNeural", "ニュースで、明日は一日中雨が降ると言っていました。", "En las noticias dijeron que mañana lloverá todo el día. (Cita 'to itte imashita')"),
            ("ja-JP-NanamiNeural", "えっ、本当ですか。私は晴れると思っていました。", "¿Eh, de verdad? Yo pensaba que se iba a despejar. (Pensamiento en pasado)"),
            ("ja-JP-KeitaNeural", "残念ですね。明日のピクニックはどうしますか？", "Qué lástima. ¿Qué haremos con el picnic de mañana?"),
            ("ja-JP-NanamiNeural", "山田さんに電話して、「ピクニックは来週にしましょう」と言います。", "Llamaré al señor Yamada y le diré: 'Dejemos el picnic para la próxima semana'. (Cita directa)"),
            ("ja-JP-KeitaNeural", "それがいいと思います。雨の中でピクニックは無理ですから。", "Creo que eso es lo mejor. Porque un picnic en la lluvia es imposible. (Pensamiento)"),
            ("ja-JP-NanamiNeural", "そうですね。山田さんも賛成すると思います。", "Es cierto. Creo que el señor Yamada también estará de acuerdo.")
        ]
    },
    "jlpt-n5-22": {
        "id": "jlpt-n5-22",
        "dialogue": [
            ("ja-JP-NanamiNeural", "あの背が高くて、黒い服を着ている人は誰ですか？", "¿Quién es esa persona que es alta y lleva ropa negra? (Modificadores largos)"),
            ("ja-JP-KeitaNeural", "あ、あの人は私が昨日パーティーで会った人です。", "Ah, esa persona es la persona que conocí ayer en la fiesta. (Modificador de sustantivo con verbo)"),
            ("ja-JP-NanamiNeural", "そうですか。どんな人ですか？", "Ya veo. ¿Qué tipo de persona es?"),
            ("ja-JP-KeitaNeural", "英語を教える先生で、とても面白い人ですよ。", "Es un profesor que enseña inglés, y es una persona muy interesante. (Modificador con verbo)"),
            ("ja-JP-NanamiNeural", "いいですね。彼が読んでいる本は難しそうですね。", "Qué bien. El libro que él está leyendo parece difícil. (Modificador con verbo)"),
            ("ja-JP-KeitaNeural", "あれは彼が書いた本です！彼は有名な作家でもあります。", "¡Ese es el libro que él escribió! Él también es un autor famoso. (Modificador con verbo pasado)"),
            ("ja-JP-NanamiNeural", "ええっ！先生が書いた本ですか。すごいですね。", "¡Eeeh! ¿Es el libro que escribió el profesor? Es increíble.")
        ]
    },
    "jlpt-n5-23": {
        "id": "jlpt-n5-23",
        "dialogue": [
            ("ja-JP-NanamiNeural", "田中さん、この機械の使い方がわかりません。どうすればいいですか？", "Señor Tanaka, no entiendo cómo usar esta máquina. ¿Qué debo hacer?"),
            ("ja-JP-KeitaNeural", "ああ、それは簡単ですよ。この赤いボタンを押すと、動きます。", "Ah, eso es fácil. Cuando presionas (si presionas) este botón rojo, se mueve. (Condicional 'to')"),
            ("ja-JP-NanamiNeural", "なるほど。止める時はどうしますか？", "Ya veo. ¿Y qué hago al momento de detenerlo? (Condición temporal 'toki')"),
            ("ja-JP-KeitaNeural", "止める時は、あの青いレバーを引いてください。", "Cuando lo detengas, por favor tira de esa palanca azul. (Temporal 'toki')"),
            ("ja-JP-NanamiNeural", "わかりました。もし壊れた時は、誰に言えばいいですか？", "Entendido. Si se rompe (en el momento que se rompa), ¿a quién debo decirle? (Condición con 'moshi' y 'toki')"),
            ("ja-JP-KeitaNeural", "機械が動かない時や、変な音がする時は、私を呼んでください。", "Cuando la máquina no se mueva o cuando haga un sonido raro, llámame a mí. (Temporal)"),
            ("ja-JP-NanamiNeural", "はい、安心しました。ありがとうございます！", "Sí, me siento aliviada. ¡Muchas gracias!")
        ]
    },
    "jlpt-n5-24": {
        "id": "jlpt-n5-24",
        "dialogue": [
            ("ja-JP-NanamiNeural", "この辞書はとても便利ですね。自分で買いましたか？", "Este diccionario es muy útil. ¿Lo compró usted mismo?"),
            ("ja-JP-KeitaNeural", "いいえ、日本語の先生が私に貸してくれました。", "No, mi profesor de japonés me lo prestó (hizo el favor de prestarme). (Uso de 'te kureru')"),
            ("ja-JP-NanamiNeural", "いい先生ですね。田中さんは先生に何かしてあげましたか？", "Es un buen profesor. ¿Y usted hizo algo por el profesor? (Uso de 'te ageru')"),
            ("ja-JP-KeitaNeural", "はい、私は先生の荷物を持ってあげました。", "Sí, yo le llevé (hice el favor de llevarle) el equipaje al profesor. (Uso de 'te ageru')"),
            ("ja-JP-NanamiNeural", "それは親切ですね。私も昨日、友達に自転車を直してもらいました。", "Eso es muy amable. A mí también ayer un amigo me reparó la bicicleta. (Uso de 'te morau')"),
            ("ja-JP-KeitaNeural", "よかったですね。友達に何かお礼をしてあげましたか？", "Qué bueno. ¿Le hizo algún favor de agradecimiento a su amigo?"),
            ("ja-JP-NanamiNeural", "はい、美味しいケーキを作ってあげました。", "Sí, le preparé un pastel delicioso. (Uso de 'te ageru')")
        ]
    },
    "jlpt-n5-25": {
        "id": "jlpt-n5-25",
        "dialogue": [
            ("ja-JP-NanamiNeural", "田中さん、明日の日曜日、海へ行きますか？", "Señor Tanaka, ¿irá al mar mañana domingo?"),
            ("ja-JP-KeitaNeural", "そうですね。もし明日天気が良かったら、海へ行きます。", "Déjame ver. Si mañana hace buen clima, iré al mar. (Condicional 'tara')"),
            ("ja-JP-NanamiNeural", "もし雨が降ったら、どうしますか？", "¿Y si llueve, qué hará? (Condicional 'tara')"),
            ("ja-JP-KeitaNeural", "雨が降ったら、家で映画を見ます。", "Si llueve, veré películas en casa. (Condicional 'tara')"),
            ("ja-JP-NanamiNeural", "私は明日、いくら雨が降っても、買い物に行かなければなりません。", "Yo, por mucho que llueva mañana, tengo que ir de compras. (Condicional concesivo 'te mo')"),
            ("ja-JP-KeitaNeural", "ええ？雨が降っても行くんですか？大変ですね。", "¿Eh? ¿Irá incluso si llueve? Qué terrible. (Concesivo 'te mo')"),
            ("ja-JP-NanamiNeural", "はい、友達の誕生日プレゼントを買いたいですから。お金がなくても、カードで買います！", "Sí, porque quiero comprar el regalo de cumpleaños de un amigo. ¡Incluso si no tengo dinero, lo compraré con tarjeta! (Concesivo negativo 'nakutemo')")
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
        continue
        
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
        
    if "Práctica de Comprensión Auditiva" in html_content:
        print(f"{lesson_id} ya fue remasterizado. Saltando.")
        continue

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
    target_string = '<h2 class="section-title">📝 Ejercicios de Práctica'
    if target_string in html_content:
        new_content = html_content.replace(target_string, dialogue_html + '\n' + target_string)
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(new_content)

print("Running add_furigana.py...")
subprocess.run("python add_furigana.py", shell=True)
print("BATCH COMPLETED!")
