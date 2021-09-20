from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import *
from team.models import *


def lessons_age_groups(request):
    age_groups = AgeGroups.objects.all()
    return render(request,
                  template_name='lessons/lessons_age_groups.html',
                  context={'age_groups': age_groups
                           })


def lessons_details(request, pk):
    lesson_type = LessonsType.objects.get(pk=pk)
    lesson_detail = lesson_type.lessons_set.all()

    return render(request,
                  template_name='lessons/lessons_details.html',
                  context={'lesson_type': lesson_type,
                           'lesson_detail': lesson_detail
                           })


