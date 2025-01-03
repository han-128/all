import re 
import os 
import sys
import random 

from des import *
from math import *

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import *
from PySide2.QtWidgets import *



def word():
    os.system('"D:\PycharmProjects\GUBKA\kursach\Mamaev\mamaev.doc"')


def fwords():
    os.system('words.txt')



class MyApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.progressBar_3.setValue(0)
        self.ui.progressBar_4.setValue(0)

        self.ui.label_4.setText("            КОЛИЧЕТСВО СЛОВ" + "\n" + "              В ПРЕДЛОЖЕНИИ")
        self.ui.label_26.setText("       РГУ НЕФТИ И ГАЗА" + "\n" + "            ИМ. ГУБКИНА")
        self.ui.label_28.setText("                    ОСНОВЫ" + "\n" + "         АЛГОРИТМИЗАЦИИ И" + "\n" + "         ПРОГРАММИРОВАНИЯ")
        self.ui.label_29.setText("   МАМАЕВ РОСТИСЛАВ" + "\n" + "               АА-23-07")
        self.ui.label_27.setText("            КУРСОВАЯ РАБОТА" + "\n" + "                   ТЕМА №34")
        

        self.ui.textEdit.setText("       ОТ:")
        self.ui.textEdit_2.setText("                ДО:")
        self.ui.label_5.setText("       КОЛИЧЕТСВО БУКВ" + "\n" + "                 В СЛОВЕ")
        self.ui.textEdit_5.setText("                         ОТ:")
        self.ui.textEdit_6.setText("      ДО:")
        
        self.ui.textEdit_43.setText("     ОТ:")
        self.ui.textEdit_44.setText("     ДО:")

        self.ui.checkBox.setText("    ИСПОЛЬЗОВАТЬ" + "\n" + "   СЛОВА ИЗ ФАЙЛА")
        
        self.ui.btn_word_3.setText("ОТКРЫТЬ ФАЙЛ" + "\n" + "СО СЛУЧАЙНЫМИ" + "\n" + "СЛОВАМИ")

        self.ui.btn_gen.clicked.connect(self.gen) 
        self.ui.btn_sort.clicked.connect(self.sor) 
        self.ui.btn_clear_gen.clicked.connect(self.clear_gen) 
        self.ui.btn_clear_sort.clicked.connect(self.clear_sort) 
        self.ui.btn_theme.clicked.connect(self.theme) 
        self.ui.btn_word.clicked.connect(word) 
        self.ui.btn_word_3.clicked.connect(fwords) 
        
        self.ui.checkBox.clicked.connect(self.text)



        self.q = False

        self.words = []

        with open("words.txt", "r") as file1:
            for line in file1:
                self.words.append(line.split())    

        w = []
        TEXT = ""
        T = ""
        c = "⋅"

        for i in range(1, 91):
            print(str(self.words[i-1][0]))
            w.append(str(self.words[i-1][0]))
            if i % 2 == 0:
                TEXT = TEXT + str(i) + ")" +  str(self.words[i-1][0]) + "\n"
            else: 
                T =  str(i) + ")" +  str(self.words[i-1][0]) 
                print(T + "1")
                T = T.ljust(14, c)
                L = 14 - len(self.words[i-1][0])
                print(T.ljust(14) + "2")
                TEXT = TEXT  + "   " + T

        print(self.words)
        print(w)
        print(TEXT)


        self.ui.textEdit_45.setText(TEXT)


    def text(self):

        n = int(self.ui.spinBox_23.text())
        k = int(self.ui.spinBox_24.text())
        
        w = []
        TEXT = ""
        T = ""
        c = "⋅"

        for i in range(n, k+1):
            print(str(self.words[i-1][0]))
            w.append(str(self.words[i-1][0]))
            TEXT = TEXT + str(self.words[i-1][0]) + " " 

        if self.ui.checkBox.isChecked() == True:
            self.ui.textEdit_3.setText(TEXT)
            self.animation = QPropertyAnimation(self.ui.progressBar_4, b"value")
            self.animation.setDuration(500)
            self.animation.setStartValue(0)
            self.animation.setEndValue(100)
            self.animation.setEasingCurve(QtCore.QEasingCurve.Linear)
            self.animation.start()

        else:
            self.ui.textEdit_3.setText("")
            self.animation = QPropertyAnimation(self.ui.progressBar_4, b"value")
            self.animation.setDuration(500)
            self.animation.setStartValue(100)
            self.animation.setEndValue(0)
            self.animation.setEasingCurve(QtCore.QEasingCurve.Linear)
            self.animation.start()



    def gen(self):

        self.ui.checkBox.setChecked(False)

        a = int(self.ui.spinBox_6.text())
        b = int(self.ui.spinBox_5.text())
        c = int(self.ui.spinBox_4.text())
        d = int(self.ui.spinBox_3.text())



        self.animation = QPropertyAnimation(self.ui.progressBar_4, b"value")
        self.animation.setDuration(500)
        self.animation.setStartValue(0)
        self.animation.setEndValue(100)
        self.animation.setEasingCurve(QtCore.QEasingCurve.Linear)
        self.animation.start()


        words = [] 
        for _ in range(random.randint(a, b)): 
            word = ''.join(random.choice('абвгдеёжзийклмнопрстуфхцчшщъыьэюя') for _ in range(random.randint(c, d))) 
            if re.match("^[а-яА-Я]+$", word):  
                words.append(word) 
        

        self.ui.textEdit_3.setText(' '.join(words) + '.' )

        return ' '.join(words) + '.' 



    def sor_nutr(self, sequence): 

        words = sequence.split() 
        words.sort() 
        sorted_sequence = ' '.join(words) 
        return sorted_sequence 



    def sor(self): 

        self.animation = QPropertyAnimation(self.ui.progressBar_3, b"value")
        self.animation.setDuration(500)
        self.animation.setStartValue(0)
        self.animation.setEndValue(100)
        self.animation.setEasingCurve(QtCore.QEasingCurve.Linear)
        self.animation.start()
                
        a = self.ui.textEdit_3.toPlainText()

        sequence = a
        
        if not re.match("^[а-яА-Я\s.]", sequence): 
            self.ui.textEdit_4.setText("Введены неправильные значения. Для ввода доступна только кириллица.") 
        else: 
            sorted_sequence = self.sor_nutr(sequence) 
            self.ui.textEdit_4.setText(sorted_sequence) 



    def clear_gen(self):

        self.ui.textEdit_3.clear()


        self.animation = QPropertyAnimation(self.ui.progressBar_4, b"value")
        self.animation.setDuration(500)
        self.animation.setStartValue(100)
        self.animation.setEndValue(0)
        self.animation.setEasingCurve(QtCore.QEasingCurve.Linear)
        self.animation.start()



    def clear_sort(self):

        self.ui.textEdit_4.clear()


        self.animation = QPropertyAnimation(self.ui.progressBar_3, b"value")
        self.animation.setDuration(500)
        self.animation.setStartValue(100)
        self.animation.setEndValue(0)
        self.animation.setEasingCurve(QtCore.QEasingCurve.Linear)
        self.animation.start()



    def theme(self, q):        
        if self.q == False:
            self.ui.frame_2.setStyleSheet(u"background-color: rgb(223, 223, 223);")
            self.ui.label_19.setStyleSheet(u"background-color: rgb(223, 223, 223);")
            self.ui.label.setStyleSheet(u"background-color: rgb(223, 223, 223);")
            self.ui.label_18.setStyleSheet(u"background-color: rgb(223, 223, 223);")
            self.ui.label_2.setStyleSheet(u"background-color: rgb(223, 223, 223);")
            self.ui.label_3.setStyleSheet(u"background-color: rgb(223, 223, 223);")
            self.ui.label_31.setStyleSheet(u"background-color: rgb(223, 223, 223);")
            self.ui.label_56.setStyleSheet(u"background-color: rgb(223, 223, 223);")
    
            self.ui.progressBar_3.setStyleSheet(u"QProgressBar {background-color: rgb(170, 255, 255);color: #FFF;border-style:\
                                                 none;border-radius: 8px;text-align: center;}QProgressBar::chunk{	\
                                                background-color: rgb(255, 0, 127);margin: 10px;border-radius: 2px;}")
            self.ui.progressBar_4.setStyleSheet(u"QProgressBar {background-color: rgb(170, 255, 255);color: #FFF;border-style:\
                                                 none;border-radius: 8px;text-align: center;}QProgressBar::chunk{	\
                                                background-color: rgb(255, 0, 127);margin: 10px;border-radius: 2px;}")

            self.ui.label_20.setStyleSheet(u"color: rgb(0, 0, 0);background-color: rgb(170, 255, 255);")
            self.ui.label_61.setStyleSheet(u"color: rgb(0, 0, 0);background-color: rgb(170, 255, 255);")
            self.ui.label_17.setStyleSheet(u"background-color: rgb(170, 255, 255);border: none;border-radius: 25px;")

            self.ui.label_25.setStyleSheet(u"color: rgb(0, 0, 0);background-color: rgb(170, 255, 255);")
            self.ui.label_24.setStyleSheet(u"background-color: rgb(170, 255, 255);border: none;border-radius: 25px;")

            self.ui.btn_theme.setStyleSheet(u"background-color: rgb(170, 255, 255);border: none;border-radius: 25px;")
            self.ui.btn_word.setStyleSheet(u"background-color: rgb(170, 255, 255);border: none;border-radius: 25px;")
            self.ui.btn_word_3.setStyleSheet(u"background-color: rgb(170, 255, 255);border: none;border-radius: 25px;")

            self.ui.btn_gen.setStyleSheet(u"background-color: rgb(170, 255, 255);border: none;border-radius: 25px;")
            self.ui.btn_sort.setStyleSheet(u"background-color: rgb(170, 255, 255);border: none;border-radius: 25px;")
            self.ui.btn_clear_gen.setStyleSheet(u"background-color: rgb(170, 255, 255);border: none;border-radius: 25px;")
            self.ui.btn_clear_sort.setStyleSheet(u"background-color: rgb(170, 255, 255);border: none;border-radius: 25px;")

            self.ui.label_6.setStyleSheet(u"background-color: rgb(170, 255, 255);")
            self.ui.label_7.setStyleSheet(u"background-color: rgb(170, 255, 255);")
            self.ui.label_8.setStyleSheet(u"background-color: rgb(170, 255, 255);")
            self.ui.label_30.setStyleSheet(u"background-color: rgb(170, 255, 255);")
            self.ui.label_21.setStyleSheet(u"background-color: rgb(170, 255, 255);")
            self.ui.label_22.setStyleSheet(u"background-color: rgb(170, 255, 255);")
            self.ui.label_23.setStyleSheet(u"background-color: rgb(170, 255, 255);")
            
            self.ui.checkBox.setStyleSheet(u"background-color: rgb(170, 255, 255);")


            self.q = True

        else:
            self.ui.frame_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
            self.ui.label_19.setStyleSheet(u"background-color: rgb(33, 37, 43);")
            self.ui.label.setStyleSheet(u"background-color: rgb(33, 37, 43);")
            self.ui.label_18.setStyleSheet(u"background-color: rgb(33, 37, 43);")
            self.ui.label_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
            self.ui.label_3.setStyleSheet(u"background-color: rgb(33, 37, 43);")
            self.ui.label_31.setStyleSheet(u"background-color: rgb(33, 37, 43);")
            self.ui.label_56.setStyleSheet(u"background-color: rgb(33, 37, 43);")
           
            self.ui.progressBar_3.setStyleSheet(u"QProgressBar {background-color: rgb(68, 76, 86);color: #FFF;border-style:\
                                                 none;border-radius: 8px;text-align: center;}QProgressBar::chunk{	\
                                                background-color: rgb(255, 0, 127);margin: 10px;border-radius: 2px;}")
            self.ui.progressBar_4.setStyleSheet(u"QProgressBar {background-color: rgb(68, 76, 86);color: #FFF;border-style:\
                                                 none;border-radius: 8px;text-align: center;}QProgressBar::chunk{	\
                                                background-color: rgb(255, 0, 127);margin: 10px;border-radius: 2px;}")

            self.ui.label_20.setStyleSheet(u"color: #FFF;background-color: rgb(68, 76, 86);")
            self.ui.label_61.setStyleSheet(u"color: #FFF;background-color: rgb(68, 76, 86);")
            self.ui.label_17.setStyleSheet(u"background-color: rgb(68, 76, 86);border: none;border-radius: 25px;")
            self.ui.btn_theme.setStyleSheet(u"background-color: rgb(68, 76, 86);border: none;border-radius: 25px;color: #FFF")
            self.ui.btn_word.setStyleSheet(u"background-color: rgb(68, 76, 86);border: none;border-radius: 25px;color: #FFF")
            self.ui.btn_word_3.setStyleSheet(u"background-color: rgb(68, 76, 86);border: none;border-radius: 25px;color: #FFF")
      
            self.ui.btn_gen.setStyleSheet(u"background-color: rgb(68, 76, 86);border: none;border-radius: 25px;color: #FFF")
            self.ui.btn_sort.setStyleSheet(u"background-color: rgb(68, 76, 86);border: none;border-radius: 25px;color: #FFF")
            self.ui.btn_clear_gen.setStyleSheet(u"background-color: rgb(68, 76, 86);border: none;border-radius: 25px;color: #FFF")
            self.ui.btn_clear_sort.setStyleSheet(u"background-color: rgb(68, 76, 86);border: none;border-radius: 25px;color: #FFF")
            	
            self.ui.label_25.setStyleSheet(u"color: #FFF;background-color: rgb(68, 76, 86);")
            self.ui.label_24.setStyleSheet(u"background-color: rgb(68, 76, 86);border: none;border-radius: 25px;")

            self.ui.label_6.setStyleSheet(u"background-color: rgb(68, 76, 86);")
            self.ui.label_7.setStyleSheet(u"background-color: rgb(68, 76, 86);")
            self.ui.label_8.setStyleSheet(u"background-color: rgb(68, 76, 86);")
            self.ui.label_30.setStyleSheet(u"background-color: rgb(68, 76, 86);")
            self.ui.label_21.setStyleSheet(u"background-color: rgb(68, 76, 86);")
            self.ui.label_22.setStyleSheet(u"background-color: rgb(68, 76, 86);")
            self.ui.label_23.setStyleSheet(u"background-color: rgb(68, 76, 86);")

            self.ui.checkBox.setStyleSheet(u"color: #FFF;background-color: rgb(68, 76, 86);")

	
            self.q = False



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec_())
