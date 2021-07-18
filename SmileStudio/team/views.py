from django.shortcuts import render
from django.http import HttpResponse


def team(request):
    return HttpResponse("<h4>КОМАНДА<h4>")
