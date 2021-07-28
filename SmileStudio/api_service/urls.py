from django.urls import path
from .views import SpecializationListView

urlpatterns = [
    path('team/specializations/', SpecializationListView.as_view())
]
