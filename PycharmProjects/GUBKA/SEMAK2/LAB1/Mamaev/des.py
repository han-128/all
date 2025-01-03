# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'des.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1077, 603)
        MainWindow.setMinimumSize(QtCore.QSize(1077, 603))
        MainWindow.setMaximumSize(QtCore.QSize(1077, 603))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.FON = QtWidgets.QLabel(self.centralwidget)
        self.FON.setGeometry(QtCore.QRect(250, 50, 581, 561))
        self.FON.setStyleSheet("background-color: rgb(6, 38, 111);")
        self.FON.setObjectName("FON")
        self.LEFTFON = QtWidgets.QLabel(self.centralwidget)
        self.LEFTFON.setGeometry(QtCore.QRect(0, 0, 250, 710))
        self.LEFTFON.setStyleSheet("background-color: rgb(255, 208, 115);")
        self.LEFTFON.setText("")
        self.LEFTFON.setObjectName("LEFTFON")
        self.VIBORMET = QtWidgets.QLabel(self.centralwidget)
        self.VIBORMET.setGeometry(QtCore.QRect(37, 63, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.VIBORMET.setFont(font)
        self.VIBORMET.setStyleSheet("color: rgb(42, 68, 128);")
        self.VIBORMET.setObjectName("VIBORMET")
        self.FONVIBORMET = QtWidgets.QLabel(self.centralwidget)
        self.FONVIBORMET.setGeometry(QtCore.QRect(0, 0, 1081, 51))
        self.FONVIBORMET.setStyleSheet("background-color: rgb(255, 191, 64);")
        self.FONVIBORMET.setText("")
        self.FONVIBORMET.setObjectName("FONVIBORMET")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 110, 181, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_1 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_1.setFont(font)
        self.radioButton_1.setStyleSheet("color: rgb(42, 68, 128);")
        self.radioButton_1.setObjectName("radioButton_1")
        self.verticalLayout.addWidget(self.radioButton_1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("color: rgb(42, 68, 128);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet("color: rgb(42, 68, 128);")
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setStyleSheet("color: rgb(42, 68, 128);")
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout.addWidget(self.radioButton_4)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(865, 540, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 191, 64);\n"
"color: rgb(42, 68, 128);")
        self.pushButton.setObjectName("pushButton")
        self.FONRATIO = QtWidgets.QLabel(self.centralwidget)
        self.FONRATIO.setGeometry(QtCore.QRect(35, 70, 180, 461))
        self.FONRATIO.setStyleSheet("background-color: rgb(255, 191, 64);")
        self.FONRATIO.setText("")
        self.FONRATIO.setObjectName("FONRATIO")
        self.FONRESHNET = QtWidgets.QLabel(self.centralwidget)
        self.FONRESHNET.setGeometry(QtCore.QRect(865, 70, 180, 441))
        self.FONRESHNET.setStyleSheet("background-color: rgb(255, 191, 64);")
        self.FONRESHNET.setText("")
        self.FONRESHNET.setObjectName("FONRESHNET")
        self.PRIRESHENII = QtWidgets.QLabel(self.centralwidget)
        self.PRIRESHENII.setGeometry(QtCore.QRect(910, 60, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.PRIRESHENII.setFont(font)
        self.PRIRESHENII.setStyleSheet("color: rgb(42, 68, 128);")
        self.PRIRESHENII.setObjectName("PRIRESHENII")
        self.METOD_TEMP = QtWidgets.QLabel(self.centralwidget)
        self.METOD_TEMP.setGeometry(QtCore.QRect(870, 110, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.METOD_TEMP.setFont(font)
        self.METOD_TEMP.setStyleSheet("color: rgb(42, 68, 128);")
        self.METOD_TEMP.setObjectName("METOD_TEMP")
        self.VIVODZNACH = QtWidgets.QLabel(self.centralwidget)
        self.VIVODZNACH.setGeometry(QtCore.QRect(740, 440, 161, 101))
        self.VIVODZNACH.setText("")
        self.VIVODZNACH.setObjectName("VIVODZNACH")
        self.SHAPKATEXT = QtWidgets.QLabel(self.centralwidget)
        self.SHAPKATEXT.setGeometry(QtCore.QRect(410, -20, 241, 91))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.SHAPKATEXT.setFont(font)
        self.SHAPKATEXT.setStyleSheet("color: rgb(42, 68, 128);")
        self.SHAPKATEXT.setObjectName("SHAPKATEXT")
        self.RIGHTFON = QtWidgets.QLabel(self.centralwidget)
        self.RIGHTFON.setGeometry(QtCore.QRect(830, -30, 250, 710))
        self.RIGHTFON.setStyleSheet("background-color: rgb(255, 208, 115);")
        self.RIGHTFON.setText("")
        self.RIGHTFON.setObjectName("RIGHTFON")
        self.VIBORMET_2 = QtWidgets.QLabel(self.centralwidget)
        self.VIBORMET_2.setGeometry(QtCore.QRect(830, -20, 241, 91))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.VIBORMET_2.setFont(font)
        self.VIBORMET_2.setStyleSheet("color: rgb(42, 68, 128);")
        self.VIBORMET_2.setText("")
        self.VIBORMET_2.setObjectName("VIBORMET_2")
        self.VIBORMET_3 = QtWidgets.QLabel(self.centralwidget)
        self.VIBORMET_3.setGeometry(QtCore.QRect(45, 280, 161, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.VIBORMET_3.setFont(font)
        self.VIBORMET_3.setStyleSheet("color: rgb(42, 68, 128);")
        self.VIBORMET_3.setObjectName("VIBORMET_3")
        self.RIGHTFON_2 = QtWidgets.QLabel(self.centralwidget)
        self.RIGHTFON_2.setGeometry(QtCore.QRect(0, 280, 1081, 31))
        self.RIGHTFON_2.setStyleSheet("background-color: rgb(255, 208, 115);")
        self.RIGHTFON_2.setText("")
        self.RIGHTFON_2.setObjectName("RIGHTFON_2")
        self.RIGHTFON_3 = QtWidgets.QLabel(self.centralwidget)
        self.RIGHTFON_3.setGeometry(QtCore.QRect(-10, 510, 1081, 31))
        self.RIGHTFON_3.setStyleSheet("background-color: rgb(255, 208, 115);")
        self.RIGHTFON_3.setText("")
        self.RIGHTFON_3.setObjectName("RIGHTFON_3")
        self.VIBORMET_4 = QtWidgets.QLabel(self.centralwidget)
        self.VIBORMET_4.setGeometry(QtCore.QRect(45, 320, 241, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.VIBORMET_4.setFont(font)
        self.VIBORMET_4.setStyleSheet("color: rgb(42, 68, 128);")
        self.VIBORMET_4.setObjectName("VIBORMET_4")
        self.RIGHTFON_4 = QtWidgets.QLabel(self.centralwidget)
        self.RIGHTFON_4.setGeometry(QtCore.QRect(-30, 340, 1091, 5))
        self.RIGHTFON_4.setStyleSheet("background-color: rgb(255, 208, 115);")
        self.RIGHTFON_4.setText("")
        self.RIGHTFON_4.setObjectName("RIGHTFON_4")
        self.RIGHTFON_5 = QtWidgets.QLabel(self.centralwidget)
        self.RIGHTFON_5.setGeometry(QtCore.QRect(-10, 100, 1200, 5))
        self.RIGHTFON_5.setStyleSheet("background-color: rgb(255, 208, 115);")
        self.RIGHTFON_5.setText("")
        self.RIGHTFON_5.setObjectName("RIGHTFON_5")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(50, 380, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox.setFont(font)
        self.spinBox.setStyleSheet("background-color: rgb(255, 208, 115);\n"
"color: rgb(42, 68, 128);")
        self.spinBox.setMinimum(-100)
        self.spinBox.setMaximum(100)
        self.spinBox.setObjectName("spinBox")
        self.VIBORMET_5 = QtWidgets.QLabel(self.centralwidget)
        self.VIBORMET_5.setGeometry(QtCore.QRect(45, 370, 241, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.VIBORMET_5.setFont(font)
        self.VIBORMET_5.setStyleSheet("color: rgb(42, 68, 128);")
        self.VIBORMET_5.setObjectName("VIBORMET_5")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(50, 430, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setStyleSheet("background-color: rgb(255, 208, 115);\n"
"color: rgb(42, 68, 128);")
        self.spinBox_2.setMinimum(-100)
        self.spinBox_2.setMaximum(100)
        self.spinBox_2.setObjectName("spinBox_2")
        self.VIBORMET_6 = QtWidgets.QLabel(self.centralwidget)
        self.VIBORMET_6.setGeometry(QtCore.QRect(45, 420, 241, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.VIBORMET_6.setFont(font)
        self.VIBORMET_6.setStyleSheet("color: rgb(42, 68, 128);")
        self.VIBORMET_6.setObjectName("VIBORMET_6")
        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(50, 480, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_3.setFont(font)
        self.spinBox_3.setStyleSheet("background-color: rgb(255, 208, 115);\n"
"color: rgb(42, 68, 128);")
        self.spinBox_3.setObjectName("spinBox_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 480, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(42, 68, 128);")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(885, 430, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 191, 64);\n"
"color: rgb(42, 68, 128);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(885, 390, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 191, 64);\n"
"color: rgb(42, 68, 128);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.VIBORMET_9 = QtWidgets.QLabel(self.centralwidget)
        self.VIBORMET_9.setGeometry(QtCore.QRect(885, 304, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.VIBORMET_9.setFont(font)
        self.VIBORMET_9.setStyleSheet("color: rgb(42, 68, 128);")
        self.VIBORMET_9.setObjectName("VIBORMET_9")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(35, 540, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 191, 64);\n"
"color: rgb(42, 68, 128);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setGeometry(QtCore.QRect(874, 165, 161, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textBrowser.setStatusTip("")
        self.textBrowser.setStyleSheet("background-color: rgb(255, 191, 64);\n"
"color: rgb(42, 68, 128);")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setLineWidth(0)
        self.textBrowser.setObjectName("textBrowser")
        self.FONVIBORMET_2 = QtWidgets.QLabel(self.centralwidget)
        self.FONVIBORMET_2.setGeometry(QtCore.QRect(250, 583, 581, 20))
        self.FONVIBORMET_2.setStyleSheet("background-color: rgb(255, 208, 115);")
        self.FONVIBORMET_2.setText("")
        self.FONVIBORMET_2.setObjectName("FONVIBORMET_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(885, 350, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 191, 64);\n"
"color: rgb(42, 68, 128);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.METOD_TEMP_2 = QtWidgets.QLabel(self.centralwidget)
        self.METOD_TEMP_2.setGeometry(QtCore.QRect(870, 130, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.METOD_TEMP_2.setFont(font)
        self.METOD_TEMP_2.setStyleSheet("color: rgb(42, 68, 128);")
        self.METOD_TEMP_2.setObjectName("METOD_TEMP_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(885, 470, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 191, 64);\n"
"color: rgb(42, 68, 128);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.LEFTFON.raise_()
        self.FONRATIO.raise_()
        self.verticalLayoutWidget.raise_()
        self.VIVODZNACH.raise_()
        self.RIGHTFON.raise_()
        self.FONVIBORMET.raise_()
        self.SHAPKATEXT.raise_()
        self.VIBORMET_2.raise_()
        self.pushButton.raise_()
        self.FONRESHNET.raise_()
        self.PRIRESHENII.raise_()
        self.METOD_TEMP.raise_()
        self.VIBORMET_3.raise_()
        self.RIGHTFON_2.raise_()
        self.RIGHTFON_3.raise_()
        self.VIBORMET_4.raise_()
        self.RIGHTFON_4.raise_()
        self.RIGHTFON_5.raise_()
        self.VIBORMET_5.raise_()
        self.VIBORMET_6.raise_()
        self.label.raise_()
        self.VIBORMET_9.raise_()
        self.pushButton_4.raise_()
        self.textBrowser.raise_()
        self.spinBox_3.raise_()
        self.spinBox_2.raise_()
        self.spinBox.raise_()
        self.VIBORMET.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.FON.raise_()
        self.FONVIBORMET_2.raise_()
        self.pushButton_5.raise_()
        self.METOD_TEMP_2.raise_()
        self.pushButton_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.FON.setText(_translate("MainWindow", "`"))
        self.VIBORMET.setText(_translate("MainWindow", "ВЫБЕРИТЕ МЕТОД РЕШЕНИЯ"))
        self.radioButton_1.setText(_translate("MainWindow", "ДИХОТОМИИ"))
        self.radioButton_2.setText(_translate("MainWindow", "ХОРД"))
        self.radioButton_3.setText(_translate("MainWindow", "КАСАТЕЛЬНЫХ"))
        self.radioButton_4.setText(_translate("MainWindow", "ИТЕРАЦИЙ"))
        self.pushButton.setText(_translate("MainWindow", "ВЫХОД"))
        self.PRIRESHENII.setText(_translate("MainWindow", "РЕЗУЛЬТАТЫ"))
        self.METOD_TEMP.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">ПРИ РЕШЕНИИ МЕТОДОМ</p></body></html>"))
        self.SHAPKATEXT.setText(_translate("MainWindow", "МАМАЕВ РОСТИСЛАВ АА-23-07"))
        self.VIBORMET_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">ВВЕДИТЕ ЗНАЧЕНИЯ</p></body></html>"))
        self.VIBORMET_4.setText(_translate("MainWindow", "ПЕРВАЯ ГРАНИЦА"))
        self.VIBORMET_5.setText(_translate("MainWindow", "ВТОРАЯ ГРАНИЦА"))
        self.VIBORMET_6.setText(_translate("MainWindow", "ТОЧНОСТЬ Е"))
        self.label.setText(_translate("MainWindow", "Х 0.001"))
        self.pushButton_2.setText(_translate("MainWindow", "EXCEL"))
        self.pushButton_3.setText(_translate("MainWindow", "MATLAB"))
        self.VIBORMET_9.setText(_translate("MainWindow", "ДОП ВОЗМОЖНОСТИ"))
        self.pushButton_4.setText(_translate("MainWindow", "ВЫЧИСЛИТЬ"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_5.setText(_translate("MainWindow", "SCIPY"))
        self.METOD_TEMP_2.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_6.setText(_translate("MainWindow", "ГРАФИК"))