from django.contrib.auth import authenticate


def jwt_get_username_from_payload_handler(payload):
    username = payload.get("sub")
    if "auth0|" in username:
        username = username.split("auth0|")[1]
    if "@clients" in username:
        username = username.split("@clients")[0]
    authenticate(remote_user=username)
    return username
