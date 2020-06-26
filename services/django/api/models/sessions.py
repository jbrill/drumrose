from django.contrib.sessions.backends.db import SessionStore as DBStore
from django.contrib.sessions.base_session import AbstractBaseSession
from django.db import models


class CustomSession(AbstractBaseSession):
    auth0_management_key = models.CharField(
        max_length=300, null=True, db_index=True
    )
    is_authorized = models.BooleanField(default=True)

    @classmethod
    def get_session_store_class(cls):
        return SessionStore


class SessionStore(DBStore):
    @classmethod
    def get_model_class(cls):
        return CustomSession

    def create_model_instance(self, data):
        obj = super().create_model_instance(data)
        try:
            auth0_management_key = data.get("_auth0_management_key")
        except (ValueError, TypeError):
            auth0_management_key = None
            obj.is_authorized = False
        obj.auth0_management_key = auth0_management_key
        return obj
