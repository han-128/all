import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from des import *
from math import *
from scipy.optimize import bisect, newton, fsolve
from tkinter import messagebox
import os 


class MyApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.l_pr) 
        self.ui.pushButton_2.clicked.connect(self.r_pr) 
        self.ui.pushButton_3.clicked.connect(self.m_pr) 
        self.ui.pushButton_4.clicked.connect(self.trap) 
        self.ui.pushButton_5.clicked.connect(self.simpson) 
        self.ui.pushButton_6.clicked.connect(self.l_tab) 
        self.ui.pushButton_7.clicked.connect(self.r_tab) 
        self.ui.pushButton_9.clicked.connect(self.m_tab) 
        self.ui.pushButton_8.clicked.connect(self.trap_tab) 
        self.ui.pushButton_10.clicked.connect(self.simpson_tab) 



    solution = (1/2) * log(5/4)


    a, b, h = 0, 1, 1/30
    n = 30


    def f(self, x):
        return (x/(4+(x**2)))


    def l_pr(self, a=0, n=30, h=1/30):
        sm = 0
        for i in range(0, n):
            sm += h * self.f(a + h * i)
        self.ui.tochno.setText("             " + str((1/2) * log(5/4))[:6])
        self.ui.otvet.setText("             " + str(sm)[:6])
        self.ui.nesxod.setText("             " + str(abs(((1/2) * log(5/4)) - sm))[:6])        
        return sm

    def r_pr(self, a=0, n=30, h=1/30):
        sm = 0
        for i in range(1, n + 1):
            sm += h * self.f(a + h * i)
        self.ui.tochno.setText("             " + str((1/2) * log(5/4))[:6])
        self.ui.otvet.setText("             " + str(sm)[:6])
        self.ui.nesxod.setText("             " + str(abs(((1/2) * log(5/4)) - sm))[:6])        
        return sm
    

    
    def m_pr(self, a=0, n=30, h=1/30):
        sm = 0
        for i in range(n):
            sm += self.f(a + h * (i + 0.5)) 
        self.ui.tochno.setText("             " + str((1/2) * log(5/4))[:6])
        self.ui.otvet.setText("             " + str(h * sm)[:6])
        self.ui.nesxod.setText("                  " + str(abs(int(((1/2) * log(5/4)) - (h * sm))))[:6])
        return h * sm

    def trap(self, a=0, b=1, n=30, h=1/30):
        sm =  (self.f(a) + self.f(b))* h * 0.5 
        for i in range(1, n):
            sm += h * self.f(a + h * i)
        self.ui.tochno.setText("             " + str((1/2) * log(5/4))[:6])
        self.ui.otvet.setText("             " + str(sm)[:6])
        self.ui.nesxod.setText("                  " + str(abs(int(((1/2) * log(5/4)) - sm)))[:6])
        return sm

    def simpson(self, a=0, b=1, n=30, h=1/30):
        sm = h / 3 * (self.f(a) + self.f(b))
        for i in range(1, n):
            sm += h / 3 * 2 * self.f(a + h * i) * (i % 2 + 1)
        self.ui.tochno.setText("             " + str((1/2) * log(5/4))[:6])
        self.ui.otvet.setText("             " + str(sm)[:6])
        self.ui.nesxod.setText("                  " + str(abs(int(((1/2) * log(5/4)) - sm)))[:6])
        return sm






    TABsolution = pi

    x = [0, 0.31, 0.63, 0.94, 1.26, 1.57, 1.88, 2.2, 2.51, 2.83, 3.14]
    y = [0.5, 0.51, 0.54, 0.59, 0.67, 0.8, 0.98, 1.24, 1.55, 1.86, 2]


    def l_tab(self):
        x = [0, 0.31, 0.63, 0.94, 1.26, 1.57, 1.88, 2.2, 2.51, 2.83, 3.14]
        y = [0.5, 0.51, 0.54, 0.59, 0.67, 0.8, 0.98, 1.24, 1.55, 1.86, 2]
        sm = 0
        for i in range(1, len(x)):
            sm += (abs(x[i] - x[i - 1])) * y[i-1]
        self.ui.tochno.setText("             " + str(pi)[:6])
        self.ui.otvet.setText("             " + str(sm)[:6])
        self.ui.nesxod.setText("              " + str(abs(((pi) - sm)))[:6])

        return sm

    def r_tab(self):
        x = [0, 0.31, 0.63, 0.94, 1.26, 1.57, 1.88, 2.2, 2.51, 2.83, 3.14]
        y = [0.5, 0.51, 0.54, 0.59, 0.67, 0.8, 0.98, 1.24, 1.55, 1.86, 2]
        sm = 0
        for i in range(1, len(x)):
            sm += (abs(x[i] - x[i - 1])) * y[i]
        self.ui.tochno.setText("             " + str(pi)[:6])
        self.ui.otvet.setText("             " + str(sm)[:6])
        self.ui.nesxod.setText("              " + str(abs(((pi) - sm)))[:6])
        return sm

    def m_tab(self):
        x = [0, 0.31, 0.63, 0.94, 1.26, 1.57, 1.88, 2.2, 2.51, 2.83, 3.14]
        y = [0.5, 0.51, 0.54, 0.59, 0.67, 0.8, 0.98, 1.24, 1.55, 1.86, 2]
        sm = (abs(x[1] - x[0])) * (abs(y[0] + y[-1]) * 0.5)
        for i in range(1, len(x) - 1):
            sm += (abs(x[i] - x[i - 1])) * (abs(y[i] + y[i - 1]) * 0.5)
        self.ui.tochno.setText("             " + str(pi)[:6])
        self.ui.otvet.setText("             " + str(sm)[:6])
        self.ui.nesxod.setText("              " + str(abs(((pi) - sm)))[:6])
        return sm

    def trap_tab(self):
        x = [0, 0.31, 0.63, 0.94, 1.26, 1.57, 1.88, 2.2, 2.51, 2.83, 3.14]
        y = [0.5, 0.51, 0.54, 0.59, 0.67, 0.8, 0.98, 1.24, 1.55, 1.86, 2]
        sm = abs(x[1] - x[0]) * 0.5 * y[0] + abs(x[-1] - x[-2]) * 0.5 * y[-1]
        for i in range(1, len(x) - 1):
            sm += abs(x[i] - x[i - 1]) * y[i]
        self.ui.tochno.setText("             " + str(pi)[:6])
        self.ui.otvet.setText("             " + str(sm)[:6])
        self.ui.nesxod.setText("              " + str(abs(((pi) - sm)))[:6])
        return sm

    def simpson_tab(self):
        x = [0, 0.31, 0.63, 0.94, 1.26, 1.57, 1.88, 2.2, 2.51, 2.83, 3.14]
        y = [0.5, 0.51, 0.54, 0.59, 0.67, 0.8, 0.98, 1.24, 1.55, 1.86, 2]
        sm = abs(x[1] - x[0]) / 3 * y[0] + abs(x[-1] - x[-2]) / 3 * y[-1]
        for i in range(1, len(x)):
            sm += abs(x[i] - x[i - 1]) / 3 * 2 * y[i] * (i % 2 + 1)
        self.ui.tochno.setText("             " + str(pi)[:6])
        self.ui.otvet.setText("             " + str(sm)[:6])
        self.ui.nesxod.setText("              " + str(abs(((pi) - sm)))[:6])
        return sm




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec_())