import os
import shutil

dialogues = {
    1: [
        ("ja-JP-NanamiNeural", "田中さん、どうしたんですか。顔が赤いですよ。"),
        ("ja-JP-KeitaNeural", "実は、熱があるんです。"),
        ("ja-JP-NanamiNeural", "ええっ、大丈夫ですか。病院へ行きましたか。"),
        ("ja-JP-KeitaNeural", "いいえ、まだ行っていないんです。今日の午後、大切な会議があるんです。"),
        ("ja-JP-NanamiNeural", "会議より体のほうが大切ですよ。無理をしないほうがいいです。"),
        ("ja-JP-KeitaNeural", "そうですね。でも、この資料を社長に渡さなければならないんです。"),
        ("ja-JP-NanamiNeural", "じゃあ、私が代わりに渡しておきますよ。"),
        ("ja-JP-KeitaNeural", "本当ですか。ありがとうございます。すみませんが、お願いしてもいいですか。"),
        ("ja-JP-NanamiNeural", "もちろんです。早く帰って休んでください。"),
        ("ja-JP-KeitaNeural", "はい、そうします。本当に助かりました。")
    ],
    2: [
        ("ja-JP-KeitaNeural", "マリアさんは、日本料理が作れますか。"),
        ("ja-JP-NanamiNeural", "はい、少し作れます。昨日も肉じゃがを作りましたよ。"),
        ("ja-JP-KeitaNeural", "すごいですね！私は食べることはできますが、料理は全然できません。"),
        ("ja-JP-NanamiNeural", "そうですか。鈴木さんはどんなことができますか。"),
        ("ja-JP-KeitaNeural", "私はスポーツが得意です。テニスや水泳ができます。"),
        ("ja-JP-NanamiNeural", "いいですね。私は泳げません。海に行くのは好きですが、泳ぐのは苦手です。"),
        ("ja-JP-KeitaNeural", "じゃあ、今度一緒にプールに行きませんか。私が泳ぎ方を教えられますよ。"),
        ("ja-JP-NanamiNeural", "本当ですか。嬉しいです。じゃあ、私はお弁当を作ってきますね。"),
        ("ja-JP-KeitaNeural", "それは楽しみです。マリアさんの作った料理が食べられるんですね。"),
        ("ja-JP-NanamiNeural", "ええ、頑張って美味しいものを作ります！")
    ],
    3: [
        ("ja-JP-NanamiNeural", "ケンさんは、毎日どんなことをしていますか。"),
        ("ja-JP-KeitaNeural", "私は毎朝、コーヒーを飲みながら、新聞を読んでいます。"),
        ("ja-JP-NanamiNeural", "へえ、いいですね。私は朝はいつも忙しいので、パンを食べながら、服を着ています。"),
        ("ja-JP-KeitaNeural", "それは大変ですね。仕事が終わったあとは、何をしていますか。"),
        ("ja-JP-NanamiNeural", "最近は、音楽を聞きながら、晩ごはんを作っています。リラックスできますよ。"),
        ("ja-JP-KeitaNeural", "いいですね。私は、テレビを見ながら、日本語を勉強しています。"),
        ("ja-JP-NanamiNeural", "ええっ、テレビを見ながらですか。集中できますか。"),
        ("ja-JP-KeitaNeural", "はい。時々わからない言葉が出ますが、ニュースを見ながら勉強するのは楽しいです。"),
        ("ja-JP-NanamiNeural", "なるほど。私も今度、日本語のラジオを聞きながら、料理をしてみます。"),
        ("ja-JP-KeitaNeural", "ぜひやってみてください。いい勉強になりますよ。")
    ]
}

audio_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\audio"
os.makedirs(audio_dir, exist_ok=True)

for lesson_id, lines in dialogues.items():
    final_mp3 = os.path.join(audio_dir, f"dialogue-n4-{lesson_id}.mp3")
    print(f"Generating audio for lesson {lesson_id}...")
    files = []
    
    for i, (voice, text) in enumerate(lines):
        filename = f"line_{lesson_id}_{i}.mp3"
        safe_text = text.replace('"', '\\"')
        cmd = f'python -m edge_tts --voice {voice} --text "{safe_text}" --rate=-10% --write-media {filename}'
        os.system(cmd)
        files.append(filename)

    with open(f"files_{lesson_id}.txt", "w", encoding="utf-8") as f:
        for filename in files:
            f.write(f"file '{filename}'\n")

    if os.path.exists(final_mp3):
        os.remove(final_mp3)
    os.system(f"ffmpeg -f concat -safe 0 -i files_{lesson_id}.txt -c copy \"{final_mp3}\"")

    for filename in files:
        if os.path.exists(filename):
            os.remove(filename)
    if os.path.exists(f"files_{lesson_id}.txt"):
        os.remove(f"files_{lesson_id}.txt")
    print(f"Finished {final_mp3}")
