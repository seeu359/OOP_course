"""
Объявите класс с именем Model, объекты которого создаются командой:

model = Model()

Объявите в этом классе метод query() для формирования записи базы данных.
Использоваться этот метод должен следующим образом:

model.query(field_1=value_1, field_2=value_2, ..., field_N=value_N)

Например:

model.query(id=1, fio='Sergey', old=33)

Все эти переданные данные должны сохраняться внутри объекта model класса Model.
 Затем, при выполнении команды:

print(model)

В консоль должна выводиться информация об объекте в формате:

"Model: field_1 = value_1, field_2 = value_2, ..., field_N = value_N"

Например:

"Model: id = 1, fio = Sergey, old = 33"

Если метод query() не вызывался, то в консоль выводится строка:

"Model"
"""


class Model:

    def __init__(self):
        self.model = 'Model'

    def query(self, **kwargs):
        result = 'Model: '
        for key, value in kwargs.items():
            result += f'{str(key)} = {str(value)}, '
        self.model = result.rstrip(' ,')

    def __str__(self):
        return self.model
