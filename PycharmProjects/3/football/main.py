import json
import operator


def authorization():
    global admin_mode
    with open("admin.json", "r") as file:
        admin = json.load(file)

    while True:
        login = input("login: ")
        password = input("password: ")
        for user in admin:
            if user["login"] == login and user["password"] == password:
                admin_mode = user["access"]
                print()
                print(f'Добро пожаловать! Вы вошли как "{user["login"]}"')
                return login
        print("Error login/password")


new_dataR = {"num": 2, "match": 15, "goal": 11, "assist": 11, "yellow_card": 9, "red_card": 1, "score": 22,
             "bio": {"name": "Ruslan", "surname": "Suanov", "birthdate": "07.12.1994"}}

with open("player.json", "r") as wf:
    data = json.load(wf)

max_num = 0
for d in data:
    if int(d["num"]) > max_num: max_num = d["num"]


def red_card(data):
    i = 1
    for d in data:
        if d["red_card"] != 0:
            print(f"[{i}]. {d['bio']['name']} {d['bio']['surname']}. Красных карточек: {d['red_card']}  ")
            i += 1


def sort(data):
    k = 1
    data.sort(key=operator.itemgetter('score'), reverse=True)

    for d in data:
        if k < 7:
            print(f"[{k}] {d['bio']['name']} {d['bio']['surname']}, его счёт: {d['score']}")
            k += 1
        else:
            break


def all_players(data):
    for d in data: print(
        f"ФИО: {d['bio']['name']} {d['bio']['surname']}, дата рождения: {d['bio']['birthdate']}, номер игрока: {d['num']} ")


def all_players_plus(data):
    for d in data:
        print(
            f"ФИО: {d['bio']['name']} {d['bio']['surname']}, дата рождения: {d['bio']['birthdate']}, номер игрока: {d['num']},\
количество матчей: {d['match']}, количество голов: {d['goal']}, количество передач: {d['assist']},\
количество жёлтых карточек: {d['yellow_card']}, количество красных карточек: {d['red_card']}, общий счёт: {d['score']} ")


def change_player(data):
    while True:
        num_changed_player = input('Введите номер игрока, которого хотите изменить: ')
        change_param = (input('''
Введите параметр, который хотите изменить:
1) количество матчей
2) количество голов
3) количество передач
4) количество жёлтых карточек
5) количество красных карточек
6) имя игрока
7) фамилию игрока
8) дату рождения игрока
:::> '''))
        for d in data:
            if d["num"] == int(num_changed_player):
                match change_param:
                    case '1':
                        d["match"] = int(input("Введите количество матчей: "))
                        save()
                        return
                    case '2':
                        d["goal"] = int(input("Введите количество голов: "))
                        d["score"] = d["goal"] + d["assist"]
                        save()
                        return
                    case '3':
                        d["assist"] = int(input("Введите количество передач: "))
                        d["score"] = d["goal"] + d["assist"]
                        save()
                        return
                    case '4':
                        d["yellow_card"] = int(input("Введите количество жёлтых карточек: "))
                        save()
                        return
                    case '5':
                        d["red_card"] = int(input("Введите количество красных карточек: "))
                        save()
                        return
                    case '6':
                        d["bio"]["name"] = (input("Введите имя игрока: "))
                        save()
                        return
                    case '7':
                        d["bio"]["surname"] = (input("Введите фамилию игрока: "))
                        save()
                        return
                    case '8':
                        d["bio"]["birthdate"] = (input("Введите дату рождения игрока: "))
                        save()
                        return
                    case _:
                        print('Такой команды нету!')
        print('Такого игрока нету')


def new_player(new_dataR):
    global data, max_num
    max_num += 1

    new_dataR["num"] = max_num
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
    save()


def select():
    global temp
    temp = 0
    if admin_mode == True:
        while temp not in ('1', '2', '3', '4', '5', '6', '33'):
            temp = input('''
Выберите одно из предложенных действий:
1) Вывести игроков, имеющих красные карточки.
2) Вывести 6 лучших игроков.
3) Вывести всех игроков.
4) Изменить игрока.
5) Добавить игрока.
6) Выход.
:::> ''')
    else:
        while temp not in ('1', '2', '3', '4'):
            temp = input('''
Выберите одно из предложенных действий:
1) Вывести игроков, имеющих красные карточки.
2) Вывести 6 лучших игроков.
3) Вывести всех игроков.
4) Выход.
:::> ''')


def save():
    global data
    with open("players_new.json", "w") as pl_new:
        json.dump(data, pl_new, indent=2)

    with open("players_new.json", "r") as n_wf:
        data = json.load(n_wf)


def main():
    while True:
        select()
        match temp:
            case '1':
                red_card(data)
            case '2':
                sort(data)
            case '3':
                all_players(data)
            case '4':
                if admin_mode == True:
                    change_player(data)
                else:
                    break
            case '5':
                new_player(new_dataR)
            case '6':
                break
            case '33':
                all_players_plus(data)


if __name__ == "__main__":
    authorization()
    main()
