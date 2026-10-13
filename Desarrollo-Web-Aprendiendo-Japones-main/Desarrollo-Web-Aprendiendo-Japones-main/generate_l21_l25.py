import os

data = {
    21: {
        "title": "Pensamientos, Citas y Confirmaciones",
        "grammar": [
            "<strong>Futsukei (Informal) + と 思います:</strong> 'Pienso que... / Creo que...'. La oración citada debe estar en estilo informal antes de la partícula と.",
            "<strong>Futsukei + と 言いました:</strong> 'Dijo que...'. Cita directa (entre comillas) o cita indirecta (Futsukei).",
            "<strong>Futsukei + でしょう？:</strong> '..., ¿verdad? / ..., ¿no es así?'. Para confirmar algo con el oyente."
        ],
        "examples": [
            ("明日雨が降ると思います。", "1. Creo que mañana lloverá.", "あしたあめがふるとおもいます"),
            ("首相は来月アメリカへ行くと言いました。", "2. El Primer Ministro dijo que irá a Estados Unidos el próximo mes.", "しゅしょうはらいげつアメリカへいくといいました"),
            ("東京は人が多いでしょう？", "3. Tokio tiene mucha gente, ¿verdad?", "とうきょうはひとがおおいでしょう？"),
            ("ええ、多いです。", "4. Sí, tiene mucha.", "ええ、おおいです"),
            ("ファクスは便利ですね。", "5. El fax es conveniente, ¿no?", "ファクスはべんりですね"),
            ("日本の物価が高いと思います。", "6. Creo que los precios en Japón son altos.", "にほんのぶっかがたかいとおもいます"),
            ("ミラーさんはどこですか。", "7. ¿Dónde está el Sr. Miller?", "ミラーさんはどこですか"),
            ("会議室にいると思います。", "8. Creo que está en la sala de reuniones.", "かいぎしつにいるとおもいます"),
            ("彼は何と言いましたか。", "9. ¿Qué dijo él?", "かれはなんといいましたか"),
            ("疲れたと言いました。", "10. Dijo que estaba cansado.", "つかれたといいました")
        ],
        "exercises": [
            {"q": "¿Qué estructura se usa para decir 'Pienso que / Creo que'?", "options": [{"text": "と 言います (to iimasu)", "correct": False}, {"text": "と 思います (to omoimasu)", "correct": True}, {"text": "と わかります (to wakarimasu)", "correct": False}]},
            {"q": "'Creo que mañana hará frío':", "options": [{"text": "明日寒いですと思います。", "correct": False}, {"text": "明日寒いと思います。", "correct": True}, {"text": "明日寒かったと思います。", "correct": False}]},
            {"q": "'Creo que NO es interesante' (Negativo de omoshiroi + to omoimasu):", "options": [{"text": "面白くないと思います。", "correct": True}, {"text": "面白いと思いません。", "correct": True}, {"text": "Ambas son correctas en la conversación.", "correct": True}]},
            {"q": "¿Cómo conjugas un sustantivo con 'to omoimasu'? 'Creo que ES lluvia':", "options": [{"text": "雨と思います。", "correct": False}, {"text": "雨だと思います。", "correct": True}, {"text": "雨ですと思います。", "correct": False}]},
            {"q": "'El Sr. Yamada dijo que viene mañana':", "options": [{"text": "山田さんは明日来ると言いました。", "correct": True}, {"text": "山田さんは明日来ますと言いました。", "correct": False}, {"text": "山田さんは明日来ると思います。", "correct": False}]},
            {"q": "¿Qué significa '~でしょう？' (deshou?) al final de una frase con entonación ascendente?", "options": [{"text": "Probablemente.", "correct": False}, {"text": "¿Verdad? / ¿No es así? (Buscando confirmación).", "correct": True}, {"text": "No lo creo.", "correct": False}]},
            {"q": "'Ese libro es interesante, ¿verdad?':", "options": [{"text": "その本は面白いでしょう？", "correct": True}, {"text": "その本は面白かったでしょう？", "correct": False}, {"text": "その本は面白くないでしょう？", "correct": False}]},
            {"q": "Persona A: 'Creo que los teléfonos son útiles'. Persona B: 'Yo también lo creo'.", "options": [{"text": "私もそう思います。", "correct": True}, {"text": "私はそう思います。", "correct": False}, {"text": "私もそう言います。", "correct": False}]},
            {"q": "Persona A: 'Creo que está durmiendo'.", "options": [{"text": "寝ていると思います。", "correct": True}, {"text": "寝ますと思います。", "correct": False}, {"text": "寝てと思います。", "correct": False}]},
            {"q": "¿Qué pasa con la partícula 'ka' (か) si la frase ya es una pregunta? '¿No crees que es caro?'", "options": [{"text": "高いと思いませんか。", "correct": True}, {"text": "高いと思いますか。", "correct": False}, {"text": "高いと思いますが。", "correct": False}]}
        ]
    },
    22: {
        "title": "Oraciones Modificadoras de Sustantivos",
        "grammar": [
            "<strong>Futsukei + Sustantivo:</strong> Un verbo en estilo informal puede modificar directamente a un sustantivo para describirlo. Ej: 私が買った本 (El libro que yo compré).",
            "<strong>Sujeto en oración subordinada:</strong> Cuando hay un sujeto dentro de la frase que modifica al sustantivo, se marca con が, no con は. Ej: 妻が作ったケーキ (El pastel que hizo mi esposa).",
            "<strong>Sustantivo + 時間/約束/用事:</strong> 'Tiempo para...', 'Cita/Promesa para...', 'Asunto para...' + Verbo en Forma Diccionario. Ej: 買い物に行く時間 (Tiempo para ir de compras)."
        ],
        "examples": [
            ("これは私が撮った写真です。", "1. Esta es la foto que yo tomé.", "これはわたしがとったしゃしんです"),
            ("カリナさんが描いた絵はどれですか。", "2. ¿Cuál es el dibujo que pintó Karina?", "カリナさんがかいたえはどれですか"),
            ("あの着物を着ている人は誰ですか。", "3. ¿Quién es la persona que lleva puesto aquel kimono?", "あのきものをきているひとはだれですか"),
            ("木村さんです。", "4. Es la señora Kimura.", "きむらさんです"),
            ("昨日買った傘をなくしました。", "5. Perdí el paraguas que compré ayer.", "きのうかったかさをなくしました"),
            ("どんな家が欲しいですか。", "6. ¿Qué clase de casa quieres?", "どんないえがほしいですか"),
            ("広い庭がある家が欲しいです。", "7. Quiero una casa que tenga un jardín amplio.", "ひろいにわがあるいえがほしいです"),
            ("今晩飲みに行きませんか。", "8. ¿No quieres ir a beber esta noche?", "こんばんのみにいきませんか"),
            ("すみません、今晩は友達に会う約束があります。", "9. Lo siento, esta noche tengo una promesa/cita de encontrarme con un amigo.", "すみません、こんばんはともだちにあうやくそくがあります"),
            ("今日は市役所へ行く用事があります。", "10. Hoy tengo un asunto de ir a la alcaldía.", "きょうはしやくしょへいくようじがあります")
        ],
        "exercises": [
            {"q": "¿Cómo se dice 'El libro que yo compré'?", "options": [{"text": "私が本を買った", "correct": False}, {"text": "私が買った本", "correct": True}, {"text": "買った私の本", "correct": False}]},
            {"q": "¿Qué partícula marca al sujeto DENTRO de una frase modificadora? (Ej. La torta que MI ESPOSA hizo)", "options": [{"text": "は (wa)", "correct": False}, {"text": "が (ga)", "correct": True}, {"text": "を (wo)", "correct": False}]},
            {"q": "'La persona que está leyendo el periódico':", "options": [{"text": "新聞を読んでいる人", "correct": True}, {"text": "人を読んでいる新聞", "correct": False}, {"text": "新聞を読むの人", "correct": False}]},
            {"q": "'Perdí el reloj que recibí de mi padre':", "options": [{"text": "父にもらった時計をなくしました。", "correct": True}, {"text": "父にもらう時計をなくしました。", "correct": False}, {"text": "時計は父にもらったなくしました。", "correct": False}]},
            {"q": "'Quiero una casa que tenga piscina':", "options": [{"text": "プールがある家が欲しいです。", "correct": True}, {"text": "プールがあった家が欲しいです。", "correct": False}, {"text": "家がプールがある欲しいです。", "correct": False}]},
            {"q": "¿Qué verbo se usa para 'Llevar puesto' (en la parte superior o cuerpo completo, como un Kimono o Camisa)?", "options": [{"text": "履いています (Haite imasu)", "correct": False}, {"text": "着ています (Kite imasu)", "correct": True}, {"text": "かぶっています (Kabutte imasu)", "correct": False}]},
            {"q": "¿Cómo se dice 'Tiempo para leer libros'?", "options": [{"text": "本を読む時間", "correct": True}, {"text": "本を読むの時間", "correct": False}, {"text": "本を読んで時間", "correct": False}]},
            {"q": "'Tengo una promesa/cita para ver una película con un amigo':", "options": [{"text": "友達と映画を見る約束があります。", "correct": True}, {"text": "友達と映画を見た約束があります。", "correct": False}, {"text": "友達と映画を見る用事があります。", "correct": False}]},
            {"q": "¿Qué significa '用事があります' (Youji ga arimasu)?", "options": [{"text": "Tener tiempo", "correct": False}, {"text": "Tener un asunto / algo que hacer", "correct": True}, {"text": "Estar enfermo", "correct": False}]},
            {"q": "'Esta es la torta que hizo María':", "options": [{"text": "これはマリアさんが作ったケーキです。", "correct": True}, {"text": "これはマリアさんが作るケーキです。", "correct": False}, {"text": "これはマリアさんを作るケーキです。", "correct": False}]}
        ]
    },
    23: {
        "title": "Cuando (とき) e Inevitabilidad (と)",
        "grammar": [
            "<strong>Futsukei + とき:</strong> 'Cuando... / En el momento de...'. Los verbos usan forma Diccionario (acción futura o en progreso) o forma TA (acción terminada). Los Adjetivos-i mantienen 'i', Adj-na añaden 'na', Sustantivos añaden 'no'.",
            "<strong>V(dic) + と、V2:</strong> 'Cuando A, inevitablemente ocurre B'. Se usa para fenómenos naturales, máquinas (presionas el botón y sale jugo), o direcciones."
        ],
        "examples": [
            ("図書館で本を借りるとき、カードが要ります。", "1. Cuando pides prestado un libro en la biblioteca, necesitas una tarjeta.", "としょかんでほんをかりるとき、カードがいります"),
            ("道がわからないとき、私に聞いてください。", "2. Cuando no sepas el camino, pregúntame.", "みちがわからないとき、わたしにきいてください"),
            ("子供のとき、よく川で泳ぎました。", "3. Cuando era niño, a menudo nadaba en el río.", "こどものとき、よくかわでおよぎました"),
            ("パリへ行くとき、時計を買いました。", "4. Cuando iba (en camino) a París, compré un reloj.", "パリへいくとき、とけいをかいました"),
            ("パリへ行ったとき、時計を買いました。", "5. Cuando fui (ya estaba en) París, compré un reloj.", "パリへいったとき、とけいをかいました"),
            ("このボタンを押すと、お釣りが出ます。", "6. Si (cuando) presionas este botón, sale el cambio.", "このボタンをおすと、おつりででます"),
            ("これを右へ曲がると、郵便局があります。", "7. Si (cuando) giras esto a la derecha, hay una oficina de correos.", "これをみぎへまがると、ゆうびんきょくがあります"),
            ("眠いとき、コーヒーを飲みます。", "8. Cuando tengo sueño, bebo café.", "ねむいとき、コーヒーをのみます"),
            ("暇なとき、遊びに来てください。", "9. Cuando estés libre, por favor ven a visitarme.", "ひまなとき、あそびにきてください"),
            ("妻が病気のとき、私が料理をします。", "10. Cuando mi esposa está enferma, yo cocino.", "つまがびょうきのとき、わたしがりょうりをします")
        ],
        "exercises": [
            {"q": "¿Qué palabra se usa para decir 'Cuando...' o 'En el momento en que...'?", "options": [{"text": "から (kara)", "correct": False}, {"text": "とき (toki)", "correct": True}, {"text": "まで (made)", "correct": False}]},
            {"q": "¿Cómo conectas un Sustantivo con とき? 'Cuando era estudiante':", "options": [{"text": "学生とき", "correct": False}, {"text": "学生のとき", "correct": True}, {"text": "学生なとき", "correct": False}]},
            {"q": "¿Cómo conectas un Adjetivo-i con とき? 'Cuando hace calor':", "options": [{"text": "暑いとき", "correct": True}, {"text": "暑いのとき", "correct": False}, {"text": "暑なとき", "correct": False}]},
            {"q": "¿Cómo conectas un Adjetivo-na con とき? 'Cuando estoy libre':", "options": [{"text": "暇とき", "correct": False}, {"text": "暇なとき", "correct": True}, {"text": "暇のとき", "correct": False}]},
            {"q": "'Compré un regalo antes de llegar a Tokio (en el camino)' (V.Diccionario):", "options": [{"text": "東京へ行くとき、お土産を買いました。", "correct": True}, {"text": "東京へ行ったとき、お土産を買いました。", "correct": False}, {"text": "東京へ行くと、お土産を買いました。", "correct": False}]},
            {"q": "'Compré un regalo DESPUÉS de llegar a Tokio (ya estando ahí)' (V.Ta):", "options": [{"text": "東京へ行くとき、お土産を買いました。", "correct": False}, {"text": "東京へ行ったとき、お土産を買いました。", "correct": True}, {"text": "東京へ行く前に、お土産を買いました。", "correct": False}]},
            {"q": "¿Qué partícula se usa para decir 'Si haces A, obligatoria e inevitablemente ocurre B' (ej. botones de máquinas)?", "options": [{"text": "と (to)", "correct": True}, {"text": "が (ga)", "correct": False}, {"text": "で (de)", "correct": False}]},
            {"q": "'Si giras a la izquierda, está el banco':", "options": [{"text": "左へ曲がると、銀行があります。", "correct": True}, {"text": "左へ曲がるから、銀行があります。", "correct": False}, {"text": "左へ曲がるのとき、銀行があります。", "correct": False}]},
            {"q": "'Cuando no entiendo (el significado), pregunto al profesor':", "options": [{"text": "わからないとき、先生に聞きます。", "correct": True}, {"text": "わからなかったとき、先生に聞きます。", "correct": False}, {"text": "わかるのとき、先生に聞きます。", "correct": False}]},
            {"q": "'Si presionas este botón, sale el jugo':", "options": [{"text": "このボタンを押すと、ジュースが出ます。", "correct": True}, {"text": "このボタンを押すとき、ジュースが出ます。", "correct": False}, {"text": "このボタンを押すから、ジュースが出ます。", "correct": False}]}
        ]
    },
    24: {
        "title": "Dar y Recibir (Favores y Acciones)",
        "grammar": [
            "<strong>N を くれます:</strong> 'Me da / Nos da a mi grupo'. Se usa cuando alguien ajeno te da algo a ti.",
            "<strong>V(te) あげます:</strong> Hacer un favor a alguien. (Yo le explico a él).",
            "<strong>V(te) もらいます:</strong> Recibir un favor de alguien. (Yo recibo la explicación de él).",
            "<strong>V(te) くれます:</strong> Alguien me hace un favor a mí. (Él me explica a mí)."
        ],
        "examples": [
            ("佐藤さんは私にクリスマスカードをくれました。", "1. La Sra. Sato me dio una tarjeta de Navidad.", "さとうさんはわたしにクリスマスカードをくれました"),
            ("私は木村さんに本を貸してあげました。", "2. Yo le presté un libro a la Sra. Kimura (favor).", "わたしはきむらさんにほんをかしてあげました"),
            ("私は山田さんに図書館の電話番号を教えてもらいました。", "3. El Sr. Yamada me enseñó (recibí la enseñanza) el teléfono de la biblioteca.", "わたしはやまださんにとしょかんのでんわばんごうをおしえてもらいました"),
            ("母は私にセーターを送ってくれました。", "4. Mi madre me envió (hizo el favor de enviar) un suéter.", "はははわたしにセーターをおくってくれました"),
            ("太郎君は誰に手伝ってもらいましたか。", "5. Taro, ¿quién te ayudó? (¿de quién recibiste ayuda?)", "たろうくんはだれにてつだってもらいましたか"),
            ("鈴木さんに手伝ってもらいました。", "6. Recibí ayuda del Sr. Suzuki.", "すずきさんにてつだってもらいました"),
            ("誰が手伝ってくれましたか。", "7. ¿Quién te ayudó? (¿quién te hizo el favor?)", "だれがてつだってくれましたか"),
            ("鈴木さんが手伝ってくれました。", "8. El Sr. Suzuki me ayudó.", "すずきさんがてつだってくれました"),
            ("私はおじいさんの荷物を持ってあげました。", "9. Yo le cargué (hice el favor de cargar) el equipaje al abuelo.", "わたしはおじいさんのにもつをもつてあげました"),
            ("友達が私を迎えに来てくれました。", "10. Mi amigo vino a recogerme (me hizo el favor de venir).", "ともだちがわたしをむかえにきてくれました")
        ],
        "exercises": [
            {"q": "¿Qué verbo usas si el Sr. Tanaka TE DA un regalo a TI?", "options": [{"text": "あげます", "correct": False}, {"text": "もらいます", "correct": False}, {"text": "くれます", "correct": True}]},
            {"q": "¿Qué verbo usas si YO LE DOY un regalo al Sr. Tanaka?", "options": [{"text": "あげます", "correct": True}, {"text": "もらいます", "correct": False}, {"text": "くれます", "correct": False}]},
            {"q": "¿Qué verbo usas si YO RECIBO un regalo del Sr. Tanaka?", "options": [{"text": "あげます", "correct": False}, {"text": "もらいます", "correct": True}, {"text": "くれます", "correct": False}]},
            {"q": "'Yo le preparé café a María' (V-te agemasu):", "options": [{"text": "マリアさんにコーヒーをいれてあげました。", "correct": True}, {"text": "マリアさんにコーヒーをいれてもらいました。", "correct": False}, {"text": "マリアさんにコーヒーをいれてくれました。", "correct": False}]},
            {"q": "'El Sr. Yamada me explicó a MÍ el problema' (V-te kuremasu):", "options": [{"text": "山田さんは私に問題を説明してくれました。", "correct": True}, {"text": "山田さんは私に問題を説明してあげました。", "correct": False}, {"text": "山田さんは私に問題を説明してもらいました。", "correct": False}]},
            {"q": "'YO recibí la explicación del Sr. Yamada' (V-te moraimasu):", "options": [{"text": "私が山田さんに説明してもらいました。", "correct": True}, {"text": "山田さんが私に説明してもらいました。", "correct": False}, {"text": "私が山田さんに説明してくれました。", "correct": False}]},
            {"q": "¿Cuál es la diferencia entre 'て もらいます' y 'て くれます' si la acción es la misma?", "options": [{"text": "El sujeto de la oración cambia. En 'moraimasu' el sujeto soy YO. En 'kuremasu' el sujeto es EL OTRO.", "correct": True}, {"text": "No hay ninguna diferencia.", "correct": False}, {"text": "Moraimasu es futuro y kuremasu es pasado.", "correct": False}]},
            {"q": "Persona A: '¡Qué bonita camisa!'. Persona B: 'Mi hermana mayor ME LA COMPRÓ':", "options": [{"text": "姉が買ってくれました。", "correct": True}, {"text": "私が姉に買ってくれました。", "correct": False}, {"text": "姉が買ってあげました。", "correct": False}]},
            {"q": "¿Por qué a veces es mejor evitar usar '~て あげます' directamente con un superior o adulto mayor?", "options": [{"text": "Porque suena condescendiente (como si les estuvieras haciendo un gran favor desde una posición superior).", "correct": True}, {"text": "Porque no es gramaticalmente correcto.", "correct": False}, {"text": "Porque ellos no pueden recibir favores.", "correct": False}]},
            {"q": "'Le tomé una foto al amigo' (Forma normal sin connotación altanera de favor):", "options": [{"text": "友達の写真を撮りました。", "correct": True}, {"text": "友達の写真を撮ってあげました。", "correct": False}, {"text": "友達の写真を撮ってくれました。", "correct": False}]}
        ]
    },
    25: {
        "title": "Condicional ら y Aunque ても",
        "grammar": [
            "<strong>Forma TA + ら:</strong> 'Si...' (Condición) o 'Cuando / Después de que...' (Si es algo que seguro va a pasar). Ej: 雨が降ったら (Si llueve).",
            "<strong>V(te) も:</strong> 'Aunque... / A pesar de...'. Condición inversa. Ej: 雨が降っても (Aunque llueva).",
            "<strong>もし ~たら:</strong> 'En el caso hipotético de que...'. Si se usa, refuerza el sentido condicional de la oración.",
            "<strong>いくら ~ても:</strong> 'Por mucho que...'. (Ej: Por mucho que piense, no lo entiendo)."
        ],
        "examples": [
            ("雨が降ったら、行きません。", "1. Si llueve, no iré.", "あめがふったら、いきません"),
            ("雨が降っても、行きます。", "2. Aunque llueva, iré.", "あめがふっても、いきます"),
            ("明日晴れたら、ピクニックに行きましょう。", "3. Si mañana hace buen clima, vayamos de picnic.", "あしたはれたら、ピクニックにいきましょう"),
            ("安かったら、パソコンを買いたいです。", "4. Si está barata, quiero comprar la computadora.", "やすかったら、パソコンをかいたいです"),
            ("お金がなかったら、どうしますか。", "5. Si no tuvieras dinero, ¿qué harías?", "おかねがなかったら、どうしますか"),
            ("駅に着いたら、電話をください。", "6. Cuando (una vez que) llegues a la estación, por favor llámame.", "えきについたら、でんわをください"),
            ("いくら考えても、わかりません。", "7. Por mucho que lo piense, no lo entiendo.", "いくらかんがえても、わかりません"),
            ("もし一億円あったら、何をしたいですか。", "8. Si (hipotéticamente) tuvieras cien millones de yenes, ¿qué te gustaría hacer?", "もしいちおくえんあったら、なにをしたいですか"),
            ("年を取っても、働きたいです。", "9. Aunque envejezca, quiero trabajar.", "としをとっても、はたらきたいです"),
            ("日曜日でも、仕事をします。", "10. Aunque sea domingo, trabajaré.", "にちようびでも、しごとをします")
        ],
        "exercises": [
            {"q": "¿Cómo se forma el condicional 'Si...' (〜ら)?", "options": [{"text": "Con la forma Diccionario + ら", "correct": False}, {"text": "Con la Forma TA + ら", "correct": True}, {"text": "Con la Forma NAI + ら", "correct": False}]},
            {"q": "'Si como' (Tabemasu -> Tabeta):", "options": [{"text": "食べたら", "correct": True}, {"text": "食べるら", "correct": False}, {"text": "食べったら", "correct": False}]},
            {"q": "'Si es barato' (Adjetivo-i: Yasui -> Yasukatta):", "options": [{"text": "安いら", "correct": False}, {"text": "安かったら", "correct": True}, {"text": "安いたら", "correct": False}]},
            {"q": "'Si estoy libre' (Adjetivo-na: Hima -> Hima datta):", "options": [{"text": "暇だったら", "correct": True}, {"text": "暇なら", "correct": False}, {"text": "暇たら", "correct": False}]},
            {"q": "¿Qué palabra se coloca al inicio para reforzar que es una suposición ('Si acaso / En caso de que')?", "options": [{"text": "いくら (Ikura)", "correct": False}, {"text": "もし (Moshi)", "correct": True}, {"text": "とても (Totemo)", "correct": False}]},
            {"q": "¿Cómo se expresa la idea contraria 'AUNQUE / A PESAR DE...'?", "options": [{"text": "V(te) も", "correct": True}, {"text": "V(ta) ら", "correct": False}, {"text": "V(nai) と", "correct": False}]},
            {"q": "'Aunque llueva, voy a jugar fútbol':", "options": [{"text": "雨が降ったら、サッカーをします。", "correct": False}, {"text": "雨が降っても、サッカーをします。", "correct": True}, {"text": "雨が降ると、サッカーをします。", "correct": False}]},
            {"q": "'Por mucho que lo piense, no lo entiendo':", "options": [{"text": "いくら考えても、わかりません。", "correct": True}, {"text": "もし考えても、わかりません。", "correct": False}, {"text": "いくら考えたら、わかりません。", "correct": False}]},
            {"q": "'Aunque sea domingo (sustantivo), trabajo':", "options": [{"text": "日曜日ても、働きます。", "correct": False}, {"text": "日曜日でも、働きます。", "correct": True}, {"text": "日曜日だったら、働きます。", "correct": False}]},
            {"q": "¿Se puede usar '~たら' para referirse a una acción futura segura? (Ej. 'CUANDO llegues a casa, avísame')", "options": [{"text": "Sí, significa 'Una vez que se cumpla la condición segura'.", "correct": True}, {"text": "No, solo sirve para cosas imposibles.", "correct": False}, {"text": "No, hay que usar 'とき' obligatoriamente.", "correct": False}]}
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
    <title>Lección {i} - Minna no Nihongo I</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=Noto+Sans+JP:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../css/style.css">
</head>
<body class="iframe-body">
    <div class="max-w-4xl">
        <div class="lesson-header-simple">
            <span>第{i}課</span>
            <h1>Minna no Nihongo I - Lección {i}</h1>
            <p class="lesson-desc">Tema: {d["title"]}</p>
        </div>

        <div class="video-link-section" style="text-align: center; margin: 2rem 0; padding: 2.5rem; background: linear-gradient(135deg, var(--secondary-color) 0%, #2a2a4a 100%); border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
            <h3 style="color: white; margin-bottom: 0.5rem; font-size: 1.5rem;">🎬 Clase en Video</h3>
            <p style="color: #cbd5e0; margin-bottom: 1.5rem; font-size: 1.05rem;">Aprende la gramática detallada de la Lección {i} con Kira Sensei.</p>
            <a href="https://www.youtube.com/results?search_query=Kira+Sensei+Minna+no+Nihongo+Leccion+{i}" target="_blank" style="display: inline-block; background: var(--primary-color); color: white; padding: 1rem 2.5rem; border-radius: 50px; text-decoration: none; font-weight: 700; font-size: 1.15rem; transition: transform 0.2s, box-shadow 0.2s; box-shadow: 0 4px 15px rgba(224, 42, 77, 0.4);" onmouseover="this.style.transform='translateY(-3px)'; this.style.boxShadow='0 6px 20px rgba(224, 42, 77, 0.6)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 15px rgba(224, 42, 77, 0.4)'">Ver Lección {i} en YouTube</a>
        </div>

        <h2 class="section-title">📚 Gramática Principal</h2>
        <div class="grammar-note">
            <ul>
{grammar_html}            </ul>
        </div>
        
        <h2 class="section-title">🌟 10 Ejemplos de Uso</h2>
        <div class="grammar-note"><p>A continuación, 10 ejemplos prácticos utilizando la gramática aprendida en esta lección.</p></div>
{examples_html}
        <h2 class="section-title">📝 Ejercicios de Práctica</h2>
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

        with open(os.path.join(base_dir, f"lesson-{i}.html"), "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated Lesson {i}")

if __name__ == '__main__':
    generate()
