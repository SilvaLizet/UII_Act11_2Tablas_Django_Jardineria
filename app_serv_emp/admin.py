# app_serv_emp/admin.py
from django.contrib import admin
from .models import Empleado, Servicio

admin.site.register(Empleado)
admin.site.register(Servicio)