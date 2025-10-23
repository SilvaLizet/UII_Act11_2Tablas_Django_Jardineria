# app_serv_emp/models.py
from django.db import models

class Servicio(models.Model):
    # La tabla 'Servicio' es la "madre"
    id_servicio = models.AutoField(primary_key=True)
    nombre_servicio = models.CharField(max_length=100)
    descripcion_servicio = models.TextField()
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    duracion_estimada = models.CharField(max_length=50) 
    materiales_requeridos = models.TextField(blank=True, null=True)
    
    # Este campo no es necesario aquí para la relación, Django lo gestiona.
    # Eliminamos el id_empleado de aquí.

    def __str__(self):
        return self.nombre_servicio

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"


class Empleado(models.Model):
    # La tabla 'Empleado' es la "hija" y se enlaza al Servicio
    id_empleado = models.AutoField(primary_key=True)
    nombre_empleado = models.CharField(max_length=50)
    apellido_empleado = models.CharField(max_length=50)
    puesto_empleado = models.CharField(max_length=50)
    telefono_empleado = models.CharField(max_length=15)
    fecha_contratacion = models.DateField()
    
    # CLAVE FORÁNEA: Un Empleado trabaja en UN Servicio (id_servicio).
    servicio = models.ForeignKey(
        Servicio, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='empleados' # Permite acceder a los empleados desde el Servicio: servicio.empleados.all()
    )

    def __str__(self):
        return f"{self.nombre_empleado} {self.apellido_empleado} ({self.puesto_empleado})"

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"