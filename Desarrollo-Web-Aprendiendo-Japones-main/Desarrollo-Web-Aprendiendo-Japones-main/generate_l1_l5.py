import os

data = {
    1: {
        "title": "Presentaciones y Ser/Estar (N1 は N2 です)",
        "grammar": [
            "<strong>N1 は N2 です:</strong> 'N1 es N2'. は (wa) marca el tema. です (desu) es el verbo ser formal.",
            "<strong>N1 は N2 じゃありません:</strong> 'N1 no es N2'. Es la forma negativa de です.",
            "<strong>~か:</strong> Partícula que se pone al final de la oración para convertirla en pregunta.",
            "<strong>~も:</strong> Significa 'también'. Sustituye a la partícula は."
        ],
        "examples": [
            ("私はマイク・ミラーです。", "1. Yo soy Mike Miller.", "わたしはマイク・ミラーです"),
            ("サントスさんは学生じゃありません。", "2. El señor Santos no es estudiante.", "サントスさんはがくせいじゃありません"),
            ("ミラーさんは会社員ですか。", "3. ¿El señor Miller es empleado de empresa?", "ミラーさんはかいしゃいんですか"),
            ("はい、会社員です。", "4. Sí, es empleado de empresa.", "はい、かいしゃいんです"),
            ("いいえ、医者じゃありません。", "5. No, no es médico.", "いいえ、いしゃじゃありません"),
            ("グプタさんも会社員です。", "6. El señor Gupta también es empleado de empresa.", "グプタさんもかいしゃいんです"),
            ("あの方はどなたですか。", "7. ¿Quién es aquella persona?", "あのかたはどなたですか"),
            ("ワットさんはさくら大学の先生です。", "8. El señor Watt es profesor de la Universidad Sakura (A de B).", "ワットさんはさくらだいがくのせんせいです"),
            ("テレザちゃんは９歳です。", "9. Teresa tiene 9 años.", "テレザちゃんはきゅうさいです"),
            ("太郎君は何歳ですか。", "10. ¿Cuántos años tiene Taro?", "たろうくんはなんさいですか")
        ],
        "exercises": [
            {"q": "¿Qué partícula marca el tema principal de la oración?", "options": [{"text": "が (ga)", "correct": False}, {"text": "は (wa)", "correct": True}, {"text": "を (wo)", "correct": False}]},
            {"q": "¿Cuál es la forma negativa de です (desu)?", "options": [{"text": "ではありません / じゃありません", "correct": True}, {"text": "でした", "correct": False}, {"text": "ません", "correct": False}]},
            {"q": "'Yo soy estudiante':", "options": [{"text": "私は学生です。", "correct": True}, {"text": "私が学生です。", "correct": False}, {"text": "私は学生か。", "correct": False}]},
            {"q": "'El Sr. Tanaka NO es profesor':", "options": [{"text": "田中さんは先生じゃありません。", "correct": True}, {"text": "田中さんは先生です。", "correct": False}, {"text": "田中さんは先生でした。", "correct": False}]},
            {"q": "¿Cómo conviertes una afirmación en pregunta?", "options": [{"text": "Agregando の al final.", "correct": False}, {"text": "Agregando か al final.", "correct": True}, {"text": "Agregando ね al final.", "correct": False}]},
            {"q": "Persona A: 'Soy estudiante'. Persona B: 'Yo _____ soy estudiante'.", "options": [{"text": "私は学生です。", "correct": False}, {"text": "私と学生です。", "correct": False}, {"text": "私も学生です。", "correct": True}]},
            {"q": "¿Qué significa 'あの方はどなたですか'?", "options": [{"text": "¿Dónde está él?", "correct": False}, {"text": "¿Quién es aquella persona? (Formal)", "correct": True}, {"text": "¿Cómo está esa persona?", "correct": False}]},
            {"q": "¿Cómo unes dos sustantivos para indicar pertenencia? (Ej. Profesor DE la universidad)", "options": [{"text": "大学と先生", "correct": False}, {"text": "大学の先生", "correct": True}, {"text": "大学に先生", "correct": False}]},
            {"q": "¿Qué se usa después del nombre de un niño o niña pequeña?", "options": [{"text": "さん (-san)", "correct": False}, {"text": "君 (-kun) / ちゃん (-chan)", "correct": True}, {"text": "様 (-sama)", "correct": False}]},
            {"q": "'¿Cuántos años tienes?' (Informal/Estándar):", "options": [{"text": "何歳ですか。", "correct": True}, {"text": "おいくつですか。", "correct": False}, {"text": "何年ですか。", "correct": False}]}
        ]
    },
    2: {
        "title": "Demostrativos (これ / それ / あれ)",
        "grammar": [
            "<strong>これ / それ / あれ:</strong> Pronombres demostrativos. Esto (cerca mío), Eso (cerca tuyo), Aquello (lejos de ambos).",
            "<strong>この / その / あの + Sustantivo:</strong> Adjetivos demostrativos. Este libro, Ese libro, Aquel libro.",
            "<strong>そうです / そうじゃありません:</strong> 'Así es' / 'No es así'. Se usa para confirmar o negar preguntas de sustantivos.",
            "<strong>N1 の N2:</strong> La partícula の indica posesión (Mi libro), origen/creador, o contenido (Un libro DE informática)."
        ],
        "examples": [
            ("これは辞書です。", "1. Esto es un diccionario.", "これはじしょです"),
            ("それは私の傘です。", "2. Eso es mi paraguas.", "それはわたしのかさです"),
            ("あれは誰のかばんですか。", "3. ¿De quién es aquel bolso?", "あれはだれのかばんですか"),
            ("この本は私のです。", "4. Este libro es mío.", "このほんはわたしのです"),
            ("そのカメラはスミスさんのですか。", "5. ¿Esa cámara es del Sr. Smith?", "そのカメラはスミスさんのですか"),
            ("はい、そうです。", "6. Sí, así es.", "はい、そうです"),
            ("いいえ、違います。", "7. No, es distinto (no es así).", "いいえ、ちがいます"),
            ("これはコンピューターの本です。", "8. Este es un libro de computadoras (contenido).", "これはコンピューターのほんです"),
            ("これは何の雑誌ですか。", "9. ¿De qué es esta revista?", "これはなんのざっしですか"),
            ("あれは日本の車です。", "10. Aquel es un auto de Japón (origen).", "あれはにほんのくるまです")
        ],
        "exercises": [
            {"q": "¿Cuál significa 'Esto' (algo cerca del que habla)?", "options": [{"text": "これ (kore)", "correct": True}, {"text": "それ (sore)", "correct": False}, {"text": "あれ (are)", "correct": False}]},
            {"q": "Si señalas algo que está muy lejos de ti y de con quien hablas, dices:", "options": [{"text": "これ", "correct": False}, {"text": "それ", "correct": False}, {"text": "あれ", "correct": True}]},
            {"q": "¿Cuál es la forma correcta para decir 'Este libro'?", "options": [{"text": "これ本", "correct": False}, {"text": "この本", "correct": True}, {"text": "本これ", "correct": False}]},
            {"q": "'Eso es mi paraguas':", "options": [{"text": "あれは私の傘です。", "correct": False}, {"text": "これは私の傘です。", "correct": False}, {"text": "それは私の傘です。", "correct": True}]},
            {"q": "¿Cómo respondes 'Sí, así es' a una pregunta de identidad (ej. ¿Es un diccionario?)", "options": [{"text": "はい、そうです。", "correct": True}, {"text": "はい、あります。", "correct": False}, {"text": "はい、違います。", "correct": False}]},
            {"q": "¿Cómo dices 'No, no es así / te equivocas'?", "options": [{"text": "いいえ、そうじゃありません。", "correct": True}, {"text": "いいえ、そうです。", "correct": False}, {"text": "いいえ、ありません。", "correct": False}]},
            {"q": "'Este bolso es MÍO':", "options": [{"text": "このかばんは私のですね。", "correct": False}, {"text": "このかばんは私のです。", "correct": True}, {"text": "このかばんは私です。", "correct": False}]},
            {"q": "'¿De qué es este libro?' (Contenido):", "options": [{"text": "何の本ですか。", "correct": True}, {"text": "誰の本ですか。", "correct": False}, {"text": "どこ本ですか。", "correct": False}]},
            {"q": "'¿De quién es aquel escritorio?' (Posesión):", "options": [{"text": "あれは何の机ですか。", "correct": False}, {"text": "あれは誰の机ですか。", "correct": True}, {"text": "あれは私の机ですか。", "correct": False}]},
            {"q": "Uso de 'の' para origen/marca. 'Un auto de la empresa Toyota':", "options": [{"text": "トヨタは車です。", "correct": False}, {"text": "トヨタの車です。", "correct": True}, {"text": "車のトヨタです。", "correct": False}]}
        ]
    },
    3: {
        "title": "Lugares (ここ / そこ / あそこ)",
        "grammar": [
            "<strong>ここ / そこ / あそこ / どこ:</strong> Aquí, Ahí, Allí, ¿Dónde?. Se refieren a lugares.",
            "<strong>こちら / そちら / あちら / どちら:</strong> Por aquí, Por ahí, Por allí, ¿Por dónde?. Forma muy educada (Keigo) de indicar lugares, direcciones, o incluso personas.",
            "<strong>N1 (Lugar/Cosa/Persona) は N2 (Lugar) です:</strong> Para indicar dónde está algo o alguien.",
            "<strong>País / Empresa + の + Producto:</strong> 'Computadora de Apple', 'Vino de Francia'."
        ],
        "examples": [
            ("ここは教室です。", "1. Aquí es el aula.", "ここはきょうしつです"),
            ("トイレはあそこです。", "2. El baño está allí.", "トイレはあそこです"),
            ("エレベーターはどちらですか。", "3. ¿Por dónde (dónde) está el ascensor?", "エレベーターはどちらですか"),
            ("あちらです。", "4. Es por allí (muy formal).", "あちらです"),
            ("山田さんはどこですか。", "5. ¿Dónde está el señor Yamada?", "やまださんはどこですか"),
            ("会議室です。", "6. Está en la sala de reuniones.", "かいぎしつです"),
            ("お国はどちらですか。", "7. ¿De qué país es usted? (Literal: Su país, ¿dónde es?)", "おくにはどちらですか"),
            ("これはどこのワインですか。", "8. ¿De dónde es este vino?", "これはどこのワインですか"),
            ("フランスのワインです。", "9. Es vino de Francia.", "フランスのワインです"),
            ("このネクタイはいくらですか。", "10. ¿Cuánto cuesta esta corbata?", "このネクタイはいくらですか")
        ],
        "exercises": [
            {"q": "¿Qué palabra significa 'Aquí'?", "options": [{"text": "そこ", "correct": False}, {"text": "ここ", "correct": True}, {"text": "あそこ", "correct": False}]},
            {"q": "Si quieres preguntar '¿Dónde está el baño?', dices:", "options": [{"text": "トイレはどこですか。", "correct": True}, {"text": "トイレはここですか。", "correct": False}, {"text": "トイレはなんですか。", "correct": False}]},
            {"q": "¿Cuál es la forma muy educada de decir '¿Dónde / Por dónde?'", "options": [{"text": "どこ", "correct": False}, {"text": "こちら", "correct": False}, {"text": "どちら", "correct": True}]},
            {"q": "'El Sr. Yamada está en la oficina':", "options": [{"text": "山田さんは事務所です。", "correct": True}, {"text": "事務所は山田さんです。", "correct": False}, {"text": "山田さんはここです。", "correct": False}]},
            {"q": "Si atiendes a un cliente y le muestras el camino diciendo 'Es por aquí':", "options": [{"text": "あちらです。", "correct": False}, {"text": "こちらです。", "correct": True}, {"text": "そちらです。", "correct": False}]},
            {"q": "¿Cómo preguntas muy formalmente '¿De qué país es usted?'", "options": [{"text": "国はどこですか。", "correct": False}, {"text": "お国はどちらですか。", "correct": True}, {"text": "お国はなんですか。", "correct": False}]},
            {"q": "'¿De qué empresa es este teléfono?':", "options": [{"text": "これはどこの電話ですか。", "correct": True}, {"text": "これは何の電話ですか。", "correct": False}, {"text": "これは誰の電話ですか。", "correct": False}]},
            {"q": "Para preguntar el precio de un objeto se usa:", "options": [{"text": "いくつですか", "correct": False}, {"text": "いくらですか", "correct": True}, {"text": "なんですか", "correct": False}]},
            {"q": "'Esta cámara cuesta 10,000 yenes':", "options": [{"text": "このカメラは一万円です。", "correct": True}, {"text": "このカメラは一万です。", "correct": False}, {"text": "このカメラは千円です。", "correct": False}]},
            {"q": "En una tienda departamental, '¿En qué piso (planta) estamos?'", "options": [{"text": "何階ですか。(Nangai desu ka)", "correct": True}, {"text": "何階ですか。(Nankai desu ka)", "correct": False}, {"text": "どこ階ですか。", "correct": False}]}
        ]
    },
    4: {
        "title": "La Hora y Verbos Básicos (~ます)",
        "grammar": [
            "<strong>今 ~時 ~分です:</strong> 'Ahora son las X y Y minutos'.",
            "<strong>Verbos (Forma ます):</strong> Expresan hábitos o futuro. Su negativo es ~ません. El pasado es ~ました. Y el pasado negativo es ~ませんでした.",
            "<strong>N (Tiempo) に Verbo:</strong> La partícula に señala el momento exacto en que ocurre la acción (a las 6, el domingo).",
            "<strong>~から ~まで:</strong> 'Desde ~ Hasta ~'. Se usa con tiempos y lugares."
        ],
        "examples": [
            ("今４時５分です。", "1. Ahora son las 4:05.", "いまよじごふんです"),
            ("私は毎朝６時に起きます。", "2. Yo me levanto todas las mañanas a las 6.", "わたしはまいあさろくじにおきます"),
            ("昨日の晩、勉強しました。", "3. Anoche estudié.", "きのうのばん、べんきょうしました"),
            ("昨日の晩、勉強しませんでした。", "4. Anoche no estudié.", "きのうのばん、べんきょうしませんでした"),
            ("銀行は９時から３時までです。", "5. El banco es de 9 a 3.", "ぎんこうはくじからさんじまでです"),
            ("毎日９時から５時まで働きます。", "6. Trabajo todos los días desde las 9 hasta las 5.", "まいにちくじからごじまではたらきます"),
            ("明日働きません。", "7. Mañana no trabajaré.", "あしたはたらきません"),
            ("昼休みは１２時半からです。", "8. El descanso de mediodía es a partir de las 12:30.", "ひるやすみはじゅうにじはんからです"),
            ("今日は何曜日ですか。", "9. ¿Qué día de la semana es hoy?", "きょうはなんようびですか"),
            ("月曜日です。", "10. Es lunes.", "げつようびです")
        ],
        "exercises": [
            {"q": "¿Cómo se dice 'Son las 4'? (Cuidado con la pronunciación)", "options": [{"text": "しじです (Shiji desu)", "correct": False}, {"text": "よじです (Yoji desu)", "correct": True}, {"text": "よんじです (Yonji desu)", "correct": False}]},
            {"q": "¿Cómo se dice 'y media' (Ej. 1:30)?", "options": [{"text": "いちじさんじゅっぷん", "correct": False}, {"text": "いちじはん", "correct": True}, {"text": "Ambas son correctas", "correct": True}]},
            {"q": "La terminación verbal que indica PASADO AFIRMATIVO es:", "options": [{"text": "~ます", "correct": False}, {"text": "~ました", "correct": True}, {"text": "~ませんでした", "correct": False}]},
            {"q": "La terminación verbal que indica PRESENTE/FUTURO NEGATIVO es:", "options": [{"text": "~ません", "correct": True}, {"text": "~ました", "correct": False}, {"text": "~ませんでした", "correct": False}]},
            {"q": "'Me levanto A las 6' (Partícula de tiempo exacto):", "options": [{"text": "６時がおきます。", "correct": False}, {"text": "６時におきます。", "correct": True}, {"text": "６時をおきます。", "correct": False}]},
            {"q": "¿Qué significa 'から' y 'まで'?", "options": [{"text": "Desde / Hasta", "correct": True}, {"text": "Con / Sin", "correct": False}, {"text": "Aquí / Allá", "correct": False}]},
            {"q": "'Estudio desde las 9 hasta las 5':", "options": [{"text": "９時まで５時から勉強します。", "correct": False}, {"text": "９時から５時まで勉強します。", "correct": True}, {"text": "９時に５時に勉強します。", "correct": False}]},
            {"q": "¿Por qué no se usa 'に' con '明日' (Mañana) o '毎日' (Todos los días)?", "options": [{"text": "Porque son palabras relativas de tiempo, no puntos exactos en el reloj/calendario.", "correct": True}, {"text": "Porque son sustantivos irregulares.", "correct": False}, {"text": "Porque se usa la partícula を en su lugar.", "correct": False}]},
            {"q": "'Ayer no estudié':", "options": [{"text": "昨日勉強しませんでした。", "correct": True}, {"text": "昨日勉強しました。", "correct": False}, {"text": "昨日勉強しません。", "correct": False}]},
            {"q": "¿Cómo preguntas 'Qué día de la semana es hoy'?", "options": [{"text": "今日は何日ですか。", "correct": False}, {"text": "今日は何曜日ですか。", "correct": True}, {"text": "今日は何時ですか。", "correct": False}]}
        ]
    },
    5: {
        "title": "Verbos de Movimiento (行く, 来る, 帰る)",
        "grammar": [
            "<strong>N (Lugar) へ 行きます/来ます/帰ります:</strong> La partícula へ (e) marca la dirección hacia un lugar.",
            "<strong>N (Vehículo) で 行きます:</strong> La partícula で marca el medio de transporte o instrumento (En tren, en taxi). Si vas caminando se usa '歩いて' sin partícula.",
            "<strong>N (Persona/Animal) と 行きます:</strong> La partícula と significa 'con' (Compañía).",
            "<strong>いつ:</strong> Pronombre interrogativo que significa '¿Cuándo?' (No usa partícula に)."
        ],
        "examples": [
            ("私は京都へ行きます。", "1. Yo voy a Kioto.", "わたしはきょうとへいきます"),
            ("日曜日どこへも行きませんでした。", "2. El domingo no fui a ningún lado.", "にちようびどこへもいきませんでした"),
            ("電車で東京へ行きます。", "3. Voy a Tokio en tren.", "でんしゃでとうきょうへいきます"),
            ("歩いて学校へ行きます。", "4. Voy caminando a la escuela.", "あるいてがっこうへいきます"),
            ("友達と日本へ来ました。", "5. Vine a Japón con un amigo.", "ともだちとにほんへきました"),
            ("一人でうちへ帰ります。", "6. Vuelvo a casa solo.", "ひとりでうちへかえります"),
            ("いつ日本へ来ましたか。", "7. ¿Cuándo viniste a Japón?", "いつにほんへきましたか"),
            ("３月２５日に来ました。", "8. Vine el 25 de marzo.", "さんがつにじゅうごにちにきました"),
            ("来週、病院へ行きます。", "9. La próxima semana iré al hospital.", "らいしゅう、びょういんへいきます"),
            ("誰とスーパーへ行きますか。", "10. ¿Con quién vas al supermercado?", "だれとスーパーへいきますか")
        ],
        "exercises": [
            {"q": "¿Qué verbos conforman el grupo básico de movimiento?", "options": [{"text": "行く (Ir), 来る (Venir), 帰る (Volver a casa)", "correct": True}, {"text": "食べる (Comer), 飲む (Beber), 見る (Ver)", "correct": False}, {"text": "読む (Leer), 書く (Escribir), 聞く (Oír)", "correct": False}]},
            {"q": "¿Qué partícula señala la DIRECCIÓN a la que te diriges? (Ej. Voy a Kioto)", "options": [{"text": "へ (e)", "correct": True}, {"text": "を (wo)", "correct": False}, {"text": "で (de)", "correct": False}]},
            {"q": "¿Qué partícula señala el MEDIO DE TRANSPORTE? (Ej. Voy en avión)", "options": [{"text": "に (ni)", "correct": False}, {"text": "で (de)", "correct": True}, {"text": "と (to)", "correct": False}]},
            {"q": "'Voy caminando' (Excepción que no lleva partícula):", "options": [{"text": "歩いて (Aruite)", "correct": True}, {"text": "足で (Ashi de)", "correct": False}, {"text": "歩きで (Aruki de)", "correct": False}]},
            {"q": "¿Qué partícula se usa para indicar LA COMPAÑÍA? (Ej. Fui con un amigo)", "options": [{"text": "へ (e)", "correct": False}, {"text": "で (de)", "correct": False}, {"text": "と (to)", "correct": True}]},
            {"q": "'Voy solo' (Excepción):", "options": [{"text": "一人と行きます。", "correct": False}, {"text": "一人で行きます。", "correct": True}, {"text": "一人に行きます。", "correct": False}]},
            {"q": "¿Cómo dices 'No fui a ningún lado'?", "options": [{"text": "どこも行きませんでした。", "correct": True}, {"text": "どこへ行きました。", "correct": False}, {"text": "どこか行きませんでした。", "correct": False}]},
            {"q": "¿Qué pronombre interrogativo significa '¿Cuándo?'", "options": [{"text": "だれ (Dare)", "correct": False}, {"text": "どこ (Doko)", "correct": False}, {"text": "いつ (Itsu)", "correct": True}]},
            {"q": "¿La palabra 'いつ' (Cuándo) necesita la partícula に detrás?", "options": [{"text": "Sí (いつに)", "correct": False}, {"text": "No, nunca la lleva.", "correct": True}, {"text": "Solo en pasado.", "correct": False}]},
            {"q": "'¿Con quién fuiste a Tokio?':", "options": [{"text": "誰と東京へ行きましたか。", "correct": True}, {"text": "誰で東京へ行きましたか。", "correct": False}, {"text": "誰に東京へ行きましたか。", "correct": False}]}
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
