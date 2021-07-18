from django.shortcuts import render
from django.http import HttpResponse

def news(request):
    return HttpResponse("<h4>НОВОСТИ<h4>")
