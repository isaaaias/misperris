from django.db import models

# Create your models here.
class Comuna(models.Model):
    comuna = models.CharField(max_length=50)


    def __str__(self):
        return self.comuna

class Ciudad(models.Model):
    ciudad = models.CharField(max_length=50)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    
     
    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
    

    def __str__(self):
        return self.ciudad

class Region(models.Model):
    region = models.CharField(max_length=50)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regiones"

    def __str__(self):
        return self.region


class Vivienda(models.Model):
    vivienda = models.CharField(max_length=50)
   
 

    def __str__(self):
        return self.vivienda

class Adoptante(models.Model):
    rut = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=50)
    fechaNacimiento = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    telefono = models.CharField(max_length=11)
    vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
   
    class Meta:
        verbose_name = "Adoptante"
        verbose_name_plural = "Adoptantes"
    
    def __str__(self):
        return self.rut

        