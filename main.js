document.addEventListener('DOMContentLoaded', () => {
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabPanes = document.querySelectorAll('.tab-pane');

    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            tabBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const targetTab = btn.getAttribute('data-tab');
            tabPanes.forEach(pane => {
                pane.classList.toggle('active', pane.id === targetTab);
            });
        });
    });

    // File upload field update
    const fileInput = document.getElementById('video_file');
    const fileInfo = document.querySelector('.file-info');

    fileInput.addEventListener('change', () => {
        fileInfo.textContent = fileInput.files[0]?.name || 'No file selected';
    });
});