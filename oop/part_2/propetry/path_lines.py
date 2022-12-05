"""Вам требуется сформировать класс PathLines для описания маршрутов,
состоящих из линейных сегментов. При этом каждый линейный сегмент
предполагается задавать отдельным классом LineTo. Объекты этого класса
будут формироваться командой:

line = LineTo(x, y)

где x, y - следующая координата линейного участка (начало
маршрута из точки 0, 0).

В каждом объекте класса LineTo должны формироваться локальные атрибуты:

x, y - для хранения координат конца линии (начало определяется по
координатам предыдущего объекта).

Объекты класса PathLines должны создаваться командами:

p = PathLines()                   # начало маршрута из точки 0, 0
p = PathLines(line1, line2, ...)  # начало маршрута из точки 0, 0

где line1, line2, ... - объекты класса LineTo.

Сам же класс PathLines должен иметь следующие методы:

get_path() - возвращает список из объектов класса LineTo (если объектов
нет, то пустой список);
get_length() - возвращает суммарную длину пути (сумма длин всех линейных
сегментов);
add_line(self, line) - добавление нового линейного сегмента (объекта
класса LineTo) в конец маршрута.

Пояснение: суммарный маршрут - это сумма длин всех линейных сегментов,
а длина каждого линейного сегмента определяется как евклидовое расстояние по
формуле:

L = sqrt((x1-x0)^2 + (y1-y0)^2)

где x0, y0 - предыдущая точка маршрута; x1, y1 - текущая точка маршрута.
"""

from math import sqrt


class LineTo:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class PathLines:

    def __init__(self, *args):
        self.start_point = LineTo(0, 0)
        self.points = [self.start_point, *args]

    def get_path(self):
        if len(self.points) == 0:
            return []
        return self.points

    def add_line(self, line):
        self.points.append(line)

    def get_length(self):
        length = int()

        def count_sum_length(prev_point, next_point, res, pr_ind, n_ind):
            if n_ind == len(self.points) - 1:
                print(self.points)
                res += sqrt((next_point.x - prev_point.x) *
                            (next_point.x - prev_point.x) +
                            (next_point.y - prev_point.y) *
                            (next_point.y - prev_point.y))
                return res
            else:
                res += sqrt((next_point.x - prev_point.x) *
                            (next_point.x - prev_point.x) +
                            (next_point.y - prev_point.y) *
                            (next_point.y - prev_point.y))
                pr_ind += 1
                n_ind += 1
                return count_sum_length(
                        self.points[pr_ind],
                        self.points[n_ind],
                        res,
                        pr_ind,
                        n_ind,)
        return count_sum_length(self.start_point, self.points[1],
                                length, 0, 1)
