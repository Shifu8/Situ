from django.shortcuts import render, redirect, get_object_or_404
from .forms import PasajeroFormulario
from .models import Pasajero

# Create your views here.

def home_view(request):
    return render(request, "index.html", {})

def pasajeros(request):
    pasajeros = Pasajero.objects.all()
    form = PasajeroFormulario()
    
    if request.method == 'POST':
        form = PasajeroFormulario(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to="pasajeros") # Redirecciona para limpiar el formulario tras guardar

    return render(request, "pasajeros.html", {"pasajeros": pasajeros, 'form': form})

def pasajerosEdit(request, id):
    pasajero = get_object_or_404(Pasajero, id=id)
    data = {
        'form': PasajeroFormulario(instance=pasajero)
    }
    
    if request.method == 'POST':
        formulario = PasajeroFormulario(data=request.POST, instance=pasajero, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="pasajeros")

    return render(request, 'pasajerosEdit.html', data)

def eliminar_pasajero(request, id):
    pasajero = get_object_or_404(Pasajero, id=id)
    pasajero.delete()
    return redirect(to="pasajeros")