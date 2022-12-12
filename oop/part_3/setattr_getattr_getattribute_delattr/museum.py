"""
Вам необходимо написать программу описания музеев. Для этого нужно объявить
класс Museum, объекты которого формируются командой:

mus = Museum(название музея)

В объектах этого класса должны формироваться следующие локальные атрибуты:

name - название музея (строка);
exhibits - список экспонатов (изначально пустой список).

Сам класс Museum должен иметь методы:

add_exhibit(self, obj) - добавление нового экспоната в музей (в конец списка
 exhibits);
remove_exhibit(self, obj) - удаление экспоната из музея (из списка exhibits
по ссылке obj - на экспонат)
get_info_exhibit(self, indx) - получение информации об экспонате (строка) по
 индексу списка (нумерация с нуля).

Экспонаты представляются объектами своих классов. Для примера объявите в
программе следующие классы экспонатов:

Picture - для картин;
Mummies - для мумий;
Papyri - для папирусов.

Объекты этих классов должны создаваться следующим образом (с соответствующим
 набором локальных атрибутов):

p = Picture(название, художник, описание)            # локальные атрибуты:
 name - название; author - художник; descr - описание
m = Mummies(имя мумии, место находки, описание)      # локальные атрибуты:
name - имя мумии; location - место находки; descr - описание
pr = Papyri(название папируса, датировка, описание)  # локальные атрибуты:
name - название папируса; date - датировка (строка); descr - описание

Метод get_info_exhibit() класса Museum должен возвращать значение атрибута
descr указанного экспоната в формате:

"Описание экспоната {name}: {descr}"

Например:

"Описание экспоната Девятый вал: Айвазовский написал супер картину."
"""


class Museum:

    def __init__(self, name):
        self.name = name
        self.exhibits = list()

    def add_exhibit(self, obj):
        self.exhibits.append(obj)

    def remove_exhibit(self, obj):
        self.exhibits.remove(obj)

    def get_info_exhibit(self, indx) -> str:
        return f'Описание экспоната {self.exhibits[indx].name}:' \
               f'{self.exhibits[indx].descr}'


class Picture:

    def __init__(self, name, author, descr):
        self.name = name
        self.author = author
        self.descr = descr


class Mummies:

    def __init__(self, name, location, descr):
        self.name = name
        self.location = location
        self.descr = descr


class Papyri:

    def __init__(self, name, date, descr):
        self.name = name
        self.date = date
        self.descr = descr
