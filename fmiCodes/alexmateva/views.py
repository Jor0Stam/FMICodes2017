from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .models import Event
from .forms import EventForm
from random import randint


class EventUpdate(View):
    template_name = 'alexmateva/edit_event.html'

    def get(self, request, event_id):
        event = Event.objects.filter(id=int(event_id)).first()
        # Add redirect for not found when there's no such event
        return render(request, 'alexmateva/edit_event.html', locals())

    def post(self, request, event_id):
        event = Event.objects.filter(id=int(event_id)).first()
        form = EventForm()

        if request.POST.name:
            event.name = request.POST.name

        if request.POST.name:
            event.description = request.POST

        if request.POST.name:
            event.location = request.POST

        return render(request, self.template_name, locals())



class EventDetail(View):
    template_name = 'alexmateva/event_info.html'

    def get(self, request, event_id):
        event = Event.objects.filter(id=int(event_id)).first()
        # Add redirect for not found when there's no such event
        return render(request, self.template_name, locals())

    def delete(self, request, event_id):
        event = Event.objects.filter(id=int(event_id)).first()
        # Add here delete method, щото не е очевидно, дъъъ!

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

        events = Event.objects.all()
        return render(request, self.template_name, locals())

class EventRandomizer(View):

    def get(self, request):
        count = Event.objects.count()
        random_index = randint(1, count)

        return redirect('event-info/{}'.format(random_index))
