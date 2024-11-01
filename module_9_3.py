# 2023/12/01 00:00|Домашнее задание по теме "Генераторные сборки"

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(y) for (x, y) in zip(first, second) if len(x) != len(y))
print(list(first_result))

second_result = (len(first[i]) <= len(second[i]) for i in range(0, len(first)))
print(list(second_result))