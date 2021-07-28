from django.contrib import admin
from .models import *


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('date', 'lesson', 'user')
    list_display_links = ('date', 'lesson')
    search_fields = ('date', 'lesson', 'team_member')
    # что касается star_choice то для админа имеет
    # смысл смотреть по средней оценке из 3х, её надо придумать в модели Reviews


admin.site.register(Reviews, ReviewsAdmin)
