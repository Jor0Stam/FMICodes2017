from datetime import timedelta
from django.db import models
from django.utils import timezone
from alexmateva.models import Event
from django.contrib.auth.models import User


# Create your models here.

class Challenge(models.Model):
    events = models.ManyToManyField(Event, related_name='event')
    name = models.CharField(max_length=255)
    description = models.TextField()
    competitors = models.ManyToManyField(User, related_name='user')
    name = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    # default_end_date = timedelta(days=10)
    # end_date = models.DateTimeField(default=start_date + default_end_date)
