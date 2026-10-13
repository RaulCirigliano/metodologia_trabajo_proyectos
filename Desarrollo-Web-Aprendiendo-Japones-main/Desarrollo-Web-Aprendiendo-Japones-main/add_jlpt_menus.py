import os

filepath = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

nav_end = '            </nav>'

jlpt_menus = '''
                <details class="book-section">
                    <summary class="book-summary">Preparación JLPT N5</summary>
                    <div class="book-lessons">
                        <div class="coming-soon">Próximamente...</div>
                    </div>
                </details>

                <details class="book-section">
                    <summary class="book-summary">Preparación JLPT N4</summary>
                    <div class="book-lessons">
                        <div class="coming-soon">Próximamente...</div>
                    </div>
                </details>

                <details class="book-section">
                    <summary class="book-summary">Preparación JLPT N3</summary>
                    <div class="book-lessons">
                        <div class="coming-soon">Próximamente...</div>
                    </div>
                </details>
            </nav>'''

if "JLPT N5" not in content:
    content = content.replace(nav_end, jlpt_menus)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added JLPT menus to index.html")
else:
    print("Already added")
