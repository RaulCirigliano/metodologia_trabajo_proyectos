import os
from bs4 import BeautifulSoup

def update_index():
    file_path = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\index.html"
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')

    # Update sidebar header to include close button
    sidebar = soup.find('aside', class_='sidebar-right')
    if sidebar:
        header_h2 = sidebar.find('h2')
        if header_h2 and not header_h2.find('button', class_='mobile-close-btn'):
            # Recreate header to include the close button and a container
            new_header = soup.new_tag('div')
            new_header['class'] = 'sidebar-header'
            
            h2_tag = soup.new_tag('h2')
            h2_tag.string = "Índice de Lecciones"
            
            close_btn = soup.new_tag('button')
            close_btn['class'] = 'mobile-close-btn'
            close_btn['id'] = 'mobileCloseBtn'
            close_btn.string = '✕'
            
            new_header.append(h2_tag)
            new_header.append(close_btn)
            
            header_h2.replace_with(new_header)

    # Theme mappings based on text
    themes = {
        "Minna no Nihongo I": "theme-minna1",
        "Minna no Nihongo II": "theme-minna2",
        "Preparación JLPT N5": "theme-n5",
        "Preparación JLPT N4": "theme-n4",
        "Preparación JLPT N3": "theme-n3",
        "Preparación JLPT N2": "theme-n2"
    }

    details_list = soup.find_all('details', class_='book-section')
    for details in details_list:
        summary = details.find('summary', class_='book-summary')
        if not summary:
            continue
            
        text = summary.get_text(strip=True).replace('▼', '').strip()
        
        # Add theme class
        for key, theme_class in themes.items():
            if key in text:
                classes = details.get('class', [])
                if theme_class not in classes:
                    classes.append(theme_class)
                details['class'] = classes
                break
                
        # Rebuild summary to include chevron properly
        summary.clear()
        span_text = soup.new_tag('span')
        span_text.string = text
        
        span_chevron = soup.new_tag('span')
        span_chevron['class'] = 'chevron'
        span_chevron.string = '▼'
        
        summary.append(span_text)
        summary.append(span_chevron)

    # Update the JS script
    script_tags = soup.find_all('script')
    for script in script_tags:
        if script.string and 'toggleSidebar' in script.string:
            script.string = """
        // Mobile Sidebar Toggle
        const mobileMenuBtn = document.getElementById('mobileMenuBtn');
        const mobileCloseBtn = document.getElementById('mobileCloseBtn');
        const sidebarRight = document.querySelector('.sidebar-right');
        const sidebarOverlay = document.getElementById('sidebarOverlay');
        const navLinks = document.querySelectorAll('.nav-link');

        function toggleSidebar() {
            sidebarRight.classList.toggle('active');
            sidebarOverlay.classList.toggle('active');
            // Lock/Unlock body scroll
            if (sidebarRight.classList.contains('active')) {
                document.body.style.overflow = 'hidden';
            } else {
                document.body.style.overflow = '';
            }
        }

        if (mobileMenuBtn && sidebarOverlay) {
            mobileMenuBtn.addEventListener('click', toggleSidebar);
            if (mobileCloseBtn) {
                mobileCloseBtn.addEventListener('click', toggleSidebar);
            }
            sidebarOverlay.addEventListener('click', toggleSidebar);
            
            // Close sidebar when a link is clicked on mobile
            navLinks.forEach(link => {
                link.addEventListener('click', () => {
                    if (window.innerWidth <= 768) {
                        sidebarRight.classList.remove('active');
                        sidebarOverlay.classList.remove('active');
                        document.body.style.overflow = '';
                    }
                });
            });
        }
    """

    # We must write it as string carefully. BeautifulSoup format might break `<script>` tags if not careful.
    # But for standard HTML5 it should be okay.
    # To be extremely safe, we will just use python string replacement instead of writing the whole soup.
    pass

# Safe string replacement approach
def update_index_safe():
    file_path = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\index.html"
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Header inside Sidebar
    if '<aside class="sidebar-right">\n            <h2>Índice de Lecciones</h2>' in content:
        new_header = '''<aside class="sidebar-right">
            <div class="sidebar-header">
                <h2>Índice de Lecciones</h2>
                <button class="mobile-close-btn" id="mobileCloseBtn">✕</button>
            </div>'''
        content = content.replace('<aside class="sidebar-right">\n            <h2>Índice de Lecciones</h2>', new_header)

    # 2. Update Details & Summaries
    themes = {
        "Minna no Nihongo I": "theme-minna1",
        "Minna no Nihongo II": "theme-minna2",
        "Preparación JLPT N5": "theme-n5",
        "Preparación JLPT N4": "theme-n4",
        "Preparación JLPT N3": "theme-n3",
        "Preparación JLPT N2": "theme-n2"
    }

    for text, theme in themes.items():
        old_tag = f'<details class="book-section">\n                    <summary class="book-summary">{text}</summary>'
        new_tag = f'<details class="book-section {theme}">\n                    <summary class="book-summary"><span>{text}</span> <span class="chevron">▼</span></summary>'
        content = content.replace(old_tag, new_tag)

    # 3. Update JS Script
    old_script_start = "// Mobile Sidebar Toggle"
    old_script_end = "</script>"
    
    if old_script_start in content:
        script_part1 = content.split(old_script_start)[0]
        script_part2 = content.split(old_script_start)[1].split(old_script_end)[1]
        
        new_script = """// Mobile Sidebar Toggle
        const mobileMenuBtn = document.getElementById('mobileMenuBtn');
        const mobileCloseBtn = document.getElementById('mobileCloseBtn');
        const sidebarRight = document.querySelector('.sidebar-right');
        const sidebarOverlay = document.getElementById('sidebarOverlay');
        const navLinks = document.querySelectorAll('.nav-link');

        function toggleSidebar() {
            sidebarRight.classList.toggle('active');
            sidebarOverlay.classList.toggle('active');
            if (sidebarRight.classList.contains('active')) {
                document.body.style.overflow = 'hidden';
            } else {
                document.body.style.overflow = '';
            }
        }

        if (mobileMenuBtn && sidebarOverlay) {
            mobileMenuBtn.addEventListener('click', toggleSidebar);
            if (mobileCloseBtn) {
                mobileCloseBtn.addEventListener('click', toggleSidebar);
            }
            sidebarOverlay.addEventListener('click', toggleSidebar);
            
            navLinks.forEach(link => {
                link.addEventListener('click', () => {
                    if (window.innerWidth <= 768) {
                        sidebarRight.classList.remove('active');
                        sidebarOverlay.classList.remove('active');
                        document.body.style.overflow = '';
                    }
                });
            });
        }
    """
        content = script_part1 + new_script + old_script_end + script_part2

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("index.html updated successfully.")

if __name__ == "__main__":
    update_index_safe()
