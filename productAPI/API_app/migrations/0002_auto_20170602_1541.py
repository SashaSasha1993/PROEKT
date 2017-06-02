# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allproducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, db_column='CATEGORY', max_length=300, null=True)),
                ('article', models.CharField(blank=True, db_column='ARTICLE', max_length=300, null=True)),
                ('color', models.CharField(blank=True, db_column='COLOR', max_length=300, null=True)),
                ('age', models.CharField(blank=True, db_column='AGE', max_length=300, null=True)),
                ('size', models.CharField(blank=True, db_column='SIZE', max_length=300, null=True)),
                ('wholeprice', models.CharField(blank=True, db_column='WHOLEPRICE', max_length=300, null=True)),
                ('retailprice', models.CharField(blank=True, db_column='RETAILPRICE', max_length=300, null=True)),
                ('inventory', models.IntegerField(blank=True, db_column='INVENTORY', null=True)),
                ('season', models.CharField(blank=True, db_column='SEASON', max_length=300, null=True)),
                ('gender', models.CharField(blank=True, db_column='GENDER', max_length=300, null=True)),
                ('brand', models.CharField(blank=True, db_column='BRAND', max_length=300, null=True)),
                ('temprature', models.CharField(blank=True, db_column='TEMPRATURE', max_length=300, null=True)),
                ('material1', models.CharField(blank=True, db_column='MATERIAL1', max_length=300, null=True)),
                ('material2', models.CharField(blank=True, db_column='MATERIAL2', max_length=300, null=True)),
                ('description', models.CharField(blank=True, db_column='DESCRIPTION', max_length=300, null=True)),
            ],
            options={
                'db_table': 'allproducts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ApiAppProductid',
            fields=[
                ('article', models.CharField(db_column='ARTICLE', max_length=200, primary_key=True, serialize=False)),
                ('category', models.CharField(db_column='CATEGORY', max_length=500)),
                ('season', models.CharField(db_column='SEASON', max_length=500)),
                ('material1', models.CharField(db_column='MATERIAL1', max_length=500)),
                ('material2', models.CharField(db_column='MATERIAL2', max_length=500)),
                ('description', models.CharField(db_column='DESCRIPTION', max_length=500)),
                ('brand', models.CharField(db_column='BRAND', max_length=500)),
            ],
            options={
                'db_table': 'api_app_productid',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ApiAppProductvar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(db_column='COLOR', max_length=500)),
                ('gender', models.CharField(db_column='GENDER', max_length=500)),
                ('wholeprice', models.CharField(db_column='WHOLEPRICE', max_length=500)),
                ('retailprice', models.CharField(db_column='RETAILPRICE', max_length=500)),
                ('age', models.CharField(db_column='AGE', max_length=500)),
                ('size', models.CharField(db_column='SIZE', max_length=500)),
            ],
            options={
                'db_table': 'api_app_productvar',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Nano1415',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, db_column='CATEGORY', max_length=300, null=True)),
                ('article', models.CharField(blank=True, db_column='ARTICLE', max_length=300, null=True)),
                ('color', models.CharField(blank=True, db_column='COLOR', max_length=300, null=True)),
                ('age', models.CharField(blank=True, db_column='AGE', max_length=300, null=True)),
                ('size', models.CharField(blank=True, db_column='SIZE', max_length=300, null=True)),
                ('wholeprice', models.CharField(blank=True, db_column='WHOLEPRICE', max_length=300, null=True)),
                ('retailprice', models.CharField(blank=True, db_column='RETAILPRICE', max_length=300, null=True)),
                ('inventory', models.IntegerField(blank=True, db_column='INVENTORY', null=True)),
                ('season', models.CharField(blank=True, db_column='SEASON', max_length=300, null=True)),
                ('gender', models.CharField(blank=True, db_column='GENDER', max_length=300, null=True)),
                ('brand', models.CharField(blank=True, db_column='BRAND', max_length=300, null=True)),
                ('temprature', models.CharField(blank=True, db_column='TEMPRATURE', max_length=300, null=True)),
                ('material1', models.CharField(blank=True, db_column='MATERIAL1', max_length=300, null=True)),
                ('material2', models.CharField(blank=True, db_column='MATERIAL2', max_length=300, null=True)),
                ('description', models.CharField(blank=True, db_column='DESCRIPTION', max_length=300, null=True)),
            ],
            options={
                'db_table': 'nano14_15',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Nano1617',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, db_column='CATEGORY', max_length=300, null=True)),
                ('article', models.CharField(blank=True, db_column='ARTICLE', max_length=300, null=True)),
                ('color', models.CharField(blank=True, db_column='COLOR', max_length=300, null=True)),
                ('age', models.CharField(blank=True, db_column='AGE', max_length=300, null=True)),
                ('size', models.CharField(blank=True, db_column='SIZE', max_length=300, null=True)),
                ('wholeprice', models.CharField(blank=True, db_column='WHOLEPRICE', max_length=300, null=True)),
                ('retailprice', models.CharField(blank=True, db_column='RETAILPRICE', max_length=300, null=True)),
                ('inventory', models.IntegerField(blank=True, db_column='INVENTORY', null=True)),
                ('season', models.CharField(blank=True, db_column='SEASON', max_length=300, null=True)),
                ('gender', models.CharField(blank=True, db_column='GENDER', max_length=300, null=True)),
                ('brand', models.CharField(blank=True, db_column='BRAND', max_length=300, null=True)),
                ('temprature', models.CharField(blank=True, db_column='TEMPRATURE', max_length=300, null=True)),
                ('material1', models.CharField(blank=True, db_column='MATERIAL1', max_length=300, null=True)),
                ('material2', models.CharField(blank=True, db_column='MATERIAL2', max_length=300, null=True)),
                ('description', models.CharField(blank=True, db_column='DESCRIPTION', max_length=300, null=True)),
            ],
            options={
                'db_table': 'nano16_17',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NanodemiSeason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, db_column='CATEGORY', max_length=300, null=True)),
                ('article', models.CharField(blank=True, db_column='ARTICLE', max_length=300, null=True)),
                ('color', models.CharField(blank=True, db_column='COLOR', max_length=300, null=True)),
                ('age', models.CharField(blank=True, db_column='AGE', max_length=300, null=True)),
                ('size', models.CharField(blank=True, db_column='SIZE', max_length=300, null=True)),
                ('wholeprice', models.CharField(blank=True, db_column='WHOLEPRICE', max_length=300, null=True)),
                ('retailprice', models.CharField(blank=True, db_column='RETAILPRICE', max_length=300, null=True)),
                ('inventory', models.IntegerField(blank=True, db_column='INVENTORY', null=True)),
                ('season', models.CharField(blank=True, db_column='SEASON', max_length=300, null=True)),
                ('gender', models.CharField(blank=True, db_column='GENDER', max_length=300, null=True)),
                ('brand', models.CharField(blank=True, db_column='BRAND', max_length=300, null=True)),
                ('temprature', models.CharField(blank=True, db_column='TEMPRATURE', max_length=300, null=True)),
                ('material1', models.CharField(blank=True, db_column='MATERIAL1', max_length=300, null=True)),
                ('material2', models.CharField(blank=True, db_column='MATERIAL2', max_length=300, null=True)),
                ('description', models.CharField(blank=True, db_column='DESCRIPTION', max_length=300, null=True)),
            ],
            options={
                'db_table': 'nanodemi_season',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PeluchedemiSeason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, db_column='CATEGORY', max_length=300, null=True)),
                ('article', models.CharField(blank=True, db_column='ARTICLE', max_length=300, null=True)),
                ('color', models.CharField(blank=True, db_column='COLOR', max_length=300, null=True)),
                ('age', models.CharField(blank=True, db_column='AGE', max_length=300, null=True)),
                ('size', models.CharField(blank=True, db_column='SIZE', max_length=300, null=True)),
                ('wholeprice', models.CharField(blank=True, db_column='WHOLEPRICE', max_length=300, null=True)),
                ('retailprice', models.CharField(blank=True, db_column='RETAILPRICE', max_length=300, null=True)),
                ('inventory', models.IntegerField(blank=True, db_column='INVENTORY', null=True)),
                ('season', models.CharField(blank=True, db_column='SEASON', max_length=300, null=True)),
                ('gender', models.CharField(blank=True, db_column='GENDER', max_length=300, null=True)),
                ('brand', models.CharField(blank=True, db_column='BRAND', max_length=300, null=True)),
                ('temprature', models.CharField(blank=True, db_column='TEMPRATURE', max_length=300, null=True)),
                ('material1', models.CharField(blank=True, db_column='MATERIAL1', max_length=300, null=True)),
                ('material2', models.CharField(blank=True, db_column='MATERIAL2', max_length=300, null=True)),
                ('description', models.CharField(blank=True, db_column='DESCRIPTION', max_length=300, null=True)),
            ],
            options={
                'db_table': 'peluchedemi_season',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Peluchesales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, db_column='CATEGORY', max_length=300, null=True)),
                ('article', models.CharField(blank=True, db_column='ARTICLE', max_length=300, null=True)),
                ('color', models.CharField(blank=True, db_column='COLOR', max_length=300, null=True)),
                ('age', models.CharField(blank=True, db_column='AGE', max_length=300, null=True)),
                ('size', models.CharField(blank=True, db_column='SIZE', max_length=300, null=True)),
                ('wholeprice', models.CharField(blank=True, db_column='WHOLEPRICE', max_length=300, null=True)),
                ('retailprice', models.CharField(blank=True, db_column='RETAILPRICE', max_length=300, null=True)),
                ('inventory', models.IntegerField(blank=True, db_column='INVENTORY', null=True)),
                ('season', models.CharField(blank=True, db_column='SEASON', max_length=300, null=True)),
                ('gender', models.CharField(blank=True, db_column='GENDER', max_length=300, null=True)),
                ('brand', models.CharField(blank=True, db_column='BRAND', max_length=300, null=True)),
                ('temprature', models.CharField(blank=True, db_column='TEMPRATURE', max_length=300, null=True)),
                ('material1', models.CharField(blank=True, db_column='MATERIAL1', max_length=300, null=True)),
                ('material2', models.CharField(blank=True, db_column='MATERIAL2', max_length=300, null=True)),
                ('description', models.CharField(blank=True, db_column='DESCRIPTION', max_length=300, null=True)),
            ],
            options={
                'db_table': 'peluchesales',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='productid',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='productvar',
            options={'managed': False},
        ),
    ]
