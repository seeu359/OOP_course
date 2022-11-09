"""
Объявите класс AppStore - интернет-магазин приложений для устройств под iOS.
В этом классе должны быть реализованы следующие методы:

add_application(self, app) - добавление нового приложения app в магазин;
remove_application(self, app) - удаление приложения app из магазина;
block_application(self, app) - блокировка приложения app (устанавливает
локальное свойство blocked объекта app в значение True);
total_apps(self) - возвращает общее число приложений в магазине.

Класс AppStore предполагается использовать следующим образом (эти строчки в
программе не писать):

store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.remove_application(app_youtube)

Здесь Application - класс, описывающий добавляемое приложение с указанным
именем. Каждый объект класса Application должен содержать локальные свойства:

name - наименование приложения (строка);
blocked - булево значение (True - приложение заблокировано; False - не
заблокировано, изначально False).

Как хранить список приложений в объектах класса AppStore решите сами.
"""


class AppStore:

    applications_list = list()

    @classmethod
    def add_application(cls, app):
        cls.applications_list.append(app)

    @classmethod
    def remove_application(cls, app):
        cls.applications_list.remove(app)

    @classmethod
    def block_application(cls, app):
        app = cls.applications_list.index(app)
        cls.applications_list[app].blocked = True

    @classmethod
    def total_apps(cls):
        return len(cls.applications_list)


class Application:

    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked
