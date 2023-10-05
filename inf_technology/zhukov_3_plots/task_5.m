x = linspace(-10, 10, 1000);

y1 = cos(pi/6 - x);
y2 = tan(x) + cot(x);
y3 = sqrt(abs(abs(x) - 5));
y4 = sin(x).^2; 

subplot(2, 2, 1); 
plot(x, y1);
title('y1 = cos(pi/6 - x)');

subplot(2, 2, 2); 
plot(x, y2);
title('y2 = tan(x) + cot(x)');

subplot(2, 2, 3); 
plot(x, y3);
title('y3 = sqrt(| |x| - 5|)');

subplot(2, 2, 4);
plot(x, y4);
title('y4 = sin(x)^2');


sgtitle('Графики функций y1, y2, y3 и y4');

subplot(2, 2, 4);
plot(x, y4);
title('y4 = sin^2(x) - cos(x)');


sgtitle('Графики функций y1, y2, y3 и y4');