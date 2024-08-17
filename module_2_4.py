# 2023/09/30 00:00|Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"
# Цель: закрепить навык решения задач при помощи цикла for, применив знания об основных типах данных
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []  # простые числа
not_primes = []  # составные числа
# простое число делится без остатка (кратно) только само на себя  и 1
# то есть беру остаток от деления числа на перебираемые делители
# умножаю его на 10 и сморю остаnок от деления на 10, если не ноль - не простое
is_prime = True  # флаг простоты:)
print((((6 / 3) * 10) % 10))

# перебор элементов списка
for i in range(len(numbers)):
    # перебор делителей
    for j in range(2, abs(numbers[i])):
        if j < abs(numbers[i]) and ((numbers[i] / j) * 10) % 10 == 0:
            # not_primes.append(numbers[i])
            is_prime = False
            break
    if is_prime == False:
        not_primes.append(numbers[i])
    elif numbers[i] != 1:
        primes.append(numbers[i])
    is_prime = True  # обновляем
# вывод результата
print(primes)
print(not_primes)
