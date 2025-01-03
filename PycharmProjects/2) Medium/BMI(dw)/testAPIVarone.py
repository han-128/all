import json
import os
import operator

with open("userData.json", "r") as _userData:
    userData = json.load(_userData)

    print(type(userData))
RUNTIME = True

def writeLine(n):
    print("_"*n)


def sortForMass(userData):
    userData.sort(key=operator.itemgetter('mass'), reverse=True)
    writeDict(userData)

def sortForHeight(userData):
    userData.sort(key=operator.itemgetter('height'))
    writeDict(userData)

def sortForBIM(userData):
    userData.sort(key=operator.itemgetter('BIM'))
    writeDict(userData)

def sortCategory(userData):
    Category = ['Obese', 'Overweight', 'Normal range', 'Underweight']
    Class = ['Class III', 'Class II', 'Class I', 'Pre-obese', 'Normal', 'Mild thinness', 'Moderate thinness','Severe thinness']

    CategoryRu = ['Ожирение', 'Избыточный вес', 'Нормальный диапазон', 'Недостаточный вес']
    ClassRu = ['Класс 3', 'Класс 2', 'Класс 1', 'Пре-ожирение', 'Нормальный', 'Легкая худоба', 'Умеренная ходоба','Сильная Худоба']

    userDataSort = []

    mod = int(input("""
    1] Сортировка по Категории
    2] Сортировка по классу
    -> """))

    if mod == 1:
        for i in range(len(CategoryRu)):
            print(f"{i+1}] {CategoryRu[i]}")
        Cary = int(input('-> '))

        for i in userData:
            if i['Categories']['Category'] == Category[Cary-1]:
                userDataSort.append(i)

    elif mod == 2:
        for i in range(len(ClassRu)):
            print(f"{i + 1}] {ClassRu[i]}")
        Cls = int(input('-> '))

        for i in userData:
            if i['Categories']['Class'] == Class[Cls - 1]:
                userDataSort.append(i)
    writeDict(userDataSort)

def exit_():
        global RUNTIME
        RUNTIME = False

def Clear():
    os.system("cls")

def writeDict(userData):
    #Clear()
    k = 0
    print(f"UserId{'':<4}mass{'':<4}height{'':<4}BIM{'':<8}Category{'':<8}Class")
    for userData in userData:
        k += 1
        print(f"{userData['UserId']:<10}{userData['mass']:<8}{userData['height']:<10}{userData['BIM']:<11}{userData['Categories']['Category']:<16}{userData['Categories']['Class']} ")
        if k == 10:
            writeLine(65)
            k = 0
    print('')


def main():
    listOfStrCommand = ['Показать исходные данные', 'Сортировка по массе','Сортировка по росту','Сортировка по BIM','Сортировка по категориям','выход']
    listOfCommand = [writeDict, sortForMass, sortForHeight,sortForBIM,sortCategory, exit_]
    while RUNTIME:
        for key, item in enumerate(listOfStrCommand):
            print(f'{key + 1}] {item}')

        while True:
            command = input(':> ')
            if command.isdigit() and int(command) <= len(listOfCommand):
                command = int(command) - 1
                listOfCommand[command](userData)
                break




if __name__ == "__main__":
    main()
