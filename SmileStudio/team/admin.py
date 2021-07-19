from django.contrib import admin
from .models import *


class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_display_links = ('name',)
    search_fields = ('name', 'description')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'contract')
    list_display_links = ('last_name',)
    search_fields = ('last_name', 'first_name', 'specialization__name')


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('specialization', 'contract_type', 'created_at', 'is_active')
    list_display_links = ('specialization',)
    search_fields = ('specialization', 'description')


admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(Position)
admin.site.register(ContractType)
admin.site.register(Team, TeamAdmin)
admin.site.register(Vacancy, VacancyAdmin)
