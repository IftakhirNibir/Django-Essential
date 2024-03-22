from django.contrib import admin
from .models import Client, Todolist, Comment 
# Register your models here.

admin.site.register(Client)
admin.site.register(Todolist)
admin.site.register(Comment)