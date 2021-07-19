from django.urls import path
from team.views import *


urlpatterns = [
    path('', VacancyView.vacancy_main)
]
