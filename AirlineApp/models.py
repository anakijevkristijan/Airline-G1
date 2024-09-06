from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Pilot(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    year_of_birth=models.DateField()
    hours_of_fly=models.IntegerField()
    pilot_act=models.CharField(max_length=50)

class Ballon(models.Model):
    type=models.CharField(max_length=50)
    manufacturer=models.CharField(max_length=50)
    max_passages=models.IntegerField()

class Airline(models.Model):
    name=models.CharField(max_length=50)
    year_of_start=models.DateField()
    isFlyEurope=models.BooleanField()
    pilot=models.ForeignKey(Pilot, on_delete=models.CASCADE)

class Fly(models.Model):
    id = models.AutoField(primary_key=True)
    airport_departue=models.ForeignKey(Airline, on_delete=models.CASCADE)
    airport_arrival=models.ForeignKey(Airline, on_delete=models.CASCADE)
    creator=models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/')
    ballon=models.ForeignKey(Ballon, on_delete=models.CASCADE)
    pilot=models.ForeignKey(Pilot, on_delete=models.CASCADE)