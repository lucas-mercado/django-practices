from django.urls import (
    path,
)
from registro.api import views


urlpatterns = [
    path(
        route='api/registros/',
        view=views.registroViewList,
        name='lista registros'
    ),
    path(
        route='api/observaciones/',
        view=views.observacionViewList,
        name='lista observaciones'
    ),
]