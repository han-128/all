a = input('Первая граница: ');
b = input('Вторая граница: ');
x2=a:0.1:b;
s = '-*m';
plot(x2,equation(x2),s)
grid on;

disp('Метод касательных')
x0 = input('Введите значение x0: ');
e = input('Введите значение точности e: ');
root = 100;
counter = 0;
while root == 100
    counter = counter +  1;
    x = x0 - (equation(x0) / derivative(x0));
    if abs(equation(x)) <= e
         root = x;
    else
         x0 = x;
    end
end
disp('Количество итераций: ')
disp(counter)
disp('Корень')
disp(root)

disp('Решение с помощью функции fzero')
f = @equation;
X = fzero(f,x0)

disp('Решение с помощью fsolve')
f = @equation;
fsolve(f ,[0],optimset('Display','on'))