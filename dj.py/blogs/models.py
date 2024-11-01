from django.db import models
from .views import *
# Create your models here.
class sandeep(models.Model):
    Name=models.CharField(max_length=200 )
    Email=models.EmailField(max_length=100)
    Number=models.IntegerField(default=0)
   
