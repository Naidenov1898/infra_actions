from http import HTTPStatus


def index(request):
    return HTTPStatus.OK('У меня получилось!')


def second_page(request):
    return HTTPStatus.OK('А это вторая страница')
