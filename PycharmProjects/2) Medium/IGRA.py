from random import randint

print('Привет! Как тебя зовут?')
name = input('Введите имя: ')
print(f'Что ж, {name}, выбери сложность игры: \033[32m\33[1m 1.Легко\033[0m, \033[33m\33[1m 2.Средне\033[0m, \033[31m\33[1m 3.Сложно\033[0m, \033[96m\33[1m 4.Невозможно\033[0m')

a = int(input('Введите номер сложности: '))


match a:
    case 1:
        b = 5
        max_num = 10
        print('Вы выбрали режим игры:\033[32m\33[1m легко\033[0m. Вам надо угадать число от \033[35m\33[1m 1\033[0m до \033[35m\33[1m 10\033[0m. У вас есть \033[35m\33[1m 5\033[0m попыток. Удачи!')
    case 2:
        b = 5
        max_num = 20
        print('Вы выбрали режим игры:'"\033[33m\33[1m средне\033[0m"'. Вам надо угадать число от \033[35m\33[1m 1\033[0m до \033[35m\33[1m 20\033[0m . У вас есть \033[35m\33[1m 5\033[0m попыток. Удачи!')
    case 3:
        b = 5
        max_num = 50
        print('Вы выбрали режим игры:\033[31m\33[1m сложно\033[0m. Вам надо угадать число от \033[35m\33[1m 1\033[0m до \033[35m\33[1m 70\033[0m. У вас есть \033[35m\33[1m 5\033[0m попыток. Удачи!')

    case 4:
        b = 5
        max_num = 150
        print('Вы выбрали режим игры:\033[96m\33[1m невозможно\033[0m. Вам надо угадать число от \033[35m\33[1m 1\033[0m до \033[35m\033[1m 150\033[0m. У вас есть \033[35m\33[1m 5\033[0m попытки. Удачи!')


secretNumber = randint(1, max_num)
#print(secretNumber)
guess = 0
count = 1

if count == b:
    guess = int(input(f'Ваша последяя, \033[96m\33[1m{count}\033[0m попытка: '))

for i in range(b):

    match count:
        case 1:
            guess = int(input(f'Ваша \033[32m\33[1m{count}\033[0m попытка: '))
        case 2:
            guess = int(input(f'Ваша \033[32m\33[1m{count}\033[0m попытка: '))
        case 3:
            guess = int(input(f'Ваша \033[33m\33[1m{count}\033[0m попытка: '))
        case 4:
            guess = int(input(f'Ваша \033[31m\33[1m{count}\033[0m попытка: '))
        case 5:
            guess = int(input(f'Ваша последняя, \033[96m\33[1m{count}\033[0m попытка: '))


    if guess > secretNumber:
        print('Твоё число слишком большое.')
    if guess < secretNumber:
        print('Твоё число слишком маленькое.')
    if guess == secretNumber:
        break
    count += 1


match count:
    case 1:
        text = "попытку"
    case 2:
        text = "попытки"
    case 3:
        text = "попытки"
    case 4:
        text = "попытки"
    case 5:
        text = "попыток"
    case 6:
        text = "попыток"


if guess == secretNumber:
    print(f'Ура! Вы угадали! Вы справились за \033[96m\33[1m {count}\033[0m {text}')
else:
    print(f'Увы, я загадал число \033[36m\33[1m{secretNumber}\033[0m')



