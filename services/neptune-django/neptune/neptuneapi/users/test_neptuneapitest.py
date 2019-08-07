import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from neptuneapi.models.neptune_core import NeptuneUser
from neptuneapi.user.serializers import NeptuneUserSerializer


# initialize the APIClient app
client = Client()
