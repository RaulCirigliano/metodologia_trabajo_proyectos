import os
import subprocess

data = [
    {
        "id": "jlpt-n2-16",
        "title": "Examen para el JLPT2 - Lección 16",
        "header_title": "JLPT N2 - 準備",
        "desc": "Tema: ~に際して / ~にあたって (En ocasión de / Al momento de)",
        "grammar_points": [
            "<strong>～に際して (ni saishite) / ～にあたって (ni atatte):</strong> Ambos significan 'En ocasión de...' o 'Antes de iniciar...'. Se usan en situaciones formales, discursos o anuncios para indicar que se hace algo especial en preparación a un evento importante.",
            "<strong>Diferencia:</strong> 'にあたって' tiene un matiz más positivo y proactivo (ej. al abrir un negocio, al casarse), mientras que 'に際して' puede usarse tanto para cosas positivas como negativas (ej. al pedir disculpas, en caso de emergencia)."
        ],
        "examples": [
            ("ja-JP-NanamiNeural", "新しい事業を始めるにあたって、多くの先輩にアドバイスをもらった。", "Antes de iniciar el nuevo negocio, recibí consejos de muchos superiores."),
            ("ja-JP-KeitaNeural", "日本へ留学するにあたって、いくつか準備すべきことがあります。", "En ocasión de tu viaje de estudios a Japón, hay algunas cosas que debes preparar."),
            ("ja-JP-NanamiNeural", "開会にあたり、社長よりご挨拶を申し上げます。", "En ocasión de la apertura, nuestro presidente les dirigirá unas palabras."),
            ("ja-JP-KeitaNeural", "ご結婚にあたり、心よりお祝い申し上げます。", "En ocasión de su matrimonio, les expreso mis más sinceras felicitaciones."),
            ("ja-JP-NanamiNeural", "受験にあたって、先生から励ましの言葉をいただいた。", "Antes de los exámenes de ingreso, recibimos palabras de ánimo de nuestro profesor."),
            ("ja-JP-KeitaNeural", "パソコンを使用するに際して、必ずパスワードを設定してください。", "Al momento de utilizar la computadora, asegúrese de configurar una contraseña."),
            ("ja-JP-NanamiNeural", "帰国に際して、お世話になった方々にお礼のメールを送った。", "En ocasión de mi regreso a mi país, envié correos de agradecimiento a quienes me ayudaron."),
            ("ja-JP-KeitaNeural", "お申し込みに際しての注意事項をよくお読みください。", "Por favor, lea atentamente las precauciones al momento de realizar su solicitud."),
            ("ja-JP-NanamiNeural", "社長の退任に際して、記念パーティーが開かれた。", "En ocasión de la renuncia del presidente, se organizó una fiesta conmemorativa."),
            ("ja-JP-KeitaNeural", "契約に際しては、印鑑と身分証明書が必要です。", "Al momento del contrato, se requiere el sello personal y una identificación.")
        ],
        "dialogue": [
            ("ja-JP-KeitaNeural", "本日はお忙しい中、お集まりいただきありがとうございます。", "Muchas gracias por reunirse hoy a pesar de estar ocupados."),
            ("ja-JP-NanamiNeural", "いよいよ、新しいプロジェクトがスタートしますね。", "Por fin comenzará el nuevo proyecto, ¿verdad?"),
            ("ja-JP-KeitaNeural", "はい。新プロジェクトの開始にあたって、皆様に一つお願いがあります。", "Sí. Antes de iniciar este nuevo proyecto, tengo una petición para todos ustedes."),
            ("ja-JP-NanamiNeural", "なんでしょうか？", "¿De qué se trata?"),
            ("ja-JP-KeitaNeural", "このプロジェクトを進めるに際して、他部署との協力が不可欠です。円滑なコミュニケーションを心がけてください。", "En el momento de avanzar con este proyecto, la cooperación con otros departamentos es indispensable. Por favor, procuren tener una comunicación fluida."),
            ("ja-JP-NanamiNeural", "承知いたしました。チーム全体で情報を共有するようにします。", "Entendido. Nos aseguraremos de compartir la información con todo el equipo."),
            ("ja-JP-KeitaNeural", "よろしくお願いします。では、成功に向けて頑張りましょう。", "Cuento con ustedes. Entonces, esforcémonos hacia el éxito.")
        ],
        "exercises": [
            {
                "q": "卒業（　　　）、先生方に感謝の言葉を述べた。",
                "options": [("に際して", True), ("にすぎない", False), ("ことだ", False)]
            },
            {
                "q": "「～にあたって」 tiene un matiz que suele asociarse a:",
                "options": [("Eventos cotidianos sin importancia", False), ("Eventos formales, preparativos e inicios positivos", True), ("Lamentos y arrepentimientos", False)]
            },
            {
                "q": "大会の開催（　　　）、多くのボランティアが集まった。",
                "options": [("にあたって", True), ("て以来", False), ("に限らず", False)]
            },
            {
                "q": "退院（　　　）、お医者さんに挨拶に行った。",
                "options": [("に際して", True), ("にほかならない", False), ("ざるを得ない", False)]
            },
            {
                "q": "新しい車を買う（　　　）、色々な店を回って調べた。",
                "options": [("にあたって", True), ("てからでないと", False), ("のみならず", False)]
            }
        ]
    },
    {
        "id": "jlpt-n2-17",
        "title": "Examen para el JLPT2 - Lección 17",
        "header_title": "JLPT N2 - 準備",
        "desc": "Tema: ~をはじめ / ~をはじめとする (Empezando por...)",
        "grammar_points": [
            "<strong>～をはじめ (o hajime):</strong> Significa 'Empezando por...'. Se utiliza para mencionar el ejemplo más representativo o importante de un grupo, sugiriendo que hay muchos otros elementos similares.",
            "<strong>～をはじめとする + Sustantivo:</strong> Se usa cuando esta expresión modifica a otro sustantivo que le sigue inmediatamente. Ej: 社長をはじめとする社員全員 (Todos los empleados, empezando por el presidente)."
        ],
        "examples": [
            ("ja-JP-NanamiNeural", "私たちの学校には、中国をはじめ、多くのアジアからの留学生がいます。", "En nuestra escuela, empezando por China, hay muchos estudiantes extranjeros de Asia."),
            ("ja-JP-KeitaNeural", "ご両親をはじめ、ご家族の皆様によろしくお伝えください。", "Por favor dele mis saludos a toda su familia, empezando por sus padres."),
            ("ja-JP-NanamiNeural", "東京をはじめとする大都市では、通勤ラッシュが深刻な問題だ。", "En las grandes ciudades, empezando por Tokio, la hora pico de los trenes es un problema grave."),
            ("ja-JP-KeitaNeural", "社長をはじめ、社員の皆様が私の送別会に来てくれました。", "Empezando por el presidente, todos los empleados vinieron a mi fiesta de despedida."),
            ("ja-JP-NanamiNeural", "このレストランでは、寿司をはじめとする日本料理が楽しめます。", "En este restaurante se puede disfrutar de comida japonesa, empezando por el sushi."),
            ("ja-JP-KeitaNeural", "京都には、金閣寺をはじめ、多くの歴史的なお寺があります。", "En Kioto hay muchos templos históricos, empezando por el Kinkaku-ji."),
            ("ja-JP-NanamiNeural", "彼は、英語をはじめとして、５ヶ国語を話すことができる。", "Él puede hablar 5 idiomas, empezando por el inglés."),
            ("ja-JP-KeitaNeural", "サッカーをはじめとするスポーツは、世界中で人気がある。", "Los deportes, empezando por el fútbol, son populares en todo el mundo."),
            ("ja-JP-NanamiNeural", "先生をはじめ、色々な方に助けていただきました。", "Recibí ayuda de varias personas, empezando por mi profesor."),
            ("ja-JP-KeitaNeural", "最近、スマートフォンをはじめとする電子機器の普及が著しい。", "Últimamente, la popularización de los dispositivos electrónicos, empezando por los smartphones, es notable.")
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "来月の国際交流パーティーですが、たくさんの人が参加するそうですね。", "Sobre la fiesta de intercambio internacional del próximo mes, escuché que participará mucha gente."),
            ("ja-JP-KeitaNeural", "ええ、市長をはじめ、多くの関係者が出席する予定です。", "Sí, empezando por el alcalde, se planea que asistan muchas personas involucradas."),
            ("ja-JP-NanamiNeural", "すごいですね。料理はどうしますか？", "Qué increíble. ¿Qué haremos con la comida?"),
            ("ja-JP-KeitaNeural", "参加者は多国籍ですから、お寿司をはじめとする和食だけでなく、色々な国の料理を用意するつもりです。", "Como los participantes son de muchas nacionalidades, planeo preparar no solo comida japonesa empezando por el sushi, sino platos de varios países."),
            ("ja-JP-NanamiNeural", "それは楽しみですね。留学生たちも喜ぶと思います。", "Eso suena muy bien. Creo que los estudiantes extranjeros también se alegrarán."),
            ("ja-JP-KeitaNeural", "はい。中国や韓国をはじめ、アジアからの学生も多いですからね。", "Sí. Porque hay muchos estudiantes de Asia, empezando por China y Corea del Sur.")
        ],
        "exercises": [
            {
                "q": "このイベントには、社長（　　　）、多くの社員が参加した。",
                "options": [("をはじめ", True), ("に際して", False), ("ことか", False)]
            },
            {
                "q": "「～をはじめ」 se usa para:",
                "options": [("Indicar un cambio de estado", False), ("Citar el ejemplo más representativo de un grupo", True), ("Dar un consejo directo", False)]
            },
            {
                "q": "日本では、地震（　　　）とする自然災害が多い。",
                "options": [("をはじめ", True), ("にすぎない", False), ("にあたって", False)]
            },
            {
                "q": "鈴木さん（　　　）、チームの皆さんに感謝しています。",
                "options": [("をはじめ", True), ("てからでないと", False), ("ざるを得ない", False)]
            },
            {
                "q": "会議には、部長（　　　）する経営陣が出席した。",
                "options": [("をはじめと", True), ("のみならず", False), ("て以来", False)]
            }
        ]
    },
    {
        "id": "jlpt-n2-18",
        "title": "Examen para el JLPT2 - Lección 18",
        "header_title": "JLPT N2 - 準備",
        "desc": "Tema: ~からして (A juzgar por / Ya desde...)",
        "grammar_points": [
            "<strong>～からして (kara shite):</strong> Significa 'A juzgar por...' o 'Ya desde...'. Se usa para señalar un detalle, generalmente algo básico o pequeño, para insinuar que todo lo demás también es de la misma manera (frecuentemente tiene una connotación negativa).",
            "<strong>Nota:</strong> Es como decir 'Incluso ese pequeño detalle es así, por lo tanto, el resto seguramente también lo es'."
        ],
        "examples": [
            ("ja-JP-NanamiNeural", "あの映画は、タイトルからして面白くなさそうだ。", "A juzgar por el título, esa película no parece interesante (ni me imagino el contenido)."),
            ("ja-JP-KeitaNeural", "あのレストランは、入り口の雰囲気からして高そうだ。", "Ese restaurante, ya desde la atmósfera de la entrada, se ve que es caro."),
            ("ja-JP-NanamiNeural", "彼の態度は、挨拶からして失礼だ。", "Su actitud, empezando desde su forma de saludar, es grosera."),
            ("ja-JP-KeitaNeural", "あの新入社員は、服装からしてビジネスマンらしくない。", "Ese nuevo empleado, ya desde su forma de vestir, no parece un hombre de negocios."),
            ("ja-JP-NanamiNeural", "この説明書は、字の大きさからして読みにくい。", "Este manual de instrucciones, ya a juzgar por el tamaño de la letra, es difícil de leer."),
            ("ja-JP-KeitaNeural", "彼女の話し方からして、どうやら私が嫌われているようだ。", "A juzgar por su forma de hablar, al parecer le caigo mal."),
            ("ja-JP-NanamiNeural", "あのホテルは、名前からして高級な感じがする。", "Ese hotel, ya desde el nombre, da una sensación de ser de lujo."),
            ("ja-JP-KeitaNeural", "私の猫は、鳴き声からして他の猫と違う。", "Mi gato, ya a juzgar por su maullido, es diferente a otros gatos."),
            ("ja-JP-NanamiNeural", "この企画は、最初のアイデアからして間違っていた。", "Este proyecto, ya desde la idea inicial, estaba equivocado."),
            ("ja-JP-KeitaNeural", "彼の部屋は、玄関からしてゴミだらけだった。", "Su habitación, ya desde la entrada, estaba llena de basura.")
        ],
        "dialogue": [
            ("ja-JP-KeitaNeural", "ねえ、新しくできたあのラーメン屋、行ってみない？", "Oye, ¿no quieres ir a probar ese nuevo restaurante de ramen que acaba de abrir?"),
            ("ja-JP-NanamiNeural", "うーん、やめておいた方がいいと思うよ。あの店、看板のデザインからして美味しくなさそうじゃない？", "Mmm, creo que es mejor que no vayamos. Ese lugar, a juzgar por el diseño del letrero, no parece estar rico, ¿verdad?"),
            ("ja-JP-KeitaNeural", "看板だけで決めるのは早いよ。でも確かに、店の外にメニューも置いてないしね。", "Es muy pronto para decidir solo por el letrero. Pero es cierto que ni siquiera tienen un menú afuera de la tienda."),
            ("ja-JP-NanamiNeural", "それに、店員の態度からして、あまり歓迎されていない感じがしたわ。", "Además, ya desde la actitud de los empleados, me dio la sensación de que no éramos muy bienvenidos."),
            ("ja-JP-KeitaNeural", "そんなに？じゃあ、やっぱりいつもの店に行こうか。", "¿Tanto así? Entonces, mejor vayamos al restaurante de siempre.")
        ],
        "exercises": [
            {
                "q": "彼の作った料理は、見た目（　　　）まずそうだ。",
                "options": [("からして", True), ("をはじめ", False), ("にあたって", False)]
            },
            {
                "q": "「～からして」 se usa para:",
                "options": [("Mencionar el mejor ejemplo de un grupo", False), ("Juzgar el todo a partir de un pequeño detalle básico", True), ("Indicar una obligación", False)]
            },
            {
                "q": "その提案は、テーマ（　　　）私たちの求めているものと違う。",
                "options": [("からして", True), ("に際して", False), ("にすぎない", False)]
            },
            {
                "q": "彼女は歩き方（　　　）自信に満ち溢れている。",
                "options": [("からして", True), ("てからでないと", False), ("ことだ", False)]
            },
            {
                "q": "あの人の話は、最初の一言（　　　）嘘だとわかった。",
                "options": [("からして", True), ("のみならず", False), ("て以来", False)]
            }
        ]
    },
    {
        "id": "jlpt-n2-19",
        "title": "Examen para el JLPT2 - Lección 19",
        "header_title": "JLPT N2 - 準備",
        "desc": "Tema: ~にわたって (A lo largo de / Durante todo...)",
        "grammar_points": [
            "<strong>～にわたって (ni watatte):</strong> Significa 'A lo largo de...' o 'Durante todo...'. Se utiliza para indicar que un estado, acción o fenómeno se extiende de manera continua a lo largo de un periodo de tiempo prolongado o una amplia zona geográfica.",
            "<strong>～にわたる + Sustantivo:</strong> Se usa cuando la expresión modifica a un sustantivo. Ej: ３日間にわたる会議 (Una reunión que se extendió a lo largo de 3 días)."
        ],
        "examples": [
            ("ja-JP-NanamiNeural", "会議は５時間にわたって行われた。", "La reunión se llevó a cabo a lo largo de 5 horas."),
            ("ja-JP-KeitaNeural", "その台風は、日本全国にわたって大きな被害をもたらした。", "Ese tifón causó grandes daños a lo largo de todo Japón."),
            ("ja-JP-NanamiNeural", "彼は長年にわたって、がんの研究を続けている。", "Él ha continuado investigando el cáncer a lo largo de muchos años."),
            ("ja-JP-KeitaNeural", "大雨の影響で、広い範囲にわたって停電が発生した。", "Debido a la fuerte lluvia, se produjo un apagón a lo largo de una amplia zona."),
            ("ja-JP-NanamiNeural", "３日間にわたるイベントが、無事に終了しました。", "El evento, que se extendió a lo largo de 3 días, ha finalizado sin problemas."),
            ("ja-JP-KeitaNeural", "その橋は、川の端から端にわたって建設されている。", "Ese puente está construido a lo largo de (cubriendo desde) un extremo del río hasta el otro."),
            ("ja-JP-NanamiNeural", "彼女は多岐にわたって才能を発揮している。", "Ella demuestra su talento a lo largo de muchas y diversas áreas."),
            ("ja-JP-KeitaNeural", "約１週間にわたって、警察の捜索が続けられた。", "A lo largo de aproximadamente una semana, la búsqueda de la policía continuó."),
            ("ja-JP-NanamiNeural", "彼は３回にわたって、手術を受けた。", "Él fue operado en tres ocasiones (a lo largo de tres intervenciones)."),
            ("ja-JP-KeitaNeural", "半世紀にわたる彼のキャリアは、本当に素晴らしい。", "Su carrera, que se extiende a lo largo de medio siglo, es verdaderamente maravillosa.")
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "ニュースを見ましたか？昨日の地震、かなり大きかったみたいですね。", "¿Viste las noticias? El terremoto de ayer parece haber sido bastante fuerte."),
            ("ja-JP-KeitaNeural", "ええ。関東地方の全域にわたって、強い揺れが観測されたそうです。", "Sí. Dicen que se observaron fuertes temblores a lo largo de toda la región de Kanto."),
            ("ja-JP-NanamiNeural", "被害も大きそうですね。", "Los daños también parecen ser grandes."),
            ("ja-JP-KeitaNeural", "はい。広い範囲にわたって、水道管が破裂しているらしいです。", "Sí. Al parecer las tuberías de agua se han roto a lo largo de una amplia zona."),
            ("ja-JP-NanamiNeural", "復旧には時間がかかりそうですね。", "Parece que la recuperación tomará tiempo."),
            ("ja-JP-KeitaNeural", "そうですね。専門家の話では、数週間にわたって影響が続くかもしれないとのことです。", "Así es. Según los expertos, el impacto podría continuar a lo largo de varias semanas.")
        ],
        "exercises": [
            {
                "q": "そのお祭りは、１週間（　　　）開催される。",
                "options": [("にわたって", True), ("からして", False), ("にあたって", False)]
            },
            {
                "q": "「～にわたって」 se usa principalmente para:",
                "options": [("Expresar una emoción profunda", False), ("Indicar extensión prolongada en tiempo o espacio", True), ("Mostrar la causa de una situación", False)]
            },
            {
                "q": "彼は10年（　　　）この町でボランティア活動をしている。",
                "options": [("にわたって", True), ("をはじめ", False), ("に際して", False)]
            },
            {
                "q": "日本海側の広い範囲（　　　）雪が降るでしょう。",
                "options": [("にわたって", True), ("にほかならない", False), ("にすぎない", False)]
            },
            {
                "q": "数ヶ月（　　　）調査の結果、ようやく原因が判明した。",
                "options": [("にわたる", True), ("にあたる", False), ("からする", False)]
            }
        ]
    },
    {
        "id": "jlpt-n2-20",
        "title": "Examen para el JLPT2 - Lección 20",
        "header_title": "JLPT N2 - 準備",
        "desc": "Tema: ~ばかりか / ~ばかりでなく (No solo... sino también)",
        "grammar_points": [
            "<strong>～ばかりか / ～ばかりでなく (bakari ka / bakari de naku):</strong> Significa 'No solo... sino también...'. Es muy similar a '～だけでなく' o '～のみならず', pero tiene un fuerte matiz de sorpresa o énfasis, implicando que algo va más allá de lo esperado ('no solo esto, sino que encima aquello').",
            "<strong>Nota:</strong> Suele ir acompañado de palabras como 'も' (también) en la segunda parte de la oración."
        ],
        "examples": [
            ("ja-JP-NanamiNeural", "彼は英語ばかりか、アラビア語も話せるそうだ。", "Dicen que él no solo habla inglés, sino también árabe (lo cual es sorprendente)."),
            ("ja-JP-KeitaNeural", "このレストランは味が悪いばかりか、店員の態度もひどい。", "Este restaurante no solo tiene mal sabor, sino que la actitud de los empleados también es terrible."),
            ("ja-JP-NanamiNeural", "熱があるばかりか、咳も止まらないんです。", "No solo tengo fiebre, sino que tampoco me para la tos."),
            ("ja-JP-KeitaNeural", "彼女は美しいばかりでなく、性格も非常に優しい。", "Ella no solo es hermosa, sino que su personalidad también es muy amable."),
            ("ja-JP-NanamiNeural", "最近の若者は、新聞を読まないばかりか、テレビも見ない人が増えている。", "En los jóvenes de hoy en día, están aumentando las personas que no solo no leen el periódico, sino que tampoco ven la televisión."),
            ("ja-JP-KeitaNeural", "あの会社は給料が安いばかりか、残業代も出ないらしい。", "Dicen que en esa empresa no solo el sueldo es bajo, sino que encima no pagan horas extras."),
            ("ja-JP-NanamiNeural", "彼は遅刻したばかりか、謝りもしなかった。", "Él no solo llegó tarde, sino que ni siquiera se disculpó."),
            ("ja-JP-KeitaNeural", "このアパートは駅から遠いばかりでなく、家賃も高い。", "Este apartamento no solo está lejos de la estación, sino que la renta también es cara."),
            ("ja-JP-NanamiNeural", "彼は自分のミスを認めないばかりか、他人のせいにした。", "Él no solo no admitió su error, sino que encima le echó la culpa a otro."),
            ("ja-JP-KeitaNeural", "この薬は効果がないばかりか、副作用もある。", "Este medicamento no solo no tiene efecto, sino que también tiene efectos secundarios.")
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "田中君、また今日も無断欠勤だって。信じられない。", "Tanaka faltó al trabajo de nuevo hoy sin avisar. Es increíble."),
            ("ja-JP-KeitaNeural", "えっ、またですか？彼は遅刻が多いばかりか、無断欠勤までするんですか。", "¿Eh, de nuevo? Él no solo llega tarde mucho, ¿sino que hasta falta sin avisar?"),
            ("ja-JP-NanamiNeural", "そうなの。しかも、注意されても反省しないばかりか、逆ギレするらしいわよ。", "Así es. Además, cuando le llaman la atención, no solo no reflexiona, sino que dicen que encima se enoja con ellos."),
            ("ja-JP-KeitaNeural", "それはひどいですね。仕事のミスが多いばかりでなく、態度も悪いとなると、さすがにクビかもしれませんね。", "Eso es terrible. Si no solo comete muchos errores en el trabajo, sino que también tiene mala actitud, me temo que podrían despedirlo."),
            ("ja-JP-NanamiNeural", "ええ、部長もかなり怒っていたわ。", "Sí, el jefe de departamento también estaba bastante enojado.")
        ],
        "exercises": [
            {
                "q": "彼は財布を落とした（　　　）、パスポートまでなくしてしまった。",
                "options": [("ばかりか", True), ("からして", False), ("にわたって", False)]
            },
            {
                "q": "「～ばかりか」 suele usarse cuando:",
                "options": [("Se habla de un largo periodo de tiempo", False), ("Hay sorpresa porque la situación va más allá de lo esperado", True), ("Se pide un favor educadamente", False)]
            },
            {
                "q": "この地域は冬に雪が降る（　　　）、風も非常に強い。",
                "options": [("ばかりでなく", True), ("にあたって", False), ("をはじめ", False)]
            },
            {
                "q": "その映画は日本国内（　　　）、海外でも大ヒットした。",
                "options": [("ばかりか", True), ("て以来", False), ("に際して", False)]
            },
            {
                "q": "彼女は嘘をついた（　　　）、謝罪の言葉もなかった。",
                "options": [("ばかりか", True), ("にわたって", False), ("からして", False)]
            }
        ]
    }
]

base_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\lessons"
audio_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\audio"
os.makedirs(audio_dir, exist_ok=True)

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

    # 3. Estructurar HTML con el estilo pastel (Azul N2)
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
        <div class="lesson-header-simple" style="background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%); color: #0f172a; padding: 2rem; border-radius: 12px; margin-bottom: 2rem; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
            <span style="background: #0284c7; color: #ffffff; padding: 0.3rem 0.8rem; border-radius: 20px; font-weight: 800; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px;">{lesson["header_title"]}</span>
            <h1 style="margin: 1rem 0; font-size: 2.2rem; font-weight: 800; letter-spacing: -0.5px; color: #0f172a;">{lesson["title"]}</h1>
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

print("Actualizando index.html...")
index_path = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

n2_menu_items = """                        <a href="lessons/jlpt-n2-16.html" target="main_frame" class="nav-link">
                            <span class="nav-num">16</span> ~に際して / ~にあたって (Ocasiones)
                        </a>
                        <a href="lessons/jlpt-n2-17.html" target="main_frame" class="nav-link">
                            <span class="nav-num">17</span> ~をはじめ (Empezando por)
                        </a>
                        <a href="lessons/jlpt-n2-18.html" target="main_frame" class="nav-link">
                            <span class="nav-num">18</span> ~からして (A juzgar por)
                        </a>
                        <a href="lessons/jlpt-n2-19.html" target="main_frame" class="nav-link">
                            <span class="nav-num">19</span> ~にわたって (A lo largo de)
                        </a>
                        <a href="lessons/jlpt-n2-20.html" target="main_frame" class="nav-link">
                            <span class="nav-num">20</span> ~ばかりか / ~ばかりでなく (No solo...)
                        </a>
                    </div>"""

target = '<a href="lessons/jlpt-n2-15.html" target="main_frame" class="nav-link">\n                            <span class="nav-num">15</span> ~のみならず / ~に限らず (No solo... sino)\n                        </a>\n                    </div>'

if target in index_html and "jlpt-n2-16" not in index_html:
    new_index = index_html.replace(target, target.replace('</div>', n2_menu_items))
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(new_index)
    print("Inyectado Lote 4 N2 en index.html")

print("Ejecutando furigana...")
subprocess.run("python add_furigana.py", shell=True)
print("COMPLETADO LOTE 4 N2")
