"""
Объявите класс GeyserClassic - фильтр для очистки воды. В этом классе должно
быть три слота для фильтров. Каждый слот строго для своего класса фильтра:

Mechanical - для очистки от крупных механических частиц;
Aragon - для последующей очистки воды;
Calcium - для обработки воды на третьем этапе.

Объекты классов фильтров должны создаваться командами:

filter_1 = Mechanical(дата установки)
filter_2 = Aragon(дата установки)
filter_3 = Calcium(дата установки)

Во всех объектах этих классов должен формироваться локальный атрибут:

date - дата установки фильтров (для простоты - положительное вещественное
число).

Также нужно запретить изменение этого атрибута после создания объектов этих
 классов (только чтение). В случае присвоения нового значения, прежнее
 значение не менять. Ошибок никаких не генерировать.

Объекты класса GeyserClassic должны создаваться командой:

g = GeyserClassic()

А сам класс иметь атрибут:

MAX_DATE_FILTER = 100 - максимальное время работы фильтра (любого)

и следующие методы:

add_filter(self, slot_num, filter) - добавление фильтра filter в указанный
слот slot_num (номер слота: 1, 2 и 3), если он (слот) пустой (без фильтра).
Также здесь следует проверять, что в первый слот можно установить только
объекты класса Mechanical, во второй - объекты класса Aragon и в третий -
объекты класса Calcium. Иначе слот должен оставаться пустым.

remove_filter(self, slot_num) - извлечение фильтра из указанного слота
(slot_num: 1, 2, и 3);

get_filters(self) - возвращает кортеж из набора трех фильтров в порядке их
установки (по возрастанию номеров слотов);

water_on(self) - включение воды: возвращает True, если вода течет и
False - в противном случае.

Метод water_on() должен возвращать значение True при выполнении следующих
условий:

- все три фильтра установлены в слотах;
- все фильтры работают в пределах срока службы (значение (time.time() - date)
должно быть в пределах [0; MAX_DATE_FILTER])
"""
import time


class DateSetter:

    def __setattr__(self, key, value):
        if key == 'date' and key not in self.__dict__:
            object.__setattr__(self, key, value)


class GeyserClassic:

    MAX_DATE_FILTER = 100

    def __init__(self):
        self.slot_1: Mechanical | None = None
        self.slot_2: Aragon | None = None
        self.slot_3: Calcium | None = None

    def add_filter(self, slot_num, filter):
        if slot_num == 1:
            if isinstance(filter, Mechanical) and self.slot_1 is None:
                self.slot_1 = filter
        if slot_num == 2:
            if isinstance(filter, Aragon) and self.slot_2 is None:
                self.slot_2 = filter
        if slot_num == 3:
            if isinstance(filter, Calcium) and self.slot_3 is None:
                self.slot_3 = filter

    def remove_filter(self, slot_num):
        if slot_num == 1:
            self.slot_1 = None
        elif slot_num == 2:
            self.slot_2 = None
        else:
            self.slot_3 = None

    def get_filters(self):
        return self.slot_1, self.slot_2, self.slot_3

    def water_on(self):
        if self.slot_1 is None or self.slot_2 is None or self.slot_3 is None:
            return False
        if not 0 <= time.time() - self.slot_1.date <= self.MAX_DATE_FILTER:
            return False
        if not 0 <= time.time() - self.slot_2.date <= self.MAX_DATE_FILTER:
            return False
        if not 0 <= time.time() - self.slot_3.date <= self.MAX_DATE_FILTER:
            return False
        return True


class Mechanical(DateSetter):

    def __init__(self, date):
        self.date = date


class Aragon(DateSetter):

    def __init__(self, date):
        self.date = date


class Calcium(DateSetter):

    def __init__(self, date):
        self.date = date
