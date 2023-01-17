"""
Объявите класс Ellipse (эллипс), объекты которого создаются командами:

el1 = Ellipse()  # без создания локальных атрибутов x1, y1, x2, y2
el2 = Ellipse(x1, y1, x2, y2)
где x1, y1 - координаты (числа) левого верхнего угла; x2, y2 - координаты
(числа) нижнего правого угла. Первая команда создает объект класса Ellipse
без локальных атрибутов x1, y1, x2, y2. Вторая команда создает объект с
локальными атрибутами x1, y1, x2, y2 и соответствующими переданными
значениями.

В классе Ellipse объявите магический метод __bool__(), который бы возвращал
True, если все локальные атрибуты x1, y1, x2, y2 существуют и False -
в противном случае.

Также в классе Ellipse нужно реализовать метод:

get_coords() - для получения кортежа текущих координат объекта.

Если координаты отсутствуют (нет локальных атрибутов x1, y1, x2, y2),
то метод get_coords() должен генерировать исключение командой:

raise AttributeError('нет координат для извлечения')
Сформируйте в программе список с именем lst_geom, содержащий четыре объекта
класса Ellipse. Два объекта должны быть созданы командой

Ellipse()
и еще два - командой:

Ellipse(x1, y1, x2, y2)
Переберите список в цикле и вызовите метод get_coords() только для объектов,
имеющих координаты x1, y1, x2, y2. (Помните, что для этого был определен
магический метод __bool__()).
"""


class Ellipse:

    def __init__(self, *args):

        self.args = args

        if len(self.args) != 4:
            pass
        else:
            self.x1 = args[0]
            self.y1 = args[1]
            self.x2 = args[2]
            self.y2 = args[3]

    def get_coords(self):
        if not bool(self):
            raise AttributeError('нет координат для извлечения')
        return self.x1, self.y1, self.x2, self.y2

    def __bool__(self):

        return len(self.args) == 4


ellipse1 = Ellipse()
ellipse2 = Ellipse()
ellipse3 = Ellipse(1, 2, 3, 4)
ellipse4 = Ellipse(1, 2, 31, 6)

lst_geom = [ellipse1, ellipse2, ellipse3, ellipse4]

for ellipse in lst_geom:

    if ellipse:
        ellipse.get_coords()
