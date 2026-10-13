import os
import shutil
import subprocess

dialogues = {
    5: {
        "title": "~て おきます (Preparación previa)",
        "lines": [
            ("ja-JP-NanamiNeural", "佐藤さん、明日の会議の準備はどうですか。", "Sato, ¿cómo van los preparativos para la reunión de mañana?"),
            ("ja-JP-KeitaNeural", "はい、もう資料はコピーしておきました。", "Sí, ya he dejado copiados los documentos."),
            ("ja-JP-NanamiNeural", "ありがとうございます。パソコンとプロジェクターも使いますから、準備しておいてください。", "Gracias. Como también usaremos computadora y proyector, por favor déjalos preparados."),
            ("ja-JP-KeitaNeural", "わかりました。会議室に運んでおきます。", "Entendido. Los llevaré (y los dejaré listos) en la sala de reuniones."),
            ("ja-JP-NanamiNeural", "あと、お茶も買っておきましょうか。", "Además, ¿compramos (y dejamos preparado) té?"),
            ("ja-JP-KeitaNeural", "いいえ、お茶は私が朝買っておきましたから、大丈夫です。", "No, el té ya lo dejé comprado yo esta mañana, así que está bien."),
            ("ja-JP-NanamiNeural", "準備がいいですね。会議が終わったら、資料はどうしますか。", "Qué bien preparado está todo. Cuando termine la reunión, ¿qué hacemos con los documentos?"),
            ("ja-JP-KeitaNeural", "私が捨てておきますから、そのままにしておいてください。", "Yo los tiraré, así que por favor déjalos tal cual están.")
        ]
    },
    6: {
        "title": "~つもりです / ~予定です (Voluntad e Intención)",
        "lines": [
            ("ja-JP-NanamiNeural", "たけしさんは、夏休みにどこかへ行く予定ですか。", "Takeshi, ¿tienes programado ir a algún sitio en las vacaciones de verano?"),
            ("ja-JP-KeitaNeural", "はい、今年は北海道へ旅行する予定です。", "Sí, este año tengo programado hacer un viaje a Hokkaido."),
            ("ja-JP-NanamiNeural", "いいですね！北海道で何をするつもりですか。", "¡Qué bien! ¿Qué tienes intención de hacer en Hokkaido?"),
            ("ja-JP-KeitaNeural", "車を借りて、いろいろな町を運転するつもりです。", "Tengo intención de alquilar un coche y conducir por varios pueblos."),
            ("ja-JP-NanamiNeural", "美味しいものもたくさん食べるつもりですか。", "¿También tienes intención de comer muchas cosas ricas?"),
            ("ja-JP-KeitaNeural", "もちろんです。カニやラーメンをたくさん食べようと思っています。", "Por supuesto. Estoy pensando en comer mucho cangrejo y ramen."),
            ("ja-JP-NanamiNeural", "羨ましいです。私はお金がないので、どこも行かないつもりです。", "Qué envidia. Como no tengo dinero, no tengo intención de ir a ninguna parte."),
            ("ja-JP-KeitaNeural", "そうですか。じゃあ、北海道のお土産を買ってくる予定ですから、待っていてくださいね。", "¿Ah sí? Bueno, tengo planeado traer recuerdos de Hokkaido, así que espéralos.")
        ]
    },
    7: {
        "title": "~たほうがいいです / ~かもしれません (Consejos y Probabilidad)",
        "lines": [
            ("ja-JP-NanamiNeural", "先生、昨日から喉が痛くて、咳が出るんです。", "Doctor, desde ayer me duele la garganta y tengo tos."),
            ("ja-JP-KeitaNeural", "熱もありますね。風邪かもしれません。今日はシャワーを浴びないほうがいいですよ。", "También tienes fiebre. Tal vez sea un resfriado. Es mejor que no te des una ducha hoy."),
            ("ja-JP-NanamiNeural", "わかりました。明日から仕事に行ってもいいですか。", "Entendido. ¿Puedo ir a trabajar a partir de mañana?"),
            ("ja-JP-KeitaNeural", "いや、他の人にうつるかもしれませんから、会社を休んだほうがいいです。", "No, tal vez contagies a otras personas, así que es mejor que faltes al trabajo."),
            ("ja-JP-NanamiNeural", "ええっ、でも明日は大切な会議があるんです。", "Ah... pero mañana tengo una reunión importante."),
            ("ja-JP-KeitaNeural", "無理をすると、もっと悪くなるでしょう。この薬を飲んで、早く寝たほうがいいですよ。", "Si te exiges demasiado, seguramente empeorará. Es mejor que tomes esta medicina y te acuestes pronto."),
            ("ja-JP-NanamiNeural", "はい、そうします。治るでしょうか。", "Sí, lo haré. ¿Seguro que me curaré?"),
            ("ja-JP-KeitaNeural", "薬を飲めば、すぐによくなるでしょう。心配しないでください。", "Si tomas la medicina, seguramente mejorarás pronto. No te preocupes.")
        ]
    },
    8: {
        "title": "Imperativo, Prohibición y Citas Directas",
        "lines": [
            ("ja-JP-KeitaNeural", "鈴木さん、あそこの機械に「触るな」と書いてありますよ！", "Suzuki, ¡en aquella máquina está escrito 'No tocar'!"),
            ("ja-JP-NanamiNeural", "あっ、すみません。危ないという意味ですか。", "Ah, disculpe. ¿Significa que es peligroso?"),
            ("ja-JP-KeitaNeural", "そうです。故障中だから、絶対に使うなと言っていましたよ。", "Exacto. Como está averiada, estaban diciendo que definitivamente no la uses."),
            ("ja-JP-NanamiNeural", "わかりました。あっちのドアには「立入禁止」と書いてあります。", "Entendido. En la puerta de allí está escrito 'Prohibido el paso' (Tachi-iri kinshi)."),
            ("ja-JP-KeitaNeural", "それは「ここに入るな」という意味です。", "Eso significa 'No entres aquí'."),
            ("ja-JP-NanamiNeural", "日本語の漢字は難しいですね。もっと注意して見ます。", "Los kanjis japoneses son difíciles. Estaré más atenta al mirar."),
            ("ja-JP-KeitaNeural", "今、部長が「すぐに事務所へ来い」と言っていました。", "Ahora mismo, el jefe de departamento estaba diciendo 'Ven a la oficina de inmediato'."),
            ("ja-JP-NanamiNeural", "ええっ、怒られるかもしれません...。急いで行きます！", "Eh... tal vez me regañen. ¡Voy de prisa!")
        ]
    },
    9: {
        "title": "~とおりに / ~あとで / ~ないで (Secuencias Temporales)",
        "lines": [
            ("ja-JP-NanamiNeural", "あなた、この新しい棚を組み立ててくれませんか。", "Cariño, ¿puedes montarme esta nueva estantería?"),
            ("ja-JP-KeitaNeural", "わかった。説明書のとおりに作ればいいんだね。", "Entendido. Solo tengo que hacerla exactamente como indica el manual, ¿verdad?"),
            ("ja-JP-NanamiNeural", "ええ。でも、その前に晩ごはんを食べましょう。食べたあとで、組み立ててください。", "Sí. Pero antes de eso, cenemos. Después de haber comido, móntala, por favor."),
            ("ja-JP-KeitaNeural", "いや、ごはんを食べないで、先にこれを作ってしまうよ。", "No, voy a terminar de construirla primero SIN cenar."),
            ("ja-JP-NanamiNeural", "そう？じゃあ、私が言うとおりに、部品を並べてね。", "¿Ah, sí? Entonces, alinea las piezas tal y como yo te diga."),
            ("ja-JP-KeitaNeural", "案外難しいな...。あっ、間違えた！", "Es más difícil de lo que pensaba... ¡Ay, me he equivocado!"),
            ("ja-JP-NanamiNeural", "だから、説明書をよく読んだあとで、始めてと言ったのに。", "Por eso te dije que empezaras después de haber leído bien el manual..."),
            ("ja-JP-KeitaNeural", "ごめんごめん。次は間違えないで作るよ。", "Perdón, perdón. La próxima vez la haré SIN equivocarme.")
        ]
    },
    10: {
        "title": "Condicional (~ば)",
        "lines": [
            ("ja-JP-NanamiNeural", "けんじさん、日本語が上手になりたいんですが、どうすればいいですか。", "Kenji, quiero mejorar en japonés. ¿Qué debería hacer?"),
            ("ja-JP-KeitaNeural", "毎日、日本人の友達と話せば、上手になりますよ。", "Si hablas con amigos japoneses todos los días, mejorarás."),
            ("ja-JP-NanamiNeural", "でも、私には日本人の友達がいません。", "Pero yo no tengo amigos japoneses."),
            ("ja-JP-KeitaNeural", "もし友達がいなければ、日本のドラマを見るのがいいですよ。", "Si no tienes amigos, es bueno ver dramas japoneses."),
            ("ja-JP-NanamiNeural", "ドラマを見れば、本当に上手になりますか。", "Si veo dramas, ¿de verdad mejoraré?"),
            ("ja-JP-KeitaNeural", "はい。わからない言葉があれば、辞書で調べてください。", "Sí. Si hay alguna palabra que no entiendas, búscala en el diccionario."),
            ("ja-JP-NanamiNeural", "漢字もたくさん覚えなければなりませんか。", "¿También tengo que memorizar muchos kanjis?"),
            ("ja-JP-KeitaNeural", "時間がなければ、少しずつでもいいですよ。頑張れば、必ずできるようになります。", "Si no tienes tiempo, puedes hacerlo poco a poco. Si te esfuerzas, seguro que serás capaz.")
        ]
    }
}

audio_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\audio"
base_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\lessons"
os.makedirs(audio_dir, exist_ok=True)

for lesson_id, data in dialogues.items():
    print(f"--- Processing Lesson {lesson_id} ---")
    
    # 1. Generate audio
    final_mp3 = os.path.join(audio_dir, f"dialogue-n4-{lesson_id}.mp3")
    if not os.path.exists(final_mp3):
        files = []
        for i, (voice, text_jp, _) in enumerate(data["lines"]):
            filename = f"line_{lesson_id}_{i}.mp3"
            safe_text = text_jp.replace('"', '\\"')
            cmd = f'python -m edge_tts --voice {voice} --text "{safe_text}" --rate=-10% --write-media {filename}'
            subprocess.run(cmd, shell=True, check=True)
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
    
    # 2. Inject HTML
    filepath = os.path.join(base_dir, f"jlpt-n4-{lesson_id}.html")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "🎧 Práctica de Comprensión Auditiva" not in content:
        html_block = f"""<h2 class="section-title">🎧 Práctica de Comprensión Auditiva (Diálogo)</h2>
<div class="grammar-note" style="background-color: #fdf2f8; border-left-color: #ec4899;">
    <p>Escucha este diálogo extenso (aprox. 1 minuto). Presta atención a cómo los personajes utilizan <strong>{data['title']}</strong>.</p>
    
    <div style="text-align: center; margin: 1.5rem 0; background: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border: 1px solid #e2e8f0;">
        <p style="margin-bottom: 15px; font-weight: 600; color: #475569; font-size: 1.1rem;">🎧 Escucha el diálogo (Voces IA):</p>
        <audio controls style="width: 100%; max-width: 450px; outline: none; border-radius: 50px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
            <source src="../audio/dialogue-n4-{lesson_id}.mp3" type="audio/mpeg">
            Tu navegador no soporta el elemento de audio.
        </audio>
    </div>

    <details style="background: white; padding: 1rem; border-radius: 8px; border: 1px solid #e2e8f0; margin-top: 1rem;">
        <summary style="font-weight: 600; cursor: pointer; color: var(--primary-color);">Ver Transcripción y Traducción</summary>
        <div style="margin-top: 1rem; display: grid; gap: 1rem; font-size: 0.95rem;">
"""
        for _, text_jp, text_es in data["lines"]:
            name = "A"
            if "：" in text_jp:
                name, text_jp_no_name = text_jp.split("：", 1)
            else:
                # Basic inference of name
                if text_jp.startswith("佐藤") or text_jp.startswith("たけし") or text_jp.startswith("先生") or text_jp.startswith("鈴木") or text_jp.startswith("あなた") or text_jp.startswith("けんじ"):
                    pass 
                
            html_block += f'            <div><div class="text-jp">{text_jp}</div><div class="text-es">{text_es}</div></div>\n'
            
        html_block += """        </div>
    </details>
</div>

"""
        target_str = '<h2 class="section-title">📝 Ejercicios de Práctica JLPT</h2>'
        new_content = content.replace(target_str, html_block + target_str)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Injected dialogue into jlpt-n4-{lesson_id}.html")

# Finally run add_furigana.py
print("Adding furigana...")
subprocess.run("python add_furigana.py", shell=True)
print("All done!")
