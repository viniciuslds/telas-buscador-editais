# principal/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='home'),
    path('quem_somos/', views.quem_somos, name='quem_somos'),
    path('nossa_plataforma/', views.nossa_plataforma, name='nossa_plataforma'),
    path('nossos_planos/', views.nossos_planos, name='nossos_planos'),
]