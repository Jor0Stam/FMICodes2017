from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', auth_views.login, name='login'),
    # path('registration', auth_views.registration, name='registration'),
]
