from django.urls import include, path
from .views import EventCreater, EventLister

urlpatterns = [
    path('create-event', EventCreater.as_view()),
    path('list-events', EventLister.as_view())
]
