import os
import re

examples_data = {
    29: [
        ("窓が閉まっています。", "1. La ventana está cerrada.", "まどがしまっています"),
        ("電車が込んでいます。", "2. El tren está lleno.", "でんしゃがこんでいます"),
        ("このパソコンは壊れています。", "3. Esta computadora está rota.", "このパソコンはこわれています"),
        ("お皿が割れています。", "4. El plato está roto.", "おさらがわれています"),
        ("宿題をしてしまいました。", "5. He terminado completamente la tarea.", "しゅくだいをしてしまいました"),
        ("パスポートをなくしてしまいました。", "6. Lamentablemente perdí mi pasaporte.", "パスポートをなくしてしまいました"),
        ("電車に傘を忘れてしまいました。", "7. Olvidé (lamentablemente) el paraguas en el tren.", "でんしゃにかさをわすれてしまいました"),
        ("お酒を全部飲んでしまいました。", "8. Me bebí todo el alcohol (terminado).", "おさけをぜんぶのんでしまいました"),
        ("エアコンがついています。", "9. El aire acondicionado está encendido.", "エアコンがついています"),
        ("道がすいています。", "10. El camino está despejado (vacío).", "みちがすいています")
    ],
    30: [
        ("カレンダーが掛けてあります。", "1. El calendario está colgado (alguien lo colgó).", "カレンダーがかけてあります"),
        ("机の上に本が置いてあります。", "2. El libro está puesto sobre el escritorio.", "つくえのうえにほんがおいてあります"),
        ("壁にポスターが貼ってあります。", "3. El póster está pegado en la pared.", "かべにポスターがはってあります"),
        ("名前にふりがなが書いてあります。", "4. El furigana está escrito en el nombre.", "なまえにふりがながかいてあります"),
        ("旅行の前に、ホテルを予約しておきます。", "5. Antes del viaje, reservaré el hotel (preparación).", "りょこうのまえに、ホテルをよやくしておきます"),
        ("パーティーの前に、部屋を掃除しておきます。", "6. Limpiaré la habitación antes de la fiesta.", "パーティーのまえに、へやをそうじしておきます"),
        ("使ったら、元の所に戻しておいてください。", "7. Si lo usas, por favor devuélvelo a su lugar original.", "つかったら、もとのところにもどしておいてください"),
        ("窓は開けておいてください。", "8. Por favor, deja la ventana abierta (como está).", "まどはあけておいてください"),
        ("冷蔵庫にビールが冷やしてあります。", "9. La cerveza está enfriada en el refrigerador.", "れいぞうこにビールがひやしてあります"),
        ("明日までにレポートを書いておきます。", "10. Escribiré el reporte para mañana (como preparación).", "あしたまでにレポートをかいておきます")
    ],
    31: [
        ("週末は海に行こうと思っています。", "1. Estoy pensando en ir al mar el fin de semana.", "しゅうまつはうみにいこうとおもっています"),
        ("将来、自分の会社を作ろうと思っています。", "2. En el futuro, pienso crear mi propia empresa.", "しょうらい、じぶんのかいしゃをつくろうとおもっています"),
        ("来年、日本へ留学するつもりです。", "3. Tengo la intención de estudiar en Japón el próximo año.", "らいねん、にほんへりゅうがくするつもりです"),
        ("今日は何もしないつもりです。", "4. Hoy tengo la intención de no hacer nada.", "きょうはなにもしないつもりです"),
        ("たばこを吸わないつもりです。", "5. Tengo la intención de no fumar.", "たばこをすわないつもりです"),
        ("７月の終わりにドイツへ出張する予定です。", "6. Está programado que haga un viaje de negocios a Alemania a finales de julio.", "しちがつのおわりにドイツへしゅっちょうするよていです"),
        ("会議は１０時からの予定です。", "7. La reunión está programada desde las 10.", "かいぎはじゅうじからのよていです"),
        ("疲れたから、ちょっと休もう。", "8. Como estoy cansado, descansemos un poco.", "つかれたから、ちょっとやすもう"),
        ("早く寝ようと思っています。", "9. Estoy pensando en dormir temprano.", "はやくねようとおもっています"),
        ("新しい車を買うつもりです。", "10. Tengo la intención de comprar un auto nuevo.", "あたらしいくるまをかうつもりです")
    ],
    32: [
        ("毎日運動したほうがいいですよ。", "1. Es mejor que hagas ejercicio todos los días.", "まいにちうんどうしたほうがいいですよ"),
        ("熱があるから、お風呂に入らないほうがいいです。", "2. Como tienes fiebre, es mejor que no te bañes.", "ねつがあるから、おふろにはいらないほうがいいです"),
        ("もっと野菜を食べたほうがいいですよ。", "3. Es mejor que comas más verduras.", "もっとやさいをたべたほうがいいですよ"),
        ("夜遅くまで起きないほうがいいです。", "4. Es mejor no quedarse despierto hasta tarde en la noche.", "よるおそくまでおきないほうがいいです"),
        ("明日は雨が降るでしょう。", "5. Probablemente mañana llueva.", "あしたはあめがふるでしょう"),
        ("彼は来ないでしょう。", "6. Probablemente él no venga.", "かれはこないでしょう"),
        ("午後は雪になるかもしれません。", "7. Quizás nieve en la tarde.", "ごごはゆきになるかもしれません"),
        ("約束の時間に間に合わないかもしれません。", "8. Quizás no llegue a tiempo a la hora acordada.", "やくそくのじかんにまにあわないかもしれません"),
        ("あのレストランはおいしいでしょう。", "9. Ese restaurante probablemente sea delicioso.", "あのレストランはおいしいでしょう"),
        ("明日のテストは難しいかもしれません。", "10. Quizás el examen de mañana sea difícil.", "あしたのテストはむずかしいかもしれません")
    ],
    33: [
        ("早く寝ろ！", "1. ¡Duérmete rápido! (Imperativo)", "はやくねろ"),
        ("もっと勉強しろ！", "2. ¡Estudia más!", "もっとべんきょうしろ"),
        ("ここに車を止めるな！", "3. ¡No aparques el coche aquí! (Prohibitivo)", "ここにくるまをとめるな"),
        ("タバコを吸うな！", "4. ¡No fumes!", "タバコをすうな"),
        ("あそこに「止まれ」と書いてあります。", "5. Allí está escrito 'Detente' (Stop).", "あそこに、とまれとかいてあります"),
        ("これはどういう意味ですか。", "6. ¿Qué significa esto?", "これはどういういみですか"),
        ("「立入禁止」は入るなという意味です。", "7. 'Tachiiri Kinshi' significa 'No entrar'.", "たちいりきんしは、はいるなという意味です"),
        ("田中さんは明日休むと言っていました。", "8. El señor Tanaka dijo que mañana descansaría.", "たなかさんはあしたやすむといっていました"),
        ("社長に会議に出るように伝えていただけませんか。", "9. ¿Podría transmitirle al director que asista a la reunión?", "しゃちょうにかいぎにでるようにつたえていただけませんか"),
        ("逃げろ！", "10. ¡Huye!", "にげろ")
    ],
    34: [
        ("私がやるとおりに、やってください。", "1. Por favor, hazlo tal y como yo lo hago.", "わたしがやるとおりに、やってください"),
        ("先生が言ったとおりに、書きました。", "2. Lo escribí tal y como dijo el profesor.", "せんせいがいたとおりに、かきました"),
        ("線のとおりに、紙を切ってください。", "3. Por favor, corta el papel siguiendo la línea.", "せんのとおりに、かみをきってください"),
        ("説明書のとおりに、組み立てます。", "4. Lo ensamblo tal como dice el manual de instrucciones.", "せつめいしょのとおりに、くみたてます"),
        ("ご飯を食べたあとで、歯を磨きます。", "5. Después de comer, me lavo los dientes.", "ごはんをたべたあとで、はをみがきます"),
        ("仕事のあとで、飲みに行きませんか。", "6. Después del trabajo, ¿vamos a beber?", "しごとのあとで、のみにいきませんか"),
        ("新しいのを買ったあとで、なくした時計が見つかりました。", "7. Después de comprar uno nuevo, encontré el reloj que había perdido.", "あたらしいのをかったあとで、なくしたとけいがみつかりました"),
        ("コーヒーは砂糖を入れないで飲みます。", "8. Bebo el café sin ponerle azúcar.", "コーヒーはさとうをいれないでのみます"),
        ("傘を持たないで出かけました。", "9. Salí sin llevar paraguas.", "かさをもたないででかけました"),
        ("日曜日はどこも行かないで、家で休みます。", "10. El domingo no voy a ningún lado y descanso en casa.", "にちようびはどこもいかないで、いえでやすみます")
    ],
    35: [
        ("春になれば、桜が咲きます。", "1. Si llega la primavera, los cerezos florecerán.", "はるになれば、さくらがさきます"),
        ("天気がよければ、散歩に行きます。", "2. Si hace buen tiempo, iré a dar un paseo.", "てんきがよければ、さんぽにいきます"),
        ("安ければ、買います。", "3. Si es barato, lo compraré.", "やすければ、かいます"),
        ("暇なら、手伝ってください。", "4. Si estás libre, ayúdame por favor.", "ひまなら、てつだってください"),
        ("いい天気なら、海へ行きたいです。", "5. Si hace buen tiempo, quiero ir al mar.", "いいてんきなら、うみへいきたいです"),
        ("温泉なら、箱根がいいですよ。", "6. Si hablamos de aguas termales, Hakone es un buen lugar.", "おんせんなら、はこねがいいですよ"),
        ("説明書を読めば、わかります。", "7. Si lees el manual, lo entenderás.", "せつめいしょをよめば、わかります"),
        ("ボタンを押せば、窓が開きます。", "8. Si presionas el botón, la ventana se abre.", "ボタンをおせば、まどがあきます"),
        ("日本語がわかれば、楽しいです。", "9. Si entiendes japonés, es divertido.", "にほんごがわかれば、たのしいです"),
        ("パソコンがなければ、不便です。", "10. Si no hay computadora, es inconveniente.", "パソコンがなければ、ふべんです")
    ],
    36: [
        ("日本語が話せるように、毎日練習します。", "1. Practico todos los días para poder hablar japonés.", "にほんごがはなせるように、まいにちれんしゅうします"),
        ("風邪を引かないように、コートを着ます。", "2. Me pongo el abrigo para no resfriarme.", "かぜをひかないように、コートをきます"),
        ("忘れないように、メモします。", "3. Tomo notas para no olvidar.", "わすれないように、メモします"),
        ("日本語がわかるようになりました。", "4. He llegado a poder entender japonés.", "にほんごがわかるようになりました"),
        ("自転車に乗れるようになりました。", "5. Ya puedo montar en bicicleta (antes no podía).", "じてんしゃにのれるようになりました"),
        ("肉が食べられなくなりました。", "6. Ya no puedo comer carne.", "にくがたべられなくなりました"),
        ("毎日運動するようにしています。", "7. Hago el esfuerzo de hacer ejercicio todos los días.", "まいにちうんどうするようにしています"),
        ("甘い物を食べないようにしています。", "8. Procuro no comer cosas dulces.", "あまいものをたべないようにしています"),
        ("もっと野菜を食べるようにしてください。", "9. Por favor, procure comer más verduras.", "もっとやさいをたべるようにしてください"),
        ("絶対に遅れないようにしてください。", "10. Por favor, asegúrese de no llegar tarde.", "ぜったいにおくれないようにしてください")
    ],
    37: [
        ("私は先生に褒められました。", "1. Fui elogiado por el profesor.", "わたしはせんせいにほめられました"),
        ("母に買い物を頼まれました。", "2. Mi madre me pidió que hiciera las compras.", "ははにかいものをたのまれました"),
        ("犬に手を噛まれました。", "3. Fui mordido en la mano por un perro.", "いぬにてをかまれました"),
        ("弟にパソコンを壊されました。", "4. Mi hermano menor rompió mi computadora (Pasiva de molestia).", "おとうとにパソコンをこわされました"),
        ("泥棒にお金を盗まれました。", "5. Un ladrón me robó el dinero.", "どろぼうにおかねをぬすまれました"),
        ("雨に降られて、服が濡れました。", "6. Llovió (fui afectado por la lluvia) y mi ropa se mojó.", "あめにふられて、ふくがぬれました"),
        ("この絵はピカソによって描かれました。", "7. Este cuadro fue pintado por Picasso.", "このえはピカソによってかかれました"),
        ("電話はベルによって発明されました。", "8. El teléfono fue inventado por Bell.", "でんわはベルによってはつめいされました"),
        ("来年大阪で展覧会が開かれます。", "9. El próximo año se realizará una exposición en Osaka.", "らいねんおおさかでてんらんかいがひらかれます"),
        ("この本は世界中で読まれています。", "10. Este libro es leído en todo el mundo.", "このほんはせかいじゅうでよまれています")
    ],
    38: [
        ("絵を描くのは楽しいです。", "1. Dibujar cuadros es divertido.", "えをかくのはたのしいです"),
        ("星を見るのが好きです。", "2. Me gusta mirar las estrellas.", "ほしをみるのがすきです"),
        ("一人で旅行するのは寂しいです。", "3. Viajar solo es solitario.", "ひとりでりょこうするのはさびしいです"),
        ("財布を持って来るのを忘れました。", "4. Me olvidé de traer la cartera.", "さいふをもってくるのをわすれました"),
        ("窓を閉めるのを忘れました。", "5. Me olvidé de cerrar la ventana.", "まどをしめるのをわすれました"),
        ("鈴木さんが結婚したのを知っていますか。", "6. ¿Sabes que el Sr. Suzuki se casó?", "すずきさんがけっこんしたのをしっていますか"),
        ("木村さんに赤ちゃんが生まれたのを知っていますか。", "7. ¿Sabes que a la Sra. Kimura le nació un bebé?", "きむらさんにあかちゃんがうまれたのをしっていますか"),
        ("娘が帰って来るのは８時ごろです。", "8. (El momento en que) mi hija vuelve es alrededor de las 8.", "むすめがかえってくるのははちじごろです"),
        ("私が生まれたのは小さな村です。", "9. Donde nací es un pueblo pequeño.", "わたしがうまれたのはちいさなむらです"),
        ("日本語を勉強するのは面白いです。", "10. Estudiar japonés es interesante.", "にほんごをべんきょうするのはおもしろいです")
    ],
    39: [
        ("ニュースを聞いて、びっくりしました。", "1. Me sorprendí al escuchar las noticias.", "ニュースをきいて、びっくりしました"),
        ("家族に会えなくて、寂しいです。", "2. Estoy triste porque no puedo ver a mi familia.", "かぞくにあえなくて、さびしいです"),
        ("お金がなくて、パソコンが買えません。", "3. Como no tengo dinero, no puedo comprar la computadora.", "おかねがなくて、パソコンがかえません"),
        ("事故で電車が遅れました。", "4. El tren se retrasó por un accidente.", "じこででんしゃがおくれました"),
        ("地震でビルが倒れました。", "5. El edificio se derrumbó por el terremoto.", "じしんでビルがたおれました"),
        ("病気で会社を休みました。", "6. Falté al trabajo por enfermedad.", "びょうきでかいしゃをやすみました"),
        ("気分が悪いので、帰ってもいいですか。", "7. Como me siento mal, ¿puedo irme a casa?", "きぶんがわるいので、かえってもいいですか"),
        ("用事があるので、お先に失礼します。", "8. Como tengo asuntos que atender, con su permiso me retiro.", "ようじがあるので、おさきにしつれいします"),
        ("日本語がわからないので、教えてください。", "9. Como no entiendo japonés, por favor enséñeme.", "にほんごがわからないので、おしえてください"),
        ("台風が来るので、気をつけてください。", "10. Como viene un tifón, tenga cuidado.", "たいふうがくるので、きをつけてください")
    ],
    40: [
        ("会議が何時に終わるか、わかりません。", "1. No sé a qué hora terminará la reunión.", "かいぎがなんじにおわるか、わかりません"),
        ("箱の中に何が入っているか、調べてください。", "2. Por favor investigue qué hay dentro de la caja.", "はこのなかになにがはいっているか、しらべてください"),
        ("彼がどこに住んでいるか、知っていますか。", "3. ¿Sabes dónde vive él?", "かれがどこにすんでいるか、しっていますか"),
        ("その話が本当かどうか、わかりません。", "4. No sé si esa historia es verdad o no.", "そのはなしがほんとうかどうか、わかりません"),
        ("明日雪が降るかどうか、心配です。", "5. Me preocupa si mañana nevará o no.", "あしたゆきがふるかどうか、しんぱいです"),
        ("間違いがないかどうか、確認してください。", "6. Por favor, confirme si hay errores o no.", "まちがいがないかどうか、かくにんしてください"),
        ("この靴を履いてみてもいいですか。", "7. ¿Puedo probarme estos zapatos?", "このくつをはいてみてもいいですか"),
        ("おいしいかどうか、食べてみます。", "8. Comeré (probaré) para ver si está delicioso o no.", "おいしいかどうか、たべてみます"),
        ("新しい店に行ってみましょう。", "9. Intentemos ir a la tienda nueva.", "あたらしいみせにいってみましょう"),
        ("あの服を着てみたいです。", "10. Quiero probarme esa ropa.", "あのふくをきてみたいです")
    ],
    41: [
        ("私は社長に時計をいただきました。", "1. Recibí un reloj del presidente.", "わたしはしゃちょうにとけいをいただきました"),
        ("先生にお土産をいただきました。", "2. Recibí un regalo (souvenir) del profesor.", "せんせいにおみやげをいただきました"),
        ("先生が私に本をくださいました。", "3. El profesor me dio un libro.", "せんせいがわたしにほんをくださいました"),
        ("部長が私を手伝ってくださいました。", "4. El jefe de departamento me ayudó.", "ぶちょうがわたしをてつだってくださいました"),
        ("私は犬にえさをやります。", "5. Yo le doy comida al perro.", "わたしはいぬにえさをやります"),
        ("私は花に水をやります。", "6. Yo riego (le doy agua) a las flores.", "わたしははなにみずをやります"),
        ("先生に漢字を教えていただきました。", "7. El profesor tuvo la amabilidad de enseñarme kanji.", "せんせいにかんじをおしえていただきました"),
        ("課長が旅行の写真を送ってくださいました。", "8. El jefe de sección tuvo la amabilidad de enviarme las fotos del viaje.", "かちょうがりょこうのしゃしんをおくってくださいました"),
        ("私は息子におもちゃを買ってやりました。", "9. Le compré un juguete a mi hijo.", "わたしはむすこにおもちゃをかってやりました"),
        ("ペンを貸していただけませんか。", "10. ¿Tendría la amabilidad de prestarme un bolígrafo?", "ペンをかしていただけませんか")
    ],
    42: [
        ("自分の店を持つために、貯金しています。", "1. Ahorro dinero para tener mi propia tienda.", "じぶんのみせをもつために、ちょきんしています"),
        ("家族のために、うちを建てます。", "2. Construiré una casa por el bien de mi familia.", "かぞくのために、うちをたてます"),
        ("健康のために、毎日走っています。", "3. Corro todos los días por mi salud.", "けんこうのために、まいにちはしっています"),
        ("日本語を勉強するために、日本へ来ました。", "4. Vine a Japón para estudiar japonés.", "にほんごをべんきょうするために、にほんへきました"),
        ("このはさみは花を切るのに使います。", "5. Estas tijeras se usan para cortar flores.", "このはさみははなをきるのに、つかいます"),
        ("このかばんは大きくて、旅行に便利です。", "6. Esta bolsa es grande y es conveniente para viajar (Sustantivo + に).", "このかばんは大きくて、りょこうにべんりです"),
        ("電話をかけるのに、時間がかかります。", "7. Toma tiempo para hacer una llamada telefónica.", "でんわをかけるのに、じかんがかかります"),
        ("このパソコンは仕事に役に立ちます。", "8. Esta computadora es útil para el trabajo.", "このパソコンはしごとにやくにたちます"),
        ("車を買うのに、１００万円必要です。", "9. Para comprar un auto, se necesitan un millón de yenes.", "くるまをかうのに、ひゃくまんえんひつようです"),
        ("大学に入るために、一生懸命勉強します。", "10. Estudiaré con todas mis fuerzas para entrar a la universidad.", "だいがくにはいるために、いっしょうけんめいべんきょうします")
    ],
    43: [
        ("今にも雨が降りそうです。", "1. Parece que va a llover de un momento a otro.", "いまにもあめがふりそうです"),
        ("この料理はとてもおいしそうです。", "2. Esta comida parece deliciosa (tiene buena pinta).", "このりょうりはとてもおいしそうです"),
        ("彼はとても忙しそうです。", "3. Él parece estar muy ocupado.", "かれはとてもいそがしそうです"),
        ("あのケーキは甘そうです。", "4. Ese pastel parece dulce.", "あのケーキはあまそうです"),
        ("この本は難しそうですね。", "5. Este libro parece difícil, ¿verdad?", "このほんはむずかしそうですね"),
        ("ちょっとたばこを買って来ます。", "6. Voy a comprar cigarrillos un momento (y vuelvo).", "ちょっとたばこをかってきます"),
        ("スーパーへ牛乳を買って来ます。", "7. Voy al supermercado a comprar leche (y vuelvo).", "スーパーへぎゅうにゅうをかってきます"),
        ("お手洗いに言って来てもいいですか。", "8. ¿Puedo ir al baño (y volver)?", "おてあらいにいってきてもいいですか"),
        ("あそこに電話をかけて来ます。", "9. Voy a hacer una llamada allí (y vuelvo).", "あそこにでんわをかけてきます"),
        ("荷物を取って来ますから、待っていてください。", "10. Voy a recoger mi equipaje y vuelvo, espere por favor.", "にもつをとってきますから、まっていてください")
    ],
    44: [
        ("ゆうべお酒を飲みすぎました。", "1. Anoche bebí demasiado alcohol.", "ゆうべおさけをのみすぎました"),
        ("このセーターは大きすぎます。", "2. Este jersey es demasiado grande.", "このセーターはおおきすぎます"),
        ("あの映画は面白すぎます。", "3. Esa película es demasiado interesante.", "あのえいがはおもしろすぎます"),
        ("ご飯を食べすぎて、お腹が痛いです。", "4. Comí demasiado y me duele el estómago.", "ごはんをたべすぎて、おなかがいたいです"),
        ("このパソコンは使いやすいです。", "5. Esta computadora es fácil de usar.", "このパソコンはつかいやすいです"),
        ("東京は住みにくいです。", "6. Tokio es difícil para vivir.", "とうきょうはすみにくいです"),
        ("この薬は飲みやすいです。", "7. Esta medicina es fácil de tomar.", "このくすりはのみやすいです"),
        ("雨の日は事故が起きやすいです。", "8. En los días de lluvia es fácil que ocurran accidentes.", "あめのひはじこがおきやすいです"),
        ("髪を短くします。", "9. Haré (cortaré) mi cabello corto.", "かみをみじかくします"),
        ("部屋をきれいにします。", "10. Limpiaré la habitación (la haré limpia).", "へやをきれいにします")
    ],
    45: [
        ("会議に間に合わない場合は、連絡してください。", "1. En caso de que no llegues a tiempo a la reunión, por favor avisa.", "かいぎにまにあわないばあいは、れんらくしてください"),
        ("地震の場合は、エレベーターを使わないでください。", "2. En caso de terremoto, no use el ascensor.", "じしんのばあいは、エレベーターをつかわないでください"),
        ("カードをなくした場合は、すぐ会社に電話してください。", "3. En caso de que pierda la tarjeta, llame inmediatamente a la compañía.", "カードをなくしたばあいは、すぐかいしゃにでんわしてください"),
        ("パソコンの調子が悪い場合は、どうしたらいいですか。", "4. En caso de que la computadora no funcione bien, ¿qué debería hacer?", "パソコンのちょうしがわるいばあいは、どうしたらいいですか"),
        ("約束をしたのに、彼女は来ませんでした。", "5. A pesar de que prometió venir, ella no vino.", "やくそくをしたのに、かのじょはきませんでした"),
        ("毎日練習しているのに、上手になりません。", "6. A pesar de que practico todos los días, no mejoro.", "まいにちれんしゅうしているのに、じょうずになりません"),
        ("日曜日は休みなのに、働かなければなりません。", "7. A pesar de que el domingo es de descanso, tengo que trabajar.", "にちようびはやすみなのに、はたらかなければなりません"),
        ("薬を飲んだのに、熱が下がりません。", "8. A pesar de que tomé la medicina, la fiebre no baja.", "くすりをのんだのに、ねつがさがりません"),
        ("静かなのに、勉強できません。", "9. A pesar de que está silencioso, no puedo estudiar.", "しずかなのに、べんきょうできません"),
        ("たくさん食べたのに、まだお腹がすいています。", "10. A pesar de haber comido mucho, todavía tengo hambre.", "たくさんたべたのに、まだおなかがすいています")
    ],
    46: [
        ("これからご飯を食べるところです。", "1. Estoy a punto de comer ahora.", "これからごはんをたべるところです"),
        ("今から出かけるところです。", "2. Estoy a punto de salir ahora.", "いまからでかけるところです"),
        ("今、部屋を掃除しているところです。", "3. Ahora, estoy en medio de limpiar la habitación.", "いま、へやをそうじしているところです"),
        ("ちょうど会議が始まったところです。", "4. La reunión justo acaba de empezar (hace nada).", "ちょうとかいぎがはじまったところです"),
        ("たった今バスが出たところです。", "5. El autobús acaba de salir justo ahora.", "たったいまバスがでたところです"),
        ("先月この会社に入ったばかりです。", "6. Acabo de entrar a esta empresa el mes pasado.", "せんげつこのかいしゃにはいったばかりです"),
        ("さっき起きたばかりです。", "7. Me acabo de levantar hace un rato.", "さっきおきたばかりです"),
        ("このカメラは買ったばかりなのに、壊れました。", "8. A pesar de que acabo de comprar esta cámara, se rompió.", "このカメラはかったばかりなのに、こわれました"),
        ("田中さんは旅行に行っているので、今日は来ないはずです。", "9. Como el Sr. Tanaka se fue de viaje, se espera (es obvio) que no venga hoy.", "たなかさんはりょこうにいっているので、きょうはこないはずです"),
        ("会議は３時に終わるはずです。", "10. La reunión debería terminar a las 3.", "かいぎはさんじにおわるはずです")
    ],
    47: [
        ("天気予報によると、明日は寒くなるそうです。", "1. Según el pronóstico del tiempo, mañana hará frío.", "てんきよほうによると、あしたはさむくなるそうです"),
        ("先生の話によると、試験は難しいそうです。", "2. Según cuenta el profesor, el examen será difícil.", "せんせいのはなしによると、しけんはむずかしいそうです"),
        ("ニュースによると、アメリカで大きい地震があったそうです。", "3. Según las noticias, hubo un gran terremoto en Estados Unidos.", "ニュースによると、アメリカでおおきいじしんがあったそうです"),
        ("彼は来年結婚するそうです。", "4. He oído que él se casará el próximo año.", "かれはらいねんけっこんするそうです"),
        ("バリ島はとてもきれいだそうです。", "5. Se dice que la isla de Bali es muy hermosa.", "バリとうはとてもきれいだそうです"),
        ("咳も出るし、風邪を引いたようです。", "6. Además de que tengo tos, parece que me he resfriado.", "せきもでるし、かぜをひいたようです"),
        ("人がたくさん集まっていますね。事故のようです。", "7. Se ha reunido mucha gente. Parece que es un accidente.", "ひとがたくさんあつまっていますね。じこのようです"),
        ("電気が消えています。彼はもう寝たようです。", "8. La luz está apagada. Parece que él ya se durmió.", "でんきがきえています。かれはもうねたようです"),
        ("あのレストランはいつも人が多いです。おいしいようです。", "9. Ese restaurante siempre tiene mucha gente. Parece ser delicioso.", "あのレストランはいつもひとがおおいです。おいしいようです"),
        ("道が濡れています。雨が降ったようです。", "10. El camino está mojado. Parece que llovió.", "みちがぬれています。あめがふったようです")
    ]
}

def inject_examples():
    base_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\lessons"
    
    for lesson_num, examples in examples_data.items():
        filepath = os.path.join(base_dir, f"lesson-{lesson_num}.html")
        if not os.path.exists(filepath):
            print(f"Skipping {filepath} - not found.")
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if "<!-- 10 Ejemplos de Uso -->" in content:
            print(f"Skipping Lesson {lesson_num} - already has examples.")
            continue
            
        html_to_inject = [
            '        <!-- 10 Ejemplos de Uso -->',
            '        <h2 class="section-title">🌟 10 Ejemplos de Uso</h2>',
            '        <div class="grammar-note"><p>A continuación, 10 ejemplos prácticos utilizando la gramática aprendida en esta lección.</p></div>',
            ''
        ]
        
        for jp, es, kana in examples:
            html_to_inject.append(f'        <div class="practice-item"><div class="practice-content"><div class="text-jp">{jp}</div><div class="text-es">{es}</div></div><button class="audio-btn" onclick="playAudio(\'{kana}\')">🔊</button></div>')
            
        html_to_inject.append('')
        html_to_inject.append('        <!-- Ejercicios Prácticos -->')
        
        replacement = "\\n".join(html_to_inject)
        
        new_content = content.replace("        <!-- Ejercicios Prácticos -->", replacement)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"Updated Lesson {lesson_num}")

if __name__ == '__main__':
    inject_examples()
