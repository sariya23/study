figure;
x = linspace(-5, 5, 100); 

y = 10.^(x + 2);


semilogy(x, y);

title('График функции y = 10^(x + 2) в логарифмическом масштабе');
xlabel('x');
ylabel('y (в логарифмической шкале)');


grid on;