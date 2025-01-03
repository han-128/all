# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerjQZJEY.ui'
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
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(1980, 900)
        MainWindow.setMaximumSize(QSize(1980, 1020))
        self.actionApi_Kei_client_id = QAction(MainWindow)
        self.actionApi_Kei_client_id.setObjectName(u"actionApi_Kei_client_id")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.client_id = QLineEdit(self.centralwidget)
        self.client_id.setObjectName(u"client_id")
        self.client_id.setGeometry(QRect(30, 60, 191, 20))
        self.api_key = QLineEdit(self.centralwidget)
        self.api_key.setObjectName(u"api_key")
        self.api_key.setGeometry(QRect(30, 110, 191, 20))
        self.warehouse_id = QLineEdit(self.centralwidget)
        self.warehouse_id.setObjectName(u"warehouse_id")
        self.warehouse_id.setGeometry(QRect(30, 160, 191, 20))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 730, 191, 31))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(40, 780, 191, 31))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(40, 830, 191, 31))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(40, 680, 191, 31))
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(40, 630, 191, 31))
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(40, 580, 191, 31))
        self.data_from = QLineEdit(self.centralwidget)
        self.data_from.setObjectName(u"data_from")
        self.data_from.setGeometry(QRect(30, 240, 191, 20))
        self.data_to = QLineEdit(self.centralwidget)
        self.data_to.setObjectName(u"data_to")
        self.data_to.setGeometry(QRect(30, 290, 191, 20))
        self.plainTextEdit_2 = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(240, 20, 1641, 831))
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.plainTextEdit_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.plainTextEdit_2.setUndoRedoEnabled(False)
        self.plainTextEdit_2.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.plainTextEdit_2.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1980, 21))
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QToolBar(MainWindow)
        self.toolBar_2.setObjectName(u"toolBar_2")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar_2)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>API-KEY</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.actionApi_Kei_client_id.setText(QCoreApplication.translate("MainWindow", u"Api-Kei / client-id", None))
#if QT_CONFIG(tooltip)
        self.client_id.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>dsfsdf</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.client_id.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.api_key.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>CLIENT_ID</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.api_key.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>dddddddddddddddd</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.warehouse_id.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>WAREHOUSE_ID</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"v3_posting_fbs_list", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.plainTextEdit_2.setPlainText("")
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.toolBar_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_2", None))
    # retranslateUi

