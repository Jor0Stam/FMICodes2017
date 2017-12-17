from django.urls import include, path, re_path
from .views import EventCreater, EventLister, EventDetail, EventUpdate

urlpatterns = [
    path('create-event', EventCreater.as_view(), name='create_event'),
    path('list-events', EventLister.as_view(), name='list_events'),
    re_path('event/(?P<event_id>[0-9])', EventDetail.as_view(), name='event_details'),
    re_path('edit_event/(?P<event_id>[0-9])', EventUpdate.as_view(), name='update_event'),
]
