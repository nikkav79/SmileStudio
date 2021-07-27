from rest_framework import serializers
from about.models import StudioDescription, ContactDetails, ContactDetails
from lessons.models import AgeGroups, LessonsType, Costs, WeekDays, Lessons, TimeTable
from media.models import Media
from news.models import NewsFlow
from reviews.models import Reviews
from team.models import Specialization, Position, ContractType, Team, Vacancy


class SpecializationListSerializer(serializers.ModelSerializer):
    """Список специализаций"""

    class Meta:
        model = Specialization
        fields = '__all__'
