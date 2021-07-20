from django.shortcuts import render, get_object_or_404
from .models import *


class VacancyView:

    def vacancy_main(self, request):
        context = {
            'vacancies': Vacancy.objects.filter(is_active=True)
        }
        return render(request, 'work/vacancies.html', context=context)

    def vacancy_distinct(self, request, slug):
        vacancy = get_object_or_404(Vacancy, slug=slug)
        context = {
            'vacancy': vacancy
        }
        return render(request, 'work/vacancy_distinct.html', context)
