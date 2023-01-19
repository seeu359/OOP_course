"""
Создается проект, в котором предполагается использовать списки из целых чисел.
Для этого вам ставится задача создать класс с именем ListInteger с базовым
классом list и переопределить три метода:

__init__()
__setitem__()
append()

так, чтобы список ListInteger содержал только целые числа. При попытке
присвоить любой другой тип данных, генерировать исключение командой:

raise TypeError('можно передавать только целочисленные значения')
"""


class ListInteger(list):

    def __init__(self, value):

        super().__init__(value)

    def __setitem__(self, key, value):

        if not isinstance(value, int):
            raise TypeError('можно передавать только целочисленные значения')
        super().__setitem__(key, value)

    def append(self, __object) -> None:

        if not isinstance(__object, int):
            raise TypeError('можно передавать только целочисленные значения')
        super().append(__object)
