import os

data = {
    6: {
        "title": "Verbos Básicos (Afirmativo, Negativo, Pasado)",
        "grammar": [
            "<strong>Afirmativo (Presente/Futuro):</strong> ~ます (masu). Sirve para acciones habituales y para el futuro. Ej. 行きます (Voy / Iré).",
            "<strong>Negativo (Presente/Futuro):</strong> ~ません (masen). Ej. 行きません (No voy / No iré).",
            "<strong>Afirmativo (Pasado):</strong> ~ました (mashita). Ej. 行きました (Fui).",
            "<strong>Negativo (Pasado):</strong> ~ませんでした (masen deshita). Ej. 行きませんでした (No fui)."
        ],
        "examples": [
            ("毎日学校へ行きます。", "1. Todos los días voy a la escuela.", "まいにちがっこうへいきます"),
            ("明日学校へ行きます。", "2. Mañana iré a la escuela.", "あしたがっこうへいきます"),
            ("今日は学校へ行きません。", "3. Hoy no iré a la escuela.", "きょうはがっこうへいきません"),
            ("昨日学校へ行きました。", "4. Ayer fui a la escuela.", "きのうがっこうへいきました"),
            ("一昨日学校へ行きませんでした。", "5. Anteayer no fui a la escuela.", "おとといがっこうへいきませんでした"),
            ("朝ごはんを食べます。", "6. Desayuno (como el desayuno).", "あさごはんをたべます"),
            ("テレビを見ます。", "7. Veo la televisión.", "テレビをみます"),
            ("音楽を聞きません。", "8. No escucho música.", "おんがくをききません"),
            ("手紙を書きました。", "9. Escribí una carta.", "てがみをかきました"),
            ("昨晩、何もしませんでした。", "10. Anoche no hice nada.", "さくばん、なにもしませんでした")
        ],
        "exercises": [
            {"q": "¿Cómo se dice 'Estudio' (presente afirmativo)?", "options": [{"text": "勉強します (Benkyou shimasu)", "correct": True}, {"text": "勉強しました (Benkyou shimashita)", "correct": False}, {"text": "勉強しません (Benkyou shimasen)", "correct": False}]},
            {"q": "¿Cómo se dice 'NO estudio' (presente negativo)?", "options": [{"text": "勉強します (Benkyou shimasu)", "correct": False}, {"text": "勉強しません (Benkyou shimasen)", "correct": True}, {"text": "勉強しませんでした (Benkyou shimasen deshita)", "correct": False}]},
            {"q": "¿Cómo se dice 'Estudié' (pasado afirmativo)?", "options": [{"text": "勉強しませんでした", "correct": False}, {"text": "勉強します", "correct": False}, {"text": "勉強しました (Benkyou shimashita)", "correct": True}]},
            {"q": "¿Cómo se dice 'NO estudié' (pasado negativo)?", "options": [{"text": "勉強しません", "correct": False}, {"text": "勉強しませんでした (Benkyou shimasen deshita)", "correct": True}, {"text": "勉強しました", "correct": False}]},
            {"q": "'Mañana _____ a Kioto' (Ir = ikimasu):", "options": [{"text": "行きました", "correct": False}, {"text": "行きます", "correct": True}, {"text": "行きませんでした", "correct": False}]},
            {"q": "'Ayer NO _____ la película' (Ver = mimasu):", "options": [{"text": "見ました", "correct": False}, {"text": "見ません", "correct": False}, {"text": "見ませんでした", "correct": True}]},
            {"q": "¿Qué tiempo verbal se usa en japonés para el FUTURO (Ej. Mañana comeré)?", "options": [{"text": "Forma ~mashou", "correct": False}, {"text": "El mismo del presente (~masu)", "correct": True}, {"text": "Forma ~mashita", "correct": False}]},
            {"q": "Persona A: '¿Fuiste al banco?'. Persona B: 'No, no fui':", "options": [{"text": "いいえ、行きました。", "correct": False}, {"text": "いいえ、行きませんでした。", "correct": True}, {"text": "いいえ、行きません。", "correct": False}]},
            {"q": "'Anoche dormí a las 10':", "options": [{"text": "昨晩、１０時に寝ました。", "correct": True}, {"text": "昨晩、１０時に寝ます。", "correct": False}, {"text": "昨晩、１０時に寝ません。", "correct": False}]},
            {"q": "¿Qué significa 'しませんでした' (shimasen deshita)?", "options": [{"text": "No hice", "correct": True}, {"text": "Hice", "correct": False}, {"text": "No hago", "correct": False}]}
        ]
    },
    7: {
        "title": "Existencia (あります / います) y Posición",
        "grammar": [
            "<strong>あります (Arimasu):</strong> Haber / Existir / Tener. Solo para objetos inanimados (cosas, plantas).",
            "<strong>います (Imasu):</strong> Haber / Existir. Solo para seres animados (personas, animales).",
            "<strong>Posición:</strong> N1(Lugar) の + Posición (上 ue, 下 shita, 前 mae, 後ろ ushiro, 中 naka, 外 soto, 隣 tonari, 近く chikaku)."
        ],
        "examples": [
            ("机の上に本があります。", "1. Hay un libro encima de la mesa.", "つくえのうえにほんがあります"),
            ("庭に犬がいます。", "2. Hay un perro en el jardín.", "にわにいぬがいます"),
            ("私は車があります。", "3. Yo tengo un auto.", "わたしはくるまがあります"),
            ("ミラーさんは会議室にいます。", "4. El Sr. Miller está en la sala de reuniones.", "ミラーさんはかいぎしつにいます"),
            ("猫は箱の中にいます。", "5. El gato está dentro de la caja.", "ねこははこのなかにいます"),
            ("郵便局の隣に銀行があります。", "6. Hay un banco al lado del correo.", "ゆうびんきょくのとなりにぎんこうがあります"),
            ("ベッドの下に靴があります。", "7. Hay zapatos debajo de la cama.", "ベッドのしたにくつがあります"),
            ("あそこに誰がいますか。", "8. ¿Quién está allí?", "あそこにだれがいますか"),
            ("ここに何がありますか。", "9. ¿Qué hay aquí?", "ここになにがありますか"),
            ("私の前に先生がいます。", "10. El profesor está delante de mí.", "わたしのまえにせんせいがいます")
        ],
        "exercises": [
            {"q": "¿Qué verbo usas para decir que HAY un LIBRO?", "options": [{"text": "います", "correct": False}, {"text": "あります", "correct": True}, {"text": "します", "correct": False}]},
            {"q": "¿Qué verbo usas para decir que HAY un GATO?", "options": [{"text": "します", "correct": False}, {"text": "あります", "correct": False}, {"text": "います", "correct": True}]},
            {"q": "¿Cómo dices 'ENCIMA de la mesa'?", "options": [{"text": "机の下 (Tsukue no shita)", "correct": False}, {"text": "机の上 (Tsukue no ue)", "correct": True}, {"text": "机の中 (Tsukue no naka)", "correct": False}]},
            {"q": "¿Cómo dices 'DENTRO de la caja' (Hako = caja)?", "options": [{"text": "箱の中 (Hako no naka)", "correct": True}, {"text": "箱の外 (Hako no soto)", "correct": False}, {"text": "箱の隣 (Hako no tonari)", "correct": False}]},
            {"q": "'El banco está AL LADO de la estación':", "options": [{"text": "銀行は駅の隣にあります。", "correct": True}, {"text": "銀行は駅の前にあります。", "correct": False}, {"text": "銀行は駅の近くにあります。", "correct": False}]},
            {"q": "'Detrás' de la escuela (Ushiro = detrás):", "options": [{"text": "学校の後ろ", "correct": True}, {"text": "学校の前", "correct": False}, {"text": "学校の下", "correct": False}]},
            {"q": "¿Qué partícula usas para indicar el lugar donde existe algo? (Ej. En la habitación _ hay...)", "options": [{"text": "へ (e)", "correct": False}, {"text": "で (de)", "correct": False}, {"text": "に (ni)", "correct": True}]},
            {"q": "Persona A: '¿Hay alguien en la sala?'. Persona B: 'No, no hay ____'.", "options": [{"text": "誰もいません (Dare mo imasen)", "correct": True}, {"text": "誰もありません (Dare mo arimasen)", "correct": False}, {"text": "何もいません (Nani mo imasen)", "correct": False}]},
            {"q": "¿Cómo dices 'Tengo dinero'?", "options": [{"text": "お金がいます。", "correct": False}, {"text": "お金があります。", "correct": True}, {"text": "お金をあります。", "correct": False}]},
            {"q": "Si hablas de una planta/árbol, ¿qué verbo usas para su existencia?", "options": [{"text": "います (porque está vivo)", "correct": False}, {"text": "あります (porque se considera inanimado/inmóvil en japonés)", "correct": True}, {"text": "Depende de la flor", "correct": False}]}
        ]
    },
    8: {
        "title": "Dar y Recibir básico (JLPT N5)",
        "grammar": [
            "<strong>あげます (Agemasu):</strong> 'Dar'. El que da (sujeto) marca con は o が. El que recibe se marca con に.",
            "<strong>もらいます (Moraimasu):</strong> 'Recibir'. El que recibe (sujeto) se marca con は o が. El que da se marca con に o から.",
            "<strong>Partícula に / から:</strong> En 'moraimasu' (recibir), la persona de la que recibes puede marcarse con に o con から. Si recibes de una organización o empresa, solo se usa から."
        ],
        "examples": [
            ("私は山田さんに本をあげました。", "1. Yo le di un libro al Sr. Yamada.", "わたしはやまださんにほんをあげました"),
            ("カリナさんは友達にプレゼントをあげました。", "2. Karina le dio un regalo a un amigo.", "カリナさんはともだちにプレゼントをあげました"),
            ("私は木村さんに花をもらいました。", "3. Yo recibí flores de la Sra. Kimura.", "わたしはきむらさんにはなをもらいました"),
            ("母から手紙をもらいました。", "4. Recibí una carta de mi madre.", "ははからてがみをもらいました"),
            ("会社からお金をもらいます。", "5. Recibo dinero de la empresa.", "かいしゃからおかねをもらいます"),
            ("誰にチョコレートをあげましたか。", "6. ¿A quién le diste chocolate?", "だれにチョコレートをあげましたか"),
            ("誰からその時計をもらいましたか。", "7. ¿De quién recibiste ese reloj?", "だれからそのとけいをもらいましたか"),
            ("先生に辞書を貸してあげました。(Nota: No es usual en N5 usar forma te-agemasu con superiores, pero es gramaticalmente correcto)", "8. Le presté el diccionario al profesor.", "せんせいにじしょをかしてあげました"),
            ("父にネクタイをあげます。", "9. Le daré una corbata a mi padre.", "ちちにネクタイをあげます"),
            ("田中さんに英語を教えてもらいました。", "10. Recibí enseñanzas de inglés de Tanaka.", "たなかさんにえいごをおしえてもらいました")
        ],
        "exercises": [
            {"q": "¿Qué verbo significa 'DAR'?", "options": [{"text": "もらいます", "correct": False}, {"text": "あげます", "correct": True}, {"text": "あります", "correct": False}]},
            {"q": "¿Qué verbo significa 'RECIBIR'?", "options": [{"text": "あげます", "correct": False}, {"text": "もらいます", "correct": True}, {"text": "います", "correct": False}]},
            {"q": "'Le di una flor A María'. ¿Qué partícula va después de María?", "options": [{"text": "は (wa)", "correct": False}, {"text": "に (ni)", "correct": True}, {"text": "を (wo)", "correct": False}]},
            {"q": "'Recibí un regalo DE Carlos'. ¿Qué partícula va después de Carlos?", "options": [{"text": "に (ni) o から (kara)", "correct": True}, {"text": "へ (e) o と (to)", "correct": False}, {"text": "を (wo) o は (wa)", "correct": False}]},
            {"q": "Si dices '会社 ___ 給料をもらいました' (Recibí el sueldo de la empresa), ¿qué partícula se usa para la empresa?", "options": [{"text": "から (kara) obligatoriamente", "correct": True}, {"text": "に (ni) obligatoriamente", "correct": False}, {"text": "を (wo)", "correct": False}]},
            {"q": "Persona A: '¡Qué buen CD!'. Persona B: 'Sí, lo ___ de un amigo'.", "options": [{"text": "あげました (Agemashita)", "correct": False}, {"text": "もらいました (Moraimashita)", "correct": True}, {"text": "買いました (Kaimashita)", "correct": False}]},
            {"q": "¿Cómo preguntas 'A quién se lo diste?'", "options": [{"text": "誰にあげましたか。", "correct": True}, {"text": "誰にもらいましたか。", "correct": False}, {"text": "誰があげましたか。", "correct": False}]},
            {"q": "¿Cómo preguntas 'De quién lo recibiste?'", "options": [{"text": "誰にあげましたか。", "correct": False}, {"text": "誰からもらいましたか。", "correct": True}, {"text": "誰をあげましたか。", "correct": False}]},
            {"q": "Si prestas algo a alguien, gramaticalmente ¿estás DANDO o RECIBIENDO un objeto temporalmente?", "options": [{"text": "Dando, la estructura es similar a あげます. (貸します - kashimasu)", "correct": True}, {"text": "Recibiendo.", "correct": False}, {"text": "Ninguna de las dos.", "correct": False}]},
            {"q": "'Me prestaron un libro' / 'Tomé prestado' (Karimasu), la estructura es similar a:", "options": [{"text": "もらいます (Recibir). Origen se marca con に/から.", "correct": True}, {"text": "あげます (Dar)", "correct": False}, {"text": "います (Existir)", "correct": False}]}
        ]
    },
    9: {
        "title": "Sugerencias e Invitaciones (ましょう / ませんか)",
        "grammar": [
            "<strong>~ましょう (Mashou):</strong> 'Hagamos... / Vamos a...'. Expresa la sugerencia o intención de hacer algo juntos.",
            "<strong>~ませんか (Masen ka):</strong> '¿No te gustaría...? / ¿Qué tal si...?'. Es una invitación más cortés que mashou, porque le da al oyente la opción de decir no.",
            "<strong>V(te) ください (te kudasai):</strong> 'Por favor haz...'. Petición directa y formal."
        ],
        "examples": [
            ("一緒に京都へ行きませんか。", "1. ¿No te gustaría ir juntos a Kioto?", "いっしょにきょうとへいきませんか"),
            ("ええ、いいですね。行きましょう。", "2. Sí, qué buena idea. Vamos.", "ええ、いいですね。いきましょう"),
            ("お茶を飲みませんか。", "3. ¿Tomamos un té?", "おちゃをのみませんか"),
            ("すみません。ちょっと...", "4. Lo siento, es que... (Rechazo cortés)", "すみません。ちょっと..."),
            ("少し休みましょう。", "5. Descansemos un poco.", "すこしやすみましょう"),
            ("昼ごはんを食べましょう。", "6. Vamos a almorzar.", "ひるごはんをたべましょう"),
            ("ちょっと待ってください。", "7. Por favor, espera un momento.", "ちょっとまってください"),
            ("ここに名前を書いてください。", "8. Por favor, escribe tu nombre aquí.", "ここになまえをかいてください"),
            ("タクシーを呼びましょうか。", "9. ¿Llamo a un taxi?", "タクシーをよびましょうか"),
            ("はい、お願いします。", "10. Sí, te lo pido.", "はい、おねがいします")
        ],
        "exercises": [
            {"q": "¿Qué sufijo se usa para invitar a alguien cortésmente? (Ej. ¿No quieres beber...?)", "options": [{"text": "〜ましょう (Mashou)", "correct": False}, {"text": "〜ませんか (Masen ka)", "correct": True}, {"text": "〜ますか (Masu ka)", "correct": False}]},
            {"q": "¿Cómo se dice 'Vamos' (Proposición directa)?", "options": [{"text": "行きましょう (Ikimashou)", "correct": True}, {"text": "行きます (Ikimasu)", "correct": False}, {"text": "行きませんか (Ikimasen ka)", "correct": False}]},
            {"q": "¿Cuál es la respuesta positiva más natural a '行きませんか' (¿No quieres ir?)?", "options": [{"text": "いいえ、行きません。", "correct": False}, {"text": "ええ、いいですね。行きましょう。", "correct": True}, {"text": "はい、行きますか。", "correct": False}]},
            {"q": "¿Cómo rechazas CORTÉSMENTE una invitación en japonés sin sonar grosero?", "options": [{"text": "いいえ、行きません。 (Iie, ikimasen)", "correct": False}, {"text": "すみません、ちょっと... (Sumimasen, chotto...)", "correct": True}, {"text": "ダメです。 (Dame desu)", "correct": False}]},
            {"q": "¿Qué significa '〜てください' (te kudasai)?", "options": [{"text": "Por favor, haz... (Petición)", "correct": True}, {"text": "Hagamos...", "correct": False}, {"text": "¿No quieres hacer...?", "correct": False}]},
            {"q": "'Por favor, lee':", "options": [{"text": "読みてください (Yomite kudasai)", "correct": False}, {"text": "読んでください (Yonde kudasai)", "correct": True}, {"text": "読んてください (Yonte kudasai)", "correct": False}]},
            {"q": "'Por favor, mírame' (Ver = Mimasu):", "options": [{"text": "見てください (Mite kudasai)", "correct": True}, {"text": "みんでください (Minde kudasai)", "correct": False}, {"text": "みててください (Mitete kudasai)", "correct": False}]},
            {"q": "¿Qué significa 'V-ましょうか' (Mashou ka)? Ej. 窓を開けましょうか (Mado o akemashou ka).", "options": [{"text": "¿Lo hago por ti? (Ofrecimiento de ayuda)", "correct": True}, {"text": "Hazlo por mí", "correct": False}, {"text": "Hagámoslo juntos (sin ofrecer ayuda unilateral)", "correct": False}]},
            {"q": "¿Cómo respondes a '¿Te ayudo?' (Mashou ka) si SÍ quieres ayuda?", "options": [{"text": "はい、お願いします (Hai, onegaishimasu)", "correct": True}, {"text": "いいえ、結構です (Iie, kekkou desu)", "correct": False}, {"text": "はい、しましょう (Hai, shimashou)", "correct": False}]},
            {"q": "¿Cómo respondes a '¿Te ayudo?' si NO necesitas ayuda (No, gracias)?", "options": [{"text": "いいえ、お願いします", "correct": False}, {"text": "いいえ、結構です (Iie, kekkou desu)", "correct": True}, {"text": "いいえ、しません", "correct": False}]}
        ]
    },
    10: {
        "title": "Conjunciones y Conectores JLPT N5",
        "grammar": [
            "<strong>そして (Soshite):</strong> 'Y / Además'. Conecta dos oraciones independientes (A. Soshite, B).",
            "<strong>それから (Sorekara):</strong> 'Y luego / Después de eso'. Enfatiza el orden temporal de acciones sucesivas.",
            "<strong>でも / しかし (Demo / Shikashi):</strong> 'Pero / Sin embargo'. Oposición entre oraciones.",
            "<strong>〜から (kara):</strong> 'Porque...'. Va al FINAL de la oración que explica el motivo. Ej: 忙しいですから (Porque estoy ocupado).",
            "<strong>〜が (ga):</strong> '..., pero ...'. Conecta dos ideas opuestas en una sola oración. Ej: 高いですが、いいです (Es caro, pero es bueno)."
        ],
        "examples": [
            ("このカメラは安いです。そして、とても便利です。", "1. Esta cámara es barata. Y (además), es muy conveniente.", "このカメラはやすいです。そして、とてもべんりです"),
            ("朝ごはんを食べました。それから、新聞を読みました。", "2. Desayuné. Y luego leí el periódico.", "あさごはんをたべました。それから、しんぶんをよみました"),
            ("日本料理はおいしいです。でも、高いです。", "3. La comida japonesa es deliciosa. Pero es cara.", "にほんりょうりはおいしいです。でも、たかいです"),
            ("時間がありませんから、タクシーで行きましょう。", "4. Como no hay tiempo (porque no hay), vayamos en taxi.", "じかんがありませんから、タクシーでいきましょう"),
            ("どうして遅れましたか。バスが来ませんでしたから。", "5. ¿Por qué llegaste tarde? Porque el autobús no vino.", "どうしておくれましたか。バスがきませんでしたから"),
            ("日本の生活はどうですか。忙しいですが、楽しいです。", "6. ¿Qué tal la vida en Japón? Es ocupada, pero divertida.", "にほんのせいかつはどうですか。いそがしいですが、たのしいです"),
            ("漢字は難しいですが、面白いです。", "7. Los kanjis son difíciles, pero interesantes.", "かんじはむずかしいですが、おもしろいです"),
            ("昨日は疲れました。ですから、早く寝ました。", "8. Ayer estaba cansado. Por eso, me dormí temprano.", "きのうはつかれました。ですから、はやくねました"),
            ("毎日６時に起きます。そしてシャワーを浴びます。", "9. Todos los días me levanto a las 6. Y (luego) me ducho.", "まいにちろくじにおきます。そしてシャワーをあびます"),
            ("りんごとバナナを買いました。", "10. Compré manzanas y bananas (conjunción 'to' para sustantivos, no soshite).", "りんごとバナナをかいました")
        ],
        "exercises": [
            {"q": "¿Qué conector usas para unir dos oraciones independientes sumando información (Y / Además)?", "options": [{"text": "でも (Demo)", "correct": False}, {"text": "そして (Soshite)", "correct": True}, {"text": "から (Kara)", "correct": False}]},
            {"q": "¿Qué conector usas para indicar secuencia temporal 'Y LUEGO / DESPUÉS DE ESO'?", "options": [{"text": "それから (Sorekara)", "correct": True}, {"text": "でも (Demo)", "correct": False}, {"text": "が (ga)", "correct": False}]},
            {"q": "Persona A: 'La cámara es buena. ___ es cara'.", "options": [{"text": "そして", "correct": False}, {"text": "でも (Pero)", "correct": True}, {"text": "それから", "correct": False}]},
            {"q": "¿Dónde se coloca 'から' para decir 'Porque estoy ocupado'?", "options": [{"text": "から忙しいです。(Kara isogashii desu)", "correct": False}, {"text": "忙しいですから。(Isogashii desu kara)", "correct": True}, {"text": "忙しいからですが。(Isogashii kara desu ga)", "correct": False}]},
            {"q": "¿Qué conjunción une dos ideas opuestas en la MISMA oración ('A es barato, PERO B es caro')?", "options": [{"text": "が (ga)", "correct": True}, {"text": "でも (demo - se usa para iniciar una NUEVA oración)", "correct": False}, {"text": "から (kara)", "correct": False}]},
            {"q": "'El japonés es difícil, pero interesante':", "options": [{"text": "日本語は難しいですが、面白いです。", "correct": True}, {"text": "日本語は難しいから、面白いです。", "correct": False}, {"text": "日本語は難しいです。が、面白いです。", "correct": False}]},
            {"q": "Pregunta: '¿POR QUÉ (Doushite) vas a dormir?'. Respuesta: '_____ tengo sueño'.", "options": [{"text": "眠いですから (Nemui desu kara)", "correct": True}, {"text": "眠いですが (Nemui desu ga)", "correct": False}, {"text": "眠いですね (Nemui desu ne)", "correct": False}]},
            {"q": "¿Puedes unir dos SUSTANTIVOS (Ej. Gato y perro) con そして (Soshite)?", "options": [{"text": "Sí (猫そして犬)", "correct": False}, {"text": "No, se debe usar と (猫と犬)", "correct": True}, {"text": "Sí, si se añade 'desu'", "correct": False}]},
            {"q": "¿Qué significa 'ですから' (Desukara) al inicio de una frase?", "options": [{"text": "Pero", "correct": False}, {"text": "Por lo tanto / Por eso", "correct": True}, {"text": "Y luego", "correct": False}]},
            {"q": "'Me lavo las manos. Y luego, como':", "options": [{"text": "手を洗います。でも、食べます。", "correct": False}, {"text": "手を洗います。それから、食べます。", "correct": True}, {"text": "手を洗います。ですから、食べます。", "correct": False}]}
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
