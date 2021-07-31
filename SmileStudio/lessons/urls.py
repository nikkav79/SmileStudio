from django.urls import path
from .views import *

urlpatterns = [
    path(' ', age_groups_lessons, name='lessons_age_groups'),
    path('/lessons_details<int:pk>/', lessons_details, name='lessons_details')
]
