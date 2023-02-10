"""
С помощью множественного наследования удобно описывать принадлежность объектов
 к нескольким разным группам. Выполним такой пример.



Определите в программе классы в соответствии с их иерархией, представленной на
рисунке выше:

Digit, Integer, Float, Positive, Negative

Каждый объект этих классов должен создаваться однотипной командой вида:

obj = Имя_класса(value)
где value - числовое значение. В каждом классе следует делать свою проверку на
корректность значения value:

- в классе Digit: value - любое число;
- в классе Integer: value - целое число;
- в классе Float: value - вещественное число;
- в классе Positive: value - положительное число;
- в классе Negative: value - отрицательное число.

Если проверка не проходит, то генерируется исключение командой:

raise TypeError('значение не соответствует типу объекта')
После этого объявите следующие дочерние классы:

PrimeNumber - простые числа; наследуется от классов Integer и Positive;
FloatPositive - наследуется от классов Float и Positive.

Создайте три объекта класса PrimeNumber и пять объектов класса FloatPositive с
произвольными допустимыми для них значениями. Сохраните все эти объекты в виде
списка digits.

Затем, используя функции isinstance() и filter(), сформируйте следующие списки
из указанных объектов:

lst_positive - все объекты, относящиеся к классу Positive;
lst_float - все объекты, относящиеся к классу Float.
"""


class Digit:
    type = None
    positive = None
    negative = None
    __exception = TypeError('значение не соответствует типу объекта')

    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise self.__exception
        self.value = value

    def is_valid_digit(self, value):

        if self.positive:
            if value < 0:
                raise self.__exception
        elif self.negative:
            if value > 0:
                raise self.__exception

        if self.type:
            if not isinstance(value, self.type):
                raise self.__exception


class Integer(Digit):
    type = int

    def __init__(self, value):
        self.is_valid_digit(value)
        super().__init__(value)


class Float(Digit):
    type = float

    def __init__(self, value):
        self.is_valid_digit(value)
        super().__init__(value)


class Positive(Digit):
    positive = True

    def __init__(self, value):
        self.is_valid_digit(value)
        super().__init__(value)


class Negative(Digit):
    negative = True

    def __init__(self, value):
        self.is_valid_digit(value)
        super().__init__(value)


class PrimeNumber(Integer, Positive):

    pass


class FloatPositive(Float, Positive):

    pass


prime_number1 = PrimeNumber(20)
prime_number2 = PrimeNumber(30)
prime_number3 = PrimeNumber(40)

float_positive1 = FloatPositive(1.5)
float_positive2 = FloatPositive(10.5)
float_positive3 = FloatPositive(10.6)
float_positive4 = FloatPositive(20.7)
float_positive5 = FloatPositive(30.9)

digits = [
    prime_number1, prime_number2, prime_number3,
    float_positive1, float_positive2, float_positive3, float_positive4,
    float_positive5
]

lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))
