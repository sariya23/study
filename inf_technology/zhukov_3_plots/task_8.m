figure;
x = linspace(-10, 10, 1000); 


y = tan(x) ./ x;


plot(x, y);


title('График функции y = tan(x)/x');
xlabel('x');
ylabel('y');


grid on;