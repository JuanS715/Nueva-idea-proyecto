from django.urls import path 
from .views import *




urlpatterns = [
    path("escuelaForm/", escuelaForm, name='detail'),
    path("busquedaCompañero/", busquedaCompañero, name='busquedaCompañero')
]

