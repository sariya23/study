data = [2, 6, 1];

% Построение круговой диаграммы
figure;
pie(data);

% Добавление легенды (по желанию)
legend('Группа 1', 'Группа 2', 'Группа 3');

% Добавление процентных значений (по желанию)
percent = 100 * data / sum(data);
labels = arrayfun(@(n) sprintf('%.1f%%', n), percent, 'UniformOutput', false);
text(1.2 * cosd(90 - cumsum(percent) - percent / 2), 1.2 * sind(90 - cumsum(percent) - percent / 2), labels);

% Заголовок
title('Круговая диаграмма данных');