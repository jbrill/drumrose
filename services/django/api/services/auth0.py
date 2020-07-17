import os

import requests


AUTH0_MANAGEMENT_URL = "https://drumrose.auth0.com/api/v2/"

TOKEN_EXPIRATION_ERR_MESSAGE = (
    "Expired token received for JSON Web Token validation"
)


def _build_headers(_access_token_in):
    return {"authorization": "Bearer {}".format(_access_token_in)}


def auth0_response_is_valid(response):
    print(response)
    print(response["statusCode"])
    if response["statusCode"] != 200:
        return False
    return True


def get_access_token():
    headers = {"content-type": "application/json"}
    payload = {
        "grant_type": "client_credentials",
        "client_id": "{}".format(os.getenv("AUTH0_CLIENT_ID")),
        "client_secret": "{}".format(os.getenv("AUTH0_CLIENT_SECRET")),
        "audience": "{}".format(os.getenv("AUTH0_AUDIENCE")),
    }

    res = requests.post(
        "{}/oauth/token".format(os.getenv("AUTH0_DOMAIN")), payload, headers
    )
    try:
        token = res.json()["access_token"]
        return token
    except KeyError:
        return None
    return None


def auth0_request(url_in, token_in):
    res = requests.get(url_in, headers=_build_headers(token_in)).json()

    if "message" in res and res["message"] == TOKEN_EXPIRATION_ERR_MESSAGE:
        return

    return res


def get_user(user_id, token):
    get_user_url = AUTH0_MANAGEMENT_URL + "users/{}".format(user_id)
    return auth0_request(get_user_url, token)
