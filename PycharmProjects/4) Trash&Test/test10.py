
# Входные данные
login_list = ['admin', 'user', 'asdf','log']
password_list = ['admin1', 'user1', 'qwer','pas']


p = 0       # Счётчик попыток
i = 0       # Порядковый номер пароля в списке
n = 0       # Порядковый номер логгина в списке
q = 0       # Переменная помогающая определить исход ввода данных
z = 0
ll = len(login_list)        # Длина списков, для возможности легко увеличить списки



while (q != 2) and (p < 5):     # Проверка на правильность ввода данных, и проверка на количество попыток
    z = 0
    login = str(input('Введите логин: '))
    password = str(input('Введите пароль: '))
    for i in range(0, ll):
        q = 4
        if login == login_list[i]:
            z = 1
            n = i
        else:
            q = 4
    if (z == 1) and (password == password_list[n]):
        q = 2
    elif z == 1:
        q = 3


    match q:
        case 2: print('Вы вошли в аккаунт')
        case 3: print('Неверный пароль')
        case 4: print('Неверный логин')

    p += 1

if p == 5:
    print('Попытки закончились. Повторите попытку позже)')