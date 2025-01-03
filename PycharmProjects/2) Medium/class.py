from random import randint as RR
import turtle

class Robot():
    def __init__(self, name, x, y):
        self.name = name +  '#331'
        self.x = x
        self.y = y
        self.energy = 100
        print('Робот создан')

    def move(self, x, y):
        if self.energy <= 0:
            print('Не хватает энергии!')
            return
        temp = abs((self.x + x)) + abs((self.y + y))
        if self.energy - temp <= 0:
            print('Не хватает энергии!')
            return
        self.energy -= temp
        self.x += x
        self.y += y

        print(f'Робот переместился: {self.energy}. {self.x}:{self.y}')

    def charging(self, k):
        self.energy += k

    def getInfo(self):
        return (self.x, self.y, self.energy)

robot_1 = Robot('Vally', 0, 0)
for i in range(25):
    robot_1.move(RR(-5, 5), RR(-5, 5))
result = robot_1.getInfo()
print(f'X: {result[0]}; Y: {result[1]}')


