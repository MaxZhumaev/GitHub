# 2023/11/12 00:00|Дополнительное практическое задание по модулю
# Дополнительное практическое задание по модулю: "Наследование классов"
# Задание "Они все так похожи"

class Figure():
    sides_count = 2
    def __init__(self):
        # список сторон (целые числа)
        self.__sides = []
        # логика - число сторон должно быть равно лимиту сторон фигуры
        for i in range(self.sides_count):
            self.__sides.append(1)
        # список цветов в формате RGB
        self.__color = [0, 0, 0]
        self.filled = True
# Метод get_color, возвращает список RGB цветов.
    def get_color(self):
        return self.__color
# Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность
    def __is_valid_color(self, color):
        for i in range(len(color)):
            if color[i] < 0 or color[i] > 255:
                #clr = ['red', 'green', 'blue']
                #print(f'Некорректный цветовой растр: {clr[i]}')
                break
            else:
                self.__color[i] = color[i]
# Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения,
# предварительно проверив их на корректность
    def set_color(self, red, green, blue):
        self.__is_valid_color([red, green, blue])
# Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон
    def __is_valid_sides(self, *sides):
        result = True
        if len(sides) != len(self.__sides):
            result = False
        for side in sides:
            if side <= 0:
                result = False
                break
        return result
# Метод get_sides должен возвращать значение я атрибута __sides
    def get_sides(self):
       return self.__sides
# Метод __len__ должен возвращать периметр фигуры
    def __len__(self):
        return sum(self.__sides)
# Метод set_sides(self, *new_sides) должен принимать новые стороны
    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1
    def __init__(self, color, line):
        Figure.__init__(self)
        self.set_sides(line)
        self.set_color(color[0], color[1], color[2])
        self.__radius = self.get_sides()[0] / 2 / 3.14
# Метод set_sides(self, *new_sides) переопределен, чтобы обновить атрибут радиус
    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        self.__radius = self.get_sides()[0] / 2 / 3.14
# Метод get_square возвращает площадь круга
    def get_square(self):
        return self.__radius*self.__radius * 3.14

class Triangle(Figure):
    sides_count = 3
# Метод get_square возвращает площадь треугольника
    def get_square(self):
        p = sum(self.get_sides()) / 2
        for side in self.get_sides():
            p *= (sum(self.get_sides()) / 2 - side)
        return p**0.5

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, side):
        Figure.__init__(self)
        self.set_sides(side)
        self.set_color(color[0], color[1], color[2])
# Метод set_sides переопределен, чтобы __sides стал списком из 12 одинаковы сторон (передаётся 1 сторона)
# Не оптимально, но решил так: создаю список из 12 сторон куба и в родительский метод
    def set_sides(self, *new_side):
        # если передана длина одной стороны
        if type(new_side[0]) == int:
            sides = []
            for i in range(self.sides_count):
                sides.append(new_side[0])
            super().set_sides(*sides)

# Метод get_volume, возвращает объём куба
    def get_volume(self):
        return self.get_sides()[0]**3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())

cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides((5, 3, 12, 4, 5)) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())