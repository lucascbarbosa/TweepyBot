import os
import tweepy as tw
import pandas as pd
CONSUMER_KEY = "JiSupB6Bv99NgGN57cpE2LqDI"
CONSUMER_SECRET = "XZQmPlALfgpxZQ1cWqKhampSdmxYQAKqkkhGRisLOC6t78hoax"
ACCESS_KEY  = "1076894136312176640-EHlxCHUDfrEKyWBh4jHmEzqBJWGWMs"
ACCESS_SECRET =  "SS9Rct5QNSJHZke0GvtjGXwHKk7TVBaHfufCUMeBNprSi "
auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tw.API(auth)

tweets = tw.Cursor(api.search,
                       q='#bolsonaro',
                       lang="pt-br",
                       since="2019-09-21").items(5)
for status in tw.Cursor(api.user_timeline, screen_name='@CarlosBolsonaro', tweet_mode="extended").items():
    print(status.full_text)