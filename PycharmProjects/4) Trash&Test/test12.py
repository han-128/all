import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from des import *
from math import *


class MyApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.calculate)
        self.ui.radioButton_3.setChecked(True)

        self.mainPlot = PlotCanvas(self)
        self.mainPlot.move(120, 150)


    def calculate(self):
        mode = self.ui.radioButton_3.isChecked()
        error = ''

        try:
            if mode:
                a = self.ui.doubleSpinBox.text()
                a = float('.'.join(a.split(',')))

                b = self.ui.doubleSpinBox_2.text()
                b = float('.'.join(b.split(',')))

                c = (a ** 2 + b ** 2) ** (1 / 2)
                ya = atan(a / b)
                ya2 = (ya * 180) / pi
                print(f'Угол лежащий между гипотенузой и первым катетом =  {round(ya2)}')
                yb = 90 - ya2
                print(f'Угол лежащий между гипотенузой и вторым катетом = {round(yb)}')
                print(f'Гипотенуза равна: {round(c)}')
            else:
                a = self.ui.doubleSpinBox.text()
                a = float('.'.join(a.split(',')))

                c = self.ui.doubleSpinBox_2.text()
                c = float('.'.join(c.split(',')))
                if c > a:
                    ya = asin(a / c)
                    ya2 = (ya * 180) / pi
                    print(f'Угол лежащий между гипотенузой и неизвестным катетом равен: {round(ya2)}')
                    yb = 90 - ya2
                    print(f'Угол лежащий между гипотенузой и изветным катетом равен: {round(yb)}')
                    b = ((c ** 2) - (a ** 2)) ** (1 / 2)
                    print(f'Неизвестный катет равен: {round(b)}')
                else:
                    error = 'c < a'
                    t = 1 / 0
                    b = 0
        except Exception as e:
            print(e)
            self.ui.statusbar.showMessage('Не правильно введены значения. ' + error)
        else:
            self.mainPlot.showPlot(a, b, f'{round(ya2)}', f'{round(yb)}')


class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def showPlot(self, a, b, ya2, yb):
        self.fig.clf()
        ax = self.figure.add_subplot(111)

        bbox_properties = dict(
            boxstyle="round, pad=0.1",
            ec="k",
            fc="y",
            ls="-",
            lw=3
        )

        ax.text(0.2, a * 0.9, ya2, fontsize=15, bbox=bbox_properties)
        ax.text(b * 0.9, 0.2, yb, fontsize=15, bbox=bbox_properties)
        #ax.text(1, 1, 'угол')
        ax.plot([0, 0, b, 0], [0, a, 0, 0])
        self.draw()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec_())
