from django.contrib import admin
from .models import(
    Persona,
    Dispositivo,
    Producto
)

# Register your models here.
admin.site.register(Persona)
admin.site.register(Producto)
admin.site.register(Dispositivo)

