# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dess.ui'
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
        self.FONVIBORMET = QtWidgets.QLabel(self.centralwidget)
        self.FONVIBORMET.setGeometry(QtCore.QRect(0, 0, 1081, 51))
        self.FONVIBORMET.setStyleSheet("background-color: rgb(255, 191, 64);")
        self.FONVIBORMET.setText("")
        self.FONVIBORMET.setObjectName("FONVIBORMET")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(35, 515, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 191, 64);\n"
"color: rgb(42, 68, 128);")
        self.pushButton.setObjectName("pushButton")
        self.FONRATIO = QtWidgets.QLabel(self.centralwidget)
        self.FONRATIO.setGeometry(QtCore.QRect(14, 70, 220, 511))
        self.FONRATIO.setStyleSheet("background-color: rgb(255, 191, 64);")
        self.FONRATIO.setText("")
        self.FONRATIO.setObjectName("FONRATIO")
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
        self.RIGHTFON_3 = QtWidgets.QLabel(self.centralwidget)
        self.RIGHTFON_3.setGeometry(QtCore.QRect(24, 80, 200, 491))
        self.RIGHTFON_3.setStyleSheet("background-color: rgb(255, 208, 115);")
        self.RIGHTFON_3.setText("")
        self.RIGHTFON_3.setObjectName("RIGHTFON_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(35, 260, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 191, 64);\n"
"color: rgb(42, 68, 128);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(35, 175, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 191, 64);\n"
"color: rgb(42, 68, 128);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(35, 430, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 191, 64);\n"
"color: rgb(42, 68, 128);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.FONVIBORMET_2 = QtWidgets.QLabel(self.centralwidget)
        self.FONVIBORMET_2.setGeometry(QtCore.QRect(250, 583, 581, 20))
        self.FONVIBORMET_2.setStyleSheet("background-color: rgb(255, 208, 115);")
        self.FONVIBORMET_2.setText("")
        self.FONVIBORMET_2.setObjectName("FONVIBORMET_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(35, 90, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 191, 64);\n"
"color: rgb(42, 68, 128);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(35, 345, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 191, 64);\n"
"color: rgb(42, 68, 128);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.RIGHTFON_4 = QtWidgets.QLabel(self.centralwidget)
        self.RIGHTFON_4.setGeometry(QtCore.QRect(9, 50, 1011, 20))
        self.RIGHTFON_4.setStyleSheet("background-color: rgb(255, 208, 115);")
        self.RIGHTFON_4.setText("")
        self.RIGHTFON_4.setObjectName("RIGHTFON_4")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(840, 70, 231, 511))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(255, 191, 64);")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.LEFTFON.raise_()
        self.FONRATIO.raise_()
        self.RIGHTFON.raise_()
        self.FONVIBORMET.raise_()
        self.SHAPKATEXT.raise_()
        self.VIBORMET_2.raise_()
        self.RIGHTFON_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.FON.raise_()
        self.FONVIBORMET_2.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton.raise_()
        self.RIGHTFON_4.raise_()
        self.textEdit.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.FON.setText(_translate("MainWindow", "`"))
        self.pushButton.setText(_translate("MainWindow", "ЛУЧШАЯ ФУНКЦИЯ"))
        self.SHAPKATEXT.setText(_translate("MainWindow", "МАМАЕВ РОСТИСЛАВ АА-23-07"))
        self.pushButton_2.setText(_translate("MainWindow", "СТЕПЕНЬ 4"))
        self.pushButton_3.setText(_translate("MainWindow", "СТЕПЕНЬ 3"))
        self.pushButton_4.setText(_translate("MainWindow", "SCIPY"))
        self.pushButton_5.setText(_translate("MainWindow", "СТЕПЕНЬ 2"))
        self.pushButton_6.setText(_translate("MainWindow", "СТЕПЕНЬ 5"))
