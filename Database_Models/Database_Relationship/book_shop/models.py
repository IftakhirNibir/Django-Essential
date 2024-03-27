from django.db import models

# Create your models here.

class Bookstore(models.Model):
    name = models.CharField(max_length=255)

class Book(models.Model):
    bookstore = models.ForeignKey(Bookstore, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)



    