#2023/10/01 00:00|Домашняя работа по уроку "Функции в Python.Функция с параметром"
#Цель: закрепить навык написания функций и их вызовов.
def get_matrix (n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([]) #создаю размерность по n
        for j in range(m):
            matrix[i].append(value) #создается размерность по m
    return matrix
print(get_matrix(2,2,10))
print(get_matrix(3,5,42))
print(get_matrix(4,2,13))
