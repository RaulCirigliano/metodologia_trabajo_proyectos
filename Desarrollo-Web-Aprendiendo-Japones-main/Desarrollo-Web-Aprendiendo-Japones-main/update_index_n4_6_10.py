import os

filepath = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

titles = {
    6: "Voluntad e Intención (~つもりです)",
    7: "Dar consejos y Probabilidades",
    8: "Imperativo y Citas Directas",
    9: "Hacer tal como... / Secuencias temporales",
    10: "Condicional (~ば)"
}

links_html = ""
for i in range(6, 11):
    links_html += f'''                        <a href="lessons/jlpt-n4-{i}.html" target="main_frame" class="nav-link">
                            <span class="nav-num">{i}</span> {titles[i]}
                        </a>\n'''

# Find the last link in the JLPT N4 section and insert after it.
target = '                            <span class="nav-num">5</span> Preparación previa (~て おきます)\n                        </a>\n'

new_content = content.replace(target, target + links_html)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Updated index.html with JLPT N4 links 6-10")
