from . import models

from rest_framework import serializers

class ProductSerializer (serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'


class ProductVarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductVar
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'
