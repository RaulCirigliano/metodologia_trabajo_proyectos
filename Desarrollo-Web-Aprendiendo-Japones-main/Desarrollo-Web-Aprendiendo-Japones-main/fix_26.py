import os
import re

filepath = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\lessons\lesson-26.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace <script> function playAudio with <script src="../js/main.js"></script>\n<script> function playAudio
if '<script src="../js/main.js"></script>' not in content:
    content = re.sub(r'<script>\s*function playAudio', '<script src="../js/main.js"></script>\n    <script>\n        function playAudio', content)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed lesson 26 script tag.")
else:
    print("Already fixed.")
