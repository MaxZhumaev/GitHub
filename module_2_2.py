#2023/09/28 00:00|Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."
first = int(input("Введите первое целое число для сравнения: "))
second  = int(input("Введите второе целое число для сравнения: "))
third = int(input("Введите третье целое число для сравнения: "))
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)