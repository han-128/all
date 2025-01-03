import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from des import *

class MyApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.button_1 = QtWidgets.QPushButton(self)
        self.button_1.setGeometry(20, 30, 75, 23)
        self.button_1.setText('клик')
        self.button_1.clicked.connect(self.showMessage)

        self.button_2 = QtWidgets.QPushButton(self)
        self.button_2.setGeometry(20, 50, 75, 23)
        self.button_2.setText('клик')
        self.button_2.clicked.connect(self.showMessage_1)


    def showMessage(self):
        QMessageBox.about(self, 'zagolovok', 'privet')
        QMessageBox.information(self, 'zagolovok', 'info')
        QMessageBox.warning(self, 'zagolovok', 'warning')
        QMessageBox.critical(self, 'zagolovok', 'critical')



    def showMessage_1(self):
        result = QMessageBox.question(self, 'zagolovok', 'message',
                                      QMessageBox.Open, QMessageBox.Ok)
        if result == QMessageBox.Ok:
            self.ui.statusbar.showMessage('привет!')
        else:
            file_path = QFileDialog.getOpenFileName(self, 'zagolovok', 'file_name',
                                                    '*.*')
            self.ui.statusbar.showMessage(f'{file_path}')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec_())