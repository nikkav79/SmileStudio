from django.shortcuts import render
from django.http import HttpResponse

def reviews(request):
    return HttpResponse("<h4>ОТЗЫВЫ<h4>")