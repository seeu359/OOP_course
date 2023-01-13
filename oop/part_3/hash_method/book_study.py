"""
Из входного потока необходимо прочитать список строк командой:

lst_in = list(map(str.strip, sys.stdin.readlines()))
Каждая строка содержит информацию об учебном пособии в формате:

"Название; автор; год издания"

Например:

Python; Балакирев С.М.; 2020
Python ООП; Балакирев С.М.; 2021
Python ООП; Балакирев С.М.; 2022
Python; Балакирев С.М.; 2021

Необходимо каждую из этих строк представить объектом класса BookStudy,
которые создаются командой:

bs = BookStudy(name, author, year)
где name - название пособия (строка); author - автор пособия (строка); year -
год издания (целое число). Такие же публичные локальные атрибуты должны быть
в объектах класса BookStudy.

Для каждого объекта реализовать вычисление хэша по двум атрибутам: name и
author (без учета регистра).

Сформировать список lst_bs из объектов класса BookStudy на основе прочитанных
строк (списка lst_in). После этого определить число книг с уникальными хэшами.
Это число сохранить через переменную unique_books (целое число).
"""


class BookStudy:

    def __init__(self, name, author, year):

        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))

lst_in = [
    'Python; Балакирев С.М.; 2020',
    'Python ООП; Балакирев С.М.; 2021',
    'Python ООП; Балакирев С.М.; 2022',
    'Python; Балакирев С.М.; 2021',
]

# здесь продолжайте программу (используйте список строк lst_in)

books = [data.split(';') for data in lst_in]
lst_bs = [BookStudy(data[0], data[1], data[2]) for data in books]
unique_books = len(set([hash(book) for book in lst_bs]))
