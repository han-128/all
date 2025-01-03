n = 10;
a = 0;
b = 2*pi;
h = (b - a)/ 10;
x = a:h:b;
y = f(x);
subplot(2,3,1)
plot(x,y) 
grid on;
title('Точное решение');

disp('Коэффициенты для полинома 2 степени')
p_2 = polyfit(x, f(x), 2)
subplot(2,3,2)
plot(x, p_2(3) + p_2(2) .* x + p_2(1) * x .^ 2) 
grid on;
title('Полином 2 степени');


disp('Коэффициенты для полинома 3 степени')
p_3 = polyfit(x, f(x), 3)
subplot(2,3,3)
plot(x, p_3(4) + p_3(3) .* x + p_3(2) * x .^ 2 + p_3(1) * x .^ 3) 
grid on;
title('Полином 3 степени');
 

disp('Коэффициенты для полинома 4 степени')
p_4 = polyfit(x, f(x), 4)
subplot(2,3,4)
plot(x, p_4(5) + p_4(4) .* x + p_4(3) * x .^ 2 + p_4(2) * x .^ 3 + p_4(1) * x.^4)
grid on;
title('Полином 4 степени');


disp('Коэффициенты для полинома 5 степени')
p_5 = polyfit(x, f(x), 5)
subplot(2,3,5)
plot(x, p_5(6) + p_5(5) .* x + p_5(4) * x .^ 2 + p_5(3) * x .^ 3 + p_5(2) * x.^4 + p_5(1) * x.^5)
grid on;
title('Полином 5 степени');
