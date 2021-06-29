from django.contrib import admin
from .models import *


# Register your models here.

class VacancyAdmin(admin.ModelAdmin):
    list_display = ('specialization', 'status', 'date_add', 'is_active')
    list_display_links = ('specialization',)
    search_fields = ('specialization', 'description')


admin.site.register(StudioDescription)
admin.site.register(Specialization)
admin.site.register(Status)
admin.site.register(Staff)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(AgeGroups)
admin.site.register(LessonsType)
admin.site.register(Costs)
admin.site.register(Lessons)
admin.site.register(Media)
admin.site.register(Reviews)
admin.site.register(ContactDetails)
admin.site.register(SocialNetworks)
admin.site.register(NewsFlow)
