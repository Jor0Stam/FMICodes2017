from django.db import models
# from django.auth.contrib import User
# Create your models here.

#Questions

YN_CHOICES = (
        ('Y', 'Yes'),
        ('M', 'Meh'),
        ('N', 'No')
    )

M_CHOICES = (
        ('M', 'Male'),
        ('F', 'Not Male')
    )

class Question(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=3, choices=YN_CHOICES)


class MultipleAnswerQuestion(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=20, choices=M_CHOICES)


# class AnswerCollector(models.Model):
    # user = models.ForeignKeyField(User)
    # answers = models.ListField
