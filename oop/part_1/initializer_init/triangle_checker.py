"""
Объявите класс TriangleChecker, объекты которого можно было бы создавать
командой:

tr = TriangleChecker(a, b, c)
Здесь a, b, c - длины сторон треугольника.

В классе TriangleChecker необходимо объявить метод is_triangle(), который бы
возвращал следующие коды:

1 - если хотя бы одна сторона не число (не float или int) или хотя бы одно
число меньше или равно нулю;
2 - указанные числа a, b, c не могут являться длинами сторон треугольника;
3 - стороны a, b, c образуют треугольник.

Проверку параметров a, b, c проводить именно в таком порядке.

Прочитайте из входного потока строку, содержащую три числа, разделенных
пробелами, командой:

a, b, c = map(int, input().split())
Затем, создайте объект tr класса TriangleChecker и передайте ему прочитанные
значения a, b, c. Вызовите метод is_triangle() из объекта tr и выведите
результат на экран (код, который она вернет)
"""


def is_triangle(a, b, c):
    for x in (a, b, c):
        if not isinstance(x, (float, int)):
            return 1
        return TriangleChecker(a, b, c)


class TriangleChecker:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not all(list(map(lambda x: x > 0, (self.a, self.b, self.c)))):
            return 1

        a, b, c = self.a, self.b, self.c
        if a >= b + c or b >= c + a or c >= b + a:
            return 2
        return 3


a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
