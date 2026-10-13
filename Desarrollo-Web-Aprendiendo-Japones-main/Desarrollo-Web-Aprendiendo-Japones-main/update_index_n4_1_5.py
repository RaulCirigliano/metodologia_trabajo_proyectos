import os

filepath = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

titles = {
    1: "Explicar situaciones (~んです)",
    2: "Forma Potencial (Puedo hacer)",
    3: "Acciones simultáneas (~ながら)",
    4: "Lamentaciones y Finalización (~て しまいます)",
    5: "Preparación previa (~て おきます)"
}

links_html = ""
for i in range(1, 6):
    links_html += f'''                        <a href="lessons/jlpt-n4-{i}.html" target="main_frame" class="nav-link">
                            <span class="nav-num">{i}</span> {titles[i]}
                        </a>\n'''

# Find the JLPT N4 section placeholder and replace it
placeholder = '<summary class="book-summary">Preparación JLPT N4</summary>\n                    <div class="book-lessons">\n                        <div class="coming-soon">Próximamente...</div>\n                    </div>'
replacement = f'<summary class="book-summary">Preparación JLPT N4</summary>\n                    <div class="book-lessons">\n{links_html}                    </div>'

if placeholder in content:
    content = content.replace(placeholder, replacement)
else:
    print("Placeholder not found. It might have been already updated.")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html with JLPT N4 links 1-5")
