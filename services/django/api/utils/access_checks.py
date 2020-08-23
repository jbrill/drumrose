"""
Auth scope identifier based on
https://github.com/auth0-samples/auth0-django-api
"""

import os
from functools import wraps

import jwt
import requests
from cryptography.hazmat.backends import default_backend
from cryptography.x509 import load_pem_x509_certificate
from django.contrib.auth import authenticate
from django.http import JsonResponse


def get_public_key():
    """
    Returns public key
    """
    cert_url = "https://music.auth0.com/.well-known/jwks.json"
    jwks = requests.get(cert_url).json()
    certificate_raw = (
        "-----BEGIN CERTIFICATE-----\n"
        + jwks["keys"][0]["x5c"][0]
        + "\n-----END CERTIFICATE-----"
    )

    certificate = load_pem_x509_certificate(
        str.encode(certificate_raw), default_backend()
    )

    return certificate.public_key()


def get_username_from_payload(payload):
    """
    Get username from jwt
    """
    username = payload.get("sub").replace("|", ".")
    authenticate(remote_user=username)

    print(username)
    return username


def get_token_auth_header(request):
    """
    Obtains the access token from the Authorization Header
    """
    auth = request.META.get("HTTP_AUTHORIZATION", None)
    parts = auth.split()
    token = parts[1]

    return token


def requires_scope(required_scope):
    """Determines if the required scope is present in the access token
    Args:
        required_scope (str): The scope required to access the resource
    """

    def require_scope(func):
        """
        Decorator for scope
        """

        @wraps(func)
        def decorated(*args, **kwargs):
            """
            Check for permissions
            """
            auth_token = get_token_auth_header(args[0])
            # AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')
            api_identifier = os.environ.get("API_IDENTIFIER")
            public_key = get_public_key()
            decoded = jwt.decode(
                auth_token, public_key, audience=api_identifier, algorithms=["RS256"]
            )

            if decoded.get("scope"):
                token_scopes = decoded["scope"].split()
                for token_scope in token_scopes:
                    if token_scope == required_scope:
                        return func(*args, **kwargs)
            response = JsonResponse(
                {"message": "You don't have access to this resource"}
            )
            response.status_code = 403
            return response

        return decorated

    return require_scope
