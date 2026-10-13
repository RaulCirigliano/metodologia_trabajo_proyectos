import os

seo_tags = """
    <!-- SEO Meta Tags -->
    <meta name="description" content="Compendio de estudio para revisar y tener una guia basado en el Minna no Nihongo y materiales de estudio para el JLPT.">
    <meta name="author" content="Raul Cirigliano">
    <meta name="keywords" content="Japonés, Minna no Nihongo, JLPT, N5, N4, N3, N2, aprender, gramática, vocabulario">
    <meta property="og:title" content="Aprendiendo Japonés - Raul Cirigliano">
    <meta property="og:description" content="Compendio de estudio para revisar y tener una guia basado en el Minna no Nihongo y materiales de estudio para el JLPT.">
    <meta property="og:type" content="website">
"""

def update_seo(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        if 'name="author"' in content or 'Raul Cirigliano' in content:
            return

        content = content.replace('</head>', seo_tags + '</head>')
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(file_path)}")
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

def main():
    root_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app"
    update_seo(os.path.join(root_dir, "index.html"))
    update_seo(os.path.join(root_dir, "welcome.html"))
    
    lessons_dir = os.path.join(root_dir, "lessons")
    for filename in os.listdir(lessons_dir):
        if filename.endswith(".html"):
            update_seo(os.path.join(lessons_dir, filename))

if __name__ == "__main__":
    main()
