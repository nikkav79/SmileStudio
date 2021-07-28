from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import *


class SpecializationListView(generics.ListAPIView):
    """Вывод списка специализаций"""
    serializer_class = SpecializationListSerializer

    def get_queryset(self):
        specializations = Specialization.objects.filter(is_active=True)
        return specializations
