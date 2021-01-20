import tweepy
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

print("Just a notification")

CONSUMER_KEY = os.getenv("API_KEY")
CONSUMER_SECRET = os.getenv("API_KEY_SECRET")
ACCESS_KEY = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

mentions = api.mentions_timeline()

for mention in mentions:
    print(str(mention.id) + " - " + mention.text)
    if '#remindmein' in mention.text.lower():
        print("Found #remindmein")
        print(mention.user.__dict__['name'])
        print("Responding back...")
