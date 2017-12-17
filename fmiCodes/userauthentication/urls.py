from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_views
# from .views import ProfileInfo

urlpatterns = [
    path('login', auth_views.login, name='login'),
    # path('profile', ProfileInfo.login, name='profil'),
    # path('registration', auth_views.registration, name='registration'),
]
