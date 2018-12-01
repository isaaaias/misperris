from django.shortcuts import render

#este paquete nos ayudara a 
#transformar arreglos de python
#en json
from django.core import serializers
from django.http import HttpResponse, HttpResponseBadRequest
import json
from core.models import Adoptante, Ciudad, Region, Mascota, Raza, Tipo
# Create your views here.
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

def listar_adoptante(request):
    adoptantes = Adoptante.oobjects.all()
    
    #transformamos el arreglo de automoviles
    #a un json
    adoptantesJson = serializers.serialize('json', adoptantes)

    #retornamos el json como respuesta al usuario
    return HttpResponse(adoptantesJson, content_type="application/json")





@csrf_exempt
@require_http_methods(['POST'])
def formulario_adoptante(request):
    #obtener el body del request donde esta el json
    body  = request.body.decode('utf-8')

    #ahora transformamos el body hacia un diccionario de python
    body_diccionario = json.loads(body)

    #ingresamos los datos a la BBDD
    adoptante = Adoptante()
    adoptante.rut = body_diccionario['rut']
    adoptante.nombre = body_diccionario['nombre']
    adoptante.fechaNacimiento = body_diccionario['fechaNacimiento']
    adoptante.email = body_diccionario['email']
    adoptante.telefono = body_diccionario['telefono']
    adoptante.region = Region(id=body_diccionario['id'])
    adoptante.ciudad = Ciudad(id=body_diccionario['id'])
    adoptante.vivienda = Vivienda(id=body_diccionario['id'])



    try:
        auto.save()
        mensaje = {
            'mensaje':'guardado correctamente'
        }
        return HttpResponse(json.dumps(mensaje), content_type="application/json")
    except:
        mensaje = {
            'mensaje':'error al guardar'
        }
        return HttpResponseBadRequest(json.dumps(mensaje), content_type="application/json")

@csrf_exempt
@require_http_methods(['PUT'])
def modificar_adoptante(request):
    #obtener el body del request donde esta el json
    body  = request.body.decode('utf-8')

    #ahora transformamos el body hacia un diccionario de python
    body_diccionario = json.loads(body)

    #ingresamos los datos a la BBDD
    adoptante = Adoptante()
    adoptante.rut = body_diccionario['rut']
    adoptante.nombre = body_diccionario['nombre']
    adoptante.fechaNacimiento = body_diccionario['fechaNacimiento']
    adoptante.email = body_diccionario['email']
    adoptante.telefono = body_diccionario['telefono']
    adoptante.region = Region(id=body_diccionario['id'])
    adoptante.ciudad = Ciudad(id=body_diccionario['id'])
    adoptante.vivienda = Vivienda(id=body_diccionario['id'])


    try:
        auto.save()
        mensaje = {
            'mensaje':'modificado correctamente'
        }
        return HttpResponse(json.dumps(mensaje), content_type="application/json")
    except:
        mensaje = {
            'mensaje':'error al modificar'
        }
        return HttpResponseBadRequest(json.dumps(mensaje), content_type="application/json")

@csrf_exempt
@require_http_methods(['DELETE'])
def eliminar_adoptante(request, id):

    try:
        adoptante = Adoptante.objects.get(id=id)
        adoptante.delete()
        mensaje = {
            'mensaje':'Eliminado correctamente'
        }
        return HttpResponse(json.dumps(mensaje), content_type='application/json')
    except:
        mensaje = {
            'mensaje': 'No se ha podido eliminar'
        }
        return HttpResponseBadRequest(json.dumps(mensaje), content_type='application/json')


def listar_mascota(request):
    mascota = Mascota.oobjects.all()
    
    #transformamos el arreglo de automoviles
    #a un json
    mascotaJson = serializers.serialize('json', mascota)

    #retornamos el json como respuesta al usuario
    return HttpResponse(adoptantesJson, content_type="application/json")


@csrf_exempt
@require_http_methods(['POST'])
def formulario_mascota(request):
    #obtener el body del request donde esta el json
    body  = request.body.decode('utf-8')

    #ahora transformamos el body hacia un diccionario de python
    body_diccionario = json.loads(body)

    #ingresamos los datos a la BBDD
    mascota = Mascota()
    mascota.nombre = body_diccionario['rut']
    mascota.genero = body_diccionario['genero']
    mascota.fechaIngreso = body_diccionario['fechaIngreso']
    mascota.fechaNacimiento = body_diccionario['fechaNacimiento']
    mascota.descripcion = body_diccionario['descripcion']
    mascota.model_pic = body_diccionario['image']
    adoptante.raza = Raza(id=body_diccionario['id'])
    adoptante.tipo = Tipo(id=body_diccionario['id'])

    try:
        auto.save()
        mensaje = {
            'mensaje':'guardado correctamente'
        }
        return HttpResponse(json.dumps(mensaje), content_type="application/json")
    except:
        mensaje = {
            'mensaje':'error al guardar'
        }
        return HttpResponseBadRequest(json.dumps(mensaje), content_type="application/json")




@csrf_exempt
@require_http_methods(['PUT'])
def modificar_mascota(request):
    #obtener el body del request donde esta el json
    body  = request.body.decode('utf-8')

    #ahora transformamos el body hacia un diccionario de python
    body_diccionario = json.loads(body)

    #ingresamos los datos a la BBDD
    mascota = Mascota()
    mascota.nombre = body_diccionario['rut']
    mascota.genero = body_diccionario['genero']
    mascota.fechaIngreso = body_diccionario['fechaIngreso']
    mascota.fechaNacimiento = body_diccionario['fechaNacimiento']
    mascota.descripcion = body_diccionario['descripcion']
    mascota.model_pic = body_diccionario['image']
    adoptante.raza = Raza(id=body_diccionario['id'])
    adoptante.tipo = Tipo(id=body_diccionario['id'])


    try:
        auto.save()
        mensaje = {
            'mensaje':'modificado correctamente'
        }
        return HttpResponse(json.dumps(mensaje), content_type="application/json")
    except:
        mensaje = {
            'mensaje':'error al modificar'
        }
        return HttpResponseBadRequest(json.dumps(mensaje), content_type="application/json")



@csrf_exempt
@require_http_methods(['DELETE'])
def eliminar_mascota(request, id):

    try:
        mascota = Mascota.objects.get(id=id)
        mascota.delete()
        mensaje = {
            'mensaje':'Eliminado correctamente'
        }
        return HttpResponse(json.dumps(mensaje), content_type='application/json')
    except:
        mensaje = {
            'mensaje': 'No se ha podido eliminar'
        }
        return HttpResponseBadRequest(json.dumps(mensaje), content_type='application/json')
