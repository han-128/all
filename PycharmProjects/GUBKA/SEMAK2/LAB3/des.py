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
        MainWindow.resize(400, 490)
        MainWindow.setMinimumSize(QtCore.QSize(400, 490))
        MainWindow.setMaximumSize(QtCore.QSize(400, 490))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.FON = QtWidgets.QLabel(self.centralwidget)
        self.FON.setGeometry(QtCore.QRect(200, 0, 711, 711))
        self.FON.setStyleSheet("background-color: rgb(34, 223, 248);")
        self.FON.setObjectName("FON")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 90, 164, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_2 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("color: rgb(84, 44, 68);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 1, 0, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("color: rgb(84, 44, 68);")
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 0, 0, 1, 1)
        self.FON_2 = QtWidgets.QLabel(self.centralwidget)
        self.FON_2.setGeometry(QtCore.QRect(10, 90, 180, 90))
        self.FON_2.setStyleSheet("background-color: rgb(213, 189, 169);")
        self.FON_2.setObjectName("FON_2")
        self.FON_3 = QtWidgets.QLabel(self.centralwidget)
        self.FON_3.setGeometry(QtCore.QRect(0, 0, 200, 720))
        self.FON_3.setStyleSheet("background-color: rgb(4, 111, 135);")
        self.FON_3.setObjectName("FON_3")
        self.FON_4 = QtWidgets.QLabel(self.centralwidget)
        self.FON_4.setGeometry(QtCore.QRect(0, 0, 921, 30))
        self.FON_4.setStyleSheet("background-color: rgb(213, 189, 169);")
        self.FON_4.setObjectName("FON_4")
        self.FON_5 = QtWidgets.QLabel(self.centralwidget)
        self.FON_5.setGeometry(QtCore.QRect(10, 40, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.FON_5.setFont(font)
        self.FON_5.setStyleSheet("background-color: rgb(213, 189, 169);\n"
"color: rgb(84, 44, 68);")
        self.FON_5.setObjectName("FON_5")
        self.SHAPKATEXT = QtWidgets.QLabel(self.centralwidget)
        self.SHAPKATEXT.setGeometry(QtCore.QRect(80, -30, 241, 91))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.SHAPKATEXT.setFont(font)
        self.SHAPKATEXT.setStyleSheet("color: rgb(84, 44, 68);")
        self.SHAPKATEXT.setObjectName("SHAPKATEXT")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 190, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color: rgb(84, 44, 68);\n"
"background-color: rgb(213, 189, 169);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 340, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("color: rgb(84, 44, 68);\n"
"background-color: rgb(213, 189, 169);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 390, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("color: rgb(84, 44, 68);\n"
"background-color: rgb(213, 189, 169);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 240, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("color: rgb(84, 44, 68);\n"
"background-color: rgb(213, 189, 169);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 440, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("color: rgb(84, 44, 68);\n"
"background-color: rgb(213, 189, 169);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(210, 40, 181, 441))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 290, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("color: rgb(84, 44, 68);\n"
"background-color: rgb(213, 189, 169);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.FON.raise_()
        self.FON_3.raise_()
        self.FON_2.raise_()
        self.gridLayoutWidget.raise_()
        self.FON_4.raise_()
        self.FON_5.raise_()
        self.SHAPKATEXT.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_9.raise_()
        self.textBrowser.raise_()
        self.pushButton_10.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.FON.setText(_translate("MainWindow", "`"))
        self.radioButton_2.setText(_translate("MainWindow", "Гаусса-Жордана"))
        self.radioButton.setText(_translate("MainWindow", "Гаусса"))
        self.FON_2.setText(_translate("MainWindow", "`"))
        self.FON_3.setText(_translate("MainWindow", "`"))
        self.FON_4.setText(_translate("MainWindow", "`"))
        self.FON_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">ВЫБЕРИТЕ МЕТОД </p></body></html>"))
        self.SHAPKATEXT.setText(_translate("MainWindow", "МАМАЕВ РОСТИСЛАВ АА-23-07"))
        self.pushButton_4.setText(_translate("MainWindow", "ВЫЧИСЛИТЬ"))
        self.pushButton_5.setText(_translate("MainWindow", "EXCEL"))
        self.pushButton_6.setText(_translate("MainWindow", "MATLAB"))
        self.pushButton_7.setText(_translate("MainWindow", "ВЫВОД В EXCEL"))
        self.pushButton_9.setText(_translate("MainWindow", "ВЫХОД"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_10.setText(_translate("MainWindow", "ВЫВОД В TXT"))
