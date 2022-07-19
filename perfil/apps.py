
from django.apps import AppConfig


class PerfilConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'perfil'

    def ready(self, *args, **kwargs):
        import perfil.signals  # noqa
        super_ready = super().ready(*args, **kwargs)

        return super_ready
