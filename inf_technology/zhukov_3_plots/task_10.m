x_values = linspace(-pi, pi, 100);
num_frames = numel(x_values);

figure;
h = zeros(1, num_frames);
axis([-pi pi -10 10]);

for i = 1:num_frames
    x = x_values(i);
    y = cot(x); 

    if i == 1
        h(i) = plot(x, y, 'ro', 'MarkerSize', 8);
        xlabel('x');
        ylabel('y = cot(x)');
        title(['График функции y = cot(x) при x = ', num2str(x)]);
        grid on;
    else
        set(h(i), 'XData', x, 'YData', y);
        title(['График функции y = cot(x) при x = ', num2str(x)]);
    end

    pause(0.1);
end