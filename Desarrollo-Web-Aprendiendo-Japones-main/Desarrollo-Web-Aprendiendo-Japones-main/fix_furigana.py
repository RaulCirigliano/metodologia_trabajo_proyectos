import os
import re

filepath = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\lessons\lesson-4.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace <ruby>時<rt>とき</rt></ruby> with <ruby>時<rt>じ</rt></ruby>
old_ruby = "<ruby>時<rt>とき</rt></ruby>"
new_ruby = "<ruby>時<rt>じ</rt></ruby>"

count = content.count(old_ruby)
if count > 0:
    content = content.replace(old_ruby, new_ruby)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed {count} occurrences in Lesson 4.")
else:
    print("No occurrences found.")
