from django.urls import path
from .views import *


urlpatterns = [
    path('', VacancyView.vacancy_main,
         name='vacancy_list_url'),
    path('<str:slug>', VacancyView.vacancy_distinct,
         name='vacancy_distinct_url'),
]
