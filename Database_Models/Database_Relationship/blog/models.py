from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    tags = models.ManyToManyField('Tag')

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

