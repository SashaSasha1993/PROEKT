# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-03 16:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API_app', '0002_auto_20170603_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='PARENTCATEGORY',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='API_app.Category'),
        ),
    ]