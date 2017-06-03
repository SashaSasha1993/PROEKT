from django.db import models

class Category(models.Model):
    NAME = models.CharField(max_length=500, primary_key = True)

class Brand(models.Model):
    NAME = models.CharField(max_length=500, primary_key = True)
    
class Material(models.Model):
    NAME = models.CharField(max_length=500, primary_key = True)
    
class Season(models.Model):
    NAME = models.CharField(max_length=500, primary_key = True)
    
class Age(models.Model):
    NAME = models.CharField(max_length=500, primary_key = True)

class Size(models.Model):
    NAME = models.CharField(max_length=500, primary_key = True)

class Color(models.Model):
    NAME = models.CharField(max_length=500, primary_key = True)

class Gender(models.Model):
    NAME = models.CharField(max_length=500, primary_key = True)
    
class Product(models.Model):

    ARTICLE = models.CharField(max_length=200, primary_key = True)
    CATEGORY = models.ForeignKey(Category)
    SEASON = models.ManyToManyField(Season)
    MATERIALS = models.ManyToManyField(Material)
    DESCRIPTION = models.CharField(max_length=500)
    BRAND = models.ForeignKey(Brand)

class ProductVar(models.Model):
    ARTICLE = models.ForeignKey(Product)
    COLOR = models.ForeignKey(Color)
    GENDER = models.ForeignKey(Gender)
    WHOLEPRICE = models.DecimalField(max_digits=10, decimal_places=2)
    RETAILPRICE = models.DecimalField(max_digits=10, decimal_places=2)
    INVENTORY = models.IntegerField
    AGE = models.ForeignKey(Age)
    SIZE = models.ForeignKey(Size)
# Create your models here.
