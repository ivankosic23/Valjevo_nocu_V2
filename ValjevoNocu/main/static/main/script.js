function openPopup(headerText, label, ig_link, wa_link) {
    document.getElementById('popup').style.display = 'block';
    document.getElementById('popup-header').textContent = headerText;
    document.getElementById('popup-label1').textContent = label;
    const ig=document.getElementById('instalink').href=ig_link;
    const wa=document.getElementById('walink').href=wa_link;
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
