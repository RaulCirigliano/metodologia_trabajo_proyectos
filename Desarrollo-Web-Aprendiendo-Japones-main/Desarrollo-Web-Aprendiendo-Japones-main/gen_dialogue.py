import os
import shutil

dialogue = [
    ("ja-JP-NanamiNeural", "ああ、どうしよう。困ってしまいました。"),
    ("ja-JP-KeitaNeural", "田中さん、どうしたんですか。"),
    ("ja-JP-NanamiNeural", "実は、電車の中に財布を忘れてしまったんです。"),
    ("ja-JP-KeitaNeural", "ええっ、本当ですか。それは大変ですね。どこで忘れたんですか。"),
    ("ja-JP-NanamiNeural", "新宿駅から乗ったんですが、たぶん寝てしまって... 目が覚めたら東京駅でした。急いで降りたので、カバンを開けたとき、財布がなかったんです。全部で3万円ぐらい入っていたのに、なくしてしまいました。"),
    ("ja-JP-KeitaNeural", "それは残念でしたね。駅員に言いましたか。"),
    ("ja-JP-NanamiNeural", "はい、すぐ言いました。でも、「まだ見つかっていません」と言われてしまいました。大切なカードもたくさん入っていたので、本当に困っています。"),
    ("ja-JP-KeitaNeural", "警察にも行ってみたほうがいいですよ。もしかしたら、誰かが拾って交番に届けてくれたかもしれません。"),
    ("ja-JP-NanamiNeural", "そうですね。これから交番へ行ってきます。今日はお昼ごはんを食べるお金もないので、お腹が空いて死んでしまいそうです。"),
    ("ja-JP-KeitaNeural", "じゃあ、私が千円貸してあげますよ。とりあえず、これで何か食べてください。"),
    ("ja-JP-NanamiNeural", "本当ですか。ありがとうございます。明日必ず返します。ああ、昨日の夜、遅くまでお酒を飲んでしまったから、こんなことになってしまったんです。これからは気をつけます。")
]

# Ensure audio dir exists
audio_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\audio"
os.makedirs(audio_dir, exist_ok=True)

final_mp3 = os.path.join(audio_dir, "dialogue-n4-4.mp3")

# Generate parts
files = []
for i, (voice, text) in enumerate(dialogue):
    filename = f"line_{i}.mp3"
    # Escaping quotes for Windows shell
    safe_text = text.replace('"', '\\"')
    cmd = f'python -m edge_tts --voice {voice} --text "{safe_text}" --rate=-10% --write-media {filename}'
    print(f"Generating {filename} with {voice}...")
    os.system(cmd)
    files.append(filename)

# Create concat list
with open("files.txt", "w", encoding="utf-8") as f:
    for filename in files:
        f.write(f"file '{filename}'\n")

# Concat with ffmpeg
print("Concatenating audio files...")
if os.path.exists(final_mp3):
    os.remove(final_mp3)
os.system(f"ffmpeg -f concat -safe 0 -i files.txt -c copy \"{final_mp3}\"")

# Clean up
print("Cleaning up temporary files...")
for filename in files:
    if os.path.exists(filename):
        os.remove(filename)
if os.path.exists("files.txt"):
    os.remove("files.txt")

print(f"Dialogue saved to {final_mp3}")
