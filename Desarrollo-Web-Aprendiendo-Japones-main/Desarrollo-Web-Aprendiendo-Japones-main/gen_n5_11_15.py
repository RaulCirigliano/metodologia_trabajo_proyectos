import os

data = {
    11: {
        "title": "Partícula も (También) y Contadores N5",
        "grammar": [
            "<strong>も (mo):</strong> Significa 'también'. Reemplaza a は, が y を. Ej: 私は学生です。彼も学生です (Yo soy estudiante. Él también es estudiante).",
            "<strong>何も / 誰も / どこも:</strong> Pronombres interrogativos + も + verbo negativo = Nada / Nadie / A ningún lado.",
            "<strong>Contadores:</strong> つ (Cosas), 人 (Personas), 枚 (Hojas/Plano), 台 (Máquinas), 匹 (Animales pequeños), 冊 (Libros)."
        ],
        "examples": [
            ("私も行きます。", "1. Yo también iré.", "わたしもいきます"),
            ("りんごを買いました。バナナも買いました。", "2. Compré manzanas. También compré bananas.", "りんごをかいました。バナナもかいました"),
            ("誰もいません。", "3. No hay nadie.", "だれもいません"),
            ("どこも行きませんでした。", "4. No fui a ningún lado.", "どこもいきませんでした"),
            ("何も食べません。", "5. No comeré nada.", "なにもたべません"),
            ("りんごを３つ食べました。", "6. Comí 3 manzanas.", "りんごをみっつたべました"),
            ("切手を５枚買いました。", "7. Compré 5 sellos (estampillas).", "きってをごまいかいました"),
            ("教室に学生が４人います。", "8. En el aula hay 4 estudiantes.", "きょうしつにがくせいがよにんいます"),
            ("犬が２匹います。", "9. Hay 2 perros.", "いぬがにひきいます"),
            ("車を１台買いたいです。", "10. Quiero comprar 1 auto.", "くるまをいちだいかいたいです")
        ],
        "exercises": [
            {"q": "¿Qué partícula reemplaza a は para decir 'También'?", "options": [{"text": "が", "correct": False}, {"text": "を", "correct": False}, {"text": "も", "correct": True}]},
            {"q": "'Tanaka es japonés. Suzuki TAMBIÉN es japonés': 鈴木さん__日本人です。", "options": [{"text": "も", "correct": True}, {"text": "はも", "correct": False}, {"text": "にも", "correct": False}]},
            {"q": "¿Qué significa '何も' (nani mo) con un verbo negativo?", "options": [{"text": "Todo", "correct": False}, {"text": "Nada", "correct": True}, {"text": "Algo", "correct": False}]},
            {"q": "'No vi a NADIE':", "options": [{"text": "誰も見ませんでした。", "correct": True}, {"text": "誰も見ました。", "correct": False}, {"text": "何も見ませんでした。", "correct": False}]},
            {"q": "¿Qué contador se usa para contar papeles, camisas o boletos (objetos planos)?", "options": [{"text": "つ (tsu)", "correct": False}, {"text": "枚 (mai)", "correct": True}, {"text": "本 (hon)", "correct": False}]},
            {"q": "¿Qué contador usarías para contar gatos o perros pequeños?", "options": [{"text": "台 (dai)", "correct": False}, {"text": "人 (nin)", "correct": False}, {"text": "匹 (hiki)", "correct": True}]},
            {"q": "'Compré DOS libros' (Libros usan el contador 冊 'satsu'):", "options": [{"text": "本を２冊買いました。", "correct": True}, {"text": "２冊本を買いました。", "correct": False}, {"text": "本の２冊を買いました。", "correct": False}]},
            {"q": "¿Cómo se dice '4 personas'?", "options": [{"text": "よんにん (Yonnin)", "correct": False}, {"text": "よにん (Yonin)", "correct": True}, {"text": "しにん (Shinin)", "correct": False}]},
            {"q": "¿Qué significa 'どこへも行きません'?", "options": [{"text": "No voy a ningún lado.", "correct": True}, {"text": "Voy a todos lados.", "correct": False}, {"text": "Voy a algún lado.", "correct": False}]},
            {"q": "¿Qué pasa con la partícula を si usas も? 'No comeré pan (pan mo)':", "options": [{"text": "パンをも食べません。", "correct": False}, {"text": "パンを も食べません。", "correct": False}, {"text": "パンも食べません。 (Se omite を)", "correct": True}]}
        ]
    },
    12: {
        "title": "Comparaciones N5 (より / ほうが)",
        "grammar": [
            "<strong>Aは Bより ~です:</strong> 'A es más ~ que B'.",
            "<strong>Aと Bと どちらが ~ですか:</strong> 'Entre A y B, ¿Cuál es más ~?'.",
            "<strong>Aの ほうが ~です:</strong> 'A es más ~' (Para responder a 'dochira').",
            "<strong>Nで 何/どこ/誰 が一番 ~ですか:</strong> 'De (grupo), ¿quién/qué es el número 1 (más ~)?'."
        ],
        "examples": [
            ("日本は韓国より大きいです。", "1. Japón es más grande que Corea del Sur.", "にほんはかんこくよりおおきいです"),
            ("電車はバスより速いです。", "2. El tren es más rápido que el autobús.", "でんしゃはバスよりはやいです"),
            ("肉と魚とどちらが好きですか。", "3. Entre la carne y el pescado, ¿cuál te gusta más?", "にくとさかなとどちらがすきですか"),
            ("肉のほうが好きです。", "4. Me gusta más la carne.", "にくのほうがすきです"),
            ("どちらも好きです。", "5. Me gustan ambos.", "どちらもすきです"),
            ("クラスで誰が一番背が高いですか。", "6. En la clase, ¿quién es el más alto?", "クラスでだれがいちばんせがたかいですか"),
            ("山田さんが一番背が高いです。", "7. El Sr. Yamada es el más alto.", "やまださんがいちばんせがたかいです"),
            ("季節でいつが一番好きですか。", "8. De las estaciones, ¿cuándo te gusta más?", "きせつでいつがいちばんすきですか"),
            ("秋が一番好きです。", "9. El otoño es lo que más me gusta.", "あきがいちばんすきです"),
            ("日本語は英語より難しいです。", "10. El japonés es más difícil que el inglés.", "にほんごはえいごよりむずかしいです")
        ],
        "exercises": [
            {"q": "¿Qué partícula usas para decir 'MÁS QUE' (comparación)?", "options": [{"text": "より (yori)", "correct": True}, {"text": "から (kara)", "correct": False}, {"text": "まで (made)", "correct": False}]},
            {"q": "'El tren es más rápido QUE el autobús':", "options": [{"text": "電車はバスから速いです。", "correct": False}, {"text": "電車はバスより速いです。", "correct": True}, {"text": "バスは電車より速いです。", "correct": False}]},
            {"q": "¿Cómo preguntas 'ENTRE A y B, ¿Cuál prefieres?'?", "options": [{"text": "A と B と なにが好きですか。", "correct": False}, {"text": "A と B と どれが好きですか。", "correct": False}, {"text": "A と B と どちらが好きですか。", "correct": True}]},
            {"q": "¿Cómo respondes 'Prefiero A'?", "options": [{"text": "Aが一番好きです。", "correct": False}, {"text": "Aが好きです。", "correct": False}, {"text": "Aのほうが好きです。", "correct": True}]},
            {"q": "'Prefiero AMBOS':", "options": [{"text": "どちらも好きです。", "correct": True}, {"text": "どちらが好きです。", "correct": False}, {"text": "どっちもが好きです。", "correct": False}]},
            {"q": "¿Qué palabra se usa para 'EL MÁS / Número Uno' (Superlativo)?", "options": [{"text": "たくさん (Takusan)", "correct": False}, {"text": "一番 (Ichiban)", "correct": True}, {"text": "とても (Totemo)", "correct": False}]},
            {"q": "'De tu familia, ¿quién es el más alto?':", "options": [{"text": "家族で何が一番高いですか。", "correct": False}, {"text": "家族で誰が一番高いですか。", "correct": True}, {"text": "家族から誰が一番高いですか。", "correct": False}]},
            {"q": "Persona A: '¿Te gusta más el té o el café?'. Persona B: 'Me gusta MÁS el café'.", "options": [{"text": "コーヒーのほうが好きです。", "correct": True}, {"text": "コーヒーより好きです。", "correct": False}, {"text": "コーヒーが一番好きです。", "correct": False}]},
            {"q": "¿Se puede usar どちら (dochira) para comparar TRES o MÁS cosas?", "options": [{"text": "Sí.", "correct": False}, {"text": "No, se usa どれ (dore) o 何/誰/どこ.", "correct": True}, {"text": "Sí, si se añade 'mo'.", "correct": False}]},
            {"q": "'Hoy hace más calor que ayer':", "options": [{"text": "今日は昨日より暑いです。", "correct": True}, {"text": "昨日は今日より暑いです。", "correct": False}, {"text": "今日は昨日のほうが暑いです。", "correct": False}]}
        ]
    },
    13: {
        "title": "Deseos N5 (欲しい / ~たい)",
        "grammar": [
            "<strong>N が 欲しい (hoshii):</strong> 'Quiero (objeto)'. Se conjuga como un Adjetivo-i (欲しかった, 欲しくない).",
            "<strong>V(raíz) + たい:</strong> 'Quiero hacer (verbo)'. El objeto directo puede ir con を o con が.",
            "<strong>Lugar へ V(raíz) に 行く/来る:</strong> 'Ir / Venir A (propósito)'. Ej: ご飯を食べに行きます (Voy a comer arroz)."
        ],
        "examples": [
            ("私は新しい車が欲しいです。", "1. Quiero un auto nuevo.", "わたしはあたらしいくるまがほしいです"),
            ("今、一番何が欲しいですか。", "2. Ahora, ¿qué es lo que más quieres?", "いま、いちばんなにがほしいですか"),
            ("日本の友達が欲しいです。", "3. Quiero un amigo japonés.", "にほんのともだちがほしいです"),
            ("私は日本へ行きたいです。", "4. Yo quiero ir a Japón.", "わたしはにほんへいきたいです"),
            ("何も食べたくないです。", "5. No quiero comer nada.", "なにもたべたくないです"),
            ("ビールを飲みたいです。", "6. Quiero beber cerveza.", "ビールをのみたいです"),
            ("日本へ日本語の勉強に来ました。", "7. Vine a Japón a estudiar japonés.", "にほんへにほんごのべんきょうにきました"),
            ("スーパーへ買い物に行きます。", "8. Voy al supermercado a hacer compras.", "スーパーへかいものにいきます"),
            ("どこかへ行きたいです。", "9. Quiero ir a algún lado.", "どこかへいきたいです"),
            ("何もしたくないです。", "10. No quiero hacer nada.", "なにもしたくないです")
        ],
        "exercises": [
            {"q": "¿Qué palabra usas para querer TENER un objeto (Ej. Quiero una cámara)?", "options": [{"text": "〜たい", "correct": False}, {"text": "欲しい (hoshii)", "correct": True}, {"text": "好き (suki)", "correct": False}]},
            {"q": "¿Qué palabra usas para querer HACER algo (Ej. Quiero comer)?", "options": [{"text": "欲しい", "correct": False}, {"text": "〜ます", "correct": False}, {"text": "〜たい (-tai)", "correct": True}]},
            {"q": "¿Cómo dices 'NO quiero ir'? (Negativo de ikitai)", "options": [{"text": "行きたくないです", "correct": True}, {"text": "行きたいじゃありません", "correct": False}, {"text": "行きないたいです", "correct": False}]},
            {"q": "¿Cómo conjugas 'Quería comer' (Pasado de tabetai)?", "options": [{"text": "食べたいでした", "correct": False}, {"text": "食べたかったです", "correct": True}, {"text": "食べたいかった", "correct": False}]},
            {"q": "'Fui a Kioto a VER un festival'. ¿Qué partícula marca el propósito 'VER'?", "options": [{"text": "お祭りを見で行きました。", "correct": False}, {"text": "お祭りを見に行きました。", "correct": True}, {"text": "お祭りを見るに行きました。", "correct": False}]},
            {"q": "¿Qué pasa con '買い物' (compras - sustantivo) para decir 'Fui de compras'?", "options": [{"text": "買い物をしに行きました (También válido)", "correct": True}, {"text": "買い物に行きました (Es lo más común con sustantivos de acción)", "correct": True}, {"text": "Ambas son correctas", "correct": True}]},
            {"q": "¿Cómo dices 'Quiero beber agua'? (Mizu = agua)", "options": [{"text": "水が欲しいです。", "correct": False}, {"text": "水が飲みたいです。(O 水を飲みたいです)", "correct": True}, {"text": "水に飲みたいです。", "correct": False}]},
            {"q": "Persona A: '¿Fuiste a algún lado?'. Persona B: 'No, no fui a ___'.", "options": [{"text": "どこも行きませんでした。", "correct": True}, {"text": "どこか行きませんでした。", "correct": False}, {"text": "何も行きませんでした。", "correct": False}]},
            {"q": "¿La partícula de objeto を (wo) puede cambiarse a が (ga) cuando se usa ~tai?", "options": [{"text": "Sí (Ej. 寿司が食べたい)", "correct": True}, {"text": "No, siempre debe ser を", "correct": False}, {"text": "No, siempre debe ser で", "correct": False}]},
            {"q": "'Quiero un coche caro' (Takai kuruma):", "options": [{"text": "高い車が欲しいです。", "correct": True}, {"text": "高い車を欲しいです。", "correct": False}, {"text": "高い車がたいです。", "correct": False}]}
        ]
    },
    14: {
        "title": "Verbos de Movimiento y Progresivo",
        "grammar": [
            "<strong>Verbos:</strong> 行く (Ir), 来る (Venir), 帰る (Volver a casa/país). Destino marcado con へ o に.",
            "<strong>Forma TE:</strong> G1 (i,chi,ri->tte / mi,bi,ni->nde / ki->ite / gi->ide / shi->shite). G2 (quita masu, pon te). G3 (shite, kite).",
            "<strong>V(te) います:</strong> 1) Acción en progreso (Estoy comiendo). 2) Estado resultante (Estoy casado). 3) Acción habitual (Trabajo en...).",
            "<strong>V(te) ください:</strong> Petición cortés."
        ],
        "examples": [
            ("今、雨が降っています。", "1. Ahora está lloviendo.", "いま、あめがふっています"),
            ("私は日本語を勉強しています。", "2. Yo estoy estudiando japonés.", "わたしはにほんごをべんきょうしています"),
            ("彼は手紙を書いています。", "3. Él está escribiendo una carta.", "かれはてがみをかいています"),
            ("私は結婚しています。", "4. Yo estoy casado (estado).", "わたしはけっこんしています"),
            ("大阪に住んでいます。", "5. Vivo en Osaka.", "おおさかにすんでいます"),
            ("ちょっと待ってください。", "6. Espera un momento, por favor.", "ちょっとまってください"),
            ("名前を書いてください。", "7. Por favor, escribe tu nombre.", "なまえをかいてください"),
            ("電話をかけています。", "8. Estoy haciendo una llamada telefónica.", "でんわをかけています"),
            ("IMCで働いています。", "9. Trabajo en IMC.", "アイエムシーではたらいています"),
            ("ゆっくり話してください。", "10. Por favor, habla despacio.", "ゆっくりはなしてください")
        ],
        "exercises": [
            {"q": "¿A qué grupo pertenece el verbo 食べます (Tabemasu)?", "options": [{"text": "Grupo I", "correct": False}, {"text": "Grupo II", "correct": True}, {"text": "Grupo III", "correct": False}]},
            {"q": "¿Cuál es la forma TE de 待ちます (Machimasu - Esperar)?", "options": [{"text": "まいて", "correct": False}, {"text": "まって (Matte)", "correct": True}, {"text": "まんで", "correct": False}]},
            {"q": "¿Cuál es la forma TE de 飲みます (Nomimasu - Beber)?", "options": [{"text": "のんで (Nonde)", "correct": True}, {"text": "のって", "correct": False}, {"text": "のみて", "correct": False}]},
            {"q": "¿Cuál es la forma TE de 行きます (Ikimasu - Ir)? (¡Excepción!)", "options": [{"text": "いいて", "correct": False}, {"text": "いって (Itte)", "correct": True}, {"text": "いんで", "correct": False}]},
            {"q": "¿Qué significa V(te) います (Te imasu)?", "options": [{"text": "Prohibición", "correct": False}, {"text": "Acción en progreso (Estar haciendo)", "correct": True}, {"text": "Deseo", "correct": False}]},
            {"q": "'Estoy leyendo un libro':", "options": [{"text": "本を読んでいます。", "correct": True}, {"text": "本を読みています。", "correct": False}, {"text": "本を読んでください。", "correct": False}]},
            {"q": "'El Sr. Yamada ESTÁ CASADO' (Estado):", "options": [{"text": "結婚します", "correct": False}, {"text": "結婚しました", "correct": False}, {"text": "結婚しています", "correct": True}]},
            {"q": "Persona A: '¿Qué estás haciendo?'. Persona B: 'Estoy mirando la TV'.", "options": [{"text": "テレビを見ています。", "correct": True}, {"text": "テレビを見ます。", "correct": False}, {"text": "テレビを見てください。", "correct": False}]},
            {"q": "'Por favor, enséñame tu pasaporte' (Mise-masu):", "options": [{"text": "パスポートを見せてください。", "correct": True}, {"text": "パスポートを見せってください。", "correct": False}, {"text": "パスポートを見しでください。", "correct": False}]},
            {"q": "¿Qué verbo usas para 'VIVIR / RESIDIR' en una ciudad (con 'te imasu')?", "options": [{"text": "働いています", "correct": False}, {"text": "住んでいます (Sunde imasu)", "correct": True}, {"text": "います", "correct": False}]}
        ]
    },
    15: {
        "title": "Permiso y Prohibición JLPT N5",
        "grammar": [
            "<strong>V(te) もいいですか:</strong> '¿Puedo hacer...?'. Sirve para pedir permiso.",
            "<strong>V(te) はいけません:</strong> 'No debes hacer...'. Prohibición estricta.",
            "<strong>Diferencias de cortesía:</strong> Para dar permiso a un superior no se dice 'いいですよ' (es condescendiente), se dice 'どうぞ' (Adelante)."
        ],
        "examples": [
            ("ここで写真を撮ってもいいですか。", "1. ¿Puedo tomar fotos aquí?", "ここでしゃしんをとってもいいですか"),
            ("ええ、いいですよ。", "2. Sí, por supuesto.", "ええ、いいですよ"),
            ("ここでタバコを吸ってはいけません。", "3. No debes fumar aquí (Está prohibido).", "ここでタバコをすってはいけません"),
            ("このカタログをもらってもいいですか。", "4. ¿Me puedo quedar (recibir) con este catálogo?", "このカタログをもらってもいいですか"),
            ("ええ、どうぞ。", "5. Sí, adelante.", "ええ、どうぞ"),
            ("車を止めてはいけません。", "6. No estaciones el coche (Prohibido aparcar).", "くるまをとめてはいけません"),
            ("入ってもいいですか。", "7. ¿Puedo entrar?", "はいってもいいですか"),
            ("ここで遊んではいけません。", "8. No debes jugar aquí.", "ここであそんではいけません"),
            ("窓を開けてもいいですか。", "9. ¿Puedo abrir la ventana?", "まどをあけてもいいですか"),
            ("触ってはいけません。", "10. No tocar (Está prohibido tocar).", "さわってはいけません")
        ],
        "exercises": [
            {"q": "¿Qué gramática usas para pedir PERMISO?", "options": [{"text": "V(te) はいけません", "correct": False}, {"text": "V(te) もいいですか", "correct": True}, {"text": "V(te) います", "correct": False}]},
            {"q": "¿Qué gramática usas para una PROHIBICIÓN estricta?", "options": [{"text": "V(te) はいけません", "correct": True}, {"text": "V(te) もいいですか", "correct": False}, {"text": "V(nai) でください", "correct": False}]},
            {"q": "'¿Puedo sentarme aquí?':", "options": [{"text": "ここに座ってもいいですか。", "correct": True}, {"text": "ここに座ってはいけません。", "correct": False}, {"text": "ここに座っていますか。", "correct": False}]},
            {"q": "'No debes beber alcohol aquí':", "options": [{"text": "お酒を飲んではいけません。", "correct": True}, {"text": "お酒を飲んでもいいですか。", "correct": False}, {"text": "お酒を飲みてはいけません。", "correct": False}]},
            {"q": "Respuesta correcta y natural si alguien pide permiso para usar tu bolígrafo: 'Sí, adelante'.", "options": [{"text": "ええ、いいですよ。/ ええ、どうぞ。", "correct": True}, {"text": "はい、いけません。", "correct": False}, {"text": "いいえ、いいですよ。", "correct": False}]},
            {"q": "¿Cómo rechazas CORTÉSMENTE un permiso sin sonar tan autoritario como 'ikemasen'?", "options": [{"text": "いいえ、いけません。", "correct": False}, {"text": "すみません、ちょっと...", "correct": True}, {"text": "ダメです。", "correct": False}]},
            {"q": "Persona A: '¿Puedo llevarme (recibir) esto?'. (Moraimasu)", "options": [{"text": "もらってもいいですか。", "correct": True}, {"text": "もらってはいけませんか。", "correct": False}, {"text": "もらいもいいですか。", "correct": False}]},
            {"q": "'No debes entrar en esa habitación' (Entrar = Hairimasu, Grupo I):", "options": [{"text": "入ってはいけません", "correct": True}, {"text": "入んではいけません", "correct": False}, {"text": "入りてはいけません", "correct": False}]},
            {"q": "'¿Puedo apagar la luz?' (Apagar = Keshimasu, Grupo I):", "options": [{"text": "消してもいいですか。", "correct": True}, {"text": "消しでもいいですか。", "correct": False}, {"text": "消してはいけませんか。", "correct": False}]},
            {"q": "¿Por qué 'いけません' (ikemasen) rara vez se usa para decirle a un jefe que no puede hacer algo?", "options": [{"text": "Porque indica una orden o prohibición de superior a inferior.", "correct": True}, {"text": "Porque es demasiado informal.", "correct": False}, {"text": "Porque significa 'Puedes hacerlo'.", "correct": False}]}
        ]
    }
}

def generate():
    base_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\lessons"
    
    for i in range(11, 16):
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
