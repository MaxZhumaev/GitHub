#2023/09/29 00:00|Домашняя работа по уроку "Стиль кода часть II. Цикл While."
#Задача "Нули ничто, отрицание недопустимо!"
numbers = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0 #переменная цикла для контроля выхода за список
while numbers[i] >= 0 and i < len(numbers):
    if numbers[i] > 0:
        print(numbers[i])
    if i < len(numbers): # чтобы не обратился к несуществующему элементу в самом конце цикла
        i += 1