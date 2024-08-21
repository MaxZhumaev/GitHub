# Самостоятельная работа по уроку "Произвольное число параметров".
from my_library import is_string

def single_root_words(root_word, *other_words):
    same_words = []
    for item in other_words:
        if is_string(root_word, item, False) or is_string(item, root_word, False):
            same_words.append(item)
    return same_words


print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))