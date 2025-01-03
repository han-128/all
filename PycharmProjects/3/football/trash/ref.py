import json
import operator

login_list = ['admin', 'user']
password_list = ['admin1', 'user1']
p = 5
vbn = 0
for i in range(p):
    login = input('Login: ')
    password = input('Password: ')
    if login in login_list:
        index = login_list.index(login)
        if password == password_list[index]:
            print('Welcome!')
            if login == "admin":
                vbn = 1
            break
        else:
            print('Error: password')
    else:
        print('Error: login')
else:
    print('End!')

new_dataR = {
    "num": 2,
    "match": 15,
    "goal": 11,
    "assist": 11,
    "yellow_card": 9,
    "red_card": 1,
    "score": 22,
    "bio": {
        "name": "Ruslan",
        "surname": "Suanov",
        "birthdate": "07.12.1994"
    }
}

with open("D:/PycharmProjects/3/football/player.json", "r") as wf:
    data = json.load(wf)
    print(type(data))
    print(data[0]["match"])


max_num = 8

iop = []

for data in data:
    iop.append(data["num"])

data = list(data) # ???????????????????????????????????????????????????????????????????

def red_card(data):
    print(type(data))

    print(data[0]["match"]) # ?????????????????????????????????????????????????????????????

    i = 1
    for data in data:
        if data["red_card"] != 0:
            print(f"[{i}]. {data['bio']['name']} {data['bio']['surname']}. Красных карточек: {data['red_card']}  ")
            i += 1


def sort(data):
    k = 1
    data.sort(key=operator.itemgetter('score'), reverse=True)

    for data in data:
        if k < 7:
            print(data["bio"]["name"], data["score"])
            k += 1
        else:
            break


def all_players(data):
    for data in data:
        print(
            f"ФИО: {data['bio']['name']} {data['bio']['surname']}, дата рождения: {data['bio']['birthdate']}, номер игрока: {data['num']} ")
    print(max_num)


def change_player(data):
    global qwe

    qwe = input('Введите номер игрока, которого хотите изменить: ')
    wasd = int(input('''
Введите параметр, который хотите изменить:
1) количество матчей
2) количество голов
3) количество передач
4) количество жёлтых карточек
5) количество красных карточек
6) имя игрока
7) фамилию игрока
8) дату рождения игрока
        '''))
    while True:
        for data in data:
            match wasd:
                case '1':
                    data[qwe]["match"] = input("Введите количество матчей: ")
                    print(111)
                case '2':
                    if data["num"] == qwe:
                        print(111)
                        data["goal"] = input("Введите количество голов: ")
                case '3':
                    if data["num"] == qwe:
                        data["assist"] = input("Введите количество передач: ")
                case '4':
                    if data["num"] == qwe:
                        data["yellow_card"] = input("Введите количество жёлтых карточек: ")
                case '5':
                    if data["num"] == qwe:
                        data["red_card"] = input("Введите количество красных карточек: ")
                case '6':
                    if data["num"] == qwe:
                        data["name"] = input("Введите имя игрока: ")
                case '7':
                    if data["num"] == qwe:
                        data["surname"] = input("Введите фамилию игрока: ")
                case '8':
                    if data["num"] == qwe:
                        data["birthdate"] = input("Введите дату рождения игрока: ")


def new_player(data, c, new_dataR):
    c += 1

    new_dataR["num"] = c
    new_dataR["match"] = int(input("Введите количество матчей: "))
    new_dataR["goal"] = int(input("Введите количество голов: "))
    new_dataR["assist"] = int(input("Введите количество передач: "))
    new_dataR["yellow_card"] = int(input("Введите количество жёлтых карточек: "))
    new_dataR["red_card"] = int(input("Введите количество красных карточек: "))
    new_dataR["score"] = new_dataR["goal"] + new_dataR["assist"]
    new_dataR["bio"]["name"] = input("Введите имя игрока: ")
    new_dataR["bio"]["surname"] = input("Введите фамилию игрока: ")
    new_dataR["bio"]["birthdate"] = input("Введите дату игрока: ")

    data.append(new_dataR)

    new_dataR["num"] = 0
    new_dataR["match"] = 0
    new_dataR["goal"] = 0
    new_dataR["assist"] = 0
    new_dataR["yellow_card"] = 0
    new_dataR["red_card"] = 0
    new_dataR["score"] = 0
    new_dataR["bio"]["name"] = ""
    new_dataR["bio"]["surname"] = ""
    new_dataR["bio"]["birthdate"] = ""


def select():
    global temp
    temp = 0
    if vbn == 1:
        while temp not in ('1', '2', '3', '4', '5', '6'):
            temp = input('''
Выберите одно из предложенных действий:
1) Вывести игроков, имеющих красные карточки.
2) Вывести 6 лучших игроков.
3) Вывести всех игроков.
4) Изменить игрока.
5) Добавить игрока.
6) Выход.
''')
    else:
        while temp not in ('1', '2', '3', '4'):
            temp = input('''
Выберите одно из предложенных действий:
1) Вывести игроков, имеющих красные карточки.
2) Вывести 6 лучших игроков.
3) Вывести всех игроков.
4) Выход.
''')


def asd():
    while True:
        global temp
        select()
        match temp:
            case '1':
                red_card(data)
            case '2':
                sort(data)
            case '3':
                all_players(data)
            case '4':
                if vbn == 1:
                    change_player(data)
                else:
                    break
            case '5':
                if vbn == 1:
                    new_player(data, max_num, new_dataR)
                else:
                    print("Недостаточно прав, для совершения операции")
            case '6':
                if vbn == 1:
                    break
                else:
                    print("Недостаточно прав, для совершения операции")


asd()
