"""
App Config Module
"""

from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    """
    Django App Config
    """

    name = "api"
    verbose_name = " Django Backend"
