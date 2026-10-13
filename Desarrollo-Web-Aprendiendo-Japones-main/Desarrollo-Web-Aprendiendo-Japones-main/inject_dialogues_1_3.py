import os

html_blocks = {
    1: """<h2 class="section-title">🎧 Práctica de Comprensión Auditiva (Diálogo)</h2>
<div class="grammar-note" style="background-color: #fdf2f8; border-left-color: #ec4899;">
    <p>Escucha este diálogo extenso (aprox. 1 minuto). Presta atención a cómo los personajes utilizan <strong>~んです (explicar situaciones)</strong> de forma natural.</p>
    
    <div style="text-align: center; margin: 1.5rem 0; background: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border: 1px solid #e2e8f0;">
        <p style="margin-bottom: 15px; font-weight: 600; color: #475569; font-size: 1.1rem;">🎧 Escucha el diálogo (Voces IA):</p>
        <audio controls style="width: 100%; max-width: 450px; outline: none; border-radius: 50px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
            <source src="../audio/dialogue-n4-1.mp3" type="audio/mpeg">
            Tu navegador no soporta el elemento de audio.
        </audio>
    </div>

    <details style="background: white; padding: 1rem; border-radius: 8px; border: 1px solid #e2e8f0; margin-top: 1rem;">
        <summary style="font-weight: 600; cursor: pointer; color: var(--primary-color);">Ver Transcripción y Traducción</summary>
        <div style="margin-top: 1rem; display: grid; gap: 1rem; font-size: 0.95rem;">
            <div><div class="text-jp">佐藤：田中さん、どうしたんですか。顔が赤いですよ。</div><div class="text-es">Sato: Tanaka, ¿qué te pasa? Tienes la cara roja.</div></div>
            <div><div class="text-jp">田中：実は、熱があるんです。</div><div class="text-es">Tanaka: La verdad es que tengo fiebre (explicación).</div></div>
            <div><div class="text-jp">佐藤：ええっ、大丈夫ですか。病院へ行きましたか。</div><div class="text-es">Sato: ¿Eh? ¿Estás bien? ¿Fuiste al hospital?</div></div>
            <div><div class="text-jp">田中：いいえ、まだ行っていないんです。今日の午後、大切な会議があるんです。</div><div class="text-es">Tanaka: No, todavía no he ido (explicación). Esta tarde tengo una reunión importante (explicación).</div></div>
            <div><div class="text-jp">佐藤：会議より体のほうが大切ですよ。無理をしないほうがいいです。</div><div class="text-es">Sato: El cuerpo es más importante que la reunión. Es mejor que no te esfuerces demasiado.</div></div>
            <div><div class="text-jp">田中：そうですね。でも、この資料を社長に渡さなければならないんです。</div><div class="text-es">Tanaka: Tienes razón. Pero es que tengo que entregarle este documento al presidente (explicación).</div></div>
            <div><div class="text-jp">佐藤：じゃあ、私が代わりに渡しておきますよ。</div><div class="text-es">Sato: Entonces, yo lo entregaré en tu lugar (dejándolo hecho).</div></div>
            <div><div class="text-jp">田中：本当ですか。ありがとうございます。すみませんが、お願いしてもいいですか。</div><div class="text-es">Tanaka: ¿De verdad? Muchas gracias. Disculpa, pero ¿puedo pedírtelo?</div></div>
            <div><div class="text-jp">佐藤：もちろんです。早く帰って休んでください。</div><div class="text-es">Sato: Por supuesto. Vete a casa pronto y descansa.</div></div>
            <div><div class="text-jp">田中：はい、そうします。本当に助かりました。</div><div class="text-es">Tanaka: Sí, lo haré. Me has sido de gran ayuda.</div></div>
        </div>
    </details>
</div>

""",
    2: """<h2 class="section-title">🎧 Práctica de Comprensión Auditiva (Diálogo)</h2>
<div class="grammar-note" style="background-color: #fdf2f8; border-left-color: #ec4899;">
    <p>Escucha este diálogo extenso (aprox. 1 minuto). Presta atención a cómo los personajes utilizan la <strong>Forma Potencial (~できる / ~られる)</strong>.</p>
    
    <div style="text-align: center; margin: 1.5rem 0; background: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border: 1px solid #e2e8f0;">
        <p style="margin-bottom: 15px; font-weight: 600; color: #475569; font-size: 1.1rem;">🎧 Escucha el diálogo (Voces IA):</p>
        <audio controls style="width: 100%; max-width: 450px; outline: none; border-radius: 50px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
            <source src="../audio/dialogue-n4-2.mp3" type="audio/mpeg">
            Tu navegador no soporta el elemento de audio.
        </audio>
    </div>

    <details style="background: white; padding: 1rem; border-radius: 8px; border: 1px solid #e2e8f0; margin-top: 1rem;">
        <summary style="font-weight: 600; cursor: pointer; color: var(--primary-color);">Ver Transcripción y Traducción</summary>
        <div style="margin-top: 1rem; display: grid; gap: 1rem; font-size: 0.95rem;">
            <div><div class="text-jp">鈴木：マリアさんは、日本料理が作れますか。</div><div class="text-es">Suzuki: Maria, ¿puedes hacer comida japonesa?</div></div>
            <div><div class="text-jp">マリア：はい、少し作れます。昨日も肉じゃがを作りましたよ。</div><div class="text-es">Maria: Sí, puedo hacer un poco. Ayer también preparé nikujaga.</div></div>
            <div><div class="text-jp">鈴木：すごいですね！私は食べることはできますが、料理は全然できません。</div><div class="text-es">Suzuki: ¡Increíble! Yo comer sí puedo, pero cocinar no puedo en absoluto.</div></div>
            <div><div class="text-jp">マリア：そうですか。鈴木さんはどんなことができますか。</div><div class="text-es">Maria: ¿Ah sí? Suzuki, ¿qué cosas puedes hacer?</div></div>
            <div><div class="text-jp">鈴木：私はスポーツが得意です。テニスや水泳ができます。</div><div class="text-es">Suzuki: Se me dan bien los deportes. Puedo jugar tenis y nadar.</div></div>
            <div><div class="text-jp">マリア：いいですね。私は泳げません。海に行くのは好きですが、泳ぐのは苦手です。</div><div class="text-es">Maria: Qué bien. Yo no puedo nadar. Me gusta ir al mar, pero nadar se me da mal.</div></div>
            <div><div class="text-jp">鈴木：じゃあ、今度一緒にプールに行きませんか。私が泳ぎ方を教えられますよ。</div><div class="text-es">Suzuki: Entonces, ¿vamos juntos a la piscina la próxima vez? Yo te puedo enseñar a nadar.</div></div>
            <div><div class="text-jp">マリア：本当ですか。嬉しいです。じゃあ、私はお弁当を作ってきますね。</div><div class="text-es">Maria: ¿De verdad? Me alegro. Entonces, yo prepararé bento (comida para llevar) y lo llevaré.</div></div>
            <div><div class="text-jp">鈴木：それは楽しみです。マリアさんの作った料理が食べられるんですね。</div><div class="text-es">Suzuki: Eso es emocionante. Así que podré comer la comida que prepara Maria.</div></div>
            <div><div class="text-jp">マリア：ええ、頑張って美味しいものを作ります！</div><div class="text-es">Maria: Sí, me esforzaré y haré algo delicioso!</div></div>
        </div>
    </details>
</div>

""",
    3: """<h2 class="section-title">🎧 Práctica de Comprensión Auditiva (Diálogo)</h2>
<div class="grammar-note" style="background-color: #fdf2f8; border-left-color: #ec4899;">
    <p>Escucha este diálogo extenso (aprox. 1 minuto). Presta atención a cómo los personajes utilizan <strong>~ながら (acciones simultáneas)</strong> y <strong>~ています (hábitos)</strong>.</p>
    
    <div style="text-align: center; margin: 1.5rem 0; background: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border: 1px solid #e2e8f0;">
        <p style="margin-bottom: 15px; font-weight: 600; color: #475569; font-size: 1.1rem;">🎧 Escucha el diálogo (Voces IA):</p>
        <audio controls style="width: 100%; max-width: 450px; outline: none; border-radius: 50px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
            <source src="../audio/dialogue-n4-3.mp3" type="audio/mpeg">
            Tu navegador no soporta el elemento de audio.
        </audio>
    </div>

    <details style="background: white; padding: 1rem; border-radius: 8px; border: 1px solid #e2e8f0; margin-top: 1rem;">
        <summary style="font-weight: 600; cursor: pointer; color: var(--primary-color);">Ver Transcripción y Traducción</summary>
        <div style="margin-top: 1rem; display: grid; gap: 1rem; font-size: 0.95rem;">
            <div><div class="text-jp">山本：ケンさんは、毎日どんなことをしていますか。</div><div class="text-es">Yamamoto: Ken, ¿qué cosas sueles hacer todos los días?</div></div>
            <div><div class="text-jp">ケン：私は毎朝、コーヒーを飲みながら、新聞を読んでいます。</div><div class="text-es">Ken: Todas las mañanas, leo el periódico mientras me tomo un café.</div></div>
            <div><div class="text-jp">山本：へえ、いいですね。私は朝はいつも忙しいので、パンを食べながら、服を着ています。</div><div class="text-es">Yamamoto: Vaya, qué bien. Yo como siempre estoy ocupada por las mañanas, me visto mientras me como un pan.</div></div>
            <div><div class="text-jp">ケン：それは大変ですね。仕事が終わったあとは、何をしていますか。</div><div class="text-es">Ken: Eso es duro. Y después de terminar el trabajo, ¿qué haces?</div></div>
            <div><div class="text-jp">山本：最近は、音楽を聞きながら、晩ごはんを作っています。リラックスできますよ。</div><div class="text-es">Yamamoto: Últimamente, preparo la cena mientras escucho música. Es relajante.</div></div>
            <div><div class="text-jp">ケン：いいですね。私は、テレビを見ながら、日本語を勉強しています。</div><div class="text-es">Ken: Qué bien. Yo estudio japonés mientras veo la televisión.</div></div>
            <div><div class="text-jp">山本：ええっ、テレビを見ながらですか。集中できますか。</div><div class="text-es">Yamamoto: ¿Eh? ¿Mientras ves la tele? ¿Te puedes concentrar?</div></div>
            <div><div class="text-jp">ケン：はい。時々わからない言葉が出ますが、ニュースを見ながら勉強するのは楽しいです。</div><div class="text-es">Ken: Sí. A veces salen palabras que no entiendo, pero es divertido estudiar mientras veo las noticias.</div></div>
            <div><div class="text-jp">山本：なるほど。私も今度、日本語のラジオを聞きながら、料理をしてみます。</div><div class="text-es">Yamamoto: Ya veo. La próxima vez yo también intentaré cocinar mientras escucho la radio en japonés.</div></div>
            <div><div class="text-jp">ケン：ぜひやってみてください。いい勉強になりますよ。</div><div class="text-es">Ken: Anímate a probarlo. Será un buen estudio.</div></div>
        </div>
    </details>
</div>

"""
}

base_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\lessons"

for i in range(1, 4):
    filepath = os.path.join(base_dir, f"jlpt-n4-{i}.html")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "🎧 Práctica de Comprensión Auditiva" in content:
        print(f"Skipping lesson {i}, already has dialogue.")
        continue
        
    target_str = '<h2 class="section-title">📝 Ejercicios de Práctica JLPT</h2>'
    new_content = content.replace(target_str, html_blocks[i] + target_str)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Injected dialogue into jlpt-n4-{i}.html")
