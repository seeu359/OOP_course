"""
 Вам необходимо написать программу для удобного обращения с
 таблицами однотипных данных (чисел, строк, булевых значений и т.п.), то есть,
 все ячейки таблицы должны представлять какой-то один указанный тип.



Для этого в программе необходимо объявить три класса:

TableValues - для работы с таблицей в целом;
CellInteger - для операций с целыми числами;
IntegerValue - дескриптор данных для работы с целыми числами.

Начнем с дескриптора IntegerValue. Это должен быть дескриптор данных (то есть,
и для записи и считывания значений). Если присваиваемое значение не является
целым числом, должно генерироваться исключение командой:

raise ValueError('возможны только целочисленные значения')
Следующий класс CellInteger описывает одну ячейку таблицы для работы с
целыми числами. В этом классе должен быть публичный атрибут (атрибут класса):

value - объект дескриптора, класса IntegerValue.

А объекты класса CellInteger должны создаваться командой:

cell = CellInteger(start_value)
где start_value - начальное значение ячейки (по умолчанию равно 0 и
сохраняется в ячейке через дескриптор value).

Наконец, объекты последнего класса TableValues создаются командой:

table = TableValues(rows, cols, cell=CellInteger)
где rows, cols - число строк и столбцов (целые числа); cell - ссылка на
класс, описывающий работу с отдельными ячейками таблицы. Если параметр cell
не указан, то генерировать исключение командой:

raise ValueError('параметр cell не указан')
Иначе, в объекте table класса TableValues создается двумерный (вложенный)
кортеж с именем cells размером rows x cols, состоящий из объектов указанного
класса (в данном примере - класса CellInteger).

Также в классе TableValues предусмотреть возможность обращения к отдельной
ячейке по ее индексам, например:

value = table[1, 2] # возвращает значение ячейки с индексом (1, 2)
table[0, 0] = value # записывает новое значение в ячейку (0, 0)
Обратите внимание, по индексам сразу должно возвращаться значение ячейки, а не
объект класса CellInteger. И то же самое с присваиванием нового значения.
"""


class IntegerValue:

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError('возможны только целочисленные значения')
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):

        return instance.__dict__[self.name]


class CellInteger:

    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value


class TableValues:

    def __init__(self, rows, cols, cell=None):

        self.rows = rows
        self.cols = cols
        if not cell:
            raise ValueError('параметр cell не указан')
        self.cells = self.create_cells()

    def create_cells(self):
        result = list()
        temp_lst = [CellInteger()] * self.cols
        for _ in range(self.rows):
            result.append(tuple(temp_lst))
        return tuple(result)

    def __setitem__(self, key, value):
        row = key[0]
        col = key[1]
        self.cells[row][col].value = value

    def __getitem__(self, item):
        row = item[0]
        col = item[1]
        return self.cells[row][col].value
