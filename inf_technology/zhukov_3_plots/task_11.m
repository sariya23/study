data = [1, 2, 7; 4, 8, 12; 5, 19, 4];

figure;
bar(data, 'grouped');

xlabel('Группы данных');
ylabel('Значения');
title('Гистограмма данных');
legend('Группа 1', 'Группа 2', 'Группа 3');

grid on;