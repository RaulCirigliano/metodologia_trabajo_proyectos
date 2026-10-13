import os

data = {
    6: {
        "title": "Voluntad e Intención (~つもりです)",
        "grammar": [
            "<strong>Forma Volitiva (Ikoukei):</strong> Para expresar voluntad ('Vamos a...' informal). G1 (u->o+u), G2 (ru->you), G3 (suru->shiyou, kuru->koyou).",
            "<strong>V(vol) + と 思っています:</strong> 'Tengo la intención de...'.",
            "<strong>V(dic) / V(nai) + つもりです:</strong> 'Tengo el firme propósito de...' (Mayor certeza que omoimasu).",
            "<strong>V(dic) / Nの + 予定です:</strong> 'Está programado que...' (Planes fijos o institucionales)."
        ],
        "examples": [
            ("週末は海に行こうと思っています。", "1. El fin de semana tengo la intención de ir al mar.", "しゅうまつはうみにいこうとおもっています"),
            ("今から銀行へ行こうと思っています。", "2. Tengo la intención de ir al banco ahora mismo.", "いまからぎんこうへいこうとおもっています"),
            ("国へ帰っても、日本語を勉強するつもりです。", "3. Aunque vuelva a mi país, tengo el propósito de estudiar japonés.", "くにへかえっても、にほんごをべんきょうするつもりです"),
            ("明日は来ないつもりです。", "4. Tengo la intención de no venir mañana.", "あしたはこないつもりです"),
            ("７月の終わりにドイツへ出張する予定です。", "5. A finales de julio está programado que haga un viaje de negocios a Alemania.", "しちがつの終わりにドイツへしゅっちょうするよていです"),
            ("旅行は１週間の予定です。", "6. El viaje está programado para una semana.", "りょこうはいっしゅうかんのよていです"),
            ("休もう！", "7. ¡Descansemos! (Volitivo informal de 休む)", "やすもう"),
            ("将来、自分の会社を作るつもりです。", "8. En el futuro, tengo el propósito de crear mi propia empresa.", "しょうらい、じぶんのかいしゃをつくるつもりです"),
            ("車を買わないつもりです。", "9. No tengo intención de comprar un auto.", "くるまをかわないつもりです"),
            ("飛行機は１１時に着く予定です。", "10. Está programado que el avión llegue a las 11.", "ひこうきはじゅういちじにつくよていです")
        ],
        "exercises": [
            {"q": "¿Cuál es la Forma Volitiva de 行きます (Ir)?", "options": [{"text": "いこう (Ikou)", "correct": True}, {"text": "いかよう (Ikayou)", "correct": False}, {"text": "いきます (Ikimasu)", "correct": False}]},
            {"q": "¿Cuál es la Forma Volitiva de 食べます (Comer)?", "options": [{"text": "食べおう (Tabeou)", "correct": False}, {"text": "食べよう (Tabeyou)", "correct": True}, {"text": "食べるう (Taberuu)", "correct": False}]},
            {"q": "¿Cuál es la Forma Volitiva de します (Hacer)?", "options": [{"text": "しよう (Shiyou)", "correct": True}, {"text": "すろう (Surou)", "correct": False}, {"text": "そう (Sou)", "correct": False}]},
            {"q": "'Tengo la INTENCIÓN de comprar una cámara':", "options": [{"text": "カメラを買おうと思っています。", "correct": True}, {"text": "カメラを買うと思っています。", "correct": False}, {"text": "カメラを買うつもりがあります。", "correct": False}]},
            {"q": "¿Cuál de estas estructuras muestra una decisión más firme y personal?", "options": [{"text": "〜ようと思っています", "correct": False}, {"text": "〜つもりです (Tsumori desu)", "correct": True}, {"text": "〜たいです", "correct": False}]},
            {"q": "'El mes que viene, TENGO EL PROPÓSITO de dejar de fumar (yameru)':", "options": [{"text": "来月、タバコを辞めようと思います。", "correct": False}, {"text": "来月、タバコを辞めるつもりです。", "correct": True}, {"text": "来月、タバコを辞める予定です。", "correct": False}]},
            {"q": "'Tengo la intención de NO ir a la universidad':", "options": [{"text": "大学へ行かないつもりです。", "correct": True}, {"text": "大学へ行かなくつもりです。", "correct": False}, {"text": "大学へ行かなかったつもりです。", "correct": False}]},
            {"q": "¿Qué se usa para un plan oficial, horario de transportes o evento de la empresa?", "options": [{"text": "つもりです", "correct": False}, {"text": "予定です (Yotei desu)", "correct": True}, {"text": "ようと思っています", "correct": False}]},
            {"q": "'La reunión ESTÁ PROGRAMADA para las 10':", "options": [{"text": "会議は１０時つもりです。", "correct": False}, {"text": "会議は１０時の予定です。", "correct": True}, {"text": "会議は１０時予定です。", "correct": False}]},
            {"q": "¿Cuál es el negativo de 'Tsukuru tsumori desu' (Propósito de crear)?", "options": [{"text": "作らないつもりです (Propósito de no crear)", "correct": True}, {"text": "作るつもりはありません (No tengo el propósito de crear)", "correct": True}, {"text": "Ambas son correctas, pero con ligeros matices de énfasis.", "correct": True}]}
        ]
    },
    7: {
        "title": "Dar consejos y Probabilidades",
        "grammar": [
            "<strong>V(ta) / V(nai) + ほうがいいです:</strong> 'Es mejor que... / Deberías...'. Se usa para dar un consejo fuerte o una advertencia médica.",
            "<strong>Futsukei + でしょう:</strong> 'Seguramente...'. El hablante cree que es probable (aprox. 80%).",
            "<strong>Futsukei + かもしれません:</strong> 'Tal vez... / Puede ser que...'. Probabilidad menor (aprox. 50%)."
        ],
        "examples": [
            ("毎日運動したほうがいいです。", "1. Es mejor que hagas ejercicio todos los días.", "まいにちうんどうしたほうがいいです"),
            ("タバコを吸わないほうがいいです。", "2. Es mejor que no fumes.", "タバコをすわないほうがいいです"),
            ("熱がありますから、早く寝たほうがいいですよ。", "3. Como tienes fiebre, es mejor que te acuestes temprano.", "ねつがありますから、はやくねたほうがいいですよ"),
            ("明日は雨が降るでしょう。", "4. Seguramente mañana lloverá.", "あしたはあめがふるでしょう"),
            ("タワポンさんは合格するでしょう。", "5. Seguramente el Sr. Tawapon aprobará.", "タワポンさんはごうかくするでしょう"),
            ("約束の時間に間に合わないかもしれません。", "6. Tal vez no lleguemos a tiempo a la cita.", "やくそくのじかんにまにあわないかもしれません"),
            ("明日は寒いかもしれません。", "7. Tal vez mañana haga frío.", "あしたはさむいかもしれません"),
            ("もしかしたら、３月に卒業できないかもしれません。", "8. A lo mejor, no pueda graduarme en marzo.", "もしかしたら、さんがつにそつぎょうできないかもしれません"),
            ("この病気はすぐによくなるでしょう。", "9. Seguramente esta enfermedad mejorará pronto.", "このびょうきはすぐによくなるでしょう"),
            ("お風呂に入らないほうがいいです。", "10. Es mejor que no tomes un baño (tina).", "おふろにはいらないほうがいいです")
        ],
        "exercises": [
            {"q": "¿Qué estructura se usa para dar un CONSEJO FUERTE o advertencia?", "options": [{"text": "〜たほうがいいです (Ta hou ga ii desu)", "correct": True}, {"text": "〜てください (Te kudasai)", "correct": False}, {"text": "〜てもいいですか (Te mo ii desu ka)", "correct": False}]},
            {"q": "¿Qué forma verbal se usa ANTES de 'hou ga ii desu' en afirmativo?", "options": [{"text": "Forma Diccionario (V-ru)", "correct": False}, {"text": "Forma TA (V-ta)", "correct": True}, {"text": "Forma TE (V-te)", "correct": False}]},
            {"q": "'Es mejor que VAYAS al hospital':", "options": [{"text": "病院へ行くほうがいいです。", "correct": False}, {"text": "病院へ行ったほうがいいです。", "correct": True}, {"text": "病院へ行かたほうがいいです。", "correct": False}]},
            {"q": "'Es mejor que NO VEAS la televisión':", "options": [{"text": "テレビを見ないほうがいいです。", "correct": True}, {"text": "テレビを見なかったほうがいいです。", "correct": False}, {"text": "テレビを見てないほうがいいです。", "correct": False}]},
            {"q": "¿Qué significa 'でしょう' (Deshou) al final de una frase (sin entonación de pregunta)?", "options": [{"text": "Seguramente / Probablemente", "correct": True}, {"text": "¿No es así?", "correct": False}, {"text": "Deberías", "correct": False}]},
            {"q": "'Seguramente mañana será un buen día' (Buen día = Ii tenki - Sustantivo):", "options": [{"text": "明日はいい天気だでしょう。", "correct": False}, {"text": "明日はいい天気でしょう。(Se omite el 'da')", "correct": True}, {"text": "明日はいい天気なでしょう。", "correct": False}]},
            {"q": "¿Qué significa 'かもしれません' (Kamo shiremasen)?", "options": [{"text": "Seguramente", "correct": False}, {"text": "Tal vez / A lo mejor (Posibilidad del 50%)", "correct": True}, {"text": "Es mejor que", "correct": False}]},
            {"q": "'Tal vez la empresa quiebre' (Taoreru = quebrar):", "options": [{"text": "会社が倒れるかもしれません。", "correct": True}, {"text": "会社が倒れるでしょう。", "correct": False}, {"text": "会社が倒れるほうがいいです。", "correct": False}]},
            {"q": "¿Qué adverbio se suele usar junto con 'kamo shiremasen' para enfatizar la duda?", "options": [{"text": "きっと (Kitto - Sin duda)", "correct": False}, {"text": "たぶん (Tabun - Probablemente)", "correct": False}, {"text": "もしかしたら (Moshikashitara - A lo mejor)", "correct": True}]},
            {"q": "Si hablas con tu amigo y quieres decir 'tal vez', ¿cuál es la forma coloquial de kamo shiremasen?", "options": [{"text": "かも (Kamo)", "correct": True}, {"text": "だろう (Darou)", "correct": False}, {"text": "だね (Da ne)", "correct": False}]}
        ]
    },
    8: {
        "title": "Imperativo y Citas Directas",
        "grammar": [
            "<strong>Imperativo Fuerte:</strong> G1(u->e), G2(ru->ro), G3(suru->shiro, kuru->koi). Muy brusco, se usa en deportes, emergencias o de jefe a subordinado masculino.",
            "<strong>Prohibición (na):</strong> V(dic) + な (na). '¡NO lo hagas!'.",
            "<strong>X は Y という意味です:</strong> 'X significa Y'.",
            "<strong>~と 言っていました:</strong> 'Dijo que...' (Transmitir un mensaje de un tercero a otra persona)."
        ],
        "examples": [
            ("急げ！", "1. ¡Date prisa! (Isogimasu -> Isoge)", "いそげ"),
            ("触るな！", "2. ¡No toques! (Sawaru + na)", "さわるな"),
            ("頑張れ！", "3. ¡Esfuérzate! (Ganbarimasu -> Ganbare)", "がんばれ"),
            ("逃げろ！", "4. ¡Huye! (Nigemasu -> Nigero)", "にげろ"),
            ("あそこに「止まれ」と書いてあります。", "5. Allí está escrito 'Deténgase'.", "あそこに「とまれ」とかいてあります"),
            ("立入禁止は「入るな」という意味です。", "6. 'Tachi-iri kinshi' significa 'No entrar'.", "たちいりきんしは「はいるな」といういみです"),
            ("田中さんは「明日休む」と言っていました。", "7. El Sr. Tanaka estaba diciendo que descansará mañana.", "たなかさんは「あしたやすむ」といっていました"),
            ("すみませんが、山田さんに「明日の会議は１０時からだ」と伝えていただけませんか。", "8. Disculpe, ¿podría transmitirle a Yamada que 'la reunión de mañana es desde las 10'?", "すみませんが、やまださんに「あしたのかいぎはじゅうじからだ」とつたえていただけませんか"),
            ("ここに荷物を置くな！", "9. ¡No pongas el equipaje aquí!", "ここににもつをおくな"),
            ("飲め！", "10. ¡Bébelo! (Nomimasu -> Nome)", "のめ")
        ],
        "exercises": [
            {"q": "¿Cómo se forma el IMPERATIVO FUERTE (Orden) para el Grupo I (Ej. 書く - Kaku)?", "options": [{"text": "書け (Kake - Termina en sonido 'e')", "correct": True}, {"text": "書こ (Kako)", "correct": False}, {"text": "書き (Kaki)", "correct": False}]},
            {"q": "¿Cuál es el Imperativo Fuerte de 食べます (Comer - Grupo II)?", "options": [{"text": "食べれ (Tabere)", "correct": False}, {"text": "食べろ (Tabero)", "correct": True}, {"text": "食べや (Tabeya)", "correct": False}]},
            {"q": "¿Cuál es el Imperativo Fuerte de 来ます (Kimasu - Venir)?", "options": [{"text": "きろ (Kiro)", "correct": False}, {"text": "こい (Koi)", "correct": True}, {"text": "こ (Ko)", "correct": False}]},
            {"q": "¿Cómo formas la PROHIBICIÓN BRUSCA ('¡No lo hagas!')?", "options": [{"text": "Forma Nai + な", "correct": False}, {"text": "Forma Diccionario + な (Ej. 飲むな)", "correct": True}, {"text": "Forma TE + な", "correct": False}]},
            {"q": "'¡No mires!' (Miru):", "options": [{"text": "見ないな", "correct": False}, {"text": "見るな (Miru na)", "correct": True}, {"text": "見てな", "correct": False}]},
            {"q": "Si ves un cartel, ¿cómo dices 'ESTÁ ESCRITO ...'?", "options": [{"text": "〜と書きます", "correct": False}, {"text": "〜と書いてあります (To kaite arimasu)", "correct": True}, {"text": "〜と書いています", "correct": False}]},
            {"q": "¿Qué frase usas para explicar el SIGNIFICADO de una palabra?", "options": [{"text": "〜という意味です (To iu imi desu)", "correct": True}, {"text": "〜と思います (To omoimasu)", "correct": False}, {"text": "〜と言います (To iimasu)", "correct": False}]},
            {"q": "'Esta señal significa ¡NO FUMAR!':", "options": [{"text": "このマークはタバコを吸うなという意味です。", "correct": True}, {"text": "このマークはタバコを吸わないという意味です。", "correct": False}, {"text": "このマークはタバコを吸うなと言います。", "correct": False}]},
            {"q": "¿Qué significa '〜と言っていました' (To itte imashita)?", "options": [{"text": "Yo estaba diciendo...", "correct": False}, {"text": "Él/Ella estaba diciendo (Para transmitir un mensaje a un 3ro)", "correct": True}, {"text": "Se dice que...", "correct": False}]},
            {"q": "¿Cómo pides cortésmente a alguien que TRANSMITA un mensaje?", "options": [{"text": "伝えてくれませんか (Tsutaete kuremasen ka)", "correct": False}, {"text": "伝えていただけませんか (Tsutaete itadakemasen ka)", "correct": True}, {"text": "言ってください (Itte kudasai)", "correct": False}]}
        ]
    },
    9: {
        "title": "Hacer tal como... / Secuencias temporales",
        "grammar": [
            "<strong>V1(ta) / V1(dic) / Nの + とおりに:</strong> 'Tal y como...'. Hacer la acción 2 exactamente igual que la 1. Ej: 私が言うとおりに (Tal como digo).",
            "<strong>V1(ta) / Nの + あとで:</strong> 'Después de...'. Similar a 'te kara', pero enfocado en que V1 ya terminó completamente.",
            "<strong>V1(nai) + ないで、V2:</strong> 'Hacer V2 SIN HACER V1'. Ej: 朝ごはんを食べないで、学校へ行きました (Fui a la escuela sin desayunar)."
        ],
        "examples": [
            ("私が言うとおりに、書いてください。", "1. Por favor, escriba tal y como yo lo digo.", "わたしがいうとおりに、かいてください"),
            ("見たとおりに、話してください。", "2. Por favor, habla (cuéntalo) tal y como lo viste.", "みたとおりに、はなしてください"),
            ("線のとおりに、紙を切ってください。", "3. Corta el papel siguiendo (tal como indica) la línea.", "せんのとおりに、かみをきってください"),
            ("新しい仕事は希望のとおりでした。", "4. El nuevo trabajo fue tal y como esperaba.", "あたらしいしごとはきぼうのとおりでした"),
            ("仕事が終わったあとで、飲みに行きませんか。", "5. Después de terminar el trabajo, ¿vamos a beber?", "しごとがおわったあとで、のみにいきませんか"),
            ("食事のあとで、コーヒーを飲みます。", "6. Después de la comida, tomaré un café.", "しょくじのあとで、コーヒーをのみます"),
            ("醤油をつけて食べます。", "7. Lo como poniéndole salsa de soja.", "しょうゆをつけてたべます"),
            ("醤油をつけないで食べます。", "8. Lo como SIN ponerle salsa de soja.", "しょうゆをつけないでたべます"),
            ("日曜日はどこも行かないで、家で休みます。", "9. El domingo descansaré en casa SIN ir a ningún lado.", "にちようびはどこもいかないで、いえでやすみます"),
            ("辞書を見ないで、日本語の新聞を読みます。", "10. Leo el periódico japonés SIN mirar el diccionario.", "じしょをみないで、にほんごのしんぶんをよみます")
        ],
        "exercises": [
            {"q": "¿Qué expresión significa 'Tal y como / Exactamente como'?", "options": [{"text": "〜あとで", "correct": False}, {"text": "〜とおりに (Toori ni)", "correct": True}, {"text": "〜ないで", "correct": False}]},
            {"q": "'Hazlo TAL COMO te enseñé' (Oshieru -> Oshieta):", "options": [{"text": "教えるとおりに、してください。", "correct": False}, {"text": "教えたとおりに、してください。", "correct": True}, {"text": "教えてとおりに、してください。", "correct": False}]},
            {"q": "¿Cómo conectas un Sustantivo con とおりに? 'Tal y como indica el manual (Setsumeisho)':", "options": [{"text": "説明書とおりに", "correct": False}, {"text": "説明書のとおりに", "correct": True}, {"text": "説明書だとおりに", "correct": False}]},
            {"q": "¿Qué significa '〜あとで' (Ato de)?", "options": [{"text": "Antes de", "correct": False}, {"text": "Durante", "correct": False}, {"text": "Después de", "correct": True}]},
            {"q": "¿Qué forma verbal va ANTES de 'ato de'?", "options": [{"text": "Forma Diccionario (V-ru)", "correct": False}, {"text": "Forma TA (V-ta)", "correct": True}, {"text": "Forma TE (V-te)", "correct": False}]},
            {"q": "'Después de comprar, fui a casa' (Kaimono = sustantivo):", "options": [{"text": "買い物のあとで、うちへ帰りました。", "correct": True}, {"text": "買い物あとで、うちへ帰りました。", "correct": False}, {"text": "買い物にあとで、うちへ帰りました。", "correct": False}]},
            {"q": "¿Qué estructura significa 'Hacer algo SIN HACER otra cosa' (Ej. Salí SIN llevar paraguas)?", "options": [{"text": "V(te) ないで", "correct": False}, {"text": "V(nai) で (Naide)", "correct": True}, {"text": "V(nakute)", "correct": False}]},
            {"q": "'Dormí SIN apagar la luz' (Keshimasu = apagar):", "options": [{"text": "電気を消さなくて寝ました。", "correct": False}, {"text": "電気を消さないで寝ました。", "correct": True}, {"text": "電気を消しで寝ました。", "correct": False}]},
            {"q": "Persona A: '¿Te tomaste el café con azúcar?'. Persona B: 'No, lo tomé ___ ponerle azúcar'.", "options": [{"text": "入れないで (Irenaide)", "correct": True}, {"text": "入れなくて (Irenakute)", "correct": False}, {"text": "入れてない (Irete nai)", "correct": False}]},
            {"q": "¿Cuál es la diferencia entre 〜ないで (naide) y 〜なくて (nakute)?", "options": [{"text": "Naide es para acciones simultáneas alternativas. Nakute es para causas (No lo hice, POR ESO...).", "correct": True}, {"text": "Son exactamente iguales.", "correct": False}, {"text": "Nakute es más formal.", "correct": False}]}
        ]
    },
    10: {
        "title": "Condicional (~ば)",
        "grammar": [
            "<strong>Forma Condicional (Bakei):</strong> 'Si ocurre A, entonces B'.",
            "<strong>G1:</strong> u -> e + ba (書く -> 書けば).",
            "<strong>G2:</strong> ru -> reba (食べる -> 食べれば).",
            "<strong>G3:</strong> する -> すれば | 来る -> 来れば (kureba).",
            "<strong>Adj-i:</strong> i -> kereba (高い -> 高ければ).",
            "<strong>Adj-na / Sust:</strong> -> なら (暇なら)."
        ],
        "examples": [
            ("春になれば、桜が咲きます。", "1. Si llega la primavera (naturalmente), los cerezos florecen.", "はるになれば、さくらがさきます"),
            ("天気がよければ、行きます。", "2. Si hace buen tiempo, iré.", "てんきがよければ、いきます"),
            ("安ければ、買います。", "3. Si es barato, lo compraré.", "やすければ、かいます"),
            ("時間がないなら、タクシーで行きましょう。", "4. Si no tienes tiempo, vayamos en taxi.", "じかんがないなら、タクシーでいきましょう"),
            ("説明書を読めば、使い方がわかります。", "5. Si lees las instrucciones, entenderás cómo usarlo.", "せつめいしょをよめば、つかいかたがわかります"),
            ("薬を飲まなければ、病気はよくなりません。", "6. Si no tomas la medicina, la enfermedad no mejorará.", "くすりをのまなければ、びょうきはよくなりません"),
            ("明日雨が降れば、試合はありません。", "7. Si mañana llueve, no habrá partido.", "あしたあめがふれば、しあいはありません"),
            ("パソコンなら、秋葉原がいいですよ。", "8. Si se trata de computadoras, Akihabara es un buen lugar.", "パソコンなら、あきはばらがいいですよ"),
            ("もっと練習すれば、上手になります。", "9. Si practicas más, te volverás hábil.", "もっとれんしゅうすれば、じょうずになります"),
            ("どうすればいいですか。", "10. ¿Qué debo (si hago qué estará bien) hacer?", "どうすればいいですか")
        ],
        "exercises": [
            {"q": "¿Cómo se forma el condicional BA para el verbo 飲みます (Grupo I)?", "options": [{"text": "飲めば (Nomeba)", "correct": True}, {"text": "飲まば (Nomaba)", "correct": False}, {"text": "飲みば (Nomiba)", "correct": False}]},
            {"q": "¿Cómo se forma el condicional BA para el verbo 食べます (Grupo II)?", "options": [{"text": "食べば (Tabeba)", "correct": False}, {"text": "食べれば (Tabereba)", "correct": True}, {"text": "食べれ (Tabere)", "correct": False}]},
            {"q": "¿Cuál es la forma condicional de します (Hacer)?", "options": [{"text": "しれば", "correct": False}, {"text": "すれば (Sureba)", "correct": True}, {"text": "されば", "correct": False}]},
            {"q": "¿Cuál es la forma condicional de 来ます (Venir - Kimasu)?", "options": [{"text": "くれば (Kureba)", "correct": True}, {"text": "きれば (Kireba)", "correct": False}, {"text": "これば (Koreba)", "correct": False}]},
            {"q": "Para un Adjetivo-i como 安い (Barato), ¿cuál es su condicional 'Si es barato'?", "options": [{"text": "安いれば", "correct": False}, {"text": "安ければ (Yasukereba)", "correct": True}, {"text": "安ならば", "correct": False}]},
            {"q": "¿Cuál es la forma condicional del Adjetivo いい (Bueno) -> 'Si es bueno'?", "options": [{"text": "いいければ", "correct": False}, {"text": "よければ (Yokereba)", "correct": True}, {"text": "よいれば", "correct": False}]},
            {"q": "Para Sustantivos y Adjetivos-na, se usa 'Nara'. Ej: 'Si estás libre' (Hima):", "options": [{"text": "暇ならば", "correct": True}, {"text": "暇なら (Más común)", "correct": True}, {"text": "Ambas son correctas", "correct": True}]},
            {"q": "¿Cómo expresas el negativo 'Si NO voy' (Ikimasen)?", "options": [{"text": "行かないれば", "correct": False}, {"text": "行かなければ (Ikanakereba)", "correct": True}, {"text": "行きなければ", "correct": False}]},
            {"q": "'¿Qué debo hacer?' (Si hago qué, está bien):", "options": [{"text": "どうすればいいですか。", "correct": True}, {"text": "どうしたらいいですか。(También correcta y más hablada)", "correct": True}, {"text": "Ambas son correctas", "correct": True}]},
            {"q": "Persona A: 'Quiero ir a un onsen (termas)'. Persona B: 'Si se trata de onsen, Hakone es bueno'.", "options": [{"text": "温泉と、箱根がいいですよ。", "correct": False}, {"text": "温泉なら、箱根がいいですよ。(Nara se usa para retomar un tema sugerido)", "correct": True}, {"text": "温泉ば、箱根がいいですよ。", "correct": False}]}
        ]
    }
}

def generate():
    base_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\lessons"
    
    for i in range(6, 11):
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
        print(f"Generated JLPT N4 Lesson {i}")

if __name__ == '__main__':
    generate()
