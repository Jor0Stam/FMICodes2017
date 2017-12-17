from django.contrib import admin
from .models import Challenge


@admin.register(Challenge)
class EventAdmin(admin.ModelAdmin):
	fields = ['name','description', 'events']
	list_display = ('name', 'get_events', 'description')
	search_fields = ('name',)

	def get_events(self, obj):
		return "\n".join([e.name for e in obj.events.all()])


