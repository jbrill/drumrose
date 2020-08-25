"""
Django settings for  project.

Generated by 'django-admin startproject' using Django 1.11.16.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

import requests
from api.services.auth0 import get_access_token
from api.utils.generate_apple_music_token import AppleMusicTokenGenerator
from cryptography.hazmat.backends import default_backend
from cryptography.x509 import load_pem_x509_certificate

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "n467bz@g24axx$=zf17ty@$j(m!t9o+tu!lhfafd4$_!r7ja&$"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
if os.getenv("DEBUG") == "1":
    Debug = True

# TODO: Revisit
ALLOWED_HOSTS = ["django-server", "127.0.0.1", "localhost", "teton.drumrose.io"]

# Application definition
INSTALLED_APPS = [
    "api.apps.AppConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "rest_framework_jwt",
    "rest_framework_auth0",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.RemoteUserMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "django.contrib.auth.backends.RemoteUserBackend",
]

ROOT_URLCONF = "api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "api.wsgi.application"


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("POSTGRES_DB_NAME", ""),
        "USER": os.getenv("POSTGRES_USER", ""),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", ""),
        "HOST": os.getenv("POSTGRES_HOST", ""),
        "PORT": os.getenv("POSTGRES_PORT", ""),
    }
}

# Rest Framework
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_auth0.authentication.Auth0JSONWebTokenAuthentication",
    ),
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


APPLE_MUSIC_KEY_ID = os.getenv("APPLE_MUSIC_KEY_ID", None)
APPLE_MUSIC_TEAM_ID = os.getenv("APPLE_MUSIC_TEAM_ID", None)
APPLE_MUSIC_SECRET = os.getenv("APPLE_MUSIC_SECRET", None)

APPLE_MUSIC_TOKEN_GENERATOR = AppleMusicTokenGenerator(
    APPLE_MUSIC_SECRET, APPLE_MUSIC_KEY_ID, APPLE_MUSIC_TEAM_ID
)


AUTH0_MANAGEMENT_TOKEN = get_access_token

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = "/static/"

CORS_ORIGIN_WHITELIST = ("http://nuxt-server:3000",)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "root": {"handlers": ["console"], "level": "WARNING"},
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": False,
        }
    },
}


AUTH0_DOMAIN = "drumrose.auth0.com"
API_IDENTIFIER = "https://django-server:8000"
PUBLIC_KEY = None
JWT_ISSUER = None


if AUTH0_DOMAIN:
    jwks_url = "https://{}/.well-known/jwks.json".format(AUTH0_DOMAIN)
    jsonurl = requests.get(jwks_url)
    jwks = jsonurl.json()
    cert = (
        "-----BEGIN CERTIFICATE-----\n"
        + jwks["keys"][0]["x5c"][0]
        + "\n-----END CERTIFICATE-----"
    )
    certificate = load_pem_x509_certificate(cert.encode("utf-8"), default_backend())
    PUBLIC_KEY = certificate.public_key()
    JWT_ISSUER = "https://" + AUTH0_DOMAIN + "/"

AUTH0 = {
    "CLIENTS": {
        "default": {
            "AUTH0_CLIENT_ID": "ApqgC9UHWyDV0Qb6rv3cby0gP47u5ZmO",
            "AUTH0_AUDIENCE": API_IDENTIFIER,
            "AUTH0_ALGORITHM": "RS256",  # default used in Auth0 apps
            "PUBLIC_KEY": PUBLIC_KEY,
        }
    },
    # Management API - For roles and permissions validation
    "MANAGEMENT_API": {
        "AUTH0_DOMAIN": "<YOUR_AUTH0_DOMAIN>",
        "AUTH0_CLIENT_ID": "<YOUR_AUTH0_M2M_API_MANAGEMENT_CLIENT_ID>",
        "AUTH0_CLIENT_SECRET": "<YOUR_AUTH0_M2M_API_MANAGEMENT_CLIENT_SECRET>",
    },
}
