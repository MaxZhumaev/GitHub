# 2023/11/17 00:00|Домашнее задание по теме "Оператор "with"
# Задача "Найдёт везде"

class WordsFinder:
    # инициализация объекта
    def __init__(self, *FileNames):
        self.file_names = []
        for file in FileNames:
            self.file_names.append(file)
    # формирование словаря
    def get_all_words(self):
        # формируем словарь из файлов
        all_words = {}
        # формирую список символов на удаление [',', '.', '=', '!', '?', ';', ':', ' - ']
        # добавил от себя удаление двойных и тройных пробелов, которые образуются после "чистки"
        simbol = [',', '.', '=', '!', '?', ';', ':', ' - ', '\n', '  ', '   ']
        # цикл по файлам (именам)
        for key in self.file_names:
            # открываем каждый файл
            with open(key, encoding='utf-8') as file:
                # считываем файл - одна большая строка сразу в нижнем регистре по ТЗ
                file_str = str.lower(file.read())
                # вычищаю ненужные символы через цикл
                for sim in simbol:
                    file_str = file_str.replace(sim, ' ')
                # формирую список слова из чистого файла - строки по разделителю "пробел"
                all_words[key] = file_str.split(' ')
        return all_words
# метод find(self, word) - найти слово
    def find(self, word):
        # создаю словарь - результат поиска
        dict = {}
        # создаю цикл просмотра словаря файлов
        for keys, words in self.get_all_words().items():
            #содержит ли список слово
            if str(word).lower() in words:
                # записываю индекс + 1 ибо с нуля в словарь если да
                dict[keys] = words.index(str(word).lower()) + 1
        return dict

# метод count(self, word) - найти позицию в словаре
    def count(self, word):
        # создаю словарь - результат поиска и счетчик числа вхождений
        dict = {}
        count = 0
        # создаю цикл просмотра словаря файлов: имя файла - список слов в нем
        for key in self.get_all_words().keys():
            # поэлементно просмотр списка конкретного файла
            for wrd in self.get_all_words()[key]:
                if str(word).lower() in wrd:
                    count += 1
            dict[key] = count

        return dict


finder2 = WordsFinder('test_file.txt')#,
                      #'Rudyard Kipling - If.txt',
                      #'Mother Goose - Monday’s Child.txt')


print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего