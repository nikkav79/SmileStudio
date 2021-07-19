from django.contrib import admin
from .models import *


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('specialization', 'contract_type', 'created_at', 'is_active')
    list_display_links = ('specialization',)
    search_fields = ('specialization', 'description')


admin.site.register(Vacancy, VacancyAdmin)
