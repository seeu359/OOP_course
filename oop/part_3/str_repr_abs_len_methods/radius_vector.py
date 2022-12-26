"""
Объявите класс с именем RadiusVector для описания и работы с n-мерным вектором
(у которого n координат). Объекты этого класса должны создаваться командами:

# создание 5-мерного радиус-вектора с нулевыми значениями координат
(аргумент - целое число больше 1)
vector = RadiusVector(5)  # координаты: 0, 0, 0, 0, 0

# создание 4-мерного радиус-вектора с координатами: 1, -5, 3.4, 10
(координаты - любые целые или вещественные числа)
vector = RadiusVector(1, -5, 3.4, 10)

То есть, при передаче одного значения, оно интерпретируется, как
размерность нулевого радиус-вектора. Если же передается более одного
числового аргумента, то они интерпретируются, как координаты радиус-вектора.

Класс RadiusVector должен содержать методы:

set_coords(coord_1, coord_2, ..., coord_N) - для изменения координат
радиус-вектора;
get_coords() - для получения текущих координат радиус-вектора (в виде кортежа).

Также с объектами класса RadiusVector должны поддерживаться следующие функции:

len(vector) - возвращает число координат радиус-вектора (его размерность);
abs(vector) - возвращает длину радиус-вектора (вычисляется как:
sqrt(coord_1*coord_1 + coord_2*coord_2 + ... + coord_N*coord_N) -
корень квадратный из суммы квадратов координат).
"""
from math import sqrt


class RadiusVector:

    def __init__(self, *coords):
        if len(coords) == 1:
            self.coords = [0 for _ in range(coords[0])]
        else:
            self.coords = coords

    def get_coords(self):
        return tuple(self.coords)

    def set_coords(self, *args):
        coords = self.get_coords()
        if len(args) > len(coords):
            self.coords = args[:len(coords)]
        else:
            self.coords = args + tuple(self.coords[len(args):])

    def __len__(self):
        if len(self.coords) == 1:
            return self.coords[0]
        return len(self.coords)

    def __abs__(self):
        _sum = 0
        for vector in self.coords:
            _sum += vector * vector
        return sqrt(_sum)
