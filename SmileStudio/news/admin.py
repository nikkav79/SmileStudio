from django.contrib import admin
from .models import *


# class NewsFlowAdmin(admin.ModelAdmin):
#     list_display = ('modified', 'title', 'author', 'created', 'digest')
#     list_display_links = ('title',)
#     search_fields = ('title', 'digest', 'modified')


admin.site.register(NewsFlow)
admin.site.register(NewsTag)
