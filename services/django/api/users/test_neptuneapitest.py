import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from api.models.core import User
from api.user.serializers import UserSerializer


# initialize the APIClient app
client = Client()
