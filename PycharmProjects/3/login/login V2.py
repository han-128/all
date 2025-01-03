# Входные данные
login_list = ['admin', 'user', 'asdf','log']
password_list = ['admin', 'user', 'qwer','pas']

p = 5
for i in range(p):
    login = input('Login: ')
    password = input('Password: ')
    if login in login_list:
        index = login_list.index(login)
        if password == password_list[index]:
            print('Welcome!')
            break
        else:
            print('Error: password')
    else:
        print('Error: login')
else:
    print('End!')