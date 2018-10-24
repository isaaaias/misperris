from django.shortcuts import render
from .models import Adoptante, Region ,Vivienda ,Ciudad ,Comuna

from django.contrib import messages

from django.contrib.auth.decorators import login_required



# Create your views here.

# Create your views here.

def home (request):
    return render(request,'core/home.html')

def home_cliente (request):
    return render(request,'core/home_cliente.html')

@login_required
def listar_adoptante(request):
    #obtenemos todos los automoviles desde la BBDD
    adoptantes = Adoptante.objects.all()
    #le pasamos los postulantes al template
    #para que el los despliegue
    return render(request, 'core/listado_adoptantes.html',{
        'adoptantes':adoptantes
    })

@login_required
def formulario_adoptante(request):

    regiones = Region.objects.all()
    #declaramos las variables que se enviarán al template
    variables = {
        'regiones':regiones
    }
    ciudades = Ciudad.objects.all()
    #declaramos las variables que se enviarán al template
    variables = {
        'ciudades':ciudades
    }

    comunas = Comuna.objects.all()
    #declaramos las variables que se enviarán al template
    variables = {
        'comunas':comunas
    }

    viviendas = Vivienda.objects.all()
    #declaramos las variables que se enviarán al template
    variables = {
        'viviendas':viviendas
    }
    #preguntamos si la peticion es POST, lo que quiere decir que el usuario
    #presiono el boton en el formulario
    if request.POST:
        #instanciamos un modelo Adoptante
        adoptante = Adoptante()
        adoptante.rut = request.POST.get('rut')
        adoptante.nombre = request.POST.get('nombre')
        adoptante.fechaNacimiento = request.POST.get('txtFechaNacimiento')
        adoptante.email = request.POST.get('email')
        adoptante.telefono = int(request.POST.get('txtTelefono'))
        #instanciar un modelo Region
        region = Region()
        region.id = int(request.POST.get('cboRegion'))
        #le pasamos el modelo region al Adoptante
        adoptante.region = region
        #instanciar un modelo Ciudad
        ciudad = Ciudad()
        ciudad.id = int(request.POST.get('cboCiudad'))
        #le pasamos el modelo ciudad al Adoptante
        adoptante.ciudad = ciudad
          #instanciar un modelo Comuna
        comuna = Comuna()
        comuna.id = int(request.POST.get('cboComuna'))
        #le pasamos el modelo comuna al Adoptante
        adoptante.comuna = comuna

        vivienda = Vivienda()
        vivienda.id = int(request.POST.get('cboVivienda'))
        #le pasamos el modelo vivienda al Adoptante
        adoptante.vivienda = vivienda

        try:
            adoptante.save()
            variables['mensaje'] = "Guardado correctamente"
        except:
            variables['mensaje'] = "No se ha podido guardar"

        
    return render(request, 'core/formulario_adoptante.html', variables)
