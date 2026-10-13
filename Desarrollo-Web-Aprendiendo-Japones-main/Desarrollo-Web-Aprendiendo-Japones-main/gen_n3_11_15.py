import os
import subprocess

data = {
    11: {
        "title": "Aspectos Temporales (~ところだ / ~ばかりだ)",
        "grammar": [
            "<strong>V(dic) + ところだ:</strong> A punto de empezar. Ej. 今から食べるところだ (Estoy a punto de comer ahora).",
            "<strong>V(て)いる + ところだ:</strong> En medio de la acción. Ej. 今、食べているところだ (Estoy en medio de la comida ahora mismo).",
            "<strong>V(た) + ところだ:</strong> Justo acabo de terminar. Ej. たった今、食べたところだ (Acabo de comer justo ahora).",
            "<strong>V(た) + ばかりだ:</strong> Acabo de hacerlo (puede haber pasado un tiempo, pero psicológicamente se siente reciente). Ej. 去年、日本へ来たばかりだ (Acabo de llegar a Japón el año pasado)."
        ],
        "examples": [
            ("今、家を出るところです。", "1. Estoy a punto de salir de casa ahora.", "いま、いえをでるところです"),
            ("これから会議が始まるところだ。", "2. La reunión está a punto de empezar a partir de ahora.", "これらかかいぎがはじまるところだ"),
            ("今、メールを書いているところです。", "3. Estoy escribiendo el correo en este preciso momento.", "いま、メールをかいているところです"),
            ("たった今、駅に着いたところです。", "4. Acabo de llegar a la estación justo ahora.", "たったいま、えきについたところです"),
            ("そのケーキは今焼けたところですよ。", "5. Ese pastel acaba de hornearse justo ahora.", "そのケーキはいまやけたところですよ"),
            ("さっきご飯を食べたばかりだから、お腹がいっぱいです。", "6. Como acabo de comer hace un momento, estoy lleno.", "さっきごはんをたべたばかりだから、おなかがいっぱいです"),
            ("先月、この会社に入ったばかりです。", "7. Acabo de entrar a esta empresa el mes pasado (sentimiento de que es reciente).", "せんげつ、このかいしゃにはいったばかりです"),
            ("買ったばかりのパソコンが壊れてしまった。", "8. La computadora que acabo de comprar se ha roto.", "かったばかりのパソコンがこわれてしまった"),
            ("今、本を読んでいるところだから、後にして。", "9. Estoy leyendo un libro ahora mismo, así que déjalo para después.", "いま、ほんをよんでいるところだから、あとにして"),
            ("今、起きるところです...", "10. Estoy a punto de levantarme...", "いま、おきるところです")
        ],
        "exercises": [
            {"q": "¿Qué expresión se usa para 'A punto de empezar'?", "options": [{"text": "V(dic) + ところだ", "correct": True}, {"text": "V(た) + ところだ", "correct": False}, {"text": "V(て)いる + ところだ", "correct": False}]},
            {"q": "¿Qué expresión se usa para 'Acabo de terminar justo ahora'?", "options": [{"text": "V(た) + ところだ", "correct": True}, {"text": "V(dic) + ところだ", "correct": False}, {"text": "V(て)いる + ところだ", "correct": False}]},
            {"q": "Diferencia: ¿Cuál de las dos expresa que la acción ocurrió 'hace un rato / hace unos meses' pero se siente reciente?", "options": [{"text": "V(た) + ばかりだ", "correct": True}, {"text": "V(た) + ところだ", "correct": False}, {"text": "Ambas son idénticas", "correct": False}]},
            {"q": "'El tren está a punto de salir' (Deru):", "options": [{"text": "電車が出るところです", "correct": True}, {"text": "電車が出たところです", "correct": False}, {"text": "電車が出たばかりです", "correct": False}]},
            {"q": "'Estoy almorzando en este momento' (Hiru gohan o taberu):", "options": [{"text": "昼ご飯を食べているところです", "correct": True}, {"text": "昼ご飯を食べるところです", "correct": False}, {"text": "昼ご飯を食べたところです", "correct": False}]},
            {"q": "'Acabo de comprar este coche el año pasado' (Katta):", "options": [{"text": "去年買ったばかりです", "correct": True}, {"text": "去年買ったところです", "correct": False}, {"text": "去年買うところです", "correct": False}]},
            {"q": "'Acabo de llegar a casa JUSTO AHORA (Tatta ima)': 家に着いた___。", "options": [{"text": "ところです", "correct": True}, {"text": "ばかりです", "correct": False}, {"text": "ところだです", "correct": False}]},
            {"q": "'La cámara que acabo de comprar' (Katta + Bakari + Sustantivo):", "options": [{"text": "買ったばかりのカメラ", "correct": True}, {"text": "買ったばかりなカメラ", "correct": False}, {"text": "買ったばかりカメラ", "correct": False}]},
            {"q": "A: '¿Ya enviaste el correo?' B: 'No, lo estoy escribiendo ahora mismo'.", "options": [{"text": "いいえ、今書いているところです。", "correct": True}, {"text": "いいえ、今書いたところです。", "correct": False}, {"text": "いいえ、今書くところです。", "correct": False}]},
            {"q": "A: '¿Estás ocupado?' B: 'Sí, estoy a punto de salir a una reunión'.", "options": [{"text": "はい、会議に出るところです。", "correct": True}, {"text": "はい、会議に出たところです。", "correct": False}, {"text": "はい、会議に出たばかりです。", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "もしもし、山田さん。今、大丈夫ですか。", "Diga, Yamada. ¿Te va bien ahora?"),
            ("ja-JP-KeitaNeural", "ああ、すみません。今、ちょうど家を出るところなんですよ。", "Ah, lo siento. Justo ahora estoy a punto de salir de casa."),
            ("ja-JP-NanamiNeural", "そうでしたか。急ぎの用事だったんですが...", "¿Ah sí? Era un asunto urgente, pero..."),
            ("ja-JP-KeitaNeural", "走りながら電話で話しているところなので、後でかけ直してもいいですか。", "Como estoy hablando por teléfono mientras corro, ¿te puedo devolver la llamada luego?"),
            ("ja-JP-NanamiNeural", "わかりました。気をつけてね。", "Entendido. Ten cuidado."),
            ("ja-JP-KeitaNeural", "（30分後）もしもし、たった今、駅に着いたところです。さっきはどうしましたか。", "(30 min después) Diga, justo ahora acabo de llegar a la estación. ¿Qué pasaba antes?"),
            ("ja-JP-NanamiNeural", "実は、昨日買ったばかりのパソコンが壊れてしまって、直し方を知りませんか。", "La verdad es que la computadora que acabo de comprar ayer se rompió, ¿no sabes cómo arreglarla?"),
            ("ja-JP-KeitaNeural", "ええっ、買ったばかりなのに！？", "¡Eh! ¿A pesar de que la acabas de comprar?")
        ]
    },
    12: {
        "title": "Expresiones de Razón y Causa (~おかげで / ~せいで / ~ばっかりに)",
        "grammar": [
            "<strong>~おかげで (Okage de):</strong> 'Gracias a...'. Se usa para expresar una causa que trae un buen resultado (Agradecimiento). Ej. 先生のおかげで合格できた (Gracias al profesor pude aprobar).",
            "<strong>~せいで (Sei de):</strong> 'Por culpa de...'. Se usa para una causa que trae un mal resultado (Culpa). Ej. 雨のせいで遅れた (Llegué tarde por culpa de la lluvia).",
            "<strong>V(ta) + ばっかりに:</strong> 'Solo por haber... / Por el simple hecho de...'. Expresa arrepentimiento extremo por una pequeña acción que causó un gran problema. Ej. 嘘をついたばっかりに、彼女と別れた (Solo por haber dicho una mentira, terminé con mi novia)."
        ],
        "examples": [
            ("薬を飲んだおかげで、熱が下がりました。", "1. Gracias a que tomé la medicina, la fiebre bajó.", "くすりをのんだおかげで、ねつがさがりました"),
            ("田中さんが手伝ってくれたおかげで、早く終わりました。", "2. Gracias a que Tanaka me ayudó, terminé rápido.", "たなかさんがてつだってくれたおかげで、はやくおわりました"),
            ("バスが遅れたせいで、会議に間に合わなかった。", "3. Por culpa de que el autobús se retrasó, no llegué a tiempo a la reunión.", "バスがおくれたせいで、かいぎにまにあわなかった"),
            ("最近忙しいせいで、とても疲れている。", "4. Por culpa de estar ocupado últimamente, estoy muy cansado.", "さいきんいそがしいせいで、とてもつかれている"),
            ("スマホを忘れたせいで、誰にも連絡できなかった。", "5. Por culpa de haber olvidado el móvil, no pude contactar a nadie.", "スマホをわすれたせいで、だれにもれんらくできなかった"),
            ("あの日、あの電車に乗ったばっかりに、事故に巻き込まれた。", "6. Solo por haberme subido a ese tren aquel día, me vi envuelto en el accidente.", "あのひ、あのでんしゃにのったばっかりに、じこにまきこまれた"),
            ("一言「ごめんなさい」と言わなかったばっかりに、大喧嘩になった。", "7. Solo por no haber dicho una palabra 'perdón', se formó una gran pelea.", "ひとこと「ごめんなさい」といわなかったばっかりに、おおげんかになった"),
            ("先生のおかげで、日本語が上手になりました。", "8. Gracias al profesor, me he vuelto bueno en japonés.", "せんせいのおかげで、にほんごがじょうずになりました"),
            ("私のせいで、みんなに迷惑をかけてすみません。", "9. Siento haber causado molestias a todos por mi culpa.", "わたしのせいで、みんなにめいわくをかけてすみません"),
            ("少し寝坊したばっかりに、飛行機に乗り遅れた。", "10. Solo por haberme quedado dormido un poco, perdí el avión.", "すこしねぼうしたばっかりに、ひこうきにのりおくれた")
        ],
        "exercises": [
            {"q": "¿Qué expresión se usa cuando la causa genera un BUEN resultado (Gracias a...)?", "options": [{"text": "おかげで", "correct": True}, {"text": "せいで", "correct": False}, {"text": "ばっかりに", "correct": False}]},
            {"q": "¿Qué expresión se usa cuando la causa genera un MAL resultado (Por culpa de...)?", "options": [{"text": "せいで", "correct": True}, {"text": "おかげで", "correct": False}, {"text": "ために", "correct": False}]},
            {"q": "¿Qué expresión indica arrepentimiento porque una acción pequeña causó un gran problema?", "options": [{"text": "ばっかりに", "correct": True}, {"text": "せいで", "correct": False}, {"text": "おかげで", "correct": False}]},
            {"q": "'Por culpa del calor, no pude dormir' (Atsui):", "options": [{"text": "暑いせいで、眠れなかった", "correct": True}, {"text": "暑いおかげで、眠れなかった", "correct": False}, {"text": "暑いばっかりに、眠れなかった", "correct": False}]},
            {"q": "'Gracias a que el clima fue bueno, el viaje fue divertido' (Tenki ga yokatta):", "options": [{"text": "天気が良かったおかげで", "correct": True}, {"text": "天気が良かったせいで", "correct": False}, {"text": "天気が良かったばっかりに", "correct": False}]},
            {"q": "Para usar un sustantivo con Okage de / Sei de. (Ej. Amigo -> Tomodachi):", "options": [{"text": "友達のおかげで / 友達のせいで", "correct": True}, {"text": "友達おかげで / 友達せいで", "correct": False}, {"text": "友達なおかげで / 友達なせいで", "correct": False}]},
            {"q": "'Solo por haber olvidado la cartera, no pude subir al tren' (Wasureta):", "options": [{"text": "忘れたばっかりに", "correct": True}, {"text": "忘れるばっかりに", "correct": False}, {"text": "忘れたせいでに", "correct": False}]},
            {"q": "Para adjetivos Na (Ej. Hima - Libre): 'Por culpa de estar libre...'", "options": [{"text": "暇なせいで", "correct": True}, {"text": "暇のせいで", "correct": False}, {"text": "暇だせいで", "correct": False}]},
            {"q": "'Gracias a que estudié todos los días, aprobé el N3' (Benkyou shita):", "options": [{"text": "勉強したおかげで", "correct": True}, {"text": "勉強したせいで", "correct": False}, {"text": "勉強するおかげで", "correct": False}]},
            {"q": "'Por mi culpa...' (Watashi):", "options": [{"text": "私のせいで", "correct": True}, {"text": "私のおかげで", "correct": False}, {"text": "私がせいで", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-KeitaNeural", "あー、もう最悪だ！", "¡Ah, qué desastre!"),
            ("ja-JP-NanamiNeural", "どうしたの？怒っているみたいだけど。", "¿Qué pasó? Pareces enojado."),
            ("ja-JP-KeitaNeural", "電車が遅れたせいで、大事な会議に間に合わなかったんだ。", "Por culpa de que el tren se retrasó, no llegué a tiempo a una reunión importante."),
            ("ja-JP-NanamiNeural", "それは大変だったね。でも、電車の遅れならあなたのせいじゃないよ。", "Eso fue terrible. Pero si fue el retraso del tren, no es tu culpa."),
            ("ja-JP-KeitaNeural", "いや、僕のせいでもあるんだ。朝、少し寝坊したばっかりに、一本遅い電車に乗ることになって...。", "No, también es mi culpa. Solo por haberme quedado dormido un poco por la mañana, tuve que subir a un tren más tarde..."),
            ("ja-JP-NanamiNeural", "なるほどね。でも、クビにならなかったおかげで、まだチャンスはあるよ！", "Ya veo. Pero gracias a que no te despidieron, ¡aún hay oportunidad!"),
            ("ja-JP-KeitaNeural", "そうだけどさ...。君の前向きな性格のおかげで、少し元気が出たよ。ありがとう。", "Sí, pero... Gracias a tu personalidad positiva, me he animado un poco. Gracias.")
        ]
    },
    13: {
        "title": "Propósito y Extensión (~ために / ~ように / ~ほど / ~くらい)",
        "grammar": [
            "<strong>Nの/V(dic) + ために:</strong> Para / Con el propósito de. Implica una fuerte voluntad y control sobre la acción. Ej. 車を買うために、貯金している (Ahorro para comprar un coche).",
            "<strong>V(dic/nai) + ように:</strong> Para que / De modo que. El sujeto no tiene control directo sobre el resultado o es un estado/potencial. Ej. 買えるように、貯金している (Ahorro para poder comprarlo).",
            "<strong>~ほど (Hodo):</strong> Tanto como... / Al grado de... Expresa el grado o extensión máxima de algo. Ej. 泣きたいほど痛い (Duele tanto que quiero llorar).",
            "<strong>~くらい / ぐらい (Kurai):</strong> Un grado ligero o aproximación. 'Apenas un poco / Al menos'. Ej. 挨拶くらいできる (Al menos puedo saludar)."
        ],
        "examples": [
            ("家族のために、毎日一生懸命働いています。", "1. Trabajo duro todos los días por mi familia (Propósito).", "かぞくのために、まいにちいっしょうけんめいはたらいています"),
            ("家を買うために、お金を貯めています。", "2. Estoy ahorrando dinero para comprar una casa (Acción con voluntad).", "いえをかうために、おかねをためています"),
            ("家が買えるように、お金を貯めています。", "3. Estoy ahorrando para poder comprar una casa (Potencial = You ni).", "いえがかえるように、おかねをためています"),
            ("みんなに聞こえるように、大きな声で話してください。", "4. Por favor, hable en voz alta para que todos puedan escuchar.", "みんなにきこえるように、おおきなこえではなしてください"),
            ("忘れないように、メモをしておきます。", "5. Tomaré notas para no olvidar (Estado negativo = You ni).", "わすれないように、メモをしておきます"),
            ("死ぬほど疲れました。", "6. Estoy tan cansado que podría morir (Extensión máxima).", "しぬほどつかれました"),
            ("富士山は、登るのが大変なほど美しい。", "7. El monte Fuji es tan hermoso como dura es su subida.", "ふじさんは、のぼるのがたいへんなほどうつくしい"),
            ("ひらがなぐらい読めますよ。", "8. Al menos puedo leer hiragana (Nivel mínimo).", "ひらがなぐらいよめますよ"),
            ("少し熱があるくらいで、病院へは行かない。", "9. No voy a ir al hospital solo por tener un poco de fiebre.", "すこしねつがあるくらいで、びょういんへはいかない"),
            ("健康のために、毎日野菜を食べるようにしている。", "10. Por mi salud, hago el esfuerzo de comer verduras (Tame ni + You ni shite iru).", "けんこうのために、まいにちやさいをたべるようにしている")
        ],
        "exercises": [
            {"q": "¿Qué partícula usas si tu objetivo es controlable y tiene mucha voluntad? (Ej. Comprar una casa -> Kau ___)", "options": [{"text": "ために", "correct": True}, {"text": "ように", "correct": False}, {"text": "ほど", "correct": False}]},
            {"q": "¿Qué partícula usas si tu objetivo usa la forma potencial o un verbo de estado? (Ej. Poder comprar -> Kaeru ___)", "options": [{"text": "ように", "correct": True}, {"text": "ために", "correct": False}, {"text": "くらい", "correct": False}]},
            {"q": "Para expresar 'A tal grado que podría morir': 死ぬ___。", "options": [{"text": "ほど", "correct": True}, {"text": "くらい", "correct": False}, {"text": "ために", "correct": False}]},
            {"q": "'Aprenderé japonés para ir a Japón' (Iku): 日本へ行く___日本語を勉強する。", "options": [{"text": "ために", "correct": True}, {"text": "ように", "correct": False}, {"text": "ほど", "correct": False}]},
            {"q": "'Estudio japonés para (poder) ir a Japón' (Ikeru): 日本へ行ける___日本語を勉強する。", "options": [{"text": "ように", "correct": True}, {"text": "ために", "correct": False}, {"text": "ほど", "correct": False}]},
            {"q": "Para expresar un nivel mínimo o un poco: 'Al menos puedo escribir mi nombre'.", "options": [{"text": "名前くらい書ける", "correct": True}, {"text": "名前ほど書ける", "correct": False}, {"text": "名前ために書ける", "correct": False}]},
            {"q": "'Tengo tanto dolor de estómago que no puedo moverme' (Ugokenai): 動けない___お腹が痛い。", "options": [{"text": "ほど", "correct": True}, {"text": "ために", "correct": False}, {"text": "ように", "correct": False}]},
            {"q": "Ojo: Verbo negativo (Nai). 'Para NO resfriarse' (Kaze o hikanai).", "options": [{"text": "風邪をひかないように", "correct": True}, {"text": "風邪をひかないために", "correct": False}, {"text": "風邪をひかないほど", "correct": False}]},
            {"q": "Sustantivo: 'Para mi familia' (Kazoku):", "options": [{"text": "家族のために", "correct": True}, {"text": "家族のように", "correct": False}, {"text": "家族のほど", "correct": False}]},
            {"q": "'Tanaka es amable, pero no TANTO COMO Suzuki'. 鈴木さん___優しくない。", "options": [{"text": "ほど", "correct": True}, {"text": "くらい", "correct": False}, {"text": "ために", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "田中さん、最近毎日ジムに行っているそうですね。", "Tanaka, he oído que últimamente vas al gimnasio todos los días."),
            ("ja-JP-KeitaNeural", "ええ、来月のマラソン大会で優勝するために、トレーニングをしているんです。", "Sí, estoy entrenando con el propósito de ganar el maratón del próximo mes."),
            ("ja-JP-NanamiNeural", "優勝ですか！それはすごいですね。", "¡Ganar! Eso es increíble."),
            ("ja-JP-KeitaNeural", "毎日、足が痛くて泣きたいほど走っていますよ。", "Todos los días corro a tal grado que me duelen las piernas y me dan ganas de llorar."),
            ("ja-JP-NanamiNeural", "無理はしないでくださいね。怪我をしないように気をつけてください。", "No te sobreesfuerces. Ten cuidado para no lastimarte (estado)."),
            ("ja-JP-KeitaNeural", "ありがとうございます。本番で実力が出せるように、しっかり休みも取りますよ。", "Gracias. Tomaré buenos descansos para que (poder) demostrar mi capacidad en el evento principal."),
            ("ja-JP-NanamiNeural", "ええ、少し筋肉痛になるくらいなら大丈夫ですが、怪我は怖いですから。", "Sí, al nivel de tener un poco de dolor muscular está bien, pero las lesiones dan miedo.")
        ]
    },
    14: {
        "title": "Expectativa y Oposición (~はずだ / ~わけがない / ~くせに / ~わりに)",
        "grammar": [
            "<strong>~はずだ (Hazu da):</strong> 'Debería ser / Es lógico que'. Expectativa basada en lógica fuerte. Ej. 彼も来るはずだ (Es lógico que él también venga).",
            "<strong>~わけがない (Wake ga nai):</strong> 'No hay motivo/Es absolutamente imposible que'. Negación lógica extrema. Ej. こんな高い服、買えるわけがない (Es imposible que pueda comprar ropa tan cara).",
            "<strong>~くせに (Kuse ni):</strong> 'A pesar de que / Y eso que...'. Contraste usado para criticar o menospreciar a alguien (tono emocional negativo). Ej. 男のくせに泣くな (No llores, siendo/a pesar de que eres un hombre).",
            "<strong>~わりに(は) (Wari ni wa):</strong> 'Para ser... / Considerando que...'. Expresa una desproporción positiva o negativa sin tanta crítica. Ej. 値段のわりに美味しい (Para el precio que tiene, es delicioso)."
        ],
        "examples": [
            ("田中さんはアメリカに10年住んでいたから、英語が話せるはずだ。", "1. Tanaka vivió en EE. UU. 10 años, así que es lógico que sepa hablar inglés.", "たなかさんはアメリカにじゅうねんすんでいたから、えいごがはなせるはずだ"),
            ("あんなに勉強しなかったんだから、テストに合格するわけがない。", "2. Como no estudió nada, es totalmente imposible que apruebe el examen.", "あんなにべんきょうしなかったんだから、テストにごうかくするわけがない"),
            ("彼は何でも知っているはずなのに、何も答えない。", "3. A pesar de que él debería saberlo todo, no responde nada.", "かれはなんでもしっているはずなのに、なにもこたえない"),
            ("あの人は、お金がないと言っているくせに、いつも新しい服を着ている。", "4. Esa persona, a pesar de que dice no tener dinero (crítica), siempre usa ropa nueva.", "あのひとは、おかねがないといっているくせに、いつもあたらしいふくをきている"),
            ("子供のくせに、大人みたいな口をきく。", "5. A pesar de ser un niño, habla como un adulto (Crítica/Queja).", "こどものくせに、おとなみたいなくちをきく"),
            ("このレストランは、値段が高いわりに、美味しくない。", "6. Este restaurante, para lo caro que es, no es sabroso (Desproporción).", "このレストランは、ねだんがたかいわりに、おいしくない"),
            ("彼は若いわりに、とてもしっかりしている。", "7. Para ser joven, él es muy maduro/responsable (Desproporción positiva).", "かれはわかいわりに、とてもしっかりしている"),
            ("こんな難しい仕事、一人で終わるわけがありません。", "8. Un trabajo tan difícil, es imposible que se termine solo.", "こんなむずかしいしごと、ひとりで終わるわけがありません"),
            ("山田さんは今日休みだから、会議に来るはずがありません。", "9. Yamada descansa hoy, así que es imposible (no debería) venir a la reunión.", "やまださんはきょうやすみだから、かいぎにくるはずがありません"),
            ("知っているくせに、教えてくれない。", "10. A pesar de que lo sabes (y me molesta), no me lo dices.", "しっているくせに、おしえてくれない")
        ],
        "exercises": [
            {"q": "¿Qué expresión denota una negación fuerte ('Es imposible que... / No hay razón lógica para que...')?", "options": [{"text": "～わけがない", "correct": True}, {"text": "～はずだ", "correct": False}, {"text": "～わりに", "correct": False}]},
            {"q": "¿Qué expresión indica una conclusión lógica fuerte ('Es lógico que / Debería ser que...')?", "options": [{"text": "～はずだ", "correct": True}, {"text": "～くせに", "correct": False}, {"text": "～わけがない", "correct": False}]},
            {"q": "¿Qué expresión de contraste se usa principalmente para CRITICAR o QUEJARSE de alguien ('Y eso que eres...')?", "options": [{"text": "～くせに", "correct": True}, {"text": "～わりに", "correct": False}, {"text": "～はずだ", "correct": False}]},
            {"q": "¿Qué expresión de contraste marca una desproporción ('Para ser / Considerando que...') y puede ser positiva?", "options": [{"text": "～わりに(は)", "correct": True}, {"text": "～くせに", "correct": False}, {"text": "～わけがない", "correct": False}]},
            {"q": "'A pesar de que eres estudiante (Gakusei), no estudias nada' (Crítica):", "options": [{"text": "学生のくせに", "correct": True}, {"text": "学生のわりに", "correct": False}, {"text": "学生のはずだ", "correct": False}]},
            {"q": "'Esta bolsa, para los 100 yenes que cuesta, es muy resistente' (100-en):", "options": [{"text": "１００円のわりに", "correct": True}, {"text": "１００円のくせに", "correct": False}, {"text": "１００円のわけがない", "correct": False}]},
            {"q": "'Tanaka siempre llega a tiempo. ¡ES IMPOSIBLE que llegue tarde!' (Okureru):", "options": [{"text": "遅れるわけがない", "correct": True}, {"text": "遅れるはずだ", "correct": False}, {"text": "遅れるわりに", "correct": False}]},
            {"q": "'Es domingo, así que el banco DEBERÍA estar cerrado' (Yasumi):", "options": [{"text": "休みのはずだ", "correct": True}, {"text": "休みのわけがない", "correct": False}, {"text": "休みのくせに", "correct": False}]},
            {"q": "'Para lo mucho que comió, no ha engordado' (Desproporción):", "options": [{"text": "食べたわりに", "correct": True}, {"text": "食べたくせに", "correct": False}, {"text": "食べたはずだ", "correct": False}]},
            {"q": "Ojo: ～くせに NO se puede usar para hablar de uno mismo. ¿Cuál sería correcta para decir 'A pesar de que YO estudié, reprobé'?", "options": [{"text": "勉強したのに、落ちた", "correct": True}, {"text": "勉強したくせに、落ちた", "correct": False}, {"text": "勉強したわりに、落ちた", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-KeitaNeural", "ねえ、山田君、今日のテスト難しかったね。", "Oye, Yamada, el examen de hoy fue difícil, ¿no?"),
            ("ja-JP-NanamiNeural", "そう？私は毎日３時間も勉強したから、簡単だったよ。１００点のはずだわ。", "¿Tú crees? Como estudié 3 horas diarias, fue fácil. Es lógico que saque 100 puntos."),
            ("ja-JP-KeitaNeural", "えーっ、毎日３時間？それだけ勉強したわりに、昨日は「全然わからない」って言ってたじゃないか。", "¿Eh? ¿3 horas diarias? Para haber estudiado tanto, ayer estabas diciendo 'no entiendo nada'."),
            ("ja-JP-NanamiNeural", "あれは冗談よ。私がそんな簡単な問題を間違えるわけがないでしょ？", "Eso era una broma. Es imposible que me equivoque en problemas tan fáciles, ¿verdad?"),
            ("ja-JP-KeitaNeural", "なんだよ、知っていたくせに僕に教えてくれなかったのか！ひどいなあ。", "¡Pero qué dices! ¡A pesar de que lo sabías (crítica) no me lo enseñaste! Qué cruel."),
            ("ja-JP-NanamiNeural", "ごめんごめん。でも、普段全然勉強しないくせに、テストの時だけ頼るのは良くないと思うよ。", "Perdón, perdón. Pero, aunque no estudias nada normalmente (crítica), depender de otros solo en los exámenes creo que no es bueno.")
        ]
    },
    15: {
        "title": "Tendencia y Similitud (~がち / ~気味 / ~っぽい / ~みたい)",
        "grammar": [
            "<strong>N/V(masu base) + がち (Gachi):</strong> Tendencia a hacer algo a menudo (generalmente negativo). Ej. 彼は遅れがちだ (Él tiende a llegar tarde / Es propenso a retrasarse).",
            "<strong>N/V(masu base) + 気味 (Gimi):</strong> Sentir un poco de... / Tener el ligero síntoma de... Ej. 風邪気味だ (Tengo un ligero resfriado / Me siento un poco resfriado).",
            "<strong>N/Adj/V + っぽい (Ppoi):</strong> Parece... / Tiene la apariencia o característica de... (Fuerte similitud visual o rasgo de personalidad). Ej. 子供っぽい (Infantil / Parece un niño), 忘れっぽい (Olvidadizo / Tiende a olvidar).",
            "<strong>N + みたい (Mitai):</strong> Al igual que... / Parece... (Metáfora o deducción). Ej. 氷みたいに冷たい (Frío como el hielo)."
        ],
        "examples": [
            ("最近、曇りがちの天気が続いている。", "1. Últimamente, continúan los días con tendencia a estar nublados.", "さいきん、くもりがちのてんきがつづいている"),
            ("彼はストレスのせいで、最近休みがちだ。", "2. Por culpa del estrés, él tiende a ausentarse (descansar) últimamente.", "かれはストレスのせいで、さいきんやすみがちだ"),
            ("今日は少し風邪気味なので、早く帰ります。", "3. Como hoy me siento con un ligero resfriado, me iré a casa temprano.", "きょうはすこしかぜぎみなので、はやくかえります"),
            ("最近、少し太り気味で、服がきつくなった。", "4. Últimamente siento que he engordado un poco, y la ropa me aprieta.", "さいきん、すこしふとりぎみで、ふくがきつくなった"),
            ("彼はもう大人なのに、言うことが子供っぽい。", "5. A pesar de que ya es un adulto, las cosas que dice son infantiles.", "かれはもうおとななのに、いうことがこどもっぽい"),
            ("この牛乳、水っぽくて美味しくない。", "6. Esta leche parece agua (aguada) y no está sabrosa.", "このぎゅうにゅう、みずっぽくておいしくない"),
            ("私の祖父は、年をとって忘れっぽくなった。", "7. Mi abuelo ha envejecido y se ha vuelto olvidadizo.", "わたしのそふは、としをとってわすれっぽくなった"),
            ("彼女のドレスは、まるで星空みたいに美しい。", "8. Su vestido es hermoso, como si fuera un cielo estrellado.", "かのじょのドレスは、まるでほしぞらみたいにうつくしい"),
            ("誰もいないね。みんな帰ったみたいだ。", "9. No hay nadie, eh. Parece que todos se han ido a casa.", "だれもいないね。みんなかえったみたいだ"),
            ("あの雲、猫みたいな形をしているね。", "10. Esa nube tiene una forma que se parece a un gato, ¿verdad?", "あのくも、ねこみたいなかたちをしているね")
        ],
        "exercises": [
            {"q": "¿Qué sufijo se añade a la raíz de un verbo para indicar una TENDENCIA a hacer algo malo repetidamente? (Ej. Tiende a faltar)", "options": [{"text": "～がち (Gachi)", "correct": True}, {"text": "～っぽい (Ppoi)", "correct": False}, {"text": "～気味 (Gimi)", "correct": False}]},
            {"q": "¿Qué sufijo se usa para un LIGERO SÍNTOMA físico o mental? (Ej. Un poco de resfriado)", "options": [{"text": "～気味 (Gimi)", "correct": True}, {"text": "～がち (Gachi)", "correct": False}, {"text": "～みたい (Mitai)", "correct": False}]},
            {"q": "¿Qué sufijo convierte un sustantivo en un adjetivo-i para decir que 'tiene fuertemente ese rasgo'? (Ej. Infantil)", "options": [{"text": "～っぽい (Ppoi)", "correct": True}, {"text": "～みたい (Mitai)", "correct": False}, {"text": "～がち (Gachi)", "correct": False}]},
            {"q": "'Me siento un poco cansado hoy' (Tsukareru):", "options": [{"text": "疲れ気味だ", "correct": True}, {"text": "疲れがちだ", "correct": False}, {"text": "疲れっぽい", "correct": False}]},
            {"q": "'Ese chico es muy olvidadizo' (Wasureru):", "options": [{"text": "忘れっぽい", "correct": True}, {"text": "忘れがちだ", "correct": False}, {"text": "忘れ気味だ", "correct": False}]},
            {"q": "'En esta época, él tiende a enfermarse' (Byouki):", "options": [{"text": "病気がちだ", "correct": True}, {"text": "病気気味だ", "correct": False}, {"text": "病気っぽい", "correct": False}]},
            {"q": "Metáfora: 'Las manos de la abuela están frías como el hielo' (Koori):", "options": [{"text": "氷みたいに冷たい", "correct": True}, {"text": "氷っぽい冷たい", "correct": False}, {"text": "氷がちに冷たい", "correct": False}]},
            {"q": "'Esta sopa parece agua (está aguada)' (Mizu):", "options": [{"text": "水っぽい", "correct": True}, {"text": "水みたいだ", "correct": False}, {"text": "水気味だ", "correct": False}]},
            {"q": "'Tiende a dejar su cuarto sucio' (Yogoreru -> Yogore):", "options": [{"text": "汚れがちだ", "correct": True}, {"text": "汚れっぽい", "correct": False}, {"text": "汚れ気味だ", "correct": False}]},
            {"q": "Deducción visual: 'Parece que lloverá' (Ame):", "options": [{"text": "雨みたいだ", "correct": True}, {"text": "雨がちだ", "correct": False}, {"text": "雨っぽい", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "田中さん、顔色が悪いですね。大丈夫ですか。", "Tanaka, te ves pálido. ¿Estás bien?"),
            ("ja-JP-KeitaNeural", "ええ、実は昨日から少し風邪気味なんです。熱はないんですが。", "Sí, la verdad es que desde ayer me siento con un poco de resfriado. Aunque no tengo fiebre."),
            ("ja-JP-NanamiNeural", "最近急に寒くなりましたからね。この季節は、みんな体調を崩しがちですよ。", "Últimamente ha hecho frío de repente, eh. En esta época, todos tienden a enfermarse."),
            ("ja-JP-KeitaNeural", "そうですね。それに、少し疲れ気味でもあって...。", "Tienes razón. Además, me siento un poco cansado también..."),
            ("ja-JP-NanamiNeural", "無理しないでください。今日の会議が終わったら、早く帰ったほうがいいですよ。", "No te sobreesfuerces. Cuando termine la reunión de hoy, es mejor que te vayas a casa temprano."),
            ("ja-JP-KeitaNeural", "はい。あ、私の声、少しおじいさんっぽくないですか？咳のせいで。", "Sí. Ah, mi voz, ¿no parece un poco de anciano? Por culpa de la tos."),
            ("ja-JP-NanamiNeural", "ふふ、少しね。じゃあ、おじいさんみたいにゆっくり休んでください！", "Jeje, un poco. ¡Entonces descansa tranquilamente como un anciano!")
        ]
    }
}

base_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\lessons"
audio_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\audio"
os.makedirs(audio_dir, exist_ok=True)

for i in range(11, 16):
    d = data[i]
    print(f"--- Generating Lesson N3-{i} ---")
    
    # Audio Gen
    final_mp3 = os.path.join(audio_dir, f"dialogue-n3-{i}.mp3")
    if not os.path.exists(final_mp3):
        files = []
        for j, (voice, text_jp, _) in enumerate(d["dialogue"]):
            filename = f"line_n3_{i}_{j}.mp3"
            safe_text = text_jp.replace('"', '\\"')
            cmd = f'python -m edge_tts --voice {voice} --text "{safe_text}" --rate=-5% --write-media {filename}'
            subprocess.run(cmd, shell=True)
            files.append(filename)

        with open(f"files_n3_{i}.txt", "w", encoding="utf-8") as f:
            for filename in files:
                f.write(f"file '{filename}'\n")

        subprocess.run(f"ffmpeg -f concat -safe 0 -i files_n3_{i}.txt -c copy \"{final_mp3}\" -y", shell=True)

        for filename in files:
            if os.path.exists(filename):
                os.remove(filename)
        if os.path.exists(f"files_n3_{i}.txt"):
            os.remove(f"files_n3_{i}.txt")
            
    # HTML Gen
    grammar_html = "".join([f"                <li>{g}</li>\n" for g in d["grammar"]])
    examples_html = "".join([f'''        <div class="practice-item"><div class="practice-content"><div class="text-jp">{ex[0]}</div><div class="text-es">{ex[1]}</div></div><button class="audio-btn" onclick="playAudio('{ex[2]}')">🔊</button></div>\n''' for ex in d["examples"]])
    
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

    dialogue_html = f"""<h2 class="section-title">🎧 Práctica de Comprensión Auditiva (Diálogo N3)</h2>
<div class="grammar-note" style="background-color: #eff6ff; border-left-color: #3b82f6;">
    <p>Escucha este diálogo a velocidad casi natural. Presta atención a cómo los personajes utilizan <strong>{d['title'].split(' (')[0]}</strong>.</p>
    
    <div style="text-align: center; margin: 1.5rem 0; background: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border: 1px solid #e2e8f0;">
        <p style="margin-bottom: 15px; font-weight: 600; color: #475569; font-size: 1.1rem;">🎧 Escucha el diálogo (Voces IA):</p>
        <audio controls style="width: 100%; max-width: 450px; outline: none; border-radius: 50px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
            <source src="../audio/dialogue-n3-{i}.mp3" type="audio/mpeg">
            Tu navegador no soporta el elemento de audio.
        </audio>
    </div>

    <details style="background: white; padding: 1rem; border-radius: 8px; border: 1px solid #e2e8f0; margin-top: 1rem;">
        <summary style="font-weight: 600; cursor: pointer; color: var(--primary-color);">Ver Transcripción y Traducción</summary>
        <div style="margin-top: 1rem; display: grid; gap: 1rem; font-size: 0.95rem;">
"""
    for _, text_jp, text_es in d["dialogue"]:
        dialogue_html += f'            <div><div class="text-jp">{text_jp}</div><div class="text-es">{text_es}</div></div>\n'
    dialogue_html += """        </div>
    </details>
</div>
"""

    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Examen para el JLPT3 - Lección {i}</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=Noto+Sans+JP:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../css/style.css">
</head>
<body class="iframe-body">
    <div class="max-w-4xl">
        <div class="lesson-header-simple" style="background: linear-gradient(135deg, #e0f2fe 0%, #f0f9ff 100%); padding: 2rem; border-radius: 12px; margin-bottom: 2rem; border-left: 6px solid var(--primary-color); border-bottom: none;">
            <span>JLPT N3 - 中級</span>
            <h1>Examen para el JLPT3 - Lección {i}</h1>
            <p class="lesson-desc">Tema: {d["title"]}</p>
        </div>

        <div class="video-link-section" style="text-align: center; margin: 2rem 0; padding: 2.5rem; background: linear-gradient(135deg, var(--secondary-color) 0%, #2a2a4a 100%); border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
            <h3 style="color: white; margin-bottom: 0.5rem; font-size: 1.5rem;">🎬 Clase en Video</h3>
            <p style="color: #cbd5e0; margin-bottom: 1.5rem; font-size: 1.05rem;">Estudia este tema con Kira Sensei o Nihongo no Mori.</p>
            <a href="https://www.youtube.com/results?search_query=JLPT+N3+grammar+{d["title"].split(' ')[0]}" target="_blank" style="display: inline-block; background: var(--primary-color); color: white; padding: 1rem 2.5rem; border-radius: 50px; text-decoration: none; font-weight: 700; font-size: 1.15rem; transition: transform 0.2s, box-shadow 0.2s; box-shadow: 0 4px 15px rgba(224, 42, 77, 0.4);" onmouseover="this.style.transform='translateY(-3px)'; this.style.boxShadow='0 6px 20px rgba(224, 42, 77, 0.6)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 15px rgba(224, 42, 77, 0.4)'">Buscar Videos N3 en YouTube</a>
        </div>

        <h2 class="section-title">📚 Gramática Principal</h2>
        <div class="grammar-note">
            <ul>
{grammar_html}            </ul>
        </div>
        
        <h2 class="section-title">🌟 10 Ejemplos de Uso</h2>
        <div class="grammar-note"><p>A continuación, 10 ejemplos clave para dominar este tema en el examen N3.</p></div>
{examples_html}

{dialogue_html}

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

    with open(os.path.join(base_dir, f"jlpt-n3-{i}.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated jlpt-n3-{i}.html")

filepath = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

links_html = ""
for i in range(11, 16):
    title = data[i]["title"]
    links_html += f'''                        <a href="lessons/jlpt-n3-{i}.html" target="main_frame" class="nav-link">
                            <span class="nav-num">{i}</span> {title}
                        </a>\n'''

target_old = '</div>\n                </details>\n            </nav>'
if target_old in content:
    new_content = content.replace(target_old, f"{links_html}                    </div>\n                </details>\n            </nav>")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Updated index.html")
else:
    print("WARNING: Could not find target in index.html to insert links")

print("Running add_furigana.py...")
subprocess.run("python add_furigana.py", shell=True)
print("ALL TASKS COMPLETED!")
