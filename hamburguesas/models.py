from django.db import models

# Create your models here.


class Ingrediente(models.Model):

    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)



class Hamburguesa(models.Model):

    nombre = models.CharField(max_length=100)
    precio = models.IntegerField(default=0)
    descripcion = models.CharField(max_length=255)
    imagen = models.URLField(max_length=255)
    ingredientes = models.ManyToManyField(Ingrediente)
