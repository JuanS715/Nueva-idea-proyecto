from django.db import models

# Create your models here.


class Escuela(models.Model):
    profesor=models.CharField(max_length=60)
    escuela=models.CharField(max_length=20)


    def __str__(self):
        return self.profesor + self.escuela


class nivel(models.Model):
    cinturon=models.CharField(max_length=12)
    edad=models.IntegerField
    peso=models.IntegerField

    def __str__(self):
        return self.cinturon + self.edad + self.edad



class BusquedaCompanero(models.Model):
    busqueda=models.CharField( max_length=50)
     
     
     
     
    def __str__(self):
        return self.busqueda