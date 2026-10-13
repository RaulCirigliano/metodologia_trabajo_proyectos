import os

filepath = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

titles = {
    21: "Expresando Pensamientos y Citas",
    22: "Modificadores de Sustantivos N5",
    23: "Condiciones temporales (とき / と)",
    24: "Dar y Recibir acciones N5",
    25: "Condicionales N5 (たら / ても)"
}

links_html = ""
for i in range(21, 26):
    links_html += f'''                        <a href="lessons/jlpt-n5-{i}.html" target="main_frame" class="nav-link">
                            <span class="nav-num">{i}</span> {titles[i]}
                        </a>\n'''

# Find the last link in the JLPT N5 section and insert after it.
target = '                            <span class="nav-num">20</span> Estilo Informal N5 (Futsukei)\n                        </a>\n'

new_content = content.replace(target, target + links_html)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Updated index.html with JLPT N5 links 21-25")
