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


def excel():
    os.system('"D:\PycharmProjects\GUBKA\Mamaev\Mamaev.xlsx"')


def matlab():
    os.system('"D:\PycharmProjects\GUBKA\Mamaev\Mamaev.m"')


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
        self.ui.radioButton_4.setChecked(False)

        self.mainPlot = PlotCanvas(self)
        self.mainPlot.move()




    def equation(self, x, a):
        return ((e**(0.724*x+a))-2.831*x)

    def derivative(self, x, a):
        return 0.724*e**(0.724*x + a) - 2.831

    def grafic(self):
        self.mainPlot.plott()

    def sc(self):
        self.ui.textBrowser.setText("""   ДЛЯ ДАННОЙ
   ФУНКЦИИ SCIPY
   ИСПОЛЬЗОВАТЬ
   НЕВОЗМОЖНО!!!""")
                                 



    def calculate(self):
        dixot = self.ui.radioButton_1.isChecked()
        xord = self.ui.radioButton_2.isChecked()
        kasat = self.ui.radioButton_3.isChecked()
        iter = self.ui.radioButton_4.isChecked()
        error = ''
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
            
            if (a != 0 and b != 0 and e != 0) and (a < b) and (a != b):
                if dixot:

                    self.ui.METOD_TEMP_2.setText("""         ДИХОТОМИИ""")

                    counter = 0
                    if self.equation(a, a) * self.equation(b, a) > 0:
                        error = "[eqzfksl]"
                    while (b - a) / 2 > ee:
                        counter += 1
                        c = (a + b) / 2
                        if self.equation(c, a) == 0:
                            root = x           
                        elif self.equation(a, a) * self.equation(c, a) < 0:
                            b = c
                        else:
                            a = c
                        TEXT = f"№ {str(counter)}: {str(round(c, 4))}"
                        RRR = RRR + "\n" + TEXT
                    self.ui.textBrowser.setText(RRR)
                    return ((a + b) / 2, counter)    
                
                
                elif xord:
                    self.ui.METOD_TEMP_2.setText("""           ХОРД""")
                    iter_count = 0
                    a = 1  
                    x0 = 0  
                    x1 = 1 
                    max_iter = 1000
                    while iter_count < max_iter:
                        x = x1 - self.equation(x1, a) * (x1 - x0) / (self.equation(x1, a) - self.equation(x0, a))
                        if iter_count != 0:
                            TEXT = f"№ {str(iter_count)}: {str(round(x, 4))}"
                            RRR = RRR + "\n" + TEXT
                        if abs(x - x1) < ee:
                            
                            self.ui.textBrowser.setText(RRR)
                            return x
                        
                        x0 = x1
                        x1 = x
                        iter_count += 1

                    return None 

                                
                elif kasat:
                    self.ui.METOD_TEMP_2.setText("""    КАСАТЕЛЬНЫХ""")
                    iter_count = 0
                    a = -10  
                    x0 = 1  
                    max_iter = 1000
                    x = x0
                    while iter_count < max_iter:
                        x_next = x - self.equation(x, a) / self.derivative(x, a)
                        if iter_count != 0:
                            TEXT = f"№ {str(iter_count)}: {str(round(x, 4))}"
                            RRR = RRR + "\n" + TEXT
                        if abs(x_next - x) < ee:
                            self.ui.textBrowser.setText(RRR)
                            return x_next
                        
                        x = x_next
                        iter_count += 1
                    
                    return None

                
                elif iter:
                    self.ui.METOD_TEMP_2.setText("""      ИТЕРАЦИЙ""")
                    RRR = ""
                    a = 1  
                    x0 = 1  
                    epsilon = 1e-6  
                    max_iter = 1000 
                    x = x0
                    iter_count = 0
                    while iter_count < max_iter:
                        x_next = (2.831 * x + a) / exp(0.724 * x)
                        if iter_count != 0:    
                            TEXT = f"№ {str(iter_count)}: {str(round(x, 4))}"
                            RRR = RRR + "\n" + TEXT
                        if abs(x_next - x) < epsilon:
                            self.ui.textBrowser.setText(RRR)
                            return x_next
                        
                        x = x_next
                        iter_count += 1
                    
                    return None 
                
                    
                
            else:
                messagebox.showinfo("Предупреждение", "Введите корректные данные!")
                pass
        except Exception as ee:
            print(ee)
        else:
            print("---")




class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5.4, height=4.9, dpi=100):
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
        x = -10
        a = 0
        TTT = ""


        while x <= 10:
            y = ((e**(0.724*x+a))-2.831*x)
            x_data.append(x)
            y_data.append(y)
            x += 0.5

        for i in range(len(x_data)):
            TTT = TTT + "\n" + str(x_data[i]) + " " + str(round(y_data[i], 3))  

        ax.plot(x_data, y_data)
        self.draw()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec_())