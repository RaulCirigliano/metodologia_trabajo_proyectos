import os
import subprocess

data = [
    {
        "id": "jlpt-n2-1",
        "title": "Examen para el JLPT2 - Lección 1",
        "header_title": "JLPT N2 - 準備",
        "desc": "Tema: ~に際して (En ocasión de) / ~にあたって (Al momento de)",
        "grammar_points": [
            "<strong>～に際して (ni saishite):</strong> Expresión formal para 'en ocasión de' o 'cuando ocurre...'. Se usa mucho en anuncios y documentos oficiales.",
            "<strong>～にあたって (ni atatte):</strong> Significa 'con motivo de' o 'al momento de comenzar'. Expresa una actitud activa o preparatoria hacia un evento especial (matrimonios, negocios, etc.)."
        ],
        "examples": [
            ("ja-JP-NanamiNeural", "日本への留学に際して、多くの書類を準備した。", "En ocasión de mi viaje de estudios a Japón, preparé muchos documentos."),
            ("ja-JP-KeitaNeural", "お申し込みに際しては、写真が必要です。", "Al momento de inscribirse, se requiere una fotografía."),
            ("ja-JP-NanamiNeural", "計画を変更するに際して、問題を検討した。", "Al modificar el plan, analizamos los problemas."),
            ("ja-JP-KeitaNeural", "開会に際して、社長からご挨拶を申し上げます。", "Con motivo de la apertura, el presidente dará unas palabras."),
            ("ja-JP-NanamiNeural", "有名な先生にお会いするに際して、緊張しました。", "Al conocer a tan famoso profesor, me puse nervioso."),
            ("ja-JP-KeitaNeural", "新しい事業を始めるにあたって、市場調査を行った。", "Al momento de iniciar el nuevo negocio, realizamos un estudio de mercado."),
            ("ja-JP-NanamiNeural", "卒業にあたって、先生方に感謝の言葉を述べたい。", "Con motivo de la graduación, me gustaría expresar palabras de agradecimiento a los profesores."),
            ("ja-JP-KeitaNeural", "このプロジェクトを進めるにあたって、皆の協力が不可欠だ。", "Al llevar a cabo este proyecto, la cooperación de todos es indispensable."),
            ("ja-JP-NanamiNeural", "決断を下すにあたって、さまざまな意見を聞いた。", "Al tomar la decisión, escuché diversas opiniones."),
            ("ja-JP-KeitaNeural", "大会の開催にあたって、多くのボランティアが集まった。", "Con motivo de la celebración del torneo, se reunieron muchos voluntarios.")
        ],
        "dialogue": [
            ("ja-JP-KeitaNeural", "来月の国際会議の開催にあたって、準備は順調ですか？", "Con motivo de la celebración de la conferencia internacional del próximo mes, ¿los preparativos van por buen camino?"),
            ("ja-JP-NanamiNeural", "はい。ただ、海外からのゲストをお迎えするに際して、ホテルの予約を再確認しています。", "Sí. Solo que, en ocasión de recibir a los invitados del extranjero, estoy reconfirmando las reservas de hotel."),
            ("ja-JP-KeitaNeural", "それは重要ですね。プログラムを決定するにあたって、何か問題はありましたか？", "Eso es importante. Al momento de decidir el programa, ¿hubo algún problema?"),
            ("ja-JP-NanamiNeural", "特にありませんが、資料を作成するに際して、最新のデータが必要です。", "Ninguno en particular, pero al momento de elaborar el material, se requieren los datos más recientes."),
            ("ja-JP-KeitaNeural", "わかりました。データの提出にあたって、各部署に連絡しておきます。", "Entendido. Al momento de entregar los datos, me pondré en contacto con cada departamento."),
            ("ja-JP-NanamiNeural", "助かります。会議を成功させるにあたって、皆さんの協力が不可欠ですからね。", "Es de gran ayuda. Al hacer que la conferencia sea un éxito, la cooperación de todos es indispensable."),
            ("ja-JP-KeitaNeural", "ええ。開幕に際して、素晴らしいスピーチができるよう頑張りましょう。", "Sí. En ocasión de la apertura, esforcémonos para poder dar un excelente discurso.")
        ],
        "exercises": [
            {
                "q": "新製品の開発（　　　）、市場調査を行った。",
                "options": [("にあたって", True), ("にむけて", False), ("にそって", False)]
            },
            {
                "q": "ご入場（　　　）、チケットをご提示ください。",
                "options": [("について", False), ("に際して", True), ("において", False)]
            },
            {
                "q": "「～にあたって」 se usa para:",
                "options": [("Cosas cotidianas e informales", False), ("Eventos negativos del pasado", False), ("Eventos especiales o inicios de proyectos", True)]
            },
            {
                "q": "結婚（　　　）、両親に挨拶に行った。",
                "options": [("に際して", True), ("にしたがって", False), ("につれて", False)]
            },
            {
                "q": "¿Cuál es más natural en un contexto de negocios para 'Al momento de firmar el contrato'?",
                "options": [("契約する時に", False), ("契約するにあたって", True), ("契約するから", False)]
            }
        ]
    },
    {
        "id": "jlpt-n2-2",
        "title": "Examen para el JLPT2 - Lección 2",
        "header_title": "JLPT N2 - 準備",
        "desc": "Tema: ~に限り / ~に限って (Particularidad y Limitación)",
        "grammar_points": [
            "<strong>～に限り (ni kagiri):</strong> Significa 'solamente' o 'limitado a'. Expresa una excepción exclusiva (ej. 'Solamente hoy', 'Limitado a estudiantes').",
            "<strong>～に限って (ni kagitte):</strong> Tiene varios usos: 1) Sentimiento de injusticia ('Justo cuando... pasa algo malo'). 2) Confianza absoluta ('Esa persona en particular no haría eso')."
        ],
        "examples": [
            ("ja-JP-NanamiNeural", "本日に限り、全品半額です。", "Limitado únicamente al día de hoy, todos los artículos están a mitad de precio."),
            ("ja-JP-KeitaNeural", "入場は１８歳以上の方に限ります。", "La entrada está limitada a mayores de 18 años."),
            ("ja-JP-NanamiNeural", "初めてのお客様に限り、無料サンプルを差し上げます。", "Solo a los clientes de primera vez, les entregaremos una muestra gratuita."),
            ("ja-JP-KeitaNeural", "この病院は、午前中に限り面会が可能です。", "En este hospital, las visitas son posibles únicamente durante la mañana."),
            ("ja-JP-NanamiNeural", "女性に限り、デザートがサービスされます。", "Solamente para las mujeres, el postre será de cortesía."),
            ("ja-JP-KeitaNeural", "傘を持っていない日に限って、雨が降る。", "Justo el día que no llevo paraguas, llueve. (Injusticia)"),
            ("ja-JP-NanamiNeural", "急いでいる時に限って、道が混んでいる。", "Justo cuando tengo prisa, hay tráfico."),
            ("ja-JP-KeitaNeural", "彼に限って、嘘をつくはずがない。", "Él en particular, es imposible que mienta. (Confianza)"),
            ("ja-JP-NanamiNeural", "うちの子に限って、そんな悪いことはしません。", "Mi hijo en particular, no haría cosas tan malas."),
            ("ja-JP-KeitaNeural", "あの真面目な田中さんに限って、遅刻するなんて信じられない。", "Justo el serio señor Tanaka llegando tarde, no lo puedo creer.")
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "ああ、最悪。今日に限って、電車が遅れているわ。", "Ah, qué fatal. Justo hoy, el tren está retrasado."),
            ("ja-JP-KeitaNeural", "本当に。急いでいる時に限って、いつもこうだよね。", "De verdad. Justo cuando uno tiene prisa, siempre es así."),
            ("ja-JP-NanamiNeural", "今日は大事なプレゼンがあるのに。山田さんに連絡しないと。", "Y eso que hoy tengo una presentación importante. Tengo que avisarle al señor Yamada."),
            ("ja-JP-KeitaNeural", "山田さんなら大丈夫だよ。あの人に限って、怒ったりしないよ。", "Tratándose del señor Yamada estará bien. Él en particular, no se enfadaría."),
            ("ja-JP-NanamiNeural", "そうだといいけど。あ、駅前のカフェ、本日に限りコーヒーが半額だって。", "Espero que sea así. Ah, la cafetería frente a la estación dice que solo por hoy el café está a mitad de precio."),
            ("ja-JP-KeitaNeural", "へえ、朝の７時から９時に限り、パンも無料らしいよ。", "Oh, y parece que limitado de 7 a 9 de la mañana, el pan también es gratis."),
            ("ja-JP-NanamiNeural", "時間がない日に限って、そんないい話があるなんて悲しい！", "¡Justo en el día que no tengo tiempo hay una oferta tan buena, qué triste!")
        ],
        "exercises": [
            {
                "q": "初めてご来店のお客様（　　　）、割引クーポンを差し上げます。",
                "options": [("に限り", True), ("に限って", False), ("にあたって", False)]
            },
            {
                "q": "「あの人に限って、そんなことをするはずがない」 expresa:",
                "options": [("Duda", False), ("Envidia", False), ("Fuerte confianza en que no lo haría", True)]
            },
            {
                "q": "私が外に干した日（　　　）、雨が降る。",
                "options": [("に限り", False), ("に限って", True), ("に際して", False)]
            },
            {
                "q": "７０歳以上の方（　　　）、入場無料です。",
                "options": [("に限り", True), ("にあたって", False), ("に限って", False)]
            },
            {
                "q": "忙しい時（　　　）、電話がたくさんかかってくる。",
                "options": [("に限り", False), ("に限って", True), ("に際して", False)]
            }
        ]
    },
    {
        "id": "jlpt-n2-3",
        "title": "Examen para el JLPT2 - Lección 3",
        "header_title": "JLPT N2 - 準備",
        "desc": "Tema: ~ばかりに / ~たいばかりに (Causas extremas y deseos)",
        "grammar_points": [
            "<strong>～ばかりに (bakari ni):</strong> Significa 'solo por culpa de...' o 'solo porque...'. Expresa que una pequeña razón causó un gran resultado negativo o lamentable.",
            "<strong>～たいばかりに (tai bakari ni):</strong> Significa 'solo por el gran deseo de...'. Expresa que uno hizo un gran esfuerzo o algo irracional solo para conseguir lo que deseaba."
        ],
        "examples": [
            ("ja-JP-NanamiNeural", "お金がないばかりに、大学に進学できなかった。", "Solo por no tener dinero, no pude ingresar a la universidad."),
            ("ja-JP-KeitaNeural", "一言謝らなかったばかりに、彼と別れることになった。", "Solo por no haberme disculpado con una palabra, terminé rompiendo con él."),
            ("ja-JP-NanamiNeural", "本当のことを言ったばかりに、みんなに嫌われてしまった。", "Solo por haber dicho la verdad, terminé siendo odiado por todos."),
            ("ja-JP-KeitaNeural", "道を知っていると言ったばかりに、道に迷ってしまった。", "Solo por haber dicho que conocía el camino, terminamos perdiéndonos."),
            ("ja-JP-NanamiNeural", "確認しなかったばかりに、大きなミスをしてしまった。", "Solo por culpa de no haber revisado, cometí un gran error."),
            ("ja-JP-KeitaNeural", "彼女に会いたいばかりに、雨の中を３時間も待った。", "Solo por el fuerte deseo de verla, esperé 3 horas bajo la lluvia."),
            ("ja-JP-NanamiNeural", "新しいゲームを買いたいばかりに、毎日アルバイトをした。", "Solo por el deseo de comprar el nuevo juego, trabajé a medio tiempo todos los días."),
            ("ja-JP-KeitaNeural", "子供を喜ばせたいばかりに、高価なプレゼントを買った。", "Solo por querer hacer feliz a mi hijo, le compré un regalo costoso."),
            ("ja-JP-NanamiNeural", "試験に合格したいばかりに、徹夜で勉強した。", "Solo por el afán de aprobar el examen, estudié toda la noche sin dormir."),
            ("ja-JP-KeitaNeural", "彼を助けたいばかりに、自分の仕事を後回しにした。", "Solo por querer ayudarlo, dejé mi propio trabajo para después.")
        ],
        "dialogue": [
            ("ja-JP-KeitaNeural", "ああ、失敗した。一瞬よそ見をしたばかりに、車をぶつけてしまった。", "Ah, qué fracaso. Solo por haber mirado a otro lado un instante, estrellé el auto."),
            ("ja-JP-NanamiNeural", "ええっ、大丈夫ですか？怪我はありませんか？", "¿Eh, estás bien? ¿No tienes heridas?"),
            ("ja-JP-KeitaNeural", "怪我はないけど、修理代が高いよ。少し急いでいたばかりに...。", "Heridas no hay, pero el costo de reparación será alto. Solo por culpa de haberme apresurado un poco..."),
            ("ja-JP-NanamiNeural", "気を落とさないでください。でも、どうしてそんなに急いでいたんですか？", "No te desanimes. Pero, ¿por qué estabas tan apresurado?"),
            ("ja-JP-KeitaNeural", "限定のケーキを買いたいばかりに、スピードを出してしまったんだ。", "Solo por el afán de querer comprar un pastel de edición limitada, aceleré."),
            ("ja-JP-NanamiNeural", "ケーキのために事故を起こしたんですか。美味しいものを食べたいばかりに、高くつきましたね。", "¿Causaste un accidente por un pastel? Solo por el deseo de comer algo rico, te salió muy caro."),
            ("ja-JP-KeitaNeural", "本当だね。注意力が足りなかったばかりに、反省しているよ。", "Es cierto. Solo por culpa de que me faltó atención, estoy reflexionando en ello.")
        ],
        "exercises": [
            {
                "q": "私が遅刻した（　　　）、みんなに迷惑をかけてしまった。",
                "options": [("ばかりに", True), ("にあたって", False), ("に限って", False)]
            },
            {
                "q": "「～たいばかりに」 expresa:",
                "options": [("Un deseo que no se cumplió", False), ("Un gran esfuerzo o acto irracional impulsado por un deseo", True), ("Una excusa para no hacer algo", False)]
            },
            {
                "q": "彼に勝ちたい（　　　）、毎日１０時間も練習した。",
                "options": [("ばかりに", True), ("に限り", False), ("に際して", False)]
            },
            {
                "q": "「～ばかりに」 a menudo lleva a un resultado...",
                "options": [("Muy positivo e inesperado", False), ("Neutro", False), ("Negativo o lamentable", True)]
            },
            {
                "q": "確認を怠った（　　　）、不良品を出荷してしまった。",
                "options": [("にあたって", False), ("ばかりに", True), ("に限り", False)]
            }
        ]
    },
    {
        "id": "jlpt-n2-4",
        "title": "Examen para el JLPT2 - Lección 4",
        "header_title": "JLPT N2 - 準備",
        "desc": "Tema: ~ところだった / ~てたまらない (Casi pasa / Sentimiento insoportable)",
        "grammar_points": [
            "<strong>～ところだった (tokoro datta):</strong> Significa 'Estuve a punto de...' o 'Casi...'. Expresa que algo estuvo a punto de suceder pero no pasó (generalmente evadiendo un peligro o perdiendo una oportunidad).",
            "<strong>～てたまらない (te tamaranai):</strong> Significa 'No puedo soportar lo...' o 'Extremadamente...'. Expresa una emoción o sensación física tan fuerte que es imposible de reprimir."
        ],
        "examples": [
            ("ja-JP-NanamiNeural", "もう少しで事故を起こすところだった。", "Por poco y casi causo un accidente."),
            ("ja-JP-KeitaNeural", "危なく電車に乗り遅れるところだった。", "Peligrosamente estuve a punto de perder el tren."),
            ("ja-JP-NanamiNeural", "友人が止めてくれなかったら、怒って彼を殴るところだった。", "Si mi amigo no me hubiera detenido, casi lo golpeo del enojo."),
            ("ja-JP-KeitaNeural", "あと少しで１００点を取るところだったのに。", "Y pensar que estuve a punto de sacar 100 puntos por tan poco..."),
            ("ja-JP-NanamiNeural", "気がつくのが遅かったら、火事になるところだった。", "Si me hubiera dado cuenta tarde, casi se convierte en un incendio."),
            ("ja-JP-KeitaNeural", "今日は暑くて暑くて、喉が渇いてたまらない。", "Hoy hace un calor tremendo, estoy que no soporto la sed."),
            ("ja-JP-NanamiNeural", "彼に会いたくてたまらない。", "Tengo unas ganas insoportables de verlo."),
            ("ja-JP-KeitaNeural", "昨日徹夜したので、眠くてたまらない。", "Como me desvelé ayer, tengo un sueño que no soporto."),
            ("ja-JP-NanamiNeural", "試合に負けて、悔しくてたまらない。", "Perdí el partido y siento una frustración extrema."),
            ("ja-JP-KeitaNeural", "新しいパソコンが欲しくてたまらない。", "Quiero una computadora nueva, no aguanto las ganas.")
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "ああ、疲れた。今日は忙しくて、死ぬほど疲れてたまらないわ。", "Ah, qué cansancio. Hoy estuve tan ocupada que no soporto este cansancio mortal."),
            ("ja-JP-KeitaNeural", "お疲れ様。さっき、廊下で転ぶところだったよ。気をつけてね。", "Buen trabajo. Hace un rato, casi me caigo en el pasillo. Ten cuidado."),
            ("ja-JP-NanamiNeural", "本当？実は私も、朝、寝坊して会議に遅刻するところだったの。", "¿De verdad? La verdad es que yo también, en la mañana me quedé dormida y casi llego tarde a la reunión."),
            ("ja-JP-KeitaNeural", "それは危なかったね。でも、今は無事に終わってよかった。", "Eso estuvo peligroso. Pero qué bueno que ahora todo terminó sin problemas."),
            ("ja-JP-NanamiNeural", "うん。でも、お腹が空いてたまらないから、早くご飯に行きましょう。", "Sí. Pero como me muero de hambre y no lo soporto, vayamos rápido a comer."),
            ("ja-JP-KeitaNeural", "僕も。美味しいラーメンが食べたくてたまらない気分だ。", "Yo también. Tengo unas ganas insoportables de comer un delicioso ramen."),
            ("ja-JP-NanamiNeural", "いいわね。急がないと、お店が閉まるところだったりして。", "Qué bien. Si no nos apuramos, casi que la tienda estará a punto de cerrar.")
        ],
        "exercises": [
            {
                "q": "もう少しで階段から落ちる（　　　）。",
                "options": [("ばかりだった", False), ("ところだった", True), ("たまらなかった", False)]
            },
            {
                "q": "家族のことが心配で（　　　）。",
                "options": [("たまらない", True), ("ところだった", False), ("に限らない", False)]
            },
            {
                "q": "「～ところだった」 implica que la acción descrita:",
                "options": [("Finalmente ocurrió", False), ("Ocurrirá en el futuro", False), ("Estuvo a punto de ocurrir, pero NO ocurrió", True)]
            },
            {
                "q": "クーラーが壊れて、部屋が暑くて（　　　）。",
                "options": [("たまらない", True), ("ところだった", False), ("ばかりに", False)]
            },
            {
                "q": "目覚まし時計が鳴らなくて、遅刻する（　　　）。",
                "options": [("ところだった", True), ("たまらない", False), ("にあたって", False)]
            }
        ]
    },
    {
        "id": "jlpt-n2-5",
        "title": "Examen para el JLPT2 - Lección 5",
        "header_title": "JLPT N2 - 準備",
        "desc": "Tema: ~抜く / ~切る (Terminar por completo / Hacer hasta el final)",
        "grammar_points": [
            "<strong>～抜く (nuku):</strong> Unido a la raíz de un verbo, significa 'hacer algo hasta el final soportando las dificultades'. Enfatiza el esfuerzo extremo para completarlo.",
            "<strong>～切る (kiru):</strong> Unido a la raíz de un verbo, significa 'terminar algo por completo' o 'hacer algo al 100%'. No necesariamente implica dificultad, solo exhaustividad (que no queda nada)."
        ],
        "examples": [
            ("ja-JP-NanamiNeural", "４２キロのマラソンを走り抜いた。", "Corrí los 42 kilómetros de la maratón hasta el final (con gran esfuerzo)."),
            ("ja-JP-KeitaNeural", "どんなに辛くても、最後までやり抜く覚悟だ。", "Por más duro que sea, tengo la determinación de llevarlo a cabo hasta el final."),
            ("ja-JP-NanamiNeural", "悩み抜いた結果、会社を辞めることにした。", "Tras pensarlo exhaustivamente (sufriendo), decidí renunciar a la empresa."),
            ("ja-JP-KeitaNeural", "彼らは過酷な訓練を耐え抜いた。", "Ellos soportaron el cruel entrenamiento hasta el final."),
            ("ja-JP-NanamiNeural", "考え抜いたアイデアが採用された。", "La idea que pensé exhaustivamente fue adoptada."),
            ("ja-JP-KeitaNeural", "テーブルの上のケーキを全部食べ切った。", "Me comí por completo todo el pastel sobre la mesa."),
            ("ja-JP-NanamiNeural", "この小説は長すぎて、一日では読み切れない。", "Esta novela es demasiado larga, no se puede terminar de leer en un día."),
            ("ja-JP-KeitaNeural", "彼は疲れ切った顔で帰ってきた。", "Él regresó con una cara de estar completamente exhausto."),
            ("ja-JP-NanamiNeural", "お金を使い切ってしまった。", "Me gasté por completo todo el dinero."),
            ("ja-JP-KeitaNeural", "彼女は夫の浮気を信じ切っていた。", "Ella creía ciegamente (al 100%) en la infidelidad de su esposo.")
        ],
        "dialogue": [
            ("ja-JP-KeitaNeural", "あー、やっとこの大きなプロジェクトをやり抜いたぞ！", "¡Ah, por fin llevamos a cabo este gran proyecto hasta el final con tanto esfuerzo!"),
            ("ja-JP-NanamiNeural", "本当にお疲れ様。毎日の残業で、皆すっかり疲れ切っているわね。", "De verdad buen trabajo. Con las horas extras diarias, todos están completamente exhaustos."),
            ("ja-JP-KeitaNeural", "うん。でも、途中で諦めないで、最後まで頑張り抜いてよかったよ。", "Sí. Pero qué bueno que no nos rendimos a la mitad y nos esforzamos hasta el final."),
            ("ja-JP-NanamiNeural", "そうね。私もこの問題について悩み抜いた結果、たくさん学べたと思うわ。", "Es cierto. Yo también creo que, como resultado de haber pensado este problema exhaustivamente, pude aprender mucho."),
            ("ja-JP-KeitaNeural", "今日は打ち上げだ！ビールを飲み切るまで帰らないぞ！", "¡Hoy es la fiesta de celebración! ¡No nos iremos hasta terminar de bebernos toda la cerveza!"),
            ("ja-JP-NanamiNeural", "ふふっ、そんなに飲んだら、明日起き切れないんじゃない？", "Jeje, si bebes tanto, ¿no serás incapaz de despertarte por completo mañana?"),
            ("ja-JP-KeitaNeural", "大丈夫、明日は休みだからね。思い切り休むよ。", "Está bien, mañana es día de descanso. Descansaré con todas mis fuerzas.")
        ],
        "exercises": [
            {
                "q": "マラソンを最後まで走り（　　　）、大きな自信になった。",
                "options": [("切って", False), ("抜いて", True), ("かけて", False)]
            },
            {
                "q": "冷蔵庫のジュースを全部飲み（　　　）しまった。",
                "options": [("抜いて", False), ("切って", True), ("だして", False)]
            },
            {
                "q": "「～抜く」 enfatiza principalmente:",
                "options": [("Que no queda nada físicamente", False), ("Hacerlo de forma rápida", False), ("Hacer algo hasta el final soportando dificultades", True)]
            },
            {
                "q": "どんな困難があっても、信念を守り（　　　）つもりだ。",
                "options": [("抜く", True), ("切る", False), ("すぎる", False)]
            },
            {
                "q": "彼は疲れ（　　　）声で電話に出た。",
                "options": [("抜いた", False), ("切った", True), ("た", False)]
            }
        ]
    }
]

base_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\lessons"
audio_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\audio"
os.makedirs(audio_dir, exist_ok=True)

# Generar HTMLs y Audios
for lesson in data:
    lesson_id = lesson["id"]
    print(f"--- Generating {lesson_id} ---")
    
    # 1. Audio del Diálogo (Concatenado)
    final_dialogue_mp3 = os.path.join(audio_dir, f"dialogue-{lesson_id}.mp3")
    if not os.path.exists(final_dialogue_mp3):
        files = []
        for j, (voice, text_jp, _) in enumerate(lesson["dialogue"]):
            filename = f"line_{lesson_id}_{j}.mp3"
            safe_text = text_jp.replace('"', '\\"')
            cmd = f'python -m edge_tts --voice {voice} --text "{safe_text}" --rate=-5% --write-media {filename}'
            subprocess.run(cmd, shell=True)
            files.append(filename)

        list_file = f"files_{lesson_id}.txt"
        with open(list_file, "w", encoding="utf-8") as f:
            for filename in files:
                f.write(f"file '{filename}'\n")

        subprocess.run(f"ffmpeg -f concat -safe 0 -i {list_file} -c copy \"{final_dialogue_mp3}\" -y", shell=True)

        for filename in files:
            if os.path.exists(filename):
                os.remove(filename)
        if os.path.exists(list_file):
            os.remove(list_file)
            
    # 2. Audios de los 10 Ejemplos individuales
    example_html_blocks = []
    for idx, (voice, ex_jp, ex_es) in enumerate(lesson["examples"]):
        ex_mp3_name = f"ex_{lesson_id}_{idx}.mp3"
        ex_mp3_path = os.path.join(audio_dir, ex_mp3_name)
        if not os.path.exists(ex_mp3_path):
            safe_text = ex_jp.replace('"', '\\"')
            cmd = f'python -m edge_tts --voice {voice} --text "{safe_text}" --rate=-5% --write-media "{ex_mp3_path}"'
            subprocess.run(cmd, shell=True)
            
        ex_block = f'''
        <div class="practice-item">
            <div class="practice-content">
                <div class="text-jp">{ex_jp}</div>
                <div class="text-es">{idx+1}. {ex_es}</div>
            </div>
            <button class="audio-btn" onclick="playRealAudio('../audio/{ex_mp3_name}')">🔊</button>
        </div>'''
        example_html_blocks.append(ex_block)

    # 3. Estructurar HTML
    html_content = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{lesson["title"]}</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=Noto+Sans+JP:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../css/style.css">
    <script>
        let currentAudio = null;
        function playRealAudio(src) {{
            if(currentAudio) {{ currentAudio.pause(); currentAudio.currentTime = 0; }}
            currentAudio = new Audio(src);
            currentAudio.play();
        }}
    </script>
</head>
<body class="iframe-body">
    <div class="max-w-4xl">
        <div class="lesson-header-simple" style="background: linear-gradient(135deg, #1e293b 0%, #334155 100%); color: white; padding: 2rem; border-radius: 12px; margin-bottom: 2rem; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            <span style="background: #e2e8f0; color: #1e293b; padding: 0.3rem 0.8rem; border-radius: 20px; font-weight: 800; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px;">{lesson["header_title"]}</span>
            <h1 style="margin: 1rem 0; font-size: 2.2rem; font-weight: 800; letter-spacing: -0.5px;">{lesson["title"]}</h1>
            <p class="lesson-desc" style="font-size: 1.1rem; opacity: 0.9;">{lesson["desc"]}</p>
        </div>

        <h2 class="section-title">📚 Gramática Principal</h2>
        <div class="grammar-note">
            <ul>
                {''.join(f'<li style="margin-bottom: 1rem;">{pt}</li>' for pt in lesson["grammar_points"])}
            </ul>
        </div>

        <h2 class="section-title">🌟 10 Ejemplos de Uso (Nativo)</h2>
        <div class="grammar-note">
            <p>Pulsa el botón de audio para escuchar la pronunciación perfecta generada por IA.</p>
        </div>
        {''.join(example_html_blocks)}

        <h2 class="section-title">🎧 Práctica de Comprensión Auditiva</h2>
        <div class="grammar-note" style="background-color: #eff6ff; border-left-color: #3b82f6;">
            <p>Escucha este diálogo a velocidad natural prestando atención a cómo se aplican todas las reglas y variaciones de esta lección en una conversación real.</p>
            
            <div style="text-align: center; margin: 1.5rem 0; background: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border: 1px solid #e2e8f0;">
                <p style="margin-bottom: 15px; font-weight: 600; color: #475569; font-size: 1.1rem;">🎧 Escucha el diálogo (Voces IA):</p>
                <audio controls style="width: 100%; max-width: 450px; outline: none; border-radius: 50px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
                    <source src="../audio/dialogue-{lesson_id}.mp3" type="audio/mpeg">
                    Tu navegador no soporta el elemento de audio.
                </audio>
            </div>

            <details style="background: white; padding: 1rem; border-radius: 8px; border: 1px solid #e2e8f0; margin-top: 1rem;">
                <summary style="font-weight: 600; cursor: pointer; color: var(--primary-color);">Ver Transcripción y Traducción</summary>
                <div style="margin-top: 1rem; display: grid; gap: 1rem; font-size: 0.95rem;">
'''
    for _, text_jp, text_es in lesson["dialogue"]:
        html_content += f'                    <div style="border-bottom: 1px solid #f1f5f9; padding-bottom: 0.5rem;"><div class="text-jp">{text_jp}</div><div class="text-es" style="color:#64748b; margin-top:0.3rem;">{text_es}</div></div>\n'
    
    html_content += '''                </div>
            </details>
        </div>

        <h2 class="section-title">📝 Ejercicios de Práctica JLPT</h2>
'''
    for i, ex in enumerate(lesson["exercises"]):
        html_content += f'''        <div class="question-block" style="background:#fff; border:1px solid #e2e8f0; padding:1.5rem; border-radius:10px; margin-bottom:1rem;">
            <p style="font-weight:600; margin-bottom:1rem; font-size:1.1rem;">{i+1}. {ex["q"]}</p>
            <div style="display:grid; gap:10px;">
'''
        for opt_text, is_correct in ex["options"]:
            correct_str = "true" if is_correct else "false"
            html_content += f'                <button class="option-btn" data-correct="{correct_str}">{opt_text}</button>\n'
        html_content += '''            </div>
            <div class="feedback-msg" style="margin-top:10px; font-weight:600; min-height:24px;"></div>
        </div>
'''
    html_content += '''    </div>
    <script src="../js/main.js"></script>
</body>
</html>'''

    html_path = os.path.join(base_dir, f"{lesson_id}.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

# Actualizar el index.html principal para inyectar el menú N2 si no existe
index_path = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

if "JLPT N2 (Avanzado)" not in index_html:
    n2_menu = """
            <details class="level-accordion">
                <summary class="level-title">📘 JLPT N2 (Avanzado)</summary>
                <ul class="lesson-list">
                    <li><a href="#" onclick="loadLesson('jlpt-n2-1')">Lección 1: ~に際して / ~にあたって</a></li>
                    <li><a href="#" onclick="loadLesson('jlpt-n2-2')">Lección 2: ~に限り / ~に限って</a></li>
                    <li><a href="#" onclick="loadLesson('jlpt-n2-3')">Lección 3: ~ばかりに / ~たいばかりに</a></li>
                    <li><a href="#" onclick="loadLesson('jlpt-n2-4')">Lección 4: ~ところだった / ~てたまらない</a></li>
                    <li><a href="#" onclick="loadLesson('jlpt-n2-5')">Lección 5: ~抜く / ~切る</a></li>
                </ul>
            </details>
"""
    # Insertarlo antes de Profundizaciones
    target = '<details class="level-accordion">\n                <summary class="level-title">💎 Profundizaciones'
    if target in index_html:
        new_index = index_html.replace(target, n2_menu + target)
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(new_index)
        print("Menu N2 inyectado en index.html")

print("Ejecutando furigana...")
subprocess.run("python add_furigana.py", shell=True)
print("COMPLETADO LOTE 1 N2")
