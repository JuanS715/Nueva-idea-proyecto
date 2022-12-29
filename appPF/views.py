from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from appPF.forms import EscuelaForm



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
            return render(request, "appPF/index.html", {"mensaje":"Atleta confirmado"})

        else:
            return render(request, "appPF/escuela.html", {"form": form, "mensaje":"iformacion erronea"})

    else:
        atleta= EscuelaForm()
        return render(request, "appPF/escuela.html", {"form":atleta})









def busquedaCompanero(request):
     return render(request, "appPF/busquedaCompanero.html")


def buscar(request):
    profesor=request.GET["profesor"]
    if profesor!="":
        escuelas=Escuela.objects.filter(profesor=profesor)
        return render(request, "appPF/resultadoBusqueda.html", {"escuelas":escuelas})
        
    else:
        return render(request, "appPF/busquedaCompanero.html", {"mensaje":"Try Again "})