"""

"""


class RetrieveMixin:
    def get(self, request):
        return "GET: " + request.get('url')


class CreateMixin:
    def post(self, request):
        return "POST: " + request.get('url')


class UpdateMixin:
    def put(self, request):
        return "PUT: " + request.get('url')


class GeneralView:
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')

    def render_request(self, request):
        method = request.get('method')

        if not method.upper() in self.allowed_methods:
            raise TypeError(f'Метод {method} не разрешен')
        method_request = method.lower()
        return self.__getattribute__(method_request)(request)


class DetailView(RetrieveMixin, UpdateMixin, GeneralView):
    allowed_methods = ('GET', 'PUT', )
