"""
Объявите в программе класс с именем Rect (прямоугольник),
объекты которого создаются командой:

rect = Rect(x, y, width, height)

где x, y - координата верхнего левого угла (числа: целые или вещественные);
width, height - ширина и высота прямоугольника (числа: целые или вещественные).

В этом классе определите магический метод, чтобы хэши объектов класса Rect с
равными width, height были равны.
"""


class Rect:

    def __init__(self, x, y, width, height):

        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __hash__(self):

        return hash((self.height, self.width))
