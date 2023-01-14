"""
Объявите класс с именем ShopItem (товар), объекты которого создаются командой:

item = ShopItem(name, weight, price)
где name - название товара (строка); weight - вес товара (число: целое или
вещественное); price - цена товара (число: целое или вещественное).

Определите в этом классе магические методы:

__hash__() - чтобы товары с одинаковым названием (без учета регистра), весом и
 ценой имели бы равные хэши;
__eq__() - чтобы объекты с одинаковыми хэшами были равны.

Затем, из входного потока прочитайте строки командой:

lst_in = list(map(str.strip, sys.stdin.readlines()))
Строки имеют следующий формат:

название товара 1: вес_1 цена_1
...
название товара N: вес_N цена_N

Например:

Системный блок: 1500 75890.56
Монитор Samsung: 2000 34000
Клавиатура: 200.44 545
Монитор Samsung: 2000 34000

Как видите, товары в этом списке могут совпадать.

Необходимо для всех этих строчек сформировать соответствующие объекты класса
ShopItem и добавить в словарь с именем shop_items. Ключами словаря должны
 выступать сами объекты, а значениями - список в формате:

[item, total]

где item - объект класса ShopItem; total - общее количество одинаковых
объектов (с одинаковыми хэшами). Подумайте, как эффективно программно
наполнять такой словарь, проходя по списку lst_in один раз.
"""


class ShopItem:

    def __init__(self, name, weight, price):

        self.name: str = name
        self.weight = weight
        self.price = price

    def __hash__(self):

        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):

        return hash(self) == hash(other)


lst_in = ['Системный блок: 1500 75890.56',
          'Монитор Samsung: 2000 34000',
          'Клавиатура: 200.44 545',
          'Монитор Samsung: 2000 34000']

shop_items = dict()

for item in lst_in:
    name = item.split(':')[0]
    weight = item.split()[-2]
    price = item.split()[-1]
    item = ShopItem(name, weight, price)
    shop_item_length_before = len(shop_items)
    shop_items[item] = [item, 1]
    shop_item_length_after = len(shop_items)

    if shop_item_length_before == shop_item_length_after:

        shop_items[item][1] += 1
