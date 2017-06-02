from . import models

from rest_framework import serializers

class ProductIDSerializer (serializers.ModelSerializer):
    class Meta:
        model = models.ProductID
        fields = '__all__'


class ProductVarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductVar
        fields = '__all__'


