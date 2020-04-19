from rest_framework import serializers
from .models import Hamburguesa, Ingrediente


class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ('id', 'nombre', 'descripcion')

class CustomIngredienteSerializer(IngredienteSerializer):

    def to_representation(self, instance):
        data = super(IngredienteSerializer, self).to_representation(instance)
        base_url = "https://tarea2iic3103.herokuapp.com/ingrediente/"
        path = base_url + str(data['id'])
        return {'path': path}



class HamburguesaSerializer(serializers.ModelSerializer):
    ingredientes = CustomIngredienteSerializer(many=True, required=False)
    class Meta:
        model = Hamburguesa
        fields = ('id', 'nombre', 'precio', 'descripcion', 'imagen', 'ingredientes')



