from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
# Create your models here.


class ManageUsers(BaseUserManager):

    def create_user(self, email, user_name, profile_picture=None, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = User(
            email=self.normalize_email(email),
            profile_picture=profile_picture,
            user_name=user_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, user_name, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            user_name=user_name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    user_name = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=20)
    profile_picture = models.ImageField(upload_to=None)
    created_evets = []
    been_to_events = []
    rated_events = []
    liked_users = []

    def __init__(self, email, user_name, password, profile_picture):
        self.email = email
        self.user_name = user_name
        self.password = password
        self.profile_picture

    def create_event(self, name, description, time, location):
        event = Event(name, description, time, location)
        self.create_event.append(event)


class Event(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now())
    description = models.TextField()
    # creator = models.ForeignKey(User, editable = False)
    rating = models.IntegerField()
    location = models.CharField(max_length=255)
    #pics
    creator = models.ForeignKey(User, editable=False)
    rating = models.IntegerField()
    location = models.CharField()
    # pics
