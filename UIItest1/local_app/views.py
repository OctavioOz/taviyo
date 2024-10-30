from django.shortcuts import render
from .models import local

# Create your views here.

def index_vista(request):
        ListadoLocales=local.objects.all()
        return render(request, "gestionarMateria.html",{"Mis_locales":ListadoLocales}) 
