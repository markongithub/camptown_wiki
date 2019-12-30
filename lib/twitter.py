import os
import sys
import tweepy

from collections import namedtuple

TwitterAuth = namedtuple(
    "TWITTER",
    ["consumer_key", "consumer_secret", "access_token", "access_token_secret"],
)


def getTwitterCredentials():

    return TwitterAuth(
        consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
        consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
        access_token=os.environ['TWITTER_ACCESS_TOKEN'],
        access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'],
    )


def sendTweet(tweet_text: str, image_path=""):
    """Post some text, and optionally an image to twitter.

    Args:
        tweet_text: String, text to post to twitter, must be less than 260 chars
        image_path: String, path to image on disk to be posted to twitter
    Returns:
        tweepy.status object, contains response from twitter request
    """
    TWITTER = getTwitterCredentials()
    auth = tweepy.OAuthHandler(TWITTER.consumer_key, TWITTER.consumer_secret)
    auth.set_access_token(TWITTER.access_token, TWITTER.access_token_secret)

    api = tweepy.API(auth)

    if image_path:
        return api.update_with_media(filename=image_path, status=tweet_text)
    else:
        return api.update_status(tweet_text)

    return api.update_status(tweet_text)
