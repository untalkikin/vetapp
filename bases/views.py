from django.shortcuts import render
from django.views.generic import ListView 
from django.views.generic.base import TemplateView 
from vets.models import Veterinaria

# Create your views here.

class Home(ListView):
    template_name = "bases/home.html"
    model = Veterinaria
    context_object_name = "obj"