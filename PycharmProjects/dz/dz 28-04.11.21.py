print('\033[96m' + '№3.32.a' + '\033[0m')
x = float(input("Введите x: "))
y = float(input("Введите y: "))
if y >= 1 and x <= -2:
    print("попал")
else:
    print("не попал")

print('\033[96m' + '№3.32.б' + '\033[0m')
x = float(input("Введите x: "))
y = float(input("Введите y: "))
if y <= 1.5 and y >= -2:
    print("попал")
else:
    print("не попал")

print('\033[96m' + '№3.32.в' + '\033[0m')
x = float(input("Введите x: "))
y = float(input("Введите y: "))
if y <= 4 and x >= 1 and x <= 2:
    print("попал")
else:
    print("не попал")

print('\033[96m' + '№3.32.г' + '\033[0m')
x = float(input("Введите x: "))
y = float(input("Введите y: "))
if y <= 4 and y >= 2 and x >= 1:
    print("попал")
else:
    print("не попал")

print('\033[96m' + '№4.2.' + '\033[0m')
from math import *
x = float(input('Введите y: '))
if x > 0:
    y = sin(x**2)
else:
    y = 1 + 2 * (sin(x)**2)
print(y)

print('\033[96m' + '№1.13.' + '\033[0m')
x = int(input('Введите x: '))
y = int(input('Введите y: '))
z = (x + ((2+y)/x**2)) / (y + (1/(x**2 + 10)**(1/2)))
print(z)


