import os

data = {
    21: {
        "title": "Expresando Pensamientos y Citas",
        "grammar": [
            "<strong>Futsukei + と 思います:</strong> 'Creo que...'. Expresa una opinión. La oración antes de 'to' debe ser informal.",
            "<strong>Futsukei + と 言いました:</strong> 'Dijo que...'. Para citar lo que alguien dijo.",
            "<strong>~でしょう？:</strong> '¿Verdad?'. Para buscar la confirmación del oyente."
        ],
        "examples": [
            ("明日雨が降ると思います。", "1. Creo que mañana lloverá.", "あしたあめがふるとおもいます"),
            ("漢字は難しいと思います。", "2. Creo que los kanjis son difíciles.", "かんじはむずかしいとおもいます"),
            ("田中さんは来ないと思います。", "3. Creo que el Sr. Tanaka no vendrá.", "たなかさんはこないとおもいます"),
            ("山田さんは東京へ行くと言いました。", "4. El Sr. Yamada dijo que irá a Tokio.", "やまださんはとうきょうへいくといいました"),
            ("先生はテストがないと言いました。", "5. El profesor dijo que no hay examen.", "せんせいはテストがないといいました"),
            ("疲れたと言いました。", "6. Dijo que estaba cansado.", "つかれたといいました"),
            ("このカメラは高いでしょう？", "7. Esta cámara es cara, ¿verdad?", "このカメラはたかいでしょう"),
            ("ええ、高いです。", "8. Sí, es cara.", "ええ、たかいです"),
            ("日本料理はおいしいでしょう？", "9. La comida japonesa es rica, ¿verdad?", "にほんりょうりはおいしいでしょう"),
            ("会議室にいると思います。", "10. Creo que está en la sala de reuniones.", "かいぎしつにいるとおもいます")
        ],
        "exercises": [
            {"q": "¿Qué estructura se usa para decir 'Pienso que'?", "options": [{"text": "と言います", "correct": False}, {"text": "と思います", "correct": True}, {"text": "とわかります", "correct": False}]},
            {"q": "'Creo que mañana hará calor':", "options": [{"text": "明日暑いと思います。", "correct": True}, {"text": "明日暑いですと思います。", "correct": False}, {"text": "明日暑かったと思います。", "correct": False}]},
            {"q": "¿Cómo conjugas un sustantivo con 'to omoimasu'? 'Creo que es lluvia':", "options": [{"text": "雨と思います。", "correct": False}, {"text": "雨だと思います。", "correct": True}, {"text": "雨ですと思います。", "correct": False}]},
            {"q": "'El Sr. Yamada dijo que viene mañana':", "options": [{"text": "山田さんは明日来ると言いました。", "correct": True}, {"text": "山田さんは明日来ますと言いました。", "correct": False}, {"text": "山田さんは明日来ると思いました。", "correct": False}]},
            {"q": "¿Qué significa 'でしょう？' al final de la frase?", "options": [{"text": "Probablemente", "correct": False}, {"text": "¿Verdad? (Buscando confirmación)", "correct": True}, {"text": "No lo sé", "correct": False}]},
            {"q": "Persona A: 'Creo que es útil'. Persona B: 'Yo también lo creo':", "options": [{"text": "私はそう思います。", "correct": False}, {"text": "私もそう思います。", "correct": True}, {"text": "私もそう言います。", "correct": False}]},
            {"q": "'Creo que NO es interesante':", "options": [{"text": "面白くないと思います。", "correct": True}, {"text": "面白いじゃないと思います。", "correct": False}, {"text": "面白いと思いました。", "correct": False}]},
            {"q": "'Dijo que NO va' (Verbo ikimasu):", "options": [{"text": "行かないと言いました。", "correct": True}, {"text": "行きないと言いました。", "correct": False}, {"text": "行かないと思いました。", "correct": False}]},
            {"q": "Si algo ya es pregunta ('¿No crees que es caro?'), ¿qué pasa con la partícula 'ka'?", "options": [{"text": "高いと思いませんか。", "correct": True}, {"text": "高いと思いますか。", "correct": False}, {"text": "高いでしょう。", "correct": False}]},
            {"q": "'Esta ciudad es tranquila, ¿verdad?' (Shizuka - Adj-na):", "options": [{"text": "この町は静かでしょう？", "correct": True}, {"text": "この町は静かだでしょう？", "correct": False}, {"text": "この町は静かですでしょう？", "correct": False}]}
        ]
    },
    22: {
        "title": "Modificadores de Sustantivos N5",
        "grammar": [
            "<strong>Futsukei + Sustantivo:</strong> Un verbo en estilo informal puede describir a un sustantivo directamente. Ej: 読む本 (El libro que voy a leer).",
            "<strong>Partícula が:</strong> En la oración que modifica, el sujeto se marca con が, no con は. Ej: 私が書いた手紙 (La carta que YO escribí).",
            "<strong>Tiempo / Promesa / Asunto + V(dic):</strong> 'Tiempo para...', 'Promesa de...'. Ej: 買い物に行く時間 (Tiempo para ir de compras)."
        ],
        "examples": [
            ("これは私が撮った写真です。", "1. Esta es la foto que tomé.", "これはわたしがとったしゃしんです"),
            ("昨日買った傘をなくしました。", "2. Perdí el paraguas que compré ayer.", "きのうかったかさをなくしました"),
            ("どんな家が欲しいですか。", "3. ¿Qué tipo de casa quieres?", "どんないえがほしいですか"),
            ("広い庭がある家が欲しいです。", "4. Quiero una casa que tenga un jardín amplio.", "ひろいにわがあるいえがほしいです"),
            ("あそこで新聞を読んでいる人は誰ですか。", "5. ¿Quién es la persona que está leyendo el periódico allá?", "あそこでしんぶんをよんでいるひとはだれですか"),
            ("木村さんです。", "6. Es el Sr. Kimura.", "きむらさんです"),
            ("映画を見る時間がありません。", "7. No tengo tiempo para ver una película.", "えいがをみるじかんがありません"),
            ("友達に会う約束があります。", "8. Tengo el compromiso (promesa) de encontrarme con un amigo.", "ともだちにあうやくそくがあります"),
            ("市役所へ行く用事があります。", "9. Tengo un asunto de ir a la alcaldía.", "しやくしょへいくようじがあります"),
            ("母が作ったケーキはおいしいです。", "10. El pastel que hizo mi madre es delicioso.", "ははがつくったケーキはおいしいです")
        ],
        "exercises": [
            {"q": "¿Cómo se dice 'El libro que yo compré'?", "options": [{"text": "私が本を買った", "correct": False}, {"text": "私が買った本", "correct": True}, {"text": "買った私の本", "correct": False}]},
            {"q": "¿Qué partícula marca al sujeto dentro de una frase modificadora? (La carta que CARLOS escribió):", "options": [{"text": "は", "correct": False}, {"text": "を", "correct": False}, {"text": "が", "correct": True}]},
            {"q": "'La persona que está comiendo pan':", "options": [{"text": "パンを食べている人", "correct": True}, {"text": "人を食べているパン", "correct": False}, {"text": "パンを食べるの人", "correct": False}]},
            {"q": "'Quiero una casa que tenga piscina':", "options": [{"text": "プールがあった家が欲しいです。", "correct": False}, {"text": "プールがある家が欲しいです。", "correct": True}, {"text": "家がプールがある欲しいです。", "correct": False}]},
            {"q": "¿Cómo se dice 'Tiempo para leer libros'?", "options": [{"text": "本を読むの時間", "correct": False}, {"text": "本を読む時間", "correct": True}, {"text": "本を読んで時間", "correct": False}]},
            {"q": "'Tengo un compromiso para ver una película con un amigo':", "options": [{"text": "友達と映画を見る約束があります。", "correct": True}, {"text": "友達と映画を見た約束があります。", "correct": False}, {"text": "友達と映画を見る用事があります。", "correct": False}]},
            {"q": "¿Qué significa '用事があります' (Youji ga arimasu)?", "options": [{"text": "Tener un asunto pendiente / algo que hacer", "correct": True}, {"text": "Tener tiempo", "correct": False}, {"text": "Estar cansado", "correct": False}]},
            {"q": "'Este es el reloj que me dio mi padre' (Reloj = tokei):", "options": [{"text": "父にもらった時計", "correct": True}, {"text": "父がもらった時計", "correct": False}, {"text": "時計にもらった父", "correct": False}]},
            {"q": "¿Cuál es correcta para 'La foto que tomé en Kioto'?", "options": [{"text": "京都に撮った写真", "correct": False}, {"text": "京都で撮った写真", "correct": True}, {"text": "京都へ撮った写真", "correct": False}]},
            {"q": "Persona A: '¿Viste el libro que compré?'", "options": [{"text": "私が買った本を見ましたか。", "correct": True}, {"text": "私の買った本を見ましたか。(También es gramaticalmente correcto usar 'no' en subordinadas, pero 'ga' es lo estándar que se enseña)", "correct": True}, {"text": "Ambas son correctas en gramática japonesa.", "correct": True}]}
        ]
    },
    23: {
        "title": "Condiciones temporales (とき / と)",
        "grammar": [
            "<strong>Futsukei + とき:</strong> 'Cuando...'. Verbo Diccionario (acción en futuro/progreso) o Verbo TA (acción terminada).",
            "<strong>Sustantivo + の + とき:</strong> Ej: 子供のとき (Cuando era niño).",
            "<strong>V(dic) + と:</strong> 'Si haces A, inevitablemente ocurre B'. Se usa para máquinas, direcciones y fenómenos naturales."
        ],
        "examples": [
            ("図書館で本を借りるとき、カードが要ります。", "1. Cuando pides prestado un libro, necesitas una tarjeta.", "としょかんでほんをかりるとき、カードがいります"),
            ("道がわからないとき、私に聞いてください。", "2. Cuando no sepas el camino, pregúntame.", "みちがわからないとき、わたしにきいてください"),
            ("子供のとき、よく川で泳ぎました。", "3. Cuando era niño, nadaba mucho en el río.", "こどものとき、よくかわでおよぎました"),
            ("パリへ行くとき、時計を買いました。", "4. Cuando iba (en el camino) a París, compré un reloj.", "パリへいくとき、とけいをかいました"),
            ("パリへ行ったとき、時計を買いました。", "5. Cuando fui (después de llegar) a París, compré un reloj.", "パリへいったとき、とけいをかいました"),
            ("このボタンを押すと、お釣りが出ます。", "6. Si presionas este botón, sale el cambio.", "このボタンをおすと、おつりででます"),
            ("これを右へ曲がると、郵便局があります。", "7. Si giras esto a la derecha, hay una oficina de correos.", "これをみぎへまがると、ゆうびんきょくがあります"),
            ("暇なとき、遊びに来てください。", "8. Cuando estés libre, ven a visitarme.", "ひまなとき、あそびにきてください"),
            ("妻が病気のとき、私が料理をします。", "9. Cuando mi esposa está enferma, yo cocino.", "つまがびょうきのとき、わたしがりょうりをします"),
            ("眠いとき、コーヒーを飲みます。", "10. Cuando tengo sueño, bebo café.", "ねむいとき、コーヒーをのみます")
        ],
        "exercises": [
            {"q": "¿Qué palabra se usa para 'Cuando / En el momento de...'?", "options": [{"text": "から", "correct": False}, {"text": "まで", "correct": False}, {"text": "とき", "correct": True}]},
            {"q": "¿Cómo conectas un Sustantivo con とき? 'Cuando era estudiante':", "options": [{"text": "学生とき", "correct": False}, {"text": "学生のとき", "correct": True}, {"text": "学生なとき", "correct": False}]},
            {"q": "¿Cómo conectas un Adjetivo-na con とき? 'Cuando estoy libre (Hima)':", "options": [{"text": "暇のとき", "correct": False}, {"text": "暇なとき", "correct": True}, {"text": "暇とき", "correct": False}]},
            {"q": "¿Cómo conectas un Adjetivo-i con とき? 'Cuando hace calor (Atsui)':", "options": [{"text": "暑いとき", "correct": True}, {"text": "暑いのとき", "correct": False}, {"text": "暑なとき", "correct": False}]},
            {"q": "'Compré un regalo ANTES de llegar a Tokio (V.Diccionario)':", "options": [{"text": "東京へ行くとき、お土産を買いました。", "correct": True}, {"text": "東京へ行ったとき、お土産を買いました。", "correct": False}, {"text": "東京へ行くと、お土産を買いました。", "correct": False}]},
            {"q": "'Compré un regalo DESPUÉS de llegar a Tokio (V.Ta)':", "options": [{"text": "東京へ行くとき、お土産を買いました。", "correct": False}, {"text": "東京へ行ったとき、お土産を買いました。", "correct": True}, {"text": "東京へ行くと、お土産を買いました。", "correct": False}]},
            {"q": "¿Qué partícula se usa para causa y efecto inevitable (Ej. Botones de máquinas)?", "options": [{"text": "が", "correct": False}, {"text": "と", "correct": True}, {"text": "で", "correct": False}]},
            {"q": "'Si giras a la izquierda, está el banco':", "options": [{"text": "左へ曲がるから、銀行があります。", "correct": False}, {"text": "左へ曲がると、銀行があります。", "correct": True}, {"text": "左へ曲がるのとき、銀行があります。", "correct": False}]},
            {"q": "'Cuando no entiendo, pregunto al profesor':", "options": [{"text": "わからないとき、先生に聞きます。", "correct": True}, {"text": "わからなかったとき、先生に聞きます。", "correct": False}, {"text": "わかるのとき、先生に聞きます。", "correct": False}]},
            {"q": "'Si presionas el botón, sale jugo':", "options": [{"text": "ボタンを押すとき、ジュースが出ます。", "correct": False}, {"text": "ボタンを押すと、ジュースが出ます。", "correct": True}, {"text": "ボタンを押すから、ジュースが出ます。", "correct": False}]}
        ]
    },
    24: {
        "title": "Dar y Recibir acciones N5",
        "grammar": [
            "<strong>N を くれます:</strong> 'Me da a mí'. Alguien te da un objeto.",
            "<strong>V(te) あげます:</strong> 'Hacer un favor a alguien'. (Tú a él o él a ella).",
            "<strong>V(te) もらいます:</strong> 'Recibir un favor de alguien'. El sujeto es quien recibe la acción.",
            "<strong>V(te) くれます:</strong> 'Me hace un favor a mí'. El sujeto es la persona que realiza la acción."
        ],
        "examples": [
            ("佐藤さんは私にプレゼントをくれました。", "1. La Sra. Sato me dio un regalo.", "さとうさんはわたしにプレゼントをくれました"),
            ("私は木村さんに本を貸してあげました。", "2. Yo le presté (hice el favor de prestar) un libro a Kimura.", "わたしはきむらさんにほんをかしてあげました"),
            ("山田さんに電話番号を教えてもらいました。", "3. Recibí el favor de que Yamada me enseñara el número.", "やまださんにでんわばんごうをおしえてもらいました"),
            ("母は私にセーターを送ってくれました。", "4. Mi madre me envió (hizo el favor de enviar) un suéter.", "はははわたしにセーターをおくってくれました"),
            ("誰に手伝ってもらいましたか。", "5. ¿De quién recibiste ayuda?", "だれにてつだってもらいましたか"),
            ("鈴木さんに手伝ってもらいました。", "6. Recibí ayuda del Sr. Suzuki.", "すずきさんにてつだってもらいました"),
            ("誰が手伝ってくれましたか。", "7. ¿Quién te ayudó?", "だれがてつだってくれましたか"),
            ("鈴木さんが手伝ってくれました。", "8. El Sr. Suzuki me ayudó.", "すずきさんがてつだってくれました"),
            ("私はおじいさんの荷物を持ってあげました。", "9. Le cargué el equipaje al abuelo.", "わたしはおじいさんのにもつをもつてあげました"),
            ("友達が私を迎えに来てくれました。", "10. Mi amigo vino a recogerme.", "ともだちがわたしをむかえにきてくれました")
        ],
        "exercises": [
            {"q": "¿Qué verbo usas si alguien te da un objeto A TI?", "options": [{"text": "くれます", "correct": True}, {"text": "あげます", "correct": False}, {"text": "もらいます", "correct": False}]},
            {"q": "'YO le preparé café a María' (V-te + ?):", "options": [{"text": "いれてあげました。", "correct": True}, {"text": "いれてもらいました。", "correct": False}, {"text": "いれてくれました。", "correct": False}]},
            {"q": "'María me explicó el problema A MÍ' (El sujeto es María):", "options": [{"text": "説明してくれました。", "correct": True}, {"text": "説明してあげました。", "correct": False}, {"text": "説明してもらいました。", "correct": False}]},
            {"q": "'YO recibí la explicación de María' (El sujeto soy Yo):", "options": [{"text": "私がマリアさんに説明してもらいました。", "correct": True}, {"text": "私がマリアさんに説明してくれました。", "correct": False}, {"text": "マリアさんが私に説明してもらいました。", "correct": False}]},
            {"q": "¿Por qué hay que tener cuidado al usar '~てあげます' con un jefe?", "options": [{"text": "Porque suena como si le estuvieras haciendo un gran favor desde una posición superior.", "correct": True}, {"text": "Porque es gramaticalmente incorrecto.", "correct": False}, {"text": "Porque los jefes no reciben favores.", "correct": False}]},
            {"q": "Persona A: '¡Qué bonita camisa!'. Persona B: 'Mi hermana mayor me la compró'.", "options": [{"text": "姉が買ってくれました。", "correct": True}, {"text": "私が姉に買ってくれました。", "correct": False}, {"text": "姉が買ってあげました。", "correct": False}]},
            {"q": "Si tú le prestas dinero a un amigo (Kashimasu):", "options": [{"text": "お金を貸してあげました。", "correct": True}, {"text": "お金を貸してくれました。", "correct": False}, {"text": "お金を貸してもらいました。", "correct": False}]},
            {"q": "Si pides prestado dinero a un banco (Karimasu):", "options": [{"text": "お金を借りてもらいました。", "correct": False}, {"text": "お金を借りました。(No se usa ageru/morau aquí, Karimasu ya implica recibir temporalmente)", "correct": True}, {"text": "お金を借りてくれました。", "correct": False}]},
            {"q": "¿Qué partícula marca a la persona de la que recibes un favor en '~てもらいます'?", "options": [{"text": "は", "correct": False}, {"text": "に / から", "correct": True}, {"text": "を", "correct": False}]},
            {"q": "¿Qué partícula marca al benefactor (el que hace la acción) en '~てくれます'?", "options": [{"text": "が / は", "correct": True}, {"text": "を", "correct": False}, {"text": "に", "correct": False}]}
        ]
    },
    25: {
        "title": "Condicionales N5 (たら / ても)",
        "grammar": [
            "<strong>Forma TA + ら:</strong> 'Si...' o 'Cuando... (futuro)'. Ej: 雨が降ったら (Si llueve).",
            "<strong>V(te) も:</strong> 'Aunque... / A pesar de...'. Ej: 雨が降っても (Aunque llueva).",
            "<strong>もし ~たら:</strong> 'En caso de que...' (Suposición).",
            "<strong>いくら ~ても:</strong> 'Por mucho que...'."
        ],
        "examples": [
            ("雨が降ったら、行きません。", "1. Si llueve, no iré.", "あめがふったら、いきません"),
            ("雨が降っても、行きます。", "2. Aunque llueva, iré.", "あめがふっても、いきます"),
            ("明日晴れたら、ピクニックに行きましょう。", "3. Si mañana está despejado, vayamos de picnic.", "あしたはれたら、ピクニックにいきましょう"),
            ("安かったら、パソコンを買いたいです。", "4. Si está barata, quiero comprar la computadora.", "やすかったら、パソコンをかいたいです"),
            ("お金がなかったら、どうしますか。", "5. Si no tuvieras dinero, ¿qué harías?", "おかねがなかったら、どうしますか"),
            ("駅に着いたら、電話をください。", "6. Cuando (una vez que) llegues a la estación, llámame.", "えきについたら、でんわをください"),
            ("いくら考えても、わかりません。", "7. Por mucho que lo piense, no lo entiendo.", "いくらかんがえても、わかりません"),
            ("もし一億円あったら、何をしたいですか。", "8. Si (hipotéticamente) tuvieras 100 millones, ¿qué harías?", "もしいちおくえんあったら、なにをしたいですか"),
            ("年を取っても、働きたいです。", "9. Aunque envejezca, quiero trabajar.", "としをとっても、はたらきたいです"),
            ("日曜日でも、仕事をします。", "10. Aunque sea domingo, trabajaré.", "にちようびでも、しごとをします")
        ],
        "exercises": [
            {"q": "¿Cómo se forma el condicional 'Si...' (〜ら)?", "options": [{"text": "Forma TA + ら", "correct": True}, {"text": "Forma Diccionario + ら", "correct": False}, {"text": "Forma Nai + ら", "correct": False}]},
            {"q": "'Si como' (Taberu):", "options": [{"text": "食べたら", "correct": True}, {"text": "食べるら", "correct": False}, {"text": "食べったら", "correct": False}]},
            {"q": "'Si es barato' (Yasui - Adj-i):", "options": [{"text": "安かったら", "correct": True}, {"text": "安いら", "correct": False}, {"text": "安いたら", "correct": False}]},
            {"q": "'Si estoy libre' (Hima - Adj-na):", "options": [{"text": "暇だったら", "correct": True}, {"text": "暇なら", "correct": False}, {"text": "暇たら", "correct": False}]},
            {"q": "¿Qué adverbio se usa a menudo con 〜たら para indicar suposición ('En caso de que')?", "options": [{"text": "いくら (Ikura)", "correct": False}, {"text": "もし (Moshi)", "correct": True}, {"text": "とても (Totemo)", "correct": False}]},
            {"q": "¿Cómo se dice 'Aunque / A pesar de'?", "options": [{"text": "V(te) も", "correct": True}, {"text": "V(ta) ら", "correct": False}, {"text": "V(nai) と", "correct": False}]},
            {"q": "'Aunque llueva, juego fútbol':", "options": [{"text": "雨が降っても、サッカーをします。", "correct": True}, {"text": "雨が降ったら、サッカーをします。", "correct": False}, {"text": "雨が降ると、サッカーをします。", "correct": False}]},
            {"q": "'Por mucho que piense, no lo entiendo':", "options": [{"text": "いくら考えても、わかりません。", "correct": True}, {"text": "もし考えても、わかりません。", "correct": False}, {"text": "いくら考えたら、わかりません。", "correct": False}]},
            {"q": "'Aunque sea domingo (sustantivo), trabajo':", "options": [{"text": "日曜日でも、働きます。", "correct": True}, {"text": "日曜日ても、働きます。", "correct": False}, {"text": "日曜日だったら、働きます。", "correct": False}]},
            {"q": "¿Se puede usar 〜たら para cosas seguras en el futuro? Ej: 'Cuando llegue a casa, te llamo'.", "options": [{"text": "Sí, significa 'Una vez que ocurra'.", "correct": True}, {"text": "No, solo es para suposiciones imposibles.", "correct": False}, {"text": "No, hay que usar 'toki' obligatoriamente.", "correct": False}]}
        ]
    }
}

def generate():
    base_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\lessons"
    
    for i in range(21, 26):
        d = data[i]
        
        grammar_html = ""
        for g in d["grammar"]:
            grammar_html += f"                <li>{g}</li>\n"
            
        examples_html = ""
        for ex in d["examples"]:
            examples_html += f'''        <div class="practice-item"><div class="practice-content"><div class="text-jp">{ex[0]}</div><div class="text-es">{ex[1]}</div></div><button class="audio-btn" onclick="playAudio('{ex[2]}')">🔊</button></div>\n'''
            
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

        html = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Examen para el JLPT5 - Lección {i}</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=Noto+Sans+JP:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../css/style.css">
</head>
<body class="iframe-body">
    <div class="max-w-4xl">
        <div class="lesson-header-simple">
            <span>JLPT N5 - 準備</span>
            <h1>Examen para el JLPT5 - Lección {i}</h1>
            <p class="lesson-desc">Tema: {d["title"]}</p>
        </div>

        <div class="video-link-section" style="text-align: center; margin: 2rem 0; padding: 2.5rem; background: linear-gradient(135deg, var(--secondary-color) 0%, #2a2a4a 100%); border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
            <h3 style="color: white; margin-bottom: 0.5rem; font-size: 1.5rem;">🎬 Clase en Video</h3>
            <p style="color: #cbd5e0; margin-bottom: 1.5rem; font-size: 1.05rem;">Estudia los fundamentos del nivel N5 en el canal de Kira Sensei.</p>
            <a href="https://www.youtube.com/results?search_query=Kira+Sensei+JLPT+N5" target="_blank" style="display: inline-block; background: var(--primary-color); color: white; padding: 1rem 2.5rem; border-radius: 50px; text-decoration: none; font-weight: 700; font-size: 1.15rem; transition: transform 0.2s, box-shadow 0.2s; box-shadow: 0 4px 15px rgba(224, 42, 77, 0.4);" onmouseover="this.style.transform='translateY(-3px)'; this.style.boxShadow='0 6px 20px rgba(224, 42, 77, 0.6)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 15px rgba(224, 42, 77, 0.4)'">Buscar Videos N5 en YouTube</a>
        </div>

        <h2 class="section-title">📚 Gramática Principal</h2>
        <div class="grammar-note">
            <ul>
{grammar_html}            </ul>
        </div>
        
        <h2 class="section-title">🌟 10 Ejemplos de Uso</h2>
        <div class="grammar-note"><p>A continuación, 10 ejemplos clave para dominar este tema en el examen N5.</p></div>
{examples_html}
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

        with open(os.path.join(base_dir, f"jlpt-n5-{i}.html"), "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated JLPT N5 Lesson {i}")

if __name__ == '__main__':
    generate()
