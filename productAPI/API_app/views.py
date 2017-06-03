from django.shortcuts import render
from . import models
from rest_framework import generics
from . import serializer

# Create your views here.


class ListCreateProduct(generics.ListCreateAPIView):
    queryset=models.Product.objects.all()
    serializer_class =serializer.ProductSerializer

class ListCreateProductVar(generics.ListCreateAPIView):
    queryset=models.ProductVar.objects.all()
    serializer_class =serializer.ProductVarSerializer
    
class ListCreateCategory(generics.ListCreateAPIView):
    queryset=models.Category.objects.all()
    serializer_class =serializer.CategorySerializer
