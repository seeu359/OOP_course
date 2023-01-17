"""
Объявите в программе класс Person, объекты которого создаются командой:

p = Person(fio, job, old, salary, year_job)
где fio - ФИО сотрудника (строка); job - наименование должности (строка);
old - возраст (целое число); salary - зарплата (число: целое или
вещественное); year_job - непрерывный стаж на указанном месте работы
(целое число).

В каждом объекте класса Person автоматически должны создаваться локальные
атрибуты с такими же именами: fio, job, old, salary, year_job и
соответствующими значениями.

Также с объектами класса Person должны поддерживаться следующие команды:

data = p[indx] # получение данных по порядковому номеру (indx) атрибута
(порядок: fio, job, old, salary, year_job и начинается с нуля)
p[indx] = value # запись в поле с указанным индексом (indx) нового значения
value
for v in p: # перебор всех атрибутов объекта в порядке: fio, job, old, salary,
year_job
    print(v)
При работе с индексами, проверить корректность значения indx. Оно должно быть
целым числом в диапазоне [0; 4]. Иначе, генерировать исключение командой:

raise IndexError('неверный индекс')
"""


class Person:

    MIN_INDEX = 0
    MAX_INDEX = 4

    def __init__(self, fio, job, old, salary, year_job):

        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.__value_list = [
            self.fio, self.job, self.old, self.salary, self.year_job
        ]

    def __getitem__(self, item):
        if not self.MIN_INDEX <= item <= self.MAX_INDEX:
            raise IndexError('неверный индекс')
        return self.__value_list[item]

    def __setitem__(self, key, value):
        if not self.MIN_INDEX <= key <= self.MAX_INDEX:
            raise IndexError('неверный индекс')

        self.__value_list[key] = value

    def __iter__(self):

        return iter(self.__value_list)

    def __next__(self):
        index = 0

        if index <= self.MAX_INDEX:
            index += 1
            return self.__value_list[index]

        raise StopIteration
