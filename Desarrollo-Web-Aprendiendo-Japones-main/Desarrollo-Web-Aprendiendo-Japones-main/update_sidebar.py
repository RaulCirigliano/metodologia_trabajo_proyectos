import os

filepath = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Update header
content = content.replace('<h1>Minna no Nihongo II</h1>', '<h1>Minna no Nihongo (I y II)</h1>')
content = content.replace('<title>Estudio de Japonés - Minna no Nihongo II</title>', '<title>Estudio de Japonés - Minna no Nihongo</title>')

# Update nav
nav_start = '<nav class="lesson-nav">'
new_nav_start = '''<nav class="lesson-nav">
                <details class="book-section">
                    <summary class="book-summary">Minna no Nihongo I</summary>
                    <div class="book-lessons">
                        <div class="coming-soon">Próximamente...</div>
                    </div>
                </details>

                <details class="book-section" open>
                    <summary class="book-summary">Minna no Nihongo II</summary>
                    <div class="book-lessons">'''
content = content.replace(nav_start, new_nav_start)

nav_end = '            </nav>'
new_nav_end = '''                    </div>
                </details>
            </nav>'''
content = content.replace(nav_end, new_nav_end)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Index.html updated")
