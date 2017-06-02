# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Allproducts(models.Model):
    category = models.CharField(db_column='CATEGORY', max_length=300, blank=True, null=True)  # Field name made lowercase.
    article = models.CharField(db_column='ARTICLE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    color = models.CharField(db_column='COLOR', max_length=300, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='AGE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(db_column='SIZE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    wholeprice = models.CharField(db_column='WHOLEPRICE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    retailprice = models.CharField(db_column='RETAILPRICE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    inventory = models.IntegerField(db_column='INVENTORY', blank=True, null=True)  # Field name made lowercase.
    season = models.CharField(db_column='SEASON', max_length=300, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=300, blank=True, null=True)  # Field name made lowercase.
    brand = models.CharField(db_column='BRAND', max_length=300, blank=True, null=True)  # Field name made lowercase.
    temprature = models.CharField(db_column='TEMPRATURE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    material1 = models.CharField(db_column='MATERIAL1', max_length=300, blank=True, null=True)  # Field name made lowercase.
    material2 = models.CharField(db_column='MATERIAL2', max_length=300, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'allproducts'


class ApiAppProductid(models.Model):
    article = models.CharField(db_column='ARTICLE', primary_key=True, max_length=200)  # Field name made lowercase.
    category = models.CharField(db_column='CATEGORY', max_length=500)  # Field name made lowercase.
    season = models.CharField(db_column='SEASON', max_length=500)  # Field name made lowercase.
    material1 = models.CharField(db_column='MATERIAL1', max_length=500)  # Field name made lowercase.
    material2 = models.CharField(db_column='MATERIAL2', max_length=500)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=500)  # Field name made lowercase.
    brand = models.CharField(db_column='BRAND', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'api_app_productid'


class ApiAppProductvar(models.Model):
    color = models.CharField(db_column='COLOR', max_length=500)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=500)  # Field name made lowercase.
    wholeprice = models.CharField(db_column='WHOLEPRICE', max_length=500)  # Field name made lowercase.
    retailprice = models.CharField(db_column='RETAILPRICE', max_length=500)  # Field name made lowercase.
    age = models.CharField(db_column='AGE', max_length=500)  # Field name made lowercase.
    size = models.CharField(db_column='SIZE', max_length=500)  # Field name made lowercase.
    article = models.ForeignKey(ApiAppProductid, models.DO_NOTHING, db_column='ARTICLE_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'api_app_productvar'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Nano1415(models.Model):
    category = models.CharField(db_column='CATEGORY', max_length=300, blank=True, null=True)  # Field name made lowercase.
    article = models.CharField(db_column='ARTICLE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    color = models.CharField(db_column='COLOR', max_length=300, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='AGE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(db_column='SIZE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    wholeprice = models.CharField(db_column='WHOLEPRICE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    retailprice = models.CharField(db_column='RETAILPRICE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    inventory = models.IntegerField(db_column='INVENTORY', blank=True, null=True)  # Field name made lowercase.
    season = models.CharField(db_column='SEASON', max_length=300, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=300, blank=True, null=True)  # Field name made lowercase.
    brand = models.CharField(db_column='BRAND', max_length=300, blank=True, null=True)  # Field name made lowercase.
    temprature = models.CharField(db_column='TEMPRATURE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    material1 = models.CharField(db_column='MATERIAL1', max_length=300, blank=True, null=True)  # Field name made lowercase.
    material2 = models.CharField(db_column='MATERIAL2', max_length=300, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nano14_15'


class Nano1617(models.Model):
    category = models.CharField(db_column='CATEGORY', max_length=300, blank=True, null=True)  # Field name made lowercase.
    article = models.CharField(db_column='ARTICLE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    color = models.CharField(db_column='COLOR', max_length=300, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='AGE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(db_column='SIZE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    wholeprice = models.CharField(db_column='WHOLEPRICE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    retailprice = models.CharField(db_column='RETAILPRICE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    inventory = models.IntegerField(db_column='INVENTORY', blank=True, null=True)  # Field name made lowercase.
    season = models.CharField(db_column='SEASON', max_length=300, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=300, blank=True, null=True)  # Field name made lowercase.
    brand = models.CharField(db_column='BRAND', max_length=300, blank=True, null=True)  # Field name made lowercase.
    temprature = models.CharField(db_column='TEMPRATURE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    material1 = models.CharField(db_column='MATERIAL1', max_length=300, blank=True, null=True)  # Field name made lowercase.
    material2 = models.CharField(db_column='MATERIAL2', max_length=300, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nano16_17'


class NanodemiSeason(models.Model):
    category = models.CharField(db_column='CATEGORY', max_length=300, blank=True, null=True)  # Field name made lowercase.
    article = models.CharField(db_column='ARTICLE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    color = models.CharField(db_column='COLOR', max_length=300, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='AGE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(db_column='SIZE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    wholeprice = models.CharField(db_column='WHOLEPRICE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    retailprice = models.CharField(db_column='RETAILPRICE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    inventory = models.IntegerField(db_column='INVENTORY', blank=True, null=True)  # Field name made lowercase.
    season = models.CharField(db_column='SEASON', max_length=300, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=300, blank=True, null=True)  # Field name made lowercase.
    brand = models.CharField(db_column='BRAND', max_length=300, blank=True, null=True)  # Field name made lowercase.
    temprature = models.CharField(db_column='TEMPRATURE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    material1 = models.CharField(db_column='MATERIAL1', max_length=300, blank=True, null=True)  # Field name made lowercase.
    material2 = models.CharField(db_column='MATERIAL2', max_length=300, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nanodemi_season'


class PeluchedemiSeason(models.Model):
    category = models.CharField(db_column='CATEGORY', max_length=300, blank=True, null=True)  # Field name made lowercase.
    article = models.CharField(db_column='ARTICLE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    color = models.CharField(db_column='COLOR', max_length=300, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='AGE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(db_column='SIZE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    wholeprice = models.CharField(db_column='WHOLEPRICE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    retailprice = models.CharField(db_column='RETAILPRICE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    inventory = models.IntegerField(db_column='INVENTORY', blank=True, null=True)  # Field name made lowercase.
    season = models.CharField(db_column='SEASON', max_length=300, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=300, blank=True, null=True)  # Field name made lowercase.
    brand = models.CharField(db_column='BRAND', max_length=300, blank=True, null=True)  # Field name made lowercase.
    temprature = models.CharField(db_column='TEMPRATURE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    material1 = models.CharField(db_column='MATERIAL1', max_length=300, blank=True, null=True)  # Field name made lowercase.
    material2 = models.CharField(db_column='MATERIAL2', max_length=300, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'peluchedemi_season'


class Peluchesales(models.Model):
    category = models.CharField(db_column='CATEGORY', max_length=300, blank=True, null=True)  # Field name made lowercase.
    article = models.CharField(db_column='ARTICLE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    color = models.CharField(db_column='COLOR', max_length=300, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='AGE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(db_column='SIZE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    wholeprice = models.CharField(db_column='WHOLEPRICE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    retailprice = models.CharField(db_column='RETAILPRICE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    inventory = models.IntegerField(db_column='INVENTORY', blank=True, null=True)  # Field name made lowercase.
    season = models.CharField(db_column='SEASON', max_length=300, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=300, blank=True, null=True)  # Field name made lowercase.
    brand = models.CharField(db_column='BRAND', max_length=300, blank=True, null=True)  # Field name made lowercase.
    temprature = models.CharField(db_column='TEMPRATURE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    material1 = models.CharField(db_column='MATERIAL1', max_length=300, blank=True, null=True)  # Field name made lowercase.
    material2 = models.CharField(db_column='MATERIAL2', max_length=300, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'peluchesales'


class ProductID(models.Model):
    article = models.CharField(db_column='ARTICLE', max_length=200,primary_key=True)  # Field name made lowercase.
    category = models.CharField(db_column='CATEGORY', max_length=300, blank=True, null=True)  # Field name made lowercase.
    season = models.CharField(db_column='SEASON', max_length=300, blank=True, null=True)  # Field name made lowercase.
    material1 = models.CharField(db_column='MATERIAL1', max_length=300, blank=True, null=True)  # Field name made lowercase.
    material2 = models.CharField(db_column='MATERIAL2', max_length=300, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=300, blank=True, null=True)  # Field name made lowercase.
    brand = models.CharField(db_column='BRAND', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productid'


class ProductVar(models.Model):
    article = models.ForeignKey(ProductID,db_column='ARTICLE')  # Field name made lowercase.
    color = models.CharField(db_column='COLOR', max_length=300, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=300, blank=True, null=True)  # Field name made lowercase.
    wholeprice = models.CharField(db_column='WHOLEPRICE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    retailprice = models.CharField(db_column='RETAILPRICE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    inventory = models.IntegerField(db_column='INVENTORY', blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='AGE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(db_column='SIZE', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productvar'
