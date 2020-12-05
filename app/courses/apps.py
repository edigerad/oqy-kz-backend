from django.apps import AppConfig


class CoursesConfig(AppConfig):
    name = 'app.courses'

    def ready(self):
        from . import signals
