from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.

# ------------------------------------------------------------------
# APIS
# ------------------------------------------------------------------
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    # DetailView
    RetrieveAPIView,
    # Delete
    DestroyAPIView,
    # Actualizar
    UpdateAPIView,
    # Recupera y actualiza
    RetrieveUpdateAPIView,
    # Recupera y elimina
    RetrieveDestroyAPIView,
)

from .serializer import (
    HabilidadesSerializer,
    EmpleadosSerializer,
)

# ------------------------------------------------------------------
# MODELOS
# ------------------------------------------------------------------
from .models import Empleado, Habilidad

# ------------------------------------------------------------------
# API CREAR UN HABILDIAD
# ------------------------------------------------------------------
class HabilidadAPISerializer(CreateAPIView):
    serializer_class = HabilidadesSerializer

# ------------------------------------------------------------------
# API CREAR UN EMPLEADO
# ------------------------------------------------------------------
class EmpleadoAPISerializer(CreateAPIView):
    serializer_class = EmpleadosSerializer

# ------------------------------------------------------------------
# API VER UN EMPLEADO
# ------------------------------------------------------------------
class EmpleadoListAPIView(ListAPIView):
    serializer_class = EmpleadosSerializer
    def get_queryset(self):
        return Empleado.objects.all()

# ------------------------------------------------------------------
# API VER UN HABILIDAD
# ------------------------------------------------------------------
class HabilidadListAPIView(ListAPIView):
    serializer_class = HabilidadesSerializer
    def get_queryset(self):
        return Habilidad.objects.all()