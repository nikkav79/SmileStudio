from rest_framework.response import Response
from rest_framework.views import APIView

from news.models import *
from .serializers import *


class NewsFlowListView(APIView):
    """Вывод списка новостей"""

    def get(self, request):
        news = NewsFlow.objects.all()
        serializer = NewsFlowListSerializer(news, many=True)
        return Response(serializer.data)


class NewsFlowDetailsView(APIView):
    """Вывод списка новостей"""

    def get(self, request, slug):
        item = NewsFlow.objects.get(slug__iexact=slug)
        serializer = NewsFlowDetailsSerializer(item)
        return Response(serializer.data)
