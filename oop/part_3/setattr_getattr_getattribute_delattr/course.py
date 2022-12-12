"""
Необходимо создать программу для обучающего курса. Для этого объявляются три
класса:

Course - класс, отвечающий за управление курсом в целом;
Module - класс, описывающий один модуль (раздел) курса;
LessonItem - класс одного занятия (урока).

Структура курса на уровне этих классов, приведена на рисунке ниже:

Объекты класса LessonItem должны создаваться командой:

lesson = LessonItem(название урока, число практических занятий, общая
длительность урока)

Соответственно, в каждом объекте класса LessonItem должны создаваться
локальные атрибуты:

title - название урока (строка);
practices - число практических занятий (целое положительное число);
duration - общая длительность урока (целое положительное число).

Необходимо с помощью магических методов реализовать следующую логику
взаимодействия с объектами класса LessonItem:

1. Проверять тип присваиваемых данных локальным атрибутам. Если типы не
соответствуют требованиям, то генерировать исключение командой:

raise TypeError("Неверный тип присваиваемых данных.")

2. При обращении к несуществующим атрибутам объектов класса LessonItem
возвращать значение False.
3. Запретить удаление атрибутов title, practices и duration в объектах класса
LessonItem.

Объекты класса Module должны создаваться командой:

module = Module(название модуля)

Каждый объект класса Module должен содержать локальные атрибуты:

name - название модуля;
lessons - список из уроков (объектов класса LessonItem), входящих в модуль
(изначально список пуст).

Также в классе Module должны быть реализованы методы:

add_lesson(self, lesson) - добавление в модуль (в конец списка lessons) нового
урока (объекта класса LessonItem);
remove_lesson(self, indx) - удаление урока по индексу в списке lessons.

Наконец, объекты класса Course создаются командой:

course = Course(название курса)

И содержат следующие локальные атрибуты:

name - название курса (строка);
modules - список модулей в курсе (изначально список пуст).

Также в классе Course должны присутствовать следующие методы:

add_module(self, module) - добавление нового модуля в конце списка modules;
remove_module(self, indx) - удаление модуля из списка modules по индексу в
этом списке.
"""


class Course:

    def __init__(self, name):
        self.name = name
        self.modules = list()

    def add_module(self, lesson):
        self.modules.append(lesson)

    def remove_module(self, indx):
        self.modules.pop(indx)


class Module:

    def __init__(self, name):
        self.name = name
        self.lessons = list()

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        self.lessons.pop(indx)


class LessonItem:

    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if key == 'title' and isinstance(value, str):
            object.__setattr__(self, key, value)
        elif key in ('practices', 'duration') and isinstance(value, int):
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, item):
        if item not in ('title', 'duration', 'practices'):
            object.__delattr__(self, item)

    def __getattr__(self, item):
        return False
