from django.urls import path
from .views import *

urlpatterns = [
    path('adoptantes/', listar_adoptante, name="api_adoptantes"),
    path('home-cliente/', home_cliente, name="api_home_cliente"),
    path('formulario_adoptante/', formulario_adoptante , name="api_formulario_adoptante"),
    path('eliminar_adoptante/<id>/', eliminar_adoptante, name="api_eliminar_adoptante"),
    path('modificar_adoptante/<id>/', modificar_adoptante, name="api_modificar_adoptante"),
    path('mascotas/', listar_mascota, name="mascotas"),
    path('eliminar_mascota/<id>/', eliminar_mascota, name="api_eliminar_mascota"),
    path('modificar_mascota/<id>/', modificar_mascota, name="api_modificar_mascota"),
    path('formulario_mascota/', formulario_mascota, name="api_formulario_mascota"),
]