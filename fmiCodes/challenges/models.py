from django.db import models
from alexmateva.models import Event
from django.contrib.auth.models import User


# Create your models here.

class Challenge(models.Model):
    events = models.ManyToManyField(Event, related_name='event')
    name = models.CharField(max_length=255)
    description = models.TextField()
    competitors = models.ManyToManyField(User, related_name='user')

