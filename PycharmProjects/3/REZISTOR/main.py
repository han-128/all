import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from des import *
from math import *


class MyApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
        self.a4 = 0
        self.a5 = 0
        self.countColor = 0
        # self.ui.buttonGroup.buttonClicked[int].connect(lambda x: self.test(x))
        self.ui.buttonGroup.buttonClicked.connect(lambda btn: self.group1(btn.text()))
        self.ui.buttonGroup_2.buttonClicked.connect(lambda btn: self.group2(btn.text()))
        self.ui.buttonGroup_3.buttonClicked.connect(lambda btn: self.group3(btn.text()))
        self.ui.buttonGroup_4.buttonClicked.connect(lambda btn: self.group4(btn.text()))
        self.ui.buttonGroup_5.buttonClicked.connect(lambda btn: self.group5(btn.text()))
        self.ui.buttonGroup_6.buttonClicked.connect(lambda btn: self.group6(btn.text()))

        self.ui.radioButton_49.setChecked(True)
        self.switchGroup(False)

    def group1(self, n):
        print('1', end=':>')
        print(f'{n}: {self.colorCheck(n, 0)}')
        self.a1 = self.colorCheck(n, 0)
        self.calculate()

    def group2(self, n):
        print(f'{n}: {self.colorCheck(n, 0)}')
        self.a2 = self.colorCheck(n, 0)
        self.calculate()

    def group3(self, n):
        print(f'{n}: {self.colorCheck(n, 0)}')
        self.a3 = self.colorCheck(n, 0)
        self.calculate()

    def group4(self, n):
        print(f'{n}: {self.colorCheck(n, 1)}')
        self.a4 = self.colorCheck(n, 1)
        self.calculate()

    def group5(self, n):
        print(f'{n}: {self.colorCheck(n, 2)}')
        self.a5 = self.colorCheck(n, 2)
        self.calculate()

    def group6(self, n):
        print(f'{n}: {self.colorCheck(n, 3)}')
        self.countColor = self.colorCheck(n, 3)
        self.calculate()
        if self.countColor == 2:
            self.switchGroup(True)
        else:
            self.switchGroup(False)
        self.calculate()

    def colorCheck(self, color, param):
        lst_1 = ['ЧЁРНЫЙ', 'КОРИЧНЕВЫЙ', 'КРАСНЫЙ',
                 'ОРАНЖЕВЫЙ', 'ЖЁЛТЫЙ', 'ЗЕЛЁНЫЙ',
                 'ГОЛУБОЙ', 'ФИОЛЕТОВЫЙ', 'СЕРЫЙ',
                 'БЕЛЫЙ', 'СЕРЕБРИСТЫЙ', 'ЗОЛОТИСТЫЙ']
        lst_2 = ['СЕРЕБРИСТЫЙ', 'ЗОЛОТИСТЫЙ'] + lst_1
        lst_3 = ['СЕРЕБРИСТЫЙ', 'ЗОЛОТИСТЫЙ',
                 'КОРИЧНЕВЫЙ', 'КРАСНЫЙ', 'ЗЕЛЁНЫЙ', 'ГОЛУБОЙ',
                 'ФИОЛЕТОВЫЙ', 'СЕРЫЙ', 'БЕЛЫЙ']
        lst_4 = ['4 ЦВЕТОВЫХ ПОЛОСКИ', '5 ЦВЕТОВЫХ ПОЛОСОК']
        lst = [lst_1, lst_2, lst_3, lst_4]
        return lst[param].index(color) + 1

    def switchGroup(self, active: bool):
        lst = [self.ui.radioButton_19, self.ui.radioButton_21, self.ui.radioButton_28,
               self.ui.radioButton_29, self.ui.radioButton_31, self.ui.radioButton_22,
               self.ui.radioButton_36, self.ui.radioButton_40, self.ui.radioButton_44,
               self.ui.radioButton_5]
        for item in lst:
            item.setEnabled(active)

    def calculate(self):
        listOfErrorRate = [0, 10, 5, 1, 2, 0.5, 0.25, 0.1, 0.05]
        lst = [self.a1, self.a2, self.a4, self.a5, self.countColor]
        for i in lst:
            if i == 0: return

        if self.countColor == 1:
            a5 = listOfErrorRate[self.a5]
            sumN = round((((self.a1 - 1) * 10) + (self.a2 - 1)) * (0.001 * (10 ** self.a4)), 2)
            print(sumN, 'Oм  +-', a5, '%')
            self.ui.textEdit.setText(f'{sumN}Ом +-{a5}%')
        elif self.countColor == 2 and self.a3 != 0:
            a5 = listOfErrorRate[self.a5]
            sumN = round(((self.a1 - 1) * 100 + ((self.a2 - 1) * 10) + (self.a3 - 1)) * (0.001 * (10 ** self.a4)), 2)
            print(sumN, 'Oм  +-', a5, '%')
            self.ui.textEdit.setText(f'{sumN}Ом +-{a5}')
        else:
            return


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec_())
