import datetime

import jwt


class AppleMusicTokenGenerator:
    """
    Apple Music Token Generator Class
    """

    def __init__(self, secret, key_id, team_id):
        """
        Init structure with `team_id` `secret` `key_id`
        """
        self.secret = secret.replace(r"\n", "\n")
        self.key_id = key_id
        self.team_id = team_id

        self.alg = "ES256"

    def generate_token(self):
        """
        Generate a token based off the current time and a delta of 12 hours
        """
        time_now = datetime.datetime.now()
        time_expired = datetime.datetime.now() + datetime.timedelta(hours=12)

        headers = {"alg": self.alg, "kid": self.key_id}

        payload = {
            "iss": self.team_id,
            "exp": int(time_expired.strftime("%s")),
            "iat": int(time_now.strftime("%s")),
        }
        token = jwt.encode(
            payload, self.secret, algorithm=self.alg, headers=headers
        )
        return token.decode("utf-8")
