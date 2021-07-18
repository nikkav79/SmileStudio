from django.shortcuts import render
from django.http import HttpResponse

def media(request):
    return HttpResponse("<h4>МЕДИА<h4>")
