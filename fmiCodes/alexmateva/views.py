from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .models import Event
from .forms import EventForm


class EventDetail(View):
    template_name = 'alexmateva/event_info.html'

    def get(self, request, event_id):
        event = Event.objects.filter(id=int(event_id))
        # Add redirect for not found when there's no such event
        return render(request, self.template_name, locals())

    def post(self, request, event_id):
        pass

    def delete(self, request, event_id):
        pass
        # Add here delete method, щото не е очевидно, дъъъ!

class EventCreater(View):
    template_name = 'alexmateva/base.html'

    def get(self, request):
        form = EventForm(request.GET)

        if form.is_valid():

            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = EventForm(request.POST)

        if form.is_valid():
            Event.objects.create(name=request.POST.get('name'),
                                 description=request.POST.get('description'),
                                 location=request.POST.get('location'),
                                 rating=0)
            return redirect('list_events')

        return render(request, self.template_name, locals())


class EventLister(ListView):

    model = Event
    template_name='alexmateva/event_list.html'

    def get(self, request):
        return render(request, self.template_name)

