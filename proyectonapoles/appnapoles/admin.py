from django.contrib import admin
from .models import Local, Reserva


admin.site.site_header = "Nápoles"
admin.site.register(Local)
admin.site.register(Reserva)