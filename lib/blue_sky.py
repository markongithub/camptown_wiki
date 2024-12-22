from atproto import Client
import os


def sendOneSkeet(skeet_text: str):
    client = Client()
    client.login(os.environ["BLUE_SKY_USERNAME"], os.environ["BLUE_SKY_PASSWORD"])
    return client.send_post(skeet_text)
