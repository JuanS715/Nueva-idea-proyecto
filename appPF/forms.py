from django import forms 


class EscuelaForm(forms.Form):
    profesor=forms.CharField(label="Profesor: ", max_length=30)
    escuela=forms.CharField(label="Escuela: ", max_length=10)


class busquedaCompañeroForm(forms.Form):
    busqueda=forms.CharField(label="Buscar: ", max_length=50)