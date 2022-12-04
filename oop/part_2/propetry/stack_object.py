"""Реализуйте односвязный список (не список Python, не использовать список
Python для хранения объектов), когда один объект ссылается на следующий и
так по цепочке до последнего:

Для этого объявите в программе два класса: 

StackObj - для описания объектов односвязного списка;
Stack - для управления односвязным списком.

Объекты класса StackObj предполагается создавать командой:

obj = StackObj(данные)

Здесь данные - это строка с некоторым содержимым. Каждый объект класса
StackObj должен иметь следующие локальные приватные атрибуты:

__data - ссылка на строку с данными, указанными при создании объекта;
__next - ссылка на следующий объект класса StackObj
(при создании объекта принимает значение None).

Также в классе StackObj должны быть объявлены объекты-свойства:

next - для записи и считывания информации из локального приватного свойства
__next;
data - для записи и считывания информации из локального приватного свойства
__data.

При записи необходимо реализовать проверку, что __next будет ссылаться
на объект класса StackObj или значение None. Если проверка не проходит,
то __next остается без изменений.

Класс Stack предполагается использовать следующим образом:

st = Stack() # создание объекта односвязного списка

В объектах класса Stack должен быть локальный публичный атрибут:

top - ссылка на первый добавленный объект односвязного списка
(если список пуст, то top = None).

А в самом классе Stack следующие методы:

push(self, obj) - добавление объекта класса StackObj в конец
односвязного списка;
pop(self) - извлечение последнего объекта с его удалением
из односвязного списка;
get_data(self) - получение списка из объектов односвязного списка
(список из строк локального атрибута __data каждого объекта в порядке их
добавления, или пустой список, если объектов нет)."""

objectss = {}


class StackObj:

    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, st_obj):
        if self.check_next_obj(st_obj):
            self.__next = st_obj

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @staticmethod
    def check_next_obj(st_obj):
        return isinstance(st_obj, (StackObj, type(None)))


class Stack:
    def __init__(self):
        self.top: StackObj | None = None
        self.last = None

    def push(self, st_obj: StackObj):
        if self.top is None:
            self.top = st_obj
            self.last = st_obj
            return
        else:
            self.get_last_elem(self.top, st_obj)

    def get_last_elem(self, item, st_obj):
        if item.next:
            return self.get_last_elem(item.next, st_obj)
        elif item.next is None:
            item.next = st_obj
            self.last = st_obj
            return st_obj

    def get_data(self):
        data_list = list()

        if not self.top:
            return []

        def _get_data(data, st_obj):
            if st_obj.next:
                data.append(st_obj.data)
                return _get_data(data, st_obj.next)
            else:
                data.append(st_obj.data)
                return data_list

        return _get_data(data_list, self.top)

    def pop(self):
        if not self.top:
            return self.top
        else:
            def pop_item(item: StackObj):
                if self.top == self.last:
                    _obj = self.last
                    self.last = None
                    self.top = None
                    return _obj
                if item.next == self.last:
                    i = self.last

                    item.next = None

                    return i
                else:
                    pop_item(item.next)

            return pop_item(self.top)
