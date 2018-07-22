import tweepy
import time
import db

consumer_key = 'X1iKxRO9vW3VBdfdQrBxCKneA'
consumer_secret = 'J73REOsIZoWFnjPC0VZtF3CWRTBrfx0l4v85TvAUC8tBIJ1PwA'
token_key = '191642356-02GI0AIT8ddbmWuDOF6twcMU0sRzyoiyjiX6bvtZ'
token_secret = 'QWMtL7jSYMgR1Rk5gQf8pI09cRqchb2jE7MUcFYXuatJD'


def download_tweets(id_file, sentiment):
    with open(id_file) as infile:
        for tweet_id in infile:
            tweet_id = tweet_id.strip()

            if db.exist_tweet(tweet_id):
                print("tweet com id: ", tweet_id, "ja foi capturado")
                continue

            try:
                tweet = api.get_status(tweet_id)
                db.add_tweet(tweet, sentiment)
            except tweepy.error.TweepError:
                print("tweet com id: ", tweet_id, "nao esta disponivel")

            time.sleep(1)


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(token_key, token_secret)
api = tweepy.API(auth)

print("Capturando tweets positivos ...")
download_tweets("positivos.txt", 1)

print("Capturando tweets negativos ...")
download_tweets("negativos.txt", 0)

print("Fim.")
