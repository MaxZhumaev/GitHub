# Самостоятельная работа по уроку "Рекурсия"
def get_multiplied_digits(number = '23'):
    first = int(number[:1])
    if len(number) == 1:
        return first
    else:
        return first * get_multiplied_digits(number[1:])
    return first

print(get_multiplied_digits('522'))