"""
Известно, что в Python мы можем соединять два списка между собой с помощью
оператора +:

lst = [1, 2, 3] + [4.5, -3.6, 0.78]

Но нет реализации оператора -, который бы убирал из списка соответствующие
значения вычитаемого списка, как это показано в примере:

lst = [1, 2, 3, 4, 5, 6] - [5, 6, 7, 8, 1] # [2, 3, 4]
 (порядок следования оставшихся элементов списка должен сохраняться)

Давайте это поправим и создадим такой функционал. Для этого нужно объявить
 класс с именем NewList, объекты которого создаются командами:

lst = NewList() # пустой список
lst = NewList([-1, 0, 7.56, True]) # список с начальными значениями

Реализуйте для этого класса работу с оператором вычитания, чтобы над
объектами класса NewList можно было выполнять следующие действия:

lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]

Также в классе NewList необходимо объявить метод:

get_list() - для возвращения результирующего списка объекта класса NewList
"""


class NewList:

    def __init__(self, _list=None):
        if _list is None:
            self._list = list()
        else:
            self._list = _list

    def __sub__(self, other, _r=None):
        result = list()
        normalize_self = self.bool_to_str() \
            if _r is None else self.bool_to_str(_r)
        if isinstance(other, NewList):
            normalize_other = other.bool_to_str()
        else:
            normalize_other = self.bool_to_str(other)
        for i in normalize_self:
            if i not in normalize_other:
                result.append(i)
            else:
                normalize_other.remove(i)
        return NewList(self.str_to_bool(result))

    def __rsub__(self, other):
        return self.__sub__(self, _r=other)

    def bool_to_str(self, array=None):
        result = list()
        to_for = self._list if array is None else array
        for i in to_for:
            if isinstance(i, bool):
                result.append(str(i))
            else:
                result.append(i)
        return result

    def str_to_bool(self, array):
        result = list()
        for i in array:
            if i == 'False':
                result.append(bool(False))
                continue
            if i == 'True':
                result.append(bool(True))
            else:
                result.append(i)
        return result

    def get_list(self):
        return self._list

    def __str__(self):
        return str(self._list)
