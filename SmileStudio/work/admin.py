from django.contrib import admin
from .models import *


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('specialization', )}
    list_display = (
        'specialization',
        'contract_type',
        'created_at',
        'is_active',
    )
    list_display_links = ('specialization',)
    search_fields = (
        'specialization',
        'description'
    )


admin.site.register(Responsibilities)
admin.site.register(Requirements)
admin.site.register(Conditions)