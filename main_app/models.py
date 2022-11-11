from django.db import models

# Create your models here.

class Car(models.Model):
  owner = models.CharField(max_length=250)
  year = models.IntegerField()
  make = models.CharField(max_length=100)
  model = models.TextField(max_length=250)
  color = models.CharField(max_length=250)
  
  
  def __str__(self):
    return self.owner