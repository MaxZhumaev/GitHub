# 2023/11/19 00:00|Домашнее задание по теме "Файлы в операционной системе".
#Цель задания:
#Освоить работу с файловой системой в Python, используя модуль os.
#Научиться применять методы os.walk, os.path.join, os.path.getmtime, os.path.dirname, os.path.getsize и
# использование модуля time для корректного отображения времени.
# Задание:
# Создайте новый проект или продолжите работу в текущем проекте.
# Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
# Примените os.path.join для формирования полного пути к файлам.
# Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
# Используйте os.path.getsize для получения размера файла.
# Используйте os.path.dirname для получения родительской директории файла.
# Импорт нужных функций
import os, time

# директория проекта
directory = "."
# начинаем обход файловой системы из пути directory
for root, dirs, files in os.walk(directory):
    for file in files:
        print(f'Обнаружен файл: {os.path.basename(file)}, Путь: {os.getcwd()}, '
                f'Размер: {os.path.getsize(file)} байт, '
                f'Время изменения: {time.strftime("%d.%m.%Y %H:%M", time.localtime(os.path.getmtime(file)))}, '
                f'Родительская директория: {os.path.dirname(os.getcwd())}')
