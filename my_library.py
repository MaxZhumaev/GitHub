#функция входит ли подстрока в строку или список
#аргументы: что ищем, где ищем, строгое/нет соответствие
#возвращает True если поиск успешен, False - если не нашли
def is_string(search_string, search_list, strong = True):
    result = False
    #если не строгое соответствие все в один регистр
    if not strong:
        search_string = str(search_string).upper()
        search_list = str(search_list).upper()
    # поиск
    if search_string in search_list:
        result = True
    return result

