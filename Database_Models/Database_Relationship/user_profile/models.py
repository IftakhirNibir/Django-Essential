from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Address(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)

    def __str__(self):
        return self.street_address
    


