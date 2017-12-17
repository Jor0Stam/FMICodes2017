from django.urls import include, path, re_path
from .views import QuestionView

urlpatterns = [
    path('survey/', QuestionView.as_view(), name='survey'),
]
