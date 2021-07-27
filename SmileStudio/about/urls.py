from django.urls import path
from .views import *

urlpatterns = [
    path('', ContactsListView.as_view(), name='contacts_cbv_url'),
]
