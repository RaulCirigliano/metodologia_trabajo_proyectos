import os
import glob
import re

base_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\lessons"
files = glob.glob(os.path.join(base_dir, "*.html"))

modified_files = 0
for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    original_content = content
    
    # Reemplazar el título
    content = re.sub(
        r'(<h[23][^>]*>)[📺🎬]?\s*Clase en [Vv]ideo(</h[23]>)', 
        r'\1📺 Recomendación de Videos\2', 
        content,
        flags=re.IGNORECASE
    )
    
    # Reemplazar el subtítulo
    # Captura cualquier etiqueta <p> que contenga Kira Sensei o Nihongo no mori
    content = re.sub(
        r'<p([^>]*)>((?:(?!</p>).)*?(?:Kira Sensei|Nihongo no [Mm]ori)(?:(?!</p>).)*?)</p>',
        r'<p\1>Estudia este tema con esta lista de videos sugeridos. Inicia con el primero que aparezca.</p>',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )
    
    if content != original_content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        modified_files += 1
        print(f"Modificado: {os.path.basename(filepath)}")

print(f"Total de archivos modificados: {modified_files}")
