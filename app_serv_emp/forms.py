# app_serv_emp/forms.py
from django import forms
from .models import Servicio, Empleado

# Formulario principal para la tabla Servicio
class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        # Solo necesitamos los campos de la tabla Servicio
        fields = ['nombre_servicio', 'descripcion_servicio', 'precio_base', 'duracion_estimada', 'materiales_requeridos']

# Formulario secundario para la tabla Empleado (si lo quieres como CRUD aparte)
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre_empleado', 'apellido_empleado', 'puesto_empleado', 
                  'telefono_empleado', 'fecha_contratacion', 'servicio']
        widgets = {
            'fecha_contratacion': forms.DateInput(attrs={'type': 'date'}),
        }