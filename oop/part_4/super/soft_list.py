"""
Объявите класс SoftList, который наследуется от стандартного класса list.
В классе SoftList следует объявить необходимые магические методы так,
чтобы при обращении к несуществующему элементу (по индексу) возвращалось
значение False (а не исключение Out of Range).
"""


class SoftList(list):

    def __getitem__(self, item):
        try:
            return super().__getitem__(item)
        except IndexError:
            return False
