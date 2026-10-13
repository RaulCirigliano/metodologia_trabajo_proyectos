import os
import subprocess

data = {
    6: {
        "title": "Decisiones y Funciones (~にする / ~ことになる / ~ようになっている)",
        "grammar": [
            "<strong>N + にする:</strong> Expresa una decisión personal sobre una opción (elegir algo). Ej. コーヒーにします (Me decido por un café).",
            "<strong>V(dic/nai) + ことになる:</strong> Se ha decidido que... (Decisión externa, reglas o destino). Ej. 来月、出張することになりました (Se decidió que iré de viaje de negocios el próximo mes).",
            "<strong>V(dic/nai) + ようになっている:</strong> Describe el mecanismo o la función automática de una máquina o sistema. Ej. このドアは自動で閉まるようになっている (Esta puerta está hecha para cerrarse automáticamente)."
        ],
        "examples": [
            ("私はハンバーグにします。", "1. Yo me decido por la hamburguesa (al pedir en un restaurante).", "わたしはハンバーグにします"),
            ("今年の旅行はハワイに行くことにしました。", "2. Hemos decidido ir a Hawái para el viaje de este año (Decisión propia).", "ことしのりょこうはハワイにいくことにしました"),
            ("来月から大阪に転勤することになりました。", "3. Se ha decidido que me trasladarán a Osaka a partir del próximo mes.", "らいげつからおおさかにてんきんすることになりました"),
            ("このボタンを押すと、お釣りが出るようになっています。", "4. Si presionas este botón, el sistema está hecho para que salga el cambio.", "このボタンをおすと、おつりでるようになっています"),
            ("うちの会社では、金曜日はカジュアルな服でいいことになっている。", "5. En nuestra empresa, la regla es que los viernes está bien usar ropa casual.", "うちのかいしゃでは、きんようびはカジュアルなふくでいいことになっている"),
            ("このストーブは、倒れると火が消えるようになっています。", "6. Esta estufa está diseñada para que el fuego se apague si se cae.", "このストーブは、たおれるとひがきえるようになっています"),
            ("明日の会議は午後３時からということになった。", "7. Se ha decidido que la reunión de mañana será desde las 3 p.m.", "あしたのかいぎはごごさんじからということになった"),
            ("A: 飲み物は何になさいますか。 B: 紅茶にします。", "8. A: ¿Qué desea de beber? B: Tomaré té negro.", "のみものはなにになさいますか。こうちゃにします"),
            ("パスワードを３回間違えると、ロックされるようになっています。", "9. Si te equivocas de contraseña 3 veces, el sistema está diseñado para bloquearse.", "パスワードをさんかいまちがえると、ロックされるようになっています"),
            ("やっぱり、パソコンを買わないことにしました。", "10. Al final, decidí no comprar la computadora.", "やっぱり、パソコンをかわないことにしました")
        ],
        "exercises": [
            {"q": "Estás en un restaurante y decides pedir un café. ¿Cómo lo dices?", "options": [{"text": "コーヒーにします", "correct": True}, {"text": "コーヒーになります", "correct": False}, {"text": "コーヒーをします", "correct": False}]},
            {"q": "Para expresar que algo se ha decidido por causas externas o reglas (ej. te transfieren de sucursal):", "options": [{"text": "～ことになった", "correct": True}, {"text": "～ことにした", "correct": False}, {"text": "～ようになった", "correct": False}]},
            {"q": "¿Qué expresión se usa para describir cómo funciona una máquina automáticamente?", "options": [{"text": "～ようになっている", "correct": True}, {"text": "～ことにしている", "correct": False}, {"text": "～ようとしている", "correct": False}]},
            {"q": "'Decidí estudiar en Japón' (Fue tu propia elección):", "options": [{"text": "日本に留学することにしました", "correct": True}, {"text": "日本に留学することになりました", "correct": False}, {"text": "日本に留学するようになっています", "correct": False}]},
            {"q": "'Si abres esta puerta, suena una alarma (está hecho así)':", "options": [{"text": "アラームが鳴るようになっています", "correct": True}, {"text": "アラームが鳴ることにしています", "correct": False}, {"text": "アラームが鳴るようにしました", "correct": False}]},
            {"q": "'La regla de la escuela es no usar el móvil' (Regla establecida):", "options": [{"text": "使わないことになっている", "correct": True}, {"text": "使わないようにしている", "correct": False}, {"text": "使わないことにしている", "correct": False}]},
            {"q": "Diferencia: '～ことにしている' vs '～ことになっている'. ¿Cuál indica una REGLA externa u oficial?", "options": [{"text": "～ことになっている", "correct": True}, {"text": "～ことにしている", "correct": False}, {"text": "Ambas son iguales", "correct": False}]},
            {"q": "Eliges la camisa roja en una tienda: 'Me quedo con la roja' (Aka):", "options": [{"text": "赤にします", "correct": True}, {"text": "赤になります", "correct": False}, {"text": "赤をします", "correct": False}]},
            {"q": "'El calentador se apaga automáticamente si la habitación se calienta':", "options": [{"text": "消えるようになっています", "correct": True}, {"text": "消えることにしています", "correct": False}, {"text": "消えるようにします", "correct": False}]},
            {"q": "Se canceló el viaje por el mal tiempo (Decisión forzada):", "options": [{"text": "旅行は中止になりました", "correct": True}, {"text": "旅行は中止にしました", "correct": False}, {"text": "旅行は中止のようになっています", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "田中さん、新しいプロジェクトのリーダーになったそうですね。おめでとうございます。", "Tanaka, escuché que te has convertido en el líder del nuevo proyecto. Felicidades."),
            ("ja-JP-KeitaNeural", "ありがとうございます。実は昨日、部長から言われて、急にリーダーをやることになったんです。", "Gracias. La verdad es que me lo dijo el jefe ayer, y se decidió de repente que yo sería el líder."),
            ("ja-JP-NanamiNeural", "それは大変ですね。でも、素晴らしいチャンスじゃないですか。", "Eso debe ser duro. Pero, ¿no es una gran oportunidad?"),
            ("ja-JP-KeitaNeural", "ええ、だから頑張ることにしました。", "Sí, por eso he decidido esforzarme."),
            ("ja-JP-NanamiNeural", "この新しいシステム、少し複雑ですね。どう使うんですか。", "Este nuevo sistema es un poco complejo, ¿verdad? ¿Cómo se usa?"),
            ("ja-JP-KeitaNeural", "ああ、これはデータを入力すると、自動的にグラフができるようになっているんです。", "Ah, este está diseñado para que, al ingresar los datos, se cree un gráfico automáticamente."),
            ("ja-JP-NanamiNeural", "へえ、便利ですね。私も使ってみることにします。", "Anda, qué útil. Yo también decidiré intentar usarlo.")
        ]
    },
    7: {
        "title": "Dar y Recibir Nivel Intermedio (~てもらう / ~てくれる / ~てあげる)",
        "grammar": [
            "<strong>A に V(て)もらう:</strong> Yo (o alguien de mi grupo) recibo el favor de que A haga algo. Ej. 友達に手伝ってもらった (Mi amigo me hizo el favor de ayudarme).",
            "<strong>A が/は V(て)くれる:</strong> A (otra persona) hace algo por mí (o por mi grupo) amablemente. Ej. 友達が手伝ってくれた (Mi amigo me ayudó).",
            "<strong>A に V(て)あげる:</strong> Yo le hago un favor a A. Ej. 弟に本を読んであげた (Le leí un libro a mi hermanito). <em>Nota: No se usa 'ageru' con superiores porque suena arrogante.</em>"
        ],
        "examples": [
            ("先生に作文を直してもらいました。", "1. El profesor me hizo el favor de corregir mi redacción.", "せんせいのにさくぶんをなおしてもらいました"),
            ("山田さんが駅まで車で送ってくれました。", "2. Yamada me hizo el favor de llevarme a la estación en coche.", "やまださんがえきまでくるまでおくってくれました"),
            ("おばあさんの荷物を持ってあげました。", "3. Le hice el favor a la anciana de llevarle el equipaje.", "おばあさんのにもつをもってもあげました"),
            ("父が新しいパソコンを買ってくれました。", "4. Mi padre me compró una computadora nueva.", "ちちがあたらしいパソコンをかってくれました"),
            ("友達に引っ越しを手伝ってもらうつもりです。", "5. Tengo la intención de recibir la ayuda de un amigo para la mudanza.", "ともだちにひっこしを手伝ってもらうつもりです"),
            ("私が写真を撮ってあげましょうか。", "6. ¿Quieres que te haga el favor de tomar la foto?", "わたしがしゃしんをとってあげましょうか"),
            ("日本語がわからないので、田中さんに翻訳してもらいました。", "7. Como no entiendo japonés, Tanaka me hizo el favor de traducirlo.", "にほんごがわからないので、たなかさんにほんやくしてもらいました"),
            ("雨が降っていたので、彼が傘を貸してくれた。", "8. Como estaba lloviendo, él me prestó un paraguas.", "あめがふっていたので、かれがかさをかしてくれた"),
            ("子供に絵本を読んであげている。", "9. Le estoy leyendo un libro de cuentos a mi hijo.", "こどもにえほんをよんであげている"),
            ("道に迷ったとき、親切な人が道を教えてくれました。", "10. Cuando me perdí, una persona amable me enseñó el camino.", "みちにまよったとき、しんせつなひとがみちをおしえてくれました")
        ],
        "exercises": [
            {"q": "¿Qué verbo usas si tú recibes un favor y el SUJETO gramatical (marcado con は o が) eres TÚ?", "options": [{"text": "～てもらう", "correct": True}, {"text": "～てくれる", "correct": False}, {"text": "～てあげる", "correct": False}]},
            {"q": "¿Qué verbo usas si el SUJETO (marcado con は o が) es la persona que hace el favor hacia ti?", "options": [{"text": "～てくれる", "correct": True}, {"text": "～てもらう", "correct": False}, {"text": "～てあげる", "correct": False}]},
            {"q": "'Tanaka me prestó dinero': 田中さんがお金を___。", "options": [{"text": "貸してくれた", "correct": True}, {"text": "貸してもらった", "correct": False}, {"text": "貸してあげた", "correct": False}]},
            {"q": "'Recibí el favor de que Tanaka me prestara dinero' (Sujeto: Yo): 田中さんに___。", "options": [{"text": "貸してもらった", "correct": True}, {"text": "貸してくれた", "correct": False}, {"text": "貸してあげた", "correct": False}]},
            {"q": "¿Por qué es de mala educación usar '～てあげる' (te hago un favor) con tu jefe?", "options": [{"text": "Porque suena condescendiente y arrogante.", "correct": True}, {"text": "Porque el jefe no necesita favores.", "correct": False}, {"text": "Porque 'ageru' solo se usa para cosas físicas, no acciones.", "correct": False}]},
            {"q": "'Le expliqué el camino a la abuela': おばあさんに道を___。", "options": [{"text": "教えてあげた", "correct": True}, {"text": "教えてくれた", "correct": False}, {"text": "教えてもらった", "correct": False}]},
            {"q": "'Mi madre me hizo un pastel': 母がケーキを___。", "options": [{"text": "作ってくれた", "correct": True}, {"text": "作ってもらった", "correct": False}, {"text": "作ってあげた", "correct": False}]},
            {"q": "'Me repararon el coche' (Recibí el favor del mecánico): 修理のひとに車を___。", "options": [{"text": "直してもらった", "correct": True}, {"text": "直してくれた", "correct": False}, {"text": "直してあげた", "correct": False}]},
            {"q": "'(Yo) te lo llevaré' (Ofreciendo un favor a un amigo): 私が持って___。", "options": [{"text": "あげるよ", "correct": True}, {"text": "くれるよ", "correct": False}, {"text": "もらうよ", "correct": False}]},
            {"q": "Si un amigo te ayuda, ¿quién recibe el marcador に en la oración de 'てもらう'?", "options": [{"text": "El amigo (友達に手伝ってもらう)", "correct": True}, {"text": "Yo (私に手伝ってもらう)", "correct": False}, {"text": "Nadie, se usa を", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "そのマフラー、とても素敵ですね。自分で編んだんですか。", "Esa bufanda es muy bonita. ¿La tejiste tú mismo?"),
            ("ja-JP-KeitaNeural", "いいえ、これは母が編んでくれたんです。誕生日のプレゼントに。", "No, me la tejió mi madre. Como regalo de cumpleaños."),
            ("ja-JP-NanamiNeural", "お母様が！いいですね。私は編み物ができないので、いつもお店で買っています。", "¡Tu madre! Qué bien. Como yo no sé tejer, siempre las compro en las tiendas."),
            ("ja-JP-KeitaNeural", "そうなんですか。じゃあ、今度母に、マリアさんの分も編んでもらいましょうか。", "¿Ah sí? Entonces, la próxima vez, ¿quieres que le pida a mi madre que teja una para ti también? (que reciba el favor de mi madre)"),
            ("ja-JP-NanamiNeural", "えっ、そんなの悪いですよ！", "¡Eh, me da pena! (Sería molestia)"),
            ("ja-JP-KeitaNeural", "大丈夫ですよ。母は編み物が好きだから、きっと喜んで編んでくれると思います。", "No te preocupes. A mi madre le gusta tejer, así que seguro que te la tejerá con gusto."),
            ("ja-JP-NanamiNeural", "本当ですか？それなら、毛糸は私が買ってあげます！", "¿De verdad? En ese caso, ¡yo le haré el favor de comprar la lana!")
        ]
    },
    8: {
        "title": "Pasiva y Causativa-Pasiva (~れる / ~られる / ~させられる)",
        "grammar": [
            "<strong>Pasiva (れる/られる):</strong> Ser afectado por una acción. A menudo expresa molestia (pasiva de sufrimiento). Ej. 弟にケーキを食べられた (Mi hermano menor se comió mi pastel [y yo lo sufro]).",
            "<strong>Causativa (せる/させる):</strong> Hacer que alguien haga algo (Obligar o dejar/permitir). Ej. 母は子供に野菜を食べさせた (La madre obligó/hizo que el niño comiera verduras).",
            "<strong>Causativa-Pasiva (させられる):</strong> Ser obligado a hacer algo en contra de tu voluntad. Ej. 母に野菜を食べさせられた (Fui obligado a comer verduras por mi madre)."
        ],
        "examples": [
            ("電車の中で足を踏まれました。", "1. En el tren me pisaron el pie (y me molestó).", "でんしゃのなかであしをふまれました"),
            ("雨に降られて、服が濡れてしまった。", "2. Llovió (fui afectado por la lluvia) y mi ropa se mojó.", "あめにふられて、ふくがぬれてしまった"),
            ("先生は学生に宿題をたくさんさせた。", "3. El profesor hizo (obligó) a los estudiantes a hacer mucha tarea.", "せんせいはがくせいにしゅくだいをたくさんさせた"),
            ("私は先生に宿題をたくさんさせられた。", "4. Yo fui obligado a hacer mucha tarea por el profesor.", "わたしはせんせいにしゅくだいをたくさんさせられた"),
            ("子供のころ、母にピアノを習わせられました。", "5. Cuando era niño, fui obligado por mi madre a aprender a tocar el piano.", "こどものころ、ははにピアノをならわせられました"),
            ("昨日、友達に一時間も待たされた。", "6. Ayer, fui obligado a esperar una hora por mi amigo (me hicieron esperar).", "きのう、ともだちにいちじかんもまたされた"),
            ("社長に歌を歌わされた。", "7. Fui obligado por el presidente a cantar una canción.", "しゃちょうにうたをうたわされた"),
            ("犬に手を噛まれました。", "8. El perro me mordió la mano.", "いぬにてをかまれました"),
            ("親は子供に好きなことをさせてあげるべきだ。", "9. Los padres deberían dejar/permitir a los niños hacer lo que les gusta.", "おやはこどもにすきなことをさせてあげるべきだ"),
            ("お酒を飲まされたので、今日は車を運転できません。", "10. Como me obligaron a beber alcohol, hoy no puedo conducir.", "おさけをのまされたので、きょうはくるまをうんてんできません")
        ],
        "exercises": [
            {"q": "¿Cuál es la forma pasiva de '踏む' (fumu - pisar)?", "options": [{"text": "踏まれる", "correct": True}, {"text": "踏ませる", "correct": False}, {"text": "踏まさせる", "correct": False}]},
            {"q": "La pasiva se usa a menudo en japonés para expresar qué emoción respecto a la acción?", "options": [{"text": "Molestia o sufrimiento (Ej. Me pisaron el pie)", "correct": True}, {"text": "Alegría y agradecimiento", "correct": False}, {"text": "Intención futura", "correct": False}]},
            {"q": "¿Cuál es la forma causativa (obligar/dejar) de '食べる' (taberu)?", "options": [{"text": "食べさせる", "correct": True}, {"text": "食べられる", "correct": False}, {"text": "食べさせられる", "correct": False}]},
            {"q": "¿Qué expresa la forma causativa-pasiva (させられる - saserareru)?", "options": [{"text": "Ser obligado a hacer algo en contra de tu voluntad", "correct": True}, {"text": "Hacer que alguien haga algo obligatoriamente", "correct": False}, {"text": "Hacer un favor a alguien", "correct": False}]},
            {"q": "Para los verbos del Grupo 1 (U -> A), hay una versión corta de la causativa-pasiva. Ej. 待たせられる se convierte en:", "options": [{"text": "待たされる (Matasareru)", "correct": True}, {"text": "待たれる (Matareru)", "correct": False}, {"text": "待ちさせる (Machisaseru)", "correct": False}]},
            {"q": "'Me hicieron esperar 2 horas' (Matsu):", "options": [{"text": "２時間待たされた", "correct": True}, {"text": "２時間待った", "correct": False}, {"text": "２時間待たせた", "correct": False}]},
            {"q": "'Llovió y me afectó' (Furu -> Furu en pasiva):", "options": [{"text": "雨に降られた", "correct": True}, {"text": "雨に降らせた", "correct": False}, {"text": "雨に降らされた", "correct": False}]},
            {"q": "'Mi madre me obligó a comer verduras' (Sujeto: Yo):", "options": [{"text": "母に野菜を食べさせられた", "correct": True}, {"text": "母に野菜を食べさせた", "correct": False}, {"text": "母に野菜を食べられた", "correct": False}]},
            {"q": "'El jefe me obligó a beber cerveza' (Nomu):", "options": [{"text": "部長にビールを飲まされた", "correct": True}, {"text": "部長にビールを飲まれた", "correct": False}, {"text": "部長にビールを飲ませた", "correct": False}]},
            {"q": "Cuando dices '弟にケーキを食べられた', ¿qué significa realmente?", "options": [{"text": "Mi hermano se comió el pastel (y yo estoy triste/molesto por ello)", "correct": True}, {"text": "Yo le di el pastel a mi hermano", "correct": False}, {"text": "Mi hermano me obligó a comer el pastel", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-KeitaNeural", "あーあ、最悪な一日だったよ。", "Ahhh, fue un día terrible."),
            ("ja-JP-NanamiNeural", "どうしたの？疲れているみたいだけど。", "¿Qué pasó? Pareces cansado."),
            ("ja-JP-KeitaNeural", "朝、電車の中で知らない人に足を踏まれて、すごく痛かったんだ。", "Por la mañana, en el tren, un desconocido me pisó el pie y me dolió mucho."),
            ("ja-JP-NanamiNeural", "それは災難だったね。", "Eso fue un desastre."),
            ("ja-JP-KeitaNeural", "それだけじゃないよ。会社では、部長に長いレポートを書かされたんだ。", "No solo eso. En la empresa, fui obligado por el jefe a escribir un reporte largo."),
            ("ja-JP-NanamiNeural", "書かされたの？自分の仕事じゃなかったの？", "¿Fuiste obligado a escribirlo? ¿No era tu trabajo?"),
            ("ja-JP-KeitaNeural", "違うよ。他の人の仕事なのに、僕がやらされたんだ。", "No. Aunque era el trabajo de otra persona, me hicieron hacerlo a mí."),
            ("ja-JP-NanamiNeural", "大変だったね。今日はゆっくり休んで。", "Qué duro. Descansa bien hoy."),
            ("ja-JP-KeitaNeural", "うん。でも、帰りに急に雨に降られて、濡れちゃったよ...", "Sí. Pero de camino a casa llovió de repente (fui afectado por la lluvia) y me mojé...")
        ]
    },
    9: {
        "title": "Condicionales avanzadas (~ば / ~なら / ~と / ~たら)",
        "grammar": [
            "<strong>~ば (Ba):</strong> Condición lógica y general. 'Si haces X, ocurre Y'. Ej. 安ければ買います (Si es barato, lo compro).",
            "<strong>~なら (Nara):</strong> Respondiendo a un contexto o información previa. 'Si es el caso de que...'. Ej. 東京へ行くなら、新幹線が便利です (Si [es cierto que] vas a Tokio, el Shinkansen es conveniente).",
            "<strong>~と (To):</strong> Condición inevitable o automática. 'Siempre que X, inevitablemente Y'. Ej. 春になると、桜が咲く (Cuando llega la primavera, los cerezos florecen).",
            "<strong>~たら (Tara):</strong> Si/Cuando ocurra X (después de que ocurra), haré Y. Uso muy general y seguro en conversaciones. Ej. 家に着いたら、電話します (Cuando/Si llego a casa, te llamaré)."
        ],
        "examples": [
            ("天気が良ければ、ピクニックに行きましょう。", "1. Si hace buen tiempo, vayamos de picnic (Ba).", "てんきがよければ、ピクニックにいきましょう"),
            ("A: 寒いです。 B: 寒いなら、窓を閉めてください。", "2. A: Hace frío. B: Si hace frío (en ese caso), cierra la ventana (Nara).", "さむいなら、まどをしめてください"),
            ("このボタンを押すと、ドアが開きます。", "3. Si presionas este botón, la puerta se abre (To - Automático).", "このボタンをおすと、ドアがあきます"),
            ("夏休みになったら、海へ行きたいです。", "4. Cuando lleguen las vacaciones de verano, quiero ir al mar (Tara).", "なつやすみになったら、うみへいきたいです"),
            ("質問があれば、聞いてください。", "5. Si tienes alguna pregunta, por favor hazla (Ba).", "しつもんがあれば、きいてください"),
            ("パソコンを買うなら、あの店がいいですよ。", "6. Si vas a comprar una PC (dado que lo mencionaste), esa tienda es buena (Nara).", "パソコンをかうなら、あのみせがいいですよ"),
            ("まっすぐ行くと、右手に銀行があります。", "7. Si vas recto, a mano derecha hay un banco (To - Indicaciones).", "まっすぐいくと、みぎてにぎんこうがあります"),
            ("雨が降ったら、試合は中止になります。", "8. Si llueve (en el caso de que), el partido se cancelará (Tara).", "あめがふったら、しあいはちゅうしになります"),
            ("もっと練習しなければ、上手になれませんよ。", "9. Si no practicas más, no podrás volverte bueno (Ba negativo).", "もっとれんしゅうしなければ、じょうずになれませんよ"),
            ("明日暇なら、一緒に映画を見に行きませんか。", "10. Si estás libre mañana (en ese caso), ¿vamos a ver una película? (Nara con Na-adj).", "あしたひまなら、いっしょにえいがをみにいきませんか")
        ],
        "exercises": [
            {"q": "¿Qué condicional se usa predominantemente para dar indicaciones de lugares o describir funciones de máquinas?", "options": [{"text": "～と (To)", "correct": True}, {"text": "～なら (Nara)", "correct": False}, {"text": "～ば (Ba)", "correct": False}]},
            {"q": "¿Qué condicional toma el contexto que acaba de decir el hablante anterior para dar un consejo o sugerencia?", "options": [{"text": "～なら (Nara)", "correct": True}, {"text": "～と (To)", "correct": False}, {"text": "～ば (Ba)", "correct": False}]},
            {"q": "A: 'Quiero comer sushi'. B: 'Si quieres comer sushi, te recomiendo este restaurante'.", "options": [{"text": "寿司を食べるなら、この店がお勧めです。", "correct": True}, {"text": "寿司を食べると、この店がお勧めです。", "correct": False}, {"text": "寿司を食べれば、この店がお勧めです。", "correct": False}]},
            {"q": "'Cuando llegue a casa, te llamaré' (La acción de llamar sucederá DESPUÉS de llegar).", "options": [{"text": "家に着いたら、電話します。", "correct": True}, {"text": "家に着くと、電話します。", "correct": False}, {"text": "家に着けば、電話します。", "correct": False}]},
            {"q": "Forma BA del adjetivo やすい (Yasui - barato): 'Si es barato...'", "options": [{"text": "安ければ", "correct": True}, {"text": "安いば", "correct": False}, {"text": "安かったら", "correct": False}]},
            {"q": "Forma BA de un verbo negativo: 行かない (Ikanai - no ir) -> 'Si no vas...'", "options": [{"text": "行かなければ", "correct": True}, {"text": "行かないば", "correct": False}, {"text": "行ったら", "correct": False}]},
            {"q": "'Si giras a la derecha, verás la estación' (Automático / Indicación):", "options": [{"text": "右に曲がると、駅が見えます。", "correct": True}, {"text": "右に曲がるなら、駅が見えます。", "correct": False}, {"text": "右に曲がったら、駅が見えます。", "correct": False}]},
            {"q": "'Si tuvieras 1 millón de yenes, ¿qué harías?' (Situación hipotética):", "options": [{"text": "１００万円あったら、どうしますか。", "correct": True}, {"text": "１００万円あると、どうしますか。", "correct": False}, {"text": "１００万円あるなら、どうしますか。", "correct": False}]},
            {"q": "¿Cuál es la forma BA de する (Suru)?", "options": [{"text": "すれば", "correct": True}, {"text": "すらば", "correct": False}, {"text": "しろば", "correct": False}]},
            {"q": "'Si eres estudiante (Gakusei), es más barato' (Sustantivo + なら):", "options": [{"text": "学生なら、安いです。", "correct": True}, {"text": "学生と、安いです。", "correct": False}, {"text": "学生ば、安いです。", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-KeitaNeural", "来週、初めて京都へ旅行に行くんですが、どこかおすすめの場所はありますか。", "La próxima semana viajaré a Kioto por primera vez. ¿Tienes algún lugar recomendado?"),
            ("ja-JP-NanamiNeural", "京都へ行くなら、金閣寺と清水寺は絶対に行ったほうがいいですよ。", "Si vas a Kioto (tomando tu contexto), definitivamente deberías ir al Kinkakuji y al Kiyomizudera."),
            ("ja-JP-KeitaNeural", "ありがとうございます。でも、バスの乗り方が少し不安です。", "Gracias. Pero estoy un poco inseguro de cómo subir al autobús."),
            ("ja-JP-NanamiNeural", "大丈夫ですよ。京都駅からバスに乗れば、どこへでも行けます。バス停には英語の案内もありますし。", "No pasa nada. Si te subes a un autobús desde la estación de Kioto (condición general), puedes ir a cualquier parte. En las paradas hay información en inglés."),
            ("ja-JP-KeitaNeural", "それは安心しました。たくさん写真を撮ってきますね。", "Eso me alivia. Tomaré muchas fotos."),
            ("ja-JP-NanamiNeural", "いい写真が撮れたら、後で見せてくださいね。", "Cuando hayas tomado buenas fotos, muéstramelas luego, ¿vale?"),
            ("ja-JP-KeitaNeural", "はい、もちろん！", "¡Sí, por supuesto!")
        ]
    },
    10: {
        "title": "Lenguaje Honorífico y Humilde (尊敬語 y 謙譲語)",
        "grammar": [
            "<strong>Sonkeigo (尊敬語 - Honorífico):</strong> Se usa para elevar al interlocutor o a la persona de la que hablas (clientes, jefes). Acciones hechas por ELLOS.",
            "<em>Especiales:</em> 行く/来る/いる -> いらっしゃる, 食べる/飲む -> 召し上がる, 言う -> おっしゃる, する -> なさる, 見る -> ご覧になる.",
            "<em>Regular:</em> お + V(masu) + になる. Ej. お帰りになる.",
            "<strong>Kenjougo (謙譲語 - Humilde):</strong> Se usa para rebajar TUS propias acciones (o las de tu grupo) y mostrar respeto al receptor.",
            "<em>Especiales:</em> 行く/来る -> 参る, いる -> おる, 食べる/飲む -> いただく, 言う -> 申す, する -> いたす, 見る -> 拝見する.",
            "<em>Regular:</em> お/ご + V(masu) + する/いたす. Ej. ご案内します."
        ],
        "examples": [
            ("社長はもうお帰りになりました。", "1. El presidente ya se ha ido a casa (Sonkeigo regular).", "しゃちょうはもうおかえりになりました"),
            ("先生、何をお召し上がりになりますか。", "2. Profesor, ¿qué va a comer/beber? (Sonkeigo especial).", "せんせい、なにをおめしあがりになりますか"),
            ("お客様がいらっしゃいました。", "3. El cliente ha llegado/venido (Sonkeigo especial).", "おきゃくさまがいらっしゃいました"),
            ("その件につきましては、私が社長にお伝えします。", "4. Sobre ese asunto, yo se lo comunicaré al presidente (Kenjougo regular).", "そのけんにつきましては、わたしがしゃちょうにおつたえします"),
            ("私は山田と申します。", "5. Yo me llamo Yamada (Kenjougo especial).", "わたしはやまだともうします"),
            ("明日、３時に社長室へ伺います。", "6. Mañana a las 3 visitaré la oficina del presidente (Kenjougo de Iku/Kiku).", "あした、さんじにしゃちょうしつへうかがいます"),
            ("先生の新しい本を拝見しました。", "7. Vi/Leí el nuevo libro del profesor (Kenjougo especial de Miru).", "せんせいのあたらしいほんをはいけんしました"),
            ("どうぞ、こちらのパンフレットをご覧になってください。", "8. Por favor, mire este folleto (Sonkeigo especial de Miru).", "どうぞ、こちらのパンフレットをごらんになってください"),
            ("駅までご案内いたします。", "9. Le guiaré hasta la estación (Kenjougo regular: ご + sustantivo + いたす).", "えきまでごあんないいたします"),
            ("部長がそうおっしゃるなら、間違いないでしょう。", "10. Si el jefe lo dice, seguro que no hay error (Sonkeigo especial de Iu).", "ぶちょうがそうおっしゃるなら、まちがいないでしょう")
        ],
        "exercises": [
            {"q": "¿El lenguaje Honorífico (Sonkeigo) se usa para describir las acciones de quién?", "options": [{"text": "Del interlocutor (Ej. cliente, jefe)", "correct": True}, {"text": "Mías", "correct": False}, {"text": "De mi familia", "correct": False}]},
            {"q": "¿El lenguaje Humilde (Kenjougo) se usa para describir las acciones de quién?", "options": [{"text": "Mías o de las personas de mi grupo/empresa", "correct": True}, {"text": "Del cliente", "correct": False}, {"text": "Del presidente de la empresa rival", "correct": False}]},
            {"q": "¿Cuál es el verbo HONORÍFICO (Sonkeigo) especial para 行く / 来る / いる?", "options": [{"text": "いらっしゃる", "correct": True}, {"text": "参る (Mairu)", "correct": False}, {"text": "申す (Mousu)", "correct": False}]},
            {"q": "¿Cuál es el verbo HUMILDE (Kenjougo) especial para 行く / 来る?", "options": [{"text": "参る (Mairu)", "correct": True}, {"text": "いらっしゃる", "correct": False}, {"text": "なさる", "correct": False}]},
            {"q": "Para decir 'El cliente COME' (Honorífico de Taberu):", "options": [{"text": "召し上がる (Meshiagaru)", "correct": True}, {"text": "いただく (Itadaku)", "correct": False}, {"text": "お食べになる", "correct": False}]},
            {"q": "Para decir 'Yo COMO/RECIBO' (Humilde de Taberu / Morau):", "options": [{"text": "いただく (Itadaku)", "correct": True}, {"text": "召し上がる", "correct": False}, {"text": "お食べする", "correct": False}]},
            {"q": "El profesor DICE (Honorífico de Iu):", "options": [{"text": "おっしゃる", "correct": True}, {"text": "申す (Mousu)", "correct": False}, {"text": "お言いになる", "correct": False}]},
            {"q": "YO DIGO / Me llamo... (Humilde de Iu):", "options": [{"text": "申す (Mousu)", "correct": True}, {"text": "おっしゃる", "correct": False}, {"text": "お言いする", "correct": False}]},
            {"q": "El cliente MIRA (Honorífico de Miru):", "options": [{"text": "ご覧になる (Goran ni naru)", "correct": True}, {"text": "拝見する (Haiken suru)", "correct": False}, {"text": "お見になる", "correct": False}]},
            {"q": "YO MIRO (Humilde de Miru, ej. vi su correo):", "options": [{"text": "拝見する (Haiken suru)", "correct": True}, {"text": "ご覧になる", "correct": False}, {"text": "お見する", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "いらっしゃいませ。株式会社XYZでございます。", "Bienvenido. Es la corporación XYZ."),
            ("ja-JP-KeitaNeural", "私、ABC会社の山田と申します。佐藤部長はいらっしゃいますか。", "Yo me llamo Yamada, de la compañía ABC (Humilde de decir). ¿Está el director Sato? (Honorífico de estar)."),
            ("ja-JP-NanamiNeural", "山田様ですね。いつもお世話になっております。申し訳ございません、佐藤は現在席を外しております。", "Señor Yamada. Gracias por todo siempre. Lo siento mucho, Sato no se encuentra en su asiento en este momento (Humilde de la empresa propia)."),
            ("ja-JP-KeitaNeural", "そうですか。何時ごろお戻りになりますか。", "Ya veo. ¿Alrededor de qué hora regresará? (Honorífico regular de regresar)."),
            ("ja-JP-NanamiNeural", "３時ごろには戻ると申しておりました。お戻りになりましたら、こちらからお電話いたしましょうか。", "Dijo (él mismo en humilde hacia afuera) que regresaría sobre las 3. Cuando regrese (Honorífico), ¿quiere que le llamemos desde aquí? (Humilde)."),
            ("ja-JP-KeitaNeural", "はい、お願いいたします。後ほど、こちらからおかけ直しいたしますので、よろしくお伝えください。", "Sí, se lo ruego. Más tarde le volveré a llamar yo, así que por favor transmítaselo (Honorífico regular)."),
            ("ja-JP-NanamiNeural", "承知いたしました。佐藤にそのようにお伝えいたします。", "Entendido (Humilde de saber). Se lo comunicaré a Sato de esa manera (Humilde regular).")
        ]
    }
}

base_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\lessons"
audio_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\audio"
os.makedirs(audio_dir, exist_ok=True)

for i in range(6, 11):
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
for i in range(6, 11):
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
