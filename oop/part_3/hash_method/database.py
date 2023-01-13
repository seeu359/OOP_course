"""
Объявите класс с именем DataBase (база данных - БД), объекты которого
создаются командой:

db = DataBase(path)
где path - путь к файлу с данными БД (строка).

Также в классе DataBase нужно объявить следующие методы:

write(self, record) - для добавления новой записи в БД, представленной
объектом record;
read(self, pk) - чтение записи из БД (возвращает объект Record) по ее
уникальному идентификатору pk (уникальное целое положительное число); запись
ищется в значениях словаря (см. ниже)

Каждая запись БД должна описываться классом Record, а объекты этого класса
создаваться командой:

record = Record(fio, descr, old)
где fio - ФИО некоторого человека (строка); descr - характеристика человека
(строка); old - возраст человека (целое число).

В каждом объекте класса Record должны формироваться следующие локальные
атрибуты:

pk - уникальный идентификатор записи (число: целое, положительное);
формируется автоматически при создании каждого нового объекта;
fio - ФИО человека (строка);
descr - характеристика человека (строка);
old - возраст человека (целое число).

Реализовать для объектов класса Record вычисление хэша по атрибутам: fio и old
(без учета регистра). Если они одинаковы для разных записей, то и хэши должны
получаться равными. Также для объектов класса Record  с одинаковыми хэшами
оператор == должен выдавать значение True, а с разными хэшами - False.

Хранить записи в БД следует в виде словаря dict_db (атрибут объекта db класса
DataBase), ключами которого являются объекты класса Record, а значениями
список из объектов с равными хэшами:

dict_db[rec1] = [rec1, rec2, ..., recN]

где rec1, rec2, ..., recN - объекты класса Record с одинаковыми хэшами.
"""
import sys


class DataBase:

    def __init__(self, path):

        self.path = path
        self.dict_db: dict[Record, list[Record]] = dict()

    def write(self, record):

        len_before = len(self.dict_db)
        self.dict_db[record] = [record]
        len_after = len(self.dict_db)
        if len_before == len_after:
            self.dict_db[record].append(record)

    def read(self, pk):

        for _, value in self.dict_db.items():
            for record in value:

                if record.pk == pk:
                    return record


class Record:
    __PK = 0

    def __new__(cls, *args, **kwargs):

        cls.__PK += 1
        return super().__new__(cls)

    def __init__(self, fio, descr, old):

        self.pk = self.__PK
        self.fio = fio
        self.descr = descr
        self.old = int(old)

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other):

        return hash(self) == hash(other)


lst_in = list(map(str.strip, sys.stdin.readlines()))

db = DataBase('some_path')

for rec in lst_in:

    data = rec.split(';')
    db.write(Record(data[0], data[1], data[2]))

