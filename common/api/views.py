from django.shortcuts import render
from common.models import (
  Persona,
  Producto,
  Dispositivo
)
from rest_framework.viewsets import ModelViewSet
from common.api.serializers import (
  PersonaSerializer,
  ProductoSerializer,
  DispositivoSerializer
)

# Create your views here.
class PersonaView(ModelViewSet):
      queryset=Persona.objects.all()
      lookup_field='id'
      serializer_class=PersonaSerializer

class ProductoView(ModelViewSet):
      queryset=Producto.objects.all()
      lookup_field='id'
      serializer_class=ProductoSerializer

class DispositivoView(ModelViewSet):
      queryset=Dispositivo.objects.all()
      lookup_field='id'
      serializer_class=DispositivoSerializer