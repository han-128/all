// Добавляем обработчик событий для каждой секции
document.querySelectorAll('.section').forEach(section => {
    section.addEventListener('click', () => {
        // Переключаем класс 'active' для раскрытия/скрытия контента
        section.classList.toggle('active');
    });
});