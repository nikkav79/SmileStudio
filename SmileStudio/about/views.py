from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse("<h4>О СТУДИИ<h4>")


