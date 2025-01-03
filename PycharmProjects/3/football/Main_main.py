import sys
import json
import operator

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from des import *


class MyApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.red_card) #работает
        self.ui.pushButton_2.clicked.connect(self.sort_players) #работает
        self.ui.pushButton_3.clicked.connect(self.all_players) #шрифт
        self.ui.pushButton_4.clicked.connect(self.change_player) #ввод
        self.ui.pushButton_5.clicked.connect(self.new_player) #сделать
        self.ui.pushButton_6.clicked.connect(self.exitFromProgramm) #работает
        self.ui.pushButton_8.clicked.connect(self.authorization) #крашит

        self.urlAdmin = 'admin.json'
        self.urlPlayer = 'player.json'


    def authorization(self):
        with open(self.urlAdmin, "r") as file:
            admin = json.load(file)
        login = self.ui.textEdit
        password = self.ui.textEdit_2
        while True:

            for user in admin:
                if user["login"] == login and user["password"] == password:
                    print(f'Добро пожаловать! Вы вошли как "{user["login"]}"')
                    print()
                    return user["access"]
            self.ui.textEdit_3.setText("Error login/password")


    def loadData(self):
        with open(self.urlPlayer, "r") as file:
            data = json.load(file)
        return data

    def red_card(self):
        self.ui.plainTextEdit.setPlainText("")
        data = self.loadData()
        i = 1
        for d in data:
            if d["red_card"] != 0:
                self.ui.plainTextEdit.appendPlainText(
                    f"{str(f'[{i}]. '):<5}{d['bio']['name'] + ' ' + d['bio']['surname']:<25}{'Красных карточек:' + str(d['red_card'])}")
                self.ui.plainTextEdit.appendPlainText("")
                i += 1

    def sort_players(self):
        self.ui.plainTextEdit.setPlainText("")
        data = self.loadData()
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
        #self.plainTextEdit.setFont()
        #font = QtGui.QFont()
        #font.setPointSize(14)
        #font.setBold(True)
        #font.setWeight(75)
        #self.ui.plainTextEdit.setFont("Arial", 2)  ####################### решить проблему с размером шрифта
        #self.ui.plainTextEdit.setPlainText("")
        data = self.loadData()
        self.ui.plainTextEdit.appendPlainText(f'{"#":<5}{"Имя":<15}{"День рождения":<15}{"Матчи":<15}{"Голы":<10}{"Помощь":<10}{"Желтые":<10}{"Красные":<10}')
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
            self.ui.plainTextEdit.appendPlainText(f'{number:<5}{name:<19}{day:<19}{total:<19}{goal:<19}{assist:<19}{yellow:<19}{red:<19}')
            self.ui.plainTextEdit.appendPlainText("")

    def change_player(self):
        self.ui.plainTextEdit.setPlainText("")
        lst_for_change = 'Введите параметр, который хотите изменить:\n1) количество матчей\n2) количество голов' \
                         '\n3) количество передач\n4) количество жёлтых карточек\n5) количество красных карточек' \
                         '\n6) имя игрока\n7) фамилию игрока\n8) дату рождения игрока'
        command_for_change = {'1': 'match', '2': 'goal', '3': 'assist', '4': 'yellow_card', '5': 'red_card',
                              '6': 'name', '7': 'surname', '8': 'birthdate'}

        data = self.loadData()
        while True:
            self.all_players()
            self.ui.plainTextEdit.appendPlainText(lst_for_change)
            num_changed_player = self.ui.plainTextEdit_3
            change_param = int(input(':::> '))

            for d in data:
                if d["num"] == num_changed_player:
                    if 6 <= change_param <= 8:
                        d['bio'][command_for_change[str(change_param)]] = input('Введите новое значение:\n:> ')
                        self.save(data)
                        return
                    else:
                        d[command_for_change[str(change_param)]] = int(input('Введите новое значение:\n:> '))
                        self.save(data)
                        return

        print('Такого игрока нету')

    def maxNumber(self, data):
        num = 0
        for d in data:
            if d["num"] > num: num = d["num"]
        return num


    def new_player(self):
        data = self.loadData()
        new_dataR = {}

        new_dataR["num"] = self.maxNumber(self) + 1
        new_dataR["match"] = int(input("Введите количество матчей: "))
        new_dataR["goal"] = int(input("Введите количество голов: "))
        new_dataR["assist"] = int(input("Введите количество передач: "))
        new_dataR["yellow_card"] = int(input("Введите количество жёлтых карточек: "))
        new_dataR["red_card"] = int(input("Введите количество красных карточек: "))
        new_dataR["score"] = new_dataR["goal"] + new_dataR["assist"]
        new_dataR["bio"] = {}
        new_dataR["bio"]["name"] = input("Введите имя игрока: ")
        new_dataR["bio"]["surname"] = input("Введите фамилию игрока: ")
        new_dataR["bio"]["birthdate"] = input("Введите дату игрока: ")
        data.append(new_dataR)
        self.save(data)

    def save(self, newDate):
        with open(self.urlPlayer, "w") as pl_new:
            json.dump(newDate, pl_new, indent=2)


    def exitFromProgramm(self):
        exit()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec_())
