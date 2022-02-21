from rest_framework.serializers import ModelSerializer
from common.models import (
    Persona,
    Producto,
    Dispositivo,
)


class PersonaSerializer(ModelSerializer):
    class Meta:
        model=Persona
        fields='__all__'


class ProductoSerializer(ModelSerializer):
    class Meta:
        model=Producto
        fields='__all__'


class DispositivoSerializer(ModelSerializer):
    class Meta:
        model=Dispositivo
        fields='__all__'