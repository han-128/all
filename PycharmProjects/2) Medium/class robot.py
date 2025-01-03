class Robot():
    def __init__(self, hp, dmg, energy):
        self.hp = hp
        self.dmg = dmg
        self.energy = energy

    def move(self):
        pass

    def attack(self):
        r = self.__delatHp()
        print('attack')
        pass

    def __delatHp(self):
        return 0

    def getInfo(self):
        pass

class RobotRonin(Robot):
    def __init__(self, hp, dmg, energy):
        super().__init__(hp, dmg, energy)

    def SwordStrike(self):
        pass

    def attack(self):
        print('attack')
        pass

class RobotTank(Robot):
    def __init__(self, hp, dmg, energy):
        super().__init__(hp, dmg, energy)

    def move(self):
        print('stop')
        pass

class RobotRogue(Robot):
    def __init__(self, hp, dmg, energy):
        super().__init__(hp, dmg, energy)

    def attack(self):
        Robot.attack(self)
        print('Add  attack')


robot_1 = RobotRonin(100, 25, 100)
robot_2 = RobotRonin(250, 5, 250)
robot_3 = RobotRogue(75, 100, 250)
robot_1.attack()
robot_2.attack()
robot_3.attack()



#
