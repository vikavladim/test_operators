from django.contrib import admin

from .models import Operator


class OperatorAdmin(admin.ModelAdmin):
    list_display = ['ne', 'address', 'latitude', 'longitude', 'gsm', 'umts', 'lte', 'status']
    list_filter = ['gsm', 'umts', 'lte', 'status']
    ordering = ['ne']
    search_fields = ['ne', 'address', 'status']

admin.site.register(Operator, OperatorAdmin)
