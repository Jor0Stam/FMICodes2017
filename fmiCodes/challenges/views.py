from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Challenge
from .forms import ChallengeForm

# Create your views here.


class ChallengeDetail(DetailView):
	model = Challenge
	def get_context_data(self,*args):
		pass


class ChallengeCreator(View):
	template_name = 'challenges/create_challenge.html'

	def get(self, request):
		form = ChallengeForm(request.GET)

		if form.is_valid():
			return HttpResponseRedirect('/success/')

		return render(request,self.template_name,{'form':form})


	def post(self,request,*args,**kwargs):
		form = ChallengeForm(request.POST)

		if form.is_valid():
			Challenge.objects.create(name=request.POST.get('name'),
									 description=request.POST.get('description'),
									 events = request.POST.get('events'))

			return redirect('challenges_list')


		return render(request,self.template_name,locals())


class ChallengeLister(ListView):

    model = Challenge
    template_name = 'challenges/challenges_list.html'

    def get(self, request):
		hallenges = Challenge.objects.all()

    	return render(request,self.template_name,locals())
