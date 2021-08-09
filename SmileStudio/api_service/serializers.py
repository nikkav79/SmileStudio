from rest_framework import serializers
from news.models import NewsFlow


class NewsFlowListSerializer(serializers.ModelSerializer):
    """Список новостей"""

    class Meta:
        model = NewsFlow
        fields = ('created', 'title', 'digest')


class NewsFlowDetailsSerializer(serializers.ModelSerializer):
    """Детали новости"""

    topic = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = NewsFlow
        exclude = ('digest',)
