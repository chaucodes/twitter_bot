import tweepy
import argparse
import os
from dotenv import load_dotenv
from twitchAPI.twitch import Twitch

load_dotenv()


TWITCH_CLIENT = os.getenv('TWITCH_CLIENT')
TWITCH_SECRET = os.getenv('TWITCH_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

twitch = Twitch(TWITCH_CLIENT, TWITCH_SECRET)

client = tweepy.Client(
  consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
  access_token=ACCESS_TOKEN, access_token_secret=ACCESS_SECRET
)

twitch_url = 'twitch.tv/chau_codes'
twitter_message = "Test text message"

channel_response = twitch.search_channels("chau_codes")
live_status = channel_response.get('data')[0].get('is_live')

if live_status:
  response = client.create_tweet(
    text=f'{twitter_message} \n\n {twitch_url}'
  )
  print(f"https://twitter.com/user/status/{response.data['id']}")
else:
  print("you're not live dummy")
