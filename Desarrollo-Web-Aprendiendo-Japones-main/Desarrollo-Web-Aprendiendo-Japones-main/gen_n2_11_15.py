import os
import subprocess

data = [
    {
        "id": "jlpt-n2-11",
        "title": "Examen para el JLPT2 - Lección 11",
        "header_title": "JLPT N2 - 準備",
        "desc": "Tema: ~ざるを得ない / ~やむを得ない (No tener más remedio que)",
        "grammar_points": [
            "<strong>～ざるを得ない (zaru o enai):</strong> Significa 'No tener más remedio que...'. Se usa cuando uno no quiere hacer algo, pero por las circunstancias es la única opción. (Se conecta a la forma Nai, quitando 'nai': 行かない -> 行かざるを得ない. *Excepción: する -> せざるを得ない).",
            "<strong>～やむを得ない (yamu o enai):</strong> Significa 'Inevitable' o 'Fuera de nuestro control'. Se usa como adjetivo para describir situaciones en las que no hay otra alternativa."
        ],
        "examples": [
            ("ja-JP-NanamiNeural", "台風が来ているので、旅行は中止せざるを得ない。", "Como viene un tifón, no tenemos más remedio que cancelar el viaje."),
            ("ja-JP-KeitaNeural", "会社が倒産したので、新しい仕事を探さざるを得ない。", "Como la empresa quebró, no tengo más remedio que buscar un nuevo trabajo."),
            ("ja-JP-NanamiNeural", "誰も手伝ってくれないから、一人でやらざるを得ない。", "Como nadie me ayuda, no me queda más remedio que hacerlo solo."),
            ("ja-JP-KeitaNeural", "こんなに証拠があるなら、彼の嘘を認めざるを得ない。", "Si hay tantas pruebas, no hay más remedio que admitir sus mentiras."),
            ("ja-JP-NanamiNeural", "終電に乗り遅れたので、タクシーで帰らざるを得なかった。", "Como perdí el último tren, no tuve más remedio que regresar en taxi."),
            ("ja-JP-KeitaNeural", "やむを得ない理由で、明日の会議は欠席します。", "Por motivos inevitables, me ausentaré a la reunión de mañana."),
            ("ja-JP-NanamiNeural", "手術をするのは、やむを得ない決断だった。", "Hacer la cirugía fue una decisión inevitable (no había otra opción)."),
            ("ja-JP-KeitaNeural", "予算が足りないため、計画の変更はやむを得ない。", "Debido a la falta de presupuesto, el cambio de planes es inevitable."),
            ("ja-JP-NanamiNeural", "渋滞で遅刻したのは、やむを得ない事情だ。", "Llegar tarde por el tráfico es una circunstancia fuera de mi control."),
            ("ja-JP-KeitaNeural", "怪我が治らないなら、引退もやむを得ないだろう。", "Si la lesión no se cura, el retiro también será inevitable.")
        ],
        "dialogue": [
            ("ja-JP-KeitaNeural", "明日の社内イベントですが、どうやら大雨になるらしいです。", "Sobre el evento de la empresa de mañana, parece que va a llover a cántaros."),
            ("ja-JP-NanamiNeural", "そうですか。ずっと準備してきたのに、残念ですね。", "Ya veo. Lo habíamos preparado por tanto tiempo, es una pena."),
            ("ja-JP-KeitaNeural", "ええ。安全を考えると、延期せざるを得ないでしょうね。", "Sí. Pensando en la seguridad, no tendremos más remedio que posponerlo, ¿verdad?"),
            ("ja-JP-NanamiNeural", "屋外でのイベントですから、やむを得ないですね。社長にも報告しましょう。", "Como es un evento al aire libre, es inevitable. Informémosle también al presidente."),
            ("ja-JP-KeitaNeural", "社長も、参加者の安全が第一だと言っていましたし、納得せざるを得ないはずです。", "El presidente también decía que la seguridad de los participantes es lo primero, así que no le quedará más remedio que aceptarlo."),
            ("ja-JP-NanamiNeural", "そうですね。参加者全員には、私からメールで連絡しておきます。", "Así es. Yo me encargaré de contactar a todos los participantes por correo."),
            ("ja-JP-KeitaNeural", "助かります。今回は本当にやむを得ない事情だから、みんなも分かってくれると思いますよ。", "Me salvas. Esta vez es una situación realmente inevitable, así que creo que todos lo entenderán.")
        ],
        "exercises": [
            {
                "q": "雨がひどいので、試合は中止（　　　）。",
                "options": [("せざるを得ない", True), ("しざるを得ない", False), ("だらけだ", False)]
            },
            {
                "q": "「～ざるを得ない」 se usa cuando:",
                "options": [("Se quiere hacer algo con muchas ganas", False), ("No hay otra opción, aunque uno no quiera", True), ("Es una regla estricta de la sociedad", False)]
            },
            {
                "q": "親が病気になったので、進学を諦めるのは（　　　）ことだ。",
                "options": [("やむを得ない", True), ("気味の", False), ("を通じての", False)]
            },
            {
                "q": "誰も行かないなら、私が（　　　）。",
                "options": [("行かざるを得ない", True), ("行きざるを得ない", False), ("向けだ", False)]
            },
            {
                "q": "「する」 se transforma en:",
                "options": [("せざるを得ない", True), ("しざるを得ない", False), ("すざるを得ない", False)]
            }
        ]
    },
    {
        "id": "jlpt-n2-12",
        "title": "Examen para el JLPT2 - Lección 12",
        "header_title": "JLPT N2 - 準備",
        "desc": "Tema: ~ことだ / ~ことか (Deberías / ¡Qué...!)",
        "grammar_points": [
            "<strong>～ことだ (koto da):</strong> Significa 'Deberías...' o 'Lo mejor es...'. Se usa para dar un consejo fuerte o una sugerencia directa sobre lo que uno considera que es la mejor opción.",
            "<strong>～ことか (koto ka):</strong> Significa '¡Qué...!' o '¡Cuánto...!'. Se usa al final de la oración para expresar un sentimiento o emoción muy profunda (a menudo con palabras interrogativas como どんなに, どれほど, 何度)."
        ],
        "examples": [
            ("ja-JP-NanamiNeural", "日本語が上手になりたいなら、毎日話すことだ。", "Si quieres mejorar tu japonés, (lo que deberías hacer) es hablarlo todos los días."),
            ("ja-JP-KeitaNeural", "風邪を引いた時は、温かくして寝ることです。", "Cuando pescas un resfriado, lo mejor es abrigarse y dormir."),
            ("ja-JP-NanamiNeural", "合格したいなら、ゲームをやめて勉強することだ。", "Si quieres aprobar, deberías dejar de jugar videojuegos y estudiar."),
            ("ja-JP-KeitaNeural", "無理をしないで、たまには休むことだよ。", "No te sobreesfuerces, de vez en cuando lo que deberías hacer es descansar."),
            ("ja-JP-NanamiNeural", "わからないことがあったら、すぐに先生に聞くことだ。", "Si hay algo que no entiendes, deberías preguntarle al profesor de inmediato."),
            ("ja-JP-KeitaNeural", "大学に合格した時、どんなに嬉しかったことか。", "Cuando aprobé el examen de la universidad, ¡qué feliz me sentí!"),
            ("ja-JP-NanamiNeural", "子供が生まれた日は、どれほど感動したことか。", "El día que nació mi hijo, ¡cuánto me emocioné!"),
            ("ja-JP-KeitaNeural", "彼を説得するために、何度彼に電話したことか。", "Para persuadirlo, ¡cuántas veces lo habré llamado por teléfono!"),
            ("ja-JP-NanamiNeural", "この景色を直接見ることができたら、どんなに素晴らしいことか。", "Si pudiera ver este paisaje directamente, ¡qué maravilloso sería!"),
            ("ja-JP-KeitaNeural", "母の料理を久しぶりに食べて、どれほど美味しかったことか。", "Comiendo la comida de mi madre después de tanto tiempo, ¡qué deliciosa estuvo!")
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "先輩、日本語の試験になかなか受からなくて、落ち込んでいます。", "Senpai, no logro aprobar el examen de japonés y estoy deprimida."),
            ("ja-JP-KeitaNeural", "うーん、試験に落ちると辛いよね。でも、諦めないで続けることだよ。", "Mmm, reprobar el examen es duro. Pero lo que deberías hacer es no rendirte y continuar."),
            ("ja-JP-NanamiNeural", "はい。でも、どれほど勉強したことか。もう疲れちゃいました。", "Sí. Pero, ¡cuánto he estudiado! Ya me he cansado."),
            ("ja-JP-KeitaNeural", "わかるよ。僕も昔、N1に受かるまでに何度不合格になったことか。", "Te entiendo. En el pasado, antes de aprobar el N1, ¡cuántas veces habré reprobado yo también!"),
            ("ja-JP-NanamiNeural", "先輩もそんな時期があったんですね。", "Usted también tuvo una época así, ¿verdad?"),
            ("ja-JP-KeitaNeural", "うん。合格した時、どんなに嬉しかったことか今でも覚えているよ。君も、まずは自分の弱点を復習することだ。", "Sí. Todavía recuerdo ¡qué feliz me sentí cuando aprobé! Tú también, por ahora deberías repasar tus puntos débiles."),
            ("ja-JP-NanamiNeural", "ありがとうございます。もう一度、頑張ってみます！", "Muchas gracias. ¡Me esforzaré una vez más!")
        ],
        "exercises": [
            {
                "q": "疲れた時は、無理をしないで早く寝る（　　　）。",
                "options": [("ことだ", True), ("ことか", False), ("だらけだ", False)]
            },
            {
                "q": "「～ことか」 se usa para expresar:",
                "options": [("Un consejo fuerte", False), ("Una emoción muy profunda", True), ("Una obligación inevitable", False)]
            },
            {
                "q": "彼が帰ってくるのを、どんなに待っていた（　　　）。",
                "options": [("ことか", True), ("ことだ", False), ("向けだ", False)]
            },
            {
                "q": "痩せたいなら、甘いものを食べない（　　　）。",
                "options": [("ことだ", True), ("ことか", False), ("気味だ", False)]
            },
            {
                "q": "どれほど涙を流した（　　　）。",
                "options": [("ことか", True), ("ことだ", False), ("を通して", False)]
            }
        ]
    },
    {
        "id": "jlpt-n2-13",
        "title": "Examen para el JLPT2 - Lección 13",
        "header_title": "JLPT N2 - 準備",
        "desc": "Tema: ~にすぎない / ~にほかならない (No es más que / No es otra cosa que)",
        "grammar_points": [
            "<strong>～にすぎない (ni suginai):</strong> Significa 'No es más que...', 'Es solamente...' o 'Nada más que'. Se usa para minimizar la importancia o el nivel de algo, indicando que no es gran cosa.",
            "<strong>～にほかならない (ni hokanaranai):</strong> Significa 'No es otra cosa que...' o 'Es exactamente... y nada más'. Se usa para enfatizar fuertemente la causa principal o la esencia de algo."
        ],
        "examples": [
            ("ja-JP-NanamiNeural", "私はただの学生にすぎないから、そんな難しい問題は解けません。", "Como no soy más que un simple estudiante, no puedo resolver un problema tan difícil."),
            ("ja-JP-KeitaNeural", "あの人は少し有名なだけで、プロの歌手というわけではない。アマチュアにすぎない。", "Esa persona solo es un poco famosa, no significa que sea cantante profesional. No es más que un aficionado."),
            ("ja-JP-NanamiNeural", "これはただの噂にすぎないので、信じない方がいいですよ。", "Como esto no es más que un simple rumor, es mejor que no lo creas."),
            ("ja-JP-KeitaNeural", "彼が言ったことは、言い訳にすぎない。", "Lo que él dijo no es más que una excusa."),
            ("ja-JP-NanamiNeural", "収入は少し増えたが、月に数千円にすぎない。", "Los ingresos aumentaron un poco, pero no es más que unos pocos miles de yenes al mes."),
            ("ja-JP-KeitaNeural", "彼が成功したのは、日々の努力の結果にほかならない。", "El que él haya tenido éxito, no es otra cosa que el resultado de su esfuerzo diario."),
            ("ja-JP-NanamiNeural", "この計画が失敗したのは、準備不足にほかならない。", "El que este plan haya fracasado, no es otra cosa que la falta de preparación."),
            ("ja-JP-KeitaNeural", "親が子供を厳しく叱るのは、子供への愛情にほかならない。", "El que los padres regañen estrictamente a los hijos, no es otra cosa que amor hacia ellos."),
            ("ja-JP-NanamiNeural", "我々が勝てたのは、チームワークの力にほかならない。", "El que hayamos podido ganar, no es otra cosa que el poder del trabajo en equipo."),
            ("ja-JP-KeitaNeural", "彼が怒っているのは、君を心配しているからにほかならない。", "El que él esté enojado, no es otra cosa que porque se preocupa por ti.")
        ],
        "dialogue": [
            ("ja-JP-KeitaNeural", "今回の新商品の売れ行きはどうですか？", "¿Cómo van las ventas del nuevo producto esta vez?"),
            ("ja-JP-NanamiNeural", "少し売れていますが、目標の10%にすぎません。まだまだですね。", "Se está vendiendo un poco, pero no es más que el 10% del objetivo. Aún falta mucho."),
            ("ja-JP-KeitaNeural", "そうですか。売れない理由は、宣伝不足にほかならないと思います。", "Ya veo. Creo que la razón por la que no se vende no es otra cosa que la falta de publicidad."),
            ("ja-JP-NanamiNeural", "私もそう思います。単にパッケージを変えたにすぎないので、消費者に魅力が伝わっていないのでしょう。", "Yo también pienso igual. Como no hicimos más que simplemente cambiar el empaque, el atractivo no le está llegando a los consumidores, supongo."),
            ("ja-JP-KeitaNeural", "ええ。ライバル会社に勝つためには、根本的な改革が必要にほかならないですね。", "Sí. Para ganar a la compañía rival, no es otra cosa que una reforma fundamental lo que necesitamos."),
            ("ja-JP-NanamiNeural", "おっしゃる通りです。次の会議で、新しい戦略を提案してみます。", "Como usted dice. En la próxima reunión, intentaré proponer una nueva estrategia.")
        ],
        "exercises": [
            {
                "q": "彼はただのアルバイト（　　　）ので、責任ある仕事は任せられない。",
                "options": [("にすぎない", True), ("にほかならない", False), ("ことだ", False)]
            },
            {
                "q": "「～にほかならない」 se usa para:",
                "options": [("Minimizar la importancia de algo", False), ("Enfatizar la razón principal o esencia de algo", True), ("Dar un consejo directo", False)]
            },
            {
                "q": "彼がいつも一番早く出社するのは、仕事への熱意（　　　）。",
                "options": [("にほかならない", True), ("にすぎない", False), ("ざるを得ない", False)]
            },
            {
                "q": "熱が少し下がったが、まだ３８度もある。少し良くなった（　　　）。",
                "options": [("にすぎない", True), ("にほかならない", False), ("ことか", False)]
            },
            {
                "q": "戦争がもたらすものは、悲劇（　　　）。",
                "options": [("にほかならない", True), ("にすぎない", False), ("向けだ", False)]
            }
        ]
    },
    {
        "id": "jlpt-n2-14",
        "title": "Examen para el JLPT2 - Lección 14",
        "header_title": "JLPT N2 - 準備",
        "desc": "Tema: ~て以来 / ~てからでないと (Desde que / A menos que)",
        "grammar_points": [
            "<strong>～て以来 (te irai):</strong> Significa 'Desde que...'. Enfatiza que un estado ha continuado o cambiado de forma permanente desde que ocurrió ese evento. (A diferencia de ~てから, se usa para periodos más largos o cambios significativos).",
            "<strong>～てからでないと (te kara denai to):</strong> Significa 'A menos que...' o 'Hasta que no...'. Se usa para indicar que la acción B no puede suceder hasta que no se complete primero la acción A. Suele ir seguido de una negación."
        ],
        "examples": [
            ("ja-JP-NanamiNeural", "日本に来て以来、毎日納豆を食べています。", "Desde que vine a Japón, estoy comiendo natto todos los días."),
            ("ja-JP-KeitaNeural", "大学を卒業して以来、彼とは一度も会っていない。", "Desde que me gradué de la universidad, no me he encontrado con él ni una sola vez."),
            ("ja-JP-NanamiNeural", "あの映画を見て以来、彼女のファンになりました。", "Desde que vi esa película, me convertí en fan de ella."),
            ("ja-JP-KeitaNeural", "引っ越しをして以来、新しい趣味を始めました。", "Desde que me mudé, empecé un nuevo pasatiempo."),
            ("ja-JP-NanamiNeural", "子供が生まれて以来、生活が大きく変わった。", "Desde que nació mi hijo, mi vida cambió enormemente."),
            ("ja-JP-KeitaNeural", "上司に相談してからでないと、この件は決定できません。", "A menos que lo consulte con mi jefe, no puedo decidir sobre este asunto."),
            ("ja-JP-NanamiNeural", "手を洗ってからでないと、ご飯を食べてはいけません。", "Hasta que no te laves las manos, no debes comer."),
            ("ja-JP-KeitaNeural", "契約書をよく読んでからでないと、サインしない方がいいですよ。", "A menos que leas bien el contrato, es mejor que no lo firmes."),
            ("ja-JP-NanamiNeural", "試験に合格してからでないと、次のレベルに進めません。", "Hasta que no apruebes el examen, no puedes avanzar al siguiente nivel."),
            ("ja-JP-KeitaNeural", "お金を貯めてからでないと、車は買えない。", "A menos que ahorre dinero, no podré comprar un auto.")
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "木村さん、最近ゴルフを始めたそうですね。", "Señor Kimura, escuché que últimamente empezó a jugar golf."),
            ("ja-JP-KeitaNeural", "ええ。先月、社長に誘われて以来、すっかりハマってしまって。", "Sí. Desde que el presidente me invitó el mes pasado, me enganché por completo."),
            ("ja-JP-NanamiNeural", "そうなんですか。私も始めてみたいんですけど、道具が高いですよね。", "¿De verdad? Yo también quisiera intentarlo, pero el equipo es caro, ¿no?"),
            ("ja-JP-KeitaNeural", "確かに。でも、まずは練習場に行って、クラブを借りて打ってみてからでないと、自分に向いているか分からないですよ。", "Ciertamente. Pero, primero, a menos que vayas a un campo de práctica, rentes un palo y pruebes golpear, no sabrás si es adecuado para ti."),
            ("ja-JP-NanamiNeural", "なるほど。じゃあ、一度試しに打ってからでないと、買うのはやめておきます。", "Ya veo. Entonces, hasta que no pruebe golpear una vez, dejaré de lado lo de comprarlo."),
            ("ja-JP-KeitaNeural", "それがいいですよ。ゴルフを始めて以来、週末が楽しくなりましたから、ぜひ一緒にやりましょう。", "Eso es lo mejor. Desde que empecé el golf, mis fines de semana se han vuelto divertidos, así que definitivamente hagámoslo juntos.")
        ],
        "exercises": [
            {
                "q": "結婚し（　　　）、彼はお酒を飲まなくなった。",
                "options": [("て以来", True), ("てからでないと", False), ("ざるを得ない", False)]
            },
            {
                "q": "「～てからでないと」 suele ir seguido de:",
                "options": [("Una expresión positiva o invitación", False), ("Una negación o algo imposible de hacer", True), ("Una emoción extrema", False)]
            },
            {
                "q": "親の許可をもらっ（　　　）、この旅行には行けません。",
                "options": [("てからでないと", True), ("て以来", False), ("にすぎない", False)]
            },
            {
                "q": "新しい社長になっ（　　　）、会社の雰囲気が良くなった。",
                "options": [("て以来", True), ("てからでないと", False), ("にほかならない", False)]
            },
            {
                "q": "実物を見（　　　）、買うかどうか決められない。",
                "options": [("てからでないと", True), ("て以来", False), ("ことか", False)]
            }
        ]
    },
    {
        "id": "jlpt-n2-15",
        "title": "Examen para el JLPT2 - Lección 15",
        "header_title": "JLPT N2 - 準備",
        "desc": "Tema: ~のみならず / ~に限らず (No solo... sino / No limitado a...)",
        "grammar_points": [
            "<strong>～のみならず (nomi narazu):</strong> Significa 'No solo... sino también...'. Es una expresión formal y escrita de 'だけじゃなくて'. Se usa a menudo en discursos o noticias.",
            "<strong>～に限らず (ni kagirazu):</strong> Significa 'No limitado a... sino (también todo lo demás)'. Indica que algo no es exclusivo de un grupo pequeño, sino que aplica a un rango más amplio (ej. 'no solo los jóvenes, sino también los adultos')."
        ],
        "examples": [
            ("ja-JP-NanamiNeural", "彼は英語のみならず、フランス語も流暢に話せる。", "Él no solo habla inglés, sino que también puede hablar francés con fluidez."),
            ("ja-JP-KeitaNeural", "このアニメは日本のみならず、世界中で人気がある。", "Este anime es popular no solo en Japón, sino también en todo el mundo."),
            ("ja-JP-NanamiNeural", "その政策は経済のみならず、環境にも悪影響を与えた。", "Esa política tuvo un impacto negativo no solo en la economía, sino también en el medio ambiente."),
            ("ja-JP-KeitaNeural", "彼女は美貌のみならず、素晴らしい才能も持っている。", "Ella no solo tiene belleza, sino que también posee un talento maravilloso."),
            ("ja-JP-NanamiNeural", "学生のみならず、教師もこのルールを守るべきだ。", "No solo los estudiantes, sino también los profesores deben seguir esta regla."),
            ("ja-JP-KeitaNeural", "最近のアニメは子供に限らず、大人も楽しめる内容が多い。", "Los animes recientes, sin limitarse a los niños, tienen mucho contenido que los adultos también pueden disfrutar."),
            ("ja-JP-NanamiNeural", "休日に限らず、平日もこの店は混んでいる。", "No limitándose a los días festivos, esta tienda está llena también los días de semana."),
            ("ja-JP-KeitaNeural", "女性に限らず、男性もスキンケアをする時代になった。", "Se ha vuelto una era en la que, sin limitarse a las mujeres, los hombres también se hacen cuidado de la piel."),
            ("ja-JP-NanamiNeural", "夏に限らず、冬でもアイスクリームがよく売れる。", "No solo en verano, sino que en invierno también se vende bien el helado."),
            ("ja-JP-KeitaNeural", "国内に限らず、海外のニュースにも関心を持つべきだ。", "Deberíamos tener interés no solo limitados al ámbito nacional, sino también en las noticias internacionales.")
        ],
        "dialogue": [
            ("ja-JP-KeitaNeural", "最近のスマートフォンの進化はすごいですね。", "La evolución de los teléfonos inteligentes últimamente es increíble, ¿verdad?"),
            ("ja-JP-NanamiNeural", "ええ。通話やメールのみならず、今では健康管理までできるんですから。", "Sí. Porque no solo hacen llamadas y correos, sino que ahora hasta pueden gestionar la salud."),
            ("ja-JP-KeitaNeural", "そうですね。それに、若者に限らず、お年寄りも上手に使いこなしていますよ。", "Así es. Además, sin limitarse a los jóvenes, las personas mayores también los están usando hábilmente."),
            ("ja-JP-NanamiNeural", "私の祖母も、毎日スマホで動画を見ています。日本国内のみならず、海外の動画も見て楽しんでいるようです。", "Mi abuela también ve videos en su celular todos los días. Parece que disfruta viendo no solo videos dentro de Japón, sino también del extranjero."),
            ("ja-JP-KeitaNeural", "それは素晴らしいですね。テクノロジーの恩恵は、一部の人に限らず、全ての人に広がっているんですね。", "Eso es maravilloso. Los beneficios de la tecnología se están expandiendo a todas las personas, sin limitarse a una parte de ellas."),
            ("ja-JP-NanamiNeural", "まさにその通りですね。", "Exactamente como usted dice.")
        ],
        "exercises": [
            {
                "q": "このイベントは若者（　　　）、お年寄りも参加できます。",
                "options": [("に限らず", True), ("て以来", False), ("にすぎない", False)]
            },
            {
                "q": "「～のみならず」 es una versión más formal de:",
                "options": [("だけじゃなくて (no solo)", True), ("しか (solo / nada más que)", False), ("からでないと (a menos que)", False)]
            },
            {
                "q": "彼の行動は、自分（　　　）、周囲の人にも迷惑をかけた。",
                "options": [("のみならず", True), ("に限らず", False), ("ことだ", False)]
            },
            {
                "q": "休日は日曜日（　　　）、土曜日も休みだ。",
                "options": [("に限らず", True), ("のみならず", False), ("てからでないと", False)]
            },
            {
                "q": "環境問題は一国（　　　）、地球全体の問題である。",
                "options": [("のみならず", True), ("に限らず", False), ("やむを得ない", False)]
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

    # 3. Estructurar HTML con el estilo pastel
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

n2_menu_items = """                        <a href="lessons/jlpt-n2-11.html" target="main_frame" class="nav-link">
                            <span class="nav-num">11</span> ~ざるを得ない / ~やむを得ない (Inevitable)
                        </a>
                        <a href="lessons/jlpt-n2-12.html" target="main_frame" class="nav-link">
                            <span class="nav-num">12</span> ~ことだ / ~ことか (Consejo y Emoción)
                        </a>
                        <a href="lessons/jlpt-n2-13.html" target="main_frame" class="nav-link">
                            <span class="nav-num">13</span> ~にすぎない / ~にほかならない (No es más que)
                        </a>
                        <a href="lessons/jlpt-n2-14.html" target="main_frame" class="nav-link">
                            <span class="nav-num">14</span> ~て以来 / ~てからでないと (Desde que / A menos que)
                        </a>
                        <a href="lessons/jlpt-n2-15.html" target="main_frame" class="nav-link">
                            <span class="nav-num">15</span> ~のみならず / ~に限らず (No solo... sino)
                        </a>
                    </div>"""

target = '<a href="lessons/jlpt-n2-10.html" target="main_frame" class="nav-link">\n                            <span class="nav-num">10</span> ~かねる / ~かねない (Dificultad / Peligro)\n                        </a>\n                    </div>'

if target in index_html and "jlpt-n2-11" not in index_html:
    new_index = index_html.replace(target, target.replace('</div>', n2_menu_items))
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(new_index)
    print("Inyectado Lote 3 N2 en index.html")

print("Ejecutando furigana...")
subprocess.run("python add_furigana.py", shell=True)
print("COMPLETADO LOTE 3 N2")
