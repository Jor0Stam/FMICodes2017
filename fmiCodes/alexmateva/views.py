from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class EventCreater(View):

    def get(self, request):

        return HttpResponse('zdr bebce')
