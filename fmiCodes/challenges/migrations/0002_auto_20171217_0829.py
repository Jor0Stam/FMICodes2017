# Generated by Django 2.0 on 2017-12-17 08:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alexmateva', '0002_auto_20171217_0148'),
        ('challenges', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='competitors',
            field=models.ManyToManyField(related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='challenge',
            name='events',
        ),
        migrations.AddField(
            model_name='challenge',
            name='events',
            field=models.ManyToManyField(related_name='event', to='alexmateva.Event'),
        ),
    ]
