# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-03 17:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API_app', '0003_category_parentcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvar',
            name='INVENTORY',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='BRAND',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='API_app.Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='CATEGORY',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='API_app.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='DESCRIPTION',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='MATERIALS',
            field=models.ManyToManyField(blank=True, null=True, to='API_app.Material'),
        ),
        migrations.AlterField(
            model_name='product',
            name='SEASON',
            field=models.ManyToManyField(blank=True, null=True, to='API_app.Season'),
        ),
        migrations.AlterField(
            model_name='productvar',
            name='AGE',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='API_app.Age'),
        ),
        migrations.AlterField(
            model_name='productvar',
            name='COLOR',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='API_app.Color'),
        ),
        migrations.AlterField(
            model_name='productvar',
            name='GENDER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='API_app.Gender'),
        ),
        migrations.AlterField(
            model_name='productvar',
            name='RETAILPRICE',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='productvar',
            name='SIZE',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='API_app.Size'),
        ),
        migrations.AlterField(
            model_name='productvar',
            name='WHOLEPRICE',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
