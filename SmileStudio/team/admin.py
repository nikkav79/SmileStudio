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


admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(Position)
admin.site.register(ContractType)
admin.site.register(Team, TeamAdmin)
