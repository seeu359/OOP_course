"""
Объявите в программе класс FloatValidator, объекты которого создаются
командой:

fv = FloatValidator(min_value, max_value)
где min_value, max_value - минимальное и максимальное допустимое значение
(диапазон [min_value; max_value]).

Объекты этого класса предполагается использовать следующим образом:

fv(value)
где value - проверяемое значение. Если value не вещественное число или не
принадлежит диапазону [min_value; max_value], то генерируется исключение
командой:

raise ValueError('значение не прошло валидацию')
По аналогии, объявите класс IntegerValidator, объекты которого создаются
командой:

iv = IntegerValidator(min_value, max_value)
и используются командой:

iv(value)
Здесь также генерируется исключение:

raise ValueError('значение не прошло валидацию')
если value не целое число или не принадлежит диапазону [min_value; max_value].

После этого объявите функцию с сигнатурой:

def is_valid(lst, validators): ...

где lst - список из данных; validators - список из объектов-валидаторов
(объектов классов FloatValidator и IntegerValidator).

Эта функция должна отбирать из списка все значения, которые прошли хотя бы по
одному валидатору. И возвращать новый список с элементами, прошедшими проверку.
"""


class BaseValidator:
    type = None

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if type(value) != self.type or not \
                self.min_value <= value <= self.max_value:
            raise ValueError('значение не прошло валидацию')
        return value


class FloatValidator(BaseValidator):
    type = float


class IntegerValidator(BaseValidator):
    type = int


def is_valid(lst, validators) -> list:
    result_lst = list()

    for value in lst:
        for validator in validators:
            try:
                _value = validator(value)
                result_lst.append(_value)
            except ValueError:
                continue
    return result_lst


fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)

lst_out = is_valid(
    [1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv]
)
