from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Doctor
from api.serializers import DoctorSerializer


@api_view(['GET'])
def get_doctors(request):
    doctors = Doctor.objects.all().order_by('-average_rating')
    serializer = DoctorSerializer(doctors, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
def get_doctor_location(request, specialisation):
    doctors = Doctor.objects.filter(specialisation=specialisation).order_by('-average_rating')
    serializer = DoctorSerializer(doctors, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
def get_doctor_location_specialisation(request, location, specialisation):
    doctors = Doctor.objects.filter(location=location, specialisation=specialisation).order_by('-average_rating')
    serializer = DoctorSerializer(doctors, many=True)
    return Response(serializer.data, status=200)


@api_view(['POST'])
def create_doctor(request):
    serializer = DoctorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
