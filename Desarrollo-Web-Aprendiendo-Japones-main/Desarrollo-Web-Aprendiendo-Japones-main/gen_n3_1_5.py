import os
import subprocess

data = {
    1: {
        "title": "Intenciones y Determinación (~ようと思う / ~つもりだ)",
        "grammar": [
            "<strong>V(volitivo) + と思う:</strong> Expresa una intención o plan actual. Ej. 行こうと思う (Pienso ir). Si dices と思っている, significa que lo llevas pensando un tiempo.",
            "<strong>V(dic/nai) + つもりだ:</strong> Expresa una intención o determinación fuerte. Ej. 行くつもりだ (Tengo la firme intención de ir).",
            "<strong>V(dic/nai) + ことにしている:</strong> Expresa una rutina o regla personal que has decidido mantener. Ej. 毎日走ることにしている (Tengo la regla de correr todos los días).",
            "<strong>V(dic/nai) + ことになった:</strong> Se ha decidido que... (La decisión fue tomada por otros o por las circunstancias). Ej. 出張することになった (Se ha decidido que iré de viaje de negocios)."
        ],
        "examples": [
            ("来年、日本へ留学しようと思っています。", "1. Llevo un tiempo pensando en ir a estudiar a Japón el próximo año.", "らいねん、にほんへりゅうがくしようとおもっています"),
            ("今日は早く寝ようと思います。", "2. Pienso dormir temprano hoy (decisión del momento).", "きょうははやくねようとおもいます"),
            ("私はタバコを吸わないつもりです。", "3. Tengo la firme intención de no fumar.", "わたしはタバコをすわないつもりです"),
            ("来月、新しい車を買うつもりだ。", "4. Tengo la intención de comprar un coche nuevo el próximo mes.", "らいげつ、あたらしいくるまをかうつもりだ"),
            ("健康のために、毎日野菜を食べることにしています。", "5. Por mi salud, tengo la regla de comer verduras todos los días.", "けんこうのために、まいにちやさいをたべることにしています"),
            ("絶対に遅刻しないことにしている。", "6. Tengo la regla estricta de nunca llegar tarde.", "ぜったいにちこくしないことにしている"),
            ("来週から大阪の支社で働くことになりました。", "7. Se ha decidido que trabajaré en la sucursal de Osaka desde la próxima semana.", "らいしゅうからおおさかのししゃではたらくことになりました"),
            ("今年からボーナスが出ないことになったそうだ。", "8. Escuché que se ha decidido que desde este año no habrá bonos.", "ことしからボーナスがでないことになったそうだ"),
            ("週末は掃除をしようと思っている。", "9. Llevo pensando en limpiar el fin de semana.", "しゅうまつはそうじをしようとおもっている"),
            ("こんな高い物、買わないつもりだったのに。", "10. Y pensar que no tenía la intención de comprar algo tan caro...", "こんなたかいもの、かわないつもりだったのに")
        ],
        "exercises": [
            {"q": "¿Qué forma verbal se usa antes de と思う (to omou) para expresar intención?", "options": [{"text": "Forma Volitiva (Ej. 買おう - Kaou)", "correct": True}, {"text": "Forma Diccionario (Ej. 買う - Kau)", "correct": False}, {"text": "Forma TA (Ej. 買った - Katta)", "correct": False}]},
            {"q": "Diferencia de tiempo: ¿Qué implica '～と思っている' a diferencia de '～と思う'?", "options": [{"text": "Que lo acabas de decidir en este instante.", "correct": False}, {"text": "Que llevas pensando en esa idea/intención durante un tiempo.", "correct": True}, {"text": "Que estás dudando si hacerlo o no.", "correct": False}]},
            {"q": "Para expresar una regla personal o hábito ('He decidido... y lo mantengo'):", "options": [{"text": "～ことにしている", "correct": True}, {"text": "～ことになった", "correct": False}, {"text": "～つもりだ", "correct": False}]},
            {"q": "'Se ha decidido que (por decisión de la empresa) me transferirán a Tokio': 東京に転勤する___。", "options": [{"text": "ことにしました", "correct": False}, {"text": "ことになりました", "correct": True}, {"text": "ことにしています", "correct": False}]},
            {"q": "¿Cómo se conjuga 'Iku' antes de 'Tsumori da' (Intención fuerte)?", "options": [{"text": "行くつもりだ", "correct": True}, {"text": "行こうつもりだ", "correct": False}, {"text": "行ってつもりだ", "correct": False}]},
            {"q": "¿Cómo digo 'Tengo la intención de NO comer'?", "options": [{"text": "食べないつもりです", "correct": True}, {"text": "食べようつもりじゃないです", "correct": False}, {"text": "食べないと思います", "correct": False}]},
            {"q": "Decides en este momento: 'Pienso tomar un taxi' (Noru):", "options": [{"text": "タクシーに乗ろうと思います", "correct": True}, {"text": "タクシーに乗ろうと思っています", "correct": False}, {"text": "タクシーに乗ることにしています", "correct": False}]},
            {"q": "'Tengo la regla de hacer ejercicio (Undou suru) todos los días':", "options": [{"text": "運動することにしています", "correct": True}, {"text": "運動することになりました", "correct": False}, {"text": "運動しようと思っています", "correct": False}]},
            {"q": "'Llevo tiempo pensando en renunciar a la empresa' (Yameru):", "options": [{"text": "会社を辞めようと思っています", "correct": True}, {"text": "会社を辞めようと思います", "correct": False}, {"text": "会社を辞めるつもりです", "correct": False}]},
            {"q": "¿Qué implica 'ことになった' (Koto ni natta)?", "options": [{"text": "Que fue tu propia decisión personal.", "correct": False}, {"text": "Que la decisión se tomó de forma externa o colectiva (ej. la empresa).", "correct": True}, {"text": "Que quieres hacer algo pero no puedes.", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "田中さん、来年の夏休みの予定は決まりましたか。", "Tanaka, ¿ya has decidido tus planes para las vacaciones de verano del próximo año?"),
            ("ja-JP-KeitaNeural", "はい、北海道へ旅行しようと思っています。", "Sí, llevo tiempo pensando en viajar a Hokkaido."),
            ("ja-JP-NanamiNeural", "北海道ですか！いいですね。飛行機で行くんですか。", "¡Hokkaido! Qué bien. ¿Vas a ir en avión?"),
            ("ja-JP-KeitaNeural", "いえ、景色を楽しみたいので、新幹線で行くつもりです。", "No, como quiero disfrutar del paisaje, tengo la intención de ir en tren bala."),
            ("ja-JP-NanamiNeural", "なるほど。私も来年はどこかへ行こうかな。", "Ya veo. Quizás yo también vaya a algún lado el próximo año."),
            ("ja-JP-KeitaNeural", "実は来月から、仕事で北海道に一ヶ月住むことになったんですよ。", "La verdad es que se ha decidido que a partir del mes que viene viviré un mes en Hokkaido por trabajo."),
            ("ja-JP-NanamiNeural", "ええっ、出張ですか。だから旅行しようと思っていたんですね。", "¿Eh? ¿Un viaje de negocios? Con razón estabas pensando en viajar allí."),
            ("ja-JP-KeitaNeural", "そうなんです。美味しい海鮮をたくさん食べることにしています！", "Así es. ¡Tengo la regla personal de que comeré muchos mariscos deliciosos!")
        ]
    },
    2: {
        "title": "Consejos y Recomendaciones (~たほうがいい / ~べきだ)",
        "grammar": [
            "<strong>V(ta) + ほうがいい:</strong> Es mejor que... / Te recomiendo que... (Si no lo haces, habrá malas consecuencias). Ej. 病院へ行ったほうがいい (Deberías ir al hospital).",
            "<strong>V(nai) + ないほうがいい:</strong> Es mejor que NO... Ej. お酒を飲まないほうがいい (Es mejor que no bebas).",
            "<strong>V(dic) + べきだ / べきではない:</strong> Deberías / No deberías... (Obligación moral, sentido común o fuerte convicción del hablante). Ej. 約束は守るべきだ (Las promesas se deben cumplir). <em>Nota: Suru -> Subeki.</em>",
            "<strong>V(tara) + どうですか:</strong> ¿Por qué no...? (Un consejo ligero o sugerencia a un compañero). Ej. 先生に聞いたらどうですか (¿Por qué no le preguntas al profesor?)."
        ],
        "examples": [
            ("熱があるなら、早く寝たほうがいいですよ。", "1. Si tienes fiebre, es mejor que te acuestes temprano.", "ねつがあるなら、はやくねたほうがいいですよ"),
            ("雨が降るかもしれないから、傘を持っていったほうがいい。", "2. Como tal vez llueva, es mejor que lleves paraguas.", "あめがふるかもしれないから、かさをもっていったほうがいい"),
            ("甘いものはあまり食べないほうがいいです。", "3. Es mejor que no comas muchas cosas dulces.", "あまいものはあまりたべないほうがいいです"),
            ("学生はもっと勉強するべきだ。", "4. Los estudiantes deberían estudiar más (es su obligación/sentido común).", "がくせいはもっとべんきょうするべきだ"),
            ("他人のメールを勝手に見るべきではない。", "5. No se deberían mirar los correos ajenos sin permiso.", "たにんのメールをかってにみるべきではない"),
            ("もっと早く謝るべきだった。", "6. Debiste haberte disculpado mucho antes.", "もっとはやくあやまるべきだった"),
            ("わからないなら、先生に聞いたらどうですか。", "7. Si no lo entiendes, ¿por qué no le preguntas al profesor?", "わからないなら、せんせいにきいたらどうですか"),
            ("たまにはゆっくり休んだらどうですか。", "8. ¿Por qué no descansas tranquilamente de vez en cuando?", "たまにはゆっくりやすんだらどうですか"),
            ("風邪をひいた時は、お風呂に入らないほうがいい。", "9. Cuando tienes un resfriado, es mejor que no te bañes.", "かぜをひいたときは、おふろにはいらないほうがいい"),
            ("どんな理由があっても、嘘をつくべきではない。", "10. Sin importar la razón, no se deben decir mentiras.", "どんなりゆうがあっても、うそをつくべきではない")
        ],
        "exercises": [
            {"q": "¿Qué forma verbal se usa antes de 'hou ga ii' para dar un consejo afirmativo? (Ej. Es mejor que vayas)", "options": [{"text": "Forma TA (行ったほうがいい)", "correct": True}, {"text": "Forma Diccionario (行くほうがいい)", "correct": False}, {"text": "Forma TE (行ってほうがいい)", "correct": False}]},
            {"q": "¿Y para el consejo negativo? (Ej. Es mejor que NO vayas)", "options": [{"text": "Forma NAI (行かないほうがいい)", "correct": True}, {"text": "Forma NAKATTA (行かなかったほうがいい)", "correct": False}, {"text": "Forma Diccionario (行くないほうがいい)", "correct": False}]},
            {"q": "'Beki da' expresa una obligación moral o expectativa de sentido común. ¿Qué forma se usa antes de 'beki da'?", "options": [{"text": "Forma TA", "correct": False}, {"text": "Forma Diccionario", "correct": True}, {"text": "Forma MASU", "correct": False}]},
            {"q": "Excepción de Beki: El verbo する (Hacer) puede ser するべき, pero también tiene una forma especial y más común. ¿Cuál es?", "options": [{"text": "すべき (Subeki)", "correct": True}, {"text": "しべき (Shibeki)", "correct": False}, {"text": "さべき (Sabeki)", "correct": False}]},
            {"q": "Para dar una sugerencia suave a un compañero: '¿Por qué no bebes agua?' (Nomu):", "options": [{"text": "水を飲むべきだ", "correct": False}, {"text": "水を飲んだらどうですか", "correct": True}, {"text": "水を飲んだほうがいい", "correct": False}]},
            {"q": "'Los niños NO DEBERÍAN beber alcohol' (Obligación / Sentido común):", "options": [{"text": "子供はお酒を飲むべきではない", "correct": True}, {"text": "子供はお酒を飲まないほうがいい", "correct": False}, {"text": "子供はお酒を飲んだらどうですか", "correct": False}]},
            {"q": "'Estás muy cansado. Es mejor que descanses' (Yasumu):", "options": [{"text": "休むほうがいいですよ", "correct": False}, {"text": "休んだほうがいいですよ", "correct": True}, {"text": "休んでほうがいいですよ", "correct": False}]},
            {"q": "'Debiste decir la verdad' (Pasado de Beki):", "options": [{"text": "本当のことを言うべきだった", "correct": True}, {"text": "本当のことを言ったべきだ", "correct": False}, {"text": "本当のことを言うべきでした", "correct": False}]},
            {"q": "'¿Por qué no vas al hospital?' (Iku -> Iki -> Itta):", "options": [{"text": "病院へ行ったほうがどうですか", "correct": False}, {"text": "病院へ行ったらどうですか", "correct": True}, {"text": "病院へ行くべきどうですか", "correct": False}]},
            {"q": "Diferencia entre 'Hou ga ii' y 'Beki': Si le dices a tu jefe 'Usted debería trabajar', suena arrogante. ¿Cuál es la forma más suave y aceptable (aunque igual ten cuidado con los superiores)?", "options": [{"text": "働くべきです", "correct": False}, {"text": "働いたらどうですか / 働いたほうがいいです", "correct": True}, {"text": "No hay diferencia", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-KeitaNeural", "最近、少し太ってしまって、服がきつくなったんですよ。", "Últimamente he engordado un poco y la ropa me queda apretada."),
            ("ja-JP-NanamiNeural", "それなら、運動したほうがいいですよ。", "Si es así, es mejor que hagas ejercicio."),
            ("ja-JP-KeitaNeural", "わかっているんですが、仕事が忙しくて時間がないんです。", "Lo sé, pero estoy ocupado con el trabajo y no tengo tiempo."),
            ("ja-JP-NanamiNeural", "でも、健康が一番大切です。無理して働くべきではないと思います。", "Pero la salud es lo más importante. Creo que no deberías trabajar esforzándote demasiado (obligación)."),
            ("ja-JP-KeitaNeural", "そうですね。これからは、夜遅くまで仕事をやらないほうがいいかもしれませんね。", "Tienes razón. De ahora en adelante, quizás sea mejor que no trabaje hasta tarde por la noche."),
            ("ja-JP-NanamiNeural", "ええ。それから、甘いものも少し減らしたらどうですか。", "Sí. Y además, ¿por qué no reduces un poco las cosas dulces? (sugerencia)"),
            ("ja-JP-KeitaNeural", "それが一番難しいんです。甘いものを食べるべきではないとわかっているのに...", "Eso es lo más difícil. A pesar de que sé que no debo comer cosas dulces..."),
            ("ja-JP-NanamiNeural", "ふふ、少しずつ頑張りましょう。", "Jeje, esfuérzate poco a poco.")
        ]
    },
    3: {
        "title": "Cambios de estado y Esfuerzo (~ようになる / ~ようにする)",
        "grammar": [
            "<strong>V(dic/nai) + ようになる:</strong> Expresa un cambio de estado natural o de habilidad (Llegar a hacer algo / Empezar a hacer algo). Ej. 日本語が話せるようになった (He llegado a poder hablar japonés).",
            "<strong>V(dic/nai) + ようにする:</strong> Expresa un esfuerzo o hábito consciente (Hacer el esfuerzo de...). Ej. 毎日野菜を食べるようにしている (Hago el esfuerzo/procuro comer verduras todos los días).",
            "<em>Diferencia clave:</em> 'Naru' es un cambio (muchas veces potencial). 'Suru' es un esfuerzo de voluntad."
        ],
        "examples": [
            ("１年勉強して、日本語が話せるようになりました。", "1. Tras estudiar un año, he llegado a poder hablar japonés.", "いちねんべんきょうして、にほんごがはなせるようになりました"),
            ("最近、日本のニュースが少しわかるようになりました。", "2. Últimamente, he empezado a entender un poco las noticias de Japón.", "さいきん、にほんのニュースがすこしわかるようになりました"),
            ("以前は肉が好きでしたが、最近は食べなくなりました。", "3. Antes me gustaba la carne, pero últimamente he dejado de comerla (Cambio al negativo: nai -> naku naru).", "いぜんはにくがすきでしたが、さいきんはたべなくなりました"),
            ("毎日３０分、散歩するようにしています。", "4. Procuro (hago el esfuerzo de) pasear 30 minutos todos los días.", "まいにちさんじゅっぷん、さんぽするようにしています"),
            ("忘れないように、メモをしてください。", "5. Por favor, tome notas de manera que (con el fin de que) no se olvide.", "わすれないように、メモをしてください"),
            ("塩をあまり入れないようにしています。", "6. Hago el esfuerzo de no ponerle mucha sal.", "しおをあまりいれないようにしています"),
            ("明日から早く起きるようにします。", "7. A partir de mañana procuraré (me esforzaré en) levantarme temprano.", "あしたからはやくおきるようにします"),
            ("自転車に乗れるようになりました。", "8. He aprendido (llegado a poder) a montar en bicicleta.", "じてんしゃにのれるようになりました"),
            ("子供が一人で服を着られるようになった。", "9. El niño ha llegado a poder ponerse la ropa solo.", "こどもがひとりでふくをきられるようになった"),
            ("風邪をひかないように、気をつけてください。", "10. Por favor, tenga cuidado para no resfriarse.", "かぜをひかないように、きをつけてください")
        ],
        "exercises": [
            {"q": "¿Qué expresión se usa para denotar un ESFUERZO consciente para crear un hábito? 'Procuro hacerlo...'", "options": [{"text": "～ようにする / ～ようにしている", "correct": True}, {"text": "～ようになる", "correct": False}, {"text": "～ようと思う", "correct": False}]},
            {"q": "¿Qué expresión se usa para denotar un CAMBIO de habilidad o estado natural? 'He llegado a poder...'", "options": [{"text": "～ようになる / ～ようになった", "correct": True}, {"text": "～ようにする", "correct": False}, {"text": "～ことにしている", "correct": False}]},
            {"q": "'He empezado a comer verduras (antes no lo hacía)': 野菜を___。", "options": [{"text": "食べるようにした", "correct": False}, {"text": "食べるようになった", "correct": True}, {"text": "食べたようになった", "correct": False}]},
            {"q": "'Hago el esfuerzo de estudiar todos los días' (Benkyou suru):", "options": [{"text": "勉強するようにしています", "correct": True}, {"text": "勉強するようになっています", "correct": False}, {"text": "勉強するつもりになっています", "correct": False}]},
            {"q": "Para cambiar un verbo NAI a 'dejar de hacerlo'. Ej. 'Dejé de beber' (Nomanai -> Nomu):", "options": [{"text": "飲まないようになりました", "correct": False}, {"text": "飲まなくなりました", "correct": True}, {"text": "飲まないようにしました", "correct": False}]},
            {"q": "'Procuro NO llegar tarde' (Okurenai):", "options": [{"text": "遅れないようにしています", "correct": True}, {"text": "遅れなくしています", "correct": False}, {"text": "遅れないようになっています", "correct": False}]},
            {"q": "'¿Ya has llegado a poder leer kanjis?' (Yomeru):", "options": [{"text": "漢字が読めるようにしましたか", "correct": False}, {"text": "漢字が読めるようになりましたか", "correct": True}, {"text": "漢字が読むようになりましたか", "correct": False}]},
            {"q": "'Por favor, procura no comer cosas dulces' (Amai mono wo tabenai):", "options": [{"text": "甘いものを食べなくしてください", "correct": False}, {"text": "甘いものを食べないようにしてください", "correct": True}, {"text": "甘いものを食べないようになってください", "correct": False}]},
            {"q": "A menudo, ～ようになる se usa con verbos en qué forma?", "options": [{"text": "Forma Potencial (Ej. 話せる - poder hablar)", "correct": True}, {"text": "Forma Pasiva", "correct": False}, {"text": "Forma Causativa", "correct": False}]},
            {"q": "'Me he acostumbrado a Japón y he empezado a entender las noticias' (Wakaru):", "options": [{"text": "ニュースがわかるようになりました", "correct": True}, {"text": "ニュースがわかるようにしました", "correct": False}, {"text": "ニュースがわかるつもりになりました", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "マリアさん、日本語がとても上手になりましたね。", "María, te has vuelto muy buena en japonés."),
            ("ja-JP-KeitaNeural", "ありがとうございます。毎日アニメを見ているので、少しずつわかるようになりました。", "Gracias. Como veo anime todos los días, he empezado a entenderlo (llegado a poder entender) poco a poco."),
            ("ja-JP-NanamiNeural", "素晴らしいですね。最初は難しかったでしょう？", "Es maravilloso. Al principio debió ser difícil, ¿verdad?"),
            ("ja-JP-KeitaNeural", "はい。全然話せませんでしたが、最近は少し話せるようになりました。", "Sí. No podía hablar nada, pero últimamente he llegado a poder hablar un poco."),
            ("ja-JP-NanamiNeural", "どんな勉強をしているんですか。", "¿Qué clase de estudio estás haciendo?"),
            ("ja-JP-KeitaNeural", "寝る前に、必ず日本語の本を少し読むようにしています。", "Antes de dormir, hago el esfuerzo (procuro) sin falta leer un poco un libro en japonés."),
            ("ja-JP-NanamiNeural", "その努力が結果に出ているんですね。", "Ese esfuerzo está dando resultados."),
            ("ja-JP-KeitaNeural", "ええ。これからも、もっと難しい漢字が読めるように頑張ります！", "Sí. ¡A partir de ahora también me esforzaré para llegar a poder leer kanjis más difíciles!")
        ]
    },
    4: {
        "title": "Transmisión formal (~そうだ / ~ということだ / ~とのことだ)",
        "grammar": [
            "<strong>Forma Plana + そうだ:</strong> 'Dicen que... / Escuché que...'. Transmite información oída (Ya visto en N4, repaso breve). Ej. 明日は雨だそうだ.",
            "<strong>Forma Plana + ということだ:</strong> 'Significa que... / Dicen que...'. Transmite un mensaje, rumor o conclusión formal. Ej. 部長は来ないということだ (Dicen/Significa que el jefe no vendrá).",
            "<strong>Forma Plana + とのことだ:</strong> Más formal que 'to iu koto da'. Se usa en el trabajo para transmitir mensajes exactos de terceros. Ej. 会議は3時からとのことです (Dice [él/ella] que la reunión es desde las 3).",
            "<em>Según...</em> se expresa con 'N + によると / によれば' al principio de la frase."
        ],
        "examples": [
            ("天気予報によると、明日は雪が降るそうです。", "1. Según el pronóstico, dicen que mañana nevará.", "てんきよほうによると、あしたはゆきがふるそうです"),
            ("手紙によると、彼は元気だということです。", "2. Según la carta, dicen que él está bien (Transmisión formal).", "てがみによると、かれはげんきだということです"),
            ("社長は今日の会議には出席しないとのことです。", "3. El presidente comunica que no asistirá a la reunión de hoy (Muy formal, en el trabajo).", "しゃちょうはきょうのかいぎにはしゅっせきしないとのことです"),
            ("ニュースによれば、事故の原因はまだわからないとのことだ。", "4. Según las noticias, dicen que la causa del accidente aún no se sabe.", "ニュースによれば、じこのげんいんはまだわからないとのことだ"),
            ("つまり、このプロジェクトは失敗したということですか。", "5. En resumen, ¿esto significa que el proyecto ha fracasado?", "つまり、このプロジェクトはしっぱいしたということですか"),
            ("明日は休みだそうだ。", "6. Escuché que mañana es día libre (Sustantivo + だ + そうだ).", "あしたはやすみだそうだ"),
            ("彼はもうすぐ結婚するということだ。", "7. Se rumorea/Dicen que él se va a casar pronto.", "かれはもうすぐけっこんするということだ"),
            ("先生からのメールによれば、テストは来週だそうです。", "8. Según el correo del profesor, dicen que el examen es la próxima semana.", "せんせいからのメールによれば、テストはらいしゅうだそうです"),
            ("ご家族は皆お元気とのこと、安心いたしました。", "9. Me alivia escuchar que toda su familia está bien (Lenguaje escrito/formal).", "ごかぞくはみなおげんきとのこと、あんしんいたしました"),
            ("このマークは「立ち入り禁止」ということだ。", "10. Esta marca significa 'Prohibido el paso'.", "このマークはたちいりきんしということだ")
        ],
        "exercises": [
            {"q": "¿Qué expresión se usa frecuentemente al inicio de la frase para indicar la fuente de la información (Según...)?", "options": [{"text": "～によると / ～によれば", "correct": True}, {"text": "～のために", "correct": False}, {"text": "～について", "correct": False}]},
            {"q": "¿Cuál es la expresión MÁS formal para transmitir el mensaje de un cliente o jefe a tus compañeros de trabajo?", "options": [{"text": "～とのことです", "correct": True}, {"text": "～みたいです", "correct": False}, {"text": "～そうです", "correct": False}]},
            {"q": "'Dicen que él está ocupado' (Sustantivo/Adjetivo-na). Ojo con el 'da' antes de 'sou da' y 'to iu koto da'.", "options": [{"text": "忙しいだそうです", "correct": False}, {"text": "忙しいということです (O isogashii sou desu)", "correct": True}, {"text": "忙しいなそうです", "correct": False}]},
            {"q": "Para un SUSTANTIVO: 'Según dicen, mañana es día libre (Yasumi)'.", "options": [{"text": "休みそうです", "correct": False}, {"text": "休みだということです", "correct": True}, {"text": "休みなということです", "correct": False}]},
            {"q": "¿Qué otro significado tiene '～ということだ' además de transmitir información?", "options": [{"text": "Intención futura", "correct": False}, {"text": "Sacar una conclusión ('Esto significa que...')", "correct": True}, {"text": "Capacidad o habilidad", "correct": False}]},
            {"q": "'En resumen, ¿significa que no puedes ir?' (Ikenai):", "options": [{"text": "つまり、行けないとのことですか", "correct": False}, {"text": "つまり、行けないということですか", "correct": True}, {"text": "つまり、行けないそうですか", "correct": False}]},
            {"q": "'Recibí una llamada de Tanaka, y dice que se retrasará 10 minutos' (Okureru - Formal de oficina):", "options": [{"text": "田中さんから電話があり、１０分遅れるとのことです。", "correct": True}, {"text": "田中さんから電話があり、１０分遅れるみたいです。", "correct": False}, {"text": "田中さんから電話があり、１０分遅れるはずです。", "correct": False}]},
            {"q": "'Según el periódico (Shinbun ni yoru to)...'", "options": [{"text": "新聞によれば", "correct": True}, {"text": "新聞によくて", "correct": False}, {"text": "新聞によりて", "correct": False}]},
            {"q": "¿Qué forma verbal va antes de とのことだ / ということだ?", "options": [{"text": "Forma MASU", "correct": False}, {"text": "Forma Plana (Futsukei)", "correct": True}, {"text": "Forma TE", "correct": False}]},
            {"q": "'Escuché que el examen fue difícil' (Muzukashikatta):", "options": [{"text": "難しかっただそうです", "correct": False}, {"text": "難しかったとのことです", "correct": True}, {"text": "難しかったなということです", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "鈴木さん、佐藤部長は今日、お休みですか。朝から見かけないんですが。", "Suzuki, ¿el director Sato tiene el día libre hoy? No le he visto desde la mañana."),
            ("ja-JP-KeitaNeural", "ああ、部長は出張中ですよ。スケジュールによれば、金曜日まで大阪だということです。", "Ah, el director está de viaje de negocios. Según el horario, significa (o dice) que estará en Osaka hasta el viernes."),
            ("ja-JP-NanamiNeural", "そうなんですか。金曜日の会議には出席なさるんでしょうか。", "¿Ah sí? ¿Asistirá a la reunión del viernes?"),
            ("ja-JP-KeitaNeural", "さっき部長から電話がありまして、新幹線の時間があるので、会議には間に合わないとのことです。", "Hace un momento me llamó el director y, como tiene la hora del tren bala, dice (formal) que no llegará a tiempo a la reunión."),
            ("ja-JP-NanamiNeural", "つまり、金曜日の会議は部長なしで行うということですね。", "O sea, ¿eso significa que haremos la reunión del viernes sin el director?"),
            ("ja-JP-KeitaNeural", "ええ、そういうことです。部長の代わりに、私が資料を説明することになりました。", "Sí, eso significa. Se ha decidido que yo explicaré los documentos en lugar del director."),
            ("ja-JP-NanamiNeural", "わかりました。資料の準備、手伝いましょうか。", "Entendido. ¿Te ayudo a preparar los documentos?"),
            ("ja-JP-KeitaNeural", "ありがとうございます。助かります。", "Gracias. Me salvas.")
        ]
    },
    5: {
        "title": "Suposiciones y Certezas (~かもしれない / ~に違いない / ~はずがない)",
        "grammar": [
            "<strong>Forma Plana + かもしれない:</strong> 'Quizás / Tal vez' (Baja probabilidad, alrededor del 50% o menos). Ej. 明日は雨かもしれない (Quizás llueva mañana).",
            "<strong>Forma Plana + に違いない (にちがいない):</strong> 'No hay duda de que / Estoy seguro de que' (Alta certeza deductiva). Ej. 彼は犯人に違いない (Sin duda él es el culpable).",
            "<strong>Forma Plana + はずがない:</strong> 'Es imposible que / No puede ser que' (Fuerte negación deductiva). Ej. 彼がそんなことをするはずがない (Es imposible que él haga tal cosa)."
        ],
        "examples": [
            ("もしかしたら、明日は雨が降るかもしれない。", "1. Quizás, mañana llueva.", "もしかしたら、あしたはあめがふるかもしれない"),
            ("約束の時間を間違えたのかもしれません。", "2. Tal vez me equivoqué con la hora de la cita.", "やくそくのじかんをまちがえたのかもしれません"),
            ("あんなに勉強したんだから、合格するに違いない。", "3. Habiendo estudiado tanto, estoy seguro de que (no hay duda de que) aprobará.", "あんなにべんきょうしたんだから、ごうかくするにちがいない"),
            ("このダイヤは本物に違いない。", "4. Este diamante es, sin duda, auténtico.", "このダイヤはほんものにちがいない"),
            ("彼が嘘をつくはずがない。彼はとても正直な人だから。", "5. Es imposible que él diga mentiras. Porque es una persona muy honesta.", "かれがうそをつくはずがない。かれはとてもしょうじきなひとだから"),
            ("こんな難しい問題、子供にわかるはずがありません。", "6. Un problema tan difícil, es imposible que un niño lo entienda.", "こんなむずかしいもんだい、こどもにわかるはずがありません"),
            ("彼は昨日、国へ帰ったから、今日ここにいるはずがない。", "7. Él regresó a su país ayer, así que es imposible que esté aquí hoy.", "かれはきのう、くにへかえったから、きょうここにいるはずがない"),
            ("道が混んでいるから、遅れるかもしれません。", "8. Como la calle está atascada, quizás me retrase.", "みちがこんでいるから、おくれるかもしれません"),
            ("あの人は有名人に違いありません。", "9. Aquella persona, sin duda, es una celebridad.", "あのひとはゆうめいじんにちがいありません"),
            ("宝くじが当たるかもしれない。", "10. Quizás me toque la lotería.", "たからくじがあたるかもしれない")
        ],
        "exercises": [
            {"q": "¿Qué expresión denota una probabilidad BAJA, equivalente a 'Tal vez / Quizás'?", "options": [{"text": "～かもしれない", "correct": True}, {"text": "～に違いない", "correct": False}, {"text": "～はずがない", "correct": False}]},
            {"q": "¿Qué expresión denota una CERTEZA MUY ALTA basada en evidencia, 'Sin duda / Estoy seguro de que...'?", "options": [{"text": "～に違いない", "correct": True}, {"text": "～かもしれない", "correct": False}, {"text": "～はずがない", "correct": False}]},
            {"q": "¿Qué expresión denota 'ES IMPOSIBLE QUE / No puede ser que...'?", "options": [{"text": "～はずがない", "correct": True}, {"text": "～かもしれない", "correct": False}, {"text": "～に違いない", "correct": False}]},
            {"q": "'Estudió 10 horas al día. SIN DUDA pasará el examen' (Goukaku suru):", "options": [{"text": "合格するかもしれない", "correct": False}, {"text": "合格するに違いない", "correct": True}, {"text": "合格するはずがない", "correct": False}]},
            {"q": "'¿Ese niño resolvió este problema de universidad? ¡ES IMPOSIBLE que lo haya hecho!' (Dekiru):", "options": [{"text": "できるはずがない", "correct": True}, {"text": "できるに違いない", "correct": False}, {"text": "できるかもしれない", "correct": False}]},
            {"q": "¿Qué adverbio se suele usar junto con 'kamo shirenai' para reforzar el 'tal vez'?", "options": [{"text": "絶対に (Zettai ni - absolutamente)", "correct": False}, {"text": "もしかしたら (Moshikashitara - por si acaso / tal vez)", "correct": True}, {"text": "必ず (Kanarazu - sin falta)", "correct": False}]},
            {"q": "'Esta bolsa es muy ligera. ES IMPOSIBLE QUE haya libros adentro' (Hon ga haitte iru):", "options": [{"text": "本が入っているはずがない", "correct": True}, {"text": "本が入っているかもしれない", "correct": False}, {"text": "本が入っているに違いない", "correct": False}]},
            {"q": "Para un SUSTANTIVO con 'ni chigai nai' (Ej. Hontou - Verdad):", "options": [{"text": "本当なに違いない", "correct": False}, {"text": "本当に違いない", "correct": True}, {"text": "本当だに違いない", "correct": False}]},
            {"q": "'Tal vez venga mañana' (Kuru):", "options": [{"text": "明日来るかもしれない", "correct": True}, {"text": "明日来るに違いない", "correct": False}, {"text": "明日来るはずがない", "correct": False}]},
            {"q": "Para un Adjetivo Na con 'Hazu ga nai' (Ej. Genki):", "options": [{"text": "元気はずがない", "correct": False}, {"text": "元気なはずがない", "correct": True}, {"text": "元気だはずがない", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-KeitaNeural", "ねえ、山田さん、最近田中さんの様子がおかしくないですか。", "Oye, Yamada, ¿no te parece que el comportamiento de Tanaka últimamente es raro?"),
            ("ja-JP-NanamiNeural", "ええ、いつもニコニコしているし、帰りも早いです。もしかしたら、彼女ができたのかもしれませんね。", "Sí, siempre está sonriendo y se va temprano. Quizás, tal vez se echó novia."),
            ("ja-JP-KeitaNeural", "彼女ですか！でも、先週は「お金がない」と言っていましたよ。デートに行くお金があるはずがありません。", "¿Novia? Pero la semana pasada estaba diciendo 'no tengo dinero'. Es imposible que tenga dinero para ir a una cita."),
            ("ja-JP-NanamiNeural", "そうですね。あ、もしかしたら、宝くじが当たったのかもしれませんよ！", "Tienes razón. Ah, ¡quizás le tocó la lotería!"),
            ("ja-JP-KeitaNeural", "いやいや、宝くじが当たるはずがないでしょう。もっと現実的に考えましょう。", "No, no, es imposible que le toque la lotería. Pensemos de forma más realista."),
            ("ja-JP-NanamiNeural", "じゃあ、新しいゲームを買ったに違いありません。彼はゲームが大好きですから。", "Entonces, sin duda se compró un juego nuevo. Como a él le encantan los videojuegos..."),
            ("ja-JP-KeitaNeural", "なるほど、それに違いありません！だから早く帰りたいんですね。", "Ya veo, ¡sin duda es eso! Por eso quiere irse a casa temprano.")
        ]
    }
}

base_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\lessons"
audio_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\audio"
os.makedirs(audio_dir, exist_ok=True)

# Generate HTML and Audio for N3 1-5
for i in range(1, 6):
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

# Update index.html
filepath = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

links_html = ""
for i in range(1, 6):
    title = data[i]["title"]
    links_html += f'''                        <a href="lessons/jlpt-n3-{i}.html" target="main_frame" class="nav-link">
                            <span class="nav-num">{i}</span> {title}
                        </a>\n'''

target_old = '<div class="coming-soon">Próximamente...</div>'

if target_old in content:
    new_content = content.replace(target_old, links_html)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Updated index.html")
else:
    print("WARNING: Could not find target in index.html")

print("Running add_furigana.py...")
subprocess.run("python add_furigana.py", shell=True)
print("ALL TASKS COMPLETED!")
