import os

data = {
    16: {
        "title": "Secuencia de Acciones y Unión de Frases (Forma TE)",
        "grammar": [
            "<strong>V(te), V(te), V:</strong> Se unen verbos en forma TE para indicar una secuencia cronológica de acciones. El tiempo verbal lo dicta el último verbo.",
            "<strong>V1(te)から、V2:</strong> 'Después de V1, hago V2'. Enfatiza que V2 ocurre inmediatamente después de V1.",
            "<strong>N1 は N2 が Adjetivo:</strong> Para describir una característica de algo. Ej: 'Osaka la comida es deliciosa' (大阪は食べ物がおいしいです).",
            "<strong>Unión de Adjetivos:</strong> Adj-i: quita い y pon くて (大きくて). Adj-na y Sustantivos: quita な/です y pon で (きれいで)."
        ],
        "examples": [
            ("朝ジョギングをして、シャワーを浴びて、会社へ行きます。", "1. Por la mañana troto, me ducho y voy a la empresa.", "あさジョギングをして、シャワーをあびて、かいしゃへいきます"),
            ("コンサートが終わってから、レストランで食事しました。", "2. Después de que terminó el concierto, cenamos en un restaurante.", "コンサートがおわってから、レストランでしょくじしました"),
            ("大阪は食べ物がおいしいです。", "3. En Osaka, la comida es deliciosa.", "おおさかはたべものがおいしいです"),
            ("マリアさんは髪が長いです。", "4. María tiene el cabello largo.", "マリアさんはかみがながいです"),
            ("この部屋は広くて、明るいです。", "5. Esta habitación es amplia y luminosa.", "このへやはひろくて、あかるいです"),
            ("神戸は静かで、きれいな町です。", "6. Kobe es una ciudad tranquila y hermosa.", "こうべはしずかで、きれいなまちです"),
            ("カリナさんは学生で、マリアさんは主婦です。", "7. Karina es estudiante y María es ama de casa.", "カリナさんはがくせいで、マリアさんはしゅふです"),
            ("お金を入れてから、ボタンを押してください。", "8. Por favor, presiona el botón después de meter el dinero.", "おかねをいれてから、ボタンをおしてください"),
            ("ミラーさんは若くて、元気です。", "9. El Sr. Miller es joven y enérgico.", "ミラーさんはわかくて、げんきです"),
            ("昨日、銀座へ行って、友達に会って、映画を見ました。", "10. Ayer fui a Ginza, me encontré con un amigo y vimos una película.", "きのう、ぎんざへいって、ともだちにあって、えいがをみました")
        ],
        "exercises": [
            {"q": "¿Cómo unes acciones en secuencia? 'Me levanto a las 6 y desayuno'", "options": [{"text": "６時に起きて、朝ごはんを食べます。", "correct": True}, {"text": "６時に起きます、朝ごはんを食べます。", "correct": False}, {"text": "６時に起きから、朝ごはんを食べます。", "correct": False}]},
            {"q": "¿Qué significa V1(te)から、V2 ?", "options": [{"text": "Antes de V1, V2", "correct": False}, {"text": "Después de V1, V2", "correct": True}, {"text": "Porque V1, V2", "correct": False}]},
            {"q": "¿Cómo unes un Adjetivo-i con otro adjetivo? (Ej. Barato y delicioso / 安い)", "options": [{"text": "安いで、おいしいです", "correct": False}, {"text": "安くて、おいしいです", "correct": True}, {"text": "安いと、おいしいです", "correct": False}]},
            {"q": "¿Cómo unes un Adjetivo-na con otro? (Ej. Amable y bonito / 親切)", "options": [{"text": "親切で、きれいです", "correct": True}, {"text": "親切くて、きれいです", "correct": False}, {"text": "親切なと、きれいです", "correct": False}]},
            {"q": "¿Cómo describes que 'Tokio tiene mucha gente'? (Tokio, la gente es mucha)", "options": [{"text": "東京は人が多いです。", "correct": True}, {"text": "東京が人多いです。", "correct": False}, {"text": "東京に人が多いです。", "correct": False}]},
            {"q": "'El elefante tiene la nariz larga':", "options": [{"text": "象が鼻は長いです。", "correct": False}, {"text": "象は鼻が長いです。", "correct": True}, {"text": "象の鼻は長いです。(Es gramatical, pero la estructura de la lección 16 es N1wa N2ga Adj).", "correct": True}]},
            {"q": "'¿Qué hiciste ayer?' (Uso de forma TE en pasado):", "options": [{"text": "神戸へ行って、映画を見ました。", "correct": True}, {"text": "神戸へ行きました、映画を見ました。", "correct": False}, {"text": "神戸へ行く、映画を見ました。", "correct": False}]},
            {"q": "¿Cómo unes dos oraciones con sustantivos? 'Yo soy estudiante y él es médico'", "options": [{"text": "私は学生くて、彼は医者です。", "correct": False}, {"text": "私は学生で、彼は医者です。", "correct": True}, {"text": "私は学生と、彼は医者です。", "correct": False}]},
            {"q": "'Después de terminar el trabajo, fui a beber':", "options": [{"text": "仕事が終わってから、飲みに行きました。", "correct": True}, {"text": "仕事が終わって、飲みに行きました。", "correct": False}, {"text": "仕事が終わるから、飲みに行きました。", "correct": False}]},
            {"q": "'Ella tiene los ojos grandes' (Ojo = 目 me):", "options": [{"text": "彼女は目が大きいです。", "correct": True}, {"text": "彼女は目を大きいです。", "correct": False}, {"text": "彼女が目は大きいです。", "correct": False}]}
        ]
    },
    17: {
        "title": "Forma NAI (Negativa) y Obligaciones",
        "grammar": [
            "<strong>Forma Nai:</strong> Es la forma negativa informal del verbo. G1: Cambia el sonido 'i' antes de 'masu' por 'a' y añade 'nai'. (Excepción: si es 'i' pura, cambia a 'wa'. Ej: kaimasu -> kawanai). G2: quita masu y pon nai. G3: suru->shinai, kuru->konai.",
            "<strong>V(nai) でください:</strong> 'Por favor NO hagas...'. Petición negativa.",
            "<strong>V(nai) なければなりません:</strong> 'Tener que / Deber'. Doble negación que indica obligación.",
            "<strong>V(nai) なくてもいいです:</strong> 'No es necesario / No tienes que...'."
        ],
        "examples": [
            ("ここで写真を撮らないでください。", "1. Por favor, no tome fotos aquí.", "ここでしゃしんをとらないでください"),
            ("パスポートを見せなければなりません。", "2. Tienes que mostrar el pasaporte.", "パスポートをみせなければなりません"),
            ("明日は早く起きなければなりません。", "3. Mañana tengo que levantarme temprano.", "あしたははやくおきなければなりません"),
            ("日曜日は起きなくてもいいです。", "4. El domingo no tienes que levantarte temprano.", "にちようびはおきなくてもいいです"),
            ("名前を書かなくてもいいです。", "5. No hace falta que escribas tu nombre.", "なまえをかかなくてもいいです"),
            ("そこに車を止めないでください。", "6. Por favor, no estaciones el auto ahí.", "そこにくるまをとめないでください"),
            ("毎日日本語を勉強しなければなりません。", "7. Debo estudiar japonés todos los días.", "まいにちにほんごをべんきょうしなければなりません"),
            ("靴を脱がなくてもいいです。", "8. No es necesario quitarse los zapatos.", "くつをぬがなくてもいいです"),
            ("薬を飲まなければなりません。", "9. Tienes que tomar la medicina.", "くすりをのまなければなりません"),
            ("心配しないでください。", "10. Por favor, no te preocupes.", "しんぱいしないでください")
        ],
        "exercises": [
            {"q": "¿Cuál es la forma NAI del verbo 読みます (Yomimasu)?", "options": [{"text": "よみない (Yominai)", "correct": False}, {"text": "よまない (Yomanai)", "correct": True}, {"text": "よむない (Yomunai)", "correct": False}]},
            {"q": "¿Cuál es la forma NAI del verbo 買います (Kaimasu)? (Excepción)", "options": [{"text": "かあない (Kaanai)", "correct": False}, {"text": "かいない (Kainai)", "correct": False}, {"text": "かわない (Kawanai)", "correct": True}]},
            {"q": "¿Cuál es la forma NAI de きます (Venir)?", "options": [{"text": "きない (Kinai)", "correct": False}, {"text": "こない (Konai)", "correct": True}, {"text": "かたない (Katanai)", "correct": False}]},
            {"q": "¿Cómo pides 'Por favor, no fumes'?", "options": [{"text": "吸わないでください。", "correct": True}, {"text": "吸わなくてください。", "correct": False}, {"text": "吸わないてください。", "correct": False}]},
            {"q": "¿Qué significa なければなりません (Nakereba narimasen)?", "options": [{"text": "No debes hacerlo", "correct": False}, {"text": "Tienes que hacerlo (Obligación)", "correct": True}, {"text": "Puedes hacerlo", "correct": False}]},
            {"q": "'Tengo que ir al hospital':", "options": [{"text": "病院へ行かなければなりません。", "correct": True}, {"text": "病院へ行かなくてもいいです。", "correct": False}, {"text": "病院へ行かないでください。", "correct": False}]},
            {"q": "¿Qué significa なくてもいいです (Nakutemo ii desu)?", "options": [{"text": "No es necesario / No tienes que", "correct": True}, {"text": "Está prohibido", "correct": False}, {"text": "Es obligatorio", "correct": False}]},
            {"q": "Persona A: '¿Tengo que quitarme los zapatos?'. Persona B: 'No, no es necesario'.", "options": [{"text": "いいえ、脱いでもいいです。", "correct": False}, {"text": "いいえ、脱がなくてもいいです。", "correct": True}, {"text": "いいえ、脱がないでください。", "correct": False}]},
            {"q": "'Por favor, no lo olvides':", "options": [{"text": "忘れないでください。", "correct": True}, {"text": "忘れなくてもいいです。", "correct": False}, {"text": "忘れなければなりません。", "correct": False}]},
            {"q": "Forma NAI de します (Hacer):", "options": [{"text": "さない (Sanai)", "correct": False}, {"text": "しない (Shinai)", "correct": True}, {"text": "すない (Sunai)", "correct": False}]}
        ]
    },
    18: {
        "title": "Forma Diccionario (Poder y Pasatiempos)",
        "grammar": [
            "<strong>Forma Diccionario:</strong> La forma base del verbo. G1: El sonido 'i' cambia a 'u' (Kakimasu -> Kaku). G2: quita masu y pon ru (Tabemasu -> Taberu). G3: Suru, Kuru.",
            "<strong>N / V(dic)こと ができます:</strong> 'Poder / Ser capaz de'. Expresa habilidad o posibilidad.",
            "<strong>趣味は N / V(dic)こと です:</strong> 'Mi pasatiempo es...'.",
            "<strong>V(dic) / Nの / Cantidad + 前に (Mae ni):</strong> 'Antes de...'."
        ],
        "examples": [
            ("私は日本語ができます。", "1. Yo puedo (hablar/entender) japonés.", "わたしはにほんごができます"),
            ("私は漢字を読むことができます。", "2. Yo puedo (soy capaz de) leer kanjis.", "わたしはかんじをよむことができます"),
            ("ここで切符を買うことができます。", "3. Aquí se pueden comprar los boletos (Posibilidad).", "ここできっぷをかうことができます"),
            ("私の趣味は映画です。", "4. Mi pasatiempo es el cine.", "わたしのしゅみはえいがです"),
            ("私の趣味は映画を見ることです。", "5. Mi pasatiempo es ver películas.", "わたしのしゅみはえいがをみることです"),
            ("寝る前に、本を読みます。", "6. Antes de dormir, leo un libro.", "ねるまえに、ほんをよみます"),
            ("食事の前に、手を洗います。", "7. Antes de la comida, me lavo las manos.", "しょくじのまえに、てをあらいます"),
            ("５年前に日本へ来ました。", "8. Vine a Japón hace 5 años (Antes de 5 años).", "ごねんまえににほんへきました"),
            ("ピアノを弾くことができますか。", "9. ¿Sabes tocar el piano?", "ピアノをひくことができますか"),
            ("はい、できます。", "10. Sí, sí puedo.", "はい、できます")
        ],
        "exercises": [
            {"q": "¿Cuál es la Forma Diccionario de 飲みます (Nomimasu)?", "options": [{"text": "のむ (Nomu)", "correct": True}, {"text": "のまる (Nomaru)", "correct": False}, {"text": "のめる (Nomeru)", "correct": False}]},
            {"q": "¿Cuál es la Forma Diccionario de 見ます (Mimasu)?", "options": [{"text": "みう (Miu)", "correct": False}, {"text": "みる (Miru)", "correct": True}, {"text": "むる (Muru)", "correct": False}]},
            {"q": "¿Qué estructura se usa para expresar HABILIDAD? (Ej. Yo puedo manejar)", "options": [{"text": "V(dic)ことができます", "correct": True}, {"text": "V(te)ことができます", "correct": False}, {"text": "V(nai)ことができます", "correct": False}]},
            {"q": "'Mi pasatiempo es ESCUCHAR música':", "options": [{"text": "趣味は音楽を聞くです。", "correct": False}, {"text": "趣味は音楽を聞くことです。", "correct": True}, {"text": "趣味は音楽を聞きことです。", "correct": False}]},
            {"q": "¿Qué significa 前に (Mae ni)?", "options": [{"text": "Después de", "correct": False}, {"text": "Antes de / Hace (tiempo)", "correct": True}, {"text": "Enfrente de", "correct": True}]},
            {"q": "'Antes de venir a Japón, estudié japonés':", "options": [{"text": "日本へ来た前に、日本語を勉強しました。", "correct": False}, {"text": "日本へ来る前に、日本語を勉強しました。", "correct": True}, {"text": "日本へ来て前に、日本語を勉強しました。", "correct": False}]},
            {"q": "'Me lavo las manos antes de la comida' (Comida es sustantivo):", "options": [{"text": "食事前に、手を洗います。", "correct": False}, {"text": "食事の前に、手を洗います。", "correct": True}, {"text": "食事と前に、手を洗います。", "correct": False}]},
            {"q": "'Me casé HACE 3 AÑOS':", "options": [{"text": "３年前に結婚しました。", "correct": True}, {"text": "３年の前に結婚しました。", "correct": False}, {"text": "３年前で結婚しました。", "correct": False}]},
            {"q": "¿Con qué partícula se une el objeto de 'dekimasu' si es solo un sustantivo? (Ej. Puedo/Sé tenis)", "options": [{"text": "を", "correct": False}, {"text": "が", "correct": True}, {"text": "で", "correct": False}]},
            {"q": "Persona A: '¿Puedes comer pescado crudo?' Persona B: 'No, no puedo'.", "options": [{"text": "いいえ、できません。", "correct": True}, {"text": "いいえ、しません。", "correct": False}, {"text": "いいえ、食べることがありません。", "correct": False}]}
        ]
    },
    19: {
        "title": "Forma TA, Experiencias y Cambios",
        "grammar": [
            "<strong>Forma TA:</strong> Es el pasado informal. Se conjuga EXACTAMENTE igual que la Forma TE, pero terminando en 'ta' o 'da'. (Ej. Nonde -> Nonda).",
            "<strong>V(ta) ことがあります:</strong> 'Haber tenido la experiencia de...'. (Ej. He ido a Japón).",
            "<strong>V(ta)り、V(ta)り します:</strong> 'Hacer cosas como A y B'. Menciona acciones representativas sin un orden fijo.",
            "<strong>Adj/Sust + なります (Narimasu):</strong> 'Volverse / Convertirse en'. Adj-i: ~くなります. Adj-na: ~になります. Sustantivos: ~になります."
        ],
        "examples": [
            ("馬に乗ったことがあります。", "1. He montado a caballo (alguna vez).", "うまにのったことがあります"),
            ("富士山に登ったことがありますか。", "2. ¿Has escalado el monte Fuji alguna vez?", "ふじさんにのぼったことがありますか"),
            ("いいえ、一度もありません。", "3. No, ni una sola vez.", "いいえ、いちどもありません"),
            ("日曜日、テニスをしたり、映画を見たりしました。", "4. El domingo jugué tenis, vi una película, etc.", "にちようび、テニスをしたり、えいがをみたりしました"),
            ("寒くなりました。", "5. Se ha vuelto frío (hace más frío ahora).", "さむくなりました"),
            ("テレザちゃんは背が高くなりました。", "6. Teresa se ha vuelto más alta.", "テレザちゃんはせがたかくなりました"),
            ("元気になりました。", "7. Me he curado (Me he vuelto saludable).", "げんきになりました"),
            ("２５歳になりました。", "8. Cumplí 25 años (Me he convertido en alguien de 25 años).", "にじゅうごさいになりました"),
            ("夜は暗くなります。", "9. Por la noche se vuelve oscuro.", "よるはくらくなります"),
            ("医者になりたいです。", "10. Quiero convertirme en médico.", "いしゃになりたいです")
        ],
        "exercises": [
            {"q": "¿Cómo se forma el Pasado Informal (Forma TA) de 飲みます (Nomimasu)?", "options": [{"text": "のむた (Nomuta)", "correct": False}, {"text": "のんだ (Nonda)", "correct": True}, {"text": "のった (Notta)", "correct": False}]},
            {"q": "¿Qué estructura se usa para hablar de EXPERIENCIAS PASADAS? (Ej. He comido sushi)", "options": [{"text": "V(te) います", "correct": False}, {"text": "V(ta) ことがあります", "correct": True}, {"text": "V(ta) 前に", "correct": False}]},
            {"q": "'He estado en Japón (He ido a Japón)':", "options": [{"text": "日本へ行ったことがあります。", "correct": True}, {"text": "日本へ行くことがあります。", "correct": False}, {"text": "日本へ行ったです。", "correct": False}]},
            {"q": "¿Cómo dices 'No, nunca lo he hecho (ni una vez)'?", "options": [{"text": "いいえ、ありません。", "correct": True}, {"text": "一度もありません。", "correct": True}, {"text": "Ambas son correctas", "correct": True}]},
            {"q": "¿Qué estructura usas para listar acciones aleatorias representativas? (Hice esto, aquello...)", "options": [{"text": "V(te), V(te) します", "correct": False}, {"text": "V(ta)り、V(ta)り します", "correct": True}, {"text": "V(dic)と、V(dic) します", "correct": False}]},
            {"q": "'El domingo limpié, lavé la ropa...':", "options": [{"text": "掃除したり、洗濯したりしました。", "correct": True}, {"text": "掃除して、洗濯してしました。", "correct": False}, {"text": "掃除した、洗濯したします。", "correct": False}]},
            {"q": "¿Qué verbo significa 'Volverse / Convertirse en' (Cambio de estado)?", "options": [{"text": "します (Shimasu)", "correct": False}, {"text": "なります (Narimasu)", "correct": True}, {"text": "あります (Arimasu)", "correct": False}]},
            {"q": "¿Cómo cambias un Adjetivo-i con なります? (Ej. Volverse caro / 高い)", "options": [{"text": "高いになります", "correct": False}, {"text": "高くなります", "correct": True}, {"text": "高にまります", "correct": False}]},
            {"q": "¿Cómo cambias un Adjetivo-na o Sustantivo con なります? (Ej. Volverse famoso / 有名)", "options": [{"text": "有名くなります", "correct": False}, {"text": "有名になります", "correct": True}, {"text": "有名だになります", "correct": False}]},
            {"q": "'Me convertí en profesor' (Sustantivo):", "options": [{"text": "先生になりました。", "correct": True}, {"text": "先生くなりました。", "correct": False}, {"text": "先生がなりました。", "correct": False}]}
        ]
    },
    20: {
        "title": "Estilo Informal (Futsukei)",
        "grammar": [
            "<strong>Futsukei (Estilo Informal):</strong> Se usa con familiares, amigos y subordinados. Quita la cortesía (~masu / ~desu).",
            "<strong>Verbos:</strong> Presente (+): Forma Diccionario. Pres (-): Forma NAI. Pasado (+): Forma TA. Pasado (-): Forma NAKATTA.",
            "<strong>Adjetivos-i:</strong> Igual, pero omitiendo 'desu'. (Ej. 高い, 高くない, 高かった, 高くなかった).",
            "<strong>Adjetivos-na / Sustantivos:</strong> Presente (+): agrega 'da' (En preguntas se omite el 'da'). Pasado: 'datta'.",
            "<strong>Preguntas:</strong> Se elimina la partícula 'ka' (か) y se sube la entonación. A veces se omiten partículas como は, が, を."
        ],
        "examples": [
            ("毎日新聞を読む？", "1. ¿Lees el periódico todos los días? (Informal)", "まいにちしんぶんをよむ？"),
            ("うん、読む。", "2. Sí, lo leo.", "うん、よむ"),
            ("ううん、読まない。", "3. No, no lo leo.", "ううん、よまない"),
            ("昨日パソコンを買った？", "4. ¿Compraste una computadora ayer?", "きのうパソコンをかった？"),
            ("うん、買った。", "5. Sí, la compré.", "うん、かった"),
            ("今忙しい？", "6. ¿Estás ocupado ahora?", "いまいそがしい？"),
            ("うん、忙しい。", "7. Sí, estoy ocupado.", "うん、いそがしい"),
            ("コーヒー飲む？", "8. ¿Bebes café? (Omisión de la partícula を)", "コーヒーのむ？"),
            ("ありがとう。もらう。", "9. Gracias. Lo acepto (lit. lo recibo).", "ありがとう。もらう"),
            ("日曜日、暇？", "10. ¿Estás libre el domingo? (Omisión del 'da')", "にちようび、ひま？")
        ],
        "exercises": [
            {"q": "¿Para qué situaciones se usa el estilo informal (Futsukei)?", "options": [{"text": "Con jefes y clientes.", "correct": False}, {"text": "Con amigos, familiares y personas de menor rango.", "correct": True}, {"text": "Solo en escritos oficiales.", "correct": False}]},
            {"q": "¿Cuál es la forma informal de 食べます (Tabemasu - Presente)?", "options": [{"text": "食べる (Taberu)", "correct": True}, {"text": "食べた (Tabeta)", "correct": False}, {"text": "食べない (Tabenai)", "correct": False}]},
            {"q": "¿Cuál es la forma informal de 食べません (Tabemasen - Negativo)?", "options": [{"text": "食べる (Taberu)", "correct": False}, {"text": "食べない (Tabenai)", "correct": True}, {"text": "食べなかった (Tabenakatta)", "correct": False}]},
            {"q": "¿Cuál es la forma informal de 食べました (Tabemashita - Pasado)?", "options": [{"text": "食べる (Taberu)", "correct": False}, {"text": "食べた (Tabeta)", "correct": True}, {"text": "食べなかった (Tabenakatta)", "correct": False}]},
            {"q": "¿Cuál es la forma informal de 食べませんでした (Tabemasen deshita - Pasado Negativo)?", "options": [{"text": "食べなかった (Tabenakatta)", "correct": True}, {"text": "食べない (Tabenai)", "correct": False}, {"text": "食べた (Tabeta)", "correct": False}]},
            {"q": "¿Cómo haces una PREGUNTA en estilo informal?", "options": [{"text": "Añadiendo か al final.", "correct": False}, {"text": "Subiendo la entonación sin usar か.", "correct": True}, {"text": "Añadiendo だ al final.", "correct": False}]},
            {"q": "Para responder SÍ y NO en informal se usa:", "options": [{"text": "はい / いいえ", "correct": False}, {"text": "うん / ううん", "correct": True}, {"text": "そう / そうじゃない", "correct": False}]},
            {"q": "'¿Es bonito?' (Adjetivo-na). Pregunta informal correcta:", "options": [{"text": "きれいだ？", "correct": False}, {"text": "きれい？ (Se omite el 'da')", "correct": True}, {"text": "きれいか？", "correct": False}]},
            {"q": "Afirmación informal (Adj-na/Sust): 'Es bonito' / 'Es estudiante'.", "options": [{"text": "きれいだ。/ 学生だ。", "correct": True}, {"text": "きれい。/ 学生。", "correct": False}, {"text": "きれいする。/ 学生する。", "correct": False}]},
            {"q": "¿Qué partículas se suelen omitir frecuentemente en la conversación informal?", "options": [{"text": "は, が, を, へ", "correct": True}, {"text": "で, に, と, から", "correct": False}, {"text": "Ninguna", "correct": False}]}
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
