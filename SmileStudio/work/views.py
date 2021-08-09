from django.shortcuts import render, get_object_or_404
from .models import *



def vacancy_list(request):
    context = {'vacancies': Vacancy.objects.filter(is_active=True)}
    return render(request, 'work/vacancy_list.html', context)


def vacancy_detail(request, slug):
    context = {'vacancy': get_object_or_404(Vacancy, slug=slug)}
    return render(request, 'work/vacancy_detail.html', context)
