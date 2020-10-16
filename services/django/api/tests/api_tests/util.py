import json

import requests

payload = {
    "client_id": "ApqgC9UHWyDV0Qb6rv3cby0gP47u5ZmO",
    "client_secret": "SP3eUc3y1SqR9gcN6reBwdO-9yZtsH8UnupujEqjbgNyU1yEd4Qj_4E3UuSolxVh",
    "audience": "https://django-server:8000",
    "grant_type": "client_credentials",
}

headers = {"content-type": "application/json"}

# pylint: disable=line-too-long
ACCESS_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkI4ZmRWNzRVa2NpM0JWM2lBVGtrUiJ9.eyJpc3MiOiJodHRwczovL2RydW1yb3NlLmF1dGgwLmNvbS8iLCJzdWIiOiJBcHFnQzlVSFd5RFYwUWI2cnYzY2J5MGdQNDd1NVptT0BjbGllbnRzIiwiYXVkIjoiaHR0cHM6Ly9kamFuZ28tc2VydmVyOjgwMDAiLCJpYXQiOjE2MDIwMTY4MTYsImV4cCI6MTYwNDYwODgxNiwiYXpwIjoiQXBxZ0M5VUhXeURWMFFiNnJ2M2NieTBnUDQ3dTVabU8iLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMifQ.OahXbApfrUAzVorL9EqBmrG4vcJFTpn0bA9F6TjZXE1X5nWKkhd1o9LYRR36RlVZUnoc-sMV6vT5gjI63t3ETkZFAiiyM1cceB6oO0Oh7PhfftkVkfLOUsCIvaYe7L1XG8A5-zUJTCBHK7YiCNRidpWLJPYMuz7fqR9CAVENZOHFSqgiDnh504J5YmvtCE4KpIsBNls_vJEcr8y7zFLVul4g79rtEzYcfpqaOO5aoSh5_xOsm4GLdA6f41CeZX-5jJ7zlYgeKoLbCh0vW3VckGcvHigHDg7wgXSAmStCwOp6hxBflkKaTUth_ByRrwk7HtotDkVfcMcQm_6hC3nYZw"


def get_test_token():
    data = requests.post(
        "https://drumrose.auth0.com/oauth/token",
        data=json.dumps(payload),
        headers=headers,
    )
    print(data.content)
    return data
