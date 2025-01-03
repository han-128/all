clc
clear
disp('Вторая часть задания:')

f = @(x, y) [4 .* y(1) + y(2) - exp(2 .* x); -2 .* y(1) + y(2)];

x0 = 0;
y0 = [3; -3];

y1_exact = @(x) (2 + x) + exp(2 .* x) + exp(3 .* x);
y2_exact = @(x) -2 .* (1 + x) + exp(2 .* x) - exp(3 .* x);

h = 0.1;
n = 10;

x_v = zeros(1, n+1);
y_v = zeros(2, n+1);
x_v(1) = x0;
y_v(:, 1) = y0;

for i = 1:n
    y = y_v(:, i) + h * f(x_v(i), y_v(:, i));
    x = x_v(i) + h;
    x_v(i+1) = x;
    y_v(:, i+1) = y;
end

disp('Точные значения:')
x_e = x0:h:n*h
y1_e = y1_exact(x_e)
y2_e = y2_exact(x_e)
disp('Получившиеся результаты методом Эйлера:')
x_v
y_v

subplot(2, 1, 1);
plot(x_v, y_v(1, :), 'o-', x_e, y1_e, '--');
xlabel('x');
ylabel('y1');
title('Решение y1(x) методом Эйлера и точное решение');
legend('Численное решение', 'Точное решение');
grid on;

subplot(2, 1, 2);
plot(x_v, y_v(2, :), 'o-', x_e, y2_e, '--');
xlabel('x');
ylabel('y2');
title('Решение y2(x) методом Эйлера и точное решение');
legend('Численное решение', 'Точное решение');
grid on;
