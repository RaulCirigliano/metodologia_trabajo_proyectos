import os

def update_css():
    css_path = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\css\style.css"
    with open(css_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Revert sidebar-right base
    old_sidebar = """/* Sidebar a la derecha (Ahora Menú a Pantalla Completa Desplegable hacia abajo) */
.sidebar-right {
    position: fixed;
    top: -100vh;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: white;
    display: flex;
    flex-direction: column;
    z-index: 200;
    transition: top 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
    overflow: hidden; /* Remove double scrolling */
}

.sidebar-right.active {
    top: 0;
}"""

    new_sidebar = """/* Sidebar a la derecha */
.sidebar-right {
    width: 320px;
    background: white;
    border-left: 1px solid #e2e8f0;
    display: flex;
    flex-direction: column;
    box-shadow: -5px 0 15px rgba(0,0,0,0.03);
    z-index: 5;
}"""
    if old_sidebar in content:
        content = content.replace(old_sidebar, new_sidebar)
    else:
        print("old_sidebar not found")

    # 2. Revert mobile-close-btn
    old_close = """.mobile-close-btn {
    display: block; /* Show always */"""
    new_close = """.mobile-close-btn {
    display: none;"""
    if old_close in content:
        content = content.replace(old_close, new_close)
    else:
        print("old_close not found")

    # 3. Revert mobile-menu-btn
    old_menu = """.mobile-menu-btn {
    display: block; /* Always visible */"""
    new_menu = """.mobile-menu-btn {
    display: none;"""
    if old_menu in content:
        content = content.replace(old_menu, new_menu)
    else:
        print("old_menu not found")

    # 4. Insert into media query
    media_query_start = "@media (max-width: 768px) {"
    if media_query_start in content:
        media_addons = """
    /* Show Hamburger Menu & Close Btn */
    .mobile-menu-btn, .mobile-close-btn {
        display: block;
    }

    /* Sidebar transforms into a full screen overlay menu sliding from top */
    .sidebar-right {
        position: fixed;
        top: -100vh;
        left: 0;
        width: 100vw;
        height: 100vh;
        max-width: 100vw;
        z-index: 200;
        transition: top 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
        overflow: hidden;
        border-left: none;
        box-shadow: none;
    }
    
    .sidebar-right.active {
        top: 0;
    }
"""
        content = content.replace(media_query_start, media_query_start + media_addons)
    else:
        print("media_query_start not found")

    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("CSS updated successfully.")

def update_js():
    html_path = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\index.html"
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

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
                    // Set active class visually
                    navLinks.forEach(l => l.classList.remove('active'));
                    link.classList.add('active');
                    
                    // Only close menu on mobile
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

        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("JS updated successfully.")

if __name__ == "__main__":
    update_css()
    update_js()
