import os

data = {
    16: {
        "title": "Secuencia de acciones y Adjetivos en forma TE",
        "grammar": [
            "<strong>V1(te), V2(te):</strong> Para conectar dos o más verbos en secuencia cronológica (Hago A y luego B).",
            "<strong>V1(te) から:</strong> 'Después de V1...'. Indica que la segunda acción ocurre Inmediatamente o a consecuencia de la primera.",
            "<strong>Adjetivos en forma TE:</strong> Para conectar oraciones descriptivas. Adj-i -> ~くて (大きくて). Adj-na / Sustantivos -> ~で (きれいで)."
        ],
        "examples": [
            ("朝６時に起きて、朝ごはんを食べます。", "1. Me levanto a las 6 de la mañana y desayuno.", "あさろくじにおきて、あさごはんをたべます"),
            ("図書館へ行って、本を借ります。", "2. Voy a la biblioteca y tomo prestado un libro.", "としょかんへいって、ほんをかります"),
            ("コンサートが終わってから、レストランで食事します。", "3. Después de que termine el concierto, comeremos en un restaurante.", "コンサートがおわってから、レストランでしょくじします"),
            ("お金を入れてから、ボタンを押してください。", "4. Por favor presiona el botón después de meter el dinero.", "おかねをいれてから、ボタンをおしてください"),
            ("この部屋は広くて、明るいです。", "5. Esta habitación es amplia y luminosa.", "このへやはひろくて、あかるいです"),
            ("神戸は静かで、きれいな町です。", "6. Kobe es una ciudad tranquila y hermosa.", "こうべはしずかで、きれいなまちです"),
            ("マリアさんは髪が長いです。", "7. María tiene el pelo largo.", "マリアさんはかみがながいです"),
            ("大阪は食べ物がおいしいです。", "8. En Osaka, la comida es deliciosa.", "おおさかはたべものがおいしいです"),
            ("カリナさんは学生で、マリアさんは主婦です。", "9. Karina es estudiante y María es ama de casa.", "カリナさんはがくせいで、マリアさんはしゅふです"),
            ("東京は人が多くて、にぎやかです。", "10. Tokio tiene mucha gente y es bulliciosa.", "とうきょうはひとがおおくて、にぎやかです")
        ],
        "exercises": [
            {"q": "¿Cómo conectas 'barato' (yasui) y 'delicioso' (oishii)?", "options": [{"text": "安いで、おいしいです。", "correct": False}, {"text": "安くて、おいしいです。", "correct": True}, {"text": "安から、おいしいです。", "correct": False}]},
            {"q": "¿Cómo conectas 'bonito/limpio' (kirei - Adj. Na) y 'tranquilo' (shizuka)?", "options": [{"text": "きれくて、静かです。", "correct": False}, {"text": "きれいで、静かです。", "correct": True}, {"text": "きれいから、静かです。", "correct": False}]},
            {"q": "¿Cómo describes a una persona con los ojos grandes?", "options": [{"text": "目が大きいです。", "correct": True}, {"text": "目を大きいです。", "correct": False}, {"text": "目と大きいです。", "correct": False}]},
            {"q": "'Me lavo las manos y como' (Lavarse = Araimasu):", "options": [{"text": "手を洗って、食べます。", "correct": True}, {"text": "手を洗いって、食べます。", "correct": False}, {"text": "手を洗んで、食べます。", "correct": False}]},
            {"q": "'Después de terminar el trabajo, voy a beber':", "options": [{"text": "仕事が終わってから、飲みに行きます。", "correct": True}, {"text": "仕事が終わるから、飲みに行きます。", "correct": False}, {"text": "仕事が終わって、飲みに行きます。", "correct": False}]},
            {"q": "¿Qué significa la conjunción de sustantivos '私は学生で、彼は医者です'?", "options": [{"text": "Yo soy estudiante, pero él es médico.", "correct": False}, {"text": "Yo soy estudiante y él es médico.", "correct": True}, {"text": "Yo soy estudiante porque él es médico.", "correct": False}]},
            {"q": "¿Cuál es la forma Te de いいです (Bueno)?", "options": [{"text": "いいて", "correct": False}, {"text": "よくて", "correct": True}, {"text": "いいで", "correct": False}]},
            {"q": "'El elefante (zou) tiene la nariz larga':", "options": [{"text": "象が鼻は長いです。", "correct": False}, {"text": "象は鼻が長いです。", "correct": True}, {"text": "象の鼻が長いです。(Gramatical, pero la forma aprendida usa Wa y Ga)", "correct": True}]},
            {"q": "'Fui a Kobe y vi una película':", "options": [{"text": "神戸へ行って、映画を見ました。", "correct": True}, {"text": "神戸へ行きました、映画を見ました。", "correct": False}, {"text": "神戸へ行って、映画を見ます。", "correct": False}]},
            {"q": "¿Cómo conectas '25 años' y 'Soltero' (Dokushin)?", "options": [{"text": "２５歳で、独身です。", "correct": True}, {"text": "２５歳くて、独身です。", "correct": False}, {"text": "２５歳と、独身です。", "correct": False}]}
        ]
    },
    17: {
        "title": "Forma NAI y Obligaciones",
        "grammar": [
            "<strong>Forma NAI (Negativa):</strong> G1(a+nai), G2(quita masu+nai), G3(shinai, konai). Ej. 書かない (no escribir).",
            "<strong>V(nai) でください:</strong> 'Por favor, no...'.",
            "<strong>V(nai) なければなりません:</strong> 'Tener que / Deber' (Obligación).",
            "<strong>V(nai) なくてもいいです:</strong> 'No tener que / No hacer falta que...'."
        ],
        "examples": [
            ("ここで写真を撮らないでください。", "1. Por favor, no tome fotos aquí.", "ここでしゃしんをとらないでください"),
            ("明日は早く起きなければなりません。", "2. Mañana tengo que levantarme temprano.", "あしたははやくおきなければなりません"),
            ("日曜日は起きなくてもいいです。", "3. El domingo no es necesario levantarse.", "にちようびはおきなくてもいいです"),
            ("パスポートを見せなければなりません。", "4. Tienes que enseñar el pasaporte.", "パスポートをみせなければなりません"),
            ("名前を書かなくてもいいです。", "5. No hace falta que escribas el nombre.", "なまえをかかなくてもいいです"),
            ("靴を脱がなくてもいいです。", "6. No hace falta quitarse los zapatos.", "くつをぬがなくてもいいです"),
            ("薬を飲まなければなりません。", "7. Debo tomar la medicina.", "くすりをのまなければなりません"),
            ("心配しないでください。", "8. Por favor, no te preocupes.", "しんぱいしないでください"),
            ("そこに入らないでください。", "9. Por favor, no entres ahí.", "そこにはいらないでください"),
            ("毎日日本語を勉強しなければなりません。", "10. Debo estudiar japonés todos los días.", "まいにちにほんごをべんきょうしなければなりません")
        ],
        "exercises": [
            {"q": "¿Cuál es la forma Nai de 読みます (Leer)?", "options": [{"text": "よみない (Yominai)", "correct": False}, {"text": "よまない (Yomanai)", "correct": True}, {"text": "よむない (Yomunai)", "correct": False}]},
            {"q": "¿Cuál es la forma Nai de 買います (Comprar - Termina en 'i' pura)?", "options": [{"text": "かあない (Kaanai)", "correct": False}, {"text": "かいない (Kainai)", "correct": False}, {"text": "かわない (Kawanai)", "correct": True}]},
            {"q": "¿Cuál es la forma Nai de 来ます (Kimasu - Venir)?", "options": [{"text": "こない (Konai)", "correct": True}, {"text": "きない (Kinai)", "correct": False}, {"text": "かない (Kanai)", "correct": False}]},
            {"q": "'Por favor, NO fumes':", "options": [{"text": "吸わなくてください", "correct": False}, {"text": "吸わないでください", "correct": True}, {"text": "吸わないてください", "correct": False}]},
            {"q": "¿Qué significa なければなりません (Nakereba narimasen)?", "options": [{"text": "No debo hacerlo.", "correct": False}, {"text": "Tengo que hacerlo (Obligación).", "correct": True}, {"text": "No es necesario hacerlo.", "correct": False}]},
            {"q": "'Tengo que ir al hospital':", "options": [{"text": "病院へ行かなければなりません。", "correct": True}, {"text": "病院へ行かなくてもいいです。", "correct": False}, {"text": "病院へ行かないでください。", "correct": False}]},
            {"q": "¿Qué significa なくてもいいです (Nakutemo ii desu)?", "options": [{"text": "Tienes que...", "correct": False}, {"text": "Está prohibido...", "correct": False}, {"text": "No tienes que / No es necesario...", "correct": True}]},
            {"q": "Persona A: '¿Tengo que pagar?'. Persona B: 'No, no es necesario pagar'.", "options": [{"text": "いいえ、払わないでください。", "correct": False}, {"text": "いいえ、払わなくてもいいです。", "correct": True}, {"text": "いいえ、払ってはいけません。", "correct": False}]},
            {"q": "'Por favor, no lo olvides':", "options": [{"text": "忘れないでください。", "correct": True}, {"text": "忘れないてください。", "correct": False}, {"text": "忘れるないでください。", "correct": False}]},
            {"q": "¿Qué significa '残業しなければなりません' (Zangyou shinakereba narimasen)?", "options": [{"text": "No debo hacer horas extras.", "correct": False}, {"text": "Tengo que hacer horas extras.", "correct": True}, {"text": "No es necesario hacer horas extras.", "correct": False}]}
        ]
    },
    18: {
        "title": "Forma Diccionario y Habilidades",
        "grammar": [
            "<strong>Forma Diccionario (Jishokei):</strong> G1 (i -> u). G2 (quita masu, pon ru). G3 (suru, kuru). Ej. 書く, 食べる.",
            "<strong>N / V(dic)こと ができます:</strong> 'Poder / Ser capaz de'.",
            "<strong>趣味は N / V(dic)こと です:</strong> 'Mi afición / pasatiempo es...'.",
            "<strong>V(dic) / Nの / Cantidad + 前に:</strong> 'Antes de...'."
        ],
        "examples": [
            ("私は日本語ができます。", "1. Yo sé (puedo hablar) japonés.", "わたしはにほんごができます"),
            ("私は漢字を読むことができます。", "2. Yo puedo leer kanjis.", "わたしはかんじをよむことができます"),
            ("ここで切符を買うことができます。", "3. Aquí se pueden comprar los boletos (posibilidad).", "ここできっぷをかうことができます"),
            ("私の趣味は映画を見ることです。", "4. Mi pasatiempo es ver películas.", "わたしのしゅみはえいがをみることです"),
            ("寝る前に、本を読みます。", "5. Antes de dormir, leo un libro.", "ねるまえに、ほんをよみます"),
            ("食事の前に、手を洗います。", "6. Antes de la comida, me lavo las manos.", "しょくじのまえに、てをあらいます"),
            ("５年前に日本へ来ました。", "7. Vine a Japón hace 5 años.", "ごねんまえににほんへきました"),
            ("ピアノを弾くことができますか。", "8. ¿Puedes tocar el piano?", "ピアノをひくことができますか"),
            ("はい、できます。", "9. Sí, sí puedo.", "はい、できます"),
            ("会議の前に、資料をコピーします。", "10. Antes de la reunión, fotocopio los documentos.", "かいぎのまえに、しりょうをコピーします")
        ],
        "exercises": [
            {"q": "¿Cuál es la Forma Diccionario de 飲みます (Nomimasu)?", "options": [{"text": "のめる (Nomeru)", "correct": False}, {"text": "のむ (Nomu)", "correct": True}, {"text": "のまる (Nomaru)", "correct": False}]},
            {"q": "¿Cuál es la Forma Diccionario de 見ます (Mimasu)?", "options": [{"text": "みる (Miru)", "correct": True}, {"text": "むる (Muru)", "correct": False}, {"text": "みう (Miu)", "correct": False}]},
            {"q": "¿Qué estructura expresa HABILIDAD / POSIBILIDAD?", "options": [{"text": "V(dic)ことができます", "correct": True}, {"text": "V(te)います", "correct": False}, {"text": "V(nai)でください", "correct": False}]},
            {"q": "'Mi pasatiempo es ESCUCHAR música':", "options": [{"text": "趣味は音楽を聞くです。", "correct": False}, {"text": "趣味は音楽を聞くことです。", "correct": True}, {"text": "趣味は音楽を聞きことです。", "correct": False}]},
            {"q": "¿Qué significa 前に (Mae ni)?", "options": [{"text": "Después de", "correct": False}, {"text": "Antes de / Hace...", "correct": True}, {"text": "Detrás de", "correct": False}]},
            {"q": "'Antes de venir a Japón, estudié japonés':", "options": [{"text": "日本へ来る前に、勉強しました。", "correct": True}, {"text": "日本へ来た前に、勉強しました。", "correct": False}, {"text": "日本へ来て前に、勉強しました。", "correct": False}]},
            {"q": "'Me lavo las manos antes de la COMIDA (Sustantivo)':", "options": [{"text": "食事前に、手を洗います。", "correct": False}, {"text": "食事の前に、手を洗います。", "correct": True}, {"text": "食事が前に、手を洗います。", "correct": False}]},
            {"q": "'Me casé HACE 3 AÑOS':", "options": [{"text": "３年の前に結婚しました。", "correct": False}, {"text": "３年前に結婚しました。", "correct": True}, {"text": "３年前で結婚しました。", "correct": False}]},
            {"q": "¿Se puede decir 'ピアノができます' (Puedo/Sé piano) con solo un sustantivo?", "options": [{"text": "Sí, si el sustantivo implica una habilidad o acción.", "correct": True}, {"text": "No, siempre hay que usar el verbo 'hiku' (tocar).", "correct": False}, {"text": "No, es incorrecto.", "correct": False}]},
            {"q": "Persona A: '¿Puedes comer pescado crudo?'. Persona B: 'No, no puedo'.", "options": [{"text": "いいえ、しません。", "correct": False}, {"text": "いいえ、できません。", "correct": True}, {"text": "いいえ、わかりません。", "correct": False}]}
        ]
    },
    19: {
        "title": "Forma TA, Experiencias y Cambios",
        "grammar": [
            "<strong>Forma TA:</strong> Pasado informal. Se conjuga idéntico a la Forma TE (Nomimasu -> Nonde -> Nonda).",
            "<strong>V(ta) ことがあります:</strong> 'Haber tenido la experiencia de...'.",
            "<strong>V(ta)り, V(ta)り します:</strong> 'Hacer cosas como A y B'.",
            "<strong>~なります:</strong> 'Volverse / Convertirse en'. Adj-i(~ku), Adj-na(~ni), Sust(~ni)."
        ],
        "examples": [
            ("馬に乗ったことがあります。", "1. He montado a caballo.", "うまにのったことがあります"),
            ("富士山に登ったことがありますか。", "2. ¿Has escalado el Monte Fuji alguna vez?", "ふじさんにのぼったことがありますか"),
            ("いいえ、一度もありません。", "3. No, ni una sola vez.", "いいえ、いちどもありません"),
            ("日曜日、テニスをしたり、映画を見たりしました。", "4. El domingo jugué tenis, vi películas, etc.", "にちようび、テニスをしたり、えいがをみたりしました"),
            ("寒くなりました。", "5. Se ha vuelto frío / Ha refrescado.", "さむくなりました"),
            ("テレザちゃんは背が高くなりました。", "6. Teresa se volvió más alta.", "テレザちゃんはせがたかくなりました"),
            ("元気になりました。", "7. Me curé (Me volví sano).", "げんきになりました"),
            ("２５歳になりました。", "8. Cumplí 25 años (Me convertí en alguien de 25).", "にじゅうごさいになりました"),
            ("夜は暗くなります。", "9. Por la noche se vuelve oscuro.", "よるはくらくなります"),
            ("医者になりたいです。", "10. Quiero convertirme en médico.", "いしゃになりたいです")
        ],
        "exercises": [
            {"q": "¿Cómo se forma el pasado informal de 飲みます (Forma TA)?", "options": [{"text": "のむた", "correct": False}, {"text": "のんだ (Nonda)", "correct": True}, {"text": "のった", "correct": False}]},
            {"q": "¿Qué estructura habla de EXPERIENCIAS (He estado en...)?", "options": [{"text": "V(ta) ことがあります", "correct": True}, {"text": "V(te) います", "correct": False}, {"text": "V(dic) ことができます", "correct": False}]},
            {"q": "'He ido a Japón':", "options": [{"text": "日本へ行ったことがあります。", "correct": True}, {"text": "日本へ行くことがあります。", "correct": False}, {"text": "日本へ行ったです。", "correct": False}]},
            {"q": "Para decir 'No, NUNCA lo he hecho' a una pregunta de experiencia:", "options": [{"text": "いいえ、しませんでした。", "correct": False}, {"text": "いいえ、一度もありません。", "correct": True}, {"text": "いいえ、行きませんでした。", "correct": False}]},
            {"q": "¿Qué usas para listar varias acciones típicas sin un orden fijo?", "options": [{"text": "V(te), V(te) します", "correct": False}, {"text": "V(ta)り、V(ta)り します", "correct": True}, {"text": "V(dic)と、V(dic)", "correct": False}]},
            {"q": "'El domingo limpié (souji), lavé ropa (sentaku)...':", "options": [{"text": "掃除したり、洗濯したりしました。", "correct": True}, {"text": "掃除して、洗濯してしました。", "correct": False}, {"text": "掃除した、洗濯したしました。", "correct": False}]},
            {"q": "¿Qué verbo significa 'Volverse / Convertirse en' (Cambio)?", "options": [{"text": "します", "correct": False}, {"text": "なります (Narimasu)", "correct": True}, {"text": "あります", "correct": False}]},
            {"q": "Con un Adjetivo-i (高い - Alto), 'Volverse alto' es:", "options": [{"text": "高いになります", "correct": False}, {"text": "高くなります", "correct": True}, {"text": "高にまります", "correct": False}]},
            {"q": "Con un Adjetivo-na (有名 - Famoso), 'Volverse famoso' es:", "options": [{"text": "有名くなります", "correct": False}, {"text": "有名になります", "correct": True}, {"text": "有名だになります", "correct": False}]},
            {"q": "'Me convertí en profesor' (Sustantivo):", "options": [{"text": "先生になりました。", "correct": True}, {"text": "先生くなりました。", "correct": False}, {"text": "先生がなりました。", "correct": False}]}
        ]
    },
    20: {
        "title": "Estilo Informal N5 (Futsukei)",
        "grammar": [
            "<strong>Futsukei:</strong> Estilo sin ~masu/~desu, usado con amigos y familia.",
            "<strong>Verbos:</strong> Pres(+) V(dic) | Pres(-) V(nai) | Pas(+) V(ta) | Pas(-) V(nakatta).",
            "<strong>Adjetivos-i:</strong> Omiten desu. (Ej: 高い, 高くない, 高かった, 高くなかった).",
            "<strong>Adj-na / Sustantivos:</strong> Pres(+) agregan だ. (Ej: 暇だ). Pas(+) agregan だった. Pres(-) ~じゃない. Pas(-) ~じゃなかった.",
            "<strong>Preguntas:</strong> Se quita か y se sube la entonación. Se pueden omitir partículas は, を, へ."
        ],
        "examples": [
            ("毎日新聞を読む？", "1. ¿Lees el periódico a diario? (Informal)", "まいにちしんぶんをよむ？"),
            ("うん、読む。", "2. Sí, lo leo.", "うん、よむ"),
            ("ううん、読まない。", "3. No, no lo leo.", "ううん、よまない"),
            ("昨日パソコンを買った？", "4. ¿Compraste una PC ayer?", "きのうパソコンをかった？"),
            ("うん、買った。", "5. Sí, compré.", "うん、かった"),
            ("今忙しい？", "6. ¿Estás ocupado?", "いまいそがしい？"),
            ("うん、忙しい。", "7. Sí, estoy ocupado.", "うん、いそがしい"),
            ("コーヒー飲む？", "8. ¿Bebes café? (Sin partícula 'wo')", "コーヒーのむ？"),
            ("ありがとう。もらう。", "9. Gracias. Lo acepto.", "ありがとう。もらう"),
            ("日曜日、暇？", "10. ¿El domingo estás libre? (Se omite 'da' en la pregunta)", "にちようび、ひま？")
        ],
        "exercises": [
            {"q": "¿Cuándo se usa el estilo informal (Futsukei)?", "options": [{"text": "Con jefes y clientes.", "correct": False}, {"text": "Con amigos cercanos y familia.", "correct": True}, {"text": "En entrevistas.", "correct": False}]},
            {"q": "Forma informal de 食べます (Presente afirmativo):", "options": [{"text": "食べる (Taberu)", "correct": True}, {"text": "食べた (Tabeta)", "correct": False}, {"text": "食べない (Tabenai)", "correct": False}]},
            {"q": "Forma informal de 食べません (Presente negativo):", "options": [{"text": "食べる (Taberu)", "correct": False}, {"text": "食べない (Tabenai)", "correct": True}, {"text": "食べなかった (Tabenakatta)", "correct": False}]},
            {"q": "Forma informal de 食べませんでした (Pasado negativo):", "options": [{"text": "食べない (Tabenai)", "correct": False}, {"text": "食べなかった (Tabenakatta)", "correct": True}, {"text": "食べた (Tabeta)", "correct": False}]},
            {"q": "¿Cómo haces una pregunta en estilo informal?", "options": [{"text": "Agregas か al final.", "correct": False}, {"text": "Subes la entonación y NO usas か.", "correct": True}, {"text": "Agregas だ al final.", "correct": False}]},
            {"q": "¿Cómo respondes 'SÍ' y 'NO' en estilo informal?", "options": [{"text": "はい / いいえ", "correct": False}, {"text": "うん / ううん", "correct": True}, {"text": "そう / そうじゃない", "correct": False}]},
            {"q": "Afirmación informal (Adj-na/Sust): 'Es bonito' (Kirei):", "options": [{"text": "きれいだ。", "correct": True}, {"text": "きれい。", "correct": False}, {"text": "きれいする。", "correct": False}]},
            {"q": "Pregunta informal (Adj-na): '¿Es bonito?':", "options": [{"text": "きれいだ？", "correct": False}, {"text": "きれい？ (Se omite el 'da' en la pregunta)", "correct": True}, {"text": "きれいか？", "correct": False}]},
            {"q": "¿Qué partículas se omiten frecuentemente al hablar informalmente?", "options": [{"text": "で, に", "correct": False}, {"text": "は, が, を", "correct": True}, {"text": "Ninguna", "correct": False}]},
            {"q": "¿Cómo se dice 'No hizo calor' (Atsuku arimasen deshita) en informal?", "options": [{"text": "暑くない", "correct": False}, {"text": "暑くなかった", "correct": True}, {"text": "暑かった", "correct": False}]}
        ]
    }
}

def generate():
    base_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\lessons"
    
    for i in range(16, 21):
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
