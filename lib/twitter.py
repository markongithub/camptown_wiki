import os
import tweepy


def sendTweet(tweet_text: str):
    """Post some text, and optionally an image to twitter.

    Args:
        tweet_text: String, text to post to twitter, must be less than 260 chars
    Returns:
        tweepy.status object, contains response from twitter request
    """

    client = tweepy.Client(
        consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
        consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
        access_token=os.environ['TWITTER_ACCESS_TOKEN'],
        access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'],
    )
    return client.create_tweet(text=tweet_text)
