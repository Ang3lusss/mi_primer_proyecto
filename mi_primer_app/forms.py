from django import forms

class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre del Curso')
    descripcion = forms.CharField(widget=forms.Textarea, label='Descripción')
    duracion_semanas = forms.IntegerField(label='Duracion (semanas)')
    fecha_inicio = forms.DateField(widget=forms.SelectDateWidget, label='Fecha de inicio')
    fecha_fin = forms.DateField(widget=forms.SelectDateWidget, label='Fecha de Fin')
    activo = forms.BooleanField(required=False, initial=True, label='Activo') #Campo opcional

class EstudianteForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='nombre')
    apellido = forms.CharField(max_length=100, label='apellido')
    email = forms.EmailField(label='email')
    edad = forms.IntegerField(label='edad')