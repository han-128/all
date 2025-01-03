from math import *

fff = open("m.txt", "w")


def f(x):
    return (x/(4+(x**2)))

def l_pr(a, n, h):
    sm = 0
    for i in range(0, n):
        sm += h * f(a + h * i)
    return sm

def r_pr(a, n, h):
    sm = 0
    for i in range(1, n + 1):
        sm += h * f(a + h * i)
    return sm

def m_pr(a, n, h):
    sm = 0
    for i in range(n):
        sm += f(a + h * (i + 0.5)) #?
    return h * sm

def trap(a, b, n, h):
    sm =  (f(a) + f(b))* h * 0.5 #?
    for i in range(1, n):
        sm += h * f(a + h * i)
    return sm

def simpson(a, b, n, h):
    sm = h / 3 * (f(a) + f(b))
    for i in range(1, n):
        sm += h / 3 * 2 * f(a + h * i) * (i % 2 + 1)
    return sm





def l_tab(x, y):
    sm = 0
    for i in range(1, len(x)):
        sm += (abs(x[i] - x[i - 1])) * y[i-1]
    return sm

def r_tab(x, y):
    sm = 0
    for i in range(1, len(x)):
        sm += (abs(x[i] - x[i - 1])) * y[i]
    return sm

def m_tab(x, y):
    sm = (abs(x[1] - x[0])) * (abs(y[0] + y[-1]) * 0.5)
    for i in range(1, len(x) - 1):
        sm += (abs(x[i] - x[i - 1])) * (abs(y[i] + y[i - 1]) * 0.5)
    return sm

def trap_tab(x, y):
    sm = abs(x[1] - x[0]) * 0.5 * y[0] + abs(x[-1] - x[-2]) * 0.5 * y[-1]
    for i in range(1, len(x) - 1):
        sm += abs(x[i] - x[i - 1]) * y[i]
    return sm

def simpson_tab(x, y):
    sm = abs(x[1] - x[0]) / 3 * y[0] + abs(x[-1] - x[-2]) / 3 * y[-1]
    for i in range(1, len(x)):
        sm += abs(x[i] - x[i - 1]) / 3 * 2 * y[i] * (i % 2 + 1)
    return sm


a, b, h = 0, 1, 1/30
n = 30

solution = (1/2) * log(5/4)
print("tochnor resh", solution)


# Метод левых прямоугольников
sm = l_pr(a, n, h)
print("lev pryamoug", sm)

# Метод правых прямоугольников
sm1 = r_pr(a, n, h)
print("prav pryamoug", sm1)

# Метод средних прямоугольников
sm2 = m_pr(a, n, h)
print("sred pryamoug", sm2)

# Метод трапеций
sm3 = trap(a, b, n, h)
print("trapec", sm3)

# Метод Симпсона
sm4 = simpson(a, b, n, h)
print("simpson", sm4)



solution1 = pi
x = [0, 0.31, 0.63, 0.94, 1.26, 1.57, 1.88, 2.2, 2.51, 2.83, 3.14]
y = [0.5, 0.51, 0.54, 0.59, 0.67, 0.8, 0.98, 1.24, 1.55, 1.86, 2]
print("tochnor resh", solution1)

# Метод левых прямоугольников
sm5 = l_tab(x, y)
print("lev pryamoug", sm5)

# Метод правых прямоугольников
sm6 = r_tab(x, y)
print("prav pryamoug", sm6)
fff.write("Метод правых прямоугольников: "+ str(sm6)[:5] + "\n")


# Метод средних прямоугольников
sm7 = m_tab(x, y)
print("sred pryamoug", sm7)

# Метод трапеций
sm8 = trap_tab(x, y)
print("trapec", sm8)

# Метод Симпсона
sm9 = simpson_tab(x, y)
print("simpson", sm9)

fff.write("Метод Симпсона: "+ str(sm9)[:5])


fff.close()