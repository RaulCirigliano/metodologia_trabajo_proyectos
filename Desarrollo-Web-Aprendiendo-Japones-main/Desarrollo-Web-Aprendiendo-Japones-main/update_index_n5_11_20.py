import os

filepath = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

titles = {
    11: "Partícula も (También) y Contadores N5",
    12: "Comparaciones N5 (より / ほうが)",
    13: "Deseos N5 (欲しい / ~たい)",
    14: "Verbos de Movimiento y Progresivo",
    15: "Permiso y Prohibición JLPT N5",
    16: "Secuencia de acciones y Adjetivos en forma TE",
    17: "Forma NAI y Obligaciones",
    18: "Forma Diccionario y Habilidades",
    19: "Forma TA, Experiencias y Cambios",
    20: "Estilo Informal N5 (Futsukei)"
}

links_html = ""
for i in range(11, 21):
    links_html += f'''                        <a href="lessons/jlpt-n5-{i}.html" target="main_frame" class="nav-link">
                            <span class="nav-num">{i}</span> {titles[i]}
                        </a>\n'''

# Find the last link in the JLPT N5 section and insert after it.
target = '                            <span class="nav-num">10</span> Conjunciones y Conectores JLPT N5\n                        </a>\n'

new_content = content.replace(target, target + links_html)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Updated index.html with JLPT N5 links 11-20")
