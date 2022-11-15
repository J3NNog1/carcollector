from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),  
  path('about/', views.about, name='about'),  
  path('cars/', views.cars_index, name='cars_index'),
  path('cars/<int:car_id>/', views.cars_detail, name='cars_detail'),
  path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
  path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
  path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
  path('cars/<int:car_id>/add_maintenance/', views.add_maintenance, name='add_maintenance'),
  path('rentals/create/', views.RentalCreate.as_view(), name='rentals_create'),
  path('rentals/<int:pk>/', views.RentalDetail.as_view(), name='rentals_detail'),
  path('rentals/', views.RentalList.as_view(), name='rentals_index'),
  path('rentals/<int:pk>/update/', views.RentalUpdate.as_view(), name='rentals_update'),
  path('rentals/<int:pk>/delete/', views.RentalDelete.as_view(), name='rentals_delete'),
  path('cars/<int:car_id>/assoc_rental/<int:rental_id>/', views.assoc_rental, name='assoc_rental'),
  
]