# 2023/11/07 00:00|Домашнее задание по теме "Зачем нужно наследование"
# Задача "Съедобное, несъедобное"

# класс Растения
class Plant():
    def __init__(self, name):
        self.edible = False
        self.name = name

# класс Животные
class Animal():
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

    def eat(self, food):
        if food.edible == True:
            self.fed = True
            print(f'{self.name} съел {food.name}')
        elif food.edible == False:
            self.alive = False
            print(f'{self.name} не стал есть {food.name}')

# наследники общего класса Животные
class Mammal(Animal):
    pass

class Predator(Animal):
    pass

# наследники общего класса Растения
class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        self.edible = True
        self.name = name

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)