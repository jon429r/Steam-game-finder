'''HomePage/apps.py:
This file provides application-specific configuration.
It's where you can specify app-level settings and signals.
'''

from django.apps import AppConfig


class Home_Page_Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Home_Page'
