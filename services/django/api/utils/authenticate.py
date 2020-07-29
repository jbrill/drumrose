from django.contrib.auth import authenticate


def jwt_get_username_from_payload_handler(payload):
    username = payload.get("sub").split("auth0|")[1]
    authenticate(remote_user=username)
    return username
