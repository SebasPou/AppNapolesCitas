from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.template import loader
import requests
from .models import Local, Reserva

def pagina_inicio(request):
    try:
        locales = Local.objects.all()
    except Local.DoesNotExist:
        raise Http404("El local no existe")

    return render(request, "index.html", { "locales": locales })

def consultar_cita(request):
    try:
        if request.POST.get('cedula'):
            cedula = request.POST.get('cedula')
        else:
            cedula = request.GET.get('cedula')

        citas = Reserva.objects.filter(cedula=cedula)
    except Local.DoesNotExist:
        raise Http404("El usuario no tiene citas")
    
    return render(request, "detalles_cita.html", {"citas": citas})

def guardar_cita(request):
    if request.method == 'POST':
        nombres = request.POST.get('nombres')
        cedula = request.POST.get('cedula')
        local_id = request.POST.get('local_id')
        telefono = request.POST.get('telefono')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        
        reserva = Reserva.objects.create(
            nombres=nombres,
            cedula=cedula,
            local_id=local_id,
            telefono=telefono,
            fecha=fecha,
            hora=hora
        )

        enviar_peticion_a_nodejs(telefono, cedula, nombres)

        return render(request, 'cita_registrada.html', {
            "nombres": nombres
        })
    else:
        # Si la solicitud no es POST, devolver un HttpResponse con un mensaje de error
        return HttpResponse('Método no permitido')
    



def enviar_peticion_a_nodejs(telefono, cedula, nombres):
    
    url_nodejs = 'http://localhost:3000/buscarPorCedula'
    
    parametros = {
        'telefono': telefono,
        'cedula': cedula,
        'nombres': nombres
    }

    try:
        respuesta = requests.get(url_nodejs, params=parametros)
        
        if respuesta.status_code == 200:
            print('Petición enviada correctamente a Node.js')
            print('Respuesta del servidor Node.js:', respuesta.text)
        else:
            print('Error al enviar la petición a Node.js')
            print('Estado de la respuesta:', respuesta.status_code)
    except requests.exceptions.RequestException as e:
        print('Error de conexión:', e)