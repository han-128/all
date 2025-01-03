class Human():

    default_name = 'user'
    default_age = 0

    def __init__(self, name = default_name, age = default_age):
        self._money = 0
        self._house = None
        self.name = name
        self.age = age

    def info(self):
        print(f'''Имя: {self.name} 
Возраст: {self.age}
Деньги: {self._money}
Дом: {self._house}''')

    @staticmethod
    def default_info():
        print(Human.default_name, Human.default_age)

    def _make_deal(self, house, cost):
            self._money = self._money - cost
            self._house = house
            print('Вы купили дом')

    def buy_house(self, house,  sale):
        if self._money >= sale:
            self._make_deal(house, sale)
        else:
            print('На балансе недостаточно средств для совершения покупки')

    def earn_money(self):
        self._money += 500
        print('Вы разаботари 500$')

class House():

    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, sale):
        return self._price * sale

class SmallHouse(House):
    def __init__(self):
        super().__init__('40м2', 7000)

Human.default_info()
human_1 = Human()
human_1.info()
house_1 = SmallHouse()
print('==========================')
human_1.buy_house(house_1, 1000)
human_1.earn_money()
human_1.earn_money()
human_1.earn_money()
human_1.earn_money()
human_1.buy_house(house_1, 1000)
human_1.info()
print('==========================')
