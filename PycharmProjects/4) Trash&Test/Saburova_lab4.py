from scipy.optimize import *
from tkinter import *

obj=[-1, -1, -1, -1]

lhs_eq=[[ 3, 2, 5, 1],[ 2, 5, 4, 1],[ 3, 4, 5, 1]]
rhs_eq =[22,24,26]

opt= linprog(c=obj,A_eq=lhs_eq, b_eq=rhs_eq, method="simplex")

root = Tk()
root.geometry('1100x350')
root.resizable(0,0)
root.title('Saburova Lab_4')
img1 = PhotoImage(file = "var_22.png")
im1 = Label(image = img1,padx=20)
im1.grid(row=1,column=2,columnspan=3,rowspan=4,pady=(20,0))

Label(text='Найденный ответ', font='Arial 15 bold',padx=10, pady=10).grid(row=2,column=0,sticky=W)
Label(text='При переменных равных: ', font='Arial 15 bold',padx=10, pady=10).grid(row=3,column=0,sticky=W)
Label(text='Количество итераций', font='Arial 15 bold',padx=10, pady=10).grid(row=4,column=0,sticky=W)

f1=Entry(font='Arial 13 bold',width=15, state='readonly')
f1.grid(row=2,column=1,sticky=W,padx=10)

f2=Entry(font='Arial 13 bold',width=15, state='readonly')
f2.grid(row=3,column=1,sticky=W,padx=10)

f3=Entry(font='Arial 13 bold',width=15, state='readonly')
f3.grid(row=4,column=1,sticky=W,padx=10)

f1.configure(state='normal')
f1.delete(0, END)
f1.insert(0,opt.fun*-1)
f1.configure(state='readonly')

f2.configure(state='normal')
f2.delete(0, END)
f2.insert(0,opt.x)
f2.configure(state='readonly')

f3.configure(state='normal')
f3.delete(0, END)
f3.insert(0,opt.nit)
f3.configure(state='readonly')

root.mainloop()