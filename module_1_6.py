# списки
my_dict = {"Max": 1985, "Lena": 1990, "Ilgiz": 1965}
print(my_dict)
print(my_dict['Max'])
print(my_dict.get('Alex'))
my_dict.update({'Alex': 1995, 'Oleg': 2001})
print('Max: ' + str(my_dict.pop('Max')))
print(my_dict)
# множества
my_set = {1, 2, 3, 5, 5, 9, 3, 'Max', 'Min', 'Min'}
print(my_set)
my_set.update({6, 'Sum'})
my_set.remove(3)
print(my_set)