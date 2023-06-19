from django.shortcuts import render
from .serializers import LaptopSerializer
from rest_framework import generics
from .models import Laptop
# Create your views here.
class LaptopApi(generics.ListAPIView):
    queryset=Laptop.objects.all()
    serializer_class=LaptopSerializer

class LaptopCreateApi(generics.CreateAPIView):
    queryset=Laptop.objects.all()
    serializer_class=LaptopSerializer

class LaptopUpdateApi(generics.UpdateAPIView):
    queryset=Laptop.objects.all()
    serializer_class=LaptopSerializer

class LaptopDeleteApi(generics.DestroyAPIView):
    queryset=Laptop.objects.all()
    serializer_class=LaptopSerializer

class LaptopReteriveApi(generics.RetrieveAPIView):
    queryset=Laptop.objects.all()
    serializer_class=LaptopSerializer
