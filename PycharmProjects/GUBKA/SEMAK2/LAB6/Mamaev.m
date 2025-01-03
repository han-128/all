clc
clear

f = @(x, y) (2 .* x .* (x .* x + 1));
a_s = @(x) (2 .* exp(x .* x) - (x .* x) - 1);

h = 0.1;
n = 8;

x_v = [0, 0.1];
y_v = [0,0.3];

for i = 2:n+1
    k1 = h/2 * f(x_v(i), y_v(i));
    k2 = h/2 * f(x_v(i) + 0.5 * h, y_v(i) + k1);
    k3 = h * f(x_v(i) + 0.5 * h, y_v(i) + k2);
    k4 = h * f(x_v(i) + h, y_v(i) + k3);
    
    y = y_v(i) + (k1 + 2*k2 + k3 + k4/2) / 3;
    x_v(i+1) = x_v(i) + h;
    y_v(i+1) = y;
end

x_v
y_v

x_a = x_v
y_a = a_s(x_v)

plot(x_v, y_v, 'o-', 'DisplayName', 'Рунге-Кутт');
hold on

plot(x_a, y_a, '--', 'DisplayName', 'Аналитическое решение');
hold off
xlabel('x');
ylabel('y');

title('Решение дифференциального уравнения и аналитическое решение');
legend;
grid on;

