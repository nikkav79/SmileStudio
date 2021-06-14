from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Страница сайта SmileStudio')

def categories(request, catid):
    return HttpResponse(f'<h1>Страница сайта SmileStudio</h1><p>{catid}</p>')
