from django.urls import path
from .views import NewsFlowListView, NewsFlowDetailsView


urlpatterns = [
    path('NewsFlow/', NewsFlowListView.as_view()),
    path('NewsFlow/<str:slug>/', NewsFlowDetailsView.as_view())
]
