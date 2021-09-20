from django.urls import path
from .views import *

urlpatterns = [
    path('', Contacts.as_view(), name='contacts_url'),
]