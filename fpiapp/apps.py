from django.apps import AppConfig


class FpiappConfig(AppConfig):
    name = 'fpiapp'

    def ready(self):
        import fpiapp.signals