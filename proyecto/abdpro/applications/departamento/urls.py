from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "departamento_app"

urlpatterns = [
        # ------------------------------------------------------------------
        # CREAR TRABAJOS
        # ------------------------------------------------------------------

        path('TrabajoAPISerializer/',
                views.TrabajoAPISerializer.as_view(),
                name='TrabajoAPISerializer'),
        # ------------------------------------------------------------------
        # CREAR DEPARTAMENTOS
        # ------------------------------------------------------------------

        path('DepartamentoAPISerializer/',
                views.DepartamentoAPISerializer.as_view(),
                name='DepartamentoAPISerializer'),
        # ------------------------------------------------------------------
        # LISTAR TRABAJOS
        # ------------------------------------------------------------------

        path('TrabajoListAPIView/',
                views.TrabajoListAPIView.as_view(),
                name='TrabajoListAPIView'),
        # ------------------------------------------------------------------
        # LISTAR DEPARTAMENTOS
        # ------------------------------------------------------------------

        path('DepartamentoListAPIView/<pk>/',
                views.DepartamentoListAPIView.as_view(),
                name='DepartamentoListAPIView'),
        # ------------------------------------------------------------------
        # VER TRABAJO POR ID
        # ------------------------------------------------------------------

        path(
                'TrabajoDetailAPIView/<pk>/',
                views.TrabajoDetailAPIView.as_view(),
                name='TrabajoDetailAPIView'
        ),

        # ------------------------------------------------------------------
        # LISTAR DEPARTAMENTOS
        # ------------------------------------------------------------------

        path('DepartamentoListAPIView/',
                views.DepartamentoListAPIView.as_view(),
                name='DepartamentoListAPIView'),


        
]
