from django.db import models
from alexmateva.models import Event

# Create your models here.

class Challenge(models.Model):
    events = models.ForeignKey(Event,on_delete=models.CASCADE)
    description = models.TextField()

