# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Place(models.Model):
    place_name = models.CharField(max_length=100)

class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=100)
    place = models.OneToOneField(Place)