import os

data = {
    6: {
        "title": "Verbos Transitivos e Invitaciones",
        "grammar": [
            "<strong>N を V(Transitivo):</strong> La partícula を (wo) marca el objeto directo. (Ej: Comer una manzana).",
            "<strong>N(Lugar) で V:</strong> La partícula で marca el lugar donde ocurre una acción. (Diferente a に que marca ubicación de existencia o destino).",
            "<strong>~ませんか:</strong> '¿Por qué no...?' Se usa para invitar a alguien a hacer algo.",
            "<strong>~ましょう:</strong> 'Hagamos...'. Forma de proponer hacer algo juntos o aceptar una invitación."
        ],
        "examples": [
            ("私はジュースを飲みます。", "1. Yo bebo jugo.", "わたしはジュースをのみます"),
            ("私は駅で新聞を買います。", "2. Yo compro el periódico en la estación.", "わたしはえきでしんぶんをかいます"),
            ("一緒に神戸へ行きませんか。", "3. ¿Por qué no vamos juntos a Kobe?", "いっしょにこうべへいきませんか"),
            ("ええ、いいですね。", "4. Sí, qué buena idea.", "ええ、いいですね"),
            ("ちょっと休みましょう。", "5. Descansemos un poco.", "ちょっとやすみましょう"),
            ("何をしますか。", "6. ¿Qué vas a hacer?", "なにをしますか"),
            ("サッカーをします。", "7. Voy a jugar fútbol.", "サッカーをします"),
            ("誰と大阪城へ行きますか。", "8. ¿Con quién vas al Castillo de Osaka?", "だれとおおさかじょうへいきますか"),
            ("一人で行きます。", "9. Voy solo.", "ひとりでいきます"),
            ("毎日パンを食べます。", "10. Todos los días como pan.", "まいにちパンをたべます")
        ],
        "exercises": [
            {"q": "¿Qué partícula marca el OBJETO DIRECTO? (Ej. Comer 'carne')", "options": [{"text": "が", "correct": False}, {"text": "を", "correct": True}, {"text": "で", "correct": False}]},
            {"q": "¿Qué partícula marca el LUGAR DE ACCIÓN? (Ej. Comprar 'en la estación')", "options": [{"text": "に", "correct": False}, {"text": "へ", "correct": False}, {"text": "で", "correct": True}]},
            {"q": "¿Cómo invitas a alguien a beber té? (¿Por qué no bebemos té?)", "options": [{"text": "お茶を飲みますか。", "correct": False}, {"text": "お茶を飲みませんか。", "correct": True}, {"text": "お茶を飲みましょう。", "correct": False}]},
            {"q": "¿Cómo aceptas la invitación y dices '¡Vamos!' / '¡Hagámoslo!'?", "options": [{"text": "行きましょう。", "correct": True}, {"text": "行きます。", "correct": False}, {"text": "行きませんか。", "correct": False}]},
            {"q": "'Leo un libro en la biblioteca':", "options": [{"text": "図書館に本を読みます。", "correct": False}, {"text": "図書館で本を読みます。", "correct": True}, {"text": "図書館を本に読みます。", "correct": False}]},
            {"q": "¿Qué verbo se usa para 'Jugar fútbol' o 'Hacer una fiesta'?", "options": [{"text": "行きます (Ikimasu)", "correct": False}, {"text": "します (Shimasu)", "correct": True}, {"text": "あそびます (Asobimasu)", "correct": False}]},
            {"q": "'No como nada' (Negación completa):", "options": [{"text": "何をたべません。", "correct": False}, {"text": "何を食べません。", "correct": False}, {"text": "何も食べません。", "correct": True}]},
            {"q": "'Veo la televisión en casa':", "options": [{"text": "うちでテレビを見ます。", "correct": True}, {"text": "うちでテレビを書きます。", "correct": False}, {"text": "うちでテレビを読みます。", "correct": False}]},
            {"q": "Persona A: '¿Qué tal si descansamos?' Persona B: '...' (Aceptar)", "options": [{"text": "ええ、休みます。", "correct": False}, {"text": "ええ、休みましょう。", "correct": True}, {"text": "ええ、休みませんか。", "correct": False}]},
            {"q": "¿Cuál está bien escrita?", "options": [{"text": "手紙をします", "correct": False}, {"text": "手紙を書きます", "correct": True}, {"text": "手紙を読みます (puede ser, pero kakimasu es la típica)", "correct": True}]}
        ]
    },
    7: {
        "title": "Herramientas e Intercambio (Dar y Recibir)",
        "grammar": [
            "<strong>N(Herramienta/Idioma) で V:</strong> La partícula で también indica con qué herramienta, medio o idioma se hace algo.",
            "<strong>Sujeto は Persona に あげます:</strong> 'Dar a'. La persona que recibe el objeto se marca con に.",
            "<strong>Sujeto は Persona に もらいます:</strong> 'Recibir de'. La persona de quien se recibe se marca con に (o から)."
        ],
        "examples": [
            ("はさみで紙を切ります。", "1. Corto el papel con tijeras.", "はさみでかみをきります"),
            ("私は木村さんに花をあげました。", "2. Yo le di flores a la Sra. Kimura.", "わたしはきむらさんはなをあげました"),
            ("私はカリナさんにチョコレートをもらいました。", "3. Yo recibí chocolates de Karina.", "わたしはカリナさんにチョコレートをもらいました"),
            ("日本語でレポートを書きます。", "4. Escribo el reporte en japonés.", "にほんごでレポートをかきます"),
            ("「ありがとう」は英語で何ですか。", "5. ¿Cómo se dice 'Arigatou' en inglés?", "ありがとうはえいごでなんですか"),
            ("「Thank you」です。", "6. Es 'Thank you'.", "サンキューです"),
            ("誰に年賀状を書きますか。", "7. ¿A quién le escribes tarjetas de Año Nuevo?", "だれにねんがじょうをかきますか"),
            ("先生と友達に書きます。", "8. Se las escribo a mi profesor y a mis amigos.", "せんせいとともだちにかきます"),
            ("もう新幹線の切符を買いましたか。", "9. ¿Ya compraste los boletos del tren bala?", "もうしんかんせんのきっぷをかいましたか"),
            ("はい、もう買いました。", "10. Sí, ya los compré.", "はい、もうかいました")
        ],
        "exercises": [
            {"q": "¿Qué partícula se usa para decir 'Como CON palillos'?", "options": [{"text": "を", "correct": False}, {"text": "と", "correct": False}, {"text": "で", "correct": True}]},
            {"q": "'Escribo la carta en japonés' (Idioma):", "options": [{"text": "日本語に手紙を書きます。", "correct": False}, {"text": "日本語で手紙を書きます。", "correct": True}, {"text": "日本語の手紙を書きます。", "correct": False}]},
            {"q": "¿Qué verbo significa DAR (a un igual o inferior)?", "options": [{"text": "あげます", "correct": True}, {"text": "もらいます", "correct": False}, {"text": "かります", "correct": False}]},
            {"q": "¿Qué verbo significa RECIBIR?", "options": [{"text": "かします", "correct": False}, {"text": "もらいます", "correct": True}, {"text": "おしえます", "correct": False}]},
            {"q": "'Le presté un libro a Suzuki':", "options": [{"text": "鈴木さんに本を借りました。", "correct": False}, {"text": "鈴木さんに本を貸しました。", "correct": True}, {"text": "鈴木さんに本をあげました。", "correct": False}]},
            {"q": "'Recibí este reloj de mi padre':", "options": [{"text": "父にこの時計をあげました。", "correct": False}, {"text": "父にこの時計をもらいました。", "correct": True}, {"text": "父がこの時計をもらいました。", "correct": False}]},
            {"q": "¿Se puede usar から en lugar de に al recibir algo de alguien?", "options": [{"text": "Sí", "correct": True}, {"text": "No", "correct": False}, {"text": "Solo si es un animal", "correct": False}]},
            {"q": "¿Qué significa la palabra 'もう' (Mou)?", "options": [{"text": "Todavía no", "correct": False}, {"text": "Ya (already)", "correct": True}, {"text": "Aún", "correct": False}]},
            {"q": "'¿Ya comiste?':", "options": [{"text": "もう食べましたか。", "correct": True}, {"text": "まだ食べましたか。", "correct": False}, {"text": "もう食べますか。", "correct": False}]},
            {"q": "Persona A: '¿Ya comiste?' Persona B: 'No, todavía no.'", "options": [{"text": "いいえ、もうです。", "correct": False}, {"text": "いいえ、まだです。", "correct": True}, {"text": "いいえ、食べません。", "correct": False}]}
        ]
    },
    8: {
        "title": "Adjetivos (Na / i)",
        "grammar": [
            "<strong>Adjetivos-na:</strong> Para modificar un sustantivo se pone な (Ej. きれいな町). Al final de la oración terminan en です (Ej. 町はきれいです).",
            "<strong>Adjetivos-i:</strong> Terminan en い y no necesitan partículas extra para modificar un sustantivo (Ej. 高い山).",
            "<strong>どうですか:</strong> '¿Cómo es...?' Para pedir una opinión.",
            "<strong>どんな N ですか:</strong> '¿Qué tipo de N es...?'"
        ],
        "examples": [
            ("桜はきれいです。", "1. Los cerezos son hermosos.", "さくらはきれいです"),
            ("富士山は高いです。", "2. El monte Fuji es alto.", "ふじさんはたかいです"),
            ("京都は静かな町です。", "3. Kioto es una ciudad tranquila.", "きょうとはしずかなまちです"),
            ("東京はにぎやかな町です。", "4. Tokio es una ciudad animada.", "とうきょうはにぎやかなまちです"),
            ("日本の生活はどうですか。", "5. ¿Qué tal la vida en Japón? / ¿Cómo es la vida en Japón?", "にほんのせいかつはどうですか"),
            ("楽しいです。", "6. Es divertida.", "たのしいです"),
            ("奈良はどんな町ですか。", "7. ¿Qué clase de ciudad es Nara?", "ならはどんなまちですか"),
            ("古い町です。", "8. Es una ciudad antigua.", "ふるいまちです"),
            ("そのパソコンは新しいですか。", "9. ¿Esa computadora es nueva?", "そのパソコンはあたらしいですか"),
            ("いいえ、新しくないです。", "10. No, no es nueva.", "いいえ、あたらしくないです")
        ],
        "exercises": [
            {"q": "¿Cuál de estos es un Adjetivo-na?", "options": [{"text": "高い (takai)", "correct": False}, {"text": "静か (shizuka)", "correct": True}, {"text": "大きい (ookii)", "correct": False}]},
            {"q": "¿Cómo unes un Adjetivo-na con un Sustantivo? (Ej. Ciudad hermosa)", "options": [{"text": "きれい町", "correct": False}, {"text": "きれいな町", "correct": True}, {"text": "きれいの町", "correct": False}]},
            {"q": "¿Cómo unes un Adjetivo-i con un Sustantivo? (Ej. Montaña alta)", "options": [{"text": "高い山", "correct": True}, {"text": "高な山", "correct": False}, {"text": "高の山", "correct": False}]},
            {"q": "¿Cómo se dice 'No es alto' (Negativo de 高い - Adjetivo i)?", "options": [{"text": "高いじゃありません", "correct": False}, {"text": "高くありません / 高くないです", "correct": True}, {"text": "高いではありません", "correct": False}]},
            {"q": "¿Cómo se dice 'No es tranquilo' (Negativo de 静か - Adjetivo na)?", "options": [{"text": "静かじゃありません", "correct": True}, {"text": "静かくないです", "correct": False}, {"text": "静かないです", "correct": False}]},
            {"q": "Excepción: ¿Cuál es el negativo de いい (ii - bueno)?", "options": [{"text": "いくないです", "correct": False}, {"text": "よくないです", "correct": True}, {"text": "いいじゃないです", "correct": False}]},
            {"q": "Para preguntar '¿Qué tal es tu trabajo? (opinión)':", "options": [{"text": "仕事はどんなですか。", "correct": False}, {"text": "仕事はどうですか。", "correct": True}, {"text": "仕事はなんですか。", "correct": False}]},
            {"q": "Para preguntar '¿Qué tipo de trabajo es?':", "options": [{"text": "どんな仕事ですか。", "correct": True}, {"text": "どう仕事ですか。", "correct": False}, {"text": "なんの仕事ですか。", "correct": False}]},
            {"q": "'La comida es sabrosa, PERO es cara':", "options": [{"text": "おいしいですが、高いです。", "correct": True}, {"text": "おいしいから、高いです。", "correct": False}, {"text": "おいしいと、高いです。", "correct": False}]},
            {"q": "'¿Qué tal el tiempo en Japón?':", "options": [{"text": "日本の天気はどうですか。", "correct": True}, {"text": "日本の天気はどんなですか。", "correct": False}, {"text": "日本の天気がどうですか。", "correct": False}]}
        ]
    },
    9: {
        "title": "Gustos, Habilidades y Razones (あります / わかります)",
        "grammar": [
            "<strong>N が 好き/嫌い/上手/下手 です:</strong> La partícula が marca el objeto de los gustos (me gusta, odio) y habilidades (soy bueno, soy malo).",
            "<strong>N が わかります / あります:</strong> Los verbos entender (wakariamsu) y tener (arimasu) son intransitivos en japonés, por lo que su objeto se marca con が, no con を.",
            "<strong>~から:</strong> 'Porque... / Por eso'. Conecta una razón al final de la frase."
        ],
        "examples": [
            ("私はイタリア料理が好きです。", "1. Me gusta la comida italiana.", "わたしはイタリアりょうりがすきです"),
            ("私は日本語が少しわかります。", "2. Yo entiendo un poco de japonés.", "わたしはにほんごがすこしわかります"),
            ("今日は約束があります。", "3. Hoy tengo un compromiso.", "きょうはやくそくがあります"),
            ("マリアさんはダンスが上手です。", "4. María es buena bailando.", "マリアさんはダンスがじょうずです"),
            ("時間がありませんから、タクシーで行きましょう。", "5. Como no tenemos tiempo, vayamos en taxi.", "じかんがありませんから、タクシーでいきましょう"),
            ("どうして昨日早く帰りましたか。", "6. ¿Por qué te fuiste a casa temprano ayer?", "どうしてきのうはやくかえりましたか"),
            ("用事がありましたから。", "7. Porque tenía cosas que hacer.", "ようじがありましたから"),
            ("どんなスポーツが好きですか。", "8. ¿Qué clase de deportes te gustan?", "どんなスポーツがすきですか"),
            ("野球が好きです。", "9. Me gusta el béisbol.", "やきゅうがすきです"),
            ("全然わかりません。", "10. No entiendo en lo absoluto.", "ぜんぜんわかりません")
        ],
        "exercises": [
            {"q": "¿Qué partícula se usa normalmente para los gustos (好き / 嫌い)?", "options": [{"text": "を", "correct": False}, {"text": "が", "correct": True}, {"text": "に", "correct": False}]},
            {"q": "'Me gusta la música':", "options": [{"text": "音楽を好きです。", "correct": False}, {"text": "音楽が好きです。", "correct": True}, {"text": "音楽は好きです。", "correct": False}]},
            {"q": "¿Qué partícula usan los verbos わかります (Entender) y あります (Tener)?", "options": [{"text": "を", "correct": False}, {"text": "が", "correct": True}, {"text": "で", "correct": False}]},
            {"q": "'No tengo tiempo':", "options": [{"text": "時間をありません。", "correct": False}, {"text": "時間がありません。", "correct": True}, {"text": "時間ではありません。", "correct": False}]},
            {"q": "¿Cómo se pregunta '¿Por qué?'", "options": [{"text": "どうして", "correct": True}, {"text": "どう", "correct": False}, {"text": "どんな", "correct": False}]},
            {"q": "Si te preguntan con 'どうして', ¿cómo debes responder?", "options": [{"text": "Agregando 'から' al final de la razón.", "correct": True}, {"text": "Agregando 'です' al final.", "correct": False}, {"text": "Solo diciendo el motivo.", "correct": False}]},
            {"q": "'¿Por qué no comes?' 'Porque estoy lleno'.", "options": [{"text": "お腹がいっぱいです。", "correct": False}, {"text": "お腹がいっぱいだからです。", "correct": False}, {"text": "お腹がいっぱいですから。", "correct": True}]},
            {"q": "¿Qué significa '上手' (Jouzu)?", "options": [{"text": "Gustar", "correct": False}, {"text": "Ser hábil o bueno en algo", "correct": True}, {"text": "Odiar", "correct": False}]},
            {"q": "¿Qué adverbio se usa para decir 'No entiendo NADA'?", "options": [{"text": "少し (Sukoshi)", "correct": False}, {"text": "全然 (Zenzen)", "correct": True}, {"text": "たくさん (Takusan)", "correct": False}]},
            {"q": "'No tengo dinero, por eso no compro':", "options": [{"text": "お金がありませんから、買いません。", "correct": True}, {"text": "お金がありませんが、買いません。", "correct": False}, {"text": "お金がありませんので、買いません。", "correct": False}]}
        ]
    },
    10: {
        "title": "Existencia y Ubicación (あります / います)",
        "grammar": [
            "<strong>あります:</strong> 'Hay / Está'. Se usa para objetos inanimados o plantas.",
            "<strong>います:</strong> 'Hay / Está'. Se usa para personas y animales (seres animados).",
            "<strong>Lugar に N が あります/います:</strong> 'En (Lugar) hay (N)'. La partícula に marca el lugar de existencia, y が marca lo que existe.",
            "<strong>N1(Cosa) は Lugar に あります/います:</strong> 'El (N) está en (Lugar)'. El sustantivo es el tema y ya sabemos de qué hablamos."
        ],
        "examples": [
            ("あそこにコンビニがあります。", "1. Allí hay una tienda de conveniencia.", "あそこにコンビニがあります"),
            ("ロビーに佐藤さんがいます。", "2. El Sr. Sato está en el lobby.", "ロビーにさとうさんがいます"),
            ("東京ディズニーランドは千葉県にあります。", "3. Tokyo Disneyland está en la prefectura de Chiba.", "とうきょうディズニーランドはちばけんにあります"),
            ("家族はニューヨークにいます。", "4. Mi familia está en Nueva York.", "かぞくはニューヨークにいます"),
            ("机の上に写真があります。", "5. Hay una foto encima del escritorio.", "つくえのうえにしゃしんがあります"),
            ("箱の中に手紙があります。", "6. Hay una carta dentro de la caja.", "はこのなかにてがみがあります"),
            ("ポストの隣に銀行があります。", "7. Hay un banco al lado del buzón.", "ポストのとなりにぎんこうがあります"),
            ("公園に誰がいますか。", "8. ¿Quién hay (está) en el parque?", "こうえんにだれがいますか"),
            ("誰もいません。", "9. No hay nadie.", "だれもいません"),
            ("ベッドの下に何がありますか。", "10. ¿Qué hay debajo de la cama?", "ベッドのしたになにがありますか")
        ],
        "exercises": [
            {"q": "¿Qué verbo se usa para expresar la existencia de objetos inanimados (ej. silla, árbol)?", "options": [{"text": "います", "correct": False}, {"text": "あります", "correct": True}, {"text": "します", "correct": False}]},
            {"q": "¿Qué verbo se usa para personas y animales?", "options": [{"text": "います", "correct": True}, {"text": "あります", "correct": False}, {"text": "きます", "correct": False}]},
            {"q": "¿Qué partícula marca el lugar donde EXISTE o está algo? (Verbos imasu/arimasu)", "options": [{"text": "で", "correct": False}, {"text": "に", "correct": True}, {"text": "へ", "correct": False}]},
            {"q": "'En la oficina hay una computadora':", "options": [{"text": "事務所にパソコンがいます。", "correct": False}, {"text": "事務所にパソコンがあります。", "correct": True}, {"text": "事務所でパソコンがあります。", "correct": False}]},
            {"q": "'El gato está en el jardín':", "options": [{"text": "庭に猫がいます。", "correct": True}, {"text": "庭に猫があります。", "correct": False}, {"text": "庭で猫がいます。", "correct": False}]},
            {"q": "¿Dónde está la silla? 'Encima del escritorio':", "options": [{"text": "机の中", "correct": False}, {"text": "机の上", "correct": True}, {"text": "机の下", "correct": False}]},
            {"q": "¿Dónde está el banco? 'Al lado de la estación':", "options": [{"text": "駅の隣", "correct": True}, {"text": "駅の前", "correct": False}, {"text": "駅の後ろ", "correct": False}]},
            {"q": "Persona A: '¿Quién está en el aula?' Persona B: 'No hay nadie'.", "options": [{"text": "誰もいません。", "correct": True}, {"text": "誰もありません。", "correct": False}, {"text": "誰もいませんか。", "correct": False}]},
            {"q": "¿Cómo se pregunta '¿Dónde está el Sr. Miller?'", "options": [{"text": "ミラーさんはどこですか。", "correct": True}, {"text": "ミラーさんはどこにいますか。", "correct": True}, {"text": "Ambas son correctas.", "correct": True}]},
            {"q": "'Hay un libro y un cuaderno' (Listado completo):", "options": [{"text": "本とノートがあります。", "correct": True}, {"text": "本やノートがあります。", "correct": False}, {"text": "本からノートがあります。", "correct": False}]}
        ]
    }
}

def generate():
    base_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\lessons"
    
    for i in range(6, 11):
        d = data[i]
        
        grammar_html = ""
        for g in d["grammar"]:
            grammar_html += f"                <li>{g}</li>\n"
            
        examples_html = ""
        for ex in d["examples"]:
            examples_html += f'''        <div class="practice-item"><div class="practice-content"><div class="text-jp">{ex[0]}</div><div class="text-es">{ex[1]}</div></div><button class="audio-btn" onclick="playAudio('{ex[2]}')">🔊</button></div>\n'''
            
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

        html = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lección {i} - Minna no Nihongo I</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=Noto+Sans+JP:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../css/style.css">
</head>
<body class="iframe-body">
    <div class="max-w-4xl">
        <div class="lesson-header-simple">
            <span>第{i}課</span>
            <h1>Minna no Nihongo I - Lección {i}</h1>
            <p class="lesson-desc">Tema: {d["title"]}</p>
        </div>

        <div class="video-link-section" style="text-align: center; margin: 2rem 0; padding: 2.5rem; background: linear-gradient(135deg, var(--secondary-color) 0%, #2a2a4a 100%); border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
            <h3 style="color: white; margin-bottom: 0.5rem; font-size: 1.5rem;">🎬 Clase en Video</h3>
            <p style="color: #cbd5e0; margin-bottom: 1.5rem; font-size: 1.05rem;">Aprende la gramática detallada de la Lección {i} con Kira Sensei.</p>
            <a href="https://www.youtube.com/results?search_query=Kira+Sensei+Minna+no+Nihongo+Leccion+{i}" target="_blank" style="display: inline-block; background: var(--primary-color); color: white; padding: 1rem 2.5rem; border-radius: 50px; text-decoration: none; font-weight: 700; font-size: 1.15rem; transition: transform 0.2s, box-shadow 0.2s; box-shadow: 0 4px 15px rgba(224, 42, 77, 0.4);" onmouseover="this.style.transform='translateY(-3px)'; this.style.boxShadow='0 6px 20px rgba(224, 42, 77, 0.6)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 15px rgba(224, 42, 77, 0.4)'">Ver Lección {i} en YouTube</a>
        </div>

        <h2 class="section-title">📚 Gramática Principal</h2>
        <div class="grammar-note">
            <ul>
{grammar_html}            </ul>
        </div>
        
        <h2 class="section-title">🌟 10 Ejemplos de Uso</h2>
        <div class="grammar-note"><p>A continuación, 10 ejemplos prácticos utilizando la gramática aprendida en esta lección.</p></div>
{examples_html}
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

        with open(os.path.join(base_dir, f"lesson-{i}.html"), "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated Lesson {i}")

if __name__ == '__main__':
    generate()
