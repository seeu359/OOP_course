"""
Объявите класс Point так, чтобы объекты этого класса можно было создавать
командами:

p1 = Point(10, 20)
p2 = Point(12, 5, 'red')
Здесь первые два значения - это координаты точки на плоскости
(локальные свойства x, y), а третий необязательный аргумент - цвет точки
(локальное свойство color). Если цвет не указывается, то он по умолчанию
принимает значение black.

Создайте тысячу таких объектов с координатами (1, 1), (3, 3), (5, 5), ... то
есть, с увеличением на два для каждой новой точки. Каждый объект следует
поместить в список points (по порядку). Для второго объекта в списке points
укажите цвет 'yellow'.

P.S. На экран в программе ничего выводить не нужно.
"""

STEP_VALUE = 2
END_POINT = 1000


class Point:

    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color


start_x_value = 1
start_y_value = 1
count = 1
points = list()

for i in range(END_POINT):
    point = Point(start_x_value, start_y_value)
    points.append(point)
    count += 1
    start_x_value += STEP_VALUE
    start_y_value += STEP_VALUE

points[1].color = 'yellow'
