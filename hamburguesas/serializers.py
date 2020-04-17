from rest_framework import serializers
from .models import Hamburguesa, Ingrediente


class HamburguesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hamburguesa
        fields = ('id', 'name', 'price', 'description', 'image')

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ('id', 'name', 'description')

