import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from des import *
from math import *
from scipy.optimize import bisect, newton, fsolve
from tkinter import messagebox
import os 
from scipy.optimize import root



def excel():
    os.system('"Mamaev.xlsx"')


def matlab():
    os.system('"Mamaev.m"')



class MyApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_4.clicked.connect(self.calculate) #ВЫЧИСЛЕНИЯ
        self.ui.pushButton_5.clicked.connect(self.sc) #SCIPY
        self.ui.pushButton_3.clicked.connect(matlab) #MATLAB
        self.ui.pushButton_2.clicked.connect(excel) #EXCEL
        self.ui.pushButton.clicked.connect(self.close) #ВЫХОД
        self.ui.pushButton_6.clicked.connect(self.grafic) #ГРАФИК
        self.ui.radioButton_1.setChecked(True)
        self.ui.radioButton_2.setChecked(False)
        self.ui.radioButton_3.setChecked(False)

        self.mainPlot = PlotCanvas(self)
        self.mainPlot.move(260, 70)


    def equation1(self, mas):
        x, y = mas[0], mas[1] 
        return [sin(x+1)-1-y, (2*x+cos(y))-2] 
    

    def f(self, x, y):
        return [sin(x+1)-1-y, (2*x+cos(y))-2] 


    def f1(self, x, y):
        c = (2-cos(y))/2
        return c
    

    def f2(self, x, y):
        c = sin(x+1)-1
        return c
    

    def jacobian(self, x, y):
        return [[cos(x+1), -1], [2, -1*sin(y)]]


    def invert_matrix(self, m):
        det = m[0][0] * m[1][1] - m[0][1] * m[1][0]
        inv_det = 1 / det
        return [[m[1][1] * inv_det, -m[0][1] * inv_det], [-m[1][0] * inv_det, m[0][0] * inv_det]]



    def grafic(self):
        self.mainPlot.plott()


    def sc(self):

        self.ui.PRIRESHENII.setText("""РЕЗУЛЬТАТЫ ПРИ РЕШЕНИИ ЧЕРЕЗ SCIPY""")

        RRR = ""

        a = self.ui.spinBox.text()
        a = float('.'.join(a.split(',')))

        b = self.ui.spinBox_2.text()
        b = float('.'.join(b.split(',')))

        ee = self.ui.spinBox_3.text()
        ee = float('.'.join(ee.split(',')))
        ee = ee * 0.001  

        sol = root(self.equation1, [a, b], method='hybr')
        RRR = RRR + "\n" + "scipy.hybr:     x = " + str(round(sol.x[0], 5)) + " y=" + str(round(sol.x[1], 5)) + "\n"
        sol1 = root(self.equation1, [a, b], method='krylov')
        RRR = RRR + "\n" + "scipy.krylov:       x = " + str(round(sol1.x[0], 5)) + " y=" + str(round(sol1.x[1], 5)) + "\n"
        sol2 = root(self.equation1, [a, b], method='broyden1')
        RRR = RRR + "\n" + "scipy.broyden1:     x = " + str(round(sol2.x[0], 5)) + " y=" + str(round(sol2.x[1], 5)) + "\n"
        self.ui.textBrowser.setText(RRR)


    def calculate(self):

        jako = self.ui.radioButton_1.isChecked()
        gaus = self.ui.radioButton_2.isChecked()
        niut = self.ui.radioButton_3.isChecked()
        RRR = ""
        TEXT = ""


        try:

            a = self.ui.spinBox.text()
            a = float('.'.join(a.split(',')))

            b = self.ui.spinBox_2.text()
            b = float('.'.join(b.split(',')))

            ee = self.ui.spinBox_3.text()
            ee = float('.'.join(ee.split(',')))
            ee = ee * 0.001

            RRR = ""
            TEXT = ""
            errorAAA = "проблемы у вас"

            if (a != 0 and b != 0 and e != 0) and (a < b) and (a != b) and ee != 0:
                if jako:  
                    RRR = ""
                    TEXT = ""
                    self.ui.PRIRESHENII.setText("""РЕЗУЛЬТАТЫ ПРИ РЕШЕНИИ МЕТОДОМ ЯКОБИ""")
                    counter = 0
                    y1 = self.f2 (a, b)
                    x1 = self.f1 (a, b)
                    while abs(a - x1) > ee and abs(b - y1) > ee:
                        counter += 1
                        a = x1
                        b = y1
                        y1 = self.f2(a, b)
                        x1 = self.f1(a, b)
                        TEXT = "№" + str(counter) + " " + str(round(a, 5)) + " " + str(round(b, 5)) + "\n"
                        RRR = RRR + "\n" + TEXT
                    
                    x = 0.5
                    y = -0.0025
                    print(sin(x+1)-1-y, (2*x+cos(y))-2)

                    self.ui.textBrowser.setText(RRR)
                    return (a, b, counter)


                elif gaus:
                    RRR = ""
                    TEXT = ""
                    self.ui.PRIRESHENII.setText("""РЕЗУЛЬТАТЫ ПРИ РЕШЕНИИ МЕТОДОМ ГАУССА-ЗЕЙДЕЛЯ""")
                    counter = 0
                    x1 = self.f1(a, b)
                    y1 = self.f2(x1, b)
                    while abs(a - x1) > ee and abs(b - y1) > ee:
                        counter += 1
                        a = x1
                        b = y1
                        x1 = self.f1(a, b)
                        y1 = self.f2(x1, b)
                        TEXT = "№" + str(counter) + " " + str(round(a, 4)) + " " + str(round(b, 4)) + "\n"
                        RRR = RRR + "\n" + TEXT
                
                    x = -0.42
                    y = 0.58
                    print(sin(x+1)-1-y, (2*x+cos(y))-2)

                    self.ui.textBrowser.setText(RRR)
                    return (a, b, counter)
                
                elif niut:

                    RRR = ""
                    TEXT = ""
                    counter = 0

                    self.ui.PRIRESHENII.setText("""РЕЗУЛЬТАТЫ ПРИ РЕШЕНИИ МЕТОДОМ НЬЮТОНА""")

                    while True:
                        counter += 1
                        fx, fy = self.f(a, b)
                        j_inv = self.invert_matrix(self.jacobian(a, b))
                        dx = j_inv[0][0] * fx + j_inv[0][1] * fy
                        dy = j_inv[1][0] * fx + j_inv[1][1] * fy
                        a, b = a - dx, b - dy
                        if sqrt(dx ** 2 + dy ** 2) < ee:
                            break

                        TEXT = "№" + str(counter) + " " + str(round(a, 4)) + " " + str(round(b, 4)) + "\n"
                        RRR = RRR + "\n" + TEXT

                    self.ui.textBrowser.setText(RRR)
                    return (a, b, counter)


            else:
                messagebox.showinfo("Предупреждение", "Введите корректные данные!")
                pass
        except Exception as errorAAA:
            print(errorAAA)
        else:
            print("---")



class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5.5, height=5.15, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)



    def plott(self):
        self.fig.clf()
        ax = self.figure.add_subplot(111)


        x_data = []
        y_data = []
        x = -3
        TTT = ""
        aaa = []
        bbb = []


        while x <= 3:
            y = (sin(x+1))-1
            x_data.append(x)
            y_data.append(y)
            x += 0.5

        y = -3

        while y <= 2:
            x = (2-cos(y))/2
            aaa.append(x)
            bbb.append(y)
            y += 0.5



        for i in range(len(x_data)):
            TTT = TTT + "\n" + str(x_data[i]) + " " + str(round(y_data[i], 3))  


        ax.grid(True)
        ax.plot(x_data, y_data)
        ax.plot(aaa, bbb)
        self.draw()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec_())