#2023/10/04 00:00|Домашняя работа по уроку "Пространство имён"
#Цель: применить на практике начальные знания о пространстве имён и оператор global. Закрепить навыки из предыдущих модулей.
#Задача "Счётчик вызовов":

def count_calls():
  global calls
  calls += 1

def string_info(Input_string):
    count_calls()
    return (len(Input_string),
        str(Input_string).upper(),
        str(Input_string).lower())

def is_contains(search_string, search_list):
    count_calls()
    for i in range(0, len(search_list)):
        result = False
        if str(search_string).upper() in str(search_list[i]).upper():
            result = True
            break
    return result

calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'urBAN', 'BaNaN']))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)