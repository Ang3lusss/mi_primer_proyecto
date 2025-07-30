
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('clientes/', views.crear_cliente, name='crear_cliente'),
    path('empleados/', views.crear_empleado, name='crear_empleado'),
    path('prendas/', views.crear_prenda, name='crear_prenda'),
    path('buscar-prenda/', views.buscar_prenda, name='buscar_prenda')
]