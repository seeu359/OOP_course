"""
Объявите класс-декоратор InputDigits для декорирования стандартной функции
input так, чтобы при вводе строки из целых чисел, записанных через пробел,
например:

"12 -5 10 83"

на выходе возвращался список из целых чисел:

[12, -5, 10, 83]
"""


class InputValues:

    def __init__(self, render):
        self.render = render

    def __call__(self, func, *args, **kwargs):
        def wrapper():
            numbers: str = func()

            return list(map(self.render(), numbers.split(' ')))
        return wrapper


class RenderDigit:

    def __call__(self, num, *args, **kwargs):
        try:
            int(num)
            return int(num)
        except ValueError:
            return None


@InputValues(render=RenderDigit)
def input_dg():
    return input()
