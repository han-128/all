import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from desss import *
from math import *
from scipy.optimize import curve_fit
from tkinter import messagebox
import os 
import numpy as np


class MyApp(QtWidgets.QMainWindow):

    global absolute_error2, relative_error2

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_5.clicked.connect(self.graf2) #SCIPY
        self.ui.pushButton_3.clicked.connect(self.graf3) #MATLAB
        self.ui.pushButton_2.clicked.connect(self.graf4) #EXCEL
        self.ui.pushButton_6.clicked.connect(self.graf5) #ГРАФИК
        self.ui.pushButton_4.clicked.connect(self.scipyy) #ВЫЧИСЛЕНИЯ
        self.ui.pushButton.clicked.connect(self.best) #ВЫХОД
       
        self.mainPlot = PlotCanvas(self)
        self.mainPlot.move(270,85)

    def func(x, a, b, c, d, e):
        return a + b * x + c * x**2 + d * x**3 + e * x**4

    def gaussian_elimination(self, A, B):

        global x, y

        x = np.array([0, pi/5, 2*pi/5, 3*pi/5, 4*pi/5, pi, 6*pi/5, 7*pi/5, 8*pi/5, 9*pi/5, 2*pi])
        y = np.array(1/((2 + np.cos(x)) * (3 + np.cos(x))))


        n = len(A)
        for i in range(n):
            max_row = i
            for j in range(i + 1, n):
                if abs(A[j][i]) > abs(A[max_row][i]):
                    max_row = j
            A[i], A[max_row] = A[max_row], A[i]
            B[i], B[max_row] = B[max_row], B[i]
            for j in range(i + 1, n):
                factor = A[j][i] / A[i][i]
                for k in range(i, n):
                    A[j][k] -= factor * A[i][k]
                B[j] -= factor * B[i]
        x = [0] * n
        for i in range(n - 1, -1, -1):
            x[i] = B[i] / A[i][i]
            for j in range(i + 1, n):
                x[i] -= A[i][j] * x[j] / A[i][i]
        return x
    
    def least_squares(self, degree):

        global x_data, y_data, coefficients

        global least_squares

        x = np.array([0, pi/5, 2*pi/5, 3*pi/5, 4*pi/5, pi, 6*pi/5, 7*pi/5, 8*pi/5, 9*pi/5, 2*pi])
        y = np.array(1/((2 + np.cos(x)) * (3 + np.cos(x))))

        x_data = x
        y_data = y


        n = len(x_data)
        A = []
        for i in range(degree + 1):
            A_row = []
            for j in range(degree + 1):
                sum_x = sum(x1 ** (i + j) for x1 in x_data)
                A_row.append(sum_x)
            A.append(A_row)
        B = []
        for i in range(degree + 1):
            sum_xy = sum(y * (x ** i) for x, y in zip(x_data, y_data))
            B.append(sum_xy)
        coefficients = self.gaussian_elimination(A, B)
        k=0

        RRR = ""

        # for i in range(degree):

        TEXT = "КОЭФФИЦИЕНТЫ ПОЛИНОМА " + str(degree) + " CТЕПЕНИ:" + "\n" + "\n"

        for q in range(len(coefficients)):
            TEXT = TEXT + str('{:.5f}'.format(coefficients[q])) + "\n"
            self.ui.textEdit.setText(TEXT)
            # lk = Label(win, text = str('{:.5f}'.format(coefficients[q]))+" *x^"f"{k}", font=("Times New Roman", 14), background='lightblue')
            # lk.place(x=550,y=200+k*35)
            k+=1
            absolute_errors = []
            relative_errors = []
            for x, y in zip(x_data, y_data):
                approximated_y = sum(coefficients[i] * x ** i for i in range(degree + 1))
                absolute_error = abs(approximated_y - y)
                relative_error = absolute_error / abs(y) if y != 0 else absolute_error
                absolute_errors.append(absolute_error)
                relative_errors.append(relative_error)
            avg_absolute = sum(absolute_errors) / n
            avg_relative = sum(relative_errors) / n
            if 'e' in str(avg_absolute) and 'e' in str(avg_relative):
                string_avg_absolute = float(str(avg_absolute).split('e')[1])
                string_avg_relative = float(str(avg_relative).split('e')[1])
            else:
                string_avg_absolute = 0
                string_avg_relative = 0
            absolute = avg_absolute * 10 ** abs(string_avg_absolute)
            relative = avg_relative * 10 ** abs(string_avg_relative)
            
        TEXT = TEXT + "\n"

        TEXT = TEXT + "АБСОЛЮТНАЯ ПОГРЕШНОСТЬ: " + str(absolute)[:5] + "\n"
        TEXT = TEXT + "\n"

        TEXT = TEXT + "ОТНОСИТЕЛЬНАЯ ПОГРЕШНОСТЬ: " + str(relative*100)[:5] + "%" + "\n"
        # TEXT = TEXT + str(coefficients[q])[:6] + "\n"
        self.ui.textEdit.setText(TEXT)


    x = np.array([0, pi/5, 2*pi/5, 3*pi/5, 4*pi/5, pi, 6*pi/5, 7*pi/5, 8*pi/5, 9*pi/5, 2*pi])
    y = np.array(1/((2 + np.cos(x)) * (3 + np.cos(x))))
    
    XXX = ""

    popt2, _ = curve_fit(func, x, y)

    y_pred2 = func(x, *popt2)

    absolute_error2 = np.abs(y - y_pred2)

    relative_error2 = absolute_error2 / y

    print(absolute_error2)
    XXX =  "АБСОЛЮТНАЯ ПОГРЕШНОСТЬ: " + "\n"
    for i in range(0, 5):
        XXX = XXX + str(i + 1) + " СТЕПЕНИ: "  + str('{:.5f}'.format(absolute_error2[i])) + "\n"
        print(XXX)
    RRR = "\n" + XXX + "ОТНОСИТЕЛЬНАЯ ПОГРЕШНОСТЬ: " + "\n"
    for i in range(0, 5):
        RRR = RRR + str(i + 1) + " СТЕПЕНИ: "  + str("{:.2%}".format(relative_error2[i])) + "\n"


    def scipyy(self):
        self.ui.textEdit.setText(self.RRR)


    # print(absolute_error2)
    # print(absolute_error3)
    # print(absolute_error4)
    # print(absolute_error5)



      
    def graf2(self):
        self.coefficients = self.least_squares(2)
        self.mainPlot.plott(degree=2)


    def graf3(self):
        self.coefficients = self.least_squares(3)
        self.mainPlot.plott(degree=3)


    def graf4(self):
        self.coefficients = self.least_squares(4)
        self.mainPlot.plott(degree=4)

    def graf5(self):
        self.coefficients = self.least_squares(5)
        self.mainPlot.plott(degree=5)

    def best(self):
        self.ui.textEdit.setText("Наилучшая апроксимирующая функция: Cтепень 4 и 5, т.к. имеют наименьшую погрешность")

class PlotCanvas(FigureCanvas):
    
    def __init__(self, parent=None, width=5.4, height=4.8, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


    def plott(self, degree):
        self.fig.clf()
        ax = self.figure.add_subplot(111)

        x_values = np.linspace(min(x_data), max(x_data), 100)
        y_values = sum(coefficients[i] * x_values ** i for i in range(degree + 1))

        ax.scatter(x_data, y_data, color = "red")
        ax.grid(True)
        ax.plot(x_values, y_values)

        self.draw()




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec_())