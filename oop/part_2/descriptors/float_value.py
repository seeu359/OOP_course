"""Объявите дескриптор данных FloatValue, который бы устанавливал и
возвращал вещественные значения. При записи вещественного числа должна
выполняться проверка на вещественный тип данных. Если проверка не проходит,
то генерировать исключение командой:

raise TypeError("Присваивать можно только вещественный тип данных.")

Объявите класс Cell, в котором создается объект value дескриптора
FloatValue. А объекты класса Cell должны создаваться командой:

cell = Cell(начальное значение ячейки)

Объявите класс TableSheet, с помощью которого создается таблица из N
строк и M столбцов следующим образом:

table = TableSheet(N, M)

Каждая ячейка этой таблицы должна быть представлена объектом класса Cell,
pаботать с вещественными числами через объект value
(начальное значение должно быть 0.0).

В каждом объекте класса TableSheet должен формироваться локальный атрибут:

cells - список (вложенный) размером N x M, содержащий ячейки таблицы
(объекты класса Cell).

Создайте объект table класса TableSheet с размером таблицы N = 5, M = 3.
Запишите в эту таблицу числа от 1.0 до 15.0 (по порядку).

"""


class FloatValue:
    @classmethod
    def validate_float(cls, number):
        if not isinstance(number, float):
            raise TypeError(
                'Присваивать можно только вещественный тип данных'
            )

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.validate_float(value)
        instance.__dict__[self.name] = value


class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value


class TableSheet:

    def __init__(self, n, m):
        self.N = n
        self.M = m
        self.cells = [[Cell() for _ in range(m)] for
                      _ in range(n)]


table = TableSheet(5, 3)

table.cells = [[Cell(float(i + 1 + j * table.M)) for i in range(table.M)]
               for j in range(table.N)]
