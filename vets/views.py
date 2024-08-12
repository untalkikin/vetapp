from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Veterinaria
from django.views.generic.detail import DetailView

# Create your views here.
class VetDetalle(DetailView):
    model = Veterinaria
    template_name = "vets/verdetalle.html"
    
    def get_object(self):
        return get_object_or_404(Veterinaria, nombre=self.kwargs['nombre'])
    