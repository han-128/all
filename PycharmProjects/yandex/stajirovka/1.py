from math import *
import tkinter as tk
import tkinter.messagebox as messagebox
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from tkinter import *

win = Tk()
win.geometry('950x450')
win.resizable(False, False)
win.config(bg="PaleGreen1")
win.title('Лабораторная работа №5 Зарипов Р.Р., 7 вариант')

data = [['2', '-', '-', '-'], ['3', '-', '-'], ['4', '-'], ['5']]
# Заданные данные
x = []
y = []
delta = (9 - 8) / 8
x0 = 8
while x0 < 9:
    x.append(x0)
    x0 += delta
for i in x:
    y.append((2*i+1)/(sqrt(i)))

x = np.array(x)
y = np.array(y)


# Функция для нахождения коэффициентов полинома МНК
def polynomial_approximation(x, y, degree):
    A = np.vander(x, degree + 1, increasing=True)
    coefficients = np.linalg.lstsq(A, y, rcond=None)[0]  # Решение методом наименьших квадратов
    return coefficients


# Аппроксимация полиномами разных степеней
degrees = [2, 3, 4, 5]
approximations = []

for degree in degrees:
    coefficients = polynomial_approximation(x, y, degree)
    approximations.append(coefficients)

for i in range(4):
    for j in range(len(approximations[i]) - 1, -1, -1):
        data[i].append(round(approximations[i][j], 3))

# Вычисление погрешностей
errors = []
for approximation in approximations:
    y_approximated = np.polyval(approximation, x)
    absolute_error = np.abs(y - y_approximated)
    relative_error = absolute_error / np.abs(y)
    errors.append((absolute_error, relative_error))

# Нахождение наилучшей аппроксимирующей функции
best_approximation_index = np.argmin(errors[-1][0])  # Выбираем аппроксимацию с наименьшей абсолютной погрешностью
best_approximation_degree = degrees[0]
best_approximation_coefficients = approximations[-1][best_approximation_index]

for i in range(4):
    a = str(round(sum(errors[i][1]) / len(errors[i][1]), 2)) + '%'
    data[i].append(a)


def best():
    messagebox.showinfo('Best function',"Наилучшая апроксимирующая функция: Cтепень"f" {best_approximation_degree}, т.к. имеет наименьшую погрешность")


# построение графика
fig = Figure(figsize=(6, 4))
ax = fig.add_subplot(111)
ax.plot(x, y, 'mo', label='Исходные данные')
for i, degree in enumerate(degrees):
    coefficients = approximations[i]
    y_approximated = np.polyval(coefficients, x)
    ax.plot(x, y_approximated, label=f'Степень {degree}')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Аппроксимация полиномами разных степеней')
ax.legend()
ax.title.set_text('График функции f(x) = |sin(x)| - |cos(x)|')
ax.grid(True)
ax.legend()
canvas1 = FigureCanvasTkAgg(fig, win)
canvas1.draw()
canvas1.get_tk_widget().place(x=300, y=20)


def tabl():
    fig, ax2 = plt.subplots(figsize=(14, 4))
    fig.patch.set_visible(False)
    fig.canvas.manager.set_window_title('Лабораторная работа №5 Зарипов Р.Р., 7 вариант')
    ax2.axis('off')
    ax2.axis('tight')
    table = ax2.table(cellText=data, loc='center',
                      colLabels=['Степень полинома', 'x^5', 'x^4', 'x^3', 'x^2', 'x', 'x^0', 'Средняя погрешность'],
                      colColours=["palegreen"] * 10,
                      cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1)
    fig.tight_layout()
    plt.show()


btn1 = tk.Button(win, text="Вывести полиномы", command=tabl)
btn1.place(x=30, y=100)

btn2 = tk.Button(win, text="Наилучшая функция", command=best)
btn2.place(x=30, y=250)
win.mainloop()
