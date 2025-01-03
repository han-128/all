def polin(str):
    lst = []
    for i in str:
        if i.isalpha():
            lst.append(i)
    return lst ==  lst[::-1]


str = input('Введите \033[96m\33[1mфразу\033[0m или \033[96m\33[1mслово\033[0m: ')


if polin(str) == True:
    print("Данная фраза/слово \033[32m\33[1mявляется палиндромом ")
else:
    print('Данная фраза/слово \033[32m\33[1mне является палиндромом')



