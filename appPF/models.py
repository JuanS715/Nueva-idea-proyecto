from django.db import models

# Create your models here.


class Escuela(models.Model):
    profesor=models.CharField(max_length=60)
    escuela=models.CharField(max_length=20)
    

    def __str__(self):
        return self.profesor + self.escuela 


class Atleta(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    cinturon=models.CharField(max_length=12)
    edad=models.IntegerField()
    peso=models.IntegerField()

    def __str__(self):
        return self.nombre + self.apellido + self.cinturon , self.edad , self.peso



class BusquedaCompanero(models.Model):
    busqueda=models.CharField( max_length=50)
     
     
     
     
    def __str__(self):
        return self.busqueda