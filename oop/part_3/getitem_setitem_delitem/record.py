"""
Объявите класс Record (запись), который описывает одну произвольную запись
из БД. Объекты этого класса создаются командой:

r = Record(field_name1=value1,... , field_nameN=valueN)
где field_nameX - наименование поля БД; valueX - значение поля из БД.

В каждом объекте класса Record должны автоматически создаваться локальные
публичные атрибуты по именам полей (field_name1,... , field_nameN) с
соответствующими значениями. Например:

r = Record(pk=1, title='Python ООП', author='Балакирев')
В объекте r появляются атрибуты:

r.pk # 1
r.title # Python ООП
r.author # Балакирев
Также необходимо обеспечить доступ к этим полям (чтение/запись) через
индексы следующим образом:

r[0] = 2 # доступ к полю pk
r[1] = 'Супер курс по ООП' # доступ к полю title
r[2] = 'Балакирев С.М.' # доступ к полю author
print(r[1]) # Супер курс по ООП
r[3] # генерируется исключение IndexError
Если указывается неверный индекс (не целое число или некорректное целое
число), то должно генерироваться исключение командой:

raise IndexError('неверный индекс поля')
"""


class Record:

    def __init__(self, **kwargs):

        self.__dict__ = kwargs
        self.values = list(self.__dict__.keys())

    def __getitem__(self, item):
        try:
            return self.__dict__[self.values[item]]
        except (IndexError, KeyError):
            raise IndexError('неверный индекс поля')

    def __setitem__(self, key, value):
        try:
            self.__dict__[self.values[key]] = value
        except (IndexError, KeyError):
            raise IndexError('неверный индекс поля')
