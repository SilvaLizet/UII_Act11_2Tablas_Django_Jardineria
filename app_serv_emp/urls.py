# app_serv_emp/urls.py
from django.urls import path
from . import views

app_name = 'app_serv_emp'

urlpatterns = [
    # CRUD de Servicios (reemplazando Artista)
    path('', views.listar_servicios, name='listar_servicios'),
    path('servicio/<int:servicio_id>/', views.detalle_servicio, name='detalle_servicio'),
    path('crear/', views.crear_servicio, name='crear_servicio'),
    path('editar/<int:servicio_id>/', views.editar_servicio, name='editar_servicio'),
    path('borrar/<int:servicio_id>/', views.borrar_servicio, name='borrar_servicio'),
]