document.addEventListener('DOMContentLoaded', () => {
    const navLinks = document.querySelectorAll('.nav-link');
    const pages = document.querySelectorAll('.page-content');
    const modeBtn = document.getElementById('mode-toggle');
    const modeIcon = document.getElementById('mode-icon');
    const filterBtns = document.querySelectorAll('[data-filter]');
    const projectCards = document.querySelectorAll('.project-card');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            filterBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');

            const filterValue = this.dataset.filter;
            projectCards.forEach(card => {
                if (filterValue === 'all' || card.dataset.category === filterValue) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });

    // Initialisation de l'icône si on est en mode sombre par défaut
    if (document.body.classList.contains('dark-mode')) {
        modeIcon.setAttribute('name', 'sunny-outline');
    }

    // Gestion de la navigation
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            const target = link.dataset.target;
            navLinks.forEach(l => l.classList.remove('active'));
            link.classList.add('active');
            pages.forEach(p => {
                p.classList.remove('active');
                if (p.id === target) p.classList.add('active');
            });
        });
    });

    // Gestion du basculement Mode Sombre / Clair
    modeBtn.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
        
        if (document.body.classList.contains('dark-mode')) {
            modeIcon.setAttribute('name', 'sunny-outline');
        } else {
            modeIcon.setAttribute('name', 'moon-outline');
        }
    });
});