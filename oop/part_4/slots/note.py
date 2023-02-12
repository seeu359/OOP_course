"""
Объявите класс Note (нота), объекты которого создаются командой:

note = Note(name, ton)
где name - название ноты (допустимые значения: до, ре, ми, фа, соль, ля, си);
ton - тональность ноты (целое число). Тональность (ton) принимает следующие
целые значения:

-1 - бемоль (flat);
0 - обычная нота (normal);
1 - диез (sharp).

Если в названии (name) или тональности (ton) передаются недопустимые значения,
то генерируется исключение командой:

raise ValueError('недопустимое значение аргумента')
В каждом объекте класса Note должны формироваться локальные атрибуты с именами
_name и _ton с соответствующими значениями.

Объявите класс с именем Notes, в объектах которого разрешены только локальные
атрибуты с именами (ограничение задается через коллекцию __slots__):

_do - ссылка на ноту до (объект класса Note);
_re - ссылка на ноту ре (объект класса Note);
_mi - ссылка на ноту ми (объект класса Note);
_fa - ссылка на ноту фа (объект класса Note);
_solt - ссылка на ноту соль (объект класса Note);
_la - ссылка на ноту ля (объект класса Note);
_si - ссылка на ноту си (объект класса Note).

Объект класса Notes должен создаваться командой:

notes = Notes()
и быть только один (одновременно в программе два и более объектов класса Notes
недопустимо). Используйте для этого паттерн Singleton.

В момент создания объекта Notes должны автоматически создаваться перечисленные
локальные атрибуты и ссылаться на соответствующие объекты класса Note
(тональность (ton) у всех нот изначально равна 0).

Обеспечить возможность обращения к нотам по индексам: 0 - до; 1 - ре; ... ; 6
- си. Например:

nota = notes[2]  # ссылка на ноту ми
notes[3]._ton = -1 # изменение тональности ноты фа
Если указывается недопустимый индекс (не целое число, или число, выходящее
за интервал [0; 6]), то генерируется исключение командой:

raise IndexError('недопустимый индекс')
Создайте в программе объект notes класса Notes.
"""


class Note:

    __slots__ = ('_name', '_ton')
    __available_tons = (-1, 0, 1,)
    __available_names = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си',)
    __exception = ValueError('недопустимое значение аргумента')

    def __init__(self, name, ton=0):
        self._name = name
        self._ton = ton

    def __setattr__(self, key, value):
        if key == '_name':
            if value not in self.__available_names:
                raise self.__exception
        elif key == '_ton':
            if value not in self.__available_tons:
                raise self.__exception
        object.__setattr__(self, key, value)


class Notes:

    __slots__ = ('_do', '_re', '_mi', '_fa', '_solt', '_la', '_si')
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            return cls.__instance
        return cls.__instance

    def __init__(self):
        self._do = Note('до', 0)
        self._re = Note("ре", 0)
        self._mi = Note("ми", 0)
        self._fa = Note("фа", 0)
        self._solt = Note("соль", 0)
        self._la = Note("ля", 0)
        self._si = Note("си", 0)

    def __getitem__(self, item):
        try:
            notes_list = (
                self._do, self._re, self._mi, self._fa, self._solt, self._la,
                self._si
            )
            return notes_list[item]
        except IndexError:
            raise IndexError('недопустимый индекс')


notes = Notes()
