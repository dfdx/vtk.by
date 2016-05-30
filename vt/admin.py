from django.contrib import admin
from .models import ScheduledTraining, Event

admin.site.register(ScheduledTraining)
admin.site.register(Event)
