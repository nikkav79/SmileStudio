from django.shortcuts import render
from django.http import HttpResponse


def lessons(request):
    n = ['Oleg', 'Masha', 'Olya', 'Ksu']
    return render(request, 'lessons/lessons.html', context={'names': n})

def lesson(request):
    return HttpResponse("<h4>ЗАНЯТИЕ<h4>")