
from django.urls import path

from api import views

urlpatterns = [
    path('',views.get_doctors,name="get-doctors"), #Returns all doctors by ranking
    path('doctors/<str:specialisation>/', views.get_doctor_location, name='get-doctors-location'), #Returns all doctors by ranking with specialisation
    path('doctors/<str:location>/<str:specialisation>/',views.get_doctor_location_specialisation,name='get-doctor-narrow'), #Returns all doctors by ranking with specialisation and city
    path('doctor-create/',views.create_doctor,name='create-doctor'), #Creates a new doctor
]
