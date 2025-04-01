function openPopup(headerText, label, ig_link, wa_link, radno_vreme, adresa) {
    document.getElementById('popup').style.display = 'flex';
    document.getElementById('popup-header').textContent = headerText;
    document.getElementById('popup-label1').textContent = label;
    document.getElementById('instalink').href = ig_link;
    document.getElementById('walink').href = wa_link;
    document.getElementById('radno_vreme').textContent = radno_vreme;
    document.getElementById('adresa').textContent = adresa;
}

function closePopup() {
    document.getElementById('popup').style.display = 'none';
}

function closePopupOutside(event) {
    const popupContent = document.querySelector(".popup-content");
    if (!popupContent.contains(event.target)) {
        closePopup();
    }
}

document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.accordion-header').forEach(header => {
        header.addEventListener('click', () => {
            const accordion = header.parentElement;
            const content = accordion.querySelector('.accordion-content');

            if (accordion.classList.contains('active')) {
                accordion.classList.remove('active');
                content.style.maxHeight = null;
            } else {
                // Close all other accordions
                document.querySelectorAll('.accordion').forEach(acc => {
                    acc.classList.remove('active');
                    acc.querySelector('.accordion-content').style.maxHeight = null;
                });

                accordion.classList.add('active');
                content.style.maxHeight = content.scrollHeight + 'px';
            }
        });
    });
});
