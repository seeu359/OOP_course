"""Объявите класс Point для представления точек на плоскости.
Создавать объекты этого класса предполагается командой:

pt = Point(x, y)

Здесь x, y - числовые координаты точки на плоскости (числа), то есть, в каждом
объекте этого класса создаются локальные свойства x, y, которые хранят
конкретные координаты точки.

Необходимо в классе Point реализовать метод clone(self), который бы создавал
 новый объект класса Point как копию текущего объекта с локальными атрибутами
 x, y и соответствующими значениями.

Создайте в программе объект pt класса Point и еще один объект pt_clone через
вызов метода clone."""


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):

        return Point(self.x, self.y)


pt = Point(3, 2)

pt_clone = Point(1, 2).clone()


class Loader:
    @classmethod
    def json_parse(cls):
        return ""


ld = Loader()

ld.json_parse()
Loader.json_parse()

res = Loader.json_parse()
