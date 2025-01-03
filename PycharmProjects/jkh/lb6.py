from math import *
from tkinter import *
import numpy as np
win = Tk()
win.geometry('800x1080')
win.configure(background='white')

img = PhotoImage(file="D:\PycharmProjects\4) Trash&Test\jkh\img.png")
label = Label(image=img)
label.pack()

def arr_create(n):
    arr = []
    for i in range(n):
        a = []
        for j in range(n):
            if i + j > 0:
                a.append((3*(i+1)+(abs(j-i))**0.25)**0.5)
            else:
                a.append(cos((i+1)*3.14/(j+1)+20.12))

        arr.append(a)


    return arr

def arr2(arr):
    result = sum( [sum(arr[i]) for i in range(len(arr))] )/(len(arr)*len(arr[0]))
    for i in range(len(arr)):
        arr[i][0],arr[i][3] = arr[i][3],arr[i][0]
    x = [arr[7][i] for i in range(len(arr))]
    for i in range(len(x)):
        x[i] = round(x[i],2)
    return result,arr, x

def xsort(x):
    for i in range(len(x)):
        for j in range(len(x)-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    for i in range(len(x)):
        x[i] = round(x[i],2)
    return x

def func1():
    s = 'исходная матрица\n'
    arr = arr_create(9)
    for i in range(9):
        for j in range(9):
            s+=f'{round(arr[i][j], 2)} '
        s +='\n'
    result, ar, x = arr2(arr)
    s+=f'среднее арифмитическое = {round(result, 3)}\nматрица после изменения\n'
    for i in range(9):
        for j in range(9):
            s+=f'{round(ar[i][j],2)} '
        s +='\n'
    s+=f'x = {x}\n'
    for i in range(len(x)):
        x[i] = round(x[i],2)

    x = xsort(x)
    s+=f'sorted x = {x}'
    label2.config(text=f'{s}')
    with open('lb6.txt', "w") as f:
        f.write(s)




button2 = Button(text='Решить',font=('Arial Black',13),background="#F0FFFF", command=func1)
button2.pack()
        
label2 = Label(font=('Arial Black',13),background="pink")
label2.pack()

win.mainloop()