import json
import operator

urlAdmin = 'admin.json'
urlPlayer = 'player.json'


def authorization():
    with open(urlAdmin, "r") as file:
        admin = json.load(file)

    while True:
        login = 'admin'  # input("login: ")
        password = 'admin'  # input("password: ")
        for user in admin:
            if user["login"] == login and user["password"] == password:
                print(f'Добро пожаловать! Вы вошли как "{user["login"]}"')
                print()
                return user["access"]
        print("Error login/password")


def loadData():
    with open(urlPlayer, "r") as file:
        data = json.load(file)
    return data


def red_card():
    data = loadData()
    i = 1
    print()
    for d in data:
        if d["red_card"] != 0:
            print(
                f"{str(f'[{i}]. '):<5}{d['bio']['name'] + ' ' + d['bio']['surname']:<20}{'Красных карточек:' + str(d['red_card'])}")
            i += 1
    print()


def sort_players():
    data = loadData()
    k = 1
    data.sort(key=operator.itemgetter('score'), reverse=True)
    print()
    for d in data:
        if k < 7:
            print(f"{str(f'[{k}]. '):<5}{d['bio']['name'] + ' ' + d['bio']['surname']:<20}{'Счёт:' + str(d['score'])}")
            k += 1
        else:
            print()
            return


def all_players():
    data = loadData()
    print()
    print(
        f'{"#":<5}{"Имя":<20}{"День рождения":<18}{"Матчи":<15}{"Голы":<15}{"Помощь":<15}{"Желтые":<15}{"Красные":<15}')
    for d in data:
        number = f"[{d['num']}]"
        name = f"{d['bio']['name']} {d['bio']['surname'][0]}."
        day = d['bio']['birthdate']
        total = d['match']
        goal = d['goal']
        assist = d['assist']
        yellow = d['yellow_card']
        red = d['red_card']
        print(f'{number:<5}{name:<20}{day:<18}{total:<15}{goal:<15}{assist:<15}{yellow:<15}{red:<15}')
    print()


def change_player():
    lst_for_change = 'Введите параметр, который хотите изменить:\n1) количество матчей\n2) количество голов' \
                     '\n3) количество передач\n4) количество жёлтых карточек\n5) количество красных карточек' \
                     '\n6) имя игрока\n7) фамилию игрока\n8) дату рождения игрока'
    command_for_change = {'1': 'match', '2': 'goal', '3': 'assist', '4': 'yellow_card', '5': 'red_card',
                          '6': 'name', '7': 'surname', '8': 'birthdate'}

    data = loadData()
    while True:
        all_players()
        num_changed_player = int(input('Введите номер игрока, которого хотите изменить: '))
        print(lst_for_change)
        change_param = int(input(':::> '))

        for d in data:
            if d["num"] == num_changed_player:
                if 6 <= change_param <= 8:
                    d['bio'][command_for_change[str(change_param)]] = input('Введите новое значение:\n:> ')
                    save(data)
                    return
                else:
                    d[command_for_change[str(change_param)]] = int(input('Введите новое значение:\n:> '))
                    save(data)
                    return

        print('Такого игрока нету')


def maxNumber(data):
    num = 0
    for d in data:
        if d["num"] > num: num = d["num"]
    return num


def new_player():
    data = loadData()
    new_dataR = {}

    new_dataR["num"] = maxNumber(data) + 1
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
    save(data)


def save(newDate):
    with open(urlPlayer, "w") as pl_new:
        json.dump(newDate, pl_new, indent=2)


def exitFromProgramm():
    exit()


def main():
    listCommandsAdmin = [red_card, sort_players, all_players, change_player, new_player, exitFromProgramm]
    listCommandsUser = [red_card, sort_players, all_players, exitFromProgramm]

    textCommandsAdmin = ['Вывести игроков, имеющих красные карточки',
                         'Вывести 6 лучших игроков',
                         'Вывести всех игроков',
                         'Изменить игрока',
                         'Добавить игрока',
                         'Выход']
    textCommandsUser = ['Вывести игроков, имеющих красные карточки',
                        'Вывести 6 лучших игроков',
                        'Вывести всех игроков',
                        'Выход']

    if authorization():
        totalCommand = listCommandsAdmin.copy()
        totalText = textCommandsAdmin.copy()
    else:
        totalCommand = listCommandsUser.copy()
        totalText = textCommandsUser.copy()

    while True:
        index = 1
        for item in totalText:
            print(f'{index}) {item}')
            index += 1
        command = int(input(':::> '))

        if 1 <= command <= len(totalCommand):
            totalCommand[command - 1]()
        else:
            print('Такой команды нет!')


if __name__ == "__main__":
    main()
