from django.shortcuts import render, redirect   
from django.http import HttpResponse
from .forms import ClienteForm, EmpleadoForm, PrendaForm, BuscarPrendaForm
from .models import Prenda

def inicio(request):
    return render(request, 'app_local_ropa/inicio.html')

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ClienteForm()
    return render(request, 'app_local_ropa/crear_cliente.html', {'form': form})

def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = EmpleadoForm()
    return render(request, 'app_local_ropa/crear_empleado.html', {'form': form})

def crear_prenda(request):
    if request.method == 'POST':
        form = PrendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = PrendaForm()
    return render(request, 'app_local_ropa/crear_prenda.html', {'form': form})

def buscar_prenda(request):
    resultados = []
    if request.GET.get('nombre'):
        form = BuscarPrendaForm(request.GET)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            resultados = Prenda.objects.filter(nombre__icontains=nombre)
    else:
        form = BuscarPrendaForm()
    return render(request, 'app_local_ropa/buscar_prenda.html', {'form': form, 'resultados': resultados})





# Create your views here.
