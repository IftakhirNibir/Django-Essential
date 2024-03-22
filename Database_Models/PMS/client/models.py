from django.contrib.auth.models import User
from django.db import models
from team.models import Team
# Create your models here.

class InfoTable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Comment(InfoTable):
    content = models.TextField()
    created_by = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)


class Client(models.Model):
    ACTIVE = 'active'
    ARCHIVED = 'archived'
    CHOICES = (
        (ACTIVE,'Active'), #first value is store in DB, second value we see in the DB
        (ARCHIVED,'Archived')
    )

    team = models.ForeignKey(Team, related_name='clients', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=CHOICES, default=ACTIVE)
    comments = models.ManyToManyField(Comment, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-name'] #now showing last entry in the first
        verbose_name = 'Clientttt'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return f'Client: {self.name}'

    def number_of_comments(self):
        return self.comments.count()

    def save(self, *args, **kwargs):
        if 'hello' in self.name:
            self.name = self.name.replace('hello','hi')
        
        super(Client,self).save(*args,**kwargs)
    

class Todolist(models.Model):
    client = models.ForeignKey(Client, related_name="todolists", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    comments = models.ManyToManyField(Comment, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name="todolists", on_delete=models.CASCADE)








   

