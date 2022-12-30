from django.urls import path 
from .views import *




urlpatterns =[ path("escuelaForm/", escuelaForm,  name='detail'),
               path("atletaForm/", atletaForm, name='atleta'),
               path("busquedaCompanero/", busquedaCompanero, name='busquedaCompanero'),
               path("buscar/", buscar, name="buscar"),]

