from django.db import models
from django import forms
# Create your models here.

#Questions 


class InitialForm(forms.Form):
    answer = forms.ChoiceField(choices=('no', 'meh', 'yes'))