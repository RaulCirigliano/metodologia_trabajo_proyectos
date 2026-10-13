// Loader: keep brand jolt visible briefly, then fade
window.addEventListener('load', () => {
  const loader = document.getElementById('loader');
  setTimeout(() => loader.classList.add('gone'), 750);
  setTimeout(() => loader.classList.add('hidden'), 1200);
});
// Fallback if 'load' is slow
setTimeout(() => {
  const loader = document.getElementById('loader');
  if (loader && !loader.classList.contains('hidden')) {
    loader.classList.add('gone');
    setTimeout(() => loader.classList.add('hidden'), 500);
  }
}, 1200);

// Reveal on scroll
const io = new IntersectionObserver((entries) => {
  entries.forEach((e) => {
    if (e.isIntersecting) {
      e.target.classList.add('in');
      io.unobserve(e.target);
    }
  });
}, { threshold: 0.08, rootMargin: '0px 0px -40px' });
document.querySelectorAll('.reveal').forEach((el) => io.observe(el));

// Menú de navegación móvil
const navToggle = document.querySelector('.nav-toggle');
const navLinksContainer = document.getElementById('nav-links');

navToggle.addEventListener('click', () => {
  document.body.classList.toggle('nav-open');
  const isExpanded = navToggle.getAttribute('aria-expanded') === 'true';
  navToggle.setAttribute('aria-expanded', !isExpanded);
});

// Cierra el menú al hacer clic en un enlace
navLinksContainer.addEventListener('click', (e) => {
  if (e.target.tagName === 'A') {
    document.body.classList.remove('nav-open');
    navToggle.setAttribute('aria-expanded', 'false');
  }
});

// Move sticky CTA when it overlaps the footer disclaimer
const stickyCta = document.querySelector('.sticky-cta');
const disclaimEl = document.querySelector('.disclaim');

if (stickyCta && disclaimEl) {
  const observer = new IntersectionObserver(
    ([entry]) => stickyCta.classList.toggle('is-at-bottom', entry.isIntersecting),
    { threshold: 0.1 }
  );
  observer.observe(disclaimEl);
}