import os
import subprocess

data = {
    21: {
        "title": "Lenguaje Honorífico (Sonkeigo - 尊敬語)",
        "grammar": [
            "El <strong>Sonkeigo</strong> se usa para mostrar respeto a las acciones del superior (Jefe, Cliente, Profesor). ¡Nunca lo uses para tus propias acciones!",
            "<strong>Verbos especiales:</strong> 行く/来る/いる -> いらっしゃる. 食べる/飲む -> 召し上がる. 言う -> おっしゃる. する -> なさる. 見る -> ご覧になる. 知っている -> ご存じです.",
            "<strong>Regla general:</strong> お + V(masu sin masu) + になります. Ej. お帰りになります (Se va a casa)."
        ],
        "examples": [
            ("社長はもうお帰りになりました。", "1. El presidente de la empresa ya se fue a casa.", "しゃちょうはもうおかえりになりました"),
            ("先生は新聞をお読みになります。", "2. El profesor lee el periódico.", "せんせいはしんぶんをおよみになります"),
            ("部長は何を召し上がりますか。", "3. ¿Qué va a comer/beber el jefe?", "ぶちょうはなにをめしあがりますか"),
            ("お客様がいらっしゃいました。", "4. Ha llegado (venido) un cliente.", "おきゃくさまがいらっしゃいました"),
            ("先生は私の名前をご存じですか。", "5. Profesor, ¿sabe usted mi nombre?", "せんせいはわたしのなまえをごぞんじですか"),
            ("会議の予定をおっしゃってください。", "6. Por favor, diga el horario de la reunión.", "かいぎのよていをおっしゃってください"),
            ("社長はゴルフをなさいます。", "7. El presidente juega (hace) golf.", "しゃちょうはゴルフをなさいます"),
            ("この映画をご覧になりましたか。", "8. ¿Usted vio esta película?", "このえいがをごらんになりましたか"),
            ("どうぞ、お座りください。", "9. Por favor, tome asiento.", "どうぞ、おすわりください"),
            ("先生は明日、学校にいらっしゃいません。", "10. El profesor no vendrá (no estará) en la escuela mañana.", "せんせいはあした、がっこうにいらっしゃいません")
        ],
        "exercises": [
            {"q": "¿Cuál es la forma honorífica (Sonkeigo) de 食べる (Comer)?", "options": [{"text": "召し上がる (Meshiagaru)", "correct": True}, {"text": "いただく (Itadaku)", "correct": False}, {"text": "なさる (Nasaru)", "correct": False}]},
            {"q": "¿Cuál es la forma honorífica de 行く / 来る / いる?", "options": [{"text": "参る (Mairu)", "correct": False}, {"text": "いらっしゃる (Irassharu)", "correct": True}, {"text": "おっしゃる (Ossharu)", "correct": False}]},
            {"q": "Si un empleado de tienda te pregunta qué vas a hacer/comprar (Suru):", "options": [{"text": "何をいたしますか。", "correct": False}, {"text": "何をなさいますか。", "correct": True}, {"text": "何をしますか。", "correct": False}]},
            {"q": "Si le hablas a tu jefe: '¿Dijo usted algo?' (Iu):", "options": [{"text": "何か言われましたか。", "correct": False}, {"text": "何か申しましたか。", "correct": False}, {"text": "何かおっしゃいましたか。", "correct": True}]},
            {"q": "Regla general: お + Raíz MASU + になります. ¿Cómo es 'Leer' (Yomu)?", "options": [{"text": "お読みにします", "correct": False}, {"text": "お読みになります", "correct": True}, {"text": "お読まれます", "correct": False}]},
            {"q": "'¿Ha visto usted este documento?' (Miru -> Goran ni naru):", "options": [{"text": "この資料をご覧になりましたか。", "correct": True}, {"text": "この資料を拝見しましたか。", "correct": False}, {"text": "この資料をお見になりましたか。", "correct": False}]},
            {"q": "Si le preguntas al cliente si 'SABE' algo (Shitte iru):", "options": [{"text": "ご存じですか。(Gozonji desu ka)", "correct": True}, {"text": "お知りになりますか。", "correct": False}, {"text": "存じておりますか。", "correct": False}]},
            {"q": "Si le ofreces un asiento a un invitado: 'Por favor, siéntese' (Suwaru):", "options": [{"text": "どうぞ、座ってください。", "correct": False}, {"text": "どうぞ、お座りください。", "correct": True}, {"text": "どうぞ、お座りになります。", "correct": False}]},
            {"q": "'El director del hospital ya se fue a casa' (Kaeru):", "options": [{"text": "院長はもうお帰りしました。", "correct": False}, {"text": "院長はもうお帰りになりました。", "correct": True}, {"text": "院長はもう帰りなさいました。", "correct": False}]},
            {"q": "El Sonkeigo se usa para elevar las acciones de...", "options": [{"text": "Uno mismo", "correct": False}, {"text": "La persona con la que hablo o de quien hablo (superior)", "correct": True}, {"text": "La familia del hablante", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "課長、明日の出張は何時にいらっしゃいますか。", "Jefe de sección, ¿a qué hora irá mañana a su viaje de negocios? (Sonkeigo)"),
            ("ja-JP-KeitaNeural", "明日は朝７時の新幹線で行くよ。", "Mañana iré en el tren bala de las 7 de la mañana. (Estilo normal)"),
            ("ja-JP-NanamiNeural", "そうですか。切符はもうお買いになりましたか。", "Ya veo. ¿Ya ha comprado (Sonkeigo) el billete?"),
            ("ja-JP-KeitaNeural", "いや、まだ買っていないんだ。", "No, aún no lo he comprado."),
            ("ja-JP-NanamiNeural", "では、私が後でお買いしておきます。昼食はどうなさいますか。", "Entonces, yo se lo compraré más tarde. ¿Qué hará (Sonkeigo) con el almuerzo?"),
            ("ja-JP-KeitaNeural", "新幹線の中で弁当を食べるつもりだ。", "Tengo intención de comer un bento dentro del tren bala."),
            ("ja-JP-NanamiNeural", "わかりました。美味しいお弁当をご用意しておきます。社長もご存じですか。", "Entendido. Prepararé un bento delicioso. ¿El presidente de la empresa también lo sabe (Sonkeigo)?"),
            ("ja-JP-KeitaNeural", "ああ、さっきおっしゃっていたよ。", "Sí, él lo estaba diciendo (Sonkeigo) hace un momento.")
        ]
    },
    22: {
        "title": "Lenguaje Humilde (Kenjougo - 謙譲語)",
        "grammar": [
            "El <strong>Kenjougo</strong> rebaja las propias acciones del hablante (o de su grupo) para mostrar respeto al oyente.",
            "<strong>Verbos especiales:</strong> 行く/来る -> 参る(まいる). いる -> おる. 食べる/飲む/もらう -> いただく. 言う -> 申す(もうす). する -> いたす. 見る -> 拝見する(はいけんする). 知っている -> 存じている.",
            "<strong>Regla general:</strong> お + V(masu sin masu) + します/いたします. Ej. お持ちします (Se lo llevo)."
        ],
        "examples": [
            ("私が荷物をお持ちします。", "1. Yo le llevaré el equipaje (Acción humilde).", "わたしがにもつをおもちします"),
            ("私から社長にご連絡いたします。", "2. Yo me comunicaré con el presidente.", "わたしからしゃちょうにごれんらくいたします"),
            ("はじめまして。私は田中と申します。", "3. Mucho gusto. Me llamo (humildemente) Tanaka.", "はじめまして。わたしはたなかともうします"),
            ("明日、午後３時に参ります。", "4. Mañana iré (humildemente) a las 3 PM.", "あした、ごごさんじにまいるます"),
            ("先生のご本を拝見しました。", "5. He visto (humildemente) el libro del profesor.", "せんせいのごほんをはいけんしました"),
            ("お茶をいただきます。", "6. Recibiré / Beberé el té (humildemente).", "おちゃをいただきます"),
            ("詳しいことは、私がご説明いたします。", "7. Los detalles, yo se los explicaré.", "くわしいことは、わたしがごせつめいいたします"),
            ("社長の奥様にお目にかかりました。", "8. Me encontré con la esposa del presidente (Ome ni kakaru = encontrarse).", "しゃちょうのおくさまにおめにかかりました"),
            ("その件は存じております。", "9. Ese asunto, lo sé (humildemente).", "そのけんはぞんじております"),
            ("アメリカから参りました。", "10. He venido de Estados Unidos (Humilde).", "アメリカからまいりました")
        ],
        "exercises": [
            {"q": "¿Cuál es la forma humilde de 言う (Decir)?", "options": [{"text": "申す (Mousu)", "correct": True}, {"text": "おっしゃる (Ossharu)", "correct": False}, {"text": "いたす (Itasu)", "correct": False}]},
            {"q": "¿Cuál es la forma humilde de 行く / 来る?", "options": [{"text": "いらっしゃる (Irassharu)", "correct": False}, {"text": "参る (Mairu)", "correct": True}, {"text": "いただく (Itadaku)", "correct": False}]},
            {"q": "¿Cuál es la forma humilde de 食べる / 飲む / もらう?", "options": [{"text": "召し上がる", "correct": False}, {"text": "いただく (Itadaku)", "correct": True}, {"text": "おる", "correct": False}]},
            {"q": "Si te presentas: 'Soy Juan' (Hacer humildemente):", "options": [{"text": "私はフアンとおっしゃいます。", "correct": False}, {"text": "私はフアンと申します。", "correct": True}, {"text": "私はフアンと存じます。", "correct": False}]},
            {"q": "Si ves los documentos del cliente (Ver -> Haiken suru):", "options": [{"text": "資料を拝見しました。", "correct": True}, {"text": "資料をご覧になりました。", "correct": False}, {"text": "資料をお見しました。", "correct": False}]},
            {"q": "Regla general humilde: お + Raíz MASU + します. 'Yo le ayudaré' (Tetsudau):", "options": [{"text": "お手伝いになります", "correct": False}, {"text": "お手伝いします", "correct": True}, {"text": "お手伝いされます", "correct": False}]},
            {"q": "'Yo le llamaré por teléfono' (Denwa suru es palabra china, se usa Go):", "options": [{"text": "お電話いたします", "correct": True}, {"text": "ご電話いたします", "correct": False}, {"text": "電話になります", "correct": False}]},
            {"q": "La expresión 'Ome ni kakaru' significa...", "options": [{"text": "Mirar (Humilde)", "correct": False}, {"text": "Encontrarse / Ver a alguien (Humilde de Au)", "correct": True}, {"text": "Hablar (Humilde)", "correct": False}]},
            {"q": "¿Quién debe ser el sujeto cuando usamos Kenjougo (Humilde)?", "options": [{"text": "El jefe o profesor", "correct": False}, {"text": "Yo mismo, o alguien de mi propio círculo/empresa", "correct": True}, {"text": "Cualquier persona", "correct": False}]},
            {"q": "'El profesor está en la sala'. Si quiero hablar con humildad SOBRE MÍ, y digo 'Yo estoy en la sala':", "options": [{"text": "私は部屋におります。", "correct": True}, {"text": "私は部屋にいらっしゃいます。", "correct": False}, {"text": "私は部屋にまいります。", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-KeitaNeural", "失礼いたします。佐藤先生でいらっしゃいますか。", "Con permiso. ¿Es usted el profesor Sato? (Honorífico)"),
            ("ja-JP-NanamiNeural", "はい、佐藤ですが。", "Sí, soy Sato."),
            ("ja-JP-KeitaNeural", "はじめまして。私は山田と申します。本日は、先生のご本を拝見して、お話を伺いに参りました。", "Mucho gusto. Me llamo Yamada (Humilde). Hoy he visto su libro (Humilde) y he venido a escuchar lo que tiene que decir (Humilde)."),
            ("ja-JP-NanamiNeural", "わざわざありがとうございます。どうぞ、お掛けください。", "Muchas gracias por venir expresamente. Por favor, tome asiento."),
            ("ja-JP-KeitaNeural", "ありがとうございます。先生の新しい研究について、少し教えていただけませんか。", "Gracias. ¿Podría hacerme el favor de enseñarme un poco sobre su nueva investigación?"),
            ("ja-JP-NanamiNeural", "ええ、いいですよ。お茶を淹れますね。", "Sí, claro. Voy a preparar té."),
            ("ja-JP-KeitaNeural", "あ、どうぞおかまいなく。私が後でお淹れいたします。", "Ah, por favor no se moleste. Yo lo prepararé (Humilde) más tarde.")
        ]
    },
    23: {
        "title": "Conjeturas (~らしい / ~みたいです / ~はずです)",
        "grammar": [
            "<strong>N / Forma Plana + らしいです:</strong> Parece que... (Basado en información objetiva, rumores o lectura). Ej. 彼は病気らしいです (Parece que él está enfermo).",
            "<strong>N / Forma Plana + みたいです:</strong> Parece... (Similar a 'you desu', muy usado coloquialmente para apariencia). Ej. 夢みたいです (Parece un sueño).",
            "<strong>Forma Plana + はずです:</strong> Debería ser... / Es seguro que... (Expresa una fuerte convicción del hablante basada en la lógica). Ej. 彼は来るはずです (Él debería venir)."
        ],
        "examples": [
            ("山田さんは明日、来ないらしいです。", "1. Parece ser que Yamada no vendrá mañana.", "やまださんはあした、こないらしいです"),
            ("先生は昨日、とても忙しかったみたいです。", "2. El profesor parece que estuvo muy ocupado ayer.", "せんせいはきのう、とてもいそがしかったみたいです"),
            ("彼は日本に１０年住んでいたから、日本語が上手なはずです。", "3. Él vivió 10 años en Japón, así que debería ser bueno en japonés.", "かれはにほんにじゅうねんすんでいたから、にほんごがじょうずなはずです"),
            ("明日は晴れるらしいです。", "4. Parece que mañana estará soleado.", "あしたははれるらしいです"),
            ("このケーキ、プラスチックみたいで硬いです。", "5. Este pastel parece plástico, está duro.", "このケーキ、プラスチックみたいでかたいです"),
            ("会議は午後２時に始まるはずです。", "6. La reunión debería empezar a las 2 de la tarde.", "かいぎはごごにじにはじまるはずです"),
            ("彼はまだ子供みたいです。", "7. Él todavía parece un niño.", "かれはまだこどもみたいです"),
            ("そのニュースは本当らしいです。", "8. Esa noticia parece ser verdad.", "そのニュースはほんとうらしいです"),
            ("鈴木さんは英語が話せないはずです。", "9. Es seguro que Suzuki no sabe hablar inglés (No debería saber).", "すずきさんはえいごがはなせないはずです"),
            ("風邪をひいたみたいです。", "10. Parece que he pillado un resfriado.", "かぜをひいたみたいです")
        ],
        "exercises": [
            {"q": "¿Qué expresión se usa para decir 'Parece que...' basándose en lo que leíste en una revista o escuchaste?", "options": [{"text": "～らしいです", "correct": True}, {"text": "～みたいです", "correct": False}, {"text": "～はずです", "correct": False}]},
            {"q": "¿Qué expresión indica una FUERTE CONVICCIÓN o certeza ('debería ser así') basada en la lógica?", "options": [{"text": "～はずです", "correct": True}, {"text": "～らしいです", "correct": False}, {"text": "～みたいです", "correct": False}]},
            {"q": "'Como hoy es domingo, el banco DEBERÍA estar cerrado' (Yasumi):", "options": [{"text": "銀行は休みらしいです", "correct": False}, {"text": "銀行は休みみたいです", "correct": False}, {"text": "銀行は休みのはずです", "correct": True}]},
            {"q": "'Esa persona parece una mujer, pero es un hombre' (Onna no hito + mitai):", "options": [{"text": "女の人のみたいです", "correct": False}, {"text": "女の人みたいです", "correct": True}, {"text": "女の人なみたいです", "correct": False}]},
            {"q": "¿Cómo se conecta 'Mitai desu' con Sustantivos?", "options": [{"text": "Directamente (Sustantivo + みたいです)", "correct": True}, {"text": "Con 'no' (Sustantivo + のみたいです)", "correct": False}, {"text": "Con 'na' (Sustantivo + なみたいです)", "correct": False}]},
            {"q": "'Escuché un rumor de que ellos se van a casar':", "options": [{"text": "結婚するらしいです。", "correct": True}, {"text": "結婚するはずです。", "correct": False}, {"text": "結婚しますみたいです。", "correct": False}]},
            {"q": "'Él es médico, así que es seguro que sabe mucho' (Kuwashii):", "options": [{"text": "詳しいはずです", "correct": True}, {"text": "詳しいらしいです", "correct": False}, {"text": "詳しいみたいです", "correct": False}]},
            {"q": "'Parece que llovió anoche' (Ame ga futta):", "options": [{"text": "雨が降ったみたいです", "correct": True}, {"text": "雨が降ったはずです", "correct": False}, {"text": "雨が降りみたいです", "correct": False}]},
            {"q": "Para conectar un Adjetivo Na con 'Hazu desu' (Ej. Genki):", "options": [{"text": "元気はずです", "correct": False}, {"text": "元気なはずです", "correct": True}, {"text": "元気のはずです", "correct": False}]},
            {"q": "Diferencia: 'Sou desu' (Apariencia visual inmediata) vs 'Mitai desu' (Parecido / Metáfora). 'Esta piedra parece un pan' (No es pan, pero se parece):", "options": [{"text": "パンそうです", "correct": False}, {"text": "パンみたいです", "correct": True}, {"text": "パンらしいです", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "ねえ、外でパトカーの音が聞こえるけど、何かあったみたいですね。", "Oye, se oyen sirenas de policía afuera, parece que ha pasado algo."),
            ("ja-JP-KeitaNeural", "ニュースによると、この近くで事故があったらしいですよ。", "Según las noticias, parece que (dicen que) ha habido un accidente por aquí cerca."),
            ("ja-JP-NanamiNeural", "本当ですか。どうりで道が混んでいるはずですね。", "¿De verdad? Con razón las calles deberían estar (seguramente están) atascadas."),
            ("ja-JP-KeitaNeural", "ええ。彼もその道を通って来るから、今日は遅れるかもしれません。", "Sí. Él también viene por ese camino, así que tal vez llegue tarde hoy."),
            ("ja-JP-NanamiNeural", "でも、彼はいつも遅れない人だから、もうすぐ着くはずですよ。", "Pero como él es una persona que nunca llega tarde, debería llegar pronto."),
            ("ja-JP-KeitaNeural", "あ、今メッセージが来ました。「道が混んでいて遅れる」らしいです。", "Ah, acaba de llegar un mensaje. Parece que 'las calles están atascadas y llegará tarde'."),
            ("ja-JP-NanamiNeural", "やっぱり。じゃあ、先にコーヒーでも飲んで待っていましょうか。", "Lo sabía. Entonces, ¿bebemos un café mientras esperamos?"),
            ("ja-JP-KeitaNeural", "そうしましょう。", "Hagamos eso.")
        ]
    },
    24: {
        "title": "Hipotéticas y Contrariedad (～場合は / ～のに)",
        "grammar": [
            "<strong>Forma Plana + 場合は:</strong> En caso de que... (Para situaciones hipotéticas indeseables o instrucciones manuales). Ej. 遅れる場合は、連絡してください (En caso de retrasarse, comuníquese).",
            "<strong>Forma Plana + のに:</strong> A pesar de que... / Aunque... (Expresa sorpresa, queja o insatisfacción profunda). Ej. 勉強したのに、テストが悪かったです (A pesar de que estudié, me fue mal en el examen)."
        ],
        "examples": [
            ("パスワードを忘れた場合は、ここに電話してください。", "1. En caso de olvidar la contraseña, llame aquí.", "パスワードをわすれたばあいは、ここでんわしてください"),
            ("雨が降っている場合は、試合は中止になります。", "2. En caso de que esté lloviendo, el partido se cancelará.", "あめがふっているばあいは、しあいはちゅうしになります"),
            ("毎日練習しているのに、上手になりません。", "3. A pesar de que practico todos los días, no mejoro.", "まいにちれんしゅうしているのに、じょうずになりません"),
            ("薬を飲んだのに、熱が下がりません。", "4. A pesar de haber tomado la medicina, no me baja la fiebre.", "くすりをのんだのに、ねつがさがりません"),
            ("地震が起きた場合は、机の下に入ってください。", "5. En caso de que ocurra un terremoto, métase debajo de la mesa.", "じしんがおきたばあいは、つくえのしたにはいってください"),
            ("今日は日曜日なのに、仕事をしなければなりません。", "6. A pesar de que hoy es domingo, tengo que trabajar.", "きょうはにちようびなのに、しごとをしなければなりません"),
            ("お金を払ったのに、商品が届きません。", "7. A pesar de haber pagado, no llega el producto.", "おかねをはらったのに、しょうひんがとどきません"),
            ("火事の場合は、エレベーターを使わないでください。", "8. En caso de incendio, no use el ascensor.", "かじのばあいは、エレベーターをつかわないでください"),
            ("彼はたくさん食べるのに、太りません。", "9. A pesar de que él come mucho, no engorda.", "かれはたくさんたべるのに、ふとりません"),
            ("約束をしたのに、彼は来ませんでした。", "10. A pesar de haber hecho una promesa, él no vino.", "やくそくをしたのに、かれはきませんでした")
        ],
        "exercises": [
            {"q": "¿Qué conjunción se usa para expresar una queja, cuando las cosas no salieron como esperabas? 'A pesar de que...'", "options": [{"text": "～けれども / が", "correct": False}, {"text": "～のに", "correct": True}, {"text": "～から", "correct": False}]},
            {"q": "'A pesar de que es BARATO (Yasui), está delicioso':", "options": [{"text": "安いのに、美味しいです。", "correct": True}, {"text": "安くのに、美味しいです。", "correct": False}, {"text": "安いなので、美味しいです。", "correct": False}]},
            {"q": "Para conectar Sustantivos o Adjetivos-Na con 'Noni', ¿qué se debe añadir?", "options": [{"text": "な (Na)", "correct": True}, {"text": "だ (Da)", "correct": False}, {"text": "の (No)", "correct": False}]},
            {"q": "'A pesar de que es mi DÍA LIBRE (Yasumi - Sustantivo), tengo que trabajar':", "options": [{"text": "休みのに、働かなければなりません。", "correct": False}, {"text": "休みなのに、働かなければなりません。", "correct": True}, {"text": "休みだのに、働かなければなりません。", "correct": False}]},
            {"q": "Para expresar 'En caso de que...', se usa:", "options": [{"text": "～場合は (Baai wa)", "correct": True}, {"text": "～時は (Toki wa)", "correct": False}, {"text": "～なら (Nara)", "correct": False}]},
            {"q": "¿Cómo se conecta un SUSTANTIVO a 'Baai wa'? Ej. En caso de terremoto (Jishin):", "options": [{"text": "地震な場合は", "correct": False}, {"text": "地震の場合は", "correct": True}, {"text": "地震場合は", "correct": False}]},
            {"q": "'A pesar de que le enseñé (Oshieta), lo olvidó':", "options": [{"text": "教えたのに、忘れました。", "correct": True}, {"text": "教えるのに、忘れました。", "correct": False}, {"text": "教えてのに、忘れました。", "correct": False}]},
            {"q": "'En caso de llegar tarde (Okureru), llama':", "options": [{"text": "遅れる場合は、電話してください。", "correct": True}, {"text": "遅れた場合は、電話してください。", "correct": False}, {"text": "遅れて場合は、電話してください。", "correct": False}]},
            {"q": "¿Se puede usar 'Noni' para peticiones u órdenes? Ej. 'A pesar de que llueve, ¡ve a comprar!'", "options": [{"text": "Sí.", "correct": False}, {"text": "No. 'Noni' es para hechos o emociones de queja/sorpresa.", "correct": True}, {"text": "Solo si es imperativo negativo.", "correct": False}]},
            {"q": "'A pesar de que la habitación estaba limpia (Kirei - Adj-Na), había bichos':", "options": [{"text": "綺麗なだったのに、虫がいました", "correct": False}, {"text": "綺麗だったのに、虫がいました", "correct": True}, {"text": "綺麗のに、虫がいました", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-KeitaNeural", "鈴木さん、このパソコン、新しいのに、もう壊れてしまったみたいです。", "Suzuki, esta computadora, a pesar de ser nueva, parece que ya se ha roto."),
            ("ja-JP-NanamiNeural", "ええっ、先週買ったばかりなのに？どうしたんですか。", "¿Eh? ¿A pesar de que la acabas de comprar la semana pasada? ¿Qué pasa?"),
            ("ja-JP-KeitaNeural", "電源ボタンを押しても、画面が暗いままなんです。", "Aunque pulso el botón de encendido, la pantalla se queda oscura."),
            ("ja-JP-NanamiNeural", "説明書に、故障の場合はどうするか書いてあるはずですよ。", "En el manual de instrucciones debería estar escrito qué hacer en caso de avería."),
            ("ja-JP-KeitaNeural", "あ、ありました。「動かない場合は、店に連絡してください」と書いてあります。", "Ah, aquí está. Dice: 'En caso de que no funcione, póngase en contacto con la tienda'."),
            ("ja-JP-NanamiNeural", "高かったのに、残念ですね。すぐにお店に電話したほうがいいですよ。", "A pesar de que era cara... qué lástima. Es mejor que llames a la tienda enseguida."),
            ("ja-JP-KeitaNeural", "そうですね。仕事で使うのに、使えなくて本当に困りました。", "Tienes razón. A pesar de que es para usar en el trabajo, no puedo usarla y estoy en problemas."),
            ("ja-JP-NanamiNeural", "私のパソコンを貸してあげましょうか。", "¿Quieres que te preste mi computadora?"),
            ("ja-JP-KeitaNeural", "助かります。ありがとうございます。", "Me salvas. Muchas gracias.")
        ]
    },
    25: {
        "title": "Causativa-Pasiva (~させられる)",
        "grammar": [
            "Esta forma expresa que <strong>fuiste obligado o forzado a hacer algo por otra persona, en contra de tu voluntad.</strong> Es una queja.",
            "<strong>G1:</strong> Cambia la 'U' final a 'A' y añade 'serareru'. (Se acorta a ~asareru en el lenguaje hablado). Ej: 書く -> 書かせられる (O Kakasareru). 飲む -> 飲ませられる (Nomasareru).",
            "<strong>G2:</strong> Raíz + 'saserareru'. Ej: 食べる -> 食べさせられる.",
            "<strong>G3:</strong> する -> させられる, 来る -> こさせられる.",
            "<strong>N1(víctima) は N2(autor) に V(caus-pas):</strong> Fui obligado por N2 a hacer X."
        ],
        "examples": [
            ("私は母に野菜を食べさせられました。", "1. Fui obligado por mi madre a comer verduras.", "わたしはははにやさいをたべさせられました"),
            ("子供の時、父に毎日ピアノを練習させられました。", "2. De niño, fui obligado por mi padre a practicar piano todos los días.", "こどものとき、ちちにまいにちピアノをれんしゅうさせられました"),
            ("昨日、部長にお酒をたくさん飲ませられました。", "3. Ayer, fui obligado por el jefe a beber mucho alcohol.", "きのう、ぶちょうにおさけをたくさんのませられました"),
            ("先生に漢字を１００回書かされました。", "4. Fui obligado por el profesor a escribir los kanjis 100 veces. (Forma corta Kakasareru)", "せんせいにかんじをひゃっかいかかされました"),
            ("日曜日なのに、学校へ来させられました。", "5. A pesar de ser domingo, me hicieron (fui obligado a) venir a la escuela.", "にちようびなのに、がっこうへこさせられました"),
            ("無理に謝らせられました。", "6. Fui forzado a pedir disculpas en contra de mi voluntad.", "むりにあやまらせられました"),
            ("友達に長い間待たされました。", "7. Fui obligado por mi amigo a esperar durante mucho tiempo.", "ともだちにながいあいだまたされました"),
            ("嫌な仕事をさせられました。", "8. Me hicieron hacer un trabajo desagradable.", "いやなしごとをさせられました"),
            ("私は走らされました。", "9. Fui obligado a correr.", "わたしははしらされました"),
            ("母に部屋の掃除をさせられました。", "10. Fui obligado por mi madre a limpiar la habitación.", "ははにへやのそうじをさせられました")
        ],
        "exercises": [
            {"q": "¿Qué significa la forma Causativa-Pasiva (~させられる)?", "options": [{"text": "Ser obligado o forzado a hacer algo", "correct": True}, {"text": "Poder hacer algo si te esfuerzas", "correct": False}, {"text": "Recibir permiso para hacer algo", "correct": False}]},
            {"q": "¿Cómo se conjuga el Grupo 2 (Ej. 食べる)?", "options": [{"text": "食べさせられる", "correct": True}, {"text": "食べさされる", "correct": False}, {"text": "食べられる", "correct": False}]},
            {"q": "¿Cómo se conjuga する (Grupo 3)?", "options": [{"text": "させられる", "correct": True}, {"text": "される", "correct": False}, {"text": "すられる", "correct": False}]},
            {"q": "Para el Grupo 1 como 飲む (Nomu), la forma larga es 飲ませられる. ¿Cuál es su forma CORTA (la más usada al hablar)?", "options": [{"text": "飲まされる (Nomasareru)", "correct": True}, {"text": "飲みされる (Nomisareru)", "correct": False}, {"text": "飲まれる (Nomareru - eso es pasiva normal)", "correct": False}]},
            {"q": "'Fui obligado a ESPERAR por mi amigo' (Matsu -> Matasareru):", "options": [{"text": "友達に待たされました。", "correct": True}, {"text": "友達を待たさせられました。", "correct": False}, {"text": "友達に待ちさせられました。", "correct": False}]},
            {"q": "¿Quién es el sujeto (marcado con は o が) en una oración causativa-pasiva?", "options": [{"text": "La 'víctima', la persona que fue obligada", "correct": True}, {"text": "La persona que dio la orden", "correct": False}, {"text": "El objeto directo", "correct": False}]},
            {"q": "'Fui forzado a ir' (Iku -> Ikasareru):", "options": [{"text": "行かされました", "correct": True}, {"text": "行かせられました", "correct": True}, {"text": "Ambas son correctas (Una corta, una larga)", "correct": True}]},
            {"q": "'Mi madre me obligó a estudiar' (Benkyou suru):", "options": [{"text": "母に勉強させられました。", "correct": True}, {"text": "母を勉強させられました。", "correct": False}, {"text": "母は勉強させられました。", "correct": False}]},
            {"q": "¿Cómo se conjuga 買う (Kau) en su forma corta? (Termina en U, así que U -> WA)", "options": [{"text": "買わされる (Kawasareru)", "correct": True}, {"text": "買あされる (Kaasareru)", "correct": False}, {"text": "買いされる (Kaisareru)", "correct": False}]},
            {"q": "Si fuiste OBLIGADO A HABLAR (Hanasu) en japonés:", "options": [{"text": "日本語で話させられました。", "correct": True}, {"text": "日本語で話さされました。", "correct": False}, {"text": "日本語で話しさせられました。", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "田中さん、今日は元気がないですね。どうしたんですか。", "Tanaka, hoy no te ves con energía. ¿Qué te pasó?"),
            ("ja-JP-KeitaNeural", "実は昨日、部長にカラオケに連れて行かれたんです。", "La verdad es que ayer, el jefe me llevó al karaoke (pasiva)."),
            ("ja-JP-NanamiNeural", "それは楽しそうじゃないですか。", "¿Y eso no suena divertido?"),
            ("ja-JP-KeitaNeural", "いや、歌いたくないのに、無理やり３回も歌わせられたんですよ。", "No, a pesar de que yo no quería cantar, fui obligado a cantar (causativa-pasiva) tres veces a la fuerza."),
            ("ja-JP-NanamiNeural", "ええっ、それは大変でしたね。", "¿Eh? Eso fue duro."),
            ("ja-JP-KeitaNeural", "それに、お酒もたくさん飲ませられて、今日は二日酔いなんです。", "Y además, fui obligado a beber (causativa-pasiva) mucho alcohol, y hoy tengo resaca."),
            ("ja-JP-NanamiNeural", "部長と一緒に行くと、いつもそうですね。私も前に、夜遅くまで付き合わされました。", "Cuando vas con el jefe siempre pasa eso. Yo también, hace un tiempo, fui obligada a acompañarlo (causativa-pasiva) hasta tarde."),
            ("ja-JP-KeitaNeural", "次からは、忙しいと言って断ろうと思います。", "A partir de la próxima vez, creo que diré que estoy ocupado y lo rechazaré.")
        ]
    }
}


base_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\lessons"
audio_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\audio"
os.makedirs(audio_dir, exist_ok=True)

# Generate HTML and Audio for 21-25
for i in range(21, 26):
    d = data[i]
    print(f"--- Generating Lesson {i} ---")
    
    # Audio Gen
    final_mp3 = os.path.join(audio_dir, f"dialogue-n4-{i}.mp3")
    if not os.path.exists(final_mp3):
        files = []
        for j, (voice, text_jp, _) in enumerate(d["dialogue"]):
            filename = f"line_{i}_{j}.mp3"
            safe_text = text_jp.replace('"', '\\"')
            cmd = f'python -m edge_tts --voice {voice} --text "{safe_text}" --rate=-10% --write-media {filename}'
            subprocess.run(cmd, shell=True)
            files.append(filename)

        with open(f"files_{i}.txt", "w", encoding="utf-8") as f:
            for filename in files:
                f.write(f"file '{filename}'\n")

        subprocess.run(f"ffmpeg -f concat -safe 0 -i files_{i}.txt -c copy \"{final_mp3}\" -y", shell=True)

        for filename in files:
            if os.path.exists(filename):
                os.remove(filename)
        if os.path.exists(f"files_{i}.txt"):
            os.remove(f"files_{i}.txt")
            
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

    dialogue_html = f"""<h2 class="section-title">🎧 Práctica de Comprensión Auditiva (Diálogo)</h2>
<div class="grammar-note" style="background-color: #fdf2f8; border-left-color: #ec4899;">
    <p>Escucha este diálogo extenso (aprox. 1 minuto). Presta atención a cómo los personajes utilizan <strong>{d['title'].split(' (')[0]}</strong>.</p>
    
    <div style="text-align: center; margin: 1.5rem 0; background: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border: 1px solid #e2e8f0;">
        <p style="margin-bottom: 15px; font-weight: 600; color: #475569; font-size: 1.1rem;">🎧 Escucha el diálogo (Voces IA):</p>
        <audio controls style="width: 100%; max-width: 450px; outline: none; border-radius: 50px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
            <source src="../audio/dialogue-n4-{i}.mp3" type="audio/mpeg">
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
    <title>Examen para el JLPT4 - Lección {i}</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=Noto+Sans+JP:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../css/style.css">
</head>
<body class="iframe-body">
    <div class="max-w-4xl">
        <div class="lesson-header-simple">
            <span>JLPT N4 - 準備</span>
            <h1>Examen para el JLPT4 - Lección {i}</h1>
            <p class="lesson-desc">Tema: {d["title"]}</p>
        </div>

        <div class="video-link-section" style="text-align: center; margin: 2rem 0; padding: 2.5rem; background: linear-gradient(135deg, var(--secondary-color) 0%, #2a2a4a 100%); border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
            <h3 style="color: white; margin-bottom: 0.5rem; font-size: 1.5rem;">🎬 Clase en Video</h3>
            <p style="color: #cbd5e0; margin-bottom: 1.5rem; font-size: 1.05rem;">Estudia este tema con Kira Sensei.</p>
            <a href="https://www.youtube.com/results?search_query=Kira+Sensei+JLPT+N4" target="_blank" style="display: inline-block; background: var(--primary-color); color: white; padding: 1rem 2.5rem; border-radius: 50px; text-decoration: none; font-weight: 700; font-size: 1.15rem; transition: transform 0.2s, box-shadow 0.2s; box-shadow: 0 4px 15px rgba(224, 42, 77, 0.4);" onmouseover="this.style.transform='translateY(-3px)'; this.style.boxShadow='0 6px 20px rgba(224, 42, 77, 0.6)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 15px rgba(224, 42, 77, 0.4)'">Buscar Videos N4 en YouTube</a>
        </div>

        <h2 class="section-title">📚 Gramática Principal</h2>
        <div class="grammar-note">
            <ul>
{grammar_html}            </ul>
        </div>
        
        <h2 class="section-title">🌟 10 Ejemplos de Uso</h2>
        <div class="grammar-note"><p>A continuación, 10 ejemplos clave para dominar este tema en el examen N4.</p></div>
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

    with open(os.path.join(base_dir, f"jlpt-n4-{i}.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated jlpt-n4-{i}.html")

# Update index.html
filepath = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

links_html = ""
for i in range(21, 26):
    title = data[i]["title"]
    links_html += f'''                        <a href="lessons/jlpt-n4-{i}.html" target="main_frame" class="nav-link">
                            <span class="nav-num">{i}</span> {title}
                        </a>\n'''

target = '                            <span class="nav-num">20</span> Forma Causativa (~せる / ~させる)\n                        </a>\n'
if target in content:
    new_content = content.replace(target, target + links_html)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Updated index.html")
else:
    print("WARNING: Could not find target in index.html")

print("Running add_furigana.py...")
subprocess.run("python add_furigana.py", shell=True)
print("ALL TASKS COMPLETED!")
