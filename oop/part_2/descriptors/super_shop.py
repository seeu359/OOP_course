from typing import Union


class StringValue:

    def __init__(self, min_length: int = 2, max_length: int = 50):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.validator(value):
            instance.__dict__[self.name] = value

    def validator(self, value: str):
        return isinstance(value, str) and \
                self.min_length <= len(value) <= self.max_length


class PriceValue:

    def __init__(self, max_value: int = 10_000):
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.validator(value):
            instance.__dict__[self.name] = value

    def validator(self, value):
        return isinstance(value, (int, float)) and \
                value <= self.max_value


class Product:
    price = PriceValue()
    goods_name = StringValue()

    def __init__(self, name: str, price: Union[int, float]):
        self.name = name
        self.price = price


class SuperShop:

    def __init__(self, name):
        self.name = name
        self.goods = list()

    def add_product(self, product: Product):
        self.goods.append(product)

    def remove_product(self, product: Product):
        self.goods.remove(product)
