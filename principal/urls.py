# principal/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='home'),
]