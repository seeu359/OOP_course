"""
Объявите класс SmartPhone, объекты которого предполагается создавать командой:

sm = SmartPhone(марка смартфона)

Каждый объект должен содержать локальные атрибуты:

model - марка смартфона (строка);
apps - список из установленных приложений (изначально пустой).

Также в классе SmartPhone должны быть объявлены следующие методы:

add_app(self, app) - добавление нового приложения на смартфон
(в конец списка apps);
remove_app(self, app) - удаление приложения по ссылке на объект app.

При добавлении нового приложения проверять, что оно отсутствует в списке
 apps (отсутствует объект соответствующего класса).

Каждое приложение должно определяться своим классом. Для примера объявите
 следующие классы:

AppVK - класс приложения ВКонтаке;
AppYouTube - класс приложения YouTube;
AppPhone - класс приложения телефона.
"""


class SmartPhone:

    def __init__(self, model):
        self.model = model
        self.apps = list()

    def add_app(self, app):
        types = list(map(type, self.apps))
        app_type = type(app)
        if app_type not in types:
            self.apps.append(app)

    def remove_app(self, app):
        self.apps.remove(app)


class AppVK:

    def __init__(self):
        self.name = 'ВКонтакте'


class AppYouTube:

    def __init__(self, memory_max):
        self.name = 'YouTube'
        self.memory_max = memory_max


class AppPhone:

    def __init__(self, phone_list):
        self.name = 'Phone'
        self.phone_list = phone_list
