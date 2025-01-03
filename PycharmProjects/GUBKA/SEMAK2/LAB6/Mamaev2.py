import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import Frame
from PIL import Image, ImageTk

def f(x, y):
    return (2 * x * ((x**2) + y) - y)

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

# def adams_method(f, x0, y0, h, xn):
#     n = int((xn - x0) / h)
#     y = np.zeros(n + 1)
#     y[0] = y0
#     for i in range(1, 4):
#         k1 = f(y[i-1], x0[i-1])
#         k2 = f(y[i-1] + 0.5*h*k1, x0[i-1] + 0.5*h)
#         k3 = f(y[i-1] + 0.5*h*k2, x0[i-1] + 0.5*h)
#         k4 = f(y[i-1] + h*k3, x0[i-1] + h)
#         y[i] = y[i-1] + h*(k1 + 2*k2 + 2*k3 + k4)/6
#     for i in range(4, n):
#         y[i] = y[i-1] + h*(55*f(y[i-1], x[i-1]) - 59*f(y[i-2], x0[i-2]) + 37*f(y[i-3], x0[i-3]) - 9*f(y[i-4], x0[i-4])) / 24

#     return x, y

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
window.geometry('1600x700')
window.config(bg='lightblue')
window.title('Л/р №6 Мамаев Ростислав АА-23-07')

frame = Frame(window)
frame.pack(fill='both', expand=True)
frame.place(x=0, y=0)

fig = plt.Figure(figsize=(11, 5), dpi=75)


image2 = Image.open("task2.png")
photo2 = ImageTk.PhotoImage(image2)
label2 = tk.Label(window, image=photo2)
label2.place(x=900, y=25)

image4 = Image.open("usl2.jpg")
photo4 = ImageTk.PhotoImage(image4)
label4 = tk.Label(window, image=photo4)
label4.place(x=900, y=250)

x0 = 0
y0 = 1
h = 0.1
xn = 1
y10 = 3
y20 = -3


x_euler, y_euler = euler_method(f, x0, y0, h, xn)
x_rk, y_rk = runge_kutta(f, x0, y0, h, xn)
x_exact = np.linspace(x0, xn, 11)
y_exact = real(x_exact)
plot2 = fig.add_subplot(111)
x_euler_sys, y1_euler, y2_euler = euler_system(f1, f2, x0, y10, y20, h, xn)
x_rk4_sys, y1_rk4, y2_rk4 = runge_kutta_system(f1, f2, x0, y10, y20, h, xn)
y1_exact_sys = real_y1(x_exact)
y2_exact_sys = real_y2(x_exact)

plot2.plot(x_euler_sys, y1_euler, 'o-', label='Метод Эйлера y1')
plot2.plot(x_rk4_sys, y1_rk4, 's-', label='Метод Рунге-Кутта y1')
plot2.plot(x_exact, y1_exact_sys, '-', label='Точное решение y1')
plot2.plot(x_euler_sys, y2_euler, 'o--', label='Метод Эйлера y2')
plot2.plot(x_rk4_sys, y2_rk4, 's--', label='Метод Рунге-Кутта y2')
plot2.plot(x_exact, y2_exact_sys, '--', label='Точное решение y2')
plot2.set_xlabel('x')
plot2.set_ylabel('y')
plot2.legend()
plot2.set_title('Система ОДУ первого порядка')
plot2.grid(True)

canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.draw()
canvas.get_tk_widget().pack()

textrsys = tk.Label(window, text='Точное решение Y1:', font=('Century Gothic', 14), background='lightgrey').place(x=25, y=400)
textrsys = tk.Label(window, text='Точное решение Y2:', font=('Century Gothic', 14), background='lightgrey').place(x=25, y=450)
texteulersys = tk.Label(window, text='Метод Эйлера Y1:', font=('Century Gothic', 14), background='lightgrey').place(x=25, y=500)
texteulersys = tk.Label(window, text='Метод Эйлера Y2:', font=('Century Gothic', 14), background='lightgrey').place(x=25, y=550)
textrenkutsys = tk.Label(window, text='Метод Рунге-Кутта Y1:', font=('Century Gothic', 14), background='lightgrey').place(x=25, y=600)
textrenkutsys = tk.Label(window, text='Метод Рунге-Кутта Y2:', font=('Century Gothic', 14), background='lightgrey').place(x=25, y=650)

y1_exact_sys_ans = []
for i in y1_exact_sys:
    y1_exact_sys_ans.append(round(i, 4))

y2_exact_sys_ans = []
for i in y2_exact_sys:
    y2_exact_sys_ans.append(round(i, 4))

y1_euler_ans = []
for i in y1_euler:
    y1_euler_ans.append(round(i, 4))

y2_euler_ans = []
for i in y2_euler:
    y2_euler_ans.append(round(i, 4))

y1_rk4_ans = []
for i in y1_rk4:
    y1_rk4_ans.append(round(i, 4))

y2_rk4_ans = []
for i in y2_rk4:
    y2_rk4_ans.append(round(i, 4))

rsysansy1 = tk.Entry(window, font=('Century Gothic', 14))
rsysansy1.place(x=240, y=400, width=1000)
rsysansy1.insert(0, f'{y1_exact_sys_ans}')
rsysansy2 = tk.Entry(window, font=('Century Gothic', 14))
rsysansy2.place(x=240, y=450, width=1000)
rsysansy2.insert(0, f'{y2_exact_sys_ans}')
eulersysansy1 = tk.Entry(window, font=('Century Gothic', 14))
eulersysansy1.place(x=240, y=500, width=1000)
eulersysansy1.insert(0, f'{y1_euler_ans}')
eulersysansy2 = tk.Entry(window, font=('Century Gothic', 14))
eulersysansy2.place(x=240, y=550, width=1000)
eulersysansy2.insert(0, f'{y2_euler_ans}')
renkutsysansy1 = tk.Entry(window, font=('Century Gothic', 14))
renkutsysansy1.place(x=240, y=600, width=1000)
renkutsysansy1.insert(0, f'{y1_rk4_ans}')
renkutsysansy2 = tk.Entry(window, font=('Century Gothic', 14))
renkutsysansy2.place(x=240, y=650, width=1000)
renkutsysansy2.insert(0, f'{y2_rk4_ans}')

window.mainloop()