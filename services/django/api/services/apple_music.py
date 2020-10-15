import requests
from api.settings import APPLE_MUSIC_TOKEN_GENERATOR


def get_track_info(apple_music_id):
    response = requests.get(
        "https://api.music.apple.com/v1/catalog/us/songs/{}".format(apple_music_id),
        headers={
            "Authorization": "Bearer {}".format(
                APPLE_MUSIC_TOKEN_GENERATOR.generate_token()
            )
        },
        verify=False,
    )
    try:
        attributes = response.json()["data"][0]["attributes"]
    except KeyError as e:
        print(e)
        attributes = None
    return attributes
