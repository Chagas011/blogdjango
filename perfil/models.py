
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Perfils(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(default='', blank=True)