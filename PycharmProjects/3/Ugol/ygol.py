from math import *
import matplotlib.pyplot as plt

x = int(input('Что будет введено: 1. Два катета. 2. Катет и гипотенуза.  '))


match x:
    case 1:
        a = int(input('Введите длину первого катета: '))
        b = int(input('Введите длину второго катета: '))
        max_num = (a ** 2 + b ** 2) ** (1 / 2)
        ya = atan(a / b)
        ya2 = (ya * 180) / pi
        print(f'Угол лежащий между гипотенузой и первым катетом =  {round(ya2)}')
        yb = 90 - ya2
        print(f'Угол лежащий между гипотенузой и вторым катетом = {round(yb)}')
        print(f'Гипотенуза равна: {round(max_num)}')
    case 2:
        a = int(input('Введите длину катету: '))
        max_num = int(input('Введите длину гипотенузы: '))
        if max_num > a:
            ya = asin(a / max_num)
            ya2 = (ya * 180) / pi
            print(f'Угол лежащий между гипотенузой и неизвестным катетом равен: {round(ya2)}')
            yb = 90 - ya2
            print(f'Угол лежащий между гипотенузой и изветным катетом равен: {round(yb)}')
            b = ((max_num ** 2) - (a ** 2)) ** (1 / 2)
            print(f'Неизвестный катет равен: {round(b)}')
        else:
            print('Не правильно введены значения.')

plt.figure()
plt.plot([0, 0, b, 0], [0, a, 0, 0])
plt.show()
