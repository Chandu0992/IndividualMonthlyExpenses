from django.db import models
from datetime import date
# Create your models here.
class Register(models.Model):
    #entry_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    mobile = models.IntegerField(default=10,primary_key=True)
    email = models.CharField(max_length=250,unique=True)
    gen = models.CharField(max_length=6)
    password = models.CharField(max_length=20)

class Expenses(models.Model):
    mobile = models.CharField(default=10,max_length=10)
    dt = models.DateField()
    type_exp = models.CharField(max_length=30)
    desc = models.CharField(max_length=250)
    amount = models.IntegerField(default=5)
