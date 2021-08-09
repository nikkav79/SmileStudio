from django.urls import path
from .views import *

urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('/writetous/', Write.as_view(), name='writetous_url'),
]