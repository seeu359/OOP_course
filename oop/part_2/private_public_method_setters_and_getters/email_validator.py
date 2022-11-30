"""
Объявите класс EmailValidator для проверки корректности email-адреса.
Необходимо запретить создание объектов этого класса: при создании экземпляров
должно возвращаться значение None, например:

em = EmailValidator() # None

В самом классе реализовать следующие методы класса (@classmethod):

get_random_email(cls) - для генерации случайного email-адреса по формату:
xxxxxxx...xxx@gmail.com, где x - любой допустимый символ в email (латинский
буквы, цифры, символ подчеркивания и точка);
check_email(cls, email) - возвращает True, если email записан верно и
False - в противном случае.

Корректность строки email определяется по следующим критериям:

- допустимые символы: латинский алфавит, цифры, символы подчеркивания, точки
и собачка @ (одна);
- длина email до символа @ не должна превышать 100 (сто включительно);
- длина email после символа @ не должна быть больше 50 (включительно);
- после символа @ обязательно должна идти хотя бы одна точка;
- не должно быть двух точек подряд.

Также в классе нужно реализовать приватный статический метод класса:

is_email_str(email) - для проверки типа переменной email, если строка,
 то возвращается значение True, иначе - False.

Метод is_email_str() следует использовать в методе check_email() перед
проверкой корректности email. Если параметр email не является строкой,
 то check_email() возвращает False.

Пример использования класса EmailValidator (эти строчки в программе писать
не нужно):

res = EmailValidator.check_email("sc_lib@list.ru") # True
res = EmailValidator.check_email("sc_lib@list_ru") # False

P.S. В программе требуется объявить только класс. На экран ничего выводить не
нужно.
"""

from random import choice, randint
from string import ascii_letters, digits


class EmailValidator:
    symbols = ascii_letters + '._' + digits
    domain = '@gmail.com'
    MAX_LENGTH = 100

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        random_length = randint(0, cls.MAX_LENGTH)
        name = ''.join([symb for symb in range(random_length)
                        for symb in choice(cls.symbols)])
        return name + cls.domain

    @classmethod
    def check_email(cls, email: str):
        if not cls.__is_email_str(email):
            return False
        if len(email.strip(cls.symbols)) != 1:
            return False
        if email.find('..') > -1:
            return False
        name, domain = email.split('@')
        check_list = [cls.__check_name(name), cls.__check_domain(domain)]
        return all(check_list)

    @classmethod
    def __check_name(cls, name):
        if len(name) > cls.MAX_LENGTH:
            return False
        return True

    @classmethod
    def __check_domain(cls, domain):
        if len(domain) > 50:
            return False
        if domain.find('.') == -1:
            return False
        return True

    @staticmethod
    def __is_email_str(email):
        if isinstance(email, str):
            return True
        return False
