import os

data = {
    1: {
        "title": "Partículas Básicas (は, が, を)",
        "grammar": [
            "<strong>は (wa):</strong> Marca el TEMA de la oración. De lo que se va a hablar. (Ej. 私は学生です - En cuanto a mí, soy estudiante).",
            "<strong>が (ga):</strong> Marca el SUJETO gramatical o enfatiza quién hace la acción. También marca el objeto de verbos como 好き, わかる, あります.",
            "<strong>を (o/wo):</strong> Marca el OBJETO DIRECTO de un verbo transitivo. (Ej. ご飯を食べる - Comer arroz)."
        ],
        "examples": [
            ("私はマリアです。", "1. Yo soy María.", "わたしはマリアです"),
            ("犬が好きです。", "2. Me gustan los perros.", "いぬがすきです"),
            ("彼が来ました。", "3. Él fue quien vino. (Enfatizando el sujeto).", "かれがきました"),
            ("毎日水を飲みます。", "4. Todos los días bebo agua.", "まいにちみずをのみます"),
            ("これは何ですか。", "5. ¿Qué es esto?", "これはなんですか"),
            ("あそこに猫がいます。", "6. Allí hay un gato.", "あそこにねこがいます"),
            ("手紙を書きます。", "7. Escribo una carta.", "てがみをかきます"),
            ("日本語がわかります。", "8. Entiendo japonés.", "にほんごがわかります"),
            ("今日は日曜日です。", "9. Hoy es domingo.", "きょうはにちようびです"),
            ("本を読みます。", "10. Leo un libro.", "ほんをよみます")
        ],
        "exercises": [
            {"q": "¿Qué partícula usas para marcar el tema principal 'Yo' en 'Yo soy Carlos'?", "options": [{"text": "が (ga)", "correct": False}, {"text": "を (wo)", "correct": False}, {"text": "は (wa)", "correct": True}]},
            {"q": "Para decir 'Bebo café' (コーヒー _ 飲みます), ¿qué partícula falta?", "options": [{"text": "を (wo)", "correct": True}, {"text": "が (ga)", "correct": False}, {"text": "は (wa)", "correct": False}]},
            {"q": "Con el verbo 'Gustar' (好きです), el objeto deseado se marca con:", "options": [{"text": "を", "correct": False}, {"text": "が", "correct": True}, {"text": "は", "correct": False}]},
            {"q": "¿Cuál es correcta? 'El señor Tanaka compró un periódico'", "options": [{"text": "田中さんは新聞が買いました。", "correct": False}, {"text": "田中さんは新聞を買いました。", "correct": True}, {"text": "田中さんは新聞は買いました。", "correct": False}]},
            {"q": "'Hay un libro en la mesa': 机の上に本 _ あります。", "options": [{"text": "が", "correct": True}, {"text": "を", "correct": False}, {"text": "は", "correct": False}]},
            {"q": "Persona A: '¿Quién rompió la ventana?' Persona B: 'Juan _ rompió'.", "options": [{"text": "フアンは (Juan wa)", "correct": False}, {"text": "フアンが (Juan ga - Enfatiza quién lo hizo)", "correct": True}, {"text": "フアンを (Juan wo)", "correct": False}]},
            {"q": "'Leo el periódico':", "options": [{"text": "新聞が読みます", "correct": False}, {"text": "新聞を読みます", "correct": True}, {"text": "新聞は読みます", "correct": False}]},
            {"q": "'Yo entiendo inglés':", "options": [{"text": "英語をわかります", "correct": False}, {"text": "英語がわかります", "correct": True}, {"text": "英語はわかります", "correct": False}]},
            {"q": "¿Qué partícula nunca inicia una oración en japonés?", "options": [{"text": "を (wo)", "correct": True}, {"text": "は (wa)", "correct": False}, {"text": "が (ga)", "correct": False}]},
            {"q": "'En cuanto a mañana, descansaré':", "options": [{"text": "明日は休みます。", "correct": True}, {"text": "明日が休みます。", "correct": False}, {"text": "明日を休みます。", "correct": False}]}
        ]
    },
    2: {
        "title": "Partículas Direccionales y de Lugar (に, で, へ, と)",
        "grammar": [
            "<strong>に (ni):</strong> Indica destino (Voy a Japón), tiempo exacto (A las 6), o ubicación de existencia (Está en la mesa).",
            "<strong>へ (e):</strong> Marca dirección hacia un lugar (Hacia Tokio). A menudo intercambiable con に para movimiento.",
            "<strong>で (de):</strong> Marca el lugar donde ocurre una acción (Comer en el parque). También marca el medio de transporte o herramienta.",
            "<strong>と (to):</strong> Significa 'y' (Unir sustantivos) o 'con' (Compañía)."
        ],
        "examples": [
            ("東京へ行きます。", "1. Voy a Tokio (dirección).", "とうきょうへいきます"),
            ("６時に起きます。", "2. Me levanto a las 6 (tiempo).", "ろくじにおきます"),
            ("レストランでご飯を食べます。", "3. Como arroz en el restaurante (lugar de acción).", "レストランでごはんをたべます"),
            ("車で来ました。", "4. Vine en auto (medio).", "くるまできました"),
            ("友達と話します。", "5. Hablo con un amigo (compañía).", "ともだちとはなします"),
            ("パンと卵を買いました。", "6. Compré pan y huevos (conjunción).", "パンとたまごをかいました"),
            ("机の上に本があります。", "7. El libro está en el escritorio (ubicación).", "つくえのうえにほんがあります"),
            ("明日、学校に行きません。", "8. Mañana no iré a la escuela.", "あした、がっこうにいきません"),
            ("鉛筆で書きます。", "9. Escribo con lápiz (herramienta).", "えんぴつでかきます"),
            ("父と母は元気です。", "10. Mi padre y mi madre están saludables.", "ちちとはははげんきです")
        ],
        "exercises": [
            {"q": "¿Qué partícula usas para decir 'Voy A Tokio'?", "options": [{"text": "で / を", "correct": False}, {"text": "へ / に", "correct": True}, {"text": "が / は", "correct": False}]},
            {"q": "'Estudio EN la biblioteca':", "options": [{"text": "図書館に勉強します", "correct": False}, {"text": "図書館で勉強します", "correct": True}, {"text": "図書館へ勉強します", "correct": False}]},
            {"q": "Para decir 'A las 8 de la mañana':", "options": [{"text": "朝８時に", "correct": True}, {"text": "朝８時で", "correct": False}, {"text": "朝８時へ", "correct": False}]},
            {"q": "¿Qué partícula une dos sustantivos? 'Perro Y gato':", "options": [{"text": "犬と猫", "correct": True}, {"text": "犬に猫", "correct": False}, {"text": "犬で猫", "correct": False}]},
            {"q": "Fui a Osaka EN TREN:", "options": [{"text": "電車に大阪へ行きました。", "correct": False}, {"text": "電車で大阪へ行きました。", "correct": True}, {"text": "電車と大阪へ行きました。", "correct": False}]},
            {"q": "Comí CON LA FAMILIA:", "options": [{"text": "家族と食べました。", "correct": True}, {"text": "家族に食べました。", "correct": False}, {"text": "家族で食べました。(Puede significar 'entre toda la familia')", "correct": True}]},
            {"q": "Hay un gato EN LA HABITACIÓN (Existencia, no acción):", "options": [{"text": "部屋で猫がいます。", "correct": False}, {"text": "部屋に猫がいます。", "correct": True}, {"text": "部屋へ猫がいます。", "correct": False}]},
            {"q": "Cortar CON TIJERAS (Herramienta):", "options": [{"text": "はさみで切ります。", "correct": True}, {"text": "はさみに切ります。", "correct": False}, {"text": "はさみと切ります。", "correct": False}]},
            {"q": "'El domingo fui al parque con mi perro':", "options": [{"text": "日曜日に犬で公園へ行きました。", "correct": False}, {"text": "日曜日に犬と公園へ行きました。", "correct": True}, {"text": "日曜日と犬に公園へ行きました。", "correct": False}]},
            {"q": "Diferencia entre に y で:", "options": [{"text": "に es para acciones dinámicas y で para estado.", "correct": False}, {"text": "に es para punto fijo/existencia y で es para el lugar donde ocurre una actividad.", "correct": True}, {"text": "Son exactamente iguales.", "correct": False}]}
        ]
    },
    3: {
        "title": "Palabras Interrogativas (¿Qué, Dónde, Quién, Cuándo?)",
        "grammar": [
            "<strong>何 (Nani / Nan):</strong> ¿Qué? Nan se usa antes de desu, de contadores, y palabras que empiezan con T, D, N.",
            "<strong>どこ (Doko):</strong> ¿Dónde? Se responde con lugares.",
            "<strong>誰 (Dare):</strong> ¿Quién? Si quieres ser formal, se usa どなた (Donata).",
            "<strong>いつ (Itsu):</strong> ¿Cuándo? No lleva la partícula に."
        ],
        "examples": [
            ("これは何ですか。", "1. ¿Qué es esto?", "これはなんですか"),
            ("何をしますか。", "2. ¿Qué vas a hacer?", "なにをしますか"),
            ("トイレはどこですか。", "3. ¿Dónde está el baño?", "トイレはどこですか"),
            ("あの人は誰ですか。", "4. ¿Quién es aquella persona?", "あのひとはだれですか"),
            ("いつ日本へ来ましたか。", "5. ¿Cuándo viniste a Japón?", "いつにほんへきましたか"),
            ("誕生日はいつですか。", "6. ¿Cuándo es tu cumpleaños?", "たんじょうびはいつですか"),
            ("どこでカメラを買いましたか。", "7. ¿Dónde compraste la cámara?", "どこでカメラをかいましたか"),
            ("誰と行きますか。", "8. ¿Con quién vas?", "だれといきますか"),
            ("何時ですか。", "9. ¿Qué hora es? (Nan-ji)", "なんじですか"),
            ("何を食べましたか。", "10. ¿Qué comiste? (Nani-wo)", "なにをたべましたか")
        ],
        "exercises": [
            {"q": "¿Cómo se pregunta '¿Quién?' en japonés?", "options": [{"text": "どこ (Doko)", "correct": False}, {"text": "いつ (Itsu)", "correct": False}, {"text": "だれ (Dare)", "correct": True}]},
            {"q": "¿Cómo se pregunta '¿Dónde?' en japonés?", "options": [{"text": "どこ (Doko)", "correct": True}, {"text": "なに (Nani)", "correct": False}, {"text": "だれ (Dare)", "correct": False}]},
            {"q": "¿Cuándo se pronuncia 'Nan' en lugar de 'Nani'?", "options": [{"text": "Antes de 'desu' y de contadores.", "correct": True}, {"text": "Siempre que va al inicio de la frase.", "correct": False}, {"text": "Cuando el objeto es plural.", "correct": False}]},
            {"q": "¿Cómo preguntas 'Qué compraste'?", "options": [{"text": "何を買いましたか。(Nani o kaimashita ka)", "correct": True}, {"text": "何で買いましたか。(Nan de kaimashita ka)", "correct": False}, {"text": "何を来ましたか。(Nani o kimashita ka)", "correct": False}]},
            {"q": "¿Qué palabra interrogativa NUNCA usa la partícula に (ni) para preguntar el tiempo?", "options": [{"text": "何時 (A qué hora)", "correct": False}, {"text": "何日 (Qué día)", "correct": False}, {"text": "いつ (Cuándo)", "correct": True}]},
            {"q": "'¿Con quién fuiste a Tokio?':", "options": [{"text": "誰に東京へ行きましたか。", "correct": False}, {"text": "誰と東京へ行きましたか。", "correct": True}, {"text": "誰が東京へ行きましたか。", "correct": False}]},
            {"q": "¿Cómo dices '¿De quién es esto?' (posesión)?", "options": [{"text": "誰がですか。", "correct": False}, {"text": "誰のですか。", "correct": True}, {"text": "誰ですか。", "correct": False}]},
            {"q": "¿Cómo respondes educadamente a 'あの方はどなたですか' (¿Quién es aquella persona?)?", "options": [{"text": "友達だれです。", "correct": False}, {"text": "山田さんです。", "correct": True}, {"text": "あそこです。", "correct": False}]},
            {"q": "¿Qué significa 'どこか' (doko ka)?", "options": [{"text": "En ningún lado", "correct": False}, {"text": "En algún lado", "correct": True}, {"text": "Dónde", "correct": False}]},
            {"q": "¿Qué significa '何も' (nani mo) usado con un verbo negativo?", "options": [{"text": "Algo", "correct": False}, {"text": "Nada", "correct": True}, {"text": "Todo", "correct": False}]}
        ]
    },
    4: {
        "title": "Números, Fechas y Horas",
        "grammar": [
            "<strong>Números base:</strong> 1(ichi), 2(ni), 3(san), 4(yon/shi), 5(go), 6(roku), 7(nana/shichi), 8(hachi), 9(kyuu), 10(juu).",
            "<strong>Horas:</strong> Número + 時 (ji). Ej. 4:00 (Yo-ji), 9:00 (Ku-ji). Minutos: 分 (fun/pun).",
            "<strong>Días de la semana:</strong> Lunes(Getsu), Martes(Ka), Miércoles(Sui), Jueves(Moku), Viernes(Kin), Sábado(Do), Domingo(Nichi) + youbi.",
            "<strong>Días del mes:</strong> Del 1 al 10 tienen nombres especiales (Tsuitachi, Futsuka, Mikka...). Del 11 en adelante es Número + 日(nichi), excepto 14, 20, 24."
        ],
        "examples": [
            ("今、何時ですか。", "1. ¿Qué hora es ahora?", "いま、なんじですか"),
            ("午後３時半です。", "2. Son las 3 y media de la tarde.", "ごごさんじはんです"),
            ("誕生日は５月５日です。", "3. Mi cumpleaños es el 5 de mayo (Go-gatsu itsu-ka).", "たんじょうびはごがついつかです"),
            ("今日は火曜日です。", "4. Hoy es martes.", "きょうはかようびです"),
            ("１００円です。", "5. Son 100 yenes (Hyaku-en).", "ひゃくえんです"),
            ("毎朝７時に起きます。", "6. Me levanto a las 7 cada mañana (Shichi-ji).", "まいあさしちじにおきます"),
            ("月曜日から金曜日まで働きます。", "7. Trabajo de lunes a viernes.", "げつようびからきんようびまではたらきます"),
            ("今日は１日です。", "8. Hoy es el día 1 del mes (Tsuitachi).", "きょうはついたちです"),
            ("２０日に旅行します。", "9. Viajaré el día 20 (Hatsuka).", "はつかにりょこうします"),
            ("１５分休みましょう。", "10. Descansemos 15 minutos (Juu-go-fun).", "じゅうごふんやすみましょう")
        ],
        "exercises": [
            {"q": "¿Cómo se dice 'Abril' (Mes 4)?", "options": [{"text": "よんがつ (Yon-gatsu)", "correct": False}, {"text": "しがつ (Shi-gatsu)", "correct": True}, {"text": "よんげつ (Yon-getsu)", "correct": False}]},
            {"q": "¿Cómo se pronuncia el día 20 del mes?", "options": [{"text": "にじゅうにち (Nijuu-nichi)", "correct": False}, {"text": "はつか (Hatsuka)", "correct": True}, {"text": "ふつか (Futsuka)", "correct": False}]},
            {"q": "¿Cómo se dice 4:00 en japonés?", "options": [{"text": "よんじ (Yon-ji)", "correct": False}, {"text": "よじ (Yo-ji)", "correct": True}, {"text": "しじ (Shi-ji)", "correct": False}]},
            {"q": "¿Cuál de estos días es MIÉRCOLES?", "options": [{"text": "月曜日 (Getsuyoubi)", "correct": False}, {"text": "水曜日 (Suiyoubi)", "correct": True}, {"text": "木曜日 (Mokuyoubi)", "correct": False}]},
            {"q": "Si algo cuesta 3,000 yenes, se dice:", "options": [{"text": "さんせんえん (San-sen en)", "correct": False}, {"text": "さんぜんえん (San-zen en)", "correct": True}, {"text": "さんびゃくえん (San-byaku en)", "correct": False}]},
            {"q": "¿Cómo se lee el día 1 del mes?", "options": [{"text": "いちにち (Ichi-nichi)", "correct": False}, {"text": "ついたち (Tsuitachi)", "correct": True}, {"text": "いつか (Itsuka)", "correct": False}]},
            {"q": "¿Qué significa '午前' (Gozen) y '午後' (Gogo)?", "options": [{"text": "Ayer / Hoy", "correct": False}, {"text": "Mañana (AM) / Tarde (PM)", "correct": True}, {"text": "Antes / Después", "correct": False}]},
            {"q": "¿Cómo se dice 9:00 en japonés?", "options": [{"text": "きゅうじ (Kyuu-ji)", "correct": False}, {"text": "くじ (Ku-ji)", "correct": True}, {"text": "ここのじ (Kokono-ji)", "correct": False}]},
            {"q": "El día 8 del mes (Yōka) y el día 4 (Yokka) suenan parecido. ¿Cuál es el 4?", "options": [{"text": "ようか", "correct": False}, {"text": "よっか", "correct": True}, {"text": "よんか", "correct": False}]},
            {"q": "¿Cómo se pronuncian los minutos 10 y 30?", "options": [{"text": "じゅっぷん (juppun) / はん (han)", "correct": True}, {"text": "じゅうふん (juufun) / さんじゅう (sanjuu)", "correct": False}, {"text": "じっぷん (jippun) / なか (naka)", "correct": False}]}
        ]
    },
    5: {
        "title": "Adjetivos Básicos y Colores (JLPT N5)",
        "grammar": [
            "<strong>Adjetivos-i:</strong> Terminan en い. (Ej: 高い - alto/caro). Modifican directamente (高い山). Pasado: 高かった. Negativo: 高くない.",
            "<strong>Adjetivos-na:</strong> No terminan en い (con excepciones como きれい). Modifican con な (きれいな町). Pasado: きれいでした. Negativo: きれいじゃありません.",
            "<strong>Colores:</strong> Algunos colores son adjetivos-i (赤い, 青い, 白い, 黒い). Otros son sustantivos y usan の (緑の, 茶色の)."
        ],
        "examples": [
            ("このりんごは赤いです。", "1. Esta manzana es roja.", "このりんごはあかいです"),
            ("あの海は青くてきれいです。", "2. Aquel mar es azul y hermoso.", "あのうみはあおくてきれいです"),
            ("日本料理はおいしいです。", "3. La comida japonesa es deliciosa.", "にほんりょうりはおいしいです"),
            ("昨日は暑かったです。", "4. Ayer hizo calor.", "きのうはあつかったです"),
            ("この本は難しくないです。", "5. Este libro no es difícil.", "このほんはむずかしくないです"),
            ("東京はにぎやかな町です。", "6. Tokio es una ciudad bulliciosa.", "とうきょうはにぎやかなまちです"),
            ("あの先生は親切じゃありません。", "7. Aquel profesor no es amable.", "あのせんせいはしんせつじゃありません"),
            ("白いシャツを買いました。", "8. Compré una camisa blanca.", "しろいシャツをかいました"),
            ("緑の車が好きです。", "9. Me gustan los autos verdes (Midori usa no).", "みどりのくるまがすきです"),
            ("日本語の勉強はどうですか。", "10. ¿Qué tal el estudio del japonés?", "にほんごのべんきょうはどうですか")
        ],
        "exercises": [
            {"q": "¿Cuál de las siguientes palabras NO es un adjetivo-i a pesar de terminar en 'i'?", "options": [{"text": "大きい (ookii)", "correct": False}, {"text": "きれい (kirei)", "correct": True}, {"text": "小さい (chiisai)", "correct": False}]},
            {"q": "¿Cómo se dice 'Libro viejo'? (Viejo = 古い furui)", "options": [{"text": "古いな本", "correct": False}, {"text": "古い本", "correct": True}, {"text": "古いの本", "correct": False}]},
            {"q": "¿Cómo se dice 'Persona famosa'? (Famoso = 有名 yuumei, Adj-na)", "options": [{"text": "有名人", "correct": False}, {"text": "有名な人", "correct": True}, {"text": "有名の人", "correct": False}]},
            {"q": "Negativo de 暑い (atsui - caluroso):", "options": [{"text": "暑いじゃないです", "correct": False}, {"text": "暑くないです", "correct": True}, {"text": "暑くありませんでした", "correct": False}]},
            {"q": "Pasado de 暇 (hima - libre, Adj-na):", "options": [{"text": "暇でした", "correct": True}, {"text": "暇かった", "correct": False}, {"text": "暇なでした", "correct": False}]},
            {"q": "¿Qué color requiere la partícula の para modificar un sustantivo? (Ej. Zapatos marrones)", "options": [{"text": "赤 (Rojo)", "correct": False}, {"text": "茶色 (Marrón)", "correct": True}, {"text": "黒 (Negro)", "correct": False}]},
            {"q": "¿Cómo se dice 'Ayer NO hizo frío'? (Samui - Frío)", "options": [{"text": "寒くなかったです / 寒くありませんでした", "correct": True}, {"text": "寒くないでした", "correct": False}, {"text": "寒かったじゃありません", "correct": False}]},
            {"q": "El adjetivo 'いい' (ii - bueno) es irregular. Su forma negativa es:", "options": [{"text": "いくない", "correct": False}, {"text": "よくない", "correct": True}, {"text": "いいじゃない", "correct": False}]},
            {"q": "'El examen fue fácil' (Kantanna - Adj-na):", "options": [{"text": "テストは簡単でした。", "correct": True}, {"text": "テストは簡単かった。", "correct": False}, {"text": "テストは簡単なでした。", "correct": False}]},
            {"q": "Une dos oraciones: 'El cuarto es estrecho PERO está limpio'.", "options": [{"text": "狭いからきれいです。", "correct": False}, {"text": "狭いですが、きれいです。", "correct": True}, {"text": "狭いときれいです。", "correct": False}]}
        ]
    }
}

def generate():
    base_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\lessons"
    
    for i in range(1, 6):
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
    <title>Examen para el JLPT5 - Lección {i}</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=Noto+Sans+JP:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../css/style.css">
</head>
<body class="iframe-body">
    <div class="max-w-4xl">
        <div class="lesson-header-simple">
            <span>JLPT N5 - 準備</span>
            <h1>Examen para el JLPT5 - Lección {i}</h1>
            <p class="lesson-desc">Tema: {d["title"]}</p>
        </div>

        <div class="video-link-section" style="text-align: center; margin: 2rem 0; padding: 2.5rem; background: linear-gradient(135deg, var(--secondary-color) 0%, #2a2a4a 100%); border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
            <h3 style="color: white; margin-bottom: 0.5rem; font-size: 1.5rem;">🎬 Clase en Video</h3>
            <p style="color: #cbd5e0; margin-bottom: 1.5rem; font-size: 1.05rem;">Estudia los fundamentos del nivel N5 en el canal de Kira Sensei.</p>
            <a href="https://www.youtube.com/results?search_query=Kira+Sensei+JLPT+N5" target="_blank" style="display: inline-block; background: var(--primary-color); color: white; padding: 1rem 2.5rem; border-radius: 50px; text-decoration: none; font-weight: 700; font-size: 1.15rem; transition: transform 0.2s, box-shadow 0.2s; box-shadow: 0 4px 15px rgba(224, 42, 77, 0.4);" onmouseover="this.style.transform='translateY(-3px)'; this.style.boxShadow='0 6px 20px rgba(224, 42, 77, 0.6)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 15px rgba(224, 42, 77, 0.4)'">Buscar Videos N5 en YouTube</a>
        </div>

        <h2 class="section-title">📚 Gramática Principal</h2>
        <div class="grammar-note">
            <ul>
{grammar_html}            </ul>
        </div>
        
        <h2 class="section-title">🌟 10 Ejemplos de Uso</h2>
        <div class="grammar-note"><p>A continuación, 10 ejemplos clave para dominar este tema en el examen N5.</p></div>
{examples_html}
        <h2 class="section-title">📝 Ejercicios de Práctica JLPT</h2>
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

        with open(os.path.join(base_dir, f"jlpt-n5-{i}.html"), "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated JLPT N5 Lesson {i}")

if __name__ == '__main__':
    generate()
