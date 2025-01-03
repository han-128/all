import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from des import *
from math import *
from scipy import linalg
from tkinter import messagebox
import os 
import xlsxwriter



def excel():
    os.system('""MamaevLab3.xlsx""')


def matlab():
    os.system('"Mamaev.m"')


def ttxt():
    os.system('""D:\PycharmProjects\GUBKA\LAB3\Mamaev2.txt""')


def vivod(self):
    os.system('"D:\PycharmProjects\GUBKA\LAB3\MamaevVivod.xlsx"')


class MyApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.ui.pushButton_4.clicked.connect(self.calculate) #ВЫЧИСЛЕНИЯ
        self.ui.pushButton_7.clicked.connect(vivod) #ВЫВОД ЗНАЧЕНИЙ
        self.ui.pushButton_5.clicked.connect(excel) #EXCEL
        self.ui.pushButton_6.clicked.connect(matlab) #MATLAB
        self.ui.pushButton_9.clicked.connect(self.close) #ВЫХОД
        self.ui.pushButton_10.clicked.connect(ttxt) #TXT

        self.ui.radioButton.setChecked(True)
        self.ui.radioButton_2.setChecked(False)


        self.A = [[0.68, 1.32, -0.63, -0.87], [0.57, 0.36, -1.24, -0.23], [0.82, -0.32, 1.42, 1.48], [0.56, -1.2, 1.50, -0.64]]
        self.B = [[1.43], [0.33], [-0.84], [0.45]]



    def SwapRows(self, A, B, row1, row2):
        A[row1], A[row2] = A[row2], A[row1]
        B[row1], B[row2] = B[row2], B[row1]


    def DivideRow(self, A, B, row, divider):
        A[row] = [a / divider for a in A[row]]
        B[row][0] /= divider


    def CombineRows(self, A, B, row, source_row, num):
        A[row] = [(a + k * num) for a, k in zip(A[row], A[source_row])]
        B[row][0] += B[source_row][0] * num



    def Rscipy(self):
        
        TEXT = ""

        workbook = xlsxwriter.Workbook('"D:\PycharmProjects\GUBKA\LAB3\MamaevVivod.xlsx"')
        worksheet = workbook.add_worksheet()

        file_txt = open('Mamaev2.txt', 'w')



        


    def calculate(self):

        file_txt = open('Mamaev2.txt', 'w')

        
        gaus = self.ui.radioButton.isChecked()
        jord = self.ui.radioButton_2.isChecked()
 

        workbook = xlsxwriter.Workbook('"D:\PycharmProjects\GUBKA\LAB3\MamaevVivod.xlsx"')
        worksheet = workbook.add_worksheet()

        RRR = ""




        try:

            if gaus:

                TEXT = "метод Гаусса" + "\n" + "\n" 


                column = 0
                while column < len(self.B):
                    current_row = None
                    for r in range(column, len(self.A)):
                        if current_row is None or abs(self.A[r][column]) > abs(self.A[current_row][column]):
                            current_row = r
                    if current_row != column:
                        self.SwapRows(self.A, self.B, current_row, column)
                    self.DivideRow(self.A, self.B, column, self.A[column][column])
                    for r in range(column + 1, len(self.A)):
                        self.CombineRows(self.A, self.B, r, column, -self.A[r][column])
                    column += 1
                X = [[0], [0], [0], [0]]
                for i in range(len(self.B) - 1, -1, -1):
                    X[i] = self.B[i][0] - sum(x * a for x, a in zip(X[(i + 1):], self.A[i][(i + 1):]))


                file_txt.write('метод Гаусса' + '\n')
                worksheet.write('J1', 'метод Гаусса')


                file_txt.write('Решение Х =' + '\n')
                worksheet.write('J2', 'Решение Х =')


                for i in range(len(X)):
                    file_txt.write(str('{:.5f}').format(X[i]) + '\n')
                    worksheet.write(('J' + str(i + 3)), str('{:.5f}').format(X[i]))

                    RRR = RRR + str(X[i])[:7] + "\n"

                TEXT += RRR

                self.ui.textBrowser.setText(TEXT)

                
                x_scipy = linalg.solve(self.A, self.B)

                TEXT = TEXT + "\n" + "SCiPY" + "\n" + "\n"

                file_txt.write("\n" + "\n" + 'метод Гаусса-Жордана' + '\n')
                file_txt.write('Решение Х =' + '\n')


                for i in range(4):


                    TEXT = TEXT + str(x_scipy[i][0])[:7] + "\n"
                    file_txt.write(str('{:.5f}').format(x_scipy[i][0]) + '\n')
                    worksheet.write(('O' + str(i + 3)), str('{:.5f}').format(X[i]))    

                self.ui.textBrowser.setText(TEXT)


                return(X)    
            

            elif jord:

                TEXT = "метод Гаусса-Жордана" + "\n" + "\n" 


                column = 0
                while column < len(self.B):
                    current_row = None
                    for r in range(column, len(self.A)):
                        if current_row is None or abs(self.A[r][column]) > abs(self.A[current_row][column]):
                            current_row = r
                    if current_row != column:
                        self.SwapRows(self.A, self.B, current_row, column)
                    self.DivideRow(self.A, self.B, column, self.A[column][column])
                    for r in range(column + 1, len(self.A)):
                        self.CombineRows(self.A, self.B, r, column, -self.A[r][column])
                    column += 1
                for row in range(len(self.A)):
                    for column in range(len(self.A)):
                        if self.A[row][column] != 0 and self.A[row][column] != 1:
                            self.CombineRows(self.A, self.B, row, column, - self.A[row][column])
                X = [[0], [0], [0], [0]]
                for i in range(len(self.B) - 1, -1, -1):
                    X[i] = self.B[i][0] - sum(x * a for x, a in zip(X[(i + 1):], self.A[i][(i + 1):]))


                file_txt.write('метод Гаусса-Жордана' + '\n')
                worksheet.write('A1', 'метод Гаусса-Жордана')


                file_txt.write('Решение Х =' + '\n')
                worksheet.write('A2', 'Решение Х =')


                for i in range(len(X)):
                    file_txt.write(str('{:.5f}').format(X[i]) + '\n')
                    worksheet.write(('A' + str(i + 3)), str('{:.5f}').format(X[i]))

                    RRR = RRR + str(X[i])[:7] + "\n"

                TEXT += RRR

                self.ui.textBrowser.setText(TEXT)


                x_scipy = linalg.solve(self.A, self.B)


                TEXT = TEXT + "\n" + "SCiPY" + "\n" + "\n"

                file_txt.write("\n" + "\n" + 'метод Гаусса' + '\n')
                file_txt.write('Решение Х =' + '\n')

                for i in range(4):
                    TEXT = TEXT + str(x_scipy[i][0])[:7] + "\n"
                    file_txt.write(str('{:.5f}').format(x_scipy[i][0]) + '\n')
                    worksheet.write(('O' + str(i + 3)), str('{:.5f}').format(X[i]))    

                self.ui.textBrowser.setText(TEXT)


                return X


            else:
                messagebox.showinfo("Предупреждение", "Введите корректные данные!")
                pass
        except Exception as errorAAA:
            print(errorAAA)
        else:
            print("---")

#     def enter():
#         if gaus:
            
           

#             X = jordan_gauss(A, B)
#             for i in range(len(X)):
#                 l3 = Label(win, text=str('{:.5f}').format(X[i]), font='Times 14')
#                 l3.config(bg='pink', fg='white')
#                 l3.place(x=500, y=50 + (i + 1) * 30)
#                 file_txt.write(str('{:.5f}').format(X[i]) + '\n')
#                 worksheet.write(('A' + str(i + 3)), str('{:.5f}').format(X[i]))
#         else:
#             file_txt.write('метод Гаусса' + '\n')
#             worksheet.write('J1', 'метод Гаусса')
#             l1 = Label(win, text='метод Гаусса', font='Times 14')
#             l1.config(fg='pink', bg='white')
#             l1.place(x=900, y=6)
#             l2 = Label(win, text='Решение Х = ', font='Times 14')
#             l2.config(bg='pink', fg='white')
#             l2.place(x=900, y=50)
#             file_txt.write('Решение Х =' + '\n')
#             worksheet.write('J2', 'Решение Х =')
#             X = gauss(A, B)
#             for i in range(len(X)):
#                 l3 = Label(win, text= str('{:.5f}').format(X[i]), font='Times 14')
#                 l3.config(bg='pink', fg='white')
#                 l3.place(x = 900, y = 50 + (i + 1) * 30)
#                 file_txt.write(str('{:.5f}').format(X[i]) + '\n')
#                 worksheet.write(('J' + str(i + 3)), str('{:.5f}').format(X[i]))
#         # else:
#         #     messagebox.showinfo("Предупреждение", "выберите метод!")
#         x_scipy = linalg.solve(A, B)
#         l4 = Label(win,text = 'Решение через scipy.linalg.solve X =', font = 'Times 14')
#         l4.config(bg = 'pink', fg = 'white')
#         l4.place(x = 500, y = 300)
#         worksheet.write('O1', 'Решение через scipy.linalg.solve')
#         worksheet.write('O2', 'Решение Х =')
#         file_txt.write('Решение через scipy.linalg.solve' + '\n')
#         for i in range(3):
#             l5 = Label(win, text= '{:.5f}'.format(x_scipy[i][0]), font='Times 14')
#             l5.config(bg='pink', fg='white')
#             l5.place(x=500, y=350 + i * 30)
#             file_txt.write(str('{:.5f}').format(x_scipy[i][0]) + '\n')
#             

        self.file_txt.close()
        workbook.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec_())