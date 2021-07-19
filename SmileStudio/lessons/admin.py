from django.contrib import admin
from .models import *


"""class TimeTableInline(admin.TabularInline):
    model = TimeTable"""


"""class LessonsAdmin(admin.ModelAdmin):
    inlines = [
        TimeTableInline,
    ]
    exclude = ('days',)"""


admin.site.register(AgeGroups)
admin.site.register(LessonsType)
admin.site.register(Costs)
admin.site.register(WeekDays)
admin.site.register(Lessons, ) # LessonsAdmin
admin.site.register(TimeTable, ) # TimeTableInline
