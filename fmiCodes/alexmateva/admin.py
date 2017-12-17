from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'rating', 'created_date', 'location')
    search_fields = ('name', 'rating')
