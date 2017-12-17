from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.forms import formset_factory
from .forms import QuestionForm
# Create your views here.


class QuestionView(View):
    template_name = 'survey/survey_form.html'
    QuestionFormSet = formset_factory(QuestionForm, extra=5)
    QUESTIONS = [
            'Do you like shkembence?',
            'Swiggity, Swoogity, Turn off the lights',
            'Have you seem 25sm?',
            'Women love it!',
            'Pray to the armanian Pope!',
            ]

    def get(self, request):
        forms = self.QuestionFormSet()
        questions = self.QUESTIONS
        pairs = zip(questions, forms)
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):

        # Save the Questions and info here ???

        return redirect(reverse_lazy('list_events'))
