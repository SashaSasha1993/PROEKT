from django.db import models

class ProductID(models.Model):

    ARTICLE = models.CharField(max_length=200, primary_key = True)
    CATEGORY = models.CharField(max_length=500)
    SEASON = models.CharField(max_length=500)
    MATERIAL1 = models.CharField(max_length=500)
    MATERIAL2 = models.CharField(max_length=500)
    DESCRIPTION = models.CharField(max_length=500)
    BRAND = models.CharField(max_length=500)

class ProductVar(models.Model):
    ARTICLE = models.ForeignKey(ProductID)
    COLOR = models.CharField(max_length=500)
    GENDER = models.CharField(max_length=500)
    WHOLEPRICE = models.CharField(max_length=500)
    RETAILPRICE = models.CharField(max_length=500)
    INVENTORY = models.IntegerField
    AGE = models.CharField(max_length=500)
    SIZE = models.CharField(max_length=500)
# Create your models here.
