from django.db.models.signals import pre_save
from django.dispatch import receiver
import requests
from .models import Reserva
from .configuraciones import URL_servidor_whatsapp

@receiver(pre_save, sender=Reserva)
def comparar_cambios(sender, instance, **kwargs):
    if instance.pk:  
        original_instance = sender.objects.get(pk=instance.pk)
        if instance.estado != original_instance.estado:
            print("El estado ha cambiado de", original_instance.estado, "a", instance.estado, "después de guardar.")

            if instance.estado=="Confirmado":
                url_nodejs = URL_servidor_whatsapp+'/confimarCita'
                
            elif instance.estado=="Cancelado":
                url_nodejs = URL_servidor_whatsapp+'/cancelarCita'

            parametros = {
                'cedula': instance.cedula,
                'telefono': instance.telefono,
                'nombres': instance.nombres,
                'fecha': instance.fecha,
                'hora': instance.hora,
                'local': instance.local.nombre
            }
            
            try:
                respuesta = requests.get(url_nodejs, params=parametros)
                if respuesta.status_code == 200:
                    print('Petición enviada correctamente a Node.js')
                else:
                    print('Error al enviar la petición a Node.js')
                    print('Estado de la respuesta:', respuesta.status_code)
            except requests.exceptions.RequestException as e:
                print('Error de conexión:', e)