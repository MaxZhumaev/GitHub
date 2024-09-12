# 2023/11/05 00:00|Дополнительное практическое задание по модулю*
# Задание "Свой YouTube"

from time import sleep

# класс экземпляров пользователей
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
# класс экземпляра видео
class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
# класс ресурса
class UrTube:
    def __init__(self):
        self.Users = []
        self.Videos = []
        self.Current_User = None
# логин
    def log_in(self, nickname, password):
        for user in self.Users:
            if user.nickname == nickname and user.password == password:
                self.Current_User = user
                break
# регистрация
    def register(self, nickname, password, age):
        isin = False
        for user in self.Users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                isin = True
                break
        if isin == False:
            self.Users.append(User(nickname, password, age))
# разлог
    def log_out(self):
        self.Current_User = None
# добавляем видео
    def add(self, *Videos):
        for video in Videos:
            self.Videos.append(Video(video.title, video.duration, video.time_now, video.adult_mode))
# найти видео
    def get_videos(self, name):
        v = []
        for video in self.Videos:
            if str(name).upper() in str(video.title).upper():
                v.append(video.title)
        return v
# просмотр видео
    def watch_video(self, name):
        if self.Current_User == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for video in self.Videos:
                if name == video.title:
                    if video.adult_mode == True and self.Current_User.age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        t = ''
                        for time in range(video.duration):
                            sleep(1)
                            t += str(time + 1) + ' '
                        print(t, "Конец видео")


ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode = True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.log_in('vasya_pupkin', hash('lolkekcheburek'))
ur.watch_video('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.log_in('urban_pythonist', hash('iScX4vIJClb9YQavjAgF'))
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
# print(ur.Current_User)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
