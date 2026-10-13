import os
import subprocess

# Datos para JLPT N5, Lecciones 11 a 18
data = {
    "jlpt-n5-11": {
        "id": "jlpt-n5-11",
        "dialogue": [
            ("ja-JP-NanamiNeural", "田中さん、昨日りんごを何個買いましたか？", "¿Señor Tanaka, cuántas manzanas compró ayer? (Contadores)"),
            ("ja-JP-KeitaNeural", "りんごを３個買いました。そして、みかんも買いました。", "Compré tres manzanas. Y también compré mandarinas. (Uso de 'mo')"),
            ("ja-JP-NanamiNeural", "みかんはいくつ買いましたか？", "¿Cuántas mandarinas compró?"),
            ("ja-JP-KeitaNeural", "５つ買いました。山田さんも果物を買いましたか？", "Compré cinco. ¿El señor Yamada también compró frutas? (Uso de 'mo')"),
            ("ja-JP-NanamiNeural", "いいえ、私は何も買いませんでした。高かったですから。", "No, yo no compré nada. Porque estaban caras. (Nada - 'nani mo')"),
            ("ja-JP-KeitaNeural", "そうですか。じゃあ、りんごを１個あげますよ。", "Ya veo. Entonces, le daré una manzana. (Contador)"),
            ("ja-JP-NanamiNeural", "本当ですか？ありがとうございます！", "¿De verdad? ¡Muchas gracias!")
        ]
    },
    "jlpt-n5-12": {
        "id": "jlpt-n5-12",
        "dialogue": [
            ("ja-JP-NanamiNeural", "東京と大阪と、どちらが好きですか？", "Entre Tokio y Osaka, ¿cuál te gusta más? (Comparación)"),
            ("ja-JP-KeitaNeural", "私は大阪のほうが好きです。", "A mí me gusta más Osaka. (Uso de 'hou ga')"),
            ("ja-JP-NanamiNeural", "どうしてですか？東京より大阪のほうが楽しいですか？", "¿Por qué? ¿Osaka es más divertido que Tokio? (Uso de 'yori')"),
            ("ja-JP-KeitaNeural", "はい、大阪のほうが東京より人が親切だと思います。", "Sí, creo que la gente de Osaka es más amable que la de Tokio."),
            ("ja-JP-NanamiNeural", "そうですか。日本の食べ物の中で、何が一番好きですか？", "Ya veo. Entre las comidas de Japón, ¿qué es lo que más te gusta? (Uso de 'ichiban')"),
            ("ja-JP-KeitaNeural", "寿司が一番好きです。でも、たこ焼きも美味しいですね。", "El sushi es lo que más me gusta. Pero los takoyaki también son deliciosos."),
            ("ja-JP-NanamiNeural", "たこ焼きは大阪が一番美味しいですよ！", "¡Los takoyaki de Osaka son los más deliciosos! (Uso de 'ichiban')")
        ]
    },
    "jlpt-n5-13": {
        "id": "jlpt-n5-13",
        "dialogue": [
            ("ja-JP-NanamiNeural", "田中さんは、今何が一番欲しいですか？", "Señor Tanaka, ¿qué es lo que más desea ahora mismo? (Uso de 'hoshii')"),
            ("ja-JP-KeitaNeural", "私は新しい車が欲しいです。今の車は古いですから。", "Yo quiero un auto nuevo. Porque el auto actual es viejo."),
            ("ja-JP-NanamiNeural", "そうですか。週末、どこかへ行きたいですか？", "Ya veo. ¿Le gustaría ir a algún lugar el fin de semana? (Uso de '~tai')"),
            ("ja-JP-KeitaNeural", "はい、海へ行きたいです。海で泳ぎたいです。", "Sí, quiero ir al mar. Quiero nadar en el mar. (Uso de '~tai')"),
            ("ja-JP-NanamiNeural", "海ですか、いいですね。私は山へ行きたいです。", "Al mar, qué bien. Yo quiero ir a la montaña. (Uso de '~tai')"),
            ("ja-JP-KeitaNeural", "じゃあ、来月一緒に山へ写真を撮りに行きませんか？", "Entonces, ¿no le gustaría que vayamos juntos a la montaña a tomar fotos el mes que viene? (Propósito + ir)"),
            ("ja-JP-NanamiNeural", "はい、ぜひ行きたいです！", "¡Sí, por supuesto que quiero ir!")
        ]
    },
    "jlpt-n5-14": {
        "id": "jlpt-n5-14",
        "dialogue": [
            ("ja-JP-NanamiNeural", "もしもし、田中さん。今、何をしていますか？", "Aló, señor Tanaka. ¿Qué está haciendo ahora? (Progresivo '~te imasu')"),
            ("ja-JP-KeitaNeural", "今、公園を散歩しています。山田さんは？", "Ahora estoy paseando por el parque. ¿Y usted, señor Yamada? (Progresivo)"),
            ("ja-JP-NanamiNeural", "私は家でテレビを見ています。外は雨が降っていますか？", "Yo estoy en casa viendo la televisión. ¿Está lloviendo afuera? (Progresivo)"),
            ("ja-JP-KeitaNeural", "いいえ、雨は降っていません。とてもいい天気ですよ。", "No, no está lloviendo. Hace muy buen clima. (Progresivo negativo)"),
            ("ja-JP-NanamiNeural", "そうですか。あ、あの道を走っている人は誰ですか？", "Ya veo. Ah, ¿quién es esa persona que está corriendo por ese camino? (Modificador progresivo)"),
            ("ja-JP-KeitaNeural", "あれは木村さんです。毎日あそこを走っていますよ。", "Ese es el señor Kimura. Todos los días corre por ahí. (Hábito con progresivo)"),
            ("ja-JP-NanamiNeural", "元気ですね。私も明日から走りましょう！", "Qué enérgico. ¡Yo también correré a partir de mañana!")
        ]
    },
    "jlpt-n5-15": {
        "id": "jlpt-n5-15",
        "dialogue": [
            ("ja-JP-NanamiNeural", "すみません、ここで写真を撮ってもいいですか？", "Disculpe, ¿puedo tomar fotos aquí? (Permiso '~te mo ii desu ka')"),
            ("ja-JP-KeitaNeural", "いいえ、ここでは写真を撮ってはいけません。", "No, aquí no se debe tomar fotos. (Prohibición '~te wa ikemasen')"),
            ("ja-JP-NanamiNeural", "あ、そうですか。わかりました。このパンフレットをもらってもいいですか？", "Ah, ya veo. Entendido. ¿Puedo llevarme este folleto? (Permiso)"),
            ("ja-JP-KeitaNeural", "はい、どうぞ。パンフレットは持って帰ってもいいですよ。", "Sí, adelante. Puede llevarse el folleto a casa. (Concesión)"),
            ("ja-JP-NanamiNeural", "ありがとうございます。あそこに座ってもいいですか？", "Muchas gracias. ¿Puedo sentarme allí? (Permiso)"),
            ("ja-JP-KeitaNeural", "あそこはスタッフの席ですから、座ってはいけません。こちらの椅子をどうぞ。", "Ese es el asiento del personal, así que no debe sentarse. Por favor use esta silla de aquí. (Prohibición)"),
            ("ja-JP-NanamiNeural", "いろいろすみません。気をつけます。", "Disculpe tantas molestias. Tendré cuidado.")
        ]
    },
    "jlpt-n5-16": {
        "id": "jlpt-n5-16",
        "dialogue": [
            ("ja-JP-NanamiNeural", "田中さん、昨日の休日は何をしましたか？", "Señor Tanaka, ¿qué hizo en su día libre ayer?"),
            ("ja-JP-KeitaNeural", "昨日は、朝ご飯を食べて、新聞を読んで、それから散歩をしました。", "Ayer, desayuné, leí el periódico y luego di un paseo. (Secuencia de acciones en forma TE)"),
            ("ja-JP-NanamiNeural", "いいですね。私はデパートへ行って、服を買って、映画を見ました。", "Qué bien. Yo fui a los grandes almacenes, compré ropa y vi una película. (Secuencia de acciones)"),
            ("ja-JP-KeitaNeural", "どんな服を買いましたか？", "¿Qué tipo de ropa compró?"),
            ("ja-JP-NanamiNeural", "青くて、安くて、とても可愛い服です。", "Es una ropa azul, barata y muy linda. (Adjetivos i y na en forma TE)"),
            ("ja-JP-KeitaNeural", "デパートのレストランで食事もしましたか？", "¿También comió en el restaurante de los grandes almacenes?"),
            ("ja-JP-NanamiNeural", "はい、高くて美味しくないレストランでした...", "Sí, fue un restaurante caro y nada delicioso... (Adjetivos en forma TE)")
        ]
    },
    "jlpt-n5-17": {
        "id": "jlpt-n5-17",
        "dialogue": [
            ("ja-JP-NanamiNeural", "山田さん、明日は大切な会議がありますから、絶対に遅れないでください。", "Señor Yamada, mañana hay una reunión importante, así que por favor no llegue tarde sin falta. (Forma NAI + de kudasai)"),
            ("ja-JP-KeitaNeural", "はい、わかりました。何時に来なければなりませんか？", "Sí, entendido. ¿A qué hora tengo que venir? (Obligación '~nakereba narimasen')"),
            ("ja-JP-NanamiNeural", "午前９時までに来なければなりません。資料も忘れないでくださいね。", "Tiene que venir antes de las 9:00 AM. Tampoco olvide los documentos, por favor. (Obligación y Petición negativa)"),
            ("ja-JP-KeitaNeural", "資料は今日作らなければなりませんか？", "¿Tengo que preparar los documentos hoy? (Obligación)"),
            ("ja-JP-NanamiNeural", "いいえ、今日作らなくてもいいですよ。明日一緒に作りましょう。", "No, no es necesario que los prepare hoy. Hagámoslo juntos mañana. (Ausencia de obligación '~nakutemo ii desu')"),
            ("ja-JP-KeitaNeural", "本当ですか？じゃあ、今日は早く帰ってもいいですか？", "¿De verdad? Entonces, ¿puedo irme a casa temprano hoy?"),
            ("ja-JP-NanamiNeural", "はい、心配しないで早く帰ってください。", "Sí, no se preocupe y regrese a casa temprano. (Forma NAI + de)")
        ]
    },
    "jlpt-n5-18": {
        "id": "jlpt-n5-18",
        "dialogue": [
            ("ja-JP-NanamiNeural", "田中さんは、ピアノを弾くことができますか？", "Señor Tanaka, ¿usted puede (sabe) tocar el piano? (Habilidad '~koto ga dekimasu')"),
            ("ja-JP-KeitaNeural", "いいえ、ピアノを弾くことはできません。でも、ギターを弾くことができます。", "No, no puedo tocar el piano. Pero puedo tocar la guitarra. (Habilidad)"),
            ("ja-JP-NanamiNeural", "すごいですね！趣味は何ですか？", "¡Qué increíble! ¿Cuál es su pasatiempo?"),
            ("ja-JP-KeitaNeural", "私の趣味は、古い音楽を聞くことと、歌を歌うことです。", "Mi pasatiempo es escuchar música antigua y cantar canciones. (Nominalización con 'koto')"),
            ("ja-JP-NanamiNeural", "私も歌うことが好きです。今度一緒にカラオケへ行きませんか？", "A mí también me gusta cantar. ¿Vamos juntos al karaoke la próxima vez?"),
            ("ja-JP-KeitaNeural", "いいですね！あ、カラオケに行く前に、銀行でお金をおろさなければなりません。", "¡Qué bien! Ah, antes de ir al karaoke, tengo que sacar dinero en el banco. (Antes de ~ 'mae ni')"),
            ("ja-JP-NanamiNeural", "じゃあ、明日銀行へ行く前に会いましょう。", "Entonces, veámonos mañana antes de que vaya al banco. (Antes de ~)")
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
            
    # Dialogue HTML with lines
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
