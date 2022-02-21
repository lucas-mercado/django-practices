from django.contrib import admin
from registro.models import(
    Reparacion,
    Observacion
)

# Register your models here.
admin.site.register(Reparacion)
admin.site.register(Observacion)