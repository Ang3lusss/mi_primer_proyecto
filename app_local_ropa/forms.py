from django import forms
from .models import Cliente, Empleado, Prenda

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

class PrendaForm(forms.ModelForm):
    class Meta:
        model = Prenda
        fields = '__all__'

class BuscarPrendaForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)
