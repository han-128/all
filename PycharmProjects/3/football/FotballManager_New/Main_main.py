import sys
import json
import operator

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from des import *
import authorization
import wID
import wChange


class Auth_window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.auth = authorization.Ui_Form()
        self.auth.setupUi(self)
        self.setWindowModality(2)

        self.validate_flag = False
        self.auth.pushButton.clicked.connect(self.check_info)  # проверка логина пароля
        self.auth.checkBox.clicked.connect(self.change_password)

        self.userData = None
        with open(urlAdmin, "r") as file:
            self.userData = json.load(file)

    def check_info(self):
        login = self.auth.lineEdit.text()  # поле логина
        password = self.auth.lineEdit_2.text()  # поле пароля

        for user in self.userData:
            if user["login"] == login and user["password"] == password:
                self.validate_flag = True
                startManager()
                self.close()
                break
        else:
            QMessageBox.information(self, 'Ошибка входа', 'Неверный логин/пароль\nПопробуйте снова.')

    def change_password(self):
        if self.auth.checkBox.isChecked():
            self.auth.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.auth.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

    def closeEvent(self, value):
        if not self.validate_flag:
            raise SystemExit


class InputIdPlayer(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = wID.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowModality(2)

        self.ui.pushButton.clicked.connect(self.findId)
        self.ui.pushButton_2.clicked.connect(self.closeWidget)
        self.ui.lineEdit.setText("")
        self.ui.lineEdit.setValidator(QtGui.QIntValidator(1, 999999, self))

    def show(self) -> None:
        self.ui.lineEdit.setText("")
        super().show()

    def findId(self):
        data = loadData()
        value = self.ui.lineEdit.text()
        value = int(value) if value != "" else 0

        for item in data:
            if item['num'] == value:
                windgetChange.show(value)
                self.closeWidget()
                break
        else:
            QMessageBox.information(self, 'Ошибка', f'Игрока по ID {value} не найден!')

    def closeWidget(self):
        self.close()


class ChangePlayer_window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = wChange.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowModality(2)
        self.IDplayer = 0
        self.ui.pushButton.clicked.connect(self.saveData)
        self.ui.pushButton_2.clicked.connect(self.closeWidget)
        self.ui.lineEdit_4.setValidator(QtGui.QIntValidator(1, 999999, self))
        self.ui.lineEdit_5.setValidator(QtGui.QIntValidator(1, 999999, self))
        self.ui.lineEdit_6.setValidator(QtGui.QIntValidator(1, 999999, self))
        self.ui.lineEdit_7.setValidator(QtGui.QIntValidator(1, 999999, self))
        self.ui.lineEdit_8.setValidator(QtGui.QIntValidator(1, 999999, self))

    def show(self, id) -> None:
        self.IDplayer = id
        self.ui.label.setText(f'ID: {self.IDplayer}')
        self.fillData()
        super().show()

    def fillData(self):
        data = loadData()
        for item in data:
            if item['num'] == self.IDplayer:
                self.ui.lineEdit.setText(f'{item["bio"]["name"]}')
                self.ui.lineEdit_2.setText(f'{item["bio"]["surname"]}')
                self.ui.lineEdit_3.setText(f'{item["bio"]["birthdate"]}')
                self.ui.lineEdit_4.setText(f'{item["match"]}')
                self.ui.lineEdit_5.setText(f'{item["goal"]}')
                self.ui.lineEdit_6.setText(f'{item["assist"]}')
                self.ui.lineEdit_7.setText(f'{item["yellow_card"]}')
                self.ui.lineEdit_8.setText(f'{item["red_card"]}')

    def saveData(self):
        data = loadData()
        for item in data:
            if item['num'] == self.IDplayer:
                item["bio"]["name"] = self.ui.lineEdit.text()
                item["bio"]["surname"] = self.ui.lineEdit_2.text()
                item["bio"]["birthdate"] = self.ui.lineEdit_3.text()
                item["match"] = int(self.ui.lineEdit_4.text())
                item["goal"] = int(self.ui.lineEdit_5.text())
                item["assist"] = int(self.ui.lineEdit_6.text())
                item["yellow_card"] = int(self.ui.lineEdit_7.text())
                item["red_card"] = int(self.ui.lineEdit_8.text())
        saveData(data)
        self.closeWidget()

    def closeWidget(self):
        self.close()

class NewPlayer_window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = wChange.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowModality(2)
        self.IDplayer = 0
        data = loadData()
        self.ui.pushButton.clicked.connect(self.NewData)
        self.ui.pushButton_2.clicked.connect(self.closeWidget)
        self.max_num = maxNumber(data)
        self.ui.lineEdit_4.setValidator(QtGui.QIntValidator(1, 999999, self))
        self.ui.lineEdit_5.setValidator(QtGui.QIntValidator(1, 999999, self))
        self.ui.lineEdit_6.setValidator(QtGui.QIntValidator(1, 999999, self))
        self.ui.lineEdit_7.setValidator(QtGui.QIntValidator(1, 999999, self))
        self.ui.lineEdit_8.setValidator(QtGui.QIntValidator(1, 999999, self))

    def show(self) -> None:
        self.IDplayer = self.max_num + 1
        self.ui.label.setText(f'ID: {self.IDplayer}')
        super().show()


    def NewData(self):
        data = loadData()
        new_dataR = {}

        new_dataR["num"] = int(self.max_num + 1)
        new_dataR["match"] = int(self.ui.lineEdit_4.text())
        new_dataR["goal"] = int(self.ui.lineEdit_5.text())
        new_dataR["assist"] = int(self.ui.lineEdit_6.text())
        new_dataR["yellow_card"] = int(self.ui.lineEdit_7.text())
        new_dataR["red_card"] = int(self.ui.lineEdit_8.text())
        new_dataR["score"] = new_dataR["goal"] + new_dataR["assist"]
        new_dataR["bio"] = {}
        new_dataR["bio"]["name"] = self.ui.lineEdit.text()
        new_dataR["bio"]["surname"] = self.ui.lineEdit_2.text()
        new_dataR["bio"]["birthdate"] = self.ui.lineEdit_3.text()
        data.append(new_dataR)
        saveData(data)

        saveData(data)
        self.closeWidget()

    def closeWidget(self):
        self.close()



class MyApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.red_card)  # работает
        self.ui.pushButton_2.clicked.connect(self.sort_players)  # работает
        self.ui.pushButton_3.clicked.connect(self.all_players)  # работает
        self.ui.pushButton_4.clicked.connect(self.change_player)  # ввод
        self.ui.pushButton_5.clicked.connect(self.new_player)  # работает
        self.ui.pushButton_6.clicked.connect(self.exitFromProgramm)  # работает

    def red_card(self):
        self.ui.plainTextEdit.setPlainText("")
        data = loadData()
        i = 1
        for d in data:
            if d["red_card"] != 0:
                self.ui.plainTextEdit.appendPlainText(
                    f"{str(f'[{i}]. '):<5}{d['bio']['name'] + ' ' + d['bio']['surname']:<25}{'Красных карточек:' + str(d['red_card'])}")
                self.ui.plainTextEdit.appendPlainText("")
                i += 1

    def sort_players(self):
        self.ui.plainTextEdit.setPlainText("")
        data = loadData()
        k = 1
        data.sort(key=operator.itemgetter('score'), reverse=True)
        for d in data:
            if k < 7:
                self.ui.plainTextEdit.appendPlainText(
                    f"{str(f'[{k}]. '):<5}{d['bio']['name'] + ' ' + d['bio']['surname']:<20}{'Счёт:' + str(d['score'])}")
                self.ui.plainTextEdit.appendPlainText("")
                k += 1
            else:
                return

    def all_players(self):
        self.ui.plainTextEdit.setPlainText("")
        data = loadData()
        self.ui.plainTextEdit.appendPlainText(
            f'{"#":<5}{"Имя":<17}{"День рождения":<19}{"Матчи":<10}{"Голы":<10}{"Помощь":<10}{"Желтые":<10}{"Красные":<10}')
        self.ui.plainTextEdit.appendPlainText("")
        for d in data:
            number = f"[{d['num']}]"
            name = f"{d['bio']['name']} {d['bio']['surname'][0]}."
            day = d['bio']['birthdate']
            total = d['match']
            goal = d['goal']
            assist = d['assist']
            yellow = d['yellow_card']
            red = d['red_card']
            self.ui.plainTextEdit.setWordWrapMode(QtGui.QTextOption.NoWrap)
            self.ui.plainTextEdit.appendPlainText(
                f'{number:<5}{name:<17}{day:<19}{total:<10}{goal:<10}{assist:<10}{yellow:<10}{red:<10}')
            self.ui.plainTextEdit.appendPlainText("")

    def change_player(self):
        windgetId.show()


    def new_player(self):
        widgetNewPlayer.show()

    def exitFromProgramm(self):
        exit()


urlAdmin = 'admin.json'
urlPlayer = 'player.json'


def maxNumber(data):
    num = 0
    for d in data:
        if d["num"] > num: num = d["num"]
    return num


def startManager():
    myApp.show()


def loadData():
    with open(urlPlayer, "r") as file:
        data = json.load(file)
    return data


def saveData(newDate):
    with open(urlPlayer, "w") as file:
        json.dump(newDate, file, indent=2)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myApp = MyApp()
    auth = Auth_window()
    windgetId = InputIdPlayer()
    windgetChange = ChangePlayer_window()
    widgetNewPlayer = NewPlayer_window()
    auth.show()
    sys.exit(app.exec_())
