"""Вы создаете телефонную записную книжку. Она определяется классом
PhoneBook. Объекты этого класса создаются командой:

p = PhoneBook()

А сам класс должен иметь следующий набор методов:

add_phone(phone) - добавление нового номера телефона (в список);
remove_phone(indx) - удаление номера телефона по индексу списка;
get_phone_list() - получение списка из объектов всех телефонных номеров.

Каждый номер телефона должен быть представлен классом PhoneNumber.
Объекты этого класса должны создаваться командой:

note = PhoneNumber(number, fio)

где number - номер телефона (число) в формате XXXXXXXXXXX (одиннадцати
цифр, X - цифра); fio - Ф.И.О. владельца номера (строка).

В каждом объекте класса PhoneNumber должны формироваться локальные атрибуты:

number - номер телефона (число);
fio - ФИО владельца номера телефона.

Необходимо объявить два класса PhoneBook и PhoneNumber в соответствии
с заданием.
"""


class PhoneNumber:

    def __init__(self, number, fio):
        self.number = number
        self.fio = fio


class PhoneBook:
    number_list = list()

    def add_phone(self, phone: PhoneNumber):
        self.number_list.append(phone)

    def remove_phone(self, index):
        self.number_list.pop(index)

    def get_phone_list(self):
        return self.number_list
