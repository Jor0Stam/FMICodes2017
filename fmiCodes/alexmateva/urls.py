from django.urls import include, path
from .views import EventCreater

urlpatterns = [
    path('create-event', EventCreater.as_view()),
]
