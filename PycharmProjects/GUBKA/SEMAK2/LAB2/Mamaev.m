ezplot('sin(x+1)-y-1',[-2, 2, -2, 2]),grid
hold on
ezplot('2*x+cos(y)-2',[-2, 2, -2, 2]),grid
axis tight
grid on;
f1 = @f1;
fsolve(f1, [-0.5,0.5])