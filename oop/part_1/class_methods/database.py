"""Из входного потока читаются строки данных с помощью команды:

lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка
строк из входного потока
в формате: id, name, old, salary (записанные через пробел). Например:

1 Сергей 35 120000
2 Федор 23 12000
3 Иван 13 1200
...

То есть, каждая строка - это элемент списка lst_in.

Необходимо в класс DataBase:

class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')
добавить два метода:

select(self, a, b) - возвращает список из элементов списка lst_data в диапазоне
[a; b] (включительно) по их индексам (не id, а индексам списка); также учесть,
что граница b может превышать длину списка.
insert(self, data) - для добавления в список lst_data новых данных
из переданного списка строк data;

Каждая запись в списке lst_data должна быть представлена словарем в формате:

{'id': 'номер', 'name': 'имя', 'old': 'возраст', 'salary': 'зарплата'}

Например:

{'id': '1', 'name': 'Сергей', 'old': '35', 'salary': '120000'}"""
# import sys


# lst_in = list(map(str.strip, sys.stdin.readlines()))


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def select(self, lower_bound, upper_bound):
        if upper_bound > len(self.lst_data) - 1:
            return self.lst_data[lower_bound:]
        return self.lst_data[lower_bound:upper_bound+1]

    def insert(self, data):
        for man in data:
            self.lst_data.append(dict(zip(self.FIELDS, man.split())))
