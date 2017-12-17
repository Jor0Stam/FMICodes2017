# Generated by Django 2.0 on 2017-12-17 08:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0003_challenge_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='name',
            field=models.TextField(),
        ),
    ]