# 2023/11/08 00:00|Домашнее задание по теме "Доступ к свойствам родителя. Переопределение свойств."
# Задача "Изменять нельзя получать"

# класс - транспортное средство
class Vehicle():
    __COLOR_VARIANT = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color
# возвращает строку: "Модель: <название модели транспорта>"
    def get_model(self):
        return f"Модель: {self.__model}"
# возвращает строку: "Мощность двигателя: <мощность>"
    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"
# возвращает строку: "Цвет: <цвет транспорта>"
    def get_color(self):
        return f"Цвет: {self.__color}"
# распечатывает результаты методов (в том же порядке): get_model, get_horsepower, get_color;
# а так же владельца в конце в формате "Владелец: <имя>"
    def print_info(self):
        print(self.get_model(), '\n',
              self.get_horsepower(), '\n',
              self.get_color(), '\n',
              f"Владелец: {self.owner}")
    def set_color(self, color):
        if str(color).upper() in str(self.__COLOR_VARIANT).upper():
            self.__color = color
        else:
            print(f"Нельзя сменить цвет на {color}")
# класс - седан
class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
