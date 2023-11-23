a = input('Enter coefficient a: ');
b = input('Enter coefficient b: ');
c = input('Enter coefficient c: ');
d = input('Enter coefficient d: ');

x = input('Enter the value of point x: ');

result = determine_polynomial_sign(a, b, c, d, x);
disp(['The sign of the polynomial at point x = ', num2str(x), ' is ', num2str(result)]);