import os

data = {
    1: {
        "title": "Explicar situaciones (~んです)",
        "grammar": [
            "<strong>~んです (ndesu):</strong> Se usa para explicar razones, pedir explicaciones o enfatizar una situación.",
            "<strong>Verbos:</strong> Futsukei + んです (Ej: 読むんです).",
            "<strong>Adj-i:</strong> Futsukei + んです (Ej: 痛いんです).",
            "<strong>Adj-na / Sustantivos:</strong> ~な + んです (Ej: きれいなんです / 病気なんです).",
            "<strong>~んですが、~ていただけませんか:</strong> Plantear una situación y pedir un favor (muy formal)."
        ],
        "examples": [
            ("どうして遅れたんですか。", "1. ¿Por qué has llegado tarde? (Pidiendo explicación)", "どうしておくれたんですか"),
            ("バスが来なかったんです。", "2. Es que el autobús no vino.", "バスがこなかったんです"),
            ("頭が痛いんです。", "3. Es que me duele la cabeza.", "あたまがいたいんです"),
            ("日本語がわからないんです。", "4. Es que no entiendo japonés.", "にほんごがわからないんです"),
            ("きれいなんです。", "5. Es que es bonito.", "きれいなんです"),
            ("雨なんです。", "6. Es que está lloviendo (es lluvia).", "あめなんです"),
            ("明日テストがあるんです。", "7. Es que mañana tengo un examen.", "あしたテストがあるんです"),
            ("どうしたんですか。", "8. ¿Qué te pasa? (Al ver a alguien mal)", "どうしたんですか"),
            ("気分が悪いんです。", "9. Es que no me encuentro bien.", "きぶんがわるいんです"),
            ("切符がないんですが、どうしたらいいですか。", "10. Es que no tengo billete, ¿qué debería hacer?", "きっぷがないんですが、どうしたらいいですか")
        ],
        "exercises": [
            {"q": "¿Para qué sirve principalmente la terminación ~んです?", "options": [{"text": "Para dar órdenes.", "correct": False}, {"text": "Para explicar razones o situaciones.", "correct": True}, {"text": "Para expresar deseos.", "correct": False}]},
            {"q": "¿Cómo se dice 'Es que me duele (itai)'?", "options": [{"text": "痛いなんです", "correct": False}, {"text": "痛いんです", "correct": True}, {"text": "痛いだんです", "correct": False}]},
            {"q": "¿Cómo se conecta un Sustantivo con んです? Ej. 'Enfermedad' (Byouki):", "options": [{"text": "病気なんです", "correct": True}, {"text": "病気んです", "correct": False}, {"text": "病気だんです", "correct": False}]},
            {"q": "Persona A: '¿No comes?'. Persona B: 'Es que ___'.", "options": [{"text": "お腹が痛いんです。(Me duele el estómago)", "correct": True}, {"text": "お腹が痛いです。(No da el matiz explicativo)", "correct": False}, {"text": "お腹が痛いくて。", "correct": False}]},
            {"q": "'Es que está limpio' (Kirei - Adj-na):", "options": [{"text": "きれいんです", "correct": False}, {"text": "きれいなんです", "correct": True}, {"text": "きれだなんです", "correct": False}]},
            {"q": "Para preguntar a alguien preocupado '¿Qué te pasa?':", "options": [{"text": "どうしてですか。", "correct": False}, {"text": "どうしたんですか。", "correct": True}, {"text": "なんですか。", "correct": False}]},
            {"q": "¿Qué expresión usas para pedir un consejo después de plantear un problema con ~んですが?", "options": [{"text": "どうしたらいいですか。", "correct": True}, {"text": "どうしましょうか。", "correct": False}, {"text": "どうしてもいいですか。", "correct": False}]},
            {"q": "¿Cómo se dice 'Es que me gusta' (Suki - Adj-na)?", "options": [{"text": "好きなんです", "correct": True}, {"text": "好きんです", "correct": False}, {"text": "好きだんです", "correct": False}]},
            {"q": "Persona A: '¿Por qué no fuiste?'. Persona B: 'Es que ___ tiempo'.", "options": [{"text": "時間がありませんんです", "correct": False}, {"text": "時間がなかったんです", "correct": True}, {"text": "時間がないんです", "correct": False}]},
            {"q": "¿Qué verbo usas para 'Me gustaría que me lo explicaras'?", "options": [{"text": "説明していただけませんか", "correct": True}, {"text": "説明してもいいですか", "correct": False}, {"text": "説明してはいけませんか", "correct": False}]}
        ]
    },
    2: {
        "title": "Forma Potencial (Puedo hacer)",
        "grammar": [
            "<strong>Forma Potencial (Kanoukei):</strong> Indica capacidad o posibilidad.",
            "<strong>Grupo I:</strong> Cambia la vocal 'u' por 'e' + ru (Ej. 書く -> 書ける).",
            "<strong>Grupo II:</strong> Quita 'ru' + 'rareru' (Ej. 食べる -> 食べられる).",
            "<strong>Grupo III:</strong> する -> できる | 来る -> 来られる (korareru).",
            "<strong>Partícula:</strong> El objeto (を) pasa a ser (が). Ej: 日本語が話せる (Puedo hablar japonés)."
        ],
        "examples": [
            ("私は日本語が話せます。", "1. Yo puedo hablar japonés.", "わたしはにほんごがはなせます"),
            ("漢字が書けますか。", "2. ¿Puedes escribir kanjis?", "かんじがかけますか"),
            ("刺身が食べられません。", "3. No puedo comer sashimi.", "さしみがたべられません"),
            ("明日ここへ来られますか。", "4. ¿Puedes venir aquí mañana?", "あしたここへこられますか"),
            ("自転車に乗れます。", "5. Puedo montar en bicicleta.", "じてんしゃにのれます"),
            ("あそこの銀行でお金が換えられます。", "6. En aquel banco se puede cambiar dinero.", "あそこのぎんこうでおかねがかえられます"),
            ("この水は飲めます。", "7. Esta agua se puede beber.", "このみずはのめます"),
            ("早く起きられませんでした。", "8. No pude levantarme temprano.", "はやくおきられませんでした"),
            ("歌が歌えます。", "9. Puedo cantar canciones.", "うたがうたえます"),
            ("英語が読めますか。", "10. ¿Puedes leer inglés?", "えいごがよめますか")
        ],
        "exercises": [
            {"q": "¿Cuál es la forma potencial de 読みます (Leer - Grupo I)?", "options": [{"text": "読まれます (Yomaremasu)", "correct": False}, {"text": "読めます (Yomemasu)", "correct": True}, {"text": "読みられます (Yomiraremasu)", "correct": False}]},
            {"q": "¿Cuál es la forma potencial de 食べます (Comer - Grupo II)?", "options": [{"text": "食べられます (Taberaremasu)", "correct": True}, {"text": "食べれます (Taberemasu - coloquial, pero no correcto en examen)", "correct": False}, {"text": "食べませます", "correct": False}]},
            {"q": "¿Cuál es la forma potencial de 来ます (Kimasu - Venir - Grupo III)?", "options": [{"text": "こられます (Koraremasu)", "correct": True}, {"text": "きられます (Kiraremasu)", "correct": False}, {"text": "これます (Koremasu)", "correct": False}]},
            {"q": "Si puedes tocar la guitarra, ¿qué partícula sustituye a を?", "options": [{"text": "が (ギターが弾けます)", "correct": True}, {"text": "に (ギターに弾けます)", "correct": False}, {"text": "へ (ギターへ弾けます)", "correct": False}]},
            {"q": "¿Cuál es la forma potencial de します (Hacer)?", "options": [{"text": "しられます", "correct": False}, {"text": "できます (Dekimasu)", "correct": True}, {"text": "すれます", "correct": False}]},
            {"q": "'Puedo nadar' (Nadar = Oyogimasu):", "options": [{"text": "泳げます (Oyogemasu)", "correct": True}, {"text": "泳ぎられます (Oyogiraremasu)", "correct": False}, {"text": "泳がれます (Oyogaremasu)", "correct": False}]},
            {"q": "'No puedo comprarlo' (Comprar = Kaimasu):", "options": [{"text": "買えません", "correct": True}, {"text": "買われません", "correct": False}, {"text": "買いません", "correct": False}]},
            {"q": "¿Cuál es la forma diccionario de 飲めます (Poder beber)?", "options": [{"text": "飲める (Nomeru)", "correct": True}, {"text": "飲む (Nomu)", "correct": False}, {"text": "飲まれる (Nomareru)", "correct": False}]},
            {"q": "Persona A: '¿Puedes comer comida picante?'. Persona B: 'No, ___'.", "options": [{"text": "食べません (No como)", "correct": False}, {"text": "食べられません (No puedo comer)", "correct": True}, {"text": "食べられませんでした", "correct": False}]},
            {"q": "'Puedo esperar' (Esperar = Machimasu):", "options": [{"text": "待てます (Matemasu)", "correct": True}, {"text": "待たれます (Mataremasu)", "correct": False}, {"text": "待ちられます (Machiraremasu)", "correct": False}]}
        ]
    },
    3: {
        "title": "Acciones simultáneas (~ながら)",
        "grammar": [
            "<strong>V1(raíz) + ながら + V2:</strong> Hacer dos acciones al mismo tiempo. 'Mientras hago V1, hago V2'.",
            "<strong>La acción principal:</strong> Es el Verbo 2 (V2).",
            "<strong>V(te) います:</strong> Hábitos o rutinas continuas. Ej: 毎日運動しています (Hago ejercicio todos los días).",
            "<strong>N も V ば, N も V ます:</strong> 'Hace tanto esto como aquello' (Patrón avanzado para N4)."
        ],
        "examples": [
            ("音楽を聞きながら、勉強します。", "1. Estudio mientras escucho música.", "おんがくをききながら、べんきょうします"),
            ("コーヒーを飲みながら、話しませんか。", "2. ¿Hablamos mientras tomamos café?", "コーヒーをのみながら、はなしませんか"),
            ("歩きながら、電話をしないでください。", "3. Por favor, no hables por teléfono mientras caminas.", "あるきながら、でんわをしないでください"),
            ("運転しながら、スマホを見てはいけません。", "4. No debes mirar el teléfono mientras conduces.", "うんてんしながら、スマホをみてはいけません"),
            ("ご飯を食べながら、テレビを見ます。", "5. Veo la televisión mientras como.", "ごはんをたべながら、テレビをみます"),
            ("毎朝ジョギングをしています。", "6. Todas las mañanas hago footing (hábito).", "まいあさジョギングをしています"),
            ("週末はいつも子供と遊んでいます。", "7. Los fines de semana siempre juego con mis hijos.", "しゅうまつはいつもこどもとあそんでいます"),
            ("歌を歌いながら、ピアノを弾きます。", "8. Toco el piano mientras canto una canción.", "うたをうたいながら、ピアノをひきます"),
            ("働きながら、大学で勉強しています。", "9. Estudio en la universidad mientras trabajo.", "はたらきながら、だいがくでべんきょうしています"),
            ("お茶を飲みながら、本を読みます。", "10. Leo un libro mientras bebo té.", "おちゃをのみながら、ほんをよみます")
        ],
        "exercises": [
            {"q": "¿Cómo se forma '~ながら' (Mientras)?", "options": [{"text": "Forma TE + ながら", "correct": False}, {"text": "Raíz del verbo (quita masu) + ながら", "correct": True}, {"text": "Forma Diccionario + ながら", "correct": False}]},
            {"q": "'Mientras bebo té...':", "options": [{"text": "飲みながら (Nomi-nagara)", "correct": True}, {"text": "飲んでながら (Nonde-nagara)", "correct": False}, {"text": "飲むながら (Nomu-nagara)", "correct": False}]},
            {"q": "'Leo el periódico mientras como' (La acción principal es Leer):", "options": [{"text": "新聞を読みながら、ご飯を食べます。", "correct": False}, {"text": "ご飯を食べながら、新聞を読みます。", "correct": True}, {"text": "ご飯を食べるながら、新聞を読みます。", "correct": False}]},
            {"q": "¿Qué estructura se usa para expresar una RUTINA que haces todos los días?", "options": [{"text": "V(te) います", "correct": True}, {"text": "V(ta) ことがあります", "correct": False}, {"text": "V(te) しまいます", "correct": False}]},
            {"q": "'Todos los días tomo leche' (Hábito):", "options": [{"text": "毎日牛乳を飲んでいます。", "correct": True}, {"text": "毎日牛乳を飲んでありました。", "correct": False}, {"text": "毎日牛乳を飲みながらです。", "correct": False}]},
            {"q": "'Por favor, no conduzcas (unten) MIENTRAS bebes alcohol':", "options": [{"text": "お酒を飲みながら、運転しないでください。", "correct": True}, {"text": "お酒を飲んでながら、運転しないでください。", "correct": False}, {"text": "運転しながら、お酒を飲みないでください。", "correct": False}]},
            {"q": "'Trabajo mientras escucho música' (Trabajar = Hatarakimasu):", "options": [{"text": "音楽を聞きながら、働きます。", "correct": True}, {"text": "音楽を聞いてながら、働きます。", "correct": False}, {"text": "音楽を聞くながら、働きます。", "correct": False}]},
            {"q": "¿Qué verbo es la acción PRINCIPAL en 'Aしながら、Bします'?", "options": [{"text": "A (Lo que se dice primero)", "correct": False}, {"text": "B (Lo que va al final de la oración)", "correct": True}, {"text": "Ambos son iguales", "correct": False}]},
            {"q": "Persona A: '¿Estudias japonés?'. Persona B: 'Sí, estudio ___ trabajo'.", "options": [{"text": "働きながら (Hataraki-nagara)", "correct": True}, {"text": "働いてながら (Hataraite-nagara)", "correct": False}, {"text": "働くながら (Hataraku-nagara)", "correct": False}]},
            {"q": "¿Se puede usar '~ながら' con estados? Ej. 'Mientras está frío (Samui nagara)':", "options": [{"text": "No, normalmente se usa con verbos de acción.", "correct": True}, {"text": "Sí, es muy común.", "correct": False}, {"text": "Solo con Adjetivos-na.", "correct": False}]}
        ]
    },
    4: {
        "title": "Lamentaciones y Finalización (~て しまいます)",
        "grammar": [
            "<strong>V(te) しまいます:</strong> Indica que una acción se completará totalmente.",
            "<strong>V(te) しまいました:</strong> 1) La acción se ha completado. 2) Expresa arrepentimiento, error o lamentación ('Por desgracia... / Sin querer...').",
            "<strong>Forma coloquial:</strong> ~てしまう -> ~ちゃう / ~でしまう -> ~じゃう."
        ],
        "examples": [
            ("パスポートをなくしてしまいました。", "1. He perdido el pasaporte (lamentación).", "パスポートをなくしてしまいました"),
            ("漢字の宿題を全部やってしまいました。", "2. He terminado completamente los deberes de kanji.", "かんじのしゅくだいをぜんぶやってしまいました"),
            ("電車に傘を忘れてしまいました。", "3. Olvidé el paraguas en el tren (por desgracia).", "でんしゃにかさをわすれてしまいました"),
            ("パソコンが壊れてしまいました。", "4. La computadora se ha roto (lamentación).", "パソコンがこわれてしまいました"),
            ("この本は明日までに読んでしまいます。", "5. Terminaré de leer este libro para mañana.", "このほんはあしたまでによんでしまいます"),
            ("ワインを全部飲んでしまいました。", "6. Me bebí todo el vino (completitud/lamento).", "ワインをぜんぶのんでしまいました"),
            ("鍵を落としてしまいました。", "7. Se me cayeron las llaves (y las perdí).", "かぎをおとしてしまいました"),
            ("道に迷ってしまいました。", "8. Me he perdido (en el camino).", "みちにまよってしまいました"),
            ("スーパーが閉まってしまいました。", "9. El supermercado se cerró (lamentación).", "スーパーがしまってしまいました"),
            ("指を切ってしまいました。", "10. Me corté el dedo (sin querer).", "ゆびをきってしまいました")
        ],
        "exercises": [
            {"q": "¿Cuáles son los DOS significados principales de V(te) しまいました?", "options": [{"text": "Deseo y Obligación", "correct": False}, {"text": "Acción completada y Lamentación/Arrepentimiento", "correct": True}, {"text": "Permiso y Prohibición", "correct": False}]},
            {"q": "'Olvidé la cartera' (Lamentación):", "options": [{"text": "財布を忘れてしまいました。", "correct": True}, {"text": "財布を忘れてありました。", "correct": False}, {"text": "財布を忘れておきました。", "correct": False}]},
            {"q": "'Se me rompió la cámara' (Kowaremasu):", "options": [{"text": "カメラが壊れていました。", "correct": False}, {"text": "カメラが壊れてしまいました。", "correct": True}, {"text": "カメラが壊れてみました。", "correct": False}]},
            {"q": "'Voy a terminar (completar) este pastel':", "options": [{"text": "このケーキを食べてしまいます。", "correct": True}, {"text": "このケーキを食べてしまいました。", "correct": False}, {"text": "このケーキを食べておきます。", "correct": False}]},
            {"q": "¿Cuál es la forma coloquial (hablada) de '食べてしまう'?", "options": [{"text": "食べちゃう (Tabechau)", "correct": True}, {"text": "食べじゃう (Tabejau)", "correct": False}, {"text": "食べきゃう (Tabekyau)", "correct": False}]},
            {"q": "¿Cuál es la forma coloquial de '飲んでしまう'?", "options": [{"text": "飲んちゃう", "correct": False}, {"text": "飲んじゃう (Nonjau)", "correct": True}, {"text": "飲んてまう", "correct": False}]},
            {"q": "Persona A: '¿Dónde está el informe?'. Persona B: 'Oh no, lo ___ en casa'.", "options": [{"text": "忘れていました", "correct": False}, {"text": "忘れてしまいました", "correct": True}, {"text": "忘れておきました", "correct": False}]},
            {"q": "'Me he resfriado' (Kaze o hikimasu - Lamentación):", "options": [{"text": "風邪を引いてしまいました。", "correct": True}, {"text": "風邪を引いてありました。", "correct": False}, {"text": "風邪を引いておきました。", "correct": False}]},
            {"q": "'He perdido el dinero' (Nakushimasu):", "options": [{"text": "お金をなくしてしまいました。", "correct": True}, {"text": "お金をなくしてありました。", "correct": False}, {"text": "お金をなくしておきました。", "correct": False}]},
            {"q": "'Me leí (completamente) el libro':", "options": [{"text": "本を読んでしまいました。", "correct": True}, {"text": "本を読んじゃった。(Ambas son correctas, una es formal y la otra coloquial)", "correct": True}, {"text": "本を読んでおきました。", "correct": False}]}
        ]
    },
    5: {
        "title": "Preparación previa (~て おきます)",
        "grammar": [
            "<strong>V(te) おきます:</strong> Significa 'Dejar algo preparado (para el futuro)'.",
            "<strong>Uso 1:</strong> Preparar algo antes de un evento. (Ej: Comprar bebidas antes de la fiesta).",
            "<strong>Uso 2:</strong> Dejar las cosas como están después de usarlas. (Ej: Dejar la ventana abierta).",
            "<strong>Forma coloquial:</strong> ~ておく -> ~とく / ~でおく -> ~どく."
        ],
        "examples": [
            ("旅行の前に、ホテルを予約しておきます。", "1. Antes del viaje, reservaré (dejaré reservado) el hotel.", "りょこうのまえに、ホテルをよやくしておきます"),
            ("パーティーの前に、飲み物を買っておきます。", "2. Antes de la fiesta, compraré bebidas (para que estén listas).", "パーティーのまえに、のみものをかっておきます"),
            ("使ったら、元の所に戻しておいてください。", "3. Después de usarlo, por favor devuélvelo (déjalo) en su lugar original.", "つかったら、もとのところにもどしておいてください"),
            ("窓を開けておいてください。", "4. Por favor, deja la ventana abierta (así como está).", "まどをあけておいてください"),
            ("明日までに、この資料を読んでおいてください。", "5. Por favor, déjate leído este documento para mañana.", "あしたまでに、このしりょうをよんでおいてください"),
            ("お皿を洗っておきます。", "6. Lavaré (dejaré lavados) los platos.", "おさらをあらっておきます"),
            ("切符を買っておきました。", "7. Compré el billete (para tenerlo preparado).", "きっぷをかっておきました"),
            ("そのままにしておいてください。", "8. Por favor, déjalo tal como está.", "そのままにしておいてください"),
            ("会議の前に、椅子を並べておきます。", "9. Antes de la reunión, alinearé las sillas.", "かいぎのまえに、いすをならべておきます"),
            ("宿題をやっておきます。", "10. Haré los deberes (para tenerlos listos).", "しゅくだいをやっておきます")
        ],
        "exercises": [
            {"q": "¿Qué significa V(te) おきます?", "options": [{"text": "Hacer algo con lamentación.", "correct": False}, {"text": "Hacer algo como preparación para el futuro o dejarlo como está.", "correct": True}, {"text": "Hacer algo completamente.", "correct": False}]},
            {"q": "'Antes del viaje, DEJO RESERVADO el hotel':", "options": [{"text": "ホテルを予約しておきます。", "correct": True}, {"text": "ホテルを予約してしまいます。", "correct": False}, {"text": "ホテルを予約してあります。", "correct": False}]},
            {"q": "'Voy a DEJAR COMPRADAS las bebidas' (Kau):", "options": [{"text": "買っておきます (Katte okimasu)", "correct": True}, {"text": "買ってしまいます (Katte shimaimasu)", "correct": False}, {"text": "買ってあります (Katte arimasu)", "correct": False}]},
            {"q": "¿Qué significa 'そのままにしておいてください'?", "options": [{"text": "Por favor, tíralo.", "correct": False}, {"text": "Por favor, déjalo tal como está.", "correct": True}, {"text": "Por favor, prepáralo.", "correct": False}]},
            {"q": "¿Cuál es la forma coloquial (hablada) de '~ておく' (te oku)?", "options": [{"text": "~とく (toku)", "correct": True}, {"text": "~ちゃう (chau)", "correct": False}, {"text": "~どく (doku - es para de oku)", "correct": False}]},
            {"q": "'Lo voy a dejar hecho' (Suru -> shite):", "options": [{"text": "しとく (Shitoku - forma coloquial)", "correct": True}, {"text": "しちゃう (Shichau - lamento)", "correct": False}, {"text": "しなきゃ (Shinakya - obligación)", "correct": False}]},
            {"q": "Persona A: '¿Cierro la ventana?'. Persona B: 'No, hace calor, así que ___'.", "options": [{"text": "開けておいてください (Déjala abierta)", "correct": True}, {"text": "開けてしまってください", "correct": False}, {"text": "開けてください", "correct": False}]},
            {"q": "'Voy a estudiar (dejar estudiado) para el examen de mañana':", "options": [{"text": "勉強しておきます。", "correct": True}, {"text": "勉強してしまいます。", "correct": False}, {"text": "勉強してあります。", "correct": False}]},
            {"q": "'Voy a lavar los platos (para que estén limpios luego)' (Arau):", "options": [{"text": "洗っておきます", "correct": True}, {"text": "洗ってしまいます", "correct": False}, {"text": "洗っています", "correct": False}]},
            {"q": "¿Cuál es la diferencia entre ておきます (te okimasu) y てあります (te arimasu)?", "options": [{"text": "Ambas son idénticas.", "correct": False}, {"text": "Te okimasu enfatiza la acción de preparar. Te arimasu describe el ESTADO resultante.", "correct": True}, {"text": "Te okimasu es pasado, Te arimasu es futuro.", "correct": False}]}
        ]
    }
}

def generate():
    base_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\lessons"
    
    for i in range(1, 6):
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
