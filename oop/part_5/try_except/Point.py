"""
lass Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
И создается объект этого класса:

pt = Point(1, 2)
Далее, вам нужно обратиться к атрибуту z объекта pt и, если такой атрибут
существует, то вывести его значение на экран. Иначе вывести строку
(без кавычек):

"Атрибут с именем z не существует"

Реализовать проверку следует с помощью блоков try/except.

Подсказка: при обращении к несуществующему атрибуту генерируется исключение
AttributeError.
"""


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __getattr__(self, item):
        try:
            return self.__dict__[item]
        except ValueError:
            return 'Атрибут с именем z не существует'


pt = Point(1, 2)

print(pt.z)
