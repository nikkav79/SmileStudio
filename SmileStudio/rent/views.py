from django.shortcuts import render
from django.shortcuts import HttpResponse

def rent(request):
    return HttpResponse('<h1> Аренда <h1>')
