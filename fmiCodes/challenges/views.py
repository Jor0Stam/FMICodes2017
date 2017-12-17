from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Challenge

# Create your views here.

class ChallengeLister(ListView):

    model = Challenge
    template_name = 'challenges/challenges_list.html'

    def get(self, request):
        return render(request,self.template_name)



