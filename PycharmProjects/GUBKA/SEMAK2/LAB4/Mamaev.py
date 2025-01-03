from tkinter import *
from PIL import Image, ImageTk
from math import *


def function(x):
    return (x/(4+(x**2)))


def left_rectangle(a, n, h):
    sm = 0
    for i in range(0, n):
        sm += h * function(a + h * i)
    return sm


def right_rectangle(a, n, h):
    sm = 0
    for i in range(1, n + 1):
        sm += h * function(a + h * i)
    return sm


def medium_rectangle(a, n, h):
    sm = 0
    for i in range(0, n):
        sm += h * function(a + h * i + h / 2)
    return sm


def trapezoid(a, b, n, h):
    sm = h * 0.5 * function(a) + h * 0.5 * function(b)
    for i in range(1, n):
        sm += h * function(a + h * i)
    return sm


def simpson(a, b, n, h):
    sm = h / 3 * (function(a) + function(b))
    for i in range(1, n):
        sm += h / 3 * 2 * function(a + h * i) * (i % 2 + 1)
    return sm


def left_rectangle_tab(x, y):
    sm = 0
    for i in range(0, len(x) - 1):
        sm += (abs(x[i] - x[i - 1])) * y[i]
    return sm


def right_rectangle_tab(x, y):
    sm = 0
    for i in range(1, len(x)):
        sm += (abs(x[i] - x[i - 1])) * y[i]
    return sm


def medium_rectangle_tab(x, y):
    sm = 0
    for i in range(0, len(x) - 1):
        sm += (abs(x[i] - x[i - 1])) * (abs(y[i] - y[i - 1]) * 0.5)
    return sm


def trapezoid_tab(x, y):
    sm = abs(x[1] - x[0]) * 0.5 * y[0] + abs(x[-1] - x[-2]) * 0.5 * y[-1]
    for i in range(1, len(x) - 1):
        sm += abs(x[i] - x[i - 1]) * y[i]
    return sm


def simpson_tab(x, y):
    sm = abs(x[1] - x[0]) / 3 * y[0] + abs(x[-1] - x[-2]) / 3 * y[-1]
    for i in range(1, len(x)):
        sm += abs(x[i] - x[i - 1]) / 3 * 2 * y[i] * (i % 2 + 1)
    return sm


win = Tk()
win.geometry('1200x600')
win.config(bg='hotpink1')
win.title("SaburovaAA2307Lab4")

#аналитически
# img = Image.open('уравнение.png')
# nimg = ImageTk.PhotoImage(img.resize((400, 100)))
# im = Label(win, image=nimg)
# im.place(x=6, y=6)

a, b, h = 0, 1, 1/30
n = 30

solution = (1/2) * log(5/4)
l = Label(win, text='Точное решение: ' + str('{:.5f}'.format(solution)), font='Times 14')
l.config(fg='purple4', bg='mediumpurple1')
l.place(x=6, y=150)

# Метод левых прямоугольников
sm = left_rectangle(a, n, h)
l1 = Label(win, text='Метод левых прямоугольников', font='Times 14')
l1.config(bg='mistyrose1', fg='mediumpurple1')
l1.place(x=6, y=180)
l2 = Label(win, text='Ответ: ' + str('{:.5f}'.format(sm)) + '  Невязка: ' + str('{:.5f}'.format(abs(solution - sm))),font='Times 14')
l2.config(fg='purple4', bg='mediumpurple1')
l2.place(x=6, y=205)

# Метод правых прямоугольников
sm1 = right_rectangle(a, n, h)
l3 = Label(win, text='Метод правых прямоугольников', font='Times 14')
l3.config(bg='mistyrose1', fg='mediumpurple1')
l3.place(x=6, y=235)
l4 = Label(win, text='Ответ: ' + str('{:.5f}'.format(sm1)) + '  Невязка: ' + str('{:.5f}'.format(abs(solution - sm1))), font='Times 14')
l4.config(fg='purple4', bg='mediumpurple1')
l4.place(x=6, y=260)

# Метод средних прямоугольников
sm2 = medium_rectangle(a, n, h)
l5 = Label(win, text='Метод средних прямоугольников', font='Times 14')
l5.config(bg='mistyrose1', fg='mediumpurple1')
l5.place(x=6, y=290)
l6 = Label(win, text='Ответ: ' + str('{:.5f}'.format(sm2)) + '  Невязка: ' + str('{:.5f}'.format(abs(solution - sm2))), font='Times 14')
l6.config(fg='purple4', bg='mediumpurple1')
l6.place(x=6, y=315)

# Метод трапеций
sm3 = trapezoid(a, b, n, h)
l7 = Label(win, text='Метод трапеций', font='Times 14')
l7.config(bg='mistyrose1', fg='mediumpurple1')
l7.place(x=6, y=345)
l8 = Label(win, text='Ответ: ' + str('{:.5f}'.format(sm3)) + '  Невязка: ' + str('{:.5f}'.format(abs(solution - sm3))), font='Times 14')
l8.config(fg='purple4', bg='mediumpurple1')
l8.place(x=6, y=370)

# Метод Симпсона
sm4 = simpson(a, b, n, h)
l7 = Label(win, text='Метод Симпсона', font='Times 14')
l7.config(bg='mistyrose1', fg='mediumpurple1')
l7.place(x=6, y=400)
l8 = Label(win, text='Ответ: ' + str('{:.5f}'.format(sm4))+ '  Невязка: ' + str('{:.5f}'.format(abs(solution - sm4))), font='Times 14')
l8.config(fg='purple4', bg='mediumpurple1')
l8.place(x=6, y=425)

# # Функция задана таблично
# img1 = Image.open('tablichn.png')
# nimg1 = ImageTk.PhotoImage(img1.resize((600, 100)))
# im1 = Label(win, image=nimg1)
# im1.place(x=500, y=6)

solution1 = pi
x = [0, 0.31, 0.63, 0.94, 1.26, 1.57, 1.88, 2.2, 2.51, 2.83, 3.14]
y = [0.5, 0.51, 0.54, 0.59, 0.67, 0.8, 0.98, 1.24, 1.55, 1.86, 2]
l9 = Label(win, text='Точное решение: ' + str('{:.5f}'.format(solution1)), font='Times 14')
l9.config(fg='purple', bg='orchid1')
l9.place(x=500, y=150)

# Метод левых прямоугольников
sm5 = left_rectangle_tab(x, y)
l10 = Label(win, text='Метод левых прямоугольников', font='Times 14')
l10.config(fg='orchid1', bg='mistyrose1')
l10.place(x=500, y=180)
l11 = Label(win, text='Ответ: ' + str('{:.5f}'.format(sm5))+ '  Невязка: ' + str('{:.5f}'.format(abs(solution1 - sm5))), font='Times 14')
l11.config(fg='purple', bg='orchid1')
l11.place(x=500, y=205)

# Метод правых прямоугольников
sm6 = right_rectangle_tab(x, y)
l12 = Label(win, text='Метод правых прямоугольников', font='Times 14')
l12.config(fg='orchid1', bg='mistyrose1')
l12.place(x=500, y=235)
l13 = Label(win, text='Ответ: ' + str('{:.5f}'.format(sm6)) + '  Невязка: ' + str('{:.5f}'.format(abs(solution1 - sm6))), font='Times 14')
l13.config(fg='purple', bg='orchid1')
l13.place(x=500, y=260)

# Метод средних прямоугольников
sm7 = medium_rectangle_tab(x, y)
l14 = Label(win, text='Метод средних прямоугольников', font='Times 14')
l14.config(fg='orchid1', bg='mistyrose1')
l14.place(x=500, y=290)
l15 = Label(win, text='Ответ: ' + str('{:.5f}'.format(sm7)) + '  Невязка: ' + str('{:.5f}'.format(abs(solution1 - sm7))), font='Times 14')
l15.config(fg='purple', bg='orchid1')
l15.place(x=500, y=315)

# Метод трапеций
sm8 = trapezoid_tab(x, y)
l16 = Label(win, text='Метод трапеций', font='Times 14')
l16.config(fg='orchid1', bg='mistyrose1')
l16.place(x=500, y=345)
l17 = Label(win, text='Ответ: ' + str('{:.5f}'.format(sm8)) + '  Невязка: ' + str('{:.5f}'.format(abs(solution1 - sm8))), font='Times 14')
l17.config(fg='purple', bg='orchid1')
l17.place(x=500, y=370)

# Метод Симпсона
sm9 = simpson_tab(x, y)
l18 = Label(win, text='Метод Симпсона', font='Times 14')
l18.config(fg='orchid1', bg='mistyrose1')
l18.place(x=500, y=400)
l19 = Label(win, text='Ответ: ' + str('{:.5f}'.format(sm9)) + '  Невязка: ' + str('{:.5f}'.format(abs(solution1 - sm9))), font='Times 14')
l19.config(fg='purple', bg='orchid1')
l19.place(x=500, y=425)

win.mainloop()