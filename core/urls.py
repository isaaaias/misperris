from django.urls import path
from .views import home, listar_adoptante, formulario_adoptante, home_cliente

urlpatterns = [
    path('', home , name="home"),
    path('adoptantes/', listar_adoptante, name="adoptantes"),
    path('formulario-adoptante/', formulario_adoptante, name="formulario_adoptante"),
    path('home-cliente/', home_cliente, name="home_cliente"),
]

