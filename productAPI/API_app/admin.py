from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Product)
admin.site.register(models.ProductVar)
admin.site.register(models.Category)
admin.site.register(models.Brand)
admin.site.register(models.Material)
admin.site.register(models.Season)
admin.site.register(models.Age)
admin.site.register(models.Size)
admin.site.register(models.Color)
admin.site.register(models.Gender)
