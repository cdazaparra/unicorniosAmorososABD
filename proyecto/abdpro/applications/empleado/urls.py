from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "empleado_app"

urlpatterns = [
    # ------------------------------------------------------------------
    # CREAR HABILIDAD
    # ------------------------------------------------------------------

    path('HabilidadAPISerializer/',
        views.HabilidadAPISerializer.as_view(),
        name='HabilidadAPISerializer'),
        
    # ------------------------------------------------------------------
    # CREAR EMPLEADO
    # ------------------------------------------------------------------

    path('EmpleadoAPISerializer/',
        views.EmpleadoAPISerializer.as_view(),
        name='EmpleadoAPISerializer'),
    # ------------------------------------------------------------------
    # LISTAR EMPLEADOS
    # ------------------------------------------------------------------

    path(
        'EmpleadoListAPIView/',
        views.EmpleadoListAPIView.as_view(),
        name='EmpleadoListAPIView'
    ),
    # ------------------------------------------------------------------
    # LISTAR HABILIDADES
    # ------------------------------------------------------------------

    path(
        'HabilidadListAPIView/',
        views.HabilidadListAPIView.as_view(),
        name='HabilidadListAPIView'
    ),
]
