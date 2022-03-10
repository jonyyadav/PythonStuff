from multiprocessing.managers import BaseManager
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin

# Create your models here.


class Employee(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []




  