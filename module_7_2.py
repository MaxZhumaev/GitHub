# 2023/11/16 00:00|Домашнее задание по теме "Позиционирование в файле"
# Задача "Записать и запомнить"

def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    for i in range(len(strings)):
        strings_positions[tuple((i + 1, file.tell()))] = strings[i]
        file.write(str(strings[i]) + '\n')
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)