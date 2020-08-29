from decouple import config
from datetime import date
import tweepy
import time

INTERVAL = 60*60*24*7

CONSUMER_KEY = config('CONSUMER_KEY')
CONSUMER_SECRET = config('CONSUMER_SECRET')
ACCESS_KEY = config('ACCESS_KEY')
ACCESS_SECRET = config('ACCESS_SECRET')


def get_message():
    today = date.today()
    year = today.year
    END_DATE = date(year+1, 1, 1)
    START_DATE = date(year, 1, 1)
    weeks_gone = (int)((today - START_DATE).days/7)
    weeks_left = (int)((END_DATE - today).days/7)
    message = "Each square represents a week in this year\n"
    printed_letters = 0
    for i in range(weeks_gone):
        message += '\u25A0'
        printed_letters += 1
        if printed_letters % 10 == 0:
            message += '\n'
    for i in range(weeks_left):
        message += '\u2610'
        printed_letters += 1
        if printed_letters % 10 == 0:
            message += '\n'
    return message


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:

    message = get_message()
    try:
        api.update_status(message)
        print("Posted Message")
    except Exception as e:
        print(e)
    for i in range((int)(INTERVAL/(60))):
        time.sleep(INTERVAL/60/7/24)
        print('Sleeping ...')
