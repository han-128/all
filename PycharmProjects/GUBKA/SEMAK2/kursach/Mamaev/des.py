# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'desBDOmpE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1100, 786)
        MainWindow.setMinimumSize(QSize(1100, 600))
        MainWindow.setMaximumSize(QSize(1100, 1000))
        MainWindow.setStyleSheet(u"	border-style: none;\n"
"	border-radius: 45px;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, -20, 821, 631))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(-10, 0, 1071, 841))
        self.frame_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.textBrowser = QTextBrowser(self.frame_2)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(290, 50, 540, 190))
        self.textBrowser.setStyleSheet(u"border-style: none;\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 40px;")
        self.btn_gen = QPushButton(self.frame_2)
        self.btn_gen.setObjectName(u"btn_gen")
        self.btn_gen.setGeometry(QRect(290, 250, 200, 50))
        self.btn_gen.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_gen.setFont(font)
        self.btn_gen.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(68, 76, 86);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	color: #FFF\n"
"}")
        self.btn_sort = QPushButton(self.frame_2)
        self.btn_sort.setObjectName(u"btn_sort")
        self.btn_sort.setGeometry(QRect(290, 340, 200, 50))
        self.btn_sort.setMinimumSize(QSize(0, 40))
        self.btn_sort.setFont(font)
        self.btn_sort.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(68, 76, 86);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	color: #FFF\n"
"}")
        self.textBrowser_2 = QTextBrowser(self.frame_2)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(290, 400, 540, 190))
        self.textBrowser_2.setStyleSheet(u"border-style: none;\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 40px;")
        self.menuu = QFrame(self.frame_2)
        self.menuu.setObjectName(u"menuu")
        self.menuu.setGeometry(QRect(40, 50, 230, 540))
        self.menuu.setStyleSheet(u"background-color: rgb(255, 170, 127);")
        self.menuu.setFrameShape(QFrame.StyledPanel)
        self.menuu.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.menuu)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 210, 520))
        self.label.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"	border-style: none;\n"
"	border-radius: 35px;")
        self.label_4 = QLabel(self.menuu)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(-20, 95, 225, 70))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"border-style: none;\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 30px;")
        self.textEdit = QTextEdit(self.menuu)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(-16, 175, 81, 35))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.textEdit.setFont(font2)
        self.textEdit.setStyleSheet(u"border-style: none;\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 15px;")
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_2 = QTextEdit(self.menuu)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(-11, 220, 161, 35))
        self.textEdit_2.setFont(font2)
        self.textEdit_2.setStyleSheet(u"border-style: none;\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 17px;")
        self.textEdit_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.label_5 = QLabel(self.menuu)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(25, 280, 225, 70))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"border-style: none;\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 30px;")
        self.spinBox_3 = QSpinBox(self.menuu)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setGeometry(QRect(75, 405, 61, 35))
        self.spinBox_3.setFont(font2)
        self.spinBox_3.setStyleSheet(u"border-style: none;\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 15px;")
        self.spinBox_3.setAlignment(Qt.AlignCenter)
        self.spinBox_3.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_3.setMinimum(2)
        self.spinBox_3.setMaximum(10)
        self.spinBox_3.setValue(10)
        self.textEdit_5 = QTextEdit(self.menuu)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(-21, 360, 171, 35))
        self.textEdit_5.setFont(font2)
        self.textEdit_5.setStyleSheet(u"border-style: none;\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 17px;")
        self.textEdit_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.spinBox_4 = QSpinBox(self.menuu)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setGeometry(QRect(160, 360, 60, 35))
        self.spinBox_4.setFont(font2)
        self.spinBox_4.setStyleSheet(u"border-style: none;\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 17px;")
        self.spinBox_4.setAlignment(Qt.AlignCenter)
        self.spinBox_4.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_4.setMinimum(1)
        self.spinBox_4.setMaximum(9)
        self.spinBox_4.setValue(1)
        self.textEdit_6 = QTextEdit(self.menuu)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setGeometry(QRect(-6, 405, 71, 35))
        self.textEdit_6.setFont(font2)
        self.textEdit_6.setStyleSheet(u"border-style: none;\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 15px;")
        self.textEdit_6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_6.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_7 = QTextEdit(self.menuu)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setGeometry(QRect(205, 360, 130, 35))
        self.textEdit_7.setStyleSheet(u"")
        self.spinBox_5 = QSpinBox(self.menuu)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setGeometry(QRect(160, 220, 60, 35))
        self.spinBox_5.setFont(font2)
        self.spinBox_5.setStyleSheet(u"border-style: none;\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 17px;")
        self.spinBox_5.setAlignment(Qt.AlignCenter)
        self.spinBox_5.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_5.setMinimum(2)
        self.spinBox_5.setMaximum(90)
        self.spinBox_5.setValue(90)
        self.textEdit_8 = QTextEdit(self.menuu)
        self.textEdit_8.setObjectName(u"textEdit_8")
        self.textEdit_8.setGeometry(QRect(205, 220, 130, 35))
        self.textEdit_8.setStyleSheet(u"")
        self.textEdit_9 = QTextEdit(self.menuu)
        self.textEdit_9.setObjectName(u"textEdit_9")
        self.textEdit_9.setGeometry(QRect(120, 405, 151, 35))
        self.textEdit_9.setStyleSheet(u"")
        self.spinBox_6 = QSpinBox(self.menuu)
        self.spinBox_6.setObjectName(u"spinBox_6")
        self.spinBox_6.setGeometry(QRect(75, 175, 51, 35))
        self.spinBox_6.setFont(font2)
        self.spinBox_6.setStyleSheet(u"border-style: none;\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 15px;")
        self.spinBox_6.setAlignment(Qt.AlignCenter)
        self.spinBox_6.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_6.setMinimum(1)
        self.spinBox_6.setMaximum(89)
        self.textEdit_10 = QTextEdit(self.menuu)
        self.textEdit_10.setObjectName(u"textEdit_10")
        self.textEdit_10.setGeometry(QRect(110, 175, 141, 35))
        self.textEdit_10.setStyleSheet(u"")
        self.label_6 = QLabel(self.menuu)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 265, 210, 5))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"border-style: none;\n"
"	background-color: rgb(68, 76, 86);\n"
"border-radius: 30px;")
        self.label_7 = QLabel(self.menuu)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 450, 210, 5))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"border-style: none;\n"
"	background-color: rgb(68, 76, 86);\n"
"border-radius: 30px;")
        self.btn_theme = QPushButton(self.menuu)
        self.btn_theme.setObjectName(u"btn_theme")
        self.btn_theme.setGeometry(QRect(20, 470, 190, 50))
        self.btn_theme.setMinimumSize(QSize(0, 40))
        self.btn_theme.setFont(font2)
        self.btn_theme.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(68, 76, 86);\n"
"	border: none;\n"
"	border-radius: 25px;\n"
"	color: #FFF\n"
"}")
        self.label_8 = QLabel(self.menuu)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 80, 210, 5))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"border-style: none;\n"
"	background-color: rgb(68, 76, 86);\n"
"border-radius: 30px;")
        self.label_17 = QLabel(self.menuu)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(20, 20, 190, 50))
        self.label_17.setFont(font)
        self.label_17.setStyleSheet(u"	background-color: rgb(68, 76, 86);\n"
"	border: none;\n"
"	border-radius: 25px;\n"
"	color: #FFF")
        self.label_20 = QLabel(self.menuu)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(50, 20, 130, 40))
        self.label_20.setFont(font)
        self.label_20.setStyleSheet(u"	background-color: rgb(68, 76, 86);\n"
"	border: none;\n"
"	border-radius: 25px;\n"
"	color: #FFF")
        self.label.raise_()
        self.label_4.raise_()
        self.textEdit.raise_()
        self.textEdit_2.raise_()
        self.label_5.raise_()
        self.textEdit_5.raise_()
        self.spinBox_4.raise_()
        self.textEdit_6.raise_()
        self.textEdit_7.raise_()
        self.textEdit_8.raise_()
        self.textEdit_9.raise_()
        self.textEdit_10.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.btn_theme.raise_()
        self.spinBox_3.raise_()
        self.spinBox_6.raise_()
        self.label_8.raise_()
        self.label_17.raise_()
        self.label_20.raise_()
        self.spinBox_5.raise_()
        self.textEdit_3 = QTextEdit(self.frame_2)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(290, 79, 540, 161))
        self.textEdit_3.setFont(font2)
        self.textEdit_3.setStyleSheet(u"border-style: none;\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 40px;")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 80, 521, 3))
        self.label_2.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"	border-style: none;\n"
"	border-radius: 35px;")
        self.textEdit_4 = QTextEdit(self.frame_2)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(290, 430, 540, 161))
        self.textEdit_4.setFont(font2)
        self.textEdit_4.setStyleSheet(u"border-style: none;\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 40px;")
        self.textEdit_4.setReadOnly(True)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(300, 430, 521, 3))
        self.label_3.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"	border-style: none;\n"
"	border-radius: 35px;")
        self.progressBar_3 = QProgressBar(self.frame_2)
        self.progressBar_3.setObjectName(u"progressBar_3")
        self.progressBar_3.setGeometry(QRect(455, 357, 210, 16))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_3.sizePolicy().hasHeightForWidth())
        self.progressBar_3.setSizePolicy(sizePolicy)
        self.progressBar_3.setLayoutDirection(Qt.LeftToRight)
        self.progressBar_3.setStyleSheet(u"QProgressBar {	\n"
"	background-color: rgb(68, 76, 86);\n"
"	color: #FFF;\n"
"	border-style: none;\n"
"	border-radius: 8px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{	\n"
"	background-color: rgb(255, 0, 127);\n"
"	margin: 10px;\n"
"	border-radius: 2px;\n"
"}")
        self.progressBar_3.setValue(24)
        self.progressBar_3.setTextVisible(False)
        self.progressBar_3.setOrientation(Qt.Horizontal)
        self.progressBar_4 = QProgressBar(self.frame_2)
        self.progressBar_4.setObjectName(u"progressBar_4")
        self.progressBar_4.setGeometry(QRect(455, 267, 210, 16))
        sizePolicy.setHeightForWidth(self.progressBar_4.sizePolicy().hasHeightForWidth())
        self.progressBar_4.setSizePolicy(sizePolicy)
        self.progressBar_4.setStyleSheet(u"QProgressBar {	\n"
"	background-color: rgb(68, 76, 86);\n"
"	color: #FFF;\n"
"	border-style: none;\n"
"	border-radius: 8px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{	\n"
"	background-color: rgb(255, 0, 127);\n"
"	margin: 10px;\n"
"	border-radius: 2px;\n"
"}")
        self.progressBar_4.setValue(24)
        self.progressBar_4.setTextVisible(False)
        self.btn_clear_sort = QPushButton(self.frame_2)
        self.btn_clear_sort.setObjectName(u"btn_clear_sort")
        self.btn_clear_sort.setGeometry(QRect(630, 340, 200, 50))
        self.btn_clear_sort.setMinimumSize(QSize(0, 40))
        self.btn_clear_sort.setFont(font)
        self.btn_clear_sort.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(68, 76, 86);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	color: #FFF\n"
"}")
        self.btn_clear_gen = QPushButton(self.frame_2)
        self.btn_clear_gen.setObjectName(u"btn_clear_gen")
        self.btn_clear_gen.setGeometry(QRect(630, 250, 200, 50))
        self.btn_clear_gen.setMinimumSize(QSize(0, 40))
        self.btn_clear_gen.setFont(font)
        self.btn_clear_gen.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(68, 76, 86);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	color: #FFF\n"
"}")
        self.label_30 = QLabel(self.frame_2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(290, 315, 540, 5))
        self.label_30.setFont(font)
        self.label_30.setStyleSheet(u"border-style: none;\n"
"	background-color: rgb(68, 76, 86);\n"
"border-radius: 5px;")
        self.textBrowser_2.raise_()
        self.textBrowser.raise_()
        self.btn_sort.raise_()
        self.btn_clear_gen.raise_()
        self.btn_clear_sort.raise_()
        self.progressBar_3.raise_()
        self.menuu.raise_()
        self.textEdit_3.raise_()
        self.btn_gen.raise_()
        self.textEdit_4.raise_()
        self.label_30.raise_()
        self.progressBar_4.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.menuu_3 = QFrame(self.centralwidget)
        self.menuu_3.setObjectName(u"menuu_3")
        self.menuu_3.setGeometry(QRect(840, 30, 230, 540))
        self.menuu_3.setStyleSheet(u"background-color: rgb(255, 170, 127);")
        self.menuu_3.setFrameShape(QFrame.StyledPanel)
        self.menuu_3.setFrameShadow(QFrame.Raised)
        self.label_18 = QLabel(self.menuu_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 10, 210, 520))
        self.label_18.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"	border-style: none;\n"
"	border-radius: 35px;")
        self.label_21 = QLabel(self.menuu_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(10, 265, 210, 5))
        self.label_21.setFont(font)
        self.label_21.setStyleSheet(u"border-style: none;\n"
"	background-color: rgb(68, 76, 86);\n"
"border-radius: 30px;")
        self.label_22 = QLabel(self.menuu_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 450, 210, 5))
        self.label_22.setFont(font)
        self.label_22.setStyleSheet(u"border-style: none;\n"
"	background-color: rgb(68, 76, 86);\n"
"border-radius: 30px;")
        self.label_23 = QLabel(self.menuu_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(10, 80, 210, 5))
        self.label_23.setFont(font)
        self.label_23.setStyleSheet(u"border-style: none;\n"
"	background-color: rgb(68, 76, 86);\n"
"border-radius: 30px;")
        self.label_25 = QLabel(self.menuu_3)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(50, 20, 130, 40))
        self.label_25.setFont(font)
        self.label_25.setStyleSheet(u"	background-color: rgb(68, 76, 86);\n"
"	border: none;\n"
"	border-radius: 25px;\n"
"	color: #FFF")
        self.label_24 = QLabel(self.menuu_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(20, 20, 190, 50))
        self.label_24.setFont(font)
        self.label_24.setStyleSheet(u"	background-color: rgb(68, 76, 86);\n"
"	border: none;\n"
"	border-radius: 25px;\n"
"	color: #FFF")
        self.label_26 = QLabel(self.menuu_3)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(25, 95, 225, 70))
        self.label_26.setFont(font1)
        self.label_26.setStyleSheet(u"border-style: none;\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 30px;")
        self.label_27 = QLabel(self.menuu_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(-20, 280, 225, 70))
        self.label_27.setFont(font1)
        self.label_27.setStyleSheet(u"border-style: none;\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 30px;")
        self.label_28 = QLabel(self.menuu_3)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(-20, 180, 225, 70))
        self.label_28.setFont(font1)
        self.label_28.setStyleSheet(u"border-style: none;\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 30px;")
        self.label_29 = QLabel(self.menuu_3)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(30, 370, 225, 70))
        self.label_29.setFont(font1)
        self.label_29.setStyleSheet(u"border-style: none;\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 30px;")
        self.btn_word = QPushButton(self.menuu_3)
        self.btn_word.setObjectName(u"btn_word")
        self.btn_word.setGeometry(QRect(20, 470, 190, 50))
        self.btn_word.setMinimumSize(QSize(0, 40))
        self.btn_word.setFont(font2)
        self.btn_word.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(68, 76, 86);\n"
"	border: none;\n"
"	border-radius: 25px;\n"
"	color: #FFF\n"
"}")
        self.label_18.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.label_25.raise_()
        self.label_26.raise_()
        self.label_27.raise_()
        self.label_28.raise_()
        self.label_29.raise_()
        self.btn_word.raise_()
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(820, -40, 311, 871))
        self.label_19.setStyleSheet(u"\n"
"background-color: rgb(33, 37, 43);\n"
"")
        self.label_31 = QLabel(self.centralwidget)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(-30, 600, 1101, 341))
        self.label_31.setStyleSheet(u"\n"
"background-color: rgb(33, 37, 43);\n"
"")
        self.menuu_4 = QFrame(self.centralwidget)
        self.menuu_4.setObjectName(u"menuu_4")
        self.menuu_4.setGeometry(QRect(30, 600, 1041, 161))
        self.menuu_4.setStyleSheet(u"background-color: rgb(255, 170, 127);")
        self.menuu_4.setFrameShape(QFrame.StyledPanel)
        self.menuu_4.setFrameShadow(QFrame.Raised)
        self.label_57 = QLabel(self.menuu_4)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(10, 265, 210, 5))
        self.label_57.setFont(font)
        self.label_57.setStyleSheet(u"border-style: none;\n"
"	background-color: rgb(68, 76, 86);\n"
"border-radius: 30px;")
        self.label_58 = QLabel(self.menuu_4)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setGeometry(QRect(10, 450, 210, 5))
        self.label_58.setFont(font)
        self.label_58.setStyleSheet(u"border-style: none;\n"
"	background-color: rgb(68, 76, 86);\n"
"border-radius: 30px;")
        self.label_60 = QLabel(self.menuu_4)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(50, 20, 130, 40))
        self.label_60.setFont(font)
        self.label_60.setStyleSheet(u"	background-color: rgb(68, 76, 86);\n"
"	border: none;\n"
"	border-radius: 25px;\n"
"	color: #FFF")
        self.label_61 = QLabel(self.menuu_4)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(20, 20, 180, 120))
        self.label_61.setFont(font)
        self.label_61.setStyleSheet(u"	background-color: rgb(68, 76, 86);\n"
"	border: none;\n"
"	border-radius: 25px;\n"
"	color: #FFF")
        self.label_63 = QLabel(self.menuu_4)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(-20, 280, 225, 70))
        self.label_63.setFont(font1)
        self.label_63.setStyleSheet(u"border-style: none;\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 30px;")
        self.label_64 = QLabel(self.menuu_4)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(-20, 180, 225, 70))
        self.label_64.setFont(font1)
        self.label_64.setStyleSheet(u"border-style: none;\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 30px;")
        self.label_65 = QLabel(self.menuu_4)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setGeometry(QRect(30, 370, 225, 70))
        self.label_65.setFont(font1)
        self.label_65.setStyleSheet(u"border-style: none;\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 30px;")
        self.btn_word_2 = QPushButton(self.menuu_4)
        self.btn_word_2.setObjectName(u"btn_word_2")
        self.btn_word_2.setGeometry(QRect(20, 470, 190, 50))
        self.btn_word_2.setMinimumSize(QSize(0, 40))
        self.btn_word_2.setFont(font2)
        self.btn_word_2.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(68, 76, 86);\n"
"	border: none;\n"
"	border-radius: 25px;\n"
"	color: #FFF\n"
"}")
        self.label_56 = QLabel(self.menuu_4)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(10, 10, 1021, 141))
        self.label_56.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"	border-style: none;\n"
"	border-radius: 35px;")
        self.checkBox = QCheckBox(self.menuu_4)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(40, 20, 170, 120))
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet(u"	background-color: rgb(68, 76, 86);\n"
"	border: none;\n"
"	border-radius: 25px;\n"
"	color: #FFF")
        self.btn_word_3 = QPushButton(self.menuu_4)
        self.btn_word_3.setObjectName(u"btn_word_3")
        self.btn_word_3.setGeometry(QRect(830, 20, 190, 120))
        self.btn_word_3.setMinimumSize(QSize(0, 40))
        self.btn_word_3.setFont(font2)
        self.btn_word_3.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(68, 76, 86);\n"
"	border: none;\n"
"	border-radius: 25px;\n"
"	color: #FFF\n"
"}")
        self.spinBox_23 = QSpinBox(self.menuu_4)
        self.spinBox_23.setObjectName(u"spinBox_23")
        self.spinBox_23.setGeometry(QRect(230, 90, 90, 40))
        self.spinBox_23.setFont(font2)
        self.spinBox_23.setStyleSheet(u"border-style: none;\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 15px;")
        self.spinBox_23.setAlignment(Qt.AlignCenter)
        self.spinBox_23.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_23.setMinimum(1)
        self.spinBox_23.setMaximum(89)
        self.spinBox_24 = QSpinBox(self.menuu_4)
        self.spinBox_24.setObjectName(u"spinBox_24")
        self.spinBox_24.setGeometry(QRect(720, 90, 90, 40))
        self.spinBox_24.setFont(font2)
        self.spinBox_24.setStyleSheet(u"border-style: none;\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 15px;")
        self.spinBox_24.setAlignment(Qt.AlignCenter)
        self.spinBox_24.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_24.setMinimum(1)
        self.spinBox_24.setMaximum(90)
        self.textEdit_43 = QTextEdit(self.menuu_4)
        self.textEdit_43.setObjectName(u"textEdit_43")
        self.textEdit_43.setGeometry(QRect(230, 30, 90, 40))
        self.textEdit_43.setFont(font2)
        self.textEdit_43.setStyleSheet(u"border-style: none;\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 15px;")
        self.textEdit_43.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_43.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_44 = QTextEdit(self.menuu_4)
        self.textEdit_44.setObjectName(u"textEdit_44")
        self.textEdit_44.setGeometry(QRect(720, 30, 90, 40))
        self.textEdit_44.setFont(font2)
        self.textEdit_44.setStyleSheet(u"border-style: none;\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 15px;")
        self.textEdit_44.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_44.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_45 = QTextEdit(self.menuu_4)
        self.textEdit_45.setObjectName(u"textEdit_45")
        self.textEdit_45.setGeometry(QRect(340, 20, 360, 120))
        self.textEdit_45.setFont(font2)
        self.textEdit_45.setStyleSheet(u"border-style: none;\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 25px;")
        self.textEdit_45.setReadOnly(True)
        self.label_57.raise_()
        self.label_58.raise_()
        self.label_60.raise_()
        self.label_63.raise_()
        self.label_64.raise_()
        self.label_65.raise_()
        self.btn_word_2.raise_()
        self.label_56.raise_()
        self.label_61.raise_()
        self.checkBox.raise_()
        self.btn_word_3.raise_()
        self.spinBox_23.raise_()
        self.spinBox_24.raise_()
        self.textEdit_43.raise_()
        self.textEdit_44.raise_()
        self.textEdit_45.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_19.raise_()
        self.frame.raise_()
        self.menuu_3.raise_()
        self.label_31.raise_()
        self.menuu_4.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">\u0412\u0412\u0415\u0414\u0418\u0422\u0415 \u041f\u0420\u0415\u0414\u041b\u041e\u0416\u0415\u041d\u0418\u0415</span></p></body></html>", None))
        self.btn_gen.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0413\u0415\u041d\u0415\u0420\u0418\u0420\u041e\u0412\u0410\u0422\u042c ", None))
        self.btn_sort.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0422\u0421\u041e\u0420\u0422\u0418\u0420\u041e\u0412\u0410\u0422\u042c ", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">\u041e\u0411\u0420\u0410\u0411\u041e\u0422\u0410\u041d\u041d\u041e\u0415 \u041f\u0420\u0415\u0414\u041b\u041e\u0416\u0415\u041d\u0418\u0415</span></p></body></html>", None))
        self.label.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p><p><br/></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.textEdit_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_7.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_8.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_9.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_10.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.btn_theme.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041c\u0415\u041d\u0410 \u0422\u0415\u041c\u042b", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/><span style=\" font-size:12pt;\">\u041d\u0410\u0421\u0422\u0420\u041e\u0419\u041a\u0418</span><br/></p><p align=\"center\"><br/></p></body></html>", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.btn_clear_sort.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0427\u0418\u0421\u0422\u0418\u0422\u042c", None))
        self.btn_clear_gen.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0427\u0418\u0421\u0422\u0418\u0422\u042c", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_18.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/><span style=\" font-size:12pt;\">\u0418\u041d\u0424\u041e\u0420\u041c\u0410\u0426\u0418\u042f</span><br/></p><p align=\"center\"><br/></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p><p><br/></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.btn_word.setText(QCoreApplication.translate("MainWindow", u"\u0412\u041e\u0420\u0414", None))
        self.label_19.setText("")
        self.label_31.setText("")
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/><span style=\" font-size:12pt;\">\u0418\u041d\u0424\u041e\u0420\u041c\u0410\u0426\u0418\u042f</span><br/></p><p align=\"center\"><br/></p></body></html>", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p><p><br/></p></body></html>", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.btn_word_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u041e\u0420\u0414", None))
        self.label_56.setText("")
#if QT_CONFIG(whatsthis)
        self.checkBox.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u0418\u0421\u041f\u041e\u041b\u042c\u0417\u041e\u0412\u0410\u0422\u042c </p><p align=\"center\">\u0421\u041b\u041e\u0412\u0410 \u0418\u0417 \u0424\u0410\u0419\u041b\u0410</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.checkBox.setText("")
        self.btn_word_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0422\u041a\u0420\u042b\u0422\u042c \u0424\u0410\u0419\u041b ", None))
        self.textEdit_43.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_44.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

