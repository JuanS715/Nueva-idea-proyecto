from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from appPF.forms import *



# Create your views here.
def escuelaForm(request):
    if request.method=="POST":
        form=EscuelaForm(request.POST)

        if form.is_valid():
            informacion=form.cleaned_data
            profesor=informacion["profesor"]
            escuela=informacion["escuela"]
            atleta=Escuela(profesor=profesor, escuela=escuela)
            atleta.save()
            return render(request, "appPF/index.html", {"mensaje":"Porfavor rellene el formulario"})

        else:
            return render(request, "appPF/escuela.html", {"form": form, "mensaje":"iformacion erronea"})

    else:
        atleta= EscuelaForm()
        return render(request, "appPF/escuela.html", {"form":atleta})

def atletaForm(request):
    if request.method=="POST":
        form1=AtletaForm(request.POST)

        if form1.is_valid():
            informacion=form1.cleaned_data
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            edad=informacion["edad"]
            peso=informacion["peso"]
            cinturon=informacion["cinturon"]
            atleta1=Atleta(nombre=nombre, apellido=apellido , edad=edad , peso=peso , cinturon=cinturon ,)
            atleta1.save()
            return render(request, "appPF/busquedaCompanero.html", {"mensaje":"Atleta confirmado"})
        else:
            return render(request, "appPF/index.html", {"form1": form1, "mensaje":" erronea"})
    else:
         atleta1= AtletaForm()
         return render(request, "appPF/atleta.html", {"form1":atleta1})

    

def busquedaCompanero(request):
     return render(request, "appPF/busquedaCompanero.html")


#def buscarLlave(request):
     

def buscar(request):
    peso=request.GET["peso"]
    if peso!="":
        atletas=Atleta.objects.filter(peso=peso)
        return render(request, "appPF/resultadoBusqueda.html", {"atletas":atletas})
        
    else:
        return render(request, "appPF/busquedaCompanero.html", {"mensaje":"Try Again "})