import json
import operator

with open("D:/PycharmProjects/3/football/player.json", "r") as wf:
    data = json.load(wf)
    print(type(data))
    print(data[0]["match"])



def red_card(data):
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


def select():
    global temp
    temp = 0
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

asd()
