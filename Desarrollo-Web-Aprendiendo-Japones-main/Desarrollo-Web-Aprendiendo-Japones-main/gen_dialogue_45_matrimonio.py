import os

dialogue = [
    ("ja-JP-NanamiNeural", "ちょっと、拓海！今日は掃除するって約束したのに、まだ寝てるの？"),
    ("ja-JP-KeitaNeural", "んー…ごめん。せっかくの休みなのに、疲れてて…"),
    ("ja-JP-NanamiNeural", "もう！あ、そういえば、洗濯機の調子が悪いんだけど。"),
    ("ja-JP-KeitaNeural", "え？壊れた場合は、すぐ修理を呼んだほうがいいよ。"),
    ("ja-JP-NanamiNeural", "呼びたいのに、今日は日曜日だから電話がつながらないのよ。"),
    ("ja-JP-KeitaNeural", "そっか。じゃあ、明日まで直らない場合は、コインランドリーに行こうか。")
]

audio_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\audio"
os.makedirs(audio_dir, exist_ok=True)

final_mp3 = os.path.join(audio_dir, "dialogue-matrimonio-45.mp3")

files = []
for i, (voice, text) in enumerate(dialogue):
    filename = f"line_{i}.mp3"
    safe_text = text.replace('"', '\\"')
    cmd = f'python -m edge_tts --voice {voice} --text "{safe_text}" --rate=-10% --write-media {filename}'
    os.system(cmd)
    files.append(filename)

with open("files.txt", "w", encoding="utf-8") as f:
    for filename in files:
        f.write(f"file '{filename}'\n")

if os.path.exists(final_mp3):
    os.remove(final_mp3)

os.system(f"ffmpeg -f concat -safe 0 -i files.txt -c copy \"{final_mp3}\"")

for filename in files:
    if os.path.exists(filename):
        os.remove(filename)
if os.path.exists("files.txt"):
    os.remove("files.txt")

print(f"Dialogue saved to {final_mp3}")
