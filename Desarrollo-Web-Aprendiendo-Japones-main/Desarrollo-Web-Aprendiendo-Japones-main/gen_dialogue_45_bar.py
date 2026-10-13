import os

dialogue = [
    ("ja-JP-KeitaNeural", "遅いよ！７時に来るって言ったのに！"),
    ("ja-JP-NanamiNeural", "ごめんごめん！実は、財布を忘れちゃって…"),
    ("ja-JP-KeitaNeural", "ええ！？財布を忘れた場合は、すぐ連絡してよ！"),
    ("ja-JP-NanamiNeural", "連絡したかったのに、スマホの充電も切れてたんだよ。"),
    ("ja-JP-KeitaNeural", "マジで？じゃあ、どうやってここまで来たの？"),
    ("ja-JP-NanamiNeural", "歩いてきたんだよ。１時間も歩いたのに、怒らないでよ〜。")
]

audio_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\audio"
os.makedirs(audio_dir, exist_ok=True)

final_mp3 = os.path.join(audio_dir, "dialogue-bar-45.mp3")

files = []
for i, (voice, text) in enumerate(dialogue):
    filename = f"line_bar_{i}.mp3"
    safe_text = text.replace('"', '\\"')
    cmd = f'python -m edge_tts --voice {voice} --text "{safe_text}" --rate=-10% --write-media {filename}'
    os.system(cmd)
    files.append(filename)

with open("files_bar.txt", "w", encoding="utf-8") as f:
    for filename in files:
        f.write(f"file '{filename}'\n")

if os.path.exists(final_mp3):
    os.remove(final_mp3)

os.system(f"ffmpeg -f concat -safe 0 -i files_bar.txt -c copy \"{final_mp3}\"")

for filename in files:
    if os.path.exists(filename):
        os.remove(filename)
if os.path.exists("files_bar.txt"):
    os.remove("files_bar.txt")

print(f"Dialogue saved to {final_mp3}")
