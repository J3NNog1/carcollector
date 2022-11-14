from django.db import models
from django.urls import reverse
# Create your models here.

SERVICE_TYPE = (
  ('M', "Maintenance"),
  ('MA', "Major Repair"),
  ('C', "Collision"),
  ('P', "Parts"),
  ('T', "Tires"),
)

class Car(models.Model):
  owner = models.CharField(max_length=250)
  year = models.IntegerField()
  make = models.CharField(max_length=100)
  model = models.CharField(max_length=250)
  color = models.CharField(max_length=250)
  description = models.TextField(max_length=250)
  
  def __str__(self):
    return self.owner
  
  def get_absolute_url(self):
    return reverse('cars_detail', kwargs={'car_id': self.id})
  
  
class Maintenance(models.Model):
  date = models.DateField('Maintenance Date')
  vin = models.CharField(max_length=6)
  mileage = models.IntegerField()
  service_type = models.CharField(
    max_length=15,
    choices=SERVICE_TYPE,
    default=SERVICE_TYPE[0][0],
    )  
  description = models.TextField(max_length=10000)
  invoice_total = models.IntegerField()

  car = models.ForeignKey(Car, on_delete=models.CASCADE)
  
  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_service_type_display()} on {self.date} for vehicle ending in {self.vin}"