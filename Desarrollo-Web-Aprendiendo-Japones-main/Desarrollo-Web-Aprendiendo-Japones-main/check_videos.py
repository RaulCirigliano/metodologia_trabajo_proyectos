import os
import glob
import re

base_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\lessons"
files = glob.glob(os.path.join(base_dir, "*.html"))

for file in files[:5]: # just check a few
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # regex to find video section
    match = re.search(r'<h2[^>]*>.*?Video.*?</h2>\s*<p[^>]*>.*?</p>', content, re.IGNORECASE | re.DOTALL)
    if match:
        print(f"File: {os.path.basename(file)}")
        print(match.group(0))
        print("-" * 50)
