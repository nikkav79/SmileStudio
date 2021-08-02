from django.urls import path
from.views import *

urlpatterns = [
    path('', news, name='news_posts_url'),
    path('<str:slug>/', NewsDetails.as_view(), name='news_details_url')
]