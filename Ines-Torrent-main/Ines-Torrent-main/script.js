document.addEventListener("DOMContentLoaded", () => {
    
    // =========================================
    // LÓGICA DE LA NAVBAR
    // =========================================
    const header = document.querySelector('header');
    if (header) {
        const navHTML = `
            <nav>
                <button class="menu-toggle" aria-label="Abrir menú" aria-expanded="false">&#9776;</button>
                <ul class="nav-links">
                    <li><a href="index.html">Inicio</a></li>
                    <li><a href="sobre_mi.html">Sobre mi</a></li>
                    <li><a href="sobre_mi_obra.html">Sobre mi obra</a></li>
                    <li><a href="galeria.html">Galería</a></li>
                    <li><a href="carrusel.html">Carrusel</a></li>
                    <li><a href="ventas.html">Ventas</a></li>
                    <li><a href="contacto.html">Contacto</a></li>
                </ul>
            </nav>
        `;
        
        // En la página de inicio se inserta al final para respetar el logo en flexbox, en el resto al principio
        if (document.body.classList.contains('index-page')) {
            header.insertAdjacentHTML('beforeend', navHTML);
        } else {
            header.insertAdjacentHTML('afterbegin', navHTML);
        }

        // Resaltamos el enlace activo basado en la URL actual
        let currentPage = window.location.pathname.split('/').pop();
        if (currentPage === '') currentPage = 'index.html';
        
        const navLinks = header.querySelectorAll('nav a');
        navLinks.forEach(link => {
            if (link.getAttribute('href') === currentPage) {
                link.classList.add('active');
            }
        });

        // Lógica del menú hamburguesa en vista móvil
        const menuToggle = header.querySelector('.menu-toggle');
        const navUl = header.querySelector('.nav-links');
        
        if (menuToggle && navUl) {
            menuToggle.addEventListener('click', () => {
                const isExpanded = navUl.classList.toggle('show');
                menuToggle.setAttribute('aria-expanded', isExpanded);
                // Cambia el ícono de hamburguesa a la 'X' cuando está abierto
                menuToggle.innerHTML = isExpanded ? '&#10006;' : '&#9776;';
            });
        }
    }

    // =========================================
    // LÓGICA DEL FOOTER
    // =========================================
    let footer = document.querySelector('footer');
    if (!footer) {
        footer = document.createElement('footer');
        document.body.appendChild(footer);
    }
    footer.innerHTML = `
        <p>&copy; ${new Date().getFullYear()}. Todos los derechos reservados. | <a href="contacto.html">Contacto</a></p>
    `;

    // =========================================
    // LÓGICA DEL CARRUSEL (Sólo para index.html)
    // =========================================
    const carouselImages = document.getElementById('carouselImages');
    if (carouselImages) {
        let currentSlide = 0;
        const slides = document.querySelectorAll('.carousel-item');
        const totalSlides = slides.length;

        window.moveSlide = function(step) {
            slides[currentSlide].classList.remove('active');
            currentSlide += step;
            if (currentSlide >= totalSlides) {
                currentSlide = 0;
            } else if (currentSlide < 0) {
                currentSlide = totalSlides - 1;
            }
            slides[currentSlide].classList.add('active');
        }

        const prevBtn = document.querySelector('.carousel-btn.prev');
        const nextBtn = document.querySelector('.carousel-btn.next');

        document.addEventListener('mousemove', (e) => {
            if (e.clientX < window.innerWidth / 2) {
                if (prevBtn) prevBtn.style.opacity = '1';
                if (nextBtn) nextBtn.style.opacity = '0';
            } else {
                if (prevBtn) prevBtn.style.opacity = '0';
                if (nextBtn) nextBtn.style.opacity = '1';
            }
        });
    }

    // =========================================
    // LÓGICA DEL CARRUSEL 3D (carrusel.html)
    // =========================================
    const carousel3D = document.querySelector('.carousel-3d');
    if (carousel3D) {
        const slides3D = document.querySelectorAll('.slide-3d img');
        const modal3D = document.getElementById('image-modal');
        const modalImg3D = document.getElementById('image-modal-img');
        const closeBtn3D = document.getElementById('image-modal-close');
        const prevBtn3D = document.getElementById('image-modal-prev');
        const nextBtn3D = document.getElementById('image-modal-next');
        let current3DIndex = 0;

        function updateModal3D() {
            modalImg3D.src = slides3D[current3DIndex].src;
            modalImg3D.alt = slides3D[current3DIndex].alt;
        }

        // Abrir Modal con Clic
        slides3D.forEach((img, index) => {
            img.addEventListener('click', () => {
                current3DIndex = index;
                updateModal3D();
                modal3D.classList.add('show');
            });
        });

        // Navegación en Modal
        if (prevBtn3D) {
            prevBtn3D.addEventListener('click', (e) => {
                e.stopPropagation(); // Evita que el clic se propague al fondo y cierre el modal
                current3DIndex = (current3DIndex - 1 + slides3D.length) % slides3D.length;
                updateModal3D();
            });
        }

        if (nextBtn3D) {
            nextBtn3D.addEventListener('click', (e) => {
                e.stopPropagation(); // Evita que el clic se propague al fondo y cierre el modal
                current3DIndex = (current3DIndex + 1) % slides3D.length;
                updateModal3D();
            });
        }

        // Cerrar Modal (Botón y clic fuera)
        if (closeBtn3D) closeBtn3D.addEventListener('click', () => modal3D.classList.remove('show'));
        if (modal3D) {
            modal3D.addEventListener('click', (e) => {
                if (e.target === modal3D) {
                    modal3D.classList.remove('show');
                }
            });
        }
    }
});
