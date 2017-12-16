from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Event
from .forms import EventForm

class EventCreater(View):
    template_name = 'alexmateva/create-event.html'

    def get(self, request):
        form = EventForm(request.GET)

        if form.is_valid():

            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = EventForm(request.POST)

        if form.is_valid():

            return HttpResponse('/success/')

        return render(request, self.template_name, locals())
