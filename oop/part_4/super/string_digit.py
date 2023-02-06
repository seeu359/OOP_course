"""
Объявите класс StringDigit, который наследуется от стандартного класса str.
Объекты класса StringDigit должны создаваться командой:

sd = StringDigit(string)
где string - строка из цифр (например, "12455752345950"). Если в строке string
окажется хотя бы один не цифровой символ, то генерировать исключение командой:

raise ValueError("в строке должны быть только цифры")
Также в классе StringDigit нужно переопределить оператор + (конкатенации строк)
так, чтобы операции:

sd = sd + "123"
sd = "123" + sd
создавали новые объекты класса StringDigit (а не класса str). Если же при
соединении строк появляется не цифровой символ, то генерировать исключение:

raise ValueError("в строке должны быть только цифры")
"""


class StringDigit(str):

    def __init__(self, value: str):
        if not value.isdigit():
            raise ValueError("в строке должны быть только цифры")

        self.value = value
        super().__init__()

    def __add__(self, other):
        return StringDigit(self.value + other)

    def __radd__(self, other):
        return StringDigit(other + self.value)


class Auto:
    __MIN_WEIGHT = 100
    __MAX_WEIGHT = 1000

    def __init__(self, model):
        self.__verify_model(model)
        self.__model = model

    def __verify_model(self, model):
        if type(model) != str:
            raise TypeError('модель должна представляться строкой')


class BMW(Auto):
    def __init__(self, model, weight):
        super().__init__(model)
        self.__verify_weight(weight)
        self.__weight = weight

    def __verify_weight(self, weight):
        if self.__MIN_WEIGHT > weight or weight > self.__MAX_WEIGHT:
            raise TypeError(
                f'вес автомобиля BMW должен быть в пределах '
                f'[{self.__MIN_WEIGHT}; {self.__MAX_WEIGHT}]'
            )
