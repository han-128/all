class Tomato:
    states = {0: 'Отсутствует', 1: 'Цветение', 2: 'Зеленый', 3: 'Красный'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        self._change_state()

    def is_ripe(self):
        return self._state == 3

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print(f'{self._index} помидор {Tomato.states[self._state]}')


class TomatoBush:

    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(1, num+1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []


class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()
        print('Садовник выполнил работу')

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Сбор урожая закончен')
        else:
            print('Помидоры ещё не созрели')

    @staticmethod
    def knowledge_base():
        print('Что бы помидоры росли быстрее, их нужно каждый день поливать.')

Gardener.knowledge_base()
great_tomato_bush = TomatoBush(8)
gardener = Gardener('Валера', great_tomato_bush)
gardener.work()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
