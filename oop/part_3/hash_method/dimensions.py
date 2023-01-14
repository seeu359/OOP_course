"""
 Объявите класс с именем Dimensions, объекты которого создаются командой:

d = Dimensions(a, b, c)
где a, b, c - положительные числа (целые или вещественные), описывающие
габариты некоторого тела: высота, ширина и глубина.

Каждый объект класса Dimensions должен иметь аналогичные публичные атрибуты
a, b, c (с соответствующими числовыми значениями). Также для каждого объекта
 должен вычисляться хэш на основе всех трех габаритов: a, b, c.

С помощью функции input() прочитайте из входного потока строку, записанную
в формате:

"a1 b1 c1; a2 b2 c2; ... ;aN bN cN"

Например:

"1 2 3; 4 5 6.78; 1 2 3; 0 1 2.5"

Если какой-либо габарит оказывается отрицательным значением или равен нулю,
то при создании объектов должна генерироваться ошибка командой:

raise ValueError("габаритные размеры должны быть положительными числами")
Сформируйте на основе прочитанной строки список lst_dims из объектов
класса Dimensions. После этого отсортируйте этот список по возрастанию
(неубыванию) хэшей этих объектов так, чтобы объекты с равными хэшами стояли
друг за другом.
"""


class Dimensions:

    def __init__(self, a, b, c):
        self.__check_dimensions(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def __check_dimensions(*args):
        for dim in args:

            if dim < 0:
                raise ValueError(
                    'габаритные размеры должны быть положительными числами'
                )

    def __hash__(self):

        return hash((self.a, self.b, self.c))


data = '1 2 3; 4 5 6.78'

lst_dims = list()
temp_list_value = list()

for i in data.split(';'):
    split = i.split()
    try:
        temp_list_value.append(list(map(int, split)))
    except ValueError:
        temp_list_value.append(list(map(float, split)))


for i in temp_list_value:
    if i[0] <= 0 or i[1] <= 0 or i[2] <= 0:
        raise ValueError(
            'габаритные размеры должны быть положительными числами'
        )
    lst_dims.append(Dimensions(i[0], i[1], i[2]))


lst_dims.sort(key=lambda dim: hash(dim))
