from django.urls import path
from . import views

urlpatterns = [
    path("", views.pagina_inicio),
    path('guardar_cita/', views.guardar_cita, name='guardar_cita'),
    path('consultar_cita/<path:cedula>', views.consultar_cita, name='consultar_cita'),
    path('modificar_cita/<int:id>', views.modificar_cita, name='modificar_cita'),
    path('guardar_cambios_reserva/<int:reserva_id>/', views.guardar_cambios_reserva, name='guardar_cambios_reserva'),
]