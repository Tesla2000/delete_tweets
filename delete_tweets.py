from auth import authenticate
from env_variables import *
from get_tweets import get_tweets

from interfaces import Iterable
from interfaces import Keywords1
from interfaces import Oauth4
from interfaces import Union


def delete_by_keywords(oauth, keywords: Union[Iterable, Keywords1]):
    data = get_tweets(oauth, 1000)
    for tweet in data:
        for word in keywords:
            if word.lower() + " " in tweet["text"].lower():
                delete_tweet(oauth, tweet["id"])


def delete_tweet(oauth: Oauth4, tweet_id):
    response = oauth.delete("https://api.twitter.com/2/tweets/" + str(tweet_id))

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))


def delete_tweets(keywords):
    session = authenticate(CONSUMER_KEY, CONSUMER_SECRET)
    delete_by_keywords(session, keywords)
