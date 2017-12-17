from django.urls import include,path
from .views import ChallengeLister,ChallengeCreator

urlpatterns = [
    path('list-challenges',ChallengeLister.as_view(),name='list-challenges'),
    path('create-challenge', ChallengeCreator.as_view(), name='create-challenge')
        ]
