from django.shortcuts import render
from .models import Service # importamos desde el mismo directorio el modelo Services
# Create your views here.
def services(request):
    services = Service.objects.all() # Solicitamos y dejamos guardado en la variable el modelo de servicios
    return render(request, "services/services.html", {'services':services}) # devolvemos la variable con la lista