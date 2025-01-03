
login_list = ['admin', 'user', 'asdf']
password_list = ['admin1', '1234', 'qwer']

login = str(input('Введите логин: '))

i = 0

while i != len(login_list):
    if login == login_list[i]:
        print('1')
        i += 1
    else:
        print('2')
        i += 1

