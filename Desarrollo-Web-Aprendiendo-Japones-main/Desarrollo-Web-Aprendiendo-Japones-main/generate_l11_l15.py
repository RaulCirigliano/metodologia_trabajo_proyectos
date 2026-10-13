import os

data = {
    11: {
        "title": "Contadores y Periodos de Tiempo",
        "grammar": [
            "<strong>Contadores:</strong> En japonés se usan sufijos especiales para contar objetos. Ej: つ (Cosas en general), 枚 (Objetos planos/hojas), 台 (Máquinas/Vehículos), 人 (Personas).",
            "<strong>Sustantivo + Contador:</strong> El contador se coloca DESPUÉS del sustantivo y la partícula, justo antes del verbo. Ej: りんごを３つ買いました。",
            "<strong>Periodo de tiempo に N 回 V:</strong> Indica la frecuencia. 'N veces por (Periodo)'. Ej: １か月に２回映画を見ます (Veo películas 2 veces al mes).",
            "<strong>~だけ:</strong> Significa 'solamente'. Ej: 日曜日だけ休みます (Solo descanso el domingo)."
        ],
        "examples": [
            ("りんごを４つ買いました。", "1. Compré cuatro manzanas.", "りんごをよっつかいました"),
            ("８０円の切手を５枚買いました。", "2. Compré cinco sellos de 80 yenes.", "はちじゅうえんのきってをごまいかいました"),
            ("教室に学生が４人います。", "3. En el aula hay 4 estudiantes.", "きょうしつにがくせいがよにんいます"),
            ("家族は何人ですか。", "4. ¿Cuántas personas hay en tu familia?", "かぞくはなんにんですか"),
            ("５人です。両親と姉と兄と私です。", "5. Somos 5. Mis padres, mi hermana mayor, mi hermano mayor y yo.", "ごにんです。りょうしんとあねとあにとわたしです"),
            ("１週間に２回テニスをします。", "6. Juego tenis dos veces a la semana.", "いっしゅうかんににかいテニスをします"),
            ("どのくらいスペイン語を勉強しましたか。", "7. ¿Cuánto tiempo estudiaste español?", "どのくらいスペインごをべんきょうしましたか"),
            ("３か月勉強しました。", "8. Lo estudié por 3 meses.", "さんかげつべんきょうしました"),
            ("大阪から東京まで新幹線でどのくらいかかりますか。", "9. ¿Cuánto tiempo se tarda en tren bala desde Osaka hasta Tokio?", "おおさかからとうきょうまでしんかんせんでどのくらいかかりますか"),
            ("２時間半かかります。", "10. Se tarda 2 horas y media.", "にじかんはんかかります")
        ],
        "exercises": [
            {"q": "¿Qué contador usarías para comprar 3 CAMISAS (objetos planos/delgados)?", "options": [{"text": "３つ (mittsu)", "correct": False}, {"text": "３台 (sandai)", "correct": False}, {"text": "３枚 (sanmai)", "correct": True}]},
            {"q": "¿Qué contador usarías para contar 2 AUTOS (vehículos/máquinas)?", "options": [{"text": "２枚 (nimai)", "correct": False}, {"text": "２台 (nidai)", "correct": True}, {"text": "２人 (futari)", "correct": False}]},
            {"q": "¿Dónde se coloca el contador en la oración 'Compré dos manzanas'?", "options": [{"text": "りんごを２つ買いました。", "correct": True}, {"text": "２つりんごを買いました。", "correct": False}, {"text": "りんごの２つを買いました。", "correct": False}]},
            {"q": "¿Cómo se dice 'Una persona' y 'Dos personas'?", "options": [{"text": "いちにん / ににん", "correct": False}, {"text": "ひとり / ふたり", "correct": True}, {"text": "ひとつ / ふたつ", "correct": False}]},
            {"q": "¿Cómo preguntas 'Cuántas personas hay en tu familia?'", "options": [{"text": "家族は何人ですか。", "correct": True}, {"text": "家族はいくつですか。", "correct": False}, {"text": "家族は誰ですか。", "correct": False}]},
            {"q": "¿Qué significa la palabra 'どのくらい' (Dono kurai)?", "options": [{"text": "¿De dónde?", "correct": False}, {"text": "¿Por qué?", "correct": False}, {"text": "¿Cuánto tiempo / Cuánto?", "correct": True}]},
            {"q": "'Veo películas 3 veces AL mes':", "options": [{"text": "１か月で３回映画を見ます。", "correct": False}, {"text": "１か月に３回映画を見ます。", "correct": True}, {"text": "１か月から３回映画を見ます。", "correct": False}]},
            {"q": "¿Qué verbo se usa para expresar que algo TOMA o TARDA tiempo/dinero?", "options": [{"text": "かかります (Kakarimasu)", "correct": True}, {"text": "あります (Arimasu)", "correct": False}, {"text": "します (Shimasu)", "correct": False}]},
            {"q": "¿Cómo dices 'Solamente el domingo'?", "options": [{"text": "日曜日から", "correct": False}, {"text": "日曜日も", "correct": False}, {"text": "日曜日だけ", "correct": True}]},
            {"q": "'Estudié japonés POR un año' (Periodo de tiempo):", "options": [{"text": "１年日本語を勉強しました。", "correct": True}, {"text": "１年で日本語を勉強しました。", "correct": False}, {"text": "１年に日本語を勉強しました。", "correct": False}]}
        ]
    },
    12: {
        "title": "Pasado de Adjetivos y Comparaciones",
        "grammar": [
            "<strong>Pasado Sustantivos y Adjetivos-na:</strong> Afirmativo: ~でした (Era/Fue). Negativo: ~じゃありませんでした.",
            "<strong>Pasado Adjetivos-i:</strong> Afirmativo: Se cambia い por ~かったです (Ej. 高かったです). Negativo: ~くありませんでした.",
            "<strong>N1 と N2 と どちらが ~ですか:</strong> 'Entre N1 y N2, ¿Cuál es más...?' (Comparación entre DOS cosas).",
            "<strong>N1 のほうが ~です:</strong> 'N1 es más...'. Forma de responder eligiendo una opción.",
            "<strong>Grupo で 疑問詞(Qué/Quién/Dónde/Cuándo) が一番 ~ですか:</strong> 'Dentro de este grupo, ¿Cuál es el más...?' (Superlativo)."
        ],
        "examples": [
            ("昨日は雨でした。", "1. Ayer fue un día lluvioso.", "きのうはあめでした"),
            ("昨日は寒かったです。", "2. Ayer hizo frío.", "きのうはさむかったです"),
            ("京都は静かでしたか。", "3. ¿Kioto estaba tranquilo?", "きょうとはしずかでしたか"),
            ("いいえ、静かじゃありませんでした。", "4. No, no estaba tranquilo.", "いいえ、しずかじゃありませんでした"),
            ("昨日のテストはどうでしたか。", "5. ¿Qué tal estuvo el examen de ayer?", "きのうのテストはどうでしたか"),
            ("難しかったですが、面白かったです。", "6. Estuvo difícil, pero fue interesante.", "むずかしかったですが、おもしろかったです"),
            ("肉と魚とどちらが好きですか。", "7. Entre la carne y el pescado, ¿cuál te gusta más?", "にくとさかなとどちらがすきですか"),
            ("肉のほうが好きです。", "8. Me gusta más la carne.", "にくのほうがすきです"),
            ("スポーツで何が一番好きですか。", "9. De los deportes, ¿cuál es el que más te gusta?", "スポーツでなにがいちばんすきですか"),
            ("サッカーが一番好きです。", "10. El fútbol es el que más me gusta.", "サッカーがいちばんすきです")
        ],
        "exercises": [
            {"q": "¿Cuál es el PASADO de un sustantivo o adjetivo-na? (Ej. Era fin de semana)", "options": [{"text": "休みです", "correct": False}, {"text": "休みでした", "correct": True}, {"text": "休みかった", "correct": False}]},
            {"q": "¿Cuál es el PASADO de un adjetivo-i? (Ej. Hizo calor / 暑い)", "options": [{"text": "暑いでした", "correct": False}, {"text": "暑かったです", "correct": True}, {"text": "暑くでした", "correct": False}]},
            {"q": "¿Cuál es el PASADO NEGATIVO de un adjetivo-i? (Ej. No estaba rico / おいしい)", "options": [{"text": "おいしくありませんでした", "correct": True}, {"text": "おいしいじゃありませんでした", "correct": False}, {"text": "おいしかったじゃありません", "correct": False}]},
            {"q": "¿Cómo se pregunta 'Entre A y B, ¿Cuál prefieres?'?", "options": [{"text": "A と B と なにが好きですか。", "correct": False}, {"text": "A と B と どちらが好きですか。", "correct": True}, {"text": "A と B と どれが好きですか。", "correct": False}]},
            {"q": "¿Cómo respondes 'Prefiero A'?", "options": [{"text": "Aが一番好きです。", "correct": False}, {"text": "Aが好きです。", "correct": False}, {"text": "Aのほうが好きです。", "correct": True}]},
            {"q": "Persona A: 'Entre el perro y el gato, ¿cuál te gusta más?'. Persona B: 'Me gustan ambos'.", "options": [{"text": "どちらが好きです。", "correct": False}, {"text": "どちらも好きです。", "correct": True}, {"text": "どちらが好きじゃありません。", "correct": False}]},
            {"q": "¿Qué palabra significa 'El más / El número uno' (Superlativo)?", "options": [{"text": "一番 (Ichiban)", "correct": True}, {"text": "たくさん (Takusan)", "correct": False}, {"text": "とても (Totemo)", "correct": False}]},
            {"q": "'En Japón, ¿DÓNDE es el más hermoso?':", "options": [{"text": "日本で何が一番きれいですか。", "correct": False}, {"text": "日本でどこが一番きれいですか。", "correct": True}, {"text": "日本でいつが一番きれいですか。", "correct": False}]},
            {"q": "'De tu familia, ¿QUIÉN es el más alto?':", "options": [{"text": "家族で誰が一番背が高いですか。", "correct": True}, {"text": "家族で何が一番背が高いですか。", "correct": False}, {"text": "家族の誰が一番背が高いですか。", "correct": False}]},
            {"q": "Pasado negativo de いい (Bueno): 'No estuvo bueno'", "options": [{"text": "いくありませんでした", "correct": False}, {"text": "よくありませんでした", "correct": True}, {"text": "いいじゃありませんでした", "correct": False}]}
        ]
    },
    13: {
        "title": "Deseos (欲しい / ~たい) y Propósito de Ir",
        "grammar": [
            "<strong>N が 欲しいです:</strong> 'Quiero (objeto)'. Se usa para cosas tangibles o personas. La partícula que marca el objeto deseado es が.",
            "<strong>V(masu) たいです:</strong> 'Quiero hacer (verbo)'. Se conjuga quitando el 'masu' y agregando 'tai'. Puede usar las partículas を o が.",
            "<strong>N(Lugar) へ V(masu) / N に 行きます:</strong> 'Ir a (Lugar) PARA (propósito)'. El propósito se marca con に."
        ],
        "examples": [
            ("私はパソコンが欲しいです。", "1. Yo quiero una computadora.", "わたしはパソコンがほしいです"),
            ("今何が一番欲しいですか。", "2. ¿Qué es lo que más quieres ahora?", "いまなにがいちばんほしいですか"),
            ("新しい車が欲しいです。", "3. Quiero un auto nuevo.", "あたらしいくるまがほしいです"),
            ("私は沖縄へ行きたいです。", "4. Yo quiero ir a Okinawa.", "わたしはおきなわへいきたいです"),
            ("お腹が痛いですから、何も食べたくないです。", "5. Como me duele el estómago, no quiero comer nada.", "おなかがいたいですから、なにもたべたくないです"),
            ("日本へ美術の勉強に来ました。", "6. Vine a Japón a estudiar bellas artes.", "にほんへびじゅつのべんきょうにきました"),
            ("明日京都へお祭りをみに行きます。", "7. Mañana iré a Kioto a ver un festival.", "あしたきょうとへおまつりをみにいきます"),
            ("冬休みはどこかへ行きましたか。", "8. ¿Fuiste a algún lado en las vacaciones de invierno?", "ふゆやすみはどこかへいきましたか"),
            ("はい、北海道へスキーに行きました。", "9. Sí, fui a Hokkaido a esquiar.", "はい、ほっかいどうへスキーにいきますた"),
            ("喉が渇きましたから、何か飲みたいです。", "10. Como tengo sed, quiero beber algo.", "のどがかわきましたから、なにかのみたいです")
        ],
        "exercises": [
            {"q": "¿Qué palabra se usa para expresar deseo de tener un OBJETO (Ej. Quiero un auto)?", "options": [{"text": "欲しい (Hoshii)", "correct": True}, {"text": "〜たい (-tai)", "correct": False}, {"text": "好き (Suki)", "correct": False}]},
            {"q": "¿Qué sufijo se añade a la raíz de un verbo para indicar 'Querer hacer' la acción?", "options": [{"text": "〜ない (-nai)", "correct": False}, {"text": "〜たい (-tai)", "correct": True}, {"text": "〜ます (-masu)", "correct": False}]},
            {"q": "Quiero comer sushi: 寿司 を(o が) _____.", "options": [{"text": "食べたいです (Tabetai desu)", "correct": True}, {"text": "食べ欲しいです (Tabehoshii desu)", "correct": False}, {"text": "食べますです (Tabemasu desu)", "correct": False}]},
            {"q": "¿Cómo se dice 'NO quiero ir'? (Negativo de ikitai)", "options": [{"text": "行きたくないです", "correct": True}, {"text": "行きたいじゃありません", "correct": False}, {"text": "行きたいありません", "correct": False}]},
            {"q": "'Fui a Japón a COMPRAR una cámara'. ¿Cómo marcas el propósito de ir?", "options": [{"text": "日本へカメラを買いで行きました。", "correct": False}, {"text": "日本へカメラを買いに行きました。", "correct": True}, {"text": "日本へカメラを買うに行きました。", "correct": False}]},
            {"q": "¿Cómo dices 'alguna cosa / algo' (para comer o beber)?", "options": [{"text": "何も (Nani mo)", "correct": False}, {"text": "何 (Nani)", "correct": False}, {"text": "何か (Nani ka)", "correct": True}]},
            {"q": "¿Cómo dices 'algún lugar / a algún lado'?", "options": [{"text": "どこも (Doko mo)", "correct": False}, {"text": "どこか (Doko ka)", "correct": True}, {"text": "どこ (Doko)", "correct": False}]},
            {"q": "Fui a Osaka a cenar (Cenar = 食事 / shokuji, sustantivo):", "options": [{"text": "大阪へ食事で行きました。", "correct": False}, {"text": "大阪へ食事に行きました。", "correct": True}, {"text": "大阪へ食事をしに行きました。(También correcta, pero la forma sustantiva con NI es la más común).", "correct": True}]},
            {"q": "¿La forma '~たいです' (quiero hacer) se conjuga como un Adjetivo-i o Adjetivo-na?", "options": [{"text": "Como Adjetivo-i (Pasado: 〜たかったです)", "correct": True}, {"text": "Como Adjetivo-na (Pasado: 〜たいでした)", "correct": False}, {"text": "No se conjuga", "correct": False}]},
            {"q": "Persona A: '¿Fuiste a algún lado?'. Persona B: 'No, no fui a NINGÚN LADO'.", "options": [{"text": "いいえ、どこか行きませんでした。", "correct": False}, {"text": "いいえ、どこも行きませんでした。", "correct": True}, {"text": "いいえ、どこか行きました。", "correct": False}]}
        ]
    },
    14: {
        "title": "La Forma TE, Peticiones y Progresivo",
        "grammar": [
            "<strong>Grupos de verbos:</strong> Grupo I (U), Grupo II (Ru/E), Grupo III (Irregulares: suru, kuru).",
            "<strong>Forma TE:</strong> Es la forma conectiva del verbo. G1 tiene reglas especiales (i,chi,ri -> tte / mi,bi,ni -> nde / ki -> ite / gi -> ide / shi -> shite). G2: quita masu y pon te. G3: shite, kite.",
            "<strong>V(te) ください:</strong> 'Por favor, haz...'. Petición directa.",
            "<strong>V(te) います:</strong> 'Estar haciendo...'. Acción en progreso (Gerundio ando/iendo).",
            "<strong>V(masu) ましょうか:</strong> '¿Te ayudo a...? / ¿Hago... por ti?'. Para ofrecer ayuda."
        ],
        "examples": [
            ("ちょっと待ってください。", "1. Por favor, espera un momento.", "ちょっとまってください"),
            ("辞書を貸してください。", "2. Por favor, préstame el diccionario.", "じしょをかしてください"),
            ("ゆっくり話してください。", "3. Por favor, hable despacio.", "ゆっくりはなしてください"),
            ("今雨が降っていますか。", "4. ¿Está lloviendo ahora?", "いまあめがふっていますか"),
            ("はい、降っています。", "5. Sí, está lloviendo.", "はい、ふっています"),
            ("ミラーさんは今電話をかけています。", "6. El Sr. Miller está haciendo una llamada ahora.", "ミラーさんはいまでんわをかけています"),
            ("荷物を持ちましょうか。", "7. ¿Te ayudo a llevar el equipaje?", "にもつをもちましょうか"),
            ("いいえ、けっこうです。", "8. No, gracias. (Estoy bien así)", "いいえ、けっこうです"),
            ("エアコンをつけましょうか。", "9. ¿Enciendo el aire acondicionado por ti?", "エアコンをつけましょうか"),
            ("はい、お願いします。", "10. Sí, por favor te lo encargo.", "はい、おねがいします")
        ],
        "exercises": [
            {"q": "¿A qué grupo pertenece el verbo 食べます (Comer)?", "options": [{"text": "Grupo I", "correct": False}, {"text": "Grupo II", "correct": True}, {"text": "Grupo III", "correct": False}]},
            {"q": "¿A qué grupo pertenecen します (Hacer) y きます (Venir)?", "options": [{"text": "Grupo III", "correct": True}, {"text": "Grupo I", "correct": False}, {"text": "Grupo II", "correct": False}]},
            {"q": "¿Cuál es la FORMA TE del verbo 待ちます (Machimasu - Esperar)? (Grupo I)", "options": [{"text": "まちて (Machite)", "correct": False}, {"text": "まって (Matte)", "correct": True}, {"text": "まんで (Mande)", "correct": False}]},
            {"q": "¿Cuál es la FORMA TE del verbo 読みます (Yomimasu - Leer)? (Grupo I)", "options": [{"text": "よんで (Yonde)", "correct": True}, {"text": "よって (Yotte)", "correct": False}, {"text": "よみて (Yomite)", "correct": False}]},
            {"q": "¿Cuál es la FORMA TE de 食べます (Tabemasu)? (Grupo II)", "options": [{"text": "たべて (Tabete)", "correct": True}, {"text": "たべって (Tabette)", "correct": False}, {"text": "たんで (Tande)", "correct": False}]},
            {"q": "¿Cómo se pide cortésmente 'Por favor, escriba' (Kakimasu)?", "options": [{"text": "かきってください。", "correct": False}, {"text": "かいてください。", "correct": True}, {"text": "かんでください。", "correct": False}]},
            {"q": "¿Qué estructura se usa para decir 'Estoy leyendo' (Ahora mismo)?", "options": [{"text": "読んでいます (Yonde imasu)", "correct": True}, {"text": "読みます (Yomimasu)", "correct": False}, {"text": "読んでください (Yonde kudasai)", "correct": False}]},
            {"q": "¿Cuál es la excepción en el Grupo I para la Forma TE? (El verbo 行きます - Ikimasu)", "options": [{"text": "いいて (Iite)", "correct": False}, {"text": "いって (Itte)", "correct": True}, {"text": "いんで (Inde)", "correct": False}]},
            {"q": "Ves a alguien cargando algo pesado y quieres ofrecer tu ayuda. Dices: '¿Te ayudo a llevarlo?' (Mochimasu)", "options": [{"text": "持ちますか。", "correct": False}, {"text": "持ちましょうか。", "correct": True}, {"text": "持ってください。", "correct": False}]},
            {"q": "Persona A: '¿Te abro la ventana?'. Persona B: 'No, así está bien / No, gracias'.", "options": [{"text": "いいえ、いいですね。", "correct": False}, {"text": "いいえ、けっこうです。", "correct": True}, {"text": "いいえ、おねがいします。", "correct": False}]}
        ]
    },
    15: {
        "title": "Permiso, Prohibición y Estado (Forma TE)",
        "grammar": [
            "<strong>V(te) もいいですか:</strong> '¿Puedo hacer...?'. Se usa para pedir permiso. Para dar permiso se responde 'ええ、いいですよ' (Sí, puedes).",
            "<strong>V(te) はいけません:</strong> 'No debes hacer...'. Prohibición estricta.",
            "<strong>V(te) います:</strong> Además de 'estar haciendo' (progresivo), también expresa un estado permanente, resultado de una acción (Ej. Estoy casado), o una acción habitual (Trabajo en...).",
            "<strong>N(Lugar/Trabajo) で 働いています:</strong> 'Trabajar EN'. Se usa で. Pero <strong>N に 住んでいます:</strong> 'Vivir EN', usa に (Punto fijo)."
        ],
        "examples": [
            ("写真を撮ってもいいですか。", "1. ¿Puedo tomar fotos?", "しゃしんをとってもいいですか"),
            ("ええ、いいですよ。", "2. Sí, por supuesto.", "ええ、いいですよ"),
            ("ここでタバコを吸ってはいけません。", "3. No debes fumar aquí (Está prohibido).", "ここでタバコをすってはいけません"),
            ("私は結婚しています。", "4. Yo estoy casado (Estado).", "わたしはけっこんしています"),
            ("ミラーさんはIMCで働いています。", "5. El Sr. Miller trabaja en IMC.", "ミラーさんはアイエムシーではたらいています"),
            ("私は大阪に住んでいます。", "6. Yo vivo en Osaka.", "わたしはおおさかにすんでいます"),
            ("カメラを持っていますか。", "7. ¿Tienes (posees) una cámara?", "カメラをもっていますか"),
            ("はい、持っています。", "8. Sí, la tengo.", "はい、もっています"),
            ("IMCの電話番号を知っていますか。", "9. ¿Sabes el número de teléfono de IMC?", "アイエムシーのでんわばんごうをしっていますか"),
            ("いいえ、知りません。", "10. No, no lo sé.", "いいえ、しりません")
        ],
        "exercises": [
            {"q": "¿Qué estructura se usa para pedir PERMISO? (Ej. ¿Puedo sentarme aquí?)", "options": [{"text": "座ってください", "correct": False}, {"text": "座ってもいいですか", "correct": True}, {"text": "座っていますか", "correct": False}]},
            {"q": "¿Qué estructura se usa para una PROHIBICIÓN estricta? (Ej. No debes entrar)", "options": [{"text": "入ってはいけません", "correct": True}, {"text": "入ってもいいですか", "correct": False}, {"text": "入っていません", "correct": False}]},
            {"q": "Persona A: '¿Puedo fumar aquí?' Persona B: 'No, te lo ruego no lo hagas' (Rechazo cortés):", "options": [{"text": "いいえ、いけません。", "correct": False}, {"text": "すみません、ちょっと...", "correct": True}, {"text": "いいえ、吸いません。", "correct": False}]},
            {"q": "'Yo estoy casado' (Estado permanente en japonés):", "options": [{"text": "結婚しました (Kekkon shimashita)", "correct": False}, {"text": "結婚します (Kekkon shimasu)", "correct": False}, {"text": "結婚しています (Kekkon shite imasu)", "correct": True}]},
            {"q": "'El Sr. Watt enseña inglés en la universidad Sakura' (Ocupación habitual):", "options": [{"text": "教えています (Oshiete imasu)", "correct": True}, {"text": "教えました (Oshieta)", "correct": False}, {"text": "教えてください (Oshiete kudasai)", "correct": False}]},
            {"q": "¿Qué partícula usa el verbo 住んでいます (Vivir / Residir) para marcar el lugar?", "options": [{"text": "で (de)", "correct": False}, {"text": "に (ni)", "correct": True}, {"text": "を (wo)", "correct": False}]},
            {"q": "¿Qué partícula usa el verbo 働いています (Trabajar) para marcar el lugar?", "options": [{"text": "に (ni)", "correct": False}, {"text": "で (de)", "correct": True}, {"text": "へ (e)", "correct": False}]},
            {"q": "¿Cómo preguntas si alguien CONOCE o SABE algo? (Ej. ¿Conoces a Suzuki?)", "options": [{"text": "知りますか (Shirimasu ka)", "correct": False}, {"text": "知っていますか (Shitte imasu ka)", "correct": True}, {"text": "知りましたか (Shirimashita ka)", "correct": False}]},
            {"q": "Excepción importante: ¿Cómo respondes 'NO LO SÉ'?", "options": [{"text": "知っていません (Shitte imasen)", "correct": False}, {"text": "知りません (Shirimasen)", "correct": True}, {"text": "知るじゃありません (Shiru ja arimasen)", "correct": False}]},
            {"q": "¿Qué verbo en forma TE IMASU se usa para 'Tener / Poseer / Llevar puesto' un objeto? (Ej. ¿Tienes carro?)", "options": [{"text": "持っています (Motte imasu)", "correct": True}, {"text": "あります (Arimasu - no aplica para pertenencias personales que llevas contigo de esta forma)", "correct": False}, {"text": "います (Imasu)", "correct": False}]}
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
