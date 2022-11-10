from django.shortcuts import render

# Add the following import
from django.http import HttpResponse


# Add the Cat class & list and view function below the imports
class Car:  # Note that parens are optional if not inheriting from another class
  def __init__(self, year, make, model, color):
    self.year = year
    self.make = make
    self.model = model
    self.color = color

cars = [
  Car(2020, 'Honda', 'Civic', 'Black'),
  Car(1987, 'Ford', 'Mustang', 'Red'),
  Car(2023, 'Porshe', '911', 'Black'),
  Car(2023, 'Ferrari', 'Purosangue', 'Grey')
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

def cars_index(request):
  return render(request, 'cars/index.html', { 'cars': cars })

