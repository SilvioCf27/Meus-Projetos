from django.shortcuts import render
from .models import TipoDoce, Doce
from django.views import View

def home(request):
    return render(request, 'index.html')

def lista_doce(request):
    doces = Doce.objects.all()
    return render(request, 'lista_doce.html', {'doces': doces})

def index(request):
    return render(request, 'index.html')

class CategoriaBolosView(View):
    def get(self, request):
        bolos = Doce.objects.filter(tipo__nome='Bolo')
        return render(request, 'categoria_bolos.html', {'bolos': bolos})