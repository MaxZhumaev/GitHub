# Самостоятельная работа по уроку "Распаковка позиционных параметров".

def print_params(a = 1, b = 'строка', c = True):
    print(f'параметр а: {a}, параметр b: {b}, параметр c: {c}')

print_params(b = 25)
print_params(c = [1,2,3])

values_list = [21, "человек", False]
values_dict = {'a': '2', 'b': 69, 'c': 9}

print_params(*values_list)
print_params(**values_dict)


