class Human():

    default_name = '---'
    default_age = 0

    def __init__(self, name, age, money, house):
        self.money = money
        self.house = house
        self.name = name
        self.age = age

    def info(self):
        print(f'''Имя: {self.name} 
Возраст: {self.age}
Деньги: {self.money}
Дом: {self.house}''')

    def default_info(self):
        print(Human.default_name, Human.default_age)

    def buy_house(self):
        price = 7000 * 0.9
        if self.house == 'house bought':
            print('Дом уже куплен')
        elif self.money < price:
            print('На балансе недостаточно средств для совершения покупки')
        else:
            if self.money >= price:
                self.money = self.money - price
                self.house = 'house bought'
                print('Вы купили дом')

    def earn_money(self):
        self.money += 1000
        print('Вы разаботари 1000$')

class House():

    def __init__(self, area, price):
        self.area = area
        self.price = price
        self.price = 7000

    def final_price(self):
        self.price = self.price * 0.9
        print(self.price)

class SmallHouse(House):
    def __init__(self, area):
        super(SmallHouse, self).__init__('40м2', 7000)
        self.area = area
        self.area = '40м2'

human_1 = Human('Rost', 15, 4000, 'none')

a = 0

def select():
    global temp
    temp = 0
    while temp not in ('1', '2', '3','4'):
        temp = input('''
Выберите одно из предложенных действий:
1) Вывести информацию
2) Купить дом
3) Заработать денег
4) Выход
''')


def asd():
    while True:
        global temp
        select()
        match temp:
            case '1':
                human_1.info()
            case '2':
                human_1.buy_house()
            case '3':
                human_1.earn_money()
            case '4':
                break

asd()





