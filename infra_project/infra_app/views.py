from django.http import HttpResponse
from rest_framework import status


def index(request):
    content = 'У меня получилось!'
    return HttpResponse(content, status=status.HTTP_200_OK)


def second_page(request):
    content = 'А это вторая страница'
    return HttpResponse(content, status=status.HTTP_200_OK)
