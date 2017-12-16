from django.db import models
from django.utils import timezone
from 
# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now())
    description = models.TextField()
    creator = models.ForeignKey(User, editable = False)
    rating = models.IntegerField()
    location = models.CharField()
    #pics