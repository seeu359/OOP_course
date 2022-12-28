"""
Объявите класс с именем ListMath, объекты которого можно создавать командами:

lst1 = ListMath() # пустой список
lst2 = ListMath([1, 2, -5, 7.68]) # список с начальными значениями

В качестве значений элементов списка объекты класса ListMath должны
отбирать только целые и вещественные числа, остальные игнорировать
(если указываются в списке). Например:

lst = ListMath([1, "abc", -5, 7.68, True]) # ListMath: [1, -5, 7.68]

В каждом объекте класса ListMath должен быть публичный атрибут:

lst_math - ссылка на текущий список объекта (для каждого объекта
создается свой список).

Также с объектами класса ListMath должны работать следующие операторы:

lst = lst + 76 # сложение каждого числа списка с определенным числом
lst = 6.5 + lst # сложение каждого числа списка с определенным числом
lst += 76.7  # сложение каждого числа списка с определенным числом
lst = lst - 76 # вычитание из каждого числа списка определенного числа
lst = 7.0 - lst # вычитание из числа каждого числа списка
lst -= 76.3
lst = lst * 5 # умножение каждого числа списка на указанное число
(в данном случае на 5)
lst = 5 * lst # умножение каждого числа списка на указанное число
(в данном случае на 5)
lst *= 5.54
lst = lst / 13 # деление каждого числа списка на указанное число
(в данном случае на 13)
lst = 3 / lst # деление числа на каждый элемент списка
lst /= 13.0

При использовании бинарных операторов +, -, *, /
должны формироваться новые объекты класса ListMath с новыми списками,
прежние списки не меняются.

При использовании операторов +=, -=, *=, /= значения должны меняться
 внутри списка текущего объекта (новый объект не создается).
"""
from operator import add, sub, mul, truediv


class ListMath:

    def __init__(self, math_array: list | None = None):
        self.lst_math = list()
        if math_array is None:
            self.lst_math = list()
        else:
            for i in math_array:
                if type(i) == int or type(i) == float:
                    self.lst_math.append(i)

    def __add__(self, other):
        return ListMath([add(num, other) for num in self.lst_math])

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        return self + other

    def __sub__(self, other, _r=None):
        if _r is not None:
            return ListMath([sub(other, num) for num in self.lst_math])
        return ListMath([sub(num, other) for num in self.lst_math])

    def __rsub__(self, other):
        return self.__sub__(other, _r=self)

    def __isub__(self, other):
        return self - other

    def __mul__(self, other):
        return ListMath([mul(num, other) for num in self.lst_math])

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        return self * other

    def __truediv__(self, other, _r=None):
        if _r is not None:
            return ListMath([truediv(other, num) for num in self.lst_math])
        return ListMath([truediv(num, other) for num in self.lst_math])

    def __rtruediv__(self, other):
        return self.__truediv__(other, _r=self)

    def __itruediv__(self, other):
        return self / other
