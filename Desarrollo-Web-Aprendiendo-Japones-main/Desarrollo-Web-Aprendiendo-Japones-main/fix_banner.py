import os
import glob

base_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\lessons"
files = glob.glob(os.path.join(base_dir, "jlpt-n2-*.html"))

old_banner = '<div class="lesson-header-simple" style="background: linear-gradient(135deg, #1e293b 0%, #334155 100%); color: white; padding: 2rem; border-radius: 12px; margin-bottom: 2rem; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">'
new_banner = '<div class="lesson-header-simple" style="background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%); color: #0f172a; padding: 2rem; border-radius: 12px; margin-bottom: 2rem; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">'

old_span = '<span style="background: #e2e8f0; color: #1e293b;'
new_span = '<span style="background: #0284c7; color: #ffffff;'

old_h1 = '<h1 style="margin: 1rem 0; font-size: 2.2rem; font-weight: 800; letter-spacing: -0.5px;">'
new_h1 = '<h1 style="margin: 1rem 0; font-size: 2.2rem; font-weight: 800; letter-spacing: -0.5px; color: #0f172a;">'

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    content = content.replace(old_banner, new_banner)
    content = content.replace(old_span, new_span)
    content = content.replace(old_h1, new_h1)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
print("Banners actualizados en las 5 lecciones del N2.")
