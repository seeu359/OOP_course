"""
Вам необходимо написать программу по работе с массивом однотипных данных
(например, только числа или строки и т.п.). Для этого нужно объявить класс
с именем Array, объекты которого создаются командой:

ar = Array(max_length, cell)
где max_length - максимальное количество элементов в массиве; cell - ссылка на
класс, описывающий отдельный элемент этого массива (см. далее, класс Integer).
Начальные значения в ячейках массива (в объектах класса Integer) должны быть
равны 0.

Для работы с целыми числами объявите в программе еще один класс с именем
Integer, объекты которого создаются командой:

cell = Integer(start_value)
где start_value - начальное значение ячейки (в данном случае - целое число).

В классе Integer должно быть следующее свойство (property):

value - для изменения и считывания значения из ячейки (само значение хранится
в локальной приватной переменной; имя придумайте сами).

При попытке присвоить не целое число должно генерироваться исключение командой:

raise ValueError('должно быть целое число')
Для обращения к отдельным элементам массива в классе Array необходимо
определить набор магических методов для следующих операций:

value = ar[0] # получение значения из первого элемента (ячейки) массива ar
ar[1] = value # запись нового значения во вторую ячейку массива ar
Если индекс не целое число или число меньше нуля или больше либо равно
max_length, то должно генерироваться исключение командой:

raise IndexError('неверный индекс для доступа к элементам массива')
"""


class Array:

    def __init__(self, max_length, cell):

        self.max_length = max_length
        self.cell = cell
        self.__array: list = [
            self.cell() for _ in range(self.max_length)
        ]

    def __getitem__(self, item):
        if not isinstance(item, int) or not 0 <= item < self.max_length \
                or item < 0:
            raise IndexError('неверный индекс для доступа к элементам массива')
        return self.__array[item].value

    def __setitem__(self, key, value):
        if not isinstance(key, int) or not 0 <= key < self.max_length \
                or key < 0:
            raise IndexError('неверный индекс для доступа к элементам массива')
        self.__array[key].value = value

    def __str__(self):
        return ' '.join([str(value.start_value) for value in self.__array])

    def __repr__(self):
        return ' '.join([str(value.start_value) for value in self.__array])


class Integer:

    def __init__(self, start_value=0):

        self.start_value = start_value

    @property
    def value(self):
        return self.start_value

    @value.setter
    def value(self, value):
        if not isinstance(value, int):
            raise ValueError('должно быть целое число')
        self.start_value = value
