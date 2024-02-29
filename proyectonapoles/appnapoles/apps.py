from django.apps import AppConfig


class AppnapolesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appnapoles'
    
    def ready(self):
        import appnapoles.signals  # Importa las señales cuando la aplicación esté lista