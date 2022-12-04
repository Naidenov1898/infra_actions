from django.http import Http404


def index(request):
    return Http404('У меня получилось!')


def second_page(request):
    return Http404('А это вторая страница')
