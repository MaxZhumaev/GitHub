# 2023/10/05 00:00|Домашняя работа по уроку "Способы вызова функции
# Цель: закрепить знания о параметрах по умолчанию и именованных аргументах.
from my_library import is_string

def send_email(message, recipient, sender = "university.help@gmail.сom"):
# условие 1: не содержит "@" или не оканчивается на ".com"/".ru"/".net"
    if (((not is_string(".сom", recipient[len(recipient) - 5:]) and
        not is_string(".ru", recipient[len(recipient) - 5:]) and
        not is_string(".net", recipient[len(recipient) - 5:])) or
        (not is_string("@", recipient)))
        or
        ((not is_string(".сom", sender[len(sender) - 5:]) and
          not is_string(".ru", sender[len(sender) - 5:]) and
          not is_string(".net", sender[len(sender) - 5:])) or
         (not is_string("@", sender)))):
        print(f"Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>")
# условие 2: Если же sender и recipient совпадают
    elif recipient in sender or sender in recipient:
        print("Нельзя отправить письмо самому себе!")
# условие 3: отправитель по умолчанию - university.help@gmail.com
    elif is_string(sender, "university.help@gmail.сom"):
        print(f"Письмо успешно отправлено с адреса <{sender}> на адрес <{recipient}>")
# условие 4: НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!
    elif not "university.help@gmail.сom" in sender:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <{sender}> на адрес <{recipient}>")
    return 1

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.сom')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.сom')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')