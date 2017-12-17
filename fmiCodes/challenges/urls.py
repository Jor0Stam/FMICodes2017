from django.urls import include,path
from .views import ChallengeLister,ChallengeCreator

urlpatterns = [
    path('challenges_list',ChallengeLister.as_view(),name='challenges_list'),
    path('create_challenge', ChallengeCreator.as_view(), name='create_challenge')
        ]
