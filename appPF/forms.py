from django import forms 


class EscuelaForm(forms.Form):
    profesor=forms.CharField(label="Profesor: ", max_length=30)
    escuela=forms.CharField(label="Escuela: ", max_length=10)
    


class AtletaForm(forms.Form):
    nombre=forms.CharField(label="Nombre: ", max_length=20)
    apellido=forms.CharField(label="Apellido: ", max_length=20)
    cinturon=forms.CharField(label="Cinturon: ", max_length=12)
    edad=forms.IntegerField(label="Edad: ",)
    peso=forms.IntegerField(label="Categoria en KGs: ", )
