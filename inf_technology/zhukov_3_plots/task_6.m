figure;

theta = linspace(0, 2*pi, 1000); 

r = 2 + 5*cos(theta);

polarplot(theta, r);

title('График в полярных координатах: r = 2 + 5*cos(theta)');