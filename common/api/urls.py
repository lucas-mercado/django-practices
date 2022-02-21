from django.urls import (
    path,
)
from common.api import views

persona_list=views.PersonaView.as_view({'get':'list'})
persona_detail=views.PersonaView.as_view({'get':'retrieve'})

producto_list=views.ProductoView.as_view({'get':'list'})
producto_detail=views.ProductoView.as_view({'get':'retrieve'})

dispositivo_list=views.DispositivoView.as_view({'get':'list'})
dispositivo_detail=views.DispositivoView.as_view({'get':'retrieve'})

urlpatterns = [
    path(
        route='api/personas/',
        view=persona_list,
        name='lista persona'
    ),
    path(
        route='api/personas/<int:id>',
        view=persona_detail,
        name='detail persona'
    ),
    path(
        route='api/dispositivos/',
        view=dispositivo_list,
        name='lista dispositivo'
    ),
    path(
        route='api/dispositivos/<int:id>',
        view=dispositivo_list,
        name='detail dispositivo'
    ),
    path(
        route='api/productos/',
        view=producto_list,
        name='lista producto'
    ),
    path(
        route='api/productos/<int:id>',
        view=producto_list,
        name='detail producto'
    )
]