import json
import os

from requests_oauthlib import OAuth1Session

from interfaces import Oauth2


# payload = {"text": "Hello world!"}

def post_tweet(oauth: Oauth2, payload):
    response = oauth.post(
        "https://api.twitter.com/2/tweets",
        json=payload,
    )

    if response.status_code != 201:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))

    # Saving the response as JSON
    json_response = response.json()
    # print(json.dumps(json_response, indent=4, sort_keys=True))
