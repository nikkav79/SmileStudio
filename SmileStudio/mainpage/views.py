from django.shortcuts import render
from django.http import HttpResponse

def mainpage(request):
    return HttpResponse("<h4>ГЛАВНАЯ СТРАНИЦА<h4>")