from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse(
        '<h1>Hello, World!</h1>'
        '<p>Essa é a minha primeira página com Django</p>'
    )
