[x, y] = meshgrid(-5:0.1:5, -5:0.1:5);
z = sin(x) + tan(y);

figure;
subplot(2, 2, 1);
mesh(x, y, z);
title('График с использованием mesh');
xlabel('x');
ylabel('y');
zlabel('z');

subplot(2, 2, 2);
meshc(x, y, z);
title('График с контурами с использованием meshc');
xlabel('x');
ylabel('y');
zlabel('z');

subplot(2, 2, 3);
meshz(x, y, z);
title('График с размытыми контурами с использованием meshz');
xlabel('x');
ylabel('y');
zlabel('z');

subplot(2, 2, 4);
surf(x, y, z);
title('График с использованием surf');
xlabel('x');
ylabel('y');
zlabel('z');

axis tight;


set(gcf, 'Position', [100, 100, 800, 600]);
view(3); 