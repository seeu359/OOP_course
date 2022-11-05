"""Объявите класс SingletonFive, с помощью которого можно было бы создавать
объекты командой:

a = SingletonFive(<наименование>)

Здесь <наименование> - это данные, которые сохраняются в локальном свойстве
name созданного объекта.

Этот класс должен формировать только первые пять объектов. Остальные (шестой,
седьмой и т.д.) должны быть ссылкой на последний (пятый) созданный объект.

Создайте первые десять объектов класса SingletonFive с помощью следующего
фрагмента программы:"""


class SingletonFive:
    __count = list()
    __instance = None

    def __new__(cls, *args, **kwargs):
        if len(cls.__count) < 5:
            cls.__count.append(cls)
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]
