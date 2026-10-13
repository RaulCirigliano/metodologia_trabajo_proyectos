import os

filepath = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

titles = {
    11: "Contadores y Periodos de Tiempo",
    12: "Pasado de Adjetivos y Comparaciones",
    13: "Deseos (欲しい / ~たい) y Propósito de Ir",
    14: "La Forma TE, Peticiones y Progresivo",
    15: "Permiso, Prohibición y Estado (Forma TE)",
    16: "Secuencia de Acciones y Unión de Frases (Forma TE)",
    17: "Forma NAI (Negativa) y Obligaciones",
    18: "Forma Diccionario (Poder y Pasatiempos)",
    19: "Forma TA, Experiencias y Cambios",
    20: "Estilo Informal (Futsukei)",
    21: "Pensamientos, Citas y Confirmaciones",
    22: "Oraciones Modificadoras de Sustantivos",
    23: "Cuando (とき) e Inevitabilidad (と)",
    24: "Dar y Recibir (Favores y Acciones)",
    25: "Condicional ら y Aunque ても"
}

links_html = ""
for i in range(11, 26):
    links_html += f'''                <a href="lessons/lesson-{i}.html" target="main_frame" class="nav-link">
                    <span class="nav-num">{i}</span> {titles[i]}
                </a>\n'''

# We insert this right after the link for lesson 10.
target = '                    <span class="nav-num">10</span> Existencia y Ubicación\n                </a>'
new_content = content.replace(target, target + "\n" + links_html)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Updated index.html with links for 11-25")
