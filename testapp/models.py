from django.urls import reverse
from django.db import models

# Create your models here.
class Restro(models.Model):
    Name=models.CharField(max_length=100)
    Taste=models.CharField(max_length=100)
    Price=models.IntegerField()

