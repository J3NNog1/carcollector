from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Car, Rental
from .forms import MaintenanceForm

# Add the following import




# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cars_index(request):
  cars = Car.objects.all()
  return render(request, 'cars/index.html', { 'cars': cars })

def cars_detail(request, car_id):
  car = Car.objects.get(id=car_id)
  rentals_car_doesnt_have = Rental.objects.exclude(id__in = car.rentals.all().values_list('id'))
  maintenance_form = MaintenanceForm()
  return render(request, 'cars/detail.html', {
    'car': car, 'maintenance_form': maintenance_form, 'rentals': rentals_car_doesnt_have})
  
def add_maintenance(request, car_id):
  form = MaintenanceForm(request.POST)
  if form.is_valid():
    new_maintenance = form.save(commit=False)
    new_maintenance.car_id = car_id
    new_maintenance.save()
  return redirect('cars_detail', car_id=car_id)

class CarCreate(CreateView):
  model = Car
  fields = ['owner', 'year', 'make', 'color', 'description']
  
class CarUpdate(UpdateView):
  model = Car
  fields = ['year', 'make', 'model', 'color', 'description']
  
class CarDelete(DeleteView):
  model = Car
  success_url = '/cars/'

class RentalCreate(CreateView):
  model = Rental
  fields = '__all__'
  
class RentalList(ListView):
  model = Rental

class RentalDetail(DetailView):
  model = Rental
  
class RentalUpdate(UpdateView):
  model = Rental
  fields = ['driver', 'start_mileage', 'end_mileage','days_rented', 'paid_by']

class RentalDelete(DeleteView):
  model = Rental
  success_url = '/rentals/'
  
def assoc_rental(request, car_id, rental_id):
  # Note that you can pass a toy's id instead of the whole object
  Car.objects.get(id=car_id).rentals.add(rental_id)
  return redirect('cars_detail', car_id=car_id)