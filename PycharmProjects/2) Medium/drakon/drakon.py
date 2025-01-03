import time
from random import randint



HPdrakon = 100.0
HPplayer = 100.0
DamageDrakon = 7.0
DamagePlayer = 5.0
load = 0
runtime = True



def baner():

    print('''

\033[33m\33[1m●▬▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬●\033[0m
\033[32m\33[1m░░░░░░░░░░░░ ДОБРО ПОЖАЛОВАТЬ В ИГРУ ░░░░░░░░░░░░\033[0m
\033[33m\33[1m●▬▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬●\033[0m


''')

def play():

    print('Нажмите Enter для входа в игру.')
    input()



def loading():

    global load
    while load < 101:
        print(f"Загрузка {load}%")
        load = load + randint(12, 20)
        time.sleep(1)
    print('Загрузка 100%:')



def displayInfo():
    time.sleep(3)
    print("\033[33m\33[1mОсень.\033[0m")
    time.sleep(2)
    print("Вы гуляете по лесу, и вдруг слышите, крики о помощи .")
    time.sleep(2)
    print("Вы смотрите в даль и видите высоченную башню.")
    time.sleep(2)
    print("На самой верхушке башни сидит прицесса, под стражей дракона.")
    time.sleep(2)
    print("Вокруг башни летает огромный дракон.")
    time.sleep(2)
    print("Что бы освободить принцессу, надо победить дракона.")
    time.sleep(2)
    print("Но вы не боитесь его, и решаете идти в бой!")
    time.sleep(4)


def chooseGun():
    print()
    print()
    print('Перед боем с драконом вам нужно выбрать \033[35m\33[1mэкипировку\033[0m и \033[35m\33[1mоружие\033[0m')
    print('Выберите \033[35m\33[1mоружие\033[0m: ')
    print('''
1. \033[96m\33[1mАЛМАЗНЫЙ МЕЧ.\033[0m С помощью этого оружия вы будите наносить больше урона. Повышает урон с \033[31m\33[1m6\033[0m до \033[31m\33[1m7\033[0m       o()xxxx[{\033[96m\33[1m::::::::::::::::::::::::::::::::::>\033[0m
    
2. \033[96m\33[1mАРБАЛЕТ.\033[0m Оружие сильное, спору нет, но сможите ли вы с него попасть...?  Повышает урон с \033[31m\33[1m6\033[0m до \033[31m\33[1m10\033[0m, но есть шанс в \033[31m\33[1m25%\033[0m промазать 

3. \033[96m\33[1mЩИТ.\033[0m Скрываясь за этим щитом, вы как за каменной стеной. Добавляет \033[31m\33[1m20\033[0m хп ''')
    gun = ''
    while gun not in ('1', '2','3'):
        gun = input('(введите 1, 2 или 3) ')
    return int(gun)


def chooseEquip():

    print()
    print()
    print('Выберите \033[35m\33[1mэкипировку\033[0m: ')
    print('''
1. \033[96m\33[1mКОЛЬЧУГА.\033[0m Лучше защищает он атаки дракона. Понижает урон дракона c \033[31m\33[1m7\033[0m до \033[31m\33[1m6\033[0m

2. \033[96m\33[1mДОСПЕХИ.\033[0m В этой экипировке вы будите себя чувствовать лучше. Добавляют \033[31m\33[1m15\033[0m хп''')
    equip = ''
    while equip not in ('1', '2'):
        equip = input('(введите 1 или 2) ')
    return int(equip)


def change():

    global DamagePlayer
    global HPplayer
    global DamageDrakon
    match selectGun:
        case 1:
            DamagePlayer = 7
        case 2:
            DamagePlayer = 10
        case 3:
            HPplayer = HPplayer + 15
    match selectEquip:
        case 1:
            DamageDrakon = 6
        case 2:
            HPplayer = HPplayer + 20


def fight():

    global dropDrakon
    global dropPlayer
    global HPplayer
    global HPdrakon
    global DamageMomemtPlayer
    global DamageMomemtDrakon
    time.sleep(2)
    print()
    print()
    print('Начинается битва. Первый удар наносит дракон')
    time.sleep(1)
    while HPplayer >= 0.0:
        if HPdrakon or HPplayer <= 0.0:
            if HPdrakon <=0:
                print('Поздравляю! Вы победили дракона')
                break
            elif HPplayer <= 0:
                print('К сожалеию вы проиграли')
                break
            else:
                if  selectGun != 2:
                    DamageMomemtPlayer = 0.0
                    print()
                    print('Ход дракона')
                    time.sleep(1)
                    dropDrakon = randint(1 , 6)
                    HPplayer = HPplayer - (dropDrakon * DamageDrakon)
                    DamageMomemtDrakon = dropDrakon * DamageDrakon
                    print(f'Дракон сносит вам \033[31m\33[1m{DamageMomemtDrakon}\033[0m хп. У вас остаётся \033[32m\33[1m{HPplayer}\033[0m хп')

                    if HPdrakon or HPplayer <= 0.0:
                        if HPdrakon <= 0:
                            print('Поздравляю! Вы победили дракона')
                            break
                        elif HPplayer <= 0:
                            print('К сожалеию вы проиграли')
                            break

                    print('Ваш ход. Нажмите Enter, что бы нанести урон дракону')
                    input()
                    dropPlayer = randint(1 , 6)
                    HPdrakon = HPdrakon - (dropPlayer * DamagePlayer)
                    DamageMomemtPlayer = dropPlayer * DamagePlayer
                    print('Вы размахиваетесь мечом и...')
                    time.sleep(2)
                    print(f'Cносите дракону \033[32m\33[1m{DamageMomemtPlayer}\033[0m хп. У дракона остаётся \033[31m\33[1m{HPdrakon}\033[0m х')
                    if HPdrakon <=0:
                        print("Поздравляю! Вы победили дракона")
                        break
                else:
                    DamageMomemtPlayer = 0.0
                    print()
                    print('Ход дракона')
                    dropDrakon = randint(1, 6)
                    HPplayer = HPplayer - (dropDrakon * DamageDrakon)
                    DamageMomemtDrakon = dropDrakon * DamageDrakon
                    print(f'Дракон сносит вам \033[31m\33[1m{DamageMomemtDrakon}\033[0m хп. У вас остаётся \033[32m\33[1m{HPplayer}\033[0m хп')
                    if HPplayer <=0:
                        print("К сожалению дракон вас убил(")
                        break

                    print('Ваш ход. Нажмите Enter, что бы нанести урон дракону')
                    input()
                    print('Вы стреляете в дракона и...')
                    time.sleep(2)
                    chance = randint(1,4)
                    if chance != 1:
                        dropPlayer = randint(1, 6)
                        HPdrakon = HPdrakon - (dropPlayer * DamagePlayer)
                        DamageMomemtPlayer = dropPlayer * DamagePlayer
                        print(f'Попадаете нанося дракону урон в \033[32m\33[1m{DamageMomemtPlayer}\033[0m хп. У дракона остаётся \033[31m\33[1m{HPdrakon}\033[0m х')
                    else:
                        print('к сожалению промахиваетесь')





def playAgain():

    print('Хотите сыграть еще раз?')
    answer = ''
    while answer not in ('1', '2'):
        answer = input('(1-да / 2-нет) ')
    return True if answer == '1'\
    else False


while runtime:
    play()
    loading()
    baner()
    displayInfo()
    selectGun = chooseGun()
    selectEquip = chooseEquip()
    change()
    fight()
    runtime = playAgain()
