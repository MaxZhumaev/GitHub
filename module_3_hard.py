# 2023/10/12 00:00|Дополнительное практическое задание по модулю*

def calculate_structure_sum(data):
    is_string = 0
    is_bool = 0
    is_number = 0
    sum_all = 0
    structure = list(data)
    print(structure)
    # сложная многократносложенная структура напоминает ветки дерева
    # идея развернуть многомерную структуру в одномерную
    # первым циклом идем по !изменяемой! длине разворачиваемого ствола дерева
    i = 0
    while i < len(structure):
        # лист в форме строки
        if type(structure[i]) == str:
            is_string += 1
            sum_all += len(structure[i])
            structure.pop(i)
            i -= 1
        # лист в форме Булевые данные
        elif type(structure[i]) == bool:
            is_bool += 1
            structure.pop(i)
            i -= 1
        # лист в форме числа
        elif type(structure[i]) == int or type(structure[i]) == float:
            is_number += 1
            sum_all += structure[i]
            structure.pop(i)
            i -= 1
        # ветка в форме списка
        elif type(structure[i]) == list or  type(structure[i]) == set or type(structure[i]) == tuple:
            # каждый элемент в структуру большего уровня
            j = 0
            while j < len(structure[i]):
                if type(structure[i][j]) == set:
                    structure[i][j] = list(structure[i][j])
                structure.append(structure[i][j])
                j += 1
            structure.pop(i)
            i -= 1
        elif type(structure[i]) == dict:
            # каждый элемент в структуру большего уровня
            j = 0
            while j < len(structure[i]):
                structure.append(list(dict(structure[i]).keys())[j])
                structure.append(list(dict(structure[i]).values())[j])
                j += 1
            structure.pop(i)
            i -= 1
        i += 1
    print(structure)
    print(f'строк: {is_string}, Булевых: {is_bool}, чисел: {is_number}')
    print(f'сумма всех элементов: {sum_all}')

    return structure

data_structure = [
                    [1, 2, 3], # ветка с листями - список
                    {'a': 4, 'b': 5}, # словарь - надо с ним еще решить!
                    (6, {'cube': 7, 'drum': 8}), # ветка с веточками
                    "Hello",  # лист из строки
                    ((), [{(2, 'Urban', ('Urban2', 35))}]) # сложная ветка
]

calculate_structure_sum(data_structure)
