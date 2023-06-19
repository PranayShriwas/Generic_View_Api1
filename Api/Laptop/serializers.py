from .models import Laptop
from rest_framework import serializers
from rest_framework import generics


class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = '__all__'
