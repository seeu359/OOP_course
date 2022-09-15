"""
Объявите в программе класс Cart (корзина), объекты которого создаются командой:

cart = Cart()
Каждый объект класса Cart должен иметь локальное свойство goods - список
объектов для покупки (объекты классов Table, TV, Notebook и Cup). Изначально
этот список должен быть пустым.

В классе Cart объявить методы:

add(self, gd) - добавление в корзину товара, представленного объектом gd;
remove(self, indx) - удаление из корзины товара по индексу indx;
get_list(self) - получение из корзины товаров в виде списка из строк:

['<наименовние_1>: <цена_1>',
'<наименовние_2>: <цена_2>',
...
'<наименовние_N>: <цена_N>']

Объявите в программе следующие классы для описания товаров:

Table - столы;
TV - телевизоры;
Notebook - ноутбуки;
Cup - кружки.

Объекты этих классов должны создаваться командой:

gd = ИмяКласса(name, price)
Каждый объект классов товаров должен содержать локальные свойства:

name - наименование;
price - цена.

Создайте в программе объект cart класса Cart. Добавьте в него два телевизора
(TV), один стол (Table), два ноутбука (Notebook) и одну кружку (Cup). Названия
и цены придумайте сами.
"""


class Cart:

    def __init__(self):
        self.goods = list()

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        goods_lst = list()
        for good in self.goods:
            goods_lst.append(f'{good.name}: {good.price}')
        return goods_lst


class Table:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:

    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()

tv1 = TV('LG', 30000)
tv2 = TV('Samsung', 40000)

table = Table('Ikea', 2000)

notebook1 = Notebook('ASUS', 50000)
notebook2 = Notebook('Apple', 100000)

cup = Cup('hi', 500)

cart.add(tv1)
cart.add(tv2)
cart.add(table)
cart.add(notebook1)
cart.add(notebook2)
cart.add(cup)
