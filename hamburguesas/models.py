from django.db import models

# Create your models here.


class Hamburguesa(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=255)
    image = models.URLField(max_length=255)

class Ingrediente(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

