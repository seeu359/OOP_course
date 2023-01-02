"""
 Имеется стихотворение, представленное следующим списком строк:

stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]

Необходимо в каждой строчке этого стиха убрать символы "–?!,.;" в начале и в
 конце каждого слова и разбить строку по словам (слова разделяются одним или
 несколькими пробелами). На основе полученного списка слов, создать объект
 класса StringText командой:

st = StringText(lst_words)

где lst_words - список из слов одной строчки стихотворения. 

С объектами класса StringText должны быть реализованы операторы сравнения:

st1 > st2   # True, если число слов в st1 больше, чем в st2
st1 >= st2  # True, если число слов в st1 больше или равно st2
st1 < st2   # True, если число слов в st1 меньше, чем в st2
st1 <= st2  # True, если число слов в st1 меньше или равно st2

Все объекты класса StringText (для каждой строчки стихотворения) сохранить
 в списке lst_text. Затем, сформировать новый список lst_text_sorted из
 отсортированных объектов класса StringText по убыванию числа слов. Для
 сортировки использовать стандартную функцию sorted() языка Python. После
 этого преобразовать данный список (lst_text_sorted) в список из строк
 (объекты заменяются на соответствующие строки, между словами ставится
 пробел).
"""


stich = ["Я к вам пишу – чего же боле?",
         "Что я могу еще сказать?",
         "Теперь, я знаю, в вашей воле",
         "Меня презреньем наказать.",
         "Но вы, к моей несчастной доле",
         "Хоть каплю жалости храня,",
         "Вы не оставите меня.",
         ]


class StringText:

    def __init__(self, lst_word):
        self.lst_word = lst_word

    def __len__(self):
        return len(self.lst_word)

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __le__(self, other):
        return len(self) <= len(other)


def normalize_data(data: str):
    symbols = '–?!,.;'
    norm_string = ''.join([char for char in data if char not in symbols])
    return norm_string.split()


lst_text = [StringText(lst) for lst in list(map(normalize_data, stich))]


lst_text_sorted = sorted(
    lst_text,
    key=lambda str_text: len(str_text),
    reverse=True,
)

lst_text_sorted = [' '.join(words.lst_word) for words in lst_text_sorted]
