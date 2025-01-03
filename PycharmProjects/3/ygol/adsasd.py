import sys
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from des2 import *
from math import *


class MyApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.calculate)
        self.ui.radioButton_3.setChecked(True)

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
            plt.figure()
            plt.plot([0, 0, b, 0], [0, a, 0, 0])
            plt.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec_())
