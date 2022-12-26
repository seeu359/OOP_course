"""
Необходимо объявить класс-декоратор с именем HandlerGET, который будет
имитировать обработку GET-запросов на стороне сервера. Для этого сам класс
HandlerGET нужно оформить так, чтобы его можно было применять к любой функции
как декоратор. Например:

@HandlerGET
def contact(request):
    return "Сергей Балакирев"

Здесь request - это произвольный словарь с данными текущего запроса, например,
 такой: {"method": "GET", "url": "contact.html"}. А функция должна возвращать
 строку.

Затем, при вызове декорированной функции:

res = contact({"method": "GET", "url": "contact.html"})

должна возвращаться строка в формате:

"GET: <данные из функции>"

В нашем примере - это будет:

"GET: Сергей Балакирев"

Если ключ method в словаре request отсутствует, то по умолчанию
подразумевается GET-запрос. Если же ключ method принимает другое значение,
например, "POST", то декорированная функция contact должна возвращать
значение None.

Для реализации имитации GET-запроса в классе HandlerGET следует объявить
вспомогательный метод со следующей сигнатурой:

def get(self, func, request, *args, **kwargs): ...

Здесь func - ссылка на декорируемую функцию; request - словарь с
переданными данными при вызове декорированной функции. Именно в этом методе
следует формировать возвращаемую строку в указанном формате:

"GET: Сергей Балакирев"
"""


class Handler:

    def __init__(self, methods):
        self.methods = methods

    def __call__(self, func, *args, **kwargs):
        def wrapper(request):
            if request.get('method') in ('GET', None):
                return self.get(func, request)
            elif request.get('method') == 'POST':
                return self.post(func, request)
            else:
                return None
        return wrapper

    def get(self, func, request, *args, **kwargs):
        if 'GET' in self.methods:
            return f'GET: {func(request)}'
        return None

    def post(self, func, request, *args, **kwargs):
        if 'POST' in self.methods:
            return f'POST: {func(request)}'
        return None


@Handler(methods=('POST',))
def contact(request):
    return 'контакты'


print(contact({'method': 'POST'}))
