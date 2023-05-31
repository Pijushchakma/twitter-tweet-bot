import os
import time

import dotenv
import tweepy

import services as _services
import unsplash as _unsplash

dotenv.load_dotenv()


API_KEY = os.environ['TWITTER_API_KEY']
SECRET_KEY = os.environ['TWITTER_API_SECRET_KEY']
ACCESS_TOKEN = os.environ['TWITTER_ACCESS']
ACCESS_TOKEN_SECRET = os.environ['TWITTER_SECRET']


ClIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']


def get_twitter_api():
    auth = tweepy.OAuth1UserHandler(API_KEY,SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
    twitter_api = tweepy.API(auth,wait_on_rate_limit=True)

    return twitter_api


def write_tweet():
    tweet = _services.get_tweet()
    twitter_api = get_twitter_api()
    twitter_api.update_status(tweet)

def post_image():
    _unsplash.download_image()
    twitter_api = get_twitter_api()
    twitter_api.update_status_with_media("picture.jpg")



def run():
    while True:
        write_tweet()
        time.sleep(30)
        post_image()
        time.sleep(30)



if __name__ == "__main__":
    run()        







