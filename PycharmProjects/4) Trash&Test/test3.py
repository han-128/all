from tkinter import Tk, StringVar, Entry, Button

master = Tk()

v = StringVar()
e = Entry(master, textvariable=v)
e.pack()


def get_value():
    print(v.get())


def clean_value():
    v.set("")


b1 = Button(master, text="get value", width=10, command=get_value)
b2 = Button(master, text="clean", width=10, command=clean_value)

b1.pack()
b2.pack()

master.mainloop()