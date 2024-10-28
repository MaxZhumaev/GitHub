# 2023/11/26 00:00|Домашнее задание по теме "Создание исключений"

# Цель: освоить навык создания пользовательских исключений и использовать его в решении задачи.
# Повторить тему ООП и принцип инкапсуляции.
#
# Задача "Некорректность":
#
# Создайте 3 класса (2 из которых будут исключениями):
# Класс Car должен обладать следующими свойствами:
# Атрибут объекта model - название автомобиля (строка).

# Атрибут объекта __vin - vin номер автомобиля (целое число). Уровень доступа private.
# Метод __is_valid_vin(vin_number) - принимает vin_number и проверяет его на корректность.
# Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
# Выбрасывает исключение IncorrectVinNumber с сообщением 'Некорректный тип vin номер',
# если передано не целое число. (тип данных можно проверить функцией isinstance).
# Выбрасывает исключение IncorrectVinNumber с сообщением 'Неверный диапазон для vin номера',
# если переданное число находится не в диапазоне от 1000000 до 9999999 включительно.
# Возвращает True, если исключения не были выброшены.

# Атрибут __numbers - номера автомобиля (строка).
# Метод __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность.
# Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.

# Выбрасывает исключение IncorrectCarNumbers с сообщением 'Некорректный тип данных для номеров',
# если передана не строка. (тип данных можно проверить функцией isinstance).

# Выбрасывает исключение IncorrectCarNumbers с сообщением 'Неверная длина номера',
# переданная строка должна состоять ровно из 6 символов.
# Возвращает True, если исключения не были выброшены.

# Классы исключений IncorrectVinNumber и IncorrectCarNumbers,
# объекты которых обладают атрибутом message - сообщение, которое будет выводиться при выбрасывании исключения.
# ВАЖНО!
# Методы __is_valid_vin и __is_valid_numbers должны вызываться и при создании объекта
# (в __init__ при объявлении атрибутов __vin и __numbers).

class Car():
    def __init__(self, model, vin, number):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_numbers(number):
            self.__number = number

    def __is_valid_vin(self, vin):
        if isinstance(vin, int) and vin >= 1000000 and vin <= 9999999:
            return True
        elif vin < 1000000 or vin > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            raise IncorrectVinNumber('Некорректный тип данных для номеров')

    def __is_valid_numbers(self, number):
        if isinstance(number, str) and len(number) == 6:
            return True
        elif not isinstance(number, str):
            raise IncorrectVinNumber('Некорректный тип данных для номеров')
        elif len(number) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
