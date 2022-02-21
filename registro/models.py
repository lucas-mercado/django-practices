from django.db import models
from common.models import (
    Persona,
    Producto,
    Dispositivo,
)
from django.contrib.auth.models import (
    User,
)

class Reparacion(models.Model):
    descripcion=models.CharField(max_length=500)
    status=models.CharField(max_length=50)
    fk_persona=models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='persona_reparaciones')
    fk_producto=models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='producto_reparaciones', null=True, blank=True)
    fk_dispositivo=models.OneToOneField(Dispositivo, on_delete=models.CASCADE, related_name='dispositivo_reparacion')
    create_at=models.DateTimeField(auto_now_add=True, blank=True, null=True)
    create_by=models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_repraciones', null=True)

    def __str__(self):
        return  'reparacion: '+str(self.id)

class Observacion(models.Model):
    descripcion=models.CharField(max_length=500)
    fk_reparacion=models.ForeignKey(Reparacion, on_delete=models.CASCADE, related_name='reparacion_obs')  