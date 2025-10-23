# app_serv_emp/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Servicio
from .forms import ServicioForm

# Usaremos las vistas de CRUD para la tabla Servicio (como Artista en tu plantilla)

def listar_servicios(request):
    """Muestra la lista de todos los servicios."""
    servicios = Servicio.objects.all()
    # Usamos el nombre de plantilla del repositorio (listar_artistas.html)
    return render(request, 'listar_servicios.html', {'servicios': servicios})

def detalle_servicio(request, servicio_id):
    """Muestra los detalles de un servicio y sus empleados asignados."""
    servicio = get_object_or_404(Servicio, id_servicio=servicio_id)
    # Usamos el nombre de plantilla del repositorio (detalle_artista.html)
    return render(request, 'detalle_servicio.html', {'servicio': servicio})

def crear_servicio(request):
    """Maneja la creación de un nuevo servicio."""
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_serv_emp:listar_servicios')
    else:
        form = ServicioForm()
        
    # Usamos el nombre de plantilla del repositorio (formulario_artista.html)
    return render(request, 'formulario_servicio.html', {'form': form, 'titulo': 'Crear Nuevo Servicio'})

def editar_servicio(request, servicio_id):
    """Maneja la edición de un servicio existente."""
    servicio = get_object_or_404(Servicio, id_servicio=servicio_id)
    
    if request.method == 'POST':
        form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('app_serv_emp:detalle_servicio', servicio_id=servicio.id_servicio)
    else:
        form = ServicioForm(instance=servicio)
        
    # Usamos el nombre de plantilla del repositorio (formulario_artista.html)
    return render(request, 'formulario_servicio.html', {'form': form, 'titulo': 'Editar Servicio'})

def borrar_servicio(request, servicio_id):
    """Maneja la eliminación de un servicio."""
    servicio = get_object_or_404(Servicio, id_servicio=servicio_id)
    
    if request.method == 'POST':
        servicio.delete()
        return redirect('app_serv_emp:listar_servicios')
        
    # Usamos el nombre de plantilla del repositorio (confirmar_borrar.html)
    return render(request, 'confirmar_borrar_servicio.html', {'servicio': servicio})