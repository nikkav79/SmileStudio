from django.contrib import admin
from about.models import *
from lessons.models import *
from media.models import *
from news.models import *
from reviews.models import *
from team.models import *


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('specialization', 'contract', 'created_at', 'is_active')
    list_display_links = ('specialization',)
    search_fields = ('specialization', 'description')


class NewsFlowAdmin(admin.ModelAdmin):
    list_display = ('modified', 'title', 'author', 'created', 'digest')
    list_display_links = ('title',)
    search_fields = ('title', 'digest', 'modified')


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('date', 'lesson', 'user')
    list_display_links = ('date', 'lesson')
    search_fields = ('date', 'lesson', 'team_member')
    # что касается star_choice то для админа имеет
    # смысл смотреть по средней оценке из 3х, её надо придумать в модели Reviews


class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_display_links = ('name',)
    search_fields = ('name', 'description')


class StaffAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'contract')
    list_display_links = ('last_name',)
    search_fields = ('last_name', 'first_name', 'specialization__name')


class TimeTableInline(admin.TabularInline):
    model = TimeTable


class LessonsAdmin(admin.ModelAdmin):
    inlines = [
        TimeTableInline,
    ]
    exclude = ('days',)


admin.site.register(StudioDescription)
admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(ContractType)
admin.site.register(Team, StaffAdmin)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(AgeGroups)
admin.site.register(LessonsType)
admin.site.register(Costs)
admin.site.register(Lessons, LessonsAdmin)
admin.site.register(Media)
admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(ContactDetails)
admin.site.register(SocialNetworks)
admin.site.register(NewsFlow, NewsFlowAdmin)
# 09.07
admin.site.register(Position)
admin.site.register(WeekDays)
admin.site.register(Rent)

