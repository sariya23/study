figure;

x = linspace(0, 2*pi, 100);

y1 = cos(x); 
y2 = cos(x) + sin(x);


[ax, h1, h2] = plotyy(x, y1, x, y2);

set(h1, 'LineStyle', '-', 'Marker', 'o', 'MarkerSize', 6, 'Color', 'b', 'DisplayName', 'cos(x)');
set(h2, 'LineStyle', '--', 'Marker', 's', 'MarkerSize', 6, 'Color', 'r', 'DisplayName', 'cos(x) + sin(x)');

legend('Location', 'best');

title('Графики функций y1 = cos(x) и y2 = cos(x) + sin(x)');
xlabel('x');
ylabel(ax(1), 'y1 = cos(x)');
ylabel(ax(2), 'y2 = cos(x) + sin(x)');

grid on;