import os
import subprocess

data = {
    11: {
        "title": "Esfuerzos y Cambios (~ようにしています / ~ようになります)",
        "grammar": [
            "<strong>V(dic) / V(nai) + ように しています:</strong> Intentar hacer algo como hábito o hacer un esfuerzo continuo. Ej: 毎日運動するようにしています (Intento hacer ejercicio todos los días).",
            "<strong>V(dic) + ようになりました:</strong> Indica un cambio de estado, pasar a poder hacer algo que antes no se podía. Ej: 日本語が話せるようになりました (He llegado a poder hablar japonés).",
            "<strong>V(dic) / V(nai) + ように してください:</strong> Por favor, asegúrese de hacer / intente hacer (más suave que te kudasai, es para hábitos o instrucciones)."
        ],
        "examples": [
            ("毎日運動するようにしています。", "1. Intento (hago el esfuerzo de) hacer ejercicio todos los días.", "まいにちうんどうするようにしています"),
            ("甘いものを食べないようにしています。", "2. Intento no comer cosas dulces.", "あまいものをたべないようにしています"),
            ("日本語が話せるようになりました。", "3. He llegado a poder (ahora puedo) hablar japonés.", "にほんごがはなせるようになりました"),
            ("泳げるようになりました。", "4. Ahora puedo nadar (antes no podía).", "およげるようになりました"),
            ("肉を食べなくなりました。", "5. He dejado de comer carne.", "にくをたべなくなりました"),
            ("もっと野菜を食べるようにしてください。", "6. Por favor, intente comer más verduras.", "もっとやさいをたべるようにしてください"),
            ("絶対に遅れないようにしてください。", "7. Por favor, asegúrese de no llegar tarde bajo ninguna circunstancia.", "ぜったいにおくれないようにしてください"),
            ("最近、よく寝るようになりました。", "8. Últimamente, he empezado a dormir bien.", "さいきん、よくねるようになりました"),
            ("忘れないようにメモします。", "9. Tomo notas para no olvidar.", "わすれないようにメモします"),
            ("毎日ニュースを見るようにしています。", "10. Hago el esfuerzo de ver las noticias todos los días.", "まいにちニュースをみるようにしています")
        ],
        "exercises": [
            {"q": "¿Qué expresión se usa para describir un HÁBITO que intentas mantener?", "options": [{"text": "ように しています", "correct": True}, {"text": "ように なりました", "correct": False}, {"text": "ように してください", "correct": False}]},
            {"q": "'Intento NO beber alcohol' (Esfuerzo consciente):", "options": [{"text": "お酒を飲まないようになりました", "correct": False}, {"text": "お酒を飲まないようにしています", "correct": True}, {"text": "お酒を飲まないようにしてください", "correct": False}]},
            {"q": "¿Qué expresión indica que has adquirido una NUEVA HABILIDAD que antes no tenías?", "options": [{"text": "ように しています", "correct": False}, {"text": "ように なりました", "correct": True}, {"text": "ように します", "correct": False}]},
            {"q": "'Ahora PUEDO leer kanjis' (Antes no podía):", "options": [{"text": "漢字が読めるようにしています", "correct": False}, {"text": "漢字が読めるようになりました", "correct": True}, {"text": "漢字を読むようになりました", "correct": False}]},
            {"q": "Si le dices a un empleado: 'Por favor, asegúrese de no olvidar la llave' (Instrucción suave):", "options": [{"text": "鍵を忘れないでください", "correct": False}, {"text": "鍵を忘れないようにしてください", "correct": True}, {"text": "鍵を忘れないようにしています", "correct": False}]},
            {"q": "¿Qué forma verbal va ANTES de 'youni narimashita' cuando se habla de HABILIDADES?", "options": [{"text": "Forma Diccionario del verbo normal (Ej. 読む)", "correct": False}, {"text": "Forma Potencial (Ej. 読める)", "correct": True}, {"text": "Forma TA (Ej. 読んだ)", "correct": False}]},
            {"q": "'Me he vuelto capaz de entender las noticias' (Wakaru):", "options": [{"text": "ニュースがわかるようになりました", "correct": True}, {"text": "ニュースがわかるようにしています", "correct": False}, {"text": "ニュースがわかれます", "correct": False}]},
            {"q": "'Me esfuerzo por dormir 8 horas' (Neru):", "options": [{"text": "８時間寝るようにしています", "correct": True}, {"text": "８時間寝るようになりました", "correct": False}, {"text": "８時間寝るようにしてください", "correct": False}]},
            {"q": "¿Cómo se dice el negativo 'He dejado de ver la televisión' (Ya no lo hago)?", "options": [{"text": "テレビを見ないようになりました", "correct": False}, {"text": "テレビを見なくなりました", "correct": True}, {"text": "テレビを見ないようにしています", "correct": False}]},
            {"q": "'Tomo notas PARA NO OLVIDAR' (El 'youni' de objetivo):", "options": [{"text": "忘れないように、メモします", "correct": True}, {"text": "忘れるように、メモします", "correct": False}, {"text": "忘れなくて、メモします", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "山田さん、最近痩せましたね。", "Yamada, últimamente has adelgazado, ¿no?"),
            ("ja-JP-KeitaNeural", "ええ、毎日１時間歩くようにしているんです。", "Sí, estoy haciendo el esfuerzo de caminar una hora todos los días."),
            ("ja-JP-NanamiNeural", "すごいですね。食事も気をつけているんですか。", "Es increíble. ¿También estás cuidando la comida?"),
            ("ja-JP-KeitaNeural", "はい。甘いものを食べないようにしています。", "Sí. Intento no comer cosas dulces."),
            ("ja-JP-NanamiNeural", "なるほど。私も運動するようにしたいです。", "Ya veo. A mí también me gustaría intentar hacer ejercicio."),
            ("ja-JP-KeitaNeural", "初めは疲れますが、すぐにもっと歩けるようになりますよ。", "Al principio te cansas, pero pronto serás capaz de caminar más."),
            ("ja-JP-NanamiNeural", "そうですか。私も明日から歩くようにします。", "¿Ah sí? Entonces yo también empezaré a hacer el esfuerzo de caminar a partir de mañana."),
            ("ja-JP-KeitaNeural", "じゃあ、無理をしないようにしてくださいね。", "Bien, pero por favor asegúrate de no esforzarte demasiado.")
        ]
    },
    12: {
        "title": "Forma Pasiva (~れる / ~られる)",
        "grammar": [
            "<strong>G1 (u->a + reru), G2 (ru->rareru), G3 (suru->sareru, kuru->korareru)</strong>",
            "<strong>N1(Persona) は N2(Persona) に V(pasiva):</strong> N1 sufre la acción de N2. Ej: 私は先生に褒められました (Fui elogiado por el profesor).",
            "<strong>N1 は N2(Persona) に N3(Objeto) を V(pasiva):</strong> La 'Pasiva de molestia'. Ej: 私は弟にパソコンを壊されました (Mi hermano menor me rompió la pc y me causó problemas).",
            "<strong>N(cosa) は V(pasiva):</strong> Cuando el autor de la acción no importa o no se sabe. Ej: この家は200年前に建てられました (Esta casa fue construida hace 200 años)."
        ],
        "examples": [
            ("私は先生に褒められました。", "1. Fui elogiado por el profesor.", "わたしはせんせいにほめられました"),
            ("私は母に買い物を頼まれました。", "2. Fui encargado de hacer las compras por mi madre (Mi madre me pidió...).", "わたしはははにかいものをたのまれました"),
            ("私は犬に噛まれました。", "3. Fui mordido por un perro.", "わたしはいぬにかまれました"),
            ("私は弟にケーキを食べられました。", "4. Mi hermano menor se comió mi pastel (y me causó un problema).", "わたしはおとうとにケーキをたべられました"),
            ("雨に降られて、服が濡れました。", "5. Me llovió (sufrí la lluvia) y mi ropa se mojó.", "あめにふられて、ふくがぬれました"),
            ("このお寺は３００年前に建てられました。", "6. Este templo fue construido hace 300 años.", "このおてらはさんびゃくねんまえにたてられました"),
            ("来年、新しい橋が造られます。", "7. El año que viene, se construirá un nuevo puente.", "らいねん、あたらしいはしがつくられます"),
            ("会議は大阪で開かれます。", "8. La reunión se celebrará en Osaka.", "かいぎはおおさかでひらかれます"),
            ("泥棒に自転車を盗まれました。", "9. Me robaron la bicicleta (Fui robado en mi bici por un ladrón).", "どろぼうにじてんしゃをぬすまれました"),
            ("みんなに笑われました。", "10. Fui objeto de burla por todos (Todos se rieron de mí).", "みんなにわらわれました")
        ],
        "exercises": [
            {"q": "¿Cómo se forma la pasiva del verbo 叱る (Shikaru - regañar, Grupo I)?", "options": [{"text": "叱られます (Shikararemasu)", "correct": True}, {"text": "叱りれます (Shikariremasu)", "correct": False}, {"text": "叱れます (Shikaremasu)", "correct": False}]},
            {"q": "¿Cómo se forma la pasiva de 食べる (Comer, Grupo II)?", "options": [{"text": "食べられます (Taberaremasu - igual que el potencial)", "correct": True}, {"text": "食べれます (Taberemasu)", "correct": False}, {"text": "食べさせられます", "correct": False}]},
            {"q": "¿Cómo se forma la pasiva de する (Hacer, Grupo III)?", "options": [{"text": "すられます", "correct": False}, {"text": "されます (Saremasu)", "correct": True}, {"text": "しられます", "correct": False}]},
            {"q": "'Fui elogiado (Homeru) POR el profesor': 私は先生___褒められました。", "options": [{"text": "を", "correct": False}, {"text": "に", "correct": True}, {"text": "が", "correct": False}]},
            {"q": "'Me robaron el dinero' (Pasiva de molestia, yo sufro la acción):", "options": [{"text": "私は泥棒をお金を盗まれました。", "correct": False}, {"text": "私は泥棒にお金を盗まれました。", "correct": True}, {"text": "泥棒は私にお金を盗まれました。", "correct": False}]},
            {"q": "'Me llovió' (Sufrí la lluvia):", "options": [{"text": "雨に降られました (Ame ni furaremashita)", "correct": True}, {"text": "雨を降られました", "correct": False}, {"text": "雨が降られました", "correct": False}]},
            {"q": "Cuando hablamos de edificios construidos, ¿quién suele ser el sujeto (con は/が)?", "options": [{"text": "El edificio (Ej: このビルは...建てられました)", "correct": True}, {"text": "El arquitecto", "correct": False}, {"text": "La constructora", "correct": False}]},
            {"q": "'El teléfono fue inventado por Bell' (Inventar = Hatsumei suru):", "options": [{"text": "電話はベルに発明しました", "correct": False}, {"text": "電話はベルによって発明されました", "correct": True}, {"text": "ベルは電話に発明されました", "correct": False}]},
            {"q": "'Mi hermano se comió MI pastel' (Usando pasiva para queja):", "options": [{"text": "弟は私のケーキを食べられました。", "correct": False}, {"text": "私は弟にケーキを食べられました。", "correct": True}, {"text": "私は弟をケーキに食べられました。", "correct": False}]},
            {"q": "¿Cómo se forma la pasiva de 来る (Kuru - Venir)?", "options": [{"text": "来られます (Koraremasu)", "correct": True}, {"text": "来られます (Kiraremasu)", "correct": False}, {"text": "来させられます (Kosaseraremasu)", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-KeitaNeural", "どうしたんですか。元気がないですね。", "¿Qué te pasa? Te veo desanimada."),
            ("ja-JP-NanamiNeural", "実は、弟にパソコンを壊されてしまったんです。", "La verdad es que mi hermano menor me rompió la computadora (sufrí esa acción)."),
            ("ja-JP-KeitaNeural", "えっ、本当ですか。それは大変ですね。", "¿Eh? ¿En serio? Qué problema."),
            ("ja-JP-NanamiNeural", "ええ。それに、私が買ったケーキも食べられました。", "Sí. Además, también se comió el pastel que yo había comprado (sufrí esa acción)."),
            ("ja-JP-KeitaNeural", "ひどい弟さんですね。お母さんに言いましたか。", "Qué hermano tan terrible. ¿Se lo dijiste a tu madre?"),
            ("ja-JP-NanamiNeural", "はい。でも、私が怒られました。「パソコンを貸してあげなさい」って。", "Sí. Pero fui yo la que fue regañada (sufrí la acción). Me dijo: 'Préstale la computadora'."),
            ("ja-JP-KeitaNeural", "それはかわいそうですね。早くパソコンが直るといいですね。", "Pobre de ti. Ojalá tu computadora se arregle pronto."),
            ("ja-JP-NanamiNeural", "ええ、新しい部品はもう注文されましたから、来週には直る予定です。", "Sí, las piezas nuevas ya fueron pedidas (acción pasiva), así que está programado que se arregle la semana que viene.")
        ]
    },
    13: {
        "title": "Nominalización con の (のを見る / のが好き)",
        "grammar": [
            "<strong>V(dic) + のは [Adjetivo] です:</strong> Convertir un verbo en un sujeto. Ej. テニスをするのは面白いです (Jugar tenis es divertido).",
            "<strong>V(dic) + のが [Adjetivo] です:</strong> Convertir un verbo en objeto de gustos/habilidades. Ej. 私は絵を描くのが好きです (Me gusta dibujar cuadros).",
            "<strong>V(dic) + のを 忘れました:</strong> Olvidé hacer X. Ej. 薬を飲むのを忘れました (Olvidé tomar la medicina).",
            "<strong>V(dic/ta) + のを 知っていますか:</strong> ¿Sabías que...? Ej. 木村さんが結婚したのを知っていますか (¿Sabías que Kimura se casó?)."
        ],
        "examples": [
            ("テニスをするのは面白いです。", "1. Jugar al tenis es divertido.", "テニスをするのはおもしろいです"),
            ("日本語を勉強するのは楽しいです。", "2. Estudiar japonés es divertido.", "にほんごをべんきょうするのはたのしいです"),
            ("私は絵を描くのが好きです。", "3. Me gusta dibujar cuadros.", "わたしはえをかくのがすきです"),
            ("私は歩くのが速いです。", "4. Soy rápido para caminar (Caminar es rápido en mí).", "わたしはあるくのがはやいです"),
            ("薬を飲むのを忘れました。", "5. Olvidé tomar la medicina.", "くすりをのむのをわすれました"),
            ("車の窓を閉めるのを忘れました。", "6. Olvidé cerrar la ventana del coche.", "くるまのまどをしめるのをわすれました"),
            ("木村さんが結婚したのを知っていますか。", "7. ¿Sabías que Kimura se casó?", "きむらさんがけっこんしたのをしっていますか"),
            ("あの人が有名な俳優なのを知っていますか。", "8. ¿Sabías que esa persona es un actor famoso? (Para Noun/Na-Adj se usa なの).", "あのひとがゆうめいなはいゆうなのをしっていますか"),
            ("赤ちゃんが泣いているのが聞こえます。", "9. Oigo que el bebé está llorando.", "あかちゃんがないているのがきこえます"),
            ("富士山が見えるのを知っていますか。", "10. ¿Sabías que se puede ver el Monte Fuji?", "ふじさんがみえるのをしっていますか")
        ],
        "exercises": [
            {"q": "¿Qué partícula se usa para nominalizar un verbo (convertirlo en sustantivo)?", "options": [{"text": "の (No)", "correct": True}, {"text": "と (To)", "correct": False}, {"text": "を (Wo)", "correct": False}]},
            {"q": "'Jugar al fútbol es divertido' (Divertido = Tanoshii):", "options": [{"text": "サッカーをするのが楽しいです。", "correct": False}, {"text": "サッカーをするのは楽しいです。", "correct": True}, {"text": "サッカーをするのを楽しいです。", "correct": False}]},
            {"q": "'Me GUSTA (Suki) escuchar música':", "options": [{"text": "音楽を聞くのが好きです。", "correct": True}, {"text": "音楽を聞くのは好きです。", "correct": False}, {"text": "音楽を聞くのを好きです。", "correct": False}]},
            {"q": "¿Qué adjetivos suelen ir con 'のが' (No ga)?", "options": [{"text": "好き (gustar), 嫌い (odiar), 上手 (hábil), 下手 (torpe)", "correct": True}, {"text": "高い (caro), 安い (barato)", "correct": False}, {"text": "大きい (grande), 小さい (pequeño)", "correct": False}]},
            {"q": "'Olvidé comprar leche' (Comprar = Kau):", "options": [{"text": "牛乳を買うのを忘れました。", "correct": True}, {"text": "牛乳を買うのが忘れました。", "correct": False}, {"text": "牛乳を買うのは忘れました。", "correct": False}]},
            {"q": "¿Cómo dices '¿SABÍAS QUE (shitte imasu ka) el profesor vino?' (Venir = Kita - Forma Ta):", "options": [{"text": "先生が来たのを知っていますか。", "correct": True}, {"text": "先生が来るのを知っていますか。", "correct": False}, {"text": "先生が来たのを知りませんか。", "correct": False}]},
            {"q": "Si nominalizas un Sustantivo o Adjetivo Na antes de 'no', ¿qué agregas? (Ej. Famoso = Yuumei)", "options": [{"text": "有名なの (Yuumei na no)", "correct": True}, {"text": "有名だの (Yuumei da no)", "correct": False}, {"text": "有名の (Yuumei no)", "correct": False}]},
            {"q": "'Soy torpe (Heta) cocinando':", "options": [{"text": "私は料理を作るのが下手です。", "correct": True}, {"text": "私は料理を作るのは下手です。", "correct": False}, {"text": "私は料理を作るのを下手です。", "correct": False}]},
            {"q": "'El profesor hablar es rápido' (El profesor habla rápido):", "options": [{"text": "先生は話すのが速いです。", "correct": True}, {"text": "先生は話すのは速いです。", "correct": False}, {"text": "先生は話すのを速いです。", "correct": False}]},
            {"q": "¿Cuál es la respuesta corta correcta a '木村さんが結婚したのを知っていますか' (¿Sabías que Kimura se casó)?", "options": [{"text": "いいえ、知りませんでした。(No, no lo sabía [en el pasado, ahora ya lo sé])", "correct": True}, {"text": "いいえ、知りません。(Incorrecto en este contexto)", "correct": False}, {"text": "はい、知りませんでした。", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "鈴木さんは、休みの日は何をしていますか。", "Suzuki, ¿qué haces en tus días libres?"),
            ("ja-JP-KeitaNeural", "私は本を読むのが好きなので、図書館によく行きます。", "Como me gusta leer libros, voy a menudo a la biblioteca."),
            ("ja-JP-NanamiNeural", "どんな本を読むのが面白いですか。", "¿Qué tipo de libros es divertido leer?"),
            ("ja-JP-KeitaNeural", "歴史の本を読むのはとても面白いですよ。", "Leer libros de historia es muy interesante."),
            ("ja-JP-NanamiNeural", "そうですか。あ、図書館と言えば、本を返すのを忘れていました！", "¿Ah sí? Ah, hablando de bibliotecas... ¡Olvidé devolver un libro!"),
            ("ja-JP-KeitaNeural", "ええっ、いつまでですか。", "¿Eh? ¿Hasta cuándo tenías plazo?"),
            ("ja-JP-NanamiNeural", "昨日まででした。早く返しに行かなければなりません。", "Era hasta ayer. Tengo que ir a devolverlo rápido."),
            ("ja-JP-KeitaNeural", "遅れると電話がかかってくるのを知っていますか。", "¿Sabías que si te retrasas te llaman por teléfono?"),
            ("ja-JP-NanamiNeural", "はい、知っています。急いで行ってきます！", "Sí, lo sé. ¡Iré enseguida!")
        ]
    },
    14: {
        "title": "Causas de emociones con ~て",
        "grammar": [
            "<strong>V(te) / V(nakute) / Adj-i(kute) / Adj-na(de), [Emoción o Situación]:</strong> Expresar la causa de un sentimiento. Ej. ニュースを聞いて、びっくりしました (Me sorprendí al escuchar las noticias).",
            "<strong>Sustantivo + で, [Efecto]:</strong> Causa por un evento incontrolable (terremoto, accidente, enfermedad). Ej. 地震で、ビルが倒れました (El edificio se derrumbó por el terremoto).",
            "<strong>OJO:</strong> No se puede usar la forma ~te para pedir favores, dar órdenes o invitaciones en la segunda parte de la oración. Para eso se usa ~kara."
        ],
        "examples": [
            ("ニュースを聞いて、びっくりしました。", "1. Al escuchar las noticias, me sorprendí.", "ニュースをきいて、びっくりしました"),
            ("家族に会えなくて、寂しいです。", "2. Como no puedo ver a mi familia, me siento solo.", "かぞくにあえなくて、さびしいです"),
            ("テストが難しくて、わかりませんでした。", "3. Como el examen era difícil, no lo entendí.", "テストがむずかしくて、わかりませんでした"),
            ("遅れて、すみません。", "4. Disculpe por llegar tarde (Por llegar tarde, disculpe).", "おくれて、すみません"),
            ("地震で、ビルが倒れました。", "5. El edificio se derrumbó por (culpa de) el terremoto.", "じしんで、ビルがたおれました"),
            ("病気で、会社を休みました。", "6. Falté a la empresa por (culpa de) una enfermedad.", "びょうきで、かいしゃをやすみました"),
            ("事故で、電車が止まっています。", "7. El tren está detenido por (culpa de) un accidente.", "じこで、でんしゃがとまっています"),
            ("話が複雑で、よくわかりませんでした。", "8. Como la historia era compleja (Adj-Na), no la entendí bien.", "はなしがふくざつで、よくわかりませんでした"),
            ("お金がなくて、パソコンが買えません。", "9. Como no tengo dinero, no puedo comprar la computadora.", "おかねがなくて、パソコンがかえません"),
            ("手紙を読んで、安心しました。", "10. Al leer la carta, me tranquilicé.", "てがみをよんで、あんしんしました")
        ],
        "exercises": [
            {"q": "¿Qué función cumple la forma TE en 'ニュースを聞いて、びっくりしました'?", "options": [{"text": "Indica el orden de las acciones (Primero escuché, luego me sorprendí)", "correct": False}, {"text": "Indica la CAUSA de una emoción (Me sorprendí PORQUE escuché...)", "correct": True}, {"text": "Indica una solicitud", "correct": False}]},
            {"q": "'Me siento triste PORQUE no puedo ver a mi amigo' (Aenai = no puedo ver):", "options": [{"text": "友達に会えなくて、悲しいです。", "correct": True}, {"text": "友達に会えないで、悲しいです。", "correct": False}, {"text": "友達に会えなくで、悲しいです。", "correct": False}]},
            {"q": "'Disculpe por llegar tarde' (Okureru = llegar tarde):", "options": [{"text": "遅れて、すみません。", "correct": True}, {"text": "遅れるから、すみません。", "correct": False}, {"text": "遅れるで、すみません。", "correct": False}]},
            {"q": "Para sustantivos como Terremoto (Jishin) o Accidente (Jiko), ¿qué partícula señala la CAUSA?", "options": [{"text": "で (De)", "correct": True}, {"text": "に (Ni)", "correct": False}, {"text": "を (Wo)", "correct": False}]},
            {"q": "'El tren se detuvo POR el tifón' (Taifuu):", "options": [{"text": "台風で、電車が止まりました。", "correct": True}, {"text": "台風に、電車が止まりました。", "correct": False}, {"text": "台風て、電車が止まりました。", "correct": False}]},
            {"q": "¿Se puede usar la forma TE como causa para DAR UNA ORDEN? Ej: 'Como hace frío, cierra la ventana (Abrete kudasai)'.", "options": [{"text": "Sí, siempre.", "correct": False}, {"text": "No, se debe usar から (Kara) o ので (Node).", "correct": True}, {"text": "Solo si es un adjetivo.", "correct": False}]},
            {"q": "'Como la cámara era cara (Takai - Adj-i), no pude comprarla':", "options": [{"text": "カメラが高くて、買えませんでした。", "correct": True}, {"text": "カメラが高くて、買いませんでした。", "correct": False}, {"text": "カメラが高いで、買えませんでした。", "correct": False}]},
            {"q": "'Como mi trabajo es ocupado (Isogashii), no puedo ir a la fiesta':", "options": [{"text": "仕事が忙しくて、パーティーに行けません。", "correct": True}, {"text": "仕事が忙しいで、パーティーに行けません。", "correct": False}, {"text": "仕事が忙しくて、パーティーに行かないで。", "correct": False}]},
            {"q": "¿Cuál es la causa en '病気で会社を休みました'?", "options": [{"text": "El trabajo (Kaisha)", "correct": False}, {"text": "La enfermedad (Byouki)", "correct": True}, {"text": "El descanso (Yasumi)", "correct": False}]},
            {"q": "'Al no entender el japonés, tuve problemas' (Wakaranai):", "options": [{"text": "日本語がわからなくて、困りました。", "correct": True}, {"text": "日本語がわからないで、困りました。", "correct": False}, {"text": "日本語がわからなくて、困ってください。", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-KeitaNeural", "すみません、遅れてしまって。", "Siento mucho haber llegado tarde (por haber llegado tarde, disculpe)."),
            ("ja-JP-NanamiNeural", "どうしたんですか。３０分も遅れましたよ。", "¿Qué pasó? Te has retrasado 30 minutos."),
            ("ja-JP-KeitaNeural", "電車が止まって、遅れました。本当にごめんなさい。", "El tren se detuvo, y por eso llegué tarde. De verdad, lo siento."),
            ("ja-JP-NanamiNeural", "電車が止まったんですか。どうしてですか。", "¿El tren se detuvo? ¿Por qué?"),
            ("ja-JP-KeitaNeural", "駅で事故があって、電車が動きませんでした。", "Hubo un accidente en la estación y el tren no se movía."),
            ("ja-JP-NanamiNeural", "そうでしたか。事故のニュースを聞いて、私も心配していました。", "Ya veo. Al escuchar las noticias del accidente, yo también me preocupé."),
            ("ja-JP-KeitaNeural", "電話したかったんですが、人が多くて、できませんでした。", "Quería llamar, pero como había mucha gente, no pude."),
            ("ja-JP-NanamiNeural", "大丈夫ですよ。無事に着いて、安心しました。", "No pasa nada. Al ver que has llegado sano y salvo, me he tranquilizado.")
        ]
    },
    15: {
        "title": "Interrogativos incrustados (~か / ~かどうか)",
        "grammar": [
            "<strong>Pregunta con interrogativo (いつ, どこ) + か、わかりますか:</strong> Ej. 会議がいつ終わるか、わかりません (No sé cuándo terminará la reunión).",
            "<strong>Pregunta Sí/No (sin interrogativo) + かどうか、知っていますか:</strong> Ej. 山田さんが来るかどうか、知っていますか (¿Sabes si Yamada vendrá o no?).",
            "<strong>V(te) みます:</strong> Intentar hacer algo para probar o ver qué pasa. Ej. サイズが合うかどうか、着てみます (Me lo probaré a ver si la talla es correcta)."
        ],
        "examples": [
            ("会議がいつ終わるか、わかりません。", "1. No sé cuándo terminará la reunión.", "かいぎがいつおわるか、わかりません"),
            ("箱の中に何が入っているか、調べてください。", "2. Por favor, investigue qué hay dentro de la caja.", "はこのなかになにが入っているか、しらべてください"),
            ("どこでチケットを買うか、教えてください。", "3. Por favor enséñeme dónde comprar el billete.", "どこでチケットをかうか、おしえてください"),
            ("あの人が誰か、知っていますか。", "4. ¿Sabes quién es esa persona?", "あのひとがだれか、しっていますか"),
            ("山田さんが来るかどうか、わかりません。", "5. No sé si el Sr. Yamada vendrá o no.", "やまださんがくるかどうか、わかりません"),
            ("その話が本当かどうか、調べてみます。", "6. Investigaré (intentaré investigar) si esa historia es verdad o no.", "そのはなしがほんとうかどうか、しらべてみます"),
            ("サイズが合うかどうか、着てみます。", "7. Me lo probaré (intentaré ponérmelo) para ver si la talla me queda o no.", "サイズがあうかどうか、きてみます"),
            ("このお酒が美味しいかどうか、飲んでみます。", "8. Beberé este alcohol (lo probaré) a ver si está rico o no.", "このおさけがおいしいかどうか、のんでみます"),
            ("新しい靴を履いてみます。", "9. Me probaré los zapatos nuevos.", "あたらしいくつをはいてみます"),
            ("どうして遅れたか、理由を言ってください。", "10. Por favor, di la razón de por qué llegaste tarde.", "どうしておくれたか、りゆうをいってください")
        ],
        "exercises": [
            {"q": "Si la oración ya tiene un pronombre interrogativo (Cuándo, Quién, Dónde), ¿qué se añade al final de la cláusula?", "options": [{"text": "か (Ka)", "correct": True}, {"text": "かどうか (Ka dou ka)", "correct": False}, {"text": "ので (Node)", "correct": False}]},
            {"q": "'Por favor, enséñame CUÁNDO (itsu) empieza la película':", "options": [{"text": "映画がいつ始まるか、教えてください。", "correct": True}, {"text": "映画がいつ始まるかどうか、教えてください。", "correct": False}, {"text": "映画がいつ始まるの、教えてください。", "correct": False}]},
            {"q": "Si la oración NO tiene un interrogativo (es de Sí/No), ¿qué se añade? Ej. 'No sé SI lloverá':", "options": [{"text": "か (Ka)", "correct": False}, {"text": "かどうか (Ka dou ka)", "correct": True}, {"text": "なら (Nara)", "correct": False}]},
            {"q": "'No sé SI el Sr. Tanaka vendrá (Kuru) o no':", "options": [{"text": "田中さんが来るかどうか、わかりません。", "correct": True}, {"text": "田中さんが来るか、わかりません。", "correct": False}, {"text": "田中さんが来るなどうか、わかりません。", "correct": False}]},
            {"q": "¿Qué significa la forma ~て みます (Te mimasu)?", "options": [{"text": "Terminar algo completamente", "correct": False}, {"text": "Mirar algo con atención", "correct": False}, {"text": "Intentar/probar hacer algo para ver cómo es", "correct": True}]},
            {"q": "'Me probaré este pantalón' (Haku = ponerse pantalones):", "options": [{"text": "このズボンを履いてみます。", "correct": True}, {"text": "このズボンを履いておきます。", "correct": False}, {"text": "このズボンを履いてしまいます。", "correct": False}]},
            {"q": "'A ver si está delicioso O NO, lo probaré (comeré)' (Oishii):", "options": [{"text": "美味しいかどうか、食べてみます。", "correct": True}, {"text": "美味しいか、食べてみます。", "correct": False}, {"text": "美味しいかどうか、食べてしまいます。", "correct": False}]},
            {"q": "¿Cómo se conecta un Sustantivo con 'ka dou ka'? Ej. 'No sé si es un estudiante (Gakusei) o no':", "options": [{"text": "学生だかどうか、わかりません。", "correct": False}, {"text": "学生かどうか、わかりません。(Se omite el 'da')", "correct": True}, {"text": "学生なのかどうか、わかりません。", "correct": False}]},
            {"q": "'Averiguaré (Shirabete mimasu) DÓNDE (doko) está la llave':", "options": [{"text": "鍵がどこにあるか、調べてみます。", "correct": True}, {"text": "鍵がどこにあるかどうか、調べてみます。", "correct": False}, {"text": "鍵がどこにあるのかどうか、調べてみます。", "correct": False}]},
            {"q": "¿Cuál es la traducción de 'このケーキを食べてみてください'?", "options": [{"text": "Por favor, cómete todo el pastel.", "correct": False}, {"text": "Por favor, prueba (intenta comer) este pastel.", "correct": True}, {"text": "Por favor, mira este pastel y cómetelo.", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "明日のパーティーに誰が来るか、知っていますか。", "¿Sabes quién vendrá a la fiesta de mañana?"),
            ("ja-JP-KeitaNeural", "いいえ、田中さんが来るかどうかはわかりませんが、鈴木さんは来ますよ。", "No, no sé si Tanaka vendrá o no, pero Suzuki sí vendrá."),
            ("ja-JP-NanamiNeural", "パーティーは何時から始まるか、教えてください。", "Dime a qué hora empieza la fiesta, por favor."),
            ("ja-JP-KeitaNeural", "午後６時からです。料理が足りるかどうか、心配ですね。", "Es desde las 6 de la tarde. Me preocupa si la comida será suficiente o no."),
            ("ja-JP-NanamiNeural", "大丈夫です。私が新しいケーキを焼いてみました。", "No hay problema. He probado a hornear un pastel nuevo."),
            ("ja-JP-KeitaNeural", "へえ、美味しいかどうか、食べてみてもいいですか。", "Vaya, ¿puedo probar a comerlo a ver si está rico o no?"),
            ("ja-JP-NanamiNeural", "はい、どうぞ。甘すぎないかどうか、チェックしてください。", "Sí, adelante. Revisa si no está demasiado dulce o no."),
            ("ja-JP-KeitaNeural", "うん、とても美味しいです！これならみんな喜ぶかどうかわかりますよ、絶対に喜びます！", "Mmm, ¡está muy rico! Con esto sé si todos se alegrarán o no, ¡seguro que se alegrarán!")
        ]
    }
}

base_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\lessons"
audio_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\audio"
os.makedirs(audio_dir, exist_ok=True)

# Generate HTML and Audio for 11-15
for i in range(11, 16):
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
for i in range(11, 16):
    title = data[i]["title"]
    links_html += f'''                        <a href="lessons/jlpt-n4-{i}.html" target="main_frame" class="nav-link">
                            <span class="nav-num">{i}</span> {title}
                        </a>\n'''

target = '                            <span class="nav-num">10</span> Condicional (~ば)\n                        </a>\n'
if target in content:
    new_content = content.replace(target, target + links_html)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Updated index.html")

print("Running add_furigana.py...")
subprocess.run("python add_furigana.py", shell=True)
print("ALL TASKS COMPLETED!")
