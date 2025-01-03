import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import Frame
from PIL import Image, ImageTk

def f(x, y):
    return (2 * x * ((x**2) + y) - 1)

def real(x):
    return (2 * np.exp((x**2)) - (x**2) - 1)

def f1(y1, y2):
    return (4 * y1 + y2 - np.exp(2))

def f2(y1, y2):
    return (-2 * y1 + y2)

def real_y1(x):
    return (x + 2) * np.exp(2*x) + np.exp(3*x)

def real_y2(x):
    return -2 * (1 + x) * np.exp(2* x) - np.exp(3*x)


def euler_method(f, x0, y0, h, xn):
    n = int((xn - x0) / h)
    x = np.linspace(x0, xn, n + 1)
    y = np.zeros(n + 1)
    y[0] = y0
    for i in range(n):
        y[i + 1] = y[i] + h * f(x[i], y[i])
    return x, y

def runge_kutta(f, x0, y0, h, xn):
    n = int((xn - x0) / h)
    x = np.linspace(x0, xn, n + 1)
    y = np.zeros(n + 1)
    y[0] = y0
    for i in range(n):
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + h / 2, y[i] + k1 / 2)
        k3 = h * f(x[i] + h / 2, y[i] + k2 / 2)
        k4 = h * f(x[i] + h, y[i] + k3)
        y[i + 1] = y[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return x, y

def euler_system(f1, f2, x0, y10, y20, h, xn):
    n = int((xn - x0) / h)
    x = np.linspace(x0, xn, n + 1)
    y1 = np.zeros(n + 1)
    y2 = np.zeros(n + 1)
    y1[0] = y10
    y2[0] = y20
    for i in range(n):
        y1[i + 1] = y1[i] + h * f1(y1[i], y2[i])
        y2[i + 1] = y2[i] + h * f2(y1[i], y2[i])
    return x, y1, y2

def runge_kutta_system(f1, f2, x0, y10, y20, h, xn):
    n = int((xn - x0) / h)
    x = np.linspace(x0, xn, n + 1)
    y1 = np.zeros(n + 1)
    y2 = np.zeros(n + 1)
    y1[0] = y10
    y2[0] = y20
    for i in range(n):
        k1_y1 = h * f1(y1[i], y2[i])
        k1_y2 = h * f2(y1[i], y2[i])
        
        k2_y1 = h * f1(y1[i] + 0.5 * k1_y1, y2[i] + 0.5 * k1_y2)
        k2_y2 = h * f2(y1[i] + 0.5 * k1_y1, y2[i] + 0.5 * k1_y2)
        
        k3_y1 = h * f1(y1[i] + 0.5 * k2_y1, y2[i] + 0.5 * k2_y2)
        k3_y2 = h * f2(y1[i] + 0.5 * k2_y1, y2[i] + 0.5 * k2_y2)
        
        k4_y1 = h * f1(y1[i] + k3_y1, y2[i] + k3_y2)
        k4_y2 = h * f2(y1[i] + k3_y1, y2[i] + k3_y2)
        
        y1[i + 1] = y1[i] + (k1_y1 + 2 * k2_y1 + 2 * k3_y1 + k4_y1) / 6
        y2[i + 1] = y2[i] + (k1_y2 + 2 * k2_y2 + 2 * k3_y2 + k4_y2) / 6
    return x, y1, y2

window = tk.Tk()
window.geometry('1300x550')
window.config(bg='lightblue')
window.title('Л/р №6 Мамаев Ростислав АА-23-07')

frame = Frame(window)
frame.pack(fill='both', expand=True)
frame.place(x=0, y=0)

fig = plt.Figure(figsize=(11, 5), dpi=75)


image1 = Image.open("task1.png")
photo1 = ImageTk.PhotoImage(image1)
label1 = tk.Label(window, image=photo1)
label1.place(x=900, y=25)


image3 = Image.open("usl1.jpg")
photo3 = ImageTk.PhotoImage(image3)
label3 = tk.Label(window, image=photo3)
label3.place(x=900, y=120)



x0 = 0
y0 = 1
h = 0.1
xn = 1
y10 = 3
y20 = -3

plot1 = fig.add_subplot(111)
x_euler, y_euler = euler_method(f, x0, y0, h, xn)
x_rk, y_rk = runge_kutta(f, x0, y0, h, xn)
x_exact = np.linspace(x0, xn, 11)
y_exact = real(x_exact)
plot1.plot(x_euler, y_euler, 'o-', label='Метод Эйлера')
plot1.plot(x_rk, y_rk, 's-', label='Метод Рунге-Кутта')
plot1.plot(x_exact, y_exact, '-', label='Точное решение')
plot1.set_xlabel('x')
plot1.set_ylabel('y')
plot1.legend()
plot1.set_title('ОДУ первого порядка')
plot1.grid(True)



canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.draw()
canvas.get_tk_widget().pack()



textr1 = tk.Label(window, text='Точное решение:', font=('Century Gothic', 14), background='lightgrey').place(x=25, y=400)
texteuler = tk.Label(window, text='Метод Эйлера:', font=('Century Gothic', 14), background='lightgrey').place(x=25, y=450)
textrenkut = tk.Label(window, text='Метод Рунге-Кутта:', font=('Century Gothic', 14), background='lightgrey').place(x=25, y=500)

y_real = []
for i in y_exact:
    y_real.append(round(i, 4))

y_euler_ins = []
for i in y_euler:
    y_euler_ins.append(round(i, 4))

y_rk_ins = []
for i in y_rk:
    y_rk_ins.append(round(i, 4))

r1ans = tk.Entry(window, font=('Century Gothic', 14))
r1ans.place(x=240, y=402, width=1000)
r1ans.insert(0, f'{y_real}')
reuler = tk.Entry(window, font=('Century Gothic', 14))
reuler.place(x=240, y=452, width=1000)
reuler.insert(0, f'{y_euler_ins}')
rrenkut = tk.Entry(window, font=('Century Gothic', 14))
rrenkut.place(x=240, y=502, width=1000)
rrenkut.insert(0, f'{y_rk_ins}')


window.mainloop()