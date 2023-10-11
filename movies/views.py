import datetime
from django.shortcuts import render, HttpResponse



def index(request):
    message = f'Hello, World!!! Now {datetime.datetime.now()}'
    return HttpResponse(message)
