from django.db import models


# Create your models here.

class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    gender = models.CharField(max_length=100)

class Account(models.Model):
    username = models.CharField(max_length=200)
    realname = models.CharField(max_length=150)
    accountNumber = models.IntegerField()
    balance = models.DecimalField(max_digits=150, decimal_places=2)
