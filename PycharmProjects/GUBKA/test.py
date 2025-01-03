from numpy import *
from tkinter import *
import matplotlib.pyplot as plt

file_txt = open('test.txt', 'w')




def fx(x,y):
    return (1.6 - sin(y)) / (-2)


def fy(x, y):
    return 0.8 - cos(x + 0.5)

def f(x):
    return (2 * (abs(-2 * x))**(1/2) - 6)


def met_gaus(x0, y0, eps):
    k = 1
    x1 = fx(x0, y0)
    y1 = fy(x0, y0)
    while abs(x0 - x1) > eps or abs(y0 - y1) > eps:
        k += 1
        x0 = x1
        y0 = y1
        x1 = fx(x0, y0)
        y1 = fy(x1, y0)
    global kol_gaus
    kol_gaus = k
    otv = [round(x1, 5), round(y1, 5)]
    return otv

print(met_gaus(-10, 10, 0.01))

korni = [0, 0]

korni[0], korni[1] = met_gaus(-10, 10, 0.01)[0], met_gaus(-10, 10, 0.01)[1]

a, b = sort(korni)[0], sort(korni)[1] 

print(a, b)

print(sort(korni))


def simpson(a=korni[0], b=korni[1], n=30, h=1/30):
    sm = h / 3 * (f(a) + f(b))
    for i in range(1, n):
        sm += h / 3 * 2 * f(a + h * i) * (i % 2 + 1)

    return sm

print(simpson(korni[0], korni[1], 30, 1/30))

TTT = "otvet: " + str(round(simpson(korni[0], korni[1], 30, 1/30), 3))

file_txt.write(TTT)

file_txt.close

y = [0] * 10
x = [0] * 10

print(y)

for i in range(0, 10):
    x[i] = [i]
    y[i] = (2 * (abs(-2 * i))**(1/2) - 6)


print(x, y)

plt.grid(True)
plt.plot(x,y)
plt.show()



win = Tk()
win.geometry("1000x1000")
win.config(bg="cyan")
win.title("asd")
viv = Label(win, bg="lightgrey", text = TTT, font= "Times 100")
viv.place(x = 100, y = 100)
win.mainloop()



