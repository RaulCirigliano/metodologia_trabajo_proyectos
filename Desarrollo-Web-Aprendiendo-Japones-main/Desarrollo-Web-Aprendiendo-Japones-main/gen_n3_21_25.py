import os
import subprocess

data = {
    21: {
        "title": "Cambios Progresivos (~に伴って / ~とともに / ~につれて)",
        "grammar": [
            "<strong>N/V(dic) + に伴って (Ni tomonatte):</strong> 'Acompañando a... / Junto con...'. Expresa que a medida que ocurre el cambio A, también ocurre el cambio B simultáneamente (Causal y formal). Ej. 人口が増えるに伴って、犯罪も増えた (A medida que aumenta la población, también aumentan los crímenes).",
            "<strong>N/V(dic) + とともに (To tomo ni):</strong> 'Junto con / Al mismo tiempo que...'. Similar a 'ni tomonatte' pero enfatiza que ambas cosas ocurren exactamente juntas. Ej. 家族とともに過ごす (Pasar el tiempo junto a la familia).",
            "<strong>N/V(dic) + につれて (Ni tsurete):</strong> 'A medida que...'. Expresa un cambio gradual en una dirección. Si A cambia poco a poco, B cambia poco a poco. Ej. 年をとるにつれて、物忘れがひどくなる (A medida que envejezco, los olvidos empeoran)."
        ],
        "examples": [
            ("経済の発展に伴って、環境問題が深刻になっている。", "1. Acompañando el desarrollo económico, los problemas ambientales se vuelven graves.", "けいざいのはってんにともなって、かんきょうもんだいがしんこくになっている"),
            ("携帯電話の普及に伴って、公衆電話が減った。", "2. Junto con la difusión de los teléfonos móviles, los teléfonos públicos disminuyeron.", "けいたいでんわのふきゅうにともなって、こうしゅうでんわがへった"),
            ("私は家族とともに、日本へ来ました。", "3. Yo vine a Japón junto con (en compañía de) mi familia.", "わたしはかぞくとともに、にほんへきました"),
            ("春が近づくとともに、少しずつ暖かくなってきた。", "4. Al mismo tiempo que se acerca la primavera, se ha vuelto cálido poco a poco.", "はるがちかづくとともに、すこしずつあたたかくなってきた"),
            ("町の発展につれて、緑が少なくなっていった。", "5. A medida que la ciudad se desarrolló, la vegetación fue disminuyendo.", "まちのはってんにつれて、みどりがすくなくなっていった"),
            ("日本語が上手になるにつれて、日本での生活が楽しくなった。", "6. A medida que mi japonés mejora, la vida en Japón se ha vuelto más divertida.", "にほんごがじょうずになるにつれて、にほんでのせいかつがたのしくなった"),
            ("台風の接近に伴い、列車の運行を取りやめます。", "7. (Formal) Acompañando la llegada del tifón, se suspende la circulación de trenes.", "たいふうのせっきんにともない、れっしゃのうんこうをとりやめます"),
            ("年をとるとともに、体力が落ちるのを感じる。", "8. Al mismo tiempo que envejezco, siento que mi fuerza física disminuye.", "としをとるとともに、たいりょくがおちるのをかんじる"),
            ("山を登るにつれて、気温が下がってきた。", "9. A medida que subo la montaña, la temperatura ha bajado.", "やまをのぼるにつれて、きおんがさがってきた"),
            ("卒業とともに、彼らは別々の道を歩き始めた。", "10. Junto con la graduación, ellos comenzaron a caminar por caminos separados.", "そつぎょうとともに、かれらはべつべつのみちをあるきはじめた")
        ],
        "exercises": [
            {"q": "¿Qué expresión enfatiza un 'cambio gradual' (poco a poco)? (Ej. A medida que subo la montaña, hace más frío).", "options": [{"text": "～につれて", "correct": True}, {"text": "～とともに", "correct": False}, {"text": "～抜きで", "correct": False}]},
            {"q": "¿Qué expresión significa literalmente 'Junto con' y se puede usar tanto para cambios simultáneos como para personas (Ej. Vivir con la familia)?", "options": [{"text": "～とともに", "correct": True}, {"text": "～に伴って", "correct": False}, {"text": "～につれて", "correct": False}]},
            {"q": "¿Qué expresión es muy formal, se usa en noticias y significa 'Acompañando al cambio A, ocurre el cambio B'?", "options": [{"text": "～に伴って (ni tomonatte)", "correct": True}, {"text": "～につれて (ni tsurete)", "correct": False}, {"text": "～にかけて (ni kakete)", "correct": False}]},
            {"q": "'A medida que envejezco, duermo menos' (Toshi o toru):", "options": [{"text": "年をとるにつれて", "correct": True}, {"text": "年をとるに伴って", "correct": False}, {"text": "年をとるはもちろん", "correct": False}]},
            {"q": "'Junto con mis amigos, viajé a Kioto' (Tomodachi):", "options": [{"text": "友達とともに", "correct": True}, {"text": "友達につれて", "correct": False}, {"text": "友達に伴って", "correct": False}]},
            {"q": "'Acompañando la internacionalización, aumentan los extranjeros' (Kokusaika):", "options": [{"text": "国際化に伴って", "correct": True}, {"text": "国際化につれて", "correct": False}, {"text": "国際化とともに", "correct": False}]},
            {"q": "'A medida que avanza la tecnología, la vida es más fácil' (Susumu):", "options": [{"text": "技術が進むにつれて", "correct": True}, {"text": "技術が進むに伴って", "correct": False}, {"text": "技術が進むとともに", "correct": False}]},
            {"q": "La versión aún más formal de に伴って (usada en escritos y anuncios):", "options": [{"text": "に伴い (ni tomonai)", "correct": True}, {"text": "に伴えば (ni tomoneba)", "correct": False}, {"text": "に伴うから (ni tomonau kara)", "correct": False}]},
            {"q": "'Al mismo tiempo que sale el sol, me despierto' (Hi ga noboru):", "options": [{"text": "日が昇るとともに", "correct": True}, {"text": "日が昇るにつれて", "correct": False}, {"text": "日が昇るに伴って", "correct": False}]},
            {"q": "¿Qué tipo de verbos suelen acompañar a '~につれて'? (A medida que...)", "options": [{"text": "Verbos de cambio gradual (aumentar, disminuir, crecer, mejorar)", "correct": True}, {"text": "Verbos de estado (estar, tener)", "correct": False}, {"text": "Verbos de movimiento rápido (correr, saltar)", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "最近、この町もすっかり変わりましたね。", "Últimamente, esta ciudad ha cambiado por completo, ¿verdad?"),
            ("ja-JP-KeitaNeural", "そうですね。新しい駅ができたことに伴って、大きなデパートやマンションがたくさん建ちました。", "Sí. Acompañando la construcción de la nueva estación, se han construido muchos grandes almacenes y apartamentos."),
            ("ja-JP-NanamiNeural", "ええ。でも、町が便利になるにつれて、昔からある小さなお店が減ってしまって寂しいです。", "Sí. Pero a medida que la ciudad se vuelve más conveniente, las tiendas pequeñas de siempre han disminuido y me da tristeza."),
            ("ja-JP-KeitaNeural", "確かに。時代の変化とともに、消えていくものがあるのは仕方がないのかもしれませんね。", "Es cierto. Al mismo tiempo que cambia la era (la época), quizás no se pueda evitar que haya cosas que desaparezcan."),
            ("ja-JP-NanamiNeural", "そうですね。でも、この美しい自然だけは、未来の子供たちとともに守っていきたいです。", "Así es. Pero al menos esta hermosa naturaleza, quiero protegerla junto con los niños del futuro."),
            ("ja-JP-KeitaNeural", "同感です。人口が増加するに伴って、自然環境の保護はさらに重要になりますからね。", "Opino lo mismo. Porque acompañando el aumento de la población, la protección del medio ambiente se vuelve aún más importante.")
        ]
    },
    22: {
        "title": "Contrastes Fuertes (~反面 / ~かわりに / ~一方)",
        "grammar": [
            "<strong>~反面 (Hanmen):</strong> 'Por otro lado / Por el contrario'. Expresa que una misma cosa tiene dos caras opuestas (una buena y una mala). Ej. 便利である反面、危険でもある (Es conveniente, pero por otro lado también es peligroso).",
            "<strong>~かわりに (Kawari ni):</strong> 'En lugar de... / A cambio de...'. Reemplazar una acción por otra, o una compensación. Ej. 日曜日に働くかわりに、月曜日に休む (En lugar de/A cambio de trabajar el domingo, descanso el lunes).",
            "<strong>~一方(で) (Ippou de):</strong> 'Mientras que... / Por una parte... y por otra'. Contraste general entre dos cosas diferentes o dos aspectos, más objetivo que 'hanmen'. Ej. 兄は静かな一方で、弟はうるさい (Mientras que el hermano mayor es tranquilo, el menor es ruidoso)."
        ],
        "examples": [
            ("都会の生活は便利な反面、ストレスも多い。", "1. La vida en la ciudad es conveniente, pero por otro lado tiene mucho estrés.", "とかいのせいかつはべんりなはんめん、ストレスもおおい"),
            ("彼は優しい反面、怒るととても怖い。", "2. Él es amable, pero por otro lado, cuando se enoja es muy aterrador.", "かれはやさしいはんめん、おこるととてもこわい"),
            ("一人暮らしは自由な反面、寂しい時もある。", "3. Vivir solo es libre, pero por otro lado a veces es solitario.", "ひとりぐらしはじゆうなはんめん、さびしいときもある"),
            ("映画を見に行くかわりに、家でDVDを見よう。", "4. En lugar de ir a ver una película, veamos un DVD en casa.", "えいがをみにいくかわりに、いえでDVDをみよう"),
            ("私が料理をするかわりに、あなたは掃除をしてください。", "5. A cambio de que yo cocine, tú limpia por favor.", "わたしがりょうりをするかわりに、あなたはそうじをしてください"),
            ("手伝ってもらったかわりに、お昼ご飯をごちそうした。", "6. A cambio de que me ayudó, lo invité a almorzar.", "てつだってもらったかわりに、おひるごはんをごちそうした"),
            ("日本はアニメが人気な一方で、漫画もよく読まれている。", "7. En Japón, por un lado el anime es popular, y por otro el manga también es muy leído.", "にほんはアニメがにんきないっぽうで、まんがもよくよまれている"),
            ("私の仕事は夏は忙しい一方で、冬は暇だ。", "8. Mi trabajo, mientras que en verano es ocupado, en invierno es libre.", "わたしのしごとはなつはいそがしいいっぽうで、ふゆはひまだ"),
            ("母親は厳しい反面、父親はとても優しい。", "9. Mientras que la madre es estricta, el padre es muy amable (También se puede usar Ippou de).", "ははおやはきびしいはんめん、ちちおやはとてもやさしい"),
            ("車で通勤するかわりに、自転車で行くことにした。", "10. En lugar de ir a trabajar en coche, decidí ir en bicicleta.", "くるまでつうきんするかわりに、じてんしゃでいくことにした")
        ],
        "exercises": [
            {"q": "¿Qué expresión significa literalmente 'La cara opuesta' y se usa para decir 'Es bueno en esto, PERO malo en esto otro' (la misma persona o cosa)?", "options": [{"text": "～反面 (hanmen)", "correct": True}, {"text": "～かわりに (kawari ni)", "correct": False}, {"text": "～一方 (ippou)", "correct": False}]},
            {"q": "¿Qué expresión significa 'En lugar de / A cambio de' (compensación o reemplazo)?", "options": [{"text": "～かわりに (kawari ni)", "correct": True}, {"text": "～一方 (ippou)", "correct": False}, {"text": "～反面 (hanmen)", "correct": False}]},
            {"q": "¿Qué expresión se usa para contrastar dos cosas diferentes de forma neutra? (Ej. Mi padre es estricto, MIENTRAS QUE mi madre es suave).", "options": [{"text": "～一方(で) (ippou de)", "correct": True}, {"text": "～反面 (hanmen)", "correct": False}, {"text": "～かわりに (kawari ni)", "correct": False}]},
            {"q": "'Te enseñaré japonés, A CAMBIO DE que me enseñes inglés' (Oshieru):", "options": [{"text": "教えるかわりに", "correct": True}, {"text": "教える反面", "correct": False}, {"text": "教える一方で", "correct": False}]},
            {"q": "'Este ordenador es ligero, PERO POR OTRO LADO, se rompe fácilmente' (Karui):", "options": [{"text": "軽い反面", "correct": True}, {"text": "軽いかわりに", "correct": False}, {"text": "軽い一方で", "correct": False}]},
            {"q": "'En lugar de viajar al extranjero, viajé por mi país' (Kaigai ni iku...):", "options": [{"text": "行くかわりに", "correct": True}, {"text": "行く反面", "correct": False}, {"text": "行く一方で", "correct": False}]},
            {"q": "'El hermano mayor es deportista, MIENTRAS QUE el menor ama la lectura' (Ani wa...):", "options": [{"text": "スポーツが得意な一方で", "correct": True}, {"text": "スポーツが得意な反面", "correct": False}, {"text": "スポーツが得意なかわりに", "correct": False}]},
            {"q": "'Internet es muy útil, PERO POR OTRO LADO, la información falsa es un problema' (Benri na...):", "options": [{"text": "便利な反面", "correct": True}, {"text": "便利なかわりに", "correct": False}, {"text": "便利なにつれて", "correct": False}]},
            {"q": "Para usar un sustantivo con 'Kawari ni' (Ej. En lugar del presidente -> Shachou):", "options": [{"text": "社長のかわりに", "correct": True}, {"text": "社長なかわりに", "correct": False}, {"text": "社長かわりに", "correct": False}]},
            {"q": "¿Cuál es la principal diferencia entre 'Hanmen' y 'Ippou de'?", "options": [{"text": "Hanmen contrasta dos lados de una MISMA cosa. Ippou de puede contrastar dos cosas DISTINTAS.", "correct": True}, {"text": "Son exactamente iguales.", "correct": False}, {"text": "Hanmen es para cosas físicas y Ippou de para emociones.", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-KeitaNeural", "最近、テレワークが増えましたね。", "Últimamente, el teletrabajo ha aumentado, ¿verdad?"),
            ("ja-JP-NanamiNeural", "ええ。家で仕事ができるのは便利な反面、プライベートとの区別が難しくてストレスもたまります。", "Sí. Poder trabajar en casa es conveniente, pero por otro lado, la distinción con la vida privada es difícil y se acumula el estrés."),
            ("ja-JP-KeitaNeural", "わかります。通勤時間がない一方で、運動不足になりがちですよね。", "Lo entiendo. Mientras que no hay tiempo de viaje al trabajo, uno tiende a la falta de ejercicio."),
            ("ja-JP-NanamiNeural", "そうなんです。だから、通勤しないかわりに、毎日夕方にジョギングをすることにしたんですよ。", "Así es. Por eso, a cambio de no viajar al trabajo, he decidido salir a correr todas las tardes."),
            ("ja-JP-KeitaNeural", "それはいいですね。僕も、夜遅くまでゲームをするかわりに、早く寝て朝活を始めようかな。", "Eso está muy bien. Yo también, en lugar de jugar videojuegos hasta tarde en la noche, creo que empezaré a dormir temprano y hacer actividades matutinas."),
            ("ja-JP-NanamiNeural", "素晴らしい心がけですね！朝は空気がきれいな反面、少し寒いですから風邪には気をつけて。", "¡Excelente actitud! Por la mañana el aire es limpio, pero por otro lado hace un poco de frío, así que ten cuidado con los resfriados.")
        ]
    },
    23: {
        "title": "Relaciones Temporales Avanzadas (~最中に / ~うちに)",
        "grammar": [
            "<strong>Nの/V(て)いる + 最中に (Saichuu ni):</strong> 'Justo en medio de...'. Expresa que algo ocurre (a menudo una interrupción molesta) justo en el momento más álgido de una acción. Ej. シャワーを浴びている最中に、電話が鳴った (Justo en medio de la ducha, sonó el teléfono).",
            "<strong>V/Adj/N + うちに (Uchi ni):</strong> 'Mientras... / Antes de que...'. Aprovechar un estado temporal antes de que cambie, o algo que ocurre naturalmente durante ese tiempo. Ej. アイスが溶けないうちに食べる (Comer el helado antes de que se derrita / Mientras no se derrita).",
            "<strong>V(て)からでないと (Te kara de nai to):</strong> 'A menos que (pase X primero), no puedo hacer Y'. Condición absoluta. Ej. 親に相談してからでないと、決められない (A menos que lo consulte con mis padres, no puedo decidir)."
        ],
        "examples": [
            ("会議の最中に、携帯電話が鳴ってしまった。", "1. Justo en medio de la reunión, sonó el teléfono móvil.", "かいぎのさいちゅうに、けいたいでんわがなってしまった"),
            ("テストの最中に、お腹が痛くなった。", "2. Justo en medio del examen, me dolió el estómago.", "テストのさいちゅうに、おなかがいたくなった"),
            ("先生が説明している最中に、寝てはいけません。", "3. No debes dormir justo en el medio de la explicación del profesor.", "せんせいがせつめいしているさいちゅうに、ねてはいけません"),
            ("温かいうちに、スープを飲んでください。", "4. Por favor, toma la sopa MIENTRAS esté caliente (antes de que se enfríe).", "あたたかいうちに、スープをのんでください"),
            ("日本にいるうちに、富士山に登りたい。", "5. Mientras esté en Japón (antes de volver a mi país), quiero subir el monte Fuji.", "にほんにいるうちに、ふじさんにのぼりたい"),
            ("暗くならないうちに、家に帰りましょう。", "6. Volvamos a casa antes de que oscurezca (mientras no esté oscuro).", "くらくならないうちに、いえにかえりましょう"),
            ("テレビを見ているうちに、寝てしまった。", "7. Mientras veía la televisión (sin darme cuenta), me quedé dormido.", "テレビをみているうちに、ねてしまった"),
            ("上司に確認してからでないと、この契約にサインできません。", "8. A menos que lo confirme con el jefe primero, no puedo firmar este contrato.", "じょうしにかくにんしてからでないと、このけいやくにサインできません"),
            ("手を洗ってからでないと、ご飯を食べてはいけない。", "9. A menos que te laves las manos primero, no debes comer.", "てをあらってからでないと、ごはんをたべてはいけない"),
            ("若いうちに、たくさん勉強しておきなさい。", "10. Mientras seas joven, estudia mucho.", "わかいうちに、たくさんべんきょうしておきなさい")
        ],
        "exercises": [
            {"q": "¿Qué expresión significa 'Aprovechar la oportunidad MIENTRAS el estado actual continúe' (Ej. Mientras está caliente / Mientras estoy en Japón)?", "options": [{"text": "～うちに", "correct": True}, {"text": "～最中に", "correct": False}, {"text": "～てからでないと", "correct": False}]},
            {"q": "¿Qué expresión significa 'Justo en medio de...' e implica a menudo una interrupción molesta o inesperada?", "options": [{"text": "～最中に (saichuu ni)", "correct": True}, {"text": "～うちに (uchi ni)", "correct": False}, {"text": "～てからでないと", "correct": False}]},
            {"q": "¿Qué expresión significa 'A menos que hagas X primero, no puedes hacer Y'?", "options": [{"text": "～てからでないと", "correct": True}, {"text": "～うちに", "correct": False}, {"text": "～最中に", "correct": False}]},
            {"q": "'Justo en medio de la comida, llegó un visitante' (Shokuji):", "options": [{"text": "食事の最中に", "correct": True}, {"text": "食事のうちに", "correct": False}, {"text": "食事てからでないと", "correct": False}]},
            {"q": "'Quiero ver a mis abuelos MIENTRAS estén sanos' (Genki):", "options": [{"text": "元気なうちに", "correct": True}, {"text": "元気な最中に", "correct": False}, {"text": "元気な反面", "correct": False}]},
            {"q": "'A menos que consiga el dinero primero, no puedo comprar el coche' (Okane o atsumeru):", "options": [{"text": "お金を集めてからでないと", "correct": True}, {"text": "お金を集める最中に", "correct": False}, {"text": "お金を集めるうちに", "correct": False}]},
            {"q": "'Mientras esperaba el tren, me puse a leer un libro' (Matsu):", "options": [{"text": "電車を待っているうちに", "correct": True}, {"text": "電車を待っている最中に", "correct": False}, {"text": "電車を待つに伴って", "correct": False}]},
            {"q": "'Por favor, come el helado ANTES de que se derrita' (Tokesou ni naru -> Tokenai):", "options": [{"text": "溶けないうちに", "correct": True}, {"text": "溶けない最中に", "correct": False}, {"text": "溶けない限り", "correct": False}]},
            {"q": "A: '¿Podemos firmar el documento ya?' B: 'A menos que lo lea bien...' (Yomu -> Yonde):", "options": [{"text": "よく読んでからでないと、無理です", "correct": True}, {"text": "よく読むうちに、無理です", "correct": False}, {"text": "よく読む最中に、無理です", "correct": False}]},
            {"q": "'Me quedé dormido justo en el medio del discurso del director' (Kouchou no hanashi):", "options": [{"text": "校長の話の最中に", "correct": True}, {"text": "校長の話のうちに", "correct": False}, {"text": "校長の話に伴って", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-NanamiNeural", "山田さん、昨日の夜、電話してごめんなさい。出ませんでしたね。", "Yamada, siento haberte llamado anoche. No contestaste."),
            ("ja-JP-KeitaNeural", "あ、すみません。ちょうどお風呂に入っている最中に電話が鳴ったので、出られなかったんです。", "Ah, lo siento. Como el teléfono sonó justo en medio de que me estaba bañando, no pude contestar."),
            ("ja-JP-NanamiNeural", "そうだったんですね。大事な話じゃなかったので、大丈夫ですよ。", "Ah, era por eso. Como no era una charla importante, no pasa nada."),
            ("ja-JP-KeitaNeural", "それは良かった。あ、このケーキ、昨日買ってきたんです。クリームがとけないうちに、食べましょう！", "Me alegro. Ah, este pastel lo compré ayer. ¡Comámoslo mientras la crema no se derrita (antes de que)!"),
            ("ja-JP-NanamiNeural", "わあ、美味しそう！でも、手を洗ってからでないと、食べられませんよ。", "¡Guau, parece delicioso! Pero, a menos que nos lavemos las manos primero, no podemos comer."),
            ("ja-JP-KeitaNeural", "そうですね。感染症の予防は大切ですからね。", "Tienes razón. La prevención de infecciones es importante, eh."),
            ("ja-JP-NanamiNeural", "ええ、健康なうちに、しっかり対策をしておきましょう。", "Sí, mientras estemos sanos, tomemos medidas adecuadamente.")
        ]
    },
    24: {
        "title": "Condiciones y Extremos (~さえ / ~てしょうがない / ~を問わず)",
        "grammar": [
            "<strong>N + さえ:</strong> 'Incluso... / Hasta...'. Marca un caso extremo y obvio para sugerir que lo demás es aún más cierto. Equivalente a 'N も / N まで'. Ej. 子供さえ知っている (Incluso los niños lo saben).",
            "<strong>V(て) + しょうがない / 仕方がない:</strong> 'Es tan... que no se puede evitar / Inmensamente'. Igual que 'Te tamaranai'. Ej. 暇でしょうがない (Estoy tan aburrido que no tiene remedio).",
            "<strong>N + を問わず (o towazu):</strong> 'Sin importar / Independientemente de...'. Se usa para indicar que una condición no importa. Ej. 年齢を問わず (Sin importar la edad)."
        ],
        "examples": [
            ("ひらがなさえ書けないのに、漢字が書けるわけがない。", "1. Si ni siquiera puedo escribir hiragana, es imposible que pueda escribir kanji.", "ひらがなさえかけないのに、かんじがかけるわけがない"),
            ("この問題は簡単だ。小学生さえ解けるよ。", "2. Este problema es fácil. Incluso los niños de primaria pueden resolverlo.", "このもんだいはかんたんだ。しょうがくせいさえとけるよ"),
            ("忙しすぎて、寝る時間さえない。", "3. Estoy tan ocupado que ni siquiera tengo tiempo para dormir.", "いそがしすぎて、ねるじかんさえない"),
            ("今日は暑くて暑くて、しょうがない。", "4. Hoy hace tanto calor, muchísimo, no se puede hacer nada.", "きょうはあつくてあつくて、しょうがない"),
            ("昨日の夜から何も食べていないので、お腹が空いて仕方がない。", "5. Como no he comido nada desde anoche, tengo un hambre que no tiene remedio.", "きのうのよるからなにもたべていないので、おなかがすいてしかたがない"),
            ("彼女のことが心配でしようがない。", "6. Estoy tan preocupado por ella que no puedo evitarlo.", "かのじょのことがしんぱいでしようがない"),
            ("この仕事は、年齢や性別を問わず、誰でもできます。", "7. Este trabajo lo puede hacer cualquiera, sin importar la edad o el género.", "このしごとは、ねんれいやせいべつをとわず、だれでもできます"),
            ("このスポーツクラブは、昼夜を問わず利用できる。", "8. Este club deportivo se puede usar independientemente de si es de día o de noche (24 hrs).", "このスポーツクラブは、ちゅうやをとわずりようできる"),
            ("国籍を問わず、多くの留学生がこの大学で学んでいる。", "9. Sin importar la nacionalidad, muchos estudiantes extranjeros estudian en esta universidad.", "こくせきをとわず、おおくのりゅうがくせいがこのだいがくでまなんでいる"),
            ("水さえあれば、一週間は生きられる。", "10. Si al menos tengo agua, puedo sobrevivir una semana (Sae + ba).", "みずさえあれば、いっしゅうかんはいきられる")
        ],
        "exercises": [
            {"q": "¿Qué partícula enfatiza un caso extremo (Incluso / Ni siquiera)? (Ej. Ni siquiera tengo tiempo)", "options": [{"text": "～さえ", "correct": True}, {"text": "～を問わず", "correct": False}, {"text": "～抜きで", "correct": False}]},
            {"q": "¿Qué expresión significa 'Independientemente de / Sin importar...'? (Ej. Sin importar la edad)", "options": [{"text": "～を問わず", "correct": True}, {"text": "～しょうがない", "correct": False}, {"text": "～さえ", "correct": False}]},
            {"q": "¿Qué expresión significa 'No puedo evitar sentir esto / Es inmenso' (Similar a 'tamaranai')?", "options": [{"text": "～てしょうがない", "correct": True}, {"text": "～を問わず", "correct": False}, {"text": "～反面", "correct": False}]},
            {"q": "'Es tan delicioso que no puedo parar / que no tiene remedio' (Oishikute...):", "options": [{"text": "美味しくてしょうがない", "correct": True}, {"text": "美味しくて問わず", "correct": False}, {"text": "美味しくてさえ", "correct": False}]},
            {"q": "'INCLUSO el profesor no pudo resolver este problema' (Sensei):", "options": [{"text": "先生さえ解けなかった", "correct": True}, {"text": "先生を問わず解けなかった", "correct": False}, {"text": "先生しょうがない解けなかった", "correct": False}]},
            {"q": "'Este festival se disfruta SIN IMPORTAR si eres hombre o mujer' (Danjo):", "options": [{"text": "男女を問わず", "correct": True}, {"text": "男女さえ", "correct": False}, {"text": "男女抜きで", "correct": False}]},
            {"q": "Gramática especial: 'Con tal de que / Si AL MENOS (Sae + ba)'. 'Si al menos tengo dinero, soy feliz':", "options": [{"text": "お金さえあれば", "correct": True}, {"text": "お金を問わずあれば", "correct": False}, {"text": "お金しょうがない", "correct": False}]},
            {"q": "'No tengo ni siquiera un yen en la cartera' (Ichi-en):", "options": [{"text": "１円さえない", "correct": True}, {"text": "１円を問わずない", "correct": False}, {"text": "１円しかない", "correct": False}]},
            {"q": "'Me pica tanto por los mosquitos que no lo soporto' (Kayui):", "options": [{"text": "痒くて仕方がない", "correct": True}, {"text": "痒くてを問わず", "correct": False}, {"text": "痒くてさえ", "correct": False}]},
            {"q": "A: '¿Pueden participar extranjeros?' B: 'Sí, ___ nacionalidad' (Kokuseki).", "options": [{"text": "国籍を問わず参加できます", "correct": True}, {"text": "国籍さえ参加できます", "correct": False}, {"text": "国籍しょうがない参加できます", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-KeitaNeural", "ああ、今日は暇で暇で、しょうがないよ。", "Ah, hoy estoy tan aburrido, pero tan aburrido, que no tiene remedio."),
            ("ja-JP-NanamiNeural", "暇なら、私の引っ越しの手伝いをしてくれませんか。荷物が多すぎて、一人じゃ運べないんです。", "Si estás aburrido, ¿no me ayudarías con mi mudanza? Tengo tanto equipaje que no puedo llevarlo sola."),
            ("ja-JP-KeitaNeural", "引っ越し？いいよ。でも、僕、力がないから重いものは持てないよ。", "¿Mudanza? Vale. Pero como no tengo fuerza, no puedo llevar cosas pesadas."),
            ("ja-JP-NanamiNeural", "大丈夫です。この仕事は、年齢や性別、力を問わず誰でもできる簡単な作業ですから。", "No te preocupes. Porque este trabajo, independientemente de la edad, el sexo o la fuerza, es una tarea sencilla que cualquiera puede hacer."),
            ("ja-JP-KeitaNeural", "そうなの？それなら、僕さえいれば十分だね！", "¿Ah, sí? En ese caso, ¡si al menos estoy yo (y nadie más), es suficiente!"),
            ("ja-JP-NanamiNeural", "ええ、本当に助かります。終わったら、美味しい焼肉をごちそうしますよ。", "Sí, me salvas la vida realmente. Cuando terminemos, te invitaré a un delicioso Yakiniku."),
            ("ja-JP-KeitaNeural", "焼肉！？それを聞いただけで、お腹が空いて仕方がないよ。すぐに行くよ！", "¡¿Yakiniku?! Solo con escuchar eso, me da un hambre que no tiene remedio. ¡Voy enseguida!")
        ]
    },
    25: {
        "title": "Evaluación, Énfasis y Resumen del N3 (~にかけては / ~だらけ / ~っぽい)",
        "grammar": [
            "<strong>N + にかけては (Ni kakete wa):</strong> 'Cuando se trata de... / En lo que respecta a...'. Se usa para destacar la superioridad o habilidad de alguien en un campo específico. Ej. 歌にかけては、彼が一番だ (Cuando se trata de cantar, él es el mejor).",
            "<strong>N + だらけ (Darake):</strong> 'Lleno de... / Cubierto de...'. Se usa de forma despectiva o negativa para cosas indeseables (barro, sangre, errores). Ej. 泥だらけの靴 (Zapatos cubiertos de barro).",
            "<strong>N/Adj/V + っぽい (Ppoi) [Repaso de la lección 15]:</strong> 'Con tendencia a... / Parece...'. En esta lección lo repasamos junto con sus contrastes.",
            "<strong>~っこない (Kkonai):</strong> 'Absolutamente imposible que...'. Versión coloquial de 'wake ga nai'. Ej. わかりっこない (Es imposible que lo entienda)."
        ],
        "examples": [
            ("数学にかけては、クラスで右に出る者はいない。", "1. Cuando se trata de matemáticas, no hay nadie en la clase que lo supere.", "すうがくにかけては、クラスでみぎにでるものはいない"),
            ("サービスにかけては、このホテルが最高です。", "2. En lo que respecta al servicio, este hotel es el mejor.", "サービスにかけては、このホテルがさいこうです"),
            ("子供たちが泥だらけになって遊んでいる。", "3. Los niños están jugando y poniéndose cubiertos de barro.", "こどもたちがどろだらけになってあそんでいる"),
            ("彼のテストの答案は、間違いだらけだった。", "4. Su hoja de respuestas del examen estaba llena de errores.", "かれのテストのとうあんは、まちがいだらけだった"),
            ("こんな難しい本、私には読み終えられっこないよ。", "5. Un libro tan difícil, es imposible que yo lo termine de leer (Coloquial).", "こんなむずかしいほん、わたしにはよみおえられっこないよ"),
            ("あの人はいつも怒りっぽいから、話しにくい。", "6. Esa persona siempre tiende a enojarse (es enojona), así que es difícil hablarle.", "あのひとはいつもおこりっぽいから、はなしにくい"),
            ("部屋中、ほこりだらけで掃除が大変だ。", "7. Toda la habitación está cubierta de polvo y limpiarla es difícil.", "へやじゅう、ほこりだらけでそうじがたいへんだ"),
            ("ピアノを弾くことにかけては、誰にも負けない自信がある。", "8. Cuando se trata de tocar el piano, tengo confianza en que no pierdo ante nadie.", "ピアノをひくことにかけては、だれにもまけないじしんがある"),
            ("あんなひどいこと、彼が許してくれっこないよ。", "9. Algo tan terrible, es imposible que él te lo perdone.", "あんなひどいこと、かれがゆるしてくれっこないよ"),
            ("黒っぽい服を着ている人が泥棒です。", "10. La persona que lleva ropa de tono oscuro (que parece negra) es el ladrón.", "くろっぽいふくをきているひとがどろぼうです")
        ],
        "exercises": [
            {"q": "¿Qué expresión se usa para decir 'En este tema específico, esa persona es la mejor'?", "options": [{"text": "～にかけては", "correct": True}, {"text": "～だらけ", "correct": False}, {"text": "～っこない", "correct": False}]},
            {"q": "¿Qué sufijo se pega a un sustantivo para decir 'Lleno de / Cubierto de' (generalmente suciedad o errores)?", "options": [{"text": "～だらけ (Darake)", "correct": True}, {"text": "～っぽい (Ppoi)", "correct": False}, {"text": "～ばかり (Bakari)", "correct": False}]},
            {"q": "¿Cuál es la versión coloquial fuerte de 'わけがない' (Es totalmente imposible que)?", "options": [{"text": "～っこない (Kkonai)", "correct": True}, {"text": "～だらけ (Darake)", "correct": False}, {"text": "～にかけては (Ni kakete wa)", "correct": False}]},
            {"q": "'Cuando se trata de computadoras, pregúntale a Yamada' (Pasokon):", "options": [{"text": "パソコンにかけては", "correct": True}, {"text": "パソコンだらけ", "correct": False}, {"text": "パソコンを問わず", "correct": False}]},
            {"q": "'Esta habitación está LLENA DE BASURA' (Gomi):", "options": [{"text": "ゴミだらけだ", "correct": True}, {"text": "ゴミにかけてはだ", "correct": False}, {"text": "ゴミっこないだ", "correct": False}]},
            {"q": "'Es imposible que yo gane contra un profesional' (Katsu -> Kachi):", "options": [{"text": "プロに勝ちっこない", "correct": True}, {"text": "プロに勝ちだらけ", "correct": False}, {"text": "プロに勝ちにかけては", "correct": False}]},
            {"q": "Repaso: 'Tiende a olvidar las cosas' (Wasureru -> Wasure):", "options": [{"text": "忘れっぽい", "correct": True}, {"text": "忘れだらけ", "correct": False}, {"text": "忘れっこない", "correct": False}]},
            {"q": "'El niño volvió cubierto de sangre' (Chi):", "options": [{"text": "血だらけになって帰ってきた", "correct": True}, {"text": "血にかけては帰ってきた", "correct": False}, {"text": "血っぽく帰ってきた", "correct": False}]},
            {"q": "'Cuando se trata de la historia de Japón, no pierdo ante nadie' (Nihon no rekishi):", "options": [{"text": "日本の歴史にかけては", "correct": True}, {"text": "日本の歴史だらけ", "correct": False}, {"text": "日本の歴史っこない", "correct": False}]},
            {"q": "A: '¿Crees que el jefe se dará cuenta del error?' B: '¡Es imposible que no se dé cuenta!' (Kizuku -> Kizuki):", "options": [{"text": "気づかないわけがない / 気づかないっこない", "correct": True}, {"text": "気づくはずだ", "correct": False}, {"text": "気づくだらけだ", "correct": False}]}
        ],
        "dialogue": [
            ("ja-JP-KeitaNeural", "見てよ、この部屋。足の踏み場もないくらいゴミだらけだ。", "Mira esta habitación. Está tan cubierta de basura que no hay ni dónde pisar."),
            ("ja-JP-NanamiNeural", "本当ですね。山田君の部屋ですか？彼は片付けにかけては、世界で一番苦手な人ですよ。", "Es cierto. ¿Es la habitación de Yamada? Cuando se trata de limpiar, él es la persona más mala del mundo en eso."),
            ("ja-JP-KeitaNeural", "そうなんだよね。彼、いつも忘れっぽいし、プリントも間違いだらけだし。", "Así es. Él siempre tiende a olvidar las cosas, y sus fotocopias también están llenas de errores."),
            ("ja-JP-NanamiNeural", "でも、プログラミングにかけては天才的ですよね。この間のシステムも、彼が一人で作ったんですよ。", "Pero, en lo que respecta a la programación, es un genio, ¿verdad? El sistema de la otra vez, lo hizo él solo."),
            ("ja-JP-KeitaNeural", "うん。僕たち凡人には、あんな複雑なコード、理解できっこないよ。", "Sí. Para nosotros la gente común, un código tan complejo, es imposible que lo podamos entender."),
            ("ja-JP-NanamiNeural", "人にはそれぞれ長所と短所があるんですね。とりあえず、山田君が帰ってくる前に、このゴミだらけの部屋を少し片付けましょうか。", "Cada persona tiene sus puntos fuertes y débiles, eh. Por el momento, antes de que Yamada regrese, ¿limpiamos un poco esta habitación llena de basura?")
        ]
    }
}

base_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\lessons"
audio_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\audio"
os.makedirs(audio_dir, exist_ok=True)

for i in range(21, 26):
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
for i in range(21, 26):
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
