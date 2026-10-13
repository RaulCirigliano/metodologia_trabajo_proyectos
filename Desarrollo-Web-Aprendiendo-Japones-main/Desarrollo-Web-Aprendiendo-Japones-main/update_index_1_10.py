import os

filepath = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

titles = {
    1: "Presentaciones y Ser/Estar",
    2: "Demostrativos (これ / それ / あれ)",
    3: "Lugares (ここ / そこ / あそこ)",
    4: "La Hora y Verbos Básicos",
    5: "Verbos de Movimiento",
    6: "Verbos Transitivos e Invitaciones",
    7: "Herramientas e Intercambio",
    8: "Adjetivos (Na / i)",
    9: "Gustos, Habilidades y Razones",
    10: "Existencia y Ubicación"
}

links_html = ""
for i in range(1, 11):
    links_html += f'''                <a href="lessons/lesson-{i}.html" target="main_frame" class="nav-link">
                    <span class="nav-num">{i}</span> {titles[i]}
                </a>\n'''

content = content.replace('<div class="coming-soon">Próximamente...</div>', links_html)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html with links for 1-10")
