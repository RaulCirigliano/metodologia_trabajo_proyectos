import os
import subprocess

data = {
    16: {
        "title": "Dar y Recibir favores (~て あげる / もらう / くれる)",
        "grammar": [
            "<strong>V(te) + あげます:</strong> Yo hago un favor a otro (o alguien a alguien más). <em>Ojo: No se usa con superiores porque suena arrogante.</em>",
            "<strong>V(te) + くれます:</strong> Alguien me hace un favor a mí (o a mi grupo familiar).",
            "<strong>V(te) + もらいます:</strong> Yo recibo un favor de alguien (El sujeto soy yo y uso に para la otra persona).",
            "Para superiores se usan formas humildes/honoríficas: さしあげます (dar), くださいます (me dan), いただきます (recibo)."
        ],
        "examples": [
            ("私は妹に日本語を教えてあげました。", "1. Le enseñé japonés a mi hermana menor (Le hice el favor).", "わたしはいもうとににほんごをおしえてあげました"),
            ("友達が私に本を貸してくれました。", "2. Un amigo me prestó un libro (Me hizo el favor).", "ともだちがわたしにほんをかしてくれました"),
            ("私は先生に本を貸してもらいました。", "3. Recibí del profesor el favor de prestarme un libro.", "わたしはせんせいにほんをかしてもらいました"),
            ("母は私に料理を作ってくれました。", "4. Mi madre me preparó comida (Me hizo el favor).", "はははわたしにりょうりをつくってくれました"),
            ("私は父に時計を買ってあげました。", "5. Le compré un reloj a mi padre.", "わたしはちちにとけいをかってあげました"),
            ("私が手伝ってあげましょうか。", "6. ¿Quieres que te ayude? (Ofrecer un favor a un igual/inferior).", "わたしがてつだってあげましょうか"),
            ("山田さんに写真を撮ってもらいました。", "7. Le pedí a Yamada que me tomara una foto (Recibí el favor).", "やまださんにしゃしんをとってもらいました"),
            ("駅まで送ってくれませんか。", "8. ¿Me llevarías a la estación? (¿Me harías el favor?)", "えきまでおくってくれませんか"),
            ("社長にネクタイをいただきました。", "9. Recibí una corbata del presidente de la empresa (Humilde).", "しゃちょうにネクタイをいただきました"),
            ("先生が本を貸してくださいました。", "10. El profesor me prestó un libro (Honorífico).", "せんせいがほんをかしてくださいました")
        ],
        "exercises": [
            {"q": "Si UN AMIGO TE PRESTA un libro, ¿cuál es correcta usando 'Amigo' como sujeto (友達が...)?", "options": [{"text": "友達が私に本を貸してもらいました。", "correct": False}, {"text": "友達が私に本を貸してくれました。", "correct": True}, {"text": "友達が私に本を貸してあげました。", "correct": False}]},
            {"q": "Si TÚ RECIBES el favor de que te presten un libro: 私は友達___本を貸してもらいました。", "options": [{"text": "に", "correct": True}, {"text": "が", "correct": False}, {"text": "を", "correct": False}]},
            {"q": "Si vas a ayudar a un anciano desconocido en la calle, ¿por qué es de MALA EDUCACIÓN decir 手伝ってあげます?", "options": [{"text": "Porque 'ageru' implica que haces un favor y suenas arrogante.", "correct": True}, {"text": "Porque significa que tú necesitas ayuda.", "correct": False}, {"text": "Porque no es gramaticalmente correcto en japonés.", "correct": False}]},
            {"q": "¿Qué significa '母が弁当を作ってくれました'?", "options": [{"text": "Yo le preparé el bento a mi madre.", "correct": False}, {"text": "Mi madre me preparó el bento (hacia mí).", "correct": True}, {"text": "Mi madre preparó el bento para otra persona.", "correct": False}]},
            {"q": "¿Cuál es la versión formal/humilde de 'もらう' (recibir)?", "options": [{"text": "いただく (Itadaku)", "correct": True}, {"text": "くださる (Kudasaru)", "correct": False}, {"text": "さしあげる (Sashiageru)", "correct": False}]},
            {"q": "¿Cuál es la versión formal/honorífica de 'くれる' (alguien me da)?", "options": [{"text": "さしあげる", "correct": False}, {"text": "くださる (Kudasaru)", "correct": True}, {"text": "いただく", "correct": False}]},
            {"q": "'Yo le preparé la cena a mi hijo' (Musuko):", "options": [{"text": "息子に晩ごはんを作ってもらいました。", "correct": False}, {"text": "息子に晩ごはんを作ってあげました。", "correct": True}, {"text": "息子に晩ごはんを作ってくれました。", "correct": False}]},
            {"q": "Para pedir un favor de manera educada: '¿Podrías enseñarme?' (Oshieru):", "options": [{"text": "教えてもらいませんか。", "correct": False}, {"text": "教えてくれませんか。", "correct": True}, {"text": "教えてあげませんか。", "correct": False}]},
            {"q": "'Recibí dinero del banco' (El banco no es persona, se usa 'kara' o 'ni'):", "options": [{"text": "銀行からお金を貸してもらいました。", "correct": True}, {"text": "銀行からお金を貸してくれました。", "correct": False}, {"text": "銀行からお金を貸してあげました。", "correct": False}]},
            {"q": "Si un profesor TE ENSEÑÓ kanjis (Tú eres el beneficiado y el profesor es el sujeto):", "options": [{"text": "先生が漢字を教えてあげました。", "correct": False}, {"text": "先生が漢字を教えていただきました。", "correct": False}, {"text": "先生が漢字を教えてくださいました。", "correct": True}]}
        ],
        "dialogue": [
            ("ja-JP-KeitaNeural", "どうしたんですか。嬉しそうですね。", "¿Qué pasa? Te ves feliz."),
            ("ja-JP-NanamiNeural", "ええ。昨日、誕生日に彼が指輪を買ってくれたんです。", "Sí. Ayer, en mi cumpleaños, mi novio me compró (me hizo el favor de comprarme) un anillo."),
            ("ja-JP-KeitaNeural", "へえ、いいですね。山田さんは彼に何をあげましたか。", "Vaya, qué bien. ¿Y qué le regalaste tú a él?"),
            ("ja-JP-NanamiNeural", "私は手編みのセーターを作ってあげました。", "Yo le hice (le hice el favor de tejerle) un suéter a mano."),
            ("ja-JP-KeitaNeural", "素晴らしいですね。私も誰かにプレゼントをもらいたいです。", "Es fantástico. Yo también quiero que alguien me haga un regalo (recibir un regalo)."),
            ("ja-JP-NanamiNeural", "じゃあ、私が美味しいクッキーを焼いてきてあげますよ。", "Entonces, yo te hornearé y traeré (te haré el favor de traerte) galletas deliciosas."),
            ("ja-JP-KeitaNeural", "本当ですか！ありがとうございます。楽しみにしています。", "¡De verdad! Muchas gracias. Las esperaré con ansias."),
            ("ja-JP-NanamiNeural", "ええ、今度作ってきますね。", "Sí, la próxima vez las haré y las traeré.")
        ]
    },
    17: {
        "title": "Propósitos y Razones (~ために / ~のに)",
        "grammar": [
            "<strong>V(dic) / Sustantivo + の + ために:</strong> 'Para', 'Por', 'Con el propósito de'. Indica un esfuerzo o meta clara. Ej. 家族のために働きます (Trabajo por mi familia).",
            "<strong>V(dic) + のに:</strong> 'Para'. Se usa seguido de verbos como 使う (usar), 役に立つ (ser útil), o expresiones de tiempo/dinero (かかる). Ej. これを切るのに使います (Se usa para cortar esto).",
            "<em>Diferencia:</em> 'Tame ni' es un propósito/meta humana absoluta. 'Noni' es el uso o la función de un objeto."
        ],
        "examples": [
            ("家を買うために、貯金しています。", "1. Estoy ahorrando para (con el propósito de) comprar una casa.", "いえをかうために、ちょきんしています"),
            ("健康のために、野菜を食べます。", "2. Como verduras por el bien de (para) la salud.", "けんこうのために、やさいをたべます"),
            ("日本の大学に入るために、勉強しています。", "3. Estudio con el propósito de entrar a una universidad japonesa.", "にほんのだいがくにはいるために、べんきょうしています"),
            ("家族のために、毎日働いています。", "4. Trabajo todos los días por mi familia.", "かぞくのために、まいにちはたらいています"),
            ("このハサミは紙を切るのに使います。", "5. Estas tijeras se usan para cortar papel.", "このハサミはかみをきるのに使います"),
            ("この本は漢字を覚えるのに役に立ちます。", "6. Este libro es útil para memorizar kanjis.", "このほんはかんじをおぼえるのにやくにたちます"),
            ("会社へ行くのに１時間かかります。", "7. Toma una hora para (el propósito de) ir a la empresa.", "かいしゃへいくのにいちじかんかかります"),
            ("修理するのに１万円必要です。", "8. Se necesitan 10.000 yenes para repararlo.", "しゅうりするのにいちまんえんひつようです"),
            ("外国へ旅行するために、パスポートを取ります。", "9. Sacaré el pasaporte para viajar al extranjero.", "がいこくへりょこうするために、パスポートをとります"),
            ("これはコーヒーを飲むのに便利です。", "10. Esto es práctico para beber café.", "これはコーヒーをのむのにべんりです")
        ],
        "exercises": [
            {"q": "'Estudio japonés PARA (con el firme propósito de) ir a Japón':", "options": [{"text": "日本へ行くのに、日本語を勉強します。", "correct": False}, {"text": "日本へ行くために、日本語を勉強します。", "correct": True}, {"text": "日本へ行くから、日本語を勉強します。", "correct": False}]},
            {"q": "'Esta bolsa es útil PARA comprar (su función)':", "options": [{"text": "この袋は買い物するのに役に立ちます。", "correct": True}, {"text": "この袋は買い物するために役に立ちます。", "correct": False}, {"text": "この袋は買い物するから役に立ちます。", "correct": False}]},
            {"q": "Sustantivos antes de 'Tame ni' llevan...", "options": [{"text": "な (Na)", "correct": False}, {"text": "の (No)", "correct": True}, {"text": "Nada, van pegados", "correct": False}]},
            {"q": "'Por (para) mi familia, trabajo': ___ために働きます。", "options": [{"text": "家族", "correct": False}, {"text": "家族な", "correct": False}, {"text": "家族の", "correct": True}]},
            {"q": "'Toma 2 horas PARA llegar a Tokio' (Se expresa tiempo/dinero):", "options": [{"text": "東京へ行くために、２時間かかります。", "correct": False}, {"text": "東京へ行くのに、２時間かかります。", "correct": True}, {"text": "東京へ行くから、２時間かかります。", "correct": False}]},
            {"q": "¿Qué palabra NO suele ir después de 'のに'?", "options": [{"text": "使います (Tsukaimasu - usar)", "correct": False}, {"text": "役に立ちます (Yakunitachimasu - ser útil)", "correct": False}, {"text": "頑張ります (Ganbarimasu - esforzarse)", "correct": True}]},
            {"q": "'Para comprar un coche (Kuruma), ahorro dinero (Chokin suru)':", "options": [{"text": "車を買うために、貯金します。", "correct": True}, {"text": "車を買うのに、貯金します。", "correct": False}, {"text": "車を買うだから、貯金します。", "correct": False}]},
            {"q": "'Este diccionario (Jisho) es muy útil PARA investigar palabras' (Shiraberu):", "options": [{"text": "言葉を調べるために役に立ちます。", "correct": False}, {"text": "言葉を調べるのに役に立ちます。", "correct": True}, {"text": "言葉を調べるから役に立ちます。", "correct": False}]},
            {"q": "Para la SALUD (Kenkou, sustantivo):", "options": [{"text": "健康のに (Kenkou no ni)", "correct": False}, {"text": "健康ために (Kenkou tame ni)", "correct": False}, {"text": "健康のために (Kenkou no tame ni)", "correct": True}]},
            {"q": "Si quieres decir 'Voy a ir en taxi para NO llegar tarde' (Negativo de Okureru):", "options": [{"text": "遅れないために、タクシーで行きます。", "correct": True}, {"text": "遅れるために、タクシーで行きます。", "correct": False}, {"text": "遅れないのに、タクシーで行きます。", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "けんじさん、毎日遅くまで勉強していますね。", "Kenji, estudias hasta tarde todos los días, ¿no?"),
            ("ja-JP-KeitaNeural", "はい。日本の大学に入るために、頑張っているんです。", "Sí. Me estoy esforzando para (con el propósito de) entrar a una universidad japonesa."),
            ("ja-JP-NanamiNeural", "日本の大学ですか。すごいですね。何になりたいんですか。", "¿A una universidad japonesa? Es increíble. ¿Qué quieres ser?"),
            ("ja-JP-KeitaNeural", "エンジニアになるために、もっと数学と日本語を勉強しなければなりません。", "Para ser ingeniero, tengo que estudiar más matemáticas y japonés."),
            ("ja-JP-NanamiNeural", "そうですか。この本は日本語の文法を勉強するのにとても役に立ちますよ。", "¿Ah sí? Este libro es muy útil para (la función de) estudiar la gramática japonesa."),
            ("ja-JP-KeitaNeural", "本当ですか。貸してくれませんか。", "¿De verdad? ¿Me harías el favor de prestármelo?"),
            ("ja-JP-NanamiNeural", "もちろんです。合格するために、使ってくださいね。", "Por supuesto. Úsalo para (con el propósito de) aprobar."),
            ("ja-JP-KeitaNeural", "ありがとうございます！", "¡Muchas gracias!")
        ]
    },
    18: {
        "title": "Apariencia y Predicciones (~そうです)",
        "grammar": [
            "<strong>1. Apariencia visual (Parece que...):</strong> V(masu sin masu) / Adj-i(sin i) / Adj-na(sin na) + そうです. Negativo: V(nasasou desu), Adj(ku nasasou desu). Ej. 降りそうです (Parece que lloverá).",
            "<strong>2. Transmisión (Dicen que... / Escuché que...):</strong> Forma Plana + そうです. Se usa para repetir información obtenida de otra fuente (noticias, rumores). Ej. 降るそうです (Dicen que lloverá).",
            "<em>Clave:</em> Fíjate bien en la conjugación antes de 'sou desu'. Si es forma Plana, es 'dicen que'. Si es raíz, es 'parece que'."
        ],
        "examples": [
            ("空が暗いです。雨が降りそうです。", "1. El cielo está oscuro. Parece que va a llover (Apariencia).", "そらがくらいです。あめがふりそうです"),
            ("天気予報によると、明日は雨が降るそうです。", "2. Según el pronóstico, dicen que mañana lloverá (Transmisión).", "てんきよほうによると、あしたはあめがふるそうです"),
            ("このケーキは美味しそうです。", "3. Este pastel parece delicioso.", "このケーキはおいしそうです"),
            ("山田さんは来ないそうです。", "4. Escuché que Yamada no vendrá (Transmisión).", "やまださんはこないそうです"),
            ("この仕事は難しそうです。", "5. Este trabajo parece difícil.", "このしごとはむずかしそうです"),
            ("田中さんはとても元気そうです。", "6. Tanaka parece muy enérgico (Genki es Adj-Na).", "たなかさんはとてもげんきそうです"),
            ("ニュースによると、事故があったそうです。", "7. Según las noticias, dicen que hubo un accidente.", "ニュースによると、じこがあったそうです"),
            ("この映画はあまり面白くなさそうです。", "8. Esta película no parece muy interesante.", "このえいがはあまりおもしろくなさそうです"),
            ("ボタンが取れそうです。", "9. El botón parece que se va a caer (a punto de...).", "ボタンがとれそうです"),
            ("彼は結婚するそうです。", "10. Dicen que él se va a casar.", "かれはけっこんするそうです")
        ],
        "exercises": [
            {"q": "El verbo Furu (llover). 'Parece que va a llover' se dice...", "options": [{"text": "降るそうです", "correct": False}, {"text": "降りそうです", "correct": True}, {"text": "降らないそうです", "correct": False}]},
            {"q": "'Dicen que lloverá' (Transmisión):", "options": [{"text": "降るそうです", "correct": True}, {"text": "降りそうです", "correct": False}, {"text": "降ったそうです", "correct": False}]},
            {"q": "'Este pastel parece delicioso' (Oishii):", "options": [{"text": "美味しいそうです", "correct": False}, {"text": "美味しそうです", "correct": True}, {"text": "美味しくそうです", "correct": False}]},
            {"q": "'Escuché que el pastel está delicioso' (Transmisión, se usa forma plana del adjetivo):", "options": [{"text": "美味しそうです", "correct": False}, {"text": "美味しいそうです", "correct": True}, {"text": "美味しかったそうです", "correct": False}]},
            {"q": "Negativo de apariencia. 'No parece interesante' (Omoshiroi -> Omoshiroku nai -> Omoshiroku nasa sou):", "options": [{"text": "面白くないそうです", "correct": False}, {"text": "面白そうじゃありません", "correct": False}, {"text": "面白くなさそうです", "correct": True}]},
            {"q": "¿Qué expresión se usa a menudo con la 'transmisión' (dicen que)?", "options": [{"text": "～によると (Según...)", "correct": True}, {"text": "～のために (Para...)", "correct": False}, {"text": "～ながら (Mientras...)", "correct": False}]},
            {"q": "'Escuché que el profesor no viene' (Konai):", "options": [{"text": "先生は来ないそうです", "correct": True}, {"text": "先生は来なさそうです", "correct": False}, {"text": "先生は来ませんそうです", "correct": False}]},
            {"q": "'El equipaje parece pesado' (Omoi):", "options": [{"text": "重いそうです", "correct": False}, {"text": "重そうです", "correct": True}, {"text": "重くそうです", "correct": False}]},
            {"q": "'Según el periódico (Shinbun ni yoruto), hubo un terremoto' (Jishin ga atta):", "options": [{"text": "地震があったそうです", "correct": True}, {"text": "地震がありそうです", "correct": False}, {"text": "地震があるそうです", "correct": False}]},
            {"q": "'Esta manzana parece dulce' (Amai):", "options": [{"text": "甘そうです", "correct": True}, {"text": "甘いそうです", "correct": False}, {"text": "甘くそうです", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-KeitaNeural", "空が暗くなってきましたね。今にも雨が降りそうです。", "El cielo se ha oscurecido. Parece que va a llover en cualquier momento."),
            ("ja-JP-NanamiNeural", "そうですね。天気予報によると、午後から大雨になるそうですよ。", "Así es. Según el pronóstico del tiempo, dicen que a partir de la tarde habrá fuertes lluvias."),
            ("ja-JP-KeitaNeural", "ええっ、傘を持っていません。困りました。", "¿Eh? No he traído paraguas. Qué problema."),
            ("ja-JP-NanamiNeural", "私の傘に入りますか。駅までなら一緒に行けますよ。", "¿Quieres meterte en mi paraguas? Si es hasta la estación podemos ir juntos."),
            ("ja-JP-KeitaNeural", "すみません、助かります。あ、あのケーキ屋さん、美味しそうですね。", "Disculpa, me salvas. Ah, esa pastelería, (los pasteles) parecen deliciosos."),
            ("ja-JP-NanamiNeural", "あそこは最近オープンした店だそうです。いつも行列ができています。", "Dicen que es una tienda que abrió recientemente. Siempre hay cola."),
            ("ja-JP-KeitaNeural", "じゃあ、雨が降る前に少し並んでみましょうか。", "Entonces, ¿intentamos hacer cola un rato antes de que llueva?"),
            ("ja-JP-NanamiNeural", "いいですね！甘いものを食べれば、雨でも元気になりそうです。", "¡Qué buena idea! Si comemos algo dulce, parece que nos sentiremos bien incluso con lluvia.")
        ]
    },
    19: {
        "title": "Exceso y Facilidad (~すぎる / ~やすい / ~にくい)",
        "grammar": [
            "<strong>V(masu sin masu) / Adj(raíz) + すぎます:</strong> En exceso, demasiado. Ej. 食べすぎました (Comí demasiado), 高すぎます (Es demasiado caro).",
            "<strong>V(masu sin masu) + やすいです:</strong> Es fácil de hacer. Trata el verbo como si fuera un Adjetivo-i. Ej. このペンは書きやすいです (Es fácil escribir con esta pluma).",
            "<strong>V(masu sin masu) + にくいです:</strong> Es difícil de hacer. Ej. この薬は飲みにくいです (Esta medicina es difícil de tomar)."
        ],
        "examples": [
            ("昨日の夜、お酒を飲みすぎました。", "1. Ayer por la noche bebí demasiado.", "きのうのよる、おさけをのみすぎました"),
            ("このテレビは高すぎます。", "2. Esta televisión es demasiado cara.", "このテレビはたかすぎます"),
            ("この靴はとても歩きやすいです。", "3. Estos zapatos son muy fáciles para caminar (cómodos).", "このくつはとてもあるきやすいです"),
            ("漢字は覚えにくいです。", "4. Los kanjis son difíciles de memorizar.", "かんじはおぼえにくいです"),
            ("静かすぎて、怖いです。", "5. Está demasiado silencioso (Adj-Na), y me da miedo.", "しずかすぎて、こわいです"),
            ("この本は字が大きくて読みやすいです。", "6. Este libro tiene letras grandes y es fácil de leer.", "このほんはじがおおきくてよみやすいです"),
            ("雨の日は運転しにくいです。", "7. Los días de lluvia son difíciles para conducir.", "あめのひはうんてんしにくいです"),
            ("塩を入れすぎました。", "8. Le puse (metí) demasiada sal.", "しおをいれすぎました"),
            ("この肉は硬くて食べにくいです。", "9. Esta carne está dura y es difícil de comer.", "このにくはかたくてたべにくいです"),
            ("彼女は働きすぎです。", "10. Ella trabaja demasiado.", "かのじょははたらきすぎです")
        ],
        "exercises": [
            {"q": "¿Qué forma verbal se usa antes de すぎる, やすい y にくい?", "options": [{"text": "Forma MASU pero quitando el 'masu' (Ej: 飲み)", "correct": True}, {"text": "Forma Diccionario (Ej: 飲む)", "correct": False}, {"text": "Forma TE (Ej: 飲んで)", "correct": False}]},
            {"q": "'Es demasiado caro' (Takai):", "options": [{"text": "高すぎます (Takasugimasu)", "correct": True}, {"text": "高いすぎます (Takaisugimasu)", "correct": False}, {"text": "高くてすぎます", "correct": False}]},
            {"q": "'Es fácil de entender' (Wakaru -> Wakarimasu):", "options": [{"text": "わかりやすいです", "correct": True}, {"text": "わかるやすいです", "correct": False}, {"text": "わかってやすいです", "correct": False}]},
            {"q": "'Comí demasiado y me duele el estómago' (Taberu):", "options": [{"text": "食べすぎて、お腹が痛いです", "correct": True}, {"text": "食べるすぎて、お腹が痛いです", "correct": False}, {"text": "食べたすぎて、お腹が痛いです", "correct": False}]},
            {"q": "'Esta medicina es difícil de tomar' (Kusuri wo nomu):", "options": [{"text": "この薬は読みにくいです", "correct": False}, {"text": "この薬は飲みにくいです", "correct": True}, {"text": "この薬は飲むにくいです", "correct": False}]},
            {"q": "¿Cómo se conjuga 'やすい' al negativo? (Ej: No es fácil de leer)", "options": [{"text": "読みやすくないです", "correct": True}, {"text": "読みやすいじゃないです", "correct": False}, {"text": "読みやすありません", "correct": False}]},
            {"q": "'Aquel examen fue demasiado difícil' (Muzukashii -> Pasado):", "options": [{"text": "難しすぎました", "correct": True}, {"text": "難しいすぎました", "correct": False}, {"text": "難しくてすぎました", "correct": False}]},
            {"q": "'Esta cama (Beddo) es difícil para dormir' (Neru):", "options": [{"text": "このベッドは寝にくいです", "correct": True}, {"text": "このベッドは寝るにくいです", "correct": False}, {"text": "このベッドは寝やすいです", "correct": False}]},
            {"q": "'Canté demasiado' (Utau):", "options": [{"text": "歌いすぎました", "correct": True}, {"text": "歌うすぎました", "correct": False}, {"text": "歌ってすぎました", "correct": False}]},
            {"q": "Para Adjetivos Na como 'Kantan' (Fácil), ¿cómo se dice 'Demasiado fácil'?", "options": [{"text": "簡単すぎます (Kantan sugimasu)", "correct": True}, {"text": "簡単なすぎます", "correct": False}, {"text": "簡単だすぎます", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "昨日の夜、ゲームをやりすぎて、目が痛いです。", "Ayer por la noche jugué demasiado a videojuegos y me duelen los ojos."),
            ("ja-JP-KeitaNeural", "大丈夫ですか。最近のゲームは面白すぎて、時間がすぐ経ちますね。", "¿Estás bien? Los juegos de últimamente son demasiado interesantes, el tiempo pasa volando."),
            ("ja-JP-NanamiNeural", "はい。でも、このコントローラーは少し使いにくいです。", "Sí. Pero este mando es un poco difícil de usar."),
            ("ja-JP-KeitaNeural", "私もそう思います。ボタンが小さすぎて、押しにくいですよね。", "Yo también lo creo. Los botones son demasiado pequeños y difíciles de presionar, ¿verdad?"),
            ("ja-JP-NanamiNeural", "ええ。新しいものを買いたいんですが、高すぎます。", "Sí. Quiero comprar uno nuevo, pero son demasiado caros."),
            ("ja-JP-KeitaNeural", "インターネットで探せば、安くて使いやすいものが見つかりますよ。", "Si buscas por internet, encontrarás algo barato y fácil de usar."),
            ("ja-JP-NanamiNeural", "じゃあ、後で一緒に探してくれませんか。", "Entonces, ¿no me harías el favor de buscar conmigo luego?"),
            ("ja-JP-KeitaNeural", "いいですよ。見つけやすいサイトを知っていますから。", "Vale. Conozco un sitio web donde es fácil encontrar cosas.")
        ]
    },
    20: {
        "title": "Forma Causativa (~せる / ~させる)",
        "grammar": [
            "<strong>G1 (u->a + seru), G2 (ru->saseru), G3 (suru->saseru, kuru->kosaseru)</strong>",
            "<strong>N1(Pers. Superior) は N2(Pers. Inferior) に V(causativo):</strong> Hacer que alguien haga algo (obligación) o permitirle que lo haga (permiso).",
            "<em>Ej:</em> お母さんは子供に野菜を食べさせました (La madre hizo que el niño comiera verduras).",
            "<strong>V(causativo) + ていただけませんか:</strong> ¿Me permitiría...? (Pedir permiso muy cortésmente al jefe o profesor)."
        ],
        "examples": [
            ("お母さんは子供に野菜を食べさせました。", "1. La madre hizo que el niño comiera verduras.", "おかあさんはこどもにやさいをたべさせました"),
            ("先生は学生に漢字を書かせました。", "2. El profesor hizo que los estudiantes escribieran kanjis.", "せんせいはがくせいにかんじをかかせました"),
            ("私は弟を買い物に行かせました。", "3. Yo mandé (hice ir) a mi hermano a hacer compras.", "わたしはおとうとをかいものにいかせました"),
            ("早く帰らせていただけませんか。", "4. ¿Me permitiría irme a casa temprano? (Muy cortés).", "はやくかえらせていただけませんか"),
            ("今日は休ませてください。", "5. Por favor, permítame descansar (faltar) hoy.", "きょうはやすませてください"),
            ("子供に好きなことをさせます。", "6. Dejo (permito) a mi hijo hacer lo que le gusta.", "こどもにすきなことをさせます"),
            ("部長は私に出張に行かせました。", "7. El jefe me hizo ir de viaje de negocios.", "ぶちょうはわたしにしゅっちょうにいかせました"),
            ("ここで写真を撮らせていただけませんか。", "8. ¿Me permitiría tomar una foto aquí?", "ここでしゃしんをとらせていただけませんか"),
            ("父は私に車を運転させてくれません。", "9. Mi padre no me permite conducir el coche.", "ちちはわたしにくるまをうんてんさせてくれません"),
            ("話をさせてください。", "10. Por favor, déjeme hablar.", "はなしをさせてください")
        ],
        "exercises": [
            {"q": "¿Cómo se forma el causativo de 食べる (Comer, Grupo II)?", "options": [{"text": "食べさせます (Tabesasemasu)", "correct": True}, {"text": "食べせます (Tabesemasu)", "correct": False}, {"text": "食べられます (Taberaremasu - esto es pasiva/potencial)", "correct": False}]},
            {"q": "¿Cómo se forma el causativo de 行く (Ir, Grupo I)?", "options": [{"text": "行かせます (Ikasemasu)", "correct": True}, {"text": "行させます (Ikasasemasu)", "correct": False}, {"text": "行かれます (Ikaremasu)", "correct": False}]},
            {"q": "¿Cómo se forma el causativo de する (Hacer, Grupo III)?", "options": [{"text": "させます (Sasemasu)", "correct": True}, {"text": "されます (Saremasu)", "correct": False}, {"text": "しさせます (Shisasemasu)", "correct": False}]},
            {"q": "'La madre hizo estudiar al niño': 母は子供に勉強___。", "options": [{"text": "させました", "correct": True}, {"text": "しました", "correct": False}, {"text": "されました", "correct": False}]},
            {"q": "¿Qué frase se usa para pedir PERMISO cortésmente a tu jefe? (Ej: Permítame descansar)", "options": [{"text": "休ませていただけませんか", "correct": True}, {"text": "休んでいただけませんか", "correct": False}, {"text": "休んでくれませんか", "correct": False}]},
            {"q": "'Por favor, déjeme (permítame) ir' (Iku):", "options": [{"text": "行かせてください", "correct": True}, {"text": "行ってください", "correct": False}, {"text": "行かれないでください", "correct": False}]},
            {"q": "'El profesor nos HIZO leer el libro' (Yomu):", "options": [{"text": "先生は私たちに本を読ませました", "correct": True}, {"text": "先生は私たちに本を読まれました", "correct": False}, {"text": "先生は私たちに本を読みました", "correct": False}]},
            {"q": "¿Cuál es el causativo de 待つ (Matsu - esperar, Grupo I)? (Hacer esperar a alguien)", "options": [{"text": "待たせます (Matasemasu)", "correct": True}, {"text": "待させます", "correct": False}, {"text": "待ちせます", "correct": False}]},
            {"q": "'Siento haberte hecho esperar' (Usando forma Te de causativo):", "options": [{"text": "待たせて、すみません", "correct": True}, {"text": "待って、すみません", "correct": False}, {"text": "待たれて、すみません", "correct": False}]},
            {"q": "¿Qué significa '子供にゲームをさせます'?", "options": [{"text": "Permito/Dejo que el niño juegue videojuegos.", "correct": True}, {"text": "El niño me obliga a jugar videojuegos.", "correct": False}, {"text": "El niño juega videojuegos solo.", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-KeitaNeural", "部長、すみません。明日、休ませていただけませんか。", "Jefe, disculpe. ¿Me permitiría tomarme el día libre mañana?"),
            ("ja-JP-NanamiNeural", "どうしたんですか。", "¿Qué ocurre?"),
            ("ja-JP-KeitaNeural", "実は、息子が熱を出しまして、病院へ行かせたいんです。", "La verdad es que mi hijo tiene fiebre, y quiero hacerle ir (llevarlo) al hospital."),
            ("ja-JP-NanamiNeural", "それは大変ですね。もちろん、休んでください。", "Eso es un problema. Por supuesto, tómate el día libre."),
            ("ja-JP-KeitaNeural", "ありがとうございます。妻も仕事があるので、私が休むしかありません。", "Muchas gracias. Mi esposa también tiene trabajo, así que no me queda más remedio que faltar yo."),
            ("ja-JP-NanamiNeural", "わかりますよ。しっかり休ませてあげてください。仕事のことは心配しなくていいですよ。", "Lo entiendo. Déjale descansar (haz el favor de permitirle descansar) bien. No te preocupes por el trabajo."),
            ("ja-JP-KeitaNeural", "申し訳ありません。来週からまた頑張ります。", "Lo siento mucho. A partir de la semana que viene me esforzaré de nuevo."),
            ("ja-JP-NanamiNeural", "ええ、息子さんにもお大事にと伝えてください。", "Sí, dile a tu hijo que se mejore.")
        ]
    }
}

base_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\lessons"
audio_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\audio"
os.makedirs(audio_dir, exist_ok=True)

# Generate HTML and Audio for 16-20
for i in range(16, 21):
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
for i in range(16, 21):
    title = data[i]["title"]
    links_html += f'''                        <a href="lessons/jlpt-n4-{i}.html" target="main_frame" class="nav-link">
                            <span class="nav-num">{i}</span> {title}
                        </a>\n'''

target = '                            <span class="nav-num">15</span> Interrogativos incrustados (~か / ~かどうか)\n                        </a>\n'
if target in content:
    new_content = content.replace(target, target + links_html)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Updated index.html")
else:
    print("WARNING: Could not find target in index.html")

print("Running add_furigana.py...")
subprocess.run("python add_furigana.py", shell=True)
print("ALL TASKS COMPLETED!")
