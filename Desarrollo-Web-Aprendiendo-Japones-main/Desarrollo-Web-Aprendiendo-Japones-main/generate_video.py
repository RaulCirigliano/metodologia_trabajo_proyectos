import os
import subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter

examples = [
    ("疲れたときは、お風呂に入って寝るに限る。", "1. Cuando estás cansado, no hay nada como darse un baño y dormir.", "つかれたときは、おふろにはいってねるにかぎる"),
    ("風邪を引いたときは、温かいスープに限ります。", "2. Cuando tienes un resfriado, lo mejor es una sopa caliente.", "かぜをひいたときは、あたたかいスープにかぎります"),
    ("うちの子は、毎日ゲームばかりしている。", "3. Mi hijo no hace más que jugar videojuegos todos los días.", "うちのこは、まいにちゲームばかりしている"),
    ("彼女は文句ばかり言っている。", "4. Ella no hace más que quejarse (decir quejas).", "かのじょはもんくばかりいっている"),
    ("野菜を食べないで、肉ばかり食べてはだめですよ。", "5. No debes comer solo carne sin comer verduras.", "やさいをたべないで、にくばかりたべてはだめですよ"),
    ("このチケットは、本日のみ有効です。", "6. Este boleto es válido solamente por el día de hoy (Formal).", "このチケットは、ほんじつのみゆうこうです"),
    ("会員のみ入場できます。", "7. Solamente los miembros pueden ingresar.", "かいいんのみにゅうじょうできます"),
    ("休みの日は、家でゴロゴロするに限るね。", "8. En los días libres, no hay nada como holgazanear en casa.", "やすみのひは、いえでゴロゴロするにかぎるね"),
    ("甘いものばかり食べると、太りますよ。", "9. Si comes solamente cosas dulces, engordarás.", "あまいものばかりたべると、ふとりますよ"),
    ("カード払いは不可。現金のみとなります。", "10. No se puede pagar con tarjeta. Solamente efectivo.", "カードばらいはふか。げんきんのみとなります")
]

W, H = 1080, 1920

def wrap_text(text, font, max_width, draw):
    lines = []
    # Simplistic wrapper
    words = text.split()
    if not words:
        words = list(text)
    else:
        # If text contains mostly Japanese chars, treat char by char
        if any('\u3040' <= c <= '\u309F' or '\u30A0' <= c <= '\u30FF' or '\u4E00' <= c <= '\u9FFF' for c in text):
            words = list(text)
    
    current_line = ""
    for w in words:
        test_line = current_line + (" " if current_line and w not in list(text) else "") + w
        bbox = draw.textbbox((0,0), test_line, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = w
    if current_line:
        lines.append(current_line)
    return lines

try:
    font_jp = ImageFont.truetype("C:/Windows/Fonts/meiryo.ttc", 60)
    font_es = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 50)
    font_title = ImageFont.truetype("C:/Windows/Fonts/meiryo.ttc", 55) # Reducido para que no se desborde
except Exception as e:
    print("Fonts not found, trying defaults")
    font_jp = ImageFont.load_default()
    font_es = font_jp
    font_title = font_jp

# Background setup
try:
    bg_orig = Image.open(r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\img\fuji_sakura_header.jpg")
    bg_ratio = bg_orig.width / bg_orig.height
    target_ratio = W / H
    if bg_ratio > target_ratio:
        new_h = H
        new_w = int(new_h * bg_ratio)
        bg = bg_orig.resize((new_w, new_h), Image.LANCZOS)
        left = (new_w - W) // 2
        bg = bg.crop((left, 0, left + W, H))
    else:
        new_w = W
        new_h = int(new_w / bg_ratio)
        bg = bg_orig.resize((new_w, new_h), Image.LANCZOS)
        top = (new_h - H) // 2
        bg = bg.crop((0, top, W, top + H))
    
    bg = bg.point(lambda p: p * 0.4)
    bg = bg.filter(ImageFilter.GaussianBlur(8))
except Exception as e:
    print("Could not load background image, using solid color.")
    bg = Image.new("RGB", (W, H), "#1e293b")

out_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\video_gen"
os.makedirs(out_dir, exist_ok=True)

clips = []

print("Starting generation...")
for idx, (jp_text, es_text, read_text) in enumerate(examples):
    print(f"Processing example {idx+1}/{len(examples)}")
    
    img = bg.copy()
    draw = ImageDraw.Draw(img)
    
    # Título principal con wrap por si es muy largo
    title = "Examen para el JLPT3 - Lección 16"
    title_lines = wrap_text(title, font_title, 950, draw)
    y_title = 200
    for t_line in title_lines:
        t_bbox = draw.textbbox((0,0), t_line, font=font_title)
        draw.text(((W - (t_bbox[2]-t_bbox[0]))//2, y_title), t_line, font=font_title, fill="white")
        y_title += t_bbox[3] - t_bbox[1] + 10
        
    draw.line([(200, y_title + 30), (880, y_title + 30)], fill="#e0f2fe", width=4)
    
    # Decoración de título del tema (usando font_jp para que no salgan cuadrados en los kanjis)
    topic = "Limitaciones y Énfasis (~に限る / ~ばかり)"
    topic_lines = wrap_text(topic, font_jp, 950, draw)
    y_topic = y_title + 80
    for top_line in topic_lines:
        top_bbox = draw.textbbox((0,0), top_line, font=font_jp)
        draw.text(((W - (top_bbox[2]-top_bbox[0]))//2, y_topic), top_line, font=font_jp, fill="#93c5fd")
        y_topic += top_bbox[3] - top_bbox[1] + 10
    
    jp_lines = wrap_text(jp_text, font_jp, 900, draw)
    y_text = 750
    for line in jp_lines:
        bbox = draw.textbbox((0,0), line, font=font_jp)
        draw.text(((W - (bbox[2]-bbox[0]))//2, y_text), line, font=font_jp, fill="#fbbf24")
        y_text += bbox[3]-bbox[1] + 25
        
    y_text += 150
    es_lines = wrap_text(es_text, font_es, 900, draw)
    for line in es_lines:
        bbox = draw.textbbox((0,0), line, font=font_es)
        draw.text(((W - (bbox[2]-bbox[0]))//2, y_text), line, font=font_es, fill="#e2e8f0")
        y_text += bbox[3]-bbox[1] + 25
        
    img_path = os.path.join(out_dir, f"frame_{idx}.png")
    img.save(img_path)
    
    audio_path = os.path.join(out_dir, f"audio_{idx}.mp3")
    safe_text = read_text.replace('"', '\\"')
    cmd = f'python -m edge_tts --voice ja-JP-NanamiNeural --text "{safe_text}" --rate=-10% --write-media "{audio_path}"'
    subprocess.run(cmd, shell=True)
    
    # Generate video clip with 1.5 seconds of audio padding directly
    clip_path = os.path.join(out_dir, f"clip_{idx}.mp4")
    ffmpeg_cmd = f'ffmpeg -loop 1 -framerate 30 -i "{img_path}" -i "{audio_path}" -af "apad=pad_dur=1.5" -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest "{clip_path}" -y'
    subprocess.run(ffmpeg_cmd, shell=True)
    
    clips.append(clip_path)

list_path = os.path.join(out_dir, "concat_list.txt")
with open(list_path, "w", encoding="utf-8") as f:
    for c in clips:
        f.write(f"file '{os.path.basename(c)}'\n")

final_video = os.path.join(out_dir, "Video_Practica_N3_16.mp4")
concat_cmd = f'ffmpeg -f concat -safe 0 -i "{list_path}" -c copy "{final_video}" -y'
subprocess.run(concat_cmd, shell=True)

print(f"Video generated at: {final_video}")

# Cleanup
for idx in range(len(examples)):
    try:
        os.remove(os.path.join(out_dir, f"frame_{idx}.png"))
        os.remove(os.path.join(out_dir, f"audio_{idx}.mp3"))
        os.remove(os.path.join(out_dir, f"clip_{idx}.mp4"))
    except:
        pass
try:
    os.remove(list_path)
except:
    pass

print("Cleanup complete.")
