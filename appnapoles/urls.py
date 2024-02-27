from django.urls import path
from . import views

urlpatterns = [
    path("", views.pagina_inicio),
    path('guardar_cita/', views.guardar_cita, name='guardar_cita'),
    path('consultar_cita/', views.consultar_cita, name='consultar_cita')
    
]