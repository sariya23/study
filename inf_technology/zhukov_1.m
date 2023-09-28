% Task 1%

result = 3.5 * ((0.027) ^ (1 / 3) - (10/7) ^ (-1)) / (-28/11);
disp(result);

result1 = (0.09) ^ 0.5 - (11 ^ 0.5 - 12 ^ 0.5) * (11 ^ 0.5 + 12 ^ 0.5);
disp(result1);

% Task 2 %
f = exp(2); 
format short; 
disp(f);

format long; 
disp(f);

format bank; 
disp(f);

format compact;
disp(f);

format loose; 
disp(f);

% Task 3 %

disp(realmin)

% Task 4 %

x = 8 + 5i;
y = complex(7, 0.8); 

sum_result = x + y;

diff_result = x - y;

prod_result = x * y;

conj_result1 = conj(x);

conj_result2 = real(x) - imag(x)*1i;

abs_x = abs(x);
abs_y = abs(y);

angle_x = angle(x);
angle_y = angle(y);

disp('Сумма:'); disp(sum_result);
disp('Разность:'); disp(diff_result);
disp('Произведение:'); disp(prod_result);
disp('Сопряженное (1 способ):'); disp(conj_result1);
disp('Сопряженное (2 способ):'); disp(conj_result2);
disp('Модуль x:'); disp(abs_x);
disp('Модуль y:'); disp(abs_y);
disp('Угол наклона x (радианы):'); disp(angle_x);
disp('Угол наклона y (радианы):'); disp(angle_y);

% Task 5 %
angle_rad = 7*pi/11;

cos_value = cos(angle_rad);
sin_value = sin(angle_rad);
tan_value = tan(angle_rad);
cot_value = 1/tan_value;
sec_value = 1/cos_value;
csc_value = 1/sin_value;

disp(['cos(7π/11) = ', num2str(cos_value)]);
disp(['sin(7π/11) = ', num2str(sin_value)]);
disp(['tan(7π/11) = ', num2str(tan_value)]);
disp(['cot(7π/11) = ', num2str(cot_value)]);
disp(['sec(7π/11) = ', num2str(sec_value)]);
disp(['csc(7π/11) = ', num2str(csc_value)]);

% Task 6 %
num1 = -1.1;
num2 = -1.5;
num3 = -1.8;

rounded1 = round([num1, num2, num3]); 
floored1 = floor([num1, num2, num3]);
ceiled1 = ceil([num1, num2, num3]); 

disp(['Округление до ближайшего целого: ', num2str(rounded1)]);
disp(['Округление вниз: ', num2str(floored1)]);
disp(['Округление вверх: ', num2str(ceiled1)]);

% Task 7 %
remainder = mod(-23, 4);
disp(['Остаток от деления -23 на 4: ', num2str(remainder)]);

% Task 8 %
num1 = 14;
num2 = 35;

gcd_result = gcd(num1, num2);

lcm_result = lcm(num1, num2);

disp(['НОД(14, 35) = ', num2str(gcd_result)]);
disp(['НОК(14, 35) = ', num2str(lcm_result)]);

% Task 9 %

save qq

% Task 10 % 

clear x y 
clear 

% Task 11 %

load qq

% Task 12 %

whos
who x*

% Task 13 %

diary('mydiary.m');
fprintf('a = cos(2 * pi);\n')
fprintf('b = cos(a);\n')
fprintf('c = sin(a);\n')
diary off;

% Task 14 %

type mydiary.m

