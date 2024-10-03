# 2023/11/15 00:00|Домашнее задание по теме "Режимы открытия файлов"
# Цель: закрепить знания о работе с файлами (чтение/запись) решив задачу.
# Задача "Учёт товаров"

def CleanFile(name):
    file = open(name, 'w')
    file.close()

# Product('Potato', 50.0, 'Vagetables')
class Product():
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return self.name + ', ' + str(self.weight) + ', ' + self.category + '\n'

# класс Shop
class Shop():
    def __init__(self):
        self.__file_name = 'products.txt'

# Метод get_products(self), который считывает всю информацию из файла __file_name
    def get_products(self):
        file = open(self.__file_name, "r")
        prod = file.read()
        file.close()
        return prod

# Метод add(self, *products), который принимает неограниченное количество объектов класса Product
    def add(self, *products):
        prod_in_Shop = self.get_products()
        file = open(self.__file_name, 'a')
        for product in products:
            if product.name in prod_in_Shop:
                print(f'Продукт {product.name + ', ' + str(product.weight) + ', ' + product.category} уже есть в магазине')
            else:
                file.write(product.__str__())
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

#CleanFile('products.txt')

s1.add(p1, p2, p3)

print(s1.get_products())