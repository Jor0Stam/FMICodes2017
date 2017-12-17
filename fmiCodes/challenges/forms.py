import datetime
from django.db import models
from .models import Challenge
# from django.extras import SelectDateWidget
from django import forms
from django.forms import ModelForm, Form, Textarea,DateField
from django.contrib.admin.widgets import AdminDateWidget

class ChallengeForm(ModelForm):

	start_date = forms.DateField(widget=AdminDateWidget)
	#end_date

	class Meta:
		model = Challenge
		# fields = ['name','description','events', 'date_field']
		exclude = ['events']