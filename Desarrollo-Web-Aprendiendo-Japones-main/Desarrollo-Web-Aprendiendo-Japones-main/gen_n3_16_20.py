import os
import subprocess

data = {
    16: {
        "title": "Limitaciones y Énfasis (~に限る / ~ばかり / ~のみ)",
        "grammar": [
            "<strong>N + に限る (Ni kagiru):</strong> 'No hay nada como...' o 'Lo mejor es...'. Expresa la opinión subjetiva del hablante de que algo es lo mejor o ideal. Ej. 夏はビールに限る (En verano, no hay nada como la cerveza).",
            "<strong>N / V(te) + ばかり (Bakari):</strong> 'Solamente / Nada más que'. Expresa que se hace algo repetidamente o solo hay una cosa, a menudo con una connotación ligeramente negativa. Ej. 肉ばかり食べている (No come nada más que carne).",
            "<strong>N + のみ (Nomi):</strong> 'Solamente'. Equivalente formal o escrito de 'だけ'. Ej. 経験者のみ募集 (Se busca solamente gente con experiencia)."
        ],
        "examples": [
            ("疲れたときは、お風呂に入って寝るに限る。", "1. Cuando estás cansado, no hay nada como darse un baño y dormir.", "つかれたときは、おふろにはいってねるにかぎる"),
            ("風邪を引いたときは、温かいスープに限ります。", "2. Cuando tienes un resfriado, lo mejor es una sopa caliente.", "かぜをひいたときは、あたたかいスープにかぎります"),
            ("うちの子は、毎日ゲームばかりしている。", "3. Mi hijo no hace más que jugar videojuegos todos los días.", "うちのこは、まいにちゲームばかりしている"),
            ("彼女は文句ばかり言っている。", "4. Ella no hace más que quejarse (decir quejas).", "かのじょはもんくばかりいっている"),
            ("野菜を食べないで、肉ばかり食べてはだめですよ。", "5. No debes comer solo carne sin comer verduras.", "やさいをたべないで、にくばかりたべてはだめですよ"),
            ("このチケットは、本日のみ有効です。", "6. Este boleto es válido solamente por el día de hoy (Formal).", "このチケットは、ほんじつのみゆうこうです"),
            ("会員のみ入場できます。", "7. Solamente los miembros pueden ingresar.", "かいいんのみにゅうじょうできます"),
            ("休みの日は、家でゴロゴロするに限るね。", "8. En los días libres, no hay nada como holgazanear en casa.", "やすみのひは、いえでゴロゴロするにかぎるね"),
            ("甘いものばかり食べると、太りますよ。", "9. Si comes solamente cosas dulces, engordarás.", "あまいものばかりたべると、ふとりますよ"),
            ("カード払いは不可。現金のみとなります。", "10. No se puede pagar con tarjeta. Solamente efectivo.", "カードばらいはふか。げんきんのみとなります")
        ],
        "exercises": [
            {"q": "¿Qué expresión se usa para dar tu fuerte opinión personal de que 'eso es lo mejor / no hay nada como eso'?", "options": [{"text": "～に限る (ni kagiru)", "correct": True}, {"text": "～ばかり (bakari)", "correct": False}, {"text": "～のみ (nomi)", "correct": False}]},
            {"q": "¿Qué expresión enfatiza que se repite la misma acción o se consume la misma cosa constantemente, a veces con tono de queja?", "options": [{"text": "～ばかり (bakari)", "correct": True}, {"text": "～に限る (ni kagiru)", "correct": False}, {"text": "～のみ (nomi)", "correct": False}]},
            {"q": "¿Cuál es la versión formal/escrita de だけ (dake) usada en carteles o avisos?", "options": [{"text": "～のみ (nomi)", "correct": True}, {"text": "～ばかり (bakari)", "correct": False}, {"text": "～に限る (ni kagiru)", "correct": False}]},
            {"q": "'En invierno, no hay nada como el Nabe (estofado japonés)':", "options": [{"text": "冬は鍋に限る", "correct": True}, {"text": "冬は鍋ばかり", "correct": False}, {"text": "冬は鍋のみ", "correct": False}]},
            {"q": "'Está llorando todo el tiempo (solamente llorando)' (Naku -> Naite):", "options": [{"text": "泣いてばかりいる", "correct": True}, {"text": "泣いてのみいる", "correct": False}, {"text": "泣いて限るいる", "correct": False}]},
            {"q": "'Solo aceptamos estudiantes universitarios' (Formal / Cartel): 大学生___募集。", "options": [{"text": "のみ", "correct": True}, {"text": "ばかり", "correct": False}, {"text": "に限る", "correct": False}]},
            {"q": "A: '¿Por qué estás enojado?' B: 'Porque mi novio no hace más que jugar con el móvil'. (Asobu -> Asonde)", "options": [{"text": "スマホで遊んでばかりいるから", "correct": True}, {"text": "スマホで遊んでのみいるから", "correct": False}, {"text": "スマホで遊んでに限るから", "correct": False}]},
            {"q": "'Para aliviar el estrés, lo mejor es el karaoke' (Sutoresu kaishou ni wa...):", "options": [{"text": "カラオケに限る", "correct": True}, {"text": "カラオケばかり", "correct": False}, {"text": "カラオケのみ", "correct": False}]},
            {"q": "Gramática: ¿Cómo se conecta un verbo con ばかり (Bakari) cuando es una acción continua?", "options": [{"text": "Verbo forma TE + ばかり + いる", "correct": True}, {"text": "Verbo diccionario + ばかり", "correct": False}, {"text": "Verbo TA + ばかり + いる", "correct": False}]},
            {"q": "'No hay más que mujeres en este departamento' (Mujeres = Onna no hito):", "options": [{"text": "女の人ばかりだ", "correct": True}, {"text": "女の人のみだ", "correct": False}, {"text": "女の人に限るだ", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "ああ、今日も本当に暑いですね。", "Ah, hoy hace mucho calor también, ¿verdad?"),
            ("ja-JP-KeitaNeural", "そうですね。こんな暑い日は、冷たいビールに限りますよ！", "Sí. ¡En un día tan caluroso como este, no hay nada como una cerveza fría!"),
            ("ja-JP-NanamiNeural", "ふふ、お酒が好きですね。でも、お酒ばかり飲んでいると体を壊しますよ。", "Jeje, te gusta el alcohol, ¿eh? Pero si no haces más que beber alcohol, arruinarás tu cuerpo."),
            ("ja-JP-KeitaNeural", "わかっています。だから、週末のみ飲むことにしているんです。", "Lo sé. Por eso he decidido beber solamente los fines de semana (Formal/Enfático)."),
            ("ja-JP-NanamiNeural", "本当ですか？昨日も飲んでいたと聞きましたけど...。", "¿De verdad? Pero escuché que ayer también estabas bebiendo..."),
            ("ja-JP-KeitaNeural", "あ、昨日は特別です。友達の誕生日だったから...。", "Ah, ayer fue una excepción. Porque era el cumpleaños de un amigo..."),
            ("ja-JP-NanamiNeural", "言い訳ばかりですね！", "¡No haces más que poner excusas!")
        ]
    },
    17: {
        "title": "Información y Rumores (~ということだ / ~とのことだ)",
        "grammar": [
            "<strong>~ということだ (To iu koto da):</strong> 'Significa que...' o 'He oído que...'. Sirve para resumir/explicar el significado de algo, o para transmitir un rumor o información obtenida de otra fuente.",
            "<strong>~とのことだ (To no koto da):</strong> 'Me dicen que... / Según informan...'. Es una forma formal de transmitir un mensaje directo de una persona a otra, muy usada en los negocios.",
            "<strong>~みたいだ (Mitai da):</strong> 'Parece que...'. Se usa para expresar una suposición basada en lo que uno ve u oye, o un rumor ligero (informal)."
        ],
        "examples": [
            ("ニュースによると、明日は雪が降るということだ。", "1. Según las noticias, se dice que mañana nevará.", "ニュースによると、あしたはゆきがふるということだ"),
            ("ご意見がないということは、賛成ということですね。", "2. Que no haya opiniones significa que están a favor, ¿verdad?", "ごいけんがないということは、さんせいということですね"),
            ("社長は午後から出社するとのことです。", "3. (Mensaje formal) Me informan que el presidente llegará a la oficina por la tarde.", "しゃちょうはごごからしゅっしゃするととのことです"),
            ("山田さんから電話があり、少し遅れるとのことです。", "4. Hubo una llamada de Yamada y dice que se retrasará un poco.", "やまださんからでんわがあり、すこしおくれるとのことです"),
            ("禁煙ということは、ここでタバコを吸ってはいけないということです。", "5. 'Kinen' significa que no se debe fumar aquí.", "きんえんということは、ここでタバコをすってはいけないということです"),
            ("物価が上がるということは、生活が苦しくなるということだ。", "6. Que los precios suban significa que la vida se volverá más difícil.", "ぶっかが上がるということは、せいかつがくるしくなるということだ"),
            ("彼と連絡が取れない。事故にでも遭ったみたいだ。", "7. No puedo contactar con él. Parece que hubiera tenido un accidente.", "かれとれんらくがとれない。じこにでもあったみたいだ"),
            ("隣の部屋が騒がしい。パーティーをしているみたいだ。", "8. La habitación de al lado está ruidosa. Parece que están haciendo una fiesta.", "となりのへやがさわがしい。パーティーをしているみたいだ"),
            ("メールによると、明日の会議は中止とのことです。", "9. Según el correo, me informan que la reunión de mañana se cancela.", "メールによると、あしたのかいぎはちゅうしとのことです"),
            ("新しい先生は、とても厳しいということだ。", "10. He oído (rumor) que el nuevo profesor es muy estricto.", "あたらしいせんせいは、とてもきびしいということだ")
        ],
        "exercises": [
            {"q": "¿Qué expresión se usa en los NEGOCIOS para retransmitir un mensaje que alguien te dejó? (Ej. Yamada me llamó para decir...)", "options": [{"text": "～とのことだ", "correct": True}, {"text": "～ということだ", "correct": False}, {"text": "～みたいだ", "correct": False}]},
            {"q": "¿Qué expresión tiene dos usos principales: 'He oído que...' (rumor formal) y 'Significa que...' (explicación)?", "options": [{"text": "～ということだ", "correct": True}, {"text": "～とのことだ", "correct": False}, {"text": "～みたいだ", "correct": False}]},
            {"q": "¿Qué expresión es más coloquial y sirve para decir 'Parece que...' basándote en la evidencia visual o auditiva?", "options": [{"text": "～みたいだ", "correct": True}, {"text": "～ということだ", "correct": False}, {"text": "～とのことだ", "correct": False}]},
            {"q": "'El cliente me dijo por teléfono que llegará a las 3' (Formal, transmitiendo el mensaje a tu jefe):", "options": [{"text": "３時に到着するとのことです", "correct": True}, {"text": "３時に到着するみたいです", "correct": False}, {"text": "３時に到着するはずです", "correct": False}]},
            {"q": "'(Yo interpreto que) Su silencio significa que está enfadado' (Okotte iru):", "options": [{"text": "怒っているということだ", "correct": True}, {"text": "怒っているとのことだ", "correct": False}, {"text": "怒っているみたいだ", "correct": False}]},
            {"q": "'Las luces están apagadas. Parece que no hay nadie' (Inai):", "options": [{"text": "誰もいないみたいだ", "correct": True}, {"text": "誰もいないということだ", "correct": False}, {"text": "誰もいないとのことだ", "correct": False}]},
            {"q": "'Según el periódico, la economía mejorará' (Rumor/Noticia formal): 経済がよくなる___。", "options": [{"text": "ということだ", "correct": True}, {"text": "とのことだ", "correct": False}, {"text": "みたいだ", "correct": False}]},
            {"q": "A: 'Este kanji dice 'Tachiiri kinshi''. B: '¿Qué significa eso?'. A: 'Significa que no puedes entrar'.", "options": [{"text": "入ってはいけないということです", "correct": True}, {"text": "入ってはいけないとのことです", "correct": False}, {"text": "入ってはいけないみたいです", "correct": False}]},
            {"q": "Si un colega te deja un mensaje para el gerente: 'Dígale que el informe está listo'. ¿Qué usas al hablar con el gerente?", "options": [{"text": "レポートができたとのことです", "correct": True}, {"text": "レポートができたみたいです", "correct": False}, {"text": "レポートができたはずです", "correct": False}]},
            {"q": "'Aquel restaurante siempre tiene fila. Parece que es delicioso' (Oishii):", "options": [{"text": "美味しいみたいだ", "correct": True}, {"text": "美味しいとのことだ", "correct": False}, {"text": "美味しいということだ", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "あ、佐藤さん。さっき山田さんから電話がありましたよ。", "Ah, Sato. Hubo una llamada de Yamada hace un momento."),
            ("ja-JP-KeitaNeural", "本当ですか？何と言っていましたか。", "¿En serio? ¿Qué dijo?"),
            ("ja-JP-NanamiNeural", "電車が遅れているので、３０分ほど遅刻するとのことです。", "Dice (me informó) que como el tren está retrasado, llegará unos 30 minutos tarde."),
            ("ja-JP-KeitaNeural", "わかりました。最近、あの路線はよく遅れるみたいですね。", "Entendido. Parece que esa línea ferroviaria se retrasa a menudo últimamente, ¿verdad?"),
            ("ja-JP-NanamiNeural", "ええ、ニュースによると、工事をしているということですよ。", "Sí, según las noticias (he oído que), están haciendo obras de construcción."),
            ("ja-JP-KeitaNeural", "なるほど。じゃあ、今日の会議は山田さん抜きで始めましょう。", "Ya veo. Entonces, comencemos la reunión de hoy sin Yamada."),
            ("ja-JP-NanamiNeural", "山田さんがいなくても進めるということですね。わかりました。", "¿Eso significa que avanzaremos aunque no esté Yamada? Entendido.")
        ]
    },
    18: {
        "title": "Exclusión y Conclusión (~抜きで / ~はもちろん)",
        "grammar": [
            "<strong>N + 抜きで / 抜きにして (Nuki de):</strong> 'Sin... / Dejando fuera...'. Significa omitir algo que normalmente estaría incluido. Ej. わさび抜きでお願いします (Sin wasabi, por favor).",
            "<strong>N + はもちろん:</strong> 'N por supuesto (pero también...)'. Expresa que algo es obvio, pero se añade más información sorprendente o adicional. Ej. 彼は英語はもちろん、フランス語も話せる (Él habla inglés por supuesto, pero también francés).",
            "<strong>V(dic) + わけにはいかない:</strong> 'No puedo (por razones morales o sociales)'. No es incapacidad física, sino responsabilidad. Ej. 休むわけにはいかない (No puedo faltar [porque soy el líder])."
        ],
        "examples": [
            ("冗談抜きで、真面目に話しましょう。", "1. Dejando las bromas fuera (sin bromas), hablemos en serio.", "じょうだんぬきで、まじめにはなしましょう"),
            ("子供用なので、わさび抜きでお寿司を作ってください。", "2. Como es para un niño, por favor prepare el sushi sin wasabi.", "こどもようなので、わさびぬきでおすしをつくってください"),
            ("彼女は顔が綺麗なのはもちろん、性格も素晴らしい。", "3. Ella es hermosa de cara por supuesto, pero además su personalidad es maravillosa.", "かのじょはかおがきれいなのはもちろん、せいかくもすばらしい"),
            ("このレストランは、休日はもちろん、平日も混んでいる。", "4. Este restaurante, por supuesto los fines de semana, pero los días de semana también está lleno.", "このレストランは、きゅうじつはもちろん、へいじつもこんでいる"),
            ("社長抜きでこの会議を始めるわけにはいかない。", "5. No podemos (no debemos) empezar esta reunión sin el presidente.", "しゃちょうぬきでこのかいぎをはじめるわけにはいかない"),
            ("明日は大切なテストがあるので、遊んでいるわけにはいかない。", "6. Mañana tengo un examen importante, así que no puedo darme el lujo de estar jugando.", "あしたはたいせつなテストがあるので、あそんでいるわけにはいかない"),
            ("あの映画は、映像はもちろん、音楽も感動的だ。", "7. Esa película, la imagen por supuesto, pero la música también es conmovedora.", "あのえいがは、えいぞうはもちろん、おんがくもかんどうてきだ"),
            ("玉ねぎ抜きでハンバーガーを注文した。", "8. Pedí una hamburguesa sin cebolla.", "たまねぎぬきでハンバーガーをちゅうもんした"),
            ("みんなが働いているのに、私だけ帰るわけにはいかない。", "9. A pesar de que todos están trabajando, no puedo irme yo solo (me siento mal si lo hago).", "みんながはたらいているのに、わたしだけかえるわけにはいかない"),
            ("挨拶抜きで、すぐに本題に入りましょう。", "10. Sin saludos (omitamos la introducción), vayamos directo al grano.", "あいさつぬきで、すぐにほんだいにはいりましょう")
        ],
        "exercises": [
            {"q": "¿Qué sufijo se usa con un sustantivo para pedir que se 'omita' algo (como en la comida o en una reunión)?", "options": [{"text": "～抜きで (Nuki de)", "correct": True}, {"text": "～はもちろん", "correct": False}, {"text": "～わけにはいかない", "correct": False}]},
            {"q": "¿Qué expresión significa '... por supuesto (es obvio), pero además...'?", "options": [{"text": "～はもちろん", "correct": True}, {"text": "～抜きで", "correct": False}, {"text": "～わけにはいかない", "correct": False}]},
            {"q": "¿Qué expresión significa 'No puedo hacerlo' pero por motivos de RESPONSABILIDAD social, moral o psicológica (no física)?", "options": [{"text": "～わけにはいかない", "correct": True}, {"text": "～できない", "correct": False}, {"text": "～抜きで", "correct": False}]},
            {"q": "'Hamburguesa SIN tomate, por favor' (Tomato):", "options": [{"text": "トマト抜きでお願いします", "correct": True}, {"text": "トマトはもちろんお願いします", "correct": False}, {"text": "トマトないでお願いします", "correct": False}]},
            {"q": "'Él sabe jugar béisbol por supuesto, pero también fútbol' (Yakyuu):", "options": [{"text": "野球はもちろん、サッカーもできる", "correct": True}, {"text": "野球抜きで、サッカーもできる", "correct": False}, {"text": "野球ばかり、サッカーもできる", "correct": False}]},
            {"q": "'Soy el líder del proyecto, así que NO PUEDO rendirme' (Akirameru):", "options": [{"text": "あきらめるわけにはいかない", "correct": True}, {"text": "あきらめることはできない", "correct": False}, {"text": "あきらめないわけにはいかない", "correct": False}]},
            {"q": "A: '¿Empezamos la fiesta?' B: '¡No podemos empezar SIN Tanaka!'", "options": [{"text": "田中さん抜きで始めるわけにはいかない", "correct": True}, {"text": "田中さんはもちろん始めるわけにはいかない", "correct": False}, {"text": "田中さんに限って始めるわけにはいかない", "correct": False}]},
            {"q": "'Este libro es útil para los estudiantes por supuesto, pero también para los adultos' (Gakusei):", "options": [{"text": "学生はもちろん、大人にも役に立つ", "correct": True}, {"text": "学生抜きで、大人にも役に立つ", "correct": False}, {"text": "学生のみ、大人にも役に立つ", "correct": False}]},
            {"q": "En un ambiente de negocios serio: 'Dejemos las bromas fuera y hablemos' (Joudan):", "options": [{"text": "冗談抜きで", "correct": True}, {"text": "冗談はもちろん", "correct": False}, {"text": "冗談ばかりで", "correct": False}]},
            {"q": "'He prometido que iré, así que NO PUEDO faltar (休む)'", "options": [{"text": "休むわけにはいかない", "correct": True}, {"text": "休むべきではない", "correct": False}, {"text": "休むはずがない", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-KeitaNeural", "いらっしゃいませ。ご注文はお決まりですか。", "Bienvenido. ¿Ya ha decidido su pedido?"),
            ("ja-JP-NanamiNeural", "はい、このチーズバーガーのセットをお願いします。あ、玉ねぎ抜きでできますか？", "Sí, este combo de hamburguesa con queso, por favor. Ah, ¿se puede hacer sin cebolla?"),
            ("ja-JP-KeitaNeural", "玉ねぎ抜きですね。かしこまりました。お飲み物はいかがですか。", "Sin cebolla, ¿verdad? Entendido. ¿Qué desea de beber?"),
            ("ja-JP-NanamiNeural", "コーラをお願いします。", "Una cola, por favor."),
            ("ja-JP-KeitaNeural", "（数分後）お待たせいたしました。チーズバーガーセット、玉ねぎ抜きです。", "(Unos minutos después) Gracias por esperar. Combo de hamburguesa con queso, sin cebolla."),
            ("ja-JP-NanamiNeural", "ありがとうございます。ここのハンバーガーは、味はもちろん、ボリュームもあって好きなんです。", "Gracias. Las hamburguesas de aquí, el sabor por supuesto, pero además tienen buen tamaño, por eso me gustan."),
            ("ja-JP-KeitaNeural", "ありがとうございます。午後も仕事があるので、しっかり食べておかないというわけにはいかないですね！", "Muchas gracias. ¡Como tiene trabajo por la tarde, no puede darse el lujo de no comer bien!")
        ]
    },
    19: {
        "title": "Decisión y Firmeza (~からには / ~以上は)",
        "grammar": [
            "<strong>V(dic/ta) + からには (Kara ni wa):</strong> 'Ya que... / Puesto que...'. Indica una fuerte determinación, obligación o conclusión natural. Ej. やるからには、最後までやりたい (Ya que lo voy a hacer, quiero hacerlo hasta el final).",
            "<strong>V(dic/ta) + 以上は (Ijou wa):</strong> 'Dado que... / Puesto que...'. Muy similar a 'kara ni wa', un poco más formal. Ej. 約束した以上は、守らなければならない (Dado que lo prometí, debo cumplirlo).",
            "<strong>V(て) + はたまらない (Te wa tamaranai):</strong> 'Es insoportable / No puedo soportar...'. Expresa un sentimiento o sensación extrema (negativa o positiva). Ej. 暑くてたまらない (Hace un calor insoportable)."
        ],
        "examples": [
            ("日本に留学するからには、日本語をペラペラになりたい。", "1. Ya que voy a estudiar en Japón, quiero volverme fluido en japonés.", "にほんにりゅうがくするからには、にほんごをペラペラになりたい"),
            ("社長になった以上は、会社の責任を負わなければならない。", "2. Dado que me he convertido en presidente, debo asumir la responsabilidad de la empresa.", "しゃちょうになったいじょうは、かいしゃのせきにんをおわなければならない"),
            ("試合に出るからには、絶対に勝ちたいです。", "3. Ya que voy a participar en el partido, absolutamente quiero ganar.", "しあいに出るからには、ぜったいにかちたいです"),
            ("引き受けた以上は、ちゃんとやりますよ。", "4. Puesto que he acept0ado el trabajo, lo haré correctamente.", "ひきうけたいじょうは、ちゃんとやりますよ"),
            ("高いお金を払って買うからには、いいものが欲しい。", "5. Ya que voy a pagar mucho dinero para comprarlo, quiero algo bueno.", "たかいおかねをはらってかうからには、いいものがほしい"),
            ("最近、忙しすぎて疲れてたまらない。", "6. Últimamente, estoy demasiado ocupado y estoy cansado a más no poder.", "さいきん、いそがしすぎてつかれてたまらない"),
            ("隣の部屋の音楽がうるさくてたまらない。", "7. La música de la habitación de al lado es insoportablemente ruidosa.", "となりのへやのおんがくがうるさくてたまらない"),
            ("プロである以上は、ミスは許されない。", "8. Dado que eres un profesional (sustantivo + de aru), no se permiten errores.", "プロであるいじょうは、ミスはゆるされない"),
            ("自分で決めたからには、文句を言ってはいけない。", "9. Ya que lo decidiste tú mismo, no debes quejarte.", "じぶできめたからには、もんくをいってはいけない"),
            ("新しいゲームが欲しくてたまらない。", "10. Quiero el nuevo videojuego tanto que es insoportable (lo deseo muchísimo).", "あたらしいゲームがほしくてたまらない")
        ],
        "exercises": [
            {"q": "¿Qué dos expresiones significan 'Ya que... / Dado que...' y muestran una fuerte determinación u obligación de cumplir algo?", "options": [{"text": "～からには / ～以上は", "correct": True}, {"text": "～抜きで / ～はもちろん", "correct": False}, {"text": "～おかげで / ～せいで", "correct": False}]},
            {"q": "¿Qué expresión significa 'Es insoportablemente...' o 'Tengo tantas ganas de... que no lo soporto'?", "options": [{"text": "～て(は)たまらない", "correct": True}, {"text": "～からには", "correct": False}, {"text": "～以上は", "correct": False}]},
            {"q": "'Ya que voy a hacerlo, quiero ser el número 1' (Yaru):", "options": [{"text": "やるからには", "correct": True}, {"text": "やる以上は", "correct": False}, {"text": "Ambas son correctas", "correct": True}]},
            {"q": "'Dado que lo prometí, debo cumplirlo' (Yakusoku shita):", "options": [{"text": "約束した以上は", "correct": True}, {"text": "約束した抜きで", "correct": False}, {"text": "約束したたまらない", "correct": False}]},
            {"q": "'Hace tanto frío que es insoportable' (Samukute):", "options": [{"text": "寒くてたまらない", "correct": True}, {"text": "寒いからには", "correct": False}, {"text": "寒い以上は", "correct": False}]},
            {"q": "Para usar un sustantivo con 'Ijou wa' (Ej. Estudiante -> Gakusei):", "options": [{"text": "学生である以上は", "correct": True}, {"text": "学生の以上は", "correct": False}, {"text": "学生以上は", "correct": False}]},
            {"q": "'Estoy tan preocupado por el resultado del examen que no lo soporto' (Shinpai de):", "options": [{"text": "心配でたまらない", "correct": True}, {"text": "心配なからには", "correct": False}, {"text": "心配な以上は", "correct": False}]},
            {"q": "'Ya que pagué dinero, voy a comer todo lo que pueda' (Okane o haratta):", "options": [{"text": "お金を払ったからには", "correct": True}, {"text": "お金を払った抜きで", "correct": False}, {"text": "お金を払ったたまらない", "correct": False}]},
            {"q": "'Quiero ver a mi novia tanto que no lo soporto' (Aitakute):", "options": [{"text": "会いたくてたまらない", "correct": True}, {"text": "会いたいからには", "correct": False}, {"text": "会う以上は", "correct": False}]},
            {"q": "¿Cuál es el matiz principal detrás de '~からには' y '~以上は'?", "options": [{"text": "Expresan que es el deber, responsabilidad o fuerte voluntad del hablante actuar de cierta manera", "correct": True}, {"text": "Expresan una excusa o razón para no hacer algo", "correct": False}, {"text": "Expresan arrepentimiento por haberlo hecho", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "田中さん、今度のスピーチコンテストに出るそうですね。", "Tanaka, escuché que vas a participar en el concurso de oratoria de esta vez."),
            ("ja-JP-KeitaNeural", "はい、そうなんです。でも、みんなの前で話すと思うと、緊張してたまらないですよ。", "Sí, así es. Pero cuando pienso en hablar frente a todos, me pongo insoportablemente nervioso."),
            ("ja-JP-NanamiNeural", "大丈夫ですよ。田中さんならきっと上手くできます。", "Estarás bien. Si eres tú, seguro que lo haces bien."),
            ("ja-JP-KeitaNeural", "ありがとうございます。参加すると決めたからには、一生懸命練習します！", "Gracias. ¡Ya que decidí participar, practicaré con todas mis fuerzas!"),
            ("ja-JP-NanamiNeural", "その意気ですね。引き受けた以上は、最後まで諦めないでくださいね。", "Ese es el espíritu. Dado que lo has aceptado, no te rindas hasta el final."),
            ("ja-JP-KeitaNeural", "はい。優勝して、賞金のハワイ旅行に行きたくてたまらないんです！", "Sí. ¡Quiero ganar y ganar el viaje a Hawái del premio tanto que no lo soporto!"),
            ("ja-JP-NanamiNeural", "ふふ、そういうことですか。頑張って！", "Jeje, con que era eso. ¡Esfuérzate!")
        ]
    },
    20: {
        "title": "Probabilidades y Riesgos (~おそれがある / ~かねない)",
        "grammar": [
            "<strong>V(dic/nai)/Nの + おそれがある (Osore ga aru):</strong> 'Hay riesgo de... / Temo que...'. Es una expresión formal usada en noticias, pronósticos del tiempo o advertencias formales. Ej. 大雨のおそれがあります (Hay riesgo de lluvias fuertes).",
            "<strong>V(masu base) + かねない (Kanenai):</strong> 'Es muy posible que (haga algo malo) / Existe el peligro de que...'. Se usa para juzgar que alguien podría causar un mal resultado por su comportamiento. Ej. 彼は秘密を漏らしかねない (Existe el peligro de que él filtre el secreto).",
            "<strong>V(masu base) + 得る / 得ない (Eru/Uru / Enai):</strong> 'Es posible / No es posible' lógicamente (no se usa para habilidad personal). Ej. あり得る (Es posible/Puede ser), あり得ない (¡Es imposible/Absurdo!)."
        ],
        "examples": [
            ("明日は台風が来るおそれがあります。", "1. Hay riesgo de que el tifón venga mañana (Pronóstico).", "あしたはたいふうがくるおそれがあります"),
            ("この病気は、他の人にうつるおそれがある。", "2. Esta enfermedad tiene el riesgo de contagiarse a otras personas.", "このびょうきは、ほかのひとにうつるおそれがある"),
            ("スピードを出しすぎると、事故を起こしかねない。", "3. Si vas a demasiada velocidad, podrías causar un accidente (Hay un gran peligro de que lo hagas).", "スピードをだしすぎると、じこをおこしかねない"),
            ("あの人なら、平気で嘘をつきかねない。", "4. Si es esa persona, existe el peligro de que diga mentiras sin importarle.", "あのひとなら、へいきでうそをつきかねない"),
            ("働きすぎると、過労で倒れかねませんよ。", "5. Si trabajas demasiado, podrías colapsar por exceso de trabajo.", "はたらきすぎると、かろうでたおれかねませんよ"),
            ("その話は、事実である可能性があり得る。", "6. Esa historia, es lógicamente posible que sea cierta.", "そのはなしは、じじつであるかのうせいがありがえる"),
            ("彼がそんなひどいことを言うなんて、あり得ない！", "7. ¡Es imposible/absurdo que él diga cosas tan crueles!", "かれがそんなひどいことをいうなんて、ありえない"),
            ("このままでは、地球の環境が破壊されるおそれがある。", "8. A este ritmo, hay riesgo de que el medio ambiente de la Tierra sea destruido.", "このままでは、ちきゅうのかんきょうがはかいされるおそれがある"),
            ("この薬は、副作用が出るおそれがあります。", "9. Esta medicina tiene el riesgo de presentar efectos secundarios.", "このくすりは、ふくさようがでるおそれがあります"),
            ("彼は口が軽いから、誰かに話しちがいかねない。", "10. Como él es de boca suelta, existe el peligro de que se lo cuente a alguien.", "かれはくちがかるいから、だれかにはなしかねない")
        ],
        "exercises": [
            {"q": "¿Qué expresión es muy formal y se escucha comúnmente en las noticias para anunciar desastres naturales o riesgos públicos?", "options": [{"text": "～おそれがある", "correct": True}, {"text": "～かねない", "correct": False}, {"text": "～あり得ない", "correct": False}]},
            {"q": "¿Qué expresión se usa conectada a la base MASU para decir 'Si sigue así, podría terminar haciendo (algo malo)'?", "options": [{"text": "～かねない", "correct": True}, {"text": "～おそれがある", "correct": False}, {"text": "～あり得る", "correct": False}]},
            {"q": "¿Qué expresión se usa como frase hecha para decir '¡Eso es imposible! / ¡Es absurdo!' ante una situación sorprendente?", "options": [{"text": "あり得ない (Arienai)", "correct": True}, {"text": "ありかねない", "correct": False}, {"text": "ありおそれがある", "correct": False}]},
            {"q": "'Hay riesgo de tsunami' (Tsunami / Sustantivo):", "options": [{"text": "津波のおそれがある", "correct": True}, {"text": "津波のかねない", "correct": False}, {"text": "津波のあり得る", "correct": False}]},
            {"q": "'Si bebes y conduces, podrías causar un accidente grave' (Okosu -> Okoshi):", "options": [{"text": "事故を起こしかねない", "correct": True}, {"text": "事故を起こしおそれがある", "correct": False}, {"text": "事故を起こし得ない", "correct": False}]},
            {"q": "'Existe el riesgo de que la información personal se filtre' (Roushutsu suru):", "options": [{"text": "漏出するおそれがある", "correct": True}, {"text": "漏出しおそれがある", "correct": False}, {"text": "漏出しかねない", "correct": False}]},
            {"q": "'Aquel político podría aceptar sobornos fácilmente' (Uketoru -> Uketori):", "options": [{"text": "賄賂を受け取りかねない", "correct": True}, {"text": "賄賂を受け取るかねない", "correct": False}, {"text": "賄賂を受け取りおそれがある", "correct": False}]},
            {"q": "A: 'Dicen que Tanaka robó el dinero'. B: '¡Es Tanaka! ¡Es imposible que haga eso!'", "options": [{"text": "彼が泥棒なんて、あり得ない！", "correct": True}, {"text": "彼が泥棒なんて、ありかねない！", "correct": False}, {"text": "彼が泥棒なんて、ありおそれがない！", "correct": False}]},
            {"q": "¿Cómo se conecta un verbo a かねない (Kanenai)? (Ej. Naru)", "options": [{"text": "なりかねない (Raíz Masu)", "correct": True}, {"text": "なるかねない (Forma Diccionario)", "correct": False}, {"text": "なってかねない (Forma TE)", "correct": False}]},
            {"q": "¿Cómo se conecta un verbo a おそれがある (Osore ga aru)? (Ej. Naru)", "options": [{"text": "なるおそれがある (Forma Diccionario)", "correct": True}, {"text": "なりおそれがある (Raíz Masu)", "correct": False}, {"text": "なっておそれがある (Forma TE)", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "ニュースの時間です。明日から明後日にかけて、大型の台風が関東地方に接近するおそれがあります。", "Es la hora de las noticias. Existe el riesgo de que un gran tifón se acerque a la región de Kanto desde mañana hasta pasado mañana."),
            ("ja-JP-KeitaNeural", "うわあ、また台風か。最近多いなあ。", "Uau, otro tifón. Hay muchos últimamente."),
            ("ja-JP-NanamiNeural", "ええ。強風で看板が飛んだり、大雨で川が氾濫するおそれがあるので、気をつけてくださいね。", "Sí. Como existe el riesgo de que vuelen carteles por el viento fuerte o de que los ríos se desborden por las lluvias, ten cuidado."),
            ("ja-JP-KeitaNeural", "でも、僕の家は川のすぐそばだから心配だよ。大雨が降ったら、家が水浸しになりかねない。", "Pero mi casa está justo al lado del río, así que estoy preocupado. Si llueve muy fuerte, mi casa podría inundarse fácilmente (peligro)."),
            ("ja-JP-NanamiNeural", "それは大変！もしもの時は、早く避難したほうがいいですよ。", "¡Eso es terrible! En caso de emergencia, es mejor que evacúes temprano."),
            ("ja-JP-KeitaNeural", "うん。こんな時に外に出るなんて、あり得ないよ。今日は早く帰って準備するよ。", "Sí. Salir afuera en un momento así es absurdo/imposible. Hoy me iré a casa temprano a prepararme.")
        ]
    }
}

base_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\lessons"
audio_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\audio"
os.makedirs(audio_dir, exist_ok=True)

for i in range(16, 21):
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
for i in range(16, 21):
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
