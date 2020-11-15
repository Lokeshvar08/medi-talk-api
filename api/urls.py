
from django.urls import path

from api import views

urlpatterns = [
    path('doctors/<str:specialisation>/', views.get_doctor_location, name='get-doctors-location'),
    path('doctors/<str:location>/<str:specialisation>/',views.get_doctor_location_specialisation,name='get-doctor-narrow'),
]
