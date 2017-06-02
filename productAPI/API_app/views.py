from django.shortcuts import render
from . import models
from rest_framework import generics
from . import serializer

# Create your views here.


class ListCreateProductID(generics.ListCreateAPIView):
    queryset=models.ProductID.objects.all()
    serializer_class =serializer.ProductIDSerializer

class ListCreateProductVar(generics.ListCreateAPIView):
    queryset=models.ProductVar.objects.all()
    serializer_class =serializer.ProductVarSerializer
