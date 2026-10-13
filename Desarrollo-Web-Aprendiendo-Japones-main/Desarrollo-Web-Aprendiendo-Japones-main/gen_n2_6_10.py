import os
import subprocess

data = [
    {
        "id": "jlpt-n2-6",
        "title": "Examen para el JLPT2 - Lección 6",
        "header_title": "JLPT N2 - 準備",
        "desc": "Tema: ~がち (Tendencia) / ~気味 (Ligeramente)",
        "grammar_points": [
            "<strong>～がち (gachi):</strong> Significa 'Tender a...' o 'Ser propenso a...'. Se usa casi siempre para tendencias negativas o indeseables que ocurren a menudo (ej. 'tiende a enfermarse', 'tiende a llegar tarde').",
            "<strong>～気味 (gimi):</strong> Significa 'Tener un ligero toque de...' o 'Sentirse un poco...'. Se usa para expresar un estado físico o mental ligero (ej. 'un poco resfriado', 'un poco cansado')."
        ],
        "examples": [
            ("ja-JP-NanamiNeural", "彼は最近、授業を休みがちだ。", "Él últimamente tiende a faltar a clases a menudo."),
            ("ja-JP-KeitaNeural", "雪の日は、電車が遅れがちになる。", "Los días de nieve, los trenes tienden a retrasarse."),
            ("ja-JP-NanamiNeural", "子どもの頃は病気がちでしたが、今は元気です。", "Cuando era niño tendía a enfermarme, pero ahora estoy saludable."),
            ("ja-JP-KeitaNeural", "一人暮らしだと、野菜が不足しがちです。", "Al vivir solo, se tiende a tener falta de verduras."),
            ("ja-JP-NanamiNeural", "この時計は進みがちなので、気をつけてください。", "Este reloj tiende a adelantarse, así que ten cuidado."),
            ("ja-JP-KeitaNeural", "今日はちょっと風邪気味なので、早く帰ります。", "Hoy me siento con un ligero resfriado, así que me iré a casa temprano."),
            ("ja-JP-NanamiNeural", "最近、少し太り気味なので運動を始めました。", "Últimamente, siento que estoy subiendo un poco de peso, así que empecé a hacer ejercicio."),
            ("ja-JP-KeitaNeural", "新入社員の山田さんは、少し緊張気味に挨拶をした。", "El nuevo empleado, Yamada, saludó sintiéndose un poco nervioso."),
            ("ja-JP-NanamiNeural", "仕事が忙しくて、最近疲れ気味だ。", "El trabajo está ocupado y últimamente me siento un poco cansado."),
            ("ja-JP-KeitaNeural", "試験の結果が悪くて、少し落ち込み気味です。", "Como el resultado del examen fue malo, me siento un poco deprimido.")
        ],
        "dialogue": [
            ("ja-JP-KeitaNeural", "咳をしていますね。風邪気味ですか？", "Estás tosiendo. ¿Te sientes con un ligero resfriado?"),
            ("ja-JP-NanamiNeural", "ええ、昨日の夜から少し熱気味なんです。", "Sí, desde anoche me siento con un poco de fiebre."),
            ("ja-JP-KeitaNeural", "最近、急に寒くなりましたからね。この季節は体調を崩しがちですよ。", "Últimamente ha hecho frío de repente, verdad. En esta estación se tiende a arruinar la salud a menudo."),
            ("ja-JP-NanamiNeural", "本当にそうですね。仕事も忙しくて、寝不足になりがちですし。", "Es muy cierto. El trabajo también está ocupado y tiendo a no dormir lo suficiente."),
            ("ja-JP-KeitaNeural", "無理はしないでください。疲れ気味の時は、温かいお茶を飲むといいですよ。", "No te sobreesforces. Cuando te sientes un poco cansado, es bueno beber té caliente."),
            ("ja-JP-NanamiNeural", "ありがとうございます。田中さんも、最近少しお疲れ気味に見えますよ。", "Muchas gracias. Señor Tanaka, usted también se ve un poco cansado últimamente."),
            ("ja-JP-KeitaNeural", "ははっ、バレましたか。僕も甘いものを食べがちなので、気をつけないと。", "Jaja, ¿me descubriste? Yo también tiendo a comer cosas dulces, así que debo tener cuidado.")
        ],
        "exercises": [
            {
                "q": "雨の日は、事故が起こり（　　　）です。",
                "options": [("がち", True), ("気味", False), ("ばかり", False)]
            },
            {
                "q": "「～気味」 se utiliza principalmente para:",
                "options": [("Un hábito que ocurre muchas veces", False), ("Una condición extrema", False), ("Un estado físico o sensación ligera", True)]
            },
            {
                "q": "昨日からお腹の調子が悪くて、下痢（　　　）だ。",
                "options": [("気味", True), ("がち", False), ("だけ", False)]
            },
            {
                "q": "祖母は最近、忘れ（　　　）になった。",
                "options": [("がち", True), ("気味", False), ("ところだ", False)]
            },
            {
                "q": "「～がち」 normalmente implica una tendencia...",
                "options": [("Positiva", False), ("Negativa", True), ("Mecánica", False)]
            }
        ]
    },
    {
        "id": "jlpt-n2-7",
        "title": "Examen para el JLPT2 - Lección 7",
        "header_title": "JLPT N2 - 準備",
        "desc": "Tema: ~向け / ~向き (Orientado a / Adecuado para)",
        "grammar_points": [
            "<strong>～向け (muke):</strong> Significa 'Orientado a' o 'Hecho específicamente para'. Indica que el creador hizo el producto con ese público en mente (ej. 'Anime hecho para niños').",
            "<strong>～向き (muki):</strong> Significa 'Adecuado para' o 'Ideal para'. Indica que algo encaja bien con cierto público por su naturaleza, sin importar para quién fue creado originalmente (ej. 'Un trabajo adecuado para ella')."
        ],
        "examples": [
            ("ja-JP-NanamiNeural", "このマンションは、一人暮らしの学生向けに作られた。", "Este departamento fue hecho orientado a estudiantes que viven solos."),
            ("ja-JP-KeitaNeural", "この絵本は幼児向けに書かれています。", "Este libro de ilustraciones está escrito orientado a niños pequeños."),
            ("ja-JP-NanamiNeural", "それは海外向けの製品なので、日本では買えません。", "Como ese es un producto orientado al extranjero, no se puede comprar en Japón."),
            ("ja-JP-KeitaNeural", "初心者向けのクラスは、水曜日と金曜日です。", "Las clases orientadas a principiantes son los miércoles y viernes."),
            ("ja-JP-NanamiNeural", "女性向けの雑誌がたくさん売られている。", "Se venden muchas revistas orientadas a mujeres."),
            ("ja-JP-KeitaNeural", "この仕事は体力が必要なので、若い人向きだ。", "Como este trabajo requiere fuerza física, es adecuado para gente joven."),
            ("ja-JP-NanamiNeural", "彼女の性格は、接客業向きだと思います。", "Creo que la personalidad de ella es adecuada para la atención al cliente."),
            ("ja-JP-KeitaNeural", "この料理は辛くないので、子ども向きですね。", "Como esta comida no es picante, es ideal para niños."),
            ("ja-JP-NanamiNeural", "このデザインは少し派手なので、若者向きです。", "Como este diseño es un poco llamativo, encaja bien con los jóvenes."),
            ("ja-JP-KeitaNeural", "左利き向きのハサミを探しています。", "Estoy buscando unas tijeras adecuadas para zurdos.")
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "田中さん、この新しいアプリはどうですか？", "Señor Tanaka, ¿qué le parece esta nueva aplicación?"),
            ("ja-JP-KeitaNeural", "画面がシンプルで使いやすいですね。お年寄り向けのアプリですか？", "La pantalla es simple y fácil de usar. ¿Es una aplicación orientada a ancianos?"),
            ("ja-JP-NanamiNeural", "いいえ、もともとは若者向けに開発されたんです。", "No, originalmente fue desarrollada orientada a jóvenes."),
            ("ja-JP-KeitaNeural", "へえ、そうなんですか。でも、字も大きくて、間違いなくお年寄り向きだと思いますよ。", "Oh, ¿es así? Pero la letra también es grande y creo sin duda que es adecuada para ancianos."),
            ("ja-JP-NanamiNeural", "ええ。だから、今後は海外のシニア層向けにも販売する予定です。", "Sí. Por eso, en el futuro planeamos venderla también orientada a personas mayores en el extranjero."),
            ("ja-JP-KeitaNeural", "それはいいアイデアですね。このデザインは、誰にでも受け入れられる万人向きの良さがあります。", "Esa es una buena idea. Este diseño tiene una bondad adecuada para todo público, aceptable para cualquiera."),
            ("ja-JP-NanamiNeural", "ありがとうございます。子ども向きの楽しい機能も追加したいと考えています。", "Muchas gracias. También estamos pensando en añadir funciones divertidas ideales para niños.")
        ],
        "exercises": [
            {
                "q": "このパンフレットは、外国人観光客（　　　）に作られました。",
                "options": [("向け", True), ("向き", False), ("がち", False)]
            },
            {
                "q": "「～向き」 se refiere a:",
                "options": [("Para quién se fabricó intencionalmente", False), ("Si la naturaleza de algo es adecuada o encaja bien con alguien", True), ("Una tendencia física", False)]
            },
            {
                "q": "彼は優しいから、先生（　　　）だと思う。",
                "options": [("向き", True), ("向け", False), ("気味", False)]
            },
            {
                "q": "初心者（　　　）のカメラを買いました。",
                "options": [("向け", True), ("向き", False), ("だらけ", False)]
            },
            {
                "q": "あの映画は怖すぎるので、子供（　　　）ではない。",
                "options": [("向き", True), ("向け", False), ("ばかり", False)]
            }
        ]
    },
    {
        "id": "jlpt-n2-8",
        "title": "Examen para el JLPT2 - Lección 8",
        "header_title": "JLPT N2 - 準備",
        "desc": "Tema: ~を通じて / ~を通して (A través de / Durante todo...)",
        "grammar_points": [
            "<strong>～を通じて (o tsuujite) / ～を通して (o tooshite):</strong> Ambos significan lo mismo y tienen 2 usos principales:<br>1) 'A través de...' (como medio o intermediario). Ej: Conocerse a través de un amigo.<br>2) 'Durante todo...' (un periodo de tiempo continuo). Ej: Hace calor durante todo el año."
        ],
        "examples": [
            ("ja-JP-NanamiNeural", "友人の紹介を通じて、彼と知り合いました。", "Lo conocí a través de la presentación de un amigo."),
            ("ja-JP-KeitaNeural", "テレビのニュースを通して、その事件を知った。", "Me enteré de ese incidente a través de las noticias de televisión."),
            ("ja-JP-NanamiNeural", "インターネットを通じて、世界中の人と話すことができる。", "A través del internet, se puede hablar con personas de todo el mundo."),
            ("ja-JP-KeitaNeural", "社長の秘書を通して、面会を申し込んだ。", "Solicité la entrevista a través de la secretaria del presidente."),
            ("ja-JP-NanamiNeural", "スポーツを通して、ルールを守る大切さを学んだ。", "A través de los deportes, aprendí la importancia de respetar las reglas."),
            ("ja-JP-KeitaNeural", "この島は、一年を通じて暖かい。", "Esta isla es cálida durante todo el año."),
            ("ja-JP-NanamiNeural", "彼は一生を通して、平和のために働いた。", "Él trabajó por la paz a lo largo de toda su vida."),
            ("ja-JP-KeitaNeural", "四季を通して、さまざまな花が楽しめます。", "A lo largo de las cuatro estaciones, se puede disfrutar de diversas flores."),
            ("ja-JP-NanamiNeural", "その作家は、生涯を通して一度も結婚しなかった。", "Ese escritor, a lo largo de toda su vida, no se casó ni una sola vez."),
            ("ja-JP-KeitaNeural", "この大会は、３日間を通して行われます。", "Este torneo se llevará a cabo a lo largo de los tres días.")
        ],
        "dialogue": [
            ("ja-JP-KeitaNeural", "山田さんとは、どこで知り合ったんですか？", "¿Dónde conociste a Yamada?"),
            ("ja-JP-NanamiNeural", "大学のボランティア活動を通して、知り合いました。", "Nos conocimos a través de las actividades de voluntariado de la universidad."),
            ("ja-JP-KeitaNeural", "そうですか。ボランティア活動を通じて、色々な経験ができたんじゃないですか？", "Ya veo. A través de las actividades de voluntariado, debes haber podido obtener varias experiencias, ¿no?"),
            ("ja-JP-NanamiNeural", "はい。一年を通して、地域の子供たちに英語を教えていました。", "Sí. A lo largo de todo un año, les estuve enseñando inglés a los niños de la zona."),
            ("ja-JP-KeitaNeural", "素晴らしいですね。子供たちも、その活動を通して多くを学んだと思いますよ。", "Qué maravilloso. Creo que los niños también aprendieron mucho a través de esa actividad."),
            ("ja-JP-NanamiNeural", "ええ。教えることを通して、私も成長できたと感じています。", "Sí. A través de la enseñanza, siento que yo también pude crecer."),
            ("ja-JP-KeitaNeural", "本当にそうですね。経験を通して得るものは大きいですから。", "Es muy cierto. Porque lo que se obtiene a través de la experiencia es grande.")
        ],
        "exercises": [
            {
                "q": "私は先輩（　　　）、この会社の社長と知り合いました。",
                "options": [("を通じて", True), ("に限り", False), ("向けに", False)]
            },
            {
                "q": "この町は、一年（　　　）雨が少ないです。",
                "options": [("を通して", True), ("にかけて", False), ("がちで", False)]
            },
            {
                "q": "インターネット（　　　）チケットを予約した。",
                "options": [("を通じて", True), ("ばかりに", False), ("向きに", False)]
            },
            {
                "q": "El uso de 'a través de' indica:",
                "options": [("Un intermediario o medio", True), ("Una tendencia negativa", False), ("Un evento especial", False)]
            },
            {
                "q": "生涯（　　　）、彼は貧しい人々を助けた。",
                "options": [("を通して", True), ("に際して", False), ("ところだった", False)]
            }
        ]
    },
    {
        "id": "jlpt-n2-9",
        "title": "Examen para el JLPT2 - Lección 9",
        "header_title": "JLPT N2 - 準備",
        "desc": "Tema: ~っぽい / ~だらけ (Parece / Lleno de)",
        "grammar_points": [
            "<strong>～っぽい (ppoi):</strong> Significa 'Parece...' o 'Da la sensación de...'. Se usa de forma casual. También significa 'tiende a...' con ciertos verbos (ej. 怒りっぽい = tiende a enojarse), o para describir colores (ej. 白っぽい = blanquecino).",
            "<strong>～だらけ (darake):</strong> Significa 'Lleno de...' o 'Cubierto de...'. Se utiliza CASI SIEMPRE para cosas desagradables o negativas (ej. lleno de basura, cubierto de barro, lleno de errores)."
        ],
        "examples": [
            ("ja-JP-NanamiNeural", "彼はもう大人なのに、子どもっぽい服を着ている。", "Aunque él ya es adulto, lleva ropa que parece de niño (infantil)."),
            ("ja-JP-KeitaNeural", "この牛乳は少し水っぽくて、美味しくない。", "Esta leche se siente un poco acuosa (aguada) y no sabe bien."),
            ("ja-JP-NanamiNeural", "私の弟は怒りっぽいので、すぐにケンカになる。", "Mi hermano menor es propenso a enojarse (irascible), así que de inmediato se pelea."),
            ("ja-JP-KeitaNeural", "母は最近、忘れっぽくなった。", "Mi madre últimamente se ha vuelto olvidadiza."),
            ("ja-JP-NanamiNeural", "あの白っぽい車は、田中さんの車ですか？", "¿Ese auto blanquecino es el auto de Tanaka?"),
            ("ja-JP-KeitaNeural", "大雨の中でサッカーをして、服が泥だらけになった。", "Jugué fútbol en medio de la lluvia fuerte y mi ropa se llenó de barro."),
            ("ja-JP-NanamiNeural", "この文章は間違いだらけで、読めない。", "Este texto está lleno de errores y no se puede leer."),
            ("ja-JP-KeitaNeural", "彼の部屋はゴミだらけで、とても臭い。", "La habitación de él está llena de basura y apesta mucho."),
            ("ja-JP-NanamiNeural", "転んで、足が血だらけになってしまった。", "Me caí y mis piernas se llenaron de sangre."),
            ("ja-JP-KeitaNeural", "あのレストランのテーブルはホコリだらけだ。", "Las mesas de ese restaurante están llenas de polvo.")
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "ねえ、見て。あの男の人、すごく子どもっぽい態度じゃない？", "Oye, mira. Ese hombre, ¿no tiene una actitud muy infantil?"),
            ("ja-JP-KeitaNeural", "ああ、彼ね。いつもあんな感じで、少し怒りっぽいんだよ。", "Ah, él. Siempre es de esa forma, y es un poco irascible (tiende a enojarse)."),
            ("ja-JP-NanamiNeural", "それにしても、彼の服、泥だらけね。何があったの？", "Aun así, su ropa está llena de barro. ¿Qué pasó?"),
            ("ja-JP-KeitaNeural", "さっき、水たまりで転んだらしいよ。可哀想に、靴も傷だらけだ。", "Parece que hace un rato se cayó en un charco de agua. Pobre, sus zapatos también están llenos de rasguños."),
            ("ja-JP-NanamiNeural", "本当だ。あ、そのせいか、少しホコリっぽい匂いがするわ。", "Es cierto. Ah, quizá por eso tiene un olor que parece a polvo."),
            ("ja-JP-KeitaNeural", "うん。でも、彼は忘れっぽいから、明日には転んだことも忘れているよ。", "Sí. Pero como él es olvidadizo, para mañana ya habrá olvidado que se cayó."),
            ("ja-JP-NanamiNeural", "ふふっ、間違いだらけの人生も、彼らしくていいかもしれないわね。", "Jeje, tal vez una vida llena de errores también está bien si es a su estilo.")
        ],
        "exercises": [
            {
                "q": "その白いシャツは、コーヒーをこぼしてシミ（　　　）になった。",
                "options": [("だらけ", True), ("っぽい", False), ("気味", False)]
            },
            {
                "q": "彼は４０歳なのに、話し方が少し子ども（　　　）。",
                "options": [("っぽい", True), ("だらけ", False), ("がち", False)]
            },
            {
                "q": "「～だらけ」 se usa generalmente con:",
                "options": [("Cosas deseables o positivas (dinero, amor)", False), ("Cosas desagradables o negativas (basura, errores)", True), ("Cualquier cosa por igual", False)]
            },
            {
                "q": "このスープは水（　　　）て、全然味がしない。",
                "options": [("っぽく", True), ("だらけ", False), ("を通して", False)]
            },
            {
                "q": "提出されたレポートは、漢字の間違い（　　　）だった。",
                "options": [("だらけ", True), ("っぽい", False), ("気味", False)]
            }
        ]
    },
    {
        "id": "jlpt-n2-10",
        "title": "Examen para el JLPT2 - Lección 10",
        "header_title": "JLPT N2 - 準備",
        "desc": "Tema: ~かねる / ~かねない (Dificultades y Peligros)",
        "grammar_points": [
            "<strong>～かねる (kaneru):</strong> Significa 'Me es difícil...' o 'No puedo...'. Es una forma muy cortés de negación o rechazo en los negocios. Aunque NO lleva forma negativa (Nai), su significado ES negativo.",
            "<strong>～かねない (kanenai):</strong> Significa 'Hay peligro de que...' o 'Podría pasar que...'. Advierte de que un mal resultado es muy posible."
        ],
        "examples": [
            ("ja-JP-NanamiNeural", "申し訳ありませんが、そのご要望にはお応えしかねます。", "Lo siento mucho, pero me resulta imposible (no puedo) responder a su solicitud."),
            ("ja-JP-KeitaNeural", "担当者が不在のため、私ではわかりかねます。", "Como el encargado está ausente, me es difícil saberlo (no sé)."),
            ("ja-JP-NanamiNeural", "その意見には賛成しかねます。", "Me es difícil estar de acuerdo con esa opinión."),
            ("ja-JP-KeitaNeural", "お客様の個人情報はお教えしかねます。", "No podemos (nos es difícil) proporcionarle la información personal de los clientes."),
            ("ja-JP-NanamiNeural", "あまりにもひどい態度に、見るに見かねて注意した。", "Ante una actitud tan terrible, no pudiendo soportar solo mirar, le llamé la atención."),
            ("ja-JP-KeitaNeural", "そんなにスピードを出したら、事故を起こしかねない。", "Si aceleras tanto, existe el peligro de causar un accidente."),
            ("ja-JP-NanamiNeural", "毎日カップラーメンばかり食べていたら、病気になりかねないよ。", "Si comes solo fideos instantáneos todos los días, podrías enfermarte."),
            ("ja-JP-KeitaNeural", "あの二人はいつも喧嘩しているので、別れかねない。", "Esos dos siempre están peleando, por lo que podrían terminar rompiendo."),
            ("ja-JP-NanamiNeural", "このままでは、会社が倒産しかねない。", "Si seguimos así, hay peligro de que la empresa vaya a la quiebra."),
            ("ja-JP-KeitaNeural", "彼なら、そのくらいの悪いことはやりかねない。", "Siendo él, es muy posible que haga algo tan malo como eso.")
        ],
        "dialogue": [
            ("ja-JP-KeitaNeural", "部長、この新しいプロジェクトの予算についてですが...。", "Jefe de departamento, sobre el presupuesto de este nuevo proyecto..."),
            ("ja-JP-NanamiNeural", "これ以上の予算の増額は、会社としても認めかねます。", "Cualquier aumento mayor del presupuesto, como empresa, nos resulta imposible de aprobar."),
            ("ja-JP-KeitaNeural", "しかし、今の予算ではシステムのエラーが起きかねない状況です。", "Sin embargo, con el presupuesto actual es una situación en la que existe el peligro de que ocurran errores en el sistema."),
            ("ja-JP-NanamiNeural", "エラーが起きかねないというのは、具体的にどういうことですか？", "Eso de que hay peligro de errores, ¿a qué te refieres concretamente?"),
            ("ja-JP-KeitaNeural", "テストの時間が足りず、大きなトラブルに発展しかねません。", "El tiempo de pruebas es insuficiente y podría derivar en un gran problema."),
            ("ja-JP-NanamiNeural", "うーん、大きなトラブルになっては困りますね。でも、私の一存では決めかねます。", "Mmm, si se vuelve un gran problema estaremos en aprietos. Pero me es difícil decidirlo por mi propia cuenta."),
            ("ja-JP-KeitaNeural", "承知いたしました。では、社長に見かねて判断していただくしかありませんね。", "Entendido. Entonces, no quedará más remedio que el presidente, al no poder ignorarlo, lo juzgue.")
        ],
        "exercises": [
            {
                "q": "申し訳ありませんが、私にはわかり（　　　）。",
                "options": [("かねます", True), ("かねません", False), ("だらけです", False)]
            },
            {
                "q": "雪道でスピードを出すと、事故を起こし（　　　）。",
                "options": [("かねない", True), ("かねる", False), ("向けだ", False)]
            },
            {
                "q": "「～かねる」 se utiliza principalmente para:",
                "options": [("Rechazar algo educadamente en los negocios", True), ("Pedir un favor", False), ("Expresar un gran peligro", False)]
            },
            {
                "q": "その提案には、どうも納得し（　　　）。",
                "options": [("かねます", True), ("かねません", False), ("気味です", False)]
            },
            {
                "q": "彼なら、平気で嘘をつき（　　　）。",
                "options": [("かねない", True), ("かねる", False), ("っぽい", False)]
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

n2_menu_items = """                        <a href="lessons/jlpt-n2-6.html" target="main_frame" class="nav-link">
                            <span class="nav-num">6</span> ~がち / ~気味 (Tendencia y Sensación)
                        </a>
                        <a href="lessons/jlpt-n2-7.html" target="main_frame" class="nav-link">
                            <span class="nav-num">7</span> ~向け / ~向き (Orientado y Adecuado)
                        </a>
                        <a href="lessons/jlpt-n2-8.html" target="main_frame" class="nav-link">
                            <span class="nav-num">8</span> ~を通じて / ~を通して (A través de / Durante)
                        </a>
                        <a href="lessons/jlpt-n2-9.html" target="main_frame" class="nav-link">
                            <span class="nav-num">9</span> ~っぽい / ~だらけ (Parece / Lleno de)
                        </a>
                        <a href="lessons/jlpt-n2-10.html" target="main_frame" class="nav-link">
                            <span class="nav-num">10</span> ~かねる / ~かねない (Dificultad / Peligro)
                        </a>
                    </div>"""

target = '<a href="lessons/jlpt-n2-5.html" target="main_frame" class="nav-link">\n                            <span class="nav-num">5</span> ~抜く / ~切る (Terminar por completo / Hasta el final)\n                        </a>\n                    </div>'

if target in index_html and "jlpt-n2-6" not in index_html:
    new_index = index_html.replace(target, target.replace('</div>', n2_menu_items))
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(new_index)
    print("Inyectado Lote 2 N2 en index.html")

print("Ejecutando furigana...")
subprocess.run("python add_furigana.py", shell=True)
print("COMPLETADO LOTE 2 N2")
