import os
import re

directory = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\lessons"
scripts_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones"

# Pattern 1: HTML tags (h1)
# Match: <h1>Lección N5 - 1</h1>
# Replace: <h1>Examen para el JLPT5 - Lección 1</h1>
h1_pattern = re.compile(r'<h1>Lección N(\d+) - (\d+)</h1>')
title_pattern = re.compile(r'<title>Lección JLPT N(\d+) - (\d+)</title>')

# Update HTML files
for filename in os.listdir(directory):
    if filename.startswith("jlpt-n") and filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace h1
        new_content = h1_pattern.sub(r'<h1>Examen para el JLPT\1 - Lección \2</h1>', content)
        # Replace title
        new_content = title_pattern.sub(r'<title>Examen para el JLPT\1 - Lección \2</title>', new_content)
        
        if content != new_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated {filename}")

# Also update python generator scripts in the root
h1_script_pattern = re.compile(r'<h1>Lección N(\d+) - \{i\}</h1>')
title_script_pattern = re.compile(r'<title>Lección JLPT N(\d+) - \{i\}</title>')

for filename in os.listdir(scripts_dir):
    if filename.startswith("gen_") and filename.endswith(".py"):
        filepath = os.path.join(scripts_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        new_content = h1_script_pattern.sub(r'<h1>Examen para el JLPT\1 - Lección {i}</h1>', content)
        new_content = title_script_pattern.sub(r'<title>Examen para el JLPT\1 - Lección {i}</title>', new_content)
        
        # There might be some scripts that use generic format, e.g., <h1>Lección N{level} - {i}</h1>
        new_content = re.sub(r'<h1>Lección N\{level\} - \{i\}</h1>', r'<h1>Examen para el JLPT{level} - Lección {i}</h1>', new_content)
        new_content = re.sub(r'<title>Lección JLPT N\{level\} - \{i\}</title>', r'<title>Examen para el JLPT{level} - Lección {i}</title>', new_content)

        if content != new_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated script {filename}")

print("All titles updated successfully.")
