"""
Подвиг 3. Для последовательной обработки файлов из некоторого списка, например:

filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.8.jpg",
"forest.jpeg", "eq_1.png", "eq_2.png", "my.html", "data.shtml"]

Необходимо объявить класс ImageFileAcceptor, который бы выделял только файлы с
указанными расширениями.

Для этого предполагается создавать объекты класса командой:

acceptor = ImageFileAcceptor(extensions)

где extensions - кортеж с допустимыми расширениями файлов, например:
extensions = ('jpg', 'bmp', 'jpeg').

А, затем, использовать объект acceptor в стандартной функции filter языка
Python следующим образом:
"""
import os


class ImageFileAcceptor:

    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, file, *args, **kwargs):
        _, extension = os.path.splitext(file)
        return True if extension[1:] in self.extensions else False
