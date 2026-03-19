from django.urls import path
from .views import vuelos_view

urlpatterns = [
    path('', vuelos_view, name='vuelos'),
]