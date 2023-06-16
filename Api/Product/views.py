from django.shortcuts import render
from .serializers import ProductSerializer
from .models import Product
from rest_framework import generics
# Create your views here.


class ProductGetApi(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateApi(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateApi(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDeleteApi(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductReteriveApi(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
