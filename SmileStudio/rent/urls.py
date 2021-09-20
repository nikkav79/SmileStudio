from django.urls import path
from .views import *

urlpatterns = [
    path('', rent, name='rent_url')
]