from datetime import timedelta
from django.db import models
from django.utils import timezone
from alexmateva.models import Event

# Create your models here.

class Challenge(models.Model):
    events = models.ForeignKey(Event,on_delete=models.CASCADE)
    description = models.TextField()
    name = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    # default_end_date = timedelta(days=10)
    # end_date = models.DateTimeField(default=start_date + default_end_date)

