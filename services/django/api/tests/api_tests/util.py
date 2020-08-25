import http.client

conn = http.client.HTTPSConnection("drumrose.auth0.com")

payload = str(
    {
        "client_id": "ApqgC9UHWyDV0Qb6rv3cby0gP47u5ZmO",
        "client_secret": "SP3eUc3y1SqR9gcN6reBwdO-9yZtsH8UnupujEqjbgNyU1yEd4Qj_4E3UuSolxVh",
        "audience": "https://django-server:8000",
        "grant_type": "client_credentials",
    }
)

headers = {"content-type": "application/json"}


def get_test_token():
    conn.request("POST", "/oauth/token", payload, headers)

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")
