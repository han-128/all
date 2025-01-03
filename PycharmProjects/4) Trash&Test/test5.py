class Human():

    def __init__(self, name, age, money, house):
        self.money = money
        self.house = house
        self.name = name
        self.age = age


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

#Human.default_info()
human_1 = Human('Rostislav', 15, 100000, 'none')
human_1.buy_house()
print(human_1.house)

