import pandas as pd
import tweepy
import json
from datetime import datetime
import s3fs


access_key = ""
access_secret = ""
consumer_key = ""
consumer_secret = ""

#Twitter Authentication
auth = tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(consumer_key,consumer_secret)

#Creating an API Object
api = tweepy.API(auth)


