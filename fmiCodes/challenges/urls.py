from django.urls import include,path
from .views import ChallengeLister

urlpatterns = [
    path('challenges_list',ChallengeLister.as_view(),name='challenges_list')
        ]
