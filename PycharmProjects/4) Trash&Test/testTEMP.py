from tkinter import *
from random import randint
from math import *
import time


def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def interpolation_search(arr, x):
    low = 0
    high = (len(arr) - 1)

    while low <= high and x >= arr[low] and x <= arr[high]:
        if low == high:
            if arr[low] == x:
                return low
            return -1

        pos = low + ((high - low) // (arr[high] - arr[low]) * (x - arr[low]))
        pos = int(pos)

        if arr[pos] == x:
            return pos

        if arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1
    return -1

def jump_search(arr, x):
    step = sqrt(len(arr))
    prev = 0

    while arr[int(min(step, len(arr) - 1))] < x:
        prev = step
        step += sqrt(len(arr))
        if prev >= len(arr):
            return -1

    while arr[int(prev)] < x:
        prev += 1

        if prev == min(step, len(arr)):
            return -1

    if arr[int(prev)] == x:
        return int(prev)

    return -1

def sentinel_linear_search(arr, x):
    last = arr[-1]
    arr[-1] = x

    i = 0
    while arr[i] != x:
        i += 1

    arr[-1] = last

    if (i < len(arr) - 1) or (arr[-1] == x):
        return i

    return -1

def random_mas():
    global a
    st=int(zn.get())
    fn=int(zn0.get())
    n=50000
    a=[]
    for i in range(n):
         a.append(randint(st,fn))
    vuvod(a,n,st,fn)
    
def read_file():
    file_name=fl.get()
    f=open(file_name)
    a=list(map(float, f.read().split()))
    vuvod(a,len(a),min(a),max(a))


def save_file():
    file_name=fl.get()
    f=open(file_name, "w")
    new_mass = ''
    for i in range(len(a)):
        new_mass = new_mass + ' ' + str(a[i])
    f.write(new_mass)
    f.close
    

def vuvod(a,n,st,fn):
    
    c=randint(st,fn)
    
    zn1.configure(state='normal')
    zn1.delete(0, END)
    zn1.insert(0,c)
    zn1.configure(state='readonly')
    
    st_t=time.time_ns()
    b=linear_search(a, c)
    fin_t= (time.time_ns() - st_t)
    
    t1.configure(state='normal')
    t1.delete(0, END)
    t1.insert(0,fin_t)
    t1.configure(state='readonly')
    

    st_t=time.time_ns()
    b=interpolation_search(sorted(a), c)
    fin_t= (time.time_ns() - st_t)
    
    t2.configure(state='normal')
    t2.delete(0, END)
    t2.insert(0,fin_t)
    t2.configure(state='readonly')
    
    st_t=time.time_ns()
    b=jump_search(sorted(a), c)
    fin_t= (time.time_ns() - st_t)
    
    t3.configure(state='normal')
    t3.delete(0, END)
    t3.insert(0,fin_t)
    t3.configure(state='readonly')
    
    st_t=time.time_ns()
    b=sentinel_linear_search(a, c)
    fin_t= (time.time_ns() - st_t)
    
    t4.configure(state='normal')
    t4.delete(0, END)
    t4.insert(0,fin_t)
    t4.configure(state='readonly')



    

root = Tk()
root.geometry('1050x400')
root.resizable(0,0)
root.title('Сабурова лаб3')
root.config(bg="grey")


Label(text='Название файла в формате "name.txt"', font='Arial 12 bold',padx=10, pady=10, bg="cyan").grid(row=1,column=0,sticky=W)
Label(text='Массив от', font='Arial 12 bold',padx=10, pady=10, bg="cyan").grid(row=1,column=2,sticky=W)
Label(text='до', font='Arial 12 bold',padx=10, pady=10, bg="cyan").grid(row=1,column=4,sticky=W)
Label(text='Искомый эелемент', font='Arial 12 bold',padx=10, pady=10, bg="cyan").grid(row=2,column=0,sticky=W)
Label(text='Время линейного поиска', font='Arial 12 bold',padx=10, pady=10, bg="cyan").grid(row=3,column=0,sticky=W)
Label(text='Время интерполяционого поиска', font='Arial 12 bold',padx=10, pady=10, bg="cyan").grid(row=4,column=0,sticky=W)
Label(text='Время Jump Search', font='Arial 12 bold',padx=10, pady=10, bg="cyan").grid(row=5,column=0,sticky=W)
Label(text='Время Sentinel Linear Search', font='Arial 12 bold',padx=10, pady=10, bg="cyan").grid(row=6,column=0,sticky=W)



fl=Entry(font='Arial 10 bold',width=15)
fl.insert(END, "1.txt")
fl.grid(row=1,column=1,sticky=W,padx=10)
zn=Entry(font='Arial 10 bold',width=15)
zn.insert(END, "9")
zn.grid(row=1,column=3,sticky=W,padx=10)
zn0=Entry(font='Arial 10 bold',width=15)
zn0.insert(END, "9000")
zn0.grid(row=1,column=5,sticky=W,padx=10)
zn1=Entry(font='Arial 10 bold',width=15, state="readonly")
zn1.grid(row=2,column=1,sticky=W,padx=10)
t1=Entry(font='Arial 10 bold',width=15, state="readonly")
t1.grid(row=3,column=1,sticky=W ,padx=10)
t2=Entry(font='Arial 10 bold',width=15, state="readonly")
t2.grid(row=4,column=1,sticky=W ,padx=10)
t3=Entry(font='Arial 10 bold',width=15, state="readonly")
t3.grid(row=5,column=1,sticky=W ,padx=10)
t4=Entry(font='Arial 10 bold',width=15, state="readonly")
t4.grid(row=6,column=1,sticky=W ,padx=10)


# Button(text='Вычислить случайные', font='Arial 12 bold',padx=20, width= 15, command=random_mas).grid(row=8,column=0,pady=(30,0))
# Button(text='Вычислить из файла', font='Arial 12 bold',padx=20, width= 15, command=read_file).grid(row=8,column=1,pady=(30,0))
# Button(text='Сохранить в файл', font='Arial 12 bold',padx=20, width= 15, command=save_file).grid(row=8,column=3,pady=(30,0))


random_button = Button(root, text="Вычислить случайные", command=random_mas, bg="cyan", font=("Times New Roman", 14))
random_button.place(x=530, y=100)

file_button = Button(root, text="Вычислить из файла", command=read_file, bg="cyan", font=("Times New Roman", 14))
file_button.place(x=530, y=150)

save_button = Button(root, text="Сохранить в файл", command=save_file, bg="cyan", font=("Times New Roman", 14))
save_button.place(x=530, y=200)


root.mainloop()