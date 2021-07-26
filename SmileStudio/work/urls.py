from django.urls import path
from .views import *


urlpatterns = [
    path('', vacancy_list, name='vacancy_list'),
    path('<slug:slug>/', vacancy_detail, name='vacancy_detail'),
]
