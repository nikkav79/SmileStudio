from django.urls import path
from .views import *

urlpatterns = [
    path('', lessons_age_groups, name='lessons_age_groups_url'),
    path('/lessons_details<int:pk>/', lessons_details, name='lessons_details_url')
]
