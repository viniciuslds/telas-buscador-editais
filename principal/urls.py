# principal/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='home'),
    path('quem_somos/', views.quem_somos, name='quem_somos'),
]