immutable_var = (5, "max", True, [1, 2])
print(immutable_var)
print(immutable_var[0:2])
#изменяю элемент списка, входящий в кортеж
print(immutable_var[3][1])
immutable_var[3][1] = 3
print(immutable_var[3][1])
mutable_list = [1,'win', False]
print(mutable_list)
print(mutable_list[-1])