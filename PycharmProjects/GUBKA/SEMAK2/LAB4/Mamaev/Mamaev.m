x = 0:0.001:1;
plot(x, f(x))
grid on;

disp('Решение с помощью функции trapz')
trapz(x, f(x))

disp('Решение с помощью функции quad')
quad(@f,0,1)

disp('Метод левых прямоугольников')
n = 30;
sm = 0;
h = 1/30;
for i = 0:n
    sm = sm + h * f(h * i);
end
disp(sm)   

disp('Абсолютная погрешность')
p = abs((2-2^(1/2)) - sm);
disp(p)

disp('Относительная погрешность в процентах')
p1 = p / (2-2^(1/2)) * 100;
disp(p1)