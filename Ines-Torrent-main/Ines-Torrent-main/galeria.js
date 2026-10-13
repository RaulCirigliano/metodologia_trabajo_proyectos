document.addEventListener("DOMContentLoaded", () => {
const obrasInesTorrent = [


  // --- Obras extraídas de la sección de trabajos recientes ---
  { titulo: "2022 - 'Azules'", url: "imagenes/2022_azules.webp" },
  { titulo: "2022 - 'Azules'. Óleo sobre fibrofácil. 38 cm de diámetro.", url: "imagenes/2022_azules_oleo.webp" },
  { titulo: "2022 - 'Gelsomino'. Óleo sobre fibrofácil. 30 cm de diámetro.", url: "imagenes/2022_gelsomino.webp" },
  { titulo: "2022 - 'Gelsomino'. Óleo sobre fibrofácil. 30 cm de diámetro. Detalle.", url: "imagenes/2022_gelsomino_detalle_1.webp" },
  { titulo: "2022 - 'Gelsomino'. Óleo sobre fibrofácil. 30 cm de diámetro.", url: "imagenes/2022_gelsomino_oleo.webp" },
  { titulo: "2022 - 'Gelsomino'. Recorte con jazmín.", url: "imagenes/2022_gelsomino_recorte.webp" },
  { titulo: "2021-2023 - 'Árbol de fuego'. Óleo sobre tela. Detalle.", url: "imagenes/2021_2023_arbol_fuego_detalle.webp" },
  { titulo: "2021-2023 - 'Árbol de fuego'. Óleo sobre tela. 70 x 60 cm.", url: "imagenes/2021_2023_arbol_fuego.webp" },
  { titulo: "2019 - 'Café à Angelina Paris'. Óleo sobre fibrofácil. 50 x 60 cm.", url: "imagenes/2019_cafe_angelina.webp" },
  { titulo: "2018-2019 - 'Regalo con moño y todo'. Óleo sobre tela. 150 x 100 cm.", url: "imagenes/2018_19_regalo_mono.webp" },
  { titulo: "2015 - 'Tres otoños'. Óleo sobre fibrofácil. 27,2 x 100 cm.", url: "imagenes/2015_tres_otonos_1.webp" },
  { titulo: "2015 - 'Tres otoños'. Emplazado.", url: "imagenes/2015_tres_otonos_emplazado.webp" },
  { titulo: "2013 - 'Así son las cosas'. Óleo sobre hardboard. 65 x 68,5 cm. Boceto.", url: "imagenes/2013_asi_son_las_cosas_boceto.webp" },
  { titulo: "2013 - 'Así son las cosas'. Óleo sobre hardboard. 65 x 68,5 cm.", url: "imagenes/2013_asi_son_las_cosas_2.webp" },
  { titulo: "2013 - '¡Ay, nuestro peso!'. Detalle.", url: "imagenes/2013_ay_nuestro_peso_detalle_1.webp" },
  { titulo: "2013 - '¡Ay, nuestro peso!'. Detalle.", url: "imagenes/2013_ay_nuestro_peso_detalle_2.webp" },
  { titulo: "2013 - '¡Ay, nuestro peso!'. Óleo sobre tela. 140 x 31 cm.", url: "imagenes/2013_ay_nuestro_peso_1.webp" },
  { titulo: "2013 - '¡Ay, nuestro peso!'. Óleo sobre tela. 140 x 31 cm.", url: "imagenes/2013_ay_nuestro_peso_2.webp" },
  { titulo: "2013 - 'Zapallos de la ruta'. Óleo sobre tela. 50 x 70 cm.", url: "imagenes/2013_zapallos_ruta.webp" },
  { titulo: "2013 - 'La Falda'. Diámetro 26,5 cm. Colección particular.", url: "imagenes/2013_la_falda.webp" },
  { titulo: "2012 - 'La Planilla'. Óleo sobre tela. 100 x 150 cm.", url: "imagenes/2012_la_planilla.webp" },
  { titulo: "2012 - 'Acrobacia en tela'. Óleo sobre lienzo. 120 x 100 cm.", url: "imagenes/2012_acrobacia_tela.webp" },
  { titulo: "2010-2011 - 'Melisa y sus ángeles'.", url: "imagenes/2010_2011_melisa_angeles_1.webp" },
  { titulo: "2010-2011 - 'Melisa y sus ángeles'. Óleo sobre tela.", url: "imagenes/2010_2011_melisa_angeles_2.webp" },
  { titulo: "2010 - 'Perdí la cabeza'. Óleo sobre hardboard. 23,2 x 43 cm.", url: "imagenes/2010_perdi_la_cabeza.webp" },
  { titulo: "2010 - 'Mundial 2010'. Óleo sobre tela. 140 x 100 cm.", url: "imagenes/2010_mundial_2010.webp" },
  { titulo: "2010 - 'Mis pensamientos y yo'. Óleo sobre hardboard. 32 x 49,5 cm. Colección particular.", url: "imagenes/2010_mis_pensamientos.webp" },
  { titulo: "2010 - 'Giros de un ángel'. Óleo sobre tela. 70 x 60 cm.", url: "imagenes/2010_giros_angel_1.webp" },
  { titulo: "2010 - 'Giros de un ángel'. Óleo sobre tela. 60 x 70 cm. Motivo.", url: "imagenes/2010_giros_angel_motivo.webp" },
  { titulo: "2010 - 'Florencia por tres'. Óleo sobre fibrofácil. 22 x 60 cm.", url: "imagenes/2010_florencia_por_tres.webp" },
  { titulo: "2010 - 'En un sueño'. Detalle.", url: "imagenes/2010_en_un_sueno_detalle.webp" },
  { titulo: "2010 - 'En un sueño'. Colección particular. 50 x 60 cm.", url: "imagenes/2010_en_un_sueno.webp" },
  { titulo: "2009 - 'Spa'.", url: "imagenes/2009_spa_1.webp" },
  { titulo: "2009 - 'Spa'. Óleo sobre lienzo. 90 x 60 cm. Colección particular.", url: "imagenes/2009_spa_2.webp" },
  { titulo: "2009 - 'Spa'. Óleo sobre lienzo, colgado. 90 x 60 cm. Colección particular.", url: "imagenes/2009_spa_colgado.webp" },
  { titulo: "2007 - Croquis Puerto de Olivos. Óleo y collage.", url: "imagenes/2007_croquis_puerto_olivos.webp" },
  { titulo: "2006 - 'El triángulo blanco'. Óleo sobre tela. Bastidor de 30 x 30 cm.", url: "imagenes/2006_triangulo_blanco.webp" },
  { titulo: "2004 - 'Enredos y senderos'. Óleo sobre tela. 50 x 70 cm. Colección particular.", url: "imagenes/2004_enredos_y_senderos.webp" },
  { titulo: "2003 - 'Mundial 78'. Óleo sobre tela. 120 x 90 cm.", url: "imagenes/2003_mundial_78_1.webp" },
  { titulo: "2003 - 'Mundial 78'. Óleo sobre hardboard. 122 x 99 cm. Estudio preliminar. Colección particular.", url: "imagenes/2003_mundial_78_estudio.webp" },
  { titulo: "2002 - '¿Tomarías de esa sopa?'. Óleo sobre hardboard. 70 x 98 cm.", url: "imagenes/2002_tomarias_sopa.webp" },
  { titulo: "1998 - 'Remolcadores, Soledad Rua'. Óleo sobre hardboard. 69 x 88 cm. Colección particular.", url: "imagenes/1998_remolcadores.webp" },
  { titulo: "1996 - 'Enrique, Felipe y Alexis'. Óleo sobre hardboard. 63 x 46 cm.", url: "imagenes/1996_enrique_felipe_alexis_1.webp" },
  { titulo: "1995 - 'Dársena Sur'. Óleo sobre hardboard. Detalle.", url: "imagenes/1995_darsena_sur_detalle.webp" },
  { titulo: "1995 - 'Dársena Sur'. Óleo sobre hardboard. 48 x 66 cm.", url: "imagenes/1995_darsena_sur.webp" },
  { titulo: "1994 - Sin título.", url: "imagenes/1994_sin_titulo.webp" },
  { titulo: "1992 - 'El amor'. Óleo sobre hardboard. 74,5 x 89,7 cm. Colección particular.", url: "imagenes/1992_el_amor.webp" },
  { titulo: "1992 - 'La salida'. Óleo sobre hardboard. 55 x 40 cm. Colección particular.", url: "imagenes/1992_la_salida.webp" },
  { titulo: "1991 - 'El despegue'. Óleo sobre hardboard. Colección particular.", url: "imagenes/1991_el_despegue.webp" },
  { titulo: "1990 - Croquis Puerto de Olivos. Tintas.", url: "imagenes/1990_croquis_puerto_olivos.webp" },
  { titulo: "1990 - 'Tras un vidrio mojado'. Óleo sobre hardboard. 96 x 66 cm. Colección particular.", url: "imagenes/1990_vidrio_mojado.webp" },
  { titulo: "1990 - 'Mujer árbol'. Óleo sobre hardboard. Colección particular.", url: "imagenes/1990_mujer_arbol.webp" },
  { titulo: "1990 - 'Leonardo y La Gioconda'. Óleo sobre hardboard. 69 x 88 cm. Colección particular.", url: "imagenes/1990_leonardo_gioconda.webp" },
  { titulo: "1989 - 'Secuencia, Futuro, presente, pasado'. Óleo sobre hardboard. 100 x 60 cm.", url: "imagenes/1989_secuencia_futuro.webp" },
  { titulo: "1989 - 'Transparencias'. Óleo sobre hardboard. 52 x 33 cm. Colección particular.", url: "imagenes/1989_transparencias.webp" },
  { titulo: "1989 - 'Trama y urdimbre'. Óleo sobre hardboard. 32 x 21 cm. Colección particular.", url: "imagenes/1989_trama_urdimbre.webp" },
  { titulo: "1989 - 'Están o no están...'. Óleo sobre hardboard. Detalle.", url: "imagenes/1989_estan_o_no_estan_detalle.webp" },
  { titulo: "1989 - 'Están o no están...'. Óleo sobre hardboard. Colección particular.", url: "imagenes/1989_estan_o_no_estan.webp" },
  { titulo: "1989 - 'El barquito'.", url: "imagenes/1989_el_barquito_1.webp" },
  { titulo: "1989 - 'El barquito'. Óleo sobre hardboard. 67 x 84 cm. Colección particular.", url: "imagenes/1989_el_barquito_2.webp" },
  { titulo: "1988 - 'Encuentro'. Óleo sobre hardboard. 46 x 66 cm. Detalle.", url: "imagenes/1988_encuentro_detalle_1.webp" },
  { titulo: "1988 - 'Encuentro'. Óleo sobre hardboard. 46 x 66 cm. Detalle.", url: "imagenes/1988_encuentro_detalle_2.webp" },
  { titulo: "1988 - 'Encuentro'. Óleo sobre hardboard. 46 x 66 cm. Colección particular.", url: "imagenes/1988_encuentro.webp" },
  { titulo: "1988 - 'Color de eternidad'. Óleo sobre hardboard. 53 x 48 cm. Detalle.", url: "imagenes/1988_color_eternidad_detalle.webp" },
  { titulo: "1988 - 'Color de eternidad'. Óleo sobre hardboard. 53 x 48 cm.", url: "imagenes/1988_color_eternidad.webp" },
  { titulo: "1988 - Boceto para 'Color de eternidad'. Óleo sobre papel. 50 x 35 cm.", url: "imagenes/1988_boceto_color_eternidad.webp" },
  { titulo: "1987 - 'Nublado, Villa La Angostura'. Óleo sobre papel. 50 x 35 cm. Colección particular.", url: "imagenes/1987_nublado_angostura.webp" },
  { titulo: "1987 - 'Vitaminas'. Óleo sobre hardboard. Colección particular.", url: "imagenes/1987_vitaminas.webp" },
  { titulo: "1987 - 'Marzo'. Óleo sobre hardboard. 65 x 54,7 cm.", url: "imagenes/1987_marzo.webp" },
  { titulo: "1986 - 'Villa La Angostura'. Óleo sobre hardboard. 50 x 35 cm. Colección particular.", url: "imagenes/1986_villa_angostura.webp" },
  { titulo: "1986 - 'La ciudad'. Óleo sobre tela. 50 x 70 cm. Colección particular.", url: "imagenes/1986_la_ciudad.webp" },
  { titulo: "1984 - Personajes de teatro. Témpera sobre papel. 50 x 35 cm.", url: "imagenes/1984_personajes_teatro.webp" },
  { titulo: "1984 - Cabeza, escultura en cemento.", url: "imagenes/1984_cabeza_escultura.webp" },
  { titulo: "1984 - Autorretrato a lápiz. 50 x 35 cm.", url: "imagenes/1984_autorretrato.webp" },
  { titulo: "1983 - Retrato a pluma. Tinta china. 50 x 35 cm.", url: "imagenes/1983_retrato_pluma.webp" },
  { titulo: "1983 - Playa. Témpera sobre papel. 35 x 50 cm.", url: "imagenes/1983_playa.webp" },
  { titulo: "1982 - Estación de tren. Témpera sobre papel. 35 x 50 cm.", url: "imagenes/1982_estacion_tren.webp" },
  { titulo: "1981 - Collage técnica mixta. 35 x 50 cm.", url: "imagenes/1981_collage.webp" }
];

// Reordenar las obras cronológicamente (más recientes primero)
obrasInesTorrent.sort((a, b) => {
    const extraerAño = (titulo) => {
        const años = titulo.match(/\b(19|20)\d{2}\b/g);
        return años ? Math.max(...años.map(Number)) : 0;
    };
    return extraerAño(b.titulo) - extraerAño(a.titulo);
});

// --- Lógica del Carrusel Superior (solo para galeria.html) ---
const topCarouselSlides = document.getElementById('topCarouselSlides');
const topCarouselPrev = document.getElementById('topCarouselPrev');
const topCarouselNext = document.getElementById('topCarouselNext');
let topCarouselIndex = 0;

if (topCarouselSlides) {
    // 1. Poblar el carrusel con las mismas obras
    obrasInesTorrent.forEach(obra => {
        const slide = document.createElement('div');
        slide.className = 'top-carousel-slide';
        const img = document.createElement('img');
        img.src = obra.url;
        img.alt = obra.titulo;
        img.loading = 'lazy';
        slide.appendChild(img);
        topCarouselSlides.appendChild(slide);
    });

    // 2. Funcionalidad de los botones
    const moveTopCarousel = () => {
        topCarouselSlides.style.transform = `translateX(-${topCarouselIndex * 100}%)`;
    };

    topCarouselNext.addEventListener('click', () => {
        topCarouselIndex = (topCarouselIndex + 1) % obrasInesTorrent.length;
        moveTopCarousel();
    });

    topCarouselPrev.addEventListener('click', () => {
        topCarouselIndex = (topCarouselIndex - 1 + obrasInesTorrent.length) % obrasInesTorrent.length;
        moveTopCarousel();
    });
}

// Lógica de inyección en el DOM
const contenedor = document.getElementById('galleryContainer');
const modal = document.getElementById('imageModal');
const modalImg = document.getElementById('modalImg');
const modalCaption = document.getElementById('modalCaption');
let currentIndex = 0;

if (contenedor) {
    obrasInesTorrent.forEach((obra, index) => {
        const item = document.createElement('div');
        item.className = 'gallery-item';
        item.onclick = () => window.openModal(index);

        const imgWrap = document.createElement('div');
        imgWrap.className = 'image-wrapper';
        
        const img = document.createElement('img');
        img.src = obra.url;
        img.alt = obra.titulo;
        img.loading = 'lazy';

        const tituloDiv = document.createElement('div');
        tituloDiv.className = 'item-title';
        tituloDiv.textContent = obra.titulo;
        
        // Diagnóstico visual si la foto no se encuentra en tu PC
        img.onerror = () => {
            img.style.display = 'none';
            tituloDiv.innerHTML = `<span style="color:red; font-size:0.8rem; font-weight:bold;">Falta:<br>${obra.url}</span>`;
            
            // Crear caja de alerta global en la parte superior
            let alertBox = document.getElementById('errorAlert');
            if (!alertBox) {
                alertBox = document.createElement('div');
                alertBox.id = 'errorAlert';
                alertBox.style.cssText = "background: #ffebee; border: 2px solid #ef5350; color: #c62828; padding: 15px; margin-bottom: 20px; border-radius: 8px; font-family: sans-serif;";
                alertBox.innerHTML = "<strong>Faltan las siguientes imágenes en tu carpeta 'imagenes':</strong><ul id='errorList' style='margin: 10px 0 0; padding-left: 20px;'></ul>";
                contenedor.parentNode.insertBefore(alertBox, contenedor);
            }
            const li = document.createElement('li');
            li.textContent = obra.url;
            document.getElementById('errorList').appendChild(li);
        };

        imgWrap.appendChild(img);
        item.appendChild(imgWrap);
        item.appendChild(tituloDiv);
        contenedor.appendChild(item);
    });
}

window.openModal = function(index) {
    currentIndex = index;
    const obra = obrasInesTorrent[currentIndex];
    modalImg.src = obra.url;
    modalCaption.textContent = obra.titulo;
    modal.classList.add('show');
}

window.changeImage = function(step) {
    currentIndex += step;
    if (currentIndex >= obrasInesTorrent.length) {
        currentIndex = 0;
    } else if (currentIndex < 0) {
        currentIndex = obrasInesTorrent.length - 1;
    }
    const obra = obrasInesTorrent[currentIndex];
    modalImg.src = obra.url;
    modalCaption.textContent = obra.titulo;
}

window.closeModal = function() {
    modal.classList.remove('show');
    setTimeout(() => { modalImg.src = ""; }, 300);
}

window.onclick = function(event) {
    if (event.target == modal) {
        closeModal();
    }
}
});

   // Gallery filtering

        const filterButtons = document.querySelectorAll('.filter-btn');
        const galleryItems = document.querySelectorAll('.gallery-item');
        
        if (filterButtons.length && galleryItems.length) {
            filterButtons.forEach(button => {
                button.addEventListener('click', () => {
                    // Remove active class from all buttons
                    filterButtons.forEach(btn => btn.classList.remove('active'));
                    
                    // Add active class to clicked button
                    button.classList.add('active');
                    
                    const filter = button.getAttribute('data-filter');
                    
                    galleryItems.forEach(item => {
                        if (filter === 'all' || item.getAttribute('data-category') === filter) {
                            item.style.display = 'block';
                        } else {
                            item.style.display = 'none';
                        }
                    });
                });
            });
        }