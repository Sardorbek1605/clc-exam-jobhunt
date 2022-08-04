from django.db import models
from helpers.models import BaseModel
from common.models import User
# Create your models here.


""" Models For the first task """
class Company(BaseModel):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.TextField()


class Vacancy(BaseModel):
    title = models.CharField(max_length=255)
    cost = models.IntegerField(default=0)
    time = models.DurationField()


""" Models For the second task """
class Vacant(BaseModel):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    about = models.TextField()
    min_price = models.IntegerField(default=0)
    max_price = models.IntegerField(default=0)


class Category(BaseModel):
    vacants = models.ManyToManyField(Vacant, related_name='categories')
    title = models.CharField(max_length=255)
    count_views = models.IntegerField(default=0)


