from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.

SERVICE_TYPE = (
  ('M', "Maintenance"),
  ('MA', "Major Repair"),
  ('C', "Collision"),
  ('P', "Parts"),
  ('T', "Tires"),
)

class Rental(models.Model):
  driver = models.CharField(max_length=250)
  start_mileage = models.CharField(max_length=1000000)
  end_mileage = models.CharField(max_length=1000000)
  days_rented = models.CharField(max_length=10000)
  paid_by= models.CharField(max_length=250)

  def __str__(self):
    return self.driver

  def get_absolute_url(self):
    return reverse('rentals_detail', kwargs={'pk': self.id})
  
  
class Car(models.Model):
  owner = models.CharField(max_length=250)
  year = models.IntegerField()
  make = models.CharField(max_length=100)
  model = models.CharField(max_length=250)
  color = models.CharField(max_length=250)
  description = models.TextField(max_length=250)
  rentals = models.ManyToManyField(Rental)
  
  def __str__(self):
    return self.owner
  
  def get_absolute_url(self):
    return reverse('cars_detail', kwargs={'car_id': self.id})
  
  def serviced_for_today(self):
    return self.maintenance_set.filter(date=date.today()).count() >= len(SERVICE_TYPE)
    
class Maintenance(models.Model):
  date = models.DateField('Maintenance Date')
  vin = models.CharField(max_length=6)
  mileage = models.CharField(max_length=1000000)
  service_type = models.CharField(
    max_length=15,
    choices=SERVICE_TYPE,
    default=SERVICE_TYPE[0][0],
    )  
  description = models.TextField(max_length=10000)
  invoice_total = models.CharField(max_length=10000000)

  car = models.ForeignKey(Car, on_delete=models.CASCADE)
  
  def __str__(self):
    return f"{self.get_service_type_display()} on {self.date} for vehicle ending in {self.vin}"

class Meta:
    ordering = ['-date']