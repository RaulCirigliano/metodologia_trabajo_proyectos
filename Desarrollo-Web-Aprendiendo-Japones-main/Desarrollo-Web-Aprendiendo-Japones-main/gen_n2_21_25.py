import os
import subprocess

data = [
    {
        "id": "jlpt-n2-21",
        "title": "Examen para el JLPT2 - Lección 21",
        "header_title": "JLPT N2 - 準備",
        "desc": "Tema: ~にかけては (En cuanto a... / Tratándose de...)",
        "grammar_points": [
            "<strong>～にかけては (ni kakete wa):</strong> Significa 'En cuanto a...' o 'Tratándose de...'. Se usa para destacar que alguien tiene una gran habilidad, conocimiento o confianza absoluta en un campo o tema específico.",
            "<strong>Nota:</strong> Generalmente la oración que le sigue expresa una valoración muy alta (ej. 'nadie le gana', 'es el mejor', 'tiene absoluta confianza')."
        ],
        "examples": [
            ("ja-JP-NanamiNeural", "彼は、数学にかけてはクラスで誰にも負けない。", "En cuanto a las matemáticas, él no pierde contra nadie en la clase."),
            ("ja-JP-KeitaNeural", "歌のうまさにかけては、彼女の右に出る者はいない。", "Tratándose de habilidad para cantar, no hay nadie superior a ella."),
            ("ja-JP-NanamiNeural", "歴史の知識にかけては、先生よりも詳しいかもしれない。", "En cuanto a conocimientos de historia, quizás él sepa más que el profesor."),
            ("ja-JP-KeitaNeural", "足の速さにかけては、彼がチームで一番だ。", "Tratándose de correr rápido, él es el número uno del equipo."),
            ("ja-JP-NanamiNeural", "この町のことにかけては、私に何でも聞いてください。", "En cuanto a cosas de este pueblo, pregúntenme lo que sea."),
            ("ja-JP-KeitaNeural", "サービス精神にかけては、あのホテルが最高だ。", "Tratándose del espíritu de servicio al cliente, ese hotel es el mejor."),
            ("ja-JP-NanamiNeural", "山田さんは、仕事の早さにかけては誰にも負けない自信があるそうだ。", "El señor Yamada parece tener la confianza de que, en cuanto a rapidez en el trabajo, no le gana nadie."),
            ("ja-JP-KeitaNeural", "料理にかけては、母が一番上手です。", "En cuanto a cocinar, mi madre es la mejor."),
            ("ja-JP-NanamiNeural", "忍耐力にかけては、彼ほど強い人はいない。", "Tratándose de paciencia, no hay nadie más fuerte que él."),
            ("ja-JP-KeitaNeural", "プログラミングにかけては、我が社に優秀な人材が揃っている。", "En cuanto a programación, nuestra empresa cuenta con personal excelente.")
        ],
        "dialogue": [
            ("ja-JP-KeitaNeural", "来月のイベントの企画、誰に任せようか迷っているんだ。", "Estoy dudando a quién dejarle a cargo la planificación del evento del próximo mes."),
            ("ja-JP-NanamiNeural", "それなら、田中さんがいいんじゃないですか？", "En ese caso, ¿no sería buena idea dárselo al señor Tanaka?"),
            ("ja-JP-KeitaNeural", "田中君か。確かに彼は真面目だけど、企画力はどうかな。", "¿Tanaka? Es cierto que es muy serio, pero ¿qué tal su capacidad de planificación?"),
            ("ja-JP-NanamiNeural", "新しいアイデアを出すことにかけては、彼が社内で一番だと思いますよ。", "Tratándose de proponer nuevas ideas, creo que él es el número uno dentro de la empresa."),
            ("ja-JP-KeitaNeural", "なるほど。じゃあ、彼にリーダーをやってもらうことにしよう。", "Ya veo. Entonces, hagamos que él sea el líder.")
        ],
        "exercises": [
            {
                "q": "彼はコンピューターの知識（　　　）、誰にも負けない。",
                "options": [("にかけては", True), ("にあたって", False), ("ばかりか", False)]
            },
            {
                "q": "「～にかけては」 suele ir seguido de:",
                "options": [("Una oración que expresa que no se puede hacer algo", False), ("Una valoración muy alta o expresión de superioridad", True), ("Una regla estricta", False)]
            },
            {
                "q": "料理の腕前（　　　）、彼女の右に出る者はいない。",
                "options": [("にかけては", True), ("からして", False), ("をはじめ", False)]
            },
            {
                "q": "道案内（　　　）、地元の人に聞くのが一番だ。",
                "options": [("にかけては", True), ("にわたって", False), ("てからでないと", False)]
            },
            {
                "q": "その歌手は、歌唱力（　　　）世界でもトップクラスだ。",
                "options": [("にかけては", True), ("に際して", False), ("にほかならない", False)]
            }
        ]
    },
    {
        "id": "jlpt-n2-22",
        "title": "Examen para el JLPT2 - Lección 22",
        "header_title": "JLPT N2 - 準備",
        "desc": "Tema: ~にこたえて (En respuesta a... / Para satisfacer...)",
        "grammar_points": [
            "<strong>～にこたえて (ni kotaete):</strong> Significa 'En respuesta a...' o 'Para satisfacer (las expectativas/peticiones) de...'. Se utiliza para indicar que se realiza una acción como respuesta positiva para complacer lo que otros desean o esperan.",
            "<strong>Nota:</strong> Se usa frecuentemente con sustantivos como 期待 (expectativas), 要望 (solicitudes), 応援 (apoyo) o リクエスト (peticiones)."
        ],
        "examples": [
            ("ja-JP-NanamiNeural", "お客様の要望にこたえて、営業時間を延長しました。", "En respuesta a las solicitudes de los clientes, hemos extendido nuestro horario de atención."),
            ("ja-JP-KeitaNeural", "親の期待にこたえて、彼は医者になった。", "Para satisfacer las expectativas de sus padres, él se convirtió en médico."),
            ("ja-JP-NanamiNeural", "ファンのリクエストにこたえて、アンコールでもう一曲歌った。", "En respuesta a la petición de los fans, cantó una canción más en el encore."),
            ("ja-JP-KeitaNeural", "市民の声にこたえて、新しい公園が作られた。", "En respuesta a la voz de los ciudadanos, se construyó un nuevo parque."),
            ("ja-JP-NanamiNeural", "皆様の応援にこたえられるよう、全力で頑張ります。", "Para poder corresponder a su apoyo, me esforzaré con todas mis fuerzas."),
            ("ja-JP-KeitaNeural", "学生たちの希望にこたえて、図書館の開館時間が見直された。", "En respuesta al deseo de los estudiantes, el horario de la biblioteca fue revisado."),
            ("ja-JP-NanamiNeural", "時代のニーズにこたえる新商品が開発された。", "Se desarrolló un nuevo producto que responde a las necesidades de la época."),
            ("ja-JP-KeitaNeural", "期待にこたえられず、申し訳ありませんでした。", "Siento mucho no haber podido cumplir con sus expectativas."),
            ("ja-JP-NanamiNeural", "彼は監督の期待にこたえて、見事にゴールを決めた。", "En respuesta a las expectativas de su entrenador, él marcó un espléndido gol."),
            ("ja-JP-KeitaNeural", "アンケートの結果にこたえて、メニューを改善しました。", "Mejoramos el menú en respuesta a los resultados de la encuesta.")
        ],
        "dialogue": [
            ("ja-JP-KeitaNeural", "新しい店舗のメニュー、すごく好評みたいですね。", "El menú del nuevo local parece ser muy popular, ¿verdad?"),
            ("ja-JP-NanamiNeural", "はい。お客様からの「ヘルシーなメニューが欲しい」という要望にこたえて、サラダの種類を増やしたのが良かったようです。", "Sí. Parece que fue buena idea aumentar los tipos de ensalada en respuesta a la petición de los clientes de 'querer un menú saludable'."),
            ("ja-JP-KeitaNeural", "なるほど。お客さんのニーズにこたえるのは、ビジネスの基本ですからね。", "Ya veo. Responder a las necesidades de los clientes es lo fundamental en los negocios, después de todo."),
            ("ja-JP-NanamiNeural", "ええ。これからも、消費者の声にこたえるサービスを提供していきたいです。", "Sí. De ahora en adelante, me gustaría seguir ofreciendo servicios que respondan a la voz de los consumidores.")
        ],
        "exercises": [
            {
                "q": "ファンの期待（　　　）、彼は最高の演技を見せた。",
                "options": [("にこたえて", True), ("にかけては", False), ("からして", False)]
            },
            {
                "q": "「～にこたえて」 se utiliza frecuentemente con palabras como:",
                "options": [("怒り (ira)", False), ("期待 (expectativas) o 要望 (peticiones)", True), ("天気 (clima)", False)]
            },
            {
                "q": "住民の要望（　　　）、この道路は広げられることになった。",
                "options": [("にこたえて", True), ("にあたって", False), ("ばかりか", False)]
            },
            {
                "q": "両親の期待（　　　）よう、必死に勉強した。",
                "options": [("にこたえられる", True), ("にわたる", False), ("をめぐる", False)]
            },
            {
                "q": "アンコールの声（　　　）、バンドは再びステージに登場した。",
                "options": [("にこたえて", True), ("に際して", False), ("をはじめ", False)]
            }
        ]
    },
    {
        "id": "jlpt-n2-23",
        "title": "Examen para el JLPT2 - Lección 23",
        "header_title": "JLPT N2 - 準備",
        "desc": "Tema: ~に沿って (De acuerdo con / Siguiendo...)",
        "grammar_points": [
            "<strong>～に沿って (ni sotte):</strong> Significa 'De acuerdo con...', 'Siguiendo (una regla/plan)' o 'A lo largo de (un camino/río)'. Se usa para expresar que una acción avanza sin desviarse de un estándar establecido, como un plan, un manual o las reglas.",
            "<strong>～に沿う (ni sou):</strong> Verbo que significa cumplir con o estar a la altura de algo (ej. ご希望に沿えず申し訳ありません - Siento no poder cumplir con sus deseos)."
        ],
        "examples": [
            ("ja-JP-NanamiNeural", "マニュアルに沿って、機械を操作してください。", "Por favor, opere la máquina de acuerdo con (siguiendo) el manual."),
            ("ja-JP-KeitaNeural", "新しい計画に沿って、プロジェクトが進められている。", "El proyecto está avanzando de acuerdo con el nuevo plan."),
            ("ja-JP-NanamiNeural", "線路に沿って、桜の木が植えられている。", "A lo largo de las vías del tren, hay plantados cerezos."),
            ("ja-JP-KeitaNeural", "会社の方針に沿って、業務を改善します。", "Mejoraremos el trabajo de acuerdo con la política de la empresa."),
            ("ja-JP-NanamiNeural", "皆様のご希望に沿えるよう、努力いたします。", "Nos esforzaremos para poder actuar de acuerdo con (satisfacer) sus deseos."),
            ("ja-JP-KeitaNeural", "法律に沿って、厳正に処罰されるべきだ。", "Debería ser castigado estrictamente de acuerdo con la ley."),
            ("ja-JP-NanamiNeural", "川に沿って１時間ほど歩くと、海に出ます。", "Si caminas a lo largo del río por más o menos una hora, saldrás al mar."),
            ("ja-JP-KeitaNeural", "時代の変化に沿った新しい教育が必要だ。", "Se necesita una nueva educación de acuerdo con (adaptada a) los cambios de la época."),
            ("ja-JP-NanamiNeural", "ガイドラインに沿って、安全対策を行ってください。", "Por favor, aplique medidas de seguridad siguiendo las directrices."),
            ("ja-JP-KeitaNeural", "ご期待に沿えず、誠に申し訳ございません。", "Lamentamos profundamente no haber podido cumplir con sus expectativas.")
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "明日のプレゼンですが、どうやって進めましょうか？", "Sobre la presentación de mañana, ¿cómo deberíamos proceder?"),
            ("ja-JP-KeitaNeural", "昨日配られたスケジュール表に沿って、順番に発表していきましょう。", "Vayamos presentando en orden, de acuerdo con el horario que se distribuyó ayer."),
            ("ja-JP-NanamiNeural", "わかりました。では、私は資料に沿って説明をしますね。", "Entendido. Entonces yo haré la explicación siguiendo (a lo largo de) los documentos."),
            ("ja-JP-KeitaNeural", "ええ、お願いします。お客様の関心に沿った内容にできるといいですね。", "Sí, por favor. Sería bueno si podemos hacer que el contenido se ajuste a los intereses de los clientes."),
            ("ja-JP-NanamiNeural", "はい、相手の反応を見ながら、柔軟に対応します。", "Sí, observando la reacción de la otra parte, responderé flexiblemente.")
        ],
        "exercises": [
            {
                "q": "先生の指示（　　　）、テストの準備をした。",
                "options": [("に沿って", True), ("にこたえて", False), ("からして", False)]
            },
            {
                "q": "「～に沿って」 puede utilizarse para referirse a espacio físico. ¿Cuál es un ejemplo correcto?",
                "options": [("時計に沿って", False), ("川に沿って歩く", True), ("空に沿って", False)]
            },
            {
                "q": "会社の基本方針（　　　）開発を進める。",
                "options": [("に沿って", True), ("に際して", False), ("にかけては", False)]
            },
            {
                "q": "せっかくの提案ですが、今回はご希望（　　　）ことができません。",
                "options": [("に沿う", True), ("にこたえる", False), ("にわたる", False)]
            },
            {
                "q": "カリキュラム（　　　）、授業が行われる。",
                "options": [("に沿って", True), ("ばかりか", False), ("をはじめ", False)]
            }
        ]
    },
    {
        "id": "jlpt-n2-24",
        "title": "Examen para el JLPT2 - Lección 24",
        "header_title": "JLPT N2 - 準備",
        "desc": "Tema: ~をめぐって (En torno a... / Sobre...)",
        "grammar_points": [
            "<strong>～をめぐって (o megutte) / ～をめぐる (o meguru):</strong> Significa 'En torno a...' o 'Sobre (un asunto)'. Se usa para indicar el tema central de un debate, discusión, disputa o conflicto entre varias personas o grupos.",
            "<strong>Diferencia con について:</strong> 'について' simplemente significa 'sobre/acerca de'. 'をめぐって' implica que varias partes están involucradas en un argumento, rumor o enfrentamiento respecto a ese tema."
        ],
        "examples": [
            ("ja-JP-NanamiNeural", "その事件をめぐって、様々な噂が流れている。", "Están circulando varios rumores en torno a ese incidente."),
            ("ja-JP-KeitaNeural", "親の遺産をめぐって、兄弟が争っている。", "Los hermanos están peleando en torno a la herencia de sus padres."),
            ("ja-JP-NanamiNeural", "新しい法律の解釈をめぐり、議論が白熱した。", "El debate se calentó en torno a la interpretación de la nueva ley."),
            ("ja-JP-KeitaNeural", "環境問題をめぐる国際会議が開かれた。", "Se celebró una conferencia internacional en torno a los problemas medioambientales."),
            ("ja-JP-NanamiNeural", "一人の女性をめぐって、二人の男が対立した。", "Dos hombres se enfrentaron en torno a (por el amor de) una sola mujer."),
            ("ja-JP-KeitaNeural", "ダムの建設をめぐって、住民と国が対立している。", "Los residentes y el país están enfrentados en torno a la construcción de la presa."),
            ("ja-JP-NanamiNeural", "消費税の引き上げをめぐる議論は、まだ終わっていない。", "El debate en torno a la subida del impuesto al consumo aún no ha terminado."),
            ("ja-JP-KeitaNeural", "人事異動をめぐって、社内で不満が出ている。", "Han surgido quejas dentro de la empresa en torno a los cambios de personal."),
            ("ja-JP-NanamiNeural", "教育制度の改革をめぐって、意見が対立している。", "Las opiniones están divididas en torno a la reforma del sistema educativo."),
            ("ja-JP-KeitaNeural", "この小説は、ある謎をめぐる若者たちの冒険を描いている。", "Esta novela describe la aventura de unos jóvenes en torno a un cierto misterio.")
        ],
        "dialogue": [
            ("ja-JP-KeitaNeural", "今朝のニュース見た？あの会社の買収の話、まだもめているみたいだね。", "¿Viste las noticias de esta mañana? Parece que el asunto de la adquisición de esa empresa todavía está en disputa."),
            ("ja-JP-NanamiNeural", "ええ、見ました。買収額をめぐって、両社の意見が合わないそうですね。", "Sí, lo vi. Parece que las opiniones de ambas compañías no concuerdan en torno al precio de compra, ¿verdad?"),
            ("ja-JP-KeitaNeural", "そうらしい。それに、新しい社長の人事をめぐる噂も飛び交っているよ。", "Eso parece. Además, están volando rumores en torno a los nombramientos del nuevo presidente."),
            ("ja-JP-NanamiNeural", "大きな会社だから、一つの決定をめぐって多くの人が関わっているんでしょうね。", "Como es una empresa grande, seguramente mucha gente está involucrada en torno a una sola decisión."),
            ("ja-JP-KeitaNeural", "全くだね。早く解決するといいけど。", "Totalmente. Espero que se resuelva pronto.")
        ],
        "exercises": [
            {
                "q": "新空港の建設（　　　）、激しい反対運動が起きた。",
                "options": [("をめぐって", True), ("に沿って", False), ("にかけては", False)]
            },
            {
                "q": "「～をめぐって」 implica principalmente:",
                "options": [("Que algo se hizo solo para complacer a alguien", False), ("Que existe un debate, conflicto o discusión entre varias partes sobre un tema", True), ("Que una acción se realiza siguiendo un manual", False)]
            },
            {
                "q": "水資源（　　　）国同士の争いが絶えない。",
                "options": [("をめぐる", True), ("にあたる", False), ("からする", False)]
            },
            {
                "q": "会議では、来年の予算（　　　）活発な議論が交わされた。",
                "options": [("をめぐって", True), ("に際して", False), ("にわたって", False)]
            },
            {
                "q": "遺産相続（　　　）トラブルは、よくある話だ。",
                "options": [("をめぐる", True), ("に沿う", False), ("にこたえる", False)]
            }
        ]
    },
    {
        "id": "jlpt-n2-25",
        "title": "Examen para el JLPT2 - Lección 25",
        "header_title": "JLPT N2 - 準備",
        "desc": "Tema: ~に基づいて (Basado en...)",
        "grammar_points": [
            "<strong>～に基づいて (ni motozuite) / ～に基づく (ni motozuku):</strong> Significa 'Basado en...' o 'Fundamentado en...'. Se usa para indicar la base, el origen o los datos sobre los que se apoya una decisión, investigación, o creación.",
            "<strong>Nota:</strong> Se usa frecuentemente con sustantivos como 事実 (hechos), データ (datos), 経験 (experiencia), 法律 (ley) o 調査結果 (resultados de una investigación)."
        ],
        "examples": [
            ("ja-JP-NanamiNeural", "この映画は、実際にあった事件に基づいて作られている。", "Esta película está hecha basándose en un incidente que ocurrió en la realidad."),
            ("ja-JP-KeitaNeural", "調査の結果に基づいて、新しい事業計画を立てた。", "Basado en los resultados de la investigación, elaboramos un nuevo plan de negocios."),
            ("ja-JP-NanamiNeural", "長年の経験に基づいて、アドバイスをさせていただきます。", "Me permito darle un consejo basado en mis años de experiencia."),
            ("ja-JP-KeitaNeural", "裁判長は、法律に基づいて公正な判断を下した。", "El juez emitió un fallo justo basado en la ley."),
            ("ja-JP-NanamiNeural", "集めたデータに基づき、グラフを作成してください。", "Por favor, elabore un gráfico basado en los datos recopilados."),
            ("ja-JP-KeitaNeural", "彼の意見は、しっかりとした証拠に基づいている。", "Su opinión está basada en pruebas sólidas."),
            ("ja-JP-NanamiNeural", "これは、最新の科学的研究に基づく結果です。", "Este es un resultado basado en las investigaciones científicas más recientes."),
            ("ja-JP-KeitaNeural", "お客様のアンケートに基づいて、商品を改良しました。", "Mejoramos el producto basándonos en las encuestas de los clientes."),
            ("ja-JP-NanamiNeural", "史実に基づいた小説を書くのは、とても難しい。", "Escribir una novela basada en hechos históricos es muy difícil."),
            ("ja-JP-KeitaNeural", "評価基準に基づいて、社員のボーナスを決定する。", "Los bonos de los empleados se decidirán basándose en los criterios de evaluación.")
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "先輩、来期の売上目標の資料、できました。", "Senpai, aquí tiene los documentos de los objetivos de ventas para el próximo trimestre."),
            ("ja-JP-KeitaNeural", "ありがとう。この目標数字は、何を基準にして計算したの？", "Gracias. ¿Tomando qué como referencia calculaste estos números objetivo?"),
            ("ja-JP-NanamiNeural", "はい、過去５年間の売上データに基づいて予測を立てました。", "Sí, elaboré el pronóstico basándome en los datos de ventas de los últimos 5 años."),
            ("ja-JP-KeitaNeural", "なるほど、客観的なデータに基づいているなら説得力があるね。", "Ya veo. Si está basado en datos objetivos, entonces es persuasivo."),
            ("ja-JP-NanamiNeural", "さらに、最近の市場調査の結果にも基づいて、少し目標を高く設定しています。", "Además, basándome en los resultados de recientes estudios de mercado, establecí el objetivo un poco más alto."),
            ("ja-JP-KeitaNeural", "素晴らしい。この資料なら、会議でも自信を持って発表できそうだよ。", "Excelente. Con este documento, parece que podré presentarlo con confianza en la reunión.")
        ],
        "exercises": [
            {
                "q": "この小説は、筆者の実体験（　　　）書かれている。",
                "options": [("に基づいて", True), ("をめぐって", False), ("に沿って", False)]
            },
            {
                "q": "「～に基づいて」 se utiliza comúnmente con:",
                "options": [("Emociones y sentimientos", False), ("Datos, leyes, experiencias o hechos", True), ("Personas y animales", False)]
            },
            {
                "q": "法律（　　　）処罰されるのは当然だ。",
                "options": [("に基づいて", True), ("にかけては", False), ("にこたえて", False)]
            },
            {
                "q": "アンケート調査（　　　）改善案を提出してください。",
                "options": [("に基づいた", True), ("に沿った", False), ("ばかりの", False)]
            },
            {
                "q": "彼の主張は、何の根拠（　　　）いない。",
                "options": [("にも基づいて", True), ("にもわたって", False), ("からして", False)]
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
    
    # 1. Audio del Diálogo
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
            
    # 2. Audios Ejemplos
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

    # 3. HTML (Azul N2)
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

n2_menu_items = """                        <a href="lessons/jlpt-n2-21.html" target="main_frame" class="nav-link">
                            <span class="nav-num">21</span> ~にかけては (Tratándose de...)
                        </a>
                        <a href="lessons/jlpt-n2-22.html" target="main_frame" class="nav-link">
                            <span class="nav-num">22</span> ~にこたえて (En respuesta a...)
                        </a>
                        <a href="lessons/jlpt-n2-23.html" target="main_frame" class="nav-link">
                            <span class="nav-num">23</span> ~に沿って (De acuerdo con...)
                        </a>
                        <a href="lessons/jlpt-n2-24.html" target="main_frame" class="nav-link">
                            <span class="nav-num">24</span> ~をめぐって (En torno a...)
                        </a>
                        <a href="lessons/jlpt-n2-25.html" target="main_frame" class="nav-link">
                            <span class="nav-num">25</span> ~に基づいて (Basado en...)
                        </a>
                    </div>"""

target = '<a href="lessons/jlpt-n2-20.html" target="main_frame" class="nav-link">\n                            <span class="nav-num">20</span> ~ばかりか / ~ばかりでなく (No solo...)\n                        </a>\n                    </div>'

if target in index_html and "jlpt-n2-21" not in index_html:
    new_index = index_html.replace(target, target.replace('</div>', n2_menu_items))
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(new_index)
    print("Inyectado Lote 5 N2 en index.html")

print("Ejecutando furigana...")
subprocess.run("python add_furigana.py", shell=True)
print("COMPLETADO LOTE 5 N2")
