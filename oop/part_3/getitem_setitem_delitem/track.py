"""
Вам необходимо для навигатора реализовать определение маршрутов.
Для этого в программе нужно объявить класс Track, объекты которого создаются
командой:

tr = Track(start_x, start_y)
где start_x, start_y - координата начала пути.

В этом классе должен быть реализован следующий метод:

add_point(x, y, speed) - добавление новой точки маршрута (линейный сегмент),
который можно пройти со средней скоростью speed.

Также с объектами класса Track должны выполняться команды:

coord, speed = tr[indx] # получение координаты (кортеж с двумя числами) и
скорости (число) для линейного сегмента маршрута с индексом indx
tr[indx] = speed # изменение средней скорости линейного участка маршрута по
индексу indx
Если индекс (indx) указан некорректно (должен быть целым числом от 0 до N-1,
где N - число линейных сегментов в маршруте), то генерируется исключение
командой:

raise IndexError('некорректный индекс')
Пример использования класса (эти строчки в программе не писать):
"""


class Track:

    def __init__(self, start_x, start_y):

        self.start_x = start_x
        self.start_y = start_y
        self.track = list()

    def add_point(self, x, y, speed):

        self.track.append([(x, y), speed])

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key > len(self.track) - 1:
            raise IndexError('некорректный индекс')
        self.track[key][1] = value

    def __getitem__(self, item):
        if not isinstance(item, int) or item > len(self.track) - 1:
            raise IndexError('некорректный индекс')
        return self.track[item]


track = Track(1, 2)
track.add_point(2, 3, 500)

a, b = track[0]

print(a, b)
