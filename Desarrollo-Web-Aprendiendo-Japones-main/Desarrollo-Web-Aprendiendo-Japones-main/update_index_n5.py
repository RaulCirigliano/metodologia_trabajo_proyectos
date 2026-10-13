import os

filepath = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

titles = {
    1: "Partículas Básicas (は, が, を)",
    2: "Partículas Direccionales y de Lugar (に, で, へ, と)",
    3: "Palabras Interrogativas (¿Qué, Dónde, Quién, Cuándo?)",
    4: "Números, Fechas y Horas",
    5: "Adjetivos Básicos y Colores (JLPT N5)",
    6: "Verbos Básicos (Afirmativo, Negativo, Pasado)",
    7: "Existencia (あります / います) y Posición",
    8: "Dar y Recibir básico (JLPT N5)",
    9: "Sugerencias e Invitaciones (ましょう / ませんか)",
    10: "Conjunciones y Conectores JLPT N5"
}

links_html = ""
for i in range(1, 11):
    links_html += f'''                        <a href="lessons/jlpt-n5-{i}.html" target="main_frame" class="nav-link">
                            <span class="nav-num">{i}</span> {titles[i]}
                        </a>\n'''

# Find the JLPT N5 section placeholder and replace it
placeholder = '<summary class="book-summary">Preparación JLPT N5</summary>\n                    <div class="book-lessons">\n                        <div class="coming-soon">Próximamente...</div>\n                    </div>'
replacement = f'<summary class="book-summary">Preparación JLPT N5</summary>\n                    <div class="book-lessons">\n{links_html}                    </div>'

content = content.replace(placeholder, replacement)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html with JLPT N5 links")
