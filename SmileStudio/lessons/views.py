from django.shortcuts import render
from django.http import HttpResponse

def lessons(request):
    return HttpResponse("<h4>ЗАНЯТИЯ И СТОИМОСТЬ<h4>")
