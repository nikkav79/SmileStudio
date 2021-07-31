from django.contrib import admin
from .models import *


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',),
        'name': ('specialization',)
    }
    list_display = (
        'name',
        'contract_type',
        'created_at',
        'is_active',
    )
    search_fields = (
        'name',
    )


admin.site.register(Responsibilities)
admin.site.register(Requirements)
admin.site.register(Conditions)
