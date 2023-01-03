"""
Перед вами стоит задача выделения файлов с определенными расширениями из
списка файлов, например:

filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc",
"my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]

Для этого необходимо объявить класс FileAcceptor, объекты которого создаются
командой:

acceptor = FileAcceptor(ext1, ..., extN)

где ext1, ..., extN - строки с допустимыми расширениями файлов, например:
'jpg', 'bmp', 'jpeg'.

После этого предполагается использовать объект acceptor в стандартной функции
filter языка Python следующим образом:

filenames = list(filter(acceptor, filenames))

То есть, объект acceptor должен вызываться как функция:

acceptor(filename) 

и возвращать True, если файл с именем filename содержит расширения, указанные
при создании acceptor, и False - в противном случае. Кроме того, с объектами
класса FileAcceptor должен выполняться оператор:

acceptor12 = acceptor1 + acceptor2

Здесь формируется новый объект acceptor12 с уникальными расширениями первого и
второго объектов. Например:

acceptor1 = FileAcceptor("jpg", "jpeg", "png")
acceptor2 = FileAcceptor("png", "bmp")
acceptor12 = acceptor1 + acceptor2    # ("jpg", "jpeg", "png", "bmp")
"""
import os.path


class FileAcceptor:

    def __init__(self, *args):
        self.extensions = (*args,)

    def __call__(self, file):

        _, file_extension = os.path.splitext(file)
        return file_extension[1:] in self.extensions

    def __add__(self, other):

        result_array = set(self.extensions + other.extensions)
        return FileAcceptor(*result_array)

    def __str__(self):
        return str(self.extensions)
