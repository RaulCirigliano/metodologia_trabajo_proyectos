import re

def check_css():
    file_path = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\css\style.css"
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    properties = ['transform', 'filter', 'perspective', 'will-change', 'contain', 'backdrop-filter']
    
    for match in re.finditer(r'([\.#a-zA-Z0-9_-]+)\s*{[^}]*}', content):
        selector = match.group(1)
        block = match.group(0)
        
        # Check if this selector is body, html, .app-body, .page-layout, etc.
        if selector in ['body', 'html', '.app-body', '.page-layout']:
            for prop in properties:
                if prop in block:
                    print(f"FOUND {prop} in {selector}!")

if __name__ == "__main__":
    check_css()
