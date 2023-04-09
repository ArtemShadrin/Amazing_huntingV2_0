from django.db import models

from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=250)
    is_published = models.BooleanField()


class Category(models.Model):
    name = models.CharField(max_length=250)
