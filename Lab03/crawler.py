import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = 'X1iKxRO9vW3VBdfdQrBxCKneA'
consumer_secret = 'J73REOsIZoWFnjPC0VZtF3CWRTBrfx0l4v85TvAUC8tBIJ1PwA'
access_token = '191642356-02GI0AIT8ddbmWuDOF6twcMU0sRzyoiyjiX6bvtZ'
access_token_secret = 'QWMtL7jSYMgR1Rk5gQf8pI09cRqchb2jE7MUcFYXuatJD'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# Open/Create a file to append data
csvFile = open('mc.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#MasterChefBR",count=100,
                           lang="pt",
                           since="2018-01-01").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
