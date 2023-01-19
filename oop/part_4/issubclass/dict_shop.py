"""
Разрабатывается интернет-магазин. Каждый товар предполагается представлять
классом Thing, объекты которого создаются командой:

thing = Thing(name, price, weight)
где name - наименование товара (строка); price - цена (вещественное число);
weight - вес товара (вещественное число). В каждом объекте этого класса
 создаются аналогичные атрибуты: name, price, weight.

Класс Thing необходимо определить так, чтобы его объекты можно было
использовать в качестве ключей словаря, например:

d = {}
d[thing] = thing
И для каждого уникального набора данных name, price, weight должны
формироваться свои уникальные ключи.

Затем, вам необходимо объявить класс словаря DictShop, унаследованный от
базового класса dict. В этом новом словаре ключами могут выступать только
объекты класса Thing. При попытке указать любой другой тип, генерировать
исключение командой:

raise TypeError('ключами могут быть только объекты класса Thing')
Объекты класса DictShop должны создаваться командами:

dict_things = DictShop() # пустой словарь
dict_things = DictShop(things) # словарь с набором словаря things
где things - некоторый словарь. В инициализаторе следует проверять, чтобы
аргумент thing был словарем, если не так, то выбрасывать исключение:

raise TypeError('аргумент должен быть словарем')
И проверять, чтобы все ключи являлись объектами класса Thing. Если это не
так, то генерировать исключение:

raise TypeError('ключами могут быть только объекты класса Thing')
Дополнительно в классе DictShop переопределить метод:

__setitem__()

с проверкой, что создаваемый ключ является объектом класса Thing. Иначе,
генерировать исключение:

raise TypeError('ключами могут быть только объекты класса Thing')
"""


class Thing(dict):

    def __init__(self, name, price, weight):
        super().__init__()
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self):
        return hash((self.name, self.price, self.weight))


class DictShop(dict):

    def __init__(self, things=None):
        self.things = {} if not things else things
        if not isinstance(self.things, dict):
            raise TypeError('аргумент должен быть словарем')

        for key in self.things.keys():
            if not isinstance(key, Thing):
                raise TypeError(
                    'ключами могут быть только объекты класса Thing'
                )

        super().__init__(self.things)

    def __setitem__(self, key, value):
        if not isinstance(key, Thing):
            raise TypeError('ключами могут быть только объекты класса Thing')
        super().__setitem__(key, value)
