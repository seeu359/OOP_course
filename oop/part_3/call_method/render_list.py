"""
Предположим, вам необходимо создать программу по преобразованию списка строк,
например:

lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]

в следующий фрагмент HTML-разметки (многострочной строки, кавычки выводить
не нужно):

'''<ul>
<li>Пункт меню 1</li>
<li>Пункт меню 2</li>
<li>Пункт меню 3</li>
</ul>'''

Для этого необходимо объявить класс RenderList, объекты которого создаются
командой:

render = RenderList(type_list)

где type_list - тип списка (принимает значения: "ul" - для списка с тегом
<ul> и "ol" - для списка с тегом <ol>). Если значение параметра type_list
другое (не "ul" и не "ol"), то формируется список с тегом <ul>.

Затем, предполагается использовать объект render следующим образом:
"""


class RenderList:

    def __init__(self, type_list):
        self.type_list = type_list

    def __call__(self, title_list, *args, **kwargs):
        result = [f'<{self.type_list}>\n', ]
        for title in title_list:
            result.append(f'<li>{title}</li>\n')
        result.append(f'</{self.type_list}>')
        return ''.join(result)

    def __setattr__(self, key, value):
        if key == 'type_list':
            if value != 'ul' and value != 'ol':
                object.__setattr__(self, key, 'ul')
            else:
                object.__setattr__(self, key, value)
