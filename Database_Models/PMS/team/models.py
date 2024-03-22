from django.contrib.auth.models import User 
from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User)


