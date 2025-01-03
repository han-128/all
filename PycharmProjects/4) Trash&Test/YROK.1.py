"""
from math import *
n = -10
y = 10
x = 5
a = 7
b = 11

r = abs(n)
print(r)
r = 5 * cos(y)
print(r)
r= -7.5*a**2
print(r)
r = 3 * x**(1/2)
print(r)
r = sin(a)*cos(b) + cos(a)*sin(b)
print(r)
r = a*(2*b)**(1/2)
print(r)
r = 3*sin(2*a) * cos(3*b)
print(r)
r = -5 * (x + y**(1/2))**(1/2)
print(r)

"""
"""

age = int(input("введите ваш возрост"))
if age >= 18:
    if age >= 21:
        print("доступ открыт")
    else:
        print("доступ ограничен(")
else:
    print("в доступе отказано")

age = int(input("введите ваш возрост"))
if age >= 21:
    print("доступ открыт")
elif age >= 18:
        print("доступ открыт")
elif age >= 18:
        print("доступ открыт")

"""
"""

from math import sin
x = int(input("x = "))
if x > 0:
    y = sin(x)**2
else:
    y = 1 - 2*sin(x**2)
print(y)

"""
"""

http_code = "200"

match http_code:
    case "200":
        print("OK")
    case "404":
        print("Not Found")
    case "418":
        print("I'm a teapot")
    case "122":
        print("Code not found")

"""
"""

a = True
b = False
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)
print(a < b)
print(a and b)  # 1 * 0 = 0
print(a or b)  # 1 + 0 = 0
print(not a)
print(not b)

"""
"""

x = 1
y = -1
if(y >=  0 and x >=2) or (y <= -1 and x >= 1):
    print("попал")
else:
    print("не попал")

"""