# 2023/11/18 00:00|Домашнее задание по теме "Форматирование строк"

# функция для простаты работы
def Who_is_Winner(score1, score2, team1, team2 ):
    if score1 > score2:
        challenge_result = team1
    elif score1 == score2:
        challenge_result = "ничья"
    else:
        challenge_result = team2
    return challenge_result
# Использование %
# Переменные: количество участников первой команды (team1_num)
# "В команде Мастера кода участников: 5 ! "
team1_num = 5
team1 = "Мастера кода"
print("В команде %s участников: %s ! " % (team1, team1_num))
# Переменные: количество участников в обеих командах (team1_num, team2_num)
# "Итого сегодня в командах участников: 5 и 6 !"
team1_num = 5
team2_num = 6
print("Итого сегодня в командах участников: %s и %s !" %(team1_num, team2_num))

# Использование format()
# Переменные: количество задач решённых командой 2 (score_2)
# "Команда Волшебники данных решила задач: 42 !"
score_1 = 40
score_2 = 42
team2 = 'Волшебники данных'
print("Команда {0} решила задач: {1} !".format(team2, score_2))
# Переменные: время за которое команда 2 решила задачи (team2_time).
# " Волшебники данных решили задачи за 18015.2 с !"
team2_time = 18015.2
print("{0} решили задачи за {1} с !".format(team2, team2_time))
# Использование f-строк
# Переменные: количество решённых задач по командам: score_1, score_2
# "Команды решили 40 и 42 задач!"
print(f"Команды решили {score_1} и {score_2} задач!")
# Переменные: исход соревнования (challenge_result).
# "Результат битвы: победа команды Мастера кода!"
challenge_result = Who_is_Winner(score_1, score_2, team1, team2)
print(f"Результат битвы: победа команды {challenge_result}!")
# Переменные: количество задач (tasks_total) и среднее время решения (time_avg)
# "Сегодня было решено 82 задач, в среднем по 350.4 секунды на задачу!."
team1_num = 5
team2_num = 6

score_1 = 40
score_2 = 42

team1_time = 1552.512
team2_time = 2153.31451

tasks_total = score_1 + score_2
time_avg = (team1_time+team2_time)/tasks_total

print(f"Сегодня было решено {tasks_total} задач, в среднем по {round(time_avg, 2)} секунды на задачу!.")
challenge_result = Who_is_Winner(score_1, score_2, team1, team2)
print(f"Результат битвы: победа команды {challenge_result}!")