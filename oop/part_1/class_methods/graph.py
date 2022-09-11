"""
Объявите класс с именем Graph и методами:

set_data(data) - передача набора данных data для последующего отображения
(data - список числовых данных);
draw() - отображение данных (в том же порядке, что и в списке data)

и атрибутом:

LIMIT_Y = [0, 10]

Метод set_data() должен формировать локальное свойство data объекта класса
Graph. Атрибут data должен ссылаться на переданный в метод список. Метод draw()
должен выводить на экран список в виде строки из чисел, разделенных пробелами и
принадлежащие заданному диапазону атрибута LIMIT_Y (границы включаются).

Создайте объект graph_1 класса Graph, вызовите для него метод set_data() и
передайте список:

[10, -5, 100, 20, 0, 80, 45, 2, 5, 7]

Затем, вызовите метод draw() через объект graph_1. На экране должна появиться
строка с соответствующим набором чисел, записанных через пробел.
Например (вывод без кавычек):

"10 0 2 5 7"
"""


class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data

    def draw(self):
        output = list()
        lower_bound, upper_bound = self.LIMIT_Y
        for number in self.data:
            if number in range(lower_bound, upper_bound + 1):
                output.append(str(number))
        return ' '.join(output)


graph_1 = Graph()

graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])

print(graph_1.draw())
