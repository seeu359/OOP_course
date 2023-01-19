"""
Известно, что с объектами класса tuple можно складывать только такие же
объекты (кортежи). Например:

t1 = (1, 2, 3)
t2 = t1 + (4, 5) # (1, 2, 3, 4, 5)
Если же мы попытаемся прибавить любой другой итерируемый объект, например,
список:

t2 = t1 + [4, 5]
то возникнет ошибка. Предлагается поправить этот функционал и создать свой
собственный класс Tuple, унаследованный от базового класса tuple и
поддерживающий оператор:

t1 = Tuple(iter_obj)
t2 = t1 + iter_obj  # создается новый объект класса Tuple с новым (соединенным)
 набором данных
где iter_obj - любой итерируемый объект (список, словарь, строка, множество,
кортеж и т.п.)
"""


class Tuple(tuple):

    def __init__(self, _tuple):

        super().__init__()

    def __add__(self, other):
        _tuple = tuple(self) + tuple(other)
        return Tuple(_tuple)
