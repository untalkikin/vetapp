from django.urls import path
from .views import VetDetalle

profiles_patterns = ([
    path('<nombre>/', VetDetalle.as_view(), name='detail'),
], "Veterinaria")