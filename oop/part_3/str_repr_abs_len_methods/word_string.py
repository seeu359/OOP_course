"""
Объявите класс WordString, объекты которого создаются командами:

w1 = WordString()
w2 = WordString(string)

где string - передаваемая строка. Например:

words = WordString("Курс по Python ООП")

Реализовать следующий функционал для объектов этого класса:

len(words) - должно возвращаться число слов в переданной строке
(слова разделяются одним или несколькими пробелами);
words(indx) - должно возвращаться слово по его индексу
(indx - порядковый номер слова в строке, начиная с 0).

Также в классе WordString реализовать объект-свойство (property):

string - для передачи и считывания строки.
"""


class WordString:

    def __init__(self, string=''):
        self.__string: str = string

    def __len__(self):
        return len(self.__string.split())

    def __call__(self, indx, *args, **kwargs):
        return self.words(indx)

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, string):
        self.__string = string.split()

    def words(self, indx):
        return self.__string.split()[indx]
